# SITE-002 — Production Baseline Pending

**Site ID:** SITE-002  
**Environment ID:** `site-002-prod`  
**Production URL:** https://bzpm.ru/  
**Status:** **PENDING — NOT ISSUED**

---

## Current state

| Field | Value |
|-------|-------|
| Production URL | **REGISTERED** |
| Production parity | **NOT YET VERIFIED** |
| Remote capture | **PARTIAL** (2026-07-02 — HTTP/visual/admin; FTP blocked) |
| File manifest | **NOT COLLECTED** |
| Production checkpoint | **NOT ISSUED** |

This document is a **readiness placeholder only**. It is not a stable checkpoint and must not be used as rollback authority.

---

## Future baseline requirements

Before issuing the first Production stable checkpoint, a dedicated authorized task must deliver:

1. Read-only remote inventory
2. Production homepage and key-page captures
3. Platform / version identification
4. Remote document root confirmation
5. File manifest for allowed theme scope
6. Current full backup reference
7. HTTP smoke verification
8. Operator confirmation
9. Baseline report
10. Checkpoint registration in OCPilot authority chain

**Future real checkpoint name (reserved, not issued):**

```text
SITE-002-STABLE-PROD-INITIAL-01
```

Do not issue that checkpoint until the requirements above are satisfied with evidence.

---

## Authority bindings

| Document | Path |
|----------|------|
| Production profile | [../production-profile.md](../production-profile.md) |
| Production storage root | `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\` |
| Captures folder | `production\captures\` |
| Baselines folder | `production\baselines\` |
| Registration report | [../reports/SITE-002-PRODUCTION-PROFILE-REGISTRATION.md](../reports/SITE-002-PRODUCTION-PROFILE-REGISTRATION.md) |

---

## TEST relationship

TEST checkpoints under [./](.) remain valid as **implementation evidence**. They are **not** automatic proof of current Production parity.

**Historical TEST URL:** https://zpm.new-site.space/
