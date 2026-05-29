# Compactness Examples v0

## `compact` — Triumph v5 hero main (productive)

**Pattern:** 5 single-line spec items with icons  
**Not:** 6 paragraph `hero__features` (G0)

```yaml
compactness_level: compact
hero_priority: capability_first
```

---

## `dense` — Triumph hero lower band

**Pattern:** 6 cargo cards × title + descriptor + CTA  
**Requires:** `hero__lower` zone + `visual_density: high`

```yaml
compactness_level: dense  # lower band only
cargo_cards_max: 6
cargo_cards_max_mobile: 4
```

---

## `airy` — hypothetical narrow route

**When:** single use-case LP with 3 specs + form only  
**Not observed** in Triumph calibration — illustrative only

```yaml
compactness_level: airy
visual_density: low
```

---

## Downgrade rule

On mobile, if `dense` lower band + stacked form → raise `visual_noise_risk` one tier unless cargo capped.
