# REPORT — MARS Server Ops FriendHosting Intake 01 — Direct TCP/443 Gate

**Programme:** MARS Server Ops  
**Wave:** FRIENDHOSTING INTAKE 01 — Cleanup + DNS Gate After Direct TCP/443 PASS  
**Date (UTC):** 2026-08-29 / closeout into 2026-08-30 local  
**Mode:** Intake closeout only — **no** Xray / 3X-UI / VPN / nginx / certbot install  
**Git:** no commit / no push  

---

## 1. Executive verdict

**FRIENDHOSTING INTAKE 01 = PASS (CLOSED CLEAN).**

| Gate | Result |
|------|--------|
| Direct Goodline ping | **PASS** |
| Direct SSH :3333 | **PASS** |
| Direct TCP/443 with known listener | **PASS** (25/25) |
| Temporary :443 listener cleanup | **PASS** |
| :443 free after cleanup | **YES** |
| DNS `metacode-cloud.com` → `92.42.99.126` | **PASS** |
| Node ready for VPN build | **YES** |
| VPN / panel install this wave | **NOT EXECUTED** (STOP) |

Primary principle satisfied: direct network gate closed cleanly, DNS confirmed, clean pre-VPN baseline captured.

---

## 2. Node identity

| Field | Value |
|-------|-------|
| Provider | FriendHosting |
| Region | Germany |
| Hostname | `imart216311` |
| Public IPv4 | `92.42.99.126` |
| SSH port | `3333` |
| OS | Ubuntu 24.04.4 LTS |
| Kernel | `6.8.0-138-generic` (x86_64) |
| Primary NIC | `eth0` |
| MTU | `1500` |
| Booted (approx) | 2026-08-29 14:07:19 UTC |

---

## 3. Direct Goodline preflight

Operator facts (recorded exactly; TUN OFF, System Proxy OFF):

| Item | Value |
|------|-------|
| Operator public IP during preflight | `46.181.159.198` |
| Target | `92.42.99.126` |
| Ping | **20/20 PASS**, 0% loss, ~89–90 ms |
| SSH TCP/3333 | **20/20 PASS** |

**Verdict:** Direct Goodline reachability to FriendHosting **PASS**.

---

## 4. SSH intake

| Item | Result |
|------|--------|
| Endpoint | `92.42.99.126:3333` |
| User | `root` (password via local-only `secrets.local.md`; not disclosed) |
| Connect | **PASS** (intake start + cleanup reconnect) |
| SSH config mutation | **0** |
| Persistent auth change | **0** |

---

## 5. Initial :443 state

At temporary-listener start (intake evidence):

- `:443` was **free** before listener start.
- No conflicting production service on `:443`.
- Firewall: ufw **absent**, firewalld **inactive**, iptables **ACCEPT/empty**, nft **empty**.
- **No** temporary firewall rule created for Intake 01.

---

## 6. Temporary listener validation

| Item | Result |
|------|--------|
| Mechanism | Temporary `python3` TCP listener on `0.0.0.0:443` |
| Script path | `/tmp/mars-intake01-443-listener.py` |
| Observed PID | `1119` (re-verified before kill) |
| Server-local `:443` test | **PASS** (`MARS-INTAKE-01-TCP443-OK`) |
| Persistence | **none** (process + `/tmp` files only) |

---

## 7. Operator 25× TCP/443 result

Operator direct Goodline test against `92.42.99.126:443` with known listener present:

| Metric | Value |
|--------|-------|
| Result | **25/25 PASS** |
| Typical connect time | ~85–100 ms |
| One outlier | ~1083 ms |
| Interpretation of outlier | **Not** treated as instability by itself |

**Historical correction:** Earlier `0/25` timeouts **before** any listener existed are classified as **NON-DIAGNOSTIC / SUPERSEDED AS PORT-PATH EVIDENCE**. Valid port-path evidence is the later known-listener + 25/25 PASS set.

---

## 8. Direct TCP/443 gate verdict

**FRIENDHOSTING DIRECT TCP/443 GATE = PASS**

Conditions met:

- known listener present;
- server-local `:443` PASS;
- operator direct Goodline 25/25 PASS;
- TUN OFF;
- System Proxy OFF.

---

## 9. Cleanup

### 9.1 Listener stop

| Step | Result |
|------|--------|
| Re-verify owner of `:443` | `python3` PID **1119** → `/tmp/mars-intake01-443-listener.py` |
| Blind kill avoided | Yes — ownership confirmed first |
| Stop method | `pkill -f '/tmp/mars-intake01-443-listener.py'` (exact Intake-01 marker only) |
| Unrelated services killed | **0** |

### 9.2 Temp files removed (exact paths only)

| Path | Action |
|------|--------|
| `/tmp/mars-intake01-443-listener.py` | deleted |
| `/tmp/mars-intake01-443.log` | deleted |
| `/tmp/mars-intake01-443-nohup.out` | deleted |

No wildcard `/tmp` cleanup. No broad destructive ops.

### 9.3 Firewall rollback

**NOT REQUIRED**

Re-verified after cleanup:

- ufw: **absent**
- firewalld: **inactive**
- iptables: ACCEPT / empty chains
- nft: empty
- Intake-01 temporary rule: **never created**

### 9.4 Cleanup verdict

**PASS** — temporary listener gone; `:443` free; SSH `:3333` still listening; no firewall residue from Intake 01.

---

## 10. Post-cleanup server baseline

| Check | Result |
|-------|--------|
| Hostname | `imart216311` |
| OS | Ubuntu 24.04.4 LTS |
| Uptime (at cleanup) | ~3h 25m (since 2026-08-29 14:07:19) |
| Listeners | `sshd` on `:3333` (IPv4+IPv6); systemd-resolved on localhost DNS only |
| SSH `:3333` | **PASS / listening** |
| `:443` | **FREE** |
| eth0 MTU | **1500** |
| Public IPv4 | `92.42.99.126` |
| Firewall state | open default ACCEPT; no host firewall engine active |

This is the **clean pre-VPN baseline**.

---

## 11. DNS gate

Read-only queries from Windows workstation:

| Resolver | `metacode-cloud.com` A |
|----------|-------------------------|
| System resolver | `92.42.99.126` |
| Cloudflare `1.1.1.1` | `92.42.99.126` |
| Google `8.8.8.8` | `92.42.99.126` |

- DNS mutation this task: **0** (operator already changed A-record).
- Stale alternate A visible in these checks: **NONE**.

**DNS gate classification: PASS**

---

## 12. metacode-cloud.com current mapping

| Domain | Type | Target |
|--------|------|--------|
| `metacode-cloud.com` | A | `92.42.99.126` (FriendHosting Germany) |

Mapping matches the live FriendHosting node used for Intake 01.

---

## 13. Control-node readiness

| # | Question | Answer |
|---|----------|--------|
| A | Direct Goodline ping gate | **PASS** |
| B | Direct SSH `:3333` gate | **PASS** |
| C | Direct TCP/443 with known listener | **PASS** |
| D | Temporary listener cleanup | **PASS** |
| E | `:443` free again | **YES** |
| F | DNS `metacode-cloud.com` → `92.42.99.126` | **PASS** |
| G | Node ready for VPN build | **YES** |

**Recommended next wave (NOT executed):**  
`FRIENDHOSTING CONTROL NODE BUILD 01`

Initial architecture recommendation:

- Ubuntu 24.04
- 3X-UI
- Xray
- VLESS
- TLS
- RAW/TCP
- `metacode-cloud.com`
- primary control port **8443**

Goal: near-equivalent clean control against EQVPS while retaining the same Windows / v2rayN / TUN client environment.  
Do **not** default to Reality / WS / XHTTP on FriendHosting unless later requested.

---

## 14. Evidence paths

| Path | Role |
|------|------|
| `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\` | Local contour (identity + secrets ref + runners) |
| `...\intake-01-direct-443-gate\session-summary.json` | Listener start summary |
| `...\intake-01-direct-443-gate\listener-start.txt` | Listener start evidence |
| `...\intake-01-direct-443-gate\local-443-test.txt` | Server-local `:443` PASS |
| `...\intake-01-direct-443-gate\cleanup-summary.json` | Cleanup verdict + baseline |
| `...\intake-01-direct-443-gate\cleanup-ss-before.txt` / `cleanup-ss-after.txt` | Listener presence → free |
| `...\intake-01-direct-443-gate\cleanup-443-owners.txt` | Ownership before kill |
| `...\intake-01-direct-443-gate\dns-gate.txt` | DNS PASS evidence |
| `...\node-identity.local.md` | Safe readiness / identity (no secrets) |
| `X:\AI MARS\projects\mars-server-ops\reports\MARS-SERVER-OPS-FRIENDHOSTING-INTAKE-01-DIRECT-443-GATE.md` | This REPORT |

Secrets remain only in local-only `secrets.local.md` — **not** copied into this REPORT.

---

## 15. Git/server mutation closeout

| Scope | Mutation |
|-------|----------|
| VEESP | **0** |
| EQVPS | **0** |
| FriendHosting persistent test mutation | **0** (temp listener + `/tmp` files removed) |
| FriendHosting SSH config | **0** |
| FriendHosting firewall rules | **0** (none created; rollback not required) |
| Xray / 3X-UI / VPN packages | **0** |
| Secret disclosure in REPORT / chat | **0** |
| Commit | **0** |
| Push | **0** |

**STOP.** Ready for a separately chartered **FRIENDHOSTING CONTROL NODE BUILD 01**.
