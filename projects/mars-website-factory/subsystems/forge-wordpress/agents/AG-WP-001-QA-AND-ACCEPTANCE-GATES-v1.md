# AG-WP-001 — QA and Acceptance Gates v1

**Document type:** QA gate specification  
**Version:** v1  
**Stage:** FW-07A  
**Date:** 2026-06-24

**Aligns with:** FW-S-08, capability validators FW-V-01–07

---

## Gate A — Input completeness

**No implementation** without approved handoff per [AG-WP-001-APPROVED-FRONTEND-INPUT-CONTRACT-v1.md](AG-WP-001-APPROVED-FRONTEND-INPUT-CONTRACT-v1.md).

| Check | Blocker |
|-------|---------|
| Production Pass present | Yes |
| Approved commit frozen | Yes |
| FW-06B authorized (integration phase) | Yes |

---

## Gate B — Architecture approval

Theme mode, functionality split, content model, plugin register — **operator approved**.

| Artifact | Required |
|----------|----------|
| Mode decision | Yes |
| Theme/functionality plans | Yes |
| Content model | Yes |
| Plugin register | Yes |

---

## Gate C — Source quality

| Check | Standard |
|-------|----------|
| PHP syntax | Pass |
| WPCS/PHPCS | Pass or documented waiver |
| Project naming | Forge conventions |
| Escaping/sanitization | FW-S-07 |
| Nonce/capability checks | Where applicable |
| No credentials in source | Blocker |
| No production URLs in local config | Blocker |

---

## Gate D — WordPress integrity

| Check | Notes |
|-------|-------|
| Core checksums | Local WP integrity |
| DB check | `wp db check` or equivalent |
| Plugin/theme state | Matches register |
| Routes | Expected URLs resolve |
| REST | If used — smoke test |
| Cron | If used — documented |
| Mail | Suppressed in local per policy |

---

## Gate E — Functional validation

Forms, menus, modals, CPT, taxonomies, fields, admin workflows, error states — per project validation plan.

---

## Gate F — Visual fidelity

| Check | Notes |
|-------|-------|
| Approved viewport matrix | From Production Pass |
| Screenshots / visual diff | Playwright + pixelmatch |
| Typography, spacing | No unapproved redesign |
| Responsive behaviour | All required breakpoints |

---

## Gate G — Accessibility

Minimum: keyboard navigation, focus visibility, labels, semantic structure, contrast, `prefers-reduced-motion` where applicable.

---

## Gate H — Security and dependencies

Plugin provenance, versions, vulnerability check (where tooling exists), no abandoned deps without approval, least privilege, no arbitrary upload/execution surface.

---

## Gate I — Operator approval

Agent **cannot** self-approve final implementation. Human sign-off required.

---

## Gate J — Handoff eligibility

Only after gates A–I required for scope pass. Produces DEPLOYMENT ELIGIBLE statement — **not** automatic deploy.

---

## Gate sequencing

```text
A → B → (implementation) → C → D → E → F → G → H → I → J
```

Failure at any gate: stop, report, rollback per failure contract.

---

*QA gates v1 — independent of agent self-certification.*
