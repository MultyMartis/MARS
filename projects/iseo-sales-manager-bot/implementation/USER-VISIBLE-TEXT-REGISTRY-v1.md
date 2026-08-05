# USER-VISIBLE TEXT REGISTRY v1

**Phase:** 3G.2 (+ 3G.2.1 guard)  
**Purpose:** inventory of Telegram / operator-visible text surfaces for audit and acceptance  
**Authority for wording:** [TELEGRAM-TEXT-CONTRACT-v2.md](../architecture/TELEGRAM-TEXT-CONTRACT-v2.md)

---

## Surfaces

| ID | Surface | Primary owner | Role audience | Contract refs | Notes |
|----|---------|---------------|---------------|---------------|-------|
| S01 | `/start` Admin | Admin.dev | Admin | TEXT-CONTRACT-v2 · ADMIN-COMMAND | INTLSEO ready + AI/reminders OFF |
| S02 | `/start` moderator | Admin.dev | Moderator | TEXT-CONTRACT-v2 | Includes `Имя в ответах` (3G.2.1) |
| S03 | `/help` Admin | Admin.dev | Admin | ROLE-AWARE-HELP-v2 | Explicit template; includes profiles; never silent |
| S04 | `/help` moderator | Admin.dev | Moderator | ROLE-AWARE-HELP-v2 | Only `/my_reply_profile` among profiles |
| S05 | `/my_status` | Admin.dev | public+staff | ADMIN-COMMAND | Personal only |
| S06 | `/status` `/health` `/config` | Admin.dev | Admin | ADMIN-COMMAND · TEXT-CONTRACT | `/config` safe summary fields (3G.2.1) |
| S27 | Command response guard fallback | Admin.dev | all recognized cmds | TEXT-CONTRACT-v2 §5 | Safe internal-error reply; no stack traces |
| S07 | AI commands/status | Admin.dev | Admin | AI-OFF-ON · TEXT-CONTRACT | Production OFF |
| S08 | `/stats` | Admin.dev | Admin | TEXT-CONTRACT | Epoch 05.08.2026 MSK; LEADS |
| S09 | `/last_error` | Admin.dev | Admin | TEXT-CONTRACT | Sanitized |
| S10 | `/leads` archive cards | Admin.dev | Admin+mod | TELEGRAM-UX-v1 | Buttonless |
| S11 | `/lead_history` | Admin.dev | Admin+mod | 3F.2.2 human labels | No raw codes |
| S12 | Pending view commands | Admin.dev | Admin+mod | PENDING-LEADS-VIEW | Read-only |
| S13 | Reminder status/config | Admin.dev | status: staff; config: Admin | PENDING-REMINDER | OFF in prod |
| S14 | Delivery commands | Admin.dev | Admin | 3D.7 | No IDs |
| S15 | Moderator registry cmds | Admin.dev | Admin | ACCESS_CONTROL | Opaque codes |
| S16 | Reply profile list/get | Admin.dev | Admin | REPLY-PROFILE-ADMIN-v2 | By number |
| S17 | Reply name set/enable/disable | Admin.dev | Admin | REPLY-PROFILE-ADMIN-v2 | No access side-effects |
| S18 | `/my_reply_profile` | Admin.dev | Admin+mod | REPLY-PROFILE-ADMIN-v2 | Self |
| S19 | Lead card body | Operational.dev | Admin+mod | TELEGRAM-UX-v1 · INTLSEO-FIRST-CONTACT | Multi-recipient |
| S20 | Customer copy `<pre>` | Operational.dev | (copied by manager) | INTLSEO · RECIPIENT-PERSONALIZED | `reply_sender_name` only |
| S21 | Manager guidance under tip | Operational.dev | manager | AI-MANAGER-ASSIST / templates | Not for client |
| S22 | Missing-name warning | Operational.dev | manager | TEXT-CONTRACT-v2 | Fail-closed copy |
| S23 | Lifecycle toasts/feedback | Admin.dev | Admin+mod | 3D.8.x | Shared status |
| S24 | Reminder Telegram body | Admin.dev | staff | PENDING-REMINDER | Engine OFF |
| S25 | Unknown/deny/error strings | Admin.dev | all | ADMIN-COMMAND · TEXT-CONTRACT | Fixed Russian |
| S26 | Role grant/revoke notices | Admin.dev | target user | 3D.6 | Access ≠ name |

---

## Classification

| Class | Meaning |
|-------|---------|
| **current** | Live wording must match TEXT-CONTRACT-v2 + role help v2 |
| **obsolete** | Username-token reply-profile addressing (pre-3G.2); substring-patched help |
| **deferred** | `/test_lead` advertising; AI ON assist live copy |

---

## Related evidence (stubs)

`evidence/phase3g2/USER-VISIBLE-TEXT-INVENTORY-v1.md` · `STALE-TEXT-AUDIT-v1.md` · `TEXT-CONTRACT-COVERAGE-v1.md`
