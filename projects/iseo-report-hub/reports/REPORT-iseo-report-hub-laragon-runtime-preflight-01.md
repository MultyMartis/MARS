# REPORT — I-SEO REPORT HUB LARAGON RUNTIME PREFLIGHT 01

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD (observed) | `978b5835` — docs(iseo-report-hub): add php mysql mvp technical brief |
| Staged index | **Empty** (`git diff --cached --name-only` empty) |
| Branch sync note | Observed `ahead 21, behind 62` vs `origin/mars/canonical-post-recovery` — **no** fetch/pull/reset |
| Foreign WIP | **Preserved** — unrelated `M` / `??` entries left untouched |
| Write scope | Only allowlisted i-SEO docs/reports/index |

Required i-SEO docs present (platform decision, technical brief, Laragon plan, phases, schema draft, route map, OPERATIONAL-INDEX). Hard preflight **passed**.

## 2. Runtime Checks Performed

| Area | Action |
|------|--------|
| Laragon discovery | Common C:/D:/X: paths; Start Menu shortcut; registry uninstall; live process paths |
| PHP discovery | System PATH; Laragon `bin\php` trees; Apache `mod_php.conf`; CLI `-v` / `-m` / ini |
| MySQL/MariaDB discovery | Laragon MySQL 8.4.3 bin; `mysqld` process; port 3306; client `--version`; safe `SELECT VERSION();` only |
| Web server discovery | Apache httpd process/version; Nginx binary presence; Laragon running |
| Ports / domain / DB candidates | Ports 80/443/8080/3306; DNS/hosts for domain candidates; DB name candidate only (no SHOW DATABASES) |
| Gitignore / secrets readiness | Root `.gitignore` read; gaps noted; **no** `.gitignore` edit |

## 3. Environment Summary

| Component | Summary |
|-----------|---------|
| **Laragon** | **Yes** — `X:\MARS-Localhost\laragon\` v8.6.1; `laragon.exe` running; www/bin/etc/data/usr present |
| **PHP** | Active **8.3.30** ZTS at `...\bin\php\php-8.3.30-Win32-vs16-x64\`; bound in Apache `mod_php.conf`; **not** on system PATH. Secondary **8.5.8** NTS present, not active / no loaded ini |
| **MySQL** | Client + server **8.4.3**; data under Laragon `data\`; port **3306** listening |
| **Web server** | Apache **2.4.66** listening on **80**; Nginx installed, **not** running; **443** / **8080** not listening |
| **SAFE UNKNOWN** | See §10 |

## 4. PHP Capability Summary

Verified on PHP **8.3.30** (active):

| Extension | Present | MVP |
|-----------|---------|-----|
| pdo_mysql | yes | required |
| mbstring | yes | required |
| json | yes | required |
| openssl | yes | required |
| fileinfo | yes | required |
| session / pdo | yes | required |
| gd / curl / intl | yes | optional useful |
| imagick | no | optional |

## 5. Database Summary

| Item | Result |
|------|--------|
| Client | MySQL 8.4.3 (Laragon path; not on PATH) |
| Server | Running; `SELECT VERSION()` → **8.4.3** |
| Connection tested | **Yes** (version query only) |
| DB created | **No** |
| Databases listed | **No** |
| Credentials exposed | **No** |
| Candidate name | `iseo_report_hub_dev` (not created; existence **SAFE UNKNOWN**) |

## 6. Layout Recommendation

**Recommend Option B for Phase 0 runtime:** `X:\MARS-Localhost\iseo-report-hub\`

| Reason | Detail |
|--------|--------|
| Policy fit | Aligns with MARS Localhost runtime root; Laragon already under `X:\MARS-Localhost\laragon\` |
| Git risk | Keeps runtime/secrets/uploads out of dirty Active Brain monorepo |
| Docs | Remain in `X:\AI MARS\projects\iseo-report-hub\` |
| Option A risk | `projects\...\app\` mixes docs WIP + runtime; weaker for jobs |
| www | Existing DocumentRoot `...\laragon\www` can later mount via charter (junction/vhost); AutoVirtualHosts=`0` |

**Operator confirmation needed:** layout choice, domain, DB create charter, PHP pin (8.3.30), source↔runtime sync policy, upload/backup location.

## 7. Secrets/Gitignore Summary

| Item | Status |
|------|--------|
| Future `.env.local` / `.env` | Planned; never commit |
| Future `.env.example` | Placeholder-only; root ignore already excepts `!.env.example` |
| Root ignore | `.env`, `.env.*` covered |
| Gaps | `/local/` is repo-root-anchored only; no dedicated `storage/uploads/` or global PHP `vendor/` ignore |
| If Option B | Runtime outside git tree — preferred for secrets/uploads |
| `.gitignore` edited | **No** |

## 8. Phase 0 Readiness

| Verdict | **Partial** |
|---------|-------------|
| Ready | Laragon/PHP/MySQL/Apache identity verified; MVP PHP extensions OK; MySQL server reachable for version check |
| Not ready without charter | Scaffold paths, vhost/hosts, DB create, sync policy |
| Hard blockers | **None** for planning; scaffold still **forbidden** until Phase 0 charter |
| Inputs needed | See Preflight Result §9 |

## 9. Validation

| Constraint | Status |
|------------|--------|
| No application code | Pass |
| No SQL files / migrations | Pass |
| No DB create/mutate beyond `SELECT VERSION()` | Pass |
| No Laragon config edits | Pass |
| No vhost / hosts edits | Pass |
| No service restart | Pass |
| No demo workspace edits | Pass |
| No registry changes | Pass |
| No secrets written | Pass |
| No git add/commit/push/fetch/checkout/reset/restore/clean/stash | Pass |

## 10. SAFE UNKNOWN

- Whether `iseo_report_hub_dev` already exists
- Final docroot mapping (www junction vs other)
- Whether PHP 8.5.x will replace 8.3.30 later
- Composer usage for MVP start (installer present; unused)
- Production hosting parity with Laragon
- Unrelated Active Brain remote divergence details (not remediated)

## 11. Recommended Next Action

Operator review of [I-SEO-REPORT-HUB-LARAGON-PREFLIGHT-RESULT-v0.1.md](../product/I-SEO-REPORT-HUB-LARAGON-PREFLIGHT-RESULT-v0.1.md), then MVP Phase 0 scaffold charter if ready.

## 12. Files Changed

1. `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LARAGON-PREFLIGHT-RESULT-v0.1.md` — **created**
2. `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-laragon-runtime-preflight-01.md` — **created**
3. `projects/iseo-report-hub/OPERATIONAL-INDEX.md` — **updated**

## 13. Git Actions

No add  
No commit  
No push  
No fetch  
No checkout  
No reset  
No restore  
No clean  
No stash  
