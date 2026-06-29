# REPORT — MARS X-DRIVE MIGRATION X0–X1 ROOT AUTHORITY AND FILESYSTEM BOUNDARY

**Task date:** 2026-06-29  
**Operator authority:** physical migration to volume **AI WS** (`X:`)  
**Wave:** X0 (authority cutover) + X1 (filesystem boundary guard)

---

## 1. Result

**COMPLETE.** Canonical X-drive authority established. AGENTS.md, `.cursorrules`, Survivability registries/contracts/guardrails, and validator rules updated. Deprecated C/D/E operational roots are write-denied. Selective commit and push performed per task charter.

---

## 2. Safety Preflight

| Check | Result |
|-------|--------|
| `Get-Location` | `X:\AI MARS` |
| `Get-Volume -DriveLetter X` | Drive `X`, label **AI WS**, FS **NTFS**, Fixed |
| `X:\AI MARS` | Present (Directory) |
| `X:\AI MARS STORAGE` | Present (Directory) |
| `X:\MARS-Localhost` | Present (Directory) |
| `git rev-parse --show-toplevel` | `X:/AI MARS` |
| `git branch --show-current` | `mars/canonical-post-recovery` |
| `git rev-parse HEAD` (start) | `7ad7d7e69f19f196da59e248278cfcb767496cc7` |
| Pre-existing staged files | **None** |
| Foreign WIP | **Present — preserved and excluded from commit** |

---

## 3. Volume Identity

| Property | Value |
|----------|-------|
| Drive letter | `X:` |
| Volume label | **AI WS** — **CONFIRMED** |
| Filesystem | NTFS |
| Identity mismatch | **None** |

---

## 4. Git State

| Item | Value |
|------|-------|
| Repository root | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| Baseline HEAD | `7ad7d7e69f19f196da59e248278cfcb767496cc7` (verified descendant at task start) |
| Foreign WIP | Modified/untracked files in `workspaces/`, `projects/atlas/`, `projects/ocpilot/`, `.tools/`, etc. — **not staged** |

---

## 5. Duplicate Authority Check

| Search terms | Finding |
|--------------|---------|
| X-drive authority, AI WS, canonical MARS root, filesystem boundary | **NOT FOUND** as accepted current authority |
| `projects/mars-survivability/protocols/safe-execution-layer-v1.md` §5 | **LEGACY** — referenced `C:\AI MARS` (operational section updated) |
| Phoenix paths in AGENTS / `.cursorrules` | **LEGACY** — replaced in operational sections |

**Classification:** no competing accepted X-drive authority; no duplicate authority document created beyond `governance/mars-x-drive-root-authority-v1.md`.

---

## 6. X-Drive Root Authority

**Created:** [governance/mars-x-drive-root-authority-v1.md](../governance/mars-x-drive-root-authority-v1.md)

Contains all 18 required sections plus Guard Capability Matrix (§18 appendix).

Canonical roots:

```text
X:\AI MARS\
X:\AI MARS STORAGE\
X:\MARS-Localhost\
```

---

## 7. AGENTS.md

**Modified:** [AGENTS.md](../AGENTS.md)

- Canonical repository root: `X:\AI MARS`
- Canonical storage root: `X:\AI MARS STORAGE`
- Canonical local runtime root: `X:\MARS-Localhost`
- Required volume label: `AI WS`
- 15-point filesystem boundary rules added
- Phoenix paths retained only as historical note

---

## 8. .cursorrules

**Modified:** [.cursorrules](../.cursorrules)

- Cursor workspace root: `X:\AI MARS`
- MARS-controlled writes: `X:\` only inside approved canonical roots
- Required volume: `AI WS`
- Direct denials for deprecated roots, volume root, canonical root deletion
- Junction/symlink/reparse escape denial
- Ambiguous scope → STOP

---

## 9. Protected Roots Registry

**Modified:** [projects/mars-survivability/registries/protected-zones-registry-v1.md](../projects/mars-survivability/registries/protected-zones-registry-v1.md)

- New §0 — canonical X-drive roots with write/destructive authority table
- Deprecated C/D/E roots as DEPRECATED OPERATIONAL ROOT / WRITE DENIED
- Changelog entry 2026-06-29

---

## 10. Validator Rules

**Modified:**

- [projects/mars-survivability/tools/validator/rules/validator-rules-registry-v1.json](../projects/mars-survivability/tools/validator/rules/validator-rules-registry-v1.json)
- [projects/mars-survivability/tools/validator/scoped-operation-validator-v1.mjs](../projects/mars-survivability/tools/validator/scoped-operation-validator-v1.mjs)

Additions:

- `filesystem_boundary` section: canonical roots, denied roots, root self-protection, drive `X:`, volume label `AI WS` with `PRECHECK_REQUIRED`
- Forbidden commands: robocopy `/MIR`, `/PURGE`, rimraf, fs.rm recursive, rmdir `/s`
- Path normalization: separators, case-insensitive compare, parent escape, UNC rejection (reparse = PARTIAL)
- Validator CLI: `checkFilesystemBoundary()` for scope and extracted paths

**JSON parse:** OK

---

## 11. Survivability Contracts and Guardrails

**Modified (operational sections only):**

| File | Change |
|------|--------|
| `contracts/destructive-operations-policy-v1.md` | F-02 → X: volume/canonical root targets |
| `protocols/safe-execution-layer-v1.md` | §5 filesystem boundary + scope lock template |
| `guardrails/cursor-operational-safety-rules-v1.md` | top-level rm rule → X: roots |
| `guardrails/cursor-agent-guardrails-v1.md` | session header → X: roots + denied writes |
| `registries/enforcement-rules-registry-v1.md` | F-02 description |

**Not modified:** historical incident reports, drill evidence, release logs under `projects/mars-survivability/reports/` (except this task's new report).

---

## 12. Guard Capability Matrix

| Capability | State |
|------------|-------|
| Drive allowlist | **CONFIGURED** |
| Canonical root allowlist | **CONFIGURED** |
| Deprecated root denylist | **CONFIGURED** |
| Volume label | **PRECHECK_REQUIRED** |
| Parent traversal | **ENFORCED** (string-level) |
| UNC rejection | **ENFORCED** |
| Reparse escape | **PARTIAL** |
| Destructive command classification | **CONFIGURED** |
| Automatic interception | **NOT ENFORCED** |
| Operator approval | **REQUIRED** |
| Dry-run | **REQUIRED** |
| Checkpoint | **REQUIRED** |
| Kill switch | **DOCUMENTED** |

Full matrix: [governance/mars-x-drive-root-authority-v1.md](../governance/mars-x-drive-root-authority-v1.md) (Guard Capability Matrix appendix).

---

## 13. Historical Path Preservation

- No historical incident/recovery reports modified
- No blind mass replacement across repository
- Phoenix/C: paths may remain in foreign WIP and historical artefacts
- Operational living documents updated only in operational sections

---

## 14. Files Created

| File |
|------|
| `governance/mars-x-drive-root-authority-v1.md` |
| `reports/mars-x-drive-migration-x0-x1-root-authority-guard-v1.md` |

---

## 15. Files Modified

| File |
|------|
| `AGENTS.md` |
| `.cursorrules` |
| `projects/mars-survivability/OPERATIONAL-INDEX.md` |
| `projects/mars-survivability/registries/protected-zones-registry-v1.md` |
| `projects/mars-survivability/registries/enforcement-rules-registry-v1.md` |
| `projects/mars-survivability/contracts/destructive-operations-policy-v1.md` |
| `projects/mars-survivability/protocols/safe-execution-layer-v1.md` |
| `projects/mars-survivability/guardrails/cursor-operational-safety-rules-v1.md` |
| `projects/mars-survivability/guardrails/cursor-agent-guardrails-v1.md` |
| `projects/mars-survivability/tools/validator/rules/validator-rules-registry-v1.json` |
| `projects/mars-survivability/tools/validator/scoped-operation-validator-v1.mjs` |

---

## 16. Validation

| # | Check | Result |
|---|-------|--------|
| 1 | AGENTS.md states `X:\AI MARS` | **PASS** |
| 2 | `.cursorrules` states `X:\AI MARS` | **PASS** |
| 3 | Authority document exists | **PASS** |
| 4 | Canonical roots listed | **PASS** |
| 5 | Validator rules parse | **PASS** |
| 6 | Validator recognizes `X:\AI MARS` | **PASS** (NEED_HUMAN under `projects/` for read — task-scoped) |
| 7 | Validator recognizes `X:\AI MARS STORAGE` | **PASS** (ALLOW read) |
| 8 | Validator recognizes `X:\MARS-Localhost` | **PASS** (ALLOW read) |
| 9 | Deprecated roots denied | **PASS** (`C:\AI MARS`, `E:\MARS-Localhost` → DENY) |
| 10 | Root self-deletion denied | **PASS** (`X:\`, `X:\AI MARS` delete → DENY) |
| 11 | Historical reports unchanged | **PASS** |
| 12 | No out-of-scope programme/runtime files changed | **PASS** |

Non-destructive validator tests used inert synthetic path strings only.

---

## 17. Selective Git Scope

Staged **only** task-approved files (13 paths). Foreign WIP excluded.

---

## 18. Git Result

| Item | Value |
|------|-------|
| Commit message | `safety: establish X-drive root authority and filesystem boundary` |
| Commit SHA | `f2f7c66bf0686754cb5637e65deda01707d24ed1` |
| Branch | `mars/canonical-post-recovery` |
| Push | `git push origin mars/canonical-post-recovery` — **SUCCESS** (`7ad7d7e6..f2f7c66b`) |
| Force push | **Not used** |

---

## 19. Limitations

- Volume label **not** auto-queried by validator — operator preflight required (`PRECHECK_REQUIRED`)
- Reparse/symlink escape detection is **string-level only** (PARTIAL)
- Validator does **not** automatically block Cursor/agent commands
- README, `registry/**`, programme indexes, runtime scripts — **deferred to X2–X3**
- Many docs still contain historical `C:\MARS Phenix` paths in evidence sections (intentional)
- OS/AppData caches outside `X:` not migrated or claimed isolated

---

## 20. Drift and Risks

- Foreign WIP on branch may reference old Phoenix paths — operators must use X: authority for new work
- Validator `protected_paths` still uses repo-relative prefixes; full-path checks rely on new `filesystem_boundary` layer
- Until X2–X3, README and central registry may still mention legacy roots in non-operational sections

---

## 21. Final Status

**X0–X1 ACCEPTED.** Active MARS volume is `X:` / **AI WS**. Canonical roots published. Filesystem default-deny boundary documented and encoded in Survivability validator rules.

---

## 22. Next Wave

```text
WAVE X2–X3 —
MARS Core Infrastructure Reality, Brain Layers,
README, Registry, Topology, Roadmap and Operational Index Alignment
```

**Not started in this task.**

---

## 23. Exact Evidence Paths

| Evidence | Path |
|----------|------|
| Authority | `governance/mars-x-drive-root-authority-v1.md` |
| Agent contract | `AGENTS.md` |
| Cursor rules | `.cursorrules` |
| Protected roots | `projects/mars-survivability/registries/protected-zones-registry-v1.md` |
| Validator rules | `projects/mars-survivability/tools/validator/rules/validator-rules-registry-v1.json` |
| Validator CLI | `projects/mars-survivability/tools/validator/scoped-operation-validator-v1.mjs` |
| Operational index | `projects/mars-survivability/OPERATIONAL-INDEX.md` |
| This report | `reports/mars-x-drive-migration-x0-x1-root-authority-guard-v1.md` |

---

## 24. Stop Confirmation

```text
Volume checked: YES
Volume label AI WS: CONFIRMED
Repository root: X:\AI MARS
Files outside approved scope modified: NO
Storage modified: NO
Localhost modified: NO
Historical reports modified: NO
Foreign WIP staged: NO
Destructive operations: NONE
Commit/push: COMPLETED (see §18)
Next wave started: NO
```

---

*End of report.*
