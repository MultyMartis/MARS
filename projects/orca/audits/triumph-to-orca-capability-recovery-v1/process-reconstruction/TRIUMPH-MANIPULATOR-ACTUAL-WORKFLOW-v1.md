# Triumph Manipulator — Actual Workflow v1

**Method:** Repository evidence reconstruction — no invented steps  
**Machine-readable:** [`triumph-manipulator-actual-workflow-v1.json`](triumph-manipulator-actual-workflow-v1.json)  
**Canonical prior:** `projects/orca/knowledge/triumph-manipulator-production-process-v1.md`

---

## Executive summary

Triumph Manipulator Search PPC was built as a **human-operated, architecture-first** pipeline: freeze 12 commercial route families → encode meaning in JSON → validate with 345 rules → mandatory cross-negatives → Commander export → human import review. Keyword surface is **small (64 phrases)** and **scenario/intent-driven**, not a bulk Wordstat dump. MIG Triumph pilot explicitly disabled `keyword_pass`.

---

## Stage reconstruction

| # | Stage | Input | Actor | Action | Output | Tool | Mode | Repeatable | Project-specific | Promoted to ORCA |
|---|-------|-------|-------|--------|--------|------|------|------------|------------------|------------------|
| 1 | Business & service scope | Operator brief; MIG gruzotaxi pilot (SERP/website, not Wordstat) | **Operator** + doctrine | Define manipulator rental scope, Krasnodar geo, equipment line | 12 route families concept | MIG intake docs; operator | **Hybrid** | Partial | Yes (5t, routes) | Route family freeze |
| 2 | Route family freeze | Scope + semantic packs | **Operator** | Lock 12 distinct commercial routes before keywords | `ORCA-ROUTE-FAMILY-FREEZE-v1` | Freeze docs | **Manual** | Yes | Triumph slugs | **Yes** — LAW-01 |
| 3 | Commercial intent architecture | `intent-groups-v1.md`; doctrine | **Operator** + ORCA doctrine | Assign S/A tiers; reject tier-X | Tier map per route | Markdown doctrine | **Manual** | Yes | Triumph examples | SE rules, tiers |
| 4 | Keyword / phrase design | Scenario examples in intent-groups; **SAFE UNKNOWN: external Wordstat** | **Operator** + chat reasoning (not in repo) | Curate ~64 phrases across 12 groups; `is_primary` anchors | Phrases in JSON instance | JSON editing; **not bulk automated gen** | **Manual/Hybrid** | Partial | Yes | Primary seed pattern |
| 5 | Campaign architecture | Scope + geo | **Operator** | 1 unified search campaign, manual CPC | Campaign block in JSON | JSON | **Manual** | Yes | Krasnodar | Pattern in decisions JSON |
| 6 | Group architecture | Route freeze | **Operator** | 12 groups = 12 intents | `grp_fc01`–`grp_fc12` | JSON + SE-01 | **Manual** | Yes | 12 routes | **Yes** — LAW-03 |
| 7 | Semantic ownership | Keyword clusters | **Operator** review; validator advisory | Assign phrases to single group; block employment/purchase | Owned phrase sets | validation-cli SE-* | **Hybrid** | Yes | Triumph blocklists | **Yes** — LAW-06 |
| 8 | Negative architecture | Cross-route matrix | **Operator** approves | Group negatives col 68; campaign negatives | Negative lists | `cross-negative-matrix-v1.4.js` | **Hybrid** | Yes | 12-route matrix | **Yes** — LAW-08/09 |
| 9 | Ad drafting | Blueprints; landing routes | **Operator** + CM rules | 20 ads; primary phrase in H1/desc | Ad entities in JSON | Manual + validation | **Manual** | Partial | Triumph copy | CM rules |
| 10 | Landing alignment | Registry + Factory pages | **Operator** + URL sync gate | `final_url` per group; 164 URL fix | URL sync PASS | `commander-url-sync-v1` | **Hybrid** | Yes | manipulator-triumph.ru | LRL, LAW-10 |
| 11 | Validation gate | JSON instance | **Operator** triggers CLI | 345 rules PASS required | validation report | `validation-cli` | **Automated check, human trigger** | Yes | Triumph schema | **Yes** — validator pattern |
| 12 | Production export | JSON + template v1 | **Operator** triggers exporter | XLSX v1.4 launch-ready | gitignored output | exporter-cli v1.4 | **Hybrid** | Yes | Template cols | Transport pattern |
| 13 | External artefact QA | XLSX | **Operator** | GROUP-FIDELITY-QA; Commander desktop dry-run | Import structural PASS | Commander | **Manual** | Yes | — | **Yes** — LAW-14 |
| 14 | Launch boundary | Import PASS | **Operator** | Budget, schedule, launch — **explicitly not done** | Pending launch | Direct UI | **Manual** | — | — | LAW-15, approval gates |

---

## Actual pipeline sequence (reproducible from repo)

```text
Route family freeze (12 routes)
  → semantic packs + intent tiers (documented)
  → JSON instance triumph-s-tier-draft-v1.json (64 phrases — curated)
  → validation-cli (345 rules, human-triggered)
  → cross-negative matrix (mandatory)
  → hygiene audit checklist
  → Exporter v1.4 sheet1-patch on template v1
  → validate:launch-ready-v1.4
  → Direct Commander import (human dry-run) — PASS
  → post-import: budget, schedule, strategy (human, pending)
```

---

## What Triumph did NOT automate

- Bulk keyword mining from Wordstat inside repo pipeline
- Autonomous semantic reclassification
- Silent scope reduction
- Launch, moderation, budget, schedule
- Operator approval substitution

---

## Unknown steps (explicit)

| Step | Status |
|------|--------|
| Original Web-GPT chat reasoning for phrase list | **SAFE UNKNOWN** — chat not in repo |
| Whether operator used Wordstat outside MARS | **SAFE UNKNOWN** — no Triumph Wordstat files in repo |
| Operator-signed launch approval | **Not found** |
