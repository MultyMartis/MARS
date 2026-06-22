# SPPC-17 — Landing and Offer Alignment

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-17-landing-and-offer-alignment.md`

---

## Stage ID

SPPC-17

## Name

Landing and Offer Alignment

## Purpose

Align final URLs, offers, and landing messaging with ads and service ownership so click paths deliver coherent commercial promises.

## Owning system

QA / Campaign Production

## Participating systems

- Website Factory
- Operator
- ORCA (ownership)

## Required inputs

- SPPC-16 ads_produced token
- Ad copy pack with provisional URLs
- SPPC-07 ownership manifest
- Landing inventory or published site map

## Optional inputs

- UTM policy
- Offer variant tests

## Source-of-truth rules

- URL alignment manifest is SoT for final landing URLs per group/ad.
- Offer claims on landing must match ad promises within intake tolerance.
- Misaligned groups block QA and export.

## Required processing

- Resolve provisional URLs to production or staging finals.
- Verify offer parity: service, geo, price signals vs ads.
- Apply UTM and tracking parameters per policy.
- Flag broken links, mismatched offers, or missing landings.
- Emit alignment manifest for SPPC-19.

## Required outputs

- Landing and offer alignment manifest
- URL verification report
- Mismatch resolution log

## Prohibited outputs

- Export XLSX
- Silent use of homepage fallback without flag
- New offer claims not in intake

## Validation rules

- All active ads have verified final URL.
- No unresolved offer mismatches.
- Tracking parameters policy-compliant.

## Blocking conditions

- SPPC-16 incomplete
- Broken URLs without waiver
- Offer mismatch above threshold

## Completion status

COMPLETE when alignment manifest committed and `landing_aligned` token issued.

## Evidence requirements

- Alignment manifest path
- URL verification report
- Mismatch resolutions

## Next allowed stages

- SPPC-18
- SPPC-19

## Rollback / reopen behavior

Site publish or offer change reopens alignment for affected groups.

## Responsible role

QA landing lead

## Operator approval required

yes — for offer mismatch waivers
