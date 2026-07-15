#!/usr/bin/env python3
"""Generate E13 architecture markdown docs. NOT FOR GIT."""
from pathlib import Path

ROOT = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS")
ARCH = ROOT / "architecture"

docs = {
    "FP-0002-V9-06E13-BASELINE-BEFORE-REPAIR-v1.md": """# FP-0002 V9-06E13 — Baseline Before Repair

**Wave:** V9-06E13 Alcohol Leaf Specialists Block V9 Parity Repair  
**Date:** 2026-07-07

## Operator evidence

Operator screenshot after E12 shows oversized specialists cards on `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`. Screenshot available in Web-GPT chat only (`Screenshot 2026-07-07 at 05-03-51`).

## Technical baseline

| Check | Before E13 | Notes |
|---|---|---|
| Renderer | `template-parts/home/specialists.php` | HOME_PARTIAL_REUSE via alcohol-direct-v9.php |
| Swiper JS | **false** | `home-vendors.php` gates on `is_front_page()` |
| Swiper CSS | **false** | Same gate |
| Card count | 5 | Markup matched static V9 |
| Slider init | **broken** | v9-shell specialists boot requires `window.Swiper` |
| Root cause | Missing vendor on service leaf | Cards render at unconstrained width |

## Screenshots captured

- `runtime-alcohol-specialists-before-e13.png`
- `runtime-full-alcohol-leaf-before-e13.png`
- `static-v9-alcohol-specialists-reference-e13-before.png`
- `static-v9-full-alcohol-leaf-reference-e13-before.png`
""",
    "FP-0002-V9-06E13-STATIC-V9-SPECIALISTS-BLOCK-EXTRACTION-CONTRACT-v1.md": """# FP-0002 V9-06E13 — Static V9 Specialists Block Extraction Contract

**Authority:** `workspaces/fp-0002-shpigovsky-v9/src/partials/sections/specialists.html`  
**Page include:** `usluga-konechnaya-v1.html` order 12

| Item | Static V9 value |
|---|---|
| Section root class | `specialists` |
| Section ID | `service-leaf-specialists` |
| Heading ID | `service-leaf-specialists-heading` |
| Heading text | Специалисты центра |
| Modifier class | (empty) |
| List wrapper | `specialists__slider swiper` + `data-specialists-slider` |
| Card wrapper | `specialists__card swiper-slide` |
| Image class | `specialists__photo` |
| Image height (CSS) | 260px, object-fit cover |
| Card count | 5 |
| Swiper config | slidesPerView 3.5 / breakpoints 1.35–3.5 |
| Content | EXACT_V9_COPY (fixture staff list) |
""",
    "FP-0002-V9-06E13-CURRENT-WP-SPECIALISTS-PROVENANCE-AUDIT-v1.md": """# FP-0002 V9-06E13 — Current WP Specialists Provenance Audit

| Component | Role | Provenance | Risk |
|---|---|---|---|
| `alcohol-direct-v9.php` | Stack orchestrator | HOME_PARTIAL_REUSE | HIGH |
| `home/specialists.php` | Block renderer | HOME_PARTIAL_REUSE | HIGH |
| `home-vendors.php` | Swiper enqueue | front-page-only gate | **CRITICAL** |
| `v9-shell.js` | Slider init | DIRECT_V9_PORT (neutral) | LOW when Swiper missing |

## Root cause

Markup was structurally identical to static V9, but **Swiper vendor was not enqueued** on alcohol leaf. Without Swiper, `data-specialists-slider` cards display at full intrinsic image width — operator-observed oversized photos.
""",
    "FP-0002-V9-06E13-SPECIALISTS-BLOCK-GAP-MATRIX-v1.md": """# FP-0002 V9-06E13 — Specialists Block Gap Matrix

| Area | Static V9 | WP before | Gap | Repair |
|---|---|---|---|---|
| Renderer | `partials/sections/specialists.html` | `home/specialists.php` | WRONG_CONTENT_SOURCE | `alcohol-direct-v9/specialists.php` |
| Swiper vendor | loaded | missing | WRONG_LAYOUT_MODE | `alcohol-direct-v9-vendors.php` |
| Card sizing | 3.5-slide grid | full-width stretch | WRONG_SIZE | Swiper init |
| Section ID | `service-leaf-specialists` | match | MATCH | — |
| Inner markup | `specialists__*` | match | MATCH | — |
""",
    "FP-0002-V9-06E13-REPAIR-PLAN-v1.md": """# FP-0002 V9-06E13 — Repair Plan

1. **Renderer:** `template-parts/service/alcohol-direct-v9/specialists.php` — exact static V9 block; bypass `home/specialists.php`.
2. **Data:** `shpigovsky_get_v9_specialists_cards()` in `v9-static-content.php`.
3. **Vendor:** `inc/alcohol-direct-v9-vendors.php` — enqueue Swiper on `alcohol-special` variant only.
4. **Orchestrator:** Update `alcohol-direct-v9.php` to call new partial.
5. **Bootstrap:** `functions.php` requires new vendor file.
6. **CSS:** none (existing `specialists__photo` height 260px sufficient once Swiper active).
7. **Regression:** home specialists unchanged; 9 regression routes.
""",
    "FP-0002-V9-06E13-SPECIALISTS-BLOCK-DIRECT-V9-REPAIR-v1.md": """# FP-0002 V9-06E13 — Specialists Block Direct V9 Repair

| Area | Before | After | Result |
|---|---|---|---|
| Renderer | `home/specialists.php` | `alcohol-direct-v9/specialists.php` | PASS |
| Home partial reuse | YES | REMOVED | PASS |
| Swiper JS | false | true | PASS |
| Swiper CSS | false | true | PASS |
| Section class | `specialists` | `specialists` | PASS |
| Card count | 5 | 5 | PASS |
| Content source | inline home fixture | `shpigovsky_get_v9_specialists_cards()` | PASS |
""",
    "FP-0002-V9-06E13-FINAL-ALCOHOL-SPECIALISTS-BLOCK-CONTRACT-v1.md": """# FP-0002 V9-06E13 — Final Alcohol Specialists Block Contract

| Item | Final state |
|---|---|
| Route | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` |
| Static source | `partials/sections/specialists.html` |
| WP renderer | `template-parts/service/alcohol-direct-v9/specialists.php` |
| Vendor | `inc/alcohol-direct-v9-vendors.php` |
| Markup | EXACT_V9_COPY |
| Content | STATIC_V9_FALLBACK (5 fixture cards) |
| Visual | PASS (16 screenshots; Swiper active) |
| Home partial | REMOVED from alcohol stack |
| Unresolved | Operator final visual sign-off recommended |
""",
    "FP-0002-V9-06E13-NEXT-STEP-RECOMMENDATION-v1.md": """# FP-0002 V9-06E13 — Next Step Recommendation

**Selected:** `CREATE_V9_06E14_OPERATOR_ALCOHOL_LEAF_VISUAL_QA_TASK`

E13 repaired specialists block technical parity (Swiper + direct V9 partial). Operator should perform final visual QA on full alcohol leaf after E12 rejection. If further block-level gaps found, scope next direct-port repair wave per E11 inventory priority.
""",
}

ARCH.mkdir(parents=True, exist_ok=True)
for name, body in docs.items():
    (ARCH / name).write_text(f"# REPORT — {name.replace('.md','')}\n\n" + body.split("\n", 1)[1] if body.startswith("#") else body, encoding="utf-8")

print("wrote", len(docs), "architecture docs")
