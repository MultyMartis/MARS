# REPORT — WINDOWS VPN CLIENT MIGRATION — CLASH VERGE CLOSURE 01

**Date:** 2026-09-11  
**Mode:** documentation closure from accumulated incident evidence + current operator facts  
**Mutations this wave:** Git-tracked docs only. No Clash runtime, no Windows networking, no VPN servers, no C: writes, no E: access, no Git stage/commit/push.  
**Baseline authority after this report:** `X:\AI MARS\projects\mars-server-ops\CLASH-VERGE-WINDOWS-OPERATOR-BASELINE-v1.md`

Secrets (UUID, VLESS URI, Sub ID, panel path, tokens) were never required for this closure and are **not** written here.

---

## 1. Executive verdict

Windows workstation VPN client posture is **migrating from v2rayN/Xray TUN as the daily driver to Clash Verge Rev 2.5.2 / Mihomo v1.19.29 TUN**.

| Claim | Standing |
|-------|----------|
| Production VPN **nodes** (VEESP NL, FriendHosting DE) | Operational. Same nodes work in v2rayN. |
| v2rayN/Xray/TUN as daily driver | **Rejected** for this workstation after repeated TUN/TCP/Cursor-stall episodes. Retained as **fallback only**. |
| Clash Verge as preferred Windows client | **Preferred candidate.** |
| Unified FriendHosting + VEESP profile | **Exists** at the canonical local path. Node switching belongs inside `MARS-VPN`. |
| TUN stack `System` | **PROVISIONALLY ACCEPTED — SYSTEM STACK** |
| Long-duration observation | **FINAL SOAK PENDING** |
| Perfect / production-final client stability | **Not claimed.** |

**Do not** read this report as `PRODUCTION_ACCEPTED` for the Windows client, and **do not** retire v2rayN yet.

---

## 2. Original v2rayN incident

Operator and telemetry class (multi-marker analysis 11 and related v2rayN TUN audits):

- `proxy/tun: connection was refused`
- TCP / SYN / retransmit / fail pressure
- Cursor reconnects
- v2rayN GUI / network freezes
- occasional whole-PC / local-latency symptoms

Attribution from analysis 11 (not a single root cause):

| Mode | Support | Role |
|------|---------|------|
| Local TCP/TUN dispatch pressure | STRONG | v2rayN sluggishness, SYN storms, refusal bursts while Xray PID + Wintun GUID stayed stable |
| Cursor-specific path/backend reconnect | MODERATE | Cursor reconnect while gateway stayed healthy |
| Whole-system scheduling / local resource latency | MODERATE | Local HDD/audio symptoms with mixed network health |

**Not proven** as the v2rayN incident: hard Xray crash, live Wintun identity loss, NIC errors, 100 Mbps as root cause, VPN **server** death.

Both production nodes continued to work when the **client** path was healthy. The incident class is **workstation client / TUN**, not “VEESP or FriendHosting is down”.

---

## 3. What was tested

Independent A/B client: **Clash Verge Rev 2.5.2 / Mihomo v1.19.29**.

| Layer | Result summary |
|-------|----------------|
| FriendHosting via Clash | Worked well (TUN-only; historically also on gVisor). |
| VEESP via Clash (gVisor) | Repeated Mihomo `context deadline exceeded` / intermittent Timeout. |
| Live UUID / VLESS / TLS / RAW / TCP / port / SNI / ALPN / fingerprint | MATCH vs live 3X-UI / Xray. |
| Hostname vs direct-IP VEESP dial | Did not fix the gVisor-era timeout. |
| Self-route DIRECT of VEESP endpoint IP | Did not fix the gVisor-era timeout. |
| YAML stanza vs live share URI | SEMANTIC_MATCH. Manual translation **not** supported as root cause. |
| Server-side correlation | Mihomo reaches VEESP; live Xray can see a normal MCA-ONE VLESS session while the client still timed out. |
| Unified dual-node YAML | Built and structure-validated. Secrets stay local/gitignored. |
| Cursor `PROCESS-NAME` → FriendHosting | Experimental A/B only; **abandoned** as architecture. |
| Clash TUN stack `gVisor` → `System` | Operator: VEESP immediately returned ~100 ms class and appeared operational **alongside** FriendHosting. |

Experimental local `*-ab.yaml` files remain evidence. They were **not** deleted.

---

## 4. Evidence-supported conclusions

1. **VPN servers are not the v2rayN stall root.** Nodes work; v2rayN TUN on this PC repeatedly did not.
2. **Clash Verge is a viable independent client** for this workstation class (TUN-only, System Proxy off, UI DNS overlay off).
3. **FriendHosting via Mihomo** was already a working Clash path before the System-stack change.
4. **VEESP via Mihomo under gVisor** produced a client-side timeout class despite matching credentials/transport and despite server-side sighting of MCA-ONE.
5. **TUN stack System is the current preferred Clash stack** after the operator result. Hypothesis:

```text
MIHOMO_GVISOR_VEESP_PATH_COMPATIBILITY_ISSUE = STRONGLY_SUPPORTED
```

6. **One unified profile + in-group select** is the desired operating model. Profile-file swapping is not the switching method.
7. **v2rayN must not autostart** while Clash is the daily TUN controller.

---

## 5. Rejected / weakened hypotheses

| Hypothesis | Standing |
|------------|----------|
| VEESP/FriendHosting servers were down during the Clash VEESP timeouts | **Rejected** as primary explanation |
| Wrong UUID / port / SNI / ALPN / fingerprint / YAML translation | **Rejected** as root cause |
| Hostname dial vs IPv4 dial as the VEESP fix | **Weakened** (did not restore under gVisor) |
| Self-route TUN loop of VEESP IP as the VEESP fix | **Weakened** (did not restore under gVisor) |
| “TCP never arrives at VEESP” | **Rejected** (server-side correlation) |
| Mihomo/Clash process crash as the VEESP timeout class | **Rejected** (runtime audit 02: no panic/fatal; service stayed healthy) |
| gVisor is universally broken | **Rejected as overclaim.** Scope is **VEESP / Mihomo / gVisor on this workstation**. FriendHosting worked on gVisor. |
| Cursor must be process-routed to FriendHosting | **Not adopted.** Abandoned A/B, not architecture. |
| System Proxy or UI DNS overlay required for VEESP | **Not supported.** Keep both **OFF** unless a justified test. |
| v2rayN should be uninstalled now | **Rejected.** Fallback retained. |

---

## 6. Clash Verge A/B findings

| Finding | Detail |
|---------|--------|
| Client | Clash Verge Rev 2.5.2 + Mihomo v1.19.29 is the A/B client of record |
| TUN-only | System Proxy OFF and UI DNS overlay OFF were the working Clash posture |
| FriendHosting | Usable Clash path |
| VEESP (gVisor) | Dial/TLS timeout class (`wsp-cloud.com:8443 context deadline exceeded`) |
| Dual-node YAML | `FRIENDHOSTING-DE` + `VEESP-NL` + group `MARS-VPN` |
| Profile reload caution | Runtime audit 02: a reload without TUN listen produced a multi-minute silent TUN gap. Prefer in-group switching over profile swapping |
| Autostart | Clash silent auto-start **ON**; v2rayN AutoRun **OFF** — otherwise reboot reintroduces two route controllers |
| 3X-UI Clash sub | Not enabled on VEESP (`/clash/` 404). Local YAML remains the client authority |

---

## 7. VEESP-specific gVisor finding

Under Mihomo **gVisor**, VEESP repeatedly timed out while:

- the same VEESP identity/transport worked in v2rayN/Xray on this PC;
- FriendHosting on the **same** Mihomo + same PC worked;
- live UUID/transport MATCH;
- YAML SEMANTIC_MATCH;
- hostname/IP and self-route DIRECT tests did not fix it;
- VEESP Xray could still classify a normal MCA-ONE session.

After the operator changed Clash TUN stack **gVisor → System**, VEESP immediately returned normal latency (~100 ms class) and appeared operational with FriendHosting.

**Standing hypothesis:** `MIHOMO_GVISOR_VEESP_PATH_COMPATIBILITY_ISSUE = STRONGLY_SUPPORTED`.

**Not claimed:** gVisor is broken for all nodes, all OS, or all cores. **gVisor is not approved for VEESP at this time.**

**Not claimed:** System stack is proven over multi-day soak.

---

## 8. Current accepted baseline

Authority: `X:\AI MARS\projects\mars-server-ops\CLASH-VERGE-WINDOWS-OPERATOR-BASELINE-v1.md`

| Item | Accepted |
|------|----------|
| Client | Clash Verge Rev 2.5.2 |
| Core | Mihomo v1.19.29 |
| TUN | ON, stack **System**, Auto Route ON, Strict Route OFF, Auto Detect Interface ON, DNS Hijack `any:53`, MTU 1500 |
| System Proxy / UI DNS | **OFF** / **OFF** |
| Mode | Rules |
| Autostart | Clash ON + silent ON; v2rayN OFF |
| Profile | `X:\AI MARS\local\infrastructure\CLASH-VERGE-WINDOWS\mars-vpn-windows.yaml` |
| Switching | Inside `MARS-VPN` only |
| Process-rule Cursor→FriendHosting | **Not** baseline |

State label:

```text
PROVISIONALLY ACCEPTED — SYSTEM STACK
FINAL SOAK PENDING
```

---

## 9. Residual unknowns

- Long-duration Clash/System stability under real Cursor/multi-agent load (**FINAL SOAK PENDING**).
- Whether the historical Clash TUN-silent gap after reload can still occur with in-group switching + System stack.
- IPv6 profile `false` vs Verge runtime overlay `true`.
- Completeness of process-based DIRECT rules vs the old v2rayN Prog list.
- Whether 3X-UI Clash/Mihomo subscription should replace local YAML later.
- Whether v2rayN can eventually be retired.
- Exact Mihomo/gVisor mechanism on the VEESP path (uTLS/dialer/timeout budget) — **UNPROVEN** as a code-level cause; stack-level compatibility is **STRONGLY_SUPPORTED**.

---

## 10. Rollback posture

1. Stop Clash TUN (GUI disable TUN / quit Clash).
2. Confirm no Meta TUN adapter remains in the way of Wintun.
3. Start **v2rayN only** (autostart still left OFF after the emergency).
4. Do not run both TUN stacks.
5. Keep v2rayN installed. Do not delete experimental `*-ab.yaml` evidence during rollback.

---

## 11. Next work

Not executed here:

- Long-duration Clash/System soak
- Full migration of required process-based DIRECT rules
- Review IPv6 runtime/profile collision
- Optional 3X-UI Clash/Mihomo subscription enablement for VEESP/FriendHosting
- AlphaVPS integration later
- Eventual decision whether v2rayN can be retired
- Optional cleanup/archive of experimental local `*-ab.yaml` **after** acceptance

---

## 12. Closure state

| Field | Value |
|-------|-------|
| **Incident class (v2rayN daily driver)** | Closed as **rejected daily driver** for this workstation; fallback retained |
| **Clash introduction** | Closed as **preferred candidate client** |
| **VEESP-on-Clash (gVisor)** | Closed as **incompatible for current use** (not a server outage) |
| **VEESP-on-Clash (System)** | **PROVISIONALLY ACCEPTED — SYSTEM STACK** |
| **Final client production acceptance** | **OPEN** — **FINAL SOAK PENDING** |
| **Git promotion** | Separate clean-worktree wave |
| **Server / Clash runtime / Windows mutation** | None in this wave |

```text
PROVISIONALLY ACCEPTED — SYSTEM STACK
FINAL SOAK PENDING
```

**NO GIT PROMOTION / NO SERVER MUTATION / NO CLASH RUNTIME MUTATION / NO WINDOWS MUTATION / NO C: WRITES / NO E: ACCESS**

---

*WINDOWS-VPN-CLIENT-MIGRATION-CLASH-VERGE-CLOSURE-01 · 2026-09-11 · no secrets.*
