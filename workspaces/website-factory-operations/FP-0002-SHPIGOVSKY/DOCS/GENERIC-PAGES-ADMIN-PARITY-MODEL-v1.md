# GENERIC PAGES ADMIN PARITY MODEL v1

**Project:** FP-0002 Shpigovsky  
**Wave:** V9-06E52  
**Status:** Implemented locally (not freeze-accepted until operator review)  
**Scope:** Ordinary WordPress pages using `page-templates/generic.php`

---

## 1. Purpose

Bring normal/generic pages to the same operational pattern as services (E50/E51):

- Demo/current visible content lives in **ACF** as source of truth.
- Frontend reads ACF; empty optional fields **hide** (no template demo inject).
- Optional **Заглушка** layout mode (shell + H1 only).

---

## 2. Included pages (E52 inventory)

All publish pages with template `page-templates/generic.php` (15):

| IDs | Family |
|---:|---|
| 12–16 | `/o-centre/` children (О нас, Программа лечения, Галерея, Специалистам, Родственникам) |
| 1039 | Интервью и СМИ |
| 1053–1056 | Программа лечения deep children |
| 1030 | Специалисты hub |
| 1031–1033, 1097 | Specialist children |

**Excluded:** Home, posts page, dedicated templates (services hub, institutional hub, contacts, reviews, legal), service CPT.

Evidence: `REPORTS/evidence/v9-06e52-generic-pages-inventory.csv`

---

## 3. Admin field groups

### 3.1 Макет страницы — `group_fp02_page_layout_mode`

| Field | Choices | Default |
|---|---|---|
| `page_layout_mode` | `full` = Полная страница; `placeholder` = Заглушка | `full` |

Location: `page_template == page-templates/generic.php`

Help: Полная страница shows editable blocks; Заглушка temporarily shows header/nav/H1/footer only; content preserved.

### 3.2 Содержимое страницы — `group_fp02_page_generic_content`

| Field | Type | Optional empty behavior |
|---|---|---|
| `generic_page_lead` | textarea | Hide lead block |
| `generic_page_body` | wysiwyg | Hide body (no demo inject) |

`hide_on_screen` (this group): the_content, excerpt, discussion, comments, revisions, author, format, categories, tags, send-trackbacks.  
**Kept:** featured image, page attributes (specialists / hierarchy).

Additional admin clutter removal: `EditorRestrictions::remove_generic_page_clutter()` for generic template only.

---

## 4. Frontend rules

| Mode | Render |
|---|---|
| `full` | Header / nav / breadcrumbs / H1 / optional specialist photo / ACF lead+body / footer |
| `placeholder` | Header / nav / H1 / footer only (`generic.php`) |

**SoT:** ACF `generic_page_*` when ACF is available.  
**Empty:** hide — no hardcoded «Раздел находится в подготовке…».  
**Emergency:** `post_content` only if ACF plugin unavailable (technical reserve).

Specialist children: featured image / placeholder photo unchanged (not ACF text).

---

## 5. Seeding rules (E52)

1. Export meta/content before.
2. Seed empty `generic_page_body` from current `post_content` (page-specific).
3. Leave `generic_page_lead` empty (hide) unless already set.
4. Preserve meaningful existing ACF.
5. Do not mass-enable placeholder; default/final `full`.
6. Store ACF value under meta `generic_page_body` + `_generic_page_body` = field key (not key-as-name).

---

## 6. Relations to frozen work

| Area | Relation |
|---|---|
| Home E42 | Untouched |
| Services hub E44 | Untouched |
| Sections E50 | Untouched |
| Services E47–E49 | Untouched |
| Placeholder Mode E51 (service CPT) | Untouched; generic uses separate `page_layout_mode` |

---

## 7. Evidence

- `v9-06e52-generic-pages-inventory.csv`
- `v9-06e52-generic-pages-current-model-audit.csv`
- `v9-06e52-generic-pages-seeding.csv`
- `v9-06e52-generic-placeholder-switch-validation.csv`
- `v9-06e52-generic-pages-frontend-validation.csv`
- `v9-06e52-empty-field-hide-validation.csv`
- `v9-06e52-regression-validation.csv`
- `v9-06e52-source-runtime-sync.csv`

Report: `REPORTS/REPORT-FP-0002-V9-06E52-generic-pages-demo-acf-sot-placeholder.md`
