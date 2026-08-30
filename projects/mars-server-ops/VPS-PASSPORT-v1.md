# MARS Server Ops — VPS Passport v1

**Status:** **reusable template** — copy per server at intake  
**Not:** populated passport for any live server

**Rule:** Capabilities and sanitized metadata only — **no passwords, tokens, or private keys.**

---

## How to use

1. Copy this template to a server-specific file, e.g. `passports/<inventory_ref>-PASSPORT-v1.md` (future phase).  
2. Fill only **verified** facts; mark others **SAFE UNKNOWN**.  
3. Link secrets via `secret_ref` paths — never values.  
4. Update `last_verified` after each verification wave.

---

## Passport template

### Identity

| Field | Value |
|-------|-------|
| **passport_id** | *(assign at intake — e.g. PASS-SRV-OPS-001)* |
| **inventory_ref** | *(link to SERVER-INVENTORY row)* |
| **operator_name** | |
| **purpose** | *(one-line mission of this host)* |
| **production_criticality** | `prod` / `staging` / `dev` / `lab` / `UNKNOWN` |

### Provider & host

| Field | Value |
|-------|-------|
| **provider** | |
| **provider_account_ref** | *(local secret ref if needed — not value)* |
| **hostname_label** | |
| **public_domain_refs** | |
| **region_datacenter** | **SAFE UNKNOWN** if not verified |

### OS

| Field | Value |
|-------|-------|
| **os_family** | |
| **os_version** | |
| **kernel_notes** | **SAFE UNKNOWN** unless verified |
| **update_policy** | documented / ad-hoc / **UNKNOWN** |

### Criticality & consumers

| Field | Value |
|-------|-------|
| **criticality** | |
| **consumers** | *(programmes or services that depend on this host)* |
| **dependencies** | *(upstream DNS, Storage, other hosts)* |

### Domains & public services

| Domain / service | Exposure | Notes |
|------------------|----------|-------|
| *(none listed)* | | |

### Internal services

| Service | Role | Notes |
|---------|------|-------|
| *(none listed)* | | |

### Docker usage

| Field | Value |
|-------|-------|
| **docker_used** | yes / no / **UNKNOWN** |
| **compose_projects** | *(names only — no env values)* |
| **volume_notes** | **SAFE UNKNOWN** until mapped |

### Reverse proxy & TLS

| Field | Value |
|-------|-------|
| **reverse_proxy** | nginx / caddy / traefik / other / none / **UNKNOWN** |
| **tls_termination** | |
| **cert_management** | **SAFE UNKNOWN** |

### Databases

| Engine | Instance label | Role | Backup ref |
|--------|----------------|------|------------|
| *(none)* | | | |

### VPN role

| Field | Value |
|-------|-------|
| **vpn_role** | none / egress / full-tunnel / admin / **UNKNOWN** |
| **3x-ui_xray** | yes / no / **UNKNOWN** |
| **vpn_notes** | **SAFE UNKNOWN** |

### Access surfaces

| Surface | Available | Read | Change authorized | secret_ref |
|---------|-----------|------|-------------------|------------|
| Provider panel | **UNKNOWN** | | **NO** | |
| SSH | **UNKNOWN** | | **NO** | |
| SFTP | **UNKNOWN** | | **NO** | |
| VPN admin / 3X-UI | **UNKNOWN** | | **NO** | |
| Docker host | **UNKNOWN** | | **NO** | |
| Reverse proxy admin | **UNKNOWN** | | **NO** | |
| n8n | **UNKNOWN** | | **NO** | |
| PostgreSQL | **UNKNOWN** | | **NO** | |
| Monitoring | **UNKNOWN** | | **NO** | |
| DNS panel | **UNKNOWN** | | **NO** | |

*Detailed capability matrix: use [ACCESS-MODEL-v1.md](ACCESS-MODEL-v1.md) instance when created.*

### Firewall status

| Field | Value |
|-------|-------|
| **firewall_documented** | yes / no / **UNKNOWN** |
| **inbound_policy_summary** | **SAFE UNKNOWN** |
| **last_reviewed** | |

### Backup model

| Class | Frequency | Location ref | Restore tested |
|-------|-----------|--------------|----------------|
| *(none)* | | | |

See [BACKUP-RESTORE-MODEL-v1.md](BACKUP-RESTORE-MODEL-v1.md).

### Restore status

| Field | Value |
|-------|-------|
| **restore_strategy_documented** | yes / no |
| **last_restore_test** | **NONE** / date |
| **restore_notes** | |

### Monitoring

| Field | Value |
|-------|-------|
| **monitoring** | none / manual / external / **UNKNOWN** |
| **healthchecks_documented** | yes / no |
| **alerting** | **SAFE UNKNOWN** |

### Risk notes

| Risk | Mitigation | Owner |
|------|------------|-------|
| *(none)* | | |

### Evidence

| Ref | Description |
|-----|-------------|
| *(none)* | |

### SAFE UNKNOWN summary

List fields not yet verified:

- *(all fields default UNKNOWN until Phase 1B intake)*

### Last verified

| Field | Value |
|-------|-------|
| **last_verified** | |
| **verified_by** | |
| **verification_method** | read-only charter id / operator attestation |

---

## Prohibited fields

Never include in a passport (Git or Storage without encryption charter):

- passwords  
- private SSH keys  
- API tokens / bot tokens  
- raw DSN with credentials  
- n8n credential export JSON  
- private TLS keys  
- VPN client private configs with sensitive client data  

Use `secret_ref` only, e.g.:

```text
secret_ref: local/infrastructure/<passport-id>/secrets.local.md → SSH section
```

---

*VPS Passport v1 · template · Phase 1A.*
