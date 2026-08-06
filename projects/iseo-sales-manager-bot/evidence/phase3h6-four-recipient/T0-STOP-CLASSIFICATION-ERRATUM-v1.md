# T+0 STOP CLASSIFICATION ERRATUM — Phase 3H.6

See also: `reports/ERRATUM-iseo-sales-manager-bot-final-pre-ai-soak-t0-recipient-classification-v1.md`

## Original verdict

`SOAK T+0 STOP — PRODUCTION INVARIANT VIOLATION`

## Corrected verdict

`SOAK T+0 INVALIDATED — OPERATOR-APPROVED RECIPIENT SET CHANGED FROM 3 TO 4`

## Why

Observed technical facts were real (MOD_C active, 4-recipient fanout). The **interpretation** as spontaneous/unauthorized reactivation was incorrect given operator-confirmed intentional restoration via `admin_command` / `moderator_add`.
