# EQVPS-MICRO-IP — Operator Client Runbook v1

**Asset:** EQVPS Micro-IP (`metacode-cloud.com` / `95.216.126.173`)  
**Stack:** 3X-UI v3.7.0 / Xray 26.7.28  
**Production candidate (2026-08-29):** VLESS + TLS + **RAW/tcp** on TCP/**8443**  
**Experimental/deferred:** VLESS + TLS + XHTTP on TCP/443 (technical test client only)  
**Local secrets:** `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\secrets.local.md`  
**Local operator URLs:** `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\operator-access.local.md`  
**Public-access wave evidence:** `EQVPS-MICRO-IP-public-panel-subscription-2026-08-28.md`  
**RAW full-transfer + cleanup evidence:** `EQVPS-MICRO-IP-raw-full-transfer-and-client-registry-cleanup-2026-08-29.md`

This document is **Git-safe**. It contains **no** panel passwords, UUIDs, VLESS URIs, subscription tokens, or private keys.

---

## 0. Daily operator workflow — use 3X-UI first

**For normal device provisioning, key retrieval, QR codes, and subscriptions:**

→ **Open the 3X-UI panel** and work from the inbound/client list there.

Do **not** require operators to browse MARS local files for day-to-day key retrieval.

| Need | Where |
|------|-------|
| VLESS link / QR / subscription for a device | **3X-UI panel** |
| Panel URL, subscription base path | `operator-access.local.md` (local-only) |
| Panel login | `secrets.local.md` (local-only) |
| Backups, forensic exports, automation inputs | MARS local tree under `EQVPS-MICRO-IP\` |

Local `clients\` artifacts remain valid as **backup / evidence / disaster recovery** — regenerate or refresh after panel changes when maintaining offline copies.

---

## 1. Normal 3X-UI panel access (public HTTPS)

1. Open the **exact panel URL** from `operator-access.local.md`.
2. URL shape (placeholders only): `https://metacode-cloud.com:20901/<SECRET_WEB_BASE_PATH>/`
3. Log in with panel credentials referenced in `secrets.local.md`.
4. Confirm browser shows valid TLS for `metacode-cloud.com`.

**Do not** commit the real web base path, username, or password to Git.

### Emergency fallback (SSH tunnel)

If public panel access fails on a specific network path:

```powershell
ssh -i "X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\ssh\marsops_ed25519" -L 20901:127.0.0.1:20901 marsops@95.216.126.173
```

Then browse `https://127.0.0.1:20901/<SECRET_WEB_BASE_PATH>/` (accept certificate hostname mismatch only as a temporary emergency measure).

---

## 2. Production inbound layout (2026-08-29)

| Role | Port | Protocol | Security | Transport | TLS identity |
|------|------|----------|----------|-----------|--------------|
| **Production candidate** | 8443/tcp | VLESS | TLS | **RAW (tcp)** | `metacode-cloud.com` |
| **Experimental/deferred** | 443/tcp | VLESS | TLS | XHTTP | `metacode-cloud.com` |

- Use **RAW :8443** for production device profiles.
- **443 XHTTP** is **not** production fleet ingress; at most one technical test client remains for deferred experiments.
- REALITY is **not** active production ingress.

Inbound remarks in panel:

- RAW: `EQVPS-TLS-RAW-8443`
- XHTTP (deferred): `EQVPS-TLS-XHTTP-PRIMARY-443`

---

## 3. Approved production devices

Six devices; each has **one** RAW production client on `:8443`:

- MCA-ONE
- MCA-PHONE
- Unit-01
- Unit-02
- Unit-03
- Unit-MichaelPhone

Panel client naming pattern:

`{Device}-RAW-8443`

Example remarks: `MCA-ONE-RAW-8443`, `Unit-02-RAW-8443`.

---

## 4. Import into v2rayN (Windows)

Operator-observed client: **v2rayN v7.22.3 x64**.

### Recommended: 3X-UI panel or subscription

1. Open 3X-UI → inbound **EQVPS-TLS-RAW-8443** → select device client.
2. Copy **VLESS link** or scan **QR**, or use **subscription** if configured for that client.
3. Import into v2rayN.
4. Verify profile shows:

| Field | Expected |
|-------|----------|
| Address | `metacode-cloud.com` |
| Port | `8443` |
| Transport | **raw** (tcp) |
| Security | TLS |
| SNI | `metacode-cloud.com` |

If v2rayN shows `localhost` or `127.0.0.1` as the server address, **delete those entries** — they are stale subscription artifacts.

Subscription base shape (placeholders only):

`https://metacode-cloud.com:2096/<SECRET_SUB_PATH><subId>/`

Per-device subscription URLs (if used) live in `operator-access.local.md`.

### Local file fallback (backup path only)

Legacy/local files under `clients\<Device>\` may exist for disaster recovery. Prefer panel-generated links for current truth after 2026-08-29 cleanup.

---

## 5. First acceptance / connectivity check

1. Connect the device profile (RAW :8443).
2. Confirm external IP is `95.216.126.173` (e.g. browse to an IP echo service or use client built-in test).
3. Verify **full sites**, not just HEAD/latency:
   - YouTube loads and plays
   - ChatGPT loads (403/challenge at edge is OK if page completes — **hang is not OK**)
   - Google works

**Note (2026-08-29 diagnostic):** Small HTTP checks and latency tests are **insufficient**. Use real browser or full-body download tests for acceptance.

Do **not** delete unrelated VEESP or other profiles unless explicitly chartered.

---

## 6. Add a future approved device

Only the six approved device names may receive production RAW clients.

1. **Backup first** (§10).
2. Open 3X-UI panel.
3. On inbound **EQVPS-TLS-RAW-8443**, ensure a client `{Device}-RAW-8443` exists (create if charter adds a new approved device — requires operator charter; current fleet is fixed at six).
4. Restart x-ui from panel or SSH: `sudo systemctl restart x-ui`.
5. Distribute link/QR from **panel** (not Git).
6. Optionally refresh local `clients\<Device>\` backup artifacts.
7. **Post-change backup** (§10).

**Rules:**

- One UUID per device; never reuse across devices.
- Revoke by disabling/deleting the specific panel client only.

---

## 7. Disable or revoke one device

1. Backup first (§10).
2. In 3X-UI, locate `{Device}-RAW-8443` on inbound **EQVPS-TLS-RAW-8443**.
3. **Disable** for temporary suspension, or **delete** for full revocation.
4. Restart x-ui.
5. Post-change backup.

Other devices on the same inbound continue independently.

---

## 8. Regenerate one device profile (lost phone / leaked link)

1. Revoke old identity (§7).
2. Create a **new** client with the **same display name** `{Device}-RAW-8443` but a **new UUID** on **EQVPS-TLS-RAW-8443**.
3. Restart x-ui.
4. Distribute new link/QR from **panel**.
5. Backup.

**Exception:** Do not rotate MCA-ONE without explicit operator charter when it is the active test identity.

---

## 9. Why UUIDs must not be shared

- Each UUID is an independent credential on the server.
- Sharing prevents per-device revocation and breaks traffic attribution.
- Each approved device must have its **own** RAW UUID on `:8443`.

---

## 10. Backup before client changes

On the server (as `marsops` with sudo):

```bash
STAMP=$(date -u +%Y%m%dT%H%M%SZ)
BDIR="/root/mars-backups/eqvps-clients-manual-${STAMP}"
sudo mkdir -p "$BDIR"/etc "$BDIR"/x-ui "$BDIR"/meta
sudo cp -a /etc/x-ui "$BDIR/etc/"
sudo cp -a /usr/local/x-ui/bin/config.json "$BDIR/x-ui/"
sudo systemctl status x-ui --no-pager | sudo tee "$BDIR/meta/x-ui-status.txt"
sudo tar -C /root/mars-backups -czf "${BDIR}.tgz" "$(basename "$BDIR")"
sudo sha256sum "${BDIR}.tgz"
```

Copy the `.tgz` to:

`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\`

Known good restore points: `EQVPS-MICRO-IP-ingress-restore-runbook-v1.md`.

Post-RAW pre-cleanup DB snapshot (2026-08-29): `backups\post-raw-pre-client-cleanup-2026-08-29\x-ui.db`

---

## 11. Restore after a bad client change

1. Stop further panel edits.
2. Restore from latest known-good backup (local or server `/etc/x-ui/x-ui.db.pre-cleanup-*` if applicable).
3. Follow `EQVPS-MICRO-IP-ingress-restore-runbook-v1.md`.
4. Re-verify SSH on :22.
5. Re-import from **panel** or restored local artifacts as needed.

---

## 12. Where secrets and evidence live

| Material | Location |
|----------|----------|
| **Daily keys / QR / subscriptions** | **3X-UI panel** |
| VLESS URIs, JSON client configs (backup) | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\clients\` |
| Panel password, web base path, sudo password | `secrets.local.md` |
| Public panel + subscription URLs | `operator-access.local.md` |
| SSH private key | `ssh\marsops_ed25519` |
| Backups | `backups\` |
| Git-safe evidence | `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\` |

**Never** stage client artifacts or secrets into the Git repository.
