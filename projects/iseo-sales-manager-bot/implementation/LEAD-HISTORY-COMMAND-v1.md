# LEAD HISTORY COMMAND v1

`/lead_history <номер> [страница]`

- Resolves `номер` from current `/leads` ordering over production LEADS
- Reads `LEAD_EVENTS` by stable lead relation
- Staff: active Admin + active moderator
- Invalid number → ask to refresh via `/leads`
- Human event labels only ([HUMAN-EVENT-LABEL-MAP-v1.md](HUMAN-EVENT-LABEL-MAP-v1.md)); missing timestamps stay explicit (`время не зафиксировано`)
- Phase 3F.2.2: `telegram_sent` humanized; raw codes never shown
