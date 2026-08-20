# ISEO-SU CURRENT STATE v1

**Programme:** ISEO-SU-SITE-OPS  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  
**Updated:** 2026-08-20 (final stabilization / housekeeping)  
**Authority rank:** primary project brain for ordinary next tasks

---

## 1. Project Status

**COMPLETE — ISEO-SU SITE OPS STABILIZED / WORKSPACE CLEAN / MARS BRAIN CURRENT / GIT CLOSED**

Glossary/site-ops production work is **accepted**. No active launch or publication programme remains open. Ordinary future work starts from this file + Task Routing Guide + Protected Zones.

## 2. Production Status

| Field | Value |
|-------|-------|
| Site | `https://i-seo.su/` |
| Glossary public | **healthy / accepted** |
| `/glossary/` | HTTP **200** |
| Active site blocker | **none** |
| Production mutations in stabilization task | **0** |

## 3. Architecture Authority

1. This file (`ISEO-SU-CURRENT-STATE-v1.md`)
2. `ISEO-SU-FINAL-LAUNCH-CLOSEOUT-v1.md`
3. `ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md`
4. `ISEO-SU-TASK-ROUTING-GUIDE-v1.md`
5. `ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md`
6. `ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md`
7. `ISEO-SU-PROTECTED-ZONES-v1.md`
8. `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`

Historical phase REPORTs are evidence, not current operating truth.

## 4. Glossary Final State

- Public archive + singles live.
- Hero: services-style `page_scene`; **no** `.page_scene__rates`.
- CTA **Подробнее** → `#SecondScreen`.
- Related-term block live (public eligible targets only).
- Archive title: **`Глоссарий - INTLSEO Studio`**.
- Operator manual CSS + glossary-scoped mobile overflow fix in production/`production-source/css/main.css` (SHA-256 `4a1202b6…`).
- Theme package mirror: `wordpress/iseoblog-glossary/`.

## 5. Published / Non-Public Corpus

| Bucket | Count | Public |
|--------|------:|--------|
| Published eligible canonical | **184** | yes |
| MERGED | 30 | no |
| DEFERRED | 14 | no |
| EXCLUDED | 13 | no |
| Non-eligible total | **57** | no |

Do **not** publish non-eligible without a new charter.

## 6. Navigation

| Surface | State |
|---------|-------|
| Desktop submenu | **Глоссарий** immediately after `Калькулятор SEO (free)` |
| Mobile offcanvas | **intentionally unchanged** / deferred optional |

## 7. SEO / Sitemap

| Source | State |
|--------|-------|
| Yoast/wp-sitemap glossary | **184** URLs |
| Custom `sitemap.xml` | **unchanged** (0 glossary URLs — intentional) |
| Archive Yoast meta description | **absent** — optional polish only |

## 8. Production Source Authority

| Artifact | Path |
|----------|------|
| Shared CSS SoT in MARS | `production-source/css/main.css` |
| Theme glossary package | `wordpress/iseoblog-glossary/` |
| Content corpus | `content/glossary/batch-0{1..4}/` + editorial CSV under `data/glossary-editorial/` |
| Immutable source workbook | `materials/glossary/ISEO-SU-GLOSSARY-SOURCE-NIKITA-v1.xlsx` |

## 9. Manual Runtime Edit Rule

Operator may edit production CSS/templates under a charter. Before any automated overwrite of `css/main.css`, reconcile against `production-source/css/main.css` and Protected Zones. Prefer promote-to-MARS over silent production-only drift.

## 10. WPilot State

| Field | Value |
|-------|-------|
| Accepted baseline | **PHASE 6C — TOKEN CREATED / RC6 SAFE DEFAULTS** |
| Bridge / writes / REST smoke | **DISABLED / NOT RUN** |
| Phase 6D | **BLOCKED** until exact approval + fresh backup lines |
| Blocks ordinary site work? | **No** |

Token remains **local-only** (Git-ignored).

## 11. Backup / Rollback Posture

- Beget full backup required before any production mutation.
- Glossary publication / batch rollback docs remain in-repo (canonical).
- Production CSS overflow backup stamp: `css/main.css.bak-glossary-overflow-20260818T101846Z` (remote).
- Scratch helpers relocated to Storage archive (not Git):  
  `X:\AI MARS STORAGE\archives\iseo-su-site-ops-scratch-stabilization-2026-08-20\`

## 12. Git / Remote State

| Field | Value |
|-------|-------|
| Canonical branch | `mars/canonical-post-recovery` |
| Accepted programme on remote | **yes** (closeout equivalents reachable; tip advances with other programmes) |
| Dirty main | may hold **foreign WIP** — never stage it for iseo tasks |
| Push method | clean `git-sync-*` worktree only |

## 13. Protected Zones

See `ISEO-SU-PROTECTED-ZONES-v1.md`. Default protect-all. Glossary CPT, menu topbar, shared CSS, forms, calculator, offers/web-KP, secrets remain protected.

## 14. Deferred Optional Work

Separate charters only — **not** launch blockers:

1. Mobile offcanvas glossary parity  
2. Archive Yoast meta description  
3. MERGED alias search polish  
4. Custom `sitemap.xml` glossary duplication — **NOT RECOMMENDED** unless a future requirement appears  
5. WPilot Phase 6D bridge + read-only smoke (exact approval lines required)

## 15. No-Longer-Required Work

- Glossary draft-only / 404 / publication-not-started programmes  
- Generic onboarding / architecture rediscovery as a default gate  
- Republishing the 184 eligible set  
- Ritual full production re-audit without a contradiction  
- Scratch-driven one-off import/update scripts for completed waves  

## 16. Entry Point for Next Task

1. Read this Current State.  
2. Open `OPERATIONAL-INDEX.md` → Task Routing Guide → Route Ownership Matrix.  
3. Confirm fresh Beget backup if mutating production.  
4. Execute only the chartered surface.  
5. Do not treat deferred optional items as open blockers.

---

*ISEO-SU CURRENT STATE v1 · stabilization 2026-08-20.*
