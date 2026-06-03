# MARS — Infrastructure reality (Stable Baseline 2026-06)

**Status:** **CORE**  
**Repo SoT:** `governance/mars-infrastructure-reality-v1.md`

**Is:** operator-confirmed physical workspace layout.  
**Is not:** cloud topology, NAS product choice, or proof that every bulk folder exists on disk.

---

## Canonical two-root model

| Layer | Path | Role |
|-------|------|------|
| **Active Brain (workspace)** | `C:\AI MARS` | Single git working copy — governance, registry, projects, workspaces, docs, narrow R1. All agent filesystem work stays here unless task charters otherwise. |
| **Storage layer (bulk)** | `C:\AI MARS STORAGE` | Out-of-git bulk: baselines, archives, snapshots, promoted artefacts. **Not** a second repo, **not** a second MARS instance, **not** a governance root. |

**Disambiguation:** In-repo folder `storage/` at `C:\AI MARS\storage\` is the **documentation** Storage Layer (architecture contracts) — **not** the physical path `C:\AI MARS STORAGE`.

---

## Pattern classification

| Pattern | Classification |
|---------|----------------|
| `C:\AI MARS` | **canonical** workspace root |
| `C:/AI MARS/...` | **canonical** (forward-slash variant — same root) |
| `C:\AI MARS STORAGE` | **canonical** bulk root |
| `C:\AI MARS STORAGE\ocpilot\...` | **canonical** OCPilot consumer layout |
| `C:\AI MARS\projects\ocpilot\baselines\...\files\` | **example** / migration source — grandfathered repo-local trees; target external per migration plan |
| `D:\AI MARS` | **obsolete** in-repo unless operator re-confirms |
| Drill logs with `c:\AI MARS\...` | **historical** evidence — preserve, don't rewrite |

---

## Normative rules

1. **One workspace root** — `C:\AI MARS` unless explicit task exception.  
2. **Storage is support only** — never describe `C:\AI MARS STORAGE` as second MARS repo or runtime.  
3. **Preserve history** — migration plans and drill logs may show old paths; mark historical in new docs.  
4. **SAFE UNKNOWN** — existence of storage subfolders, sync/NAS layout, per-machine mirrors — verify per session.

---

## System-specific storage pointers

| System | Metadata in repo | Bulk consumer path |
|--------|------------------|-------------------|
| OCPilot | `projects/ocpilot/external-storage-registry.md` | `C:\AI MARS STORAGE\ocpilot\` |
| EAR Runtime | `projects/ear-runtime/DECISION-EAR-RUNTIME-PLACEMENT-v1.md` | External artefacts per charter |
| Cold Brain | Operator archive root | `C:\AI MARS STORAGE\ARCHIVE` (see Brain doc) |

`.gitignore` at baseline protects OCPilot vendor bulk `baselines/**/files/**` from accidental commit.

---

## Bootstrap alignment

| Surface | Workspace | Storage |
|---------|-----------|---------|
| `AGENTS.md`, `.cursorrules` | `C:\AI MARS` | Pointer to infrastructure reality doc |
| Web-GPT packs | Distillate only | Per-system registry when bulk needed |
| Survivability safe execution | `C:\AI MARS` | External bulk via passport/task |

---

*Infrastructure Reality v1 — synchronized 2026-06-02; affirmed at Stable Baseline 2026-06.*
