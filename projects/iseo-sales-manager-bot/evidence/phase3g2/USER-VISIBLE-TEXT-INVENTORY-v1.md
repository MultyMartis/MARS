# User-visible text inventory

**Phase:** 3G.2  
**Status:** FILLED — live acceptance + registry  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Source

- Registry: `implementation/USER-VISIBLE-TEXT-REGISTRY-v1.md` (S01–S26)
- Live samples: Storage incoming `COMMAND-ACCEPTANCE.json` textSurfaces (sanitized; display nickname rewritten to MOD_A)
- Pre-patch forensic: Storage incoming `FORENSIC-TEXT-INVENTORY.json` (command matrix present)

## Surfaces S01–S26

| ID | Surface | Live sample / note (sanitized) | Status |
|----|---------|--------------------------------|--------|
| S01 | `/start` Admin | `INTLSEO Sales Manager готов к работе.` + Admin access + `ИИ: выключен` + `Напоминания: выключены` + `/reply_profiles` tip | current |
| S02 | `/start` moderator | Same greeting; moderator access; `/my_reply_profile` in basics | current |
| S03 | `/help` Admin | Explicit template; full reply-profile block with `<номер>` placeholders | current |
| S04 | `/help` moderator | Among profile cmds: only `/my_reply_profile` | current |
| S05 | `/my_status` | Personal ACCESS_CONTROL status only (unchanged contract) | current |
| S06 | `/status` `/health` `/config` | Non-secret; Russian labels; `/config` allowlisted keys | current |
| S07 | AI commands/status | `/ai_status`: `Состояние: выключен`; no provider leak | current |
| S08 | `/stats` | Epoch **05.08.2026**; authoritative sheet **LEADS** | current |
| S09 | `/last_error` | Sanitized summary only | current |
| S10 | `/leads` archive | Buttonless archive cards | current |
| S11 | `/lead_history` | Human event labels | current |
| S12 | Pending view | `/pending_count` `/pending_leads` | current |
| S13 | Reminder status/config | Status readable by staff; config Admin-only in help | current |
| S14 | Delivery cmds | Counts/names only | current |
| S15 | Moderator registry | Opaque codes; no raw IDs | current |
| S16 | Reply list/get | Number-based `/reply_profiles` `/reply_profile N` | current |
| S17 | Name set/enable/disable | Number syntax; Admin-only mutations | current |
| S18 | `/my_reply_profile` | Self view for Admin+moderator | current |
| S19 | Lead card body | UX-v1 layout + INTLSEO first-contact | current |
| S20 | Customer `<pre>` | `reply_sender_name` only (Михаил for MOD_A) | current |
| S21 | Manager guidance | Tip block outside client copy | current |
| S22 | Missing-name warning | Fail-closed manager warning | current |
| S23 | Lifecycle toasts | Shared status (3D.8.x) | current |
| S24 | Reminder Telegram body | Engine OFF — no production send | deferred-live |
| S25 | Unknown/deny | Fixed Russian deny / unknown | current |
| S26 | Role grant/revoke notices | Access ≠ name mutation | current |

## Result

- [x] Inventory filled against registry + live acceptance surfaces
- [x] Nickname display cue rewritten to label MOD_A in evidence samples
