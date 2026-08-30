# EQVPS-MICRO-IP — Current Ingress Baseline (2026-08-28)

**Asset:** EQVPS Micro-IP  
**Host:** `metacode-cloud.com` / `95.216.126.173`  
**OS:** Ubuntu 24.04.4 LTS  
**Stack:** 3X-UI v3.7.0 / Xray 26.7.28 / certbot 2.9.0  
**Status:** **PRODUCTION STABLE** (Goodline-validated)

---

## PRIMARY

| Field | Value |
|-------|-------|
| Protocol | VLESS |
| Security | TLS (Let’s Encrypt) |
| Transport | XHTTP |
| Port | **443/tcp** |
| TLS / SNI identity | `metacode-cloud.com` |
| Listener | `*:443` (Xray) |
| UFW | `443/tcp` — **MARS XRAY XHTTP PRIMARY** |
| Goodline client | **PASS** (connect, egress `95.216.126.173`, DNS, browsing) |

---

## FALLBACK

| Field | Value |
|-------|-------|
| Protocol | VLESS |
| Security | TLS (Let’s Encrypt) |
| Transport | XHTTP |
| Port | **8443/tcp** |
| TLS / SNI identity | `metacode-cloud.com` |
| Listener | `*:8443` (Xray) |
| UFW | `8443/tcp` — **MARS XRAY TLS FALLBACK** |
| Goodline client | **PASS** (unchanged from pre-cutover) |

---

## REALITY (historical / withdrawn)

| Field | Value |
|-------|-------|
| Status | **NOT ACTIVE AS PRODUCTION INGRESS** |
| Former role | VLESS + REALITY on TCP/443 |
| Goodline outcome | Operational failure — `REALITY: received real certificate…` |
| Scope of claim | Operator Goodline path only — **not** universal blocking |
| Evidence | Pre-change backup + local raw logs |

---

## Local-only services

| Service | Bind |
|---------|------|
| 3X-UI panel | `127.0.0.1:20901` |
| Subscription | `127.0.0.1:2096` |

No public panel. No public subscription endpoint.

---

## Public exposure summary

```
22/tcp    SSH (marsops key)
443/tcp   Xray XHTTP PRIMARY
8443/tcp  Xray XHTTP FALLBACK
80/tcp    CLOSED
```

---

## Certificate

- Domain: `metacode-cloud.com`
- Issuer: Let’s Encrypt
- Valid until: **2026-11-25** (per pre-cutover inventory; re-verify before renewal window)

---

## Authoritative backups (restore)

| Label | SHA256 |
|-------|--------|
| Post-install (2026-08-27 Reality era) | `02f66631dfc3055f2ba6b57a5538cd3454baa943a8826b860d65415e079b80ab` |
| Goodline pre-change (2026-08-28) | `c6a95274f28251941c2c806b5f5e29c1104f19d6cff0725e299b781a9f2ad9ae` |
| **Current production (2026-08-28)** | `95adc3085b37cc59fd22fb1ac47deb7d968690ca9745fa0cff6d4b14e6e418c0` |

Restore procedure: `EQVPS-MICRO-IP-ingress-restore-runbook-v1.md`

---

## Security baseline (unchanged)

- SSH: pubkey only, root disabled, MaxAuthTries 3, X11 off (MARS drop-in)
- fail2ban: active (sshd jail)
- UFW: active, default deny incoming
- DNS / NTP: healthy at cutover validation

---

## Change log pointer

Full wave evidence: `EQVPS-MICRO-IP-goodline-ingress-stabilization-2026-08-28.md`
