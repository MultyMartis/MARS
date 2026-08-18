# Forge WordPress — Repeater vs Entity Decision Matrix v1

**ID:** FW-S-24  
**Status:** ACTIVE — PRODUCTION-INFORMED  
**Date:** 2026-08-18  
**Companion:** [CMS ARCHITECTURE](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) · [FW-S-10 CPT](FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md)

```text
REPEATERS ARE FOR PARENT-OWNED ROWS, NOT A SUBSTITUTE FOR DOMAIN ENTITIES.
```

---

## 1. When a repeater is correct

All of the following should hold:

| Criterion | Repeater-friendly |
|-----------|-------------------|
| Ownership | Tightly owned by one parent (page, CPT item, or one Options section) |
| URL | Rows have **no** independent public permalink |
| Lifecycle | No independent publish/draft/trash workflow |
| Reuse | Rows are **not** reused across unrelated parents |
| Order | Manual order matters |
| Scale | Modest row count (see §3) |
| SEO | No per-row SEO landing |

**GOOD examples:** Hero slides; page statistics; small feature list; timeline stages; compact FAQ **local to one page**; contact methods if strictly local to one location record.

---

## 2. When a repeater is wrong

| Bad repeater | Why | Promote to |
|--------------|-----|------------|
| 80–100 reviews | Collection lifecycle; editor list needed | CPT **or** Options-only if no singles (**J**) |
| Staff directory | People are entities | CPT |
| Services | URLs, SEO, relations | CPT |
| Portfolio cases | Same | CPT |
| FAQs reused on many pages | Shared library | CPT or taxonomy+content |
| Locations | Often URLs / maps / hours | CPT |
| Independently managed documents | Files + titles + dates | CPT or Media + CPT |
| Nested repeater as database | Pseudo-SQL in Admin | Entities + relationships |

**BAD (AP-CMS-002 / AP-CMS-008):** modeling the business as nested repeaters because “ACF Pro can do it.”

---

## 3. Complexity limits and warning signs

Treat as **promotion signals**. One strong signal can be enough; several weak signals compound.

| Signal | Threshold / meaning |
|--------|---------------------|
| Nested repeaters | Default **no**. One nest max, charter only |
| Fields per row | Warn at **8+**; promote or split at **15+** |
| Row count | Warn at **15+**; almost always wrong at **40+** on a page; **80+** is a collection |
| Relationships inside rows | Warn; relationships inside nested relationships = stop |
| Editor scroll | Form longer than ~2–3 viewports for one repeater |
| Rows reused elsewhere | Not a repeater |
| SEO or URL needed | Entity |
| Searching / filtering needed | Entity + Admin list |
| Frequent independent editing | Entity |
| Need draft vs publish per row | Entity |

Options-repeater exception (**J**): a bounded social-proof wall with stable UIDs, **no** public singles, editors accept Options UX. Revisit if editors ask for a list table, search, or permalinks.

---

## 4. REPEATER → ENTITY PROMOTION CHECKLIST

If **any** of the following is true, promote.

- [ ] Row needs its own URL or SEO landing  
- [ ] Row must be reused on multiple parents  
- [ ] Editors need a dedicated Admin list (photo, type, order, status)  
- [ ] Items are added/removed without editing a parent page  
- [ ] Search, sitemap, or Smart Search group should include items  
- [ ] Other objects must **relate to** the row  
- [ ] Nested repeater is being used as a database  
- [ ] Row count or field count crossed §3 warnings  
- [ ] Draft/publish per item is required  
- [ ] The parent ACF screen is unusable (AP-CMS-007)

**Promotion path:** CPT (default) · taxonomy (classification-only) · relationship to an existing CPT · Options only if still global-and-URL-less after review.

Then run [CMS-MIGRATION-PLAN](../templates/FORGE-WORDPRESS-CMS-MIGRATION-PLAN-TEMPLATE-v1.md). Do not leave the old repeater as a second SoT.

---

## 5. Decision matrix (quick)

| Situation | Repeater | CPT | Options repeater | Taxonomy |
|-----------|----------|-----|------------------|----------|
| 3–6 feature bullets on About | ● | | | |
| 12 service cards with own URLs | | ● | | |
| 12 service cards, **no** singles, never reused | ● (warn: score it) | prefer ● if growing | | |
| Staff with profile pages | | ● | | |
| Team photos **only** on About, no profiles | ● | | | |
| 80 reviews, no singles | | maybe | ● **J** | |
| 80 reviews with author pages | | ● | | |
| Article topics | | | | ● |
| Hero slides on Home | ● | | | |
| FAQ used on 10 pages | | ● | | |

● = typical first choice. Document overrides in CONTENT-ENTITY-MAP.

**Conflict with FW-S-01 §7 (2026-06-22):** “Team cards on one page → repeater” remains valid **only** when there is no public single and no collection workflow. Public people/services → [FW-S-10](FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md) + this matrix. This document **wins** for production modeling.

---

## 6. After promotion

Keep hub Page if the collection has a marketing index. Set `has_archive = false` when the hub owns that URL. Preserve IDs/slugs. Retarget search and sitemap. Native permalink UX only.

---

*FW-S-24 v1 — promote when rows behave like entities.*
