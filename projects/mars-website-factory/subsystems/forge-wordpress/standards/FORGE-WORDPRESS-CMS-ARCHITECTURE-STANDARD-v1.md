# Forge WordPress — CMS and Editable Architecture Standard v1

**ID:** FW-S-22  
**Status:** ACTIVE — PRODUCTION-INFORMED (one live case: FP-0002); second-site validation still required where marked **J**  
**Date:** 2026-08-18  
**Class:** A (modeling) / E (editor)  
**Extends:** [FW-S-01 Content Modeling](FORGE-WORDPRESS-CONTENT-MODELING-STANDARD-v1.md) · [FW-S-10 CPT](FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md) · [FW-S-02 ACF](FORGE-WORDPRESS-ACF-ARCHITECTURE-STANDARD-v1.md) · [FW-S-11 Site Settings](FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md)  
**Audience:** Content modelers, Admin UX, theme specialists, operators, Cursor / Web-GPT sessions starting a new WP Forge site

**Honesty:** FP-0002 proved many Admin/content patterns under production pressure. This standard turns those lessons into a **deterministic decision system** so the next site does not rediscover Page vs CPT vs repeater vs Options during implementation. Do **not** copy client content, clinical IA, or brand fields.

---

## 1. Purpose

Answer one question:

```text
HOW DO WE TURN A WEBSITE DESIGN / CONTENT REQUIREMENT
INTO A CLEAN WORDPRESS EDITING MODEL?
```

The answer always has two halves, designed together:

| Half | Meaning |
|------|---------|
| **A. Data model** | What is stored, where, who owns it, how it relates |
| **B. Editor experience** | What the client sees, in what order, with what labels, on which screens |

A technically correct CPT with an unusable Admin form is a failed architecture. A pretty ACF screen that duplicates phones across templates is also a failed architecture.

**Primary rule:**

```text
DO NOT START BY CREATING ACF FIELDS.
```

Start by identifying entities, relationships, globals, page-owned content, repeating records, presentation variants, lifecycle, and editor responsibilities. Only then choose WordPress storage.

---

## 2. Modeling sequence (canonical)

Execute in this order. Do not skip to field groups.

| Step | Identify | Output |
|------|----------|--------|
| **1. Entities** | Named things with independent identity | [CONTENT-ENTITY-MAP](../templates/FORGE-WORDPRESS-CONTENT-ENTITY-MAP-TEMPLATE-v1.md) |
| **2. Relationships** | Who points to whom | [RELATIONSHIP-MAP](../templates/FORGE-WORDPRESS-RELATIONSHIP-MAP-TEMPLATE-v1.md) |
| **3. Reusable globals** | Values used by many consumers | [SITE-SETTINGS-MAP](../templates/FORGE-WORDPRESS-SITE-SETTINGS-MAP-TEMPLATE-v1.md) · [FIELD-OWNERSHIP-MAP](../templates/FORGE-WORDPRESS-FIELD-OWNERSHIP-MAP-TEMPLATE-v1.md) |
| **4. Page-owned content** | Unique to one route/template | [PAGE-EDITABILITY-MAP](../templates/FORGE-WORDPRESS-PAGE-EDITABILITY-MAP-TEMPLATE-v1.md) |
| **5. Repeating records** | Rows vs entities | [REPEATER VS ENTITY](FORGE-WORDPRESS-REPEATER-VS-ENTITY-DECISION-MATRIX-v1.md) |
| **6. Presentation variants** | Controlled enums, not CSS | [COMPONENT DATA CONTRACT](FORGE-WORDPRESS-COMPONENT-DATA-CONTRACT-STANDARD-v1.md) |
| **7. Content lifecycle** | draft / publish / schedule / trash; who may create | entity map + Admin IA |
| **8. Editor responsibilities** | Client editor vs Administrator vs technical operator | [EDITOR UX](FORGE-WORDPRESS-EDITOR-UX-STANDARD-v1.md) · [ADMIN IA](FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-STANDARD-v1.md) |

**Then** choose storage (Page / Post / CPT / taxonomy / Options / repeater / Flexible Content / relationship / hardcoded).  
**Then** define field schema.  
**Then** define frontend contracts.  
**Then** define Admin UX.  
**Then** simulate editor workflows before coding the frontend.

Workflow detail: [DESIGN-TO-CMS](FORGE-WORDPRESS-DESIGN-TO-CMS-WORKFLOW-v1.md).  
Phase gate: Blueprint **P1b** — CMS / Editable Architecture Design (this document §16).

---

## 3. Entity identification

A candidate is likely a **real content entity** if several of the following are true:

| Signal | Typical meaning |
|--------|-----------------|
| Has its own title/name | Identity, not a caption on a parent |
| May have its own URL | Public single or at least a stable permalink |
| Appears in multiple places | Reuse → not page-local copy |
| Has multiple fields | More than a label + icon |
| Independently created/edited/deleted | Own CRUD, not a row in a parent form |
| Needs search / filtering / Admin list | Collection workflow |
| Needs SEO | Public landing of its own |
| Needs relationships | Other objects point at it |
| May appear in sitemap | Indexable object |
| May grow independently | Count will increase without redesigning a page |

**Generic service-site entity candidates (not a mandatory set):** Service, Specialist / Team Member, Case / Project, Review, Product, Document, Event, Location. FAQ Item is an entity **only sometimes** (shared FAQ library vs page-local accordion).

**Not an entity:** a statistic number on one hero; a single page’s three feature bullets; a decorative icon; a CSS variant.

Decision rules: [REPEATER VS ENTITY](FORGE-WORDPRESS-REPEATER-VS-ENTITY-DECISION-MATRIX-v1.md) · reusability score (§14).

---

## 4. Storage decision system

### 4.1 Page

**USE PAGE when:**

- unique structural route (Home, About, Contacts, legal, one-off landing);
- one-off content, not a growing collection;
- hierarchical navigation / breadcrumbs are meaningful;
- no independent collection Admin workflow is needed;
- the URL is a hub that **introduces** a CPT archive (hub Page + CPT singles).

**DO NOT USE PAGE when:** 12–N same-class public objects (services, people, cases) merely because Pages already exist.

**BAD (AP-CMS-001 / AP-001):** twenty specialists as child Pages “because WordPress Pages already exist.”

### 4.2 Post

```text
Post  = chronological editorial / article stream.
CPT   = domain entity.
```

Do **not** use Posts as a generic database. Services, people, products, cases, locations are not Posts.

**Exceptions (document in CONTENT-MODEL):** a tiny site with one editorial stream and no other collections; a temporary bootstrap before a CPT exists (must have a migration plan). Using Posts for staff/services is a modeling defect, not a shortcut.

### 4.3 CPT

**USE CPT when** (see [FW-S-10](FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md) hard matrix): collection of same-class entities; independent CRUD; own URL/template; own fields; search/sitemap/relationships; editors need a dedicated Admin section.

**GOOD:** Specialists → CPT. Services with own URLs → CPT.  
**Hierarchical CPT:** use when the **same class** nests (service group → service) **and** editors need that tree in one Admin type. Do not fake hierarchy with unrelated child Pages. Hub Page + flat CPT remains the default when a marketing hub owns the index URL (`has_archive = false`).

### 4.4 Taxonomy

**USE TAXONOMY when:** terms are shared across many entities; terms need independent management; filtering / archive / search is useful; hierarchy may exist; term URL/SEO might exist.

**Examples:** service categories, article topics, locations-as-terms, specializations, project types.

**DO NOT CREATE TAXONOMY when:** a closed 2–4 value enum (use select); a one-off tag on a single page; a substitute for a relationship to another CPT; “categories” with one term and no archive.

Prefer taxonomy over: free-typed category text; per-row checkbox lists that must stay in sync; repeaters of term names.

### 4.5 Options / Site Settings

**USE OPTIONS when** the value is a **global business value** consumed by multiple surfaces.

**GOOD:** organization contacts, phones, email, address, social/messenger URLs, company identity, reusable global CTA labels, analytics IDs, verification, global footer/header controls, SEO/integration configuration.

**BAD:** content belonging to one page; records with their own lifecycle; huge lists that should be CPT; repeated page-specific sections.

```text
GLOBAL VALUE USED BY MULTIPLE CONSUMERS
→ ONE GLOBAL SOURCE OF TRUTH.
```

Detail: [GLOBAL SETTINGS OWNERSHIP](FORGE-WORDPRESS-GLOBAL-SETTINGS-OWNERSHIP-STANDARD-v1.md) · [FW-S-11](FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md).

### 4.6 Repeater

**USE REPEATER when:** rows are tightly owned by one parent; no independent URL; no independent lifecycle; no reuse across parents; ordering matters; modest row count.

**GOOD:** Hero slides, page statistics, small feature list, timeline stages, compact FAQ local to one page.

**BAD:** 80–100 reviews; staff directory; services; portfolio cases; reusable FAQs used on many pages; locations; independently managed documents.

```text
IF A REPEATER ROW STARTS BEHAVING LIKE AN ENTITY,
PROMOTE IT TO CPT / TAXONOMY / RELATIONSHIP.
```

**Reviews (J):** FP-0002 stored reviews as an Options repeater with stable UIDs because items had **no** public single. If the next site needs permalinks, authors, or sitemap entries → CPT. Do not copy that choice blindly.

### 4.7 Flexible Content

**USE FLEXIBLE CONTENT when:** page sections are reorderable; the editor may choose from a **controlled registry** of design components; layouts may appear in arbitrary sequence.

Canonical preference:

```text
CONTROLLED FLEXIBILITY
not
UNLIMITED PAGE BUILDER.
```

Risks: page-builder syndrome, enormous Admin forms, inconsistent UX, too much design freedom, impossible global refactoring, broken compositions. Each layout must be a named component with a data contract. See §8 and [COMPONENT DATA CONTRACT](FORGE-WORDPRESS-COMPONENT-DATA-CONTRACT-STANDARD-v1.md).

### 4.8 Relationship

**REFERENCE REAL WORDPRESS OBJECTS** instead of typing URLs when the target is internal content.

Prefer: Post Object / Relationship / Taxonomy / User.  
Avoid: specialist URL text field; pasted staging hostnames; free-text “related service name”.

Detail: [RELATIONSHIP MODELING](FORGE-WORDPRESS-RELATIONSHIP-MODELING-STANDARD-v1.md).

### 4.9 Hardcoded in the theme

Keep in code when: structural/system label; component invariant; no plausible editor need; making it editable increases risk without benefit.

Do **not** make every string an ACF field (AP-CMS-003).

---

## 5. Structured template vs Flexible Content vs Gutenberg vs WYSIWYG vs CPT

Choose **intentionally**. Do not default.

| Mode | Use when | Do not use when |
|------|----------|-----------------|
| **Fixed structured template** | Design is a known section stack; editors fill fields; order is design-owned | Marketing must invent new section sequences weekly |
| **Controlled flexible sections** | Bounded layout registry; reorder within a page type | Unlimited layouts; raw CSS; nested flex as a CMS |
| **Gutenberg (bounded)** | Articles / hybrid zones; whitelist blocks | PIXEL_PERFECT chrome; curated CPT bodies owned by ACF |
| **WYSIWYG** | Long editorial body; generic content page | Card title, phone, button label, feature row |
| **Custom CPT** | Domain collection (see §4.3) | One-off landing |

**Default for PIXEL_PERFECT service sites (A):** ACF-first structured templates + Options + CPTs. Gutenberg for articles if the project has a blog. Flexible Content only with a written layout registry. Full page-building is **charter opt-in**.

Coexistence: ACF can own structured regions while Gutenberg owns `post` body. Do not give both a competing H1/hero.

---

## 6. Field ownership

Every editable value has **one owner**.

**Example — phone:**

```text
PHONE
→ STORAGE OWNER: Site Settings
→ EDITOR: client editor on «Контакты»
→ FRONTEND CONSUMERS: header, mobile nav, floating header, footer, contacts
→ FALLBACK: hide if empty (do not invent a number)
→ VALIDATION: phone format on save
```

Never: header phone field + footer phone field + contacts phone field unless they are **genuinely different business values** (e.g. sales vs support), in which case they are two named globals, still not per-template copies.

Template: [FIELD-OWNERSHIP-MAP](../templates/FORGE-WORDPRESS-FIELD-OWNERSHIP-MAP-TEMPLATE-v1.md).

---

## 7. Page section model

A typical editable section **may** include: `enabled`, eyebrow/kicker, heading, text, media, CTA, variant, items, relation.

**Warn:** not every section needs all of these. The schema must match the **component contract**, not a universal section super-object.

**Enable / disable:**

- explicit `enabled` only where editors actually need on/off while keeping content;
- otherwise derive rendering from meaningful content presence.

Frontend: empty optional data → do not render the section/control. Never output empty cards, empty social icons, blank headings, placeholder Lorem, or demo fallback (AP-009 / AP-CMS-009).

Proven pattern (anonymized): featured image is the portrait SoT — do not add a duplicate ACF image “because the section also shows a photo.”

---

## 8. Flexible Content — controlled layout registry

If Flexible Content is used, document:

| Item | Requirement |
|------|-------------|
| Allowed layouts | Named IDs matching frontend components |
| Max layouts per page | Project limit (warn above ~12–15) |
| Nesting | Default **forbidden**; one level max if chartered |
| Variants | Enums, not class names |
| Empty layout | Hide; do not render a husk |
| Global refactor | Changing a layout must update every page using it — keep the registry small |

**Page-builder prevention:** no “HTML block”, no unrestricted nested repeaters, no arbitrary color pickers, no “custom CSS class” for client editors.

---

## 9. Fallback policy

| Class | Behavior |
|-------|----------|
| **A. REQUIRED** | Validation prevents publish/save of an invalid entity |
| **B. OPTIONAL** | Hide when empty |
| **C. SAFE GLOBAL FALLBACK** | Use Site Setting (e.g. page CTA label empty → global CTA label) |
| **D. PROGRAMMATIC FALLBACK** | Generated value (permalink from object; reading time; SEO title ← post title) |
| **E. DEMO FALLBACK** | **NEVER ON PRODUCTION** |

FP-0002 lesson: demo/Lorem leftovers in templates survive empty Admin fields and leak to the live site. Treat template demo strings as a defect, not a convenience.

---

## 10. Internal linking and domain independence

```text
CONTENT DATA SHOULD BE DOMAIN-INDEPENDENT WHERE POSSIBLE.
Store internal object relationships. Generate URLs at render time.
```

Prefer: object relationship, page selector, Post Object, `get_permalink()` / `home_url()`.  
Avoid storing absolute staging domains.

Free URL remains necessary for: external links, in-page anchors, special protocols (`mailto:`, `tel:` as derived from structured phone), custom JS actions.

This is a **modeling** requirement, not only a cutover tactic. It shrinks final-domain mutation scope.

---

## 11. Media

Prefer **attachment ID**, not raw absolute media URL, where practical.

| Need | Field |
|------|-------|
| Single image | Image (ID) |
| Ordered set owned by parent | Gallery (IDs) |
| Downloadable file | File (ID) |
| External video | oEmbed or validated URL |
| External-only asset | URL (documented exception) |

**Alt:** meaningful images use Media Library alt. Decorative images: component-level decorative semantics when required. Do not duplicate alt text fields on every section without a reason.

SVG: follow coding/security standard; do not blindly inline untrusted SVG from editors.

---

## 12. CTA model

Reusable CTA fields:

- label  
- destination **type** (discriminator)  
- internal target **or** external URL **or** form/modal action  
- style/variant only if the design system exposes it  
- open-in-new-tab only for external (or explicit exception)

Do not expose URL + page relationship + modal ID simultaneously without a type discriminator. Use ACF conditional logic.

Proven fallback chain (generic): page/entity CTA → reusable CTA defaults → Site Settings global CTA → hide if still empty.

---

## 13. Reusable blocks — three meanings (do not conflate)

| Kind | Meaning | Example |
|------|---------|---------|
| **A. Reusable DATA entity** | First-class object | Service CPT |
| **B. Reusable PRESENTATION component** | Theme partial + contract | CTA band component |
| **C. Reusable CONTENT instance** | Same copy/settings on many pages | Global consultation defaults on Options |

“CTA component” ≠ “global consultation block” ≠ “Service”. Architecture must name which kind is meant.

**Global identical content:** Options page, reusable CPT/block, Gutenberg synced pattern, or programmatic component with global settings — choose by complexity/lifecycle. Do not duplicate manually across pages.

---

## 14. Reusability score (quick method)

Score **Yes = 1**. Guidance, not a substitute for judgment.

| # | Question |
|---|----------|
| 1 | Appears on many pages? |
| 2 | Independent editor lifecycle? |
| 3 | Independent URL? |
| 4 | Independently searchable? |
| 5 | Reused as a relation target? |
| 6 | Independently ordered as a collection? |
| 7 | Independent SEO? |
| 8 | Count will grow without redesigning a parent page? |

| Score | Typical storage |
|-------|-----------------|
| 0–1 | Page-local fields or hardcoded |
| 2–3 | Repeater on parent **or** Options (if global and no URL) |
| ≥4 or hard URL/lifecycle | CPT (or taxonomy if classification-only) |

---

## 15. Static vs editable

**Keep hardcoded when:** structural/system label; invariant of the component; no plausible editor need; editability increases risk (layout internals, CSS, motion constants).

**Make editable when:** the client is expected to change it; business data changes; marketing copy changes; content lifecycle requires it.

```text
EDIT BUSINESS CONTENT, NOT IMPLEMENTATION DETAILS.
```

---

## 16. New-site phase — CMS / Editable Architecture Design

This is a **formal pre-frontend WordPress phase**. Frontend implementation must not begin with unresolved content ownership.

Blueprint mapping: expand **P1 Content model** into **P1 + P1b**. Lifecycle mapping: FWP-04 outputs the pack below before FWP-07 code.

**Required outputs before theme field wiring:**

1. Entity map  
2. Storage map  
3. Relationship map  
4. Site Settings map  
5. Page field / editability map  
6. Reusable component map (data contracts)  
7. Admin information architecture  
8. Editor workflow checklist (can be filled as a plan, signed after Admin exists)  
9. URL ownership  
10. SEO ownership  
11. Migration assumptions (even if “greenfield — none”)

Pack templates: §18.

---

## 17. Future second-site baseline (starting reference, not a hard requirement)

Typical company / services website:

| Layer | Starting model |
|-------|----------------|
| **Pages** | Home, About, Contacts, policy/legal, unique landings |
| **Posts** | Articles / blog |
| **CPT candidates** | Services; Specialists/Team; Cases/Projects; Reviews depending on scale |
| **Taxonomies** | Project-dependent (topics, types) — do not invent unused ones |
| **Global Options** | Contacts, social, header/footer, integrations, global CTA |
| **Page fields** | Page-specific Hero / content sections per PAGE-EDITABILITY-MAP |
| **Optional modules** | Smart Search, DOCX, Activity Log, advanced forms — [MODULE-CATALOG](../registries/FORGE-WORDPRESS-MODULE-CATALOG-v1.md) |

Editors should see business concepts in the left menu (Услуги, Специалисты, Статьи, Настройки сайта), not a dump of internal modules.

---

## 18. CMS architecture deliverable pack

For every future WP Forge site, fill:

| Artifact | Template |
|----------|----------|
| CONTENT-ENTITY-MAP | [template](../templates/FORGE-WORDPRESS-CONTENT-ENTITY-MAP-TEMPLATE-v1.md) |
| FIELD-OWNERSHIP-MAP | [template](../templates/FORGE-WORDPRESS-FIELD-OWNERSHIP-MAP-TEMPLATE-v1.md) |
| PAGE-EDITABILITY-MAP | [template](../templates/FORGE-WORDPRESS-PAGE-EDITABILITY-MAP-TEMPLATE-v1.md) |
| SITE-SETTINGS-MAP | [template](../templates/FORGE-WORDPRESS-SITE-SETTINGS-MAP-TEMPLATE-v1.md) |
| RELATIONSHIP-MAP | [template](../templates/FORGE-WORDPRESS-RELATIONSHIP-MAP-TEMPLATE-v1.md) |
| COMPONENT-DATA-CONTRACT | [template](../templates/FORGE-WORDPRESS-COMPONENT-DATA-CONTRACT-TEMPLATE-v1.md) |
| ADMIN-INFORMATION-ARCHITECTURE | [template](../templates/FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-TEMPLATE-v1.md) |
| EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST | [template](../templates/FORGE-WORDPRESS-EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST-v1.md) |
| DESIGN-TO-CMS-MAPPING-WORKSHEET | [template](../templates/FORGE-WORDPRESS-DESIGN-TO-CMS-MAPPING-WORKSHEET-v1.md) |
| CMS-MIGRATION-PLAN | [template](../templates/FORGE-WORDPRESS-CMS-MIGRATION-PLAN-TEMPLATE-v1.md) when data already exists |

Existing FW-T-04 CONTENT-MODEL remains the **summary registry**; this pack is the operational depth behind it.

---

## 19. Frontend consumption

Templates must not scatter competing `get_field()` + fallback + formatting logic.

Desired level: **one data contract per component** — helper / module service / assembler. Cross-cutting normalization (phone format, URL, social icon, typography, reading time, SEO fallback) has **one canonical owner** (P16 lesson generalized).

Rendering contract: [COMPONENT DATA CONTRACT](FORGE-WORDPRESS-COMPONENT-DATA-CONTRACT-STANDARD-v1.md).

---

## 20. Content lifecycle and relational integrity

Entities may be draft, publish, private, scheduled, trash. Queries must be intentional. Never assume every related record is publishable.

If a related object is unpublished, deleted, or unavailable: **fail gracefully** — no broken card, no empty link to `#`, no PHP notices. Document the fallback (skip item / hide block / use global CTA).

---

## 21. Schema change and migration

Field architecture is a migration surface. Prefer IDs, relationships, attachment IDs, global settings over absolute URLs and pasted HTML.

When promoting Page → CPT (proven specialists path): inventory → mapping → dry-run → backup → create/retarget objects → copy fields → preserve slugs/URLs → update relationships → update queries/search/sitemap → verify → retire old owner → rollback plan.

Use [CMS-MIGRATION-PLAN](../templates/FORGE-WORDPRESS-CMS-MIGRATION-PLAN-TEMPLATE-v1.md). Silent field renames that orphan meta are **MAJOR**.

---

## 22. Related standards

| Topic | Document |
|-------|----------|
| ACF fields, naming, JSON, validation | [ACF FIELD MODELING](FORGE-WORDPRESS-ACF-FIELD-MODELING-STANDARD-v1.md) |
| Repeater limits and promotion | [REPEATER VS ENTITY](FORGE-WORDPRESS-REPEATER-VS-ENTITY-DECISION-MATRIX-v1.md) |
| Menus, tabs, list tables | [ADMIN IA](FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-STANDARD-v1.md) |
| Labels, Gutenberg, roles, acceptance | [EDITOR UX](FORGE-WORDPRESS-EDITOR-UX-STANDARD-v1.md) |
| Component contracts, empty states | [COMPONENT DATA CONTRACT](FORGE-WORDPRESS-COMPONENT-DATA-CONTRACT-STANDARD-v1.md) |
| Figma → schema | [DESIGN-TO-CMS](FORGE-WORDPRESS-DESIGN-TO-CMS-WORKFLOW-v1.md) |
| Relations and permalinks | [RELATIONSHIP MODELING](FORGE-WORDPRESS-RELATIONSHIP-MODELING-STANDARD-v1.md) |
| Globals and fallbacks | [GLOBAL SETTINGS OWNERSHIP](FORGE-WORDPRESS-GLOBAL-SETTINGS-OWNERSHIP-STANDARD-v1.md) |
| CMS anti-patterns | [CMS ANTI-PATTERNS](FORGE-WORDPRESS-CMS-ANTI-PATTERNS-v1.md) · [AP registry](FORGE-WORDPRESS-ANTI-PATTERN-REGISTRY-v1.md) |

---

## 23. Operational speed objective

A future site should not spend weeks on:

- Should this be a Page or a CPT?  
- Where should this field live?  
- Why is this phone duplicated?  
- Why do we have 40 repeater rows?  
- Why can’t the editor understand this screen?  
- Why is the staging hostname in content?

If those questions are still open at implementation start, **P1b is not done**.

---

*FW-S-22 v1 — 2026-08-18. Data model and editor experience are one architecture. Not a shipped ACF library. Not a claim that every FP-0002 field group is a universal default.*
