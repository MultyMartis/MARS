# Production Plan — Корво Неро v1

**Operating model:** FULL-SERVICE CLUSTERED SEARCH CAMPAIGN  
**No client questionnaire gate**

---

## Stage 2A — COMPLETE (this task)

| Deliverable | Status |
|-------------|--------|
| Operator scope correction | ✓ |
| Full-service charter | ✓ |
| Service-to-cluster inventory | ✓ |
| Campaign architecture (8 campaigns, 48 groups) | ✓ |
| Ad group registry JSON | ✓ |
| Keyword production boundary | ✓ |
| Negative keyword architecture | ✓ |
| Conflict-negative matrix | ✓ |
| Bidding model T1–T4 | ✓ |
| URL/landing map (31 pages) | ✓ |
| Direct Commander format contract | ✓ |
| Triumph pattern audit | ✓ |
| Landing document contract | ✓ |
| Ad production contract | ✓ |

---

## Stage 2B — Ads, negatives, bids, URLs, UTM

| # | Task | Output |
|---|------|--------|
| 1 | Full keyword assignment script | `keyword-production-registry-v1.json` |
| 2 | Expand phrases per group (15–25 T1) | Updated `ad-group-registry-v1.json` |
| 3 | Write 48–96 ads | `ad-copy-registry-v1.json` |
| 4 | Finalize group + campaign negatives | Negatives embedded in registry |
| 5 | Compute phrase-level bids | Bid fields per tier rules |
| 6 | Append UTM to all URLs | Validated link set |

**Gate:** Human review of ad copy — no launch.

---

## Stage 2C — Direct Commander XLSX

| # | Task | Output |
|---|------|--------|
| 1 | Fork Triumph template v1 → corvonero template | `assets/direct-commander-template/` |
| 2 | Adapt sheet1-patch exporter OR manual validated export | `output/corvonero-commander-v1.xlsx` |
| 3 | Run duplicate-ads + launch-ready validation | Validation report |
| 4 | Cross-negative matrix applied in col 68 | Verified |

**Gate:** Import-ready claim only after validation pass.

---

## Stage 2D — Import validation + instructions

| # | Task | Output |
|---|------|--------|
| 1 | Template diff audit vs Commander UI | Diff report |
| 2 | Commander import checklist (adapt v1.4) | `commander-import-checklist-v1.md` |
| 3 | Human import dry-run | Import observations log |

---

## Stage 3 — Landing copy

| # | Task | Output |
|---|------|--------|
| 1 | Generate 31 × `.md` landing specs | `landing-copy/` |
| 2 | Generate 31 × `.docx` for Roman | Same folders |
| 3 | Roman builds Tilda pages | External — not ORCA |

**Order:** P1 pages first (see landing document contract).

---

## Stage 4 — Launch (NOT AUTHORIZED)

- Metrika goals — SAFE UNKNOWN  
- Call tracking — SAFE UNKNOWN  
- Daily budget split — human operator  
- Campaign go-live — explicit operator authorization required

---

## Dependencies

```text
MIG (complete) → 2A (complete) → 2B → 2C → 2D → Stage 3 landings → Launch gate
```

---

## Next production task

**Stage 2B:** Full keyword assignment + ad copy for 48 groups per [ad-production-contract-v1.md](ad-production-contract-v1.md).
