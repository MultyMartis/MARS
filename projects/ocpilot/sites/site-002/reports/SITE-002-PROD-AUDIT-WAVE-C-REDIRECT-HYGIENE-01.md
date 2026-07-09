# REPORT — SITE-002 Audit Wave C Redirect Hygiene

**Operation:** `SITE-002-PROD-AUDIT-WAVE-C-REDIRECT-HYGIENE-01`  
**OCPilot run:** 4.242  
**Date:** 2026-07-10  
**Environment:** https://bzpm.ru/ (Production — verification only, **no mutation**)  
**Baseline (unchanged):** `SITE-002-STABLE-PROD-CRON-RUN-REPORTS-DURATION-FIX-01`  
**Related audit:** Run 4.241 — `SITE-002-PROD-FULL-TECH-SEO-AUDIT-01` (AUDIT-006)

---

## 1. Scope

Controlled redirect hygiene verification after Full Tech SEO Audit Run 4.241.

| Target | Intent |
|--------|--------|
| **AUDIT-006** (primary) | Confirm flat Lari URLs **301** → nested canonical paths |
| **AUDIT-010** (secondary) | Confirm bare `/index.php` alias behavior; do not break `index.php?route=...` |

**Allowed:** HTTP GET/HEAD, read-only DB SELECT, read-only FTP download, rollback bundle prep, docs.  
**Forbidden:** DB writes, import/monitor, admin saves, broad redirect rewrites, `/contact`/`/kontakty` changes.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume X: label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `7457e50d` |
| Staged changes before task | **none** |
| Foreign WIP | Present — excluded from commit |

---

## 3. Audit issue target

### AUDIT-006 — Flat Lari URLs

Run 4.241 flagged flat `/katalog/nejtralnoe-oborudovanie/lari` tree as **200 + canonical nested** (duplicate URL hygiene).

**Root cause of audit false positive:** audit crawler (`urllib.request.urlopen`) **auto-follows redirects** and recorded final **200** at nested URL while attributing status to the requested flat URL. Curl with `--max-redirs 0` shows true first-hop behavior.

### AUDIT-010 — Homepage `/index.php` alias

Optional secondary check for bare `/index.php` duplicate homepage access.

---

## 4. Before HTTP verification

Tool: `site-002-prod-audit-wave-c-redirect-hygiene-01.py` (curl-based, no auto-follow).  
Storage: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-AUDIT-WAVE-C-REDIRECT-HYGIENE-01\http-before\`

| URL | Status (no-follow) | Location | Pass |
|-----|-------------------|----------|------|
| `/katalog/.../shkafy-i-lari/lari` (nested) | **200** | — | yes |
| `/katalog/.../lari` (flat parent) | **301** | `.../shkafy-i-lari/lari` | yes |
| `/katalog/.../shkafy-i-lari/lari/skladskie-lari` | **200** | — | yes |
| `/katalog/.../lari/skladskie-lari` (flat) | **301** | `.../shkafy-i-lari/lari/skladskie-lari` | yes |
| `/katalog/.../shkafy-i-lari/lari/proizvodstvennye-lari` | **200** | — | yes |
| `/katalog/.../lari/proizvodstvennye-lari` (flat) | **301** | `.../shkafy-i-lari/lari/proizvodstvennye-lari` | yes |
| `/` | **200** | — | yes |
| `/index.php` (bare) | **301** | `/` | yes |
| `/index.php?route=information/contact` | **301** | `/contact` | yes |
| `/index.php?route=extension/feed/google_sitemap` | **200** | — | yes |

**Stability:** `/contact` 200; `/kontakty` 404 (accepted); sitemap/robots/llms 200; **0** public `БЗПМ`.

**Minor note:** Lari 301 `Location` headers use `http://` scheme (server default); clients upgrade to HTTPS. Not a functional blocker.

---

## 5. Source authority

Read-only FTP mirrors captured under `source-before/`.

| Remote path | Lari redirect logic | Index redirect logic | Will modify |
|-------------|--------------------|-----------------------|-------------|
| `/public_html/.htaccess` | **yes** — Run 4.235 rules | indirect (OpenCart rewrite) | **no** |
| `seo_url.php` | canonical path v2 | route handling | **no** |
| `seo_pro.php` | category path | — | **no** |
| `category.php` | link generation | — | **no** |
| `category_visibility.php` | hub links | — | **no** |

Active `.htaccess` block (Run 4.235):

```apache
# SITE-002 lari reparent redirects (SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01)
RewriteRule ^katalog/nejtralnoe-oborudovanie/lari/(.+)$ /katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/$1 [R=301,L]
RewriteRule ^katalog/nejtralnoe-oborudovanie/lari/?$ /katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari [R=301,L]
```

Bare `/index.php` → `/` redirect is handled by existing OpenCart/SEO layer (not added in this run).

---

## 6. DB read-only cross-check

| Check | Result |
|-------|--------|
| Category **88** `parent_id` | **358** (PASS) |
| `category_path` 88/140/141 | Nested under 79→358→88 |
| SEO keywords | `lari`, `skladskie-lari`, `proizvodstvennye-lari` — no duplicates |
| Duplicate lari keywords | **none** |

Artefacts: `db-readonly/lari-structure-crosscheck.*`

---

## 7. Patch plan and rollback

**Decision: NO-OP — deploy not required.**

All flat Lari URLs already return **301**. Bare `/index.php` already **301** to `/`. Route query URLs remain functional.

Rollback bundle prepared from `source-before/` mirrors (pre-emptive; not used).

---

## 8. Dry-run gates

All gates **PASS** (G1–G15). See `manifests/dry-run-gates.json`.

Deploy skipped — gates satisfied for no-op path.

---

## 9. Controlled deploy

**Not executed.** 0 FTP uploads. 0 remote overwrites.

---

## 10. After HTTP verification

Post-verification matches before state (no mutation). All target URLs pass.

Artefacts: `http-after/redirect-targets-after.*`, `verification/after-http-verification.*`

---

## 11. Regression verification

14 bounded URLs checked — **0 failures**, **0** HTTP 500, **0** public `БЗПМ`.

Artefacts: `verification/regression.*`

---

## 12. Production mutation summary

| Action | Count |
|--------|------:|
| Remote uploads | 0 |
| Remote overwrites | 0 |
| Remote deletes | 0 |
| FTP writes | 0 |
| FTP reads/listings | 5 (read-only; cached from prior run in tool re-execution) |
| DB SELECTs | 4 |
| DB direct writes | 0 |
| Admin saves | 0 |
| Import runs triggered | 0 |
| Monitor runs triggered | 0 |
| Redirect changes | 0 (already active from Run 4.235) |
| Sitemap / robots / llms changes | 0 |
| Header/footer/Yandex changes | 0 |
| Cache clears | 0 |
| public БЗПМ introduced | no |

---

## 13. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-AUDIT-WAVE-C-REDIRECT-HYGIENE-01\`

- `http-before/`, `http-after/`
- `source-before/`
- `db-readonly/`
- `patch/`, `rollback/`
- `manifests/operation.json`, `dry-run-gates.*`, `source-authority-map.*`
- `verification/regression.*`, `after-http-verification.*`
- `logs/run-summary.json`

---

## 14. Authority updates

- `OPERATIONAL-INDEX.md` — Run 4.242 entry
- `OCPILOT-STATE.md` — AUDIT-006 resolved (no-op confirmation)
- `production-profile.md`, `site-passport.md`, `SITE-002-TECHNICAL-KNOWLEDGE-MAP.md`, `tools/README.md`

**Checkpoint:** unchanged `SITE-002-STABLE-PROD-CRON-RUN-REPORTS-DURATION-FIX-01` (no production mutation).

---

## 15. Git status

Selective commit of operation report + authority docs + tool only. Foreign WIP excluded. Storage not committed.

---

## 16. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Post-1C Lari reparent persistence (Run 4.240) | **still BLOCKED** — next import not observed; unrelated to redirect hygiene |
| TXT Duration fix confirmation (Run 4.239) | **pending** next import |
| Lari 301 Location `http://` scheme | minor cosmetic; optional future polish |
| AUDIT-007 legacy `index.php?route=information` in sitemap | **deferred** — Wave B |

---

## 17. Final verdict

**SITE-002 AUDIT WAVE C REDIRECT HYGIENE COMPLETE — NO-OP, ISSUE ALREADY RESOLVED**

Flat Lari URLs **301** → nested canonical paths (Run 4.235 `.htaccess`). Bare `/index.php` **301** → `/`. AUDIT-006 closed. AUDIT-010 homepage/index.php alias **resolved** for bare path; sitemap legacy information URLs remain Wave B.

---

## 18. Next task recommendation

1. **`SITE-002-PROD-POST-1C-LARI-REPARENT-AND-DURATION-VERIFICATION-01` (repeat)** — when next scheduled 1C import occurs (Run 4.240 gate).
2. **`SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01`** — legacy `index.php?route=information/...` sitemap entries; `compare-products`/`wishlist` SEO keyword duplicates (AUDIT-004/007).
3. Optional: **`SITE-002-PROD-CONTACT-SITEMAP-INCLUSION-01`** — add `/contact` to sitemap (AUDIT-002 P3).
