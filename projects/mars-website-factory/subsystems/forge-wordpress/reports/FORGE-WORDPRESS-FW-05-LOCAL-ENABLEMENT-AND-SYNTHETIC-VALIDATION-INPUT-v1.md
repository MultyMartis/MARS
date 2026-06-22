# Forge WordPress FW-05 — Local Enablement and Synthetic Validation Input v1

**Document type:** Stage input for FW-05  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-04 prepares input — **FW-05 not executed**

---

## Purpose

Define what FW-05 must install, configure, and execute to prove the FW-04 capability pack on a synthetic case.

---

## Missing local tools (from FW-03 audit)

| Tool | Status | FW-05 action |
|------|--------|--------------|
| Local WordPress runtime (DDEV / Local / Docker) | NOT READY | Install per [FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md](../FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md) |
| PHP + Composer | PARTIAL | Verify versions match decision doc |
| WP-CLI | NOT READY | Install local only |
| PHPCS + WPCS | NOT READY | Install project-local |
| Node/npm (asset build) | Likely available | Verify per project |
| Playwright (visual) | NOT READY | Install for FW-SK-12 |
| ACF PRO | SAFE UNKNOWN | Operator license — not in repo |

---

## Install sequence (recommended)

```text
1. Choose local stack per LOCAL-ENVIRONMENT-DECISION
2. Create isolated synthetic workspace (not FP-0002)
3. Install WordPress core locally — outside git or gitignored
4. Install WP-CLI
5. Install PHPCS + WordPress Coding Standards
6. Install ACF (operator-provided license)
7. Configure Playwright for visual capture
8. Register paths in synthetic project intake
9. Update tool registry with ACTUAL versions
10. Re-run LOCAL-TOOLING-CAPABILITY-AUDIT with evidence
```

---

## Environment setup

| Item | Requirement |
|------|-------------|
| Workspace path | Operator-declared — e.g. `workspaces/forge-wordpress-synthetic-v1/` |
| WordPress URL | Local only — e.g. `https://forge-synthetic.ddev.site` |
| Database | Local — gitignored |
| Scope contract | Per FW-04 filesystem scope |

---

## Synthetic workspace creation

1. Create project folder structure per repository model
2. Add synthetic frontend (static HTML/CSS) — artificial content only
3. Create synthetic handoff manifest
4. No client branding, no FP-0002 assets

---

## Synthetic frontend creation

Per [capability/reports/FORGE-WORDPRESS-SYNTHETIC-TEST-CASE-SPEC-v1.md](../capability/reports/FORGE-WORDPRESS-SYNTHETIC-TEST-CASE-SPEC-v1.md):

- Home, service archive, single service, FAQ, contact, header, footer, options
- Desktop + mobile CSS
- Operator approval of synthetic frontend before WP work

---

## Synthetic WordPress implementation

Execute full skill chain FW-SK-01 through FW-SK-14 using capability prompt pack.

---

## Skill execution order

```text
FW-SK-01 → FW-SK-02 [gate] → FW-SK-03 [gate] → FW-SK-04 → FW-SK-05
→ FW-SK-06 → FW-SK-07 → FW-SK-08 → FW-SK-09 [gate] → FW-SK-10
→ FW-SK-11 → FW-SK-12 [operator gate] → FW-SK-13 → FW-SK-14
```

---

## Validator passes

| Validator | When |
|-----------|------|
| FW-V-01 | After architecture artifacts |
| FW-V-02 | After FW-SK-10 |
| FW-V-03 | After FW-SK-10 |
| FW-V-04 | After local WP up |
| FW-V-05 | After FW-SK-12 |
| FW-V-06 | After admin configured |
| FW-V-07 | Before handoff simulation |

Use independent Cursor passes per independence policy.

---

## Visual regression

1. Capture synthetic frontend baselines
2. Capture local WP renders
3. Compare desktop + mobile
4. Operator visual approval — mandatory

---

## Packaging

- FW-SK-13 release package
- Verify exclusions per git workflow
- No production deploy

---

## Handoff simulation

- FW-SK-14 produces FW-C-03 artifact
- WPilot reviewer simulation by operator
- No live WPilot deployment

---

## Pass/fail criteria

| Result | Condition |
|--------|-----------|
| **PASS** | Full pipeline + all validators + operator WV6 approval |
| **PARTIAL** | Pipeline complete with documented non-blocking debt |
| **FAIL** | Blocking validator or missing local env without recovery plan |

---

## Stop conditions

- Attempting FP-0002 as synthetic substitute
- Production credentials or URLs
- Skipping human gates
- Registering agent without charter
- Claiming OPERATIONAL without PASS

---

## FW-05 deliverables (expected)

1. Local environment evidence (audit update)
2. Synthetic workspace with implementation
3. Full report bundle per skill
4. Updated capability readiness matrix
5. FW-06 input (pilot intake) if synthetic PASS

---

## Related

- [../capability/FORGE-WORDPRESS-CAPABILITY-READINESS-MATRIX-v1.md](../capability/FORGE-WORDPRESS-CAPABILITY-READINESS-MATRIX-v1.md)
- [../capability/OPERATIONAL-INDEX.md](../capability/OPERATIONAL-INDEX.md)
- [FORGE-WORDPRESS-LOCAL-TOOLING-CAPABILITY-AUDIT-v1.md](FORGE-WORDPRESS-LOCAL-TOOLING-CAPABILITY-AUDIT-v1.md)

---

*FW-05 input v1 — prepared by FW-04; not executed.*
