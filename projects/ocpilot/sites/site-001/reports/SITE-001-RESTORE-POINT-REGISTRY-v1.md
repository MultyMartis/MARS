# SITE-001 Restore Point Registry v1

**Type:** Restore point registry — **documentation only**  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Purpose:** Зафиксировать две стратегические точки восстановления перед переходом на WF-V3

**Explicit exclusions (honored):** No site modifications · No FTP uploads · No CSS/Twig edits · No deploy · No cache clears

---

## Registry summary

| Alias | Role | Primary backup-id | Date |
|-------|------|-------------------|------|
| **`site-001-rebrand-baseline-v1`** | Последняя стабильная точка после ребрендинга Phase 1, до Website Factory implementation waves | `pre-w5a-header-shell-20260609-2251` | 2026-06-09 |
| **`site-001-wfv2-final-experimental-20260610`** | Экспериментальная база WF-V2 после W1→W2→W2S→W2A→W3 | `pre-wfv2-w4-final-surface-cleanup-20260610-0447` | 2026-06-10 |

**External storage root (all backups):**

```
C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\
```

---

## A) REBRAND BASELINE

### A.1 Alias and checkpoint

| Field | Value |
|-------|-------|
| **Alias** | `site-001-rebrand-baseline-v1` |
| **Checkpoint document** | [SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md](SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md) |
| **Checkpoint ID** | `SITE-001-PHASE1-STABLE-CHECKPOINT-v1` |
| **Recommended git tag** | `site-001-phase1-stable-2026-06` |
| **Decision** | **APPROVED** — [SITE-001-PHASE1-STABLE-CHECKPOINT-DECISION-v1.md](SITE-001-PHASE1-STABLE-CHECKPOINT-DECISION-v1.md) |
| **Date** | **2026-06-09** |
| **Acceptance** | **PHASE 1 ACCEPTED WITH NOTES** — [SITE-001-PHASE1-FINAL-DECISION-v1.md](SITE-001-PHASE1-FINAL-DECISION-v1.md) |

### A.2 Definition

**Rebrand baseline** = TEST после завершения Phase 1 Brand Replacement (АЦ Хмельницкий → СИБКАР), **до первой Website Factory implementation wave** (W5-A Header Shell, 2026-06-09 22:51).

Включает:

- W1A–W1G (store settings, theme branding, controllers, logos, YML/robots, information pages, SEO controllers, DB SEO cleanup)
- OCPilot Phase 2 **visual** waves W3-V / W3V2 / W3UX-C1 / W3ATMOSPHERE / W4 / W4.1 (cosmetic & structural, **не** Website Factory)

**Не включает:** W5-A · W5-A-S · W5-C · WF-V2 (W1–W4)

### A.3 Primary backup-id (file bundle)

| Field | Value |
|-------|-------|
| **Backup ID** | `pre-w5a-header-shell-20260609-2251` |
| **Path** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w5a-header-shell-20260609-2251\` |
| **Manifest** | `BACKUP-MANIFEST.md` (same folder) |
| **Created** | 2026-06-09T22:51:24 |
| **Rationale** | Последний **полный** incremental backup непосредственно **перед** W5-A — первой Website Factory implementation wave на TEST |

### A.4 File composition

| Remote path | Local backup name | Bytes (manifest) | Lines |
|-------------|-------------------|------------------|-------|
| `catalog/view/theme/auto/template/common/header.twig` | `catalog__view__theme__auto__template__common__header.twig` | 11,719 | 343 |
| `css/main.css` | `css__main.css` | 146,267 | 8,466 |
| `css/media.css` | `css__media.css` | 36,456 | 2,480 |

**Note:** `product.twig` не входит в этот backup. Для полного PDP-состояния rebrand-era + W4 используйте companion backup `pre-w4-1-stable-20260609-1506` (5 файлов, см. A.6).

### A.5 Active wave markers (pre-W5-A)

| Marker | Present |
|--------|---------|
| W3UX-C1 Used Catalog Card Density | **YES** |
| W3ATMOSPHERE-01 Global Atmosphere Refresh | **YES** |
| W4 Used PDP Structural Visual Slice | **YES** |
| W4.1 Header & Hero Authority | **YES** |
| W5-A Header Shell Recomposition | **NO** |
| Website Factory / WF-V2 | **NO** |

### A.6 State description

TEST на rebrand baseline:

- Бренд **СИБКАР** на всех 13 проверенных public URL (legacy dictionary **0 FAIL**)
- Phase 1 copy, URLs, phones, menu labels — **frozen**
- Визуальный слой: W3 atmosphere + W4 structural slice + W4.1 header/hero — **без** W5 graphite shell и **без** WF-V2 experimental
- Header: pre-W5-A DOM (11,719 bytes twig)
- Used PDP: W4 wrappers present; W5-C commercial stage **absent**

**Companion backups (same era):**

| Backup ID | Scope | Path |
|-----------|-------|------|
| `pre-w4-1-stable-20260609-1506` | 5-file bundle incl. `product.twig`, `footer.twig` | `...\backups\pre-w4-1-stable-20260609-1506\` |
| `pre-w3v-20260609-0327` | CSS-only Phase 1 visual layer (pre W3-V) | `...\backups\pre-w3v-20260609-0327\` |

**Phase 1 pure rebrand (logical, no monolithic file archive):**

| Layer | Recovery |
|-------|----------|
| Documentation checkpoint | `site-001-phase1-stable-2026-06` |
| DB (W1G rollback) | `w1g-seo-db-pre-replace-2026-06-09\rollback.sql` |
| Per-wave FTP (W1D/W1F-*) | `w1d-pre-replace-2026-06-08`, `w1f-a-pre-replace-2026-06-08`, `w1f-b-pre-replace-2026-06-08`, `w1f-c1-pre-replace-2026-06-08` |
| Full site T3 | [SITE-001-W1-BACKUP-PROCEDURE-v1.md](SITE-001-W1-BACKUP-PROCEDURE-v1.md) — operator Beget backup 2026-06-08 |

### A.7 Related reports (rebrand branch)

| Category | Reports |
|----------|---------|
| **Checkpoint & acceptance** | [SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md](SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md) · [SITE-001-PHASE1-STABLE-CHECKPOINT-DECISION-v1.md](SITE-001-PHASE1-STABLE-CHECKPOINT-DECISION-v1.md) · [SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md](SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md) · [SITE-001-PHASE1-FINAL-DECISION-v1.md](SITE-001-PHASE1-FINAL-DECISION-v1.md) · [SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md](SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md) |
| **W1 execution** | [SITE-001-W1A-EXECUTION-v1.md](SITE-001-W1A-EXECUTION-v1.md) · [SITE-001-W1B-EXECUTION-v1.md](SITE-001-W1B-EXECUTION-v1.md) · [SITE-001-W1C-EXECUTION-v1.md](SITE-001-W1C-EXECUTION-v1.md) · [SITE-001-W1D-EXECUTION-v1.md](SITE-001-W1D-EXECUTION-v1.md) · [SITE-001-W1F-A-EXECUTION-v1.md](SITE-001-W1F-A-EXECUTION-v1.md) · [SITE-001-W1F-B-EXECUTION-v1.md](SITE-001-W1F-B-EXECUTION-v1.md) · [SITE-001-W1F-C1-EXECUTION-v1.md](SITE-001-W1F-C1-EXECUTION-v1.md) · [SITE-001-W1G-SEO-DB-CLEANUP-v1.md](SITE-001-W1G-SEO-DB-CLEANUP-v1.md) |
| **Rollback & backup** | [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) · [SITE-001-W1-BACKUP-PROCEDURE-v1.md](SITE-001-W1-BACKUP-PROCEDURE-v1.md) |
| **Pre-WF boundary** | [SITE-001-W2-VISUAL-REFRESH-DECISION-v1.md](SITE-001-W2-VISUAL-REFRESH-DECISION-v1.md) · [SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md](SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md) (design only — no writes) |

### A.8 Restore procedure (T1)

1. FTP **STOR** restore from `pre-w5a-header-shell-20260609-2251` (header + CSS)
2. If PDP rollback needed: additionally restore from `pre-w4-1-stable-20260609-1506` (`product.twig`, optional `footer.twig`)
3. Admin: system + modification + image cache clear; modification refresh
4. Verify: W5-A markers **absent**; Phase 1 brand markers **present**

---

## B) WF-V2 FINAL EXPERIMENTAL

### B.1 Alias and scope

| Field | Value |
|-------|-------|
| **Alias** | `site-001-wfv2-final-experimental-20260610` |
| **Scope** | Cumulative TEST state after **WF-V2-W1 · W2 · W2S · W2A · W3** |
| **Date** | **2026-06-10** |
| **Entry baseline (parent)** | Visual Baseline V1 — `pre-w5c-commercial-stage-20260610-0002` |
| **Out of alias scope** | WF-V2-W4 (deployed separately on TEST; not part of this registry entry) |

### B.2 File snapshot backup-id (post-W3 capture)

| Field | Value |
|-------|-------|
| **Backup ID** | `pre-wfv2-w4-final-surface-cleanup-20260610-0447` |
| **Path** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-wfv2-w4-final-surface-cleanup-20260610-0447\` |
| **Manifest** | `BACKUP-MANIFEST.md` (same folder) |
| **Created** | 2026-06-10T04:47:10 |
| **Rationale** | Pre-write backup **перед W4** = точный file-level снимок **после W3** (manifest confirms all W1–W3 markers **YES**, W4 marker **NO**) |

### B.3 File composition (snapshot)

| Remote path | Local backup name | Bytes (manifest) | Lines |
|-------------|-------------------|------------------|-------|
| `catalog/view/theme/auto/template/product/product.twig` | `catalog__view__theme__auto__template__product__product.twig` | 38,185 | 946 |
| `css/main.css` | `css__main.css` | 212,975 | 11,060 |
| `css/media.css` | `css__media.css` | 55,575 | 3,273 |

**Header (not in snapshot folder — unchanged W1–W3):**

| Remote path | Post-W1 bytes | Source |
|-------------|---------------|--------|
| `catalog/view/theme/auto/template/common/header.twig` | 12,443 | WF-V2-W1 deploy — [SITE-001-WFV2-W1-HEADER-EXECUTION-v1.md](SITE-001-WFV2-W1-HEADER-EXECUTION-v1.md); working copy `.recovery-temp/site-001-wfv2-w1-work/` |

**Full 4-file restore recipe:**

1. `header.twig` — from WF-V2-W1 post-deploy (working copy or re-apply W1 from `pre-wfv2-w1-header-20260610-0216` rollback inverse)
2. `product.twig` + `css/main.css` + `css/media.css` — from `pre-wfv2-w4-final-surface-cleanup-20260610-0447`

### B.4 Parent backup chain (WF-V2 waves)

| Order | Wave | Pre-write backup-id | Path suffix | Parent |
|-------|------|---------------------|-------------|--------|
| 0 | **Visual Baseline V1** (entry) | `pre-w5c-commercial-stage-20260610-0002` | `pre-w5c-commercial-stage-20260610-0002\` | W5-A/S stable |
| 1 | **WF-V2-W1** Hybrid Header | `pre-wfv2-w1-header-20260610-0216` | `pre-wfv2-w1-header-20260610-0216\` | Visual Baseline V1 |
| 2 | **WF-V2-W2** Flat Used PDP | `pre-wfv2-w2-flat-pdp-20260610-0304` | `pre-wfv2-w2-flat-pdp-20260610-0304\` | post-W1 |
| 3 | **WF-V2-W2S** Clean Stabilization | `pre-wfv2-w2s-pdp-clean-20260610-0330` | `pre-wfv2-w2s-pdp-clean-20260610-0330\` | post-W2 |
| 4 | **WF-V2-W2A** Anatomy Rebuild | `pre-wfv2-w2a-pdp-anatomy-rebuild-20260610-0401` | `pre-wfv2-w2a-pdp-anatomy-rebuild-20260610-0401\` | post-W2S |
| 5 | **WF-V2-W3** Layout Recomposition | `pre-wfv2-w3-layout-recomposition-20260610-0413` | `pre-wfv2-w3-layout-recomposition-20260610-0413\` | post-W2A |
| **→** | **Alias snapshot (post-W3)** | `pre-wfv2-w4-final-surface-cleanup-20260610-0447` | `pre-wfv2-w4-final-surface-cleanup-20260610-0447\` | post-W3 |

**Alternate W2A backups (same session):** `pre-wfv2-w2a-pdp-anatomy-rebuild-20260610-0356` (clean W2S baseline) · `pre-wfv2-w2a-pdp-anatomy-rebuild-20260610-0359`  
**Alternate W3 backups:** `pre-wfv2-w3-layout-recomposition-20260610-0411`

### B.5 Cumulative files modified (W1→W3)

| Remote path | Modified by waves | Cumulative hooks / blocks |
|-------------|-------------------|---------------------------|
| `catalog/view/theme/auto/template/common/header.twig` | **W1** | `wfv2-header wfv2-header--hybrid`; hybrid contact rail + dark band + light promo |
| `catalog/view/theme/auto/template/product/product.twig` | **W2 · W2S · W2A · W3** | `wfv2-flat-pdp` · `wfv2-clean-pdp` · `wfv2-anatomy-pdp` · `wfv2-layout-pdp`; DOM reorder (anatomy + offer column) |
| `css/main.css` | **W1 · W2 · W2S · W2A · W3** | Blocks: `WF-V2-W1` · `WF-V2-W2` · `WF-V2-W2S` · `WF-V2-W2A` · `WF-V2-W3` |
| `css/media.css` | **W1 · W2 · W2S · W2A · W3** | Responsive blocks for each wave above |

**Not modified (W1–W3):** `footer.twig` · PHP · JS · DB

### B.6 Active wave markers (post-W3)

| Marker | Present |
|--------|---------|
| WF-V2-W1 Hybrid Header System | **YES** |
| WF-V2-W2 Flat Used PDP Stage | **YES** |
| WF-V2-W2S Clean Used PDP Stabilization | **YES** |
| WF-V2-W2A PDP Anatomy Rebuild | **YES** |
| WF-V2-W3 PDP Layout Recomposition | **YES** |
| `wfv2-layout-pdp` | **YES** |
| WF-V2-W4 Final Surface Cleanup | **NO** |
| `wfv2-surface-pdp` | **NO** |

### B.7 State description

TEST на WF-V2 final experimental (post-W3):

- **Header:** hybrid light rail + dark primary band + light promo (WF-V2-W1); phone/WhatsApp in rail only
- **Used PDP:** flat → clean → anatomy rebuild → layout recomposition (68/32 hero, offer column reorder, Layer 3 vertical stack, scoped 1780px container)
- **Underlying layers preserved:** Visual Baseline V1 (W5-C commercial stage markers, W4 wrappers, W3UX-C1, W3ATMOSPHERE) under WF-V2 override blocks
- **Verification:** W3 decision **ACCEPT** — 8/8 URL matrix PASS — [SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-DECISION-v1.md](SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-DECISION-v1.md)
- **Operator HITL:** W1/W2/W2A automated PASS; visual sign-off **PENDING** on all waves

### B.8 Related reports (WF-V2 branch)

| Wave | Charter | CR | Execution | Decision | Rollback |
|------|---------|----|-----------|----------|----------|
| **Program** | — | — | — | — | [SITE-001-WF-V2-IMPLEMENTATION-PLAN-v1.md](SITE-001-WF-V2-IMPLEMENTATION-PLAN-v1.md) · [SITE-001-WF-V2-GAP-ANALYSIS-v1.md](SITE-001-WF-V2-GAP-ANALYSIS-v1.md) |
| **W1** | [WRITE-CHARTER](SITE-001-WFV2-W1-HEADER-WRITE-CHARTER-v1.md) | [CR](SITE-001-WFV2-W1-HEADER-CHANGE-REQUEST-v1.md) | [EXEC](SITE-001-WFV2-W1-HEADER-EXECUTION-v1.md) | [DEC](SITE-001-WFV2-W1-HEADER-DECISION-v1.md) | [RB](SITE-001-WFV2-W1-HEADER-ROLLBACK-PLAN-v1.md) |
| **W2** | [WRITE-CHARTER](SITE-001-WFV2-W2-FLAT-PDP-WRITE-CHARTER-v1.md) | [CR](SITE-001-WFV2-W2-FLAT-PDP-CHANGE-REQUEST-v1.md) | [EXEC](SITE-001-WFV2-W2-FLAT-PDP-EXECUTION-v1.md) | [DEC](SITE-001-WFV2-W2-FLAT-PDP-DECISION-v1.md) | [RB](SITE-001-WFV2-W2-FLAT-PDP-ROLLBACK-PLAN-v1.md) |
| **W2S** | [WRITE-CHARTER](SITE-001-WFV2-W2S-PDP-CLEAN-STABILIZATION-WRITE-CHARTER-v1.md) | [CR](SITE-001-WFV2-W2S-PDP-CLEAN-STABILIZATION-CHANGE-REQUEST-v1.md) | [EXEC](SITE-001-WFV2-W2S-PDP-CLEAN-STABILIZATION-EXECUTION-v1.md) | *(no separate decision doc)* | [RB](SITE-001-WFV2-W2S-PDP-CLEAN-STABILIZATION-ROLLBACK-PLAN-v1.md) |
| **W2A** | [WRITE-CHARTER](SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-WRITE-CHARTER-v1.md) | [CR](SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-CHANGE-REQUEST-v1.md) | [EXEC](SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-EXECUTION-v1.md) | [DEC](SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-DECISION-v1.md) | [RB](SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-ROLLBACK-PLAN-v1.md) |
| **W3** | [WRITE-CHARTER](SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-WRITE-CHARTER-v1.md) | [CR](SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-CHANGE-REQUEST-v1.md) | [EXEC](SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-EXECUTION-v1.md) | [DEC](SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-DECISION-v1.md) | [RB](SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-ROLLBACK-PLAN-v1.md) |

**Entry baseline report:** [SITE-001-W5-STABLE-BACKUP-v1.md](SITE-001-W5-STABLE-BACKUP-v1.md)

**Local evidence (repo):**

| Wave | Result JSON | Working copy |
|------|-------------|--------------|
| W1 | `.recovery-temp/site-001-wfv2-w1-result.json` | `.recovery-temp/site-001-wfv2-w1-work/` |
| W2 | `.recovery-temp/site-001-wfv2-w2-result.json` | `.recovery-temp/site-001-wfv2-w2-work/` |
| W2S | `.recovery-temp/site-001-wfv2-w2s-result.json` | `.recovery-temp/site-001-wfv2-w2s-work/` |
| W2A | `.recovery-temp/site-001-wfv2-w2a-result.json` | `.recovery-temp/site-001-wfv2-w2a-work/` |
| W3 | `.recovery-temp/site-001-wfv2-w3-result.json` | `.recovery-temp/site-001-wfv2-w3-work/` |

**QA screenshots:** `projects/ocpilot/sites/site-001/qa/wfv2-w{1,2,2s,2a,3}-*/`

### B.9 Restore procedure (T1 → alias state)

1. Restore `header.twig` from WF-V2-W1 post-deploy source (see B.3)
2. FTP **STOR** `product.twig` + `main.css` + `media.css` from `pre-wfv2-w4-final-surface-cleanup-20260610-0447`
3. Admin: system + modification + image cache clear; modification refresh
4. Verify: markers per B.6; 8-URL matrix; W3 layout order on used PDP

**Rollback to prior wave:** use parent backup-id from chain B.4 (T1 per wave rollback plan).

**Rollback to Visual Baseline V1:** restore from `pre-w5c-commercial-stage-20260610-0002` (4 files).

**Rollback to rebrand baseline:** see section A.8.

---

## C) Cross-reference matrix

| From → To | Method |
|-----------|--------|
| Current TEST → **rebrand baseline** | T1: `pre-w5a-header-shell-20260609-2251` (+ optional `pre-w4-1-stable-20260609-1506` for PDP) |
| Current TEST → **WF-V2 experimental (W3)** | T1: composite restore B.9; or rollback W4 first if live |
| **WF-V2 experimental** → **Visual Baseline V1** | T1: `pre-w5c-commercial-stage-20260610-0002` |
| **Visual Baseline V1** → **rebrand baseline** | T1: `pre-w5a-header-shell-20260609-2251` |
| **rebrand baseline** → **Phase 1 pure** | Per-wave W1 backups + W1G DB rollback; CSS proxy `pre-w3v-20260609-0327` |

---

## D) UNKNOWN / notes

| Item | Status |
|------|--------|
| WF-V2-W4 on live TEST | **LIKELY YES** — [SITE-001-WFV2-W4-FINAL-SURFACE-CLEANUP-EXECUTION-v1.md](SITE-001-WFV2-W4-FINAL-SURFACE-CLEANUP-EXECUTION-v1.md) reports DONE; **out of scope** for alias `site-001-wfv2-final-experimental-20260610` |
| Monolithic Phase 1 file archive (`pre-phase1-*`) | **DOES NOT EXIST** on external storage — use checkpoint + per-wave backups |
| Beget full-site restore drill | **SAFE UNKNOWN** |
| Git tag `site-001-phase1-stable-2026-06` applied | **SAFE UNKNOWN** — recommended in checkpoint doc |
| Operator HITL sign-off (W1–W3) | **PENDING** |

---

## E) Registry status

| Field | Value |
|-------|--------|
| Registry ID | `SITE-001-RESTORE-POINT-REGISTRY-v1` |
| Created | 2026-06-10 |
| Site modifications | **NONE** |
| FTP / deploy | **NONE** |
| Next intended transition | WF-V3 (not authorized by this document) |

*SITE-001 Restore Point Registry v1 — audit and registry only; TEST only; no commit.*
