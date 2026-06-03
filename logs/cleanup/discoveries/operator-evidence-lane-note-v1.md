# Operator Evidence Lane Note v1

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 2A  
**Upstream:** [wave-2-cross-system-review-v1.md](wave-2-cross-system-review-v1.md) §3  
**Mode:** Pure documentation note — **not** a subsystem, **not** runtime, **not** new architecture.

---

## Observed relationship (documentation)

Four existing surfaces cooperate in human-operated MARS work without sharing a single folder or engine:

```text
Incoming          →  untrusted external drops / transport
        ↓ promote (human)
IdeaBox           →  trusted session capture (continuity/)
        ↓ incubate (human, optional)
GitGuard          →  survivability advisory + helpers (mars-survivability)
        ↓ protect paths / pre-destructive checks
Lifecycle Log     →  governance events recorded (append-only)
        ↓ audit trail
Registry / projects / governance SoT
```

| Step | Surface | Canonical path |
|------|---------|----------------|
| 1 | **Incoming** | `incoming/**`, program-scoped `projects/*/incoming/` |
| 2 | **IdeaBox** | `continuity/**` |
| 3 | **GitGuard** | `projects/mars-survivability/**` (concept + tools) |
| 4 | **Lifecycle** | `logs/lifecycle-log.md` |
| 5 | **Registry** | `registry/project-registry.md` |

---

## What this is not

| Claim | Status |
|-------|--------|
| A MARS subsystem or `project_id` | **No** — not registered, not implemented |
| A runtime or orchestration lane | **No** — human-gated only |
| A replacement for cleanup program | **No** — `logs/cleanup/` remains investigation evidence |
| Mandatory workflow engine | **No** — observed pattern for operator training |

Wave 2 Discovery explicitly deferred **implementing** this as a product; Wave 2A only documents the observation for navigation.

---

## Differentiation (anti-conflation)

| Risk | Resolution |
|------|------------|
| Incoming vs IdeaBox | Incoming = **untrusted** artefacts; IdeaBox = **authored** session notes |
| GitGuard vs GIT CHECKPOINT signal | GitGuard = survivability pack; checkpoint signal = rare commit discipline |
| Lifecycle vs cleanup logs | Lifecycle = governance **events**; cleanup = census **evidence** |
| Registry vs lifecycle | Registry = **current** row; lifecycle = **when** it changed |

---

## Related evidence

- [incoming/README.md](../../incoming/README.md) — ecosystem intake policy (Wave 2A)
- [lifecycle-backfill-review-v1.md](../actions/lifecycle-backfill-review-v1.md)
- [gitguard-crosslink-alignment-v1.md](../actions/gitguard-crosslink-alignment-v1.md)
- [lifecycle-log-deep-review-v2.md](lifecycle-log-deep-review-v2.md)
- [gitguard-deep-review-v2.md](gitguard-deep-review-v2.md)
- [ideabox-deep-review-v2.md](ideabox-deep-review-v2.md)
- [incoming-deep-review-v2.md](incoming-deep-review-v2.md)

---

*Operator Evidence Lane note v1 — observational documentation only.*
