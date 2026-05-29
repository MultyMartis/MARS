# Conversion Friction v1

**Method:** Human reasoning from structure + reports — **no** heatmaps, A/B, or analytics.

## Friction register

| Risk | Mechanism | Likelihood | Severity |
|------|-----------|------------|----------|
| **Overload** | 5 specs + 4 proof + 6 cargo + form | medium | medium |
| **Weak call CTA** | Form dominates; call below consent | medium | medium |
| **Visual confusion** | Many icons + red accents | low | medium |
| **Too much text** | Long consent + form note | medium | medium |
| **Hidden proof** | 4.9 ★ not in hero | medium | medium |
| **Weak urgency** | «От 30 мин» not quantified in lead | low | low |
| **Weak qualification** | No hero notice | medium | **high** (junk leads) |
| **Mobile collapse** | Form stack order | **UNKNOWN** | high |
| **Form mock / broken POST** | hardening audit | **UNKNOWN live** | **critical** if unfixed |
| **Consent friction** | Required checkbox in hero | certain | low–medium (legal) |
| **Cargo CTA competition** | 6 modal triggers | medium | medium |
| **Scroll to trust** | Reviews below fold | medium | medium |

## What reduces friction (observed)

- Single primary verb «Рассчитать» across hero + specs
- Specs answer «подходит ли» before ask
- Denied tasks reduce wrong submissions (if read)
- `tel:` link present in form

## Priority fixes (calibration ranking)

1. Qualification visible early (hero or sticky)
2. Live form handler + operator test
3. Mobile: call prominence for call-first ads
4. Trust social proof in hero OR first scroll stop
5. Cargo count / hierarchy

## Not claimed

- Conversion rate impact
- Bounce rate
- Quality score changes

Operator should run `fast-review/mobile-friction-review-v1.md` from ORCA operational index for live session.
