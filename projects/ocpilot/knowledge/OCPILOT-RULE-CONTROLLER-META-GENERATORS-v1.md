# OCPilot Rule — Controller-Based Meta Generators v1

**Rule ID:** OCPILOT-RULE-CONTROLLER-META-v1  
**Status:** **ACTIVE** — inspection rule for custom OpenCart / ocStore project sites  
**Created:** 2026-06-09  
**Origin:** SITE-001 (СИБКАР) Phase 1 final audit — new-car product title residual

---

## Rule title

**Controller-based meta generators must be audited on custom OpenCart sites.**

---

## Context

SITE-001 / SIBCAR revealed that legacy branding may persist in **generated meta tags** even after admin Store Settings and visible theme templates are updated.

Operator visual QA confirmed **СИБКАР** on homepage, header/footer, and used-car surfaces — yet **new car product pages** still showed browser titles containing **`АЦ Хмельницкий`**.

Automated final audit (2026-06-09) additionally confirmed legacy brand in **`<title>` and meta description on `/auto/`** (new car catalog root), while manufacturer pages `/auto/{brand}` were clean after W1F-A.

**Root insight:** On this site class, SEO title/description/keywords are **not exclusively controlled** by OpenCart admin Store Settings. They may be:

1. Hardcoded in **catalog controllers** via `$this->document->setTitle()` / `setDescription()` / `setKeywords()`
2. **Conditionally overridden** only for specific category IDs (e.g. used cars but not new cars)
3. **Passed through from database** product/category description tables without sanitization
4. **Seeded by admin UI JavaScript** in `product_form.twig` or similar templates

---

## Developer pattern

OpenCart custom implementations — including sites associated in ATLAS with **ИП Дьяконов Сергей** (intake candidate `DYAKONOV-INTAKE-CAND-O01`; full population **SAFE UNKNOWN**) — may generate title, description, and keywords **directly in controllers** rather than relying on admin config alone.

**Observed SITE-001 pattern:**

| Route class | Meta source | Brand control |
|-------------|-------------|---------------|
| Store-wide defaults | `oc_setting` (`config_meta_*`) | W1A admin |
| Custom info pages | `information/about.php`, `contact.php` hardcoded | W1C controller edit |
| Manufacturer category | `category.php` fallback strings when `$man['TitleNew']` empty | W1F-A controller edit |
| Category root `/auto/` | `oc_category_description.meta_*` for category_id 59 | **DB — not wave-scoped** |
| Used product detail | `product.php` override when `category_id == 60` | W1F-A controller edit |
| New product detail | `product.php` passthrough `$product_info['meta_title']` | **DB — admin JS seeded** |
| YML exports | `yml.php`, `ymlnew.php` hardcoded shop block | W1F-C1 controller edit |

**Never assume:** updating Store Settings alone completes SEO rebranding.

---

## Required future OCPilot inspection

Apply on **every** OpenCart/ocStore rebrand or SEO audit — minimum checklist:

### Code grep (FTP read-only)

Search under `catalog/controller/`, `catalog/model/`, `catalog/view/theme/*/template/`:

```
setTitle
setDescription
setKeywords
meta_title
meta_description
meta_keyword
document->setTitle
document->setDescription
document->setKeywords
```

Search hardcoded brand suffixes and legacy tokens from project dictionary:

```
| АЦ Хмельницкий
АЦ Хмельницкий
Автоцентр Хмельницкий
ац Хмельницкий
```

Also inspect **admin templates**:

```
admin/view/template/catalog/product_form.twig
admin/view/template/catalog/category_form.twig
```

### Live HTML verification

After any wave touching SEO:

| Route type | Must probe |
|------------|------------|
| Homepage | `/` |
| Custom controllers | `/about`, `/contact/` |
| Legal / service | project-specific list |
| Used category | `/cars/{brand}` |
| New category | `/auto/{brand}` |
| **New catalog root** | `/auto/` |
| **Used product detail** | at least one live URL |
| **New product detail** | at least one live URL |

Extract and compare: `<title>`, `meta description`, `meta keywords`, H1, visible body, header, footer.

### Admin vs generated value comparison

When admin shows **СИБКАР** in Store Settings but public HTML differs:

1. Identify controller override vs DB passthrough code path
2. Check `oc_product_description` / `oc_category_description` for legacy strings
3. Check manufacturer custom fields (`TitleNew`, `DescrNew`, `HeaderNew`, `SeoTextNew`, etc.) if present
4. Check admin JS auto-fill templates

### Post-change QA rule

- Include **product** and **new-car** pages in post-change QA — not only homepage and category listings
- Treat **empty catalog** as **NOT VERIFIED** — document explicitly
- Record geographic exceptions separately (e.g. `ул. Богдана Хмельницкого`)

---

## Applicability

| Project | Applies |
|---------|---------|
| **SITE-001** (СИБКАР) | **YES** — origin site |
| **BZPM** | **YES** — same developer pattern suspected |
| Future OpenCart / ocStore custom builds | **YES** — default inspection rule |

---

## Related artefacts

| Document | Role |
|----------|------|
| [SITE-001-PHASE1-FINAL-AUDIT-v1.md](../sites/site-001/reports/SITE-001-PHASE1-FINAL-AUDIT-v1.md) | Evidence table |
| [SITE-001-W1F-LEGACY-SWEEP-v1.md](../sites/site-001/reports/SITE-001-W1F-LEGACY-SWEEP-v1.md) | Pre-remediation inventory |
| [controllers/README.md](controllers/README.md) | Controller knowledge skeleton |
| [ATLAS-DYAKONOV-INTAKE-SUMMARY-v1.md](../../atlas/population/ATLAS-DYAKONOV-INTAKE-SUMMARY-v1.md) | Developer intake *(SAFE UNKNOWN population)* |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — from SITE-001 Phase 1 final audit learning |

*OCPilot inspection rule — documentation only; no runtime claimed.*
