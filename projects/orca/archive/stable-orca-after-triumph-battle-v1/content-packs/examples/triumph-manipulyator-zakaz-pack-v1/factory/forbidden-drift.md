# Factory — Forbidden drift

Changes that **violate** semantic lock, PPC continuity, or honesty — **reject** in Factory review.

## Positioning / claims

- Fake fleet («автопарк», «5–10 т», «подберём машину»)
- Fake pricing («от 1000 ₽/час», fixed lowball hero rate)
- Unsupported stats (review counts, years on market without source)
- Nationwide / «любой груз» without qualification

## PPC / intent

- Breaking capability numbers (≠ 5 т / 3 т / 14 м)
- Removing qualification (denied tasks, anti-evacuation line)
- Breaking PPC continuity for launched ad variant without ads update
- Changing H1 without `primary_ad_variant` strategy

## Machine / offer

- Changing machine specs without operator + pack bump
- Adding second machine on master hot page
- Implying 10+ т capability on this route

## Visual destructive

- Restoring G0 hero (`hero__rate`, fleet features)
- Hero carousel / video autoplay with semantic competition
- Six primary-red buttons in one viewport

## Process

- Shipping copy changes under MODE 1 without pack approval
- Claiming Factory auto-enforces this list (no runtime enforcer in repo)

## Current open items (calibration destructive class)

| ID | Issue |
|----|-------|
| D2 | Multi-ad H1 unresolved for A1 |
| — | Removing `hero__notice` if QA proves it hidden — treat as forbidden until pack amends |

## Historical — never restore

```yaml
never_restore:
  - hero__rate fake hourly
  - hero__features fleet 5-10t
  - hero_proof own_fleet
```
