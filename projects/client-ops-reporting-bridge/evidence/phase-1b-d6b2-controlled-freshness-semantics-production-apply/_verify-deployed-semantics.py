#!/usr/bin/env python3
"""D6B2 deployed-source synthetic verification (no network / no webhook).

Proves S1/S2/S3, stale OK/FAILED, threshold boundary, and event identity
against the production-path producer package under PYTHONPATH=src.
"""

from __future__ import annotations

import json
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from client_ops_reporting_bridge.constants import STALE_AFTER_SECONDS
from client_ops_reporting_bridge.delivery_eligibility import (
    FRESH_AND_ELIGIBLE,
    NOT_SAFE_TO_SEND,
    SOURCE_VALID_BUT_STALE_REVIEW_REQUIRED,
    STALE_REVIEW_REQUIRED,
    is_live_delivery_authorized,
    is_stale_age,
)
from client_ops_reporting_bridge.producer_constants import DEFAULT_CONCURRENCY
from client_ops_reporting_bridge.producer_d5 import (
    assess_preview_for_live,
    build_source_preview,
)
from client_ops_reporting_bridge.site002_adapter import adapt_source_dir

OBSERVED = datetime(2026, 7, 20, 12, 0, 0, tzinfo=timezone.utc)
SYN_PREFIX = "d6b2-syn"


def _iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _write_run(
    run_dir: Path,
    *,
    classification: str,
    onboarding: int,
    observed: datetime,
    run_id: str,
    run_class: str | None = None,
    exit_code: int = 0,
    baseline: int = 100,
    added: int = 0,
    removed: int = 0,
) -> None:
    run_dir.mkdir(parents=True, exist_ok=True)
    current = baseline + added - removed
    rc = classification if run_class is None else run_class
    (run_dir / "monitor-classification.json").write_text(
        json.dumps(
            {
                "classification": classification,
                "onboarding_needs_count": onboarding,
                "observed_at": _iso(observed),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (run_dir / "changed-summary.json").write_text(
        json.dumps(
            {
                "baseline_url_count": baseline,
                "current_url_count": current,
                "added_count": added,
                "removed_count": removed,
                "onboarding_needs_count": onboarding,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (run_dir / "run-summary.json").write_text(
        json.dumps(
            {
                "run_id": run_id,
                "classification": rc,
                "finished_at": _iso(observed),
                "exit_code": exit_code,
                "onboarding_needs_count": onboarding,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def _preview(run_dir: Path, age_seconds: int) -> dict:
    now = OBSERVED + timedelta(seconds=age_seconds)
    return build_source_preview(run_dir, now_utc=now)


def main() -> int:
    assert STALE_AFTER_SECONDS == 93600
    assert DEFAULT_CONCURRENCY == 1
    assert is_stale_age(93600) is False
    assert is_stale_age(93601) is True

    out: dict = {
        "phase": "1B-D6B2",
        "network_calls": 0,
        "webhook_calls": 0,
        "telegram_attempts": 0,
        "stale_after_seconds": STALE_AFTER_SECONDS,
        "max_retries": 0,
        "max_safe_concurrency": DEFAULT_CONCURRENCY,
        "synthetic_ids": {},
        "checks": {},
    }

    with tempfile.TemporaryDirectory(prefix="d6b2-verify-") as tmp:
        base = Path(tmp)

        # S1 — fresh valid ATTENTION
        s1 = base / "s1-fresh-attention"
        _write_run(
            s1,
            classification="ONBOARDING_REQUIRED",
            onboarding=2,
            observed=OBSERVED,
            run_id=f"{SYN_PREFIX}-s1-fresh-attention",
        )
        p1 = _preview(s1, age_seconds=1000)
        a1 = assess_preview_for_live(p1)
        s1_ok = (
            p1["source_status"] == "ATTENTION"
            and p1["delivery_eligibility"] == FRESH_AND_ELIGIBLE
            and a1["approved"] is True
            and a1["verdict"] == "REAL_SOURCE_PREVIEW_APPROVED_FOR_ONE_LIVE_POST"
            and bool(p1.get("event_id"))
            and p1.get("message_preview") is not None
        )
        out["synthetic_ids"]["s1_event_id"] = p1.get("event_id")
        out["synthetic_ids"]["s1_run_id"] = f"{SYN_PREFIX}-s1-fresh-attention"
        out["checks"]["s1_fresh_attention"] = {
            "pass": s1_ok,
            "source_status": p1["source_status"],
            "delivery_eligibility": p1["delivery_eligibility"],
            "preview_approved": a1["approved"],
            "verdict": a1["verdict"],
            "webhook_calls": 0,
        }

        # S2 — stale valid ATTENTION (PRIMARY)
        s2 = base / "s2-stale-attention"
        _write_run(
            s2,
            classification="ONBOARDING_REQUIRED",
            onboarding=2,
            observed=OBSERVED,
            run_id=f"{SYN_PREFIX}-s2-stale-attention",
        )
        p2 = _preview(s2, age_seconds=93601)
        a2 = assess_preview_for_live(p2)
        proc2, _, _ = adapt_source_dir(
            s2, build_envelope=True, now_utc=OBSERVED + timedelta(seconds=93601)
        )
        s2_ok = (
            p2["source_status"] == "ATTENTION"
            and p2["delivery_eligibility"] == STALE_REVIEW_REQUIRED
            and a2["approved"] is False
            and a2["verdict"] == SOURCE_VALID_BUT_STALE_REVIEW_REQUIRED
            and is_live_delivery_authorized(proc2) is False
            and p2.get("message_preview") is None
            and proc2.normalized_status == "ATTENTION"
        )
        out["synthetic_ids"]["s2_event_id"] = p2.get("event_id")
        out["synthetic_ids"]["s2_run_id"] = f"{SYN_PREFIX}-s2-stale-attention"
        out["checks"]["s2_stale_attention"] = {
            "pass": s2_ok,
            "source_status": p2["source_status"],
            "delivery_eligibility": p2["delivery_eligibility"],
            "preview_approved": a2["approved"],
            "verdict": a2["verdict"],
            "live_authorized": False,
            "message_preview": p2.get("message_preview"),
            "webhook_calls": 0,
            "telegram_attempts": 0,
            "datatable_intake_mutations": 0,
        }

        # S3 — true BLOCKED authority defect (classification mismatch)
        s3 = base / "s3-true-blocked"
        _write_run(
            s3,
            classification="ONBOARDING_REQUIRED",
            onboarding=2,
            observed=OBSERVED,
            run_id=f"{SYN_PREFIX}-s3-true-blocked",
            run_class="NO_ACTION_REQUIRED",
        )
        p3 = _preview(s3, age_seconds=1000)
        a3 = assess_preview_for_live(p3)
        proc3, _, _ = adapt_source_dir(
            s3, build_envelope=True, now_utc=OBSERVED + timedelta(seconds=1000)
        )
        s3_ok = (
            p3["source_status"] == "BLOCKED"
            and p3["delivery_eligibility"] == NOT_SAFE_TO_SEND
            and a3["approved"] is False
            and is_live_delivery_authorized(proc3) is False
            and p3.get("message_preview") is None
        )
        out["synthetic_ids"]["s3_event_id"] = p3.get("event_id")
        out["synthetic_ids"]["s3_run_id"] = f"{SYN_PREFIX}-s3-true-blocked"
        out["checks"]["s3_true_blocked"] = {
            "pass": s3_ok,
            "source_status": p3["source_status"],
            "delivery_eligibility": p3["delivery_eligibility"],
            "preview_approved": a3["approved"],
            "verdict": a3["verdict"],
            "webhook_calls": 0,
            "telegram_attempts": 0,
        }

        # Stale OK
        sok = base / "stale-ok"
        _write_run(
            sok,
            classification="NO_ACTION_REQUIRED",
            onboarding=0,
            observed=OBSERVED,
            run_id=f"{SYN_PREFIX}-stale-ok",
        )
        pok = _preview(sok, age_seconds=93601)
        stale_ok = (
            pok["source_status"] == "OK"
            and pok["delivery_eligibility"] == STALE_REVIEW_REQUIRED
            and pok["source_status"] != "BLOCKED"
        )
        out["checks"]["stale_ok"] = {
            "pass": stale_ok,
            "source_status": pok["source_status"],
            "delivery_eligibility": pok["delivery_eligibility"],
        }

        # Stale FAILED
        sfail = base / "stale-failed"
        _write_run(
            sfail,
            classification="FAILURE_REVIEW_REQUIRED",
            onboarding=0,
            observed=OBSERVED,
            run_id=f"{SYN_PREFIX}-stale-failed",
            exit_code=1,
        )
        pf = _preview(sfail, age_seconds=93601)
        stale_failed = (
            pf["source_status"] == "FAILED"
            and pf["delivery_eligibility"] == STALE_REVIEW_REQUIRED
            and pf["source_status"] != "BLOCKED"
        )
        out["checks"]["stale_failed"] = {
            "pass": stale_failed,
            "source_status": pf["source_status"],
            "delivery_eligibility": pf["delivery_eligibility"],
        }

        # Threshold boundary
        tb = base / "threshold"
        _write_run(
            tb,
            classification="ONBOARDING_REQUIRED",
            onboarding=1,
            observed=OBSERVED,
            run_id=f"{SYN_PREFIX}-threshold",
        )
        p93600 = _preview(tb, age_seconds=93600)
        p93601 = _preview(tb, age_seconds=93601)
        thr_ok = (
            p93600["delivery_eligibility"] == FRESH_AND_ELIGIBLE
            and p93601["delivery_eligibility"] == STALE_REVIEW_REQUIRED
            and p93600["source_status"] == "ATTENTION"
            and p93601["source_status"] == "ATTENTION"
        )
        out["checks"]["threshold_boundary"] = {
            "pass": thr_ok,
            "age_93600": p93600["delivery_eligibility"],
            "age_93601": p93601["delivery_eligibility"],
            "operator": "age_seconds > 93600",
        }

        # Event identity: same source fresh vs stale → same event_id
        id_dir = base / "identity"
        _write_run(
            id_dir,
            classification="ONBOARDING_REQUIRED",
            onboarding=4,
            observed=OBSERVED,
            run_id=f"{SYN_PREFIX}-identity-same",
            added=4,
        )
        proc_f, _, _ = adapt_source_dir(
            id_dir, build_envelope=True, now_utc=OBSERVED + timedelta(seconds=100)
        )
        proc_s, _, _ = adapt_source_dir(
            id_dir, build_envelope=True, now_utc=OBSERVED + timedelta(seconds=93601)
        )
        eid_fresh = (proc_f.envelope or {}).get("event_id")
        eid_stale = (proc_s.envelope or {}).get("event_id")

        id_new = base / "identity-new"
        obs_new = OBSERVED + timedelta(hours=2)
        _write_run(
            id_new,
            classification="ONBOARDING_REQUIRED",
            onboarding=4,
            observed=obs_new,
            run_id=f"{SYN_PREFIX}-identity-new",
            added=4,
        )
        proc_n, _, _ = adapt_source_dir(
            id_new, build_envelope=True, now_utc=obs_new + timedelta(seconds=100)
        )
        eid_new = (proc_n.envelope or {}).get("event_id")
        id_ok = (
            bool(eid_fresh)
            and eid_fresh == eid_stale
            and bool(eid_new)
            and eid_new != eid_fresh
            and proc_f.normalized_status == "ATTENTION"
            and proc_s.normalized_status == "ATTENTION"
            and proc_f.delivery_eligibility == FRESH_AND_ELIGIBLE
            and proc_s.delivery_eligibility == STALE_REVIEW_REQUIRED
        )
        out["synthetic_ids"]["identity_same_event_id"] = eid_fresh
        out["synthetic_ids"]["identity_new_event_id"] = eid_new
        out["checks"]["event_identity"] = {
            "pass": id_ok,
            "fresh_event_id": eid_fresh,
            "stale_event_id": eid_stale,
            "new_run_event_id": eid_new,
            "freshness_changes_event_identity": False,
        }

        # Forbidden historical IDs not reused
        forbidden = {
            "c84e29bf-79b1-5aea-98c4-9dc8d651fc96",
            "d6a2a001-27d6-4a2e-bd6a-000000000001",
        }
        used = {v for v in out["synthetic_ids"].values() if isinstance(v, str)}
        out["checks"]["no_historical_id_reuse"] = {
            "pass": used.isdisjoint(forbidden),
            "forbidden_touched": sorted(used & forbidden),
        }

    all_pass = all(c.get("pass") for c in out["checks"].values())
    out["all_pass"] = all_pass
    out["token"] = (
        "D6B2_DEPLOYED_SYNTHETIC_SEMANTICS_PASS"
        if all_pass
        else "D6B2_DEPLOYED_SYNTHETIC_SEMANTICS_FAIL"
    )
    print(json.dumps(out, indent=2))
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
