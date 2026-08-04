# FIRST REPLY CONSISTENCY RULES v1

**IMPLEMENTED — Phase 3E.1.** Architecture: [FIRST-REPLY-RULES-v1.md](../../architecture/FIRST-REPLY-RULES-v1.md). See also evidence `evidence/phase3e1/FIRST-REPLY-CONSISTENCY-v1.md`.

- Reply использует resolved intent по утверждённому precedence.
- Не упоминает site, name, budget, deadline, channel или услугу, которых нет в semantic model.
- `explicitly_absent` site не превращается в просьбу «укажите адрес», если задача относится к созданию сайта.
- Alternative contact отражается только как доступный канал, не как сайт.
- При intent conflict reply остаётся нейтральным и просит уточнение.
- Manager-only notes, internal states и provenance не попадают в client copy.
- AI OFF template — baseline; будущий AI ON обязан проходить те же consistency checks и fallback.
- Ответ никогда не отправляется клиенту автоматически.