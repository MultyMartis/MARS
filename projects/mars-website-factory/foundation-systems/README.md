# Website Factory — foundation systems (Wave 2)

**Status:** **documented** — implementation standards for Gulp/static landings. **Not** repo code, **not** runtime enforcement.

**Wave 1 anchors (do not duplicate):** [frontend-foundation-blueprint-v1.md](../frontend-foundation-blueprint-v1.md), [section-replacement-contract-v1.md](../section-replacement-contract-v1.md).

**Governance intent (Tier 3 only):** token/responsive/interaction *governance* docs stay in Extended — these files are **production implementation law**.

---

## Systems map

| # | System | Doc | Target workspace artifact |
|---|--------|-----|---------------------------|
| 1 | Tokens | [token-system-v2.md](token-system-v2.md) | `scss/_tokens.scss`, `scss/_layers.scss` |
| 2 | Responsive | [responsive-system-v2.md](responsive-system-v2.md) | `scss/_breakpoints.scss`, section collapse utilities |
| 3 | Forms | [form-system-v2.md](form-system-v2.md) | `scss/foundations/_forms.scss`, `js/core/form.js` |
| 4 | Modals / overlays | [modal-overlay-system-v2.md](modal-overlay-system-v2.md) | `scss/foundations/_modals.scss`, `js/core/modal.js` |
| 5 | JS lifecycle | [js-lifecycle-system-v2.md](js-lifecycle-system-v2.md) | `js/core/lifecycle.js`, `data-module` contract |
| 6 | Interaction / motion | [interaction-motion-system-v2.md](interaction-motion-system-v2.md) | motion tokens + allowed/forbidden patterns |
| 7 | Conversion blocks | [conversion-blocks-v2.md](conversion-blocks-v2.md) | partial + SCSS + hook normalization per `block_id` |

**Wave 3–4 reference implementation:** [workspaces/website-factory-reference-v1/](../../workspaces/website-factory-reference-v1/) (7 blocks) · golden slice [golden-implementation-slice-v1.md](../golden-implementation-slice-v1.md). **Wave 4 adoption:** [foundation-adoption-charter-v1.md](../foundation-adoption-charter-v1.md) · [onboarding-flow-v1.md](../onboarding-flow-v1.md).

---

## Operator entry

1. Open the system doc for the task.
2. Cross-check blast radius — [section-replacement-contract-v1.md](../section-replacement-contract-v1.md).
3. Implement in **src/** only — [frontend-production-rules-v0.md](../frontend-production-rules-v0.md).
4. REPORT with paths touched and freeze state.

*Wave 2 — 2026-05-20.*
