# FP-0003 — OVERSEO (overseo.ru)

**Factory Project ID:** FP-0003  
**Project name:** OVERSEO  
**Domain:** `overseo.ru`  
**LOC-ZONE:** `workspaces/website-factory-operations/FP-0003-OVERSEO/`  
**Registered:** 2026-08-20  
**Charter:** FP-0003 Phase 0B — Project Registration + Materials Intake Skeleton  

---

## Project identity

| Field | Value |
|-------|-------|
| Factory Project ID | **FP-0003** |
| Canonical project name | **FP-0003-OVERSEO** |
| Primary domain | **overseo.ru** |
| Client / owner context | Olga (coordination; materials intake) |
| Process precedent | FP-0002 Shpigovsky — **lifecycle only**; not an implementation template |

---

## Current phase

**PHASE 0B — PROJECT REGISTERED / MATERIALS INTAKE READY**

See [PROJECT-STATUS.md](PROJECT-STATUS.md) for live status.  
Passport: [FP-0003-PROJECT-PASSPORT.md](FP-0003-PROJECT-PASSPORT.md).

**Next gate:** **PHASE 1 — MATERIALS INTAKE & CREATIVE BRIEF**

---

## Lifecycle intent (documented)

```text
Olga materials intake
  → creative / structural analysis
  → homepage design (screen-by-screen)
  → operator / Olga approval
  → Gulp frontend
  → responsive approval
  → CMS architecture
  → Forge WordPress
  → production QA / handoff / operations
```

This wave establishes **identity and intake only**. No design, frontend, WordPress, or production work has started.

---

## Canonical paths

| Role | Path | Status |
|------|------|--------|
| **LOC-ZONE (this tree)** | `X:\AI MARS\workspaces\website-factory-operations\FP-0003-OVERSEO\` | **ACTIVE** |
| **Future frontend workspace** | `X:\AI MARS\workspaces\fp-0003-overseo-v1\` | **NOT CREATED** — reserved for post-design approval |
| **Future local runtime domain** | `overseo.test` | **NOT CREATED** — reserved for post-frontend + CMS architecture |
| **Bulk intake drop (Storage)** | `X:\AI MARS STORAGE\incoming\overseo.ru\` | **DOCUMENTED ONLY** — not created in Phase 0B |

---

## Production mode

**`production_mode = PIXEL_PERFECT`** — declared in passport ([FP-0003-PROJECT-PASSPORT.md](FP-0003-PROJECT-PASSPORT.md)).

Frontend work (when authorized) must reproduce **operator-approved** visual targets produced screen-by-screen in the design wave. Olga's current rough mockup is **source material**, not the approved pixel-perfect target.

**Contract:** [FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md](../FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md) · [website-factory-production-modes-charter-v1.md](../../../projects/mars-website-factory/website-factory-production-modes-charter-v1.md)

---

## Materials intake

Two-stage model:

1. **Bulk drop (outside Git):** `X:\AI MARS STORAGE\incoming\overseo.ru\` — large originals, exports, archives.
2. **Promoted project intake (Git-tracked pointers and curated copies):** [INCOMING/](INCOMING/)

| Folder | Purpose |
|--------|---------|
| [INCOMING/01_DESIGN/](INCOMING/01_DESIGN/) | Rough mockup, homepage screenshots, visual drafts, design references |
| [INCOMING/07_NOTES/](INCOMING/07_NOTES/) | Telegram excerpts, operator/client thoughts, coordination notes |
| [INCOMING/08_CLIENT_MATERIALS/](INCOMING/08_CLIENT_MATERIALS/) | General source documents, content, brand/client materials |

**Intake rules:**

- Intake **does not equal approval**.
- Source files **must not** be interpreted as final design automatically.
- Original client materials remain **source evidence**.
- The design phase derives a **new production-ready visual system** from them.

---

## Design-first gate

No Gulp frontend, no WordPress, no local runtime until:

1. Materials intake and creative brief (Phase 1).
2. Homepage design screen-by-screen with operator/Olga approval.
3. Explicit frontend authorization against approved visual targets.

---

## Future phases (not started)

| Lane | State |
|------|-------|
| Design implementation | **NOT STARTED** |
| Gulp frontend | **NOT STARTED** |
| CMS architecture | **NOT STARTED** |
| Forge WordPress | **NOT STARTED** |
| Local runtime (`overseo.test`) | **NOT STARTED** |
| Production operations | **NOT STARTED** |

---

## Active authority pointers

| Concern | Document |
|---------|----------|
| LOC-ZONE root | [workspaces/website-factory-operations/README.md](../README.md) |
| Passport field contract | [FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md](../FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md) |
| Production modes | [website-factory-production-modes-charter-v1.md](../../../projects/mars-website-factory/website-factory-production-modes-charter-v1.md) |
| Factory operational index | [projects/mars-website-factory/OPERATIONAL-INDEX.md](../../../projects/mars-website-factory/OPERATIONAL-INDEX.md) |
| Forge WordPress (future) | [subsystems/forge-wordpress/OPERATIONAL-INDEX.md](../../../projects/mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md) |

---

## Next expected artifact

**PHASE 1:** Promoted materials in `INCOMING/` + creative brief document derived from Olga source materials.

---

*Human-operated Factory records. No runtime. No frontend. No WordPress. No production mutation.*
