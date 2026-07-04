# FP-0002 V9-06D8A Site Options Seed Report v1

**Date:** 2026-07-05  
**Task:** V9-06D8-A Site Options Seed  
**Verdict:** BLOCKED  
**Operator authorization:** YES (this task)

---

## Executive summary

Planning and safety gates for the first D8 mutation wave completed. Exact 16-field site options allowlist confirmed from ACF JSON and D8 planning. Proposed seed payload defines **11 writable** V9-static placeholder fields and **5 skipped** fields (operator URLs, legal, social). Dry-run verdict: **SAFE_TO_APPLY_EXACT_OPTIONS_ALLOWLIST**.

**Apply did not run.** MySQL/DB and HTTP runtime were unavailable. Zero database writes. Documentation and evidence committed to Git.

---

## Safety preflight

| Check | Result |
|---|---|
| Volume X: / AI WS | PASS |
| Branch mars/canonical-post-recovery | PASS |
| Local HEAD | `d98557fb234769ec0f12bdbf7e65dcff4f1961a0` |
| Remote HEAD | `d98557fb234769ec0f12bdbf7e65dcff4f1961a0` |
| Required HEAD | `989b97a912832f2d3e73de20e5e07aa34fc57c4a` |
| Ahead / Behind | 0 / 0 |
| Strict HEAD gate | **VARIANCE** — 1 commit ahead of D8 pin (descendant) |
| Foreign WIP | Present unstaged — not staged |
| Pre-existing staged | None |

---

## Authorization and scope

| Scope | Result |
|---|---|
| Runtime delivery | NOT_PERFORMED |
| Source changes | 0 |
| Runtime file writes | 0 |
| DB writes | 0 |
| Content writes | 0 |
| ACF page/meta writes | 0 |
| Options writes | 0 (planned 11) |
| Documentation/evidence | YES |

---

## Runtime and DB gate

| Check | Result |
|---|---|
| Runtime path exists | PASS |
| HTTP domain | FAIL (code 0) |
| wp-load.php | FAIL — database connection error |
| MySQL port 3306 | Not listening |

---

## Allowlist and payload

See `validation/v9-06d8a-site-options-seed/site-options-field-allowlist.json` and `proposed-site-options-seed-payload.json`.

**Writable (11):** organisation_name, phone_primary, phone_secondary, site_email, site_address, opening_hours, default_callback_title, default_button_label, default_secondary_button_label, global_cta_title, global_cta_text.

**Skipped (5):** map_link, social_links, legal_org_identifiers, default_callback_text, default_consent_text_reference.

All writable values traced to `workspaces/fp-0002-shpigovsky-v9/src/` — classified LOCAL_MVP_PLACEHOLDER.

---

## Mutation gates

| Gate | Result |
|---|---|
| DB checkpoint | FAIL — not created |
| Dry-run | PASS (planning) |
| Apply | NOT_PERFORMED |
| Post-seed verify | NOT_PERFORMED |
| Route smoke | NOT_PERFORMED |
| Olga admin UX | NOT_PERFORMED |

---

## Prepared apply tooling

Local helper (not staged to Git): `validation/v9-06d8a-site-options-seed/_site_options_seed_runner.php`

Modes: `identity | baseline | dry-run | apply | verify | all`

---

## Recommended next action

**OPERATOR_DECISION_REQUIRED** — start MySQL/Laragon stack, confirm HEAD pin policy, re-run D8-A apply phase.

---

## Evidence index

`validation/v9-06d8a-site-options-seed/` — full JSON pack + `final-verdict.json`

## Architecture

- `architecture/FP-0002-V9-06D8A-SITE-OPTIONS-SEED-PAYLOAD-v1.md`
- `architecture/FP-0002-V9-06D8A-SITE-OPTIONS-SEED-RESULT-v1.md`
- `architecture/FP-0002-V9-06D8A-OLGA-ADMIN-USABILITY-AFTER-SEED-v1.md`
- `architecture/FP-0002-V9-06D8A-ROLLBACK-READY-v1.md`
- `architecture/FP-0002-V9-06D8A-NEXT-STEP-RECOMMENDATION-v1.md`
