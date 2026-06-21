# FP-0002 v2 — Block Inventory v1

**Document type:** Block Inventory (v2 audit pass)  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-22  
**Sources:** FIG (`Шпиговский.fig`, decoded 2026-06-22) + PDF cross-check + v1 inventory **re-verified**  
**Method:** Component instances + top-level section frames; dedupe by visual role  

**Reuse legend**

| REUSE POTENTIAL | Rule |
|-----------------|------|
| **SHARED** | Global chrome or appears on **5+** page templates |
| **SEMI-SHARED** | **2–4** templates |
| **UNIQUE** | Single page role or single IA slot |

---

## 1. Executive summary

| Metric | v2 count | Notes |
|--------|----------|-------|
| Unique Block IDs | **40** | Matches v1 count after FIG verification — IDs retained for continuity |
| SHARED | **19** | Global + high-repeat marketing blocks |
| SEMI-SHARED | **12** | Service tail, archive patterns |
| UNIQUE | **9** | Page-role slots (About narratives, service IA slots, article body stack) |
| FIG-only naming drift | **YES** | Section **names** in FIG ≠ Block **names** in v1 — mapping by role, not label |

**v2 finding (About / PG-005):** FIG lists **13** desktop / **11** mobile top-level sections; names differ between viewports (`2 - Дом - вступление` vs `Кого мы лечим`, duplicate `Программа центра` on desktop). Block IDs BLK-036…038 remain valid **roles** — exact FIG↔BLK mapping deferred to Discovery text-lock pass.

---

## 2. Master block table

| BLOCK ID | NAME | TYPE | REUSE POTENTIAL | FIG signal | PDF verified |
|----------|------|------|-----------------|------------|--------------|
| FP-0002-BLK-001 | Header — Top Bar | Global Navigation | **SHARED** | `Хедер` band 1 inside `1 - Главный экран` | ✓ |
| FP-0002-BLK-002 | Header — Main Navigation | Global Navigation | **SHARED** | `Хедер` band 2 · 7 nav TEXT + search instance | ✓ |
| FP-0002-BLK-003 | Site Footer | Global Footer | **SHARED** | INSTANCE `Подвал` | ✓ |
| FP-0002-BLK-004 | Mobile Sticky CTA Bar | Global Navigation | **SHARED** | `Подвал моби` / sticky pattern on mobile PDF | ✓ |
| FP-0002-BLK-005 | Breadcrumbs | Navigation | **SHARED** | Present inner pages (not Home/404) | ✓ |
| FP-0002-BLK-006 | In-Page Anchor Navigation | Navigation | **SEMI-SHARED** | Service + About templates | ✓ |
| FP-0002-BLK-007 | Page Hero | Hero | **SHARED** | `1 - Главный экран` / `Моби` — 4 layout contexts | ✓ |
| FP-0002-BLK-008 | 404 Error Content | System | **UNIQUE** | `404` body frames | ✓ |
| FP-0002-BLK-009 | UTP Value Cards | Content | **UNIQUE** | Home `2 - Дом - вступление` cluster | ✓ |
| FP-0002-BLK-010 | Home Services Preview Grid | Service | **UNIQUE** | Home `3- Услуги` | ✓ |
| FP-0002-BLK-011 | Service Catalog Category Grid | Service | **UNIQUE** | Service hub catalog slot | ✓ |
| FP-0002-BLK-012 | Service Section Body | Service | **UNIQUE** | Service section IA slot | ✓ |
| FP-0002-BLK-013 | Service Leaf Body | Service | **UNIQUE** | Service leaf IA slot | ✓ |
| FP-0002-BLK-014 | Feature Cards «Нас выбирают» | Content | **SEMI-SHARED** | Frame `Нас выбирают` | ✓ |
| FP-0002-BLK-015 | Reviews Preview | Review | **SEMI-SHARED** | Frame `Отзывы` · INSTANCE `отзыв` | ✓ |
| FP-0002-BLK-016 | Reviews Archive Listing | Review | **UNIQUE** | PG-007 listing | ✓ |
| FP-0002-BLK-017 | Pagination | System | **SEMI-SHARED** | PG-007 · PG-008 | ✓ |
| FP-0002-BLK-018 | Rehabilitation Steps (01–04) | Content | **SHARED** | `С чего начать` · `Этапы процедуры` · INSTANCE `этап` | ✓ |
| FP-0002-BLK-019 | Guest Visit CTA Section | CTA | **SEMI-SHARED** | Full-width CTA bands | ✓ |
| FP-0002-BLK-020 | Program Four Directions | Service | **SHARED** | `Программа центра` (duplicate frames on some pages — artifact) | ✓ |
| FP-0002-BLK-021 | Genotyping Detail Section | Service | **UNIQUE** | Home `Генотипирование` only | ✓ |
| FP-0002-BLK-022 | Expert Opinion | Content | **SEMI-SHARED** | `Слово спецу` / `Слово специалиста` | ✓ |
| FP-0002-BLK-023 | Comfort · Privacy · Care | Content | **SEMI-SHARED** | `преимущества` / `Комфорт, приватность` | ✓ |
| FP-0002-BLK-024 | Video Section | Content | **UNIQUE** | Home `Видео` | ✓ |
| FP-0002-BLK-025 | Inline Consultation CTA | CTA | **SEMI-SHARED** | INSTANCE `Кнопка` inline | ✓ |
| FP-0002-BLK-026 | Specialists Cards Grid | Specialist | **SEMI-SHARED** | `Специалисты` · INSTANCE `Врач` | ✓ |
| FP-0002-BLK-027 | Articles Preview (Home) | Article | **UNIQUE** | Home `Статьи` | ✓ |
| FP-0002-BLK-028 | Blog Archive Cards Grid | Article | **UNIQUE** | PG-008 grid | ✓ |
| FP-0002-BLK-029 | Article Table of Contents | Article | **UNIQUE** | PG-009 TOC column | ✓ |
| FP-0002-BLK-030 | Article Long-Read Body | Article | **UNIQUE** | PG-009 `Заг+текст` repeats | ✓ |
| FP-0002-BLK-031 | Article Author Meta | Article | **UNIQUE** | PG-009 meta band | ✓ |
| FP-0002-BLK-032 | Article Sources / Bibliography | Article | **UNIQUE** | PG-009 `Заключение` area | ✓ |
| FP-0002-BLK-033 | Related Articles | Article | **UNIQUE** | PG-009 `Статьи` tail | ✓ |
| FP-0002-BLK-034 | FAQ Accordion | FAQ | **SEMI-SHARED** | `faq` · INSTANCE `Расскрытие вопроса` | ✓ |
| FP-0002-BLK-035 | Contact Form «Остались вопросы» | Form | **SEMI-SHARED** | INSTANCE `Поле ввода` ×4 + submit | ✓ |
| FP-0002-BLK-036 | About Narrative — «Кто мы» | About | **UNIQUE** | PG-005 — maps to FIG `2 - Дом - вступление` / mobile `Кого мы лечим` | ✓ |
| FP-0002-BLK-037 | About Narrative — «Наш Дом» | About | **UNIQUE** | PG-005 — FIG `3- Услуги` / mobile `Подход` (name drift) | ✓ |
| FP-0002-BLK-038 | About Infrastructure | About | **UNIQUE** | PG-005 — FIG `преимущества` / infrastructure band | ✓ |
| FP-0002-BLK-039 | Contacts Locations | Contact | **UNIQUE** | PG-006 locations | ✓ |
| FP-0002-BLK-040 | Legal Document Body | Legal | **UNIQUE** | PG-010 body | ✓ |

---

## 3. Page → block composition (canonical scroll order)

Aligned with v1 after FIG spot-check. **PG-005** section **count** in FIG = 13 D / 11 M top-level frames; **block count** below = logical blocks (chrome + content), not raw FIG frame count.

| PAGE ID | Blocks (order) | Top-level FIG sections (D / M) |
|---------|----------------|--------------------------------|
| PG-001 | 001,002,007,009,022†,010,014,015,018,019,020,021,023,024,026,027,034,035,003 | 15 / 15 |
| PG-002 | 001,002,005,006,007,011,014,020,018,022,023,026,015,034,035,019,003 | 12 / — |
| PG-003 | 001,002,005,006,007,012,020,018,022,023,026,015,034,035,019,003 | 14 / — |
| PG-004 | 001,002,005,006,007,013,020,018,022,023,026,015,034,035,019,003 | 14 / — |
| PG-005 | 001,002,005,006,007,036,037,038,020,018,022,023,026,015,019,003 | **13 / 11** |
| PG-006 | 001,002,005,039,018,003 | 5 / — |
| PG-007 | 001,002,005,016,018,017,003 | 4 / — |
| PG-008 | 001,002,005,007,028,017,022,019,025,003 | 7 / — |
| PG-009 | 001,002,005,029,030,031,032,033,019,003 | **17** FIG frames / — |
| PG-010 | 001,002,005,040,003 | 4 / — |
| PG-011 | 008,003 | 4 / — |

† Home: FIG `Слово спецу` y-order anomaly (SECTION-10) — visual order ≠ layer index; Discovery must use **y-bounds sort**, not parent index alone.

---

## 4. G-SERVICE unified template (confirmed)

PG-002 / PG-003 / PG-004 share chrome + tail; **one swap slot**: BLK-011 / BLK-012 / BLK-013.

---

## 5. Out of scope (unchanged)

M-01…M-06 screens — no Block IDs until PDF or charter.

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 (v2 audit pass) |
| Evidence | `_fig_audit_page_sections_v2.json`, `FP-0002-BLOCK-INVENTORY-v1.md` |
