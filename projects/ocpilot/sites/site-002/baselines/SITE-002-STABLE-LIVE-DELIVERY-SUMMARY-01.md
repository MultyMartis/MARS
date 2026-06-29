# SITE-002 — Stable Live Delivery Summary Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-DELIVERY-SUMMARY-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Registered at:** 2026-06-29  
**Mode:** Delivery page summary strip — Commercial Trust services reuse  
**Status:** **ACTIVE / PASS**

---

## 1. Authority state

**Checkpoint:** `SITE-002-STABLE-LIVE-DELIVERY-SUMMARY-01`

**Parent authority:** `SITE-002-STABLE-LIVE-M9.14-DELIVERY-01` (page) · `SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01` (card pattern) · `SITE-002-STABLE-LIVE-CUSTOM-PROOF-STRIP-01` (reuse strategy)

**Scope:** Block `.zpm-delivery-summary` on `/delivery` only (BLOCK 01 — organization section).

---

## 2. Live surface

| Item | Value |
|------|--------|
| URL | https://zpm.new-site.space/delivery |
| Twig | `catalog/view/theme/default/template/information/delivery.twig` |
| Wrapper | `.zpm-delivery-summary` |
| Card pattern | `.zpm-commercial-trust__services` + `.zpm-commercial-trust__service*` |
| CSS append | `assets/css/style.css` — `SITE-002 — Delivery summary → commercial trust services reuse` |

### Cards (4)

| Title | Icon | Body |
|-------|------|------|
| География | `fad fa-map-marked-alt` | Поставки по России |
| Точки отгрузки | `fad fa-warehouse` | Барнаул · склад партнёра в Московской области |
| Способы получения | `fad fa-shipping-fast` | Самовывоз · транспортная компания |
| Сопровождение | `fad fa-user-headset` | Менеджер заказа на этапе отгрузки |

---

## 3. SHA256 (post-deploy)

| File | post SHA256 |
|------|-------------|
| `delivery.twig` | `19af3aa1a94c4253ce7bc889796ccf73c48f940f8d858aa630b21f7d76d35bbe` |
| `style.css` | `7470384cf7d585a3d853580716175d45a65ad09079e254caf1f1510030393b2d` |

Manifest: [reports/delivery-summary-work/deploy-sha256.json](../reports/delivery-summary-work/deploy-sha256.json)

---

## 4. Rollback

```bash
python projects/ocpilot/sites/site-002/reports/delivery-summary-work/site-002-delivery-summary-rollback.py
```

Backups: `backups/*.{pre-site-002-delivery-summary-01.bak}`

---

## 5. Report

[reports/SITE-002-DELIVERY-SUMMARY-RESTYLE.md](../reports/SITE-002-DELIVERY-SUMMARY-RESTYLE.md)
