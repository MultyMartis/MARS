# EQVPS-MICRO-IP — Ingress Restore Runbook v1

**Asset:** EQVPS Micro-IP (`metacode-cloud` / `95.216.126.173`)  
**Scope:** Restore 3X-UI / Xray ingress configuration after failure or intentional rollback  
**Companion evidence:** `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-ingress-deployment-2026-08-27.md`  
**Current baseline (2026-08-28):** `EQVPS-MICRO-IP-current-ingress-baseline-2026-08-28.md`  
**Goodline stabilization wave:** `EQVPS-MICRO-IP-goodline-ingress-stabilization-2026-08-28.md`  
**Local secrets:** `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\secrets.local.md` (not Git)

**Hard constraints:** Preserve SSH on TCP/22 and `marsops` key access. Do **not** mutate Server A.  
**Management plane (since 2026-08-28):** Public HTTPS panel `:20901` and subscription `:2096` are **approved production state** — see `EQVPS-MICRO-IP-public-panel-subscription-2026-08-28.md`.

---

## 1. Backup inventory

| Backup | Remote path |
|--------|-------------|
| Pre-install (OS/ssh/ufw/fail2ban baseline) | `/root/mars-backups/eqvps-ingress-preinstall-20260827T172605Z/` (+ `.tgz`) |
| Post-install (full ingress) | `/root/mars-backups/eqvps-ingress-postinstall-20260827T175740Z/` (+ `.tgz`) |
| Post-install SHA256 | `02f66631dfc3055f2ba6b57a5538cd3454baa943a8826b860d65415e079b80ab` |
| Local copy of post-install tgz | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-ingress-postinstall-20260827T175740Z.tgz` |
| Goodline pre-change (Reality still on :443) | `/root/mars-backups/eqvps-ingress-goodline-prechange-20260828T091121Z.tgz` |
| Goodline pre-change SHA256 | `c6a95274f28251941c2c806b5f5e29c1104f19d6cff0725e299b781a9f2ad9ae` |
| Local pre-change tgz | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-ingress-goodline-prechange-20260828T091121Z.tgz` |
| **Current production (XHTTP :443 primary)** | `/root/mars-backups/eqvps-ingress-goodline-post-xhttp443-20260828T091206Z.tgz` |
| **Current production SHA256** | `95adc3085b37cc59fd22fb1ac47deb7d968690ca9745fa0cff6d4b14e6e418c0` |
| Local current-production tgz | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-ingress-goodline-post-xhttp443-20260828T091206Z.tgz` |
| **Pre client provisioning (2026-08-28)** | `/root/mars-backups/eqvps-clients-pre-provision-20260828T102318Z.tgz` |
| Pre client provisioning SHA256 | `4d341d6b748811634e18e035a68fa77f4a9d6af230ab49f34e0f3d488a7ba7be` |
| Local pre client provisioning tgz | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-clients-pre-provision-20260828T102318Z.tgz` |
| **Post client provisioning (2026-08-28)** | `/root/mars-backups/eqvps-clients-post-provision-20260828T102402Z.tgz` |
| Post client provisioning SHA256 | `76e0f144e08dcd5e24774003e286eef5706f65a868cb45f5d777cbd15b706949` |
| Local post client provisioning tgz | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-clients-post-provision-20260828T102402Z.tgz` |
| **Pre public panel/sub (2026-08-28)** | `/root/mars-backups/eqvps-public-access-pre-public-access-20260828T104233Z.tgz` |
| Pre public panel/sub SHA256 | `cd7219cf63b477ddac0579c89defbc526fc8ea0175c71f15b6ecbfa1a1d1f0aa` |
| Local pre public panel/sub tgz | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-public-access-pre-public-access-20260828T104233Z.tgz` |
| **Post public panel/sub (2026-08-28)** | `/root/mars-backups/eqvps-public-access-post-public-access-20260828T104807Z.tgz` |
| **Post public panel/sub SHA256 (recommended default since public-access wave)** | `f2a965ab1901f4edb3c16710ec1a5fcca381a7a65e542e0c130dc49bb5f99400` |
| Local post public panel/sub tgz | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-public-access-post-public-access-20260828T104807Z.tgz` |

Post-install archive typically contains:

- `/etc/x-ui/` including `x-ui.db`
- `/usr/local/x-ui/bin/config.json` (copy under `x-ui/`)
- systemd unit metadata
- `/etc/ssh/sshd_config` + `sshd_config.d/`
- `/etc/ufw/`, `/etc/fail2ban/`
- `certs-meta/` — LE fullchain + privkey copies + leaf metadata
- `meta/` — ufw status, `ss` snapshot, versions

---

## 2. Preconditions

1. Operator can SSH as `marsops` to `95.216.126.173:22` with the dedicated Ed25519 key.  
2. Password sudo for `marsops` still works (local secrets).  
3. Choose restore target:
   - **post public panel/sub** (`…public-access-post-public-access-20260828T104807Z`) — ingress + 12 production clients + **public HTTPS panel/sub** (recommended default since 2026-08-28 public-access wave)
   - **pre public panel/sub** (`…public-access-pre-public-access-20260828T104233Z`) — immediately before public panel/sub publication (localhost management plane)
   - **post client provisioning** (`…clients-post-provision-20260828T102402Z`) — ingress + 12 production device clients (localhost panel/sub)
   - **pre client provisioning** (`…clients-pre-provision-20260828T102318Z`) — ingress only, before production device clients
   - **current production ingress** (`…post-xhttp443-20260828T091206Z`) — VLESS + TLS + XHTTP on :443 and :8443 (technical clients only)
   - **post-install** (2026-08-27 Reality era on :443)
   - **goodline pre-change** (Reality on :443 immediately before cutover)
   - **pre-install** (remove application stack state toward baseline)
4. Confirm disk space: `df -h /`.

---

## 3. Safe withdraw (ingress off, SSH kept)

Use when public ingress must stop immediately without full restore:

```bash
sudo ufw delete allow 443/tcp || true
sudo ufw delete allow 8443/tcp || true
sudo ufw status verbose
sudo systemctl stop x-ui
sudo systemctl status x-ui --no-pager
sudo ss -lntp | awk 'NR==1 || /:22|:443|:8443|:20901/'
```

Expected: only SSH public; no :443/:8443; panel not required to run.

Re-add rules only after listeners are healthy again (see section 6).

---

## 4. Restore ingress configuration

### 4.1 Extract

**Current production (default since 2026-08-28):**

```bash
STAMP=20260828T091206Z
ARCH=eqvps-ingress-goodline-post-xhttp443-${STAMP}.tgz
cd /root/mars-backups
sudo tar -tzf ${ARCH} | head
sudo tar -xzf ${ARCH}
B=/root/mars-backups/eqvps-ingress-goodline-post-xhttp443-${STAMP}
```

**Legacy post-install (Reality on :443, 2026-08-27):**

```bash
STAMP=20260827T175740Z
ARCH=eqvps-ingress-postinstall-${STAMP}.tgz
cd /root/mars-backups
sudo tar -tzf ${ARCH} | head
sudo tar -xzf ${ARCH}
B=/root/mars-backups/eqvps-ingress-postinstall-${STAMP}
```

### 4.2 Stop service

```bash
sudo systemctl stop x-ui
# ensure no stray xray child
sudo pkill -f xray-linux-amd64 || true
```

### 4.3 Restore 3X-UI DB / config

```bash
sudo cp -a /etc/x-ui /etc/x-ui.bak.$(date -u +%Y%m%dT%H%M%SZ) || true
sudo cp -a ${B}/etc/x-ui/. /etc/x-ui/
sudo cp -a ${B}/x-ui/config.json /usr/local/x-ui/bin/config.json
```

### 4.4 Restore certificates (if needed)

Prefer live Let’s Encrypt tree if still valid:

```bash
sudo ls -la /etc/letsencrypt/live/metacode-cloud.com/
```

If missing/corrupt, restore from backup copies then point/renew carefully:

```bash
sudo mkdir -p /etc/letsencrypt/live/metacode-cloud.com
sudo cp -a ${B}/certs-meta/fullchain.pem /etc/letsencrypt/live/metacode-cloud.com/fullchain.pem
sudo cp -a ${B}/certs-meta/privkey.pem /etc/letsencrypt/live/metacode-cloud.com/privkey.pem
sudo chmod 600 /etc/letsencrypt/live/metacode-cloud.com/privkey.pem
```

If ACME renewal is required later: time-box UFW `80/tcp`, run certbot, **delete** the 80 rule immediately. Do **not** leave port 80 permanently open.

### 4.5 Optional: restore UFW/fail2ban trees

Only if those files were damaged (SSH risk — review diffs first):

```bash
sudo diff -ru /etc/ufw ${B}/etc/ufw | less
# apply selectively after review — do not blindly overwrite without confirming 22/tcp allow remains
```

---

## 5. Start and validate

```bash
sudo systemctl start x-ui
sudo systemctl is-active x-ui
sudo journalctl -u x-ui -n 80 --no-pager
sudo ss -lntp | awk 'NR==1 || /:22|:443|:8443|:20901|:2096|:80 /'
```

Expected (**post public-access** production baseline):

- `*:20901` — 3X-UI HTTPS panel (x-ui)  
- `*:2096` — 3X-UI HTTPS subscription (x-ui)  
- `*:443` — VLESS + TLS + XHTTP (primary)  
- `*:8443` — VLESS + TLS + XHTTP (fallback)  
- **no** public `:80` listener  

Older backups (pre public-access wave) will show `127.0.0.1:20901` / `127.0.0.1:2096` instead. Legacy post-install restore shows `*:443` as REALITY.

Panel check (from workstation):

- **Normal:** HTTPS to `metacode-cloud.com:20901` with secret web base path — exact URL in local `operator-access.local.md`.  
- **Emergency:** SSH tunnel to localhost as documented in `EQVPS-MICRO-IP-operator-client-runbook-v1.md` §1.

---

## 6. Re-open UFW only after listeners exist

```bash
sudo ss -lntp | grep -E ':443\\b' && sudo ufw allow 443/tcp comment 'MARS XRAY XHTTP PRIMARY'
sudo ss -lntp | grep -E ':8443\\b' && sudo ufw allow 8443/tcp comment 'MARS XRAY TLS FALLBACK'
sudo ss -lntp | grep -E ':20901\\b' && sudo ufw allow 20901/tcp comment 'MARS 3XUI PANEL HTTPS'
sudo ss -lntp | grep -E ':2096\\b' && sudo ufw allow 2096/tcp comment 'MARS 3XUI SUBSCRIPTION HTTPS'
sudo ufw status verbose
```

If restoring legacy Reality-era post-install backup, use comment `MARS XRAY REALITY PRIMARY` on :443 only when that inbound is intentionally reinstated.

If restoring **pre public-access** backup, omit 20901/2096 allows (management plane was localhost-only).

Final public allows for **post public-access** baseline: **22, 443, 8443, 20901, 2096**.

---

## 7. Application-level smoke

1. TCP: `Test-NetConnection 95.216.126.173 -Port 443` and `-Port 8443`.  
2. Primary client (TLS+XHTTP :443) — expect egress `95.216.126.173`, DNS and HTTPS browsing PASS on operator Goodline path.  
3. Fallback client (TLS+XHTTP :8443) — same egress and application checks.  
4. If restored to **post public-access** baseline: confirm `*:20901` and `*:2096` listeners and UFW allows; validate panel/subscription HTTPS from workstation. Subscription output must not contain `@localhost` in VLESS URIs.  
5. If restored to **pre public-access** baseline: panel/subscription remain localhost-only (`127.0.0.1`).

Do not declare ingress PASS from TCP alone. Reality-era restores require separate Goodline client validation if Reality is reinstated.

Client parameters live only in `secrets.local.md` / operator client profiles under the local raw evidence directory.

---

## 8. Restore toward pre-install baseline (application removal)

Use only with explicit operator approval if ingress must be fully removed:

1. Section 3 withdraw (UFW + stop x-ui).  
2. Disable/remove x-ui unit per upstream uninstall guidance if chartered.  
3. Restore ssh/ufw/fail2ban from **pre-install** tarball if those were altered.  
4. Leave LE certs or remove only if separately chartered (certs are not in Git).

---

## 9. Rollback testability status

| Item | Status |
|------|--------|
| Backups exist on server | **YES** |
| Local tgz copy | **YES** |
| Restore steps documented | **YES** (this runbook) |
| Destructive restore drill executed | **NO** (deployment left intact by charter) |

---

## 10. Contacts / authority

- Operator SSH identity: dedicated `marsops` key under local EQVPS contour  
- Connectivity fallback: Server A (do not mutate from this runbook)  
- Public panel/subscription on :20901/:2096 are **chartered** (2026-08-28). Permanent :80 allow still requires a separate MARS charter.
