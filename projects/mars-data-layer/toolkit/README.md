# MARS DB Toolkit (iSEO Sales)

Closed, parameterized operation catalog for `app_iseo_sales`.

## Rules

- **Allowed:** named ops wrapping `SECURITY DEFINER` functions (`IseoSalesOps`).
- **Forbidden:** generic `execute_sql` / arbitrary query tools as a product surface.
- Secrets stay in n8n credentials / local secret contour — never in Git.

## Ops (Operational.v3.dev)

See `ALLOWED_OPS` in `ops_iseo_sales.py`. Primary commit path:

`process_gmail_inbound_commit` → then Gmail finalize (labels) only if `gmail_finalize_allowed=true`.

Delivery path:

`claim_pending_deliveries` → dry-run / worker send → `mark_delivery_result`.

## Role

Runtime role: `iseo_runtime` (least privilege). Do not use `mars_admin` / `mars_migrator` / `postgres` from n8n.
