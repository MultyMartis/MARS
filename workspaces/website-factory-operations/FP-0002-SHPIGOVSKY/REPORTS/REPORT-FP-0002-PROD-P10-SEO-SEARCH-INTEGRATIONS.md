# REPORT — FP-0002 PROD-P10 SEO / Search / Integrations

**Date:** 2026-08-14  
**Evidence:** `REPORTS/evidence/prod-p10-seo-search-integrations/`  
**Rollback mode:** `PROD-P10 EXACT-FILE / EXACT-OBJECT ROLLBACK MODE`

## 1. Status

- **PARTIAL PASS** (technical closeout complete; Admin interactive visual acceptance pending due to WP `reauth` on automated login; operator visual/SEO acceptance pending)
- Production file writes: **yes** (exact allowlist + robots.txt safe fix)
- DB/Admin writes: **temporary Smart Search option QA only** (restored to code defaults; lasting product settings writes = 0)
- ACF/schema mutations: **source group added** (PHP + JSON); no broad ACF sync
- SEO safe fixes: **1** (robots Sitemap append)
- WPilot writes: **0** (`write_enabled=false` unchanged)
- Commit/push: **none**

## 2. Rollback

**PROD-P10 EXACT-FILE / EXACT-OBJECT ROLLBACK MODE**

- File snapshots: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p10-layer-b-pre\`
- After copies: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p10-prod-after\`
- DB/settings snapshots: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p10-db-snapshots\`
- Rollback ready: **YES** for all mutated files/objects

## 3. Sitemap Architecture

| Item | Result |
|------|--------|
| Existing owner | WordPress core sitemaps (were 404 under `blog_public=0`) |
| Selected implementation | Extend native via `wp_sitemaps_*` + specialists provider |
| Included types | pages, services, articles (posts), specialists |
| Exclusions | legal/system pages + Admin relationship exclusions + specialists de-duped from pages |
| Main sitemap URL | `http://shpigovsky.beget.tech/wp-sitemap.xml` |
| Child maps | posts / pages / service / specialists-1 |
| XML validation | well-formed XML index + child urlsets; published permalinks via `home_url()`/`get_permalink()` |

**GOOGLE/YANDEX-COMPATIBLE SITEMAP GENERATION LIVE**

## 4. Yandex Webmaster Integration

| Item | Result |
|------|--------|
| Official specification checked | YES |
| Official source | https://yandex.ru/support/webmaster/controlling-robot/sitemap.html |
| Separate general page/service feed applicable | **NO** |
| Implementation | Standards-compliant XML sitemap + Admin explanation/links |
| Admin | «SEO и интеграции → Sitemap» Yandex help + sitemap URLs |

```
YANDEX GENERAL PAGE/SERVICE FEED = NOT APPLICABLE UNDER CURRENT OFFICIAL SPEC
```

YML vertical feeds (realty/vacancies/doctors/…) are not a substitute for ordinary clinic page/section/service discovery.

## 5. Sitemap Admin UX

- Enable/disable sitemap
- Include toggles: pages / services / articles / specialists
- Exact object exclusions (relationship IDs)
- Clickable resulting URLs (index + children)
- Indexing vs generation status note (temporary host)

## 6. Smart Search Admin

- Groups enable: Услуги / Статьи / Специалисты / Страницы
- Min chars: 2–10 (default 3)
- Per-group limit: 1–20 (default 5)
- Group order: numeric priorities (defaults 1–4)
- Matching: title always; excerpt/extra toggle; body toggle
- Exclusions: relationship object IDs
- Admin UX: Russian labels under «Умный поиск»

**SMART SEARCH ADMIN CONFIGURATION LIVE** (code + defaults; ACF options page registered)

## 7. Smart Search Regression

| Test | Result |
|------|--------|
| Desktop/mobile shared endpoint | PASS (same REST; JS groupOrder from localize) |
| Defaults preserve P09 | PASS (`min=3`, order services→articles→specialists→pages, services hit on «алк») |
| Min-chars gate | PASS (2-char query empty) |
| Settings mutation (MySQL exact options) | PASS (min=4, articles off, exclude #74, then restored) |
| Final live config | code defaults (no lasting options_*) |

## 8. Technical SEO Audit

See `REPORT-FP-0002-PROD-P10-TECHNICAL-SEO-AUDIT.md`.

- URLs scanned: 89
- 200/405: 88/1
- Critical 0 / High 1 / Medium 6 / Low 71 / Informational 75
- SAFE TECH FIX applied: 1
- DOMAIN CUTOVER / OPERATOR DECISION dominate (expected on temporary host + demo content)

## 9. SEO Safe Fixes

| Finding | Owner | Action | Before/After | Rollback |
|---------|-------|--------|--------------|----------|
| Static robots missing Sitemap | `public_html/robots.txt` | Append Sitemap; keep Disallow:/ | Disallow-only → Disallow + Sitemap | Layer B robots snapshot |

## 10. Deferred SEO Findings

- Content/demo titles/H1/meta descriptions
- Domain cutover / noindex / Disallow / `.test` residue
- xmlrpc 405 policy
- Meta description ownership product decision

## 11. Analytics / Verification Admin

| Field | Status |
|-------|--------|
| Yandex.Metrica counter ID | LIVE (empty → no output) |
| Yandex Webmaster verification | LIVE (empty → no meta) |
| Google Search Console verification | LIVE (empty → no meta) |
| GA Measurement ID / GTM ID | LIVE optional (GTM preferred if both set) |
| Advanced head/body/footer code | LIVE (Administrator options; warning label) |
| Duplicate prevention | empty defaults; GTM vs GA preference |

**SEO / ANALYTICS / VERIFICATION ADMIN SETTINGS LIVE**

Homepage smoke: no empty verification/metrica/GTM tags with empty settings.

## 12. ACF / Settings Architecture

- New options subpage: `fp02-site-settings-seo-integrations`
- New group: `group_fp02_site_options_seo_integrations` (`SeoIntegrationsOptions`)
- Location: options_page == SEO subpage; storage `option`
- Source PHP + `WORDPRESS/acf-json/...json`
- No broad sync; existing contacts/modal/reviews groups untouched

## 13. Exact Files Changed

Theme:

- `functions.php`
- `inc/seo-integrations.php` (new)
- `inc/sitemap-helpers.php` (new)
- `inc/search-helpers.php`
- `inc/assets.php`
- `assets/js/v9-shell.js`

Plugin:

- `src/Admin/OptionsPage.php`
- `src/Fields/FieldGroups.php`
- `src/Fields/SeoIntegrationsOptions.php` (new)

ACF JSON:

- `group_fp02_site_options_seo_integrations.json` (new)

Production-only safe fix:

- `public_html/robots.txt` (Sitemap append)

## 14. DB/Admin Objects Changed

- Lasting product options: **none** (defaults via code)
- Temporary QA options (`options_smart_search_*`): written then deleted/restored — snapshot under `prod-p10-db-snapshots/`
- No secret values retained in reports

## 15. Frontend / Endpoint QA

- Sitemap index + children: **200 XML**
- Smart search REST: defaults + settings proof
- Page source integrations empty: **PASS**
- robots Disallow preserved + Sitemap line: **PASS**

## 16. P07/P08/P09 Regression

Smoke intent: no unrelated visual/CSS mutate set; Smart Search defaults preserved; Fancybox/search CSS not re-uploaded.

Residual: P08 broad WYSIWYG typography out of scope (unchanged).

Matrix note: `evidence/.../P07-P08-P09-REGRESSION.md`

## 17. Source / Production Parity

**10/10 SOURCE ↔ PRODUCTION MATCH** (allowlisted theme/plugin/acf files)

Plus production-only robots.txt (documented; rollback snapshot exists).

## 18. WPilot

- `write_enabled=false`
- business writes **0**

## 19. Migration / Domain Tails (deferred)

- `.test` broad cleanup
- blogname
- WP_DEBUG / WP_ENVIRONMENT_TYPE
- final home/siteurl
- HTTPS / DNS
- final-domain SEO cutover / indexing enable

## 20. Secret Safety

- exposed in reports: **0**
- tracked secrets: **0**
- no live verification/tracking IDs stored in evidence

## 21. Git

- commit: none
- push: none
- foreign WIP: untouched

## 22. Acceptance

**PROD-P10 TECHNICAL CLOSEOUT COMPLETE — OPERATOR VISUAL/SEO ACCEPTANCE PENDING**

Admin interactive form render: **PARTIAL** this wave (Beget/WP `reauth` blocked automated `mars` login; submenu slug registered on production code). Operator should open:

`Настройки сайта → SEO и интеграции`

## 23. Next Recommendation

1. Operator visual accept Admin SEO tabs + fill real Metrica/verification IDs when ready.
2. Keep indexing closed until `shpigovsky.ru` cutover; then enable visibility and resubmit sitemap to Google/Yandex.
3. Editorial meta-description ownership decision.
4. Do not invent a Yandex “pages/services feed” — continue with XML sitemap.
