# Incoming Hybrid Alignment v1

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 2B  
**Upstream:** [incoming-deep-review-v2.md](../discoveries/incoming-deep-review-v2.md), Wave 2A [incoming-readme-v1.md](incoming-readme-v1.md)  
**Architect decision:** **Hybrid model** — Active Incoming in Active Brain; Historical Bulk toward Storage Layer (documentation only; **no moves**)

---

## Hybrid model (normative documentation)

| Layer | Scope | What lives here |
|-------|-------|-----------------|
| **Active Incoming** | **Active Brain** (`C:\AI MARS`) | Operational drop zones (`incoming/mig/`), active stubs, small pending triage |
| **Historical Bulk** | **Storage Layer** (`C:\AI MARS STORAGE\…`, Cold Brain) | Retired raw packs, superseded exports, large legal ZIPs **after** operator triage sign-off |

**Rule:** `incoming/` at repo root is **not** long-term bulk storage. Promotion → `projects/*`; retirement → archive or Storage Layer — **operator-gated**, not Wave 2B execution.

---

## Actions taken

| Surface | Change |
|---------|--------|
| `incoming/README.md` | Hybrid model section (Active Incoming vs Historical Bulk) |
| `governance/ecosystem-topology-index.md` | `incoming/` topology node + hybrid placement |
| `governance/mars-reality-index-v0.md` | New § Incoming (hybrid) |

**Not done:** folder moves (N-02, W2-A08); migration plans; delete/archive execution.

---

## Contradictions corrected

| Prior read | Correction |
|------------|------------|
| “Active Brain = only trusted SoT” without intake | Active Brain **includes** untrusted **staging** under `incoming/` by charter |
| Incoming absent from topology | `incoming/` listed as ecosystem intake zone |
| Incoming vs archive conflated | README + topology: intake ≠ `archive/` |

---

## Files changed

- `incoming/README.md`
- `governance/ecosystem-topology-index.md`
- `governance/mars-reality-index-v0.md`

---

*Incoming hybrid alignment v1 — Wave 2B evidence.*
