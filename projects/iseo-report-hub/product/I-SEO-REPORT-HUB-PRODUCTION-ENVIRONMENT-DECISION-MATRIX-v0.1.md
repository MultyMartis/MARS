# I-SEO Report Hub — Production Environment Decision Matrix v0.1

**Status:** DECISION SUPPORT — recommendation only; not operator approval  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Authority:** Operator I-SEO Report Hub Production Environment Decision 01  
**Related:**
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPTIONS-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPTIONS-v0.1.md)
- [I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-BRIEF-v0.1.md](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-BRIEF-v0.1.md)

---

## 1. Purpose

Сравнить options **A–E** по измерениям, критичным для production pilot i-SEO Report Hub (custom PHP + MySQL + headless PDF + public share).

Scoring legend:

| Score | Meaning |
|-------|---------|
| **H** | High / strong fit |
| **M** | Medium / conditional |
| **L** | Low / weak fit |
| **X** | Unsuitable for production claim |

Statuses: **Recommended** / **Conditional** / **Deferred** / **Rejected as production**.

---

## 2. Options

| ID | Name |
|----|------|
| **A** | Local workstation pilot only |
| **B** | Shared hosting PHP + MySQL |
| **C** | VPS PHP-FPM / Nginx (or Apache) / MySQL |
| **D** | Containerized VPS |
| **E** | Managed app platform |

---

## 3. Decision matrix

| Dimension | A Local | B Shared | C VPS | D Containers | E Managed |
|-----------|---------|----------|-------|--------------|-----------|
| Production suitability | **X** | **M** | **H** | **H** | **M** / unknown |
| Public share compatibility | **L** (local/internal only) | **M** (if HTTPS + `/public`) | **H** | **H** | **M** / variable |
| PDF generation compatibility | **H** (local Edge attested) | **L** (exec often blocked) | **H** (if headless validated) | **H** (sidecar possible) | **L–M** (often poor) |
| Security / control | **L** (workstation risk) | **M** | **H** | **H** | **M** (vendor limits) |
| Operational burden | **L** day-to-day / **X** for clients | **L–M** | **M** | **H** setup | **L–M** ops / **H** lock-in risk |
| Cost / complexity | Low cost; not production | Low cost; constraint risk | Medium | Higher | Variable |
| Backup / rollback | Weak for client delivery | Manual / limited | **H** (if designed) | **H** (if designed) | Vendor-dependent |
| Recommended status | **Rejected as production** | **Conditional** | **Recommended** | **Deferred** (later) | **Deferred** |

---

## 4. Dimension notes

### Production suitability

- **A** — подходит для internal demo / local MVP only; не production.
- **B** — возможен только после compatibility validation (особенно PDF).
- **C** — лучший баланс control vs complexity для first real pilot.
- **D** — сильный path, обычно избыточен как mandatory first.
- **E** — не выбран default: fit с headless PDF и MARS Model A не доказан.

### Public share

Route baseline: `GET /share/report/{token}` — direct PDF stream; hash-only token; 64-hex; 404/410 policy; no portal/email/landing.

Client-facing shares требуют stable HTTPS domain. Local-only и tunnels **не** production topology.

### PDF

Local MVP: Edge headless attested. Production generation на host должна быть **validated** или заменена serve-only / pre-generated upload mode.

### Backup / rollback

Conceptual VPS layout (не создавать сейчас): `current` / `releases` / `shared` storage + `.env.production` вне Git.

---

## 5. Final recommendation

| Field | Value |
|-------|-------|
| Recommended default | **Option C — VPS PHP-FPM/Nginx/MySQL** |
| Webserver preference | Nginx preferred; Apache acceptable |
| PHP / DB preference | PHP **8.3**; MySQL **8.x** |
| Decision state | **`RECOMMENDATION_READY`** — awaiting operator answers |

---

## 6. Why alternatives are deferred / rejected

| Option | Classification | Reason |
|--------|----------------|--------|
| **A** Local | **Rejected as production** | Нет production uptime / HTTPS / external client delivery posture |
| Public tunnel (any host) | **Rejected as production** | Unstable URLs; security/ops debt (Charter 01) |
| **B** Shared hosting | **Conditional** | Cheap, но PDF/exec/storage risks — нужен Compatibility Validation 01 |
| **D** Containers | **Deferred** | Reproducible, но higher setup cost for first pilot |
| **E** Managed platform | **Deferred** | Headless PDF / custom PHP fit unproven |
| Portal / email / landing | **Deferred (product)** | Not environment prerequisites for minimal share pilot |

---

## 7. Binding rule

Matrix scores are **advisory**. Binding selection requires filled [Operator Approval Checklist](I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPERATOR-APPROVAL-CHECKLIST-v0.1.md). Until then: **not** `PRODUCTION_SELECTED`, **not** `APPROVED_FOR_IMPLEMENTATION`.
