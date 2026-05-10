# Intake workflow

**Classification:** part of the **external multi-workflow** MetaBOT system.  
**Evidence in this repo:** none (documentation only).

---

## Intended responsibilities

- Receive user input from **Telegram** (commands and message bodies).
- Parse command names and arguments (e.g. `from:task_id`, `--strict`).
- Attach or forward **user metadata** available from Telegram (`user_id`, `username`, `first_name`, `last_name`) — see [user-metadata.md](user-metadata.md).
- Route work toward the **Worker** (and optionally **Admin**) — **mechanism SAFE UNKNOWN** (sub-workflow, HTTP, queue, shared row).

---

## Out of scope (for this doc)

- **Node-level** n8n design.
- **Credential** configuration.

---

## SAFE UNKNOWN

- Which commands are fully handled inside Intake vs delegated immediately to Worker.
- Rate limiting or flood protection at intake — **not** described here.
- Whether **Intake** writes any **Sheets** rows directly or only via Worker.

---

*See [workflow-map.md](workflow-map.md), [telegram-commands.md](telegram-commands.md).*
