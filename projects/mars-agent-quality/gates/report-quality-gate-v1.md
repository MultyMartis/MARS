# REPORT Quality Gate v1

**Status:** `MINIMAL_V1`  
**Mode:** `HUMAN_INVOKED` / `NOT_AUTOMATED`

## Purpose

Define the minimal gate for accepting a MARS agent REPORT as usable handoff evidence.

This is not a parser, CI gate, runtime validator, or automatic enforcement mechanism.

## Required Checks

| Check | Required Evidence |
|---|---|
| Task id | Explicit task id or stage id |
| Scope executed | Short statement of actual scope completed |
| Files changed | Repo-relative path list or `none` |
| Files created | Repo-relative path list or `none` |
| Files deleted | Repo-relative path list or `none` |
| Commands run | Exact commands or `none` |
| Validation evidence | Output, receipt, screenshot, checksum, or `SAFE_UNKNOWN` |
| Git status | Post-task `git status --short` summary |
| Foreign WIP preservation | Statement that unrelated WIP was not touched |
| UNKNOWN / SAFE UNKNOWN | Bounded unknowns, or `none` |
| Risks | Open risks, or `none` |
| Operator approval required or not | Explicit yes/no and reason |
| Next step | Exact next allowed action |
| No commit unless authorized | Confirm no commit, or cite explicit commit request |

## Minimal Verdicts

| Verdict | Meaning |
|---|---|
| `PASS` | Required fields present and backed by evidence |
| `PASS_WITH_NOTES` | Usable, but non-blocking evidence gaps are listed |
| `FAIL` | Required field missing, contradictory, or unsupported |
| `UNKNOWN` | Gate cannot be applied because evidence is absent or scope is unclear |

## REPORT Is Not Proof By Itself

REPORT is a handoff and evidence index. It is not proof by itself.

REPORT must be backed by file paths, git status, validation output, screenshots, checksums, receipts or other task-appropriate evidence.

Forbidden claims:

- `COMPLETE` without file or command evidence.
- `PASS` without validation evidence when validation was required.
- `Visual PASS` from build output alone.
- `Git persisted` from report text alone.
- `No foreign WIP touched` when git status was not read.
- `Runtime enforcement active` from documentation alone.

## Failure Triggers

The REPORT gate fails when:

- task id is missing;
- changed files are not enumerated;
- deleted files are hidden or unexplained;
- validation is claimed but not evidenced;
- git status is omitted after a mutating task;
- foreign WIP is staged, reverted, cleaned, or ignored;
- risks or SAFE_UNKNOWN are suppressed;
- operator approval is required but not stated;
- commit/push happened without explicit authorization.

## Operator Use

Use this gate before accepting an agent task as complete, before approving downstream work, or before using a REPORT as source evidence in another programme.

This gate does not replace programme-specific QA gates, OPERATIONAL-INDEX files, production lifecycles, or operator approval laws.
