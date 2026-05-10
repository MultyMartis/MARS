# User metadata

Telegram provides user identity fields that MetaBOT can persist or pass through workflows for auditing, personalization, and support.

---

## Fields (already available in operations)

| Field | Typical source |
|-------|----------------|
| **user_id** | Telegram numeric id |
| **username** | `@handle` (may be empty) |
| **first_name** | Profile |
| **last_name** | Profile (may be empty) |

---

## Usage (intended)

- Attach metadata to **task** and **memory** rows where needed — **SAFE UNKNOWN** which columns store which field.
- Support **admin** troubleshooting (who ran `/run`, who holds a lock — **SAFE UNKNOWN** implementation).

---

## Privacy / governance

- Treat as **operational PII**; do not commit spreadsheets or exports with live user rows into MARS.
- **MARS** repo should only describe **field names** and **purpose**, not real values.

---

## SAFE UNKNOWN

- Retention and deletion policy per user.
- Whether GDPR / local privacy procedures apply to stored Telegram metadata — **organizational**, not documented here.

---

*See [telegram-commands.md](telegram-commands.md), [storage-layer.md](storage-layer.md).*
