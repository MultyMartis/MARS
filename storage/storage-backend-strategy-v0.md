# Storage Backend Strategy v0

**Status:** documented — strategy-level guidance for selecting storage backend patterns in MARS. Documentation-only, with no fixed backend decision.

## 1. Purpose

- Define candidate backend patterns for Stage 14 runtime/deployment planning.
- Provide a selection framework without hard-binding MARS to one storage technology.
- Align backend choices with data governance, compliance posture, and memory/runtime contracts.

## 2. Backend options (v0)

| Option | Strengths | Constraints / cautions |
|--------|-----------|------------------------|
| `Google Sheets` | Simple operational entry point, rapid manual visibility. | Limited scale/control; high governance discipline needed for sensitive data. |
| `SQL (VPS)` | Structured querying, transactional semantics, stronger control patterns. | Requires operational maturity, security hardening, and admin discipline. |
| `file storage` | Straightforward artifact persistence and portability. | Metadata/query limits; integrity and indexing concerns at scale. |
| `hybrid` | Flexibility by workload class (state vs artifacts vs analytical data). | Increased complexity, boundary management, and consistency overhead. |

## 3. Selection rules

1. Backend selection is project-specific and must align with actual task/data requirements.
2. Compliance obligations (including locale/regional requirements such as RF data laws) must be assessed before choosing a backend path.
3. Selection should preserve separation between runtime state, durable memory, and artifact storage concerns.
4. If requirements are unclear, selection status remains **SAFE UNKNOWN** until scope is explicit.

## 4. Relation to other artefacts

- [storage-architecture-v0.md](storage-architecture-v0.md) — storage classes and pluggable architecture model.
- [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) — write authority, prohibited content, retention metadata.

## 5. Explicit non-goals

- No backend is mandated as universal default for all projects.
- No concrete schema, migration, or adapter implementation is provided.
- No operational SLA/backup implementation details are provided.

**Explicit statement:** **NO fixed backend chosen** in v0.
