# Runtime–Operator Canon Pattern

**Reusable scope:** Forge Proger WordPress visual-development waves  
**Evidence base:** FP-0002 E54–E63 (especially E56–E63 CSS/JS hash promotions; E63 freeze parity)  
**Project-specific hashes:** cite release docs; do not hard-code into brains

---

## 1. Durable operational pattern

During active visual development on FP-0002:

1. The **operator** often edits runtime CSS/templates/JS manually (browser-facing files under local WordPress).
2. Runtime may become **newer** than canonical Git source.
3. Every automated wave **begins** with a source ↔ runtime audit of protected files.
4. Legitimate runtime-only changes are **promoted** into source before agent mutations.
5. No broad sync of theme/plugin/ACF trees.
6. Agents **merge into latest operator files** (additive scoped edits).
7. Delivery uses **exact-file** copy with post-hash verification.
8. Checkpoint / backup **before** mutation.

At release (E63), development-time runtime canon transitions to **frozen source/runtime parity** recorded in the release manifest.

---

## 2. Why “source is always canon” failed during visual development

| Assumption | Reality on FP-0002 |
|------------|--------------------|
| Git `WORDPRESS/` is always newest truth | Operator edited runtime `v9-style.css` / `v9-shell.js` / search CSS between waves |
| Restoring last backup “fixes drift” | Older backup can **destroy newer operator work** |
| Hash match at previous freeze forever protects CSS | Operator continued editing after freezes (post–E57-FIX02, post–E62E, pre–E63) |

**Rule:** During active visual development, **current accepted runtime** outranks stale source and outranks older freezes **for files the operator is actively tuning**, unless the operator explicitly names a freeze as style authority (example: E60-FIX01 named E58 freeze for breadcrumb hover).

---

## 3. Why old backup restoration is dangerous

Restoring an older full backup (theme + DB) can:

- overwrite operator CSS that was accepted after the backup timestamp;
- reintroduce removed admin fields or FE bugs already fixed;
- create a false sense of “safety” while silently rolling back product.

Use older backups for:

- **targeted rule extraction** (copy specific selectors from a named freeze);
- rollback **only** under an explicit restore charter with operator approval;
- forensic comparison.

Do **not** use them as default “sync source.”

---

## 4. Transition at Stable release

| Phase | Authority for operator-tuned CSS/JS |
|-------|-------------------------------------|
| Active visual development | Runtime-first after audit; promote → mutate → deliver |
| Pre-release closeout (E63) | Promote latest runtime → source; verify DIFF 0; freeze both |
| Post-Stable maintenance | Treat frozen hashes as baseline; new edits restart the loop |

E63 evidence: theme DIFF 3 files before promote → 0 after; hashes recorded in `REPORTS/STABLE-V1/RELEASE-MANIFEST-FP-0002-V9-STABLE-V1.md`.

---

## 5. Standard preflight algorithm (Forge Proger)

```text
PREFLIGHT_RUNTIME_OPERATOR_CANON
1. Resolve paths: SOURCE_THEME, RUNTIME_THEME (and plugin if in scope)
2. Build protected-file list (default: v9-style.css, critical shell JS, wave-touched CSS)
3. SHA256 compare each protected file SOURCE vs RUNTIME
4. Classify each file:
   MATCH | RUNTIME_AHEAD | SOURCE_AHEAD | BOTH_DIVERGED_UNKNOWN
5. Decision:
   - MATCH → proceed
   - RUNTIME_AHEAD + edits look operator-legitimate → PROMOTE runtime→source (exact file), re-hash
   - SOURCE_AHEAD → STOP / ask operator (do not overwrite runtime blindly)
   - BOTH_DIVERGED_UNKNOWN → STOP — SAFE UNKNOWN; manual merge
6. Record operator-change-manifest.csv (before/after hashes)
7. Create checkpoint backup (scoped or full per risk)
8. Apply wave mutations only on promoted tree
9. Exact-file deliver SOURCE→RUNTIME for touched files only
10. Re-hash; unresolved product drift must be 0 for delivered set
11. Do not claim operator acceptance from hashes alone
```

### Decision tree (short)

```text
                  [source vs runtime hash]
                           |
              +------------+------------+
              |            |            |
           MATCH     RUNTIME_AHEAD  SOURCE_AHEAD / UNKNOWN
              |            |            |
           proceed     promote?      STOP / HITL
                           |
                    yes → promote → proceed
                    no  → STOP (operator)
```

---

## 6. Reusable checklist

### Before mutation

- [ ] Volume/workspace/branch preflight (MARS)
- [ ] Protected-file hash audit complete
- [ ] Promotions completed or MATCH proven
- [ ] Backup path recorded + BACKUP-OK
- [ ] Wave scope file allowlist written
- [ ] Foreign WIP identified and excluded

### During mutation

- [ ] Edit promoted files only (no parallel “clean” copy of old CSS)
- [ ] No broad robocopy MIR/PURGE
- [ ] No DB writes unless charter allows
- [ ] Preserve intentional operator rules outside scope

### After mutation

- [ ] Exact-file delivery + hash verify
- [ ] Frontend smoke for touched routes
- [ ] Screenshot/viewport evidence if visual
- [ ] Report lists preserved operator hashes
- [ ] Open tails listed (never silent)

### At freeze / Stable

- [ ] Final promote to DIFF 0
- [ ] Freeze backup + DB dump hashes
- [ ] Release manifest records protected hashes
- [ ] Rollback path documented

---

## 7. Human supervision required

- Classifying RUNTIME_AHEAD as “legitimate operator” vs “accidental runtime corruption”
- Choosing freeze-as-authority for targeted restores (E60-FIX01 pattern)
- Approving any full backup restore
- Declaring Stable parity after closeout

---

## 8. Traceability

| Lesson | Source |
|--------|--------|
| Promote-before-wave | E56, E59, E61, E62A, E63 reports |
| Operator continues after FIX | E57-FIX02 → E58 freeze hash notes in `PROJECT-STATUS.md` |
| Freeze as style authority | E60-FIX01 + E58 freeze backup |
| Final parity | E63 closeout + release manifest |
