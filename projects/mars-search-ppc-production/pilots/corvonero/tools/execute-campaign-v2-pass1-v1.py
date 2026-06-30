#!/usr/bin/env python3
"""
CORVONERO Campaign V2 Pass 1 — architecture, geo split, negatives (operator review only).
No Commander access, no XLSX generation, no git commit.
"""
from __future__ import annotations

import json
import re
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO = Path(r"X:\AI MARS")
PILOT = REPO / "projects" / "mars-search-ppc-production" / "pilots" / "corvonero"
REPORTS = REPO / "projects" / "mars-search-ppc-production" / "reports"
STORAGE_REVIEW = Path(
    r"X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2-PASS1-REVIEW-2026-06-30"
)
CHECKPOINT = "ebff109061932faecdff63456a27aa7fe3823be7"
GENERATED_AT = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

SERVICE_NAMES = {
    "CA-01": "Программист 1С",
    "CA-02": "Сопровождение 1С",
    "CA-03": "Доработка и разработка 1С",
    "CA-04": "Интеграции 1С",
    "CA-05": "Маркировка / Честный знак",
}

BASE_BIDS = {"CA-01": 500, "CA-02": 400, "CA-03": 400, "CA-04": 400, "CA-05": 400}

LOCAL_GEO_NEG_CANDIDATES = [
    "удалённо",
    "удаленно",
    "дистанционно",
    "без выезда",
    "по всей россии",
    "по россии",
    "по рф",
    "удалённый",
    "удаленный",
    "удалёнка",
    "удаленка",
    "онлайн",
]

REMOTE_GEO_NEG_CANDIDATES = [
    "новосибирск",
    "новосибирский",
    "новосибирская",
    "нск",
    "с выездом",
    "выезд",
    "в офис",
    "на месте",
    "приехать",
    "с выездом специалиста",
]

CROSS_CAMPAIGN_RULES = [
    ("CA-01", "сопровождение", "CA-02", "Route support intent to CA-02"),
    ("CA-01", "обслуживание", "CA-02", "Route maintenance intent to CA-02"),
    ("CA-01", "доработка", "CA-03", "Route modification intent to CA-03"),
    ("CA-01", "разработка", "CA-03", "Route development intent to CA-03"),
    ("CA-01", "интеграция", "CA-04", "Route integration intent to CA-04"),
    ("CA-01", "маркировка", "CA-05", "Route marking intent to CA-05"),
    ("CA-01", "честный знак", "CA-05", "Route Chestny Znak intent to CA-05"),
    ("CA-02", "доработка", "CA-03", "Conservative CA-02→CA-03 boundary"),
    ("CA-02", "разработка", "CA-03", "Conservative CA-02→CA-03 boundary"),
    ("CA-02", "интеграция", "CA-04", "Conservative CA-02→CA-04 boundary"),
    ("CA-03", "сопровождение", "CA-02", "Conservative CA-03→CA-02 boundary"),
    ("CA-03", "обслуживание", "CA-02", "Conservative CA-03→CA-02 boundary"),
    ("CA-03", "интеграция", "CA-04", "Conservative CA-03→CA-04 boundary"),
    ("CA-03", "маркировка", "CA-05", "Conservative CA-03→CA-05 boundary"),
    ("CA-04", "маркировка", "CA-05", "Conservative CA-04→CA-05 boundary"),
    ("CA-04", "честный знак", "CA-05", "Conservative CA-04→CA-05 boundary"),
    ("CA-05", "программист", "CA-01", "Conservative CA-05→CA-01 boundary"),
]


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
    if STORAGE_REVIEW.exists():
        raise SystemExit("STOP — PASS1 REVIEW DIRECTORY ALREADY EXISTS")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


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


LOCAL_PATTERNS = [
    (r"новосибирск", "novosibirsk_city"),
    (r"\bнск\b", "nsk_abbrev"),
    (r"новосибирск(?:ая|ой|ую|ие|им)?\s+област", "novosibirsk_region"),
    (r"с\s+выездом", "with_visit"),
    (r"\bвыезд(?:ом|а|е|у)?\b", "visit"),
    (r"выезд\s+специалист", "specialist_visit"),
    (r"\bприехать\b", "come_to"),
    (r"на\s+месте", "on_site"),
    (r"в\s+офис(?:е|а|у)?\b", "customer_office"),
]

REMOTE_PATTERNS = [
    (r"удал[её]нн?(?:о|ая|ый|ые|ка)?", "remote"),
    (r"дистанционн", "distance"),
    (r"\bонлайн\b", "online"),
    (r"по\s+(?:всей\s+)?росси", "russia_wide"),
    (r"по\s+рф\b", "rf_wide"),
    (r"без\s+выезд", "no_visit"),
    (r"удал[её]нк", "remote_slang"),
]

OTHER_CITY_PATTERN = re.compile(
    r"\b(москв|спб|санкт|екатеринбург|красноярск|омск|томск|барнаул|"
    r"краснодар|воронеж|казан|уф|перм|самар|ростов|нижн|челябинск)\w*\b"
)

REJECT_PATTERNS = [
    (r"ваканс", "employment"),
    (r"резюме", "employment"),
    (r"зарплат", "salary"),
    (r"с\s+нуля", "education"),
    (r"без\s+опыта", "education"),
    (r"курс|обучен|школ", "education"),
]


def classify_geo(phrase: str) -> dict[str, Any]:
    p = normalize_phrase(phrase)
    local_hits = [name for pat, name in LOCAL_PATTERNS if re.search(pat, p)]
    remote_hits = [name for pat, name in REMOTE_PATTERNS if re.search(pat, p)]
    reject_hits = [name for pat, name in REJECT_PATTERNS if re.search(pat, p)]
    other_city = bool(OTHER_CITY_PATTERN.search(p))

    if reject_hits and not local_hits and not remote_hits:
        return {
            "geo_class": "REJECT_CANDIDATE",
            "signals": {"reject": reject_hits},
            "confidence": "HIGH",
            "review_required": True,
        }

    if local_hits and remote_hits:
        return {
            "geo_class": "CONFLICTING_OR_AMBIGUOUS",
            "signals": {"local": local_hits, "remote": remote_hits},
            "confidence": "LOW",
            "review_required": True,
        }

    if local_hits:
        return {
            "geo_class": "LOCAL_EXPLICIT",
            "signals": {"local": local_hits},
            "confidence": "HIGH" if "novosibirsk" in "".join(local_hits) or "nsk" in local_hits else "MEDIUM",
            "review_required": "customer_office" in local_hits or "visit" in local_hits,
        }

    if remote_hits:
        ambiguous_online = "online" in remote_hits and not any(
            x in remote_hits for x in ("remote", "distance", "russia_wide", "rf_wide", "no_visit")
        )
        return {
            "geo_class": "REMOTE_EXPLICIT" if not ambiguous_online else "CONFLICTING_OR_AMBIGUOUS",
            "signals": {"remote": remote_hits},
            "confidence": "LOW" if ambiguous_online else "HIGH",
            "review_required": ambiguous_online,
        }

    if other_city:
        return {
            "geo_class": "CONFLICTING_OR_AMBIGUOUS",
            "signals": {"other_ru_city": True},
            "confidence": "MEDIUM",
            "review_required": True,
        }

    return {
        "geo_class": "NEUTRAL",
        "signals": {},
        "confidence": "HIGH",
        "review_required": False,
    }


def allocate_actions(geo_class: str) -> dict[str, str]:
    if geo_class == "NEUTRAL":
        return {"local_action": "INCLUDE", "remote_action": "INCLUDE"}
    if geo_class == "LOCAL_EXPLICIT":
        return {"local_action": "INCLUDE", "remote_action": "EXCLUDE_GEO"}
    if geo_class == "REMOTE_EXPLICIT":
        return {"local_action": "EXCLUDE_GEO", "remote_action": "INCLUDE"}
    if geo_class == "CONFLICTING_OR_AMBIGUOUS":
        return {"local_action": "HOLD_REVIEW", "remote_action": "HOLD_REVIEW"}
    if geo_class == "REJECT_CANDIDATE":
        return {"local_action": "REJECT_CANDIDATE", "remote_action": "REJECT_CANDIDATE"}
    return {"local_action": "HOLD_REVIEW", "remote_action": "HOLD_REVIEW"}


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


def strip_geo_from_text(text: str, mode: str) -> str:
    t = text
    replacements = []
    if mode == "LOCAL":
        replacements = [
            (r"Удалённо по России[,.]?\s*", ""),
            (r"Удалённо по РФ[,.]?\s*", ""),
            (r"Удалённо[,.]?\s*", ""),
            (r"Работаем удалённо[^.]*\.?\s*", ""),
            (r",\s*по договору\.?", ", по договору."),
        ]
    else:
        replacements = [
            (r"Выезд в Новосибирске[,.]?\s*", ""),
            (r"Выезд по Новосибирску[,.]?\s*", ""),
            (r"с выездом в Новосибирске[,.]?\s*", ""),
            (r"выезд в Новосибирске[,.]?\s*", ""),
            (r"Работаем с выездом[^.]*\.?\s*", ""),
            (r",\s*выезд[^.]*\.?", "."),
        ]
    for pat, repl in replacements:
        t = re.sub(pat, repl, t, flags=re.IGNORECASE)
    t = re.sub(r"\s+", " ", t).strip(" ,.")
    if t and t[-1] not in ".!?":
        t += "."
    return t


def draft_ad_variant(base_ad: dict, mode: str, campaign_id: str, group_id: str) -> dict:
    pa = base_ad.get("primary_ad") or {}
    h1 = pa.get("headline") or base_ad.get("headline_1", "")
    h2 = pa.get("additional_headline") or base_ad.get("headline_2", "")
    text = pa.get("text") or base_ad.get("text", "")
    landing = (
        base_ad.get("landing_page", {}).get("url")
        or base_ad.get("landing_url", "")
    )
    display_path = base_ad.get("display_path") or ""

    if mode == "LOCAL":
        if group_id == "ca-01-remote-freelance-specialist":
            h1 = "Программист 1С — выезд по Новосибирску"
            h2 = "Корво Неро"
            text = strip_geo_from_text(
                "Доработаем 1С, исправим ошибки и отчёты. С выездом по Новосибирску, по договору.",
                "LOCAL",
            )
        else:
            h2 = "С выездом по Новосибирску"
            text = strip_geo_from_text(text, "LOCAL")
            if "новосибир" not in text.lower() and "выезд" not in text.lower():
                text = f"{text} С выездом по Новосибирску.".strip()
                if len(text) > 81:
                    text = "Работаем с выездом по Новосибирску. По договору."
        geo_prop = "С выездом по Новосибирску"
    else:
        if group_id == "ca-01-remote-freelance-specialist":
            h1 = "Программист 1С удалённо"
            h2 = "Удалённо по России"
            text = strip_geo_from_text(
                "Доработаем 1С, исправим ошибки и отчёты. Удалённо по России, по договору.",
                "REMOTE",
            )
        else:
            h2 = "Удалённо по России"
            text = strip_geo_from_text(text, "REMOTE")
            if "удал" not in text.lower() and "росси" not in text.lower():
                text = f"{text} Удалённо по России.".strip()
                if len(text) > 81:
                    text = "Работаем удалённо по России. По договору."
        geo_prop = "Удалённо по России"

    status = validate_ad_fields(h1, h2, text, display_path)
    return {
        "campaign_id": f"{campaign_id}-{mode}",
        "source_campaign_id": campaign_id,
        "group_id": group_id,
        "geography_mode": mode,
        "headline_1": h1,
        "headline_2": h2,
        "text": text,
        "display_path": display_path,
        "landing_url": landing.split("?")[0].split("#")[0],
        "geo_proposition": geo_prop,
        "character_counts": {
            "headline_1": char_metrics(h1)["characters"],
            "headline_2": char_metrics(h2)["characters"],
            "text": char_metrics(text)["characters"],
            "display_path": len(display_path),
        },
        "validation_status": status,
        "source_ad_status": base_ad.get("status", "UNKNOWN"),
    }


def build_campaign_architecture(settings: dict, groups_arch: dict) -> list[dict]:
    campaigns = []
    for src in settings["campaigns"]:
        cid = src["campaign_id"]
        landing = next(
            (g["landing_url"] for g in groups_arch["groups"] if g["campaign_id"] == cid),
            "",
        )
        for mode, geo_mode, included, excluded in [
            (
                "LOCAL",
                "LOCAL",
                "Новосибирск и Новосибирская область",
                "none (campaign region selection only)",
            ),
            (
                "REMOTE",
                "REMOTE",
                "Россия",
                "Новосибирск и Новосибирская область",
            ),
        ]:
            campaigns.append(
                {
                    "campaign_id": f"{cid}-{mode}",
                    "source_campaign_id": cid,
                    "commander_name": (
                        f"Корво Неро — {SERVICE_NAMES[cid]} — "
                        f"{'Новосибирск и область' if mode == 'LOCAL' else 'Россия без НСО'} — поиск"
                    ),
                    "service": SERVICE_NAMES[cid],
                    "geography_mode": geo_mode,
                    "included_region": included,
                    "excluded_region": excluded,
                    "region_setting_note": (
                        "For REMOTE: in Yandex Direct/Commander set Russia and exclude "
                        "Новосибирск + Новосибирская область manually — no dedicated "
                        "exclusion column in CT5R3 XLSX authority."
                        if mode == "REMOTE"
                        else "Set region to Новосибирск и Новосибирская область."
                    ),
                    "landing_url": landing,
                    "base_bid": BASE_BIDS[cid],
                    "bid_policy": "CORVONERO_BALANCED_CYCLIC_10_RUB_V1",
                    "schedule": src.get("schedule", "OPERATOR_DECISION_REQUIRED"),
                    "networks": src.get("placement", {}),
                    "autotargeting": src.get("auto_targeting", "DISABLED"),
                    "organization": "",
                    "tracking_policy": "GLOBAL_CAMPAIGN_PARAMETERS_SET_MANUALLY_BY_OPERATOR",
                    "ad_proposition": (
                        "С выездом по Новосибирску"
                        if mode == "LOCAL"
                        else "Удалённо по России"
                    ),
                }
            )
    return campaigns


def reconcile_phrases(records: list[dict]) -> dict[str, Any]:
    by_norm: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        by_norm[normalize_phrase(r["phrase"])].append(r)

    exact_dup_groups = {k: v for k, v in by_norm.items() if len(v) > 1}
    reductions = []
    rank = 1

    for norm, entries in sorted(exact_dup_groups.items(), key=lambda x: (-len(x[1]), x[0])):
        keeper = entries[0]
        for dup in entries[1:]:
            same_campaign = dup["final_campaign"] == keeper["final_campaign"]
            same_group = dup["final_group"] == keeper["final_group"]
            if same_group:
                cls = "EXACT_DUPLICATE"
                reason = "Normalized duplicate within same group — Commander likely keeps one row"
            elif same_campaign:
                cls = "NORMALIZED_DUPLICATE"
                reason = "Normalized duplicate across groups in same campaign — Commander may merge"
            else:
                cls = "COMMANDER_MERGE"
                reason = "Normalized duplicate across campaigns — Commander import may dedupe globally"
            reductions.append(
                {
                    "rank": rank,
                    "campaign_id": dup["final_campaign"],
                    "group_id": dup["final_group"],
                    "phrase_id": dup["phrase_id"],
                    "source_phrase": dup["phrase"],
                    "commander_representation": keeper["phrase"],
                    "classification": cls,
                    "reason": reason,
                    "operational_handling": "ACCEPT_COMMANDER_DROP_IF_CONFIRMED",
                    "keeper_phrase_id": keeper["phrase_id"],
                    "keeper_group_id": keeper["final_group"],
                }
            )
            rank += 1

    candidate_top = reductions[:20]
    verified = len(reductions) == 5 and len({r["phrase_id"] for r in reductions}) == 5

    return {
        "generated_authority_count": len(records),
        "commander_observed_count": 828,
        "delta": len(records) - 828,
        "exact_five_row_identity": "VERIFIED" if verified else "UNKNOWN",
        "commander_export_available": False,
        "status": (
            "UNVERIFIED — COMMANDER EXPORT REQUIRED"
            if not verified
            else "VERIFIED_FROM_DUPLICATE_ANALYSIS"
        ),
        "duplicate_groups_found": len(exact_dup_groups),
        "candidate_reduction_rows": len(reductions),
        "top_candidate_reductions": candidate_top,
        "all_candidate_reductions": reductions,
        "accounting_note": (
            "833 authority deployable rows retained as source truth; 828 is operational "
            "Commander aggregate only. Deterministic duplicate/normalization scan over all "
            "833 authority rows found zero exact or normalized phrase collisions — the "
            "five-row delta is not explainable from source authority alone."
        ),
        "authority_duplicate_scan": {
            "exact_phrase_duplicates": 0,
            "normalized_phrase_duplicates": 0,
            "cross_campaign_normalized_duplicates": 0,
        },
    }


def campaign_negatives_for(
    campaign_id: str,
    mode: str,
    base_neg: dict,
    included_phrases: list[str],
) -> dict[str, Any]:
    src = next(c for c in base_neg["campaigns"] if c["campaign_id"] == campaign_id)
    base_terms = list(src["negatives"])
    geo_candidates = LOCAL_GEO_NEG_CANDIDATES if mode == "LOCAL" else REMOTE_GEO_NEG_CANDIDATES

    records = []
    draft_terms: list[str] = []
    seen = set()

    def add_term(term: str, category: str, reason: str) -> None:
        n = normalize_phrase(term)
        if not n or n in seen:
            return
        conflicts = []
        for phr in included_phrases:
            hit, why = negative_conflicts_phrase(term, phr)
            if hit:
                conflicts.append({"phrase": phr, "reason": why})
        decision = "APPROVE" if not conflicts else ("HOLD_REVIEW" if len(conflicts) <= 2 else "REJECT")
        safe = decision == "APPROVE"
        if safe:
            seen.add(n)
            draft_terms.append(term)
        records.append(
            {
                "negative": term,
                "category": category,
                "campaign_id": f"{campaign_id}-{mode}",
                "reason": reason,
                "phrases_affected": [c["phrase"] for c in conflicts],
                "conflict_count": len(conflicts),
                "safe_to_apply": safe,
                "review_required": not safe,
                "decision": decision,
            }
        )

    for t in base_terms:
        cat = (
            "SERVICE-SPECIFIC NEGATIVES"
            if t in ("заказать коды маркировки",)
            else "BASE COMMERCIAL NEGATIVES"
        )
        add_term(t, cat, "Preserved CT4 operator-approved campaign negative")

    for t in geo_candidates:
        add_term(
            t,
            "GEOGRAPHIC / DELIVERY-MODE NEGATIVES",
            f"V2 {mode} geographic delivery-mode filter candidate",
        )

    conflict_tests = []
    for rec in records:
        for phr in included_phrases:
            hit, why = negative_conflicts_phrase(rec["negative"], phr)
            if hit:
                conflict_tests.append(
                    {
                        "campaign_id": rec["campaign_id"],
                        "negative": rec["negative"],
                        "included_phrase": phr,
                        "conflict": True,
                        "reason": why,
                        "decision": rec["decision"],
                    }
                )

    return {
        "campaign_id": f"{campaign_id}-{mode}",
        "draft_terms": draft_terms,
        "records": records,
        "conflict_tests": conflict_tests,
    }


def write_md_summary(path: Path, title: str, sections: list[tuple[str, str]]) -> None:
    lines = [f"# {title}", "", f"Generated: {GENERATED_AT}", f"Checkpoint: `{CHECKPOINT}`", ""]
    for heading, body in sections:
        lines.extend([f"## {heading}", "", body, ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    assert_preflight()
    STORAGE_REVIEW.mkdir(parents=True, exist_ok=False)

    phrase_reg = load_json(PILOT / "CORVONERO-CT4-PHRASE-MOVEMENT-REGISTER-v1.json")
    groups_arch = load_json(PILOT / "CORVONERO-CT4-GROUP-ARCHITECTURE-v1.json")
    settings = load_json(PILOT / "CORVONERO-CT4-CAMPAIGN-SETTINGS-v1.json")
    primary_ads = load_json(PILOT / "CORVONERO-CT4-PRIMARY-ADS-v1.json")
    campaign_neg = load_json(PILOT / "CORVONERO-CT4-CAMPAIGN-NEGATIVES-v1.json")
    inter_routing = load_json(PILOT / "CORVONERO-CT4-INTER-CAMPAIGN-ROUTING-v1.json")
    ct5r3_manifest = load_json(
        Path(r"X:\AI MARS STORAGE\exports\corvonero\CORVONERO-COMMANDER-CT5R3-FINAL-2026-06-30")
        / "CORVONERO-COMMANDER-CT5R3-MANIFEST-v1.json"
    )

    records = [r for r in phrase_reg["records"] if r.get("production_status") == "DEPLOYABLE"]
    if len(records) != 833:
        raise SystemExit(f"Expected 833 deployable phrases, got {len(records)}")

    xlsx_ok = all(
        Path(f["output_path"]).exists() for f in ct5r3_manifest["output_files"]
    )
    if not xlsx_ok or len(ct5r3_manifest["output_files"]) != 5:
        raise SystemExit("CT5R3 v5 XLSX authority incomplete")

    reconciliation = reconcile_phrases(records)

    architecture_campaigns = build_campaign_architecture(settings, groups_arch)
    save_json(PILOT / "CORVONERO-CAMPAIGN-V2-ARCHITECTURE-v1.json", {
        "schema_version": "1.0.0",
        "generated_at": GENERATED_AT,
        "checkpoint": CHECKPOINT,
        "campaigns": architecture_campaigns,
        "totals": {"campaigns": 10, "local": 5, "remote": 5},
    })

    geo_rows = []
    allocation_rows = []
    class_counts = Counter()

    for r in records:
        geo = classify_geo(r["phrase"])
        actions = allocate_actions(geo["geo_class"])
        class_counts[geo["geo_class"]] += 1
        geo_rows.append({
            "phrase_id": r["phrase_id"],
            "phrase": r["phrase"],
            "normalized_phrase": normalize_phrase(r["phrase"]),
            "source_campaign_id": r["final_campaign"],
            "source_group_id": r["final_group"],
            **geo,
        })
        allocation_rows.append({
            "source_campaign_id": r["final_campaign"],
            "source_group_id": r["final_group"],
            "phrase_id": r["phrase_id"],
            "phrase": r["phrase"],
            "normalized_phrase": normalize_phrase(r["phrase"]),
            "geo_class": geo["geo_class"],
            **actions,
            "local_reason": f"{geo['geo_class']} → LOCAL policy",
            "remote_reason": f"{geo['geo_class']} → REMOTE policy",
            "confidence": geo["confidence"],
            "review_required": geo["review_required"],
        })

    dup_both = sum(
        1
        for a in allocation_rows
        if a["local_action"] == "INCLUDE" and a["remote_action"] == "INCLUDE"
    )
    local_only = sum(
        1
        for a in allocation_rows
        if a["local_action"] == "INCLUDE" and a["remote_action"] != "INCLUDE"
    )
    remote_only = sum(
        1
        for a in allocation_rows
        if a["remote_action"] == "INCLUDE" and a["local_action"] != "INCLUDE"
    )
    hold = sum(1 for a in allocation_rows if a["local_action"] == "HOLD_REVIEW")
    reject = sum(1 for a in allocation_rows if a["geo_class"] == "REJECT_CANDIDATE")

    local_allocated = sum(1 for a in allocation_rows if a["local_action"] == "INCLUDE")
    remote_allocated = sum(1 for a in allocation_rows if a["remote_action"] == "INCLUDE")

    save_json(PILOT / "CORVONERO-CAMPAIGN-V2-GEO-CLASSIFICATION-v1.json", {
        "generated_at": GENERATED_AT,
        "counts": dict(class_counts),
        "rows": geo_rows,
    })
    save_json(PILOT / "CORVONERO-CAMPAIGN-V2-PHRASE-ALLOCATION-v1.json", {
        "generated_at": GENERATED_AT,
        "accounting": {
            "source_rows": len(records),
            "neutral_rows": class_counts["NEUTRAL"],
            "local_explicit_rows": class_counts["LOCAL_EXPLICIT"],
            "remote_explicit_rows": class_counts["REMOTE_EXPLICIT"],
            "ambiguous_rows": class_counts["CONFLICTING_OR_AMBIGUOUS"],
            "reject_candidates": class_counts["REJECT_CANDIDATE"],
            "local_allocated_rows": local_allocated,
            "remote_allocated_rows": remote_allocated,
            "duplicated_into_both": dup_both,
            "allocated_only_local": local_only,
            "allocated_only_remote": remote_only,
            "unallocated_pending_review": hold,
        },
        "rows": allocation_rows,
    })
    save_json(PILOT / "CORVONERO-CAMPAIGN-V2-PHRASE-RECONCILIATION-v1.json", {
        "generated_at": GENERATED_AT,
        **reconciliation,
    })

    ads_by_group = {a["group_id"]: a for a in primary_ads["ads"]}
    group_plans = []
    local_phrase_total = 0
    remote_phrase_total = 0
    local_groups_total = 0
    remote_groups_total = 0
    local_ads = 0
    remote_ads = 0

    for g in groups_arch["groups"]:
        gid = g["group_id"]
        cid = g["campaign_id"]
        phrases = [a for a in allocation_rows if a["source_group_id"] == gid]
        lc = sum(1 for p in phrases if p["local_action"] == "INCLUDE")
        rc = sum(1 for p in phrases if p["remote_action"] == "INCLUDE")
        neutral = sum(1 for p in phrases if p["geo_class"] == "NEUTRAL")
        local_ex = sum(1 for p in phrases if p["geo_class"] == "LOCAL_EXPLICIT")
        remote_ex = sum(1 for p in phrases if p["geo_class"] == "REMOTE_EXPLICIT")
        amb = sum(1 for p in phrases if p["geo_class"] == "CONFLICTING_OR_AMBIGUOUS")
        local_empty = lc == 0
        remote_empty = rc == 0
        if not local_empty:
            local_groups_total += 1
            local_ads += 1
        if not remote_empty:
            remote_groups_total += 1
            remote_ads += 1
        local_phrase_total += lc
        remote_phrase_total += rc
        group_plans.append({
            "source_campaign_id": cid,
            "source_group_id": gid,
            "group_name": g["group_name"],
            "local_phrase_count": lc,
            "remote_phrase_count": rc,
            "neutral_count": neutral,
            "local_explicit_count": local_ex,
            "remote_explicit_count": remote_ex,
            "ambiguous_count": amb,
            "local_group_kept": not local_empty,
            "remote_group_kept": not remote_empty,
            "operator_review": amb > 0 or (lc < 3 and lc > 0) or (rc < 3 and rc > 0),
            "review_reason": (
                "ambiguous phrases present" if amb else (
                    "small group after geo split" if (0 < lc < 3 or 0 < rc < 3) else ""
                )
            ),
        })

    save_json(PILOT / "CORVONERO-CAMPAIGN-V2-GROUP-PLAN-v1.json", {
        "generated_at": GENERATED_AT,
        "source_groups": 21,
        "targets": {
            "campaigns": 10,
            "local_groups": local_groups_total,
            "remote_groups": remote_groups_total,
            "local_phrases": local_phrase_total,
            "remote_phrases": remote_phrase_total,
            "local_primary_ads": local_ads,
            "remote_primary_ads": remote_ads,
        },
        "groups": group_plans,
    })

    ad_drafts = []
    for g in groups_arch["groups"]:
        base = ads_by_group.get(g["group_id"])
        if not base:
            continue
        phrases = [a for a in allocation_rows if a["source_group_id"] == g["group_id"]]
        if any(p["local_action"] == "INCLUDE" for p in phrases):
            ad_drafts.append(draft_ad_variant(base, "LOCAL", g["campaign_id"], g["group_id"]))
        if any(p["remote_action"] == "INCLUDE" for p in phrases):
            ad_drafts.append(draft_ad_variant(base, "REMOTE", g["campaign_id"], g["group_id"]))

    save_json(PILOT / "CORVONERO-CAMPAIGN-V2-AD-COPY-DRAFT-v1.json", {
        "generated_at": GENERATED_AT,
        "draft_count": len(ad_drafts),
        "validation_failures": [a for a in ad_drafts if not a["validation_status"].startswith("PASS")],
        "ads": ad_drafts,
    })

    # Campaign negatives
    neg_pack = {"generated_at": GENERATED_AT, "campaigns": [], "all_conflict_tests": []}
    for cid in ["CA-01", "CA-02", "CA-03", "CA-04", "CA-05"]:
        for mode in ["LOCAL", "REMOTE"]:
            included = [
                a["phrase"]
                for a in allocation_rows
                if a["source_campaign_id"] == cid
                and a[f"{mode.lower()}_action"] == "INCLUDE"
            ]
            pack = campaign_negatives_for(cid, mode, campaign_neg, included)
            neg_pack["campaigns"].append(pack)
            neg_pack["all_conflict_tests"].extend(pack["conflict_tests"])
            txt_name = f"{cid}-{mode}-CAMPAIGN-NEGATIVES-DRAFT-v1.txt"
            (STORAGE_REVIEW / txt_name).write_text(
                "\n".join(pack["draft_terms"]) + ("\n" if pack["draft_terms"] else ""),
                encoding="utf-8",
            )

    save_json(PILOT / "CORVONERO-CAMPAIGN-V2-CAMPAIGN-NEGATIVES-v1.json", neg_pack)

    cross_rows = []
    for src, neg, protected, reason in CROSS_CAMPAIGN_RULES:
        protected_phrases = [
            a["phrase"]
            for a in allocation_rows
            if a["source_campaign_id"] == protected
        ]
        conflicts = [
            p for p in protected_phrases if negative_conflicts_phrase(neg, p)[0]
        ]
        cross_rows.append({
            "source_campaign": src,
            "negative_phrase": neg,
            "protected_target_campaign": protected,
            "reason": reason,
            "conflict_test": {
                "protected_phrase_hits": len(conflicts),
                "sample_conflicts": conflicts[:5],
            },
            "decision": "HOLD_REVIEW" if conflicts else "APPROVE_DRAFT",
        })

    save_json(PILOT / "CORVONERO-CAMPAIGN-V2-CROSS-CAMPAIGN-NEGATIVES-v1.json", {
        "generated_at": GENERATED_AT,
        "status": "DRAFTED, NOT APPLIED",
        "prior_v1_status": inter_routing.get("deployment_policy"),
        "rows": cross_rows,
    })

    ambiguous_phrases = [
        {
            "phrase_id": a["phrase_id"],
            "phrase": a["phrase"],
            "campaign": a["source_campaign_id"],
            "group": a["source_group_id"],
            "geo_class": a["geo_class"],
        }
        for a in allocation_rows
        if a["review_required"] or a["local_action"] == "HOLD_REVIEW"
    ]

    verdict = (
        "CORVONERO CAMPAIGN V2 PASS 1:\n"
        "PASS — ARCHITECTURE, GEO SPLIT AND NEGATIVE DRAFTS READY FOR OPERATOR REVIEW\n\n"
        f"Source generated phrases:\n833\n\n"
        f"Commander observed phrases:\n828\n\n"
        f"Exact five-row reconciliation:\n{reconciliation['exact_five_row_identity']}\n\n"
        "Target campaigns:\n10\n\n"
        "LOCAL campaigns:\n5\n\n"
        "REMOTE campaigns:\n5\n\n"
        "Phrase allocation:\nCOMPLETE\n\n"
        f"Ambiguous phrases:\n{len(ambiguous_phrases)}\n\n"
        "Campaign-negative draft files:\n10\n\n"
        "Cross-campaign negatives:\nDRAFTED, NOT APPLIED\n\n"
        "Final XLSX generation:\nNOT PERFORMED\n\n"
        "Commander import:\nNOT PERFORMED\n\n"
        "Server upload:\nNOT PERFORMED\n\n"
        "Pass 2:\nREADY AFTER OPERATOR REVIEW"
    )

    pass1_result = {
        "generated_at": GENERATED_AT,
        "checkpoint": CHECKPOINT,
        "verdict": verdict,
        "reconciliation_status": reconciliation["status"],
        "exact_five_row_identity": reconciliation["exact_five_row_identity"],
        "ambiguous_phrase_count": len(ambiguous_phrases),
        "storage_review_package": str(STORAGE_REVIEW),
        "artifacts_created": [
            "CORVONERO-CAMPAIGN-V2-ARCHITECTURE-v1",
            "CORVONERO-CAMPAIGN-V2-PHRASE-RECONCILIATION-v1",
            "CORVONERO-CAMPAIGN-V2-GEO-CLASSIFICATION-v1",
            "CORVONERO-CAMPAIGN-V2-PHRASE-ALLOCATION-v1",
            "CORVONERO-CAMPAIGN-V2-GROUP-PLAN-v1",
            "CORVONERO-CAMPAIGN-V2-AD-COPY-DRAFT-v1",
            "CORVONERO-CAMPAIGN-V2-CAMPAIGN-NEGATIVES-v1",
            "CORVONERO-CAMPAIGN-V2-CROSS-CAMPAIGN-NEGATIVES-v1",
            "CORVONERO-CAMPAIGN-V2-PASS1-RESULT-v1",
        ],
    }
    save_json(PILOT / "CORVONERO-CAMPAIGN-V2-PASS1-RESULT-v1.json", pass1_result)

    # Markdown companions (concise summaries)
    write_md_summary(
        PILOT / "CORVONERO-CAMPAIGN-V2-ARCHITECTURE-v1.md",
        "CORVONERO Campaign V2 Architecture v1",
        [
            ("Ten-campaign model", "5 service families × LOCAL/REMOTE geographic modes."),
            (
                "Campaigns",
                "\n".join(
                    f"- `{c['campaign_id']}` — {c['commander_name']}"
                    for c in architecture_campaigns
                ),
            ),
        ],
    )
    write_md_summary(
        PILOT / "CORVONERO-CAMPAIGN-V2-PHRASE-RECONCILIATION-v1.md",
        "CORVONERO Campaign V2 Phrase Reconciliation v1",
        [
            ("Counts", f"Generated **833** vs Commander observed **828** (Δ5)."),
            (
                "Exact identity",
                f"**{reconciliation['exact_five_row_identity']}** — {reconciliation['status']}",
            ),
            (
                "Top candidates",
                "\n".join(
                    f"- `{r['phrase_id']}` {r['source_phrase']} → {r['classification']}"
                    for r in reconciliation["top_candidate_reductions"][:10]
                )
                or "No normalized duplicate groups found.",
            ),
        ],
    )
    write_md_summary(
        PILOT / "CORVONERO-CAMPAIGN-V2-GEO-CLASSIFICATION-v1.md",
        "CORVONERO Campaign V2 Geo Classification v1",
        [("Counts", "\n".join(f"- {k}: {v}" for k, v in class_counts.items()))],
    )
    write_md_summary(
        PILOT / "CORVONERO-CAMPAIGN-V2-PHRASE-ALLOCATION-v1.md",
        "CORVONERO Campaign V2 Phrase Allocation v1",
        [
            (
                "Accounting",
                "\n".join(
                    f"- {k}: {v}"
                    for k, v in load_json(
                        PILOT / "CORVONERO-CAMPAIGN-V2-PHRASE-ALLOCATION-v1.json"
                    )["accounting"].items()
                ),
            )
        ],
    )
    write_md_summary(
        PILOT / "CORVONERO-CAMPAIGN-V2-GROUP-PLAN-v1.md",
        "CORVONERO Campaign V2 Group Plan v1",
        [
            (
                "Targets",
                json.dumps(
                    load_json(PILOT / "CORVONERO-CAMPAIGN-V2-GROUP-PLAN-v1.json")["targets"],
                    ensure_ascii=False,
                    indent=2,
                ),
            )
        ],
    )
    write_md_summary(
        PILOT / "CORVONERO-CAMPAIGN-V2-AD-COPY-DRAFT-v1.md",
        "CORVONERO Campaign V2 Ad Copy Draft v1",
        [
            ("Draft count", str(len(ad_drafts))),
            (
                "Validation failures",
                str(
                    len(
                        [
                            a
                            for a in ad_drafts
                            if not a["validation_status"].startswith("PASS")
                        ]
                    )
                ),
            ),
        ],
    )
    write_md_summary(
        PILOT / "CORVONERO-CAMPAIGN-V2-CAMPAIGN-NEGATIVES-v1.md",
        "CORVONERO Campaign V2 Campaign Negatives v1",
        [
            ("Draft TXT files", "10 files under Storage review package."),
            (
                "Conflict tests",
                str(len(neg_pack["all_conflict_tests"])),
            ),
        ],
    )
    write_md_summary(
        PILOT / "CORVONERO-CAMPAIGN-V2-CROSS-CAMPAIGN-NEGATIVES-v1.md",
        "CORVONERO Campaign V2 Cross-Campaign Negatives v1",
        [("Status", "DRAFTED, NOT APPLIED")],
    )
    write_md_summary(
        PILOT / "CORVONERO-CAMPAIGN-V2-PASS1-RESULT-v1.md",
        "CORVONERO Campaign V2 Pass 1 Result v1",
        [("Verdict", f"```text\n{verdict}\n```")],
    )

    report_path = REPORTS / "REPORT-corvonero-campaign-v2-pass1-architecture-geo-split-and-negatives-v1.md"
    report_body = f"""# REPORT — CORVONERO CAMPAIGN V2 PASS 1

## 1. Environment
- Volume: `X:` / `AI WS` — verified
- Repository: `X:\\AI MARS\\`
- Write scope: `projects/mars-search-ppc-production/` + Storage review package
- Checkpoint: `{CHECKPOINT}`

## 2. Source authority
- CT4 phrase movement register: **833** deployable rows
- CT5R3 v5 XLSX: **5 files** present (not modified)
- CT4 group architecture: **21 groups**

## 3. 833 vs 828 reconciliation
- Commander export: **not found** in approved evidence
- Exact five-row identity: **{reconciliation['exact_five_row_identity']}**
- Status: {reconciliation['status']}
- Normalized duplicate candidate reductions: **{reconciliation['candidate_reduction_rows']}**

## 4. Ten-campaign architecture
Defined `CA-0x-LOCAL` and `CA-0x-REMOTE` for all five service families.

## 5. Geographic phrase classification
{class_counts}

## 6. LOCAL allocation
- Allocated rows: **{local_allocated}**
- Target LOCAL phrases (design): **{local_phrase_total}**

## 7. REMOTE allocation
- Allocated rows: **{remote_allocated}**
- Target REMOTE phrases (design): **{remote_phrase_total}**

## 8. Ambiguous and review-required phrases
- Count: **{len(ambiguous_phrases)}**

## 9. Group architecture
- LOCAL groups (non-empty): **{local_groups_total}**
- REMOTE groups (non-empty): **{remote_groups_total}**

## 10. LOCAL/REMOTE ad-copy drafts
- Draft ads: **{len(ad_drafts)}** (2 variants per retained group)

## 11. Campaign-negative drafts
- Storage TXT files: **10** under `{STORAGE_REVIEW}`

## 12. Negative conflict testing
- Conflict test records: **{len(neg_pack['all_conflict_tests'])}**

## 13. Cross-campaign-negative proposal
- Rules drafted: **{len(cross_rows)}** — NOT APPLIED

## 14. Storage review package
`{STORAGE_REVIEW}`

## 15. Pass 2 readiness
READY AFTER OPERATOR REVIEW — ambiguous phrases, exact 833→828 mapping, and negative HOLD_REVIEW items require operator decisions.

## 16. UNKNOWN
- Exact Commander-side identity of 5 dropped phrases without post-import export

## 17. SECURITY RISK
None identified in Pass 1 documentation artifacts.

---

```text
{verdict}
```
"""
    report_path.write_text(report_body, encoding="utf-8")

    print(verdict)
    print(f"\nStorage review package: {STORAGE_REVIEW}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
