# LANDING Scaffold Manifest v1

**Page type:** `LANDING_PAGE`  
**Site type:** `LANDING`  
**Scaffold file:** `src/pages/index.html`  
**Output:** `dist/index.html`  
**Status:** STUB-DECLARED · T1+ HONESTY  
**Metric:** RSC — LANDING wave **1/1**

**Authority:** [wf-r01-3-2-landing-completion-charter-v1.md](../../projects/mars-website-factory/wf-r01-3-2-landing-completion-charter-v1.md) Wave D · [PAGE-TYPE-REGISTRY-v1.md](page-architecture/PAGE-TYPE-REGISTRY-v1.md)

---

## Scaffold identity

| Field | Value |
|-------|-------|
| **page_type** | `LANDING_PAGE` |
| **site_type_code** | `LANDING` |
| **Scaffold path** | `workspaces/website-factory-reference-v1/src/pages/index.html` |
| **Build command** | `npm run build` |
| **Global RSC denominator** | **10** primary page types (PAGE-TYPE-REGISTRY-v1 Core minimum set) |
| **Global RSC numerator** | **1** — only `LANDING_PAGE` scaffold exists |
| **LANDING wave RSC** | **1/1** |

---

## Stub honesty declaration

This scaffold is a **single-page golden slice** for the LANDING reference workspace. It is **not** a multi-route site tree. Secondary LANDING routes (`CONTACT_PAGE`, `FAQ_PAGE`, etc.) are **not** scaffolded at G1.

| Property | Declaration |
|----------|-------------|
| **Stub type** | Full-stack single page with T1+ section partials |
| **Production scaffold** | **No** — reference implementation only |
| **CMS binding** | **None** |
| **Route model** | `/` only (`index.html`) |

---

## Shell composition (validated)

```text
HEADER_NAV  →  layout/header.html → sections/header-nav.html
MAIN        →  <main id="main"> (content sections only)
FOOTER      →  sections/footer.html (after </main>)
  └── LEGAL_LINKS → components/legal-links.html (nested)
```

**Post–G1 correction:** FOOTER relocated outside `<main>` (was incorrectly nested pre–G1 exit).

---

## MAIN include stack

Ordered `@@include` list in `src/pages/index.html`:

1. `hero.html`
2. `benefits.html`
3. `process.html`
4. `testimonials.html`
5. `trust.html`
6. `cases.html`
7. `pricing.html`
8. `lead_form.html`
9. `cta_band.html`
10. `faq.html`
11. `contact_block.html`

---

## Cross-references

| Artifact | Path |
|----------|------|
| Reference Composition (PC) | [REFERENCE-COMPOSITION-v1.md](REFERENCE-COMPOSITION-v1.md) |
| Golden slice pointer | [golden-implementation-slice-v1.md](../../projects/mars-website-factory/golden-implementation-slice-v1.md) |
| G1 exit evidence | [wf-r01-3-2-g1-five-dimension-exit-v1.md](../../reports/wf-r01-3-2-g1-five-dimension-exit-v1.md) |

---

*Published: 2026-06-19 — WF-R01.3.2 Gate G1 exit pass*
