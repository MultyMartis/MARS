# External Access — Safety Boundaries

**Scope:** common rules across all access channels (browser, FTP, database).  
**Applies to:** WPilot, OCPilot, future MODxPilot, CustomSitePilot.

## Core principles

1. **Human confirms target** — no work on assumed or guessed hosts/URLs/DB names.
2. **Human confirms environment** — production mistakes are high severity; staging preferred when available.
3. **Human confirms backup status** — write-class work requires backup; read-only audit still records backup *availability*.
4. **Human controls credentials/session** — operator owns login; repo never stores secrets.
5. **Evidence-only for AI/Cursor** — work from operator-provided exports, screenshots, manifests, or explicit supervised steps.
6. **No destructive actions without approval** — delete, overwrite, bulk SQL, mass file operations.
7. **No secrets in repo** — configs with credentials, tokens, dumps forbidden by default.
8. **REPORT after every access-based operation** — `# REPORT — …` mandatory.

## Risk levels

| Level | Examples | Default stance |
|-------|----------|----------------|
| **Low** | Public storefront view, sanitized path list | Proceed with passport update |
| **Medium** | Admin read-only, FTP tree list, schema inspect | Gates + REPORT |
| **High** | Production file edit, catalog SQL, theme overwrite | Charter + backup + rollback + HITL |
| **Critical** | Mass delete, core vendor overwrite, unscoped dump to git | Refuse until explicit approval and safeguards |

## Stop conditions (halt task)

- Target or environment mismatch.
- Backup unavailable for write-class work.
- Secret detected in material destined for repo.
- Scope creep beyond charter.
- Operator withdraws approval.
- Destructive action requested without rollback path.

## SAFE UNKNOWN triggers

Record SAFE UNKNOWN when:

- OpenCart/WordPress/MODx version unverified.
- Extension/module list incomplete.
- Baseline version match uncertain.
- Backup existence unconfirmed.
- Custom vs core file classification unclear.
- Hosting access class unknown.

Do not fill gaps with assumptions. Ask operator or inspect read-only evidence first.

## Channel cross-reference

| Channel | Pattern doc |
|---------|-------------|
| Browser / admin | [browser-admin-access-pattern.md](browser-admin-access-pattern.md) |
| FTP / hosting files | [ftp-hosting-file-access-pattern.md](ftp-hosting-file-access-pattern.md) |
| Database / PMA | [pma-database-access-pattern.md](pma-database-access-pattern.md) |

## SECURITY RISK

If secrets were exposed in repo or report → halt, operator remediation, no commit of affected files. See pilot-specific [access-and-safety.md](../../projects/ocpilot/access-and-safety.md) for OCPilot; WPilot has its own safety docs under `projects/wpilot/`.

## Not automation

These boundaries describe **human-operated** discipline. No claim of autonomous access bots, MCP hosting adapters, or runtime FTP/PMA agents unless separately evidenced in-repo.
