# EAR Snapshot Contract v1

**Purpose:** Define the **output package** EAR delivers to consumers.  
**Status:** contract specification — **no** serializer, validator, or schema file in-repo at foundation freeze.

---

## Package identity

| Field | Required | Notes |
|-------|----------|-------|
| `snapshot_id` | Yes | Unique id, e.g. `snap-20260601-site-001-run5-p1` |
| `snapshot_version` | Yes | Contract version: `ear-snapshot-v1` |
| `site_ref` | Yes | Consumer site id (e.g. `SITE-001`) |
| `created_at` | Yes | ISO 8601, operator timezone noted in metadata |
| `ear_mode` | Yes | `0`, `1`, or `2` at acquisition time |
| `operator_approval` | Yes | Who approved publish (non-secret identifier) |

---

## Package structure (logical)

```
Snapshot/
├── metadata/
├── file-manifest/
├── extension-inventory/
├── database-metadata/
├── access-log/
└── safe-unknown/
```

Physical layout may be a folder tree or `.zip` in external bulk storage — **SAFE UNKNOWN** until Phase 2 charter.

---

## Section: metadata

**Purpose:** Context for consumers without opening bulk files.

**Suggested fields:**

| Field | Example | Verification |
|-------|---------|--------------|
| `platform_claim` | `ocStore 3.0.3.8 (rs.2)` | Consumer must cross-check file evidence |
| `environment` | `TEST` | Operator-recorded |
| `urls` | test storefront, admin pattern | No credentials |
| `baseline_ref` | `ocstore-3038-rs2` | OCPilot consumer |
| `consumer_target` | `ocpilot` | Routing |
| `bulk_root` | External path to payload | Reference only |

---

## Section: file-manifest

**Purpose:** Enable diff vs baseline or prior snapshot.

**Contents (one of):**

- Inline path list with size + hash (SHA256 recommended)
- **OR** `archive_ref` pointing to external ZIP + sidecar manifest

**Rules:**

- No absolute secrets paths in git-bound copies
- Exclude cache/tmp if policy defines — document exclusions in metadata

---

## Section: extension-inventory

**Purpose:** Modules, themes, ocMod, plugins — platform-specific.

**OpenCart / ocStore (OCPilot):**

- Extension list from admin or `extension/` scan
- ocMod XML paths (names only if large)

**WordPress (future):**

- Plugins, themes, mu-plugins

**SAFE UNKNOWN:** Unified schema across CMS — Phase 4.

---

## Section: database-metadata

**Purpose:** Schema-level audit without mandating full dump in v1.

**Suggested contents:**

- Table list + count
- Prefix (e.g. `oc_`)
- Engine/collation summary if available
- Version markers from `oc_setting` or equivalent — **if** obtained read-only

**Not required in v1:**

- Full row data
- Customer PII tables content

---

## Section: access-log

**Purpose:** Audit trail of **how** evidence was acquired (not site access log files).

| Entry | Example |
|-------|---------|
| `approved_by` | operator handle |
| `approved_at` | timestamp |
| `channel` | `sftp`, `manual-drop`, `pma-export` |
| `scope` | `read-only`, paths prefix |
| `hitl_checklist` | reference to charter or run id |

---

## Section: safe-unknown

**Purpose:** Explicit honesty — consumers must not hallucinate missing data.

**Format:** List of objects:

```yaml
# Illustrative only — not enforced schema file
- topic: live_version_proof
  reason: no index.php in package
  unblock: P1-A or SFTP download of root index.php
```

**Rule:** If a section is empty because data is missing, **`safe-unknown` must say so** — empty section alone is insufficient.

---

## Consumer handoff rules

1. Consumer receives **Snapshot Package** (or reference thereto).
2. Consumer **never** receives raw passwords in the package.
3. Consumer may read `secret_ref` for operator-local resolution — **not** for agent commit to git.
4. Consumer validates contract version; rejects or partial-runs on mismatch.
5. Consumer writes analysis to its own report paths (e.g. OCPilot `reports/`).

---

## Example snapshot (SITE-001 hypothetical)

**Status:** **not an actual snapshot** — illustrates target shape after acquisition.

| Section | State at Run 5 init freeze |
|---------|----------------------------|
| metadata | Partial (repo docs only) |
| file-manifest | **Missing** — blocker B-EV-02 |
| extension-inventory | **Missing** |
| database-metadata | **Missing** |
| access-log | Run 5 init only (documentation) |
| safe-unknown | Would list all technical unknowns from RUN-5-FIRST-FINDINGS |

---

## Versioning

| Contract | When to bump |
|----------|--------------|
| `ear-snapshot-v1` | Breaking field removals or renames |
| Minor additions | Optional fields only — document in changelog **SAFE UNKNOWN** location |

---

## SAFE UNKNOWN

- JSON Schema / JSON-LD official file — not created in v1 foundation task.
- Checksum of entire package — recommended Phase 4.
