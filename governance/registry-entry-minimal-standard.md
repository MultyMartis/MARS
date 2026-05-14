# MARS — Registry entry minimal standard (human-managed)

**Status:** **documented** — documentation-oriented. **Version:** v0 (Phase S2).

**Purpose:** A **lightweight** minimum set of fields for **human-maintained** registries (`agents`, `tools`, `registry/project-registry`, future governance tables). **Not** a JSON Schema product, **not** a database DDL, **not** an API.

---

## 1. Minimum fields (conceptual)

Each **entry** (row or short record) **should** make the following clear at a glance:

| Field | Intent |
|-------|--------|
| **id** | Stable string for **this registry’s** scope (e.g. `project_id`, `tool_id`, agent role id). **Not** automatically equal to external workflow ids. |
| **type** | What kind of thing this is (`agent`, `tool`, `project`, `workflow-contract`, `external-system`, …) — pick vocabulary consistent with [identity-and-naming-rules.md](identity-and-naming-rules.md). |
| **status** | Lifecycle band for **documentation / program** — e.g. `planned`, `active`, `archived`, `legacy`, `experimental` (use enums your table already defines; extend only via governance). |
| **scope** | Where it applies: `mars-core`, `website-factory`, `external-metabot`, `r1-demo`, … |
| **authority level** | What this row is allowed to assert: `normative-governance`, `descriptive-pack`, `experimental-code`, `external-reference`, … |
| **owner** | Human or team role accountable for updates (free text is fine). |
| **source-of-truth** | Primary doc or system for **truth** (e.g. `registry/project-registry.md`, `integration-boundary.md`, `live n8n`). |
| **related systems** | Pointers: paths, URLs (non-secret), or external system names. |
| **implementation status** | One of: **planned** · **documented** · **experimental** · **operationally verified** (human) · **external** — see §2. |
| **notes** | Drift warnings, deprecation, “do not confuse with X”. |

**Optional:** `last_updated` (ISO date), `depends_on`, `risk` — when already used by an existing table, keep them.

---

## 2. Implementation status vocabulary (distinct meanings)

| Value | Meaning |
|-------|---------|
| **planned** | Intent only; no in-repo implementation claimed |
| **documented** | Contracts / packs exist as Markdown; still not runnable product |
| **experimental** | Code or demo exists for learning (e.g. R1); **not** production assertion |
| **operationally verified** | A **human** procedure was followed and recorded (e.g. runbook, checklist) — **not** “MARS verified it automatically” |
| **external** | Live behavior is owned outside the repo; docs may be partial or sanitized |

---

## 3. Rules

- Prefer **one row per id**; if a legacy id must appear, cross-link to the canonical id in **notes**.  
- Do not imply **sync** from code or from n8n — updates are **manual**.  
- When in doubt, set **authority level** to **descriptive-pack** and **implementation status** to **documented** or **external**.

---

*No automated validation, migration tooling, or registry engine is specified here.*
