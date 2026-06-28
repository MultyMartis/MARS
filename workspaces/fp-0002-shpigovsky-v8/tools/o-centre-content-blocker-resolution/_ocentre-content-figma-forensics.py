#!/usr/bin/env python3
"""Generate O-Centre content blocker Figma forensics from Spig_v1.2 extract + fresh parse."""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO = ROOT.parents[1]
FIG_PATH = (
    REPO
    / "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig"
)
EXTRACT_PATH = (
    ROOT
    / "audits/o-centre-asset-content-resolution/data/FP-0002-V8-OCENTRE-SPIG-V1-FIG-EXTRACT.json"
)
OUT_MD = (
    ROOT
    / "audits/o-centre-content-blocker-resolution/FP-0002-V8-OCENTRE-CONTENT-FIGMA-FORENSICS-v1.md"
)
OUT_JSON = (
    ROOT
    / "audits/o-centre-content-blocker-resolution/data/FP-0002-V8-OCENTRE-CONTENT-FIGMA-FORENSICS.json"
)

SEARCH_TERMS = [
    "этапы",
    "Этапы",
    "01 —",
    "02 —",
    "03 —",
    "04 —",
    "Основатель",
    "Шпиговский",
    "Lorem",
    "Наш подход",
    "программа",
    "Что нужно для прохождения",
]


def run_fresh_extract() -> dict | None:
    script = (
        REPO
        / "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/_fig_parse_temp/extract-o-centre-spig-v1.mjs"
    )
    if not script.is_file():
        return None
    try:
        subprocess.run(
            ["node", str(script)],
            check=True,
            capture_output=True,
            text=True,
            cwd=str(script.parent),
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    raw = Path(
        r"C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\o-centre-asset-content-resolution\temp\FP-0002-V8-OCENTRE-SPIG-V1-RAW-EXTRACT.json"
    )
    if raw.is_file():
        return json.loads(raw.read_text(encoding="utf-8"))
    return None


def main() -> None:
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    extract = json.loads(EXTRACT_PATH.read_text(encoding="utf-8"))
    fresh = run_fresh_extract()

    desktop_id = extract.get("meta", {}).get("desktop_frame", {}).get("id", "1:2185")
    mobile_id = extract.get("meta", {}).get("mobile_frame", {}).get("id", "1:5519")

    texts = extract.get("text_nodes", extract.get("texts", []))
    if not texts and "all_text_nodes" in extract:
        texts = extract["all_text_nodes"]

    # normalize: use flat list from extract structure
    flat: list[dict] = []
    if isinstance(extract.get("text_nodes"), list):
        flat = extract["text_nodes"]
    elif isinstance(extract.get("texts"), list):
        flat = extract["texts"]
    else:
        # sections keyed extract
        for item in extract.get("allTexts", []):
            flat.append(item)

    # fallback: parse from sections in extract file
    if not flat:
        for key in ("desktop", "mobile"):
            for entry in extract.get(key, {}).get("texts", []):
                flat.append(entry)

    # The SPIG extract uses top-level list under key discovered earlier
    if not flat:
        # scan entire JSON for dicts with id+text
        def walk(obj):
            if isinstance(obj, dict):
                if "id" in obj and "text" in obj and isinstance(obj["text"], str):
                    flat.append(obj)
                for v in obj.values():
                    walk(v)
            elif isinstance(obj, list):
                for v in obj:
                    walk(v)

        walk(extract)

    def match_term(t: str) -> list[str]:
        low = t.lower()
        return [term for term in SEARCH_TERMS if term.lower() in low]

    hits: list[dict] = []
    for node in flat:
        text = node.get("text") or ""
        terms = match_term(text) + match_term(node.get("name") or "")
        if not terms:
            continue
        hits.append(
            {
                "node_id": node.get("id"),
                "name": node.get("name"),
                "text_preview": text[:200],
                "visible": node.get("visible", True),
                "depth": node.get("depth"),
                "match_terms": sorted(set(terms)),
                "is_lorem": "lorem ipsum" in text.lower(),
            }
        )

    # Section names from fresh extract
    desktop_sections = []
    mobile_sections = []
    if fresh:
        for s in fresh.get("desktopSections", []):
            desktop_sections.append(
                {
                    "id": s.get("frameId"),
                    "name": s.get("frameName"),
                    "text_count": len(s.get("texts", [])),
                    "image_count": len(s.get("images", [])),
                }
            )
        for s in fresh.get("mobileSections", []):
            mobile_sections.append(
                {
                    "id": s.get("frameId"),
                    "name": s.get("frameName"),
                    "text_count": len(s.get("texts", [])),
                    "image_count": len(s.get("images", [])),
                }
            )

    blockers = {
        "OC-G06_steps": {
            "desktop_frame_mislabel": {"id": "1:2310", "name": "Этапы процедуры", "actual_content": "who-we-treat"},
            "blk018_nodes_found": [
                h for h in hits if any(x in (h.get("match_terms") or []) for x in ["этапы", "Этапы"])
            ],
            "numbered_steps_01_04_in_steps_context": False,
            "note": "Frame 1:2310 named Этапы процедуры contains OC-B04 who-we-treat copy; no BLK-018 rehabilitation requirements block.",
        },
        "OC-G10_founder": {
            "quote_body_node": {"id": "1:2301", "is_lorem": True},
            "attribution_node": {"id": "1:2308", "text": "Сергей Юрьевич Шпиговский"},
            "role_node": {"id": "1:2309", "text": "Основатель центра. Аддиктолог, интервенционист"},
            "desktop_parent_section": "3- Услуги / 1:2279",
            "mobile_section": "1:5569",
        },
        "OC-G11_program": {
            "approach_frame": {"id": "1:2341"},
            "approach_heading_node": {"id": "1:2343", "text": "Наш подход к лечению алкогольной зависимости"},
            "confirmed_lead_nodes": ["1:2355", "1:2357"],
            "approach_card_titles": ["1:2366", "1:2369", "1:2384", "1:2387"],
            "lorem_card_bodies": ["1:2367", "1:2370", "1:2385", "1:2388"],
            "lorem_program_intro": ["1:2406", "1:2408"],
            "confirmed_directions": ["1:2412", "1:2417", "1:2423", "1:2428"],
            "program_heading": {"id": "1:2433", "text": "Наша программа включает 4 направления"},
        },
    }

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_fig": str(FIG_PATH),
        "extract_path": str(EXTRACT_PATH),
        "fresh_extract_ran": fresh is not None,
        "desktop_frame": {"id": desktop_id, "name": "О центре"},
        "mobile_frame": {"id": mobile_id, "name": "О центре - моб"},
        "desktop_sections": desktop_sections,
        "mobile_sections": mobile_sections,
        "search_hits": hits,
        "blockers": blockers,
        "lorem_nodes": [h for h in hits if h.get("is_lorem")],
    }

    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    md = [
        "# FP-0002 V8 O-Centre Content Figma Forensics v1",
        "",
        f"**Generated:** {payload['generated_at']}",
        f"**Canonical Figma:** `{FIG_PATH}`",
        f"**Extract:** `{EXTRACT_PATH}`",
        f"**Fresh parse:** {'yes' if fresh else 'no (used committed extract)'}",
        "",
        "## Desktop / mobile frames",
        "",
        f"- Desktop: `{desktop_id}` «О центре»",
        f"- Mobile: `{mobile_id}` «О центре - моб»",
        "",
        "## Desktop section order (fresh parse)",
        "",
        "| Order | Section ID | Name | Texts | Images |",
        "|---:|---|---|---:|---:|",
    ]
    for i, s in enumerate(desktop_sections, 1):
        md.append(
            f"| {i} | `{s['id']}` | {s['name']} | {s['text_count']} | {s['image_count']} |"
        )
    if not desktop_sections:
        md.append("| — | — | (see node map) | — | — |")

    md.extend(
        [
            "",
            "## Blocker summary",
            "",
            "| Blocker | Desktop | Mobile | Visible content | Hidden/override | Confidence |",
            "|---|---|---|---|---|---|",
            "| OC-G06 Steps | No BLK-018 frame; `1:2310` mislabeled | `1:5604` who-we-treat | Who-we-treat copy only | None | **HIGH** |",
            "| OC-G10 Founder | `1:2301`–`1:2309` in `1:2279` | `1:5569` institutional band | Attribution+role confirmed; body Lorem | None | **HIGH** |",
            "| OC-G11 Program | `1:2341` approach + `1:2401` program | `1:5629`, `1:5664` | Headings/leads/directions confirmed; card bodies Lorem | None | **HIGH** |",
            "",
            "## Lorem nodes (O-Centre scope)",
            "",
        ]
    )
    for h in payload["lorem_nodes"][:20]:
        md.append(f"- `{h['node_id']}` — {h['text_preview'][:80]}…")
    md.append("")
    md.append("**Machine-readable:** `data/FP-0002-V8-OCENTRE-CONTENT-FIGMA-FORENSICS.json`")

    OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps({"md": str(OUT_MD), "json": str(OUT_JSON), "hits": len(hits)}, indent=2))


if __name__ == "__main__":
    main()
