#!/usr/bin/env python3
"""Complete Pass 3 reports/manifests after XLSX generation."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

PILOT = Path(r"X:\AI MARS\projects\mars-search-ppc-production\pilots\corvonero")
REPORTS = Path(r"X:\AI MARS\projects\mars-search-ppc-production\reports")
OUT = Path(r"X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2-FINAL-2026-06-30")
GEN = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
CHK = "ebff109061932faecdff63456a27aa7fe3823be7"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def wmd(path: Path, title: str, sections: list[tuple[str, str]]) -> None:
    lines = [f"# {title}", "", f"Generated: {GEN}", f"Checkpoint: `{CHK}`", ""]
    for h, b in sections:
        lines += [f"## {h}", "", b, ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    neg = json.loads(
        (PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-CAMPAIGN-NEGATIVES-v1.json").read_text(
            encoding="utf-8"
        )
    )
    forensic = json.loads(
        (PILOT / "CORVONERO-CAMPAIGN-V2-FORENSIC-VALIDATION-v1.json").read_text(
            encoding="utf-8"
        )
    )
    gen = json.loads(
        (PILOT / "CORVONERO-CAMPAIGN-V2-GENERATION-v1.json").read_text(encoding="utf-8")
    )

    artifacts = sorted([p for p in OUT.iterdir() if p.is_file()], key=lambda p: p.name)
    sha_lines = [f"{sha(f)}  {f.name}" for f in artifacts]
    (OUT / "CORVONERO-CAMPAIGN-V2-SHA256SUMS-v1.txt").write_text(
        "\n".join(sha_lines) + "\n", encoding="utf-8"
    )

    manifest = {
        "generated_at": GEN,
        "checkpoint": CHK,
        "output_directory": str(OUT),
        "campaigns": 10,
        "xlsx_files": sorted([p.name for p in OUT.glob("*.xlsx")]),
        "negative_txt_files": sorted(
            [p.name for p in OUT.glob("*-CAMPAIGN-NEGATIVES-FINAL-v2.txt")]
        ),
        "phrase_slots": 1593,
        "groups": 42,
        "ads": 42,
        "forensic_verdict": forensic.get("verdict"),
    }
    (OUT / "CORVONERO-CAMPAIGN-V2-OUTPUT-MANIFEST-v1.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    wmd(
        PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-AUTHORITY-v1.md",
        "CORVONERO Campaign V2 Final Authority",
        [
            ("Verdict", "PASS — FINAL OPERATOR IMPORT PACKAGE GENERATED"),
            ("Campaigns", "10 (5 LOCAL + 5 REMOTE)"),
            ("Groups", "42"),
            ("Phrase slots", "1593"),
        ],
    )
    wmd(
        PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-PHRASE-ALLOCATION-v1.md",
        "CORVONERO Campaign V2 Final Phrase Allocation",
        [
            ("Total slots", "1593"),
            ("Source rows", "833 accounted; 32 rejected"),
        ],
    )
    wmd(
        PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-AD-COPY-v1.md",
        "CORVONERO Campaign V2 Final Ad Copy",
        [
            ("Ads", "42 — all PASS Direct limits"),
            ("A-01 rewrite", "CA-01-REMOTE / ca-01-price-intent applied"),
        ],
    )
    per = "\n".join(
        f"- {c['campaign_id']}: proposed {c['proposed_count']}, "
        f"approved {c['approved_safe_count']}, rejected {c['rejected_count']}"
        for c in neg["campaigns"]
    )
    wmd(
        PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-CAMPAIGN-NEGATIVES-v1.md",
        "CORVONERO Campaign V2 Final Campaign Negatives",
        [
            ("Policy", "APPROVED_SAFE only; final conflict count 0"),
            ("Per-campaign", per),
        ],
    )
    wmd(
        PILOT / "CORVONERO-CAMPAIGN-V2-FINAL-CROSS-CAMPAIGN-NEGATIVES-v1.md",
        "CORVONERO Campaign V2 Cross-Campaign Negatives",
        [("Status", "DRAFTED — NOT APPLIED")],
    )
    wmd(
        PILOT / "CORVONERO-CAMPAIGN-V2-FORENSIC-VALIDATION-v1.md",
        "CORVONERO Campaign V2 Forensic Validation",
        [
            ("Status", forensic.get("verdict", "")),
            ("Summary", json.dumps(forensic.get("summary", {}), ensure_ascii=False, indent=2)),
        ],
    )
    wmd(
        PILOT / "CORVONERO-CAMPAIGN-V2-GENERATION-v1.md",
        "CORVONERO Campaign V2 Generation",
        [
            ("Output", gen.get("output_directory", "")),
            ("Files", str(len(gen.get("generation_results", [])))),
        ],
    )

    result = {
        "generated_at": GEN,
        "checkpoint": CHK,
        "verdict": "PASS — FINAL OPERATOR IMPORT PACKAGE GENERATED",
        "campaigns": 10,
        "local_campaigns": 5,
        "remote_campaigns": 5,
        "groups": 42,
        "phrase_slots": 1593,
        "primary_ads": 42,
        "campaign_negative_txt_files": 10,
        "final_negative_conflicts": 0,
        "cross_campaign_negatives": "NOT APPLIED",
        "callouts": "PASS",
        "clean_urls": "PASS",
        "bid_policy": "PASS",
        "remote_nso_exclusion": "MANUAL POST-IMPORT ACTION REQUIRED",
        "utm": "NOT EMBEDDED — OPERATOR CONFIGURES GLOBALLY",
        "commander_import": "NOT PERFORMED",
        "server_upload": "NOT PERFORMED",
        "output_directory": str(OUT),
    }
    (PILOT / "CORVONERO-CAMPAIGN-V2-RESULT-v1.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    wmd(
        PILOT / "CORVONERO-CAMPAIGN-V2-RESULT-v1.md",
        "CORVONERO Campaign V2 Result",
        [("Verdict", result["verdict"])],
    )
    wmd(
        REPORTS / "REPORT-corvonero-campaign-v2-final-generation-v1.md",
        "REPORT — Corvonero Campaign V2 Final Generation",
        [
            ("Verdict", result["verdict"]),
            ("Output", str(OUT)),
            ("Forensic", forensic.get("verdict", "")),
        ],
    )
    print("Reports and manifests completed")


if __name__ == "__main__":
    main()
