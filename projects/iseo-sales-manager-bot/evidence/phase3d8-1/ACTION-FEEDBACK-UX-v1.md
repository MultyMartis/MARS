# ACTION FEEDBACK UX v1

## Layers

1. **Early toast** — `answerCallbackQuery` (`Обрабатываю…` / malformed / deny)
2. **Durable** — card final status + Safe Telegram Reply final sentence

## Final card status block

```
✅ Обработан   |   🚫 Спам
Кем: сотрудник
Время: DD.MM.YYYY HH:MM МСК
```

No role IDs, hashes, or employee PII required on card.

## Initiator reply texts

See LIFECYCLE-MUTATION-CONTRACT-v1.md.
