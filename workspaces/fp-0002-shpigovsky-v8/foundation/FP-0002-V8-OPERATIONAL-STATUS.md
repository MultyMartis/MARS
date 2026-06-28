# FP-0002 V8 Operational Status

**Updated:** 2026-06-29 (operator manual polish canonical checkpoint)

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
fp0002_v8_o_centre: CHARTER_COMPLETE_IMPLEMENTATION_NOT_STARTED
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
- Status: **CHARTER COMPLETE WITH KNOWN GAPS** — implementation **NOT AUTHORIZED**
- Blockers: BLK-037/038 copy and assets; About hero asset confirmation; FAQ inventory vs Figma conflict
- Next recommended task: **FP-0002 V8 O-Centre implementation prompt** (after optional asset prep)

## Next wave (documentation only)

- O-Centre page HTML/CSS — **NOT STARTED** (await operator implementation authorization)
