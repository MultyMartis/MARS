# FP-0002 — ACF Foundation Decision v1

**Version:** v1 | **Date:** 2026-06-23 | **Stage:** FW-06A.1

## Installed

| Package | Version | Source | Status |
|---------|---------|--------|--------|
| Advanced Custom Fields (Free) | 6.8.4 | wordpress.org | **ACTIVE** |

## ACF Pro

```text
NOT INSTALLED — decision deferred to FW-06B content model review
```

No ACF Pro ZIP or license key in Git. Not claimed as available.

## Foundation decision (FW-06A / FW-06A.1)

```text
FW-06A foundation:
ACF Free is sufficient.

FW-06B:
ACF Pro decision is deferred until the approved content model
shows a justified need for Pro-only fields.
```

## JSON workflow

| Path | Role |
|------|------|
| Brain source | `workspaces/fp-0002-shpigovsky-v6/WORDPRESS/acf-json/` |
| Runtime sync | `wp-content/acf-json/` (prepared, empty) |

Plugin `shpigovsky-core` registers ACF JSON load/save paths.

## Not created (FW-06A / FW-06A.1)

- Flexible Content groups
- Repeater-based page builder
- Section constructor
- Final page groups
- Final block schema

### Candidate global groups (FW-06B only, if authority confirms)

- Site contacts
- Company settings
- Social links
- Legal references
- Basic CTA defaults

---

*FP-0002 ACF foundation — FW-06A.1 complete.*

## V9-06B.2 update

ACF PRO is now installed, active, and admitted as an operator-managed external dependency. The earlier FW-06A.1 ACF Free path remains historical foundation context only; ACF Free is currently inactive and not used while PRO is active.

ACF Extended PRO is active but not architecturally approved for FP-0002 use by default.

