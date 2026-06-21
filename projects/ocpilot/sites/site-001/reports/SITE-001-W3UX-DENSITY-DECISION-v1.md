# SITE-001 W3-UX Density Decision v1

**Type:** Post-discovery gate — W3-UX Density & Visual Effectiveness  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Audit input:** [SITE-001-W3UX-DENSITY-AUDIT-v1.md](SITE-001-W3UX-DENSITY-AUDIT-v1.md)

---

## Verdict

**DISCOVERY COMPLETE — READY FOR W3-UX EXECUTION CHARTER**

W3-UX density audit confirms operator diagnosis: **W3-V failed the perceptual bar** because spacing and hierarchy — not chrome — drive “empty catalog / weak cards” perception. Execution is **feasible CSS-first** with **optional minimal twig** (homepage map height, class hooks only). **No implementation authorized** in this document.

---

## Success criteria pre-check (discovery)

| # | Criterion | Discovery assessment |
|---|-----------|----------------------|
| 1 | More useful information on screen | **Achievable** — 15–20% card height ↓ → +1 catalog row desktop |
| 2 | Catalogs feel richer | **Achievable** — density + price hierarchy |
| 3 | Vehicle cards feel more valuable | **Achievable** — price/CTA dominance plan ready |
| 4 | Site feels less empty | **Achievable** — homepage −350–450 px first 2 screens |
| 5 | No functionality loss | **Achievable** — spacing/hierarchy only; forms/JS untouched |
| 6 | No SEO changes | **Achievable** — no route/content/meta edits in scope |

---

## Top 10 highest-impact density improvements

| Rank | ID | Improvement | Surfaces | Est. UX impact | Primary files |
|------|-----|-------------|----------|----------------|---------------|
| **1** | U-01 + U-11 | Remove used-card image top margin + cap image height (`object-fit`) | `/cars/`, home catalog | **Very High** — largest single card waste (~40–60 px) | `main.css`, `media.css` |
| **2** | U-07 + U-08 + U-09 | Price hierarchy: larger price, compact VIN, inline credit strip | Used cards, used PDP hero | **Very High** — “offer value” perception | `main.css` |
| **3** | P-U-05 + P-U-06 | Compress VIN check + credit calculator section margins/padding | Used PDP | **High** — ~110 px recoverable | `main.css` |
| **4** | H-01 + H-02 | Homepage hero `min-height` 600→440; slider content pad 50→32 | `/` | **High** — first screen **−120–180 px** | `main.css`, `media.css` |
| **5** | U-03–U-06 | Tighten card info padding and inter-block margins (used) | `/cars/`, home | **High** — ~35 px/card | `main.css` |
| **6** | P-N-01 + P-N-02 | New PDP hero box padding + car-media grid gap | `/auto/*` PDP | **High** — ~65–75 px hero/mosaic | `main.css` |
| **7** | N-01–N-03 | New catalog face padding + price/credit hierarchy | `/auto/` | **Medium–High** — “vehicle offer” vs OC tile | `main.css` |
| **8** | H-03 + H-04 | Section title margins 50→32; `.four_blocks` pad 30→16 | Homepage advantages | **Medium** — ~150 px cumulative | `main.css` |
| **9** | P-U-02 + P-U-03 | PDP discount widget + characteristics grid compaction | Used PDP | **Medium** — ~70–90 px | `main.css` |
| **10** | P-N-03 + P-N-04 | New-car bonus grid + gallery section break | New PDP | **Medium** — ~80–100 px | `main.css` |

**Impact scale:** Very High = operator notices immediately on `/cars/` or `/`; High = clear on side-by-side; Medium = supports overall density goal.

---

## Recommended implementation order

Execution waves are **sequential**; each requires backup + verification before next.

| Phase | Wave ID | Scope | Rationale |
|-------|---------|-------|-----------|
| **0** | W3UX-PRE | Introduce `--w3ux-space-*` tokens in `:root`; no visual change | Rollback clarity; avoids ad-hoc px |
| **1** | **W3UX-C1** | Used catalog card density (U-01–U-11) | Highest traffic inventory surface; CSS-only |
| **2** | **W3UX-C2** | New catalog card density (N-01–N-03) | Paired template track; reuse tokens |
| **3** | **W3UX-PDP-U** | Used PDP compaction (P-U-01–P-U-07) | Conversion surface; independent of catalog |
| **4** | **W3UX-PDP-N** | New PDP compaction (P-N-01–P-N-06) | Dual-track parity |
| **5** | **W3UX-HOME** | Homepage spacing (H-01–H-04, partner banks pad) | Visible “less empty” sitewide entry |
| **6** | **W3UX-QA** | Full matrix + mobile + inventory-rich TEST spot-check | Gate before operator sign-off |

**Optional (operator-gated):** W3UX-C3 — 5-column grid at ≥1680 px only if readability QA passes.

**Explicitly deferred / forbidden:**

- Footer, header structure — **frozen**
- W3-V token rollback — **not required** unless operator rejects combined look
- Content rewrite, block removal, animations — **forbidden**

---

## Proposed W3-UX execution roadmap

```mermaid
flowchart LR
  PRE[W3UX-PRE tokens]
  C1[W3UX-C1 used cards]
  C2[W3UX-C2 new cards]
  PU[W3UX-PDP-U]
  PN[W3UX-PDP-N]
  HM[W3UX-HOME]
  QA[W3UX-QA]

  PRE --> C1 --> C2 --> PU --> PN --> HM --> QA
```

### Per-wave deliverables (when authorized)

| Wave | Files (expected) | Verification URLs |
|------|------------------|---------------------|
| W3UX-PRE | `css/main.css` | `/`, `/cars/`, `/auto/` — visual diff = none |
| W3UX-C1 | `css/main.css`, `css/media.css` | `/cars/` + 1 used PDP |
| W3UX-C2 | `css/main.css`, `css/media.css` | `/auto/` + 1 new PDP |
| W3UX-PDP-U | `css/main.css`, `css/media.css` | used PDP sample |
| W3UX-PDP-N | `css/main.css`, `css/media.css` | new PDP sample |
| W3UX-HOME | `css/main.css`, `css/media.css`; optional `home.twig` map height only | `/` |
| W3UX-QA | report artefact | 7/7 matrix + mobile |

### Authorization prerequisites (not yet met)

| Artefact | Status |
|----------|--------|
| W3-UX write charter | **NOT CREATED** |
| Change request CR-SITE-001-W3UX | **NOT CREATED** |
| Rollback plan instance | **NOT CREATED** |
| Pre-write backup | **NOT EXECUTED** |
| Operator approval of density-first scope (not redesign) | **PENDING** |

---

## Risk register

| Risk | Mitigation |
|------|------------|
| Card too tight on mobile | Separate `media.css` overrides; touch targets ≥40 px |
| Image crop loses detail | `object-fit: cover` + max-height cap; verify on SUV/portrait photos |
| W3-V + W3UX specificity clash | Append W3UX block after W3-V EOF marker |
| Sparse TEST inventory hides grid gain | Re-verify when stock ≥8 or use W2 snapshot screenshots |
| Inline map height in twig | Flag for operator if twig touch rejected — accept 500 px map |

---

## Notes

| ID | Note | Severity |
|----|------|----------|
| N-W3UX-01 | Live TEST catalog shows **1** item vs W2 **14** — density QA needs fuller grid | **Medium** |
| N-W3UX-02 | W3-V operator sign-off still **PENDING** — W3UX builds on W3-V baseline | **Info** |
| N-W3UX-03 | Twig samples in repo are W1B snapshots; live paths confirmed via W2 FTP | **Info** |
| N-W3UX-04 | 5-column grid optional — readability risk on 1440 | **Low** |

---

## Decision record

| Field | Value |
|-------|--------|
| Decision | **DISCOVERY COMPLETE** |
| Date | 2026-06-09 |
| Wave | W3-UX — Density & Visual Effectiveness |
| Implementation | **NOT AUTHORIZED** |
| Next step | Operator review → W3-UX write charter + CR |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — W3-UX density gate decision |

*SITE-001 W3-UX Density Decision v1 — discovery gate only.*
