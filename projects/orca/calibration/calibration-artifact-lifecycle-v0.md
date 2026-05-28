# Calibration Artifact Lifecycle v0

## Artifact types

| Type | Pattern | Example |
|------|---------|---------|
| System doc | `*-v0.md` at calibration root | `orca-calibration-system-v0.md` |
| Case README | `triumph-manipulator/README.md` | Case charter |
| Loop charter | `calibration-loop-v1/` | One closed calibration cycle |
| Finding doc | `*-v1.md` in case subfolders | `hero-drift-analysis-v1.md` |
| Evolution spec | `next-evolution/*` | Requirements for vNext |

## Versioning

- **v0** — system semantics (may evolve slowly)
- **v1** — first complete findings pass for a case (Triumph manipulator, 2026-05-28)
- Increment **v2** only when a **new production cycle** changes hero or section contracts materially

## States

| State | Meaning |
|-------|---------|
| `draft` | Initial calibration write; not reviewed by operator |
| `reviewed` | Human operator read and tagged findings |
| `superseded` | Replaced by v2 after major landing change |
| `archived` | Kept for history; no longer active SoT |

**v0 Triumph pass default:** `draft` (repo evidence only).

## Promotion path (human)

```text
calibration finding (draft)
    → operator review
    → optional: update content pack template / handoff template
    → optional: new handoff or hero v2 build charter
```

Calibration docs do **not** auto-update ORCA packs.

## Location rules

- All calibration artifacts live under `projects/orca/calibration/`
- Do not store calibration truth in `workspaces/` (implementation) or `governance/`
- Cross-link to workspace paths as **evidence**, not as SoT

## Retention

Keep superseded v1 files when hero redesign ships — they document **why** v2 was needed.
