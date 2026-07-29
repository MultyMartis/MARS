# I-SEO Report Hub — Production Environment Decision Brief v0.1

**Status:** `RECOMMENDATION_READY` — not `APPROVED_FOR_IMPLEMENTATION`; not `PRODUCTION_SELECTED`  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Authority:** Operator I-SEO Report Hub Production Environment Decision 01 (docs / decision-support)  
**Related:**
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPTIONS-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPTIONS-v0.1.md)
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-MATRIX-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-MATRIX-v0.1.md)
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPERATOR-APPROVAL-CHECKLIST-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPERATOR-APPROVAL-CHECKLIST-v0.1.md)
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-NEXT-WAVE-PLAN-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-NEXT-WAVE-PLAN-v0.1.md)

---

## 1. Purpose

Короткий decision brief для оператора: зафиксировать **recommended default** production environment / deployment topology для i-SEO Report Hub после Production Environment Charter 01, без претензии что сервер/домен уже выбраны.

Эта волна — **docs / decision-support only**. Она **не** provision’ит сервер, **не** покупает домен, **не** настраивает HTTPS и **не** деплоит приложение.

---

## 2. Current Decision State

| Field | Value |
|-------|-------|
| Decision state | **`RECOMMENDATION_READY`** |
| Production environment selected | **No** |
| Approved for implementation | **No** |
| Production claim | **Forbidden** until Decision + Validation + explicit deploy charter |

Charter 01 (docs/policy) завершён: options A–E сравнены; rejected local-only / public tunnel as production; deferred container-first и managed platform как mandatory first path.

---

## 3. Recommended Default

**Option C — VPS PHP-FPM/Nginx/MySQL**

| Topic | Advisory default |
|-------|------------------|
| Webserver | **Nginx preferred**; Apache acceptable |
| PHP | **8.3 preferred** |
| DB | **MySQL 8.x preferred** (MariaDB compatible only if validated) |
| Public docroot | Application **`/public` only** |
| Storage / logs | **Outside** public webroot |
| HTTPS | **Stable domain + TLS required** before client-facing shares |
| PDF mode | **Primary:** validate headless browser on VPS; **fallback:** pre-generated PDFs / serve-only until generation validated |
| Deployment | Release-hash exact sync **or** Git-based deploy — after operator choice |
| Deploy now | **No** — no production deploy in this wave |

---

## 4. Why This Recommendation

1. **Best fit** для текущего custom PHP + MySQL + headless PDF stack (локальный MVP уже на PHP 8.3 + MySQL 8.x + Edge headless).
2. **Public share compatibility** — стабильный HTTPS domain + controlled headers/logs для `GET /share/report/{token}`.
3. **PDF realism** — на VPS можно установить и провалидировать Chromium/Chrome/Edge; на shared hosting это частый blocker.
4. **Control** — storage вне public, backup/rollback layout (`current`/`releases`/`shared`), secrets вне Git.
5. **Operational balance** — Option D (containers) сильнее, но обычно overkill для first pilot; Option E (managed) fit с headless PDF / MARS flow не доказан.

Local MVP (gates A–D) **PASS**; production gates E–K остаются blockers до выбора среды и последующих charters.

---

## 5. What Is Not Decided Yet

Оператор должен ответить (см. Operator Approval Checklist; все поля **pending** в этой волне):

1. Environment option approved (A–E)
2. Provider / server (name, identifier, OS)
3. Domain / subdomain (exact hostname)
4. HTTPS method
5. DB engine / version
6. PHP version
7. PDF mode
8. Deployment method
9. Backup policy (DB + storage + retention + restore test)
10. Access model
11. Logging policy (token URL sensitivity)
12. Real data mode
13. DB-11 delivery audit before pilot (yes / no / defer)
14. Production implementation approved (yes / no after this decision)

**Не выдуманы:** конкретный provider, server ID, FQDN, сертификат, prod DB name, credentials.

---

## 6. Non-Negotiable Requirements

Независимо от выбранной option (для любого client-facing / production pilot path):

| Requirement | Rule |
|-------------|------|
| HTTPS | Mandatory TLS before client-facing public shares |
| Stable domain | Operator-approved FQDN; no ad-hoc tunnel as production |
| Docroot | **`/public` only** |
| Storage / logs | Outside public; exports never web-listed |
| Secrets | Outside Git; no `.env.production` in monorepo |
| Backup / restore | DB + storage backup; restore drill before real clients |
| Fixture data | **No** `LOCAL_FIXTURE_ONLY` data to real clients |
| Token logs | Access logs treating share URLs as **sensitive** |
| Production DB | **Not** `iseo_report_hub_dev`; dedicated prod DB |

---

## 7. Next Step

**`I-SEO Report Hub — Production Environment Operator Decision 01`**

Оператор заполняет checklist / отвечает в chat. Это **не** implementation wave.

После ответов — branching по [Next Wave Plan](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-NEXT-WAVE-PLAN-v0.1.md) (Validation 01 / Follow-up / Shared Hosting Compatibility / Local Demo Hardening / DB-11).

---

## Boundaries (this package)

- no server access; no deployment; no DNS; no HTTPS setup  
- no DB creation / mutation; no secrets creation  
- no app-source / runtime code changes  
- no production claim  
