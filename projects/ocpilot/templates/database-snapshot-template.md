# OCPilot Database Snapshot Metadata

**Purpose:** label external DB backups — **not** store dump in repo.

## Snapshot identity

| Field | Value |
|-------|-------|
| Snapshot ID | |
| Site slug | |
| Created at | |
| Created by | |
| Type | full / schema-only / table-subset |

## Technical facts (sanitized)

| Field | Value |
|-------|-------|
| OpenCart version at snapshot | SAFE UNKNOWN |
| Table prefix | |
| Approx. size | |
| Engine | InnoDB / mixed / SAFE UNKNOWN |

## Storage (external)

| Field | Value |
|-------|-------|
| Location label | e.g. operator backup drive path **name only** |
| Encryption | yes / no / SAFE UNKNOWN |
| Retention | |

## Scope

| Included | Excluded |
|----------|----------|
| | e.g. customer PII tables if policy requires |

## Restore drill

| Field | Value |
|-------|-------|
| Restore tested | yes / no / SAFE UNKNOWN |
| Last test date | |

## Relation to site folders

| Copy metadata stored in | `sites/<slug>/snapshots/database/` or `backups/database/` |
|-------------------------|-----------------------------------------------------------|

## SAFE UNKNOWN

- 

## SECURITY

- Dump file must **not** be committed to git.
