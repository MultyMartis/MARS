# Admin workflow

**Classification:** operational workflow within MetaBOT — **external** to MARS.

---

## Intended responsibilities

- **Housekeeping**: lock inspection (`/locks`), possibly stale lock cleanup coordination with Worker — **exact split SAFE UNKNOWN**.
- **Health-style** checks that touch **Google Sheets** or other dependencies — may trigger quota issues — [known-issues.md](known-issues.md).
- **Admin commands** (restricted users or roles) — specific list **SAFE UNKNOWN** in this repo; see [admin-operations.md](admin-operations.md) and [telegram-commands.md](telegram-commands.md).

---

## Relation to Intake / Worker

- **SAFE UNKNOWN** whether Admin shares the same Telegram bot with different authorization, or uses separate entrypoints.
- **SAFE UNKNOWN** whether Admin invokes Worker via execute-workflow or only mutates Sheets that Worker reads.

---

## SAFE UNKNOWN

- Full command matrix for admins vs standard users.
- Audit logging destination for admin actions.

---

*See [workflow-map.md](workflow-map.md), [admin-operations.md](admin-operations.md).*
