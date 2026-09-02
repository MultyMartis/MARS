# iSEO Sales fixtures

**Synthetic only.** Data under this folder is for local schema/constraint/permission tests.

- No production dumps
- No real PII (use `example.com`, synthetic phones like `79001234567`)
- No bot tokens, OAuth, or chat secrets

Entry point: [`synthetic_v1.sql`](synthetic_v1.sql) — apply after `database/` migrations (see `tests/iseo_sales/01_schema_apply.sh`).
