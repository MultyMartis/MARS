# REPORT — I-SEO REPORT HUB LOCAL VHOST HOSTS MAPPING 01

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD (pre-commit) | `ea54116b205bd80f4bba3b01e20e758bfed9c919` |
| Staged/index before work | **empty** |
| Foreign WIP | **Preserved** — many unrelated `M`/`??` paths left untouched |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |
| Docroot | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\public` |
| Domain | `iseo-report-hub.test` |
| Write scope | Laragon dedicated vhost + Active Brain docs only; no app-source; no runtime app code; no hosts mutation |

---

## 2. Preflight Findings

| Item | Finding |
|------|---------|
| Laragon path | `X:\MARS-Localhost\laragon\` (v8.6.1); AutoVirtualHosts=`0` |
| Apache | 2.4.66 running (`httpd`); include `sites-enabled/*.conf` |
| Apache config paths | `X:\MARS-Localhost\laragon\etc\apache2\`; `sites-enabled\` present; `sites-available\` **absent**; `alias\` present; Laragon `etc\hosts` **absent** |
| Windows hosts | `C:\Windows\System32\drivers\etc\hosts` — MLI block has `fws-0001.test`, `shpigovsky.test`, `mli-smoke-001.test`; **no** `iseo-report-hub.test` |
| Vhost before | No `iseo-report-hub.test.conf` |
| Domain resolution before | Unresolved |
| HTTP before | `http://iseo-report-hub.test/` fail (no such host); `http://127.0.0.1/` → 200 Laragon www |
| Runtime required files | `public/index.php`, `public/health.php`, `app/bootstrap.php`, `app/routes.php` — present |
| Forbidden runtime artefacts | no `.env`, `.env.local`, `.git`, `vendor/`, `node_modules/` |

---

## 3. Mapping Action

| Field | Value |
|-------|-------|
| Option | **B + C** — dedicated vhost created; hosts **manual** (write denied even as elevated Administrator) |
| Hosts entry | **Not added** — `UnauthorizedAccessException` / cmd append exit 1; length stayed 986 |
| Vhost file | **Created** `X:\MARS-Localhost\laragon\etc\apache2\sites-enabled\iseo-report-hub.test.conf` |
| DocumentRoot | `X:/MARS-Localhost/sites/php/projects/iseo-report-hub/public` |
| Front controller | `FallbackResource /index.php` (skeleton has no `public/.htaccess`) |
| Apache restart | **Yes** — stop/start httpd with Laragon `-d` root (no Windows service `Apache2.4`; `-k graceful` unavailable) |
| Unrelated vhosts | Not deleted / not overwritten |

### Manual hosts instruction

Append one line to `C:\Windows\System32\drivers\etc\hosts` (Administrator / session that can write hosts):

```text
127.0.0.1 iseo-report-hub.test
```

---

## 4. HTTP Smoke

Method: `GET http://127.0.0.1{path}` with header `Host: iseo-report-hub.test` (validates vhost without DNS).

| URL | Status | Response markers |
|-----|--------|------------------|
| `/` | **200** | `i-SEO Report Hub`; Phase 1A (`data-phase="1a"`); DB negation; no SQL error |
| `/health` | **200** | same; DB negation; no SQL error |
| `/login` | **200** | same; no SQL error |
| `/not-existing` | **404** | app Not Found page; no SQL error |
| `http://iseo-report-hub.test/` | **FAIL** | DNS/hosts unresolved |

DB not tested.

---

## 5. Validation

| Constraint | Result |
|------------|--------|
| no DB created/mutated | pass |
| no SQL | pass |
| no `.env` / `.env.local` | pass |
| no app-source edits | pass |
| no runtime app code edits | pass |
| no source→runtime sync | pass |
| no secrets/credentials | pass |
| no Composer/npm / vendor/node_modules | pass |
| no WordPress | pass |
| no demo workspace edits | pass |
| no registry changes | pass |
| no push/fetch/pull/checkout/reset/restore/clean/stash | pass |
| foreign WIP preserved | pass |
| local config only for `iseo-report-hub.test` | pass (plus Apache log files under runtime `storage/logs/`) |

---

## 6. Documentation

| Doc | Action |
|-----|--------|
| `product/I-SEO-REPORT-HUB-LOCAL-VHOST-HOSTS-MAPPING-RESULT-v0.1.md` | created |
| `OPERATIONAL-INDEX.md` | updated — domain mapping partial; docroot; Host-header smoke; DB still not done; next = fix hosts |
| This closeout report | created |

---

## 7. Commit

| Field | Value |
|-------|-------|
| Exact-path stage | yes |
| Staged list | `projects/iseo-report-hub/OPERATIONAL-INDEX.md`; `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LOCAL-VHOST-HOSTS-MAPPING-RESULT-v0.1.md`; `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-local-vhost-hosts-mapping-01.md` |
| Commit message | `docs(iseo-report-hub): record local vhost mapping` |
| Commit hash | `30609482d3b7bb55eedf5c623e0029ec89fd2e22` (`30609482`) — verify with `git log -1 --oneline --grep="record local vhost mapping"` |
| HEAD verification | `git show --name-only --oneline --stat HEAD` — only the three Active Brain docs above |
| Push | **no** |

---

## 8. SAFE UNKNOWN

- Root cause of elevated Administrator still being denied write to `C:\Windows\System32\drivers\etc\hosts` in this session (policy / AV / lock).
- Whether operator prefers Laragon UI Apache reload vs process stop/start used here.

---

## 9. Recommended Next Action

**Fix mapping** — add `127.0.0.1 iseo-report-hub.test` to Windows hosts with a session that can write the file, then re-smoke `http://iseo-report-hub.test/` (`/`, `/health`, `/login`, `/not-existing`).

---

## 10. Files Changed

### Active Brain docs

- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LOCAL-VHOST-HOSTS-MAPPING-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-local-vhost-hosts-mapping-01.md`

### Local config (not in Git)

- `X:\MARS-Localhost\laragon\etc\apache2\sites-enabled\iseo-report-hub.test.conf` (created)
- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\logs\apache-error.log` (created by Apache)
- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\logs\apache-access.log` (created by Apache)

---

## 11. Git Actions

| Action | Done |
|--------|------|
| exact-path git add | **yes** |
| commit | **yes** |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout | **no** |
| reset | **no** |
| restore | **no** |
| clean | **no** |
| stash | **no** |
