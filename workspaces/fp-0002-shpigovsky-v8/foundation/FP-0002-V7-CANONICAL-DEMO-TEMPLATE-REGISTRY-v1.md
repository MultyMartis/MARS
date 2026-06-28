# FP-0002 V7 — Canonical Demo Template Registry v1

**Status:** CANONICAL_STABLE (four-template baseline freeze)  
**Tag:** `fp-0002-v7-four-template-canonical-demo-baseline-01`  
**Purpose:** Reference baseline for static client demo site generation.

## Template registry

| Template ID | Type | Canonical source | Compiled page | Status | Future demo use |
| ----------- | ---- | ---------------- | ------------- | ------ | --------------- |
| FP0002-TPL-001 | HOME_PAGE_TEMPLATE | `src/pages/index.html` | `dist/index.html` | CANONICAL_STABLE | Главная демосайта |
| FP0002-TPL-002 | SERVICES_HUB_INTERNAL_PAGE | `src/pages/uslugi-v2.html` | `dist/uslugi-v2.html` | CANONICAL_STABLE | Каталог/общая страница услуг |
| FP0002-TPL-003 | SERVICE_SUBDIVISION_INTERNAL_PAGE | `src/pages/usluga-podrazdel-v1.html` | `dist/usluga-podrazdel-v1.html` | CANONICAL_STABLE | Раздел/подраздел услуг |
| FP0002-TPL-004 | SERVICE_LEAF_INTERNAL_PAGE | `src/pages/usluga-konechnaya-v1.html` | `dist/usluga-konechnaya-v1.html` | CANONICAL_STABLE | Конечная услуга |

## Historical reference anchors

| Template | Reference commit / tag |
| -------- | ---------------------- |
| Home | `f5a9ecd7` (prior home baseline) |
| Services hub | `3a3c648b` / `fp-0002-v7-services-v2-internal-page-reference-01` |
| Service subdivision | `eb10c71b` / `fp-0002-v7-service-subdivision-internal-page-reference-01` |
| Service leaf assembly | `48fbb38f` (prior commit; disk state + `style.scss` overrides supersede for visuals) |

## Usage rules

1. **Do not modify** these four source templates during mass page multiplication for the static demo site.
2. Demo URL, `<title>`, and H1 changes must be applied via **page instances**, copies, or include parameters — not by editing the canonical template files.
3. Source templates remain the **reference baseline**; instances inherit structure and styling.
4. Placeholder pages (Header + neutral main + Footer) are **not** a fifth design — see `FP-0002-V7-STATIC-DEMO-PLACEHOLDER-PAGE-CONTRACT-v1.md`.
