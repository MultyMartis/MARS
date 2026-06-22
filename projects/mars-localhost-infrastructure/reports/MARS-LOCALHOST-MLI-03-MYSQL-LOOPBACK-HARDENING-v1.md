# MARS Localhost MLI-03 — MySQL Loopback Hardening v1

**Document type:** MySQL loopback hardening validation  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03  
**Git baseline:** commit `4621388` on `mars/post-cycle8-live-tests`

---

## Objective

Confirm MySQL accepts TCP connections on loopback only for the primary SQL port (3306), supporting MLI-03 WordPress database access without exposing 3306 on all interfaces.

---

## Configuration verified

| Setting | Value | Result |
|---------|-------|--------|
| `bind_address` | `127.0.0.1` | **PROVEN** |

---

## Listen state

| Endpoint | Port | Protocol | Result |
|----------|------|----------|--------|
| `127.0.0.1` | 3306 | MySQL | **PROVEN** — LISTENING |
| `0.0.0.0` | 3306 | MySQL | **PROVEN** — NOT listening |
| All interfaces | 33060 | MySQL X Protocol | **WITH LIMITATIONS** — still listening |

---

## Assessment

| Check | Status |
|-------|--------|
| Primary SQL port loopback-only | **PROVEN** |
| WordPress / WP-CLI DB connectivity on loopback | **PROVEN** (via successful MLI-03 install and queries) |
| X Protocol (33060) loopback-only | **NOT PROVEN** — remains on all interfaces |

---

## Residual risk

Port **33060** (MySQL X Protocol) is outside the MLI-03 WordPress hardening target for port 3306. Restricting 33060 was **not** validated in this pass. WordPress and WP-CLI use classic MySQL protocol on **3306** only.

---

## Related

- [MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md](../MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md)

---

*MySQL loopback hardening report v1 — MLI-03.*
