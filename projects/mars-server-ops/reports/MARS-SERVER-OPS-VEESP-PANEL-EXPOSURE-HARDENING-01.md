# REPORT — VEESP PANEL EXPOSURE HARDENING 01

**inventory_ref:** MCA-VPN-001  
**Provider:** VEESP  
**IPv4 / domain:** `178.173.250.69` / `wsp-cloud.com`  
**Wave date (UTC):** 2026-08-30  
**Overall:** **PASS WITH RESIDUALS**  
**Commit/push:** **0** (not authorized)

---

## 1. Verdict

Panel-exposure wave completed as **decision + evidence**, not as an architecture rebuild.

| Item | Result |
|------|--------|
| `:2096` dependency | **UNUSED UNPROVEN** — subscription service is **live and functional**, but current device dependence is **not proven** |
| `:2096` public access | **LEFT OPEN** (charter: close only if UNUSED PROVEN) |
| `:5928` panel | **OPTION C** — keep **PUBLIC TLS-DIRECT** as **ACCEPTED RESIDUAL** |
| nginx `:443` migration | **DEFERRED** (complexity not justified; no lockout-safe proxy already present) |
| VPN `:8443` | **UNCHANGED** / regression **PASS** |
| Mutations | **0** (no UFW/x-ui/nginx change) |

Independent admin egress during wave: FriendHosting **`92.42.99.126`**. FriendHosting mutation **0**.

Rollback baseline verified readable:  
`X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-post-system-hardening-20260830T163612Z.tgz`  
Scoped mutation snapshot: **NOT REQUIRED** (no config mutation).

---

## 2. `:5928` ownership / purpose

| Field | Live evidence |
|-------|----------------|
| Process | `x-ui` (3X-UI **3.7.0**) |
| Bind | `*:5928` (`webListen` empty/ABSENT → all interfaces) |
| Purpose | Admin panel HTTPS (TLS-direct) |
| TLS | **YES** — cert CN=`wsp-cloud.com` (same leaf family as VPN) |
| Setting | `webPort=5928`; `webCertFile`/`webKeyFile` PATH_SET; `webBasePath` NON_DEFAULT (len 18; secret not recorded here) |
| Protections already present | TLS; non-default path; rotated strong credentials; `hasDefaultCredential` false (prior wave) |

Localhost-only bind **without** a reverse proxy would lock out remote operator access → **not** applied.

---

## 3. `:2096` ownership / purpose

| Field | Live evidence |
|-------|----------------|
| Process | `x-ui` |
| Bind | `*:2096` |
| Purpose | 3X-UI **subscription** HTTPS server (`Sub server running HTTPS on [::]:2096`) |
| TLS | **YES** (`subCertFile`/`subKeyFile` PATH_SET) |
| DB keys | `subEnable` / `subPort` / `subPath` **ABSENT** in settings table |
| Effective defaults (from binary UI defaults) | `subEnable` default **true** (`!0`); `subPort` default **2096** |
| Functional probe | Valid enabled client `subId` via `/sub/<id>` → **HTTP 200** (body size observed; content not stored) |
| Root `/` and wrong paths | **404** |

---

## 4. `:2096` dependency verdict

**Classification: UNUSED UNPROVEN**

Evidence for “not currently depended on”:

- No successful `/sub` access lines in `/var/log/x-ui/3xui.log` (zero `/sub` string hits; mostly startup + scanner TLS handshake noise in journal).
- Inbound JSON blobs do not embed `:2096` or subscription URLs.
- Accepted VEESP workload path is **direct VLESS** on `:8443` (prior waves + this regression).

Evidence against “UNUSED PROVEN”:

- Subscription endpoint **works** (HTTP 200 for valid `subId`).
- All **9** clients have `subId` populated (7 enable=true) — tokens exist even if unused.
- Incomplete client-side inventory: cannot prove no phone/desktop uses subscription refresh.

**Action per charter:** leave public UFW allow for `:2096`; do **not** close.

---

## 5. Panel-hardening decision

Evaluated in required order:

| Option | Assessment | Decision |
|--------|------------|----------|
| **A — UFW source restrict** | Admin egress today `92.42.99.126` (FriendHosting). Not proven stable as a permanent allowlist; charter warns against permanent FriendHosting-IP lock. Lockout risk if egress changes. | **SKIP** |
| **B — nginx `:443` → localhost panel** | Host has **no local `:443` listener** (`Connection refused` on-box). nginx **ABSENT**. Would require install + cert reuse + bind change + UFW edits. Disproportionate vs current TLS-direct + secret path + rotated creds. | **DEFER** |
| **C — keep TLS-direct** | Already TLS; non-default path; strong rotated credentials; UFW explicit allow only. | **SELECTED — ACCEPTED RESIDUAL** |

`:443` note: host listener **UNUSED**. External TCP connect from admin workstation may still appear to succeed without a TLS service (path/middlebox **UNKNOWN**) — re-verify before any future nginx wave.

---

## 6. Mutations

| Surface | Change |
|---------|--------|
| UFW | **0** |
| `/etc/x-ui/` | **0** |
| 3X-UI / Xray versions | **0** |
| VLESS clients / UUIDs | **0** |
| nginx | **not installed** |
| SSH / fail2ban / swap / sysctl | **0** (out of scope) |
| FriendHosting / EQVPS | **0** |
| Reboot | **0** |

---

## 7. Final public-port state

| Port | Classification |
|------|----------------|
| **22** | **PUBLIC REQUIRED** (SSH key-only) |
| **8443** | **PUBLIC REQUIRED** (VLESS + TLS + RAW) |
| **46489** | **PUBLIC REQUIRED** (live Reality inbound; not mutated this wave) |
| **5928** | **UNKNOWN/RESIDUAL** → treated as **ACCEPTED RESIDUAL** (PUBLIC TLS-direct panel) |
| **2096** | **UNKNOWN/RESIDUAL** (PUBLIC subscription; UNUSED UNPROVEN) |
| **8445** | **PUBLIC REQUIRED** for current MTProto docker-proxy publish (unchanged; Docker/UFW caveat remains) |
| **443** | **CLOSED** on host (no listener); external path anomaly **UNKNOWN** — **not** nginx panel |

---

## 8. VPN regression

| Check | Result |
|-------|--------|
| x-ui | **active** / **3.7.0** |
| Xray | **26.7.28** |
| TCP `:8443` | **PASS** (listen + external) |
| TLS `:8443` | **PASS** (CN=`wsp-cloud.com`) |
| Inbounds | **2** UNCHANGED |
| Clients | **9** UNCHANGED |
| Client mutation | **0** |
| VPN architecture mutation | **0** |

---

## 9. Residual risks

1. **Panel `:5928` public** — mitigated by TLS + secret path + rotated creds; still internet-reachable admin surface.  
2. **Subscription `:2096` public** — functional `/sub/<subId>` if token known; scanners generate handshake noise.  
3. **Docker `:8445` / UFW interaction** — unchanged caveat from system-hardening wave.  
4. **Reboot-required** flag may still be present from prior apt state — **not** cleared here.  
5. Future nginx-on-`:443` must re-check external `:443` path behavior before install.

---

## 10. Next step

**Recommended:** **FRESH FULL VEESP OPERATIONAL BACKUP** (freeze post–system-hardening + this decision state), then operator real-workload smoke on existing VEESP VLESS profile if still pending.

Optional later charter (only if operator wants): nginx `:443` → localhost panel **or** explicit disable/`subEnable=false` + UFW close for `:2096` after operator confirms no subscription clients.

---

## Confirmations

| Item | Value |
|------|-------|
| FriendHosting mutation | **0** |
| VEESP VPN mutation | **0** |
| VEESP client mutation | **0** |
| reboot | **0** |
| Secret disclosure in this report | **0** (path/UUIDs/URIs omitted) |
| Foreign WIP mutation | **0** |
| commit/push | **0** |

---

*Panel exposure hardening 01 · MCA-VPN-001 · 2026-08-30 · no secrets.*
