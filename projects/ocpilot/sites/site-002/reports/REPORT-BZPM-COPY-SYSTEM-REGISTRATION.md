# REPORT — BZPM COPY SYSTEM REGISTRATION

**Task:** BZPM Corporate Pages Copy Artefact System registration  
**Date:** 2026-06-22  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Policy:** MANUAL UI REFINEMENTS ARE CANONICAL  
**Mode:** Documentation only — **no** copywriting · **no** design · **no** implementation · **no** deploy · **no** TEST/production changes

---

## 1. Summary

Система **COPY ARTEFACTS** для Corporate Pages Program (M9.13–M9.18) зарегистрирована в MARS. Для каждой страницы программы зафиксирована модель **четырёх обязательных артефактов**: Research → IA → Copy → Design Charter. Создан канонический стандарт [BZPM-COPY-STANDARDS-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-COPY-STANDARDS-v1.md) и шесть PAGE-COPY v1 **shells** (статус **REGISTERED** — полный текст страницы **не начат**).

| Field | Value |
|-------|--------|
| **Copy system status** | **REGISTERED** |
| **Copy content status** | **NOT STARTED** (all pages) |
| **Commit** | **NO** |
| **Push** | **NO** |
| **Deploy** | **NO** |

---

## 2. Files updated

| File | Change |
|------|--------|
| [BZPM-CORPORATE-PAGES-PROGRAM-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-PROGRAM-v1.md) | Copy system phase; registry columns Copy / Design Charter; workflow gates |
| [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-IA-MAP-v1.md) | Copy phase in program table; IA → Copy → Design Charter sequence |
| [BZPM-PRODUCT-ROADMAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md) | Copy column; PAGE-COPY links; copy standard reference |
| [site-passport.md](../site-passport.md) | Copy system status; PAGE-COPY artifact index |
| [OCPILOT-STATE.md](../../OCPILOT-STATE.md) | SITE-002 focus; Corporate Pages row; evidence links; changelog |
| [README.md](../README.md) | Active stage; Copy standard + PAGE-COPY index links |

---

## 3. New files

| File | Role |
|------|------|
| [BZPM-COPY-STANDARDS-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-COPY-STANDARDS-v1.md) | Canonical copy standard — purpose, artefacts, naming, versioning, approval workflow |
| [BZPM-M9.13-ABOUT-COMPANY-PAGE-COPY-v1.md](../copy/BZPM-M9.13-ABOUT-COMPANY-PAGE-COPY-v1.md) | M9.13 PAGE-COPY shell — **REGISTERED** |
| [BZPM-M9.14-DELIVERY-PAGE-COPY-v1.md](../copy/BZPM-M9.14-DELIVERY-PAGE-COPY-v1.md) | M9.14 PAGE-COPY shell — **REGISTERED** |
| [BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md](../copy/BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md) | M9.15 PAGE-COPY shell — **REGISTERED** |
| [BZPM-M9.16-DEALERS-PAGE-COPY-v1.md](../copy/BZPM-M9.16-DEALERS-PAGE-COPY-v1.md) | M9.16 PAGE-COPY shell — **REGISTERED** |
| [BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md](../copy/BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md) | M9.17 PAGE-COPY shell — **REGISTERED** |
| [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.md](../copy/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.md) | M9.18 PAGE-COPY shell — **REGISTERED** |
| [REPORT-BZPM-COPY-SYSTEM-REGISTRATION.md](REPORT-BZPM-COPY-SYSTEM-REGISTRATION.md) | This registration report |

**Storage:** PAGE-COPY artefacts → `projects/ocpilot/sites/site-002/copy/`

---

## 4. Copy standard summary

Каждый approved PAGE-COPY файл обязан содержать **полный финальный текст страницы**:

- H1 · Lead
- Все блоки сверху вниз · все заголовки · все тексты
- FAQ · CTA · тексты форм · микро-тексты · подписи · служебные тексты

Страница должна быть **полностью воспроизводима** только по документу PAGE-COPY (+ Research + IA для контекста). Запрещены: тезисы, заметки, частичные блоки как канонический источник.

---

## 5. Naming convention

```
BZPM-M9.{NN}-{PAGE-SLUG}-PAGE-COPY-v{N}.md
```

| ID | Registered file |
|----|-----------------|
| M9.13 | `BZPM-M9.13-ABOUT-COMPANY-PAGE-COPY-v1.md` |
| M9.14 | `BZPM-M9.14-DELIVERY-PAGE-COPY-v1.md` |
| M9.15 | `BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md` |
| M9.16 | `BZPM-M9.16-DEALERS-PAGE-COPY-v1.md` |
| M9.17 | `BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md` |
| M9.18 | `BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.md` |

**Versioning:** `v1` = first approved full copy · `v2`, `v3`, … = major operator-approved revisions.

---

## 6. Approval workflow

```
Research  →  IA  →  Copy  →  Design Charter  →  Design  →  Implementation
```

| Gate | Requirement |
|------|-------------|
| Copy pass | Operator-approved IA (map section or whole map) |
| Design Charter | PAGE-COPY status **COPY COMPLETE** + operator approval |
| Design | Per-page Design Charter approved |
| Implementation | Design approved + implementation charter |

Research complete **≠** copy authorized without IA approval.  
Copy complete **≠** design authorized without Design Charter.

---

## 7. Four-artefact model (per page)

| # | Artefact | M9.13–M9.18 status |
|---|----------|-------------------|
| 01 Research | **COMPLETE** — forensic reports in `site-002/reports/` |
| 02 IA | **READY** — per-page sections in IA map |
| 03 Copy | **REGISTERED** — v1 shells; content **NOT STARTED** |
| 04 Design Charter | **NOT STARTED** |

---

## 8. Recommended next step

**Operator approval** of [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-IA-MAP-v1.md) — затем **первый copy pass** на выбранной странице (рекомендация программы: M9.13 About или M9.16 Dealers / M9.17 Warranty по коммерческому приоритету оператора).

Resolve operator OQ clusters (payment VAT/bank, warranty term, dealer framework, custom SLA) параллельно или до copy pass — они блокируют финальный **COPY COMPLETE** на затронутых страницах.

**Explicit stop:** No copywriting in this task · no design · no implementation.

---

## 9. Git status

Documentation-only pass. **No commit.** **No push.**

---

## 10. SAFE UNKNOWN / SECURITY RISK

| Topic | Status |
|-------|--------|
| Operator IA map verbal approval | **Pending** — map registered, not operator-signed |
| Per-page copy priority order | **Operator decision** — not fixed in this registration |
| Design Charter folder `bzpm-roadmap/charters/` | Reserved in standard — **not created** until charter pass |
| SECURITY RISK | **None identified** |

---

*Copy system registration complete — documentation only.*
