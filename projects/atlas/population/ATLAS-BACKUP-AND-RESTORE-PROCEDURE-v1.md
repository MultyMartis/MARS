# ATLAS Backup and Restore Procedure v1

**Status:** **documented** — operator backup / restore discipline for Atlas documentation and evidence.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-BACKUP-SNAPSHOT-v1.md](ATLAS-BACKUP-SNAPSHOT-v1.md) · [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) · [ATLAS-OPERATIONAL-MODEL-v1.md](../foundation/ATLAS-OPERATIONAL-MODEL-v1.md)  
**Is not:** automated backup job, CI pipeline, cloud DR contract, runtime database backup.

---

## 1. Purpose

Define **what to copy**, **where it lives**, and **in what order to restore** Atlas registry state before major population or attestation work.

Atlas state is **documentation-only** in Phase 1 — no in-repo runtime or database. A complete backup spans:

1. **Repository tree** — normative foundation + population registers under git.
2. **External storage tree** — Counterparty Card evidence and future bulk artifacts **outside git**.

---

## 2. Backup scope

### 2.1 Repository backup

**Root:**

```text
X:\AI MARS\projects\atlas\
```

**Required subfolders:**

| Folder | Contents | Backup priority |
|--------|----------|-----------------|
| `foundation\` | Identity, lifecycle, attestation, taxonomy, governance models | **Critical** |
| `population\` | Wave registers, attestation acts, population plans, snapshots | **Critical** |
| `audit\` | Foundation audits, gap analysis, risk register | **Recommended** |

**Operator action:** Copy entire `projects\atlas\` tree to dated archive **or** rely on git history for repository portion. For pre-population checkpoints, prefer **both** git tag (operator-initiated) **and** filesystem copy.

**Exclude from manual copy (regenerate if needed):** none required at Phase 1 — all markdown/xlsx under `atlas\` are source artifacts.

---

### 2.2 Storage backup

**Root:**

```text
X:\AI MARS STORAGE\atlas\
```

**Required folders (normative layout):**

| Folder | Role | Current state (2026-06-07) |
|--------|------|----------------------------|
| `foundation\` | Optional mirror / bulk foundation exports | **Not present** — repo is SoT for foundation |
| `population\` | Optional mirror / bulk population exports | **Not present** — repo is SoT for population |
| `evidence\` | Evidence artifacts (CC, future tiers) | **Present** |
| `evidence\counterparty-cards\` | Organization Counterparty Cards | **Present** |

**Operator action:** Copy entire `X:\AI MARS STORAGE\atlas\` recursively to dated external archive (second disk, NAS, or encrypted cloud — operator choice).

**Critical subpaths at snapshot:**

```text
X:\AI MARS STORAGE\atlas\evidence\counterparty-cards\
├── README.md
├── bzpm\
├── i-seo\
├── metacode\
├── metallka\
├── moscow-serm\
├── polygon\
├── sibcar\
└── triumph\
```

**Rule:** Counterparty Card files **must not** be committed to git. Storage backup is **mandatory** for evidence recovery.

---

## 3. Backup procedure (operator checklist)

| Step | Action | Verify |
|------|--------|--------|
| **B-01** | Record snapshot metadata — date, steward, reason (e.g. pre-population) | [ATLAS-BACKUP-SNAPSHOT-v1.md](ATLAS-BACKUP-SNAPSHOT-v1.md) or successor |
| **B-02** | Copy `X:\AI MARS\projects\atlas\` → `{archive}\atlas-repo-{YYYYMMDD}\` | File count matches source |
| **B-03** | Copy `X:\AI MARS STORAGE\atlas\` → `{archive}\atlas-storage-{YYYYMMDD}\` | CC folders present |
| **B-04** | Optional: create git tag `atlas-backup-YYYYMMDD` on current commit | `git tag -l atlas-backup-*` |
| **B-05** | Write one-line entry to operator log / lifecycle log | Traceability |
| **B-06** | Confirm archive readable (spot-open 2–3 CC files + 2 register md files) | Read test |

**Frequency recommendation:** Before each major population wave, attestation tranche, or canonical rename.

---

## 4. Restore sequence

Restore **storage first**, then **repository**, then **verify cross-references**.

```text
1. Storage evidence restore
        ↓
2. Repository documentation restore
        ↓
3. Cross-reference verification
        ↓
4. Steward sign-off — safe to resume population
```

### 4.1 Step 1 — Restore storage

| Order | Path | Action |
|-------|------|--------|
| 1.1 | `X:\AI MARS STORAGE\atlas\evidence\counterparty-cards\` | Restore all org subfolders + README |
| 1.2 | `X:\AI MARS STORAGE\atlas\evidence\` | Restore any additional evidence tiers if present in archive |
| 1.3 | `X:\AI MARS STORAGE\atlas\population\` | Restore only if archive contains mirrored exports |
| 1.4 | `X:\AI MARS STORAGE\atlas\foundation\` | Restore only if archive contains mirrored exports |

**Gate:** CC paths cited in attestation acts must resolve on disk ([ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md)).

### 4.2 Step 2 — Restore repository

| Order | Path | Action |
|-------|------|--------|
| 2.1 | `X:\AI MARS\projects\atlas\foundation\` | Restore or checkout from git tag / archive |
| 2.2 | `X:\AI MARS\projects\atlas\population\` | Restore registers + attestation acts + snapshots |
| 2.3 | `X:\AI MARS\projects\atlas\audit\` | Restore if available |

**Gate:** [ATLAS-FOUNDATION-INDEX-v1.md](../foundation/ATLAS-FOUNDATION-INDEX-v1.md) entry paths must resolve.

### 4.3 Step 3 — Cross-reference verification

| Check | Method |
|-------|--------|
| Org count vs snapshot | Compare [ATLAS-BACKUP-SNAPSHOT-v1.md](ATLAS-BACKUP-SNAPSHOT-v1.md) |
| CC path citations | Grep population docs for `AI MARS STORAGE\atlas` — paths must exist |
| Active attestation lineage | ORG/LE/PER/REL registers consistent with latest attestation acts |
| Rename / correction history | Identity correction + rename docs not orphaned |

### 4.4 Step 4 — Steward sign-off

Document restore completion: date, archive source, verification checklist result, residual **SAFE UNKNOWN** items.

**Do not** resume population attestation until Steps 1–3 pass.

---

## 5. Partial restore scenarios

| Scenario | Restore |
|----------|---------|
| Lost CC files only | Storage §4.1 only |
| Lost population registers only | Repository `population\` §4.2.2 |
| Lost foundation docs only | Repository `foundation\` §4.2.1 |
| Full machine rebuild | Complete §4.1 + §4.2 |

---

## 6. Coverage summary (2026-06-07 baseline)

| Surface | Path | Files / folders (approx.) | In git? |
|---------|------|----------------------------|---------|
| Foundation docs | `projects\atlas\foundation\` | ~40 md | Yes |
| Population docs | `projects\atlas\population\` | ~45 md + 1 xlsx | Yes |
| Audit docs | `projects\atlas\audit\` | ~4 md | Yes |
| CC evidence | `STORAGE\atlas\evidence\counterparty-cards\` | 8 org folders + README | **No** |
| Storage mirrors | `STORAGE\atlas\foundation\`, `population\` | Not deployed | N/A |

---

## 7. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-BACKUP-SNAPSHOT-v1.md](ATLAS-BACKUP-SNAPSHOT-v1.md) | Entity counts + active roster at checkpoint |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | CC placement rules |
| [ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md) | Latest identity change before this backup baseline |

---

*ATLAS Backup and Restore Procedure v1 — documentation only.*
