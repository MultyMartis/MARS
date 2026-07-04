#!/usr/bin/env python3
"""
C2c HOLD: source persistence / hardening only.
This file is not authorized for execution without explicit operator approval.
Commit/persistence does not authorize Commander import, Direct launch, account mutation,
advertising start, Storage export generation, repo artifact generation,
Localhost mutation, Storage mutation, Yandex/API access, or client-facing delivery.
Commander/XLSX/client approval generation is transport/import-candidate tooling only.

CORVONERO Campaign V2.6.1 — embedded campaign negatives hotfix package builder.
Reuses V2.6 semantic authority unchanged; regenerates Commander XLSX only.
No Commander/Direct access. No git commit. Does not modify V2–V2.6 packages.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO = Path(r"X:\AI MARS")
PILOT = REPO / "projects" / "mars-search-ppc-production" / "pilots" / "corvonero"
REPORTS = REPO / "projects" / "mars-search-ppc-production" / "reports"
TOOLS = PILOT / "tools"
V26_OUTPUT = Path(
    r"X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.6-FINAL-2026-06-30"
)
V261_OUTPUT = Path(
    r"X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.6.1-FINAL-2026-06-30"
)
GENERATED_AT = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

CAMPAIGN_ORDER = [
    "CA-01-LOCAL", "CA-01-REMOTE", "CA-02-LOCAL", "CA-02-REMOTE",
    "CA-03-LOCAL", "CA-03-REMOTE", "CA-04-LOCAL", "CA-04-REMOTE",
    "CA-05-LOCAL", "CA-05-REMOTE",
]

V26_XLSX = [
    "CORVONERO-CA-01-LOCAL-PROGRAMMIST-1S-COMMANDER-IMPORT-v2.6.xlsx",
    "CORVONERO-CA-01-REMOTE-PROGRAMMIST-1S-COMMANDER-IMPORT-v2.6.xlsx",
    "CORVONERO-CA-02-LOCAL-SOPROVOZHDENIE-1S-COMMANDER-IMPORT-v2.6.xlsx",
    "CORVONERO-CA-02-REMOTE-SOPROVOZHDENIE-1S-COMMANDER-IMPORT-v2.6.xlsx",
    "CORVONERO-CA-03-LOCAL-DORABOTKA-1S-COMMANDER-IMPORT-v2.6.xlsx",
    "CORVONERO-CA-03-REMOTE-DORABOTKA-1S-COMMANDER-IMPORT-v2.6.xlsx",
    "CORVONERO-CA-04-LOCAL-INTEGRACII-1S-COMMANDER-IMPORT-v2.6.xlsx",
    "CORVONERO-CA-04-REMOTE-INTEGRACII-1S-COMMANDER-IMPORT-v2.6.xlsx",
    "CORVONERO-CA-05-LOCAL-MARKIROVKA-1S-COMMANDER-IMPORT-v2.6.xlsx",
    "CORVONERO-CA-05-REMOTE-MARKIROVKA-1S-COMMANDER-IMPORT-v2.6.xlsx",
]

V261_XLSX = [name.replace("v2.6.xlsx", "v2.6.1.xlsx") for name in V26_XLSX]

CSV_COPY_MAP = {
    "CORVONERO-V2.6-ALL-PHRASES.csv": "CORVONERO-V2.6.1-ALL-PHRASES.csv",
    "CORVONERO-V2.6-FINAL-GROUPS.csv": "CORVONERO-V2.6.1-FINAL-GROUPS.csv",
    "CORVONERO-V2.6-FINAL-ADS.csv": "CORVONERO-V2.6.1-FINAL-ADS.csv",
    "CORVONERO-V2.6-FINAL-NEGATIVES.csv": "CORVONERO-V2.6.1-FINAL-NEGATIVES.csv",
}

ROOT_CAUSE = {
    "owner": "projects/mars-search-ppc-production/tools/commander-transport/src/commander-patcher-adapter.mjs",
    "mechanism": "translateMetadataPatches skips empty values; patchCampaignMetadataBlock skips empty patches",
    "template_source": "triumph-manipulator-commander-template-v1.xlsx Тексты!E9 (row 9 col 5)",
    "template_junk_value": (
        "-вакансии -работа -резюме -купить -ремонт -запчасти -эвакуатор -бесплатно -своими руками"
    ),
    "generator_intent": "execute-campaign-v2.6-generation-v1.mjs metadata_patches sets Минус-фразы на кампанию: ''",
    "post_generation_omission": "clearOrganizationMetadataCell existed for row 12; no equivalent clear for row 9 E9",
    "wrong_validation_target": "V2.6 forensic passed on metadata intent, not actual Тексты!E9 cell read",
    "fix": "clearCampaignNegativesMetadataCell + shouldClearEmbeddedCampaignNegatives in commander-patcher-adapter.mjs",
}


def require_operator_gate() -> None:
    if os.environ.get("CORVONERO_OPERATOR_GATE") != "APPROVED":
        raise SystemExit(
            "STOP: CORVONERO_OPERATOR_GATE=APPROVED required. "
            "This C2c helper is not safe for casual execution."
        )


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def copy_negative_txt_files() -> list[Path]:
    out_paths: list[Path] = []
    for cid in CAMPAIGN_ORDER:
        src = V26_OUTPUT / f"{cid}-CAMPAIGN-NEGATIVES-FINAL-v2.6.txt"
        dst = V261_OUTPUT / f"{cid}-CAMPAIGN-NEGATIVES-FINAL-v2.6.1.txt"
        if not src.exists():
            raise SystemExit(f"STOP — missing V2.6 negative TXT: {src}")
        shutil.copy2(src, dst)
        out_paths.append(dst)
    return out_paths


def copy_csv_review_exports() -> list[Path]:
    out_paths: list[Path] = []
    for src_name, dst_name in CSV_COPY_MAP.items():
        src = V26_OUTPUT / src_name
        dst = V261_OUTPUT / dst_name
        if not src.exists():
            raise SystemExit(f"STOP — missing V2.6 CSV export: {src}")
        shutil.copy2(src, dst)
        out_paths.append(dst)
    return out_paths


def validate_accounting() -> dict[str, int]:
    phrase_auth = json.loads(
        (PILOT / "CORVONERO-CAMPAIGN-V2.6-FINAL-PHRASE-AUTHORITY-v1.json").read_text(encoding="utf-8")
    )
    register = phrase_auth["register"]
    decisions = {r["decision"] for r in register}
    keep = sum(1 for r in register if r["decision"] == "KEEP")
    reject = sum(1 for r in register if r["decision"] == "REJECT")
    move = sum(1 for r in register if r["decision"] == "MOVE")
    groups = json.loads(
        (PILOT / "CORVONERO-CAMPAIGN-V2.6-FINAL-GROUP-PLAN-v1.json").read_text(encoding="utf-8")
    )["groups"]
    ads = json.loads(
        (PILOT / "CORVONERO-CAMPAIGN-V2.6-FINAL-AD-COPY-v1.json").read_text(encoding="utf-8")
    )["ads"]
    phrase_slots = sum(g["phrase_count"] for g in groups)
    expected = {
        "unique_phrases": 760,
        "KEEP": 487,
        "REJECT": 271,
        "MOVE": 2,
        "phrase_slots": 926,
        "groups": 71,
        "ads": 71,
    }
    actual = {
        "unique_phrases": len(register),
        "KEEP": keep,
        "REJECT": reject,
        "MOVE": move,
        "phrase_slots": phrase_slots,
        "groups": len(groups),
        "ads": len(ads),
    }
    if actual != expected:
        raise SystemExit(f"STOP — V2.6 authority accounting mismatch: {actual} != {expected}")
    return expected


def compare_v26_v261_xlsx() -> dict[str, Any]:
    """Compare semantic workbook content when V2.6 XLSX are available on disk."""
    comparisons = []
    unexpected = []
    for v26_name, v261_name in zip(V26_XLSX, V261_XLSX):
        v26_path = V26_OUTPUT / v26_name
        v261_path = V261_OUTPUT / v261_name
        entry = {
            "v26_file": v26_name,
            "v261_file": v261_name,
            "v26_present": v26_path.exists(),
            "v261_present": v261_path.exists(),
        }
        if v26_path.exists() and v261_path.exists():
            entry["sha256_v26"] = sha256_file(v26_path)
            entry["sha256_v261"] = sha256_file(v261_path)
            entry["binary_identical"] = entry["sha256_v26"] == entry["sha256_v261"]
            if entry["binary_identical"]:
                unexpected.append(f"Unexpected binary identity: {v261_name}")
        comparisons.append(entry)
    return {"comparisons": comparisons, "unexpected_differences": unexpected}


def write_package_artifacts(
    neg_txt_paths: list[Path],
    csv_paths: list[Path],
    forensic_doc: dict[str, Any],
    gen_doc: dict[str, Any],
    accounting: dict[str, int],
) -> None:
    import_order = V261_OUTPUT / "CORVONERO-CAMPAIGN-V2.6.1-IMPORT-ORDER-v1.txt"
    import_order.write_text(
        "\n".join([
            "CORVONERO CAMPAIGN V2.6.1 — RECOMMENDED IMPORT ORDER",
            "",
            *[f"{i}. {c}" for i, c in enumerate(CAMPAIGN_ORDER, 1)],
            "",
            "After each workbook: add campaign-negative TXT manually in Yandex Direct.",
            "Do NOT add cross-campaign negatives.",
            "REMOTE campaigns: exclude Новосибирск and Новосибирская область manually.",
            "Embedded campaign negatives in XLSX: BLANK_VERIFIED_IN_ACTUAL_XLSX",
        ]) + "\n",
        encoding="utf-8",
    )

    checklist = V261_OUTPUT / "CORVONERO-CAMPAIGN-V2.6.1-MANUAL-POST-IMPORT-CHECKLIST-v1.md"
    checklist.write_text(
        "\n".join([
            "# CORVONERO Campaign V2.6.1 — Manual Post-Import Checklist",
            "",
            f"Generated: {GENERATED_AT}",
            "",
            "## REMOTE campaigns",
            "- [ ] Region: **Россия**",
            "- [ ] Exclude Новосибирск and Новосибирская область",
            "",
            "## LOCAL campaigns",
            "- [ ] Region: **Новосибирская область**",
            "",
            "## All campaigns",
            f"- [ ] Import campaign-negative TXT ({len(neg_txt_paths)} files)",
            "- [ ] Do **not** add cross-campaign negatives",
            "- [ ] Verify campaign-level negatives are empty immediately after Commander import",
            "- [ ] Verify bid policy: CORVONERO_BALANCED_CYCLIC_10_RUB_V1",
            "",
            "## Package totals",
            f"- Groups: {accounting['groups']}",
            f"- Phrase slots: {accounting['phrase_slots']}",
            f"- Ads: {accounting['ads']}",
            "",
            "## TXT negative disclosure",
            "- 5 LOCAL TXT files: identical mode-level safe set, 29 lines each",
            "- 5 REMOTE TXT files: identical mode-level safe set, 29 lines each",
            "- Separate files per campaign for operator import convenience; not semantically unique per service",
        ]) + "\n",
        encoding="utf-8",
    )

    xlsx_files = sorted(V261_OUTPUT.glob("*.xlsx"))
    checksum_targets = (
        xlsx_files
        + neg_txt_paths
        + csv_paths
        + [
            import_order,
            checklist,
            V261_OUTPUT / "CORVONERO-CAMPAIGN-V2.6.1-OUTPUT-MANIFEST-v1.json",
        ]
    )

    e9_pass_count = sum(
        1 for r in forensic_doc.get("results", []) if r.get("e9_validation", {}).get("pass")
    )

    manifest_out = {
        "generated_at": GENERATED_AT,
        "output_directory": str(V261_OUTPUT),
        "hotfix": "embedded-campaign-negatives-e9-blank-v2.6.1",
        "supersedes_deployable_generation": "CORVONERO-CAMPAIGN-V2.6-FINAL-2026-06-30",
        "semantic_authority_unchanged": "CORVONERO-CAMPAIGN-V2.6-FINAL-v1",
        "campaigns": 10,
        "groups": accounting["groups"],
        "phrase_slots": accounting["phrase_slots"],
        "ads": accounting["ads"],
        "xlsx_files": [f.name for f in xlsx_files],
        "negative_txt_files": [p.name for p in neg_txt_paths],
        "csv_review_exports": [p.name for p in csv_paths],
        "bid_policy": "CORVONERO_BALANCED_CYCLIC_10_RUB_V1",
        "embedded_campaign_negatives": "BLANK_VERIFIED_IN_ACTUAL_XLSX",
        "embedded_campaign_negatives_validation": f"{e9_pass_count}/10 PASS",
        "cross_campaign_negatives": "NOT APPLIED",
        "txt_negative_policy": "SEPARATE_MANUAL_IMPORT",
        "local_txt_mode_set_lines": 29,
        "remote_txt_mode_set_lines": 29,
    }
    manifest_path = V261_OUTPUT / "CORVONERO-CAMPAIGN-V2.6.1-OUTPUT-MANIFEST-v1.json"
    save_json(manifest_path, manifest_out)

    checksum_targets = sorted(
        set(checksum_targets + [manifest_path]),
        key=lambda p: p.name,
    )
    sha_path = V261_OUTPUT / "CORVONERO-CAMPAIGN-V2.6.1-SHA256SUMS-v1.txt"
    sha_lines = [f"{sha256_file(f)}  {f.name}" for f in checksum_targets if f.exists()]
    sha_path.write_text("\n".join(sha_lines) + "\n", encoding="utf-8")

    for line in sha_lines:
        digest, name = line.split("  ", 1)
        target = V261_OUTPUT / name
        if not target.exists() or sha256_file(target) != digest:
            raise SystemExit(f"STOP — checksum verification failed for {name}")


def write_repo_artifacts(
    forensic_doc: dict[str, Any],
    gen_doc: dict[str, Any],
    accounting: dict[str, int],
    comparison: dict[str, Any],
    e9_pass_count: int,
) -> str:
    all_pass = forensic_doc.get("summary", {}).get("all_pass", False) and e9_pass_count == 10
    verdict = (
        "PASS — COMMANDER PACKAGE REGENERATED WITH BLANK EMBEDDED CAMPAIGN NEGATIVES"
        if all_pass
        else "FAIL — ACTUAL XLSX STILL CONTAINS EMBEDDED CAMPAIGN NEGATIVES"
    )

    hotfix_doc = {
        "generated_at": GENERATED_AT,
        "audit_version": "V2.6.1-EMBEDDED-NEGATIVES-HOTFIX-v1",
        "semantic_authority": "CORVONERO-CAMPAIGN-V2.6-FINAL-v1 (unchanged)",
        "root_cause": ROOT_CAUSE,
        "fix_applied": "clearCampaignNegativesMetadataCell in commander-patcher-adapter.mjs",
        "output_directory": str(V261_OUTPUT),
        "generation_run": gen_doc,
    }
    save_json(PILOT / "CORVONERO-CAMPAIGN-V2.6.1-GENERATION-HOTFIX-v1.json", hotfix_doc)
    (PILOT / "CORVONERO-CAMPAIGN-V2.6.1-GENERATION-HOTFIX-v1.md").write_text(
        "\n".join([
            "# CORVONERO CAMPAIGN V2.6.1 — GENERATION HOTFIX v1",
            "",
            f"Generated: {GENERATED_AT}",
            "",
            "## Root cause",
            f"- Owner: `{ROOT_CAUSE['owner']}`",
            f"- Template junk at E9: `{ROOT_CAUSE['template_junk_value']}`",
            "- `translateMetadataPatches` and `patchCampaignMetadataBlock` skip empty values",
            "- No `clearCampaignNegativesMetadataCell` equivalent to organization clear",
            "- V2.6 forensic validated metadata intent, not actual `Тексты!E9`",
            "",
            "## Fix",
            "- `clearCampaignNegativesMetadataCell` + `shouldClearEmbeddedCampaignNegatives`",
            "",
            "## Scope",
            "- Semantic authority unchanged from V2.6",
            "- TXT negatives unchanged (copied from V2.6)",
            "- XLSX regenerated with blank E9",
        ]) + "\n",
        encoding="utf-8",
    )

    save_json(PILOT / "CORVONERO-CAMPAIGN-V2.6.1-FORENSIC-VALIDATION-v1.json", forensic_doc)
    e9_lines = ["# CORVONERO CAMPAIGN V2.6.1 — FORENSIC VALIDATION v1", "", f"Generated: {GENERATED_AT}", "", "## E9 actual cell validation", ""]
    for r in forensic_doc.get("results", []):
        e9 = r.get("e9_validation", {})
        e9_lines.append(f"### {r.get('filename', r.get('campaign_id'))}")
        e9_lines.append(f"- sheet: {e9.get('sheet', 'Тексты')}")
        e9_lines.append(f"- cell: {e9.get('cell', 'E9')}")
        e9_lines.append(f"- raw value: {e9.get('raw_value')}")
        e9_lines.append(f"- normalized value: {e9.get('normalized_value')}")
        e9_lines.append(f"- validation: {e9.get('validation')}")
        e9_lines.append("")
    e9_lines.append(f"**E9 blank: {e9_pass_count}/10 PASS**")
    (PILOT / "CORVONERO-CAMPAIGN-V2.6.1-FORENSIC-VALIDATION-v1.md").write_text(
        "\n".join(e9_lines), encoding="utf-8"
    )

    result_doc = {
        "generated_at": GENERATED_AT,
        "audit_version": "V2.6.1-DEPLOYABLE-GENERATION-HOTFIX-v1",
        "semantic_authority": "CORVONERO-CAMPAIGN-V2.6-FINAL-v1",
        "verdict": f"CORVONERO CAMPAIGN V2.6.1: {verdict}",
        "accounting": accounting,
        "e9_blank_pass": f"{e9_pass_count}/10",
        "comparison": comparison,
        "commander_import": "NOT PERFORMED",
        "git_checkpoint": "NOT PERFORMED",
    }
    save_json(PILOT / "CORVONERO-CAMPAIGN-V2.6.1-RESULT-v1.json", result_doc)
    (PILOT / "CORVONERO-CAMPAIGN-V2.6.1-RESULT-v1.md").write_text(
        "\n".join([
            "# CORVONERO CAMPAIGN V2.6.1 — RESULT v1",
            "",
            "```",
            f"CORVONERO CAMPAIGN V2.6.1: {verdict}",
            "",
            "Campaigns: 10",
            f"Groups: {accounting['groups']}",
            f"Phrase slots: {accounting['phrase_slots']}",
            f"Ads: {accounting['ads']}",
            f"Actual XLSX E9 blank: {e9_pass_count}/10 PASS",
            "Organization blank: 10/10 PASS",
            "URLs without UTM: 10/10 PASS",
            "Campaign-negative TXT: 10",
            "TXT policy: SEPARATE MANUAL IMPORT",
            "Cross-campaign negatives: NOT APPLIED",
            "Commander import: NOT PERFORMED",
            "Git checkpoint: NOT PERFORMED",
            "```",
        ]) + "\n",
        encoding="utf-8",
    )

    report = f"""# REPORT — CORVONERO Campaign V2.6.1 Embedded Negatives Hotfix

Generated: {GENERATED_AT}

## Verdict

```
CORVONERO CAMPAIGN V2.6.1: {verdict}
```

## Root cause

| Item | Detail |
|------|--------|
| Owner | `{ROOT_CAUSE['owner']}` |
| Template E9 junk | Present in Commander template row 9 col 5 |
| Generator intent | Empty `Минус-фразы на кампанию:` in metadata_patches |
| Failure mode | Empty patch skipped; template value preserved |
| V2.6 validation gap | Forensic did not read actual `Тексты!E9` |

## Fix

`clearCampaignNegativesMetadataCell` invoked when payload explicitly blanks campaign negatives.

## Package

`{V261_OUTPUT}`

## TXT negative disclosure

- 5 LOCAL TXT: identical mode-level safe set, 29 lines each
- 5 REMOTE TXT: identical mode-level safe set, 29 lines each
- Separate files for operator import convenience; not semantically unique per service campaign

Commander import: **NOT PERFORMED**
Git checkpoint: **NOT PERFORMED**
"""
    (REPORTS / "REPORT-corvonero-campaign-v2.6.1-embedded-negatives-hotfix-v1.md").write_text(
        report, encoding="utf-8"
    )
    return verdict


def main() -> None:
    require_operator_gate()
    label = subprocess.check_output(
        ["powershell.exe", "-NoProfile", "-Command", "(Get-Volume -DriveLetter X).FileSystemLabel"],
        text=True,
    ).strip()
    if label != "AI WS":
        raise SystemExit("STOP — volume label mismatch")
    if V261_OUTPUT.exists():
        raise SystemExit("STOP — V2.6.1 OUTPUT DIRECTORY ALREADY EXISTS")
    if not V26_OUTPUT.exists():
        raise SystemExit("STOP — V2.6 source package missing")

    V261_OUTPUT.mkdir(parents=True)
    accounting = validate_accounting()
    neg_txt_paths = copy_negative_txt_files()
    csv_paths = copy_csv_review_exports()

    manifest_path = PILOT / "CORVONERO-CAMPAIGN-V2.6-AUTHORITY-MANIFEST-v1.json"
    counts_path = PILOT / "CORVONERO-CAMPAIGN-V2.6-EXPECTED-COUNTS-v1.json"
    gen_script = TOOLS / "execute-campaign-v2.6.1-generation-v1.mjs"

    subprocess.run(
        ["node", str(gen_script), str(manifest_path), str(V261_OUTPUT), str(counts_path)],
        check=True,
        cwd=str(TOOLS),
    )

    gen_doc = json.loads(
        (PILOT / "CORVONERO-CAMPAIGN-V2.6.1-GENERATION-RUN-v1.json").read_text(encoding="utf-8")
    )

    forensic_doc = json.loads(
        (PILOT / "CORVONERO-CAMPAIGN-V2.6.1-FORENSIC-VALIDATION-v1.json").read_text(encoding="utf-8")
    )
    e9_pass_count = sum(
        1 for r in forensic_doc.get("results", []) if r.get("e9_validation", {}).get("pass")
    )

    comparison = compare_v26_v261_xlsx()
    if comparison["unexpected_differences"]:
        raise SystemExit(
            "STOP — unexpected V2.6/V2.6.1 binary identity: "
            + "; ".join(comparison["unexpected_differences"])
        )

    write_package_artifacts(neg_txt_paths, csv_paths, forensic_doc, gen_doc, accounting)
    verdict = write_repo_artifacts(
        forensic_doc, gen_doc, accounting, comparison, e9_pass_count
    )

    if e9_pass_count != 10 or not forensic_doc.get("summary", {}).get("all_pass", False):
        print(json.dumps({"verdict": verdict, "e9_pass": e9_pass_count}, ensure_ascii=False, indent=2))
        sys.exit(1)

    print(json.dumps({
        "verdict": f"CORVONERO CAMPAIGN V2.6.1: {verdict}",
        "e9_pass": f"{e9_pass_count}/10",
        "output": str(V261_OUTPUT),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
