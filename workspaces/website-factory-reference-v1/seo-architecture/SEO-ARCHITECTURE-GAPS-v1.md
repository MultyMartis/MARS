# Website Factory — SEO Architecture Gaps v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/seo-architecture/`  
**Статус:** gaps register — **documentation only, no solutions**

**Правило:** этот документ **только фиксирует** ожидаемые будущие пробелы. Решения, контракты генерации и runtime **не** входят в SEO Architecture Layer v2.

---

## 1. Keyword architecture

| Gap | Notes |
|-----|-------|
| Keyword research methodology | Not defined |
| Keyword-to-page mapping contract | Not defined |
| Keyword cluster / topic model | Not defined |
| Cannibalization detection tooling | Not defined |

---

## 2. Content contracts

| Gap | Notes |
|-----|-------|
| Copy patterns (H1/H2, tone) | Charter — not queued in foundation |
| Content generation contract | Not started |
| Blog / `CONTENT_HUB_PAGE` page type | FUTURE in Page Architecture |
| Long-form editorial standards | Not defined |

---

## 3. Metadata contracts

| Gap | Notes |
|-----|-------|
| Title / description templates | Not defined |
| Open Graph / Twitter card contract | Not defined |
| Canonical URL automation rules | Project-level only |
| hreflang contract | Not defined |
| robots meta production strings | Intent only in v2 |

---

## 4. MIG integration

| Gap | Notes |
|-----|-------|
| MIG ↔ Website Factory SEO handoff | **Explicitly out of scope** v2 |
| Content pipeline from MIG | Not defined |
| Shared entity / brand vocabulary | Not defined |

---

## 5. SEO generation

| Gap | Notes |
|-----|-------|
| AI meta generation | Forbidden in v2 scope |
| Automated schema JSON-LD | Not defined |
| Sitemap generation | Not defined |
| Automated internal link suggestions | Not defined |

---

## 6. SERP intelligence

| Gap | Notes |
|-----|-------|
| SERP scraping / rank tracking | **Explicitly excluded** |
| Competitor SERP analysis pipeline | Not defined |
| SERP feature targeting (snippets, etc.) | Not modeled in v2 |

---

## 7. Validation

| Gap | Notes |
|-----|-------|
| SEO Architecture matrix automated check | Not implemented |
| Page SEO Contract JSON Schema | Not defined |
| CI gate for SEO vs Page Contract | Not implemented |
| Cross-layer validator (SEO + Block + Legal) | Not implemented |
| Technical SEO audit tooling | Out of scope v2 |

---

## 8. Extended site types

| Gap | Notes |
|-----|-------|
| SAAS SEO architecture parity | Shallow v1 registry only |
| WEB_APPLICATION SEO architecture | Shallow v1 registry only |
| MARKETPLACE SEO architecture | Shallow v1 registry only |
| Extended type × intent × page matrix rows | Not in Core v2 |

---

## 9. Downstream layers

| Gap | Notes |
|-----|-------|
| Design System Mapping | **ACCEPTED** (2026-06-04) |
| ORCA visual contract binding | Related external doc; not integrated in v2 |
| Frontend meta implementation standard | Not defined |
| Faceted SEO addendum (CATALOG) | Referenced in v1; not delivered |

---

## 10. Registry hygiene

| Gap | Notes |
|-----|-------|
| `registry/SITE-TYPE-SEO-MAPPING-v1.md` supersession banner | **CLOSED** (acceptance 2026-06-01) |
| PAGE-CONTRACT `seo_requirements` pointer update to v2 path | **CLOSED** (acceptance 2026-06-01) |

---

## SAFE UNKNOWN

- Priority order among gap closures after Design Mapping — **requires charter**.
- Whether SEO validation merges with Page Block Validation CLI — **FUTURE** — no implementation proof.

---

*SEO Architecture Gaps version: v1 — register only, no solutions.*
