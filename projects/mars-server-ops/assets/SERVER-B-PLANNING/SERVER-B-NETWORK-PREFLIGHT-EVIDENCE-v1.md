# Server B Network Preflight Evidence v1

**Planning locus:** `SERVER-B-PLANNING`  
**Provider under test:** AdminVPS  
**Status:** **PRE-PURCHASE EVIDENCE RECORDED** — operator-observed  
**Not:** post-provision verification; not continuous monitoring  
**Generic procedure:** [../../VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md](../../VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md)

---

## 1. Scope

Records operator-observed **pre-purchase** network evidence for Server B provider selection.

Assigned Server B IP: **NOT YET ASSIGNED** — Stage 10 not applicable yet.

---

## 2. Local workstation link context

| Adapter | Reported LinkSpeed | Interpretation |
|---------|-------------------|----------------|
| Physical Ethernet | **100 Mbps** | Practical local ceiling |
| Virtual Xray TUN | **100 Gbps** (reported) | **Not** a physical link speed |

**Interpretation rule applied:** iperf results near ~87–92 Mbit/s are consistent with a **100 Mbps physical Ethernet** ceiling — do **not** attribute that ceiling to FI1 without further evidence.

---

## 3. Finland — AdminVPS / Helsinki / FI1

### 3.1 Ping

| Metric | Observed |
|--------|----------|
| Average RTT | approximately **71 ms** |
| Observed range | approximately **71–78 ms** |
| Packet loss | **0%** |

### 3.2 Route

Direct operator ISP path through Russian transit toward Finland (operator-observed shape). Intermediate non-responsive hops: do **not** auto-classify as packet loss.

### 3.3 HTTP 100 MB test

| Metric | Observed |
|--------|----------|
| Throughput | approximately **18.63 Mbit/s** |

**Important:** Do **not** interpret this HTTP result as the final network ceiling.

### 3.4 iperf3 — FI1

| Mode | Observed |
|------|----------|
| Single-stream upload | approximately **91.7 Mbit/s** sender |
| 4-stream upload | approximately **88.0 Mbit/s** sender; approximately **82.4 Mbit/s** receiver |
| 4-stream reverse / download | approximately **87.1 Mbit/s** receiver |
| TCP test endpoint | **Reachable** |

Provider-specific endpoint hostnames/ports: retained in operator test notes / local evidence if needed — **not** hard-coded into the generic runbook.

---

## 4. Germany (comparison)

| Metric | Observed |
|--------|----------|
| Ping average | approximately **97 ms** |
| Packet loss | **0%** |
| HTTP 100 MB | approximately **4.54 Mbit/s** |

**Result:** Materially **worse** than Finland in the observed test window.

---

## 5. Netherlands (control)

| Check | Observed |
|-------|----------|
| Ping endpoint | **No ICMP replies** observed |
| HTTP endpoint | **Connection failed** |

**Do not claim** the entire Netherlands provider location is unavailable from this alone.

**Geography note:** Netherlands is **not desired** for Server B failure-domain geography because Server A is already VEESP Amsterdam.

---

## 6. Pre-purchase network verdict

```text
ADMINVPS FINLAND / HELSINKI / FI1
PRE-PURCHASE NETWORK VERDICT: APPROVED
```

**Evidence basis:**

- Low/stable RTT for operator route  
- 0% observed ping loss  
- iperf throughput close to local 100 Mbps Ethernet ceiling  
- Materially better observed results than Germany  
- Appropriate geographic separation from Server A  

**Explicitly not yet:**

```text
POST-PROVISION VERIFIED
```

The assigned Server B IP must still be tested after purchase.

---

## 7. Related documents

- [SERVER-B-PROVIDER-DECISION-v2.md](SERVER-B-PROVIDER-DECISION-v2.md)  
- [SERVER-B-PROVIDER-SELECTION-CASE-v1.md](SERVER-B-PROVIDER-SELECTION-CASE-v1.md)  
- [../../VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md](../../VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md)  

---

*Network Preflight Evidence v1 · pre-purchase only · Server B not provisioned.*
