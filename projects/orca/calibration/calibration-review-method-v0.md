# Calibration Review Method v0

Human-operated pass — target **45–90 minutes** for one landing route.

## Preconditions

- [ ] Route identified (URL, `data-page-type`, PPC group id)
- [ ] ORCA sources open: blueprint, campaign instance, pack (if any), handoff (if any)
- [ ] Factory workspace identified (do not assume v4 vs v5 — check `index.html` includes)
- [ ] Built `dist/` or src partials available for read-only review

## Steps

### 1. State capture (15 min)

Fill `current-state/`:

- Page identity, section order, hero structure, CTA map, semantic lock status
- List UNKNOWNs (no handoff, mock forms, live URL not verified)

### 2. PPC continuity (15 min)

Fill `ppc-alignment/`:

- For **each active ad variant** in the group: H1, description, callouts vs hero + first screen
- Mark pass / fail / ambiguous per variant

### 3. Drift analysis (20 min)

Fill `drift-analysis/`:

- Line-by-line: blueprint/pack → as-built
- Tag productive vs destructive
- Hero and trust blocks get separate files

### 4. UX + factory (15 min)

Fill `ux-observations/` and `implementation-findings/`:

- Density, hierarchy, mobile risks
- What ORCA did not specify but Factory needed

### 5. Evolution (10 min)

Fill `next-evolution/`:

- Pack fields to add
- Hero v2 requirements
- Scaling rules for sibling pages

## Evidence rules

- Cite repo paths — no invented fleet, prices, or stats
- Browser QA findings → mark **UNKNOWN** until operator confirms
- Do not cite heatmaps or A/B results unless attached by operator

## Exit criteria

| Criterion | Required |
|-----------|----------|
| At least one destructive or productive drift documented with evidence | yes |
| PPC continuity table for primary ad variant | yes |
| Factory gap list (≥3 items) | yes |
| Scaling rules draft | yes |
| `approved_for_launch` verdict | **no** — out of scope |

## Stop cues

Stop when findings repeat across sections — consolidate in `implementation-findings/handoff-gaps-v1.md`.

Do not expand calibration into rebuilding the landing in the same session.
