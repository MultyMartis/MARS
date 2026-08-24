# ISEO-SU CURRENT STATE v1

**Programme:** ISEO-SU-SITE-OPS  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  
**Updated:** 2026-08-24 (STATIC SITEMAP COMPLETENESS FIX 01)  
**Authority rank:** primary project brain for ordinary next tasks

---

## 1. Project Status

**COMPLETE — ISEO-SU STATIC SITEMAP COVERAGE RECONCILED / HIGH FIX WAVE 01 TECH HEALTH RETAINED / FORMS HARDENED / METRIKA IP PARAM ACTIVE**  
**Static sitemap completeness fix 01:** **CLOSED** — SEO-supplied 54 missing public URLs validated and added; +2 legal pages from broader reconciliation; static sitemap **71 → 127**; generator completeness gate added. See `ISEO-SU-STATIC-SITEMAP-COMPLETENESS-FIX-EVIDENCE-v1.md`.  
**HIGH FIX WAVE 01:** **CLOSED** (technical) — root `/sitemap.xml` repaired; initial allowlist generator shipped with **incomplete coverage** (historical fact retained); theme relative `img/` → `/img/`. See `ISEO-SU-HIGH-FIX-WAVE-01-EVIDENCE-v1.md`.  
**All-forms isolated mail acceptance:** **COMPLETE** (historical) — Acceptance 02 proved correct operator mailbox delivery; typo `im.work@nail.ru` removed.  
**Form recipient restore verification:** **COMPLETE** (historical) — see `ISEO-SU-FORM-RECIPIENT-RESTORATION-EVIDENCE-v1.md`.  
**Operator recipient removal:** **COMPLETE** — `im.work@mail.ru` intentionally removed from production recipients; active set = `nikel007i33@yandex.ru` only; `test_mode` OFF; see `ISEO-SU-FORM-OPERATOR-RECIPIENT-REMOVAL-EVIDENCE-v1.md`.  
**Tech/SEO audit (read-only):** **COMPLETE** — two HIGH items closed by WAVE 01; static completeness post-review defect closed by completeness fix 01; MEDIUM/LOW/REVIEW backlog remains.  
**Metrika visitor IP param addon:** **ACTIVE / ENABLED** — analytics-only; parameter `ipaddress` → counter **54287016**; kill switch `production-source/metrika-ip/metrika-visitor-ip-config.php` (`"enabled"`); IP blocking remains **manual / out of scope**. See `ISEO-SU-METRIKA-VISITOR-IP-PARAM-BASELINE-v1.md`.  
**Form HMAC secret remediation:** **COMPLETE** — active HMAC secret rotated, removed from current tracked source, moved to production-local PHP authority under protected runtime path, and validated with isolated test mode. See `ISEO-SU-FORM-HMAC-SECRET-ROTATION-EVIDENCE-v1.md`.

Glossary/site-ops stabilization remains accepted. Public form anti-spam/validation charter is **closed**. Ordinary future work starts from this file + Task Routing Guide + Protected Zones + Form Security Baseline.

## 2. Production Status

| Field | Value |
|-------|-------|
| Site | `https://i-seo.su/` |
| Glossary public | **healthy / accepted** |
| `/glossary/` | HTTP **200** |
| Active site blocker | **none** |
| Production mutations in form anti-spam task | **YES** (bounded form/security/JS only) |
| Current HMAC authority | production-local PHP file under protected `.iseo-form-runtime/` |

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
| Canonical root `/sitemap.xml` | **sitemapindex** → `sitemap-static.xml` + `wp-sitemap.xml` (HIGH FIX WAVE 01) |
| `sitemap-static.xml` | **71** URLs; allowlist generator `tools/generate-sitemap-static.py` |
| Yoast/wp-sitemap glossary | **184** URLs (via `/wp-sitemap.xml`) |
| Custom root index | **0** glossary URLs — intentional (WP owns glossary) |
| robots.txt Sitemap | `https://i-seo.su/sitemap.xml` |
| Architecture note | `ISEO-SU-SITEMAP-ARCHITECTURE-AND-CURRENT-STATE-v1.md` |
| Archive Yoast meta description | **absent** — optional polish only |

## 8. Production Source Authority

| Artifact | Path |
|----------|------|
| Shared CSS SoT in MARS | `production-source/css/main.css` |
| Shared forms JS SoT | `production-source/js/common.js` (includes Metrika IP loader hook) |
| Shared forms config / loader SoT | `production-source/forms/iseo-form-config.php`, `production-source/forms/iseo-form-security.php`, `production-source/forms/iseo-form-token.php` |
| Metrika visitor IP addon | `production-source/metrika-ip/` |
| Sitemaps SoT | `production-source/sitemaps/` + `data/sitemaps/sitemap-static-urls-v1.txt` |
| Theme img-path SoT (homepage/cases/recommendations) | `production-source/theme/iseoblog/` |
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

## 10a. Form HMAC Secret Authority

- Current tracked source contains **no active HMAC secret literal**.
- Runtime HMAC authority is a **production-local PHP file** at protected path `.iseo-form-runtime/iseo-form-secrets.local.php`.
- Missing secret file must **fail closed** for HMAC-protected submission behavior; no hardcoded default secret is permitted.
- Historical Git commits may still contain a **revoked** prior secret value; rotation removed current operational risk without history rewrite.

## 11. Backup / Rollback Posture

- Beget full backup required before any production mutation.
- Glossary publication / batch rollback docs remain in-repo (canonical).
- Production CSS overflow backup stamp: `css/main.css.bak-glossary-overflow-20260818T101846Z` (remote).
- Current HMAC rotation rollback receipts / scoped backups: `X:\AI MARS\local\sites\iseo-su-production\_hmac-rotation-01\`.
- HIGH FIX WAVE 01 deploy/rollback: `X:\AI MARS\local\sites\iseo-su-production\_high-fix-wave-01\`.
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
4. Custom `sitemap.xml` glossary duplication — **NOT RECOMMENDED** (root index already points at `wp-sitemap.xml`; do not duplicate glossary into static sitemap)  
5. WPilot Phase 6D bridge + read-only smoke (exact approval lines required)
6. MEDIUM / LOW / REVIEW tech-SEO backlog (separate charter)

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
