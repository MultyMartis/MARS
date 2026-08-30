# REPORT — FriendHosting 3X-UI nginx public access (TLS reverse proxy)

**Date (UTC):** 2026-08-30T06:14Z  
**Wave:** FRIENDHOSTING-3XUI-NGINX-PUBLIC-ACCESS  
**Target:** FriendHosting Germany `92.42.99.126` / `metacode-cloud.com`  
**Verdict:** **PASS**

---

## 1. Executive verdict

Public panel access is live as:

`https://metacode-cloud.com/[SECRET PANEL PATH — LOCAL ONLY]`

Architecture:

**PUBLIC HTTPS `:443` (nginx + existing Let’s Encrypt cert) → `http://127.0.0.1:20901` (3X-UI localhost-only).**

Panel port is **not** published as the public control plane. SSH `:3333` and VPN `:8443` were not mutated and remain healthy. VEESP / EQVPS mutation = **0**. Secret path / passwords / UUID / private key not written into this report.

---

## 2. Pre-state

| Check | Result |
|-------|--------|
| nginx | **ABSENT** (installed this wave) |
| TCP `:443` | **FREE** before install |
| 3X-UI listen | `127.0.0.1:20901` only |
| Panel protocol (probed, not guessed) | **HTTP** |
| VPN `:8443` | listening (Xray) |
| SSH `:3333` | listening (sshd) |
| TLS cert paths | `/etc/letsencrypt/live/metacode-cloud.com/fullchain.pem` + `privkey.pem` |
| `openssl verify` | **OK** (`fullchain.pem: OK`) |
| UFW | **active**; allow `3333/tcp`, `8443/tcp` (pre); `443/tcp` added this wave |
| Secret web path | present in local-only `secrets.local.md` (hash16 `a065fd3481c653b1`) |

Evidence: `projects/mars-server-ops/evidence/FRIENDHOSTING-3XUI-NGINX-PUBLIC/20260830T061431Z_precheck.json`  
Local full contour: `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\nginx-public-access-20260830T061431Z\`

---

## 3. Checkpoint / rollback

**Classification: BACKUP + RESTORE STRATEGY CONFIRMED**

| Item | Value |
|------|-------|
| Remote checkpoint | `/root/mars-backups/friendhosting-nginx-3xui-20260830T061431Z` |
| Local tarball | `...\FRIENDHOSTING-GERMANY\nginx-public-access-20260830T061431Z\remote-checkpoint.tgz` |
| SHA256 | `c0bf2c5b1a7a82e44047b59f56e081047b10b6afea9fa465c1455ac5457824d9` |
| Rollback procedure | `...\nginx-public-access-20260830T061431Z\rollback-procedure.md` |

Rollback (exact):

1. Remove only site `metacode-cloud-3xui` (`sites-enabled` + `sites-available`).
2. If nginx was installed only for this task: `systemctl disable --now nginx` (package remove only with separate operator approval).
3. Restore firewall: delete `443/tcp` allow if rolling back this wave; keep `3333` / `8443`.
4. Confirm `127.0.0.1:20901` unchanged.
5. Confirm `:443` free after nginx stop.
6. Confirm VPN `:8443` and SSH `:3333` healthy.

Checkpoint contents: dpkg nginx state, UFW status, listeners, service status, pre-nginx `/etc/nginx` absence note, cert path refs (no private key material), panel bind snapshot.

---

## 4. nginx installation

| Item | Value |
|------|-------|
| Installed this wave | **YES** (Ubuntu repo) |
| Version | **nginx/1.24.0 (Ubuntu)** |
| Docker | **not** installed |
| Default site | disabled (`sites-enabled/default` removed) |
| WebSocket map | `/etc/nginx/conf.d/mars-websocket-upgrade.conf` |

---

## 5. TLS configuration

| Item | Value |
|------|-------|
| Listen | `443 ssl` (+ IPv6) |
| `server_name` | `metacode-cloud.com` |
| Certificate | existing Let’s Encrypt fullchain (not re-issued) |
| Private key | path only — contents **not** exposed |
| Protocols | TLSv1.2 / TLSv1.3 |
| External TLS | subject/SAN = `metacode-cloud.com`; handshake **OK** from workstation |

---

## 6. Reverse-proxy architecture

```text
Client
  → https://metacode-cloud.com:443  (nginx, SNI metacode-cloud.com)
      → location [SECRET PANEL PATH — LOCAL ONLY]
          → proxy_pass http://127.0.0.1:20901
      → location /  → 404
```

Proxy headers / behaviour:

- `Host`, `X-Real-IP`, `X-Forwarded-For`, `X-Forwarded-Proto`
- WebSocket `Upgrade` / `Connection` via map
- Long timeouts (`3600s` read/send) for panel operations
- `proxy_buffering off`; `proxy_redirect off`

Upstream protocol chosen after live probe: **HTTP** to localhost panel (HTTPS probe not selected).

Site file (server only): `/etc/nginx/sites-available/metacode-cloud-3xui` → enabled symlink.

---

## 7. Panel localhost-only verification

| Check | Result |
|-------|--------|
| `ss` bind | `127.0.0.1:20901` (`x-ui`) |
| `0.0.0.0:20901` / `*:20901` | **not** present |
| Panel bind changed to public | **NO** |
| UFW allow `20901` | **NO** |
| Public application exposure of panel port | **NO** |

Note on workstation TCP to `:20901`: TCP connect may appear to complete on the path (provider/middlebox blackhole behaviour), but **no HTTP response** is returned (`curl` times out with 0 bytes). Combined with localhost bind + UFW deny, panel is **not** publicly served on `:20901`.

---

## 8. Public `:443` validation

| Check | Local (SNI→127.0.0.1) | Workstation external |
|-------|------------------------|----------------------|
| `nginx -t` | **PASS** | — |
| `systemctl is-active nginx` | **active** | — |
| Secret path HTTPS | **200** (login page markers: login/sign) | **200** |
| TLS SAN/CN | `metacode-cloud.com` | `metacode-cloud.com` |
| Listeners | `:443` nginx; `:8443` Xray; `127.0.0.1:20901` x-ui; `:3333` sshd | `:443` OPEN |

Operator URL instruction (no secret printed here):

> Open the same secret panel path from `secrets.local.md`, via `https://metacode-cloud.com/` **without** `:20901`.

---

## 9. Root-path behaviour

| URL | Result |
|-----|--------|
| `https://metacode-cloud.com/` | **404** (intentional; panel not on `/`) |
| Non-secret paths | **404** via default `location /` |

Panel is **not** exposed on the site root.

---

## 10. VPN `:8443` regression check

| Check | Result |
|-------|--------|
| Listener after nginx deploy | **present** (`xray-linux-amd6`) |
| UFW `8443/tcp` | still **ALLOW** |
| Transport / UUID / VLESS config | **not mutated** |
| Regression | **PASS** |

---

## 11. SSH `:3333` regression check

| Check | Result |
|-------|--------|
| Listener | **present** (sshd) |
| UFW `3333/tcp` | still **ALLOW** |
| Port / auth model | **unchanged** |
| Regression | **PASS** |

---

## 12. Security boundary

| Boundary | Status |
|----------|--------|
| Public control plane | HTTPS `:443` only (secret path) |
| Panel process bind | `127.0.0.1:20901` |
| Public `:20901` application exposure | **NO** |
| UFW | `3333`, `443`, `8443` only (no `20901`) |
| VEESP / EQVPS | untouched |
| Secret disclosure in Git report | **0** |
| Default nginx welcome surface | not used as intended public UI |

---

## 13. Evidence paths

| Kind | Path |
|------|------|
| Safe Git-adjacent evidence | `X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-3XUI-NGINX-PUBLIC\` |
| Summary JSON | `...\20260830T061431Z_summary-safe.json` |
| Local-only full evidence | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\nginx-public-access-20260830T061431Z\` |
| Local orchestrator | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\run-nginx-3xui-public-access.py` |
| Secrets (unchanged) | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\secrets.local.md` |

---

## 14. Git / server mutation closeout

| Item | Value |
|------|-------|
| FriendHosting mutations | nginx install + site + UFW `443/tcp` allow |
| 3X-UI listen / secret path / VPN / SSH | **unchanged** |
| VEESP mutation | **0** |
| EQVPS mutation | **0** |
| Git commit | **0** |
| Git push | **0** |
| Foreign WIP | **out of scope** (not staged) |

**This report file** is the only intended new programme artifact under `projects/mars-server-ops/reports/` for this wave (plus redacted evidence under `evidence/FRIENDHOSTING-3XUI-NGINX-PUBLIC/`).
