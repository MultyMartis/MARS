# I-SEO Report Hub — Local Hosts Re-Smoke Result v0.1

**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Wave:** Local Hosts Re-Smoke 01

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **Complete** — direct domain HTTP smoke **PASS** |
| **Domain** | `iseo-report-hub.test` |
| **Hosts entry** | **Present** — `127.0.0.1 iseo-report-hub.test` (operator manual; this wave did not edit hosts) |
| **Vhost** | Unchanged — `X:\MARS-Localhost\laragon\etc\apache2\sites-enabled\iseo-report-hub.test.conf` |
| **DocumentRoot** | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\public` |
| **DB** | **No** — not created, not connected, not tested |
| **App code** | **Unchanged** — no `app-source/` edits; no runtime `app/` / `public/` edits |
| **Apache restart** | **Not performed** — not required |

---

## 2. Hosts / DNS

| Check | Result |
|-------|--------|
| Hosts entry present | **Yes** — exactly one match |
| Duplicate | **No** |
| Conflicting line | **No** |
| Hosts path inspected | `C:\Windows\System32\drivers\etc\hosts` (read-only) |
| `ping -n 1 iseo-report-hub.test` | Resolves to **127.0.0.1** |
| `Resolve-DnsName iseo-report-hub.test` | A record **127.0.0.1** |
| `.NET GetHostAddresses` | **127.0.0.1** |

---

## 3. HTTP Smoke

Direct domain URLs (no Host-header fallback needed).

| URL | Expected | Actual | Result |
|-----|----------|--------|--------|
| `http://iseo-report-hub.test/` | 200 | **200** | **PASS** |
| `http://iseo-report-hub.test/health` | 200 | **200** | **PASS** |
| `http://iseo-report-hub.test/login` | 200 | **200** | **PASS** |
| `http://iseo-report-hub.test/not-existing` | 404 | **404** | **PASS** |

Host-header fallback (`GET http://127.0.0.1/` + `Host: iseo-report-hub.test`): **not used** — direct domain smoke succeeded.

---

## 4. Response Markers

| Marker | Evidence |
|--------|----------|
| App marker | `i-SEO Report Hub` in titles / body (`Dashboard`, `Health`, `Login`, `Not Found`) |
| Phase 1A marker | `data-phase="1a"`; health copy includes `Phase 1A - App skeleton` |
| DB negation | Health: `Database: DB not configured / not tested in Phase 1A`; footer/skeleton notes no DB |
| SQL error | **None** observed on any probed route |
| DB connection | **Not attempted** by this smoke (out of scope) |

---

## 5. What Was Not Done

- DB creation / mutation
- SQL / migrations
- `.env` / `.env.local`
- Hosts edits (this agent)
- Vhost edits
- Apache restart
- App-source edits
- Runtime app code edits
- Source → runtime sync
- Composer / npm
- WordPress
- Demo workspace / registry changes
- Push / fetch / pull

---

## 6. Next Phase

**PASS** — recommend next charter: **DB creation + schema migration** for `iseo_report_hub_dev` (separate operator-approved wave; secrets / `.env.local` only if that charter allows).

---

## 7. SAFE UNKNOWN

- Exact wall-clock moment the operator appended the hosts line (attested present at re-smoke time only).
- Whether MLI registry files (`mli-hosts-domains.txt` etc.) were also updated — optional; not required for Apache + Windows hosts resolution observed here.
