# FP-0002 — WPilot Local Installation v1

**Version:** v1 | **Date:** 2026-06-23 | **Stage:** FW-06A.1

## Result

```text
WPilot installation:
HOLD

Reason:
Canonical approved package/version checkpoint required.

FP-0002 foundation:
NOT BLOCKED
```

## Evidence (read-only authority review)

| Check | Result |
|-------|--------|
| Brain plugin source | `projects/wpilot/plugin/metacode-wpilot/` — v0.3.0 (Sprint 2) |
| Source lifecycle | DEV/test bridge — Phase 0–1 + Sprint 1–2 |
| Latest approved checkpoint | **NOT ISSUED** for FP-0002 local install |
| Canonical distributable ZIP | **NOT IN** `D:\MARS-Localhost\storage\packages\` |
| Build/package procedure | Manual copy/zip per README — no brain checksum charter |
| Checksum for FP-0002 local | **NOT ISSUED** |
| FWS-0001 reference install | **NOT INSTALLED** on synthetic runtime |
| Active unrelated WPilot WIP | None verified as approved package |
| Production DEV token | Exists outside runtime — **NOT USED** |

## Rationale

FW-06A / FW-06A.1 does not authorize ad-hoc WPilot install from unverified path. Operator must declare canonical local package, version pin, reproducible build, and checksum before install on `shpigovsky.test`.

Absence of WPilot does **not** block approved frontend intake (FW-06B).

## Target placeholder (future controlled install)

When authorized separately:

- Runtime: `shpigovsky.test` only
- Mode: local/dev inspection
- No production credentials
- No remote operations
- Package source: approved checkpoint only — not unverified WIP

---

*FP-0002 WPilot local installation — FW-06A.1 HOLD decision.*
