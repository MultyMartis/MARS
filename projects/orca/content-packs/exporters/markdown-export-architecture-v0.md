# Markdown Export Architecture v0

## Status

**PRE-IMPLEMENTATION** — operational / internal export format.

## Role

Markdown export supports:

- Git diffs and review in Cursor
- Agent-assisted editing with human approval
- Intermediate SoT before DOCX sign-off

Markdown is **not** the default client-facing approval format unless operator explicitly uses `approved_for_client_export` on a Markdown bundle (discouraged — prefer DOCX).

## Output shape

Two modes:

| Mode | Output |
|------|--------|
| **Pack-native** | Same structure as [landing-content-pack-template-v0.md](../templates/landing-content-pack-template-v0.md) |
| **Flattened** | Linear read order for email / quick review (sections 01–10 only) |

## Front-matter (required)

```yaml
---
export_id: export-20260527-01
exported_at: 2026-05-27T12:00:00+03:00
exported_by: <human>
export_format: markdown
export_mode: internal_review
source_pack_id: ...
source_pack_version: ...
semantic_lock_snapshot: active
approval_gates_snapshot: { ... }
---
```

## Section headings

```markdown
## 01 HERO {#hero}

> **Purpose:** …
> **PPC continuity:** …
> **🔒 Locks:** …
```

## Lock annotations

Locked copy blocks suffix:

```markdown
**H1:** Манипулятор 5 тонн в Краснодаре <!-- locked: true -->
```

## SAFE UNKNOWN

```markdown
> ⚠ **SAFE UNKNOWN:** hourly_rate_rub — do not publish until operator confirms
```

## Relationship to DOCX

Recommended flow:

```
Pack Markdown (SoT) → human approve → export DOCX → client review
```

Reverse sync (DOCX → Markdown) requires operator merge — not automated.

## Boundary

Architecture only.
