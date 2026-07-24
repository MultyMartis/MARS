# REPORT — I-SEO REPORT HUB LOCAL HOSTS RE-SMOKE 01

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD (pre-commit) | `c376fb94b201b31ae63859b8b548cc355c88a1a8` |
| Staged/index before work | **empty** |
| Foreign WIP | **Preserved** — unrelated `M`/`??` paths left untouched |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |
| Docroot | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\public` |
| Domain | `iseo-report-hub.test` |
| Write scope | Active Brain docs only; no hosts/vhost/app-source/runtime app edits |

Runtime required files present: `public/index.php`, `public/health.php`, `app/bootstrap.php`, `app/routes.php`.  
Forbidden artefacts absent: `.env`, `.env.local`, nested `.git`, `vendor/`, `node_modules/`.

---

## 2. Hosts / DNS Check

| Check | Result |
|-------|--------|
| Hosts line | `127.0.0.1 iseo-report-hub.test` — **present** (read-only inspect of `C:\Windows\System32\drivers\etc\hosts`) |
| Duplicate | **No** (single match) |
| Conflict | **No** |
| Agent hosts edit | **No** |
| `ping -n 1 iseo-report-hub.test` | **127.0.0.1** |
| `Resolve-DnsName` | A **127.0.0.1** |
| `.NET GetHostAddresses` | **127.0.0.1** |

---

## 3. HTTP Smoke

Direct domain (Host-header fallback **not used**).

| URL | Expected | Actual | Markers |
|-----|----------|--------|---------|
| `http://iseo-report-hub.test/` | 200 | **200** | `i-SEO Report Hub`; `data-phase="1a"`; DB negation; no SQL error |
| `http://iseo-report-hub.test/health` | 200 | **200** | same; `Database: DB not configured / not tested in Phase 1A` |
| `http://iseo-report-hub.test/login` | 200 | **200** | app + Phase 1A markers; no SQL error |
| `http://iseo-report-hub.test/not-existing` | 404 | **404** | title `Not Found - i-SEO Report Hub`; `data-phase="1a"`; no SQL error |

DB not tested. Apache restart **not** performed (not required).

---

## 4. Validation

| Constraint | Result |
|------------|--------|
| no DB created/mutated | pass |
| no SQL | pass |
| no `.env` / `.env.local` | pass |
| no hosts edits (this agent) | pass |
| no vhost edits | pass |
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

---

## 5. Documentation

| Doc | Action |
|-----|--------|
| `product/I-SEO-REPORT-HUB-LOCAL-HOSTS-RESMOKE-RESULT-v0.1.md` | created |
| `OPERATIONAL-INDEX.md` | updated — hosts re-smoke PASS; direct domain PASS; HTTP routes PASS; DB still not done; next = DB charter |
| This closeout report | created |

---

## 6. Commit

| Field | Value |
|-------|--------|
| Exact-path stage | yes |
| Staged list | `projects/iseo-report-hub/OPERATIONAL-INDEX.md`; `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LOCAL-HOSTS-RESMOKE-RESULT-v0.1.md`; `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-local-hosts-resmoke-01.md` |
| Commit message | `docs(iseo-report-hub): record local hosts resmoke` |
| Commit hash | `38eb6421cbee706e850c3ee212f92d20f28f4e7b` (`38eb6421`) |
| HEAD verification | `git show --name-only --oneline --stat HEAD` — only the three Active Brain docs above |
| Push | **no** |

---

## 7. SAFE UNKNOWN

- Exact wall-clock time the operator added the hosts line (present at re-smoke; not observed being written).
- Whether optional MLI hosts registry files were also updated (not required for observed resolution).

---

## 8. Recommended Next Action

**DB creation + schema migration charter** for local `iseo_report_hub_dev`.

---

## 9. Files Changed

### Active Brain docs

- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LOCAL-HOSTS-RESMOKE-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-local-hosts-resmoke-01.md`

### Not changed

- Hosts file, vhost conf, `app-source/**`, runtime `app/**` / `public/**`

---

## 10. Git Actions

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
