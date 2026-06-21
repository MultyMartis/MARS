# Frontend Lessons v1 — Website Factory

**Source workspace (lessons era):** `triumph-manipulator-landing-v5` — **canonical edit surface today:** `triumph-manipulator-landing-v6`  
**Cross-ref:** `projects/mars-website-factory/frontend-production-invariants-v1.md`

## Lessons learned (encode in ORCA → Factory bridge)

| # | Lesson | Evidence |
|---|--------|----------|
| L1 | **Never ship v4 index hero semantics** on PPC routes | v4 `screen-01-hero.html` fleet + fake rate |
| L2 | **Hero needs explicit layout contract** — grid zones, not just copy | `hero--v5` + `_v5-hero-extensions.scss` emerged in production |
| L3 | **Bg image = separate layer** with overlay stack | Prevents text/photo competition |
| L4 | **Inline form is default for PPC** on desktop | zakaz partial |
| L5 | **Share page01 trust/footer** across routes — document shared partial risk | index includes `v5-page01/*` |
| L6 | **Typography nbsp discipline** required for Russian PPC | v5-word-splitting report |
| L7 | **Hero img dimensions must match file** | hardening audit CLS |
| L8 | **`data-cta-source` attributes** help human QA — not analytics product | cargo cards |
| L9 | **Mock form handler is launch blocker** | production hardening audit |
| L10 | **Legacy SCSS coexists** — v4 hero rules may dead-code in bundle | cleanup low priority |

## What Factory did well without pack

- Recovered semantic locks from doctrine after v4 drift
- Standardized section rhythm with 5-ton page01 kit
- Applied PPC-scoped `data-page-type` styling

## What Factory cannot infer reliably

- Which H1 wins for multi-ad groups
- Trust hero mode (stars vs ops)
- Max density / cargo count
- Mobile CTA order when instance says call-first

## Invariant candidates (governance-free note)

Suggest future addition to Website Factory invariants:

- PPC hero must not contain fleet tonnage ranges
- PPC hero must not contain placeholder currency
- Qualification line required when blueprint marks anti-evacuation

**This calibration doc does not edit Factory governance.**
