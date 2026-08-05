# PENDING COUNT ACCEPTANCE v1

**Command:** `/pending_count` (staff — active Admin or active moderator).

## Contract

`formatPendingCountReply(view, opts)` renders:

- Zero state: `Необработанных заявок сейчас нет.`
- Non-zero: `Необработанных заявок: N` plus an age-bucket line (`до 2 часов: X · 2–24 часа: Y · старше суток: Z`, only non-zero buckets shown).
- Admin diagnostic addendum (`adminDiagnostics=true`): appends `Тестовых заявок: N` when test leads exist — Admin only, never shown to a plain moderator reply.

No PII, no lead IDs, no Telegram identifiers in the reply — counts and buckets only.

## Fixture snapshot result

Using `implementation/harness/phase3f1-harness.mjs` fixtures (business, tests excluded): **4** pending business leads (2 fresh SEO/website-development leads + 1 legacy-compatibility row + 1 missing-timestamp row); **5** total including the one excluded test fixture. The харness's own minimum-floor assertion (`fixtureBusinessExpectedMin`) requires **≥2**; the actual fixture set produces 4, which is honestly reported here rather than rounded down to the floor value.

| Counter | Value |
|---|---:|
| Business pending (fixture snapshot) | 4 |
| Test leads excluded from default view | 1 |
| Processed control excluded | 1 |
| Spam control excluded | 1 |
| With tests included (`/pending_leads_test`) | 5 |

## Live acceptance

`/pending_count` was exercised live for admin, moderator, and revoked identities:

| Actor | Expected | Result |
|---|---|---|
| Admin (active) | count reply | PASS — showed the live business pending count |
| Moderator (active) | count reply | PASS |
| Revoked | denied | PASS |

## Harness coverage

Checks 16–19 (authorization), X3–X4 (zero/non-zero reply shape) in `implementation/harness/phase3f1-harness.mjs`.

*Related: [PENDING-LIST-ACCEPTANCE-v1.md](PENDING-LIST-ACCEPTANCE-v1.md), [COMMAND-AUTHORIZATION-v1.md](COMMAND-AUTHORIZATION-v1.md).*
