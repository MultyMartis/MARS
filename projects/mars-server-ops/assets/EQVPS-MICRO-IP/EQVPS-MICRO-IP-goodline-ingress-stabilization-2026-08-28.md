# EQVPS-MICRO-IP — Goodline Ingress Stabilization (2026-08-28)

**Asset:** EQVPS Micro-IP (`metacode-cloud.com` / `95.216.126.173`)  
**Operator network constraint:** Goodline fixed-line only (no alternate ISP / mobile / external VPN comparison)  
**Wave verdict:** `XHTTP_443_PRIMARY_PASS`  
**Companion baseline:** `EQVPS-MICRO-IP-current-ingress-baseline-2026-08-28.md`

---

## 1. Objective

Preserve the known-working **VLESS + TLS + XHTTP :8443** path, triage **VLESS + REALITY :443** on the operator’s required Goodline path, and — if Reality remains operationally unusable — migrate **TCP/443** to the proven **VLESS + TLS + XHTTP** family using the existing Let’s Encrypt identity for `metacode-cloud.com`.

---

## 2. Phase A — Pre-change XHTTP :8443 baseline

**Server-side (before mutation):** `x-ui` active; `:8443` listening; LE certificate valid; UFW allows 8443; no public `:80`.

**Operator Goodline client (direct path; TUN intended OFF):**

| Check | Result |
|-------|--------|
| TCP `:8443` | PASS |
| Client connect | PASS |
| Egress IP | `95.216.126.173` |
| DNS via tunnel | PASS |
| HTTPS browsing | PASS |

**Classification:** `XHTTP_8443_BASELINE = PASS`

---

## 3. Phase B — Pre-change backup

| Item | Value |
|------|-------|
| Remote | `/root/mars-backups/eqvps-ingress-goodline-prechange-20260828T091121Z.tgz` |
| Local | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-ingress-goodline-prechange-20260828T091121Z.tgz` |
| SHA256 | `c6a95274f28251941c2c806b5f5e29c1104f19d6cff0725e299b781a9f2ad9ae` |

Prior post-install backup retained: `02f66631dfc3055f2ba6b57a5538cd3454baa943a8826b860d65415e079b80ab`.

---

## 4. Phase C–E — Reality triage and bounded Goodline retest

### Runtime (effective Xray on `:443` before cutover)

| Parameter | Observed |
|-----------|----------|
| Protocol | VLESS |
| Port | 443 |
| Security | REALITY |
| Network | tcp |
| dest | `www.cloudflare.com:443` |
| serverNames | `www.cloudflare.com` |
| shortIds | present (matches local profile inventory) |

### Flow state

| Layer | Vision flow |
|-------|-------------|
| x-ui DB client row | `xtls-rprx-vision` |
| Generated `config.json` client | **null / omitted** |

**Classification:** `REALITY_EFFECTIVE_FLOW = MISMATCHED` (3X-UI regeneration omits Vision flow in effective runtime config despite DB correction attempt).

### Profile match (non-secret parameters)

**Classification:** `REALITY_PROFILE_MATCH = YES` (dest, serverNames, shortId alignment confirmed).

### Minimal correction attempted (Phase D)

- Applied DB/settings Vision flow correction and restarted `x-ui`.
- Effective generated config still omitted client `flow`.
- **One** bounded Goodline retest after correction: **FAIL**.

### Goodline Reality client failure class

Exact client error retained in local raw evidence logs:

`REALITY: received real certificate (potential MITM or redirection)`

**Classification:** `REALITY_GOODLINE = FAIL`

**Operational conclusion (Goodline-only, not universal):**

`REALITY_NOT_USABLE_ON_TARGET_NETWORK = CONFIRMED_OPERATIONALLY`

This documents failure on the operator’s required Goodline path only. It does **not** claim global ISP/DPI blocking of REALITY.

---

## 5. Phase F — Production decision

**CASE 2 applied:** Reality withdrawn as production ingress; `:443` migrated to TLS + XHTTP.

| Role | Ingress |
|------|---------|
| **PRIMARY** | VLESS + TLS + XHTTP — TCP/443 — `metacode-cloud.com` |
| **FALLBACK** | VLESS + TLS + XHTTP — TCP/8443 — `metacode-cloud.com` |
| **Reality** | NOT ACTIVE AS PRODUCTION INGRESS (historical evidence retained) |

---

## 6. Phase G–I — Cutover and validation

### Remote mutations (summary)

1. Removed REALITY inbound from TCP/443 (preserved in pre-change backup).
2. Created new VLESS + TLS + XHTTP inbound on TCP/443 using existing LE certificate.
3. Did **not** modify TCP/8443 inbound.
4. Updated UFW `:443` rule comment to `MARS XRAY XHTTP PRIMARY`.

### Goodline validation matrix (post-cutover)

| Path | TCP | TLS | Connect | Egress | DNS | Browsing |
|------|-----|-----|---------|--------|-----|----------|
| **:443 XHTTP primary** | PASS | PASS | PASS | PASS (`95.216.126.173`) | PASS | PASS |
| **:8443 XHTTP fallback** | PASS | PASS | PASS | PASS (`95.216.126.173`) | PASS | PASS |

**Classification:** `XHTTP_8443_AFTER_CUTOVER = PASS`

---

## 7. Phase J–K — Final exposure and security

### Public listeners

- `22/tcp` — SSH
- `443/tcp` — Xray XHTTP primary
- `8443/tcp` — Xray XHTTP fallback

### Localhost-only

- `127.0.0.1:20901` — 3X-UI panel
- `127.0.0.1:2096` — subscription

### UFW (final)

- `22/tcp` — MARS SSH
- `443/tcp` — MARS XRAY XHTTP PRIMARY
- `8443/tcp` — MARS XRAY TLS FALLBACK
- Default deny incoming / allow outgoing — active

### Port 80

Closed (no listener).

### Security preservation

| Control | Status |
|---------|--------|
| root SSH | no (drop-in hardening active) |
| password SSH | no (drop-in) |
| pubkey SSH | yes |
| MaxAuthTries | 3 |
| X11Forwarding | no (drop-in) |
| fail2ban sshd | active |
| NTP synchronized | yes |

---

## 8. Phase L — Final backup

| Item | Value |
|------|-------|
| Remote | `/root/mars-backups/eqvps-ingress-goodline-post-xhttp443-20260828T091206Z.tgz` |
| Local | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-ingress-goodline-post-xhttp443-20260828T091206Z.tgz` |
| SHA256 | `95adc3085b37cc59fd22fb1ac47deb7d968690ca9745fa0cff6d4b14e6e418c0` |

Restore runbook updated: `EQVPS-MICRO-IP-ingress-restore-runbook-v1.md`.

---

## 9. Operator client rollout notes (local contour only)

- New **:443 primary** client identity created during cutover; parameters stored in `secrets.local.md` and raw client JSON under local infrastructure (not Git).
- Existing **:8443 fallback** client profile unchanged and revalidated.
- Legacy Reality client profile retained locally for historical analysis only — not production.

---

## 10. Residuals / UNKNOWN

| Item | Status |
|------|--------|
| Strict TUN-OFF attestation | **PARTIAL** — `xray_tun` disable required elevation; tests still showed correct server egress on both paths |
| 3X-UI Vision flow omission in generated config | **OPEN** — known panel behavior; irrelevant while Reality is withdrawn |

---

## 11. Explicit non-mutations

Alternate ISP/mobile testing; Beget DNS/PTR; SSH port change; root/password SSH enable; nginx/Docker; public panel/subscription; Server A; AdminVPS; reboot; git commit.
