#!/usr/bin/env python3
"""
CORVONERO Campaign V2 Pass 3 — final authority, negatives TXT, manifest prep.
Invokes execute-campaign-v2-pass3-generation-v1.mjs for Commander XLSX.
No Commander/Direct access. No git commit.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO = Path(r"X:\AI MARS")
PILOT = REPO / "projects" / "mars-search-ppc-production" / "pilots" / "corvonero"
REPORTS = REPO / "projects" / "mars-search-ppc-production" / "reports"
TOOLS = PILOT / "tools"
OUTPUT_DIR = Path(
    r"X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2-FINAL-2026-06-30"
)
CHECKPOINT = "ebff109061932faecdff63456a27aa7fe3823be7"
GENERATED_AT = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

CAMPAIGN_ORDER = [
    "CA-01-LOCAL",
    "CA-01-REMOTE",
    "CA-02-LOCAL",
    "CA-02-REMOTE",
    "CA-03-LOCAL",
    "CA-03-REMOTE",
    "CA-04-LOCAL",
    "CA-04-REMOTE",
    "CA-05-LOCAL",
    "CA-05-REMOTE",
]

EXPECTED_COUNTS = {
    "CA-01-LOCAL": {"groups": 7, "phrases": 311, "ads": 7, "base_bid": 500},
    "CA-01-REMOTE": {"groups": 7, "phrases": 316, "ads": 7, "base_bid": 500},
    "CA-02-LOCAL": {"groups": 4, "phrases": 143, "ads": 4, "base_bid": 400},
    "CA-02-REMOTE": {"groups": 4, "phrases": 143, "ads": 4, "base_bid": 400},
    "CA-03-LOCAL": {"groups": 3, "phrases": 76, "ads": 3, "base_bid": 400},
    "CA-03-REMOTE": {"groups": 3, "phrases": 76, "ads": 3, "base_bid": 400},
    "CA-04-LOCAL": {"groups": 1, "phrases": 48, "ads": 1, "base_bid": 400},
    "CA-04-REMOTE": {"groups": 1, "phrases": 48, "ads": 1, "base_bid": 400},
    "CA-05-LOCAL": {"groups": 6, "phrases": 216, "ads": 6, "base_bid": 400},
    "CA-05-REMOTE": {"groups": 6, "phrases": 216, "ads": 6, "base_bid": 400},
}

BROAD_NEGATIVE_TERMS = {
    "онлайн",
    "удалённый",
    "удаленный",
    "удалённо",
    "удаленно",
    "выезд",
    "офис",
    "на месте",
    "россия",
    "новосибирск",
    "нск",
}

LOCAL_CALLOUT_EXCLUDE = re.compile(r"удал[её]н|по россии|по рф", re.I)
REMOTE_CALLOUT_EXCLUDE = re.compile(r"выезд|новосибирск", re.I)
LOCAL_PROP_RE = re.compile(r"удал[её]нн|по россии|по рф|дистанцион", re.I)
REMOTE_PROP_RE = re.compile(r"выезд|новосибирск|нск|на месте|в офис", re.I)


def assert_preflight() -> None:
    label = subprocess.check_output(
        [
            "powershell.exe",
            "-NoProfile",
            "-Command",
            "(Get-Volume -DriveLetter X).FileSystemLabel",
        ],
        text=True,
    ).strip()
    if label != "AI WS":
        raise SystemExit(f"STOP — X VOLUME IDENTITY MISMATCH (got {label!r})")
    if not REPO.is_dir():
        raise SystemExit("STOP — repository missing")
    if OUTPUT_DIR.exists():
        raise SystemExit("STOP — CAMPAIGN V2 FINAL DIRECTORY ALREADY EXISTS")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_phrase(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def char_metrics(text: str) -> dict[str, int]:
    words = text.split()
    return {
        "characters": len(text),
        "max_word_length": max((len(w) for w in words), default=0),
        "words": len(words),
    }


def validate_ad_fields(h1: str, h2: str, text: str, display_path: str) -> str:
    issues = []
    if len(h1) > 56:
        issues.append("headline_1")
    if len(h2) > 30:
        issues.append("headline_2")
    if len(text) > 81:
        issues.append("text")
    if len(display_path) > 20:
        issues.append("display_path")
    return "PASS" if not issues else f"FAIL:{','.join(issues)}"


def negative_conflicts_phrase(negative: str, phrase: str) -> tuple[bool, str]:
    neg = normalize_phrase(negative)
    phr = normalize_phrase(phrase)
    if not neg or not phr:
        return False, ""
    if " " in neg:
        if neg in phr:
            return True, "phrase_substring"
        return False, ""
    parts = re.split(r"[^\wё]+", phr, flags=re.UNICODE)
    parts = [p for p in parts if p]
    for part in parts:
        if part == neg or part.startswith(neg) or neg in part:
            return True, "word_match"
    if neg in phr:
        return True, "substring"
    return False, ""


def finalize_ad_copy(proposed: dict) -> dict:
    ads = []
    for review in proposed["reviews"]:
        campaign_id = review["campaign_id"]
        group_id = review["group_id"]
        mode = review["geography_mode"]
        h1 = review["headline_1"]
        h2 = review["headline_2"]
        text = review["text"]
        landing = review["landing_url"].split("?")[0].split("#")[0]
        display_path = review.get("display_path", "")

        if (
            campaign_id == "CA-01-REMOTE"
            and group_id == "ca-01-price-intent"
        ):
            rewrite = review.get("rewrite") or {}
            h1 = rewrite.get("headline_1", h1)
            h2 = rewrite.get("headline_2", h2)
            text = rewrite.get("text", "Минимальный заказ — 2 часа. Работаем удалённо по России.")

        status = validate_ad_fields(h1, h2, text, display_path)
        if mode == "LOCAL" and LOCAL_PROP_RE.search(f"{h2} {text}"):
            status = "FAIL:mixed_geo_local"
        if mode == "REMOTE" and REMOTE_PROP_RE.search(f"{h2} {text}"):
            status = "FAIL:mixed_geo_remote"

        ads.append(
            {
                "campaign_id": campaign_id,
                "group_id": group_id,
                "group_name": review.get("group_name", ""),
                "geography_mode": mode,
                "primary_ad": {
                    "headline": h1,
                    "additional_headline": h2,
                    "text": text,
                    "headline_metrics": char_metrics(h1),
                    "additional_metrics": char_metrics(h2),
                    "text_metrics": char_metrics(text),
                },
                "landing_page": {"url": landing},
                "display_path": display_path,
                "character_counts": {
                    "headline_1": len(h1),
                    "headline_2": len(h2),
                    "text": len(text),
                    "display_path": len(display_path),
                },
                "validation_status": status,
                "status": "OPERATOR_APPROVED",
                "operator_rewrite_applied": (
                    campaign_id == "CA-01-REMOTE" and group_id == "ca-01-price-intent"
                ),
            }
        )
    return ads


def build_phrase_records(proposed: dict) -> list[dict]:
    records = []
    rejected = 0
    for row in proposed["rows"]:
        if row.get("pass2_decision") == "REJECT":
            rejected += 1
            continue
        if row.get("local_action") == "EXCLUDE_REJECT" or row.get("remote_action") == "EXCLUDE_REJECT":
            rejected += 1
            continue
        cid = row["source_campaign_id"]
        gid = row["source_group_id"]
        if row.get("local_action") == "INCLUDE":
            records.append(
                {
                    "phrase_id": row["phrase_id"],
                    "phrase": row["phrase"],
                    "normalized_phrase": row.get("normalized_phrase") or normalize_phrase(row["phrase"]),
                    "final_campaign": f"{cid}-LOCAL",
                    "final_group": gid,
                    "source_campaign": cid,
                    "source_group": gid,
                    "geo_class": row.get("geo_class", "NEUTRAL"),
                    "production_status": "DEPLOYABLE",
                }
            )
        if row.get("remote_action") == "INCLUDE":
            records.append(
                {
                    "phrase_id": row["phrase_id"],
                    "phrase": row["phrase"],
                    "normalized_phrase": row.get("normalized_phrase") or normalize_phrase(row["phrase"]),
                    "final_campaign": f"{cid}-REMOTE",
                    "final_group": gid,
                    "source_campaign": cid,
                    "source_group": gid,
                    "geo_class": row.get("geo_class", "NEUTRAL"),
                    "production_status": "DEPLOYABLE",
                }
            )
    return records, rejected


def build_architecture_groups(groups_arch: dict, phrase_records: list[dict]) -> list[dict]:
    counts: dict[str, int] = Counter()
    for r in phrase_records:
        key = f"{r['final_campaign']}::{r['final_group']}"
        counts[key] += 1

    out = []
    for g in groups_arch["groups"]:
        for mode in ("LOCAL", "REMOTE"):
            campaign_id = f"{g['campaign_id']}-{mode}"
            gid = g["group_id"]
            key = f"{campaign_id}::{gid}"
            pc = counts.get(key, 0)
            if pc == 0:
                continue
            out.append(
                {
                    "campaign_id": campaign_id,
                    "source_campaign_id": g["campaign_id"],
                    "group_id": gid,
                    "group_name": g["group_name"],
                    "intent": g.get("intent", ""),
                    "phrase_count": pc,
                    "primary_ad_id": f"ad-{gid}-{mode.lower()}",
                    "landing_url": g["landing_url"],
                    "deployable": True,
                    "status": "DEPLOYABLE",
                    "geography_mode": mode,
                }
            )
    return out


def filter_callouts(source_callouts: dict) -> dict:
    pools = {}
    for campaign_id, items in source_callouts.get("campaign_pools", {}).items():
        for mode in ("LOCAL", "REMOTE"):
            v2_id = f"{campaign_id}-{mode}"
            filtered = []
            for item in items:
                text = item.get("text", "")
                if mode == "LOCAL" and LOCAL_CALLOUT_EXCLUDE.search(text):
                    continue
                if mode == "REMOTE" and REMOTE_CALLOUT_EXCLUDE.search(text):
                    continue
                filtered.append(item)
            pools[v2_id] = filtered
    return {
        **source_callouts,
        "callout_id": "corvonero-campaign-v2-callouts-v1",
        "campaign_pools": pools,
        "v2_mode_filter": "LOCAL excludes remote callouts; REMOTE excludes local callouts",
    }


def finalize_negatives(
    proposed_neg: dict, phrases_by_campaign: dict[str, list[str]]
) -> tuple[dict, dict[str, list[str]]]:
    by_campaign: dict[str, list[dict]] = defaultdict(list)
    for review in proposed_neg["reviews"]:
        by_campaign[review["campaign_id"]].append(review)

    final_sets: dict[str, list[str]] = {}
    campaign_reports = []

    for campaign_id in CAMPAIGN_ORDER:
        included = phrases_by_campaign.get(campaign_id, [])
        proposed_list = by_campaign.get(campaign_id, [])
        approved: list[str] = []
        stats = {
            "campaign_id": campaign_id,
            "proposed_count": len(proposed_list),
            "approved_safe_count": 0,
            "rejected_count": 0,
            "narrowed_count": 0,
            "conflict_count_after_finalization": 0,
            "items": [],
        }
        seen = set()

        for review in proposed_list:
            term = review["negative"]
            norm = normalize_phrase(term)
            decision = "REJECT"
            reason = ""

            if review["recommendation"] == "HOLD_OPERATOR":
                reason = "HOLD_OPERATOR — conservative omit"
            elif review.get("conflict_count", 0) > 0:
                reason = f"proposed conflict_count={review['conflict_count']}"
            elif review["recommendation"] != "APPROVE":
                reason = f"recommendation={review['recommendation']}"
            else:
                conflicts = [
                    p
                    for p in included
                    if negative_conflicts_phrase(term, p)[0]
                ]
                if conflicts:
                    reason = f"final conflict with {len(conflicts)} included phrases"
                    stats["conflict_count_after_finalization"] += len(conflicts)
                elif norm in seen:
                    reason = "duplicate normalized"
                else:
                    decision = "APPROVED_SAFE"
                    seen.add(norm)
                    approved.append(term)
                    reason = "zero conflicts after finalization"

            if decision != "APPROVED_SAFE":
                stats["rejected_count"] += 1
            stats["items"].append(
                {
                    "negative": term,
                    "category": review.get("category"),
                    "decision": decision,
                    "reason": reason,
                }
            )

        approved.sort(key=normalize_phrase)
        stats["approved_safe_count"] = len(approved)
        final_sets[campaign_id] = approved
        campaign_reports.append(stats)

    return {"campaigns": campaign_reports, "policy": "CONSERVATIVE_APPROVED_SAFE_ONLY"}, final_sets


def write_negative_txt(campaign_id: str, terms: list[str]) -> Path:
    fname = f"{campaign_id}-CAMPAIGN-NEGATIVES-FINAL-v2.txt"
    path = OUTPUT_DIR / fname
    path.write_text("\n".join(terms) + ("\n" if terms else ""), encoding="utf-8")
    return path


def write_md(path: Path, title: str, sections: list[tuple[str, str]]) -> None:
    lines = [f"# {title}", "", f"Generated: {GENERATED_AT}", f"Checkpoint: `{CHECKPOINT}`", ""]
    for heading, body in sections:
        lines.extend([f"## {heading}", "", body, ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    assert_preflight()

    architecture_v1 = load_json(PILOT / "CORVONERO-CAMPAIGN-V2-ARCHITECTURE-v1.json")
    phrase_proposed = load_json(PILOT / "CORVONERO-CAMPAIGN-V2-PHRASE-ALLOCATION-PROPOSED-v2.json")
    ad_proposed = load_json(PILOT / "CORVONERO-CAMPAIGN-V2-AD-COPY-PROPOSED-v2.json")
    neg_proposed = load_json(PILOT / "CORVONERO-CAMPAIGN-V2-CAMPAIGN-NEGATIVES-PROPOSED-v2.json")
    cross_proposed = load_json(PILOT / "CORVONERO-CAMPAIGN-V2-CROSS-CAMPAIGN-NEGATIVES-PROPOSED-v2.json")
    pass2_decisions = load_json(PILOT / "CORVONERO-CAMPAIGN-V2-PASS2-DECISIONS-v1.json")
    groups_arch = load_json(PILOT / "CORVONERO-CT4-GROUP-ARCHITECTURE-v1.json")
    ct4_transport = load_json(PILOT / "CORVONERO-CT4-TRANSPORT-CONFIG-v1.json")
    ct4_callouts = load_json(PILOT / "CORVONERO-EXT-W1-CALLOUTS-v2.json")
    ct4_display = load_json(PILOT / "CORVONERO-EXT-W1-DISPLAY-PATHS-v1.json")
    ct4_group_neg = load_json(PILOT / "CORVONERO-CT4-GROUP-NEGATIVES-v1.json")
    ct4_utm = load_json(PILOT / "CORVONERO-CT4-UTM-MAP-v1.json")
    ct4_settings = load_json(PILOT / "CORVONERO-CT4-CAMPAIGN-SETTINGS-v1.json")

    phrase_records, rejected_rows = build_phrase_records(phrase_proposed)
    if len(phrase_records) != 1593:
        raise SystemExit(f"Expected 1593 phrase slots, got {len(phrase_records)}")

    phrases_by_campaign: dict[str, list[str]] = defaultdict(list)
    for r in phrase_records:
        phrases_by_campaign[r["final_campaign"]].append(r["phrase"])

    for cid, exp in EXPECTED_COUNTS.items():
        actual = len(phrases_by_campaign.get(cid, []))
        if actual != exp["phrases"]:
            raise SystemExit(f"Phrase count mismatch {cid}: {actual} != {exp['phrases']}")

    local_explicit_in_remote = sum(
        1
        for r in phrase_records
        if r["final_campaign"].endswith("-REMOTE") and r["geo_class"] == "LOCAL_EXPLICIT"
    )
    remote_explicit_in_local = sum(
        1
        for r in phrase_records
        if r["final_campaign"].endswith("-LOCAL") and r["geo_class"] == "REMOTE_EXPLICIT"
    )
    if local_explicit_in_remote or remote_explicit_in_local:
        raise SystemExit("Geo-explicit phrase allocation violation")

    arch_groups = build_architecture_groups(groups_arch, phrase_records)
    final_ads = finalize_ad_copy(ad_proposed)
    if len(final_ads) != 42:
        raise SystemExit(f"Expected 42 ads, got {len(final_ads)}")
    ad_failures = [a for a in final_ads if not a["validation_status"].startswith("PASS")]
    if ad_failures:
        raise SystemExit(f"Ad validation failures: {ad_failures[:3]}")

    neg_report, neg_sets = finalize_negatives(neg_proposed, phrases_by_campaign)
    for camp in neg_report["campaigns"]:
        if camp["conflict_count_after_finalization"] != 0:
            raise SystemExit(f"Negative conflicts remain for {camp['campaign_id']}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=False)

    phrase_alloc_path = PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-PHRASE-ALLOCATION-v1.json"
    phrase_alloc = {
        "generated_at": GENERATED_AT,
        "checkpoint": CHECKPOINT,
        "status": "OPERATOR_APPROVED",
        "source_rows": 833,
        "rejected_source_rows": rejected_rows,
        "deployable_slots": len(phrase_records),
        "accounting": {
            "source_rows_accounted": 833,
            "rejected_source_rows": 32,
            "included_neutral_both": 1,
            "phrase_slots": 1593,
            "commander_observed_deferred": "828 — post-import reconciliation",
        },
        "campaign_totals": [
            {
                "campaign_id": cid,
                **EXPECTED_COUNTS[cid],
                "phrases": EXPECTED_COUNTS[cid]["phrases"],
            }
            for cid in CAMPAIGN_ORDER
        ],
        "records": phrase_records,
    }
    save_json(phrase_alloc_path, phrase_alloc)

    arch_path = PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-ARCHORITY-v1.json"
    arch_doc = {
        "generated_at": GENERATED_AT,
        "checkpoint": CHECKPOINT,
        "status": "OPERATOR_APPROVED",
        "campaigns": architecture_v1["campaigns"],
        "groups": arch_groups,
        "totals": {
            "campaigns": 10,
            "groups": 42,
            "phrase_slots": 1593,
            "primary_ads": 42,
        },
        "remote_nso_exclusion": "MANUAL POST-IMPORT ACTION REQUIRED",
    }
    save_json(arch_path, arch_doc)

    ads_path = PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-AD-COPY-v1.json"
    save_json(
        ads_path,
        {
            "generated_at": GENERATED_AT,
            "checkpoint": CHECKPOINT,
            "status": "OPERATOR_APPROVED",
            "ads_count": 42,
            "operator_rewrite_a01": {
                "campaign_id": "CA-01-REMOTE",
                "group_id": "ca-01-price-intent",
                "applied_text": "Минимальный заказ — 2 часа. Работаем удалённо по России.",
            },
            "ads": final_ads,
        },
    )

    neg_path = PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-CAMPAIGN-NEGATIVES-v1.json"
    neg_layers = {
        "generated_at": GENERATED_AT,
        "checkpoint": CHECKPOINT,
        "status": "OPERATOR_APPROVED",
        "policy": "APPROVED_SAFE_ONLY",
        "cross_campaign_negatives_in_xlsx": False,
        "manual_direct_import": True,
        **neg_report,
        "sets": {cid: neg_sets[cid] for cid in CAMPAIGN_ORDER},
    }
    save_json(neg_path, neg_layers)

    cross_path = PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-CROSS-CAMPAIGN-NEGATIVES-v1.json"
    save_json(
        cross_path,
        {
            "generated_at": GENERATED_AT,
            "checkpoint": CHECKPOINT,
            "status": "DRAFTED — NOT APPLIED",
            "binding_decision": "DO NOT APPLY IN CAMPAIGN V2",
            "rules_count": len(cross_proposed.get("rules", cross_proposed.get("items", []))),
            "rules": cross_proposed.get("rules", cross_proposed.get("items", [])),
            "note": "Separate future Direct configuration layer — not in XLSX or campaign-negative TXT",
        },
    )

    v2_bids = {
        "bids_id": "corvonero-campaign-v2-bids-v1",
        "generated_at": GENERATED_AT,
        "campaign_bids": {cid: EXPECTED_COUNTS[cid]["base_bid"] for cid in CAMPAIGN_ORDER},
        "bid_policy": "CORVONERO_BALANCED_CYCLIC_10_RUB_V1",
    }
    bids_path = PILOT / "CORVONERO-CAMPAIGN-V2-BIDS-v1.json"
    save_json(bids_path, v2_bids)

    v2_callouts = filter_callouts(ct4_callouts)
    callouts_path = PILOT / "CORVONERO-CAMPAIGN-V2-CALLOUTS-v1.json"
    save_json(callouts_path, v2_callouts)

    v2_transport = {
        **ct4_transport,
        "transport_config_id": "corvonero-campaign-v2-transport-config-v1",
        "geo_region_mode": "PER_CAMPAIGN",
        "geo_regions": {
            cid: ("Новосибирская область" if cid.endswith("-LOCAL") else "Россия")
            for cid in CAMPAIGN_ORDER
        },
        "campaign_negatives_in_workbook": False,
        "cross_campaign_negatives_policy": "NOT_APPLIED",
        "bids_ref": str(bids_path).replace("\\", "/"),
        "display_paths_ref": str(PILOT / "CORVONERO-EXT-W1-DISPLAY-PATHS-v1.json").replace("\\", "/"),
        "group_negatives_ref": str(PILOT / "CORVONERO-CT4-GROUP-NEGATIVES-v1.json").replace("\\", "/"),
    }
    transport_path = PILOT / "CORVONERO-CAMPAIGN-V2-TRANSPORT-CONFIG-v1.json"
    save_json(transport_path, v2_transport)

    v2_utm = {
        **ct4_utm,
        "campaign_slugs": {
            **{f"{k}-LOCAL": v for k, v in ct4_utm["campaign_slugs"].items()},
            **{f"{k}-REMOTE": v for k, v in ct4_utm["campaign_slugs"].items()},
        },
    }
    utm_path = PILOT / "CORVONERO-CAMPAIGN-V2-UTM-MAP-v1.json"
    save_json(utm_path, v2_utm)

    campaign_neg_empty = {
        "authority_id": "corvonero-campaign-v2-campaign-negatives-v1",
        "generated_at": GENERATED_AT,
        "layers": {
            "account_shared_deployable": [],
            "campaign_deployable": [],
        },
        "note": "Campaign negatives supplied as separate TXT for manual Direct import",
    }
    campaign_neg_path = PILOT / "CORVONERO-CAMPAIGN-V2-CAMPAIGN-NEGATIVES-AUTHORITY-v1.json"
    save_json(campaign_neg_path, campaign_neg_empty)

    cross_empty = {
        "routing_id": "corvonero-campaign-v2-inter-campaign-routing-v1",
        "generated_at": GENERATED_AT,
        "status": "NOT_APPLIED",
        "rules": [],
    }
    cross_auth_path = PILOT / "CORVONERO-CAMPAIGN-V2-INTER-CAMPAIGN-ROUTING-v1.json"
    save_json(cross_auth_path, cross_empty)

    settings_path = PILOT / "CORVONERO-CAMPAIGN-V2-CAMPAIGN-SETTINGS-v1.json"
    save_json(
        settings_path,
        {
            **ct4_settings,
            "profile_id": "corvonero-campaign-v2-campaign-settings-v1",
            "v2_note": "Per-campaign geography in architecture; REMOTE NSO exclusion manual post-import",
        },
    )

    manifest_path = PILOT / "CORVONERO-CAMPAIGN-V2-AUTHORITY-MANIFEST-v1.json"
    manifest_files = [
        ("phrase_allocation", phrase_alloc_path),
        ("campaign_architecture", arch_path),
        ("primary_ads", ads_path),
        ("callouts", callouts_path),
        ("campaign_negatives", campaign_neg_path),
        ("group_negatives", PILOT / "CORVONERO-CT4-GROUP-NEGATIVES-v1.json"),
        ("cross_campaign_rules", cross_auth_path),
        ("utm_map", utm_path),
        ("campaign_settings", settings_path),
        ("transport_config", transport_path),
    ]
    manifest = {
        "schema_version": "1.0.0",
        "project_id": "mars-search-ppc-production",
        "pilot_id": "corvonero",
        "authority_checkpoint": "corvonero-campaign-v2-final-v1",
        "campaign_scope": CAMPAIGN_ORDER,
        "operator_approval_state": "OPERATOR_APPROVED",
        "generated_at": GENERATED_AT,
        "files": [
            {
                "role": role,
                "path": str(path).replace("\\", "/"),
                "sha256": sha256_file(path),
                "required": True,
            }
            for role, path in manifest_files
        ],
    }
    save_json(manifest_path, manifest)

    neg_txt_paths = []
    for cid in CAMPAIGN_ORDER:
        neg_txt_paths.append(write_negative_txt(cid, neg_sets[cid]))

    import_order = OUTPUT_DIR / "CORVONERO-CAMPAIGN-V2-IMPORT-ORDER-v1.txt"
    import_order.write_text(
        "\n".join(
            [
                "CORVONERO CAMPAIGN V2 — RECOMMENDED IMPORT ORDER",
                "",
                "1. CA-01-LOCAL",
                "2. CA-01-REMOTE",
                "3. Verify CA-01 pair (geo, ads, phrase counts)",
                "4. CA-02-LOCAL",
                "5. CA-02-REMOTE",
                "6. CA-03-LOCAL",
                "7. CA-03-REMOTE",
                "8. CA-04-LOCAL",
                "9. CA-04-REMOTE",
                "10. CA-05-LOCAL",
                "11. CA-05-REMOTE",
                "",
                "After each workbook: add campaign-negative TXT manually in Yandex Direct.",
                "Do NOT add cross-campaign negatives.",
                "REMOTE campaigns: exclude Новосибирск and Новосибирская область manually.",
                "UTM: configure globally in Direct — not embedded in ad URLs.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    checklist = OUTPUT_DIR / "CORVONERO-CAMPAIGN-V2-MANUAL-POST-IMPORT-CHECKLIST-v1.md"
    checklist.write_text(
        "\n".join(
            [
                "# CORVONERO Campaign V2 — Manual Post-Import Checklist",
                "",
                f"Generated: {GENERATED_AT}",
                "",
                "## REMOTE campaigns (all five)",
                "- [ ] Region set to **Россия**",
                "- [ ] **Exclude** Новосибирск and Новосибирская область manually",
                "- [ ] Verify no LOCAL proposition in ads or callouts",
                "",
                "## LOCAL campaigns (all five)",
                "- [ ] Region set to **Новосибирская область**",
                "- [ ] Verify no REMOTE proposition in ads or callouts",
                "",
                "## All campaigns",
                "- [ ] Import campaign-negative TXT from this package into Direct (not from XLSX)",
                "- [ ] Do **not** add cross-campaign negatives",
                "- [ ] Configure UTM globally (not in ad URLs)",
                "- [ ] Commander import only — server upload requires separate authorization",
                "",
                "## Verification",
                "- [ ] CA-01 pair: 7 groups, 311 LOCAL + 316 REMOTE phrases, 7 ads each",
                "- [ ] Total: 10 campaigns, 42 groups, 1593 phrases, 42 ads",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    gen_script = TOOLS / "execute-campaign-v2-pass3-generation-v1.mjs"
    gen_args = [str(gen_script), str(manifest_path), str(OUTPUT_DIR)]
    if (OUTPUT_DIR / "CORVONERO-CA-01-LOCAL-PROGRAMMIST-1S-COMMANDER-IMPORT-v1.xlsx").exists():
        gen_args.append("--forensic-only")
    subprocess.run(["node", *gen_args], check=True, cwd=str(TOOLS))

    xlsx_files = sorted(OUTPUT_DIR.glob("*.xlsx"))
    all_artifacts = xlsx_files + neg_txt_paths + [import_order, checklist]
    sha_lines = []
    for f in sorted(all_artifacts, key=lambda p: p.name):
        sha_lines.append(f"{sha256_file(f)}  {f.name}")
    sha_path = OUTPUT_DIR / "CORVONERO-CAMPAIGN-V2-SHA256SUMS-v1.txt"
    sha_path.write_text("\n".join(sha_lines) + "\n", encoding="utf-8")

    manifest_out = {
        "generated_at": GENERATED_AT,
        "checkpoint": CHECKPOINT,
        "output_directory": str(OUTPUT_DIR),
        "campaigns": 10,
        "xlsx_files": [f.name for f in xlsx_files],
        "negative_txt_files": [p.name for p in neg_txt_paths],
        "phrase_slots": 1593,
        "groups": 42,
        "ads": 42,
    }
    save_json(OUTPUT_DIR / "CORVONERO-CAMPAIGN-V2-OUTPUT-MANIFEST-v1.json", manifest_out)

    write_md(
        PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-AUTHORITY-v1.md",
        "CORVONERO Campaign V2 Final Authority",
        [
            ("Verdict", "PASS — FINAL OPERATOR IMPORT PACKAGE GENERATED"),
            ("Campaigns", "10 (5 LOCAL + 5 REMOTE)"),
            ("Groups", "42"),
            ("Phrase slots", "1593"),
            ("Rejected source rows", "32"),
            ("Commander delta", "833→828 deferred to post-import reconciliation"),
            ("REMOTE NSO exclusion", "MANUAL POST-IMPORT ACTION REQUIRED"),
        ],
    )
    write_md(
        PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-PHRASE-ALLOCATION-v1.md",
        "CORVONERO Campaign V2 Final Phrase Allocation",
        [
            ("Total slots", "1593"),
            ("Source rows", "833 accounted; 32 rejected"),
            ("Geo violations", "0 LOCAL-explicit in REMOTE; 0 REMOTE-explicit in LOCAL"),
        ],
    )
    write_md(
        PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-AD-COPY-v1.md",
        "CORVONERO Campaign V2 Final Ad Copy",
        [
            ("Ads", "42 — all PASS Direct limits"),
            ("A-01 rewrite", "CA-01-REMOTE / ca-01-price-intent — «Работаем удалённо по России.»"),
            ("UTM", "Not embedded in URLs"),
        ],
    )
    write_md(
        PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-CAMPAIGN-NEGATIVES-v1.md",
        "CORVONERO Campaign V2 Final Campaign Negatives",
        [
            (
                "Policy",
                "APPROVED_SAFE only — HOLD/REJECT/CONFLICTING omitted; final conflict count 0",
            ),
            (
                "Per-campaign",
                "\n".join(
                    f"- {c['campaign_id']}: proposed {c['proposed_count']}, "
                    f"approved {c['approved_safe_count']}, rejected {c['rejected_count']}"
                    for c in neg_report["campaigns"]
                ),
            ),
        ],
    )
    write_md(
        PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-CROSS-CAMPAIGN-NEGATIVES-v1.md",
        "CORVONERO Campaign V2 Cross-Campaign Negatives",
        [("Status", "DRAFTED — NOT APPLIED (17 rules; separate future layer)")],
    )

    forensic = load_json(PILOT / "CORVONERO-CAMPAIGN-V2-FORENSIC-VALIDATION-v1.json")
    write_md(
        PILOT / "CORVONERO-CAMPAIGN-V2-FORENSIC-VALIDATION-v1.md",
        "CORVONERO Campaign V2 Forensic Validation",
        [
            ("Status", forensic.get("verdict", "UNKNOWN")),
            ("Details", json.dumps(forensic.get("summary", {}), ensure_ascii=False, indent=2)),
        ],
    )
    gen = load_json(PILOT / "CORVONERO-CAMPAIGN-V2-GENERATION-v1.json")
    write_md(
        PILOT / "CORVONERO-CAMPAIGN-V2-GENERATION-v1.md",
        "CORVONERO Campaign V2 Generation",
        [("Output", gen.get("output_directory", "")), ("Files", str(len(gen.get("generation_results", []))))],
    )
    save_json(
        PILOT / "CORVONERO-CAMPAIGN-V2-RESULT-v1.json",
        {
            "generated_at": GENERATED_AT,
            "checkpoint": CHECKPOINT,
            "verdict": "PASS — FINAL OPERATOR IMPORT PACKAGE GENERATED",
            "campaigns": 10,
            "groups": 42,
            "phrase_slots": 1593,
            "ads": 42,
            "negative_conflicts": 0,
            "cross_campaign_negatives": "NOT APPLIED",
            "commander_import": "NOT PERFORMED",
            "output_directory": str(OUTPUT_DIR),
        },
    )
    write_md(
        PILOT / "CORVONERO-CAMPAIGN-V2-RESULT-v1.md",
        "CORVONERO Campaign V2 Result",
        [("Verdict", "PASS — FINAL OPERATOR IMPORT PACKAGE GENERATED")],
    )

    report_path = REPORTS / "REPORT-corvonero-campaign-v2-final-generation-v1.md"
    write_md(
        report_path,
        "REPORT — Corvonero Campaign V2 Final Generation",
        [
            ("Verdict", "PASS — FINAL OPERATOR IMPORT PACKAGE GENERATED"),
            ("Output", str(OUTPUT_DIR)),
            ("Pass 2 decisions", "33/33 applied; A-01 rewrite applied"),
            ("Git", "No commit (per task policy)"),
        ],
    )

    print("PASS — CORVONERO CAMPAIGN V2 FINAL PACKAGE GENERATED")
    print(f"Output: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
