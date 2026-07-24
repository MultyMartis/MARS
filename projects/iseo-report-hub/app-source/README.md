# i-SEO Report Hub — Runtime Scaffold

## Status

**Phase 0 scaffold only.** This tree is a minimal custom PHP + SQL/MySQL runtime placeholder. It is **not** a product implementation.

| Fact | State |
|------|-------|
| Platform | Custom **PHP + SQL/MySQL** |
| WordPress | **Not used** as runtime or source of truth |
| Framework / Composer | **None** in this phase |
| Database | **Not created** |
| Migrations | **None** |
| Vhost / hosts | **Not created** by Phase 0 |
| Secrets | **None** — `.env.example` placeholders only; no `.env` |

## Local identity

| Item | Value |
|------|-------|
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub` |
| Intended domain | `iseo-report-hub.test` |
| DB candidate | `iseo_report_hub_dev` |
| PHP target | **8.3.30** (Laragon verified) |

Docs and specs remain in the MARS Active Brain:

`X:\AI MARS\projects\iseo-report-hub\`

## How to review manually

1. Inspect files under this runtime path.
2. Open `public/index.php` through a **local server mapping once configured** (vhost/hosts are **manual next steps**, not done here).
3. Open `public/health.php` for a PHP/extension sanity page (no DB connection).
4. PHP built-in server is **optional** and only if the operator explicitly chooses later, for example from `public/`:

   `php -S 127.0.0.1:8080`

   Domain `iseo-report-hub.test` may **not** resolve until hosts/vhost are configured.

## Secrets policy

- Do **not** commit `.env` or `.env.local`.
- Copy `.env.example` → `.env` only under operator control; use local credentials never stored in git.
- No production credentials, no real private client metrics in this tree.

## Next phase

**Phase 1** — app skeleton + config loader + environment handling + basic routing/layout + auth baseline (DB still optional unless Phase 1 charter decides otherwise).

## Source Mirror Note

This directory is the versioned Active Brain source mirror for i-SEO Report Hub. Runtime deployment target is `X:\MARS-Localhost\sites\php\projects\iseo-report-hub`. Primary sync direction is source → runtime. Do not commit `.env`, `.env.local`, uploads, logs, cache, DB dumps, or private client data.
