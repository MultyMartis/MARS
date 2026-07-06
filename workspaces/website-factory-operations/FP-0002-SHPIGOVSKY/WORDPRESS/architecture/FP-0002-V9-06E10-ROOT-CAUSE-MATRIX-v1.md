# FP-0002 V9-06E10 Root Cause Matrix v1

**Evidence JSON:** `validation/v9-06e10-full-backup-wp-port-root-cause-audit/root-cause-matrix.json`

## Primary root cause (confirmed)

**WordPress port uses semantic PHP reconstruction instead of direct static V9 HTML section-stack porting**, combined with **probe-only validation that false-PASSed structural parity while inner markup diverged**.

## Root cause matrix (abbreviated)

| Root cause | Severity | Affected routes | Recommended fix |
|------------|----------|-----------------|-----------------|
| No direct V9 HTML port | CRITICAL | All V9 routes | E11 inventory + E12 strict replacement |
| D7-D semantic architecture | HIGH | Services, service CPT | Governance ban + refactor stacks |
| Home partial reuse on leaf | HIGH | Alcohol, subdivision | Fork/parameterize service partials |
| Probe-only validation | HIGH | Alcohol leaf (E9) | Screenshot gate mandatory |
| Truncated leaf-stack | HIGH | Non-alcohol leaves | Align to static 17-section stack |
| ACF seed overrides | MEDIUM | Service CPT | EXACT_V9 classification |
| Demo fixture lorem | LOW | Program/signs | DEMO inventory + operator decision |

## Answers to operator questions (§1)

1. **Did agents read V9?** Partially — referenced src pages; did not enforce HTML-faithful port.
2. **Old rules overriding V9?** Yes — V6 foundation, D7-D semantic model, D8 ACF seeds, home partial reuse.
3. **Semantic reconstruction?** **Yes** — core architecture, not exception.
4. **Wrong template mapping?** Variant loader correct for alcohol; **inner partials wrong provenance**.
5. **V8/V9/demo mixing?** **Yes** — home partials + skeleton institutional/blog + demo lorem.
6. **Repairs patch symptoms?** **Yes** — E9 fixed wrapper/subnav; not full static HTML replacement.
7. **Why alcohol page still wrong visually?** Section classes match; **inner markup/home partial context** differs; ACF may mutate copy; operator compares pixels not DOM probes.
8. **Governance rule needed?** **FP-0002-V9-06E10-STATIC-V9-WP-PORT-GOVERNANCE-CONTRACT-v1.md** (10 rules).
