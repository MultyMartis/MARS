# REPORT — RU Typography Stabilization Pass v1

> **HISTORICAL / INTEGRATION SUMMARY ONLY — NOT AUTHORITY.**  
> **Authority:** [russian-no-word-splitting-typography-v1.md](../russian-no-word-splitting-typography-v1.md) · **RU QA preset:** [ru-landing-qa-preset-v1.md](../ru-landing-qa-preset-v1.md).

**Date:** 2026-05-24  
**Lane:** B — Website Factory / Typography governance (documentation only)  
**Scope:** Authority lock, RU QA preset, QA flow sync, overflow alignment, cross-links — **no** V5/workspace/runtime changes.

---

## Summary

Canonical stabilization for Russian no word-splitting typography: **one authority document**, **one RU QA viewport preset**, duplicated rule prose removed from satellite docs, procedural drift and viewport ambiguity reduced.

---

## Files created

| File | Role |
|------|------|
| [ru-landing-qa-preset-v1.md](../ru-landing-qa-preset-v1.md) | **Canonical** RU commercial landing QA widths + checks |
| [reports/ru-typography-stabilization-pass-v1.md](ru-typography-stabilization-pass-v1.md) | This report |

---

## Files updated (authority-linked / drift cleanup)

| File | Change |
|------|--------|
| [russian-no-word-splitting-typography-v1.md](../russian-no-word-splitting-typography-v1.md) | §3 QA defers to RU preset; authority pointer reinforced |
| [frontend-production-rules-v0.md](../frontend-production-rules-v0.md) | §12 shortened — summary + authority + preset (no full rule duplication) |
| [production-hardening-rules-v1.md](../production-hardening-rules-v1.md) | Overflow edge cases: explicit forbidden/preferred + authority |
| [foundation-systems/responsive-system-v2.md](../foundation-systems/responsive-system-v2.md) | RU preset mandatory note; generic widths supplementary |
| [typography-rhythm-governance.md](../typography-rhythm-governance.md) | C-04/C-05 headline/orphan guidance; preset link |
| [operational-qa-entry-v1.md](../operational-qa-entry-v1.md) | RU preset mandatory; REPORT line for RU typography |
| [reference-workspace-qa-flow-v1.md](../reference-workspace-qa-flow-v1.md) | **C-01:** no longer legacy/incomplete; RU preset + REPORT format |
| [responsive-intent-governance.md](../responsive-intent-governance.md) | RU preset pointer; generic QA supplementary |
| [visual-regression-workflow-v1.md](../visual-regression-workflow-v1.md) | RU landings: preset widths authoritative for typography QA |
| [frontend-handoff-contract-v0.md](../frontend-handoff-contract-v0.md) | Minimal cross-link to authority + RU preset |
| [frontend-foundation-blueprint-v1.md](../frontend-foundation-blueprint-v1.md) | Typography row links RU authority |
| [canonical-implementation-pack-architecture.md](../canonical-implementation-pack-architecture.md) | implementation-pack QA pointer |
| [README.md](../README.md) | Index rows for RU typography + preset |
| [registries.md](../registries.md) | §6 relations: RU typography authority + preset |
| [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) | Cadence/rhythm + Wave 5 QA entries |
| [agents/frontend-gulp-agent/*](../../agents/frontend-gulp-agent/) | Authority lock on rules/QA/README/workflow/constraints/prompt-patterns |
| [agents/mars-forge/rhythm-governance-checklist.md](../../agents/mars-forge/rhythm-governance-checklist.md) | §10 defers to authority + preset |
| [agents/mars-forge/responsive-intent-checklist.md](../../agents/mars-forge/responsive-intent-checklist.md) | RU check → preset widths |
| [agents/mars-forge/design-token-checklist.md](../../agents/mars-forge/design-token-checklist.md) | Responsive QA: RU preset for commercial RU |

**Not touched:** `workspaces/`, Triumph V5, survivability tree, governance expansion.

---

## Drift / conflicts resolved

| ID | Issue | Resolution |
|----|-------|------------|
| **Authority** | Full CSS/HTML rules duplicated in `frontend-production-rules-v0.md`, Forge §10, integration report | Satellite docs: short summary + pointer to `russian-no-word-splitting-typography-v1.md` |
| **C-01** | `reference-workspace-qa-flow-v1.md` read as legacy; RU checks only in compact pass string | QA flow updated: RU preset mandatory section; REPORT includes `RU TYPOGRAPHY / NO WORD-SPLITTING` |
| **C-02** | Generic 375/768/1280 lists implied authority | Marked **supplementary**; RU commercial → `ru-landing-qa-preset-v1.md` |
| **C-03** | Residual `anywhere` recommendation risk in overflow docs | Explicit **FORBIDDEN** / **preferred** in hardening + responsive anti-overflow |
| **C-04** | “No orphaned short lines” provoked `nowrap` / `&nbsp;` chains | Clarified: fix via layout/cadence; selective ties per authority only |
| **C-05** | Headline overflow checks without word-break guardrails | Headline overflow → layout first; no word fragmentation (rhythm + QA flow) |

---

## Authority hierarchy (post-pass)

```text
1. russian-no-word-splitting-typography-v1.md     — CSS, HTML ties, overflow policy (authority)
2. ru-landing-qa-preset-v1.md                     — RU commercial landing QA widths + checks (canonical preset)
3. frontend-production-rules-v0.md §12            — operator summary + pointers only
4. Satellite checklists / responsive / hardening  — pointers + supplementary generic widths
```

---

## Viewport lists downgraded to supplementary

| Doc | Generic / legacy widths | Status |
|-----|-------------------------|--------|
| `reference-workspace-qa-flow-v1.md` | 375 / 768 / desktop | Supplementary interaction pass |
| `visual-regression-workflow-v1.md` | 375 / 768 / ≥1280 | Supplementary screenshot minimum |
| `frontend-handoff-contract-v0.md` example | 375 / 768 / 1280 | Example only; RU → preset |
| `frontend-gulp-agent/qa-checklist.md` | handoff `responsive_rules` | Supplementary unless RU landing |

**Authoritative for RU commercial typography QA:** `320 / 375 / 390 / 420 / 760 / 1180 / 1320 / 1440` per `ru-landing-qa-preset-v1.md`.

---

## Legacy ambiguity removed

- `operational-qa-entry-v1.md` no longer implies `reference-workspace-qa-flow` is “unchanged legacy” — flow is the **checklist body**; RU widths come from preset.
- Duplicate forbidden-CSS tables removed from `frontend-production-rules-v0.md` §12 and compressed in Forge §10.
- Integration report `no-word-splitting-typography-rule-integration-v1.md` remains historical record; not rewritten (superseded by this stabilization pass for operator routing).

---

## Validation (manual)

| Check | Result |
|-------|--------|
| Contradictory viewport policies | **Resolved** — RU preset canonical; generics labelled supplementary |
| Leftover `overflow-wrap: anywhere` recommendations | **None found** in Factory docs after grep (authority forbids; hardening/responsive aligned) |
| Conflicting authority wording | **Resolved** — single authority + preset |
| RU preset referenced in QA entry, reference flow, agents | **Yes** |

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| `REPORT — Website Factory Typography Rule Conflict Audit v1` | **Not located in-repo** at task read time — stabilization applied from task spec + integration report |
| Automated CSS lint for word-break | **Not** implemented |
| Non-RU primary locales | Preset **not** mandatory; authority applies when locale is RU |
| CMS / dynamic copy | Typography ties **SAFE UNKNOWN** until pipeline defined |
| Retroactive legacy workspaces | Requires explicit migration charter — **not** done |

---

## Git status

No commit. No push. Documentation-only diff under `projects/mars-website-factory/` and `agents/`.
