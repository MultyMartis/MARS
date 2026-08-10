# WRONG REOPEN ACK FORENSIC — Phase 3H.7.2

## Verdict
Root cause **proven** in live Admin workflow node `Aggregate Card Sync Result`.

## Operator symptom
Terminal lead reopened → card correctly showed pending + «Возвращено в обработку», but bot confirmation said:
`Лид отмечен как обработанный.`

## Trace (expected pipeline)
1. Telegram callback `sm:r:<token>`
2. Normalize Command → action=`reopen`
3. Handle Callback Action → mutate terminal→pending, `answer_text` reopen-ish
4. Expand Card Sync Copies → edit tracked cards
5. **Aggregate Card Sync Result → OVERWRITES ack**
6. Prepare Callback Answer / Safe Telegram Reply → user-visible text

## Exact root cause
```
if (h.callback_outcome === 'applied') {
  if (failed > 0) { /* partial */ }
  else if (h.new_status === 'spam') { answer = spam; }
  else { answer = 'Лид отмечен как обработанный.'; } // ← reopen new_status=pending lands here
}
```

Handle mutation is correct (status pending). Acknowledgement builder after sync is wrong.

## Live scan counters
- Admin executions scanned: 50
- Callback-related rows captured: 8
- Reopen applied observed in window: 2
- Wrong reopen→processed final ack in window: 2

## SAFE UNKNOWN
If operator reopen occurred outside the last 50 Admin executions window, exact execution id may be absent from this scan; code-path proof remains definitive.

No PII in this evidence.
