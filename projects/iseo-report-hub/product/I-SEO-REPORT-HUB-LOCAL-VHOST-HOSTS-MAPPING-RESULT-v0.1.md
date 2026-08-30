# I-SEO Report Hub — Local Vhost / Hosts Mapping Result v0.1

**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Wave:** Local Vhost / Hosts Mapping 01

---

## 1. Status

| Field | Value |
|-------|-------|
| **Mapping status** | **Partial** — Apache vhost complete; Windows `hosts` entry **blocked** by OS access denial (even elevated) |
| **Domain** | `iseo-report-hub.test` |
| **DocumentRoot** | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\public` |
| **Runtime path** | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |
| **Source path** | `X:\AI MARS\projects\iseo-report-hub\app-source\` |
| **DB** | **No** — not created, not connected, not tested |
| **`.env` / `.env.local`** | **Absent** — not created |
| **App code** | **Unchanged** — no `app-source/` edits; no runtime `app/` / `public/` edits |

Option used: **B (vhost) + C (hosts manual)** — AutoVirtualHosts=`0`; dedicated vhost created; hosts write not safely possible from this session.

---

## 2. Configuration Summary

| Item | Status |
|------|--------|
| **Hosts entry** | **Not present** — `127.0.0.1 iseo-report-hub.test` missing; elevated write → `UnauthorizedAccessException` / cmd `echo >>` exit 1; file length unchanged |
| **Vhost file** | **Created** — `X:\MARS-Localhost\laragon\etc\apache2\sites-enabled\iseo-report-hub.test.conf` |
| **Apache include** | `IncludeOptional "X:/MARS-Localhost/laragon/etc/apache2/sites-enabled/*.conf"` (httpd.conf) |
| **Laragon AutoVirtualHosts** | `0` (`laragon.ini`) — manual mapping expected |
| **Apache restart** | **Yes** — non-service Laragon httpd; `httpd -k graceful/shutdown` unavailable (no Apache2.4 service); safe stop/start of httpd processes with same `-d` root |
| **Front controller** | `FallbackResource /index.php` in vhost (no `public/.htaccess` in skeleton) |
| **Logs** | `storage/logs/apache-error.log`, `storage/logs/apache-access.log` under runtime |

### Manual hosts step (required for domain URL)

As Administrator, append exactly one line to `C:\Windows\System32\drivers\etc\hosts` (do not remove existing MLI lines):

```text
127.0.0.1 iseo-report-hub.test
```

Then re-check: `http://iseo-report-hub.test/`

---

## 3. HTTP Smoke

Probed via `http://127.0.0.1{path}` with `Host: iseo-report-hub.test` (vhost proof without DNS).

| URL path | Status | Markers |
|----------|--------|---------|
| `/` | **200** | `i-SEO Report Hub`; `data-phase="1a"` / Phase 1A; DB negation present; no SQL error |
| `/health` | **200** | same app markers; DB negation; no SQL error |
| `/login` | **200** | app markers; no SQL error |
| `/not-existing` | **404** | app 404 page (`Not Found - i-SEO Report Hub`); no SQL error |

| Domain URL | Result |
|------------|--------|
| `http://iseo-report-hub.test/` | **FAIL resolve** — DNS/hosts unresolved until manual hosts line |

**DB:** not tested (out of scope).

---

## 4. Files / Config Changed

| Path | Action |
|------|--------|
| `X:\MARS-Localhost\laragon\etc\apache2\sites-enabled\iseo-report-hub.test.conf` | **Created** |
| `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\logs\apache-error.log` | Created empty by Apache |
| `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\logs\apache-access.log` | Created empty by Apache |
| `C:\Windows\System32\drivers\etc\hosts` | **Not modified** (access denied) |

Unrelated existing vhosts (`00-default`, `fws-0001`, `mli-smoke-001`, `shpigovsky`) **not** overwritten.

---

## 5. What Was Not Done

- DB creation / SQL / migrations
- `.env` / `.env.local`
- App-source edits
- Runtime app code edits
- Source → runtime sync
- Production deployment
- Push / fetch / pull
- Composer / npm
- WordPress
- Demo workspace / registry changes

---

## 6. Security Notes

- No secrets or credentials introduced
- Local-only Apache vhost on port 80
- Hosts file not mutated by agent (permission blocked)
- Apache logs under runtime `storage/logs/` (local)
- No DB connection attempted by mapping smoke

---

## 7. Next Phase

**Fix mapping** — operator (or elevated session that can write `hosts`) adds `127.0.0.1 iseo-report-hub.test`, then re-smoke domain URLs. After domain smoke PASS, next product charter: **DB creation + schema migration**.

---

## 8. SAFE UNKNOWN

- Why elevated Administrator still receives `UnauthorizedAccessException` on `C:\Windows\System32\drivers\etc\hosts` in this session (policy / AV / OS lock — not fully identified).
- Whether Laragon UI “Reload Apache” would be preferred by operator over process stop/start used here.
- Whether operator will also append the domain to `X:\MARS-Localhost\runtime\registries\mli-hosts-domains.txt` / MLI hosts toolkit (optional; not required for Apache vhost).
