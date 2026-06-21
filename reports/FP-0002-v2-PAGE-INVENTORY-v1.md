# FP-0002 v2 — Page Inventory v1

**Document type:** Page Inventory (v2 audit pass — fresh verification)  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-22  
**Workspace:** `workspaces/fp-0002-shpigovsky-v2/`  
**Method:** Disk verification + FIG decode (`openfig-core` 0.3.7, 2026-06-22) + PDF header check — **not** v1 inventory as sole truth  

**Authority (this pass):** PRIMARY = FIG · SECONDARY = PDF · VISUAL CONTROL = JPG · OPERATOR = tie-breaker — **APPROVED for this pass**

**Upstream (reference only, re-verified):** `FP-0002-PAGE-INVENTORY-v1.md`, `FP-0002-v2-SOURCE-AVAILABILITY-CHECK-v1.md`, `REPORTS/_fig_audit_page_sections_v2.json`

---

## Status legend

| Status | Meaning |
|--------|---------|
| **READY** | Desktop + mobile sources confirmed; pair usable for Discovery |
| **PARTIAL** | Source exists with naming/responsive/structure debt |
| **BLOCKED** | No usable source for page type |
| **SAFE UNKNOWN** | Evidence insufficient without operator action |

---

## 1. Page master table

| PAGE ID | NAME | DESKTOP SOURCE | MOBILE SOURCE | FIG AVAILABLE | STATUS |
|---------|------|----------------|---------------|---------------|--------|
| **FP-0002-PG-001** | Главная (v2 canonical) | `2026-06-11-home-v2/Главная страница (v2).pdf` | `2026-06-11-home-v2/Главная страница - моб (v2).pdf` | ✓ `Главная страница` · `Главная страница - моб` | **READY** |
| **FP-0002-PG-002** | Услуги — хаб | `Услуги хаб.pdf` | `Услуги хаб - моб.pdf` | ✓ | **READY** |
| **FP-0002-PG-003** | Услуга — подраздел | `Услуга подраздел.pdf` | `Услуга подраздел - моб.pdf` | ✓ | **READY** |
| **FP-0002-PG-004** | Услуга — конечная | `Услуга конечная.pdf` | `Услуга конечная - моб.pdf` | ✓ | **READY** |
| **FP-0002-PG-005** | О центре | `О центре.pdf` | `О центре - моб.pdf` | ✓ | **READY** ‡ |
| **FP-0002-PG-006** | Контакты | `Контакты.pdf` | `Контакты - моб.pdf` | ✓ | **READY** |
| **FP-0002-PG-007** | Отзывы | `Отзывы.pdf` | `Отзывы - моб.pdf` | ✓ | **READY** |
| **FP-0002-PG-008** | Статьи — хаб | `Блог хаб.pdf` | ‡ see pairing §3 | ✓ `Блог хаб - моб` | **PARTIAL** |
| **FP-0002-PG-009** | Статья | `Статья.pdf` | `Статья - моб.pdf` | ✓ `Статья` · `Статья - моб` | **READY** |
| **FP-0002-PG-010** | Правовая информация | `Правовая инфа.pdf` | `Правовая инфа - моб.pdf` | ✓ | **READY** |
| **FP-0002-PG-011** | 404 | `404.pdf` | `404 - моб.pdf` | ✓ | **READY** |

‡ **PG-005:** Full PDF pair + FIG frames confirmed; **FIG desktop ↔ mobile section naming diverges** (see Design Audit Report §A3) — does not block inventory, records Discovery debt.

### Superseded (on disk — not canonical)

| Role | Files | Treatment |
|------|-------|-----------|
| Home v1 | `Главная стр.pdf` · `Главная стр - моб.pdf` | **DUPLICATED** — superseded by Home v2; exclude from Discovery default |

---

## 2. Corrections vs v1 Page Inventory

| Item | v1 claim | v2 verified fact |
|------|----------|------------------|
| Visual SoT | PDF-only; Figma absent | **Superseded** — `Шпиговский.fig` present, decodable, 11/11 template pairs |
| PG-009 mobile | **Partial** — mobile missing | **READY** — `Статья - моб.pdf` **FOUND** on disk (2026-06-22) |
| PG-008 mobile | Misnamed `Блог конечная - моб.pdf` | **PARTIAL** — canonical name `Блог хаб - моб.pdf` **MISSING** in PDF; FIG frame **FOUND**; misnamed PDF may exist — operator rename required |
| FIG availability | Not in v1 scope | **All 11 page types** have desktop + `- моб` top-level frames on FIG `Page 1` |

---

## 3. FIG frame register (machine discovery)

| PAGE ID | FIG desktop frame | W×H | FIG mobile frame | W×H |
|---------|-------------------|-----|------------------|-----|
| PG-001 | Главная страница | 1437×16809 | Главная страница - моб | 380×22883 |
| PG-002 | Услуги хаб | 1437×11999 | Услуги хаб - моб | 380×17611 |
| PG-003 | Услуга подраздел | 1437×13675 | Услуга подраздел - моб | 380×18101 |
| PG-004 | Услуга конечная | 1437×13313 | Услуга конечная - моб | 380×18136 |
| PG-005 | О центре | 1437×12830 | О центре - моб | 390×16586 |
| PG-006 | Контакты | 1437×4505 | Контакты - моб | 380×4827 |
| PG-007 | Отзывы | 1437×5155 | Отзывы - моб | 380×6902 |
| PG-008 | Блог хаб | 1437×5031 | Блог хаб - моб | 380×8678 |
| PG-009 | Статья | 1437×11861 | Статья - моб | 380×17833 |
| PG-010 | Правовая инфа | 1437×3151 | Правовая инфа - моб | 380×5035 |
| PG-011 | 404 | 1437×1900 | 404 - моб | 380×1734 |

---

## 4. Missing pages register (unchanged scope — no new pages invented)

| ID | Mention | Design PDF | Status |
|----|---------|------------|--------|
| M-01 | Специалисты (листинг) | None | PROJECT DECISION |
| M-02 | Детальная страница отзыва | None | PROJECT DECISION |
| M-03…M-04 | Legal sub-pages | Hub only | PROJECT DECISION |
| M-05 | Генотипирование (service page) | Section on Home only | SAFE UNKNOWN |
| M-06 | Modal «Заказать звонок» | CTA only | SAFE UNKNOWN |

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 (v2 audit pass) |
| Supersedes for v2 work | `FP-0002-PAGE-INVENTORY-v1.md` as unchecked truth |
| Next | Block Inventory v2 · Discovery |
