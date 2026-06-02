# OCPilot — Recommended Baseline Storage Model

**Run:** 3.6 — Baseline Storage Review (updated Run 3.7 — external root approved)  
**Status:** canonical policy — external root `C:\AI MARS STORAGE` formalized in Run 3.7.

---

## Selected model

**Option D — External baseline storage + Metadata in repo**

With one explicit operational supplement:

> **Active baseline local cache:** promoted `files/` trees for baselines marked **READY** and in active comparison use may remain on the operator workstation under `baselines/<folder>/files/`, but are **not** git-tracked.

This is Option D as canonical storage policy, not a compromise between A and C. External storage owns **canonical ZIP**; the repo owns **operational truth**; local promoted trees are a **disposable performance cache** for audit work.

---

## Decision summary

| Question | Answer |
|----------|--------|
| Keep promoted baseline trees permanently? | **On operator machine — yes for active READY baselines.** In git — **no**. On external store — **optional** pre-promoted copy for fast restore. |
| Git-track promoted trees? | **No** |
| Git-track ZIP archives? | **No** (canonical ZIP lives externally; path + checksum in passport) |
| Exclude bulk from git? | **Yes** — `files/`, `incoming/baselines/*.zip`, vendor packages, install SQL bulk |
| Externalize? | **Yes** — canonical ZIP is primary external artifact |
| Sustainable long-term? | **Yes**, with metadata in repo and bulk outside git |

---

## Justification

### 1. MARS size control

Measured state: 7608 promoted files (95.5 MB) vs 129 metadata files — bulk is **~98% of file count**. At 25 baselines, OCPilot alone approaches **~1.6 GB** ([storage-audit-run-3.6.md](storage-audit-run-3.6.md)). MARS is a multi-project documentation and pilot workspace; vendor trees must not become the default git payload.

Option A fails this constraint. Option D keeps the repo at documentation scale.

### 2. Audit usefulness

Audits need **identity, manifest, comparison notes, and readiness evidence** — all small and durable. These belong in git.

File-level diff needs a **local tree** — satisfied by operator-side promoted cache or on-demand promotion from external ZIP. Metadata in repo records **what** was promoted, **from which ZIP**, and **when** — sufficient audit chain without git-tracking 3800 PHP/JS files per baseline.

### 3. Comparison workflows

Run 3.5 proved promoted trees enable structured path-set comparison ([comparison-notes/3038-vs-3039-structured-review-v1.md](comparison-notes/3038-vs-3039-structured-review-v1.md)). Option C alone would force re-extract before every Run 5 session — unacceptable friction for active baselines.

Option D + local cache preserves Run 3.5 workflow **without** committing bulk.

### 4. Long-term maintainability

| Lifecycle stage | Storage class |
|-----------------|---------------|
| Acquisition | External ZIP + intake report |
| Verified | Passport + manifest in repo |
| READY / active comparison | Local promoted `files/` (gitignored) + metadata in repo |
| Inactive / retired | External ZIP only; delete local `files/`; update passport status |
| Re-promotion | Always from canonical ZIP ([baseline-promotion-strategy.md](baseline-promotion-strategy.md)) |

Clear classes reduce drift and duplicate retention.

### 5. Approved external storage root (Run 3.7)

| Root | Path |
|------|------|
| **MARS bulk root** | `C:\AI MARS STORAGE` |
| **OCPilot bulk root** | `C:\AI MARS STORAGE\ocpilot\` |

Registry: [external-storage-registry.md](external-storage-registry.md). Family note: [mars-storage-family-note.md](mars-storage-family-note.md).

**Repo keeps:** metadata, passports, manifests, comparison notes, reports, policies, templates.

**External storage keeps:** baseline ZIPs, promoted baseline trees (target), project site archives, file snapshots, DB snapshots, temporary extracts, backup artifacts.

**Run 3.5 grandfathering:** promoted `files/` under `projects/ocpilot/baselines/*/files/` remain temporarily as local cache — not removed in Run 3.7. Future acquisition should prefer external storage.

### 6. Operator workflow simplicity

**Simple rules for operators:**

1. **ZIP goes external** (`C:\AI MARS STORAGE\ocpilot\`) — record path and SHA256 in passport.
2. **Metadata goes in repo** — passport, manifest, database metadata, comparison notes.
3. **Promote once per baseline** to local `files/` when READY; keep while baseline is active.
4. **Never commit** `files/` or incoming ZIP to git.
5. **Re-promote from ZIP** if local tree missing or suspect — ZIP wins on conflict.

Fewer rules than maintaining full git history of vendor trees across 25+ baselines.

---

## What happens to current Run 3.5 baselines

**No removal. No relocation in Run 3.6 or Run 3.7.**

| Baseline | Action |
|----------|--------|
| `ocstore-3038-rs2` | Keep local promoted tree and incoming ZIP as-is (grandfathered local cache) |
| `ocstore-3039-rs1` | Keep local promoted tree and incoming ZIP as-is (grandfathered local cache) |

**Policy going forward:**

- New baseline ZIPs and promoted trees should land under `C:\AI MARS STORAGE\ocpilot\` per [external-storage-registry.md](external-storage-registry.md).
- Record external paths and SHA256 in passports.
- When first OCPilot git commit occurs, commit **metadata only** — not current bulk.
- Migration of existing repo-local bulk: [baseline-storage-migration-plan.md](baseline-storage-migration-plan.md) — **not executed** in Run 3.7.

Grandfathering is intentional — external root is formalized; retroactive move is a separate chartered run.

---

## Storage class diagram

```
                    ┌─────────────────────────────┐
                    │ C:\AI MARS STORAGE\ocpilot\  │
                    │  baselines\ · incoming\ · …  │
                    │  (canonical ZIP per baseline)│
                    └──────────────┬──────────────┘
                                   │
                    intake / verify │  SHA256 + path → passport
                                   ▼
┌──────────────────────────────────────────────────────────────┐
│  MARS git — projects/ocpilot/ (metadata only)               │
│  passports · manifests · database-metadata · comparison-notes│
│  readiness reports · storage policy docs · knowledge principles│
└──────────────────────────────┬───────────────────────────────┘
                               │
              promote (human)  │  active READY baselines only
                               ▼
                    ┌─────────────────────────────┐
                    │  Local operator cache        │
                    │  baselines/*/files/ (ignored)│
                    │  incoming/baselines/*.zip    │
                    │  (ignored — working copies)  │
                    └─────────────────────────────┘
```

---

## Future artifact classes (same model)

| Future content | Canonical storage | In git |
|----------------|-------------------|--------|
| Additional ocStore / OpenCart baselines | External ZIP | Metadata only |
| OpenCart 4.x baselines | External ZIP | Metadata only |
| Extension reference packages | External archive | Package manifest + notes |
| Comparison packs | External archive | Pack index + diff summary |
| Project site snapshots (Run 4+) | External or `sites/` policy TBD | Site passport + audit reports |

Extension and comparison bulk follow the same **external canonical + repo metadata** rule.

---

## Rejected alternatives (explicit)

| Option | Why rejected as canonical model |
|--------|--------------------------------|
| **A — Git track all** | Fails MARS size control; unsustainable beyond ~2–3 baselines in git |
| **C — Metadata only, no local cache** | Correct for inactive baselines but too slow as sole model for Run 5+ active comparison |
| **B alone** | Solves git size but not canonical storage or multi-machine sync — subordinate to D, not standalone |

---

## Related documents

| Doc | Role |
|-----|------|
| [git-storage-policy.md](git-storage-policy.md) | Allow/deny list for git |
| [storage-strategy-options.md](storage-strategy-options.md) | Full option evaluation |
| [storage-audit-run-3.6.md](storage-audit-run-3.6.md) | Measurements |
| [knowledge/knowledge-storage-principles.md](knowledge/knowledge-storage-principles.md) | Knowledge vs archive dump |
| [baselines/storage-policy.md](baselines/storage-policy.md) | Run 2.7 three-class model; Run 3.7 external root alignment |
| [external-storage-registry.md](external-storage-registry.md) | Approved paths and folder contract (Run 3.7) |
| [baseline-storage-migration-plan.md](baseline-storage-migration-plan.md) | Future repo → external migration |

---

## SAFE UNKNOWN

- Timeline for passport updates with external paths for grandfathered baselines — separate migration run.
- Whether incoming ZIP working copies remain under repo `incoming/baselines/` or move entirely external — operator choice during transition; both gitignored under this model.
- Multi-machine sync of `C:\AI MARS STORAGE` — operator infrastructure not defined.
