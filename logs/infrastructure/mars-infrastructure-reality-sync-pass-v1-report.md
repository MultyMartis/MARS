# REPORT — MARS Infrastructure Reality Synchronization Pass v1

**Date:** 2026-06-02  
**Lane:** B (Validation / Infrastructure Reality Synchronization)  
**Baseline commits:** ac4b973, 786cea3, 3e89625 (entity / relationship / operational state sync complete)

---

## Infrastructure reality discovered

Operator-confirmed layout matches the majority of in-repo references:

- **Workspace root:** `C:\AI MARS` (git repository)
- **Bulk storage layer:** `C:\AI MARS STORAGE` (out-of-git, per-system subfolders)
- **Relationship:** storage supports bulk; governance and metadata stay in the repo

Full-path audit (`D:\AI MARS`, `C:\AI MARS`, `C:\AI MARS STORAGE`, variants) across governance, registry, projects, web-gpt-sources, AGENTS.md, README, bootstrap, migration, operational, and survivability docs.

| Finding | Count / note |
|---------|----------------|
| `D:\AI MARS` / `D:/AI MARS` | **0** matches |
| `C:\AI MARS` / `C:/AI MARS` | **~100+** files (canonical operational references) |
| `C:\AI MARS STORAGE` | **~35** files (OCPilot, EAR, shared EAR docs) |
| In-repo `storage/` folder | Architecture **documentation** layer — not physical bulk root |

---

## Canonical workspace root

**`C:\AI MARS`**

Evidence: `.cursorrules`, `AGENTS.md`, mars-v2 bootstrap packs, mars-survivability protocols, validator `repo_root_markers`, pilot tooling.

---

## Canonical storage layer

**`C:\AI MARS STORAGE`**

Evidence: [projects/ocpilot/external-storage-registry.md](../../projects/ocpilot/external-storage-registry.md), [mars-storage-family-note.md](../../projects/ocpilot/mars-storage-family-note.md), EAR placement decision, site passports.

**Not** the same as `C:\AI MARS\storage\` (doc contracts).

---

## Historical path references found

| Reference | Treatment |
|-----------|-----------|
| `D:\AI MARS` | Not present in repo — no rewrite |
| `C:\AI MARS\projects\ocpilot\baselines\...\files\` in migration plan | **Intentional** source path for future migration — kept |
| `c:\AI MARS\...` in D-01 observability drill report | **Historical** run log — kept |
| Archived ORCA / triumph migration prompts with `C:\AI MARS\...` | **Historical** freeze artefacts — kept |

---

## Documentation updates

| Change | Rationale |
|--------|-----------|
| Added [governance/mars-infrastructure-reality-v1.md](../../governance/mars-infrastructure-reality-v1.md) | Canonical infrastructure statement + reality matrix |
| Updated [README.md](../../README.md) | Operator-facing root + storage pointer |
| Updated [AGENTS.md](../../AGENTS.md) | File-ops cross-link |
| Updated [storage/README.md](../../storage/README.md) | Disambiguate doc `storage/` vs `C:\AI MARS STORAGE` |
| Updated [governance/README.md](README.md) | Index row for new doc |
| Updated [governance/onboarding-survivability.md](onboarding-survivability.md) | Optional read for physical layout |

No changes to architecture entities, relationships, maturity classifications, runtime boundaries, or governance phases.

---

## Files updated

- `governance/mars-infrastructure-reality-v1.md` (new)
- `logs/infrastructure/mars-infrastructure-reality-sync-pass-v1-report.md` (new)
- `logs/infrastructure/.gitkeep` (new, if needed for folder)
- `README.md`
- `AGENTS.md`
- `storage/README.md`
- `governance/README.md`
- `governance/onboarding-survivability.md`

---

## Remaining obsolete references

**None critical.** No `D:\` workspace root references. Residual items are **by design**:

- Repo-local OCPilot baseline trees (grandfathered; migration doc describes target external paths)
- Lowercase `c:\` in one drill report (historical evidence)
- Hardcoded `C:/AI MARS/...` in MIG n8n workflow JSON (dev-machine paths; MIG contract already warns against hardcoding in production)

---

## Risks

| Risk | Mitigation |
|------|------------|
| Confusion between `storage/` docs and `C:\ AI MARS STORAGE` | Disambiguation in `storage/README.md` + infrastructure v1 doc |
| Agent assumes bulk exists on disk | Passports/registries should state **SAFE UNKNOWN** if path not verified |
| n8n MIG workflows embed Windows paths | Operator-configured `MIG_SESSION_ROOT` per existing MIG contract |

---

## SAFE UNKNOWN

- Whether all `C:\AI MARS STORAGE\ocpilot\...` folders exist on the current machine (operator verify).
- NAS/cloud sync for storage root (documented as operator infrastructure in mars-storage-family-note).
- Any pre-repo history on `D:\` — **not evidenced** in this tree.

---

*End of pass v1 report.*
