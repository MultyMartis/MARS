# REPORT — Search PPC phrase-slot reconciliation checkpoint

**Checkpoint type:** scoped git checkpoint and push  
**Date:** 2026-07-01  
**Branch:** `mars/canonical-post-recovery`  
**Pre-commit HEAD:** `925ef8169ba93cc567f1b290d2fb3c37d1768dc0`  
**Commit hash:** _(this commit — see `git rev-parse HEAD` after checkout)_  
**Volume:** `X:` / `AI WS`

---

## False-PASS summary

Corvonero V2.6.1 release gate recorded `RELEASE_GATE_PASS` on 2026-06-30 while authority phrase slots were **926** and deployable XLSX keyword rows were **924**. The delta was noted in `authority_reconciliation.phrase_slot_delta_note` but not enforced. `OPERATOR_IMPORT_READY` was incorrectly set true.

V2.6.1 gate result **invalidated** via `supersession` metadata; original historical PASS preserved.

---

## Root cause

**GENERATION_DEFECT** in `build_phrase_allocation`: `V26_SINGLE_PHRASE_MERGE` applied in group plan (`ca-02-troubleshooting-not-working` → `ca-02-support-tech`) but not when resolving group IDs during phrase allocation. Two slots for **программа 1с не работает** (CA-02 LOCAL and REMOTE, group `ca-02-support-tech`) were omitted from XLSX output.

---

## Exact two restored slots

| Campaign | Mode | Group | Phrase |
|----------|------|-------|--------|
| CA-02-LOCAL | LOCAL | ca-02-support-tech | программа 1с не работает |
| CA-02-REMOTE | REMOTE | ca-02-support-tech | программа 1с не работает |

Restored in deployable package **V2.6.2** only. Semantic authority **V2.6** unchanged.

---

## Shared gate changes

| Module | Change |
|--------|--------|
| `phrase-slot-reconciler.mjs` | Package/campaign/group row-level reconciliation |
| `phrase-normalizer.mjs` | Slot key normalization |
| `release-gate.mjs` | Enforce phrase-slot reconciliation; manifest XLSX discovery |
| `release-gate-cli.mjs` | `--group-plan`, `--architecture` CLI args |
| `phrase-slot-reconciler.test.mjs` | Multi-campaign regression scenarios |
| `release-gate.test.mjs` | Gate integration with group plan fixtures |

---

## Test result (pre-commit)

Run from `projects/mars-search-ppc-production/tools/commander-transport/`:

```
npm test
```

| Metric | Value |
|--------|------:|
| Total  | 98 |
| Passed | 98 |
| Failed | 0 |

Scenarios verified: package-wide mismatch, per-campaign mismatch, missing/unexpected/duplicate slots, wrong group/mode, normalization collision, equal total with campaign mismatch, exact multi-campaign match, V2.6.1 false-PASS regression pattern.

---

## Production release-gate confirmation (read-only)

**Authority:** Corvonero V2.6 (frozen group plan via operator receipt paths)  
**Package:** `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.6.2-FINAL-2026-06-30`  
**Receipt:** `CORVONERO-CAMPAIGN-V2.6-OPERATOR-SEMANTIC-APPROVAL-v1.json` (unchanged)

| Field | Value |
|-------|------:|
| authority_phrase_slots | 926 |
| artifact_phrase_slots | 926 |
| phrase_slot_delta | 0 |
| missing_slots | 0 |
| unexpected_slots | 0 |
| duplicate_slots | 0 |
| gate | RELEASE_GATE_PASS |

Package not modified. Commander import not performed.

---

## Corvonero V2.6.2 package path

`X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.6.2-FINAL-2026-06-30`

Not tracked in Git.

---

## Authority / artifact totals

| Version | Role | Phrase slots |
|---------|------|-------------:|
| V2.6 | semantic authority | 926 |
| V2.6.1 | invalidated deployable | 924 |
| V2.6.2 | corrected deployable | 926 |

---

## Staging manifest — included

| Path | Git status | Role | Reason |
|------|------------|------|--------|
| `tools/commander-transport/src/release-gate.mjs` | M | shared gate | phrase-slot enforcement |
| `tools/commander-transport/src/release-gate-cli.mjs` | M | shared CLI | group-plan/architecture args |
| `tools/commander-transport/tests/release-gate.test.mjs` | M | tests | gate fixture integration |
| `tools/commander-transport/src/phrase-slot-reconciler.mjs` | ?? | shared reconciler | new module |
| `tools/commander-transport/src/phrase-normalizer.mjs` | ?? | shared normalizer | new module |
| `tools/commander-transport/tests/phrase-slot-reconciler.test.mjs` | ?? | tests | regression coverage |
| `pilots/corvonero/CORVONERO-CAMPAIGN-RELEASE-STATE-v1.json` | M | release state | V2.6.2 deployable state |
| `pilots/corvonero/CORVONERO-CAMPAIGN-V2.6.1-RELEASE-GATE-RESULT-v1.json` | ?? | gate history | false-PASS + invalidation |
| `pilots/corvonero/CORVONERO-CAMPAIGN-V2.6.1-RELEASE-GATE-RESULT-v1.md` | ?? | gate history | companion |
| `pilots/corvonero/CORVONERO-CAMPAIGN-V2.6.1-PHRASE-SLOT-RECONCILIATION-v1.json` | ?? | reconciliation | row-level evidence |
| `pilots/corvonero/CORVONERO-CAMPAIGN-V2.6.1-PHRASE-SLOT-RECONCILIATION-v1.md` | ?? | reconciliation | companion |
| `pilots/corvonero/CORVONERO-CAMPAIGN-V2.6.1-RELEASE-GATE-CORRECTION-v1.json` | ?? | correction | invalidation record |
| `pilots/corvonero/CORVONERO-CAMPAIGN-V2.6.1-RELEASE-GATE-CORRECTION-v1.md` | ?? | correction | companion |
| `pilots/corvonero/CORVONERO-CAMPAIGN-V2.6.2-GENERATION-v1.json` | ?? | generation | V2.6.2 restore run |
| `pilots/corvonero/CORVONERO-CAMPAIGN-V2.6.2-FORENSIC-VALIDATION-v1.json` | ?? | validation | forensic PASS |
| `pilots/corvonero/CORVONERO-CAMPAIGN-V2.6.2-RELEASE-GATE-RESULT-v1.json` | ?? | gate result | corrected PASS |
| `pilots/corvonero/CORVONERO-CAMPAIGN-V2.6.2-RELEASE-GATE-RESULT-v1.md` | ?? | gate result | companion |
| `pilots/corvonero/CORVONERO-V2.6.1-PHRASE-SLOT-RECONCILIATION.csv` | ?? | evidence | full reconciliation CSV |
| `pilots/corvonero/CORVONERO-V2.6.1-MISSING-SLOTS.csv` | ?? | evidence | 2 missing slots |
| `pilots/corvonero/CORVONERO-V2.6.1-UNEXPECTED-SLOTS.csv` | ?? | evidence | empty |
| `pilots/corvonero/CORVONERO-V2.6.1-DUPLICATE-SLOTS.csv` | ?? | evidence | empty |
| `pilots/corvonero/tools/execute-campaign-v2.6-final-consolidation-v1.py` | ?? | generation fix | `resolve_deployable_group_id` in allocation |
| `pilots/corvonero/tools/execute-campaign-v2.6.2-phrase-slot-restore-v1.mjs` | ?? | generation | V2.6.2 slot restore |
| `reports/REPORT-search-ppc-multi-campaign-phrase-slot-release-gate-fix-v1.md` | ?? | report | systemic fix |
| `reports/REPORT-corvonero-v2.6-phrase-slot-reconciliation-v1.md` | ?? | report | Corvonero reconciliation |
| `reports/REPORT-search-ppc-phrase-slot-reconciliation-checkpoint-v1.md` | ?? | report | this checkpoint |

**Scoped file count:** 26

---

## Exclusions (preserved WIP)

- `X:\AI MARS STORAGE\**` — deployable package binaries
- `.recovery-temp/**`, `.tools-test-output/**`, `.tools/**` corvonero checkpoint scripts
- ATLAS, FP-0002, Website Factory, MLI, BZPM, unrelated Corvonero V2–V2.6 historical untracked artifacts
- Commander import candidates, template recovery, operator receipt (unchanged)
- `CORVONERO-CAMPAIGN-V2.6-OPERATOR-SEMANTIC-APPROVAL-v1.json` — not modified

---

## Push result

_(recorded after `git push origin mars/canonical-post-recovery`)_

---

## Verdict

MARS SEARCH PPC PHRASE-SLOT CHECKPOINT: scoped commit for exact authority/artifact phrase-slot reconciliation. Commander import and Yandex Direct launch **not** authorized in this task.
