# Clash Verge — Windows Operator Baseline v1

**Programme:** MARS Server Ops & VPS Forge  
**Status:** **PROVISIONALLY ACCEPTED — SYSTEM STACK** · **FINAL SOAK PENDING**  
**Role:** operational authority for the operator Windows VPN **workstation client**  
**Does not own:** VPN servers, 3X-UI, Windows networking, Clash runtime mutation, Git promotion  
**Last operator evidence:** 2026-09-11 (TUN stack `gVisor` → `System`; VEESP latency ~100 ms class restored alongside FriendHosting)

This file is the standing Windows-client baseline. Incident reports remain evidence. Server passports remain server authority. Do **not** treat experimental `*-ab.yaml` files as this baseline.

---

## 1. Status / scope

| Field | Value |
|-------|-------|
| **Workstation role** | Operator Windows VPN client for Cursor / real-workload traffic |
| **Preferred client (candidate)** | **Clash Verge Rev** + **Mihomo** TUN |
| **Acceptance** | **PROVISIONALLY ACCEPTED — SYSTEM STACK** |
| **Long-duration soak** | **FINAL SOAK PENDING** — not yet proven |
| **Production client retirement of v2rayN** | **NOT DECIDED** |
| **Servers in this baseline** | FriendHosting DE + VEESP NL only (AlphaVPS later) |
| **Git contour** | Local YAML/secrets stay gitignored; this document has **no** UUIDs / URIs / tokens |

**Scope in:** one unified Clash profile, TUN-only operation, in-group node switching, v2rayN fallback posture, known incompatibilities.

**Scope out:** mutating Clash/Windows/servers; enabling 3X-UI Clash subscriptions; migrating the full v2rayN process-DIRECT list; deleting experimental YAML.

---

## 2. Architecture

Preferred architecture:

```text
Windows workstation (this operator PC)
  → Clash Verge Rev GUI + clash_verge_service
  → Mihomo TUN (stack = System)
  → one unified profile
  → proxy-group MARS-VPN  (select: FRIENDHOSTING-DE | VEESP-NL)
  → VLESS + TLS + RAW/TCP :8443 on the selected node
  → Internet egress
```

**One unified profile is preferred.** Do **not** switch FriendHosting vs VEESP by swapping entire YAML profiles. Switch only the selected member of `MARS-VPN`.

TUN is owned by the Clash Verge **UI / service**, not by a profile-level `tun:` block.

v2rayN + Xray TUN remains **rollback / emergency comparison** only. Do **not** run v2rayN TUN and Clash TUN at the same time.

---

## 3. Current software / core versions

| Component | Accepted version | Notes |
|-----------|------------------|-------|
| Clash Verge Rev | **2.5.2** | Install contour historically `C:\Program Files\Clash Verge` (do not mutate from this doc) |
| Mihomo core | **v1.19.29** (`verge-mihomo`, Windows amd64, binary tagged `with_gvisor`) | Keep `verge-mihomo`. Do **not** switch to alpha unless separately chartered |
| Clash service | `clash_verge_service` | Required for TUN; StartType Automatic in prior audits |
| v2rayN / Xray | retained, version not re-baselined here | Fallback only; autostart **OFF** |

---

## 4. Approved VPN nodes

Both production nodes are **operational**. Same nodes also work through v2rayN. Clash is the **client** variable.

| Proxy name in profile | Node | Identity class | Transport |
|-----------------------|------|----------------|-----------|
| `FRIENDHOSTING-DE` | FriendHosting / Germany | WSP-ONE (workstation) | VLESS + TLS + RAW/TCP `:8443` |
| `VEESP-NL` | VEESP / Netherlands (`MCA-VPN-001`) | MCA-ONE (workstation) | VLESS + TLS + RAW/TCP `:8443` |

Shared group: **`MARS-VPN`** (`select`), members `FRIENDHOSTING-DE`, `VEESP-NL`, `DIRECT`. Fresh load without a stored selection starts on `FRIENDHOSTING-DE`.

AlphaVPS is **not** in this baseline.

---

## 5. Canonical local profile path

```text
X:\AI MARS\local\infrastructure\CLASH-VERGE-WINDOWS\mars-vpn-windows.yaml
```

| Rule | Detail |
|------|--------|
| **Canonical** | This single file |
| **Git** | Under `/local/` — **gitignored**. Never stage, commit, or paste secrets from it |
| **Experimental `*-ab.yaml`** | Evidence only. Do **not** delete in this era. Do **not** promote them to baseline |
| **Abandoned A/B** | `PROCESS-NAME,Cursor.exe,FRIENDHOSTING-DE` is **not** baseline architecture |

---

## 6. Accepted Windows / Clash settings

**PROVISIONALLY ACCEPTED — SYSTEM STACK.** Do not retune this trio unless a new charter requires a single-variable test.

| Setting | Accepted value |
|---------|----------------|
| TUN | **ON** |
| TUN stack | **System** (preferred) |
| Auto Route | **ON** |
| Strict Route | **OFF** |
| Auto Detect Interface | **ON** |
| DNS Hijack | `any:53` |
| MTU | **1500** |
| System Proxy | **OFF** |
| UI DNS overlay | **OFF** |
| Routing / UI mode | **Rules** |
| Clash autostart | **ON** |
| Clash silent start | **ON** |
| v2rayN autostart | **OFF** (operator-managed) |
| Profile DNS | redir-host; nameservers `8.8.8.8` / `1.1.1.1`; listen `127.0.0.1:1053`; no FakeIP |
| HTTP external controller | keep **off** unless a later charter needs it |
| Core | `verge-mihomo` (not alpha) |

**Not approved without a justified test:** System Proxy, UI DNS overlay, `strict-route: true`, Clash alpha core, profile-level `tun:`.

**TUN stack caution:** `gVisor` is **not** approved for **VEESP** at this time. It is **not** documented as universally broken. FriendHosting previously worked on gVisor; VEESP on Mihomo gVisor produced `context deadline exceeded` / Timeout until the stack was changed to System.

---

## 7. Routing policy

Conservative profile rules (unified YAML). Full v2rayN process-DIRECT inventory is **not** migrated yet.

| Match | Action |
|-------|--------|
| Private / LAN (`GEOIP,private`, RFC1918, loopback, link-local, multicast, equivalent IPv6) | **DIRECT** |
| `DOMAIN-SUFFIX,ru` (`.ru`) | **DIRECT** |
| `DOMAIN-SUFFIX,xn--p1ai` (`.рф`) | **DIRECT** |
| `GEOIP,RU` | **DIRECT** |
| Final `MATCH` | selected member of **`MARS-VPN`** |

Do **not** add `PROCESS-NAME,Cursor.exe,FRIENDHOSTING-DE` (or any Cursor-forced-node rule) to the baseline.

---

## 8. Switching VEESP ↔ FriendHosting

1. Confirm v2rayN is **fully closed** (no `v2rayN.exe` / `xray.exe` TUN).
2. Confirm Clash TUN is **ON**, stack **System**, mode **Rules**.
3. In group **`MARS-VPN`**, select `FRIENDHOSTING-DE` or `VEESP-NL`.
4. Do **not** import a different YAML to change nodes.
5. Confirm `.ru` / `.рф` / LAN remain DIRECT after the switch.
6. If VEESP again shows Mihomo `context deadline exceeded`, check TUN stack first — if it drifted back to `gVisor`, restore **System** before any YAML experiment.

---

## 9. Startup / shutdown behavior

| Event | Expected |
|-------|----------|
| Windows logon | Clash Verge silent auto-start → service-mode Mihomo → TUN System |
| Clash GUI exit (historical gVisor era) | TUN was disabled with the GUI; silent auto-start is intended to restore TUN after reboot |
| Reboot conflict | v2rayN AutoRun **must stay OFF** so two TUN controllers do not race |
| Shutdown of Clash | Disable TUN in Clash before starting v2rayN |
| Shutdown of v2rayN | Fully quit v2rayN/Xray before starting Clash TUN |

---

## 10. v2rayN fallback posture

| Rule | Detail |
|------|--------|
| Role | Rollback / emergency comparison only |
| Autostart | **OFF** |
| Removal | **Do not uninstall** in this era |
| Simultaneous TUN | **Forbidden** — Clash TUN and v2rayN TUN must not both be up |
| When to use | Clash cannot provide a usable path; need Xray comparison; or a chartered A/B against Mihomo |
| After fallback | Close v2rayN completely before returning to Clash |

---

## 11. Known incompatibilities / cautions

| Item | Standing statement |
|------|--------------------|
| **Mihomo gVisor + VEESP** | `MIHOMO_GVISOR_VEESP_PATH_COMPATIBILITY_ISSUE = STRONGLY_SUPPORTED`. gVisor is **not** approved for VEESP. Scope is **VEESP via Mihomo gVisor on this workstation**, not “gVisor is broken everywhere”. |
| **YAML / UUID / SNI mismatch** | **Not** supported as VEESP timeout root cause. Live UUID/transport MATCH; stanza vs URI SEMANTIC_MATCH. |
| **Hostname vs direct-IP** | Did **not** restore VEESP under gVisor. |
| **Self-route DIRECT of VEESP IP** | Did **not** restore VEESP under gVisor. |
| **Server-side VEESP inbound** | Mihomo can reach live Xray; server can see a normal MCA-ONE VLESS session while the client still timed out under gVisor. Failure class was **client-side**. |
| **IPv6** | Profile `ipv6: false` vs historical Verge runtime overlay `ipv6: true` — **pending review**, not retuned here. |
| **3X-UI Clash subscription** | VEESP `/clash/` is **not** enabled (404). Local YAML is the authority. Optional enablement is future work. |
| **Cursor process-routing A/B** | Abandoned. Not architecture. |
| **Dual TUN** | Clash Meta TUN + v2rayN Wintun together is a collision class. |

---

## 12. Validation checklist

Use after reboot, after a client change, or after a suspected stall. Do **not** treat a single latency sample as soak.

1. Only one TUN controller: Clash **or** v2rayN, not both.
2. Clash Verge 2.5.2 / Mihomo v1.19.29 / TUN ON / stack **System**.
3. System Proxy OFF, UI DNS overlay OFF, mode Rules.
4. Active profile is the unified file in §5 (not an `*-ab.yaml`).
5. `MARS-VPN` selection is the intended node.
6. LAN / `.ru` / `.рф` still DIRECT.
7. FriendHosting path: usable latency and real-workload (at least browser + Cursor control check).
8. VEESP path: ~100 ms class and real-workload, **without** returning the stack to gVisor.
9. No concurrent `v2rayN.exe` autostart after reboot.
10. Record duration: this checklist is **not** a substitute for long soak.

---

## 13. Incident response

| Symptom | First actions (read, then charter if mutating) |
|---------|------------------------------------------------|
| VEESP Timeout / `context deadline exceeded` in Mihomo | Confirm stack is **System**, not gVisor. Confirm v2rayN is down. Do **not** rewrite YAML credentials first. |
| Both nodes dead in Clash | Confirm TUN still up; do not assume server death. Historical gap: TUN silent after reload. |
| Cursor reconnect storms + local TCP pressure | If Clash is not running and v2rayN TUN is up, this is the **legacy v2rayN incident class** — close v2rayN TUN rather than retuning servers. |
| Need comparison | Fully stop Clash TUN, then start v2rayN **alone**. |
| Temptation to add Cursor → FriendHosting process rule | **Stop.** That A/B is not baseline. |

Do **not** cycle Reality / WS / gRPC / random MTU / System Proxy / UI DNS overlay to “fix” a TUN-stack issue.

---

## 14. Pending work

Captured, **not** executed by this baseline:

| Item | State |
|------|-------|
| Long-duration Clash / System soak | **FINAL SOAK PENDING** |
| Full migration of required process-based DIRECT rules | Future charter |
| Review IPv6 runtime vs profile collision | Future charter |
| Optional 3X-UI Clash/Mihomo subscription enablement (VEESP / FriendHosting) | Future mutation charter |
| AlphaVPS integration into the unified profile | Later |
| Decision whether v2rayN can be retired | After soak + residual process-rule work |
| Optional cleanup/archive of experimental local `*-ab.yaml` | Only **after** acceptance; do not delete now |

---

## 15. Evidence references

| Document | Role |
|----------|------|
| `X:\AI MARS\projects\mars-server-ops\reports\WINDOWS-VPN-CLIENT-MIGRATION-CLASH-VERGE-CLOSURE-01.md` | Migration closure / verdict |
| `X:\AI MARS\projects\mars-server-ops\reports\WINDOWS-CURSOR-V2RAYN-GOOD-BAD-MULTI-MARKER-ANALYSIS-11.md` | v2rayN TUN / TCP stall class |
| `X:\AI MARS\projects\mars-server-ops\reports\CLASH-VERGE-SETTINGS-AUDIT-01.md` | Historical Clash settings (gVisor-era snapshot) |
| `X:\AI MARS\projects\mars-server-ops\reports\CLASH-VERGE-RUNTIME-FAILURE-AUDIT-02.md` | VEESP Mihomo deadline + TUN gap |
| `X:\AI MARS\projects\mars-server-ops\reports\VEESP-3XUI-CLASH-SUBSCRIPTION-AUDIT-01.md` | Subscription not Clash-YAML; credentials MATCH |
| `X:\AI MARS\projects\mars-server-ops\reports\VEESP-VLESS-MIHOMO-STANZA-DIFFERENTIAL-AUDIT-01.md` | YAML translation rejected as root cause |
| `X:\AI MARS\projects\mars-server-ops\reports\VEESP-SERVER-SIDE-MIHOMO-COMPATIBILITY-AUDIT-01.md` | Server sees normal MCA-ONE session |
| `X:\AI MARS\projects\mars-server-ops\reports\CLASH-VERGE-UNIFIED-DUAL-NODE-PROFILE-BUILD-01.md` | Unified profile creation |
| `X:\AI MARS\projects\mars-server-ops\reports\CLASH-CURSOR-VIA-FRIENDHOSTING-AB-01.md` | Abandoned Cursor process-rule A/B (evidence only) |
| `X:\AI MARS\projects\mars-server-ops\DUAL-VPN-OPERATOR-BASELINE-v1.md` | **Server** operator cheat sheet (nodes/panels/backups) |

---

*Windows Clash Verge operator baseline v1 · 2026-09-11 · PROVISIONALLY ACCEPTED — SYSTEM STACK · FINAL SOAK PENDING · no secrets.*
