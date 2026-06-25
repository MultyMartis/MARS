# AG-WP-001 — Command Execution Contract v1

**Document type:** Command execution contract  
**Version:** v1  
**Stage:** FW-07B  
**Date:** 2026-06-24

**Extends:** [FORGE-WORDPRESS-SAFE-COMMAND-POLICY-v1.md](../FORGE-WORDPRESS-SAFE-COMMAND-POLICY-v1.md)

---

## Allowed command families (R0 local)

| Family | Examples |
|--------|----------|
| Git read | `git status`, `git diff`, `git log`, `git show` |
| PHP lint | `php -l <file>` |
| Composer validation | `composer validate`, `composer install` (approved lock only) |
| PHPCS | `phpcs --standard=WordPress` |
| WP-CLI read | `wp core verify-checksums`, `wp db check`, `wp plugin list`, `wp theme list`, `wp option get` |
| HTTP read-only | GET probes to local MLI host |
| Playwright | project smoke tests (read-only validation) |

---

## Controlled families (R2–R3 — not auto-authorized)

| Family | Examples | Gate |
|--------|----------|------|
| WP-CLI mutation | `wp plugin activate/deactivate`, `wp option update` | R3 + operator approval |
| Content ops | `wp post create/update` | R3 + approval + backup |
| DB migrations | scripted migrations | R3 + backup + rollback plan |
| Filesystem writes | theme/plugin source | R2 + plan + checkpoint |
| Git write | `git commit` selective | R2 + approval scope |

---

## Forbidden families

- Arbitrary shell from user-provided text
- Arbitrary SQL
- `DROP` / `TRUNCATE` without explicit migration contract
- Recursive deletion outside approved backup cleanup
- `git push --force`, `git reset --hard`
- Production SSH / production WP-CLI
- Credential printing (`wp config list` with secrets)

---

## Execution record (required per command)

| Field | Required |
|-------|----------|
| `operation_id` | yes |
| `environment` | yes |
| `working_directory` | yes |
| `approval_reference` | when R2+ |
| `expected_output` | yes |
| `failure_code_mapping` | yes |
| `audit_record` | yes |

**Runtime:** Contract only until FW-07C harness.

---

*Command execution contract v1.*
