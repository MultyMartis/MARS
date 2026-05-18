# WPilot Capability Matrix v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** allowed and excluded capabilities for first plugin implementation.

This matrix is the implementation boundary. Anything not listed as CAN is excluded unless a later contract explicitly adds it.

## CAN

| Capability | Status | Conditions |
|---|---|---|
| Install from local ZIP | CORE / PLANNED / DEV-ONLY | Human administrator installs plugin. |
| Activate plugin | CORE / PLANNED / DEV-ONLY | Activation leaves bridge disabled. |
| Show admin status page | CORE / PLANNED | Admin-only, escaped output. |
| Enable/disable bridge | CORE / PLANNED | Admin-only, nonce-protected, DEV confirmation required. |
| Generate/rotate/revoke token | CORE / PLANNED | Admin-only; plaintext shown once; no plaintext log. |
| Read site info | CORE / PLANNED | Token required; sanitized response. |
| Read theme metadata | CORE / PLANNED | Token required; no updates. |
| Read plugin metadata | CORE / PLANNED | Token required; no updates. |
| List pages | CORE / PLANNED | Token required; allowed post types only. |
| Read page content | CORE / PLANNED | Token required; allowed target only. |
| Detect WPBakery | CORE / PLANNED | Shortcode-aware, no full rendering claim. |
| Build structure map | CORE / PLANNED | Refuse or mark SAFE UNKNOWN for unclear structures. |
| Inspect indexing signals | CORE / PLANNED / DEV-ONLY | Read-only; no production SEO automation. |
| Create page backup | CORE / PLANNED | Plugin-owned snapshot before write. |
| Perform exact scoped replacement | CORE / PLANNED / DEV-ONLY | One page, exact once, approved, backed up, validated. |
| Roll back plugin-created backup | CORE / PLANNED / DEV-ONLY | Backup target must match; WordPress API write. |
| Log operations | CORE / PLANNED | Sanitized audit records; no secrets. |
| Emergency disable | CORE / PLANNED | Admin action or critical safety condition. |
| Refuse unsafe operation | CORE / PLANNED | Refusal is a valid safety outcome. |

## CANNOT

| Capability | Status | Reason |
|---|---|---|
| Mass edits | EXCLUDED | Too broad for MVP. |
| Unrestricted replace | EXCLUDED | Must be exact scoped replacement only. |
| Arbitrary SQL | EXCLUDED | No SQL console or request-supplied SQL. |
| Direct SQL content mutation | EXCLUDED | Scoped writes use WordPress APIs. |
| Unrestricted filesystem access | EXCLUDED | No file manager behavior. |
| Execute PHP | EXCLUDED | No code execution. |
| Execute shell commands | EXCLUDED | No shell bridge. |
| Execute JavaScript/templates from request | EXCLUDED | No code execution. |
| Modify plugins/themes/core | EXCLUDED | No update/deployment capability. |
| Edit `wp-config.php` | EXCLUDED | Secret-bearing and high-risk file. |
| Upload/delete arbitrary files | EXCLUDED | Filesystem mutation outside MVP. |
| Autonomous operation | EXCLUDED | Human-supervised only. |
| Browser automation | EXCLUDED | Outside plugin MVP. |
| Deployment | EXCLUDED | Not a deploy bot. |
| Auto-recovery | EXCLUDED | Manual rollback only. |
| Hidden edits | EXCLUDED | All writes logged and human-approved. |
| SaaS/cloud connector | EXCLUDED | Local DEV plugin only. |
| Production readiness claim | EXCLUDED | Not proven. |
| Credential storage | EXCLUDED | No external secrets. |

## Conditional / SAFE UNKNOWN

| Capability | Status | Handling |
|---|---|---|
| Read private/draft pages | SAFE UNKNOWN | Depends on capability decision; may be excluded in first implementation. |
| Multisite support | SAFE UNKNOWN | Outside MVP unless explicitly added. |
| SEO plugin-specific signal reads | SAFE UNKNOWN | Read-only only; exact plugin support unknown. |
| Cache purge | EXCLUDED for MVP | Avoid broad site-control surface. |
| WPBakery raw HTML edits | SAFE UNKNOWN / EXCLUDED | Refuse unless safely classified in future. |
| The7-specific parsing | SAFE UNKNOWN | Do not claim compatibility until tested. |

## Rule For Unlisted Capabilities

If a capability is not listed in CAN, implementation must treat it as EXCLUDED or SAFE UNKNOWN and refuse the operation.

