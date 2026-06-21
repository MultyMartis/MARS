# CORPORATE Reference Blueprint-Instance v1

**Site type:** `CORPORATE`  
**Reference workspace:** `workspaces/website-factory-reference-v1/`  
**Version:** v1  
**Date:** 2026-06-21  
**Status:** **PUBLISHED · EVIDENCE-ONLY · NOT TEMPLATE-ART · NOT PRODUCTION BLUEPRINT**  
**Authority:** [wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md](../../../projects/mars-website-factory/wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md) §16 · [wf-r01-3-5-w7-cd-corporate-slice-blueprint-evidence-v1.md](../../../projects/mars-website-factory/wf-r01-3-5-w7-cd-corporate-slice-blueprint-evidence-v1.md) · [wf-r01-3-reference-expansion-program-design-v1.md](../../../reports/wf-r01-3-reference-expansion-program-design-v1.md)

**Honesty boundary:** Reference Blueprint-instance companion documentation only. **Not** a vocabulary-canon operational Blueprint. **Not** production IA. **Not** client delivery. **Not** SC PASS. **Not** coverage accrual.

---

## 1. Identity

| Field | Value |
|-------|-------|
| **Artefact class** | Reference Blueprint-instance (SC component per Coverage Model) |
| **site_type_code** | `CORPORATE` (Core 5 — existing) |
| **Pilot slice name** | CORPORATE G3 pilot reference slice |
| **Publication wave** | WF-R01.3.5 W7-CD |

---

## 2. Pilot Page Surfaces

| page_type | Scaffold | Composition | Manifest | G3 pilot role |
|-----------|----------|-------------|----------|---------------|
| `ABOUT_PAGE` | `src/pages/about-page-reference.html` | [ABOUT-PAGE-REFERENCE-COMPOSITION-v1.md](ABOUT-PAGE-REFERENCE-COMPOSITION-v1.md) | [ABOUT-PAGE-SCAFFOLD-MANIFEST-v1.md](ABOUT-PAGE-SCAFFOLD-MANIFEST-v1.md) | **Required** — company narrative · TEAM · TRUST |
| `CONTACT_PAGE` | `src/pages/contact-page-reference.html` | [CONTACT-PAGE-REFERENCE-COMPOSITION-v1.md](CONTACT-PAGE-REFERENCE-COMPOSITION-v1.md) | [CONTACT-PAGE-SCAFFOLD-MANIFEST-v1.md](CONTACT-PAGE-SCAFFOLD-MANIFEST-v1.md) | **Required** — CONTACTS · LEAD_FORM |
| `SERVICE_PAGE` | `src/pages/service-page-reference.html` | [SERVICE-PAGE-REFERENCE-COMPOSITION-v1.md](SERVICE-PAGE-REFERENCE-COMPOSITION-v1.md) | [SERVICE-PAGE-SCAFFOLD-MANIFEST-v1.md](SERVICE-PAGE-SCAFFOLD-MANIFEST-v1.md) | **Pilot extension** — money-page · BENEFITS (FEATURES substitute lane) |

**Not in G3 pilot minimum:** `REVIEWS_PAGE` · `FAQ_PAGE` · `HOME_PAGE` corporate hub — **G4 / optional** per charter §16.

**Site-type note:** Scaffolds were built under PROMO G2-R2 corridor; `PAGE-TYPE-REGISTRY` allows `ABOUT_PAGE` · `CONTACT_PAGE` · `SERVICE_PAGE` on **PROMO** and **CORPORATE**. This blueprint-instance **rebinds evidence** to `CORPORATE` pilot context without scaffold mutation.

---

## 3. Block Selection Map

| Concern | Canonical block | Evidence surface | Maturity | G3 role |
|---------|-----------------|------------------|----------|---------|
| Global shell | HEADER_NAV · FOOTER · LEGAL_LINKS | All three scaffolds | Implemented | Inherited |
| Company narrative | ABOUT | ABOUT_PAGE | PARTIAL / T1+ | **Present** |
| People | TEAM | ABOUT_PAGE | PARTIAL / T1+ | **Present** |
| Trust / proof | TRUST | ABOUT_PAGE | Implemented | Supporting proof |
| Contact / NAP | CONTACTS | CONTACT_PAGE | Implemented | **Present** · MAP geo substitute lane |
| Lead capture | LEAD_FORM | CONTACT_PAGE · SERVICE_PAGE | Implemented | **Present** |
| Capabilities | BENEFITS | SERVICE_PAGE | Implemented | **FEATURES substitution** |
| Workflow | PROCESS | SERVICE_PAGE | Implemented | Supporting |
| Objections | FAQ | SERVICE_PAGE | Implemented | Supporting |
| Commercial action | CTA | SERVICE_PAGE | Implemented | Supporting |
| Reviews lane | REVIEWS | — | No dedicated partial | **TESTIMONIALS substitution** (partial exists; not mounted on pilot scaffolds) |
| Certificates | CERTIFICATES | — | Not implemented | **G4-only RPC** · SC honesty gap |
| Partners | PARTNERS | — | Not implemented | **G4-only RPC** · SC honesty gap |
| Dedicated map | MAP | — | Not implemented | **CONTACTS geo substitution** |
| Dedicated features | FEATURES | — | No dedicated partial | **BENEFITS substitution** |

---

## 4. Substitution Decisions (G3-scoped)

| Missing / dedicated concern | Substitute | Authority | Temporary | G3 allowed |
|-----------------------------|------------|-----------|-----------|------------|
| FEATURES | BENEFITS on SERVICE_PAGE | Charter §11 · §15 · G2-R2 | **Yes** | **Yes** — explicit waiver at G3-F |
| REVIEWS | TESTIMONIALS partial (programme) · TRUST on ABOUT (pilot) | Charter §11 · §30 | **Yes** | **Yes** — non-blocking with waiver |
| MAP | CONTACTS NAP on CONTACT_PAGE | Charter §11 · CONTACT composition §9 | **Yes** | **Yes** — no embed/API in reference |

**Not equivalent to dedicated partial maturity.** G4 hygiene waves (W7-B) remain for honest dedicated partials.

---

## 5. Coverage Dimensions (unchanged by this doc)

| Dimension | Effect |
|-----------|--------|
| RC | **No change** — 32/32 |
| RPC | **No change** — 29/32 |
| RSC | **No change** — 7/11 (three registered scaffolds already accrued at G2-R2) |
| SC | **Evidence input only** — CORPORATE pilot evaluation **NOT PASS** |
| PC | **No change** — no new corporate PC corridor at G3 floor |

---

## 6. Runtime Boundary

Static reference-only · fictional company · fictional NAP · presentation-only forms · `href="#"` · no map API · no CMS · no production claims.

---

## 7. Dist Outputs

| Surface | Dist path | Build |
|---------|-----------|-------|
| ABOUT_PAGE | `dist/about-page-reference.html` | PASS (G2-R2 P3) |
| CONTACT_PAGE | `dist/contact-page-reference.html` | PASS (G2-R2 P2) |
| SERVICE_PAGE | `dist/service-page-reference.html` | PASS (G2-R2 P4) |

---

## 8. Related Authority

| Document | Path |
|----------|------|
| CORPORATE Blueprint (planning) | [blueprints/CORPORATE-BLUEPRINT-v1.md](../blueprints/CORPORATE-BLUEPRINT-v1.md) |
| Site-Type Block Matrix | [block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md](../block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md) § CORPORATE |
| W7-CD evidence package | [wf-r01-3-5-w7-cd-corporate-slice-blueprint-evidence-v1.md](../../../projects/mars-website-factory/wf-r01-3-5-w7-cd-corporate-slice-blueprint-evidence-v1.md) |

---

## 9. G4 Deferred Work

- Dedicated `CERTIFICATES` · `PARTNERS` partials (W7-A) — binding RPC gaps #5–#6
- Dedicated `FEATURES` · `REVIEWS` · `MAP` hygiene partials (W7-B)
- Optional `REVIEWS_PAGE` scaffold (+1 RSC if validated)
- CORPORATE `HOME_PAGE` hub scaffold
- Full Core 5 blueprint-instance set (G4-E)

---

*Reference Blueprint-instance v1 — evidence-only companion doc. Not Template-Art. Not production blueprint.*
