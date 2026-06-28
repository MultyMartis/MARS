# FP-0002 V8 Operational Status

**Updated:** 2026-06-28 (bootstrap reconciliation + git protection + browser parity)

```text
fp0002_v8: BOOTSTRAP_RECONCILIATION_COMPLETE
fp0002_v8_git_protection: ENABLED
fp0002_v8_baseline: FOUR_TEMPLATE_AUTHORITY_6eb493e9
fp0002_v8_component_audit: COMPLETE
fp0002_v8_component_consolidation: NOT_STARTED
fp0002_v8_cf003_upper_navigation: READY_PENDING_OPERATOR_APPROVAL
fp0002_v8_o_centre: DEFERRED
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
build_before_consolidation: PASS
browser_parity: PASS (V7 authority reference dist vs V8 dist)
four_template_source_parity: PASS (git blob match vs authority tag)
component_family_audit: COMPLETE
consolidation_implementation: NOT_STARTED

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
