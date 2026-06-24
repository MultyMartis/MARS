# AG-WP-001 — Secret Boundary Contract v1

**Document type:** Secret and credential boundary  
**Version:** v1  
**Stage:** FW-07B  
**Date:** 2026-06-24

---

## Rules

- Credentials live **outside Git**
- No secrets in operation input/output **examples** or fixtures
- No full `wp-config.php` in reports
- No complete `runtime.env` in artifacts
- No passwords on command lines when avoidable
- No authentication strings in audit logs
- Sanitized logs (`logging_policy.sanitize_secrets: true`)
- Local secrets consumed only by approved MLI runtime scripts (indirect)
- Production secrets **not available** to AG-WP-001 foundation

---

## Secret access classes

| Class | AG-WP-001 foundation |
|-------|---------------------|
| `NO_ACCESS` | brain/planning ops |
| `INDIRECT_CONSUMPTION` | **default** for local runtime read-only |
| `OPERATOR_PROVIDED_SESSION` | future staging charter only |
| `PROHIBITED` | production, MCP, WPilot auto-bind |

---

## Redacted paths (minimum)

`wp-config.php` · `runtime.env` · `.env` · `*credentials*` · database password fields

---

*Secret boundary contract v1.*
