# Dated Analytical Pack Contract v1

**Stage:** SPPC-12  
**Schema:** `schemas/dated-analytical-pack-v1.schema.json`

## Required sections

1. Project identity  
2. Business authority  
3. Analysis period  
4. Evidence inventory (with authority + checksum)  
5. Source coverage  
6. Corpus summary  
7. Accepted/rejected/abstain demand  
8. T1–T5 distribution  
9. Service ownership  
10. Semantic clusters  
11. Negative intelligence  
12. Paid SERP evidence  
13. Competitor advertising evidence  
14. Competitor landing evidence  
15. Landing inventory  
16. Offer inventory  
17. Geography  
18. Historical campaign evidence (optional)  
19. Data limitations  
20. Stale evidence  
21. Missing evidence  
22. Readiness assessment  
23. Statements (typed OBSERVED FACT / DERIVED FINDING / etc.)

## Readiness levels

- **COMPLETE** — all mandatory production evidence current  
- **COMPLETE WITH APPROVED DEGRADATION** — degraded Paid SERP or similar formally approved  
- **PARTIAL — PROVISIONAL ONLY** — draft analysis allowed, not production strategy  
- **BLOCKED** — mandatory evidence absent (e.g. Paid SERP)

## Builder

`runtime/lib/analytical-pack-builder.mjs` — fail-closed on invalid authority.
