# FP-XXXX — Project Passport Fields v1 (LOC-ZONE contract)

**Class:** LOC-ZONE passport field contract  
**Authority:** [website-factory-production-modes-charter-v1.md](../../projects/mars-website-factory/website-factory-production-modes-charter-v1.md)  
**Status:** **documented** — template contract for all `FP-XXXX-PROJECT-PASSPORT.md` files.  
**Not:** runtime schema, validator, or automated passport generator.

**Date:** 2026-06-17  
**Implementation pass:** WF-A01 — Pass 01 · WF-A02 — Pass 01 (validation fields §2.1)  
**Validation authority:** [website-factory-validation-architecture-charter-v1.md](../../projects/mars-website-factory/website-factory-validation-architecture-charter-v1.md)

---

## 1. Purpose

Defines mandatory **production mode** fields for Factory Project passports in LOC-ZONE (`workspaces/website-factory-operations/`).

Passports are **foundation documents** — distinct from MOC-* manifest records and ROC-* registry cards.

---

## 2. Mandatory fields

Insert after **§1 Project identifiers** (or equivalent identity block):

### § Production mode (mandatory)

| Field | Type | Required | Values |
|-------|------|----------|--------|
| `production_mode` | enum | **Yes** | `PIXEL_PERFECT` \| `TEMPLATE_ART` |
| `mode_declared_at` | ISO-8601 date | **Yes** when mode set | e.g. `2026-06-17` |
| `mode_declared_by` | string | **Yes** when mode set | operator / coordinator ID |
| `mode_rationale` | string | **Yes** when mode set | 1–3 sentences + evidence pointer |
| `mode_waivers` | string or list | No | Scoped PF N/A, interaction stubs, hybrid `page_mode_map` ref |
| `mode_history[]` | array | **Yes** (may be empty at first declare) | Transition log — see §3 |

**Blocking rule:** If `production_mode` is absent, `UNDECLARED`, `UNKNOWN`, or `CONFLICT`:

```text
SAFE UNKNOWN → STOP all frontend production
```

### § Validation lifecycle (recommended — WF-A02)

Optional display fields — **not** runtime-enforced; align with [frontend-qa-reporting-standard-v1.md](../../projects/mars-website-factory/frontend-qa-reporting-standard-v1.md) Layer F and Validation Architecture charter §5–§6.

| Field | Type | Required | Values |
|-------|------|----------|--------|
| `lifecycle_state` | enum | No | `—` \| `BUILT` \| `VERIFIED` \| `PRODUCTION PASS` |
| `validation_status` | enum | No | `—` \| `INTAKE_VALIDATED` \| `ARCHITECTURE_VALIDATED` \| `DESIGN_CONTRACT_VALIDATED` \| `COMPOSITION_VALIDATED` \| `NOT_VERIFIED` \| `PRODUCTION_BLOCKED` |
| `lifecycle_updated_at` | ISO-8601 | When lifecycle set | e.g. `2026-06-17` |
| `lifecycle_report_ref` | string | Recommended when lifecycle set | Path to REPORT citing VL evidence |

**Rules:**

- `lifecycle_state` **SoT** is the latest compliant REPORT Layer F line — passport row is **display/cache** only.
- `validation_status` may reflect latest completed VL layer or rollup blockers — **must not** claim VERIFIED without charter §5.3 evidence.
- Mode transition resets affected `validation_status` / `lifecycle_state` per production modes charter §6.

**Cross-links:** `production_mode` (mandatory §2) · `lifecycle_state` (optional §2.1) · charter [§8 Production Mode Integration](../../projects/mars-website-factory/website-factory-validation-architecture-charter-v1.md#8-production-mode-integration).

### Example block (markdown)

```markdown
## Production mode

| Field | Value |
|-------|-------|
| production_mode | **PIXEL_PERFECT** |
| mode_declared_at | 2026-06-17 |
| mode_declared_by | PER-0010 |
| mode_rationale | Approved FIG `INCOMING/01_DESIGN/*.fig` — pixel delivery contract per client brief. |
| mode_waivers | (none) |

### mode_history[]

| # | from | to | at | by | report_ref |
|---|------|-----|-----|-----|------------|
| — | — | PIXEL_PERFECT | 2026-06-17 | PER-0010 | (initial declare) |
```

---

## 3. mode_history[] entry contract

Each transition **appends** one row — silent overwrite **forbidden**.

| Field | Required | Description |
|-------|----------|-------------|
| `from` | Yes | Prior mode token or `—` for initial declare |
| `to` | Yes | New mode token |
| `at` | Yes | ISO-8601 date |
| `by` | Yes | Operator ID |
| `rationale` | Yes | Short reason |
| `report_ref` | Recommended | Path to MODE TRANSITION REPORT |
| `gates_rerun` | Recommended | List of gates re-executed post-transition |

---

## 4. MOC-01 / manifest integration

When a Factory Project is manifest-enrolled:

| Surface | Field | Rule |
|---------|-------|------|
| **MOC-01** entry anchor | Link to passport § Production mode | Operator sees mode in quick nav |
| **MOC-03** scope | `factory.production_mode` display line | Current mode + declared date |
| **MOC-11** amendment | Mode transition | Append-only via `mode_history[]` + MOC-11 narrative if scope tier changes |
| **SOC-02** orientation | Current Production Mode | Read from passport — not recomputed |

**Rule:** Passport is **SoT** for `production_mode`; MOC/SOC surfaces **display** only.

---

## 5. Enrollment checklist

Before ROC enrollment or frontend handoff:

- [ ] `production_mode` declared per charter
- [ ] `mode_declared_at`, `mode_declared_by`, `mode_rationale` filled
- [ ] `mode_history[]` has initial row
- [ ] Mode-specific intake evidence registered (visual SSOT for PIXEL; blueprint/content for TEMPLATE)
- [ ] REPORT cites `Production mode:` header line
- [ ] (Recommended) `lifecycle_state` / `validation_status` aligned with latest REPORT when VL4+ executed — see §2.1

---

## 6. Retroactive declaration (existing projects)

Projects created before WF-A01 may **retroactively** declare mode with:

```text
mode_history[] row: from — → to <MODE> · rationale: retroactive WF-A01 declare · report_ref: <pass-01 or project REPORT>
```

Do **not** infer mode from chat memory — cite evidence (FIG pack, blueprint path, execution case).

---

*LOC-ZONE contract only. No runtime.*
