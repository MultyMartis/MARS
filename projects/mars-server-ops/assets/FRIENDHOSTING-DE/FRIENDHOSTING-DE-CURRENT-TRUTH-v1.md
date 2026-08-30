# FRIENDHOSTING-DE — Canonical current truth v1

**Status:** **CANONICAL** for documentation waves as of 2026-08-30  
**Evidence precedence:** newer reproducible reports win over older chat/handoffs  
**Secrets:** none in this file  

---

## 1. Identity

| Field | Value |
|-------|-------|
| Stable ID | `FRIENDHOSTING-DE` |
| Provider | FriendHosting |
| Country / signal | Germany / FRA-facing |
| Network | `92.42.99.0/24` · AS47447 / 23M GmbH |
| IPv4 | `92.42.99.126` |
| Domain / SNI | `metacode-cloud.com` |
| Hostname label | `imart216311` |
| OS | Ubuntu 24.04.4 LTS |
| SSH | `3333/tcp` |

---

## 2. Hardware (accepted Plus baseline)

| Resource | Value |
|----------|-------|
| vCPU | 2 (Common KVM) |
| RAM | ~1.9 GiB (MemTotal ≈ 2014844 kB) |
| Disk | 20 GiB (`/dev/sda`) |
| Root FS | ~19G ext4 |
| Swap | 2 GiB |

---

## 3. Stack

| Component | Version / note |
|-----------|----------------|
| 3X-UI | 3.7.0 |
| Xray | 26.7.28 |
| nginx | public TLS front for panel |
| Let's Encrypt / certbot | HTTP-01 webroot; renew dry-run **PASS** |
| UFW | default deny |
| fail2ban | SSH jail active |

---

## 4. Network / services (summary)

| Port / bind | Role |
|-------------|------|
| `80/tcp` | nginx ACME / HTTP→HTTPS narrow surface |
| `3333/tcp` | SSH |
| `443/tcp` | nginx TLS → 3X-UI reverse proxy |
| `8443/tcp` | Xray VLESS TLS RAW (primary VPN) |
| `127.0.0.1:20901` | 3X-UI panel (localhost) |
| `*:2096` | process may listen; **UFW DENY** accepted boundary |
| `24443/tcp` | **DEFERRED** (P4 reserve) — not present |

Full map: [FRIENDHOSTING-DE-PORT-SERVICE-MAP-v1.md](FRIENDHOSTING-DE-PORT-SERVICE-MAP-v1.md)

---

## 5. Security (summary)

- Key-based SSH; `marsops` sudo; PasswordAuthentication **disabled**  
- Root password remote login **prohibited**; root key recovery access **retained**  
- UFW default deny; fail2ban SSH; journald size cap  
- ACME renewal automated; dry-run **PASS**  

Detail: [FRIENDHOSTING-DE-SECURITY-POSTURE-v1.md](FRIENDHOSTING-DE-SECURITY-POSTURE-v1.md)

---

## 6. VPN

| Field | Value |
|-------|-------|
| Protocol | VLESS |
| Security | TLS |
| Network | RAW/TCP |
| Port | `:8443` |
| SNI | `metacode-cloud.com` |
| flow | empty |
| sniffing | OFF |
| Inbound remark | `FRIENDHOSTING-DE-RAW-8443` |

---

## 7. Per-device identities (safe labels only)

| Label | Status |
|-------|--------|
| WSP-ONE | physically **PASS** |
| MCA-PHONE | physically **PASS** |
| Unit-01 | SERVER_IDENTITY_READY · DEVICE_TEST_PENDING |
| Unit-02 | SERVER_IDENTITY_READY · DEVICE_TEST_PENDING |
| Unit-03 | SERVER_IDENTITY_READY · DEVICE_TEST_PENDING |
| Unit-MichaelPhone | SERVER_IDENTITY_READY · DEVICE_TEST_PENDING |
| MCA-ONE-FRIENDHOSTING-DE-RAW-8443 | **RETIRED / REMOVED FROM SERVER** |

Model: [FRIENDHOSTING-DE-DEVICE-IDENTITY-MODEL-v1.md](FRIENDHOSTING-DE-DEVICE-IDENTITY-MODEL-v1.md)

---

## 8. Acceptance

| Gate | Result |
|------|--------|
| Transport | **PASS** |
| WSP-ONE | **PASS** |
| MCA-PHONE | **PASS** |
| Cursor | **PASS** |
| ChatGPT | **PASS** |
| YouTube playback | **PASS** |
| Long-term soak | **NOT YET PROVEN** |

---

## 9. Lifecycle

| Label | Value |
|-------|-------|
| Programme lifecycle | **OPERATIONALLY ACCEPTED — CURRENT VPN WORKLOAD** |
| Production | **not** `PRODUCTION_ACCEPTED` |
| Control role | Independent modern control (third control vs VEESP / EQVPS) |
| Soak | **NOT YET PROVEN** |
| Generic production suitability (arbitrary apps) | **NOT CLAIMED** |

---

## 10. Final backup (canonical freeze)

| Field | Value |
|-------|-------|
| Stamp | `20260830T125003Z` |
| Remote | `/root/mars-backups/friendhosting-final-operational-20260830T125003Z.tgz` |
| Local | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-final-operational-20260830T125003Z.tgz` |
| Size | 80746687 bytes |
| SHA-256 | `1012e3157db97ea3ba2a1c4d0b8d02328223e6656adf12ade22fa1adbb3a0ea2` |
| Remote/local hash | **MATCH** |
| Readability | **PASS** |
| Restore procedure | **CONFIRMED** |
| Bare-metal restore | **NOT YET EXERCISED** |

Distinction: **BACKUP VERIFIED** ≠ **FULL DISASTER RESTORE TESTED**.

---

## 11. Local secret contour

`X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\`

Holds panel path, credentials, client UUIDs/URIs, keys — **out of Git**.

---

## 12. Deferred / next

| Item | State |
|------|-------|
| P4 `:24443` reserve | **DEFERRED** |
| Multi-day soak / light monitoring | Next FriendHosting ops priority |
| Bare-metal DR drill | Optional high-value future wave |

---

*Current truth v1 · reconciled from P2/P3/final-backup evidence · 2026-08-30.*
