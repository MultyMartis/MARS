# MARS Evidence Persistence Discipline v1

## Status

| Field | Value |
|---|---|
| **Status** | CURRENT SUPPLEMENT |
| **Purpose** | defines evidence classes and persistence rules for MARS reports, receipts and validation artefacts |
| **Relationship to Agent Quality** | uses AQ report quality rules, but adds persistence classification |
| **Relationship to Maturity Overlay** | supports maturity decisions by distinguishing evidence existence from persisted truth |
| **Relationship to Web-GPT sources** | Web-GPT sources may only be updated from accepted repo authority, not from unverified reports |
| **Relationship to parent chats** | parent chats may produce evidence; MASTER CORE classifies global impact when needed |

## Non-claims

- This discipline does not prove implementation.
- This discipline does not create automatic enforcement.
- This discipline does not make untracked files authoritative.
- This discipline does not authorize broad staging.
- This discipline does not authorize remote operations.
- This discipline does not replace programme parent-chat review.
- This discipline does not replace Git status verification.

## Core rules

1. **REPORT is not proof by itself.**
2. **REPORT plus file path is not proof of Git persistence.**
3. **Commit hash is proof of Git persistence only for the files included in that commit.**
4. **External evidence is not repo authority until referenced/classified in repo.**
5. **Untracked evidence is useful but must be labelled untracked.**
6. **Dirty working tree evidence is useful but must be labelled modified/uncommitted.**
7. **Storage evidence is external/bulk until indexed or referenced by repo authority.**
8. **Runtime evidence is external execution evidence, not governance authority.**
9. **Web-GPT chat memory is not source of truth.**
10. **SAFE UNKNOWN is required when persistence status is unclear.**

## Evidence classes

| Class | Name | Meaning |
|---|---|---|
| **E0** | CLAIM_ONLY | Agent/user/report states something, but no artefact path or proof |
| **E1** | CHAT_CONTEXT | Evidence exists only in chat or pasted report |
| **E2** | LOCAL_UNTRACKED | File exists locally but is untracked |
| **E3** | LOCAL_MODIFIED | Tracked file exists but has uncommitted modifications |
| **E4** | COMMITTED_REPO | Evidence is committed in Git |
| **E5** | STORAGE_EXTERNAL | Evidence exists in `X:\AI MARS STORAGE\` or other external/bulk storage |
| **E6** | RUNTIME_EXTERNAL | Evidence exists in `X:\MARS-Localhost\` or external runtime |
| **E7** | REMOTE_EXTERNAL | Evidence exists on live/remote system, hosting, CMS, API, FTP, DB or n8n |
| **E8** | OPERATOR_CONFIRMED | Operator explicitly confirms result, visual state, acceptance or business truth |
| **E9** | RECONCILED_AUTHORITY | Evidence is committed, linked, classified and accepted into current repo authority |

**Authority rule:** Only **E4** or **E9** can safely update repo-level current truth by default. **E5 / E6 / E7 / E8** can support decisions, but must be referenced and classified before becoming repo authority.

## Persistence status labels

Use exactly one primary label per evidence item (or `SAFE_UNKNOWN` when unclear):

| Label | Typical class |
|---|---|
| `CLAIM_ONLY` | E0 |
| `CHAT_ONLY` | E1 |
| `UNTRACKED_LOCAL` | E2 |
| `MODIFIED_UNCOMMITTED` | E3 |
| `COMMITTED` | E4 |
| `EXTERNAL_STORAGE` | E5 |
| `EXTERNAL_RUNTIME` | E6 |
| `REMOTE_ONLY` | E7 |
| `OPERATOR_CONFIRMED` | E8 |
| `RECONCILED_AUTHORITY` | E9 |
| `SAFE_UNKNOWN` | persistence or authority not proven |

## REPORT acceptance checklist

A REPORT affecting MARS authority must state:

- task id
- scope
- files created
- files changed
- files deleted
- commands run
- validation evidence
- git status before or after
- staged files if any
- commit hash if committed
- external evidence if any
- operator approval if required
- persistence status
- SAFE UNKNOWN if any uncertainty remains

This checklist extends AQ report-quality fields with **persistence status** and explicit Git/external classification. It does not replace programme-specific gates.

## Git persistence rule

- A committed report must include exact file paths and commit hash.
- If files were created but not committed, status is `UNTRACKED_LOCAL`.
- If files were edited but not committed, status is `MODIFIED_UNCOMMITTED`.
- If evidence is in Storage or Localhost, it is `EXTERNAL_STORAGE` or `EXTERNAL_RUNTIME`.
- If evidence is remote/live, it is `REMOTE_ONLY` until captured/referenced.
- Do not use `git add .` or `git add -A` to persist evidence.
- Stage only explicit task files.
- Do not stage foreign WIP.
- Do not commit unrelated receipts accidentally.

Commit hash proves Git persistence **only** for paths included in that commit. A REPORT text claiming “committed” without hash and path list is not Git proof.

## Authority promotion rule

Promotion path:

1. `CLAIM_ONLY` / `CHAT_ONLY`
2. → artefact path identified
3. → persistence status classified
4. → parent owner validates
5. → MASTER CORE reviews if global impact
6. → exact files committed or referenced
7. → lifecycle / registry / OPERATIONAL-INDEX updated if needed
8. → Web-GPT sources updated only after accepted repo authority

Do not skip classification. Do not promote project-local WIP to global MARS truth without owner validation and, when global impact exists, MASTER CORE review.

## Parent-chat handling

- Parent chat owns project-local WIP.
- MASTER CORE does not decide canonical project WIP alone.
- MASTER CORE may classify system-level impact.
- Parent reports must identify whether they are:
  - local project evidence
  - programme authority evidence
  - global MARS authority evidence
  - external operational evidence
  - historical evidence

Historical / incident paths (for example former `C:\`, `D:\`, `E:\` roots) may appear in evidence but are not current operational roots.

## Web-GPT source update prerequisite

Before updating `web-gpt-sources/`, confirm:

- repo authority file changed
- commit exists
- operator accepted current truth
- sync pack scope is clear
- old pack relationship is documented
- foreign WIP is protected
- source pack does not claim implementation beyond evidence

Web-GPT sources must not be updated from chat memory, untracked reports, or remote-only claims without repo reconciliation.

## Maturity impact

L-level increases require evidence.

| Level | Evidence expectation |
|---:|---|
| L0 / L1 | can be based on docs |
| L2 | requires structured contract/authority |
| L3 | requires template/gate/checklist |
| L4 | requires pilot proof or receipt |
| L5 | requires repeatability across task contexts |
| L6 | requires tool/helper/validator and human-invoked repeatability |
| L7 | requires automatic enforcement proof |
| L8 | requires production subsystem proof |

A REPORT without persistence classification cannot raise maturity alone. Evidence existence is not the same as persisted truth.

## Remote / external evidence rule

- Remote operations require separate ROL charter.
- Live CMS/hosting/DB/API/n8n evidence must be treated as `REMOTE_ONLY` unless captured and referenced.
- Screenshots, hashes, backup IDs, HTTP checks, admin saves, FTP logs and DB export receipts must be classified.
- Remote evidence must not be used to update Web-GPT sources directly without repo reconciliation.

This discipline does not authorize remote work.

## Storage / Runtime evidence rule

- `X:\AI MARS STORAGE\` is out-of-Git bulk storage.
- `X:\MARS-Localhost\` is runtime, not governance authority.
- Storage/Runtime evidence can support decisions but must be linked/classified in repo before becoming current MARS authority.
- Do not copy or index Storage/Runtime broadly without charter.

## Failure cases this prevents

- REPORT accepted as truth without files.
- Untracked report treated as committed.
- Remote success treated as repo authority.
- Roadmap treated as implementation.
- Build PASS treated as visual PASS.
- Cache treated as checkpoint.
- Storage artefact treated as current governance.
- Web-GPT source updated from chat memory.
- Foreign WIP accidentally staged.
- Parent project WIP promoted globally without owner review.

## Usage rule

Before accepting a REPORT, ask: **what evidence class is this?**

Before updating maturity, ask: **what proof persists?**

Before updating Web-GPT sources, ask: **what repo authority changed?**

Before committing, ask: **are only exact task files staged?**

Before globalizing a project lesson, ask: **did the parent owner validate it?**

Before remote claims, ask: **is there ROL authority and captured evidence?**

## SAFE UNKNOWN

- If evidence exists but persistence is unclear, mark `SAFE_UNKNOWN`.
- If a report references a file not verified on disk, mark `SAFE_UNKNOWN`.
- If a commit hash is missing, mark `SAFE_UNKNOWN` for Git persistence.
- If external system state is not freshly verified, mark `SAFE_UNKNOWN`.
- If parent ownership is unclear, mark `SAFE_UNKNOWN` and route to owner.

Do not invent persistence status. Prefer a lower evidence class and `SAFE_UNKNOWN` over false authority.
