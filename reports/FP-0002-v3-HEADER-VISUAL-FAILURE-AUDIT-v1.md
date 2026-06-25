# FP-0002 v3 — Header Visual Failure Audit v1

**Date:** 2026-06-22  
**Phase:** HB-VISUAL-AUDIT  
**Workspace:** `workspaces/fp-0002-shpigovsky-v3/`  
**Compare set:** `dist/index.html` (pre-patch) · PDF / FIG geometry · `HOME-PAGE-FULL-MOCKUP.jpg`

---

## Verdict flags (mandatory)

| Flag | Value |
|------|-------|
| **FORMAL LOCK PASS BUT VISUAL FAIL** | **YES** |
| **FALSE GREEN BUILD** | **YES** |

Prior QA (`FP-0002-v3-HEADER-QA-v1.md`) recorded **BUILD PASS** and structural compliance while operator screenshot shows unacceptable visual output.

---

## Sources used

| Source | Path / artefact | Role |
|--------|-----------------|------|
| PDF PRIMARY | `INCOMING/01_DESIGN/2026-06-11-home-v2/Главная страница (v2).pdf` | Row model · text lock · zone order |
| FIG SECONDARY | `Шпиговский.fig` frame `1:877` | Envelope 1170×143 · slot sizes |
| JPG REFERENCE | `INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` | Visual tie-break · alignment check |
| Visual Scale Spec | `FP-0002-HEADER-VISUAL-SCALE-SPEC-v1.md` | Mass / proportion law |
| Built output | `dist/index.html` + compiled CSS (pre-patch) | Failure manifestation |

**Disk honesty:** PDF/FIG/JPG canonical paths documented in registry; geometry derived from prior parse artefacts where live files unavailable in some sessions.

---

## Visual delta register (pre-patch build)

### Container / envelope

| Check | Reference intent | Pre-patch build | Delta |
|-------|------------------|-----------------|-------|
| Outer header width | Full viewport bleed | `width: 100%` on `.header` | **OK structurally** |
| Inner container | 1170px max + 40px pad desktop | `.container` token | **OK structurally** |
| Perceived width | Content spans full 1170 inner track | Row `space-between` on 4 siblings collapsed visual mass into narrow cluster | **FAIL — compressed island** |
| Header total height | FIG ~143px envelope; MAIN ROW dominant | Both rows `min-height: 46px` | **FAIL — row parity (~1:1 not ~2:1)** |

### Row 1 (TOP ROW)

| Zone | Reference | Pre-patch | Delta |
|------|-----------|-----------|-------|
| Region | Left anchor, weak meta 14px | Present, 14px | Placement OK; weak mass OK |
| Hours | Center-left, weak meta | In flex row with equal spacing | **FAIL — drifted center, not anchored to grid** |
| Utility | Center-right pair | Same row flex | **FAIL — spacing vs phones/hours not PDF-like** |
| Phones | Right anchor, 20px strong | 20px, right column | **Partial — strong size OK but column misaligned vs CTA** |
| Row height | ~40–46px band | 46px min only | **FAIL — equal to MAIN ROW** |

### Row 2 (MAIN ROW)

| Zone | Reference | Pre-patch | Delta |
|------|-----------|-----------|-------|
| Logo group | `logo.svg` only — graphic includes full wordmark | SVG **plus** duplicate HTML title/subtitle spans | **FAIL — double brand stack, wrong grouping** |
| Logo size | 205×46 slot (FIG); dominant mass ≈ CTA | 205px mark + extra text block `max-width: 420px` | **FAIL — bloated/wrong group, not institution block** |
| Nav | 5 links, 16px, centered between anchors | 5 links OK; `flex:1` center nav | **FAIL — vertical/horizontal alignment vs PDF** |
| CTA | 190×44 dominant right anchor | `min-width: 190px` but global `.btn { min-width: 280px }` fight | **FAIL — size/position inconsistent** |
| Row height | Dominant band (~2× TOP ROW) | 46px min (= TOP ROW) | **FAIL — MAIN ROW not visually dominant** |

### Typography / mass hierarchy

| Relationship (Visual Scale Spec) | Required | Pre-patch | Delta |
|----------------------------------|----------|-----------|-------|
| MAIN ROW band >> TOP ROW band | ~2×–2.5× | ~1× | **FAIL (VS-F04)** |
| Logo mark ≈ CTA mass | Paired anchors | Logo group oversized by duplicate text; CTA generic btn | **FAIL (VS-F01, VS-F03)** |
| Phones >> hours/region | Strong vs weak | Phones 20px OK but row density equalized | **Partial FAIL (VS-F02)** |
| Nav > utility | Strong vs medium | Similar 14–16px without band separation | **FAIL (VS-F07)** |

### Compression / grouping failures

| Symptom | Root in implementation |
|---------|------------------------|
| Header reads as small centered block | Single flex `space-between` rows without shared column grid; no left/right anchor columns |
| Brand/logo group wrong | Duplicate text next to full wordmark SVG |
| Top/bottom rows misaligned | No shared 205px left column / auto right column between rows |
| CTA wrong size/position | Global button min-width 280px vs header override 190px; no grid `justify-self: end` |
| Nav spacing wrong | Fixed gap only; nav in unbounded flex center without anchor grid |

---

## False-green analysis

| Prior QA check | Recorded | Visual reality |
|----------------|----------|----------------|
| PDF ROW MODEL USED | YES | Row **labels** correct; **geometry** wrong |
| ROW 1/2 GROUPS CORRECT | YES | Group **order** correct; **mass/placement** wrong |
| BUILD PASS | YES | Gulp exit 0 — **no visual geometry gate** |
| READY FOR OPERATOR VISUAL REVIEW | Implied pass | Operator **REJECT** |

**Failure class:** `SPEC FORMALISM WITHOUT VISUAL SCALE` (per `FP-0002-HEADER-VISUAL-SCALE-SPEC-v1.md` §9).

---

## ROOT CAUSE (summary)

1. Layout lock satisfied **content and order** but not **visual mass or grid geometry**.
2. Logo group treated as mark + caption text while `logo.svg` already embeds full wordmark paths.
3. Both header rows given equal min-height and uniform flex distribution.
4. No shared 3-column grid tying Region↔Logo (left) and Phones↔CTA (right).
5. QA gate checked structural excludes, not proportional/visual acceptance (VS-A01…A14).

---

**STOP — HB-VISUAL-AUDIT complete.**
