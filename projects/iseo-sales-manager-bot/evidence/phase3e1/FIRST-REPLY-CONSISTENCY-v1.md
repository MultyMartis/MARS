# FIRST REPLY CONSISTENCY v1 — Phase 3E.1

**Architecture:** [FIRST-REPLY-RULES-v1.md](../../architecture/FIRST-REPLY-RULES-v1.md)  
**Harness:** H19–H21, H25, H41

## Accepted

- Valid site present → reply does not ask for site again.
- Explicit no-site → reply does not ask for existing site URL.
- Telegram/messenger contact never appears as website in card or reply facts.
- Request summary / reply contain only supported facts.
- Card states reply is not auto-sent to client.

## Rejected

- Inventing budget, deadline, or service not in semantic model.
- Putting manager notes / provenance into client copy.
