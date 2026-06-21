# Audit Blockers — SITE-001 Pre–Runtime Bridge (v1)

**Scope:** Blockers to **Run 5 execution** (Phases 2–8), not to **READY FOR AUDIT** status.

---

## Primary blocker (architectural)

| ID | Blocker | Type | Resolution path |
|----|---------|------|-----------------|
| B-ARCH-01 | No **Snapshot Package** contract or acquisition layer | Architecture | EAR v1 docs + future human-chartered implementation |
| B-ARCH-02 | Run 5 paused pending **EAR / Runtime Bridge** direction | Process | Operator reviews EAR foundation; charters next phase |

---

## Evidence blockers (operational)

These block audit **findings**, not charter **readiness**.

| ID | Blocker | Severity | Unblock requires |
|----|---------|----------|------------------|
| B-EV-01 | No site `index.php` / version proof in repo or external bulk | High | P1-A version excerpts or EAR snapshot `metadata` |
| B-EV-02 | No file manifest vs baseline | High | P1-C manifest or EAR `file-manifest` |
| B-EV-03 | No optional site archive in external storage | Medium | Operator archive or EAR assisted/connected collection |
| B-EV-04 | Live theme / extension / SEO / DB facts unknown | High | Phases 4–7 evidence via snapshot sections |
| B-EV-05 | `comparison-notes/` empty for ocStore-specific methodology | Medium | Human methodology pass — parallel to EAR |

---

## Non-blockers (do not downgrade readiness)

| Item | Note |
|------|------|
| Stale access brief / site README headers | Documentation drift only |
| Empty analysis subfolders in repo | Expected until audit execution |
| Business checklist on access brief | Intent, not technical proof |

---

## Explicitly out of scope for unblock

| Item | Reason |
|------|--------|
| WPilot changes | Forbidden by task charter |
| ORCA / Website Factory / Governance edits | Forbidden |
| Autonomous site access | Forbidden — HITL remains |
| Write access to TEST or production | Out of Run 5 scope |

---

## Unblock sequence (recommended)

1. ~~**Human:** Accept EAR v1 architecture docs as Phase 1 baseline.~~ **DONE** — architecture program complete (frozen 2026-06-01); EAR Runtime Program **STARTED** (foundation only).
2. **Human:** Charter EAR Phase 2 (read-only OpenCart acquisition) — **no date implied**. Runtime R1 in progress — connector **not** implemented.
3. **Operator:** Produce first Snapshot Package for SITE-001 via Mode 0/1 until Mode 2 exists.
4. **OCPilot:** Resume Run 5 Phase 2+ against snapshot + baseline — status may move to **AUDIT IN PROGRESS** when execution starts.

---

## SAFE UNKNOWN

- Whether SITE-001 will use Mode 0 (manual files) or wait for Mode 2 connectors — operator decision.
- Timeline for first snapshot — **not** estimated in this document.
