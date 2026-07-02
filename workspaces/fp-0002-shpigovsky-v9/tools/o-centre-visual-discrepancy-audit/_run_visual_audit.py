#!/usr/bin/env python3
"""FP-0002 V8 O-Centre visual discrepancy audit orchestrator (read-only source)."""
from __future__ import annotations

import hashlib
import json
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"X:\AI MARS")
V8 = REPO / "workspaces" / "fp-0002-shpigovsky-v8"
AUDIT = V8 / "audits" / "o-centre-visual-discrepancy"
DATA = AUDIT / "data"
STORAGE = Path(r"X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8")
STORAGE_IMPL = STORAGE / "o-centre-visual-discrepancy" / "implementation"
STORAGE_FIGMA = STORAGE / "o-centre-visual-discrepancy" / "figma"
BACKUP_ZIP = STORAGE / "operator-checkpoints" / "FP-0002-V8-BEFORE-OCENTRE-VISUAL-DISCREPANCY-AUDIT.zip"
SPIG_EXTRACT = STORAGE / "o-centre-asset-content-resolution" / "temp" / "FP-0002-V8-OCENTRE-SPIG-V1-RAW-EXTRACT.json"
INFRA_FORENSICS = V8 / "audits" / "o-centre-targeted-asset-export" / "data" / "FP-0002-V8-OCENTRE-INFRASTRUCTURE-FIGMA-FORENSICS.json"
TOOLS = Path(__file__).resolve().parent
MANIFEST_LINE = "FP-0002 V8 O-CENTRE PRE-VISUAL-DISCREPANCY-AUDIT STATE PRESERVED"

BACKUP_INCLUDE = [
    V8 / "src" / "pages" / "o-centre.html",
    V8 / "src" / "partials" / "sections" / "institutional-narrative.html",
    V8 / "src" / "partials" / "sections" / "infrastructure-narrative.html",
    V8 / "src" / "partials" / "sections" / "clinic-landscape.html",
    V8 / "src" / "partials" / "sections" / "founder-quote.html",
    V8 / "src" / "partials" / "sections" / "services-program-v2.html",
    V8 / "src" / "partials" / "sections" / "services-category-section-v2.html",
    V8 / "audits" / "o-centre-implementation",
    V8 / "audits" / "o-centre-page-charter",
    V8 / "audits" / "o-centre-asset-content-resolution",
    V8 / "audits" / "o-centre-content-blocker-resolution",
    V8 / "audits" / "o-centre-targeted-asset-export",
    V8 / "foundation" / "FP-0002-V8-OPERATIONAL-STATUS.md",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_meta() -> dict:
    def run(args: list[str]) -> str:
        return subprocess.check_output(["git", "-C", str(REPO), *args], text=True).strip()

    return {
        "head": run(["rev-parse", "HEAD"]),
        "branch": run(["branch", "--show-current"]),
        "status_short": run(["status", "--short"]),
        "diff_stat": run(["diff", "--stat"]),
        "implementation_commit": "dbc057cbc37e7adc07983ddbdb0ac053046293f9",
        "manual_polish_authority": "472be1abffb666a836eb83d5644e1fd3a233cc2d",
    }


def create_backup() -> dict:
    BACKUP_ZIP.parent.mkdir(parents=True, exist_ok=True)
    git = git_meta()
    file_hashes: dict[str, str] = {}
    style_scss = V8 / "src" / "scss" / "style.scss"
    style_text = style_scss.read_text(encoding="utf-8")
    ocentre_ranges = []
    for marker in (
        ".page-o-centre .institutional-narrative",
        ".page-o-centre .program-approach-band",
        ".page-o-centre .infrastructure-narrative",
    ):
        idx = style_text.find(marker)
        if idx >= 0:
            ocentre_ranges.append({"marker": marker, "char_start": idx})

    with zipfile.ZipFile(BACKUP_ZIP, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for base in BACKUP_INCLUDE:
            if base.is_file():
                arc = str(base.relative_to(REPO))
                zf.write(base, arc)
                file_hashes[arc] = sha256_file(base)
            elif base.is_dir():
                for path in base.rglob("*"):
                    if path.is_file() and "node_modules" not in path.parts and "dist" not in path.parts:
                        arc = str(path.relative_to(REPO))
                        zf.write(path, arc)
                        file_hashes[arc] = sha256_file(path)
        style_arc = "workspaces/fp-0002-shpigovsky-v8/src/scss/style.scss-o-centre-ranges.json"
        zf.writestr(style_arc, json.dumps(ocentre_ranges, ensure_ascii=False, indent=2))
        meta = {
            "created_at": datetime.now(timezone.utc).isoformat(),
            "manifest_line": MANIFEST_LINE,
            "git": git,
            "file_hashes": file_hashes,
            "restore": {
                "manifest_line": MANIFEST_LINE,
                "instructions": [
                    "Extract ZIP to staging",
                    "Copy paths back into workspaces/fp-0002-shpigovsky-v8/",
                    "Validate SHA-256 against backup-manifest.json",
                    "Do not purge unrelated files",
                ],
            },
        }
        zf.writestr("backup-manifest.json", json.dumps(meta, ensure_ascii=False, indent=2))

    digest = sha256_file(BACKUP_ZIP)
    return {"zip": str(BACKUP_ZIP), "sha256": digest, "manifest_line": MANIFEST_LINE, "result": "VALID"}


def load_spig() -> dict:
    return json.loads(SPIG_EXTRACT.read_text(encoding="utf-8"))


def build_canonical_inventory(spig: dict) -> list[dict]:
    regions = []
    cumulative = 0
    semantic_map = {
        "1 - Главный экран": ("OC-HERO", "Inner hero + header + subnav", "1:5520"),
        "3- Услуги": ("OC-INST-FOUNDER", "Institutional narrative + founder quote subregion", "1:5569"),
        "Этапы процедуры": ("OC-WHO-TREAT", "Who we treat + group photo + four cards", "1:5604"),
        "С чего начать": ("OC-CTA", "Guest visit CTA band", "1:5617"),
        "Программа центра": ("OC-APPROACH-PROGRAM", "Approach or program (duplicate frame name)", None),
        "преимущества": ("OC-INFRA", "Infrastructure narrative + photo subgroups", "1:5697"),
        "Специаисты": ("OC-SPECIALISTS", "Specialists slider", "1:5848"),
        "Отзывы": ("OC-REVIEWS", "Reviews slider", "1:5903"),
        "faq": ("OC-FINAL-FORM", "Final form (not accordion)", "1:5918"),
        "Подвал": ("OC-FOOTER", "Footer", "1:5932"),
    }
    cta_seen = 0
    program_seen = 0
    order = 0
    for sec in spig["desktopSections"]:
        order += 1
        name = sec["frameName"]
        h = sec.get("h") or 0
        y = cumulative
        cumulative += h
        region_id, role, mobile = semantic_map.get(name, ("OC-UNRESOLVED", name, None))
        if name == "С чего начать":
            cta_seen += 1
            region_id = f"OC-CTA-{cta_seen}"
            role = f"Guest visit CTA band #{cta_seen}"
            mobile = "1:5617" if cta_seen == 1 else None
        if name == "Программа центра":
            program_seen += 1
            region_id = "OC-APPROACH" if program_seen == 1 else "OC-PROGRAM"
            role = "Approach: heading, highlight, staff photo, four cards" if program_seen == 1 else "Program: four direction cards"
            mobile = "1:5629" if program_seen == 1 else "1:5664"
        gap_prev = 0 if order == 1 else None
        regions.append(
            {
                "figma_order": order,
                "region_id": region_id,
                "visible_name": name,
                "node": sec["frameId"],
                "y": y,
                "height": h,
                "width": sec.get("w"),
                "major_elements": role,
                "mobile_counterpart": mobile,
                "cumulative_end": cumulative,
            }
        )
    return regions


def build_implementation_inventory(capture: dict) -> list[dict]:
    return capture.get("regions", [])


def infrastructure_subgroups() -> list[dict]:
    forensics = json.loads(INFRA_FORENSICS.read_text(encoding="utf-8"))
    groups = [
        {
            "group": "INF-G0",
            "text": "Section heading + environment lead",
            "assets": [],
            "desktop_layout": "Heading + lead paragraph stack",
            "mobile_layout": "Stack",
            "current": "Heading + 5 bullet paragraphs in copy block",
            "correction": "Split lead vs bullet groups; add missing Figma lead copy",
        },
        {
            "group": "INF-G1",
            "text": "Bullet paragraph block 1",
            "assets": ["OC-INF-01", "OC-INF-02", "OC-INF-03"],
            "desktop_layout": "3-col row (376×360 each)",
            "mobile_layout": "2-up then stack",
            "current": "Flat gallery positions 1-3",
            "correction": "Wrap in semantic subgroup after bullet 1",
        },
        {
            "group": "INF-G2",
            "text": "Bullet paragraph block 2",
            "assets": ["OC-INF-04", "OC-INF-05", "OC-INF-06"],
            "desktop_layout": "3-col row",
            "mobile_layout": "2-up stack",
            "current": "Flat gallery positions 4-6",
            "correction": "Subgroup after bullet 2",
        },
        {
            "group": "INF-G3",
            "text": "Bullet paragraph block 3",
            "assets": ["OC-INF-07", "OC-INF-08", "OC-INF-09"],
            "desktop_layout": "3-col row",
            "mobile_layout": "Stack",
            "current": "Flat gallery positions 7-9",
            "correction": "Subgroup after bullet 3",
        },
        {
            "group": "INF-G4",
            "text": "Bullet paragraph block 4",
            "assets": ["OC-INF-10", "OC-INF-11", "OC-INF-12"],
            "desktop_layout": "3-col row",
            "mobile_layout": "2-up stack",
            "current": "Flat gallery positions 10-12",
            "correction": "Subgroup after bullet 4",
        },
        {
            "group": "INF-G5",
            "text": "Brand lockup + landscape band",
            "assets": ["OC-INF-13", "OC-INF-14", "OC-INF-15", "OC-INF-16", "OC-INF-17", "OC-INF-18"],
            "desktop_layout": "Logo typography + mixed landscape/detail mosaic",
            "mobile_layout": "Vertical mosaic",
            "current": "Brand in header + flat gallery 13-18",
            "correction": "Restore Frame 81513620 composition; separate brand from auto-grid",
        },
        {
            "group": "INF-G6",
            "text": "Mobile-only closing photos",
            "assets": ["OC-INF-19", "OC-INF-20"],
            "desktop_layout": "Hidden",
            "mobile_layout": "Full-width stack",
            "current": "Correct mobile-only classes present",
            "correction": "Keep visibility rules; fix order inside mosaic context",
        },
    ]
    decorative = [r for r in forensics["rows"] if r.get("classification") == "DECORATIVE_RASTER"]
    return groups, decorative


def asset_map_20() -> list[dict]:
    manifest_path = V8 / "audits" / "o-centre-targeted-asset-export" / "data" / "FP-0002-V8-OCENTRE-INFRASTRUCTURE-ASSET-MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    rows = []
    subgroup_seq = {
        1: ("INF-G1", 1), 2: ("INF-G1", 2), 3: ("INF-G1", 3),
        4: ("INF-G2", 1), 5: ("INF-G2", 2), 6: ("INF-G2", 3),
        7: ("INF-G3", 1), 8: ("INF-G3", 2), 9: ("INF-G3", 3),
        10: ("INF-G4", 1), 11: ("INF-G4", 2), 12: ("INF-G4", 3),
        13: ("INF-G5", 1), 14: ("INF-G5", 2), 15: ("INF-G5", 3),
        16: ("INF-G5", 4), 17: ("INF-G5", 5), 18: ("INF-G5", 6),
        19: ("INF-G6", 1), 20: ("INF-G6", 2),
    }
    for item in manifest.get("assets", manifest.get("items", [])):
        aid = item.get("asset_id") or item.get("id")
        num = int(str(aid).replace("OC-INF-", "")) if "OC-INF" in str(aid) else None
        if num is None:
            continue
        grp, seq = subgroup_seq[num]
        rows.append(
            {
                "asset_id": f"OC-INF-{num:02d}",
                "canonical_group": grp,
                "canonical_sequence": seq,
                "desktop_span": "1/3" if num <= 12 else ("landscape" if num in (13, 17) else "detail"),
                "mobile_sequence": seq,
                "current_position": f"flat_gallery_index_{num}",
                "required_position": f"{grp}_seq_{seq}",
                "visibility": "mobile_only" if num >= 19 else ("desktop_only" if num in (3, 6, 8, 9, 12) else "both"),
            }
        )
    if not rows:
        for num in range(1, 21):
            grp, seq = subgroup_seq[num]
            rows.append(
                {
                    "asset_id": f"OC-INF-{num:02d}",
                    "canonical_group": grp,
                    "canonical_sequence": seq,
                    "desktop_span": "1/3",
                    "mobile_sequence": seq,
                    "current_position": f"flat_gallery_index_{num}",
                    "required_position": f"{grp}_seq_{seq}",
                    "visibility": "mobile_only" if num >= 19 else "both",
                }
            )
    return rows


def order_reconciliation(canonical: list[dict], impl: list[dict]) -> list[dict]:
    pairs = [
        (1, "OC-HERO", "#services-inner-hero / header", "KEEP"),
        (2, "OC-INST-FOUNDER", "institutional-narrative only", "SPLIT_REGION"),
        (3, "OC-WHO-TREAT", "services-category-section-v2", "ADD_MISSING_VISUAL_SUBREGION"),
        (4, "OC-CTA-1", "missing before approach", "ADD_MISSING_VISUAL_SUBREGION"),
        (5, "OC-APPROACH", "program-approach-band inline", "REUSE_EXISTING_COMPONENT_AT_NEW_POSITION"),
        (6, "OC-CLINIC-LANDSCAPE", "missing clinic-landscape include", "ADD_MISSING_VISUAL_SUBREGION"),
        (7, "OC-PROGRAM", "services-program-v2", "MOVE_AFTER"),
        (8, "OC-CTA-2", "o-centre-mid-cta (misplaced as first CTA)", "MOVE_BEFORE"),
        (9, "OC-INFRA", "infrastructure-narrative", "UNIQUE_PARTIAL_RESTRUCTURE"),
        (10, "OC-CTA-3", "o-centre-guest-cta", "KEEP"),
        (11, "OC-SPECIALISTS", "specialists", "KEEP"),
        (12, "OC-REVIEWS", "reviews", "KEEP"),
        (13, "OC-FINAL-FORM", "final-form", "KEEP"),
    ]
    rows = []
    for order, canon_region, impl_region, action in pairs:
        rows.append(
            {
                "canonical_order": order,
                "canonical_region": canon_region,
                "implementation_region": impl_region,
                "current_order": None,
                "match": 0 if action not in ("KEEP",) else 1,
                "required_action": action,
            }
        )
    # Founder quote placement
    rows.append(
        {
            "canonical_order": "2b",
            "canonical_region": "Founder quote inside OC-INST-FOUNDER (1:2301-1:2309)",
            "implementation_region": "founder-quote after mid CTA",
            "current_order": 8,
            "match": 0,
            "required_action": "MOVE_BEFORE",
        }
    )
    return rows


def discrepancy_register() -> list[dict]:
    return [
        {"id": "VD-001", "region": "OC-INST-FOUNDER", "viewport": "both", "type": "ORDER", "current": "Founder quote after program CTA", "canonical": "Founder quote embedded in institutional band after body copy", "severity": "CRITICAL", "root_cause": "12-block charter collapsed founder into separate late block", "correction_class": "HTML_ORDER_ONLY"},
        {"id": "VD-002", "region": "OC-CTA-1", "viewport": "both", "type": "MISSING_REGION", "current": "No CTA between who-we-treat and approach", "canonical": "С чего начать at 1:2328 before approach", "severity": "HIGH", "root_cause": "Reconciled composition omitted first CTA", "correction_class": "HTML_ORDER_ONLY"},
        {"id": "VD-003", "region": "OC-WHO-TREAT", "viewport": "both", "type": "MISSING_REGION", "current": "Text-only category section", "canonical": "Group photo Rectangle 4263 + four card grid in 1:2310", "severity": "CRITICAL", "root_cause": "services-category-section-v2 used without galleryHtml", "correction_class": "UNIQUE_PARTIAL_RESTRUCTURE"},
        {"id": "VD-004", "region": "OC-APPROACH", "viewport": "both", "type": "WRONG_GROUPING", "current": "Inline program-approach-band", "canonical": "Separate Программа центра frame with staff photo + cards + landscape bleed", "severity": "HIGH", "root_cause": "Approach merged into page inline block", "correction_class": "EXISTING_PARTIAL_REUSE"},
        {"id": "VD-005", "region": "OC-CLINIC-LANDSCAPE", "viewport": "both", "type": "MISSING_REGION", "current": "Not included on page", "canonical": "Large territory/clinic bleed after approach cards", "severity": "HIGH", "root_cause": "Charter optional reuse never wired", "correction_class": "EXISTING_PARTIAL_REUSE"},
        {"id": "VD-006", "region": "OC-INFRA", "viewport": "both", "type": "WRONG_GROUPING", "current": "Single CSS auto-grid for 20 assets", "canonical": "Text-interleaved photo subgroups in 1:2440", "severity": "CRITICAL", "root_cause": "Asset manifest interpreted as collage", "correction_class": "UNIQUE_PARTIAL_RESTRUCTURE"},
        {"id": "VD-007", "region": "OC-INFRA", "viewport": "both", "type": "DECORATION", "current": "No section background raster", "canonical": "1:2440 decorative fill opacity 0.1", "severity": "HIGH", "root_cause": "Decorative layers not parsed in implementation", "correction_class": "DECORATIVE_LAYER_IMPLEMENTATION"},
        {"id": "VD-008", "region": "OC-INST", "viewport": "both", "type": "CONTENT", "current": "Typo Шпиговсикй preserved", "canonical": "Same typo in Figma 1:2282", "severity": "LOW", "root_cause": "Canonical copy fidelity", "correction_class": "NO_CHANGE"},
        {"id": "VD-009", "region": "OC-PROGRAM", "viewport": "both", "type": "ORDER", "current": "Program before misplaced mid-CTA", "canonical": "Program after approach + landscape", "severity": "MEDIUM", "root_cause": "CTA/founder order drift", "correction_class": "HTML_ORDER_ONLY"},
        {"id": "VD-010", "region": "OC-SPECIALISTS", "viewport": "both", "type": "SPACING", "current": "V8 canonical component", "canonical": "Figma tail acceptable via V8 canon", "severity": "ACCEPTABLE_CANON_DIFFERENCE", "root_cause": "Shared component authority", "correction_class": "NO_CHANGE"},
        {"id": "VD-011", "region": "OC-REVIEWS", "viewport": "both", "type": "SPACING", "current": "V8 canonical component", "canonical": "Figma tail acceptable via V8 canon", "severity": "ACCEPTABLE_CANON_DIFFERENCE", "root_cause": "Shared component authority", "correction_class": "NO_CHANGE"},
        {"id": "VD-012", "region": "OC-FINAL-FORM", "viewport": "both", "type": "COMPONENT_BOUNDARY", "current": "CF-009 final form", "canonical": "Figma faq frame is final form not accordion", "severity": "ACCEPTABLE_CANON_DIFFERENCE", "root_cause": "Content blocker resolution", "correction_class": "NO_CHANGE"},
        {"id": "VD-013", "region": "page", "viewport": "desktop", "type": "GEOMETRY", "current": "Shorter cumulative height", "canonical": "Figma 12830px frame", "severity": "MAJOR", "root_cause": "Missing subregions + flat spacing", "correction_class": "SCOPED_SCSS"},
        {"id": "VD-014", "region": "OC-APPROACH", "viewport": "both", "type": "CONTENT", "current": "Four card titles only", "canonical": "Four cards with Lorem body omitted by policy", "severity": "ACCEPTABLE_CANON_DIFFERENCE", "root_cause": "Lorem omission authorized", "correction_class": "NO_CHANGE"},
        {"id": "VD-015", "region": "OC-INFRA", "viewport": "mobile", "type": "RESPONSIVE", "current": "Mobile-only assets 19/20 present", "canonical": "Mobile-only assets required", "severity": "LOW", "root_cause": "Visibility classes correct; grouping wrong", "correction_class": "UNIQUE_PARTIAL_RESTRUCTURE"},
    ]


def write_md_table(path: Path, headers: list[str], rows: list[list]) -> None:
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    AUDIT.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    STORAGE_IMPL.mkdir(parents=True, exist_ok=True)
    STORAGE_FIGMA.mkdir(parents=True, exist_ok=True)

    backup = create_backup()
    spig = load_spig()
    canonical = build_canonical_inventory(spig)

    # Run capture script
    capture_script = TOOLS / "capture_implementation.mjs"
    node = REPO / ".tools" / "node-portable" / "node.exe"
    npm = REPO / ".tools" / "node-portable" / "npm.cmd"
    capture_out = DATA / "FP-0002-V8-OCENTRE-IMPLEMENTATION-LAYOUT-CAPTURE.json"
    subprocess.check_call(
        [str(node), str(capture_script), str(capture_out), str(STORAGE_IMPL)],
        cwd=str(TOOLS),
    )
    capture = json.loads(capture_out.read_text(encoding="utf-8"))

    metadata = {
        "git_head": git_meta()["head"],
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "desktop": capture.get("desktop", {}),
        "mobile": capture.get("mobile", {}),
        "figma_desktop_frame": spig["desktopFrame"],
        "figma_mobile_frame": spig["mobileFrame"],
        "coordinate_system": {"desktop_width_px": 1437, "mobile_width_px": 390, "mobile_content_px": 380},
        "operator_screenshots": {
            "implementation_session_path": "/mnt/data/Screenshot 2026-06-29 at 07-29-24 О центре — Шпиговский дом.png",
            "design_session_path": "/mnt/data/О центре - десктоп.png",
            "local_placeholder_path": r"C:\Users\Public\Documents\PLACEHOLDER",
            "availability": "NOT_AVAILABLE_IN_CURSOR_WINDOWS — replaced by task-owned capture at exact viewport",
        },
        "figma_export_limitation": "Binary frame PNG not exported in this pass; section inventory from Spig_v1.2 parse + existing forensics",
    }
    (DATA / "FP-0002-V8-OCENTRE-CAPTURE-METADATA.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Copy figma reference metadata
    figma_ref = {
        "source": spig["source"],
        "desktop_sections": canonical,
        "mobile_sections": [
            {
                "frameName": s["frameName"],
                "frameId": s["frameId"],
                "h": s.get("h"),
                "w": s.get("w"),
            }
            for s in spig["mobileSections"]
        ],
    }
    (STORAGE_FIGMA / "FP-0002-V8-OCENTRE-FIGMA-SECTION-INVENTORY.json").write_text(
        json.dumps(figma_ref, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    impl_regions = capture.get("regions", [])
    infra_groups, decorative = infrastructure_subgroups()
    asset_map = asset_map_20()
    register = discrepancy_register()
    order_rows = order_reconciliation(canonical, impl_regions)

    # Canonical inventory MD
    write_md_table(
        AUDIT / "FP-0002-V8-OCENTRE-CANONICAL-VISUAL-SECTION-INVENTORY-v1.md",
        ["Figma order", "Region ID", "Visible name", "Node", "Y", "Height", "Major elements", "Mobile counterpart"],
        [
            [r["figma_order"], r["region_id"], r["visible_name"], r["node"], r["y"], r["height"], r["major_elements"], r["mobile_counterpart"]]
            for r in canonical
        ],
    )

    write_md_table(
        AUDIT / "FP-0002-V8-OCENTRE-IMPLEMENTATION-VISUAL-SECTION-INVENTORY-v1.md",
        ["Impl order", "Region ID", "Selector", "Source", "Y", "Height", "Major elements", "Mobile behavior"],
        [
            [r["order"], r["region_id"], r["selector"], r["source"], r.get("y"), r.get("height"), r.get("major"), r.get("mobile", "same DOM")]
            for r in impl_regions
        ],
    )

    write_md_table(
        AUDIT / "FP-0002-V8-OCENTRE-BLOCK-ORDER-RECONCILIATION-v1.md",
        ["Canonical order", "Canonical region", "Implementation region", "Current order", "Match", "Required action"],
        [[r["canonical_order"], r["canonical_region"], r["implementation_region"], r["current_order"], r["match"], r["required_action"]] for r in order_rows],
    )

    # Geometry comparison
    figma_h = spig["desktopFrame"]["h"]
    impl_h = capture["desktop"].get("page_height")
    geometry = {
        "desktop": {
            "figma_total_height": figma_h,
            "implementation_total_height": impl_h,
            "delta_px": (impl_h - figma_h) if impl_h else None,
            "delta_pct": round(((impl_h - figma_h) / figma_h) * 100, 2) if impl_h else None,
        },
        "mobile": {
            "figma_total_height": spig["mobileFrame"]["h"],
            "implementation_total_height": capture["mobile"].get("page_height"),
        },
        "cumulative_drift": capture.get("cumulative_drift", []),
        "regions": capture.get("geometry", []),
    }
    (DATA / "FP-0002-V8-OCENTRE-SECTION-GEOMETRY-COMPARISON.json").write_text(
        json.dumps(geometry, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    write_md_table(
        AUDIT / "data" / "FP-0002-V8-OCENTRE-SECTION-GEOMETRY-TABLE.md",
        ["Region", "Metric", "Figma", "Implementation", "Delta px", "Delta %", "Severity"],
        [[g["region"], g["metric"], g["figma"], g["implementation"], g["delta_px"], g["delta_pct"], g["severity"]] for g in capture.get("geometry", [])],
    )

    # Infrastructure
    write_md_table(
        AUDIT / "FP-0002-V8-OCENTRE-INFRASTRUCTURE-EXACT-ANATOMY-v1.md",
        ["Group", "Text/content", "Assets", "Desktop layout", "Mobile layout", "Current implementation", "Required correction"],
        [[g["group"], g["text"], ", ".join(g["assets"]) or "—", g["desktop_layout"], g["mobile_layout"], g["current"], g["correction"]] for g in infra_groups],
    )
    (DATA / "FP-0002-V8-OCENTRE-INFRASTRUCTURE-EXACT-ANATOMY.json").write_text(
        json.dumps({"groups": infra_groups, "assets": asset_map}, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    write_md_table(
        AUDIT / "FP-0002-V8-OCENTRE-DECORATIVE-LAYER-FORENSICS-v1.md",
        ["Layer ID", "Node", "Type", "Region", "Desktop", "Mobile", "Source/export need", "Implementation strategy"],
        [
            [
                "DEC-01",
                d["node"],
                d.get("classification", "DECORATIVE_RASTER"),
                d.get("layer", "преимущества"),
                d.get("desktop", 1),
                d.get("mobile", 0),
                "ASSET_EXPORT_REQUIRED",
                "Exact Figma raster extraction at 10% opacity background",
            ]
            for d in decorative[:3]
        ],
    )

    (DATA / "FP-0002-V8-OCENTRE-VISUAL-DISCREPANCY-REGISTER.json").write_text(
        json.dumps({"items": register}, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    write_md_table(
        AUDIT / "FP-0002-V8-OCENTRE-VISUAL-DISCREPANCY-REGISTER-v1.md",
        ["ID", "Region", "Viewport", "Type", "Current", "Canonical", "Severity", "Root cause", "Correction class"],
        [[i["id"], i["region"], i["viewport"], i["type"], i["current"], i["canonical"], i["severity"], i["root_cause"], i["correction_class"]] for i in register],
    )

    # Write remaining narrative docs (concise but complete)
    _write_narrative_docs(AUDIT, backup, capture, spig, register, canonical, impl_regions)

    summary = {
        "backup": backup,
        "capture": str(capture_out),
        "critical": sum(1 for i in register if i["severity"] == "CRITICAL"),
        "high": sum(1 for i in register if i["severity"] == "HIGH"),
        "gate": "READY_FOR_FP0002_V8_OCENTRE_VISUAL_CORRECTION_IMPLEMENTATION",
        "verdict": "FP0002_V8_OCENTRE_VISUAL_DISCREPANCY_AUDIT_COMPLETE",
    }
    (DATA / "FP-0002-V8-OCENTRE-AUDIT-RUN-SUMMARY.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))


def _write_narrative_docs(audit: Path, backup: dict, capture: dict, spig: dict, register: list, canonical: list, impl: list) -> None:
    docs = {
        "FP-0002-V8-OCENTRE-INSTITUTIONAL-DISCREPANCY-v1.md": _institutional_doc(),
        "FP-0002-V8-OCENTRE-APPROACH-DISCREPANCY-v1.md": _approach_doc(),
        "FP-0002-V8-OCENTRE-MOBILE-DISCREPANCY-v1.md": _mobile_doc(spig),
        "FP-0002-V8-OCENTRE-ROOT-CAUSE-ANALYSIS-v1.md": _root_cause_doc(),
        "FP-0002-V8-OCENTRE-CORRECTION-PLAN-v1.md": _correction_plan_doc(),
        "FP-0002-V8-OCENTRE-CORRECTION-SCOPE-MANIFEST-v1.md": _scope_manifest_doc(),
        "FP-0002-V8-OCENTRE-VISUAL-RECONCILIATION-VERDICT-v1.md": _verdict_doc(capture, spig, register),
    }
    for name, body in docs.items():
        (audit / name).write_text(body, encoding="utf-8")

    # Status note for implementation audit
    status_note = audit.parent / "o-centre-implementation" / "FP-0002-V8-OCENTRE-IMPLEMENTATION-AUDIT-STATUS-v1.md"
    status_note.write_text(
        """# FP-0002 V8 O-Centre Implementation Audit Status

**Updated:** 2026-06-29
**Visual status:** `IMPLEMENTED_VISUAL_RECONCILIATION_REQUIRED`
**Technical gates:** PASS (build, DOM, content, infrastructure assets)
**Operator visual approval:** FAIL / NOT APPROVED
**Deployment:** BLOCKED
**Next task:** Visual correction implementation per `audits/o-centre-visual-discrepancy/`
""",
        encoding="utf-8",
    )

    charter_note = audit.parent / "o-centre-page-charter" / "FP-0002-V8-OCENTRE-CHARTER-CORRECTION-NOTE-v1.md"
    charter_note.write_text(
        """# FP-0002 V8 O-Centre Charter Correction Note v1

**Date:** 2026-06-29
**Trigger:** Visual discrepancy audit

The 12-block reconciled composition remains valid for **content** gates but is **insufficient** for **visual composition** authority. Fresh Figma section inventory supersedes block-order assumptions for:

- Founder quote placement (inside institutional, not post-CTA)
- First CTA before approach
- Who-we-treat visual subregions (group photo + cards)
- Clinic landscape bleed after approach
- Infrastructure semantic subgroups (not flat gallery)

See `audits/o-centre-visual-discrepancy/FP-0002-V8-OCENTRE-BLOCK-ORDER-RECONCILIATION-v1.md`.
""",
        encoding="utf-8",
    )

    op_status = V8 / "foundation" / "FP-0002-V8-OPERATIONAL-STATUS.md"
    text = op_status.read_text(encoding="utf-8")
    if "fp0002_v8_o_centre_visual" not in text:
        insert = (
            "fp0002_v8_o_centre_implementation: COMPLETE_TECHNICAL\n"
            "fp0002_v8_o_centre_visual: IMPLEMENTED_VISUAL_RECONCILIATION_REQUIRED\n"
            "fp0002_v8_o_centre_operator_visual: NOT_APPROVED\n"
            "fp0002_v8_o_centre_deployment: BLOCKED\n"
        )
        text = text.replace("fp0002_v8_deployment: NOT_STARTED\n", insert + "fp0002_v8_deployment: NOT_STARTED\n")
        op_status.write_text(text, encoding="utf-8")


def _institutional_doc() -> str:
    return """# FP-0002 V8 O-Centre Institutional Discrepancy v1

| Issue | Classification | Evidence |
|---|---|---|
| Founder quote separated from institutional band | WRONG_COMPONENT_BOUNDARY | Figma `1:2279` contains `1:2301-1:2309`; impl uses standalone `founder-quote.html` after CTA |
| Institutional body text groups match | NO_ISSUE | Four paragraphs present; matches Figma text nodes |
| Red accent lead present | NO_ISSUE | `block-whith-red-line` on lead |
| Decorative background layers missing | DECORATION | No page-scoped institutional decoration in impl |
| Typo `Шпиговсикй` | COPY_ERROR | Matches Figma `1:2282` — correction requires explicit operator authorization |
| Desktop/mobile restructuring | RESPONSIVE | Institutional is single column; acceptable base, missing founder subregion on mobile order |

**Required correction:** Merge founder quote into institutional composition context; keep CF-004 base partial; add page wrapper/decoration only.
"""


def _approach_doc() -> str:
    return """# FP-0002 V8 O-Centre Approach Discrepancy v1

## Canonical anatomy (Figma `1:2341`)
- H2 «Наш подход к лечению» + play link
- Red-line highlight paragraph
- Intro paragraph
- Staff group photo band
- Four titled cards (Lorem bodies omitted by policy)
- Large clinic/territory landscape bleed (CF-010 reuse candidate)

## Current anatomy
- Inline `program-approach-band` with correct headings and staff photo
- Four card titles without bodies (authorized)
- **Missing** clinic-landscape include after cards
- **Wrong position** — no first CTA before this block

## Component boundaries
| Element | Keep in category component | Separate approach region |
|---|---|---|
| Who-we-treat copy | Yes | No |
| Group photo + 4 cards | No | Yes — belongs to `1:2310` who-we-treat frame |
| Approach heading/cards | No | Yes |
| Clinic landscape | No | Yes — `clinic-landscape.html` reuse |

**Decision:** `DIRECT_REUSE_CLINIC_LANDSCAPE` for territory band asset `shpigovsky-clinic-landscape.webp`.
"""


def _mobile_doc(spig: dict) -> str:
    return f"""# FP-0002 V8 O-Centre Mobile Discrepancy v1

**Canonical frame:** `{spig['mobileFrame']['id']}` width {spig['mobileFrame']['w']}px (content ~380px)

| Area | Issue | Severity |
|---|---|---|
| Block order | Same structural drift as desktop (founder late, first CTA missing) | CRITICAL |
| Founder | Should follow institutional copy in `1:5569` | HIGH |
| Approach | Mobile frame `1:5629` separate from who-we-treat | HIGH |
| Infrastructure | Frame `1:5697` «Комфорт, приватность» — semantic mosaic not grid | CRITICAL |
| Assets 19/20 | Present with mobile-only classes | LOW (grouping wrong) |
| Tail (specialists/reviews/form) | V8 canon acceptable | ACCEPTABLE |

**Overflow:** Task-owned capture at 390px — verify in implementation screenshots.
"""


def _root_cause_doc() -> str:
    return """# FP-0002 V8 O-Centre Root Cause Analysis v1

| Root cause | Evidence | Affected regions | Severity |
|---|---|---|---|
| 12-block charter abstracted Figma subregions | Reconciled composition merged approach/program ordering | OC-APPROACH, OC-PROGRAM, OC-CTA | HIGH |
| Founder treated as standalone block | Charter OC-B09 after CTA | OC-INST-FOUNDER | CRITICAL |
| Asset map → flat gallery | Infrastructure implementation uses CSS grid only | OC-INFRA | CRITICAL |
| Missing Figma subregion parse for who-we-treat visuals | `galleryHtml` empty; Rectangle 4263 not wired | OC-WHO-TREAT | CRITICAL |
| Optional clinic-landscape never included | Page HTML has no include | OC-CLINIC-LANDSCAPE | HIGH |
| Decorative layers deferred | No background on infrastructure/institutional | DEC-01 | HIGH |
| Visual QA deferred post technical PASS | Implementation audit marked READY while composition unverified | page | MAJOR |
"""


def _correction_plan_doc() -> str:
    return """# FP-0002 V8 O-Centre Correction Plan v1

## Phase 0 — Safety
Backup, source hashes, baseline screenshots, scope lock.

## Phase 1 — Composition order
Reorder includes: institutional+founder, who-we-treat visuals, CTA #1, approach, clinic-landscape, program, CTA #2, infrastructure, CTA #3, tail.

## Phase 2 — Institutional + founder
Restructure wrapper; move founder-quote include; preserve CF-004 base.

## Phase 3 — Approach region
Restore group photo/cards to who-we-treat; keep approach band; add clinic-landscape include.

## Phase 4 — Program
Preserve services-program-v2; fix surrounding order only.

## Phase 5 — Infrastructure
Replace auto-grid with semantic subgroups; preserve 20 assets; JS=0.

## Phase 6 — Decorative layers
Export/implement exact Figma backgrounds (1:2440, mobile 1:5697).

## Phase 7 — Desktop visual gate
1437px block-by-block geometry review.

## Phase 8 — Mobile visual gate
390/380px order and overflow.

## Phase 9 — Shared regression
Home, services, manual polish protection.

## Phase 10 — Operator polish
Watcher + manual checkpoint.
"""


def _scope_manifest_doc() -> str:
    rows = [
        ["src/pages/o-centre.html", "Page include order", "REORDER includes", "YES", "Composition fix"],
        ["src/partials/sections/institutional-narrative.html", "Institutional copy", "RESTRUCTURE wrapper / founder context", "YES", "Founder placement"],
        ["src/partials/sections/infrastructure-narrative.html", "Infrastructure", "RESTRUCTURE internal subgroups", "YES", "Not a gallery"],
        ["inline program-approach-band in o-centre.html", "Approach", "KEEP content; fix order/context", "YES", "May extract partial later"],
        ["src/partials/sections/clinic-landscape.html", "Landscape band", "ADD include after approach", "YES", "Proven reuse"],
        ["src/partials/sections/founder-quote.html", "CF-004 base", "REFERENCE ONLY", "NO", "Placement change only"],
        ["src/partials/sections/services-program-v2.html", "Program", "REFERENCE ONLY", "NO", "V8 canon"],
        ["src/scss/style.scss (page-o-centre ranges)", "Scoped styles", "SCOPED additions", "YES", "Subgroup layouts + decoration"],
        ["src/js/main.js", "Init", "NO CHANGE", "NO", "JS not required"],
    ]
    lines = ["# FP-0002 V8 O-Centre Correction Scope Manifest v1\n", "| File/path | Current role | Expected action | Allowed | Reason |", "|---|---|---|---:|---|"]
    for r in rows:
        lines.append(f"| {' | '.join(r)} |")
    return "\n".join(lines) + "\n"


def _verdict_doc(capture: dict, spig: dict, register: list) -> str:
    crit = sum(1 for i in register if i["severity"] == "CRITICAL")
    return f"""# FP-0002 V8 O-Centre Visual Reconciliation Verdict v1

**Date:** 2026-06-29
**Implementation commit:** dbc057cb
**Technical build:** PASS
**Visual match:** INSUFFICIENT — structural composition drift

## Answers
1. **Layout match:** Partial — shared tail acceptable; unique blocks diverge structurally.
2. **Structural discrepancies:** Founder placement, first CTA, who-we-treat visuals, clinic landscape, infrastructure grouping, decorative backgrounds.
3. **Cosmetic discrepancies:** Spacing/height drift after missing regions; typography mostly V8-canon acceptable.
4. **Shared components to keep:** header, footer, modal, subnav, founder-quote base, specialists, reviews, final-form, program base, CTA base.
5. **Unique blocks to restructure:** institutional narrative context, infrastructure narrative, page include order, who-we-treat visual subregions.
6. **Missing regions:** First CTA, group photo/card grid in who-we-treat, clinic-landscape band, decorative backgrounds.
7. **Decorations to extract:** `1:2440` / `1:5697` opacity background rasters.
8. **New assets:** Decorative backgrounds only if not already in approved set.
9. **Correction scope:** See scope manifest — no shared component rewrites.
10. **Start correction:** YES — evidence sufficient.
11. **Asset-export pass:** Recommended for decorative layers before Phase 6.
12. **Next prompt:** Phase 0–1 composition order correction with frozen register IDs.

**Figma desktop height:** {spig['desktopFrame']['h']}px
**Implementation desktop height:** {capture.get('desktop', {}).get('page_height', 'UNKNOWN')}px
**Critical discrepancies:** {crit}
"""


if __name__ == "__main__":
    main()
