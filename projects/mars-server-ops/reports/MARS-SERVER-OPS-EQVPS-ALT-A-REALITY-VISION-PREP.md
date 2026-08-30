# MARS-SERVER-OPS — EQVPS ALT-A REALITY+VISION — PREPARATION REPORT

**Test ID:** `EQ-ALT-A-REALITY-VISION`  
**Wave:** EQVPS TRANSPORT ALTERNATIVES WAVE 01 — Stage A only  
**Node:** EQVPS Micro-IP / Helsinki `95.216.126.173` / `metacode-cloud.com`  
**Date (UTC context):** 2026-08-29  
**Status:** PREPARATION COMPLETE — waiting for operator offline acceptance  
**Classification of this document:** safe (no secrets)

---

## 1. Executive preparation verdict

Stage A server preparation is **READY FOR OPERATOR OFFLINE ACCEPTANCE**.

- Isolated **VLESS + REALITY + TCP/RAW + XTLS Vision** inbound is live on **`:9443`**.
- Existing EQVPS control **RAW/TLS `:8443` is preserved and healthy** (TLS subject `CN=metacode-cloud.com`).
- Pre-wave backup is classified **BACKUP + RESTORE STRATEGY CONFIRMED**.
- Client profile material exists local-only as **[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]**.
- Offline harness DryValidate **PASS**.

**Not yet decided:** real-app PASS/FAIL (Cursor / ChatGPT / YouTube). Transport-only success is insufficient.

**Workstation note:** isolated Xray probe from the operator workstation to `:9443` timed out; server loopback/hairpin Reality transport **PASS**. Operator must still run acceptance under v2rayN TUN (EXP-A01b model).

---

## 2. Preflight

| Check | Result |
|--------|--------|
| Workspace | `X:\AI MARS` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Foreign WIP | Present elsewhere in tree — **out of scope** |
| Staged changes for this wave | Empty (no commit authorized) |
| VEESP mutation | **0** |
| EQVPS `:8443` mutation | **0** |
| Commit/push | **0** |

**Pre-Stage-A answers:**

| Q | Answer |
|---|--------|
| A. Is `:443` free? | **No** — occupied (XHTTP). Not used for Stage A. |
| B. Xray supports REALITY+Vision? | **Yes** (server Xray family compatible with Reality+Vision; Vision via `flow_override` path). |
| C. Client supports profile? | **Yes** — v2rayN/Xray client contour aligned with programme evidence. |
| D. Conflict services? | `:443` XHTTP; `:8443` control; `:24443` prior test; panel ports unchanged. |
| E. `:8443` untouched? | **Yes** — still listening; TLS subject unchanged. |
| F. Rollback ready? | **Yes** — see §3. |

---

## 3. Backup / rollback anchor

**Classification:** `BACKUP + RESTORE STRATEGY CONFIRMED`

| Item | Absolute path / value |
|------|------------------------|
| Backup name | `eqvps-pre-alt-a-reality-vision-20260829T113219Z` |
| Local tarball | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\eqvps-alt-a-reality-vision-2026-08-29\backups\eqvps-pre-alt-a-reality-vision-20260829T113219Z.tgz` |
| Remote tarball | `/root/mars-backups/eqvps-pre-alt-a-reality-vision-20260829T113219Z.tgz` |
| SHA256 (local=remote) | `021ce536bc814519280b046d794fe14fee84c3b0a85e0c5d17acb07372246b7a` |
| Meta | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\eqvps-alt-a-reality-vision-2026-08-29\backup-meta.json` |
| Evidence copy | `X:\AI MARS\projects\mars-server-ops\evidence\EQVPS-TRANSPORT-ALTERNATIVES-WAVE-01\EQ-ALT-A_2026-08-29_190348_prep\backup-meta.json` |

**Rollback procedure (exact):**

1. Disable/remove only inbound remark `EQVPS-ALT-A-REALITY-VISION` / port **9443** and client display name `MCA-ONE-EQ-ALT-A-REALITY-VISION`.
2. Remove UFW allow **9443/tcp** (comment `EQ-ALT-A REALITY VISION`).
3. If DB/runtime drift: stop `x-ui`; restore `/etc/x-ui` and Xray `config.json` from the pre-wave tarball; start `x-ui`.
4. Verify listeners `22` / `443` / `8443` / panel; confirm **9443 absent**; confirm `:8443` RAW/TLS unchanged.

Destructive restore was **not** executed on production.

---

## 4. Existing EQVPS baseline (safe)

Recorded before/around Stage A mutation (programme evidence):

- Public IP / host: `95.216.126.173` / `metacode-cloud.com`
- Control inbound: VLESS TLS RAW/TCP **`:8443`** (must remain)
- `:443` occupied (not taken for Stage A)
- `:24443` prior experimental contour remains as historical listener (not Stage A target)
- nginx: not required for Stage A
- VEESP / MCA-VPN-001: control only — **not mutated**

---

## 5. Port / listener assessment

| Port | Role | Stage A decision |
|------|------|------------------|
| 8443 | EQVPS RAW/TLS control | **Do not touch** |
| 443 | Occupied (XHTTP) | **Do not take over** |
| 24443 | Prior test | Leave alone |
| **9443** | Stage A REALITY+Vision | **Selected isolated test port** |

**Why not 443:** would conflict with existing production-shaped listener and expand scope beyond isolated experiment.

**Live listeners (post-implement check):** `:443`, `:8443`, `:9443`, `:24443` present; `:8443` TLS subject `CN=metacode-cloud.com`.

---

## 6. REALITY+Vision architecture

| Field | Value |
|-------|--------|
| Test ID | `EQ-ALT-A-REALITY-VISION` |
| Protocol | VLESS |
| Network | TCP / RAW |
| Security | REALITY |
| Flow | `xtls-rprx-vision` |
| uTLS fingerprint | `chrome` |
| Listen port | **9443** |
| REALITY dest / SNI | `www.cloudflare.com:443` / `www.cloudflare.com` |
| Inbound remark | `EQVPS-ALT-A-REALITY-VISION` |
| Client display name | `MCA-ONE-EQ-ALT-A-REALITY-VISION` |
| Public key material | **[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]** (`pub_sha12` evidence: `e83743293573`) |

**Implementation note:** 3X-UI generated config required Vision via `client_inbounds.flow_override` (empty flow in generated client object otherwise). Initial Microsoft dest produced Reality fallthrough; rebuilt to Cloudflare dest with fresh x25519 keys.

---

## 7. Exact variables changed

**Changed (Stage A):**

- New isolated inbound on **`:9443`** (REALITY + Vision)
- Narrow UFW allow for **9443/tcp**
- Local-only client secret/profile artifacts under EQVPS local contour
- Programme tools + evidence under `projects/mars-server-ops/`

**Not changed:**

- VEESP node / profiles on VEESP
- EQVPS `:8443` inbound content/purpose
- SSH hardening
- Broad package/OS upgrade
- nginx (deferred to later experiment)
- WireGuard / DNS-control experiments

---

## 8. Server implementation summary

1. Pre-wave backup of x-ui DB/config, firewall, listeners.
2. Created isolated REALITY+Vision inbound on `:9443` (not `:8443`).
3. Applied Vision `flow_override`; rebuilt dest/SNI to Cloudflare after Microsoft fallthrough failure.
4. Opened UFW **9443/tcp** only for this experiment.
5. Exported client URI/profile to local-only paths.
6. Built offline harness from EXP-A01b model.

---

## 9. Server-side validation

Evidence:  
`X:\AI MARS\projects\mars-server-ops\evidence\EQVPS-TRANSPORT-ALTERNATIVES-WAVE-01\EQ-ALT-A_2026-08-29_190348_prep\`

| Probe | Result |
|-------|--------|
| Server loopback → `:9443` Reality transport + EQVPS egress | **PASS** (`95.216.126.173`) |
| Server hairpin → public IP `:9443` | **PASS** (`95.216.126.173`) |
| Workstation isolated Xray → `:9443` | **FAIL** (connection timeout ~25s) |
| Xray / listener health for `:9443` | **PASS** (listening) |

**Server PASS threshold for prep handoff:** met for server-side Reality stack.  
**Real-app PASS:** not claimed.

---

## 10. Existing `:8443` regression check

| Check | Result |
|-------|--------|
| Listener `:8443` | Present |
| TLS subject | `CN=metacode-cloud.com` |
| Content mutation of RAW/TLS control inbound | **0** |

---

## 11. Client profile preparation

| Item | Value |
|------|--------|
| Display name to select | **`MCA-ONE-EQ-ALT-A-REALITY-VISION`** |
| Import source (if missing) | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\eqvps-alt-a-reality-vision-2026-08-29\vless-share.uri.local` |
| Local secrets | **[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]** |
| Meta | `...\client-profile-meta.json` (local + evidence copy) |

Do **not** select historical EQVPS RAW `:8443` for this Stage A acceptance.

---

## 12. Offline harness

| Item | Absolute path |
|------|----------------|
| Harness | `X:\AI MARS\projects\mars-server-ops\tools\experiments\EQ-ALT-A-REALITY-VISION\Invoke-EQ-ALT-A-REALITY-VISION.ps1` |
| Builder | `X:\AI MARS\projects\mars-server-ops\tools\experiments\EQ-ALT-A-REALITY-VISION\build-harness.py` |
| Evidence root | `X:\AI MARS\projects\mars-server-ops\evidence\EQVPS-TRANSPORT-ALTERNATIVES-WAVE-01\` |
| DryValidate | **PASS** (2026-08-29_190730_dryvalidate) |
| Admin PowerShell | **Not required** |
| Auto profile switch | **No** |

UX follows EXP-A01b: VEESP baseline → switch to Stage A profile → transport auto → Y/N/U apps → restore VEESP → recovery → `COMPLETED.marker`.

---

## 13. Operator instructions

1. Keep **VEESP RAW `:8443`** active first.
2. Import Stage A profile from `vless-share.uri.local` if not already present.
3. Launch harness (one-liner in terminal handoff).
4. When prompted, select **`MCA-ONE-EQ-ALT-A-REALITY-VISION`** (port **9443**), not EQVPS `:8443`.
5. Press ENTER; allow transport tests.
6. Answer Cursor / ChatGPT / YouTube (optional Facebook) Y/N/U.
7. Restore **VEESP RAW `:8443`**; press ENTER; confirm recovery.
8. Do not start experiments B–E until Web-GPT/operator checkpoint after Stage A results.

---

## 14. Risks / unresolved items

- Workstation path timeout vs server PASS — same class of path uncertainty as EXP-A01b; TUN acceptance still required.
- REALITY dest choice (Cloudflare) is operational, not a claim of DPI immunity.
- One transport PASS must not be treated as final production architecture.
- Early wave incident (`tg_id` empty) briefly disrupted listeners; restored; `:8443` preserved as control.
- Foreign MARS WIP must remain untouched.

---

## 15. Evidence paths

| Path | Role |
|------|------|
| `X:\AI MARS\projects\mars-server-ops\evidence\EQVPS-TRANSPORT-ALTERNATIVES-WAVE-01\EQ-ALT-A_2026-08-29_190348_prep\` | Stage A prep evidence pack |
| `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\eqvps-alt-a-reality-vision-2026-08-29\` | Local secret + backup contour |
| `X:\AI MARS\projects\mars-server-ops\tools\experiments\EQ-ALT-A-REALITY-VISION\` | Harness + mutate/probe helpers |
| This report | `X:\AI MARS\projects\mars-server-ops\reports\MARS-SERVER-OPS-EQVPS-ALT-A-REALITY-VISION-PREP.md` |

Post-acceptance report (after offline run):  
`X:\AI MARS\projects\mars-server-ops\reports\MARS-SERVER-OPS-EQVPS-ALT-A-REALITY-VISION.md` — **not written yet**.

---

## 16. Git / server mutation closeout

| Item | Status |
|------|--------|
| VEESP mutation | **0** |
| Existing EQVPS `:8443` mutation | **0** |
| Secret disclosure in reports/chat | **0** |
| Commit | **0** |
| Push | **0** |
| Experiments B–E | **Not started** |
| Next gate | Operator offline REALITY acceptance |

**STOP** — await operator Stage A offline run results before any further alternative transport.
