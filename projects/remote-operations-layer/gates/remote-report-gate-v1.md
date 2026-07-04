# Remote Report Gate v1

**Status:** `MINIMAL_CHARTER`
**Mode:** `HUMAN_INVOKED` / `NOT_AUTOMATED`

## Purpose

Define the minimal closeout gate for remote-facing MARS tasks.

This is not a parser, CI gate, runtime validator, or automatic enforcement mechanism.

## Required Closeout Fields

| Field | Required content |
|---|---|
| What was inspected | Exact remote surfaces, objects, or panels reviewed |
| What was changed | Exact mutations performed, or `none` |
| What was not changed | Explicit non-mutation statement for out-of-scope or blocked items |
| Evidence collected | Paths, receipts, hashes, or `none` with reason |
| Backup / rollback state | Backup taken / not required / missing; rollback readiness |
| Credential handling confirmation | Confirm secrets were not pasted into chat or committed |
| Screenshots / logs / receipts | List artefacts if any, or `none` |
| External state | Verified facts only; otherwise `SAFE UNKNOWN` |
| Next action | Exact next allowed action, or `stop` |
| Operator approval used | `yes` / `no` and what approval covered |

## Minimal Verdicts

| Verdict | Meaning |
|---|---|
| `PASS` | Required fields present; mutations match approved scope and evidence |
| `PASS_WITH_NOTES` | Usable handoff, non-blocking gaps listed |
| `FAIL` | Required field missing, scope exceeded, or unsupported PASS claim |
| `BLOCKED` | Mutation blocked by charter (unknown environment/class, missing approval, etc.) |
| `UNKNOWN` | Gate cannot be applied because evidence or scope is unclear |

## External State Rule

If a live remote fact was not verified in this task, mark it `SAFE UNKNOWN`.

Do not promote remote success to repo authority without captured evidence and persistence classification.

## Credential Rule

Closeout must confirm:

- no credentials or tokens were pasted into chat;
- no secrets were written into repo files;
- credentials remained operator-managed.

ROL is not a credential vault and does not store secrets.

## REPORT Is Not Proof By Itself

A completed REPORT is handoff evidence only.

It is not:

- automatic enforcement proof;
- Git persistence proof unless commit evidence exists;
- production control plane authority;
- permission for further remote work beyond the stated next action.

## Compatibility

Use with:

- `templates/remote-task-starter-v1.md`
- `contracts/remote-operations-charter-v1.md`
- AQ report quality gate when programme tasks also use Agent Quality
