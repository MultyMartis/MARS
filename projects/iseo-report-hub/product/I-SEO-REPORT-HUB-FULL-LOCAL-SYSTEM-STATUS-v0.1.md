# i-SEO Report Hub — Full Local System Status v0.1

**Дата аудита:** 2026-08-24  
**Волна:** Full Local System Status Audit 01  
**Тип:** audit / intake / planning — **без** code/DB/runtime/host mutation  
**Closeout:** [REPORT-iseo-report-hub-full-local-system-status-audit-01.md](../reports/REPORT-iseo-report-hub-full-local-system-status-audit-01.md)  
**Roadmap:** [I-SEO-REPORT-HUB-LOCAL-ROADMAP-AFTER-HOST-DEMO-v0.1.md](I-SEO-REPORT-HUB-LOCAL-ROADMAP-AFTER-HOST-DEMO-v0.1.md)

---

## 1. Verdict

**FULL LOCAL SYSTEM STATUS AUDIT ATTENTION**

Локальный source + runtime + DB готовы продолжать разработку. Host demo по словам оператора работает после re-upload `DatabaseService.php`; независимый public GET из среды аудита **не** подтвердил `/health`/`/login` (403/404). В source по-прежнему нет `public/.htaccess`. PDF/export/share parked.

---

## 2. Repo / Source Status

| Item | Value |
|------|--------|
| Repo | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD at audit | `9aa018f254c46c696f2c756f20546b4adba1a7ae` (Host DB Guard Fix hash-record tip) |
| i-SEO scope WIP | clean |
| Foreign WIP elsewhere | present, preserved |
| Source truth | `X:\AI MARS\projects\iseo-report-hub\app-source` |
| Runtime | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub` |
| Top-level source | `app/`, `public/`, `config/`, `database/`, `docs/`, `storage/`, `tools/`, `.env.example`, `.gitignore`, `README.md` |
| `public/.htaccess` in source | **missing** |
| `tools/` | present — **exclude from host** |
| `DatabaseService` host guard fix | present (opt-in local guard; web runtime allows host DB name) |
| Source ↔ runtime `DatabaseService.php` | hash **match** |
| `ConfigService` | reads **`.env.local` only** (not `.env`) |
| `public/index.php` / routing | stable front controller + `app/routes.php` |

**Known source gaps:** missing `public/.htaccess`; production config normalization still needed; PDF/export host compatibility deferred.

---

## 3. Local Runtime Status

| Route | Result |
|-------|--------|
| `GET /health` | 200 |
| `GET /login` | 200 |
| `GET /` (anon) | 302 → `/login` |
| Auth as `test@mail.ru` | POST `/login` 302 → `/` |
| `GET /` | 200; demo scenario visible |
| `GET /reporting-periods` | 200 |
| `GET /monthly-reports/7` (+ preview) | 200 |
| `GET /monthly-reports/8` (+ preview) | 200 |
| `GET /monthly-reports/8/work-entries/create` | 200 |
| `GET /monthly-report-work-entries/28/edit` | 200 |
| Raw `REFUSED:` / Fatal in smoked pages | none |

Local URL: `http://iseo-report-hub.test/`  
Auth works. Demo `ПРОВЕРКА.рф` visible. Local development can continue.

---

## 4. Local DB Status

DB: `iseo_report_hub_dev` @ local loopback (`APP_ENV=local`). Read-only probe only.

| Entity | Count |
|--------|------:|
| users | 3 |
| roles | 6 |
| clients / projects / sites | 1 / 1 / 1 |
| reporting_periods | 2 |
| monthly_report_contents | 2 |
| report_blocks | 12 |
| monthly_report_work_entries | 22 |
| report_snapshots / report_exports / report_export_shares | 0 / 0 / 0 |
| weekly_checkpoints | 0 |
| audit_log | 68 |

**Checks**

| Check | Result |
|-------|--------|
| `test@mail.ru` active + `seo_specialist` | yes |
| Admin users | yes (`admin_owner`: `admin@iseo-report-hub.test`, `polygon-ws@mail.ru`) |
| Only demo client/project/site `ПРОВЕРКА.рф` | yes (ids 2) |
| Old Demo Client row | absent |
| Monthly 7 finalized / 8 in_progress | yes |
| Blocks 12 / work entries 22 | yes |
| Snapshots/exports/shares 0 | yes |
| Marker `.рa` | none found |
| App URL `iseo-report-hub.test` in content | none; only admin **email** domain `admin@iseo-report-hub.test` |
| `sites.url` | `https://proverka.example` (demo content) |
| `clients.notes` | training note (“local demo client…”) — not old “Demo Client” entity |

Password hashes: not printed.

---

## 5. Host-known Status

| Claim | Basis |
|-------|--------|
| Host demo manually uploaded | operator |
| Host `.env.local` host-specific; DB ≠ `iseo_report_hub_dev` | docs + operator |
| Blocker fixed by re-upload `app/Services/DatabaseService.php` | Host DB Guard Fix report + operator |
| Main pages working on host | operator |
| Old `/report-exports/…/shares`, `/report-snapshots/…/exports` 404 expected | cleanup + operator |
| No active PDF/export/share expectation | operator / readiness |
| SEO team looked; no actionable feedback | operator |
| Independent public GET `/`, `/health`, `/login` from audit env | **403 / 404 / 404** — not confirmed here |

Do **not** assume other local commits beyond the re-uploaded `DatabaseService.php` are on host unless documented.

---

## 6. Config / Env / DB Connection Status

| Topic | State |
|-------|--------|
| Env file model | Runtime `.env.local` (Git-ignored) |
| Keys read by ConfigService | `APP_NAME`, `APP_ENV`, `APP_DEBUG`, `APP_URL`, `DB_HOST`, `DB_PORT`, `DB_DATABASE`, `DB_USERNAME`, `DB_PASSWORD` |
| `.env.example` | present in source (placeholders) |
| Host DB guard | fixed in source; opt-in for CLI tools only |
| Remaining debt | production config normalization; clarify `.env` vs `.env.local`; keep local guards out of web runtime; optional HTTPS/session cookie flags; clean deploy packaging |

**Future charter (not now):** `I-SEO Report Hub — Production Config Normalization 01`

---

## 7. Deployment Package Status

Pre-hosting readiness remains **ATTENTION**:

- Document root = `public`
- Copy from `app-source` (not whole runtime)
- Exclude `tools/`, secrets, evidence
- PHP 8.3
- Host needs `.env.local` (not `.env`)
- `public/.htaccess` **missing in source** — host rewrite may be manual
- No WP-like DB URL replace
- Manual upload process documented enough for operator; clean deploy package builder still optional later
- Source should include `public/.htaccess` in a future hygiene wave

---

## 8. Product / UX Status

Working locally: dashboard, periods, monthly detail, work entries create/edit, field help icons, client preview, demo `ПРОВЕРКА.рф`, roles admin vs seo_specialist, July (7) finalized + August (8) in progress.

**Gaps:** SEO feedback pending; Browser Filled Demo Report Pass not done; August content deltas not applied; real team create/edit testing; real users/clients not seeded; onboarding/checklist missing; empty/parked PDF-export-share UX if users click files.

---

## 9. Export / PDF / Share Status

| Item | State |
|------|--------|
| DB snapshots/exports/shares | 0 |
| Old exports removed | yes (cleanup wave) |
| Old share/export URLs | 404 expected |
| PDF/share | parked |
| `ReportExportService` | Windows Edge/Chrome headless paths — shared hosting risk |
| Recommendation | separate charter before enabling: **Export Share PDF Readiness Charter 01**; product UX first is acceptable |

---

## 10. Risks / Technical Debt

1. Missing source `public/.htaccess`
2. Production config / `.env.local` semantics not normalized
3. Weak demo password on shared demo accounts
4. Host state not independently verified in this audit
5. Possible host/source drift beyond `DatabaseService.php`
6. PDF/export assumes local desktop browsers
7. Foreign monorepo WIP (out of scope) — use selective staging / worktree discipline
8. Unpushed i-SEO commits exist on canonical branch (push not part of this wave)

---

## 11. Can local development continue?

**Yes.** Local auth, demo scenario, monthly 7/8, preview, and work-entry create/edit smoke are healthy. Prefer product MVP polish + config/deploy hygiene before PDF/share or broad production ops.
