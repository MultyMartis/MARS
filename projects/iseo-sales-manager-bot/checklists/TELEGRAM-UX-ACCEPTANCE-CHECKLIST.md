# Telegram UX Acceptance Checklist

- [ ] Manager card is readable and concise.
- [ ] Card uses Russian action labels where required.
- [ ] Card does not expose secrets, stack traces, raw AI JSON, or debug dumps.
- [ ] `✅ Обработано` is visible and correctly bound.
- [ ] `🚫 Спам` is visible and correctly bound.
- [ ] `📄 Исходная заявка` is visible and correctly bound.
- [ ] Unauthorized user behavior is safe.
- [ ] Repeated processed callback is idempotent.
- [ ] Repeated spam callback is idempotent.
- [ ] Raw click does not mutate lifecycle.
- [ ] Telegram formatting is safe for special characters.
- [ ] Evidence is captured without raw PII.

