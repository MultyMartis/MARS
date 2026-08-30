# Server B Identity & Secrets Checklist v1

**Status:** **CHECKLIST ONLY** — all values **EMPTY / NOT YET ASSIGNED**  
**Wave:** MARS Server Ops Phase 3A  
**Rule:** **Never put secret values in Git**

---

## 1. Purpose

Enumerate every independent identity and secret Server B must receive **without cloning Server A**.

Each field records:

- **Status** — always `NOT YET ASSIGNED` until operator intake  
- **secret_ref** — future local-only storage pointer  
- **Git-safe note** — what may appear in sanitized docs later

Populate values only in:

```text
X:\AI MARS\local\infrastructure\SERVER-B-PLANNING\secrets.local.md
```

*(File does **not** exist in this wave — create at provisioning intake.)*

Bulk sensitive exports: `X:\AI MARS STORAGE\mars-server-ops\` per [../../STORAGE-MODEL-v1.md](../../STORAGE-MODEL-v1.md).

See [../../SECRET-HANDLING-MODEL-v1.md](../../SECRET-HANDLING-MODEL-v1.md).

---

## 2. Provider & infrastructure identity

| Field | Status | secret_ref (future) | Git-safe later |
|-------|--------|---------------------|----------------|
| UpCloud server ID / reference | NOT YET ASSIGNED | `local/infrastructure/SERVER-B-PLANNING/secrets.local.md` → Provider | Sanitized server ref label only |
| Public IPv4 | NOT YET ASSIGNED | same → Provider / Network | Optional per IP policy — prefer `ip_ref` |
| Public IPv6 | NOT YET ASSIGNED | same → Network | Optional per IP policy |
| Hostname | NOT YET ASSIGNED | same → Hostname | Sanitized hostname label |
| New independent domain | NOT YET ASSIGNED | same → DNS | Domain name (sanitized) |
| DNS records (A/AAAA/CNAME/etc.) | NOT YET ASSIGNED | same → DNS | Record types + names — not credentials |

---

## 3. Initial access & SSH

| Field | Status | secret_ref (future) | Git-safe later |
|-------|--------|---------------------|----------------|
| Initial provider credentials / reference | NOT YET ASSIGNED | same → Provider bootstrap | `SECRET_REFERENCE_PRESENT: yes` only |
| Operator sudo username | NOT YET ASSIGNED | same → SSH | Username label (non-secret) |
| SSH Ed25519 private key reference | NOT YET ASSIGNED | same → SSH → private key path | Key fingerprint only |
| SSH public key reference | NOT YET ASSIGNED | same → SSH → authorized_keys | Public key material (acceptable local) |

---

## 4. 3X-UI panel

| Field | Status | secret_ref (future) | Git-safe later |
|-------|--------|---------------------|----------------|
| 3X-UI admin username | NOT YET ASSIGNED | same → VPN / 3X-UI | Never in Git |
| 3X-UI admin password | NOT YET ASSIGNED | same → VPN / 3X-UI | Never in Git |
| Panel base path | NOT YET ASSIGNED | same → VPN / 3X-UI | Never in Git |
| Panel port | NOT YET ASSIGNED | same → VPN / 3X-UI | Port number may be sanitized post-build |

---

## 5. TLS

| Field | Status | secret_ref (future) | Git-safe later |
|-------|--------|---------------------|----------------|
| TLS private key | NOT YET ASSIGNED | same → TLS | Never in Git |
| TLS certificate (fullchain) | NOT YET ASSIGNED | same → TLS | Expiry/issuer may be sanitized |

---

## 6. VLESS / WebSocket (primary initial transport)

| Field | Status | secret_ref (future) | Git-safe later |
|-------|--------|---------------------|----------------|
| VLESS client UUID / identity | NOT YET ASSIGNED | same → VPN / clients | Never in Git |
| WebSocket path | NOT YET ASSIGNED | same → VPN / transport | Never in Git |
| Inbound port (TLS/WS) | NOT YET ASSIGNED | same → VPN / transport | May sanitize post-build |

---

## 7. VLESS / Reality (secondary validation transport)

| Field | Status | secret_ref (future) | Git-safe later |
|-------|--------|---------------------|----------------|
| Reality private key | NOT YET ASSIGNED | same → VPN / Reality | Never in Git |
| Reality public key | NOT YET ASSIGNED | same → VPN / Reality | Derived — store with private |
| Reality ShortID | NOT YET ASSIGNED | same → VPN / Reality | Never in Git |
| Reality SNI (if applicable) | NOT YET ASSIGNED | same → VPN / Reality | Config-dependent |
| Reality target (if applicable) | NOT YET ASSIGNED | same → VPN / Reality | Config-dependent |
| Inbound port (Reality) | NOT YET ASSIGNED | same → VPN / Reality | May sanitize post-build |

**Independence rule:** Do **not** copy any Reality or TLS material from Server A (MCA-VPN-001).

---

## 8. Client / subscription

| Field | Status | secret_ref (future) | Git-safe later |
|-------|--------|---------------------|----------------|
| Subscription URL / token | NOT YET ASSIGNED | same → VPN / subscription | Never in Git |
| Client profile secrets | NOT YET ASSIGNED | same → VPN / clients | Never in Git |
| QR / import URI payloads | NOT YET ASSIGNED | same → VPN / clients | Never in Git |

---

## 9. Backup identity

| Field | Status | secret_ref (future) | Git-safe later |
|-------|--------|---------------------|----------------|
| Backup encryption key (if used) | NOT YET ASSIGNED | same → Backup | Never in Git |
| Backup manifest identity | NOT YET ASSIGNED | Storage path ref in Git | Manifest filename + checksum in evidence |

---

## 10. Clone prohibition (from Server A)

Do **not** reuse from MCA-VPN-001:

- Public IP, domain, hostname  
- SSH credentials or keys  
- TLS certificate / private key  
- 3X-UI admin credentials or panel path  
- Xray client UUIDs  
- Reality keypair, ShortIDs  
- Subscription / client secrets  
- Backup encryption identity  

See [../MCA-VPN-001/SERVER-B-CLONE-BASELINE-v1.md](../MCA-VPN-001/SERVER-B-CLONE-BASELINE-v1.md).

---

## 11. Completion criteria

This checklist is **complete for Phase 3A** when:

1. All fields exist with `NOT YET ASSIGNED` status.  
2. No secret values appear in Git.  
3. Operator provisioning intake can fill local-only references.

**Final MCA asset ID:** assign only via operator/registry authority after provisioning — until then, locus remains `SERVER-B-PLANNING`.

---

*Identity & Secrets Checklist v1 · fields only · no values · Phase 3A.*
