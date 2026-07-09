# FP-0002 V9-06E26C Validation Post Gate v1

**Decision:** Option A — no DB content seed

## Rationale

- Published posts count: 0
- No authenticated preview workflow in automated runner
- Source/runtime template markers + HTTP regression sufficient for E26C acceptance
- `/blog/nazvanie-stati/` correctly returns 404 until E26D seeds fixture content

## Constraints honored

- No published article created
- No validation draft post created
- E26D will perform public visual QA with real fixture content

Evidence: `validation/v9-06e26c-blog-single-template-wordpress-acf-port/validation-post-gate-result.json`
