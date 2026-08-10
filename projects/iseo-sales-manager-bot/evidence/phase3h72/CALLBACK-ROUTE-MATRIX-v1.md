# CALLBACK ROUTE MATRIX

| Transition | Ack |
|---|---|
| pending→processed | Лид отмечен как обработанный. |
| pending→spam | Лид отмечен как спам. |
| processed→pending | Лид возвращён в обработку. |
| spam→pending | Лид возвращён в обработку. |
| already pending reopen | Заявка уже находится в обработке. |
| already processed | Заявка уже отмечена как обработанная. |
| already spam | Заявка уже отмечена как спам. |
| not found | Заявка не найдена в рабочем реестре. Обратитесь к администратору. |
