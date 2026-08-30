# EQVPS-MICRO-IP — Public 3X-UI Panel + Subscription (2026-08-28)

**Asset:** EQVPS Micro-IP  
**Host:** `metacode-cloud.com` / `95.216.126.173`  
**Stack:** 3X-UI v3.7.0 / Xray 26.7.28  
**Wave:** Operator-facing management plane publication  
**Verdict:** **PUBLIC_PANEL_SUBSCRIPTION_PASS**

This document is **Git-safe**. It contains **no** panel passwords, secret web base paths, subscription tokens, or full subscription URLs.

---

## 1. Objective

Remove localhost-only operational friction for the 3X-UI panel and subscription endpoint while preserving the production VPN ingress on TCP/443 (PRIMARY) and TCP/8443 (FALLBACK).

**Critical defect (pre-wave):** Subscription output generated portable client profiles with remote address `localhost` instead of `metacode-cloud.com`, because the subscription service listened on `127.0.0.1:2096` and `subDomain` was unset.

**Fix scope:** 3X-UI settings in `x-ui.db` + native TLS via existing Let’s Encrypt certificate. **No nginx.** **No VPN inbound redesign.**

---

## 2. Root cause (3X-UI v3.7.0)

| Setting | Pre-wave (defect) | Post-wave (correct) |
|---------|-------------------|---------------------|
| `webListen` | `127.0.0.1` | empty (all interfaces) |
| `webDomain` | unset / empty | `metacode-cloud.com` |
| Panel TLS | none (plain HTTP on localhost) | LE fullchain + privkey |
| `subListen` | `127.0.0.1` | empty (all interfaces) |
| `subDomain` | unset / empty | `metacode-cloud.com` |
| Subscription TLS | none | LE fullchain + privkey |

**Authoritative field for generated client host:** `subDomain` (with public listen + TLS). When subscription is localhost-only, 3X-UI emits VLESS URIs as `@localhost:<port>` even if `host`/`sni` query params reference the public domain.

**Preserved unchanged:** `webBasePath`, `subPath`, `subURI`, panel credentials, `secret`, all production client UUIDs.

Certificate paths (both panel and subscription):

- `/etc/letsencrypt/live/metacode-cloud.com/fullchain.pem`
- `/etc/letsencrypt/live/metacode-cloud.com/privkey.pem`

Applied via 3X-UI DB update + `/usr/local/x-ui/x-ui cert` + `systemctl restart x-ui`.

---

## 3. Approved target state (achieved)

| Service | Protocol | Public bind | Domain | TLS identity |
|---------|----------|-------------|--------|--------------|
| **Panel** | HTTPS | `*:20901` | `metacode-cloud.com` | `metacode-cloud.com` |
| **Subscription** | HTTPS | `*:2096` | `metacode-cloud.com` | `metacode-cloud.com` |
| **VPN PRIMARY** | VLESS+TLS+XHTTP | `*:443` | `metacode-cloud.com` | unchanged |
| **VPN FALLBACK** | VLESS+TLS+XHTTP | `*:8443` | `metacode-cloud.com` | unchanged |

**Operator URLs (exact paths local-only):** `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\operator-access.local.md`

Git-safe URL shape:

- Panel: `https://metacode-cloud.com:20901/<SECRET_WEB_BASE_PATH>/`
- Subscription: `https://metacode-cloud.com:2096/<SECRET_SUB_PATH><subId>/`

---

## 4. MCA-ONE subscription model

MCA-ONE uses **two independent 3X-UI clients** (PRIMARY and FALLBACK) with **separate** `sub_id` values in the `clients` table:

| Profile | Inbound port | Subscription role |
|---------|--------------|-------------------|
| MCA-ONE-PRIMARY-443 | 443 | Primary-only subscription link |
| MCA-ONE-FALLBACK-8443 | 8443 | Fallback-only subscription link |

v2rayN import requires **both** subscription URLs (or local `.vless.txt` files) for full PRIMARY+FALLBACK coverage.

**Post-wave semantic check (MCA-ONE):**

| Check | PRIMARY | FALLBACK |
|-------|---------|----------|
| Address in VLESS URI | `metacode-cloud.com` | `metacode-cloud.com` |
| Port | 443 | 8443 |
| Security | TLS | TLS |
| Transport | XHTTP | XHTTP |
| `localhost` occurrences | 0 | 0 |
| `127.0.0.1` occurrences | 0 | 0 |

---

## 5. Production VPN preservation

| Item | Status |
|------|--------|
| PRIMARY `:443` listener | **UNCHANGED / HEALTHY** |
| FALLBACK `:8443` listener | **UNCHANGED / HEALTHY** |
| 12 production device clients | **UNCHANGED** (UUIDs preserved) |
| REALITY reactivation | **NOT DONE** |
| nginx | **NOT INSTALLED** |
| Permanent `:80` | **NOT OPEN** |

---

## 6. UFW (final public TCP)

| Port | Comment | Role |
|------|---------|------|
| 22/tcp | MARS SSH | SSH |
| 443/tcp | MARS XRAY XHTTP PRIMARY | VPN PRIMARY |
| 8443/tcp | MARS XRAY TLS FALLBACK | VPN FALLBACK |
| 20901/tcp | MARS 3XUI PANEL HTTPS | 3X-UI panel |
| 2096/tcp | MARS 3XUI SUBSCRIPTION HTTPS | 3X-UI subscription |

**Newly opened in this wave:** 20901, 2096 only.  
**Port 80:** no application listener; not permanently allowed.

---

## 7. Listeners (post-wave)

| Port | Process | Bind | Function |
|------|---------|------|----------|
| 22 | sshd | `0.0.0.0` / `[::]` | SSH |
| 443 | xray | `*` | VLESS TLS XHTTP PRIMARY |
| 8443 | xray | `*` | VLESS TLS XHTTP FALLBACK |
| 20901 | x-ui | `*` | 3X-UI HTTPS panel |
| 2096 | x-ui | `*` | 3X-UI HTTPS subscription |

No unexpected public application listeners observed at validation.

---

## 8. Validation summary

| Check | Result |
|-------|--------|
| `x-ui` active | PASS |
| Xray active | PASS |
| TCP 20901 (workstation → server) | PASS |
| TCP 2096 | PASS |
| TCP 443 / 8443 | PASS |
| Panel HTTPS + TLS hostname | PASS |
| Subscription HTTPS | PASS |
| MCA-ONE generated address correction | PASS (`localhost` count = 0) |
| Local client `.vless.txt` artifacts | PASS (all 12 files already use `metacode-cloud.com`) |

Raw evidence (local-only, may contain redacted secrets):  
`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\public-panel-subscription-raw-2026-08-28\`

---

## 9. Security baseline (immediate)

| Control | State |
|---------|-------|
| Panel HTTPS only | **YES** |
| Strong panel username/password | **PRESERVED** (not rotated) |
| Secret `webBasePath` | **PRESERVED** |
| Subscription secret path + per-client `sub_id` | **PRESERVED** |
| SSH hardening | **UNCHANGED** |
| fail2ban | **ACTIVE** (unchanged) |
| 3X-UI `twoFactorEnable` | **NOT ENABLED** (null in DB) |
| 3X-UI `sessionMaxAge` | **DEFAULT / unset** |
| 3X-UI `loginSecurity` | **DEFAULT / unset** |

**Residual hardening (deferred wave):** 2FA, session policy, login rate limits, optional IP allowlisting — not in scope for this wave.

Localhost panel access via SSH tunnel remains technically possible as emergency fallback; not required for normal operations.

---

## 10. Backups

| Label | Remote | Local copy | SHA256 |
|-------|--------|------------|--------|
| **Pre public-access** | `/root/mars-backups/eqvps-public-access-pre-public-access-20260828T104233Z.tgz` | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-public-access-pre-public-access-20260828T104233Z.tgz` | `cd7219cf63b477ddac0579c89defbc526fc8ea0175c71f15b6ecbfa1a1d1f0aa` |
| **Post public-access** | `/root/mars-backups/eqvps-public-access-post-public-access-20260828T104807Z.tgz` | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-public-access-post-public-access-20260828T104807Z.tgz` | `f2a965ab1901f4edb3c16710ec1a5fcca381a7a65e542e0c130dc49bb5f99400` |

Restore procedure updated in `EQVPS-MICRO-IP-ingress-restore-runbook-v1.md`.

---

## 11. Related documents

| Document | Role |
|----------|------|
| `EQVPS-MICRO-IP-operator-client-runbook-v1.md` | Normal operator workflow (updated) |
| `EQVPS-MICRO-IP-ingress-restore-runbook-v1.md` | Restore inventory (updated) |
| `EQVPS-MICRO-IP-current-ingress-baseline-2026-08-28.md` | VPN ingress baseline (VPN section still valid; management plane superseded by this wave) |
| `operator-access.local.md` (local-only) | Exact panel + subscription URLs |

---

## 12. Operator next steps

See `EQVPS-MICRO-IP-operator-client-runbook-v1.md` §1 and §5. Summary:

1. Open public panel URL from `operator-access.local.md` (no SSH tunnel required).
2. Confirm login with existing credentials.
3. Import MCA-ONE **both** subscription links into v2rayN (remove prior localhost-imported entries).
4. Verify PRIMARY address = `metacode-cloud.com:443`, FALLBACK = `metacode-cloud.com:8443`, transport XHTTP.
5. Connect and confirm external IP `95.216.126.173`.
