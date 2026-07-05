# REPORT — SITE-002 Sitemap Enable

**OCPilot run:** 4.191  
**Operation ID:** SITE-002-PROD-SITEMAP-ENABLE-01  
**Date:** 2026-07-06  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Parent checkpoint:** SITE-002-STABLE-PROD-HTML-BODY-FIX-01  
**New checkpoint:** SITE-002-STABLE-PROD-SITEMAP-01

---

## 1. Scope

Controlled enablement of valid OpenCart Google Sitemap feed plus single-line `Sitemap:` directive in `robots.txt`.

| Allowed | Forbidden (not touched) |
|---------|-------------------------|
| HTTP sitemap / robots verification | header.twig / footer.twig |
| FTP read/write `robots.txt` only | Meta / SEO title-description edits |
| OpenCart admin — Google Sitemap status enable only | Product / category content |
| Targeted feed source read-only discovery | DB direct writes |
| Backup / rollback artefacts | Cron / import / mail / Load More |

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume X label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Staged files | **none** |
| Parent checkpoint | `SITE-002-STABLE-PROD-HTML-BODY-FIX-01` |

**Foreign WIP:** FP-0002, forge-wordpress, `.recovery-temp/` — not staged, not touched.

---

## 3. Sitemap before

| URL | HTTP | Content-Type | Body | Valid XML | URL count |
|-----|------|--------------|------|-----------|-----------|
| https://bzpm.ru/sitemap.xml | 200 | text/html | 0 | **NO** | 0 |
| https://bzpm.ru/index.php?route=extension/feed/google_sitemap | 200 | text/html | 0 | **NO** | 0 |
| https://bzpm.ru/index.php?route=feed/google_sitemap | 404 | text/html | — | **NO** | 0 |
| https://bzpm.ru/sitemap_index.xml | 404 | text/html | — | **NO** | 0 |

Storage: `deployments/SITE-002-PROD-SITEMAP-ENABLE-01/sitemap-before/`

---

## 4. Robots before

| Field | Value |
|-------|-------|
| HTTP | 200 `text/plain` |
| SHA-256 (FTP) | `9fe056f7a2d84112ce053d20083537ef245d8bf083d41c0273058ccec701a9d8` |
| Run 4.188 deploy hash match | **NO** (robots evolved since 4.188; current file verified live) |
| `Sitemap:` directives | **none** |
| Size | 1554 bytes |

Backup: `backup/robots.txt`, `rollback/robots.txt`

---

## 5. Source / admin discovery

### FTP source (read-only)

| Path | Exists | Classification |
|------|--------|----------------|
| `/public_html/catalog/controller/extension/feed/google_sitemap.php` | yes | READ_ONLY |
| `/public_html/admin/controller/extension/feed/google_sitemap.php` | yes | READ_ONLY |
| `/public_html/admin/view/template/extension/feed/google_sitemap.twig` | yes | READ_ONLY |
| `/public_html/sitemap.xml` (static) | **no** | OUT_OF_SCOPE |
| Legacy route `catalog/controller/feed/google_sitemap.php` | no | OUT_OF_SCOPE |

Catalog controller checks `feed_google_sitemap_status` — when disabled, outputs **empty body** (HTTP 200).

### Admin discovery

| Field | Value |
|-------|--------|
| Google Sitemap on Feeds list | **yes** (install link present pre-enable) |
| Settings form route | `extension/feed/google_sitemap` |
| Pre-change status | **Disabled (0)** |
| Post-change status | **Enabled (1)** |
| Data feed URL | `https://bzpm.ru/index.php?route=extension/feed/google_sitemap` |

---

## 6. Root cause

| Question | Answer |
|----------|--------|
| Why empty sitemap? | OpenCart built-in Google Sitemap feed had **`feed_google_sitemap_status=0`** — controller returns no XML when disabled |
| Extension missing? | **No** — PHP controllers/templates present |
| Route wrong? | **No** — `extension/feed/google_sitemap` is correct (ocStore 3.x) |
| Static broken file? | **No** static `/public_html/sitemap.xml`; SEO URL `/sitemap.xml` routes to feed when enabled |
| Minimal fix | **PLAN A** — admin enable Google Sitemap + add `Sitemap:` to robots.txt |

---

## 7. Implementation plan

**Plan executed:** PLAN A + robots update

1. OpenCart admin — set `feed_google_sitemap_status` → **Enabled (1)** only  
2. Verify `https://bzpm.ru/sitemap.xml` and feed route return valid XML  
3. Upload prepared `robots.txt` with exactly one `Sitemap: https://bzpm.ru/sitemap.xml`  
4. No PHP/Twig deploy

---

## 8. Backup and rollback readiness

| File | Backup SHA-256 | Rollback ready |
|------|----------------|----------------|
| `/public_html/robots.txt` | `9fe056f7a2d84112ce053d20083537ef245d8bf083d41c0273058ccec701a9d8` | **YES** |

Pre-upload SHA match confirmed before robots deploy.

---

## 9. Deploy / admin action

| Action | Performed |
|--------|-----------|
| Admin save — `feed_google_sitemap_status=1` | **YES** (single setting only) |
| FTP upload `/public_html/robots.txt` | **YES** |
| Feed PHP upload | **NO** |
| Twig upload | **NO** |
| Remote deletes / renames | **0** |

---

## 10. Sitemap verification

| URL | HTTP | Content-Type | Valid | URL count | Products | Categories | Info |
|-----|------|--------------|-------|-----------|----------|------------|------|
| https://bzpm.ru/sitemap.xml | 200 | application/xml | **YES** | **1320** | yes | yes | yes |
| https://bzpm.ru/index.php?route=extension/feed/google_sitemap | 200 | application/xml | **YES** | **1320** | yes | yes | yes |

- XML root: `urlset`  
- Canonical domain: `https://bzpm.ru` only  
- No dev/staging/localhost domains detected  
- No admin/cart/checkout/account/search URLs in sample scan  
- Sample product URL: `/katalog/nejtralnoe-oborudovanie/stoly/...`  
- Sample info URLs: `/privacy-policy`, `/terms`, information routes  

**Selected robots target:** `https://bzpm.ru/sitemap.xml`

Storage: `verification/sitemap-after.json`

---

## 11. Robots verification

| Field | Value |
|-------|-------|
| HTTP | 200 |
| SHA-256 (post-deploy) | `8428d6e43b5f5cc79167504137491a4300c4fe92328768e64e860db13a2b6d40` |
| `Sitemap:` count | **1** |
| Sitemap URL | `https://bzpm.ru/sitemap.xml` |
| Prior Disallow/Allow rules | **preserved** |
| Crawl-delay / Host | **not added** |

---

## 12. Site spot check

| URL | HTTP | body×1 | Metrika | Webmaster |
|-----|------|--------|---------|-----------|
| https://bzpm.ru/ | 200 | yes | yes | yes |
| https://bzpm.ru/katalog/nejtralnoe-oborudovanie | 200 | yes | yes | yes |
| https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly | 200 | yes | yes | yes |
| https://bzpm.ru/guarantee | 200 | yes | yes | yes |

**All pass.**

---

## 13. Yandex / duplicate body preservation

| Check | Result |
|-------|--------|
| header.twig modified | **NO** |
| footer.twig modified | **NO** |
| Yandex.Metrika on live HTML | **present** |
| Yandex.Webmaster on live HTML | **present** |
| Duplicate `<body>` | **still fixed** (1× on all sampled URLs) |

---

## 14. Rollback status

| Artefact | Path |
|----------|------|
| robots rollback | `deployments/.../rollback/robots.txt` |
| Admin revert | Set `feed_google_sitemap_status=0` in admin (documented) |

**Rollback not required** — operation verified PASS.

---

## 15. Remote mutation summary

| Class | Count |
|-------|-------|
| Remote uploads | **1** |
| Remote overwrites | **1** (`robots.txt`) |
| Remote deletes | **0** |
| Remote renames | **0** |
| Admin saves by Cursor | **1** (Google Sitemap status enable only) |
| DB direct operations | **0** |
| Twig/header/footer changes | **0** |
| Yandex.Metrika/Webmaster changes | **0** |
| Duplicate body/header changes | **0** |
| Meta changes | **0** |
| Product/PDP changes | **0** |
| Cron/import changes | **0** |
| Mail changes | **0** |
| Cache clears | **0** |

---

## 16. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-SITEMAP-ENABLE-01\`

Subfolders: `source\`, `prepared\`, `backup\`, `rollback\`, `verification\`, `sitemap-before\`, `sitemap-after\`, `robots-before\`, `robots-after\`, `admin-evidence\`, `manifests\`, `logs\`

Checkpoint storage: `production/baselines/SITE-002-STABLE-PROD-SITEMAP-01\`

---

## 17. Authority updates

- [OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md) — Run 4.191  
- [OCPILOT-STATE.md](../../OCPILOT-STATE.md)  
- [production-profile.md](../production-profile.md)  
- [site-passport.md](../site-passport.md)  
- [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)  
- Baseline [SITE-002-STABLE-PROD-SITEMAP-01.md](../baselines/SITE-002-STABLE-PROD-SITEMAP-01.md)

---

## 18. Git status

Repository files from this operation staged selectively after report/checkpoint (see task closeout).

---

## 19. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Legacy route `feed/google_sitemap` | 404 — expected; not used |
| Some information URLs use `index.php?route=information/information` in sitemap | OpenCart default feed behaviour — **not modified** |
| Extension install button visible pre-enable | Install not required — enable on settings form sufficient |

**No blockers.**

---

## 20. Final verdict

**SITE-002 SITEMAP ENABLE COMPLETE — VALID XML SITEMAP VERIFIED**

---

## 21. Next task recommendation

Proceed with **`SITE-002-PROD-SEO-META-FIX-01`** — non-product meta fixes per Run 4.188 audit plan (separate scoped operation).
