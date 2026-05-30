# Website Factory — Site Type Matrix v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/registry/`  
**Статус:** сравнительная матрица для классификации и planning  
**Связь:** [SITE-TYPE-REGISTRY-v1.md](SITE-TYPE-REGISTRY-v1.md)

**Легенда шкал:**

| Шкала | Значения |
|-------|----------|
| **Page count** | `1` · `low` (2–15) · `medium` (15–100) · `high` (100+) · `app-heavy` (мало публичных, много app routes) |
| **Importance / capability** | `—` (не применимо / отсутствует) · `low` · `medium` · `high` · `critical` |
| **Complexity** | `low` · `medium` · `high` · `very high` |

---

## Матрица

| site_type_code | Page count | SEO importance | PPC importance | Lead generation | Catalog | Cart | Payment | User accounts | Custom logic | Integrations | Complexity |
|----------------|------------|----------------|----------------|-----------------|---------|------|---------|---------------|--------------|--------------|------------|
| **LANDING** | 1 | low | **critical** | **critical** | — | — | — | — | low | low | low |
| **PROMO** | low | **high** | medium | high | — | — | — | — | low | low | medium |
| **CATALOG** | high | **high** | medium | medium | **critical** | — | — | — | medium | medium | high |
| **ECOMMERCE** | high | **high** | high | medium | **critical** | **critical** | **critical** | medium | medium | **high** | **high** |
| **CORPORATE** | medium–high | **high** | medium | high | medium | low | low | medium | **high** | **high** | **high** |
| **SAAS** | medium + app | medium | high | high | — | — | **critical** | **critical** | **high** | **high** | **very high** |
| **WEB_APPLICATION** | app-heavy | low | — | — | — | — | low | **critical** | **critical** | **high** | **very high** |
| **MARKETPLACE** | **very high** | **high** | high | medium | **critical** | **critical** | **critical** | **critical** | **critical** | **very high** | **very high** |

---

## Краткие пояснения по столбцам

### Page count

- **LANDING** — одна conversion page (+ legal).
- **PROMO** — типичный SMB/corporate-lite сайт.
- **CATALOG / ECOMMERCE / MARKETPLACE** — масштабируются с ассортиментом и sellers.
- **WEB_APPLICATION** — публичный слой минимален; основной объём — authenticated app.

### SEO importance

- **Critical path:** PROMO, CATALOG, ECOMMERCE, CORPORATE, MARKETPLACE — organic acquisition существенен.
- **Low:** LANDING (PPC-first), WEB_APPLICATION (task tool, not discovery surface).

### PPC importance

- **Critical:** LANDING — primary acquisition channel.
- **High:** SAAS, ECOMMERCE, MARKETPLACE — paid scale common.
- **— / low:** WEB_APPLICATION — rarely PPC-driven.

### Lead generation

- **Critical:** LANDING.
- **High:** PROMO, CORPORATE, SAAS (trial/signup).
- **Medium:** CATALOG (RFQ), ECOMMERCE (secondary to purchase), MARKETPLACE (buyer + seller onboarding).

### Catalog / Cart / Payment

- **CATALOG:** catalog **critical**; cart/payment explicitly **—**.
- **ECOMMERCE:** all three **critical**.
- **MARKETPLACE:** catalog + cart + payment **critical** + multi-seller layer.

### User accounts

- **Critical:** SAAS, WEB_APPLICATION, MARKETPLACE.
- **Medium:** ECOMMERCE (buyer account), CORPORATE (partner/employee portals).

### Custom logic / Integrations

- Растут от PROMO (minimal) → CORPORATE → Extended Types.
- **MARKETPLACE** и **WEB_APPLICATION** — maximum integration surface.

### Complexity

- **Core Types:** LANDING (low) → ECOMMERCE/CORPORATE (high).
- **Extended Types:** SAAS, WEB_APPLICATION, MARKETPLACE — **very high**; require architecture beyond default Factory production.

---

## Группы

| Group | Members | Default Factory production |
|-------|---------|---------------------------|
| **Core** | LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE | **Yes** — default targets |
| **Extended** | SAAS, WEB_APPLICATION, MARKETPLACE | **No** — charter + extended architecture required |

---

*Matrix version: v1.*
