# FRIENDHOSTING-DE — Security posture v1

**inventory_ref:** FRIENDHOSTING-DE  
**Status:** **CANONICAL** safe posture (no secrets)  
**Classification of `:2096`:** **ACCEPTED HARDENED BOUNDARY** (UFW DENY) — not “port fully absent”

---

## 1. SSH

- Port `3333/tcp`  
- Key-based only; PasswordAuthentication disabled  
- `marsops` operational + sudo  
- Root password remote login prohibited  
- Root key recovery retained  

---

## 2. Firewall (UFW)

| Policy | Detail |
|--------|--------|
| Default | deny incoming |
| Allow | `3333`, `443`, `8443`, `80` |
| Deny (explicit / default) | `20901`, `2096`, all other |

---

## 3. fail2ban / logging

- fail2ban active (sshd jail and related)  
- journald size cap applied (P2 wave)  

---

## 4. Public surface

| Surface | Posture |
|---------|---------|
| `:80` | Narrow ACME / redirect |
| `:443` | nginx TLS + authenticated panel path |
| `:8443` | VLESS TLS — authorized UUIDs only |
| `:3333` | SSH keys only |

---

## 5. Localhost services

- 3X-UI on `127.0.0.1:20901`  
- Not a public listen for panel UI  

---

## 6. TLS

- Let's Encrypt for `metacode-cloud.com`  
- Automated renew + dry-run PASS  
- Hook reloads consumers (nginx / panel-Xray TLS path)  

---

## 7. Memory / OOM

- 2 GiB swap present (Plus baseline)  
- RAM ~1.9 GiB — avoid memory-heavy unrelated stacks without capacity charter  

---

## 8. Updates

- Unattended package upgrade waves: **not** standing practice without charter  
- Security updates: human-supervised, backup-first  

---

## 9. Backup / secrets

- Final operational backup verified (hash twin)  
- Secrets in local contour + secret-bearing archives — never Git  
- Restore procedure confirmed; bare-metal drill pending  

---

## 10. Operator access

See [FRIENDHOSTING-DE-ACCESS-MODEL-v1.md](FRIENDHOSTING-DE-ACCESS-MODEL-v1.md).

---

## 11. Known residuals

| Residual | Classification |
|----------|----------------|
| `*:2096` process listener while UFW DENY | **ACCEPTED HARDENED BOUNDARY** |
| Unit-* physical device tests pending | Operational residual (identity ready) |
| Long-term soak | **NOT YET PROVEN** |
| Bare-metal restore | **NOT YET EXERCISED** |
| P4 `:24443` | **DEFERRED** |

---

## 12. Related

- Port map: [FRIENDHOSTING-DE-PORT-SERVICE-MAP-v1.md](FRIENDHOSTING-DE-PORT-SERVICE-MAP-v1.md)  
- P2 evidence: [../../reports/MARS-SERVER-OPS-FRIENDHOSTING-P2-CLEAN-HARDENING-RECONCILIATION-02.md](../../reports/MARS-SERVER-OPS-FRIENDHOSTING-P2-CLEAN-HARDENING-RECONCILIATION-02.md)

---

*Security posture v1 · 2026-08-30.*
