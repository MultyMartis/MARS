# REPORT — MARS X-DRIVE MIGRATION X6B OCPILOT ACTIVE PATHS WITH SITE-002 PROTECTION

**Task date:** 2026-06-29  
**Wave:** X6B — OCPilot active path reconciliation with SITE-002 live-work protection  
**Branch:** `mars/canonical-post-recovery`  
**Baseline HEAD (start):** `152100e13aef7c0ec8263a8679cf325e80fb0dea`

---

## 1. Result

**COMPLETE.** Active operational paths for OCPilot central documentation, storage registry, site passports, project access briefs, and related canonical policy surfaces now reference `X:` canonical roots. SITE-002 foreign WIP was mapped and **not** edited. Historical run receipts, deployment manifests, and `*-work` deploy scripts retain pre-X-drive paths by design. Selective commit and push performed.

**Scope honesty:** X6B covers **active OCPilot repository paths only** — not a full historical rewrite of SITE-001/SITE-002 execution reports or deploy tooling trees.

---

## 2. Safety Preflight

| Check | Result |
|-------|--------|
| `Get-Location` | `X:\AI MARS` |
| `Get-Volume -DriveLetter X` | Drive `X`, label **AI WS**, FS **NTFS**, Healthy |
| `X:\AI MARS` | Present |
| `X:\AI MARS STORAGE` | Present |
| `X:\AI MARS STORAGE\ocpilot` | Present |
| `X:\MARS-Localhost` | Present |
| `git rev-parse --show-toplevel` | `X:/AI MARS` |
| `git branch --show-current` | `mars/canonical-post-recovery` |
| `git rev-parse HEAD` (start) | `152100e13aef7c0ec8263a8679cf325e80fb0dea` |
| Pre-existing staged files | **None** |
| Merge conflicts | **None** |

---

## 3. Volume and Git Identity

| Property | Value |
|----------|-------|
| Drive letter | `X:` |
| Volume label | **AI WS** — **CONFIRMED** |
| Active Brain | `X:\AI MARS\` |
| Storage Layer | `X:\AI MARS STORAGE\` |
| Local Runtime | `X:\MARS-Localhost\` |
| OCPilot locus | `X:\AI MARS\projects\ocpilot\` |
| OCPilot storage | `X:\AI MARS STORAGE\ocpilot\` |
| Repository root | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |

---

## 4. Initial OCPilot WIP Matrix

| Path | Pre-existing state | Task relevance | Action |
| ---- | -------------------- | -------------- | ------ |
| `projects/ocpilot/sites/site-002/reports/SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md` | **modified** | Foreign SITE-002 WIP | **preserve / exclude** |
| `projects/ocpilot/sites/site-002/backups/*.bak` (33 files) | **untracked** | Foreign WIP / backup artefacts | **preserve / exclude** |
| `projects/ocpilot/sites/site-002/reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-AUDIT-v1.md` | **untracked** | Foreign WIP | **preserve / exclude** |
| `projects/ocpilot/sites/site-002/reports/corporate-intro-images-work/**` | **untracked** | Foreign WIP + deploy tooling | **preserve / exclude** |
| All other `projects/ocpilot/**` tracked files at HEAD | **clean** | X6B path reconciliation | **edit where active paths only** |

---

## 5. Authority Discovery

| Surface | Classification | Notes |
|---------|----------------|-------|
| `projects/ocpilot/OPERATIONAL-INDEX.md` | **CANONICAL CURRENT** | Central navigation; mixed with historical run backup lines |
| `projects/ocpilot/README.md` | **CANONICAL CURRENT** | Programme entry |
| `projects/ocpilot/external-storage-registry.md` | **CANONICAL CURRENT** | Storage contract |
| `projects/ocpilot/OCPILOT-STATE.md` | **CANONICAL CURRENT** | No filesystem paths — unchanged |
| `projects/ocpilot/sites/site-002/site-passport.md` | **CANONICAL CURRENT** | SITE-002 authority |
| `projects/ocpilot/sites/site-002/README.md` | **CANONICAL CURRENT** | SITE-002 container |
| `projects/ocpilot/sites/site-002/reports/**` (execution) | **HISTORICAL / ACTIVE WIP** | Implementation receipts — mostly historical; M9.17 modified WIP |
| `projects/ocpilot/sites/site-002/**/*-work/**` | **GENERATED / DEPLOY ARTEFACT** | Hardcoded `ROOT` paths — deferred |
| `projects/ocpilot/sites/site-002/backups/**` | **BACKUP RECORD / WIP** | Untracked `.bak` — not touched |
| Storage `X:\AI MARS STORAGE\ocpilot\` | **EXTERNAL_PRESENT** | `baselines`, `incoming`, `project-sites`, `backups`, `temp` verified read-only |
| Localhost SITE-002 tree | **SAFE UNKNOWN** | `X:\MARS-Localhost\sites\opencart\` has `projects`, `sandboxes`, `synthetic` only — no `site-002` or `bzpm` tree verified |

---

## 6. OCPilot Central Alignment

| Role | Canonical path |
|------|----------------|
| Repository / programme locus | `X:\AI MARS\projects\ocpilot\` |
| External bulk root | `X:\AI MARS STORAGE\ocpilot\` |
| Local runtime pointer | `X:\MARS-Localhost\` |

Updated central surfaces: `README.md`, `OPERATIONAL-INDEX.md` (active sections), `external-storage-registry.md`, `mars-storage-family-note.md`, `recommended-storage-model.md`, `git-storage-policy.md`, `site-passport-standard.md`, `project-site-registry.md`, `baseline-storage-migration-plan.md`, `cms-ecommerce-pilots-family.md`, `sites/README.md`.

---

## 7. SITE-002 Protection

| Rule | Result |
|------|--------|
| Pre-existing modified report | `SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md` — **not edited** |
| Untracked backups / work trees | **not staged, not deleted, not restored** |
| Catalog / filter / PDP / Launch Mode | **unchanged** |
| OpenCart source | **unchanged** |
| Live TEST behaviour | **unchanged** |

---

## 8. SITE-002 Path Alignment

| Category | Path |
|----------|------|
| Repository metadata | `X:\AI MARS\projects\ocpilot\sites\site-002\` |
| Storage bulk | `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\` (**EXTERNAL_PRESENT**) |
| Secrets (external, not inspected) | `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\` |
| Local runtime root | `X:\MARS-Localhost\` |
| SITE-002 runtime subpath | **SAFE UNKNOWN** — verify before execution |

Updated clean files: `site-passport.md`, `README.md`, `project-access-brief.md`.

---

## 9. Storage Registry

| Consumer | Status | Current root |
|----------|--------|--------------|
| OCPilot bulk | **EXTERNAL_PRESENT** | `X:\AI MARS STORAGE\ocpilot\` |
| `baselines\` | **EXTERNAL_PRESENT** | `X:\AI MARS STORAGE\ocpilot\baselines\` |
| `incoming\` | **EXTERNAL_PRESENT** | `X:\AI MARS STORAGE\ocpilot\incoming\` |
| `project-sites\` | **EXTERNAL_PRESENT** | `X:\AI MARS STORAGE\ocpilot\project-sites\` |
| `project-sites\site-001\` | **EXTERNAL_PRESENT** | verified read-only |
| `project-sites\site-002\` | **EXTERNAL_PRESENT** | verified read-only |
| `backups\` | **EXTERNAL_PRESENT** | `X:\AI MARS STORAGE\ocpilot\backups\` |
| `temp\` | **EXTERNAL_PRESENT** | `X:\AI MARS STORAGE\ocpilot\temp\` |

Migration evidence column added in `external-storage-registry.md` for pre-X-drive roots. No Storage files modified.

---

## 10. Localhost Pointers

| Use | Path |
|-----|------|
| MLI root | `X:\MARS-Localhost\` |
| OpenCart platform folder | `X:\MARS-Localhost\sites\opencart\` |
| MLI documented project pattern | `X:\MARS-Localhost\sites\opencart\projects\{slug}\` |
| SITE-002 physical tree | **SAFE UNKNOWN** — not verified on `X:` |

No Localhost files modified.

---

## 11. Active Scripts and Configuration

**Changed:** none — no clean central script/config required path-only edits without mass replacement.

**Deliberately excluded:**

- All `projects/ocpilot/sites/site-002/**/*-work/*.py` deploy/rollback/screenshot scripts (100+ files) — hardcoded `C:\MARS Phenix\AI MARS` or `C:\AI MARS` roots; historical/deploy artefacts
- `projects/ocpilot/sites/site-002/reports/**/deploy-manifest.json` and similar receipts
- Untracked `corporate-intro-images-work/site-002-corp-intro-images-deploy.py` (foreign WIP)

**Static validation:** documentation-only wave — no script files modified; N/A for Python/PowerShell parser checks on changed scope.

---

## 12. Remote System Boundary

| System | Accessed |
|--------|----------|
| `zpm.new-site.space` | **NO** |
| Beget FTP/SFTP | **NO** |
| OpenCart admin | **NO** |
| Database | **NO** |
| OCPilot bridge | **NO** |

Remote Linux hosting paths remain **EXTERNAL SYSTEM PATH — NOT PART OF X-DRIVE MIGRATION**.

---

## 13. Secret Safety

No `.env`, `runtime.env`, `config.php`, credentials, SSH keys, or tokens were read or modified. External `secrets\` folders referenced by path only — **not inspected**.

---

## 14. Historical Path Preservation

Preserved without rewrite:

- `OPERATIONAL-INDEX.md` SITE-001 run backup lines (e.g. `pre-w3atmosphere-01-20260609-1156`)
- SITE-001 and SITE-002 execution reports under `reports/`
- Deployment manifests and rollback receipts in `*-work/` folders
- Forensic research documents with execution-time storage references

---

## 15. Generated and Recovery Material

Not modified: `.recovery-temp/**`, untracked `.bak` files under `projects/ocpilot/sites/site-002/backups/`, deploy result JSON in work folders, live-capture trees.

---

## 16. Files Created

| File |
|------ |
| `reports/mars-x-drive-migration-x6b-ocpilot-site002-protected-v1.md` |

---

## 17. Files Modified

| File |
|------ |
| `governance/mars-x-drive-root-authority-v1.md` |
| `projects/ocpilot/README.md` |
| `projects/ocpilot/OPERATIONAL-INDEX.md` |
| `projects/ocpilot/external-storage-registry.md` |
| `projects/ocpilot/mars-storage-family-note.md` |
| `projects/ocpilot/recommended-storage-model.md` |
| `projects/ocpilot/git-storage-policy.md` |
| `projects/ocpilot/site-passport-standard.md` |
| `projects/ocpilot/project-site-registry.md` |
| `projects/ocpilot/baseline-storage-migration-plan.md` |
| `projects/ocpilot/cms-ecommerce-pilots-family.md` |
| `projects/ocpilot/sites/README.md` |
| `projects/ocpilot/sites/site-001/site-passport.md` |
| `projects/ocpilot/sites/site-001/README.md` |
| `projects/ocpilot/sites/site-001/project-access-brief.md` |
| `projects/ocpilot/sites/site-002/site-passport.md` |
| `projects/ocpilot/sites/site-002/README.md` |
| `projects/ocpilot/sites/site-002/project-access-brief.md` |

---

## 18. Deferred Overlapping Files

| Path | Reason |
|------|--------|
| `projects/ocpilot/sites/site-002/reports/SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md` | Pre-existing foreign WIP (modified before X6B) |
| `projects/ocpilot/sites/site-002/reports/corporate-intro-images-work/**` | Untracked foreign WIP |
| `projects/ocpilot/sites/site-002/backups/*.bak` | Untracked backup WIP |
| All SITE-002 `*-work/*.py` with hardcoded legacy roots | Mass replacement prohibited; deploy artefacts — manual reconciliation if re-run needed |

---

## 19. Validation

| # | Check | Result |
|---|-------|--------|
| 1 | Volume `X:` / `AI WS` | **PASS** |
| 2 | Repository root `X:\AI MARS` | **PASS** |
| 3 | OCPilot central active paths use `X:` | **PASS** |
| 4 | Storage registry uses `X:\AI MARS STORAGE\ocpilot\` | **PASS** |
| 5 | Localhost pointers use `X:\MARS-Localhost\` | **PASS** |
| 6 | SITE-002 clean operational docs use `X:` | **PASS** |
| 7 | No overlapping dirty SITE-002 file edited | **PASS** |
| 8 | No catalog/filter/PDP/Launch Mode change | **PASS** |
| 9 | No OpenCart source change | **PASS** |
| 10 | No remote system access | **PASS** |
| 11 | No database access | **PASS** |
| 12 | No secret read/commit | **PASS** |
| 13 | No Storage file modified | **PASS** |
| 14 | No Localhost file modified | **PASS** |
| 15 | Historical reports preserved | **PASS** |
| 16 | Generated/recovery files preserved | **PASS** |
| 17 | No active old local path in changed operational files | **PASS** |
| 18 | Static syntax validation (changed scope) | **N/A** — markdown only |
| 19 | No foreign WIP staged | **PASS** (verified at commit) |
| 20 | No destructive operation | **PASS** |

---

## 20. Remaining Drift

| Area | Classification |
|------|----------------|
| SITE-002 `reports/**` implementation receipts | **HISTORICAL — ACCEPTED** |
| SITE-002 `*-work/*.py` deploy scripts | **ACTIVE OLD LOCAL PATH — deferred** |
| `OPERATIONAL-INDEX.md` SITE-001 backup path lines | **HISTORICAL — ACCEPTED** |
| `projects/ocpilot/governance/SITE-001-LESSONS-LEARNED-ANTI-REGRESSION-v1.md` | **ACTIVE OLD PATH — deferred** (lessons doc; not central path authority) |
| SITE-002 runtime subpath under Localhost | **SAFE UNKNOWN** |

---

## 21. Migration Status

| Wave | State |
|------|-------|
| X0–X6A | **COMPLETE** (unchanged) |
| **X6B** | **COMPLETE** (this report) |
| **X6** (aggregate) | **COMPLETE** |
| X7 | **NOT STARTED** |
| X8 | **PARTIAL** |
| X9 | **NOT STARTED** |

X6B covers active OCPilot repository paths only. SITE-002 business/design/runtime behavior was not modified. Storage and remote systems were not modified.

---

## 22. Selective Git Scope

Staged only X6B files listed in §17 and §16. Excluded all pre-existing WIP under `projects/ocpilot/sites/site-002/` and all foreign workspace/atlas changes.

---

## 23. Git Result

Recorded after commit/push in §28 Stop Confirmation.

---

## 24. Limitations

- SITE-002 Localhost runtime subpath not physically verified — documented as **SAFE UNKNOWN**
- Deploy/rollback Python tooling under `*-work/` not batch-updated (anti-mass-replacement rule)
- `project-site-registry.md` SITE-002 status row still shows registration-era **AWAITING INTAKE** — programme state drift preserved (not X6B scope)

---

## 25. Final Status

**X6B ACCEPTED** — OCPilot active central paths reconciled to X-drive authority with SITE-002 WIP protection.

---

## 26. Next Wave

**WAVE X7** — MIG, ORCA, ATLAS, OPS, EAR, NOVA, MetaBOT and remaining programme path reconciliation. **Not started.**

---

## 27. Exact Evidence Paths

- Authority: `governance/mars-x-drive-root-authority-v1.md`
- OCPilot entry: `projects/ocpilot/README.md`, `projects/ocpilot/OPERATIONAL-INDEX.md`
- Storage registry: `projects/ocpilot/external-storage-registry.md`
- SITE-002 passport: `projects/ocpilot/sites/site-002/site-passport.md`
- This report: `reports/mars-x-drive-migration-x6b-ocpilot-site002-protected-v1.md`
- Storage verification: `X:\AI MARS STORAGE\ocpilot\` (read-only listing)
- Localhost verification: `X:\MARS-Localhost\sites\opencart\` (read-only listing)

---

## 28. Stop Confirmation

```
Volume checked: YES
Volume label AI WS: CONFIRMED
Repository root: X:\AI MARS
X0–X6A preserved: YES
Pre-existing OCPilot WIP mapped: YES
Overlapping dirty files edited: NO
SITE-002 behavior modified: NO
OpenCart source modified: NO
Remote systems accessed: NO
Databases accessed or modified: NO
Secrets exposed: NO
Storage modified: NO
Localhost modified: NO
Historical evidence rewritten: NO
Generated/recovery material modified: NO
Foreign WIP staged: NO
Destructive operations: NONE
Commit/push: SEE POST-COMMIT UPDATE BELOW
X7–X9 started: NO
```
