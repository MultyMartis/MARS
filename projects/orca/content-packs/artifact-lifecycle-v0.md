# Content Pack Artifact Lifecycle v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — aligns with [../artifacts/orca-artifact-system-v0.md](../artifacts/orca-artifact-system-v0.md) for pack-specific states.

## Artifact states

| State | Meaning | Typical next step |
|-------|---------|-------------------|
| `draft` | Work in progress; not operational truth | Operator review |
| `reviewed` | Human read; findings logged | Approve or revise |
| `approved` | Copy and locks accepted for export | DOCX export; Factory prep |
| `factory-ready` | Handoff issued; MODE 1 build allowed | Factory implementation |
| `client-ready` | DOCX (or future PDF) cleared for external share | Client delivery |
| `archived` | Frozen; superseded by newer `pack_version` | Reference only |

**Rule:** `draft` ≠ SoT for paid traffic or Factory MODE 1.

## State transitions (human only)

```
draft → reviewed → approved → factory-ready → client-ready
                              ↘ archived (any time after approved)
```

| Transition | Requires |
|------------|----------|
| → `reviewed` | Operator review checklist complete |
| → `approved` | No blocking SAFE UNKNOWN on launch-critical claims |
| → `factory-ready` | `approved_for_factory` gate + handoff doc |
| → `client-ready` | `approved_for_client_export` + DOCX revision recorded |
| → `archived` | Operator note; new pack version supersedes |

AI tools **must not** set states or gates.

## Approval gates (content-packs scope)

These gates are **boolean flags** on the pack envelope — set only by human operator in `approvals/` or `PROJECT.md`.

| Gate | Unlocks |
|------|---------|
| `approved_for_factory` | Website Factory MODE 1 handoff; semantic lock for implementation |
| `approved_for_client_export` | External DOCX / future PDF to client |
| `approved_for_ads` | PPC continuity sign-off against pack (pre-launch QA) |
| `approved_for_launch` | Live ads + production URL (with Commander checklist) |

### Relationship to global ORCA gates

| Global gate ([approval-gates-contract-v0.md](../artifacts/approval-gates-contract-v0.md)) | Content-packs gate |
|-------------------------------------------------------------------------------------------|-------------------|
| `approved_for_factory` | Same name — pack must be `approved`+ |
| `approved_for_launch` | Requires `approved_for_ads` + landing QA |
| `approved_for_client_pdf` | Maps to `approved_for_client_export` for pack/DOCX path |
| `approved_for_commander_import` | **Separate** — Commander exporter-cli |

## Recording approvals

| Location | Content |
|----------|---------|
| Pack front-matter | `artifact_state`, `approval_gates` snapshot |
| `projects/orca/projects/<id>/approvals/*.md` | Dated sign-off |
| Export metadata | Gates at export time — [schemas/export-metadata-schema-v0.md](schemas/export-metadata-schema-v0.md) |

## Versioning

- `pack_version`: semver or `v0`, `v1` per route  
- Breaking copy change → increment version; prior → `archived`  
- Factory handoff must cite exact `pack_id` + `pack_version`

## Anti-patterns

- Validation CLI green → treat as `approved` (**forbidden**)
- DOCX generated from `draft` pack labeled “final” (**forbidden**)
- Factory edits copy without pack version bump under MODE 1 (**forbidden**)

## SAFE UNKNOWN

- Verbal client OK without written gate → **not approved**
- Partial section approval → document scope in approval file; do not imply full-page lock

## Boundary

Lifecycle vocabulary only. No workflow engine.
