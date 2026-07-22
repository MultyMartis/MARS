# Problem Statement — PC14-FU03 HOTFIX03 Preface Gating

## Symptom (operator-visible)

After `/run`, the bot still sends an optimistic success preface:

```text
✅ Задача завершена

Результат готов. Отправляю материалы...
```

Later the final outcome may be either:

1. clean / repair-clean final materials, or
2. STRICT QA REJECT diagnostic (`blocked-dirty`).

On the reject path the preface is **false and misleading**: it claims completion and outgoing materials before the final result is known, and before materials are (correctly) blocked.

## HOTFIX02 context

HOTFIX02 (`65642ef2` apply · `1343b676` operator smoke) fixed Telegram plain-safe reject delivery. Operator smoke task `seo20260720182937io0c5y` (2026-07-21 01:29–01:31 local):

- STRICT QA REJECT delivered (PASS).
- Telegram 400 entity parse did **not** repeat.
- Raw `*` in reject body = 0.
- `/locks` → no active tasks; `/health` OK.
- Decision: `PC14_FU03_HOTFIX02_OPERATOR_SMOKE_PASS`.

False Status Complete preface was **explicitly deferred** to HOTFIX03 and does **not** fail HOTFIX02.

## Structural cause (committed evidence)

Shared final send chain (clean and reject):

`Format* → Take First Item → Status Complete → Restore Format Run Items → Close Lock Before Sending → Restore Format Run Items After Lock → Parse Mode → Send Telegram Run`

`Status Complete` is an HTML `editMessageText` **upstream** of restore / lock / parse / send. Its text is a **static success string**, independent of whether `Format Run Pipeline` or `Format Strict Reject Message` prepared the payload. Reject path therefore always announces success before the reject diagnostic.

Primary target node: **`Status Complete`**.  
`Status Final` is a progress edit (`⏳ … Готовим итоговый результат…`) and is not the false-success claim; leave unless sandbox shows otherwise.

## Desired outcome

- Do not send success-preface before final outcome is known.
- Reject / blocked-dirty: reject-safe or blocked wording only (no «Отправляю материалы…»).
- Clean / repair-clean: success wording allowed only when that branch is selected.
- Preserve HOTFIX02 send safety, HOTFIX01 restore, PC-07 Close Lock mapping, TZ HOTFIX01, memory append, lock close, credentials, side-effect states.
- Sandbox-first; production apply only after harness evidence.
