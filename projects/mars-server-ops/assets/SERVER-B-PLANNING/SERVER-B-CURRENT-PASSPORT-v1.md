# Server B Current Passport v1 — SERVER-B-PLANNING

**Status:** **LIVE RECONCILIATION + PHASE 3E3 DIRECT IP REJECTION + CLEANUP** — 2026-08-26  
**Authority:** Phase 3B–3E + 3E2 forensic + **3E3** final network verdict / temp SSH cleanup / sudo rotation  
**Asset locus:** `SERVER-B-PLANNING`  
**Final MCA / ATLAS asset ID:** **NOT ASSIGNED** — **PROVISIONED — FINAL ASSET REGISTRATION PENDING**  
**Not:** proof of VPN stack, domain DNS readiness, or accepted direct TUN-OFF path

---

## Intake / hardening gates

| Gate | Result |
|------|--------|
| Phase 3B read-only charter | **PASS WITH RESIDUALS** (2026-08-25) |
| Phase 3C secure SSH bootstrap | **PASS WITH RESIDUALS** (2026-08-25) |
| Phase 3D base OS security + network baseline | **PASS WITH RESIDUALS** (2026-08-25) |
| Phase 3E controlled reboot | **PASS** (2026-08-25) — [SERVER-B-CONTROLLED-REBOOT-v1.md](SERVER-B-CONTROLLED-REBOOT-v1.md) |
| Phase 3E / 3E3 direct network gate | **REJECTED** — current assigned IP for direct entry — [SERVER-B-DIRECT-NETWORK-GATE-v1.md](SERVER-B-DIRECT-NETWORK-GATE-v1.md) · [SERVER-B-PHASE-3E-FINAL-NETWORK-VERDICT-v1.md](SERVER-B-PHASE-3E-FINAL-NETWORK-VERDICT-v1.md) |
| Phase 3E2 connectivity forensic | **CLOSED** — temp SSH/443 **REMOVED** — [SERVER-B-DIRECT-CONNECTIVITY-FORENSIC-v1.md](SERVER-B-DIRECT-CONNECTIVITY-FORENSIC-v1.md) |
| Local access reference | **PRESENT** — `local/infrastructure/SERVER-B-PLANNING/secrets.local.md` |
| Remote access model | **KEY-ONLY** — [SERVER-B-SSH-ACCESS-MODEL-v1.md](SERVER-B-SSH-ACCESS-MODEL-v1.md) |

---

## 1. Identity (live)

| Field | Live observed | Classification |
|-------|---------------|----------------|
| Planning / inventory locus | `SERVER-B-PLANNING` | **PRESENT** |
| Provider | AdminVPS (operator attestation) | **NOT REJECTED** (product); assigned IP **REJECTED** for direct entry |
| Hostname | `metacode-cloud.com` | **MATCH** |
| Public domain intent | `metacode-cloud.com` | **PRESENT** — DNS **not** configured |
| Public IPv4 | `<SERVER_B_IP>` | **PRESENT** (redacted in Git; local `secret_ref`) |
| OS | Ubuntu 24.04.4 LTS | **MATCH** |
| Kernel | 6.8.0-36-generic (linux meta kept back at 6.8.0-138) | **PRESENT** |
| Architecture | x86_64 | **PRESENT** |
| Virtualization | KVM | **PRESENT** |
| Timezone | Etc/UTC | **PRESENT** |
| NTP service | active | **PRESENT** |
| Clock synchronized | no | **RESIDUAL** — NTP flag; wall clock **ACCURATE** via HTTPS Date cross-check |
| Reboot required | **NO** | **PRESENT** |
| Datacenter / FI1 confirmation | — | **SAFE UNKNOWN** from guest OS |

---

## 2. Resources (live)

| Resource | Live observed | Classification |
|----------|---------------|----------------|
| CPU | 2 vCPU — AMD EPYC (KVM) | **MATCH** |
| RAM | ~4 GB class (~3.8 GiB) | **MATCH** |
| Swap | 512 Mi `/swapfile` | **PRESENT** |
| Disk | 30G `/` | **MATCH** |

---

## 3. Network / listeners (live) — post 3E3

| Port / surface | Process / role | Classification |
|----------------|----------------|----------------|
| 22/tcp | sshd | **PRESENT** |
| 443/tcp SSH | — | **ABSENT** |
| DHCP client UDP/68 | systemd-networkd | **PRESENT** |
| Ephemeral UDP (timesyncd NTP client) | systemd-timesyncd | **PRESENT** |
| 3X-UI | — | **ABSENT** |
| Xray / VLESS / Reality | — | **ABSENT** |
| nginx | — | **ABSENT** |
| Docker application stack | — | **ABSENT** |

---

## 4. Firewall / fail2ban (live)

| Layer | Live observed | Classification |
|-------|---------------|----------------|
| ufw | **active** — deny in / allow out; **22/tcp only** (public) | **HARDENED** |
| fail2ban | **active** — jail `sshd` | **HARDENED** |
| IPv6 global address | none observed | **PRESENT** (link-local only) |

Docs: [SERVER-B-FIREWALL-BASELINE-v1.md](SERVER-B-FIREWALL-BASELINE-v1.md), [SERVER-B-FAIL2BAN-BASELINE-v1.md](SERVER-B-FAIL2BAN-BASELINE-v1.md).

---

## 5. SSH effective policy (Phase 3E3 revalidated)

| Field | Live observed | Classification |
|-------|---------------|----------------|
| ports | **22 only** | **PRESENT** |
| permitrootlogin | **no** | **HARDENED** |
| passwordauthentication | **no** | **HARDENED** |
| kbdinteractiveauthentication | **no** | **HARDENED** |
| pubkeyauthentication | **yes** | **PRESENT** |
| maxauthtries | **3** | **HARDENED** |
| Operator user | `marsops` (sudo) | **PRESENT** |
| Managed hardening drop-in | `/etc/ssh/sshd_config.d/00-mars-server-ops-hardening.conf` | **PRESENT** |
| Forensic SSH/443 drop-ins | — | **ABSENT** (removed 3E3) |
| ssh.service / ssh.socket | sshd running; `ssh.socket` enabled | **PRESENT** |
| Operator sudo password | **ROTATED** Phase 3E3 (local contour) | **PRESENT** |

---

## 6. Software baseline (live)

| Component | State | Class |
|-----------|-------|-------|
| docker | ABSENT | **ABSENT** |
| nginx | ABSENT | **ABSENT** |
| x-ui | ABSENT | **ABSENT** |
| xray | ABSENT | **ABSENT** |
| ufw | ACTIVE | **PRESENT** |
| fail2ban | ACTIVE | **PRESENT** |

---

## 7. Purpose

Independent secondary production VPN node (planned). Application stack **not** installed.

**Server A (MCA-VPN-001):** untouched.

---

## 8. Secret contour

| Item | State |
|------|-------|
| Local secrets file | **PRESENT** |
| Operator SSH key | **PRESENT** (local) |
| Operator sudo password | **PRESENT** (rotated Phase 3E3; previous **RETIRED**) |
| Initial root bootstrap secret | **PRESENT** (local; remote root SSH disabled) |
| Values in Git | **NONE** |

---

## 9. SAFE UNKNOWN / residuals

- Provider panel fields not re-checked.  
- NTP synchronization flag remains **no** (UDP/123); clock accuracy **ACCEPTABLE**.  
- Linux meta 6.8.0-138 kept back (security-relevant residual) — **not** addressed in 3E3.  
- Direct TUN-OFF path to current assigned IP **FAILED** (ping/22/443); root cause owner **SAFE UNKNOWN**.  
- AdminVPS Finland provider **NOT REJECTED**; current IP **REJECTED** for direct entry.  
- DNS production mapping deferred (no A/AAAA while IP rejected).  
- Final asset ID pending.  

---

*Server B Current Passport v1 · Phase 3E3 · SSH 22 only · direct IP rejected · provider not rejected · no secrets in Git.*
