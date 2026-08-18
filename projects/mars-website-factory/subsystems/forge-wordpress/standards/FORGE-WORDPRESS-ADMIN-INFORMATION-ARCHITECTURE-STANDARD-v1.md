# Forge WordPress — Admin Information Architecture Standard v1

**ID:** FW-S-25  
**Status:** ACTIVE — PRODUCTION-INFORMED  
**Date:** 2026-08-18  
**Extends:** [FW-S-05 Admin UX](FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md)  
**Companion:** [EDITOR UX](FORGE-WORDPRESS-EDITOR-UX-STANDARD-v1.md) · [CMS ARCHITECTURE](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md)

Admin IA is how WordPress **looks and groups work** for editors: left menu, field groups, tabs, list tables. Curated editor, not unrestricted editor.

---

## 1. Left menu

Design the menu as **business information architecture**.

**Goals:**

- business concepts visible;  
- technical concepts hidden;  
- related settings grouped;  
- dangerous utilities limited.

**Typical shape (locale of the site):**

```text
Услуги
Специалисты
Отзывы          ← only if a collection exists
Статьи
Настройки сайта
```

Optional, not top-level by default: Импорт из Word, Activity Log, Smart Search settings (may live under Site Settings or Tools with a clear label).

**Do not** expose every internal module as a top-level menu. **Do not** leave `options.php`, migration runners, or debug dumps in the client menu (AP-006).

CPT icons: distinct. Menu order: content first, settings next, tools last.

---

## 2. Field grouping on an entity

Possible tabs/groups (use only what the entity needs):

| Group | Typical contents |
|-------|------------------|
| Основное | Title-adjacent, role, short intro, enabled |
| Контент | Body sections, long text |
| Медиа | Gallery beyond featured image |
| Карточка | Fields used **only** on listing cards |
| SEO | seo_title, meta_description |
| Связи | Relationships, taxonomies |
| Дополнительно | Rare fields |

Groups follow **editor workflow**, not the PHP file structure. Important fields first. Advanced/rare later.

Proven: message fields as section titles; instructions that name the frontend surface; featured image as portrait SoT with a notice instead of a duplicate field.

---

## 3. Screen length

Prevent enormous editor pages.

**Strategies:** tabs; groups; conditional logic; CPT extraction; relationships; separate Site Settings; separate module screens.

**Practical warnings:**

| Signal | Action |
|--------|--------|
| > ~25 visible fields without tabs | Add tabs/groups |
| Scroll > 3–4 viewports | Split or conditionals |
| Repeater dominates the screen | § promotion checklist |
| Page template fields + CPT fields mixed | Hide irrelevant metaboxes |
| SEO + GTM + Hero on one untitled stack | Separate groups |

Giant flat ACF editor = AP-CMS-007.

---

## 4. Entity editor pattern (generic)

Example: **Specialist / Team member** (generalize to Service, Case, etc.)

**Native:** title, slug (core permalink row only), featured image if meaningful, status, `menu_order` if collection order matters. Hide parent/template/excerpt/editor when unused.

**ACF:** role/specialty; experience; short intro; profile details; certificates/gallery; relations; SEO.

**Admin list:** thumbnail, name, type/specialization, status/order — not Date-only.

**Frontend contracts (three, not one):**

1. ADMIN RECORD — full edit  
2. COLLECTION CARD — subset  
3. SINGLE PAGE — subset + extras  

Do not assume all single-page fields belong on the listing card. Document in [COMPONENT DATA CONTRACT](../templates/FORGE-WORDPRESS-COMPONENT-DATA-CONTRACT-TEMPLATE-v1.md).

---

## 5. Collection + single + Admin

| Surface | Owns |
|---------|------|
| Hub Page | Intro, hub SEO, layout |
| CPT list table | Find / order / status |
| CPT single Admin | Full entity |
| Card partial | Card contract fields only |
| `single-{cpt}.php` | Single contract |

`has_archive = false` when the hub Page owns the index URL.

---

## 6. Admin list table standard

For important CPTs:

| Possible column | Use when |
|-----------------|----------|
| image | Visual entities |
| title | always |
| category/type | if taxonomy or type field exists |
| relation | if a primary parent/hub is useful |
| order | `menu_order` collections |
| date | articles; optional elsewhere |
| status | if drafts are common |

Remove irrelevant default columns (comments, author, date) when they add noise.

---

## 7. Manual ordering

Use native `menu_order` (page-attributes) for staff order, service order, controlled collections.

Use taxonomy / date / title where that is the real sort. Avoid a second custom order field unless `menu_order` cannot express it.

---

## 8. Site Settings IA

Follow [FW-S-11](FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md) section order: general → contacts → social → SEO/integrations → module settings → **Advanced code last**. System status is a Dashboard widget, not a settings tab.

---

## 9. Slug / permalink UX

WordPress native permalink UI is the only slug editor for public pages/posts/CPTs (AP-002). Uniqueness logic may exist under the hood. The editor sees one owner.

---

*FW-S-25 v1 — business menu, short screens, three presentation contracts.*
