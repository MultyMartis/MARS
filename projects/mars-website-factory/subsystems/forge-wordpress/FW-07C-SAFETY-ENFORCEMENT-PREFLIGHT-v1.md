# FW-07C — Safety Enforcement Preflight v1

**Document type:** Safety enforcement preflight and admission design
**Version:** v1
**Date:** 2026-06-25
**Stage:** FW-07C preflight (design only — **no runtime harness built**)
**Authority:** Canonical repo `C:\MARS Phenix\AI MARS` @ `mars/canonical-post-recovery`

**Prerequisite forensic audit:** `C:\MARS Phenix\_reconstruction-control\wp-forge-incident-forensic\`
**External reports:** `C:\MARS Phenix\_reconstruction-control\wp-forge-safety-preflight\`

**Honesty:** This document defines **mandatory enforcement design** and **admission gates**. Policy and prompt instructions are **not** technical safeguards until bound to executable components with negative tests.

---

## 1. Preflight verdict

| Field | Value |
|-------|-------|
| **Resume verdict (prior)** | `WP_FORGE_READY_FOR_SAFE_PREFLIGHT` |
| **Preflight outcome** | `FW07C_PREFLIGHT_COMPLETE_READY_FOR_ENFORCEMENT_FOUNDATION` |
| **FW-07C-0** | **YES** — implement enforcement foundation in repo only |
| **FW-07C-1** | **YES_AFTER_PRECONDITION** — after FW-07C-0 gates G1–G14 pass |
| **Runtime writes** | **NO** until FW-07C-2+ with operator charter |
| **Exact next task** | Implement FW-07C-0 enforcement foundation (repo only) |

---

## 2. Safeguard taxonomy (required distinction)

| Class | Definition | Counts as enforcement? |
|-------|------------|------------------------|
| **POLICY** | Human-readable rule without executable binding | **No** |
| **DOCUMENTED_SAFEGUARD** | Contract/checklist describing intended control | **No** |
| **VALIDATOR** | CLI/script that can evaluate inputs when invoked | **Partial** |
| **EXECUTABLE_GUARD** | Code path that blocks execution before side effects | **Yes** (if invoked) |
| **TESTED_ENFORCEMENT** | Guard with negative fixtures proving fail-closed | **Yes** |
| **RUNTIME_BINDING** | Guard wired into harness execution path | **Yes** (required for FW-07C+) |
| **OPERATOR_PROCEDURE** | Human checklist/drill | **No** (supports only) |

---

## 3. Safeguard inventory

| Safeguard | Path | Type | Executable? | Entrypoint | Maturity |
|-----------|------|------|-------------|------------|----------|
| Destructive Operations Policy | `projects/mars-survivability/contracts/destructive-operations-policy-v1.md` | POLICY | DOCUMENT_ONLY | — | F-01..F-14 documented |
| Normal ops resumption checklist | `governance/mars-normal-operations-resumption-checklist-v1.md` | OPERATOR_PROCEDURE | DOCUMENT_ONLY | — | Phoenix paths current |
| Path validator CLI | `projects/mars-survivability/tools/validator/scoped-operation-validator-v1.mjs` | VALIDATOR | PARTIAL_EXECUTABLE | `node scoped-operation-validator-v1.mjs` | D-01 drill; **not** WP-bound |
| Validator rules registry | `projects/mars-survivability/tools/validator/rules/validator-rules-registry-v1.json` | DOCUMENTED_SAFEGUARD | PARTIAL_EXECUTABLE | bundled with validator | Legacy `C:\AI MARS` markers |
| GitGuard | `projects/mars-survivability/contracts/gitguard-survivability-evolution-v1.md` | POLICY | DOCUMENT_ONLY | — | No automation |
| Survivability protocols | `projects/mars-survivability/protocols/` | POLICY | DOCUMENT_ONLY | — | Ecosystem-wide |
| Denylist (shell) | `validator-rules-registry-v1.json` → `forbidden_commands` | VALIDATOR | PARTIAL_EXECUTABLE | pattern match in validator | No reparse/UNC |
| Allowlist (roots) | resumption checklist + protected-zones-registry | OPERATOR_PROCEDURE | DOCUMENT_ONLY | — | Phoenix canonical |
| Dry-run | `projects/mars-survivability/protocols/safe-execution-layer-v1.md` | POLICY | DOCUMENT_ONLY | — | Not harness-bound |
| Backup/checkpoint | MLI `backups/` + FP-0002 scripts | OPERATOR_PROCEDURE | PARTIAL_EXECUTABLE | `mars-runtime/scripts/backup-runtime.ps1` | Operator-initiated |
| Operator confirmation | `projects/mars-survivability/protocols/human-authority-protocol-v1.md` | POLICY | DOCUMENT_ONLY | — | Not token-enforced |
| Audit receipt | `projects/mars-survivability/tools/validator/validator-report-format-v1.md` | DOCUMENTED_SAFEGUARD | DOCUMENT_ONLY | — | No forge log dir |
| Kill switch | `projects/mars-survivability/protocols/operational-halt-protocol-v1.md` | POLICY | DOCUMENT_ONLY | — | Not productized |
| Sandbox configuration | Cursor settings | SAFE_UNKNOWN | NOT_FOUND in repo | IDE | Not repo-enforceable |
| Typed operation approval | `agents/AG-WP-001-APPROVAL-TOKEN-CONTRACT-v1.md` | DOCUMENTED_SAFEGUARD | DOCUMENT_ONLY | — | No token runtime |
| Rollback contract | `operations/ag-wp-001/wp-plan-rollback.json`, `wp-rollback-prepare.json` | DOCUMENTED_SAFEGUARD | DOCUMENT_ONLY | — | Scoped design only |
| AG-WP-001 contract validator | `tools/validate-ag-wp-001-operation-contracts.mjs` | VALIDATOR | EXECUTABLE_UNTESTED | `node validate-ag-wp-001-operation-contracts.mjs` | Schema/contracts only |
| AG-WP-001 filesystem scope | `agents/AG-WP-001-FILESYSTEM-SCOPE-CONTRACT-v1.md` | DOCUMENTED_SAFEGUARD | DOCUMENT_ONLY | — | References legacy `C:\AI MARS` |
| Forge safe command policy | `FORGE-WORDPRESS-SAFE-COMMAND-POLICY-v1.md` | POLICY | DOCUMENT_ONLY | — | WP-specific design |
| MLI WordPress local guard | `projects/mars-localhost-infrastructure/MARS-LOCALHOST-WORDPRESS-LOCAL-GUARD-STANDARD-v1.md` | POLICY | DOCUMENT_ONLY | — | MLI authority |

**Bypass risk (summary):** All ecosystem validators are **human-invoked**; Cursor agent shell is **not** auto-gated. WP Forge has **zero** `RUNTIME_BOUND` safeguards today.

---

## 4. WordPress sandbox model

### 4.1 Authority-aligned roots (verified 2026-06-25)

| Zone | Path | Default access | Notes |
|------|------|----------------|-------|
| Canonical brain | `C:\MARS Phenix\AI MARS` | READ ONLY except exact task scope | Git SoT |
| Canonical STORAGE | `C:\MARS Phenix\AI MARS STORAGE` | READ ONLY by default | Bulk artefacts |
| Runtime root (protected parent) | `E:\MARS-Localhost` | **DENY writes** | MLI authority |
| WordPress site sandbox | `E:\MARS-Localhost\sites\wordpress\{class}\{slug}\` | Scoped per manifest | **Only** writable target |
| Site backups (MLI) | `E:\MARS-Localhost\backups\wordpress\{class}\{slug}\` | Operator charter | Not `snapshots/` — **MLI uses `backups/`** |
| Forge audit logs (proposed) | `E:\MARS-Localhost\logs\forge-wordpress\{site-id}\` | Append-only when harness exists | **NOT_FOUND** on disk |
| Brain synthetic source | `workspaces/forge-wordpress-synthetic/FWS-0001/` | READ for inspect; WRITE deferred | Git-tracked |
| Secrets | `C:\AI MARS\local\mli\{site}\runtime.env` (per MLI manifest) | **NO_ACCESS** for agent | Location only in docs |

### 4.2 Registered local sandboxes

| site_id | runtime_id | class | physical_root | URL | FW-07C initial |
|---------|------------|-------|---------------|-----|----------------|
| `fws-0001` | MLI-WP-SYN-001 | synthetic | `E:\MARS-Localhost\sites\wordpress\synthetic\fws-0001` | `http://fws-0001.test/` | **YES** (LOCAL_SYNTHETIC) |
| `shpigovsky` | MLI-WP-FP0002-LOCAL | projects | `E:\MARS-Localhost\sites\wordpress\projects\shpigovsky` | `http://shpigovsky.test/` | **NO** (pilot — defer to FW-07C-2+) |

### 4.3 Per-operation envelope (mandatory)

Every write-capable operation **must** carry:

```text
site_id, runtime_root, allowed_root, exact_target_path, operation_type,
risk_class, dry_run_result, backup_snapshot_id, approval_state,
rollback_method, audit_receipt_id
```

Fail-closed: missing any required field → **DENY**.

---

## 5. Hard denylist

### 5.1 Protected roots (always DENY as write target)

```text
C:\
C:\Users
C:\Program Files
C:\Program Files (x86)
C:\Windows
C:\MARS Phenix          (parent — only explicit subpaths allowlisted)
C:\AI MARS              (legacy)
C:\this is backUP AI MARS 23.06.2026
E:\
E:\MARS-Localhost       (parent — site sandbox descendants only)
canonical repo root (full tree as bulk target)
canonical STORAGE root (full tree as bulk target)
legacy / archive / _legacy-hold trees
```

### 5.2 Path rejection rules

| Rule | Behavior |
|------|----------|
| Empty/null path | DENY |
| Drive root | DENY |
| Parent of selected site sandbox | DENY |
| Wildcards (`*`, `?`) | DENY |
| Relative traversal (`..`) | DENY |
| UNC (`\\server\share`) | DENY |
| Symlink/junction/reparse escape | DENY (must resolve and re-validate) |
| source == destination | DENY |
| destination parent of source (reversal) | DENY |
| Case-only bypass | DENY (normalize to canonical case) |
| Trailing dot/space (Win32) | DENY |
| Path > MAX_PATH without `\\?\` handling | DENY until explicit support |

---

## 6. Path validation contract (fail-closed)

```text
1.  Receive raw path
2.  Reject empty/null → DENY
3.  Resolve absolute path
4.  Normalize separators
5.  Reject wildcards → DENY
6.  Reject traversal → DENY
7.  Resolve reparse points (junction/symlink) → re-validate resolved path
8.  Validate selected site root from MLI manifest registry
9.  Confirm target is descendant of allowed_root
10. Confirm target is not protected parent
11. Confirm operation risk class vs zone policy
12. Require dry-run artifact (mutating ops)
13. Require checkpoint/snapshot id (R2+)
14. Require approval token (R2+ per matrix)
15. Execute only via typed operation_id
16. Write audit receipt (allow or deny)
```

Any step failure → **DENY** (not warning).

**Gap:** Survivability `scoped-operation-validator-v1.mjs` implements steps 1–6 partially for **shell command strings**, not Forge typed-operation paths, and lacks reparse resolution.

---

## 7. Risk classes (R0–R5)

| Class | Description | FW-07C initial policy |
|-------|-------------|----------------------|
| **R0** | Read-only inspect | Automatic after preflight |
| **R1** | Additive drafts (brain artefacts) | Automatic in brain paths only |
| **R2** | Bounded file modification | Snapshot + diff + approval — **FW-07C-3** |
| **R3** | Bounded delete/replace | Operator approval mandatory — **deferred** |
| **R4** | Directory-level mutation | **Disabled** for initial harness |
| **R5** | DB/runtime/global | **Disabled** until later validated phase |

---

## 8. AG-WP-001 operations (42)

**Registry:** `operations/ag-wp-001/operations-v1.json`
**Binding state:** 0 proven runtime bindings; 11 `BOUND_NOT_IMPLEMENTED`, 31 `UNBOUND`

### 8.1 FW-07C-1 initial read-only subset (bound-first)

| operation_id | legacy_op_id | binding |
|--------------|--------------|---------|
| `wp.inspect.runtime` | inspect_wp_runtime | BOUND_NOT_IMPLEMENTED |
| `wp.inspect.theme` | inspect_theme | BOUND_NOT_IMPLEMENTED |
| `wp.inspect.plugin_state` | inspect_plugin_state | BOUND_NOT_IMPLEMENTED |
| `wp.inspect.routes` | inspect_routes | BOUND_NOT_IMPLEMENTED |
| `wp.validate.php_syntax` | validate_php_syntax | BOUND_NOT_IMPLEMENTED |
| `wp.validate.wpcs` | validate_wpcs | BOUND_NOT_IMPLEMENTED |
| `wp.validate.core_checksums` | validate_wordpress_checksums | BOUND_NOT_IMPLEMENTED |
| `wp.validate.database` | validate_database | BOUND_NOT_IMPLEMENTED (read-only check) |
| `wp.validate.routes` | validate_routes | BOUND_NOT_IMPLEMENTED |

**Brain-only inspect (no runtime touch):** remaining `wp.inspect.*` with `BRAIN_ONLY` scope — admit in FW-07C-1 after path validator covers brain paths.

**Deferred:** all `wp.scaffold.*`, `wp.generate.*`, `wp.change.*`, `wp.backup.*`, `wp.checkpoint.*`, mutating validate side-effects.

Full map: `ag-wp-001-operation-risk-map.csv` (external manifest).

---

## 9. Snapshot and rollback model

### 9.1 Snapshot types

| Type | FW-07C-0 | FW-07C-1 read-only | FW-07C-2+ |
|------|----------|-------------------|-----------|
| Filesystem snapshot | Design | Optional manifest-only | Required R2+ |
| Database export | Design | Not required | Required R3+ |
| Configuration snapshot | Design | wp-config hash log | Required R2+ |
| Operation manifest | **Required** | **Required** | **Required** |
| Pre-change hashes | Design | N/A | Required R2+ |
| Post-change hashes | Design | N/A | Required R2+ |
| Rollback receipt | Design | N/A | Required R2+ |

### 9.2 Rollback principles

- **Scoped, operation-specific** — never `git reset --hard` on runtime tree
- Never restore whole parent `E:\MARS-Localhost`
- Never mirror-delete site root
- Use MLI backup baselines + per-file revert from checkpoint manifest

---

## 10. WordPress protected zones

| Zone | Read | Write (initial harness) | Snapshot | Approval |
|------|------|-------------------------|----------|----------|
| WordPress core | Allowed (inspect) | **DENY** | N/A | N/A |
| wp-config.php | Metadata only | **DENY** | Hash log | Operator |
| .htaccess | Allowed | **DENY** | Hash log | Operator |
| wp-content/themes (custom) | Allowed | **DENY** until FW-07C-2+ | Required later | Plan+checkpoint |
| wp-content/plugins (custom) | Allowed | **DENY** until FW-07C-2+ | Required later | Plan+checkpoint |
| wp-content/uploads | Allowed | **DENY** | N/A | Operator |
| mu-plugins | Allowed | **DENY** | Hash log | Operator |
| languages | Allowed | **DENY** | N/A | N/A |
| cache | Allowed | **DENY** | N/A | N/A |
| vendor | Allowed | **DENY** | N/A | N/A |
| database | Read-only validate | **DENY** | Export deferred | Operator |
| generated assets | Allowed | **DENY** | N/A | N/A |
| logs | Allowed | Append audit only | N/A | N/A |
| backups | Allowed | Operator only | N/A | Operator |

---

## 11. Environment boundary

| Environment | FW-07C initial | Evidence |
|-------------|----------------|----------|
| LOCAL_SYNTHETIC | **ALLOW** (read-only harness) | MLI-WP-SYN-001, FWS-0001 |
| LOCAL_PROJECT_RUNTIME | **DENY** (initial) | shpigovsky = pilot |
| REMOTE_DEV | **DENY** | WPilot bridge not first harness |
| REMOTE_TEST | **DENY** | — |
| REMOTE_PRODUCTION | **DENY** | `production_allowed: false` all ops |

**Credential isolation:** No mixing MLI local secrets with WPilot remote credentials in one harness session.

---

## 12. WPilot / Forge / MLI boundary

```text
Website Factory package
  → Forge WordPress plan (AG-WP-001)
  → typed operations (operations-v1.json)
  → local sandbox (MLI manifest)
  → forge-path-validator (FW-07C-0, to build)
  → operator approval gate
  → future WPilot bridge (FW-07C-5+)
```

| Actor | Role |
|-------|------|
| **Website Factory** | Frontend/package producer |
| **Forge WordPress** | Agent + typed-operation producer |
| **AG-WP-001** | Bounded WordPress programming agent (brain preserved, runtime inactive) |
| **MLI** | Runtime provider (`E:\MARS-Localhost`) |
| **WPilot** | Reference operational bridge — **not** FW-07C-1 target |

---

## 13. Admission gates G1–G15

| Gate | Requirement | Current state | Blocking? |
|------|-------------|---------------|-----------|
| G1 | Canonical authority confirmed | **PASS** — HEAD `bd5ddef7` = remote | No |
| G2 | Exact local sandbox selected | **PASS** — fws-0001 manifest | No |
| G3 | Path validator executable | **PARTIAL** — survivability CLI; not Forge-bound | **Yes** for FW-07C-1 |
| G4 | Denylist executable | **PARTIAL** — shell patterns only | **Yes** for FW-07C-1 |
| G5 | Reparse escape protection | **NOT_FOUND** | **Yes** for FW-07C-1 |
| G6 | Operation registry mapped | **PASS** — 42 ops in JSON | No |
| G7 | Risk classes assigned | **PASS** — R0–R5 in registry | No |
| G8 | Dry-run contract | **DOCUMENT_ONLY** | **Yes** for mutating phases |
| G9 | Snapshot contract | **DOCUMENT_ONLY** | **Yes** for FW-07C-2+ |
| G10 | Rollback contract | **DOCUMENT_ONLY** | **Yes** for FW-07C-2+ |
| G11 | Audit logging | **NOT_FOUND** — no `logs/forge-wordpress/` | **Yes** for FW-07C-1 |
| G12 | Kill switch | **DOCUMENT_ONLY** | **Yes** for FW-07C-1 |
| G13 | Negative fixtures | **NOT_FOUND** for Forge paths | **Yes** for FW-07C-1 |
| G14 | Destructive commands disabled | **PARTIAL** — validator patterns | **Yes** for harness |
| G15 | Operator approval policy | **DOCUMENT_ONLY** | **Yes** for R2+ |

**FW-07C-0 admission:** G1, G2, G6, G7 satisfied — **proceed**.
**FW-07C-1 admission:** G3–G5, G11–G14 must reach TESTED_ENFORCEMENT.

---

## 14. Kill switch (design)

| Control | Specification |
|---------|---------------|
| Global default | Forge execution **disabled** |
| Per-site enable | Operator-issued `site_enable_token` bound to `site_id` + expiry |
| Concurrency | Single active operation per site |
| Cancel | Operator abort → receipt, no auto-resume |
| Stale lock | TTL expiry releases lock with audit entry |
| Authority | **Not** PID-file alone — token + registry state |

---

## 15. Audit log contract

Each attempt (including DENY) logs:

```text
timestamp, agent_id, operation_id, site_id, raw_path, resolved_path,
risk_class, validator_decision, dry_run_result, snapshot_id, approval_id,
execution_result, rollback_result, pre_hash, post_hash, reason_code
```

**Secrets:** never log credentials, `runtime.env`, wp-config secrets.

**Target path:** `E:\MARS-Localhost\logs\forge-wordpress\{site-id}\` (to be created in FW-07C-0/1).

---

## 16. Required enforcement components (build in FW-07C-0)

| Component | Purpose | Language | Phase |
|-----------|---------|----------|-------|
| `forge-path-validator` | Fail-closed path gate with denylist + reparse | Node.js (repo) | FW-07C-0 |
| `forge-scope-policy` | Site sandbox registry from MLI manifests | JSON + loader | FW-07C-0 |
| `forge-operation-registry` | Load `operations-v1.json` | Node.js | FW-07C-0 |
| `forge-risk-engine` | Map op_id → R0–R5 + zone rules | Node.js | FW-07C-0 |
| `forge-dry-run-runner` | Simulate mutating ops (stub in -0) | Node.js | FW-07C-0 stub |
| `forge-snapshot-manager` | Manifest IDs (stub in -0) | Node.js | FW-07C-0 stub |
| `forge-approval-gate` | Token validation (stub in -0) | Node.js | FW-07C-0 stub |
| `forge-audit-logger` | Append-only JSONL schema | Node.js | FW-07C-0 |
| `forge-kill-switch` | Global/site enable state file | JSON state | FW-07C-0 |
| `forge-negative-fixtures` | Path/op denial cases | JSON fixtures | FW-07C-0 |
| `forge-admission-validator` | G1–G15 checker CLI | Node.js | FW-07C-0 |

**Not in scope for FW-07C-0:** runtime writes, WP-CLI invocation, database connections.

---

## 17. FW-07C phase decomposition

| Phase | Allowed | Prerequisites | Exit criteria |
|-------|---------|---------------|---------------|
| **FW-07C-0** | Repo enforcement components + negative tests | This preflight | All G3–G5, G11–G14 components exist; tests pass in CI/local |
| **FW-07C-1** | Read-only local harness on fws-0001 | FW-07C-0 complete | 9 bound inspect/validate ops emit audit receipts; zero writes |
| **FW-07C-2** | Additive file ops in brain + sandbox | FW-07C-1 + snapshot stub | R1 brain drafts + controlled R1 file create with receipts |
| **FW-07C-3** | Bounded modifications R2 | Snapshot + approval live | Scoped theme/plugin edits with rollback drill |
| **FW-07C-4** | Database operations R3 | MLI backup integration | Read-only validate + chartered mutations |
| **FW-07C-5** | Remote bridge | WPilot contract | Staging read-only first |

---

## 18. Runtime/write decisions

| Question | Status |
|----------|--------|
| Can start FW-07C-0? | **YES** |
| Can start FW-07C-1? | **YES_AFTER_PRECONDITION** (FW-07C-0) |
| Can touch `E:\MARS-Localhost`? | **YES_AFTER_PRECONDITION** (read-only listing/inspect in harness) |
| Can use fws-0001? | **YES_AFTER_PRECONDITION** (FW-07C-1, synthetic only) |
| Can use shpigovsky.test? | **NO** (initial harness — pilot deferred) |
| WordPress writes? | **NO** |
| DB writes? | **NO** |
| Remote writes? | **NO** |

---

## 19. Exact next implementation task

**Task:** Implement FW-07C-0 enforcement foundation in repository only.

| Field | Value |
|-------|-------|
| Target folder | `projects/mars-website-factory/subsystems/forge-wordpress/enforcement/` |
| Components | See §16 |
| Tests | `enforcement/fixtures/negative/` + `npm test` or `node --test` |
| Runtime writes | **Prohibited** |
| Commit | `forge-wordpress: FW-07C-0 enforcement foundation` |
| Report | `# REPORT — FW-07C-0 Enforcement Foundation` |

---

## 20. Blocking issues

1. No Forge-specific path validator with reparse handling
2. Survivability validator uses legacy `C:\AI MARS` repo markers — not Phoenix canonical
3. `logs/forge-wordpress/` and admission state files not on disk
4. Zero `RUNTIME_BOUND` safeguards
5. `AG-WP-001-STATE.md` was stale (updated 2026-06-25)
6. `AG-WP-001-FILESYSTEM-SCOPE-CONTRACT` references `C:\AI MARS` — needs Phoenix path reconciliation in FW-07C-0

---

*FW-07C Safety Enforcement Preflight v1 — design complete; enforcement foundation authorized.*
