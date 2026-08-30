# FRIENDHOSTING-DE — Architecture v1

**inventory_ref:** FRIENDHOSTING-DE  
**Status:** **CANONICAL** architecture documentation  
**Secrets:** none  

---

## 1. Purpose

One place for how FriendHosting VPN, operator panel, and certificate issuance relate — without scattering facts across REPORT-only prose.

---

## 2. Primary VPN path (clients)

```text
Device (Windows / phone)
  → v2rayN (or compatible) / TUN or system proxy
  → metacode-cloud.com:8443
  → Xray (VLESS + TLS + RAW/TCP)
  → Internet egress (public IP 92.42.99.126)
```

| Property | Value |
|----------|-------|
| Inbound | `FRIENDHOSTING-DE-RAW-8443` |
| Auth | Per-device VLESS UUID (one identity per device) |
| SNI | `metacode-cloud.com` |
| flow | empty |
| sniffing | OFF |
| nginx on `:8443` | **No** — Xray owns `:8443` |

---

## 3. Operator panel path

```text
Operator browser
  → https://metacode-cloud.com:443/<secret-web-path>
  → nginx (TLS termination)
  → 127.0.0.1:20901 (3X-UI)
```

| Property | Value |
|----------|-------|
| Panel bind | localhost `:20901` only |
| Public panel port `:2096` | **UFW DENY** (may still listen process-side) |
| Preferred UX | 3X-UI native QR / copy-link |
| Secret path | Local secret contour only — **never Git** |

Do **not** open `:2096` publicly for convenience.

---

## 4. ACME / TLS path

```text
Let's Encrypt (HTTP-01)
  → TCP/80
  → nginx webroot (/var/www/letsencrypt)
  → certbot
  → deploy/reload hook
  → consumers: nginx (:443) + 3X-UI/Xray TLS material for :8443
```

| Property | Value |
|----------|-------|
| Domain | `metacode-cloud.com` |
| Method | HTTP-01 webroot |
| Scheduler | certbot.timer |
| Dry-run | **PASS** (P2 clean reconciliation 02) |
| Detail | [FRIENDHOSTING-DE-TLS-ACME-LIFECYCLE-v1.md](FRIENDHOSTING-DE-TLS-ACME-LIFECYCLE-v1.md) |

---

## 5. SSH / recovery path

```text
Operator workstation
  → SSH key → marsops@92.42.99.126:3333
  → sudo (as required by charter)
```

Root key recovery access retained; password auth disabled. See [FRIENDHOSTING-DE-ACCESS-MODEL-v1.md](FRIENDHOSTING-DE-ACCESS-MODEL-v1.md).

---

## 6. Explicit non-ownership

| Surface | Owner |
|---------|-------|
| `:443` public HTTPS | **nginx** (panel reverse proxy) |
| `:8443` VPN | **Xray** |
| `:80` | **nginx** ACME / redirect narrow surface |
| Future `:24443` | Planned **Xray** reserve — **not deployed** |

Do **not** put RAW Xray on `:443` while nginx owns that port.

---

## 7. Related

- Port map: [FRIENDHOSTING-DE-PORT-SERVICE-MAP-v1.md](FRIENDHOSTING-DE-PORT-SERVICE-MAP-v1.md)  
- Security: [FRIENDHOSTING-DE-SECURITY-POSTURE-v1.md](FRIENDHOSTING-DE-SECURITY-POSTURE-v1.md)  
- Inventory: [../../SERVER-INVENTORY-v1.md](../../SERVER-INVENTORY-v1.md)

---

*Architecture v1 · 2026-08-30.*
