# FINAL LIVE DEFECTS v1 — Phase 3F.2.2

## Defect 1 — machine event label

| Field | Value |
|---|---|
| Surface | `/lead_history 1` |
| Observed (pre-repair) | `• время не зафиксировано — telegram_sent` |
| Expected | `• время не зафиксировано — заявка передана сотрудникам` |
| Root cause | `telegram_sent` absent from display map; fallback returned raw code |
| Status | **REPAIRED** in Admin.dev `Lead History Handler` |

## Defect 2 — broken `/help`

| Field | Value |
|---|---|
| Surface | Admin `/help` |
| Observed (pre-repair) | `/ai_o` merged with `/lead_history &lt;номер&gt; — история лидаn` |
| Expected | Separate lines; intact `/ai_on`; visible `/lead_history <номер>`; pending + reminder_status listed |
| Root cause | Unsafe substring insertion into `cmdHtml('/ai_on')` argument |
| Status | **REPAIRED** — full `helpReply` rebuild (Admin + moderator templates) |

## Non-defects (regression baseline)

- `/leads` processed card with service/comment/source — PASS (pre-patch live)
- `/pending_count` / `/pending_leads` zero — PASS
- `/reminder_status` OFF / 10:00 / Europe/Moscow — PASS
- Clean ledger counts 1/1/0/0 — unchanged by this polish
