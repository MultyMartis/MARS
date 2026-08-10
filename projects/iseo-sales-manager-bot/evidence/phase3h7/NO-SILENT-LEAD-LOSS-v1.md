# NO SILENT LEAD LOSS — Phase 3H.7

## Pre-patch
Gmail auth failures were written as `telegram_delivery_failed`, hiding the real stage.

## Post-patch
Gmail auth failures append `gmail_read_failed` / stage `gmail_read` (proof execution 27427).

## Remaining risk
While OMail OAuth remains invalid, **all** new form leads are lost at fetch — errors are now visible, but intake is still down until reauth.
