# CLEAN-LEAD-END-TO-END-v1

**Phase:** 3D.1  
**Status:** **PENDING** — operator new test not observed in readiness window

## Done before observe

- Parser repair live (`sm-parser-v3.1`)
- Exactly-once / idempotency guard preserved
- Operator readiness Telegram notice sent (exact charter text)
- Malformed prior message left terminal (PROCESSED) — not auto-replayed

## Observe window

| Metric | Value |
|--------|-------|
| Window | ~10 minutes |
| Empty polls observed | 165 route samples / 19 poll cycles |
| New lead chains | **0** |
| Telegram cards | **0** |
| AI provider calls | **0** |
| Dual-active risk | **no** |

## Required checklist (awaits operator submission)

- [ ] Email delivered and eligible
- [ ] Exactly one Operational processing chain
- [ ] Fields extracted (name/contact/site/audit)
- [ ] One RAW + one CLEAN business row
- [ ] One Telegram card; no duplicate across ≥3 later polls
- [ ] `duplicate_status=new` (or justified)
- [ ] Valid quality; manual-copy reply; no contact clarification when contact present
- [ ] No synthetic footer; no internal IDs
- [ ] No automatic client response; AI = 0
- [ ] PROCESSED + incoming removed after Telegram success
