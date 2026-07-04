# Remote Operations Charter v1

**Status:** `MINIMAL_CHARTER`
**Mode:** `HUMAN_INVOKED` / `NOT_AUTOMATED`

## Purpose

Define the minimal normative contract for human-supervised remote operations in MARS.

This charter is documentation discipline only. It is not a runtime, not a connector, not a credential vault, and not a production control plane.

## Target System Identity

Every remote task must identify:

- system name / label;
- platform family (hosting, FTP/SFTP, CMS admin, WordPress, OpenCart/ocStore, DB/phpMyAdmin, API, n8n/MetaBOT, remote files, other);
- URL or host label **without secrets**;
- owner / operator contact when known;
- programme consumer when applicable (WPilot, OCPilot, MetaBOT, EAR, other).

If target identity cannot be stated, stop with `SAFE UNKNOWN`. Do not mutate.

## Environment Classification

| Class | Meaning |
|---|---|
| `prod` | Live production surface |
| `dev` | Development / non-production surface |
| `stage` | Staging / pre-production surface |
| `unknown` | Environment not verified |

**Rule:** `unknown` environment **blocks mutation**.

Read-only inspection of an `unknown` environment still requires operator approval and must not escalate into writes.

## Allowed Actions

Allowed only when all of the following are true:

- target identity is known;
- environment is known (`prod` / `dev` / `stage`);
- action class is known and not `UNKNOWN`;
- allowed scope is exact;
- forbidden scope is explicit;
- credentials remain operator-managed and are not pasted into chat;
- backup/rollback plan exists for any write or destructive class;
- operator approval is present for the requested mutation class;
- stop conditions are checked.

Allowed action examples (only when chartered):

- read-only inspection of a named remote surface;
- low-risk write on a non-production surface with approval;
- content or config change within exact scope and approval;
- evidence capture (screenshots, logs, receipts) without secret leakage.

## Forbidden Actions

- Any remote mutation when environment is `unknown`.
- Any remote mutation when action class is `UNKNOWN`.
- Credential discovery, extraction, storage, or pasting into chat/agent context.
- Automated remote mutation without human operator approval for that task.
- Production changes without explicit operator approval.
- Broad or unbounded remote scope ("fix the site", "update everything").
- Destructive change without backup/rollback and explicit approval.
- Treating this charter as blanket permission for live systems.
- Replacing WPilot / OCPilot / MetaBOT / EAR programme authority.

## Credential Boundary

- Credentials and tokens are **operator-managed**.
- Agents must **not** request secrets into chat.
- Agents must **not** invent, store, or commit credentials.
- ROL is **not** a credential vault.
- Token/path references may name local operator-only locations when already established by a programme, but values must never appear in repo docs or chat.
- If credentials are missing, stop with `NEED HUMAN APPROVAL` / `SECURITY RISK` — do not improvise access.

## Backup / Rollback Requirement

Before any write or destructive class:

- state backup method and location class (operator-managed, programme backup path, host panel backup, DB export, etc.);
- state rollback method;
- state who can execute rollback;
- if backup/rollback cannot be stated, **block mutation**.

`READ_ONLY` may proceed without backup only when no mutation is performed.

## Evidence Requirement

Remote tasks must define evidence to collect, for example:

- what was inspected;
- what was changed;
- what was not changed;
- screenshots / logs / receipts when available;
- backup/rollback state;
- credential handling confirmation (no secrets in chat/repo);
- external state `SAFE UNKNOWN` when not verified.

Evidence classification follows `governance/mars-evidence-persistence-discipline-v1.md`. Live remote proof is `REMOTE_ONLY` until captured and referenced.

## Stop Conditions

Stop immediately when:

- target identity is incomplete;
- environment is `unknown` and mutation is requested;
- action class is `UNKNOWN` and mutation is requested;
- operator approval is absent for mutation;
- credentials are requested into chat;
- backup/rollback is missing for write/destructive classes;
- scope is unbounded;
- production status is unknown for a live surface;
- evidence cannot be produced for a PASS claim;
- security risk is detected.

Stop outputs: `SAFE UNKNOWN`, `NEED HUMAN APPROVAL`, or `SECURITY RISK`.

## HITL / Operator Approval

Remote mutation requires human-in-the-loop operator approval for the exact task.

Approval must cover:

- target system;
- environment;
- action class;
- allowed scope;
- backup/rollback acceptance.

Absence of approval blocks mutation. This charter does not create an autonomous operator.

## Remote Mutation Classes

| Class | Meaning |
|---|---|
| `READ_ONLY` | Inspect only; no remote write |
| `LOW_RISK_WRITE` | Narrow, reversible, non-destructive write on a known non-critical surface |
| `CONFIG_CHANGE` | Configuration / settings change |
| `CONTENT_CHANGE` | Content / media / copy change |
| `CODE_CHANGE` | Theme, plugin, template, or remote code change |
| `DATA_CHANGE` | Database or structured data change |
| `DESTRUCTIVE_CHANGE` | Delete, overwrite, reset, irreversible, or broad destructive action |
| `UNKNOWN` | Action class not verified |

## Blocking Rule

**`UNKNOWN` environment or `UNKNOWN` action class blocks mutation.**

No remote write, config, content, code, data, or destructive action may proceed under either unknown.
