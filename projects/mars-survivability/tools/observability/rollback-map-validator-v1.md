# Rollback Map Validator (v1)

**Status:** **documented** — human validation procedure for rollback plans.  
**Not:** rollback engine, auto-restore, or JSON schema enforcement product.

**Schema:** [rollback-map-schema-v1.json](rollback-map-schema-v1.json)  
**Guidance:** [../helpers/rollback-advisor-v1.md](../helpers/rollback-advisor-v1.md)

---

## 1. Purpose

Validate **rollback map** consistency before operator executes selective restore — using read-only observability tools and checklist discipline.

---

## 2. Rollback map structure

A rollback map is a **human-authored** JSON or markdown plan matching [rollback-map-schema-v1.json](rollback-map-schema-v1.json):

| Section | Validates |
|---------|-----------|
| `rollbackId` | Unique, dated |
| `snapshotLinkage` | Points to real `snap-*` + manifest path |
| `restoreOrdering` | Ordered steps — no skip |
| `pathConsistency` | Source/target workspaces documented |
| `quarantineReferences` | Present if contamination suspected |
| `severity` | INFO / WARNING / HIGH / CRITICAL |

Store completed maps under:

- `tools/observability/reports/rollback-map-<id>.json` (optional), or  
- `logs/rollback-history/rollback-<date>-<slug>.md` (preferred audit trail)

---

## 3. Validation procedure (operator)

### Step 1 — Snapshot linkage

1. Confirm `snapshotId` directory exists under `workspaces/_snapshots/`.  
2. Run:

```powershell
node snapshot-integrity-checker-v1.mjs --snapshot-dir "workspaces/_snapshots/<snapshotId>"
```

3. Expect **VALID** or acknowledged **WARNING** — not **INVALID**.

### Step 2 — Manifest cross-validation

```powershell
node manifest-cross-validator-v1.mjs --manifest "workspaces/_snapshots/<id>/SNAPSHOT-MANIFEST.md" --scope "<comma-separated allowlist>" --expected-snapshot-id "<id>"
```

Record status: VALID / WARNING / INVALID.

### Step 3 — Path consistency

| Check | Pass |
|-------|------|
| `targetWorkspace` matches manifest `workspace` field (or documented successor) | Yes |
| `allowedPaths` ⊆ snapshot tree | Yes |
| No `forbiddenPaths` include `_snapshots/` delete or repo root | Yes |
| Triumph v4/v5 → selective file restore only | Yes |

Use [scope-analyzer-v1.mjs](../helpers/scope-analyzer-v1.mjs) on `allowedPaths`.

### Step 4 — Restore ordering

Restore order must follow [rollback-advisor-v1.md](../helpers/rollback-advisor-v1.md):

1. Stop AGENT  
2. Quarantine if contaminated  
3. Selective copy from snapshot  
4. Verify build/lint  
5. `git diff` post-restore  
6. Append `logs/rollback-history/`

Rollback map `restoreOrdering` array must list these explicitly.

### Step 5 — Quarantine references

If scope escape or unknown file set:

- `quarantineReferences` **required**  
- `rollbackNotRecommended` may be `true` until analysis complete

### Step 6 — Log linkage

| Log | Path |
|-----|------|
| Rollback history | `logs/rollback-history/` |
| Incident (if any) | `logs/incidents/` |
| Drift (if registry issue) | `logs/survivability/` per [operational-log-format-v1.md](../../protocols/operational-log-format-v1.md) |

---

## 4. Validation outcomes

| Outcome | Meaning |
|---------|---------|
| **CONSISTENT** | All steps pass — operator may proceed |
| **GAPS** | Missing snapshot, manifest, or path docs — fill before restore |
| **BLOCKED** | INVALID manifest or contamination — quarantine-first |

**No tool auto-writes rollback maps** — operator creates and validates.

---

## 5. When NOT to validate rollback map

- Read-only audit sessions  
- Tabletop drill with no restore intent  
- Snapshot drill in `_sandbox/` only

---

## 6. SAFE UNKNOWN

- Byte-level snapshot completeness — operator verifies manually.  
- Automated JSON schema validation CLI — **planned G5**; v1 is human + existing read-only tools.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | G4 — rollback map validator v1 |

---

*End of Rollback Map Validator v1.*
