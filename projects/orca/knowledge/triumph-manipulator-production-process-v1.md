# Triumph Manipulator — Actual Production Process v1

**Source:** Repository evidence only — not idealized ORCA theory  
**Reference stable state:** `freeze/battle-pilot-triumph-search-v1/TRIUMPH-SEARCH-RK-STABLE-STATE-v1.md`

---

## Stage map

| # | Stage | Input | Decision authority | Output | Validation | Failure modes | Successful rule |
|---|-------|-------|------------------|--------|------------|---------------|-----------------|
| 1 | Business & service scope | Operator brief; MIG intake; doctrine | **Operator** + doctrine | 12 route families; capability line | Route family freeze | Scope creep; generic «манипулятор» dump | Freeze 12 routes before keywords |
| 2 | Commercial intent architecture | `intent-groups-v1.md`; Wordstat (external) | **Operator** + ORCA doctrine | S/A tiers; reject tier-X | SE-04 tier gate | Volume-first grouping | Search intent first |
| 3 | Campaign architecture | Scope + geo Krasnodar | **Operator** | 1 search campaign; manual CPC | Campaign metadata in JSON | Multi-campaign premature split | Single unified search campaign |
| 4 | Group architecture | Route family index | **Operator** + route freeze | 12 groups = 12 intents | SE-01 single intent | Mixed employment/rental/purchase | One group = one intent |
| 5 | Semantic ownership | Keyword clusters per group | **Operator** review; validator advisory | Phrase ownership per group | SE-02 cross-intent risk | Semantic dumps | No outliers in cluster |
| 6 | Commercial/informational filter | Blocklists; campaign negatives | **Validator** flags; **operator** decides | Employment/purchase terms excluded | SE-03 blocklist | Informational bleed | Campaign + group negatives |
| 7 | Narrow group handling | Low-volume capability routes | **Operator** | Valid narrow groups (e.g. 5t, vezdehod) | Group viability = intent not count | False HOLD on low count | Narrow OK if intent distinct |
| 8 | Ads | Blueprints; landing routes | **Operator** + CM rules | 20 ads; phrase in H1/desc | CM-01..CM-* | Generic fluff; false capability | Primary phrase in H1 + description |
| 9 | Landing alignment | `landing-route-registry.json`; Factory pages | **Operator** + URL sync gate | final_url per group | LM-* continuity | URL drift after Factory deploy | URL registry sync before export |
| 10 | Negative architecture | Cross-route matrix script | **Operator** approves matrix | Group negatives col 68 | Cross-negative QA | Wildcards; syntax errors | Matrix mandatory pre-export |
| 11 | Cross-negatives | `cross-negative-matrix-v1.4.js` | **Production rules** | Sibling-route separation | `commander_negative_syntax_pass` | Artificial groups via negatives | Negatives separate neighbors only |
| 12 | Bids | `BID-MANAGEMENT-RULES-v1.md` | **Operator** in Direct post-import | Keyword-row bids 400–600 | Bid assignment script | Zero bids; ad-row bids | Bids on keyword rows only |
| 13 | Production export | JSON instance + template v1 | **Exporter** human-triggered | `triumph-sheet1-patch-launch-ready-v1.4.xlsx` | validate launch-ready v1.4 | Transport split errors | Validate before Commander |
| 14 | Operator review | XLSX + Commander preview | **Operator** | Import PASS / fix list | GROUP-FIDELITY-QA | Trusting PASS without reopen | Independent XLSX reopen |
| 15 | Corrections | Commander import feedback | **Operator** | Iterative exporter fixes v0.1–v1.4 | Import observations docs | Silent auto-fix | Document every transport fix |
| 16 | Dry-run/import readiness | Commander desktop | **Operator** | Structural import PASS | Entity counts 12/20/64 | Launch confused with import PASS | Import PASS ≠ launch approved |

---

## Actual pipeline sequence (reproducible)

```text
Route family freeze (12 routes)
  → JSON instance (meaning SoT)
  → validation-cli (345 rules, human-triggered)
  → cross-negative matrix (mandatory)
  → hygiene audit checklist
  → Exporter v1.4 sheet1-patch on template v1
  → validate:launch-ready-v1.4
  → Direct Commander import (human dry-run)
  → post-import: budget, schedule, strategy (human, pending)
```

---

## What Triumph did NOT automate

- Launch, moderation, budget, schedule
- Autonomous semantic reclassification
- Silent scope reduction
- Operator approval substitution
