# Triumph — Demand Evidence Trace v1

**Question:** Did Manipulator use Wordstat, MIG, SERP, operator seeds, model-generated hypotheses, or business/scenario reasoning only?

---

## Confirmed evidence

| Source | Triumph usage | Evidence path |
|--------|---------------|---------------|
| **MIG pilot (Triumph gruzotaxi)** | **Used for SERP + website/landing intelligence; Wordstat pass OFF** | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/request-triumph-gruzotaxi-krasnodar-v1-fields.md` — `keyword_pass: false` |
| **Scenario / intent-tier reasoning** | **CONFIRMED** — `intent-groups-v1.md` defines S/A tiers with example queries per commercial scenario | `projects/orca/ppc/triumph-manipulator/research/intent-groups-v1.md` |
| **Operator-curated phrase set** | **CONFIRMED** — 64 phrases in JSON, not corpus-scale ingestion | `triumph-s-tier-draft-v1.json` |
| **Doctrine: search intent first, not volume first** | **CONFIRMED** | `doctrine/generation-logic-v0.md` |
| **Production process doc cites Wordstat (external)** | **REFERENCED only** — not wired to Triumph repo pipeline | `knowledge/triumph-manipulator-production-process-v1.md` stage 2 |
| **Campaign negatives include employment/DIY blockers** | **CONFIRMED** — semantic filter encoded in JSON | `triumph-s-tier-draft-v1.json` `campaign_negatives` |
| **No Triumph Wordstat files in repository** | **CONFIRMED absence** | Evidence inventory gaps; grep across `ppc/triumph-manipulator` finds no Wordstat artifacts |
| **No MIG Wordstat for Triumph in incoming/** | **CONFIRMED** — Triumph MIG request disables keyword surface | MIG request fields |

---

## Probable inference (not operationally proven in repo)

| Inference | Basis | Confidence |
|-----------|-------|------------|
| Operator or Web-GPT chat may have used **external Wordstat or market knowledge** informally when drafting 64 phrases | Process doc mentions "Wordstat (external)"; intent-groups reads like market-informed scenarios; operator reported similar chat built campaign without passed Wordstat keys | **Medium — not provable from repo** |
| Phrases reflect **commercial scenario design** more than frequency-driven expansion | Small curated set; tier S routes emphasize capability/use-case fit over volume | **High** |
| **Web-GPT chat** performed semantic architecture and copy structuring | Battle artifacts, doctrine, JSON structure — **SAFE UNKNOWN for chat-local steps** | **Low-Medium** |

---

## Absent evidence

| Expected if Wordstat-driven | Status |
|----------------------------|--------|
| Wordstat XLSX or normalized JSON under Triumph paths | **Absent** |
| MIG `keyword_registry` for Triumph manipulator search campaign | **Absent** (gruzotaxi pilot only) |
| Seed-to-expansion pipeline script for Triumph | **Absent** |
| Frequency fields on Triumph JSON keywords | **Absent** |
| Operator-provided Wordstat key list in repo | **Not found** |

---

## Corvonero contrast (for boundary clarity)

| Source | Corvonero clean-room | Evidence |
|--------|---------------------|----------|
| MIG Wordstat Pass A | **CONFIRMED USED** — 2399 rows | `session-mig-20260622-corv01` |
| Operator seeds in MIG | 20 seeds → expansion | `research_pack.approved.md` |
| SERP R1 partial | Captured | MIG session SERP evidence |
| Pipeline treated topical 1С match as commercial admission | **CONFIRMED failure** — 1892 accepts | `corvonero-direct-v2-clean-room/PROJECT.md` |

**Triumph and Corvonero used opposite demand postures:** Triumph = architecture-first small curated set; Corvonero clean-room = bulk Wordstat corpus + weak regex admission.

---

## SAFE UNKNOWN

1. **Full Web-GPT chat-local reasoning** for Triumph phrase generation — **unavailable in repository**; cannot reconstruct completely from repo alone.
2. **Whether operator used Wordstat in browser** without storing exports in MARS — **unknown**.
3. **Historical campaign data** for Triumph — **not in repo**.

---

## Conclusion (evidence-bounded)

**Cannot claim** Triumph was built "without Wordstat" in absolute terms — no repo proof of external Wordstat use, but also no repo proof it was never used informally.

**Can claim from repo:**

- Triumph **production pipeline in MARS** did **not** ingest a Wordstat corpus.
- Triumph MIG pilot **explicitly disabled** keyword/Wordstat pass.
- Triumph final keyword set is **small, operator/architecture-curated**, scenario-tier driven.
- Corvonero clean-room **did** ingest Wordstat and failed admission logic — separate failure mode from Triumph's approach.
