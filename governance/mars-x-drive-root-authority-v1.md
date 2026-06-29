# MARS X-Drive Root Authority v1

## 1. Status

**ACTIVE** — canonical filesystem authority for MARS operational placement after operator physical migration to dedicated SSD volume **AI WS** (`X:`).

**Authority type:** operator decision + documented enforcement surfaces (AGENTS.md, `.cursorrules`, Survivability registries, validator rules).

**Not:** automated volume enforcement product, Windows ACL policy, or proof that OS/application caches write only on `X:`.

**Supersedes (operational only):** Phoenix-era paths `C:\MARS Phenix\AI MARS`, `C:\AI MARS`, and related C/D/E operational roots as **active targets**. Historical evidence retaining old paths is preserved.

---

## 2. Operator Decision

Operator completed physical copy of the acting MARS system to dedicated SSD volume **AI WS** (`X:`).

Effective **2026-06-29**, the following are the **only** active MARS operational roots:

| Role | Path |
|------|------|
| Active Brain (Git) | `X:\AI MARS\` |
| Storage Layer | `X:\AI MARS STORAGE\` |
| Local Runtime | `X:\MARS-Localhost\` |

Prior operational roots on `C:`, `D:`, and `E:` are **deprecated** for write and routine agent work.

---

## 3. Volume Identity

| Property | Required value |
|----------|----------------|
| Drive letter | `X:` |
| Volume label | `AI WS` |
| Filesystem | NTFS (expected) |

**Preflight rule:** before filesystem mutation tasks, confirm drive `X:` and label `AI WS` when volume identity can be checked (`Get-Volume -DriveLetter X`). Mismatch → **STOP — X VOLUME IDENTITY MISMATCH**.

---

## 4. Canonical Roots

```text
Volume label: AI WS
Canonical drive: X:\

Active Brain:     X:\AI MARS\
Storage Layer:    X:\AI MARS STORAGE\
Local Runtime:    X:\MARS-Localhost\
```

---

## 5. Root Roles

### `X:\AI MARS\`

Git repository, governance, projects, agents, contracts, workspaces, and tracked MARS intelligence.

### `X:\AI MARS STORAGE\`

Out-of-Git storage, backups, archives, recovery evidence, bulk datasets, Knowledge Center, and promoted artefacts.

### `X:\MARS-Localhost\`

Local runtime, Laragon, CMS installations, databases, runtime backups, logs, and local development services.

---

## 6. Deprecated Operational Roots

The following paths are **DEPRECATED OPERATIONAL ROOT — WRITE DENIED — HISTORICAL READ ONLY WHEN AUTHORIZED**:

```text
C:\AI MARS\
C:\MARS Phenix\
C:\MARS Phenix\AI MARS\
C:\AI MARS STORAGE\
C:\MARS Phenix\AI MARS STORAGE\
D:\MARS-Localhost\
E:\MARS-Localhost\
```

They may remain as historical incident evidence, backup records, reports, releases, or legacy examples. **Do not** present them as current operational targets in active rule surfaces.

---

## 7. Historical Path Preservation Rule

- Incident narratives, recovery reports, drill evidence, release logs, and immutable receipts **must not** be rewritten to replace historical paths.
- Canonical **operational** sections in living documents must reference `X:` roots.
- When a document mixes historical and operational content, update **operational sections only**.

---

## 8. Write Boundary

All MARS-controlled write operations are allowed **only** inside explicitly approved roots on volume **AI WS** (`X:`).

No MARS-controlled write operation may target another drive by default.

**Applies to:** MARS-controlled project, storage, runtime, and generated data under agent/Cursor discipline.

**Does not claim:** Windows, Cursor internals, or AppData physically write only on `X:`.

---

## 9. Read Boundary

Reading outside `X:\` is **denied by default** for routine MARS agent work.

A named external path may be read only after **explicit operator authorization** for that exact task and path.

External source material should normally be copied by the operator into:

```text
X:\AI MARS STORAGE\incoming\
```

before agent processing.

---

## 10. Destructive Operation Boundary

Destructive operations require **all** of:

1. Exact path list
2. Dry-run or equivalent preview
3. Checkpoint / backup
4. Explicit operator approval
5. Rollback method
6. Audit evidence

**Prohibited without operator charter:** deletion, replacement, or cleanup of canonical roots themselves (`X:\AI MARS\`, `X:\AI MARS STORAGE\`, `X:\MARS-Localhost\`) or volume root `X:\`.

Aligns with [projects/mars-survivability/contracts/destructive-operations-policy-v1.md](../projects/mars-survivability/contracts/destructive-operations-policy-v1.md).

---

## 11. Reparse / Junction / Symlink Rule

Do not follow junctions, symlinks, or reparse points that escape approved `X:` scope.

Resolve full target path before mutation. If resolution crosses outside an approved canonical root → **STOP**.

**Validator capability:** reparse/symlink escape detection = **PARTIAL** (path-string rules only; no runtime reparse probe in validator v1).

---

## 12. External Import Rule

Imports from outside `X:` enter via operator copy to `X:\AI MARS STORAGE\incoming\` unless a task explicitly authorizes a different exact external read path.

---

## 13. Application/System Cache Boundary

Operating-system and application-internal caches may remain outside `X:\` unless separately migrated.

The MARS write boundary applies to **MARS-controlled** artefacts, not to claiming full-machine single-volume isolation.

---

## 14. Enforcement Surfaces

| Surface | Role |
|---------|------|
| [AGENTS.md](../AGENTS.md) | Repo-wide agent filesystem authority |
| [.cursorrules](../.cursorrules) | Cursor workspace and write boundary |
| [protected-zones-registry-v1.md](../projects/mars-survivability/registries/protected-zones-registry-v1.md) | Canonical root registry |
| [validator-rules-registry-v1.json](../projects/mars-survivability/tools/validator/rules/validator-rules-registry-v1.json) | Path/deny pattern registry |
| [scoped-operation-validator-v1.mjs](../projects/mars-survivability/tools/validator/scoped-operation-validator-v1.mjs) | Human-operated CLI check |

**Automatic interception:** **NOT ENFORCED** — documentation and manual validator only.

---

## 15. Migration State

| Wave | State |
|------|-------|
| **X0** — canonical X-drive authority cutover | **COMPLETE** (this document) |
| **X1** — Cursor, agent, survivability filesystem boundary | **COMPLETE** (AGENTS, `.cursorrules`, Survivability updates) |
| **X2** — Core infrastructure reality and brain layers | **COMPLETE** ([mars-infrastructure-reality-v1.md](mars-infrastructure-reality-v1.md)) |
| **X3** — Central registry, topology, README, build-map alignment | **COMPLETE** ([reports/mars-x-drive-migration-x2-x3-core-alignment-v1.md](../reports/mars-x-drive-migration-x2-x3-core-alignment-v1.md)) |
| **X4** — Website Factory, FOUNDRY, FP-0002 path reconciliation | **COMPLETE** ([reports/mars-x-drive-migration-x4-website-factory-foundry-fp0002-v1.md](../reports/mars-x-drive-migration-x4-website-factory-foundry-fp0002-v1.md); active operational paths only — not full historical rewrite) |
| **X5** — MARS Localhost Infrastructure runtime configuration | **COMPLETE** ([reports/mars-x-drive-migration-x5-localhost-infrastructure-v1.md](../reports/mars-x-drive-migration-x5-localhost-infrastructure-v1.md)) |
| **X6A** — Forge WordPress, AG-WP-001, WPilot | **COMPLETE** ([reports/mars-x-drive-migration-x6a-forge-agwp-wpilot-v1.md](../reports/mars-x-drive-migration-x6a-forge-agwp-wpilot-v1.md)) |
| **X6B** — OCPilot active path reconciliation | **COMPLETE** ([reports/mars-x-drive-migration-x6b-ocpilot-site002-protected-v1.md](../reports/mars-x-drive-migration-x6b-ocpilot-site002-protected-v1.md)) |
| **X6** — CMS pilot programmes (aggregate) | **COMPLETE** (X6A + X6B) |
| **X7** — MIG, ORCA, ATLAS, OPS, EAR, NOVA programmes | **COMPLETE** ([reports/mars-x-drive-migration-x7-remaining-programmes-v1.md](../reports/mars-x-drive-migration-x7-remaining-programmes-v1.md)) |
| **X8** — Web-GPT sync and current source-pack publication | **COMPLETE** ([reports/mars-x-drive-migration-x8-web-gpt-current-sync-pack-v1.md](../reports/mars-x-drive-migration-x8-web-gpt-current-sync-pack-v1.md); pack `web-gpt-sources/mars-current-x-drive-2026-06/`; legacy packs unchanged) |
| **X9** — Final active-path audit, deferred classification, migration closure | **COMPLETE** ([mars-x-drive-migration-closure-v1.md](mars-x-drive-migration-closure-v1.md); [reports/mars-x-drive-migration-x9-final-audit-and-closure-v1.md](../reports/mars-x-drive-migration-x9-final-audit-and-closure-v1.md); deferred register [mars-x-drive-deferred-path-register-v1.md](mars-x-drive-deferred-path-register-v1.md)) |

**X9 scope honesty:** X9 closes canonical authority and clean active operational documentation. It does **not** mean all historical old paths were removed, all external chats updated, all deferred tooling migrated, all runtime components tested, or all database locations verified.

**X7 scope (2026-06-29):** X7 covers clean active operational programme paths for remaining registered programmes. Overlapping dirty WIP, historical evidence, generated artefacts, semantic caches, and programme-specific deferred tooling remain outside this completion claim.

---

## 16. Out of Scope (X0–X1)

- Runtime scripts and programme docs outside Survivability boundary files
- `X:\AI MARS STORAGE\` content mutation
- `X:\MARS-Localhost\` config mutation
- README.md, `registry/**`, project programme indexes (deferred to X2–X3)
- Blind mass path replacement across historical reports

---

## 17. Evidence

| Check | Result |
|-------|--------|
| Drive letter | `X:` |
| Volume label | `AI WS` |
| Filesystem | `NTFS` |
| Repository root | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| Baseline HEAD (X0 task start) | `7ad7d7e69f19f196da59e248278cfcb767496cc7` |
| X2–X3 task HEAD (start) | `497ee8c4f045ba1575c80f09138f309cfbb8338d` |

---

## 18. Decision

**ACCEPTED** — `X:` on volume **AI WS** is the sole active MARS operational volume. Canonical roots are `X:\AI MARS\`, `X:\AI MARS STORAGE\`, and `X:\MARS-Localhost\`. Deprecated C/D/E roots are write-denied for MARS-controlled operations.

---

## Guard Capability Matrix (X0–X1)

| Capability | State | Evidence |
|------------|-------|----------|
| Drive allowlist | **CONFIGURED** | `filesystem_boundary.required_drive` in validator rules; AGENTS.md, `.cursorrules` |
| Canonical root allowlist | **CONFIGURED** | This document §4; protected-zones registry §0; validator rules |
| Deprecated root denylist | **CONFIGURED** | This document §6; validator rules `denied_roots` |
| Volume label | **PRECHECK_REQUIRED** | Operator preflight; not auto-queried by validator |
| Parent traversal (`..`) | **ENFORCED** | Validator path normalization rejects `..` escape |
| UNC rejection | **ENFORCED** | Validator rejects `\\` UNC paths |
| Reparse escape | **PARTIAL** | String-level only; no OS reparse probe |
| Destructive command classification | **CONFIGURED** | `forbidden_commands`, `dangerous_patterns` in validator rules |
| Automatic interception | **NOT ENFORCED** | Human-operated validator + agent rules only |
| Operator approval | **REQUIRED** | destructive-operations-policy, AGENTS.md |
| Dry-run | **REQUIRED** | destructive-operations-policy |
| Checkpoint | **REQUIRED** | snapshot-manifest-standard, enforcement registry |
| Kill switch | **DOCUMENTED** | operational-halt-protocol; not automated |

---

*End of MARS X-Drive Root Authority v1.*
