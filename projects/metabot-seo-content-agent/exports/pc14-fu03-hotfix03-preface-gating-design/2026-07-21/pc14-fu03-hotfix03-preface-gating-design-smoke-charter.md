# PC14-FU03 HOTFIX03 — Future Operator Smoke Charter (design draft)

**Status:** Design draft only — **not** an authorization to run smoke now.  
**Depends on:** sandbox implementation PASS → production proposal → production apply → then this smoke.

## Goal

Prove that after HOTFIX03 production apply, reject/blocked-dirty `/run` does **not** show:

```text
✅ Задача завершена
Результат готов. Отправляю материалы...
```

before the STRICT QA REJECT diagnostic (or blocked status message).

## Suggested bait

Reuse HOTFIX02 bait class (forced table reason + banned stems) that yields `blocked-dirty`, unless a cleaner dedicated bait is chartered.

## Pass signals

1. No success-materials preface on reject path.
2. Reject diagnostic still delivered plain-safe (HOTFIX02 regression).
3. Raw `*` in reject body = 0.
4. `/locks` shows no active task after completion.
5. `/health` remains OK.
6. Clean-path check (separate run or fixture): success wording allowed only when materials actually go out.

## Fail signals

- Success preface still appears on reject.
- Reject diagnostic missing.
- Telegram 400 entity parse returns.
- Lock left active.
- HOTFIX01 restore / PC-07 / memory regressions.

## Constraints

No unsupervised `/run` from design task. Operator executes smoke only after apply charter.
