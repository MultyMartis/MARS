# i-SEO Report Hub — App Source Mirror

## Status

**Phase 1A source skeleton complete.** Versioned Active Brain mirror with minimal PHP app skeleton (bootstrap, router, views, controllers, services, config loader). **Not** synced to Localhost runtime in this phase.

| Fact | State |
|------|-------|
| Platform | Custom **PHP + SQL/MySQL** |
| WordPress | **Not used** as runtime or source of truth |
| Framework / Composer | **None** — plain PHP 8.3 |
| Database | **Not created** · no connection attempted |
| Migrations | **None** |
| Auth | **Stub only** — no DB login |
| Secrets | **None** — `.env.example` placeholders only; **no** `.env` / `.env.local` |
| Runtime sync | **Not done** in Phase 1A |

## Paths

| Item | Value |
|------|-------|
| Source mirror (this tree) | `X:\AI MARS\projects\iseo-report-hub\app-source\` |
| Runtime target (unchanged) | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |
| Intended domain | `iseo-report-hub.test` (not mapped yet) |
| DB candidate | `iseo_report_hub_dev` (not created) |
| PHP target | **8.3.30** (Laragon) |

Docs and specs remain in:

`X:\AI MARS\projects\iseo-report-hub\`

## Optional source review (built-in server)

Operator-only local review from this tree (does **not** update runtime):

```bash
php -S 127.0.0.1:8088 -t public public/index.php
```

Charter-equivalent document form (same intent):

```bash
php -S 127.0.0.1:8088 -t public
```

For path routes (`/`, `/login`, `/health`), pass `public/index.php` as the built-in server router script so requests dispatch through the front controller. Static assets under `public/assets/` are served as files.

Routes: `GET /`, `GET /login`, `POST /login` (stub), `GET /logout`, `GET /health`, 404 fallback.

## Secrets policy

- Do **not** commit `.env` or `.env.local`.
- Do **not** create `.env.local` in Phase 1A.
- Copy `.env.example` → `.env.local` only under a later operator charter.
- No production credentials, no real private client metrics in this tree.

## What this phase is not

- Runtime not updated / not claimed updated
- No source → runtime sync
- No DB / SQL / migrations
- No Composer / npm / frameworks
- No vhost / hosts changes

## Next phase

**Recommended:** Phase 1B — source → runtime sync + local smoke.

**Alternative:** DB creation charter only after runtime skeleton smoke.
