# SITE-002 — Offers Input (`offers0_*.xml`) Current State

**Status: OPEN** (root cause not closed; intermittent recovery observed)

## CURRENT OBSERVATION

- Canonical offers input family: `offers0_*.xml`.
- Persistent historical pattern: `import0_1.xml` arrives; `offers0_*.xml` absent → ATTENTION / `OFFERS_INPUT_MISSING`.
- Natural scheduled ATTENTION days accepted historically include 2026-08-08 … 2026-08-12 (distinct daily events).
- Later healthcheck windows (e.g. ~2026-08-19…24) have shown SUCCESS with `offers0_1.xml` present on some runs — this is **intermittent recovery evidence**, not proof that upstream root cause is solved.

## EVIDENCE

- Client Ops D6G / D6G1 / D6G1B evidence under `X:\AI MARS\projects\client-ops-reporting-bridge\evidence\`
- Terminal / completion samples under `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\`
- Do not treat old “offers always missing” or “always fixed” slogans as absolute without fresh terminal proof.

## KNOWN IMPACT

- Prices / stock may not update when offers input missing.
- Operator receives ATTENTION Telegram (when dispatch healthy).
- Catalog phase may still succeed.

## WHAT IS NOT AFFECTED (when ATTENTION only)

- Server-side reporting architecture itself.
- Requirement that workstation run poller.
- Product mass-disable solely due to missing offers (must not happen).

## RESPONSIBILITY BOUNDARY

Unresolved which of:

1. 1C never generates offers export;
2. generated but uploaded elsewhere / wrong path;
3. wrong name (e.g. literal `offer.xml`);
4. cleanup/removal before importer;
5. race — wrapper starts before complete exchange;
6. server importer expectation mismatch;
7. 1C configuration excludes offers/prices/stocks;
8. other proven cause.

## NEXT FORENSIC QUESTIONS

See also `DEEP-RESEARCH-BACKLOG.md` and future D6G2 charter. Do not start forensic in this knowledge-only phase.

## STOP CONDITIONS (for claiming RESOLVED)

All required:

- Proven root cause with owner;
- Sustained natural scheduled runs with offers present **or** accepted configuration change explaining absence;
- Terminal + Telegram semantics updated if classification changes;
- Explicit human acceptance of closure.

Until then: **OPEN**.
