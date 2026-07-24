# REPORT — ISEO-SU SITE OPS COMPLETE PRODUCTION ARCHITECTURE AND ROUTE KNOWLEDGE CAPTURE

**Task ID:** ISEO-SU-SITE-OPS-COMPLETE-PRODUCTION-ARCHITECTURE-ROUTE-KNOWLEDGE-CAPTURE  
**Date:** 2026-07-24  
**Mode:** Read-only production discovery + documentation persistence  
**Final decision:** **ARCHITECTURE KNOWLEDGE READY FOR SITE WORK**  
**Final status:** **COMPLETE — ARCHITECTURE KNOWLEDGE READY / PROJECT BRAIN PERSISTED**

---

## 1. Execution Summary

One consolidated read-only architecture discovery completed for https://i-seo.su/. Evidence sources correlated: public HTTP/REST, SFTP filesystem, Playwright WordPress Admin (no saves). Knowledge package created/updated under `projects/iseo-su-site-ops/`. Production unchanged. WPilot bridge/writes remained disabled; no REST invoked. One scoped project-brain Git commit prepared as authorized.

Ordinary site work no longer requires a generic onboarding phase — use the Task Routing Guide + Route Ownership Matrix after a fresh Beget backup and a concrete task.

---

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` label **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| HEAD (pre-commit) | `f0a79f07e3b8d3ce52a7b92d30b1bdbe4dadfc07` (`f0a79f07`) |
| Upstream | `origin/mars/canonical-post-recovery` |
| Ahead/behind (local knowledge) | ahead 23 / behind 62 vs origin (no pull/push performed) |
| Staged before task | empty |
| Access files present + ignored | `local/sites/iseo-su-production/secrets.local.md`, `site-profile.json` |
| Foreign WIP | Present across other projects — **preserved** |

---

## 3. Evidence Sources

| Source | Use |
|--------|------|
| Public GET probes | Bounded route set (status, final URL, title, generator, markers) |
| Public REST `/wp-json/` | Site, pages, posts sample, categories, types, namespaces |
| SFTP read-only | Docroot listing, theme templates/parts, handlers, `js/common.js`, robots/sitemaps, plugin dirs |
| Playwright WP Admin | Login; Plugins; Pages; edit screens (no save); Offers CPT list metadata; Menus; Reading; Permalinks; ACF groups; WPilot page presence; Site Health attempt |
| Prior Phase 2B–6C-P docs | Context only; historical reports not rewritten |

Scratch evidence (gitignored): `projects/iseo-su-site-ops/_arch-knowledge-scratch/`.

---

## 4. Architecture Summary

Hybrid Beget production: WordPress root install coexists with PHP-capable marketing HTML trees and shared `css/`/`js/`. Homepage `/` is WP-routed but template-hardcoded. Blog is WordPress. Calculator/tariffs are hybrid (WP+ACF+JS+PHP handlers). Offers/CPT `offer` is the commercial-proposal technical surface. Report Hub is a sibling external surface. Dual header/footer channels (static vs theme) are confirmed.

---

## 5. Route Discovery

Bounded discovery covered homepage, home/blog parallels, blog/categories, tariff-calc, offers, marketing HTML set, services samples, report-hub, varvara-new, robots/sitemaps, false web-kp paths, and `sitemap-static.xml` (71 URLs). No unrestricted crawl.

---

## 6. Route Classification Results

Major surfaces classified into: `STATIC_HARDCODED`, `WORDPRESS_CONTENT`, `WORDPRESS_TEMPLATE_STATIC_LIKE`, `HYBRID_COMPOSITE`, `REDIRECT_OR_ALIAS`, `LEGACY_OR_PARALLEL`, `SAFE_UNKNOWN`, `EXTERNAL_SIBLING`. Full table in `ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md`.

---

## 7. Homepage

| Fact | Value |
|------|-------|
| Front page | page 1732 `glavnaya` |
| Template | `page-home.php` |
| Editor content | unused (length 0) |
| ACF on page | 0 fields |
| Chrome | hardcoded in template; shared `/css` `/js` |
| `home.html` | public 200; LEGACY_OR_PARALLEL drift twin |

---

## 8. Blog

| Fact | Value |
|------|-------|
| Hub | `/blog` page 1730 / `page-blog.php` |
| Posts page setting | not set |
| Permalink | `/blog/%postname%.html` |
| Single | `single.php` + ACF «Записи» |
| Categories | live under `/blog/category/{slug}` |
| Parallel | `blog.html` not live renderer |

---

## 9. Static and PHP Marketing Pages

Root and `services/`/`cases/` HTML are STATIC_HARDCODED, PHP-capable, shared-asset consumers, duplicated chrome. Form posts go to `*__FORM.php` (root and service copies). `/services.html` showed one intermittent 500 then 200 — noted as U-047.

---

## 10. WordPress Surfaces

Four public pages; active theme `iseoblog`; ACF PRO with four field groups; plugins active/inactive matrix captured; Yoast sitemap index includes static sitemap; WPilot active with safe defaults.

---

## 11. Hybrid Surfaces

`/tariff-calc`, homepage calculator/tariff embeds, and shared JS+handlers+theme parts are HYBRID_COMPOSITE. Dual chrome is the primary cross-channel risk.

---

## 12. Forms, Calculators, and Web-KP

Forms mapped structurally (JS endpoints + handlers + mail()). Calculator owned by ACF + `tarif-calc.php` + `common.js` + handlers. Web-KP public paths `/web-kp`/`/kp` are 404; technical system = `/offers` + CPT `offer` + ACF «Предложения» + `single-offer.php` (private; titles not harvested).

---

## 13. Shared Components and Assets

Documented in `ISEO-SU-GLOBAL-COMPONENT-DEPENDENCY-MAP-v1.md`: dual header/footer, shared CSS/JS blast radius, menus mixed with hardcoded topbar, contact details hardcoded multi-file.

---

## 14. Ownership Model

Operator: Андрей. Runtime SoT is production files + WP DB/ACF as mapped. Historical freelancer attribution beyond operator-known facts left SAFE UNKNOWN. Report Hub remains sibling-owned.

---

## 15. Protected Zones

Updated with architecture evidence: shared css/js, FORM handlers, calculator/ACF, offers/KP, dual chrome, analytics verification files, htaccess/wp-config, core, uploads, local token, RC5 rollback dir.

---

## 16. Task Routing Readiness

`ISEO-SU-TASK-ROUTING-GUIDE-v1.md` covers text, SEO, static layout, WP pages, blog, header/footer, menu, form, calculator/tariff, ACF, web-KP, CSS/JS, image, redirect, plugin, analytics, emergency repair.

**Verdict:** usable for ordinary site work.

---

## 17. Knowledge Files Created or Updated

**Created:**

- `ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md`
- `ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md`
- `ISEO-SU-PAGE-TO-SOURCE-MAP-v1.md`
- `ISEO-SU-WORDPRESS-OBJECT-AND-TEMPLATE-MAP-v1.md`
- `ISEO-SU-STATIC-PHP-FILE-OWNERSHIP-MAP-v1.md`
- `ISEO-SU-FORMS-CALCULATORS-AND-WEB-KP-MAP-v1.md`
- `ISEO-SU-GLOBAL-COMPONENT-DEPENDENCY-MAP-v1.md`
- `ISEO-SU-TASK-ROUTING-GUIDE-v1.md`
- `ISEO-SU-SITE-ROUTE-REGISTER-v1.md`
- this REPORT

**Updated:**

- `OPERATIONAL-INDEX.md`
- `ISEO-SU-STATIC-WP-BOUNDARY-MAP-v1.md`
- `ISEO-SU-HYBRID-SOURCE-OF-TRUTH-MATRIX-v1.md`
- `ISEO-SU-REMOTE-FILESYSTEM-INVENTORY-v1.md`
- `ISEO-SU-WORDPRESS-INVENTORY-v1.md`
- `ISEO-SU-PROTECTED-ZONES-v1.md`
- `ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md`
- `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`

Historical Phase reports: **not rewritten**.

---

## 18. Remaining SAFE UNKNOWN

Named in SAFE UNKNOWN register (PHP runtime, web-KP nickname confirmation, SMTP path, offline SoT, intermittent services.html 500, ACF location export detail, offers listing UX nuance, varvara business role, WPilot 6D items). **None block ordinary classified site work.**

---

## 19. Production Boundary Validation

| Check | Result |
|-------|--------|
| Remote file changed | **No** |
| WordPress object changed | **No** |
| WP Admin form saved | **No** |
| Plugin state changed | **No** |
| Bridge enabled | **No** (remains disabled) |
| Writes enabled | **No** |
| `dev_confirmed` enabled | **No** |
| Token changed | **No** (local-only unchanged) |
| WPilot REST invoked | **No** |
| Public form submitted | **No** |
| Email triggered | **No** |
| Cache purged | **No** |
| Database accessed | **No** |

---

## 20. Git Persistence

Scoped commit (no `git add .` / `-A` / pathspec directory dump; explicit file paths only; no push; no amend).

| Field | Value |
|-------|-------|
| Subject (project-brain) | `docs(iseo-su): complete production architecture knowledge base` |
| Commit hash (full) | `3a934926e30bde3c3244203881b68e93629763df` |
| Commit hash (short) | `3a934926` |
| Committed file count | **18** |
| Follow-up (REPORT hash fill only) | `03a44add` — `docs(iseo-su): record architecture knowledge persistence commit hash` (1 file) |
| Paths (brain commit) | see post-commit path list below |
| Staged index after commits | empty |
| Push | **not performed** |
| Secrets committed | **No** |
| Scratch/local secrets | **Not staged** |
| Foreign WIP | preserved (a mistaken mixed staging attempt was soft-reset and never left on branch tip) |

---

## 21. Foreign WIP

Unrelated modified/untracked files outside this allowlist were left untouched.

---

## 22. Final Decision

**ARCHITECTURE KNOWLEDGE READY FOR SITE WORK**

Major public surfaces classified; sources of truth mapped; task routing guide usable; remaining unknowns do not block ordinary work.

---

## 23. Operator Review

Please review the knowledge package and this REPORT. No production changes were made.

---

## 24. Next Operational Step

1. Operator creates a fresh full Beget backup before the first real production task.  
2. Operator provides the concrete site task.  
3. MARS uses `ISEO-SU-TASK-ROUTING-GUIDE-v1.md` and the route ownership matrix.  
4. No additional generic onboarding is required.

---

## 25. Stop Condition

- production unchanged  
- project architecture knowledge persisted  
- no push  
- WPilot bridge remains disabled  
- writes remain disabled  
- token remains local-only  
- wait for operator review and the first real site task  

---

*REPORT · ISEO-SU architecture route knowledge capture · 2026-07-24.*
