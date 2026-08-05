# DAMAGED CONTACT UX v1

## Target

- Next step once: `Проверить контактные данные.`
- Suppression once: `⚠️ Готовый ответ не сформирован: нет надёжного способа связи.`
- `first_reply_ready=false`
- No copy block
- No duplicated warnings
- Known audit intent (`нужен аудит`) → missing labels like `контакт, фокус аудита` — **not** bare `контакт, задача`

## Live (fixture `PHASE_3E2_1_G_DAMAGED_CONTACT_UX` retry)

| Field | Value |
|-------|-------|
| ready | false |
| missing | контакт, фокус аудита |
| warnCount | 1 |
| hasCopy | false |
| theme | vague_service |
| service | Audit |
