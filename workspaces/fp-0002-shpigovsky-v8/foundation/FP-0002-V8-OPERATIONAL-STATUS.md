# FP-0002 V8 Operational Status

**Updated:** 2026-07-01 (Phase 07C-A reconciliation complete; operator gate pending)

## Operator-approved frontend baseline

| Field | Value |
|-------|-------|
| Record | [FP-0002-V8-OPERATOR-APPROVED-FRONTEND-BASELINE-01.md](../../website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-V8-OPERATOR-APPROVED-FRONTEND-BASELINE-01.md) |
| Documentation pack | [FP-0002-V8-IMPLEMENTATION-GUIDE-v1.md](../../website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-V8-IMPLEMENTATION-GUIDE-v1.md) |
| Phase 07B report | [REPORT-FP-0002-V8-PHASE-07B-DOCUMENTATION-AND-LESSONS-LEARNED-v1.md](../../website-factory-operations/FP-0002-SHPIGOVSKY/REPORT-FP-0002-V8-PHASE-07B-DOCUMENTATION-AND-LESSONS-LEARNED-v1.md) |
| Phase 07C-A report | [REPORT-FP-0002-V8-PHASE-07C-A-EXCEL-DEMO-RECONCILIATION-v1.md](../../website-factory-operations/FP-0002-SHPIGOVSKY/REPORT-FP-0002-V8-PHASE-07C-A-EXCEL-DEMO-RECONCILIATION-v1.md) |
| WordPress facts | [FP-0002-V8-WORDPRESS-READY-BASELINE-v1.md](../../website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-V8-WORDPRESS-READY-BASELINE-v1.md) |
| Tag | `fp-0002-v8-operator-approved-frontend-stable-01` |
| Pages | 10 (Home, O-Centre, Contacts, Reviews, Blog archive, Blog Article, 4× services) |
| Blog Article | OPERATOR_APPROVED desktop + mobile (Pass 06) |

```text
fp0002_v8_operator_approved_frontend_baseline: STABLE_01
fp0002_v8_blog_article: OPERATOR_APPROVED
fp0002_v8_next_phase: 07C_B_STATIC_CLIENT_DEMO_ASSEMBLY
fp0002_v8_phase_07c_a: RECONCILIATION_COMPLETE_PENDING_OPERATOR_SCOPE_DECISIONS
fp0002_v8_phase_07b: DOCUMENTATION_COMPLETE
```

## ACTIVE TEMPORARY PRIORITY RULE

Before any FP-0002 frontend implementation, read:

[`FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md`](../../website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md)

- **Visual PASS:** OPERATOR ONLY
- **Commit before operator visual approval:** PROHIBITED
- **Mandatory report header:** REQUIRED
- **Web-GPT recovery source:** THIS PROTOCOL

```text
fp0002_v8: BOOTSTRAP_RECONCILIATION_COMPLETE
fp0002_v8_git_protection: ENABLED
fp0002_v8_baseline: FOUR_TEMPLATE_AUTHORITY_6eb493e9
fp0002_v8_component_audit: COMPLETE
fp0002_v8_component_consolidation: CF003_CF012_COMPLETE
fp0002_v8_operator_manual_polish: OPERATOR_MANUAL_POLISH_CANONICAL
fp0002_v8_visual_authority: V8_WORKING_SOURCE_POST_MANUAL_POLISH
fp0002_v8_cf003_upper_navigation: COMPLETE
fp0002_v8_cf003_commit: 361502bf
fp0002_v8_cf004_founder_quote: COMPLETE
fp0002_v8_cf005_specialists: COMPLETE
fp0002_v8_cf006_comfort: COMPLETE
fp0002_v8_cf007_reviews: COMPLETE
fp0002_v8_cf008_faq: COMPLETE
fp0002_v8_cf009_final_form: COMPLETE
fp0002_v8_cf009_commit: ec5ff2c0
fp0002_v8_duplicate_id_repair: COMPLETE
fp0002_v8_duplicate_id_repair_commit: 2107d2b9
fp0002_v8_consolidation_checkpoint: DOCUMENTED
fp0002_v8_page_wide_dom_gate: PASS
fp0002_v8_cf011_dark_cta: COMPLETE
fp0002_v8_cf012_program_modifiers: COMPLETE_OPERATOR_APPROVED
fp0002_v8_cf012_commit: 9e8fa083
fp0002_v8_manual_polish_checkpoint: DOCUMENTED
fp0002_v8_cf010_clinic_landscape: COMPLETE
fp0002_v8_next_wave: O_CENTRE_IMPLEMENTATION_NOT_AUTHORIZED
fp0002_v8_o_centre_charter: COMPLETE_WITH_KNOWN_GAPS
fp0002_v8_o_centre: STABLE_IN_OPERATOR_BASELINE
fp0002_v8_o_centre_historical_audit: SUPERSEDED_SEE_BASELINE
fp0002_v8_priority_visual_protocol: ACTIVE
fp0002_v8_deployment: NOT_STARTED

workspace: V8
lifecycle: ACTIVE_CONSOLIDATION
parent_v7: IMMUTABLE_STABLE_FALLBACK
bootstrap_authority_tag: fp-0002-v7-four-template-canonical-demo-baseline-01
bootstrap_authority_commit: 6eb493e9eadb2578c2223278d41bdfe6970e5637
v7_static_demo_reference_tag: fp-0002-v7-static-client-demo-stable-02
v7_static_demo_reference_commit: e33e59af0d0b233a9fd3d455d445f217fd5b6288

bootstrap_reconciliation: COMPLETE
git_whitelist: ENABLED
build_cf003: PASS
browser_qa_cf003: PASS
dom_validation_cf003: PASS
selector_validation_cf003: PASS
cf003_commit: PUSHED (361502bf)
build_cf004: PASS
browser_qa_cf004: PASS
dom_validation_cf004: PASS
selector_validation_cf004: PASS
visual_parity_cf004: PASS
shared_component_audit: COMPLETE
consolidation_wave_1_cf003: COMPLETE
consolidation_wave_2_cf004: COMPLETE
consolidation_wave_3_cf005: COMPLETE
consolidation_wave_4_cf006: COMPLETE
consolidation_wave_5_cf007: COMPLETE
consolidation_wave_6_cf008: COMPLETE
consolidation_wave_7_cf009: COMPLETE
duplicate_id_repair_treatment_prevention: COMPLETE
consolidation_checkpoint_cf003_cf009: DOCUMENTED
page_wide_dom_gate: PASS
consolidation_wave_9_cf012: COMPLETE_OPERATOR_APPROVED
operator_manual_polish_canonical: DOCUMENTED
build_cf012: PASS
browser_qa_cf012: PASS
dom_validation_cf012: PASS
selector_validation_cf012: PASS
visual_parity_cf012: PASS
functional_qa_cf012: PASS
cf011_protection_cf012: PASS
build_cf007: PASS
browser_qa_cf007: PASS
dom_validation_cf007: PASS
selector_validation_cf007: PASS
visual_parity_cf007: PASS
slider_qa_cf007: PASS
build_cf008: PASS
browser_qa_cf008: PASS
dom_validation_cf008: PASS
selector_validation_cf008: PASS
visual_parity_cf008: PASS
accordion_qa_cf008: PASS

excluded_from_bootstrap:
  - o-centre-v1.html (rejected WIP)
  - node_modules/
  - dist/
  - static-demo generator tooling (not present at four-template baseline tag)

design_authority: Spig_v1.2.fig
design_authority_status: ACTIVE
```

## Authority split

| Layer | Authority | Use |
| ----- | --------- | --- |
| Four canonical templates (HTML/CSS/JS source) | `fp-0002-v7-four-template-canonical-demo-baseline-01` | V8 bootstrap source |
| Deployed static client demo | `fp-0002-v7-static-client-demo-stable-02` | Unchanged; V7-only reference |
| V7 workspace disk (post-baseline WIP) | **Not authority** | Includes rejected o-centre attempts |

## V7 immutability

V7 source, SCSS, canonical template HTML, runtime JS, registry, and generator must not be modified for consolidation. V7 remains evidence and fallback.

## CF-003

- Canonical partial: `partials/components/internal-page-nav.html`
- Canonical class: `.internal-page-nav`
- Receipt: `audits/cf-003-upper-navigation/CF-003-COMPLETION-RECEIPT.md`

## CF-004

- Canonical partial: `partials/sections/founder-quote.html`
- Canonical class: `.founder-quote`
- Retired name: `home-founder-quote`
- Consumers: `index.html`, `uslugi-v2.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html`, `uslugi.html`
- Receipt: `audits/cf-004-founder-quote/CF-004-IMPLEMENTATION-RECEIPT.md`

## CF-005

- Canonical partial: `partials/sections/specialists.html`
- Canonical class: `.specialists`
- Retired name: `home-specialists`
- Slider hooks: `data-specialists-slider`, `data-specialists-pagination`
- Consumers: `index.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html`
- Receipt: `audits/cf-005-specialists/CF-005-IMPLEMENTATION-RECEIPT.md`

## CF-006

- Canonical partial: `partials/sections/comfort.html`
- Canonical class: `.comfort`
- Retired name: `home-comfort`
- Gallery hook: `data-fancybox="comfort"`
- Consumers: `index.html`, `uslugi.html`, `uslugi-v2.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html`
- Historical asset path: `assets/img/content/home-comfort/` — preserved
- Receipt: `audits/cf-006-comfort/CF-006-IMPLEMENTATION-RECEIPT.md`

## CF-007

- Canonical partial: `partials/sections/reviews.html`
- Canonical class: `.reviews`
- Retired name: `home-reviews`
- Slider hooks: `data-reviews-slider`, `data-reviews-pagination`
- Init: `initReviews`
- Consumers: `index.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html`
- Receipt: `audits/cf-007-reviews/CF-007-IMPLEMENTATION-RECEIPT.md`

## CF-008

- Canonical partial: `partials/sections/faq.html`
- Canonical class: `.faq`
- Retired name: `home-faq`
- Accordion hooks: `data-accordion`, `data-accordion-button`, `data-accordion-panel` (global init unchanged)
- Consumers: `index.html`, `uslugi.html`, `uslugi-v2.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html`
- Receipt: `audits/cf-008-faq/CF-008-IMPLEMENTATION-RECEIPT.md`

## CF-009

- Canonical partial: `partials/sections/final-form.html`
- Canonical class: `.final-form`
- Retired name: `home-final-form`
- Form hooks: `data-lead-form`, `data-phone-input` (unchanged)
- Consumers: all five template pages with final form
- Commit: `ec5ff2c0`
- Receipt: `audits/cf-009-final-form/CF-009-IMPLEMENTATION-RECEIPT.md`

## Duplicate-ID repair

- Defect: `home-treatment-prevention-panel-1` duplicate on Home
- Fix commit: `2107d2b9`
- Receipt: `audits/dom-defect-repair/FP-0002-V8-DUPLICATE-ID-REPAIR-RECEIPT.md`

## Consolidation checkpoint

- Receipt: `audits/consolidation-checkpoint/FP-0002-V8-CF003-CF009-CONSOLIDATION-CHECKPOINT-v1.md`

## Operator manual polish checkpoint

- Receipt: `audits/operator-manual-polish/FP-0002-V8-OPERATOR-MANUAL-POLISH-CANONICAL-CHECKPOINT-v1.md`
- Status: OPERATOR_MANUAL_POLISH_CANONICAL

## O-Centre charter (2026-06-29)

- Charter: `audits/o-centre-page-charter/FP-0002-V8-OCENTRE-PAGE-ANATOMY-REUSE-CHARTER-v1.md`
- Content blocker resolution: `audits/o-centre-content-blocker-resolution/` (2026-06-29)
- Technical baseline: `06096d51d41c0fee3639d94bb3b30855e08f79ad`
- Visual status: **STRUCTURAL_REGRESSION_REQUIRES_FIX**
- Operator approval: **REJECTED**
- Visual correction pack: `audits/o-centre-visual-correction/` (historical — superseded by protocol O-Centre status)
- Implementation: `src/pages/o-centre.html` → `dist/o-centre.html`
- Evidence: `audits/o-centre-implementation/`
- Ops status: [FP-0002-OCENTRE-VISUAL-AUDIT-STATUS-v1.md](../../website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-OCENTRE-VISUAL-AUDIT-STATUS-v1.md)

## Next wave (documentation only)

- O-Centre — **desktop micro-pass** · one narrow problem · no commit · preview + runtime crop · operator review required
- Governed by: [FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md](../../website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md)


## O-Centre infrastructure assets (2026-06-29)

- Status: **APPROVED_EXPORTED** — 20 WebP under `src/img/content/o-centre/o-centre-infrastructure-*.webp`
- Evidence: `audits/o-centre-targeted-asset-export/`
- Implementation authorized: **false** (operator must authorize implementation task)

## O-Centre decorative asset DEC-01 (2026-06-29)

- Status: **APPROVED_EXPORTED** — `src/img/content/o-centre/decorative/o-centre-infrastructure-background.webp`
- Asset ID: OC-DEC-01 · ref `d3ac7d00af36` · 953×988 WebP · SHA-256 `e64e5d29440036dca7e944f1ce46e75ada9255857a7074c9694362f1864ce769`
- Evidence: `audits/o-centre-decorative-asset-extraction/`
- Rendering/use: **NOT APPROVED** — lifebuoy decoration **prohibited**
- Next visual task: remove/disable from rendering
- Figma resource existence does not override PNG/operator authority
- Operator visual approval: **REJECTED**
