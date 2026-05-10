# MARS — Project registry

**Normative role:** This file is the **single source of truth** for **projects** in the MARS repository. Introspection, governance consumers, and human operators **must** treat rows defined here as authoritative for **project identity** and **project-level lifecycle fields** listed below. If a project is not listed, its project facts are **unknown** at registry level until a row is added (see `../interfaces/introspection-v0.md` — **SAFE UNKNOWN** for unresolved `<id>`).

**Version:** v0 (append or amend rows per `../governance/versioning-model.md` when governance requires it).

---

## Record schema (required fields)

Each project **must** have exactly one row (or one structured record) with:

| Field | Type / values | Meaning |
|-------|----------------|---------|
| **project_id** | Opaque string, stable | Unique project identifier used in introspection **PROJECT** mode and in cross-references. |
| **status** | `planned` \| `active` \| `archived` | Lifecycle band: not yet started, in use, or retired from active work. |
| **phase** | String | Current or target MARS / product phase label (align with `../README.md`, `../governance/` phase vocabulary when applicable). |
| **related_entities** | List or comma-separated ids | Agent names, cards, or other registry entity ids tied to this project (see `../agents/registry.md`). |
| **last_updated** | ISO-8601 date (or datetime) | When this row was last reviewed or changed. |

Optional narrative columns may be added **only** if governance documents them; do not use optional columns to bypass the required fields above.

---

## Projects (authoritative table)

| project_id | status | phase | related_entities | last_updated |
|------------|--------|-------|------------------|--------------|
| *example:* `mars-core` | planned | Phase 1 | *(none yet)* | 2026-04-27 |
| `seo-content-agent` | planned | documentation / planned MVP | *(none yet)* | 2026-05-04 |
| `metabot-seo-content-agent` | active | external multi-workflow AI system (n8n runtime); in-repo docs only | *(none yet)* | 2026-05-10 |

*(Replace the example row or add rows as projects are formally registered.)*

**Note:** `seo-content-agent` is an earlier **spec-oriented** pack under `projects/seo-content-agent/`. **`metabot-seo-content-agent`** documents **MetaBOT — SEO Content Agent** as operated (Intake / Worker / Admin); reconcile overlaps against **live n8n**, not only markdown.

---

## Maintenance rules

1. **Single source of truth** — Do not duplicate canonical project rows in other markdown files; **link** to this file or cite `project_id` instead.
2. **Consistency** — When **status** or **phase** changes, update **last_updated** and prefer recording a matching event in `../logs/lifecycle-log.md`.
3. **No shadow registries** — Spreadsheets, chats, or external tools are **not** authoritative unless their content is reflected here.
