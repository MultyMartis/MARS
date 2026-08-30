# i-SEO Report Hub — Screenshot QA Triage Plan v0.1

**Next wave name:** `I-SEO Report Hub — Screenshot QA Triage 01`  
**Trigger:** оператор прислал скриншоты + замечания  
**This doc:** план triage — **без implementation** до старта волны

---

## Goal

Прочитать скрины и notes оператора, классифицировать замечания, собрать очередь правок для следующих implementation waves.

---

## Inputs required

1. Скриншоты по checklist (`iseo-hub-YYYYMMDD-##_….png`).
2. Замечания в формате [I-SEO-REPORT-HUB-SCREENSHOT-ISSUE-INTAKE-FORMAT-v0.1.md](I-SEO-REPORT-HUB-SCREENSHOT-ISSUE-INTAKE-FORMAT-v0.1.md).
3. (Опционально) короткий комментарий «что важнее всего».

---

## Triage steps

1. Inventory received files vs P0 list (missing = note).
2. Parse each issue → category + priority.
3. Split into buckets:

| Bucket | Meaning | Typical next wave |
|--------|---------|-------------------|
| **Quick UI fixes** | CSS/spacing/buttons/borders | small Impl wave |
| **Content / text fixes** | RU labels, copy, badges | text pass |
| **Product logic fixes** | wrong status, flow, empty state logic | charter if risky |
| **Deferred PDF / export** | PDF look, export 4 alignment | **after** UI polish; needs operator confirm |
| **Dangerous / separate charter** | finalize, apply write, share mutate, DB | explicit charter |

4. Produce implementation queue (ordered by priority + risk).
5. Propose first implementation wave name (e.g. `UI Screenshot Fixes Pack 01`).
6. **Do not implement** inside Triage 01 unless operator explicitly expands scope.

---

## Explicitly deferred until later

Per operator decision (Visual QA Preparation 01):

- PDF regeneration  
- New export HTML alignment implementation  
- Overwrite / replace export 4  
- Client preview → export/PDF pipeline  

These stay in **Deferred PDF / export** bucket even if screenshots mention PDF look.

---

## Expected Triage 01 outputs

- `product/I-SEO-REPORT-HUB-SCREENSHOT-QA-TRIAGE-RESULT-v0.1.md` (or similar)
- Classified issue table
- Implementation queue
- Closeout REPORT
- OPERATIONAL-INDEX update

---

## Stop conditions

- No screenshots received → Triage not started.
- Secrets/tokens in notes → redact; do not commit secrets.
- Request to mutate export/PDF during triage → refuse; park as deferred.
