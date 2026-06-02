# OCPilot — Intake Workflow

**Purpose:** define human-supervised intake steps for packages entering through [incoming/](incoming/README.md).

**Status:** documented workflow only; **no** automatic moves; **no** automatic imports; **no** runtime.

**Core safety principle:**

```
Incoming Material  must pass intake  before  Trusted Baseline  or  Project Site
```

Operator approves all movement out of incoming.

---

## Shared intake rules

| Rule | Meaning |
|------|---------|
| **Nothing trusted by default** | Every package is quarantined until review completes |
| **No auto-move** | OCPilot recommends destination; operator physically moves or copies |
| **Intake report required** | Use [templates/intake-report-template.md](templates/intake-report-template.md) for each package |
| **Stop on risk** | See [quarantine-policy.md](quarantine-policy.md) — halt and ask operator when triggered |
| **SAFE UNKNOWN** | Mark unknowns explicitly; do not infer version, completeness, or cleanliness |

---

## Baseline intake workflow

For packages placed in `incoming/baselines/`.

| Step | Actor | Action |
|------|-------|--------|
| **1. Drop** | Operator | Place package into `incoming/baselines/`; note declared source in task brief if available |
| **2. Identify source** | OCPilot (assist) | Record declared origin; evaluate trust per [baseline-acquisition-strategy.md](baseline-acquisition-strategy.md); assign High / Medium / Low |
| **3. Identify version** | OCPilot (assist) | Infer platform (OpenCart vs ocStore) and version from archive listing, filenames, changelog — **SAFE UNKNOWN** if inconclusive |
| **4. Readiness review** | OCPilot (assist) | Pre-check against rejection criteria: missing dirs, credentials, custom modules, live-site artifacts; **not** full [baseline-readiness-checklist.md](baseline-readiness-checklist.md) until after sanitization in destination |
| **5. Determine destination baseline** | OCPilot (assist) | Recommend `baselines/<version-folder>/` (e.g. `opencart-3037/`, `ocstore-3037/`) or **reject** if wrong platform/version |
| **6. Create passport (draft)** | OCPilot (assist) | Prepare draft fields for [templates/versioned-baseline-passport-template.md](templates/versioned-baseline-passport-template.md); final passport stored in destination `passports/` after operator approval |
| **7. Recommend move** | OCPilot (assist) | Document recommended sanitization steps and move into `baselines/<folder>/files/` (+ manifest, notes); **operator approves and executes** |

### Baseline intake outputs

- Completed intake report (stored in operator-chosen location — e.g. destination `notes/` or run report; not auto-written to repo unless operator requests)
- Trust level and risk level
- Recommended destination or rejection reason
- Draft passport fields
- List of suspicious/missing items

### Baseline intake forbidden actions

- Moving package from incoming to `baselines/` without operator approval
- Committing unsanitized secrets
- Declaring baseline **READY** before [baseline-readiness-checklist.md](baseline-readiness-checklist.md) passes in destination

---

## Project site intake workflow

For materials placed in `incoming/project-sites/`.

| Step | Actor | Action |
|------|-------|--------|
| **1. Drop** | Operator | Place archive or material bundle into `incoming/project-sites/` |
| **2. Identify platform** | OCPilot (assist) | OpenCart vs ocStore vs unknown; note mixed or non-OpenCart content if present |
| **3. Identify version** | OCPilot (assist) | Version string from file tree metadata if visible — **SAFE UNKNOWN** if not verifiable without executing site |
| **4. Identify archive type** | OCPilot (assist) | Classify: full site backup, partial files, DB-only, theme-only, extension pack, mixed handoff, documentation-only |
| **5. Identify risks** | OCPilot (assist) | Credentials, PII, destructive scripts, unknown binaries; apply [quarantine-policy.md](quarantine-policy.md) |
| **6. Recommend site folder** | OCPilot (assist) | Propose `sites/<site-slug>/` (new copy from `_template-site/` or existing slug); map materials to subfolders per [project-sites-workflow.md](project-sites-workflow.md) |
| **7. Create intake report** | OCPilot (assist) | Fill [templates/intake-report-template.md](templates/intake-report-template.md); include recommended next steps (passport, baseline selection for future audit) |

### Project site intake outputs

- Intake report with archive type and risk level
- Recommended `site-slug` and target subfolders (`materials/`, `backups/`, etc.)
- Explicit list of items that must **not** enter repo (secrets, raw dumps)
- SAFE UNKNOWN list for version/platform gaps

### Project site intake forbidden actions

- Auto-creating `sites/<slug>/` without operator approval of slug name
- Importing DB or copying live configs into repo
- Treating project export as baseline candidate without separate baseline intake path

---

## Human approval gate

Before any move out of incoming, operator confirms:

| # | Confirmation |
|---|--------------|
| 1 | Intake report reviewed |
| 2 | Trust / risk level accepted or override documented |
| 3 | Destination path correct |
| 4 | Secrets stripped or kept external |
| 5 | No quarantine stop condition active |

OCPilot emits `# REPORT — …` when run completes; movement itself remains operator action.

---

## Workflow diagram

```
                    ┌─────────────────────┐
                    │  External package   │
                    └──────────┬──────────┘
                               │
              ┌────────────────┴────────────────┐
              ▼                                 ▼
   incoming/baselines/              incoming/project-sites/
              │                                 │
              ▼                                 ▼
      Baseline intake steps              Project site intake steps
      (source, version,                  (platform, version, type,
       readiness pre-check)               risks, site folder)
              │                                 │
              └────────────────┬────────────────┘
                               ▼
                    Intake report template
                               │
                               ▼
                    Operator review (HITL)
                               │
              ┌────────────────┴────────────────┐
              ▼                                 ▼
   baselines/<version>/                 sites/<site-slug>/
   (Run 3+)                             (Run 4+)
```

---

## Relation to runs

| Run | Intake path |
|-----|-------------|
| Run 2.5 | Workflows defined; incoming zone empty except placeholders |
| Run 3 | First baseline package through baseline intake |
| Run 4 | First project site through project site intake |
| Run 5+ | Audits use baselines/sites only after intake complete |

See [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md).

---

## Related documents

| Doc | Role |
|-----|------|
| [incoming/README.md](incoming/README.md) | Zone architecture |
| [baseline-acquisition-strategy.md](baseline-acquisition-strategy.md) | Source trust and rejection |
| [quarantine-policy.md](quarantine-policy.md) | Stop conditions |
| [templates/intake-report-template.md](templates/intake-report-template.md) | Report structure |
| [baseline-readiness-checklist.md](baseline-readiness-checklist.md) | Post-placement baseline gate |
| [project-sites-workflow.md](project-sites-workflow.md) | Site folder semantics |

---

## SAFE UNKNOWN

- Automated archive listing tools — **not** claimed; operator may provide file lists; agent reviews what is available without executing unknown archives.
- Standard intake report storage path in repo — operator choice per run; template does not mandate folder until Run 3/4 convention emerges.
