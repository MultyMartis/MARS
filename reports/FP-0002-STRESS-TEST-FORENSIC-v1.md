# REPORT — FP-0002 STRESS TEST FORENSIC v1

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-17  
**Phase:** Post–Full Build Stress Test — forensic audit only  
**SSOT:** `INCOMING/01_DESIGN/Шпиговский.fig` (via `_fig_full_build_extract.json`)  
**Build artifact:** `workspaces/fp-0002-shpigovsky-frontend/dist/desktop-shell.html`  
**Build log:** `workspaces/fp-0002-shpigovsky-frontend/logs/full-build-run.log`  
**Forensic log:** `workspaces/fp-0002-shpigovsky-frontend/logs/stress-test-forensic-v1.log`

**Constraints honored:** no HTML/SCSS/JS edits · no rebuild · no new discovery/layout/assembly docs.

---

## 1. Build Summary

| Metric | Value |
|--------|-------|
| Sections in FIG home frame | 15 |
| Sections in dist HTML | 15 |
| Section partials created (stress test) | 14 (`section-02` … `section-14`) |
| Header + Hero | Pre-existing in `desktop-shell.html` (shell v5.5 + brand fix) |
| Footer | Pre-existing `section-15-footer.html` |
| Images exported (build log) | 34 |
| Image files on disk (`src/img`) | 36 |
| Images referenced in dist HTML | 15 unique paths |
| Orphan / unreferenced exports | ~19 files |
| Gulp build | PASS (`npm run build`) |
| Build log section verdict | 15/15 PASS |
| **Forensic verdict** | **Page assembles; content fidelity PARTIAL; 2 sections FAIL** |

### Build log vs reality

`full-build-run.log` reports unconditional PASS for all 15 sections. Forensic review against FIG extract shows **no section achieves full FIG fidelity** except footer (pre-built shell). The build pipeline lacks an automated FIG↔HTML verification gate, so the log is **optimistic / false green**.

### DOM section order (dist)

`section-01` → `section-02` → … → `section-15` — matches FIG **layer child index** order.

**Exception:** SECTION-10 (`Слово спецу`) has FIG bounds `y=2389`, visually between SECTION-02 (`y=1029`) and SECTION-03 (`y=3000`). Discovery v1 flagged this anomaly; HTML keeps layer-index order, producing **visual order drift** for SECTION-10.

---

## 2. Section Audit

| SECTION | STATUS | PASS / PARTIAL / FAIL | COMMENT |
|---------|--------|----------------------|---------|
| SECTION-01 HEADER+HERO | Assembled | **PARTIAL** | Structure complete; hero img `52431f99` correct; logo fixed to Shpigovsky; messenger `href="#"`; CTAs non-functional; empty hero `alt` |
| SECTION-02 INTRO | Assembled | **PARTIAL** | Headings match; lead + card bodies **rewritten** vs FIG; intro image export unused |
| SECTION-03 SERVICES | Assembled | **PARTIAL** | H2 + lead match; service links + 3 cards **invented** beyond FIG TEXT extract |
| SECTION-04 WHY-US | Assembled | **PARTIAL** | H2, stats, lead, 4 features largely match; per-stat descriptions **lost**; 4/6 content images used |
| SECTION-05 REVIEWS | Assembled | **PARTIAL** | Shell OK; review bodies **hallucinated**; FIG disclaimer text not rendered |
| SECTION-06 HOW-TO-START | Assembled | **PARTIAL** | Steps + aside text strong; step images **missing** |
| SECTION-07 PROGRAM | Assembled | **PARTIAL** | H2 + partial lead; 4 program cards **invented** |
| SECTION-08 GENOTYPING | Assembled | **PARTIAL** | Headings mostly match; body **shortened/drifted**; image uses collision hash `d3ac7d00` |
| SECTION-09 ADVANTAGES | Assembled | **PARTIAL** | Brand + H2 + lead match; card titles/bodies largely **generated** |
| SECTION-10 SPECIALIST-WORD | Assembled | **PARTIAL** | Name, role, photo `93c2fbf5` OK; quote **truncated**; **wrong page position** vs visual FIG |
| SECTION-11 VIDEO | Assembled | **PARTIAL** | Poster `cd50b3a4` OK; no video source / embed |
| SECTION-12 SPECIALISTS | Assembled | **FAIL** | Generic «Специалист центра» ×3; same photo ×3; FIG doctor components not mapped |
| SECTION-13 ARTICLES | Assembled | **FAIL** | Article titles/excerpts **invented**; thumbnails are CSS placeholders, no FIG assets |
| SECTION-14 FAQ | Assembled | **PARTIAL** | Form shell matches FIG labels; accordion Q&A **invented**; sidebar image missing |
| SECTION-15 FOOTER | Assembled | **PASS** | Prior shell build; real IA labels; social/legal placeholders remain |

**Totals:** PASS 1 · PARTIAL 12 · FAIL 2

---

## 3. Failure Register

### FAIL-001 — False-green build log

| Field | Value |
|-------|-------|
| **TITLE** | Build reports 15/15 PASS without FIG verification |
| **SEVERITY** | HIGH |
| **ROOT CAUSE** | No post-build diff gate; agent self-attestation only |
| **EVIDENCE** | `full-build-run.log` all PASS; forensic finds 12 PARTIAL + 2 FAIL |
| **RECOMMENDED FIX** | Mandatory FIG-text / FIG-image hash checklist per section before PASS |

### FAIL-002 — Review body hallucination (SECTION-05)

| Field | Value |
|-------|-------|
| **TITLE** | Invented review paragraphs |
| **SEVERITY** | HIGH |
| **ROOT CAUSE** | FIG `отзыв` component text not extracted; generator filled generic copy |
| **EVIDENCE** | FIG TEXT extract for S05 has 5 nodes (title, meta, disclaimer, links) — no review bodies; HTML has 3 full paragraphs |
| **RECOMMENDED FIX** | Component-instance text walker for `отзыв`; forbid generative fill |

### FAIL-003 — Intro text drift (SECTION-02)

| Field | Value |
|-------|-------|
| **TITLE** | Lead and card copy rewritten |
| **SEVERITY** | HIGH |
| **ROOT CAUSE** | Frontend generator paraphrased instead of locking FIG strings |
| **EVIDENCE** | FIG `1:931` canonical lead absent; card texts shortened vs `1:945`/`1:951`/`1:957` |
| **RECOMMENDED FIX** | Text lock file per section from FIG extract; diff gate |

### FAIL-004 — Image hash collision `d3ac7d00`

| Field | Value |
|-------|-------|
| **TITLE** | Frame-export hash reused across sections |
| **SEVERITY** | CRITICAL |
| **ROOT CAUSE** | FIG parser exports section FRAME as image; same hash in S02,S03,S04,S06,S07,S08,S09,S11,S12,S14 |
| **EVIDENCE** | `genotyping-d3ac7d00.jpg` in HTML; hash appears 10+ times in `exportedImages` |
| **RECOMMENDED FIX** | Exclude FRAME-level exports; rank leaf IMAGE nodes by area; hash dedup registry |

### FAIL-005 — Asset orphans (56% unused)

| Field | Value |
|-------|-------|
| **TITLE** | Exported images not wired to HTML |
| **SEVERITY** | MEDIUM |
| **ROOT CAUSE** | Export-all strategy without reference mapping |
| **EVIDENCE** | 36 files on disk, 15 referenced in dist |
| **RECOMMENDED FIX** | Asset manifest with `section → nodeId → html src` binding |

### FAIL-006 — Component instance blindness

| Field | Value |
|-------|-------|
| **TITLE** | FIG components not mapped to HTML |
| **SEVERITY** | HIGH |
| **ROOT CAUSE** | Flat TEXT extract ignores INSTANCE subtrees (`Пункт услуги`, `Статья`, `Врач`, `отзыв`, `Расскрытие вопроса`) |
| **EVIDENCE** | Discovery lists component instances; HTML uses generic cards |
| **RECOMMENDED FIX** | Group Register pass over INSTANCE nodes before generation |

### FAIL-007 — SECTION-10 visual order drift

| Field | Value |
|-------|-------|
| **TITLE** | «Слово спецу» wrong vertical position |
| **SEVERITY** | HIGH |
| **ROOT CAUSE** | Assembly follows layer index; FIG anomaly (y=2389) unresolved |
| **EVIDENCE** | Discovery §SECTION-10 anomaly; DOM order places S10 after S09 |
| **RECOMMENDED FIX** | Assembly rule: sort sections by `bounds.y` when delta > threshold; HITL on conflicts |

### FAIL-008 — Specialists placeholders (SECTION-12)

| Field | Value |
|-------|-------|
| **TITLE** | Generic names + duplicate portrait |
| **SEVERITY** | CRITICAL |
| **ROOT CAUSE** | `Врач` component names/photos not extracted per instance |
| **EVIDENCE** | HTML: «Специалист центра» ×3, `specialists-39136806.jpg` ×3 |
| **RECOMMENDED FIX** | Enumerate `Врач` instances; map unique image hashes per card |

### FAIL-009 — Articles missing assets (SECTION-13)

| Field | Value |
|-------|-------|
| **TITLE** | CSS gradient blocks instead of article thumbnails |
| **SEVERITY** | HIGH |
| **ROOT CAUSE** | `Статья` component images not extracted/linked |
| **EVIDENCE** | `<div class="home-articles__image" aria-hidden="true">` ×3; FIG has `Статья` instances |
| **RECOMMENDED FIX** | Per-article asset extraction from component symbol |

### FAIL-010 — Interaction stubs

| Field | Value |
|-------|-------|
| **TITLE** | Non-functional CTAs, form, video |
| **SEVERITY** | MEDIUM |
| **ROOT CAUSE** | Build scope = static shell only |
| **EVIDENCE** | `type="button"` CTAs; `form action="#"`; video play without `src` |
| **RECOMMENDED FIX** | Explicit interaction charter or document as KNOWN NON-GOALS |

### FAIL-011 — Accessibility: empty alt

| Field | Value |
|-------|-------|
| **TITLE** | Decorative/content images with `alt=""` |
| **SEVERITY** | MEDIUM |
| **ROOT CAUSE** | Generator default empty alt on home images |
| **EVIDENCE** | 13+ `<img alt="">` in home sections |
| **RECOMMENDED FIX** | Alt text from FIG node `name` or adjacent TEXT |

### FAIL-012 — Stat description loss (SECTION-04)

| Field | Value |
|-------|-------|
| **TITLE** | Per-stat explanatory copy dropped |
| **SEVERITY** | MEDIUM |
| **ROOT CAUSE** | Generator rendered stat labels only |
| **EVIDENCE** | FIG `1:1010`–`1:1019` stat bodies absent in HTML |
| **RECOMMENDED FIX** | Pair stat NUMBER + DESCRIPTION from adjacent TEXT nodes |

### FAIL-013 — Expert quote truncation (SECTION-10)

| Field | Value |
|-------|-------|
| **TITLE** | Second quote paragraph missing |
| **SEVERITY** | MEDIUM |
| **ROOT CAUSE** | Multi-paragraph TEXT node split/truncated in generation |
| **EVIDENCE** | FIG `1:1214` includes «Наша цель… контроль над ней» — absent in HTML |
| **RECOMMENDED FIX** | Preserve `\n` splits as separate `<p>` inside blockquote |

### FAIL-014 — Program cards invented (SECTION-07)

| Field | Value |
|-------|-------|
| **TITLE** | Four direction cards generated |
| **SEVERITY** | MEDIUM |
| **ROOT CAUSE** | FIG `этап` component text not extracted; titles inferred from lead |
| **EVIDENCE** | FIG extract has 4 texts; HTML has 4 cards with distinct invented bodies |
| **RECOMMENDED FIX** | Walk `этап` instances in frame `1:1115` |

### FAIL-015 — Services blocks invented (SECTION-03)

| Field | Value |
|-------|-------|
| **TITLE** | Service list + cards beyond FIG extract |
| **SEVERITY** | MEDIUM |
| **ROOT CAUSE** | Same as FAIL-006 for `Пункт услуги` / `Услуга` |
| **EVIDENCE** | FIG TEXT count=3; HTML has 4 links + 3 cards |
| **RECOMMENDED FIX** | Component-driven services assembly |

### FAIL-016 — FIG disclaimer text leak

| Field | Value |
|-------|-------|
| **TITLE** | Price disclaimer in FIG but not in HTML |
| **SEVERITY** | LOW |
| **ROOT CAUSE** | Text nodes attached to wrong section in extract / ignored in build |
| **EVIDENCE** | «Цены указаны примерные…» in FIG S05, S12, S13 extracts — not rendered |
| **RECOMMENDED FIX** | Section-scoped text binding review |

### FAIL-017 — Prior logo collision (mitigated)

| Field | Value |
|-------|-------|
| **TITLE** | Skinerica logo in header slot `1:880` |
| **SEVERITY** | BLOCKER (resolved before stress test) |
| **ROOT CAUSE** | First-image-in-header selection (`de219c6e`) |
| **EVIDENCE** | `FP-0002-HEADER-FIG-BRAND-ASSET-FIX-v1.md`; logo now `262f79db` |
| **RECOMMENDED FIX** | Brand hash allowlist (already documented in factory failures) |

### FAIL-018 — No post-build FIG diff

| Field | Value |
|-------|-------|
| **TITLE** | Pipeline ends at gulp PASS |
| **SEVERITY** | HIGH |
| **ROOT CAUSE** | Missing validation chain stage |
| **EVIDENCE** | Stress test shipped with known content gaps |
| **RECOMMENDED FIX** | Automated `fig_extract ↔ dist` script in CI / pre-report |

---

## 4. Lessons Learned (by factory layer)

| Layer | Failures | Lesson |
|-------|----------|--------|
| **Discovery** | FAIL-007 | Y-order vs layer-index conflicts must produce explicit ASSEMBLY DECISION, not silent default |
| **Group Register** | FAIL-006, FAIL-008, FAIL-015 | INSTANCE-heavy sections (services, doctors, articles) need group register before HTML |
| **Layout Spec** | — | Not in scope this run; drift suggests layout spec did not lock text blocks |
| **Assembly Spec** | FAIL-007 | Section order rule undefined for FIG anomalies |
| **Build** | FAIL-001, FAIL-010, FAIL-018 | Build PASS must require forensic checklist, not agent assertion |
| **Assets** | FAIL-004, FAIL-005, FAIL-009, FAIL-017 | Hash collision + orphan exports = systemic asset layer failure |
| **Components** | FAIL-002, FAIL-008, FAIL-014 | Flat TEXT extract insufficient for component-based sections |
| **FIG Parser** | FAIL-004, FAIL-016 | Frame-level image export pollutes manifest; cross-section text bleed |
| **Frontend Generator** | FAIL-003, FAIL-011, FAIL-012, FAIL-013 | Generator paraphrases and invents when extract incomplete — must hard-fail instead |

---

## 5. Factory Score

| Capability | Score | Explanation |
|------------|-------|-------------|
| **SECTION EXTRACTION** | **82** | All 15 FIG frames → DOM sections; order anomaly unresolved |
| **GROUP EXTRACTION** | **48** | Discovery names groups; build does not bind INSTANCE subtrees |
| **TEXT EXTRACTION** | **42** | Headings/links often correct; body copy frequently rewritten or invented |
| **IMAGE EXTRACTION** | **46** | Volume OK; collision hash + wrong leaf selection + 56% orphans |
| **COMPONENT EXTRACTION** | **38** | Cards/accordion/reviews approximate layout, not component truth |
| **FULL PAGE BUILD** | **72** | Single page compiles; includes work; coherent navigation IA |
| **PIXEL FIDELITY** | **34** | **SAFE UNKNOWN** for spacing/type render; known structural/asset gaps imply low fidelity |
| **PRODUCTION READINESS** | **28** | Placeholders, no backend, content trust failures, a11y gaps |

**Composite stress-test grade:** ~49/100 — **prototype assembly, not production FIG fidelity**.

---

## 6. Memory Analysis

**Current page weight (evidence):**

- 15 sections, ~611 lines dist HTML, ~37 KB HTML
- FIG extract JSON ~1 675 lines
- 14 partials + 1 shared SCSS created in one build run
- Full conversation + extract + partials ≈ high context load

| Scale | Sections | MEMORY RISK | TOKEN RISK | CURSOR CHAT RISK | Full chain without staging? |
|-------|----------|-------------|------------|------------------|----------------------------|
| **1×** (current) | 15 | MEDIUM | HIGH | HIGH | Yes — with quality loss (this run proves) |
| **2×** | ~30 | HIGH | CRITICAL | CRITICAL | Unlikely — requires per-section charters + frozen SSOT |
| **3×** | ~45 | CRITICAL | CRITICAL | CRITICAL | No — context truncation will drop FIG detail |
| **5×** | ~75 | CRITICAL | CRITICAL | CRITICAL | No — must split across runs + machine artifacts |

**Risk drivers:** full-page FIG JSON in chat, generative fill when context tightens, no incremental diff artifacts, combined header+hero+14 sections+SCSS in one agent turn.

---

## 7. Recommended Upgrades

1. **Mandatory FIG diff gate** — block PASS until text hashes + image hashes match per section.
2. **Ban generative paraphrase** — on missing text, emit `UNKNOWN` + HITL, not invented copy.
3. **Component instance walker** — replace flat TEXT extract for INSTANCE-heavy frames.
4. **Asset identity registry** — forbid `d3ac7d00`-class frame exports; enforce unique hash per slot.
5. **Section order policy** — `bounds.y` primary, layer index fallback, explicit conflict report.
6. **Staged build charters** — max 2–3 sections per agent run with frozen prior sections.
7. **Machine-readable section SSOT** — `section-NN.lock.json` (texts, images, order) generated once, consumed by builder.
8. **False-green log fix** — rename build log PASS to `BUILT` vs `VERIFIED`.

---

## UNKNOWN / limits of this pass

- **Pixel fidelity** (spacing, fonts, colors vs FIG) — not measured; score is inference from missing assets/text.
- **COMPONENT text inside INSTANCE symbols** — partially invisible in flat extract; some FIG content may exist but was not machine-exported to JSON.
- **SECTION-15 footer** — evaluated as pre-built shell, not stress-test generator output.

---

*End of report — forensic only, no code changes.*
