# ERRATUM — Final pre-AI soak T+0 recipient classification

## 1. Original T+0 verdict

`SOAK T+0 STOP — PRODUCTION INVARIANT VIOLATION`

Document: `reports/REPORT-iseo-sales-manager-bot-final-pre-ai-soak-t0-v1.md`

## 2. Facts observed (unchanged)

- MOD_C became active after final soak T+0 (16:20 Europe/Moscow)
- MOD_C received a lead card (4-recipient fanout)
- Recipient fanout became four
- Profile-number evidence at the checkpoint may have been incomplete for MOD_C

## 3. Missing operator context at classification time

The T+0 stop report did not yet include the operator’s explicit confirmation that MOD_C restoration was intentional.

## 4. Operator clarification

- Operator personally restored MOD_C / Никита as a moderator
- MOD_C must remain active, receive cards, client name Никита
- Personalized replies explicitly enabled via `/reply_name_enable 4`
- Approved production recipient set is now **four**

## 5. Corrected interpretation

- Operator-approved staff restoration
- Intentional baseline change from three to four recipients
- **No** revoked-recipient security incident
- **No** unauthorized restoration

## 6. Corrected classification

`SOAK T+0 INVALIDATED — OPERATOR-APPROVED RECIPIENT SET CHANGED FROM 3 TO 4`

## 7. Consequences

- Previous three-recipient soak attempt is **invalidated** (not a security failure)
- New four-recipient soak required (Phase 3H.6)
- Phase 3I.1 remains blocked until a valid soak PASS

## 8. Historical preservation

This erratum does **not** delete or silently rewrite the original T+0 report. The original evidence remains; this document corrects the interpretation.
