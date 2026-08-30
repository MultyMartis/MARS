# Server B Provisioning Intake Checklist v1

**Status:** **PREPARED** — awaiting operator AdminVPS provisioning  
**Wave:** MARS Server Ops Phase 3A + Provider Selection Intelligence  
**Use:** Collect facts **immediately after** operator creates the AdminVPS Finland VPS  
**Stop rule:** Stop **before** manual application configuration (3X-UI, Xray, DNS beyond provider defaults)

**Current procurement authority:** [SERVER-B-PROVIDER-DECISION-v2.md](SERVER-B-PROVIDER-DECISION-v2.md)  
**Historical (SUPERSEDED):** [PROCUREMENT-DECISION-v1.md](PROCUREMENT-DECISION-v1.md) — UpCloud

---

## 1. Intake gate

| Gate | Required |
|------|----------|
| Current procurement decision frozen | [SERVER-B-PROVIDER-DECISION-v2.md](SERVER-B-PROVIDER-DECISION-v2.md) — **YES** (AdminVPS) |
| Architecture freeze recorded | [ARCHITECTURE-FREEZE-v1.md](ARCHITECTURE-FREEZE-v1.md) — **YES** |
| Network preflight | [SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md](SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md) — **PASS** (pre-purchase) |
| Server B provisioned in AdminVPS | **NO** — operator action pending |
| Application stack configured | **NO** — out of scope for this checklist wave |

---

## 2. PUBLIC / SANITIZED FACTS

Record in Git-safe documents and inventory after operator attestation.

| # | Field | Value | Status |
|---|-------|-------|--------|
| 1 | Provider | AdminVPS (expected) | ☐ |
| 2 | Location / network | Finland / Helsinki / FI1 (expected preferred) | ☐ |
| 3 | Plan name | Micro (expected) | ☐ |
| 4 | OS image | Ubuntu 24.04 LTS clean (expected) | ☐ |
| 5 | vCPU count | 2 (expected) | ☐ |
| 6 | RAM | 4 GB (expected) | ☐ |
| 7 | Storage size | **as shown at checkout** — confirm; do not invent | ☐ |
| 8 | Public IPv4 | | ☐ NOT YET ASSIGNED |
| 9 | Public IPv6 | | ☐ NOT YET ASSIGNED |
| 10 | Initial hostname | | ☐ NOT YET ASSIGNED |
| 11 | Provider server identifier | | ☐ NOT YET ASSIGNED |
| 12 | Creation timestamp (UTC) | | ☐ NOT YET ASSIGNED |
| 13 | Console access available | yes / no / SAFE UNKNOWN | ☐ |
| 14 | Provider backup / snapshot state | enabled / disabled / SAFE UNKNOWN | ☐ |
| 15 | Provider firewall state | enabled / disabled / default / SAFE UNKNOWN | ☐ |
| 16 | Domain intended (DNS not mutated here) | `metacode-cloud.com` | ☐ registered — DNS pending separate charter |

**Git policy for IPs:** Record per programme IP policy — omit from Git if operator directs local-only; use `ip_ref` in inventory if needed.

**Post-provision network:** After facts above, repeat network tests against **assigned IP** per [../../VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md](../../VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md) Stage 10.

---

## 3. LOCAL-ONLY SECRET FACTS

Record **only** in:

```text
X:\AI MARS\local\infrastructure\SERVER-B-PLANNING\secrets.local.md
```

Do **not** commit values. Do **not** create secret files in this documentation wave — this section defines what to collect **after** provisioning.

| # | Field | Collected | secret_ref section |
|---|-------|-----------|-------------------|
| 1 | Initial SSH method (password / key / console) | ☐ | Provider bootstrap |
| 2 | Initial root or bootstrap password (if applicable) | ☐ | Provider bootstrap |
| 3 | Initial SSH key (if provider-injected) | ☐ | SSH |
| 4 | Provider API token reference (if used) | ☐ | Provider |
| 5 | Emergency console credentials reference | ☐ | Provider |

---

## 4. Post-intake actions (deferred — not this wave)

After sanitized facts are returned to MARS:

1. Update [IDENTITY-AND-SECRETS-CHECKLIST-v1.md](IDENTITY-AND-SECRETS-CHECKLIST-v1.md) statuses (still no secret values in Git).  
2. Consider inventory row in [../../SERVER-INVENTORY-v1.md](../../SERVER-INVENTORY-v1.md) — **only after** operator assigns `inventory_ref` / MCA asset ID if applicable.  
3. Plan Phase 3B+ implementation charter — SSH hardening, 3X-UI install, transport config.  
4. **Do not** mutate Server A.

---

## 5. Operator return format

When provisioning completes, operator provides:

**Sanitized (Git-safe):**

- Provider, location/network, plan, OS, resources (including **confirmed** disk)  
- Public IPv4/IPv6 (per IP policy)  
- Hostname, server identifier, creation timestamp  
- Console / backup / firewall state observations  
- Post-provision ping/iperf summary if already measured  

**Local-only:**

- Bootstrap credentials and SSH material → `secrets.local.md`  
- Any provider panel export → Storage `incoming\` if large  

Then **stop** — no 3X-UI, Xray, DNS, or TLS setup until next chartered wave.

---

## 6. Validation (intake completeness)

| Check | Expected |
|-------|----------|
| Server B not falsely marked provisioned before facts exist | ☐ |
| No invented IP, UUID, or disk size | ☐ |
| No credentials in Git commit | ☐ |
| Server A untouched | ☐ |
| Procurement state remains APPROVED / NOT YET PROVISIONED until facts attested | ☐ |

After successful intake attestation, update procurement state to **PROVISIONED — APPLICATION NOT CONFIGURED** in a future wave (not automatic here).

---

## 7. Related documents

- [SERVER-B-PROVIDER-DECISION-v2.md](SERVER-B-PROVIDER-DECISION-v2.md)
- [PROCUREMENT-DECISION-v1.md](PROCUREMENT-DECISION-v1.md) — SUPERSEDED
- [ARCHITECTURE-FREEZE-v1.md](ARCHITECTURE-FREEZE-v1.md)
- [IDENTITY-AND-SECRETS-CHECKLIST-v1.md](IDENTITY-AND-SECRETS-CHECKLIST-v1.md)
- [SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md](SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md)
- [../MCA-VPN-001/LIVE-INTAKE-CHECKLIST-v1.md](../MCA-VPN-001/LIVE-INTAKE-CHECKLIST-v1.md) — pattern reference for Server A

---

*Provisioning Intake Checklist v1 · prepared · awaiting AdminVPS create.*
