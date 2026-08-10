# CALLBACK ACKNOWLEDGEMENT CONTRACT — iseo-lead-callback-ack-v1.0

One recognized callback → one route → ≤1 transition → exactly one user-visible acknowledgement.

## Required texts
- pending→processed: Лид отмечен как обработанный.
- pending→spam: Лид отмечен как спам.
- processed|spam→pending: Лид возвращён в обработку.
- already pending reopen: Заявка уже находится в обработке.
- already processed: Заявка уже отмечена как обработанная.
- already spam: Заявка уже отмечена как спам.
- not found: Заявка не найдена в рабочем реестре. Обратитесь к администратору.

## Hard rules
- No fallthrough after unknown_lead
- Aggregate Card Sync Result must not overwrite semantic ack with processed default
- acknowledgements=1 per execution
