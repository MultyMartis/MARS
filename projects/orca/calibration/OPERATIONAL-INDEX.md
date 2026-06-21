# ORCA Calibration — Operational Index

**Lane:** B — ORCA Calibration Layer v0  
**Default case:** Triumph manipulator — master hot (`zakaz`)

---

## Fast path (one calibration session)

1. Open [triumph-manipulator/calibration-loop-v1/](triumph-manipulator/calibration-loop-v1/) — loop charter for this case.
2. Read [triumph-manipulator/current-state/landing-state-summary-v1.md](triumph-manipulator/current-state/landing-state-summary-v1.md) — what is live in repo today.
3. Run drift pass: [triumph-manipulator/drift-analysis/](triumph-manipulator/drift-analysis/).
4. Record UX + implementation findings under [triumph-manipulator/ux-observations/](triumph-manipulator/ux-observations/) and [triumph-manipulator/implementation-findings/](triumph-manipulator/implementation-findings/).
5. Close with [triumph-manipulator/next-evolution/](triumph-manipulator/next-evolution/) — pack / hero vNext requirements.
6. **STOP** — do not expand to all 11 sibling pages in the same session unless chartered.

---

## System docs (cross-case)

| File | Use when |
|------|----------|
| [orca-calibration-system-v0.md](orca-calibration-system-v0.md) | Defining what calibration is |
| [semantic-drift-rules-v0.md](semantic-drift-rules-v0.md) | Classifying a change as productive / destructive |
| [calibration-review-method-v0.md](calibration-review-method-v0.md) | Running a human review |
| [calibration-artifact-lifecycle-v0.md](calibration-artifact-lifecycle-v0.md) | Naming, versioning, archiving findings |

---

## Triumph case tree

```text
triumph-manipulator/
├── README.md
├── calibration-loop-v1/          ← loop scope + evidence map
├── current-state/                ← as-built snapshot
├── drift-analysis/               ← ORCA vs factory vs PPC
├── ux-observations/              ← hero, density, mobile
├── implementation-findings/      ← factory + pack gaps
├── ppc-alignment/                ← ad ↔ landing continuity
└── next-evolution/               ← vNext pack + scaling rules
```

---

## Evidence sources (read-only for calibration)

| Artifact | Path |
|----------|------|
| Master hot blueprint | `projects/orca/ppc/triumph-manipulator/landing-pages/01-master-hot-general.md` |
| Campaign instance (grp 12) | `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json` |
| Capability pack (reference) | `projects/orca/content-packs/examples/triumph-manipulyator-5-tonn-pack-v0.md` |
| 5-ton handoff (structural cousin) | `projects/orca/ppc/triumph-manipulator/handoff/triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff.md` |
| **Canonical implementation (v6)** | `workspaces/triumph-manipulator-landing-v6/` — master hot zakaz: `src/pages/index.html` (or route HTML) + `v5-ppc/zakaz/*` partials |
| v6 production state | `projects/triumph-manipulator-landing/V6-PRODUCTION-CANDIDATE-STATE.md` · authority [triumph-workspace-authority-map-v1.md](../../../triumph-manipulator-landing/triumph-workspace-authority-map-v1.md) |
| v5 hardening reports (historical) | `workspaces/triumph-manipulator-landing-v5/reports/` |
| Legacy v4 hero (anti-pattern) | `workspaces/triumph-manipulator-landing-v4/src/partials/sections/screen-01-hero.html` |

**Note:** No dedicated `*-zakaz-handoff.md` exists yet — calibration treats blueprint + instance + as-built HTML as evidence (SAFE UNKNOWN for formal handoff sign-off).

---

## Boundaries

- Do **not** edit `workspaces/triumph-manipulator-landing-v6/` (or v5 historical trees) from this lane unless a separate production charter says so.
- Do **not** claim launch readiness or conversion performance — human reasoning only.
