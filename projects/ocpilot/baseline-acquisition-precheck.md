# OCPilot — Baseline Acquisition Precheck

**Purpose:** stop/go checklist before full baseline intake begins. If any step fails → **SAFE UNKNOWN**, **stop**, request operator clarification.

**Status:** documented checklist only; **no** archive import in Run 2.7.

**Use when:** operator has placed a baseline ZIP in `incoming/baselines/` and Run 3 (or later) acquisition is about to start.

**Related:** [archive-intake-rules.md](archive-intake-rules.md), [intake-workflow.md](intake-workflow.md), [quarantine-policy.md](quarantine-policy.md)

---

## Precheck checklist

Complete in order. Do not skip steps.

| # | Step | Pass criteria | On fail |
|---|------|---------------|---------|
| 1 | **Archive present** | Expected ZIP exists in `incoming/baselines/` (or operator-declared path); filename matches operator brief | **Stop** — request operator place archive |
| 2 | **Archive readable** | Archive opens/listing succeeds; not corrupted, empty, or password-protected without credentials | **Stop** — SAFE UNKNOWN; request re-upload or password |
| 3 | **Archive structure inspected** | Archive Root entries documented (top-level files and directories) | **Stop** — cannot proceed without structure listing |
| 4 | **Package Root identified** | Package Root path recorded per [archive-intake-rules.md](archive-intake-rules.md) | **Stop** — SAFE UNKNOWN; request operator clarify layout |
| 5 | **OpenCart Root identified** | Directory with `admin/`, `catalog/`, `system/`, `image/`, `config.php`, `index.php` located and path recorded | **Stop** — SAFE UNKNOWN; may be wrong package type or incomplete archive |
| 6 | **Version identified** | Platform (OpenCart vs ocStore) and version/rs build inferred from tree metadata + operator brief — or explicitly marked SAFE UNKNOWN with gaps listed | **Stop** if destination baseline cannot be recommended safely |
| 7 | **Archive understood** | Archive Root → Package Root → OpenCart Root chain documented; no unresolved structural ambiguity | **Stop** — request operator clarification |
| 8 | **No obvious credentials** | No `.env`, SQL dumps with users/passwords, populated `config.php` secrets, API tokens, or credential sidecar files in archive listing | **Stop** — escalate per [quarantine-policy.md](quarantine-policy.md); do not commit secrets |
| 9 | **Ready for intake report** | Sufficient evidence to fill [templates/intake-report-template.md](templates/intake-report-template.md) | **Stop** — gather missing metadata first |
| 10 | **Ready for passport creation** | Draft passport fields can be prepared for target `baselines/<version-folder>/` | **Stop** if version/destination still SAFE UNKNOWN |

---

## Expected Run 3 archives (reference)

| Archive | Package Root candidate | Target baseline |
|---------|------------------------|-----------------|
| `opencart-3.0.3.8-rs.zip` | `upload-3038-rs2/` | `baselines/ocstore-3038-rs2/` |
| `opencart-3.0.3.9-rs.zip` | `upload-3039-rs1/` | `baselines/ocstore-3039-rs1/` |

Presence of these filenames does **not** auto-pass precheck — all steps still required.

---

## Pass / fail behavior

### All steps pass

Proceed to full baseline intake per [intake-workflow.md](intake-workflow.md):

- complete intake report
- prepare draft passport
- recommend sanitization and destination placement
- **wait for operator approval** before any move to `baselines/`

### Any step fails

| Action | Required |
|--------|----------|
| Mark failing step(s) | In run report and operator message |
| State **SAFE UNKNOWN** | What is unknown and what would verify it |
| **Stop** | No extraction into `baselines/`; no passport marked final; no baseline promotion |
| Request operator clarification | Specific question — not generic «please fix» |

---

## Quick reference — detection reminders

```
ZIP
 ↓
Archive Root          (list ZIP top level)
 ↓
Package Root          (single top-level dir → inspect first)
 ↓
OpenCart Root         (admin/, catalog/, system/, image/, config.php, index.php)
 ↓
Version + destination baseline folder
```

See [archive-intake-rules.md](archive-intake-rules.md) for full rules.

---

## Integration with other gates

| Gate | When |
|------|------|
| **This precheck** | Before intake report and passport draft |
| [quarantine-policy.md](quarantine-policy.md) | Any stop condition during steps 1–8 |
| [intake-workflow.md](intake-workflow.md) | After precheck passes |
| [baseline-readiness-checklist.md](baseline-readiness-checklist.md) | After operator-approved placement in `baselines/` |

Precheck pass does **not** mean baseline is **READY** for comparison — readiness requires passport, files, and manifest in destination folder.

---

## Related documents

| Doc | Role |
|-----|------|
| [run-3-preparation.md](run-3-preparation.md) | Run 3 scope and operator actions |
| [incoming/baselines/README.md](incoming/baselines/README.md) | Dropzone rules |
| [baselines/storage-policy.md](baselines/storage-policy.md) | ZIP vs extract vs metadata |
| [baseline-acquisition-strategy.md](baseline-acquisition-strategy.md) | Trust and rejection criteria |

---

## SAFE UNKNOWN

- Precheck without physical archive in repo — steps 1–7 remain unverified until Run 3.
- Automated credential scanning — **not** claimed; filename/metadata review only unless operator provides scan results.
