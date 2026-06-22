# P0-I Pilot Selection Policy v1

**Target:** ~200 unique phrases (preferred 200)  
**Seed:** `p0-i-real-slice-v1-20260622`

## Stratified coverage

### Commercial-looking (~90)

- explicit service requests
- implementation/configuration
- modification/integration
- support/recovery
- quote/price/contact

### Protected non-commercial (~70)

- career, education, DIY/how-to, regulatory, navigational/login, documentation/download/free

### Ambiguous/high risk (~40)

- short head, problem queries, product vs service, support vs info, career vs provider, provider vs DIY, malformed/noise, unknown

## Rules

1. Preserve natural phrases and source IDs
2. No old Corvonero decisions as selection criteria
3. No duplicate normalized phrases
4. Avoid single-family domination via per-stratum quotas
5. Include diagnostic failure patterns via supplementary integration fixtures when needed
6. Seeded random sample within strata
7. Distinguish `natural` vs `synthetic` phrase origin

## Prohibited

- Manual phrase picking based on desired output
- Prefilled truth labels in manifest
