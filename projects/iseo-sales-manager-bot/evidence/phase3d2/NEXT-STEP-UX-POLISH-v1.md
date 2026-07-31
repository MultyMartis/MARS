# NEXT-STEP-UX-POLISH v1

**Phase:** 3D.2  
**Node:** Deterministic Lead Processor (Operational.dev)

## Change

Replaced tautology:

`Можно готовить следующий шаг.`

With service-aware complete-lead guidance:

| Service | Next step |
|---------|-----------|
| Audit | Связаться с клиентом и уточнить детали аудита. |
| SEO | Связаться с клиентом и уточнить задачи по продвижению. |
| Other / generic | Связаться с клиентом и уточнить задачу. |

Preserved:

- missing-data clarification guidance;
- no-contact guidance;
- specialized repeat guidance unchanged elsewhere.

## Acceptance

Local formatter replay (no Telegram resend of the accepted production card):

```
Следующий шаг: Связаться с клиентом и уточнить детали аудита.
```

PASS. No tautology. No production card re-send.
