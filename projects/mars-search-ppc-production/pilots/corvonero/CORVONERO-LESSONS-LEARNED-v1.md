# Corvonero lessons learned v1

Grounded in Corvonero V2.1–V2.6.2 evidence. Not a generic retrospective.

## Research

**What happened:** Wordstat and SERP waves produced a corpus with career, education, and informational contamination before V2.1 cleanup.  
**Why it mattered:** 24+ confirmed non-commercial phrases reached CA-01 deployable slots.  
**Next time:** Run binding reject audit (`execute-campaign-v2.3-corrective-audit-v1.py` pattern) before group architecture freeze.  
**Enforced:** `semantic-classification-controls.mjs` + regression corpus.  
**Operator judgement:** Ambiguous «как» queries and short role phrases still need HOLD.

## Semantic judgement

**What happened:** «найти программиста 1с» risked employment classification; price-hour phrases risked over-rejection.  
**Why it mattered:** Buyer intent vs job-seeker intent is the core B2B discriminator.  
**Next time:** Separate BUYER_SERVICE, COMMERCIAL_PRICE, EMPLOYMENT classes with explicit regression fixtures.  
**Enforced:** `corvonero-regression.test.mjs` buyer/price/career cases.  
**Operator judgement:** Salary-adjacent hour-rate phrases.

## Campaign architecture

**What happened:** Over-fragmented groups and generic ad «Услуги 1С для бизнеса…» reused across unrelated intents.  
**Why it mattered:** Quality score and client comprehension suffer; audits flagged generic reuse in V2.2–V2.3.  
**Next time:** `validateCampaignArchitecture` + `detectGenericAdReuse` before ad freeze.  
**Enforced:** `campaign-architecture-validator.mjs` (WARNING vs HARD_FAIL documented).  
**Operator judgement:** Single-phrase group justification.

## Ads

**What happened:** LOCAL ads without Novosibirsk/visit framing; REMOTE ads implying visit.  
**Next time:** `validateAdCopy` mode checks before client pack.  
**Enforced:** `ad-copy-validator.mjs`.  
**Operator judgement:** Commercial claims register still requires client confirmation.

## Negatives

**What happened:** Triumph E9 stale negatives survived when blank string mapped to PRESERVE; quoted negatives simulated phrase-match.  
**Next time:** `embedded_negative_policy: blank` + separate TXT import; `resolveCampaignNegativeOperation`.  
**Enforced:** `negative-keyword-policy.mjs`, release gate E9 tests.  
**Operator judgement:** Post-launch search-query negative expansion.

## Commander transport

**What happened:** Foreign-client Triumph template contamination (organization, URL, E9 negatives).  
**Next time:** Template sanitization contract + release gate contamination scan.  
**Enforced:** `template-sanitizer.mjs`, `release-gate.mjs`.  
**Operator judgement:** Per-client template selection.

## Artifact validation

**What happened:** V2.6.1 gate PASS while phrase-slot delta was 2 (926 authority vs 924 XLSX).  
**Next time:** Mandatory `reconcilePackagePhraseSlots` in release gate — aggregate and per-campaign.  
**Enforced:** `phrase-slot-reconciler.mjs` + gate enforcement tests.  
**Operator judgement:** None for slot counts — hard fail.

## Operator approval

**What happened:** Script PASS was occasionally read as semantic approval.  
**Next time:** Separate `SCRIPT_PASS`, `OPERATOR_SEMANTIC_APPROVAL`, `CLIENT_APPROVAL` in lifecycle.  
**Enforced:** `semantic-lifecycle.mjs`, existing approval receipt spec.  
**Operator judgement:** Semantic approval remains human-only.

## Client approval

**What happened:** Client materials created late; commercial claims scattered across registers.  
**Next time:** Client pack generator + feedback intake before import authorization.  
**Enforced:** Client approval workflow doc + intake templates.  
**Operator judgement:** Client response interpretation.

## Landing production

**What happened:** Final page copy and Roman production briefs split across export waves and chats; two artifact families confused.  
**Next time:** ONE LANDING PAGE = ONE FILE; separate FINAL_PAGE_COPY vs IMPLEMENTATION_PRODUCTION_BRIEF.  
**Enforced:** `SEARCH-PPC-LANDING-PAGE-PRODUCTION-PACK-STANDARD-v1.md`, artifact index families.  
**Operator judgement:** LP mapping exceptions (one group → two pages).

## Manual edits

**What happened:** Operator polished strategy HTML manually; regeneration risk on next pack run.  
**Next time:** MANUAL_STABLE status + hash guard; new version filename for replacements.  
**Enforced:** `manual-stable-guard.mjs`, `CORVONERO-MANUAL-STABLE-ARTIFACTS-v1.json`.  
**Operator judgement:** When to supersede vs patch.

## Delivery packaging

**What happened:** Mixed V2.6.1 and V2.6.2 XLSX in delivery folders; import-order version drift.  
**Next time:** `validatePackagePurity` — single deployable version per package.  
**Enforced:** `package-purity-validator.mjs`.  
**Operator judgement:** Historical archive retention.

## Git and Storage hygiene

**What happened:** No single current-deliverables index; backup ad hoc.  
**Next time:** Post-project closure backup + artifact index + Storage README.  
**Enforced:** This closure task artifacts.  
**Operator judgement:** Checkpoint timing (rare GIT CHECKPOINT per git-rules).

## Project closure

**What happened:** No formal CLIENT_FEEDBACK_PENDING state; lessons not institutionalized automatically.  
**Next time:** `SEARCH-PPC-PROJECT-CLOSURE-CHECKLIST-v1.md` at pilot end.  
**Enforced:** Corvonero closure checklist + problem register.  
**Operator judgement:** When to declare closure vs pause.
