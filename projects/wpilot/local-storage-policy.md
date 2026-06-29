# WPilot Local Storage Policy

**Classification:** local-only operational storage policy.
**Chat type:** Plugin Engineering + Governance.
**Active lane:** B.
**Status:** documentation policy; not runtime proof.

## Purpose

WPilot local operational storage is unified under the MARS repository working root:

`X:\AI MARS`

This replaces the older separate local-root concept for WPilot operator workflows.

The target local-only structure is:

```text
X:\AI MARS
├─ backups/
│  ├─ wpilot/
│  ├─ github/
│  ├─ exports/
│  └─ temporary/
├─ local/
│  ├─ tokens/
│  ├─ sites/
│  └─ runtime/
```

These folders are operational support folders for the local operator machine. They are not source-pack content, runtime proof, commit targets, public artifacts, or evidence of autonomous runtime.

## Git Boundary

The root `.gitignore` must exclude:

- `/backups/`
- `/local/`

Nothing under those folders should be committed, exported as source-pack content, attached to public reports, or treated as canonical repository documentation.

Only sanitized examples may live in tracked documentation paths, such as:

- `projects/wpilot/runtime-local.example/tokens.example.json`
- `projects/wpilot/runtime-local.example/sites.example.json`

## Local Token Storage Policy

Per-site WPilot tokens may be stored only in local operator storage:

- `X:\AI MARS\local\tokens\`

### MARS Token Standard (canonical)

| Field | Value |
|-------|-------|
| **Canonical storage root** | `X:\AI MARS\local\tokens\` |
| **Canonical DEV token file** | `X:\AI MARS\local\tokens\wpilot-dev-gktriumph.token` |
| **Site alias** | `dev-gktriumph` |
| **REST auth header** | `X-WPilot-Token` |
| **Current DEV site** | `https://dev.gktriumph.ru` |
| **Registration sync** | 2026-06-19 — [reports/wpilot-token-registration-sync-report.md](reports/wpilot-token-registration-sync-report.md) |

This file is the **single canonical operator token source** for DEV REST auth. Runtime docs, contracts, runbooks, and release-candidate specs must reference this path — not sprint evidence copies.

Token files contain **plaintext token only** (single value per file). Do not commit token files, copy token values into reports, or store tokens in the WordPress database beyond the hashed credential.

Rules:

- Store plaintext tokens only if the operator explicitly accepts local-machine risk.
- Prefer OS credential storage or an external password manager when available.
- Never copy real tokens into markdown, reports, templates, screenshots, commits, issue text, or chat transcripts intended for repository use.
- Never place real tokens in `projects/wpilot/runtime-local.example/`.
- Rotate or revoke a token if it is accidentally exposed.
- Record only sanitized token metadata in docs, such as site alias, token status, creation/rotation date, and revocation status.

## Site Metadata Storage Policy

Local site connection metadata may be stored under:

- `X:\AI MARS\local\sites\`

Allowed local fields:

- site alias;
- DEV/test confirmation state;
- WordPress base URL;
- REST namespace;
- local token reference name;
- human owner;
- last verified timestamp;
- safe notes that do not expose secrets.

Disallowed local fields for tracked docs:

- real tokens;
- passwords;
- cookies;
- SSH keys;
- API keys;
- recovery codes;
- database passwords;
- `wp-config.php` values;
- database dumps.

## Backup Storage Policy

Operator-managed WPilot backups may be staged under:

- `X:\AI MARS\backups\wpilot\`

Recommended local layout:

```text
X:\AI MARS\backups\wpilot\
├─ site-alias\
│  ├─ yyyy-mm-dd-hhmm-pre-change\
│  ├─ yyyy-mm-dd-hhmm-post-change\
│  └─ rollback-snapshots\
```

Rules:

- Backups are local operational materials, not repository artifacts.
- Backup archives, database dumps, `wp-config.php`, uploaded media copies, and secret-bearing screenshots must remain ignored by git.
- Backup names should include site alias, timestamp, and purpose without exposing credentials or private client data.
- Backup integrity, retention, and restore viability remain external-system facts until verified by the operator.

## Rollback Snapshot Storage

Rollback snapshots may be stored under:

- `X:\AI MARS\backups\wpilot\<site-alias>\rollback-snapshots\`

Rollback snapshots should be scoped to the approved target where possible:

- page/post before-state export;
- child theme CSS before-state copy;
- approved test-file before-state copy;
- operator note with restore owner and verification step.

Rollback snapshots must not become a substitute for hosting-panel backups, database backups, or human rollback planning.

## Cursor Token Handoff Workflow

When Cursor or an operator needs to use a WPilot token:

1. The human administrator generates or rotates the token in WordPress admin.
2. The plaintext token is shown once by WordPress and copied by the human operator into approved local secret storage.
3. The tracked repository records only sanitized metadata and the local reference name.
4. Cursor may be told the local reference name, site alias, endpoint, and intended operation.
5. Cursor must not print, persist, or commit the token value.
6. After the run, the operator decides whether to revoke, rotate, or keep the token.

Example safe handoff:

```text
site_alias: dev-gktriumph
token_file: X:\AI MARS\local\tokens\wpilot-dev-gktriumph.token
auth_header: X-WPilot-Token
site_url: https://dev.gktriumph.ru
operation: read-only site inspection
environment: DEV/test confirmed by operator
```

Legacy reference-name form (still valid for metadata-only docs):

```text
site_alias: dev-example
token_ref: local/tokens/dev-example.wpilot-token.json
operation: read-only site inspection
environment: DEV/test confirmed by operator
```

## Missing Token Operational Flow

If a required token is missing:

1. Stop authenticated WPilot work.
2. Do not guess, reconstruct, search git history, or ask Cursor to recover the token.
3. Ask the human WordPress administrator to generate or rotate a token.
4. Store the new token only in approved local operator storage.
5. Update sanitized local site metadata if needed.
6. Resume only after DEV/test status, endpoint, and token reference are confirmed.

## No-Secret-In-Git Rules

Never commit:

- `X:\AI MARS\local\`
- `X:\AI MARS\backups\`
- real token files;
- `.env` files;
- WordPress credentials;
- Beget/hosting credentials;
- database dumps;
- backup archives;
- `wp-config.php`;
- screenshots or logs exposing secrets, cookies, account IDs, personal data, or auth headers.

Accidental secret exposure is a security incident. Stop copying the value, notify the operator, rotate or revoke the exposed credential, and follow the operator's remediation instructions.

## SAFE UNKNOWN

- Whether the operator will use filesystem token files, OS credential storage, or an external password manager is unknown until chosen per machine.
- Backup restore behavior, retention, and integrity are unknown until verified in Beget/WordPress or the relevant external system.
- Exact WPilot token file schema is not a runtime contract until a separate implementation task defines it.
- The presence of `backups/` or `local/` on disk does not prove a WPilot runtime, autonomous bridge, or deployed integration exists.
