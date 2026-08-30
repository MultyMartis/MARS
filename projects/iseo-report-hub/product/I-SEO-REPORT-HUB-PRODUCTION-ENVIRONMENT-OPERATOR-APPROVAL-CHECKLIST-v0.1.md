# I-SEO Report Hub — Production Environment Operator Approval Checklist v0.1

**Status:** PENDING OPERATOR ANSWERS — all production-specific values blank  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Authority:** Operator I-SEO Report Hub Production Environment Decision 01  
**Related:**
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-BRIEF-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-BRIEF-v0.1.md)
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-NEXT-WAVE-PLAN-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-NEXT-WAVE-PLAN-v0.1.md)

---

## Instructions for operator

1. Заполните поля ниже **или** ответьте по пунктам в chat (Operator Decision 01).
2. Рекомендованные defaults помечены как **RECOMMENDATION ONLY** — это **не** approval.
3. **Не** вставляйте passwords, API keys, private keys, DB credentials, share tokens в отчёты/чаты/Git.
4. Credentials / secrets — только local secret contour (например host panel / password manager / local `.env` вне Git). **Never commit secrets.**
5. Пока checklist не закрыт оператором, decision state остаётся **`RECOMMENDATION_READY`**.

---

## Recommended defaults (advisory — NOT approvals)

| Topic | Recommendation only |
|-------|---------------------|
| Environment | **C — VPS** |
| Webserver | Nginx preferred (Apache OK) |
| PHP | 8.3 |
| DB | MySQL 8.x |
| Docroot | `/public` |
| PDF | Validate headless on VPS; fallback serve-only / pre-generated |
| Deploy method | Release-hash exact sync or Git-based (operator chooses) |
| Production implementation now | **No** until Decision + Validation |

---

## Checklist fields (1–14) — PENDING

### 1. Environment option approved

- [ ] **A** — local-only demo  
- [ ] **B** — shared hosting  
- [ ] **C** — VPS  
- [ ] **D** — containerized VPS  
- [ ] **E** — managed platform  

**Operator answer:** `_pending_`  
**Notes:** `_pending_`

---

### 2. Provider / server

| Field | Operator answer |
|-------|-----------------|
| Provider name | `_pending_` |
| Server identifier | `_pending_` |
| OS | `_pending_` |

---

### 3. Domain / subdomain

| Field | Operator answer |
|-------|-----------------|
| Exact hostname (FQDN) | `_pending_` |

Do not invent example production hostnames as selected values.

---

### 4. HTTPS method

- [ ] Let’s Encrypt  
- [ ] Hosting panel certificate  
- [ ] Reverse proxy  
- [ ] Other: `_pending_`  

**Operator answer:** `_pending_`

---

### 5. DB engine / version

| Field | Operator answer |
|-------|-----------------|
| Engine (MySQL / MariaDB) | `_pending_` |
| Version | `_pending_` |

**Recommendation only:** MySQL 8.x utf8mb4; dedicated prod DB — **not** `iseo_report_hub_dev`.

---

### 6. PHP version

| Field | Operator answer |
|-------|-----------------|
| Target PHP version | `_pending_` |

**Recommendation only:** PHP 8.3.

---

### 7. PDF mode

- [ ] Production headless browser (validate on host)  
- [ ] Local / pre-generated upload  
- [ ] Serve-only first pilot  

**Operator answer:** `_pending_`

---

### 8. Deployment method

- [ ] Git deploy  
- [ ] SFTP exact sync  
- [ ] Release archive  
- [ ] Other: `_pending_`  

**Operator answer:** `_pending_`

---

### 9. Backup policy

| Field | Operator answer |
|-------|-----------------|
| DB backup location | `_pending_` |
| Storage backup location | `_pending_` |
| Retention | `_pending_` |
| Restore test required (yes/no) | `_pending_` |

Do not paste backup credentials here.

---

### 10. Access model

- [ ] Internal-only  
- [ ] IP allowlist / VPN  
- [ ] Normal login over HTTPS  
- [ ] Extra basic auth  

**Operator answer:** `_pending_`  
**Notes:** `_pending_`

---

### 11. Logging policy

| Field | Operator answer |
|-------|-----------------|
| Token URL log handling | `_pending_` |
| Retention | `_pending_` |

Treat share URLs / tokens in access logs as **sensitive**.

---

### 12. Real data mode

- [ ] Fixture only  
- [ ] Internal test client  
- [ ] First real client  

**Operator answer:** `_pending_`

---

### 13. DB-11 delivery audit before pilot

- [ ] Yes  
- [ ] No  
- [ ] Defer  

**Operator answer:** `_pending_`

---

### 14. Production implementation approved

- [ ] Yes — after this decision (still requires Validation / separate implement charter)  
- [ ] No  

**Operator answer:** `_pending_`  

Default expectation for this package wave: **No** until Operator Decision 01 answers are recorded and next wave selected.

---

## Sign-off block (leave blank until operator decides)

| Field | Value |
|-------|-------|
| Operator name | `_pending_` |
| Date | `_pending_` |
| Decision state after answers | `_pending_` (expected future: direction selected; still not auto-deploy) |
| Secrets pasted into this doc | **Must remain none** |

---

## Boundaries

Filling this checklist does **not** by itself authorize SSH, DNS, HTTPS install, DB create, secrets commit, app-source edits, runtime sync, or production deploy. Those require explicit follow-up charters per Next Wave Plan.
