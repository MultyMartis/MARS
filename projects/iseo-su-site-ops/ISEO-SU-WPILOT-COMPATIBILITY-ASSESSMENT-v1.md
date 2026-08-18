# ISEO-SU WPILOT COMPATIBILITY ASSESSMENT v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** PHASE 4B  
**Date:** 2026-07-24  
**Basis:** Phase 2B production architecture + static WPilot RC5 source/package audit  
**Decision input:** **CONDITIONAL GO** (see §13)

---

## 1. Site Baseline

| Fact | Value | Confidence |
|------|-------|------------|
| Site | `https://i-seo.su/` | High |
| Hosting | Beget; production only | High |
| WordPress | Root install in shared docroot; **7.0.2** | High |
| Theme | `iseoblog` custom; no child theme | High |
| Architecture | Hybrid WP + PHP-capable static HTML + shared `css/` `js/` | High |
| Homepage | WP page + `page-home.php`; parallel `home.html` | High |
| Blog | `/blog/` WordPress-owned | High |
| WPilot | Absent | High |
| Staging | Absent | High |
| Dedicated MARS WP admin | Exists (local-only; username not recorded here) | High |
| Backup policy | Fresh full Beget backup before every production task | Operator policy |

---

## 2. WordPress Compatibility

| Check | Assessment |
|-------|------------|
| WP 7.0.2 vs plugin APIs | Source uses standard WP REST, options, `$wpdb`, `dbDelta`, `get_posts`, plugin APIs — **no deprecated-API blockers identified in static review** |
| Header `Requires at least` / `Tested up to` | **Missing** → version contract **incomplete** |
| Multisite | Site not multisite; plugin has no MS install path beyond reporting |

**Verdict:** Technically plausible; contract incomplete → **condition**, not NO-GO by itself.

---

## 3. PHP Compatibility

| Check | Assessment |
|-------|------------|
| Runtime PHP on i-seo.su | **SAFE UNKNOWN** (Phase 2B) |
| Floor from co-resident plugins/core | ≥ 7.4 indicated by WP/ACF/Yoast headers |
| Plugin `Requires PHP` | **Absent** |
| Local `php -l` | **SAFE UNKNOWN** — PHP binary unavailable on agent host |

**Verdict:** Not a proven incompatibility; must capture PHP via Admin/Site Health or authenticated `site-info` after activation (GATE 6B/6D). Pre-install condition: operator accepts deferred capture.

---

## 4. Theme Compatibility

| Check | Assessment |
|-------|------------|
| `iseoblog` | WPilot does not mutate theme files |
| No child theme | N/A for CSS-patch patterns proven elsewhere |
| `page-home.php` full HTML templates | **Critical boundary:** page `post_content` edits may **not** change rendered marketing homepage if template ignores content |

**Verdict:** Compatible for plugin presence; **unsafe to assume** homepage visual edits via WPilot without separate content/template analysis.

---

## 5. Plugin Compatibility

| Plugin | Presence | WPilot interaction risk |
|--------|----------|-------------------------|
| ACF PRO 6.3.10 | On disk | No ACF API in WPilot — do not use WPilot for ACF |
| Yoast 28.0 | Present | Read coexistence expected; no Yoast write API |
| Jetpack 14.8 | Present | Possible rate-limit/WAF/challenge on automation |
| WP-Optimize | Present | Cache may hide content changes until purge (manual/other channel) |
| Exact actives | SAFE UNKNOWN | Confirm via WPilot `/plugins` after authorized smoke |

No WPBakery/The7 found — WPBakery safety paths largely unused but harmless.

---

## 6. REST and Header Compatibility

| Check | Assessment |
|-------|------------|
| Public `/wp-json/` | Reachable (Phase 2B) |
| Custom `X-WPilot-Token` forwarding | **SAFE UNKNOWN** until GATE 6D |
| Admin JS challenge | Observed for non-browser Admin clients — may or may not affect REST |

**Verdict:** Install may proceed only with fail-closed REST smoke later; do not assume header survival.

---

## 7. Cache and Security Compatibility

WP-Optimize / Jetpack / possible host WAF: treat as **risk amplifiers** for false negatives/positives during smoke. No WPilot cache-purge capability — operator must handle cache outside plugin if needed (separate charter).

---

## 8. Hybrid Architecture Boundary

WPilot may operate only on **explicitly WordPress-owned** entities (MVP: `page` `post_content`).

Must **not** mutate via WPilot:

- static HTML (`home.html`, `services/`, etc.)
- shared `css/` / `js/`
- calculator / tariff PHP handlers / `/tariff-calc`
- web-KP unresolved files
- theme templates
- ACF options
- forms / mail
- routing / `.htaccess`

Parallel homepage files mean WPilot success on a WP page ID ≠ marketing HTML file update.

---

## 9. Custom Tools Protection

| Surface | Protection posture |
|---------|-------------------|
| Calculator + tariffs | PROTECTED — out of WPilot scope |
| Forms / mail handlers | PROTECTED |
| CPT `offer` / web-KP candidates | PROTECTED / unresolved ownership |
| Report Hub tree | Separate programme surface |

---

## 10. No-staging Risk

All activation/smoke risk is **production-direct**. Mitigations: fresh Beget backup; separated gates; bridge/write remain off until explicit HITL; prefer unpublished draft WP page for any future write smoke.

---

## 11. Installation Risk

| Risk | Level | Mitigation |
|------|-------|------------|
| Wrong ZIP (stale v0.3.0) | Medium | SHA-256 gate |
| Wrong ZIP (RC5 vs RC6 mix-up after remediation) | Medium | Prefer RC6 SHA-256 `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` for 6C-R; keep RC5 hash for rollback identity |
| Activation creates tables/options | Medium | Pre-backup; post-check Admin/SFTP |
| Public ping discloses bridge flags | Low | Expected; no secrets |
| Operator enables write too early | High | Separated GATE 6E optional later |
| Hybrid misunderstanding | High | Boundary docs + protected zones update |

---

## 12. Required Conditions (pre-install)

1. Operator accepts package ACCEPTED MATCH (`GATE 4B-1`).  
2. Operator accepts this compatibility assessment including hybrid limits and incomplete version headers (`GATE 4B-2`).  
3. Fresh full Beget backup confirmed immediately before upload (`GATE 4B-3`).  
4. Future gates remain separated (upload ≠ activate ≠ token ≠ smoke ≠ write).  
5. PHP/header/WAF unknowns deferred only to later **read-only** gates with fail-closed stop.  
6. Production controlled writes remain **NOT AUTHORIZED** by Phase 4B.

---

## 13. Decision

**CONDITIONAL GO** for eventual install packaging suitability.

Not GO: residual mandatory operator conditions + incomplete PHP/version contract + production-only/no-staging risk acceptance required.  
Not NO-GO: package exact; defaults safe; no material static security blocker found for install/activate-with-bridge-off posture.

---

## 14. SAFE UNKNOWN

- Exact PHP runtime  
- Exact active plugin set  
- `X-WPilot-Token` host forwarding  
- Interaction of Admin JS challenge with REST clients  
- Cache behavior after future content writes  
- Web-KP exact URL/ownership  
- Beget restore drill proof  
- Live production behavior of RC6 until GATE 6C-R  

---

## 15. Phase 4C / RC6 note (2026-07-24)

Token-generation gate conflict observed in Phase 6C is remediated in WPilot **v0.3.0-RC6** (source + package). Compatibility CONDITIONAL GO for RC5 install remains historical. For update-only remediation use RC6 SHA-256 above; do not silently replace the accepted RC5 identity records.

*Compatibility assessment v1 · 2026-07-24 · addendum Phase 4C / RC6.*
