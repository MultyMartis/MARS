# Server B Clone Baseline v1 — MCA-VPN-001 → Future Independent VPN

**Status:** PLANNING BRIDGE — Server B **does not exist yet**  
**Not:** a Server B passport, provider selection, or implementation charter

---

## Goal

Build a **second independent VPN VPS (Server B)** without disturbing **Server A (MCA-VPN-001)**.

Architectural principle:

```text
Server A and Server B are independent.
No A → B dependency.
No shared DB, private keys, certificates, credentials, or control plane.
```

Initial client strategy: **manual profile switching** between Server A and Server B profiles.

---

## CLONE AS CONCEPT (reuse patterns, not identities)

| Item | Clone? |
|------|--------|
| Dedicated VPN-only role | YES |
| Workload separation from n8n/apps | YES |
| 3X-UI / Xray management model (if research still supports) | YES — conceptually |
| VLESS / Reality compatibility direction | YES — subject to current research |
| Client A/B profile compatibility | YES |
| HTTPS management panel | YES |
| Backup-before-change discipline | YES |
| Inventory / passport / recovery documentation pattern | YES |
| systemd-style service supervision | YES — conceptually |
| Independent off-server backup | YES |
| Non-default protected panel endpoint | YES — conceptually |

---

## GENERATE NEW (mandatory for Server B)

| Item | New value required |
|------|-------------------|
| Provider / failure domain | YES — prefer independent from VEESP |
| Public IP | YES |
| Domain | YES |
| Hostname | YES |
| SSH credentials / keys | YES |
| TLS certificate + private key | YES |
| 3X-UI admin credentials | YES |
| Panel base path | YES |
| Xray client UUID(s) | YES |
| Reality keypair | YES |
| Reality ShortID | YES |
| Subscription secrets | YES if used |
| Client profiles / configs | YES — built for B |
| Backup identity / encryption key | YES or managed vault |
| Server-specific DNS records | YES |
| Provider metadata | YES |

---

## DO NOT CLONE

| Item | Reason |
|------|--------|
| Stale 3X-UI DB wholesale | Carries old clients/secrets/state |
| Old panel path | Security through obscurity + compromise domain |
| Old passwords | Independent compromise domain |
| TLS private keys from A | Cryptographic identity must be new |
| Reality private key | Never clone |
| Temporary repair directories | Noise |
| Old logs / package cache | Not portable value |
| Accidental 443/2096 incident panel state | Bad known state |
| Assumptions about `/usr/local/x-ui/web` | Disproved hypothesis |
| Server-specific network/firewall state | Environment-specific |
| Historical troubleshooting hacks | — |
| Version 3.4.1 merely because historical | Research current stable |
| `/etc/letsencrypt` identity from A | Domain/server bound |

---

## MUST RESEARCH (before procurement/build)

All items: **CURRENT WEB RESEARCH REQUIRED** — not performed in Phase 1B-0.

| Area | Topics |
|------|--------|
| Provider | VEESP limits; independent alternatives; snapshots |
| Location | Finland, Netherlands, France, UAE, Serbia; reachability from RU |
| OS baseline | Supported Ubuntu LTS (22.04 vs 24.04) |
| Software | Current stable 3X-UI, Xray, Reality recommendations |
| Security | Firewall baseline; panel exposure strategy |
| Transport | WS/TLS/nginx relevance for **separate** mask node — not mandatory on B |
| Operations | Backup/restore proof; provider abuse/VPN policy |
| Economics | Current pricing — do not reuse stale tariffs |

See [RESEARCH-BACKLOG-v1.md](RESEARCH-BACKLOG-v1.md).

---

## Target architecture (conceptual)

```
Client Device
  ├── Profile A → Server A (existing MCA-VPN-001)
  └── Profile B → Server B (new)

Server A ──X── Server B   (no dependency)

Optional future:
  Web Mask node (WS/TLS/nginx) — independent third VPS
  GEO nodes — independent failure domains
```

---

## Implementation gate

Server B build requires **explicit implementation charter** after:

1. Phase 1B-1 — Server A read-only live reconciliation  
2. Phase 2 — current provider/architecture research  
3. Operator approval of provider, region, and design

**Do not create Server B asset folder with factual passport until B exists.**

---

## Related documents

- [SERVER-A-LEGACY-PASSPORT-v1.md](SERVER-A-LEGACY-PASSPORT-v1.md)
- [RESEARCH-BACKLOG-v1.md](RESEARCH-BACKLOG-v1.md)
- [CLIENT-COMPATIBILITY-v1.md](CLIENT-COMPATIBILITY-v1.md)

---

*Server B Clone Baseline v1 · planning only · B is hypothetical.*
