# Research Backlog v1 — MCA-VPN-001 / Server B / Resilience Map

**Status:** EXTRACTED FROM LEGACY HANDOFF — **NOT RESEARCHED IN THIS WAVE**  
**Mark every item:** `CURRENT WEB RESEARCH REQUIRED`

No web research, provider contact, or procurement in Phase 1B-0.

---

## Provider and platform

| Item | Legacy context | Research status |
|------|----------------|-----------------|
| VEESP current products / limitations | Existing provider for A + n8n VPS | **CURRENT WEB RESEARCH REQUIRED** |
| VEESP snapshot / backup capabilities | Operator believed absent — unverified | **CURRENT WEB RESEARCH REQUIRED** |
| Independent alternatives to VEESP | Desired for failure-domain separation | **CURRENT WEB RESEARCH REQUIRED** |
| Provider ownership / AS / upstream diversity | Resilience objective | **CURRENT WEB RESEARCH REQUIRED** |
| Payment methods | — | **CURRENT WEB RESEARCH REQUIRED** |
| VPN / proxy / abuse policies | — | **CURRENT WEB RESEARCH REQUIRED** |
| Anti-DDoS offerings | — | **CURRENT WEB RESEARCH REQUIRED** |
| Traffic limits / port restrictions | — | **CURRENT WEB RESEARCH REQUIRED** |
| Pricing (current) | Old tariffs must not be reused | **CURRENT WEB RESEARCH REQUIRED** |

---

## Regional options (planning map)

| Role | Locations discussed | Research status |
|------|---------------------|-----------------|
| MAIN | Finland, Netherlands | **CURRENT WEB RESEARCH REQUIRED** |
| WEB MASK | France | **CURRENT WEB RESEARCH REQUIRED** |
| GEO FALLBACK 1 | UAE (preferred first) | **CURRENT WEB RESEARCH REQUIRED** |
| GEO FALLBACK 2 | Serbia | **CURRENT WEB RESEARCH REQUIRED** |
| Exploratory | Uzbekistan, Tajikistan | **CURRENT WEB RESEARCH REQUIRED** |
| Russian reachability | Operator concern | **CURRENT WEB RESEARCH REQUIRED** |
| VPN/proxy blocking environment | Regulatory / ISP patterns | **CURRENT WEB RESEARCH REQUIRED** |

---

## Software stack (current stable)

| Item | Legacy last-known | Research status |
|------|-----------------|-----------------|
| 3X-UI current stable release | Historical 3.4.1 on A | **CURRENT WEB RESEARCH REQUIRED** |
| Xray current stable release | Historical 26.6.22 | **CURRENT WEB RESEARCH REQUIRED** |
| Reality current recommendations | Legacy direction on A | **CURRENT WEB RESEARCH REQUIRED** |
| WS/TLS current viability | Future mask node | **CURRENT WEB RESEARCH REQUIRED** |
| Chrome fingerprint / TCP-RAW reports | Mentioned in legacy news context | **CURRENT WEB RESEARCH REQUIRED** |
| Ubuntu supported baseline | 22.04.5 on A | **CURRENT WEB RESEARCH REQUIRED** (24.04 vs 22.04) |
| 3X-UI upgrade/migration behaviour | Incident association uncertain | **CURRENT WEB RESEARCH REQUIRED** |
| Certificate renewal best practices | Renewal on A SAFE UNKNOWN | **CURRENT WEB RESEARCH REQUIRED** |

---

## Server A live verification (Phase 1B-1 — not web research)

These are **read-only live intake**, not web research — listed for completeness:

| Item | Status |
|------|--------|
| Firewall effective state | LIVE VERIFY REQUIRED |
| fail2ban | LIVE VERIFY REQUIRED |
| SSH auth policy | LIVE VERIFY REQUIRED |
| Docker usage | LIVE VERIFY REQUIRED |
| nginx installed on A? | LIVE VERIFY REQUIRED |
| certbot renewal timers | LIVE VERIFY REQUIRED |
| Backup checksums / local copy | LIVE VERIFY REQUIRED |

---

## Research execution gate

| Phase | Action |
|-------|--------|
| **Phase 1B-1** | Server A read-only live reconciliation (no mutation) |
| **Phase 2** | Execute this backlog — web research + operator review |
| **Phase 3+** | Server B implementation charter only after research + approval |

---

## Related documents

- [SERVER-B-CLONE-BASELINE-v1.md](SERVER-B-CLONE-BASELINE-v1.md)
- [CURRENT-STATE-RECONCILIATION-v1.md](CURRENT-STATE-RECONCILIATION-v1.md)

---

*Research Backlog v1 · deferred · CURRENT WEB RESEARCH REQUIRED.*
