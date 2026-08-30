# VPS Provider Requirement Intake v1

**Programme:** MARS Server Ops & VPS Forge  
**Stage:** 0 — OPERATOR REQUIREMENT INTAKE  
**Status:** **BASELINE v1** — reusable intake model  
**Not:** filled questionnaire product, CRM, or automated eligibility checker

---

## 1. Purpose

Before searching providers, establish what the server is **actually for**.

Agents must complete this intake (or reuse safely available MARS context) **before** country ranking or provider long-listing.

---

## 2. Sanitization rule

| Allowed in Git | Forbidden / local-only |
|----------------|------------------------|
| Sanitized operational region (e.g. “operator jurisdiction: RU”) | Exact home address, passport data, full personal identity dumps |
| ISP class / network class (e.g. home Ethernet, mobile) | Payment card numbers, account credentials |
| Required service names (OpenAI, Cursor, …) | Secrets, API keys, panel passwords |

Use only **sanitized operational facts** in canonical documentation.

---

## 3. Question categories

Complete only categories relevant to the task.

### 3.1 Workload

Mark applicable roles:

| Item | Applicable? | Notes |
|------|-------------|-------|
| VPN | ☐ | |
| Xray | ☐ | |
| 3X-UI | ☐ | |
| WireGuard | ☐ | |
| Reverse proxy | ☐ | |
| Websites | ☐ | |
| Docker | ☐ | |
| n8n | ☐ | |
| PostgreSQL | ☐ | |
| AI / API traffic | ☐ | |
| Development | ☐ | |
| Production | ☐ | |
| Backup node | ☐ | |
| Monitoring | ☐ | |
| Mixed workload | ☐ | |

### 3.2 Client location (sanitized)

| Field | Value (sanitized) | Status |
|-------|-------------------|--------|
| Operator physical region / country | | |
| Actual networks used | | |
| Home ISP (label only) | | |
| Mobile networks if relevant | | |
| Expected client geography | | |

### 3.3 Service compatibility

What external services must work **through** the server?

| Service / class | Required? | Current country support status | Evidence / reverify date |
|-----------------|-----------|--------------------------------|--------------------------|
| OpenAI / ChatGPT | ☐ | | |
| Cursor / model providers via Cursor | ☐ | | |
| Anthropic | ☐ | | |
| Google services | ☐ | | |
| GitHub | ☐ | | |
| Telegram | ☐ | | |
| Required APIs | ☐ | | |
| Target websites | ☐ | | |

**Rule:** Do not assume country compatibility. Current availability/compliance must be researched when time-sensitive. Mark stale rows **REVERIFY AT NEXT PROCUREMENT**.

### 3.4 Performance

| Dimension | Target / constraint | Priority |
|-----------|---------------------|----------|
| Latency | | |
| Throughput | | |
| Concurrent users | | |
| Monthly traffic | | |
| CPU | | |
| RAM | | |
| Disk (size / performance) | | Confirm at checkout — do not invent |
| IPv4 | | |
| IPv6 | | |

### 3.5 Resilience / failure domain

| Question | Answer |
|----------|--------|
| Primary node? | |
| Secondary node? | |
| Different provider required? | |
| Different ASN required? | |
| Different country required? | |
| Different DNS/domain failure domain? | |
| Independent payment / control plane required? | |
| Existing node to separate from (inventory_ref) | |

### 3.6 Access / recovery

| Capability | Required? | Notes |
|------------|-----------|-------|
| Emergency console | ☐ | |
| Rescue mode | ☐ | |
| Snapshots | ☐ | |
| Provider backup | ☐ | |
| Reinstall | ☐ | |
| IP replacement | ☐ | |
| Reverse DNS | ☐ | |

### 3.7 Payment / compliance

| Field | Constraint |
|-------|------------|
| Operator / customer jurisdiction constraints | |
| Card / payment path requirements | |
| Sanctions / compliance notes (sanitized) | |
| Provider must accept customer from actual operator location | **YES / NO / UNKNOWN** |
| Identity verification requirements | |

**Never suggest falsifying** country, address, residency, company identity, or payment origin.

---

## 4. Output of Stage 0

Hand-off to Stage 1 ([normalization](VPS-PROVIDER-SELECTION-RUNBOOK-v1.md)):

1. Filled (or context-derived) answers for relevant categories  
2. Explicit list of **open questions** for the operator  
3. Explicit list of **time-sensitive** items requiring re-check  

---

## 5. Related documents

- [VPS-PROVIDER-SELECTION-RUNBOOK-v1.md](VPS-PROVIDER-SELECTION-RUNBOOK-v1.md)  
- [VPS-PROVIDER-RESEARCH-SCORECARD-v1.md](VPS-PROVIDER-RESEARCH-SCORECARD-v1.md)  
- [SECRET-HANDLING-MODEL-v1.md](SECRET-HANDLING-MODEL-v1.md)  

---

*Requirement Intake v1 · Stage 0 · no provider recommendation implied.*
