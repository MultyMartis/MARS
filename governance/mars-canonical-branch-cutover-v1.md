# MARS Phoenix — Permanent canonical branch cutover v1

**Status:** **documented** — operator-authoritative branch authority record after Phoenix recovery finalization.
**Date:** 2026-06-25
**Is not:** legacy tree archival, STORAGE migration, runtime validation, or GitHub default-branch change.

---

## Incident and reconstruction summary

| Field | Value |
|-------|-------|
| **Incident date** | 2026-06-24 |
| **Phoenix reconstruction** | Validated tree at `C:\MARS Phenix\AI MARS` |
| **Recovery branch** | `recovery/mars-phenix-2026-06-25` |
| **Verified recovery anchor** | `fe9d9c8e52edd2632de15dcc5ee5d353d8660362` |
| **Branch cutover date** | 2026-06-25 |

Full recovery and path cutover context: [mars-phoenix-recovery-cutover-receipt-v1.md](mars-phoenix-recovery-cutover-receipt-v1.md).
Branch integration decision (Strategy B): [mars-phoenix-branch-integration-decision-v1.md](mars-phoenix-branch-integration-decision-v1.md).

---

## Canonical authority (post-cutover)

| Layer | Path / ref | Role |
|-------|------------|------|
| **Canonical git repository** | `C:\MARS Phenix\AI MARS` | MARS brain — governance, projects, workspaces, docs |
| **Canonical development branch** | `mars/canonical-post-recovery` | Active development line after recovery |
| **Branch creation anchor** | `fe9d9c8e52edd2632de15dcc5ee5d353d8660362` | Direct pointer from verified recovery HEAD — no merge |
| **Canonical bulk storage** | `C:\MARS Phenix\AI MARS STORAGE` | Out-of-git bulk — baselines, archives, large assets |
| **Localhost runtime** | `E:\MARS-Localhost` | Shared Windows local web runtime — **not** Git authority |

**Mandatory formulation (MLI):**

```text
C:\MARS Phenix\AI MARS governs.
E:\MARS-Localhost executes.
```

---

## Branch roles

| Branch | SHA (anchor) | Classification |
|--------|--------------|----------------|
| `mars/canonical-post-recovery` | `fe9d9c8e` (initial); advances on canonical commits | **ACTIVE_CANONICAL_DEVELOPMENT_BRANCH** |
| `recovery/mars-phenix-2026-06-25` | `fe9d9c8e52edd2632de15dcc5ee5d353d8660362` | **IMMUTABLE_RECOVERY_ANCHOR** |
| `mars/post-cycle8-live-tests` | `f78af433` (remote legacy forward) | **LEGACY_FORWARD_BRANCH_DO_NOT_MERGE** |
| `main` | `219d609a` (remote) | **EXISTING_REPOSITORY_DEFAULT_OR_HISTORICAL_LINE** — unchanged |

---

## Rejected integration methods

| Method | Status |
|--------|--------|
| Merge recovery into `mars/post-cycle8-live-tests` | **REJECTED / DEFERRED** |
| Rebase recovery onto forward line | **REJECTED** |
| Cherry-pick forward commits onto recovery | **REJECTED** |
| Force-push legacy forward to recovery state | **REJECTED** |
| GitHub default branch change | **NOT EXECUTED** — operator decision later |

Canonical branch was created with `git switch -c mars/canonical-post-recovery` from recovery HEAD. **No new commit** at branch creation.

---

## Recovery branch immutability rule

`recovery/mars-phenix-2026-06-25` is a **fixed recovery anchor** at `fe9d9c8e52edd2632de15dcc5ee5d353d8660362`.

**Forbidden on recovery branch:**

- Direct commits
- Force-push
- Rebase
- Branch deletion
- Branch pointer movement
- Merge into recovery

**Further development** proceeds only on `mars/canonical-post-recovery` or feature branches created from it.

---

## Legacy and evidence boundaries

| Tree / branch | Status |
|---------------|--------|
| `C:\AI MARS` | `LEGACY_READ_ONLY_HOLD` — not canonical working copy |
| `C:\this is backUP AI MARS 23.06.2026` | `PERMANENT_IMMUTABLE_BACKUP` |
| `mars/post-cycle8-live-tests` | Legacy forward line — comparison and historical reports only |

Do not delete, rename, or archive legacy branches or trees without a separate operator charter.

---

## Operator workflow (current)

1. Clone or work from `C:\MARS Phenix\AI MARS`.
2. Checkout `mars/canonical-post-recovery` for active development.
3. Create feature branches from canonical line as needed.
4. Treat `recovery/mars-phenix-2026-06-25` as read-only forensic anchor.
5. Do not use `C:\AI MARS` checkout as branch SHA authority.
6. GitHub default branch remains `main` until explicitly changed by operator.

---

## Rollback / reference boundaries

- **Recovery anchor rollback:** reference `recovery/mars-phenix-2026-06-25` @ `fe9d9c8e` — do not rewrite recovery pointer.
- **Pre-cutover forward history:** `mars/post-cycle8-live-tests` @ remote `f78af433` — historical only.
- **Control artefacts:** `C:\MARS Phenix\_reconstruction-control\` (out-of-repo manifests, checkpoints, reports).

---

## Related authority

| Topic | Path |
|-------|------|
| Infrastructure reality | [mars-infrastructure-reality-v1.md](mars-infrastructure-reality-v1.md) |
| Recovery cutover receipt | [mars-phoenix-recovery-cutover-receipt-v1.md](mars-phoenix-recovery-cutover-receipt-v1.md) |
| Branch integration decision | [mars-phoenix-branch-integration-decision-v1.md](mars-phoenix-branch-integration-decision-v1.md) |
| Control reports | `C:\MARS Phenix\_reconstruction-control\reports\` |

---

*Permanent canonical branch cutover v1 — branch authority established 2026-06-25.*
