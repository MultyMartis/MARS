# HARNESS RESULTS — Phase 3H.7.2

mandatory_pass: **true**

## Ack cases
- spam_applied: PASS (got: Лид отмечен как спам.)
- processed_applied: PASS (got: Лид отмечен как обработанный.)
- reopen_applied: PASS (got: Лид возвращён в обработку.)
- already_pending: PASS (got: Заявка уже находится в обработке.)
- already_spam: PASS (got: Заявка уже отмечена как спам.)
- already_processed: PASS (got: Заявка уже отмечена как обработанная.)
- not_found: PASS (got: Заявка не найдена в рабочем реестре. Обратитесь к администратору.)
- not_found_no_fallthrough: PASS (got: Заявка не найдена в рабочем реестре. Обратитесь к администратору.)

## Old bug proof
Pre-fix Aggregate would emit: `Лид отмечен как обработанный.` for reopen applied.

## Keyboard
```json
{
  "pending_has_processed": true,
  "pending_has_spam": true,
  "pending_has_reopen": false,
  "spam_has_reopen": true,
  "processed_has_reopen": true,
  "reopen_restores_pending": true
}
```

## Archive batches 3/5/10
- batch3: true
- batch5: true
- batch10: true
