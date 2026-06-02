# EAR Acquisition Selection Guide v1

**Purpose:** Decision guide — map project facts and operator answers to **Offline**, **Connected**, or **Hybrid** acquisition track.  
**Status:** architecture / process — **no** automation or implementation.  
**Phase:** 2E  
**Parent:** [EAR-ACQUISITION-TRACKS-v1.md](EAR-ACQUISITION-TRACKS-v1.md)

---

## How to use this guide

1. Answer the **decision questions** below honestly (repository facts + operator confirmation).
2. Apply the **scoring table** — no single question is sufficient alone.
3. Record the chosen track on the **Request** artifact and in snapshot metadata when published.
4. If **Hybrid**, document which legs are Offline vs Connected and expected snapshot levels per leg.

**This guide does not authorize live access.** Connected selection still requires channel charter, credentials, and Phase 3+ runtime charter where applicable.

---

## Decision questions

| # | Question | If **Yes** tends toward… | If **No** tends toward… |
|---|----------|---------------------------|-------------------------|
| Q1 | Do **approved read-only access channels** exist (SFTP, SSH, PMA, Admin, …)? | **Connected** | **Offline** |
| Q2 | Is this a **one-time** audit with no planned recurrence? | **Offline** | **Connected** or **Hybrid** |
| Q3 | Is the project **actively maintained** (ongoing support, Run N audits)? | **Connected** | **Offline** |
| Q4 | Will **recurring snapshots** be required (baseline drift, extension changes)? | **Connected** or **Hybrid** | **Offline** |
| Q5 | Will **future operations** (support tickets, regression audits) use the same `site_id`? | **Connected** / **Hybrid** | **Offline** |
| Q6 | Is evidence available only as **client/hosting archives** (no live login)? | **Offline** | **Connected** |
| Q7 | Is **connector runtime** chartered and available? | **Connected** | **Offline** (Mode 0/1) until charter |
| Q8 | Is a **fresh live manifest** required for Level 2–3 extension/ocMod proof? | **Connected** or **Hybrid** | **Offline** (if archives sufficient) |
| Q9 | Are **credentials forbidden** or unavailable by policy? | **Offline** | **Connected** |
| Q10 | Does consumer need **structured `acquisition-log`** from live channels? | **Connected** | **Offline** acceptable |

---

## Quick outcomes (examples)

| Scenario | Recommended track | Typical EAR mode |
|----------|-------------------|------------------|
| Legacy ZIP + SQL dump, no hosting access | **Offline** | 0 |
| Client package one-off audit | **Offline** | 0 or 1 |
| SITE-001 Run 5, channels confirmed, no runtime yet | **Offline** or **Hybrid** (offline first) | 0/1 now; Connected when pilot |
| SITE-001 recurring support, connector chartered | **Connected** | 2 |
| Initial ZIP baseline, then quarterly SFTP audit | **Hybrid** | 0/1 then 2 |
| Beget backup only for first publish, SFTP later for L2 | **Hybrid** | 1 → 2 |

---

## Mapping matrix

| Pattern | Offline signals | Connected signals | Result |
|---------|-----------------|-------------------|--------|
| **A** | Q6 Yes, Q1 No, Q2 Yes | — | **Offline** |
| **B** | — | Q1 Yes, Q3 Yes, Q4 Yes, Q7 Yes | **Connected** |
| **C** | Q6 Yes (baseline) | Q4 Yes, Q5 Yes (later) | **Hybrid** |
| **D** | Q2 Yes, Q9 Yes | Q1 Yes but unused | **Offline** (do not connect “because channels exist”) |
| **E** | Q7 No | Q1 Yes, Q3 Yes | **Offline** until runtime charter; plan **Hybrid** transition |

---

## Offline — select when

- Archives or exports are the **only** or **preferred** evidence source.
- One-time audit; no recurring snapshot charter.
- No-access, legacy, or client-delivered package engagement.
- Connector runtime **not** approved — use Mode 0/1 per [EAR-OFFLINE-ACQUISITION-v1.md](EAR-OFFLINE-ACQUISITION-v1.md).

**Do not select Offline when:** recurring live deltas are required **and** Connected is chartered and available — operator toil will dominate.

---

## Connected — select when

- Active managed project (SITE-001, BZPM, dealership support).
- Recurring read-only snapshots with stable channels.
- Target Level 2–3 with repeatable connector scope.
- Phase 3+ pilot or runtime explicitly chartered.

**Do not select Connected when:** only archives exist, or write access is needed (non-EAR), or no HITL/credential path.

---

## Hybrid — select when

| Hybrid pattern | Description |
|----------------|-------------|
| **H1 — Baseline + refresh** | Offline Level 1 from backup; Connected Level 2+ for extension pass |
| **H2 — Gap fill** | Connected partial fails DB leg; Offline PMA export completes snapshot |
| **H3 — Compare** | Two snapshots (offline stale vs connected fresh) for consumer diff — explicit charter |
| **H4 — Transition** | Project moves from archive-only to managed hosting mid-engagement |

**Rules:**

- Each leg gets its own **`snapshot_id`** unless future merge policy is chartered (**SAFE UNKNOWN** today).
- Record `acquisition_track`: `hybrid` on snapshots that are part of a documented multi-leg plan.
- Consumer compares snapshots only when analysis charter allows — see [EAR-OCPILOT-INTEGRATION-v1.md](EAR-OCPILOT-INTEGRATION-v1.md).

---

## Relation to EAR modes

| Track | Mode selection |
|-------|----------------|
| Offline | Mode **0** (minimal) or **1** (guided checklist) |
| Connected | Mode **2** only (read-only) |
| Hybrid | **0/1** and **2** on different acquisition cycles |

Mode 3 (read-write): **never** — stop at Request.

---

## SITE-001 worked example (documentation only)

| Fact (repo) | Implication |
|-------------|-------------|
| Multiple channels theoretically available | Connected **eligible** when operator confirms |
| Run 5 paused; no runtime | **Offline** or **Hybrid** offline-first **now** |
| Ongoing test site / consumer Run 5 | **Connected** is **strategic target** |

See [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](EAR-SITE-001-ACQUISITION-OPTIONS-v1.md) — **not** execution authority.

---

## Escalation

| Condition | Action |
|-----------|--------|
| Answers split evenly | Prefer **Offline** for first snapshot; charter Connected second leg |
| Write access requested | **Stop** — non-EAR |
| Quality target unreachable on chosen track | Downgrade level + `safe-unknown`; do not switch track without new Request |

---

## SAFE UNKNOWN

- Automated track recommendation tool — not in Phase 2E.
- Org-wide default track per consumer — not frozen (see [EAR-FUTURE-CONSUMERS-v1.md](EAR-FUTURE-CONSUMERS-v1.md) preferences as guidance only).

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-OFFLINE-PATHS-v1.md](EAR-OFFLINE-PATHS-v1.md) | Offline path recipes |
| [EAR-CONNECTED-PATHS-v1.md](EAR-CONNECTED-PATHS-v1.md) | Connected path recipes |
| [EAR-PHASE-2E-DESIGN-DECISIONS-v1.md](EAR-PHASE-2E-DESIGN-DECISIONS-v1.md) | DD-2E-01–04 |
