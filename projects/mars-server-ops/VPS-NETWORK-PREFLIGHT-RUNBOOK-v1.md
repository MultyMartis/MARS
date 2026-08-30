# VPS Network Preflight Runbook v1

**Programme:** MARS Server Ops & VPS Forge  
**Stages:** 8 (pre-purchase), 10 (post-provision)  
**Status:** **BASELINE v1** — reusable network test procedure  
**Not:** continuous monitoring product or automated speed-test fleet

---

## 1. Purpose

Measure path quality from the **actual operator workstation/network** to candidate provider test endpoints (pre-purchase) and to the **assigned VPS IP** (post-provision).

Provider marketing latency is **not** operator truth.

---

## 2. Test environment rules

| Rule | Detail |
|------|--------|
| Source network | Actual operator network for the use case |
| VPN / TUN distortion | Direct path tests require **TUN OFF** and **System Proxy OFF** |
| Cursor / AI tools | **Not required** during measurement |
| Endpoints | Prefer **provider official** test / iperf / looking-glass hosts **and** later the **assigned** IP |
| Known-listener TCP | Prefer testing against a **known listening** port; empty-port timeouts are non-diagnostic |
| Generic runbook | **Do not** hard-code provider-specific endpoints here — put them in case evidence |

**Case lesson (AdminVPS Server B):** looking-glass / pre-purchase path performance can **PASS** while the **actually assigned** subnet/IP fails direct Goodline entry.

```text
provider looking-glass PASS  ≠  assigned IP / subnet PASS
```

Direct ISP preflight on the **assigned** address is required where possible before declaring network suitability.

**Case lesson (FriendHosting):** after known-listener TCP gates and real-workload acceptance on the assigned IP, an independent ASN/provider can validate the same client/Xray/RAW architecture that fails on EQVPS — without proving EQVPS's exact mechanism.

---

## 3. Local bottleneck check (mandatory before blaming VPS)

Before concluding that a VPS/datacenter is slow, inspect operator-side link capacity.

**Windows example:**

```powershell
Get-NetAdapter | Where-Object Status -eq "Up" | Format-Table Name,InterfaceDescription,LinkSpeed
```

Distinguish:

| Adapter type | Interpretation |
|--------------|----------------|
| Physical NIC | Real link ceiling (e.g. 100 Mbps Ethernet) |
| Virtual TUN | Often reports unrealistic speeds (e.g. 100 Gbps) — **not** physical capacity |

If physical Ethernet negotiates at **100 Mbps** and iperf reaches roughly **85–95 Mbps**, do **not** attribute the ceiling to the remote provider without further evidence.

---

## 4. Pre-purchase measurements (Stage 8)

### 4.1 Ping

At least approximately **20 packets**.

Record: minimum; average; maximum; packet loss.

### 4.2 Traceroute

Record route shape and major anomalies.

Do **not** treat non-responsive intermediate hops as automatic packet loss.

### 4.3 HTTP test file

Use provider official test endpoint where available.

Record: file size; duration; calculated throughput.

**Interpretation caution:** A slower HTTP test endpoint does **not** prove VPS network capacity is equally slow if iperf demonstrates substantially higher throughput.

### 4.4 iperf3

Prefer provider official iperf3 endpoint when available.

Test forms (generic):

```text
iperf3 -c <TEST_HOST> -p <PORT>
iperf3 -c <TEST_HOST> -p <PORT> -P 4
iperf3 -c <TEST_HOST> -p <PORT> -P 4 -R
```

| Mode | Purpose |
|------|---------|
| Single TCP stream upload | Single-flow behaviour |
| Multi-stream upload (`-P 4`) | Aggregate uplink |
| Multi-stream reverse (`-P 4 -R`) | Aggregate download |

---

## 5. Result interpretation

Never use one metric alone. Evaluate together:

- RTT  
- Jitter / stability  
- Packet loss  
- Single-stream performance  
- Multi-stream performance  
- Reverse performance  
- Route shape  
- Local link ceiling  

Additional cautions:

| Observation | Do not conclude |
|-------------|-----------------|
| ICMP failure | Automatic HTTPS / VPS unreachability |
| HTTP slow, iperf high | That HTTP alone equals path capacity |
| Looking-glass unavailable | Entire country/DC is down |

---

## 6. Post-provision validation (Stage 10)

After actual VPS procurement, **repeat** testing against the **assigned server IP**.

Pre-purchase endpoints prove **provider/location** suitability only — **not** the assigned VPS/IP path.

**Mandatory diversity notes (qualification doctrine):**

- Prefer **ASN / network diversity** when building independent controls.  
- Prefer **country / provider diversity** when diagnosing path-specific failures.  
- Record route/ASN evidence for assigned IP (not only marketing region labels).

Before full production build verify:

| Check | Status |
|-------|--------|
| IP reachability (TUN OFF) | ☐ |
| Known-listener TCP (SSH / HTTPS as applicable) | ☐ |
| Latency | ☐ |
| Loss | ☐ |
| Download / throughput sample | ☐ |
| Network/ASN identity of assigned prefix | ☐ |
| IP reputation (where relevant) | ☐ |
| Required AI / external services (real workload — see acceptance doctrine) | ☐ |
| Provider console | ☐ |
| Backup + restore strategy present | ☐ |

If assigned IP has poor reachability: investigate **IP/subnet replacement** before investing heavily in configuration.

**AdminVPS case evidence:** [SERVER-B-PHASE-3E-FINAL-NETWORK-VERDICT-v1.md](assets/SERVER-B-PLANNING/SERVER-B-PHASE-3E-FINAL-NETWORK-VERDICT-v1.md) — provider not globally rejected; **assigned IP REJECTED** for direct entry.

**Verdict vocabulary:**

| Verdict | Meaning |
|---------|---------|
| **PRE-PURCHASE NETWORK APPROVED** | Location / provider path suitable for procurement |
| **POST-PROVISION VERIFIED** | Assigned IP path validated |
| **HOLD / INVESTIGATE** | Path or IP issues — do not proceed to heavy build |

---

## 7. Evidence record fields

For each test wave, record at minimum:

| Field | Value |
|-------|-------|
| Date / time (operator local or UTC) | |
| Source path (direct ISP / via TUN) | |
| Local physical link speed | |
| Target provider / DC / endpoint | |
| Ping summary | |
| Traceroute notes | |
| HTTP result | |
| iperf results | |
| Interpretation | |
| Verdict | |

Provider-specific numbers belong in **case evidence** documents under `assets/`.

---

## 8. Related documents

- [VPS-PROVIDER-SELECTION-RUNBOOK-v1.md](VPS-PROVIDER-SELECTION-RUNBOOK-v1.md)  
- [VPS-PROCUREMENT-GATE-v1.md](VPS-PROCUREMENT-GATE-v1.md)  
- Server B evidence: [assets/SERVER-B-PLANNING/SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md](assets/SERVER-B-PLANNING/SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md)  

---

*Network Preflight Runbook v1 · measurement discipline · no endpoints hard-coded.*
