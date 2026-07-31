# GMAIL CREDENTIAL BINDING v1

| Check | Result |
|-------|--------|
| OPS Gmail Fetch credential present | **yes** (name redacted) |
| OPS ↔ Sales-Manager-v2 fetch credential hash equal | **yes** |
| All OPS Gmail nodes same credential hash | **yes** |
| Bounded read-only query succeeds | **yes** (`in:anywhere`, `in:trash`, production label filter) |
| Stale credential causing zero reads | **not evidenced** (queries return mailbox data; production filter returns 0 eligible) |

Operator re-authorization did not change the binding identity vs v2 (hash parity held).
