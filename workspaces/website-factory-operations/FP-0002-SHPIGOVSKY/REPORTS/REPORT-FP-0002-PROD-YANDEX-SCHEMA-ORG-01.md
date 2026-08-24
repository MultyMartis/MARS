# REPORT — FP-0002 YANDEX SCHEMA.ORG STRUCTURED DATA 01

## 1. Verdict

**PASS_WITH_ATTENTION**

Core structured-data system is live on production, JSON-LD validates, canonical URLs are correct, robots/indexing preserved, and no fabricated ratings/geo/Product/Offer/Physician misuse detected. Attention items: authenticated Yandex Webmaster validator not executed in this session; production still has **no Open Graph** (pre-existing, unchanged); child institutional pages under `/o-centre/` remain generic `WebPage` while the about hub `/o-centre/` uses `AboutPage` (intentional/truthful).

---

## 2. Current-origin preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` on volume `X:` / `AI WS` |
| Worktree | `X:\AI MARS\worktrees\fp0002-yandex-schema-01` |
| Branch | `mars/canonical-post-recovery` |
| Remote SHA (preflight + post) | `1c9e92ed90a495000e2be4a022dcb40dda9abfbc` |
| Foreign WIP | Main repo dirty — bypassed via clean worktree |
| Staged pre-commit | Empty |

---

## 3. Fresh production / Olya intake

- **robots.txt** captured pre/post deploy: SHA256 `6157B0529C95CA6299BFD994C9F63C0B4F2B95A8CFA8CACBEC81181723E981FF` (151 lines) — **unchanged**.
- **Indexing:** `blog_public=1` confirmed post-deploy via server probe.
- **Pre-deploy structured data:** **0** JSON-LD scripts on all sampled public URLs — greenfield implementation, no duplicate owner conflict.
- **Pre-deploy OG:** **0** on sampled pages (unchanged by this wave).
- **Core before:** `0.3.29-specialists-nav-seo-maps-01`.
- **Deprecated path:** `https://shpigovsky.ru/specyalisty/` → `https://shpigovsky.ru/specialisty/` (301/redirect chain; JSON-LD uses canonical `/specialisty/` only).

Evidence: `REPORTS/evidence/prod-yandex-schema-org-01/01-pre-intake.json`

---

## 4. Yandex documentation research

| Source | Relevant requirement | Implementation impact |
|--------|---------------------|------------------------|
| [Schema.org intro (RU)](https://yandex.ru/support/webmaster/schema-org/intro-schema-org.html) | Schema.org is recommended semantic vocabulary; not all types get special presentation | Used only truthful types; report distinguishes semantic vs Yandex-supported |
| [JSON-LD about (EN)](https://yandex.ru/support/webmaster/en/json-ld/about.html) | JSON-LD must live in `<script type="application/ld+json">` | Single server-rendered script via `wp_head` priority 6 |
| [Structured data validator (EN)](https://yandex.ru/support/webmaster/en/yandex-indexing/validator.html) | Validator checks Schema.org + Yandex service requirements | **ACCESS BLOCKED** in session — see §21 |
| Yandex organization/place guidance (research + prior Web-GPT pack) | Organization/Place descendants supported; branches as separate orgs; fields: name, url, address, telephone, geo, openingHours | `MedicalClinic` main + branch nodes; geo omitted (no authoritative coords) |
| BreadcrumbList guidance | JSON-LD BreadcrumbList supported for navigation chains | Emitted only when theme breadcrumb trail exists |

**Distinction maintained throughout:**

- **YANDEX EXPLICITLY SUPPORTED (organization/address surfaces):** `MedicalClinic`, `Organization` descendants, `PostalAddress`, `openingHoursSpecification`, `BreadcrumbList` where applicable.
- **SCHEMA.ORG SEMANTIC ONLY:** `WebPage`, `ContactPage`, `CollectionPage`, `Service`, `Person`, `Article`, `ItemList` — valid Schema.org, no rich-result promise.

Valid markup **does not** guarantee ranking or enhanced snippets.

---

## 5. Existing structured-data audit

Production before deploy:

| URL | JSON-LD | Microdata | RDFa | OG |
|-----|---------|-----------|------|-----|
| `/` | 0 | 0 | 0 | 0 |
| `/kontakty/` | 0 | 0 | 0 | 0 |
| `/uslugi/` | 0 | 0 | 0 | 0 |
| `/specialisty/` | 0 | 0 | 0 | 0 |

No theme/plugin duplicate owner found. **shpigovsky-core** is now the sole JSON-LD owner.

---

## 6. Current public entity/template inventory

| Surface | WordPress owner | Canonical URL pattern |
|---------|-----------------|----------------------|
| Homepage | Static front page | `/` |
| Contacts | `page-templates/contacts.php` / `kontakty` | `/kontakty/` |
| Services hub | `page-templates/services-hub.php` / `uslugi` | `/uslugi/` |
| Service singles | CPT `service` | `/uslugi/.../` |
| Specialists hub | `page-templates/specialists-hub.php` / page `specialisty` | `/specialisty/` |
| Specialist singles | CPT `specialist` | `/specialisty/{slug}/` |
| Articles | `post` | `/blog/{slug}/` |
| About hub | institutional template + `shpigovsky_is_about_hub_page()` | `/o-centre/` |
| Other institutional | institutional template children | `/o-centre/.../` |
| Reviews | `page-templates/reviews.php` / `otzyvy` | `/otzyvy/` |
| Legal | generic page e.g. `privacy-policy` | `/privacy-policy/` |
| Generic pages | default page template | various |

Deprecated: `/specyalisty/` — redirect only.

---

## 7. Final schema architecture

```
WordPress request
  → DataReaders (ACF / theme helpers)
  → OrganizationBuilder (MedicalClinic graph)
  → GraphBuilder (page-aware nodes)
  → BreadcrumbBuilder (conditional)
  → StructuredData::render_json_ld()
  → one <script type="application/ld+json"> in <head>
```

Module id: `structured-data.schema-org` in `shpigovsky-core`.

Stable `@id` scheme via `EntityIds` (`#website`, `#organization`, `#location-{slug}`, `{url}#webpage`, etc.).

---

## 8. Organization / clinic / branch model

- **Primary type:** `MedicalClinic` (narrowest truthful Yandex-supported medical org descendant for addiction-treatment clinic network).
- **Not used:** generic `Organization` alone, `Hospital`, universal `Physician`.
- **Branches:** two separate `MedicalClinic` nodes from `contacts_locations` repeater, linked via `parentOrganization` / `subOrganization`.
- **Geo:** omitted — no authoritative coordinates in Admin (SAFE UNKNOWN).
- **Addresses:** `PostalAddress` with verified public strings only; optional `addressLocality` / `addressRegion` when safely derivable from text.

Production example (homepage graph): main org + 2 branch clinics with distinct addresses and per-location hours.

---

## 9. Data ownership

| Schema property | WordPress / theme source |
|-----------------|--------------------------|
| Organization name | ACF `organisation_name` / site option |
| Phones | `phone_primary`, location rows |
| Email | `site_email`, location email |
| Main address | `site_address` |
| Branch addresses/hours | `contacts_locations` on contacts page (`contacts-helpers.php`) |
| Site URL | `home_url()` |
| Logo | theme site logo helper |
| Page name/description | `fp02_seo_title`, `fp02_seo_description`, fallbacks |
| Specialist jobTitle | ACF `specialist_role` |
| Breadcrumbs | theme breadcrumb trail helpers |
| Service/specialist lists | published CPT queries / `shpigovsky_get_specialists_cards()` |

No manual JSON-LD Admin UI added.

---

## 10. Page-type schema matrix

| WordPress type/template | Schema graph | Main entity | Yandex explicit support | Data owner | Result |
|-------------------------|--------------|-------------|-------------------------|------------|--------|
| Homepage | WebSite + WebPage + MedicalClinic×3 | org/branches | Org/address — **supported** | site settings + contacts | PASS |
| Contacts | ContactPage + org/branches | ContactPage | Org/address — **supported** | contacts ACF | PASS |
| Services hub | CollectionPage + ItemList | ItemList | Semantic only | CPT `service` | PASS |
| Service single | WebPage + Service | Service | Semantic only | service CPT + SEO fields | PASS |
| Specialists hub | CollectionPage + ItemList | ItemList | Semantic only | specialists cards helper | PASS |
| Specialist single | WebPage + Person | Person | Semantic only | specialist CPT | PASS |
| Article | WebPage + Article | Article | Semantic only | post + SEO | PASS |
| About hub `/o-centre/` | AboutPage + org | AboutPage | Semantic only | institutional | PASS |
| About child pages | WebPage + BreadcrumbList | WebPage | Semantic only | institutional | PASS |
| Reviews | CollectionPage | CollectionPage | Semantic only | reviews template | PASS |
| Legal/generic | WebPage + BreadcrumbList | WebPage | Semantic only | page + SEO | PASS |

---

## 11. Homepage

- Graph: `WebSite`, `WebPage`, main `MedicalClinic`, 2 branch `MedicalClinic` nodes.
- No BreadcrumbList (no trail on front page).
- Canonical URL `https://shpigovsky.ru` — no `/specyalisty/`.

---

## 12. Contacts

- `ContactPage` with `about → #organization`.
- Branch clinics included in global org graph from contacts data.
- No breadcrumb (contacts uses empty-shell breadcrumb policy in theme).

---

## 13. Services Hub + service singles

- Hub: `CollectionPage` + `ItemList` of published services; BreadcrumbList present.
- Single: `Service` with `provider → #organization`; real name/url/description/image only.

---

## 14. Specialists Hub + specialist singles

- Hub: `CollectionPage` + `ItemList` from specialist cards; **no BreadcrumbList** (matches intentional UI).
- Item URLs normalized to `/specialisty/` if legacy path appears in helper output.
- Single: `Person` (not `Physician`) with `worksFor → #organization`, optional `jobTitle`.

---

## 15. Articles

- `Article` with publisher org, ISO dates, optional author only for non-technical public display names.
- BreadcrumbList from blog trail.

---

## 16. About / Reviews / Generic / Legal

- **About hub** `/o-centre/`: `AboutPage` + breadcrumbs.
- **About children** (e.g. `/o-centre/o-nas/`): `WebPage` + breadcrumbs — truthful (not org hub).
- **Reviews:** `CollectionPage` only — **no** `Review` / `AggregateRating` despite internal testimonial ratings in PHP data.
- **Legal** (`/privacy-policy/`): `WebPage` + breadcrumbs.

---

## 17. BreadcrumbList

- Emitted when theme provides a real trail via `BreadcrumbBuilder`.
- Skipped: front page, specialists hub, contacts, reviews (empty-shell / intentional no-trail pages).
- Uses canonical HTTPS URLs and position/name per Yandex JSON-LD guidance.

---

## 18. Types intentionally NOT used

| Type | Status |
|------|--------|
| Product | NOT APPLICABLE — medical services site, not product commerce |
| Offer | NOT APPLICABLE — no price/availability data owned |
| QAPage | NOT APPLICABLE — FAQ blocks are not single-question Q&A pages |
| AggregateRating / Review | NOT EMITTED — would fabricate numeric scores from testimonials |
| Physician (universal) | NOT USED — specialists are `Person` with optional `jobTitle` |

---

## 19. Open Graph separation

- Pre-existing production state: **OG count = 0** on all sampled URLs before and after deploy.
- Schema.org implementation does **not** replace OG; separate systems.
- SEO title/description remain theme-owned (`seo-entity-meta.php`).

---

## 20. Implementation

**Plugin:** `shpigovsky-core` @ `0.3.30-yandex-schema-org-01`

**New module:** `src/StructuredData/`

| File | Role |
|------|------|
| `StructuredData.php` | Module + `wp_head` renderer |
| `GraphBuilder.php` | Page-aware `@graph` assembly |
| `OrganizationBuilder.php` | MedicalClinic org + branches |
| `DataReaders.php` | ACF/theme data accessors |
| `EntityIds.php` | Stable `@id` helpers |
| `BreadcrumbBuilder.php` | Conditional BreadcrumbList |
| `OpeningHoursParser.php` | Conservative RU hours → OpeningHoursSpecification |

**Registry:** `ModuleRegistry.php` — `structured-data.schema-org`

---

## 21. Yandex validator matrix

| URL | Detected types (production HTML) | Errors | Warnings | Result |
|-----|----------------------------------|--------|----------|--------|
| `/` | MedicalClinic×3, WebSite, WebPage | — | — | JSON parse PASS; **Yandex UI not run** |
| `/kontakty/` | ContactPage, MedicalClinic×3, WebSite | — | — | JSON parse PASS |
| `/uslugi/` | CollectionPage, ItemList, BreadcrumbList, … | — | — | JSON parse PASS |
| service single | Service, BreadcrumbList, … | — | — | JSON parse PASS |
| `/specialisty/` | CollectionPage, ItemList, … | — | — | JSON parse PASS |
| specialist single | Person, BreadcrumbList, … | — | — | JSON parse PASS |
| article | Article, BreadcrumbList, … | — | — | JSON parse PASS |
| `/o-centre/` | AboutPage, BreadcrumbList, … | — | — | JSON parse PASS |
| `/otzyvy/` | CollectionPage, … | — | — | JSON parse PASS |
| `/privacy-policy/` | WebPage, BreadcrumbList, … | — | — | JSON parse PASS |

**YANDEX VALIDATOR = ACCESS BLOCKED** (authenticated Webmaster UI). Evidence: `06-yandex-validator.json`

---

## 22. Raw source / JSON validation

- 12/12 representative URLs: exactly **1** JSON-LD script each.
- All JSON parses successfully (`05-qa-matrix.json`).
- `@context`: `https://schema.org`
- No `/specyalisty/` in JSON-LD payloads.
- Sample payloads: `05-jsonld-*.json`

---

## 23. Production QA

- Layout/presentation: unchanged (head-only JSON-LD injection).
- No visible JSON on page body.
- Specialists, services, contacts, maps: no functional regression observed in HTTP probes.
- SEO `<title>` / meta remain present in source.

---

## 24. Robots / indexing safety

| Check | Result |
|-------|--------|
| robots SHA pre/post | **MATCH** — not modified |
| blog_public | **1** |
| Indexing | **OPEN** |
| robots semantic rules | **Preserved** (human/Olya-owned) |

---

## 25. Production ↔ source parity

Deploy manifest: `9/9` files remote SHA256 match local (`03-deploy-manifest.json`).

Post-deploy probe:

```json
{
  "blog_public": 1,
  "core_version": "0.3.30-yandex-schema-org-01",
  "schema_module_enabled": true
}
```

---

## 26. Backup / rollback

Layer B pre-deploy snapshots:

`X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-yandex-schema-org-01\`

Rollback: restore 9 exact plugin files from Layer B + prior `shpigovsky-core.php` / `ModuleRegistry.php`. No DB migration required.

---

## 27. Files changed

**Production-deployed (plugin):**

- `WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php`
- `WORDPRESS/plugins/shpigovsky-core/src/ModuleRegistry.php`
- `WORDPRESS/plugins/shpigovsky-core/src/StructuredData/EntityIds.php`
- `WORDPRESS/plugins/shpigovsky-core/src/StructuredData/DataReaders.php`
- `WORDPRESS/plugins/shpigovsky-core/src/StructuredData/OpeningHoursParser.php`
- `WORDPRESS/plugins/shpigovsky-core/src/StructuredData/OrganizationBuilder.php`
- `WORDPRESS/plugins/shpigovsky-core/src/StructuredData/BreadcrumbBuilder.php`
- `WORDPRESS/plugins/shpigovsky-core/src/StructuredData/GraphBuilder.php`
- `WORDPRESS/plugins/shpigovsky-core/src/StructuredData/StructuredData.php`

**Documentation / evidence:**

- `REPORTS/REPORT-FP-0002-PROD-YANDEX-SCHEMA-ORG-01.md`
- `REPORTS/evidence/prod-yandex-schema-org-01/*`
- `PROJECT-STATUS.md`
- `REPORTS/FP-0002-NEXT-WEBGPT-HANDOFF.md`

---

## 28. Core/version state

- **Production core:** `0.3.30-yandex-schema-org-01`
- **Prior core:** `0.3.29-specialists-nav-seo-maps-01`

---

## 29. Git

| Item | Value |
|------|-------|
| Commit | `fc39a5a922c398824306574b701ac7bf9860a698` |
| Message | `FP-0002: add Yandex-aligned Schema.org JSON-LD graph in shpigovsky-core.` |
| Branch | `origin/mars/canonical-post-recovery` |
| Prior origin tip | `1c9e92ed90a495000e2be4a022dcb40dda9abfbc` |
| Final origin tip | `fc39a5a922c398824306574b701ac7bf9860a698` |
| Files in commit | 32 (plugin module + report + evidence + status/handoff) |
| Staging | Selective allowlist only — no `git add .` |

---

## 30. WP Forge harvesting

Candidate reusable pattern (documentation-only, not auto-imported):

- **Entity-aware JSON-LD graph** in WordPress functionality plugin with stable `@id` references.
- **Yandex-first type selection:** MedicalClinic + separate branch nodes; omit geo when not owned.
- **No-fabrication rule:** omit Review/AggregateRating/Product/Offer/QAPage unless production truth supports them.
- **Template → schema routing table** driven by existing theme helpers, not parallel Admin JSON.

---

## 31. Residuals

1. **Yandex Webmaster validator UI** — operator may run authenticated check on representative URLs; no blocking errors expected from JSON structure.
2. **Open Graph** — still absent on production; out of scope for this wave but noted for future SEO work.
3. **Sitemap.xml** — public sitemap index reported only 4 URLs at probe time; unrelated to schema wave — SAFE UNKNOWN whether full sitemap index is elsewhere (`/wp-sitemap.xml`).

---

## 32. Mutation statement

This wave **added** a new `shpigovsky-core` structured-data module and **deployed** exact plugin files to production. **Did not** modify robots.txt, indexing policy, Olya editorial DB content, or theme presentation. **Did not** install a generic schema plugin.
