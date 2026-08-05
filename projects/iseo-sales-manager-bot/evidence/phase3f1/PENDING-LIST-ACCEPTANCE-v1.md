# PENDING LIST ACCEPTANCE v1

**Command:** `/pending_leads [page] [test]` (staff — active Admin or active moderator). `/pending_leads_test` is the Admin-only explicit test-inclusive variant.

## Reply shape

`formatPendingListReply(pageResult)` renders, per item:

```
N. <age> · <client name>
<service> · <website>
<request summary>
Черновик ответа: готов|нет

Страница P из PC · всего T
```

Zero state: `Необработанных заявок сейчас нет.`

All dynamic text is HTML-escaped (`escHtml`) before insertion — no raw `<`, `>`, `&` from lead content can break Telegram's HTML parse mode (harness #14).

## Argument parsing

`parsePendingLeadsArgs(args)` accepts an optional page number and an optional `test` token in either order; any other token is a usage error. `test` is honored only when the caller is Admin (enforced by `authorizePendingCommand`, not by the parser itself — see [COMMAND-AUTHORIZATION-v1.md](COMMAND-AUTHORIZATION-v1.md)).

## Message length

Telegram HTML message length for a full default page (5 items) stayed under 3500 characters in the fixture snapshot (harness #15) — comfortably inside Telegram's 4096-character limit.

## Live acceptance

| Actor | Command | Result |
|---|---|---|
| Admin (active) | `/pending_leads` | PASS |
| Moderator (active) | `/pending_leads` | PASS |
| Admin (active) | `/pending_leads_test` | PASS (test row inclusion Admin-only) |
| Moderator (active) | `/pending_leads_test` | denied (admin-only config-class command) |
| Revoked | `/pending_leads` | denied |

## Harness coverage

Checks 1–15 (view + list rendering), X5 (reminder message reuse of the same list vocabulary) in `implementation/harness/phase3f1-harness.mjs`.

*Related: [PAGINATION-ACCEPTANCE-v1.md](PAGINATION-ACCEPTANCE-v1.md), [PENDING-COUNT-ACCEPTANCE-v1.md](PENDING-COUNT-ACCEPTANCE-v1.md).*
