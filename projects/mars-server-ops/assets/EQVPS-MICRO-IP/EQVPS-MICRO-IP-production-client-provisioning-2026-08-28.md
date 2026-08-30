# EQVPS-MICRO-IP — Production Client Provisioning (2026-08-28)

**Asset:** EQVPS Micro-IP (`metacode-cloud.com` / `95.216.126.173`)  
**Wave:** Production device client provisioning (Phase A–O)  
**Ingress baseline:** `EQVPS-MICRO-IP-current-ingress-baseline-2026-08-28.md`  
**Operator runbook:** `EQVPS-MICRO-IP-operator-client-runbook-v1.md`  
**Local secrets / artifacts:** `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\` (not Git)

---

## Verdict

**READY_FOR_OPERATOR_CLIENT_ACCEPTANCE**

Human operator must manually import and test MCA-ONE PRIMARY and FALLBACK in v2rayN before production acceptance is complete.

---

## Server / stack baseline (verified)

| Item | Value |
|------|-------|
| 3X-UI | v3.7.0 |
| Xray | 26.7.28 |
| x-ui service | active |
| Panel bind | `127.0.0.1:20901` |
| Subscription bind | `127.0.0.1:2096` |
| Public panel | NO |
| Public subscription | NO |
| Public :80 | NO (not listening) |
| DB path | `/etc/x-ui/x-ui.db` |

---

## Production inbounds (unchanged)

### PRIMARY — inbound id 3

| Field | Value |
|-------|-------|
| Remark | `EQVPS-TLS-XHTTP-PRIMARY-443` |
| Protocol | VLESS |
| Security | TLS |
| Transport | XHTTP |
| Port | 443/tcp |
| TLS SNI | `metacode-cloud.com` |
| Health | listeners active; x-ui active |

### FALLBACK — inbound id 2

| Field | Value |
|-------|-------|
| Remark | `EQVPS-TLS-XHTTP-FALLBACK` |
| Protocol | VLESS |
| Security | TLS |
| Transport | XHTTP |
| Port | 8443/tcp |
| TLS SNI | `metacode-cloud.com` |
| Health | listeners active; x-ui active |

Ingress transport, TLS certificate, domain, and public ports were **not** modified in this wave.

---

## 3X-UI client model (discovered)

3X-UI v3.7.0 uses a **dual-layer** model:

1. **Effective Xray runtime** — clients listed in each inbound’s `settings.clients[]` JSON array inside `inbounds` table. This is **authoritative** for authentication.
2. **Panel global registry** — `clients` table plus `client_inbounds` junction for UI management, traffic accounting, and revocations.

Observations:

- Global `clients` rows may exist without inbound membership (e.g. historical `marsops-reality-primary` — orphaned Reality identity).
- The panel column “Привязанные входящие” may show `—` when `client_inbounds` is empty even if a global row exists.
- **Provisioning must update both:** inbound `settings.clients[]`, global `clients`, and `client_inbounds`.

Existing technical identities were **preserved** (not deleted):

| Name | Role |
|------|------|
| `marsops-reality-primary` | Historical / orphaned (Reality withdrawn) |
| `marsops-xhttp-443-primary` | Technical primary test identity on :443 |
| `marsops-fallback-xhttp` | Technical fallback test identity on :8443 |

---

## Production device inventory (approved)

Six devices × two inbounds = **12 new production identities**.

| Device | PRIMARY name | FALLBACK name |
|--------|--------------|---------------|
| MCA-ONE | MCA-ONE-PRIMARY-443 | MCA-ONE-FALLBACK-8443 |
| MCA-PHONE | MCA-PHONE-PRIMARY-443 | MCA-PHONE-FALLBACK-8443 |
| Unit-01 | Unit-01-PRIMARY-443 | Unit-01-FALLBACK-8443 |
| Unit-02 | Unit-02-PRIMARY-443 | Unit-02-FALLBACK-8443 |
| Unit-03 | Unit-03-PRIMARY-443 | Unit-03-FALLBACK-8443 |
| Unit-MichaelPhone | Unit-MichaelPhone-PRIMARY-443 | Unit-MichaelPhone-FALLBACK-8443 |

Each identity received a **unique** cryptographically random UUID. No UUID is shared across devices or between PRIMARY/FALLBACK pairs.

No WSP-ONE, WSP-PHONE, Unit-Metallka, or other unapproved devices were provisioned.

---

## Effective binding proof

Verified against effective Xray runtime config (`/usr/local/x-ui/bin/config.json`) after `systemctl restart x-ui`.

| Check | Result |
|-------|--------|
| PRIMARY_CLIENT_BINDINGS (6 production on :443) | **PASS** |
| FALLBACK_CLIENT_BINDINGS (6 production on :8443) | **PASS** |
| Wrong-inbound bindings | **0** |
| :443 total clients in inbound | 7 (6 production + 1 technical) |
| :8443 total clients in inbound | 7 (6 production + 1 technical) |
| TLS + XHTTP on both inbounds | unchanged |
| `client_inbounds` junction rows | 14 (12 new + 2 technical with links) |

---

## Local client artifacts (secret — not Git)

Root: `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\clients\`

Per device:

- `primary-443.vless.txt` — v2rayN-importable VLESS URI
- `fallback-8443.vless.txt`
- `primary-443.json` / `fallback-8443.json` — optional JSON outbound snippets
- `README.local.md`

Master inventory: `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\clients\CLIENT-INVENTORY.local.md`

XHTTP path/host/mode encoded from live inbound `stream_settings` (same path on both inbounds; path length 18 chars; host `metacode-cloud.com`; mode `auto`).

---

## v2rayN readiness

| Item | Status |
|------|--------|
| Operator-observed version | v7.22.3 x64 |
| Local auto-detect | inconclusive in agent environment |
| VLESS + TLS + XHTTP URI import | **expected compatible** with v7.x |
| Import method | clipboard import of `.vless.txt` contents (see operator runbook) |
| v2rayN upgrade | **not performed** in this wave |

---

## Backups

### Pre-provisioning

| Field | Value |
|-------|-------|
| Remote | `/root/mars-backups/eqvps-clients-pre-provision-20260828T102318Z.tgz` |
| Local | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-clients-pre-provision-20260828T102318Z.tgz` |
| SHA256 | `4d341d6b748811634e18e035a68fa77f4a9d6af230ab49f34e0f3d488a7ba7be` |

### Post-provisioning

| Field | Value |
|-------|-------|
| Remote | `/root/mars-backups/eqvps-clients-post-provision-20260828T102402Z.tgz` |
| Local | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-clients-post-provision-20260828T102402Z.tgz` |
| SHA256 | `76e0f144e08dcd5e24774003e286eef5706f65a868cb45f5d777cbd15b706949` |

Restore runbook updated: `EQVPS-MICRO-IP-ingress-restore-runbook-v1.md` (client-provisioning backup rows).

---

## Security preservation (verified)

| Control | Status |
|---------|--------|
| SSH :22 | allowed (UFW) |
| UFW default deny incoming | active |
| fail2ban sshd | active |
| Panel | localhost only |
| Subscription | localhost only |
| Port 80 | not publicly listening |
| NTP sync | yes |
| Reality reactivation | not performed |
| Ingress redesign | not performed |

---

## Raw evidence (local)

`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\client-provisioning-raw-2026-08-28\`

- `provisioning-evidence-20260828.txt`
- `provisioning-state-20260828.json`
- `binding-verify-redacted.json`
- `eqvps-production-client-provisioning-20260828.py`
- `eqvps-finish-provisioning-20260828.py`

---

## Operator next step

Manual MCA-ONE acceptance in v2rayN — see operator runbook § “First acceptance device (MCA-ONE)”.

Do **not** treat server-side provisioning as end-user connectivity proof until operator reports successful tests.
