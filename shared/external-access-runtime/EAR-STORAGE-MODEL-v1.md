# EAR Storage Model v1

**Purpose:** Conceptual model of **where** snapshots live across roles — repository, external storage, archive, and consumer access.  
**Status:** architecture specification — **no** paths, volumes, cloud products, or implementation.  
**Phase:** 2B  

---

## Design principle

Snapshots are **evidence packages**, not live connections. Storage separates:

1. **What may appear in git** (contracts, references, small manifests)
2. **What must stay external** (bulk, secrets)
3. **What consumers read** (published references only)

---

## Storage roles

```
┌─────────────────────────────────────────────────────────────────┐
│  Repository (MARS / consumer repos)                              │
│  • Specs, indexes, REPORTs                                      │
│  • Optional contract slice copies — no secrets                    │
└────────────────────────────┬────────────────────────────────────┘
                             │ references
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  External storage (operator-controlled)                          │
│  • Bulk payloads, large manifests, archives                       │
│  • Acquisition registry (optional) — SAFE UNKNOWN location       │
│  • secrets/ — never part of snapshot package                      │
└────────────────────────────┬────────────────────────────────────┘
                             │ published reference
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  Consumer workspace (read-only intake)                           │
│  • Published snapshot contract slice + bulk refs                  │
│  • Analysis outputs in consumer-owned paths                       │
└────────────────────────────┬────────────────────────────────────┘
                             │ supersession / policy
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  Archive tier (operator-controlled)                              │
│  • Retired snapshots; citeable from historical reports             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Repository role

| Responsibility | Owner |
|----------------|-------|
| EAR architecture and workflow docs | MARS `shared/external-access-runtime/` |
| Snapshot **contract** definitions | EAR specs (Phase 2A) |
| Optional small metadata copies for traceability | Operator policy — **not required** |
| Consumer reports and baselines | Consumer project (e.g. OCPilot) |

**Must not store in repository (git-bound):**

- Raw passwords, tokens, connection strings
- Full database dumps with PII
- Unredacted bulk trees unless explicitly chartered and reviewed

**EAR behavior:** Metadata may include `bulk_root` as opaque reference string — not a secret.

---

## External storage role

| Storage class | Contents | Typical owner |
|---------------|----------|---------------|
| **Contract slice** | Metadata, manifests, inventories, `safe-unknown`, logs | Operator + EAR assembly |
| **Bulk payload** | ZIP trees, large XML bodies, full path manifests | Operator placement |
| **Secrets** | FTP, SSH, DB credentials | Operator `secrets/` — **outside** snapshot |

**Lifecycle placement:**

| Stage | External storage use |
|-------|----------------------|
| Acquire | Candidate may live in staging area (operator-defined) |
| Validate | Candidate reviewed in place or copied — no consumer access |
| Store | Immutable placement per `snapshot_id` |
| Publish | Consumer receives reference to stored location |
| Archive | Move or re-tier bulk; logical `snapshot_id` unchanged |

**SAFE UNKNOWN:** Exact host, bucket, or folder naming — operator choice; not specified in EAR v1.

---

## Archive role

| Aspect | Definition |
|--------|------------|
| **Purpose** | Long-term retention after supersession or audit closure |
| **Mutability** | Archive is **not** active publish target; corrections = new `snapshot_id` |
| **Deletion** | Operator policy only — not EAR-automated |
| **Consumer** | May read archived snapshot if reference retained; default workflows use latest published |

**Triggers:** Newer snapshot supersedes; site audit closed; retention elapsed — per [EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md).

---

## Consumer role

| Aspect | Definition |
|--------|------------|
| **Access type** | Read-only to **published** snapshot |
| **Typical layout** | Consumer registry (e.g. OCPilot `snapshots/` external to git) — **conceptual only** |
| **Writes** | Reports, diffs, findings — consumer-owned paths |
| **Must not** | Write back to snapshot; store credentials in git |

Consumer storage is **downstream** of Publish — see [EAR-SNAPSHOT-PUBLISHING-v1.md](EAR-SNAPSHOT-PUBLISHING-v1.md).

---

## Immutability convention

| Event | Rule |
|-------|------|
| Post-Store | Artifacts for `snapshot_id` are not overwritten |
| Fix error | New acquisition → new `snapshot_id` |
| Metadata typo after Publish | Prefer superseding snapshot; in-place edit **discouraged** |

---

## OCPilot alignment (documentation)

| Concept | OCPilot (planned) |
|---------|-------------------|
| Published intake | External `snapshots/` per consumer registry — **SAFE UNKNOWN** exact path |
| Baselines | Consumer repo (`ocstore-3038-rs2`) — not EAR |
| SITE-001 bulk | Operator external bulk — reference in `bulk_root` |

No implementation claimed.

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-SNAPSHOT-LIFECYCLE-v1.md](EAR-SNAPSHOT-LIFECYCLE-v1.md) | Store stage (Phase 2A) |
| [EAR-SECURITY-MODEL-v1.md](EAR-SECURITY-MODEL-v1.md) | Secrets placement |
| [EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md) | Package sections |

---

## SAFE UNKNOWN

- Checksum registry, WORM, encryption standards
- Whether contract slice is copied into consumer repo vs referenced only
- Central MARS snapshot catalog
