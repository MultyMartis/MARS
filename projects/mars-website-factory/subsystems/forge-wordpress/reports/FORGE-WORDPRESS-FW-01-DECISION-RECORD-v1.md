# Forge WordPress — FW-01 Decision Record v1

**Document type:** Stage decision summary  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-01 — **COMPLETE**

---

## 1. Decisions accepted

| # | Decision | Document |
|---|----------|----------|
| 1 | Ten-layer architecture L1–L10 with spec-first L7 gate | [FORGE-WORDPRESS-ARCHITECTURE-v1.md](../FORGE-WORDPRESS-ARCHITECTURE-v1.md) |
| 2 | FWP-01–FWP-12 lifecycle with blocking gates G1–G10 | [FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md](../FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md) |
| 3 | Mode A default; B/C/D exception paths | [FORGE-WORDPRESS-IMPLEMENTATION-MODES-v1.md](../FORGE-WORDPRESS-IMPLEMENTATION-MODES-v1.md) |
| 4 | Theme vs functionality separation with proportionality | [FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md](../FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md) §4.1 |
| 5 | Per-project classic/hybrid/block — no global FSE default | §4.2 |
| 6 | ACF **preferred**, not mandatory | §4.3 |
| 7 | Mandatory Git for code, schema, specs, validation | §4.4 |
| 8 | Local/DEV implementation; WPilot production ops | §4.5 |
| 9 | Curated editor default | §4.6 |
| 10 | WV0–WV9 separate from Factory VL | [FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md](../FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md) |
| 11 | Minimal role model; no agent registration | [FORGE-WORDPRESS-ROLE-AND-AGENT-MODEL-v1.md](../FORGE-WORDPRESS-ROLE-AND-AGENT-MODEL-v1.md) |
| 12 | Three handoff boundaries B1–B3 | [FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md](../FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md) |
| 13 | Research adapted via classification register | [FORGE-WORDPRESS-RESEARCH-ADAPTATION-REGISTER-v1.md](../FORGE-WORDPRESS-RESEARCH-ADAPTATION-REGISTER-v1.md) |
| 14 | nineteen core project artifacts defined | [FORGE-WORDPRESS-PROJECT-ARTIFACT-MODEL-v1.md](../FORGE-WORDPRESS-PROJECT-ARTIFACT-MODEL-v1.md) |

---

## 2. Decisions deferred

| # | Topic | Target stage |
|---|-------|--------------|
| 1 | Handoff contract text (B1, B3) | **FW-02** |
| 2 | Artifact templates | **FW-02** |
| 3 | ACF / Theme / Plugin coding standards | **FW-02** |
| 4 | Local WordPress stack selection | **FW-03** |
| 5 | Validation runner scripts | **FW-03** |
| 6 | Agent promotion (`AG-WP-001`) | **FW-05** charter |
| 7 | FP-0002 pilot authorization | **FW-04** |
| 8 | WordPress Abilities/MCP integration | **FW-03+** |
| 9 | Repo layout standard (mono vs split) | **FW-02** |
| 10 | WV8 blocking thresholds | **FW-02** Validation Standard |

---

## 3. Rejected approaches

| Approach | Reason |
|----------|--------|
| Page builders as Factory-native | Breaks Gulp pipeline ownership |
| Autonomous production deploy | MARS execution model |
| Mandatory Docker/enterprise CI | Unproven operator need |
| Headless as Mode A default | WPilot + hosting alignment |
| Agent army | Minimal model adopted |
| Runtime / implementation in FW-01 | Stage boundary |

---

## 4. Open questions

| # | Question | Owner |
|---|----------|-------|
| 1 | Exact WPilot package format for Factory-native theme | FW-02 + WPilot sync |
| 2 | FP-0002 frontend readiness at WordPress intake | Factory VL + FW-04 |
| 3 | ACF Pro licensing across projects | Operator |
| 4 | Shared hosting plugin allowlist | FW-02 Plugin Governance |
| 5 | Playground vs Local WP as FW-03 default on Windows | FW-03 |

---

## 5. Consequences

| Area | Consequence |
|------|-------------|
| **Lifecycle** | Remains **FOUNDATION** — architecture documented, not operational |
| **Website Factory** | Layer §9 candidate formalized; VL/WV orthogonality explicit |
| **WPilot** | Downstream consumer role unchanged; handoff contract pending |
| **AG-WP-001** | Stays internal seed |
| **Operators** | Must complete FW-02 contracts before pilot intake |

---

## 6. Next required documents (FW-02)

See [FORGE-WORDPRESS-FW-02-CONTRACTS-AND-STANDARDS-INPUT-v1.md](FORGE-WORDPRESS-FW-02-CONTRACTS-AND-STANDARDS-INPUT-v1.md).

---

## 7. Impact on FW-02

FW-02 must convert FW-01 methodology into **enforceable contracts and standards** — handoff, content modeling, theme/plugin, validation, artifact templates.

---

## 8. Impact on FP-0002

| Aspect | FW-01 impact |
|--------|--------------|
| Implementation | **NOT authorized** |
| Probable mode | Mode A candidate when frontend ready |
| Eligibility | **SAFE UNKNOWN** — FW-04 pilot intake |
| Frontend | **Unchanged** by FW-01 |

---

## Status after FW-01

```text
FW-00 — COMPLETE
FW-01 — COMPLETE
FW-02 — NEXT
Architecture: DOCUMENTED
Methodology: BASELINE v1
Implementation capability: NOT STARTED
```

---

*FW-01 decision record v1.*
