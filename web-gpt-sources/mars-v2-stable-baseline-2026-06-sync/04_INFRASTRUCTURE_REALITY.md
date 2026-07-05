# HISTORICAL / SUPERSEDED SOURCE PACK

This file belongs to the pre-X-drive historical Web-GPT source pack `mars-v2-stable-baseline-2026-06-sync`.

It MUST NOT be used to bootstrap current operational paths, current storage roots, current runtime roots, or current Cursor prompts.

Current operational authority is:

- Repo / Active Brain: `X:\AI MARS\`
- Storage: `X:\AI MARS STORAGE\`
- Local Runtime: `X:\MARS-Localhost\`
- Branch: `mars/canonical-post-recovery`
- Volume label: `AI WS`

For current Web-GPT authority, use:

- `web-gpt-sources/mars-current-x-drive-2026-06/`
- `WEB-GPT-SOURCE-PACK-INDEX.md`
- current root authority documents under `governance/`

Historical C:/D:/E: paths in this pack are evidence only.

---

# MARS — Infrastructure reality (Sync Pack 2026-06)

**Status:** **CORE**  
**Repo SoT:** `governance/mars-infrastructure-reality-v1.md`

**Is:** operator-confirmed physical workspace layout.  
**Is not:** cloud topology, NAS product choice, or proof that every bulk folder exists on disk.

---

## Canonical two-root model

> **Historical path note (this pack):** `C:\` paths in the tables below reflect the pre-X-drive sync pack at publication time. They are **superseded** by `X:\AI MARS\` and `X:\AI MARS STORAGE\` for current operational work.

| Layer | Path | Role |
|-------|------|------|
| **Active Brain (workspace)** | `C:\AI MARS` | Single git working copy — governance, registry, projects, workspaces, docs, narrow R1. All agent filesystem work stays here unless task charters otherwise. |
| **Storage layer (bulk)** | `C:\AI MARS STORAGE` | Out-of-git bulk: baselines, archives, snapshots, promoted artefacts, Knowledge Center. **Not** a second repo, **not** a second MARS instance, **not** a governance root. |

**Disambiguation:** In-repo folder `storage/` at `C:\AI MARS\storage\` is the **documentation** Storage Layer (architecture contracts) — **not** the physical path `C:\AI MARS STORAGE`.

---

## Pattern classification

| Pattern | Classification |
|---------|----------------|
| `C:\AI MARS` | **canonical** workspace root |
| `C:/AI MARS/...` | **canonical** (forward-slash variant — same root) |
| `C:\AI MARS STORAGE` | **canonical** bulk root |
| `C:\AI MARS STORAGE\ocpilot\...` | **canonical** OCPilot consumer layout |
| `C:\AI MARS STORAGE\MARS KNOWLEDGE CENTER` | **canonical** KC operator vault |
| `C:\AI MARS\projects\ocpilot\baselines\...\files\` | **example** / migration source — target external per migration plan |
| `D:\AI MARS` | **obsolete** in-repo unless operator re-confirms |

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
| Cold Brain | Operator archive root | `C:\AI MARS STORAGE\ARCHIVE` |
| Knowledge Center | `06_KNOWLEDGE_CENTER.md` (this pack) | `C:\AI MARS STORAGE\MARS KNOWLEDGE CENTER` |
| Incoming (historical bulk) | `incoming/README.md` | Toward Storage/Cold Brain **after** operator triage |

`.gitignore` protects OCPilot vendor bulk `baselines/**/files/**` from accidental commit.

---

## Factory LOC-ZONE (workspace placement)

| Attribute | Value |
|-----------|--------|
| **Path** | `workspaces/website-factory-operations/` |
| **Class** | LOC-ZONE — Authorized Records Zone |
| **Doctrine (outside zone)** | `workspaces/website-factory-reference-v1/` |
| **Role** | Factory structured records — ROC-01 catalog, FP manifests |

LOC-ZONE lives in **Active Brain** (git) — distinct from Storage bulk layer.

---

*Infrastructure Reality v1 — synchronized at Stable Baseline; affirmed post-cleanup and awareness alignment.*
