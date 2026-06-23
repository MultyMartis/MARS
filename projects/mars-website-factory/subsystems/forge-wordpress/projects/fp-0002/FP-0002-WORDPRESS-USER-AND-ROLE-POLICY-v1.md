# FP-0002 — WordPress User and Role Policy v1

**Version:** v1 | **Date:** 2026-06-23

## Local runtime (FW-06A)

| Rule | Value |
|------|-------|
| Administrators | **One** — synthetic local identity (`mli_admin_fp0002`) |
| Client users | **None** |
| Real emails | **None** — `@localhost.test` only |
| Production password reuse | **Forbidden** |
| Shared root DB account for WP | **Forbidden** |

## Credentials

Stored in `C:\AI MARS\local\mli\fp-0002\runtime.env` — not in reports.

## Future roles (planned, not applied)

| Role | Purpose |
|------|---------|
| Editor | Content operators — least privilege |
| SEO / admin restrictions | Planned at FW-07 — not premature |

## Admin UI restrictions

Not applied in FW-06A — document only per Forge admin UX standard.

---

*FP-0002 user and role policy — FW-06A.*
