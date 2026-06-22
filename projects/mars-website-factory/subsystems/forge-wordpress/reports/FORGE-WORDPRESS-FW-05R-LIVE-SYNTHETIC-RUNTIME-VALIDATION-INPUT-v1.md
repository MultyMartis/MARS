# Forge WordPress — FW-05R Live Synthetic Runtime Validation Input v1

**Document type:** Consumer validation input  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03 complete → **FW-05R authorized**

---

## Runtime provider

**MARS Localhost Infrastructure** — MLI-WP-SYN-001

---

## MLI runtime binding

| Field | Value |
|-------|-------|
| **Runtime ID** | MLI-WP-SYN-001 |
| **Synthetic case** | FWS-0001 |
| **Runtime path** | `D:\MARS-Localhost\sites\wordpress\synthetic\fws-0001` |
| **URL (HTTP)** | `http://fws-0001.test` |
| **Manifest** | [MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md](../../../../mars-localhost-infrastructure/manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md) |
| **Handoff** | [MARS-LOCALHOST-MLI-03-FORGE-WORDPRESS-RUNTIME-HANDOFF-v1.md](../../../../mars-localhost-infrastructure/reports/MARS-LOCALHOST-MLI-03-FORGE-WORDPRESS-RUNTIME-HANDOFF-v1.md) |

---

## Stack (verified MLI-03)

| Component | Version |
|-----------|---------|
| WordPress | 7.0 (ru_RU) |
| PHP | 8.3.30 |
| MySQL | 8.4.3 (loopback) |
| Apache | 2.4.66 |
| WP-CLI | 2.12.0 |

---

## FW-05R scope (not executed in MLI-03)

FW-05R shall:

1. Install synthetic Forge theme
2. Install functionality plugin
3. Connect ACF compatibility profile
4. Load synthetic content
5. Run PHP/WPCS validation
6. Verify CPT/templates/admin
7. Execute WordPress visual comparison
8. Assemble RC2
9. Update WPilot handoff simulation

---

## Preconditions

| Check | MLI-03 state |
|-------|----------------|
| WordPress installed | **YES** |
| Isolated DB/user | **YES** |
| Backup baseline | **YES** — `baseline-001` |
| Forge theme/plugin | **NO** — FW-05R installs |
| `fws-0001.test` hosts | **PENDING** — operator elevation before browser gate |
| HTTPS | Cert ready; untrusted local CA |

---

## Stop conditions

- Do not use FP-0002 or client data
- Do not deploy to production
- Do not register AG-WP-001 without charter
- Reset only via documented baseline scripts

---

*FW-05R input v1 — MLI-03 consumer handoff.*
