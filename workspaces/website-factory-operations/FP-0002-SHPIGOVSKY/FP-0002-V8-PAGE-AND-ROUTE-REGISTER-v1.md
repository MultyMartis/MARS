# FP-0002 V8 — Page and Route Register v1

**Date:** 2026-07-01  
**Baseline:** `eb47ebb` · tag `fp-0002-v8-operator-approved-frontend-stable-01`  
**Workspace:** `workspaces/fp-0002-shpigovsky-v8/`

---

## Legend

| Status | Meaning |
|--------|---------|
| OPERATOR_APPROVED | Explicit operator visual approval recorded |
| STABLE_PREVIOUSLY_APPROVED | Stable from earlier per-page passes; included in baseline |
| TECHNICAL_SMOKE_PASS | Built and smoke-tested; dedicated mobile pass may lag |
| NOT_IMPLEMENTED | No V8 source page |
| DEFERRED | Planned; not in current baseline |

---

## Implemented pages (10)

### 1. Home

| Field | Value |
|-------|-------|
| Canonical name | Home / Главная |
| Page ID | FP0002-TPL-001 (template reference) |
| Source | `src/pages/index.html` |
| Output | `dist/index.html` |
| Preview route | `/index.html` |
| Production route | `/` |
| Page family | Core / Home |
| Desktop | OPERATOR_APPROVED |
| Mobile | OPERATOR_APPROVED |
| Content | Production fixture copy; `TEMPORARY_SEO_COPY` in meta |
| Demo readiness | Ready — primary entry |
| WordPress type | Front page template |
| Shared deps | header, footer, hero, founder-quote, comfort, specialists, faq, final-form, modal |
| Limitations | Full long-scroll home; no pagination |

### 2. O-Centre

| Field | Value |
|-------|-------|
| Canonical name | O-Centre / О центре |
| Source | `src/pages/o-centre.html` |
| Output | `dist/o-centre.html` |
| Preview route | `/o-centre.html` |
| Production route | `/o-centre/` (expected) |
| Page family | Core / About |
| Desktop | STABLE_PREVIOUSLY_APPROVED |
| Mobile | STABLE_PREVIOUSLY_APPROVED |
| Content | Institutional narrative sections |
| Demo readiness | Ready |
| WordPress type | Page template |
| Shared deps | header, footer, hero-inner, institutional/infrastructure narratives, comfort, modal |
| Limitations | Historical audit docs conflict — baseline record is authority |

### 3. Contacts

| Field | Value |
|-------|-------|
| Canonical name | Contacts / Контакты |
| Source | `src/pages/kontakty.html` |
| Output | `dist/kontakty.html` |
| Preview route | `/kontakty.html` |
| Production route | `/kontakty/` |
| Page family | Core / Contacts |
| Desktop | STABLE_PREVIOUSLY_APPROVED |
| Mobile | STABLE_PREVIOUSLY_APPROVED |
| Content | Map body + rehabilitation steps |
| Demo readiness | Ready |
| WordPress type | Page template |
| Limitations | Map may be static embed |

### 4. Reviews

| Field | Value |
|-------|-------|
| Canonical name | Reviews / Отзывы |
| Source | `src/pages/otzyvy.html` |
| Output | `dist/otzyvy.html` |
| Preview route | `/otzyvy.html` |
| Production route | `/otzyvy/` |
| Page family | Content / Reviews archive |
| Desktop | STABLE_PREVIOUSLY_APPROVED |
| Mobile | STABLE_PREVIOUSLY_APPROVED |
| Content | Archive cards + rehabilitation requirements block |
| Demo readiness | Ready |
| WordPress type | Archive or page + query |
| Limitations | No single-review detail page |

### 5. Blog archive

| Field | Value |
|-------|-------|
| Canonical name | Blog archive / Статьи |
| Source | `src/pages/blog.html` |
| Output | `dist/blog.html` |
| Preview route | `/blog.html` |
| Production route | `/blog/` |
| Page family | Content / Blog archive |
| Desktop | STABLE_PREVIOUSLY_APPROVED |
| Mobile | STABLE_PREVIOUSLY_APPROVED |
| Content | Card list + lower stack (expert quote, CTA) |
| Demo readiness | Ready |
| WordPress type | `home.php` or archive template |
| Limitations | Placeholder excerpts; no pagination |

### 6. Blog Article

| Field | Value |
|-------|-------|
| Canonical name | Blog Article / Статья |
| Source | `src/pages/blog/nazvanie-stati.html` |
| Output | `dist/blog/nazvanie-stati.html` |
| Preview route | `/blog/nazvanie-stati.html` |
| Production route | `/blog/nazvanie-stati/` (fixture slug) |
| Page family | Content / Blog single |
| Desktop | OPERATOR_APPROVED |
| Mobile | OPERATOR_APPROVED |
| Content | Alcohol dependence article fixture |
| Demo readiness | Ready as article template |
| WordPress type | `single.php` / custom post template |
| Limitations | Related links placeholder; internal link TODOs in copy |

### 7. Services hub

| Field | Value |
|-------|-------|
| Canonical name | Services hub (legacy) |
| Source | `src/pages/uslugi.html` |
| Output | `dist/uslugi.html` |
| Preview route | `/uslugi.html` |
| Production route | `/uslugi/` |
| Page family | Service / Hub |
| Desktop | STABLE_PREVIOUSLY_APPROVED |
| Mobile | TECHNICAL_SMOKE_PASS |
| Content | Category hub layout |
| Demo readiness | Usable; v2 preferred for demo nav |
| WordPress type | Page or archive parent |
| Limitations | Superseded visually by uslugi-v2 for template work |

### 8. Services v2

| Field | Value |
|-------|-------|
| Canonical name | Services hub v2 |
| Page ID | FP0002-TPL-002 |
| Source | `src/pages/uslugi-v2.html` |
| Output | `dist/uslugi-v2.html` |
| Preview route | `/uslugi-v2.html` |
| Production route | `/uslugi/` (target) |
| Page family | Service / Hub |
| Desktop | STABLE_PREVIOUSLY_APPROVED |
| Mobile | TECHNICAL_SMOKE_PASS |
| Content | Category sections v2 |
| Demo readiness | Ready — canonical service hub template |
| WordPress type | Page template |

### 9. Service subdivision

| Field | Value |
|-------|-------|
| Canonical name | Service subdivision |
| Page ID | FP0002-TPL-003 |
| Source | `src/pages/usluga-podrazdel-v1.html` |
| Output | `dist/usluga-podrazdel-v1.html` |
| Preview route | `/usluga-podrazdel-v1.html` |
| Production route | `/uslugi/zavisimosti/` (fixture) |
| Page family | Service / Section |
| Desktop | STABLE_PREVIOUSLY_APPROVED |
| Mobile | TECHNICAL_SMOKE_PASS |
| Demo readiness | Ready as section template |
| WordPress type | Page template or taxonomy archive |

### 10. Service leaf

| Field | Value |
|-------|-------|
| Canonical name | Service leaf |
| Page ID | FP0002-TPL-004 |
| Source | `src/pages/usluga-konechnaya-v1.html` |
| Output | `dist/usluga-konechnaya-v1.html` |
| Preview route | `/usluga-konechnaya-v1.html` |
| Production route | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` |
| Page family | Service / Leaf |
| Desktop | STABLE_PREVIOUSLY_APPROVED |
| Mobile | TECHNICAL_SMOKE_PASS |
| Demo readiness | Ready as leaf template |
| WordPress type | Page template |
| Limitations | Lorem in program block |

---

## Not implemented in V8 (design / Excel inventory)

| Page (inventory) | Excel / design | V8 status | Notes |
|------------------|----------------|-----------|-------|
| Legal hub | FP-0002-PG-010 | NOT_IMPLEMENTED | Phase 07C disposition required |
| 404 | FP-0002-PG-011 | NOT_IMPLEMENTED | Phase 07C disposition required |
| Specialists archive | Missing from design pack | NOT_IMPLEMENTED | Section on home only |
| Review detail | Planned | NOT_IMPLEMENTED | DEFERRED |
| Genotyping leaf | Excel `/uslugi/genotipirovanie/` | NOT_IMPLEMENTED | Home section exists |
| Additional service leaves | Excel tree | NOT_IMPLEMENTED | Template reuse in 07C |

---

## Utility / test routes

None in `src/pages/` beyond the 10 production pages above.

---

## Historical variants (not canonical)

| File | Status |
|------|--------|
| `o-centre-v1.html` | Rejected WIP — excluded from V8 |
| V7 demo pages | Historical — see V7 workspace |

---

*Register reconciled against V8 source at baseline `eb47ebb`.*
