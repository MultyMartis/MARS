# REPORT — VEESP VS CUSTOM V1/V2 DIFFERENTIAL ROOT CAUSE

**Date:** 2026-08-28  
**Scope:** Local-only offline differential analysis. No v2rayN / Xray / EQVPS / Server A mutation. No commit.  
**Operator constraint honored:** Working VEESP profile (`MCA-Gate-TLS-MCA-ONE`) remains active; live `binConfigs\config.json` verified unchanged.

**Raw evidence (local, not in git):**  
`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-v1-v2-differential-raw-2026-08-28\`

---

## Verdict

**ROOT CAUSE (evidence-based):** Custom v2 copied the VEESP routing/DNS shell **without retargeting the VPN endpoint hostname exemption.** The working VEESP runtime resolves `wsp-cloud.com` via **direct DNS** (`direct-dns-1`) and routes that DNS traffic **direct**. Custom v2 still lists **`wsp-cloud.com`** (stale) and has **no** `metacode-cloud.com` entry. Therefore `metacode-cloud.com` resolution falls through to the fallback resolver and is routed by rule 17 (`dns-module` → **proxy**) — a **bootstrap deadlock** before the XHTTP tunnel exists. This explains Custom v2 GUI failure (`schannel` TLS handshake failure, `-1 ms`, no ChatGPT/YouTube) while Custom v1 (no DNS subsystem) and standalone XHTTP (no DNS subsystem) succeed.

**Secondary amplifier (MEDIUM):** Custom v2 adds **TUN** and full 18-rule routing; Custom v1 does not. TUN is not required to explain explicit `curl -x 127.0.0.1:10808` failure, but it amplifies system-wide breakage once DNS bootstrap fails.

**Not root cause:** Proxy outbound leg itself — Custom v1 and Custom v2 **proxy outbounds are byte-identical** and match the known-good standalone XHTTP artifact (validated in prior forensic waves).

---

## Working VEESP baseline

| Check | Result |
|-------|--------|
| Live `C:\Program Files\v2rayN\binConfigs\config.json` | **VEESP confirmed** — `wsp-cloud.com:8443`, `network=raw`, `security=tls` |
| Byte-identical to captured `veesp-working-runtime.json` | **YES** (9663 bytes) |
| Egress (operator) | `178.173.250.69` |
| Top-level sections | `log`, `dns`, `inbounds`, `outbounds`, `routing`, `policy`, `stats`, `metrics` |
| Inbounds | `socks` mixed `:10808`, **TUN**, `api` `:10812` |
| Routing rules | **18** (catch-all → proxy; RU/direct split; UDP/443 block) |
| Proxy outbound | VLESS raw/TLS → `wsp-cloud.com:8443`, ALPN `http/1.1` only |

**FACT:** Operator production client works with this full stack (TUN + DNS + split routing + raw/TLS VEESP leg).

---

## Why standalone EQVPS XHTTP works

| Property | Standalone `standalone-primary-corrected.json` |
|----------|-----------------------------------------------|
| DNS subsystem | **Absent** |
| TUN | **Absent** |
| Routing rules | **0** (default first outbound) |
| Inbound | HTTP proxy test port only (forensic isolation) |
| Proxy outbound | VLESS XHTTP/TLS → `metacode-cloud.com:443` with full `xPaddingBytes` |

**FACT:** Isolated Xray test with this file reaches `95.216.126.173` (prior forensic wave).

**INFERENCE:** With no internal DNS module, Xray resolves `metacode-cloud.com` via **OS/system resolver** on a direct path — no `dns-module → proxy` loop.

---

## Custom v1

| Property | Value |
|----------|-------|
| File size | **1676 bytes** |
| Inbounds | **1** — mixed `127.0.0.1:10808` only (tag `mixed`) |
| Outbounds | **proxy only** |
| Routing | `domainStrategy: AsIs`, **rules: []** |
| DNS | **Absent** |
| TUN | **No** |
| Proxy outbound | **Identical to Custom v2 proxy leg** (EQVPS XHTTP/TLS) |

**Operator facts (accepted):**

- Explicit proxy tests: Google/YouTube **PASS**, egress `95.216.126.173`
- Real GUI activation: YouTube **partially** worked (slow/uncertain)
- **Not** production-ready

**INFERENCE:** v1 succeeds for the same reason as standalone — **no DNS bootstrap trap**. Partial GUI behavior may reflect missing TUN/split routing (browser/system path differs from explicit `-x 10808`), not a broken proxy leg.

---

## Custom v2

| Property | Value |
|----------|-------|
| File size | **9936 bytes** |
| Structural diff vs VEESP (non-proxy) | **IDENTICAL** (routing, DNS, inbounds, aux outbounds) |
| Structural diff vs VEESP (proxy only) | Address/port/transport replaced (intended) |
| Proxy outbound vs Custom v1 | **BYTE-IDENTICAL** |

**Operator facts (accepted, not reinterpreted):**

- Real GUI activation: `curl -x http://127.0.0.1:10808 https://api.ipify.org` → **schannel TLS handshake failure**
- ChatGPT / YouTube: **FAIL**
- v2rayN delay: **-1 ms**
- `CUSTOM_V2_OPERATOR_REALITY = FAIL`

**INFERENCE:** Failure is not the XHTTP outbound definition; it is the **surrounding VEESP shell** applied to a **different endpoint hostname** without retargeting DNS exemptions.

---

## Full structural difference

| SECTION | VEESP live | Custom v1 | Custom v2 | Standalone XHTTP |
|---------|------------|-----------|-----------|------------------|
| `log` | present | present | present | present |
| `dns` | present (4 servers) | **absent** | present (4 servers, **identical to VEESP**) | **absent** |
| `inbounds` | mixed+**tun**+api | mixed only | mixed+**tun**+api | http test only |
| `outbounds` | proxy+direct+block+dns | **proxy only** | proxy+direct+block+dns | proxy only |
| `routing` | 18 rules | **0 rules** | 18 rules (VEESP clone) | 0 rules |
| `policy` / `stats` / `metrics` | present | absent | present | absent |
| Proxy leg | raw/TLS `wsp-cloud.com:8443` | xhttp `metacode-cloud.com:443` | xhttp `metacode-cloud.com:443` | xhttp `metacode-cloud.com:443` |
| v2 vs VEESP non-proxy | — | — | **IDENTICAL** | — |

---

## Endpoint bypass comparison

### VEESP (`wsp-cloud.com` / `178.173.250.69`)

| Mechanism | Present? | Detail |
|-----------|----------|--------|
| Routing direct domain rule for VPN hostname | **NO** | No explicit `domain:wsp-cloud.com → direct` routing rule |
| Routing direct IP rule for VPN IP | **NO** | No `178.173.250.69` rule |
| **DNS direct-dns-1 domain list** | **YES** | `wsp-cloud.com` in server[0] `domains` with `skipFallback: true` |
| DNS query path for VPN hostname | **direct-dns-1** → routing rule 16 → **direct** outbound |
| Process self-traffic rule | **YES** | Rule 4: `xray.exe` / `self/` → **direct** (protects TCP dial after resolve) |

### EQVPS in Custom v2 (`metacode-cloud.com` / `95.216.126.173`)

| Mechanism | Present? | Detail |
|-----------|----------|--------|
| Routing direct domain rule | **NO** | — |
| Routing direct IP rule | **NO** | — |
| DNS direct-dns-1 domain list | **NO for metacode-cloud.com** | List still contains **`wsp-cloud.com` only** (stale VEESP copy) |
| DNS query path for VPN hostname | Fallback `https://dns.google/dns-query` → tagged `dns-module` → rule 17 → **proxy** |
| Process self-traffic rule | **YES** (copied) | Same rule 4 — helps TCP **after** DNS resolves, but does not fix DNS bootstrap |

**FACT:** Copying routing "identically" from VEESP was **wrong** for EQVPS because the **endpoint-specific DNS exemption was hostname-bound to `wsp-cloud.com`**, not transport-bound. Replacing the outbound leg alone did not retarget that exemption.

---

## DNS comparison

| Question | `wsp-cloud.com` (VEESP / v2 DNS) | `metacode-cloud.com` (v2 DNS) |
|----------|----------------------------------|-------------------------------|
| Which DNS server resolves it? | Server[0] DoH `1.1.1.1`, tag `direct-dns-1` | Server[3] fallback `dns.google` DoH (not in direct-dns lists) |
| In direct DNS domain list? | **YES** (VEESP + v2) | **NO** |
| DNS query routing | `direct-dns-1` inbound → rule 16 → **direct** | `dns-module` inbound → rule 17 → **proxy** |
| Under TUN | Port 53 from TUN → rule 5 → `dns` outbound (then internal DNS logic) | Same — but internal resolution still hits rule 17 for non-exempt names |
| Can outbound establish without tunnel? | **YES** — direct DNS path | **NO** — DNS for server hostname requires proxy that needs DNS |

**Explicit answer:** The EQVPS server hostname **cannot** reliably resolve under Custom v2's DNS/routing without relying on the tunnel it is trying to open.

Custom v1 / standalone: **no internal DNS** → system resolver → **no rule 17 loop**.

---

## TUN / routing interaction

**Rule order (Custom v2 = VEESP):**

1. Rules 0–14: block noise, RU/direct/process exceptions, UDP/443 block  
2. **Rule 15:** catch-all `0-65535` → **proxy** (user traffic)  
3. **Rule 16:** `direct-dns-1`, `direct-dns-2` → **direct**  
4. **Rule 17:** `dns-module` → **proxy**

**Self-routing trace for `metacode-cloud.com` DNS lookup inside Xray:**

```
Need resolve metacode-cloud.com
  → not in direct-dns-1/2 domain lists
  → fallback dns.google (dns-module tag)
  → rule 17 matches → outbound proxy
  → proxy must connect to metacode-cloud.com
  → requires resolve metacode-cloud.com → RECURSION / DEADLOCK
```

**Self-routing trace for `wsp-cloud.com` in VEESP:**

```
Need resolve wsp-cloud.com
  → direct-dns-1 (skipFallback)
  → rule 16 → outbound direct
  → resolve succeeds
  → rule 4 (xray.exe process) → TCP to wsp-cloud.com:8443 direct
  → tunnel establishes
```

**TUN:** Adds system-wide capture (`0.0.0.0/0`) and TUN DNS injection (rule 5). Custom v1 lacks TUN — consistent with "explicit proxy works, full GUI split weaker." TUN is **not** the primary schannel failure mode for rule-17 DNS bootstrap on `:10808`, but worsens browser/ChatGPT paths once core is unhealthy.

**XHTTP-specific note:** XHTTP uses multiple HTTP/TLS sub-connections (`mode: auto`, padding, upload/download streams). It depends on stable **prior** resolution and direct core egress more than single-socket raw/TLS. Bootstrap failure surfaces as TLS handshake errors to local clients.

---

## V1 vs V2 suspects

### V1_WORKING_COMPONENTS

- Proxy outbound only (known-good EQVPS XHTTP)
- Mixed inbound `:10808` without TUN
- Empty routing (all traffic → default proxy outbound)
- No DNS subsystem → system resolver bootstrap
- No auxiliary outbounds

### V2_ADDED_COMPONENTS

- TUN inbound with default route capture
- Full DNS module (4 servers, hosts map, tags)
- 18 routing rules (VEESP clone)
- `direct` / `block` / `dns` outbounds
- `api` inbound, `policy`, `stats`, `metrics`
- Stale `wsp-cloud.com` in direct-dns-1

### V2_SUSPECT_COMPONENTS (ranked)

1. **HIGH — DNS bootstrap deadlock:** `metacode-cloud.com` missing from `direct-dns-1`; rule 17 routes `dns-module` → proxy. Evidence: traced rule indices; `wsp-cloud.com` exempt in VEESP; v1/standalone without DNS work.

2. **HIGH — Stale endpoint copy error:** `wsp-cloud.com` retained in DNS domains after proxy retarget to `metacode-cloud.com`. Evidence: DNS server[0] domain list byte-identical to VEESP.

3. **MEDIUM — TUN + system DNS path:** v1 partial GUI vs v2 total GUI failure. Evidence: v2 adds TUN; v1 lacks it. Not sole cause of explicit-proxy schannel symptom.

4. **LOW — UDP/443 block:** Present in working VEESP. Unlikely schannel root cause.

5. **LOW — Proxy transport (XHTTP vs raw):** Ruled out — v1/v2/standalone share same proxy definition; isolated tests pass.

---

## Root cause

**Strongest evidence-based cause:**

Custom v2 is a **hostname-unadjusted VEESP shell**. The VEESP shell includes an implicit contract: **the VPN server's own hostname must resolve and route outside the catch-all proxy path** (`wsp-cloud.com` → direct DNS). Custom v2 breaks that contract for `metacode-cloud.com` while still sending non-exempt DNS through the proxy outbound (rule 17), preventing XHTTP tunnel bootstrap.

**Classification:** FACT (DNS list + rule trace from JSON) + INFERENCE (deadlock mechanism consistent with schannel symptom and v1/standalone contrast).

---

## Why copying VEESP config was insufficient

Replacing only the `proxy` outbound is **not** sufficient because VEESP working behavior depends on **three coupled layers**:

1. **Transport** — raw/TLS single-socket vs XHTTP multi-request (different, but proven OK in isolation)  
2. **DNS exemption** — VPN hostname in `direct-dns-1` domains (**hostname-specific**, was `wsp-cloud.com`)  
3. **Routing** — `direct-dns-* → direct` (rule 16) and `dns-module → proxy` (rule 17) together define bootstrap order

Custom v2 changed (1) partially in the outbound object but **left (2) pointing at the old VEESP hostname** and kept (3) unchanged. The new endpoint therefore enters the `dns-module → proxy` path, which VEESP never used for its own server name.

Raw/TLS VEESP masked this because **`wsp-cloud.com` was explicitly exempted**. XHTTP does not remove the need for that exemption — if anything, multi-connection XHTTP is **more sensitive** to failed bootstrap.

---

## Minimal proposed fix

**DO NOT APPLY in this wave.**

In Custom v2 DNS `servers[0].domains`, **replace** `wsp-cloud.com` with **`metacode-cloud.com`** (or add `metacode-cloud.com` alongside removal of stale `wsp-cloud.com`).

This is the **smallest single change** that restores the VEESP bootstrap contract for the new endpoint without altering routing rules, TUN, or the proxy outbound.

Optional follow-up (not part of minimal fix): add explicit routing `domain:metacode-cloud.com → direct` as belt-and-suspenders — not required if DNS direct-dns-1 is corrected.

---

## Server mutation

**NO**

## v2rayN mutation

**NO**

## Git

**NO COMMIT**

---

## NEXT ACTION

**Exactly one:** Human review this report; if accepted, produce **Custom v2.1** as a **copy of Custom v2 with only** `wsp-cloud.com` → `metacode-cloud.com` in DNS `direct-dns-1` domains — then operator activates v2.1 (still without touching live VEESP) and re-tests `curl -x http://127.0.0.1:10808 https://api.ipify.org` plus browser ChatGPT/YouTube.

Stop.
