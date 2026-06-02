# OCPilot Site Passport (Generic)

**Purpose:** sanitized facts for an OpenCart site.  
**Do not record secrets.**

## Identity

| Field | Value |
|-------|-------|
| Site label | |
| Public URL (sanitized) | |
| Environment | test / staging / production / SAFE UNKNOWN |
| Operator / owner contact | |
| Hosting provider | SAFE UNKNOWN |

## OpenCart

| Field | Value |
|-------|-------|
| OpenCart / ocStore version | SAFE UNKNOWN |
| PHP version (if known) | SAFE UNKNOWN |
| Active theme | SAFE UNKNOWN |
| Admin theme | SAFE UNKNOWN |
| Multi-store | yes / no / SAFE UNKNOWN |

## Extensions & modifications

| Signal | Present |
|--------|---------|
| ocMod | yes / no / SAFE UNKNOWN |
| vQmod | yes / no / SAFE UNKNOWN |
| Custom modules (list names only) | |
| Payment/shipping (names only) | |

## Catalog (high level)

| Field | Value |
|-------|-------|
| Approx. product count | SAFE UNKNOWN |
| Category depth | SAFE UNKNOWN |
| Filters / attributes in use | SAFE UNKNOWN |
| SEO URL enabled | SAFE UNKNOWN |

## Access classes (no secrets)

| Channel | Class (read-only / write / none) |
|---------|----------------------------------|
| Public storefront | |
| OpenCart admin | |
| FTP/SFTP | |
| Database (PMA/CLI) | |

Access patterns: [shared/external-access-patterns/](../../shared/external-access-patterns/README.md).

## Backup facts

| Field | Value |
|-------|-------|
| File backup confirmed | yes / no |
| DB backup confirmed | yes / no |
| Backup storage | external only |
| Restore method summary | |

## Baseline compare

| Field | Value |
|-------|-------|
| Versioned baseline used | e.g. `baselines/opencart-3037/` / SAFE UNKNOWN |
| Baseline empty | if yes, operator must provide baseline before diff claims |
| Major custom deltas noted | |

## Site analysis folders (where to record findings)

| Topic | Folder |
|-------|--------|
| Core / version | `opencart-analysis/` |
| Catalog | `catalog-analysis/` |
| Extensions | `extension-analysis/` |
| Theme | `theme-analysis/` |
| Controllers | `controller-analysis/` |
| SEO URLs | `seo-url-analysis/` |
| Database | `database-analysis/` |
| Import plans | `import-planning/` |
| QA | `qa/` |

## SAFE UNKNOWN

- 

## Security notes

- No secrets recorded: yes / no
- PII exposure risk:
- Access closeout needed:
