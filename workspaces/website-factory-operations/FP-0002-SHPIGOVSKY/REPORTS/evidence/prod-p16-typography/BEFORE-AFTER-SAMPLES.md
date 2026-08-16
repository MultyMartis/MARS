# REPRESENTATIVE BEFORE/AFTER SAMPLES — PROD-P16

From dry-run (stored → render transform preview). **Stored values not mutated.**

## Home CTA (`#4` / `home_cta_text`)

Before: `Опишите вашу ситуацию в форме заявки, и мы расскажем, как сможем помочь`  
After: `Опишите вашу ситуацию в форме заявки, и мы расскажем, как сможем помочь`

## Home recovery intro heading

Before: entity `&nbsp;` / `&mdash;` mix  
After: Unicode NBSP + em dash (idempotent with already-typographed source)

## Privacy policy page content (`#3`)

Entity NBSP normalized to Unicode in text nodes; HTML tags preserved.

Full set: `TYPOGRAPHY-DRY-RUN.json` → `samples` / `changes`.
