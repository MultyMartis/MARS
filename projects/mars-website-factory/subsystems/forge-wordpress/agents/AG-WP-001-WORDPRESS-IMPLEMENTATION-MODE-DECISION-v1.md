# AG-WP-001 — WordPress Implementation Mode Decision v1

**Document type:** Decision framework  
**Version:** v1  
**Stage:** FW-07A  
**Date:** 2026-06-24

**Rule:** The agent **must not** choose block theme automatically.

---

## 1. Supported modes

| Mode | Code |
|------|------|
| Classic theme | `CLASSIC_THEME` |
| Hybrid theme | `HYBRID_THEME` |
| Block theme (FSE) | `BLOCK_THEME` |

---

## 2. Mode profiles

### CLASSIC_THEME

| Aspect | Detail |
|--------|--------|
| Suitable projects | High-fidelity marketing sites; complex custom layouts; gulp/static parity priority |
| Benefits | Maximum fidelity to approved HTML/CSS; familiar PHP template workflow |
| Risks | Editor may be less intuitive for clients; block editor friction |
| Editor implications | Curated fields + limited block usage; classic editor patterns |
| Fidelity implications | **Best** for pixel-parity from static frontend |
| Skills/tools | PHP templates, SCSS build sync, ACF optional |
| QA | Visual regression primary; template map validation |
| Disqualifying | Client requires full block editing of layout shell |

### HYBRID_THEME

| Aspect | Detail |
|--------|--------|
| Suitable projects | Marketing sites with **some** reusable editor blocks; mixed template + block areas |
| Benefits | Balance of fidelity and editor flexibility |
| Risks | Boundary drift between theme and blocks; higher architecture discipline |
| Editor implications | Locked templates + approved custom blocks |
| Fidelity implications | **Good** with explicit locked regions |
| Skills/tools | `theme.json` partial, custom blocks, ACF |
| QA | Block + template validation; visual parity on locked regions |
| Disqualifying | Unapproved flexible page builder expectation |

### BLOCK_THEME

| Aspect | Detail |
|--------|--------|
| Suitable projects | Editor-first sites; lower custom layout complexity |
| Benefits | Native FSE; pattern reuse |
| Risks | Harder to match approved static frontend exactly; performance/theme.json complexity |
| Editor implications | Full site editing — **high governance** required |
| Fidelity implications | **Weakest** for strict static parity unless heavily constrained |
| Skills/tools | `theme.json`, block patterns, styles |
| QA | Block markup + visual diff; editor breakage tests |
| Disqualifying | Approved frontend requires bespoke PHP template complexity |

---

## 3. Decision factors (required review)

1. Fidelity to approved frontend
2. Client editor needs
3. Reusable block requirements
4. Template complexity
5. Performance budget
6. Long-term maintenance ownership
7. WordPress core compatibility target
8. ACF dependency (mode, not default)
9. Hosting/runtime constraints (MLI profile)
10. Project budget and scope

---

## 4. Required decision output

Every project must produce:

```text
selected_mode:
rejected_alternatives: (with reason)
evidence: (frontend handoff refs)
risks:
operator_approval_status: PENDING | APPROVED | REJECTED
```

Template: [FORGE-WORDPRESS-ARCHITECTURE-DECISION-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-ARCHITECTURE-DECISION-TEMPLATE-v1.md)

---

## 5. FP-0002 preliminary note

FP-0002 has **not** completed mode decision at pilot start. Expected bias from handoff shape: **CLASSIC_THEME** or **HYBRID_THEME** — **not** decided until FW-06B architecture approval.

---

*Mode decision v1 — block theme is never the default.*
