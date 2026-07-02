# FP-0002 V9-03F Triumph Modal Authority Map v1

**Classification:** `CURRENT_OPERATOR_APPROVED_TRIUMPH_AUTHORITY`

## Selected authority

| Role | Path |
|------|------|
| Workspace | `X:\AI MARS\workspaces\triumph-manipulator-landing-v6` |
| Modal JS | `src/js/modal.js` |
| Modal markup | `src/partials/components/callback-modal.html` |
| Modal SCSS | `src/scss/components/_modal.scss` |
| Shell template | `src/partials/components/modal-shell.html` |

## Approval evidence

- Operator task V9-03F explicitly names Triumph Manipulator as proven modal technology authority.
- Triumph v6 is the expected candidate workspace; source inspected read-only with stable hashes.

## Rejected / other candidates

| Candidate | Classification | Reason |
|-----------|----------------|--------|
| `triumph-manipulator-landing-v2` | `SUPERSEDED` | Older workspace copy; v6 is current task candidate |
| FP-0002 V9-03D body-fixed runtime | `REJECTED` | Operator rejected — visible scroll movement |
| FP-0002 V9-03E page-shell fixed runtime | `REJECTED` | Operator rejected — close restoration movement |

## Reusable Triumph contract (behavior only)

- Triggers: `[data-modal-open]` with `preventDefault`
- Open: remove `hidden`, `aria-hidden=false`, open class/state, **overflow lock on body**
- Close: remove open state, transition end → `hidden`, unlock body, restore trigger focus
- Escape + overlay click + focus trap
- No scroll-position save/restore in Triumph base (FP-0002 adds minimal adaptation — see migration plan)
