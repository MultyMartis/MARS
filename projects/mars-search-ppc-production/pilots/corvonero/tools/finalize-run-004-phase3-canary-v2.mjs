#!/usr/bin/env node
/**
 * Finalize Corvonero Run 004 Phase 3 canary Attempt 2 — review package and operator report.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const RUN_ID = 'corv-semantic-v2-20260626-004';
const ATTEMPT_ID = 'corv-run004-phase3-canary-attempt-002';
const PILOT = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const GIT_RUN = path.join(PILOT, 'runs', RUN_ID);
const REPORTS = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/reports');
const STORAGE = path.join('C:\\MARS Phenix\\AI MARS STORAGE', 'mig', 'corvonero', 'semantic-runs', RUN_ID);

function readJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function writeText(p, t) {
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, t);
}

function writeJson(p, d) {
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, JSON.stringify(d, null, 2));
}

function pct(n, d) {
  return d ? ((n / d) * 100).toFixed(1) : '0.0';
}

function familyAnalysis(results, family) {
  const items = results.filter((r) => r.primary_family === family);
  const dist = { ACCEPT: 0, REJECT: 0, ABSTAIN: 0 };
  for (const r of items) dist[r.final_verdict] = (dist[r.final_verdict] || 0) + 1;
  return { family, count: items.length, distribution: dist };
}

function main() {
  const resultPath = path.join(PILOT, 'CORVONERO-RUN-004-PHASE-3-CANARY-RESULT-v2.json');
  if (!fs.existsSync(resultPath)) {
    console.error('Missing canary attempt 2 result — run execute-run-004-phase3-canary-v2.mjs first');
    process.exit(2);
  }
  const data = readJson(resultPath);
  const manifest = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-3-CANARY-SELECTION-v2.json'));
  const audit = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-3-CANARY-EXPECTATION-AUDIT-v2.json'));
  const results = data.results || [];
  const total = results.length;
  const dist = data.verdict_distribution || {};
  const scored = results.filter((r) => r.scored && r.expected_verdict);
  const reviewSubset = results.filter((r) => !r.scored || r.review_required);
  const falseAccepts = scored.filter((r) => r.error_class === 'confirmed_false_accept');
  const falseRejects = scored.filter((r) => r.error_class === 'confirmed_false_reject');
  const canaryVerdict = data.canary_verdict?.canary || 'UNKNOWN';
  const lifecycle = data.canary_verdict?.run || 'UNKNOWN';

  const reviewPackage = {
    package_id: 'corvonero-run-004-phase-3-canary-review-v2',
    run_id: RUN_ID,
    attempt_id: ATTEMPT_ID,
    canary_verdict: canaryVerdict,
    lifecycle_state: lifecycle,
    processed_count: total,
    manifest_id: manifest.manifest_id,
    expectation_audit_pass: audit.preflight?.pass,
    family_counts: manifest.family_counts,
    attempt_1_overlap: manifest.attempt_1_overlap_count,
    verdict_distribution: dist,
    metrics: data.metrics,
    cost: data.cost,
    scored_authoritative: {
      total: scored.length,
      false_accepts: falseAccepts.map((r) => ({ id: r.phrase_id, phrase: r.phrase })),
      false_rejects: falseRejects.map((r) => ({ id: r.phrase_id, phrase: r.phrase })),
    },
    review_required_subset: {
      total: reviewSubset.length,
      accept: reviewSubset.filter((r) => r.final_verdict === 'ACCEPT').length,
      reject: reviewSubset.filter((r) => r.final_verdict === 'REJECT').length,
      abstain: reviewSubset.filter((r) => r.final_verdict === 'ABSTAIN').length,
    },
    family_reviews: [
      'direct_commercial_1c_service',
      'careers_training_education',
      'informational_self_service',
      'problem_troubleshooting',
      'generic_erp_platform_ambiguity',
      'integrations',
      'marking_chestny_znak',
      'ts_piot',
      'geography_modified',
      'product_license_version',
      'ambiguous_mixed_intent',
    ].map((f) => familyAnalysis(results, f)),
    operator_review_required: true,
    full_corpus_authorized: false,
    project_counters: {
      canonical_corpus_total: 2368,
      attempt_1_canary_processed: 120,
      attempt_2_canary_selected: 120,
      attempt_2_canary_processed: total,
      full_production_processed: 0,
    },
    completed_at: data.completed_at,
  };

  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-3-CANARY-REVIEW-PACKAGE-v2.json'), reviewPackage);

  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-3-CANARY-RESULT-v2.md'), `# CORVONERO RUN 004 — PHASE 3 CANARY RESULT v2 (Attempt 2)

**Run ID:** \`${RUN_ID}\`  
**Attempt ID:** \`${ATTEMPT_ID}\`  
**Canary verdict:** \`${canaryVerdict}\`  
**Lifecycle:** \`${lifecycle}\`

## Summary

| Metric | Value |
|--------|------:|
| Phrases processed | ${total} |
| ACCEPT | ${dist.ACCEPT || 0} |
| REJECT | ${dist.REJECT || 0} |
| ABSTAIN | ${dist.ABSTAIN || 0} |
| Scored authoritative | ${scored.length} |
| Review-required subset | ${reviewSubset.length} |
| Confirmed false accepts | ${falseAccepts.length} |
| Confirmed false rejects | ${falseRejects.length} |
| Cumulative cost (USD) | ${data.cost?.cumulative_cost_usd?.toFixed(4)} |

**Full corpus NOT continued. Operator review required.**
`);

  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-3-CANARY-REVIEW-PACKAGE-v2.md'), `# CORVONERO RUN 004 — PHASE 3 CANARY REVIEW PACKAGE v2

**Attempt ID:** \`${ATTEMPT_ID}\`  
**Verdict:** \`${canaryVerdict}\`

## Scored authoritative results

- Total scored: **${scored.length}**
- False accepts: **${falseAccepts.length}**
- False rejects: **${falseRejects.length}**

## Review-required subset

- Total: **${reviewSubset.length}**
- ACCEPT: **${reviewSubset.filter((r) => r.final_verdict === 'ACCEPT').length}**
- REJECT: **${reviewSubset.filter((r) => r.final_verdict === 'REJECT').length}**
- ABSTAIN: **${reviewSubset.filter((r) => r.final_verdict === 'ABSTAIN').length}**

## Next gate

\`\`\`text
OPERATOR REVIEW OF CORVONERO RUN 004 PHASE 3 CANARY ATTEMPT 2
\`\`\`
`);

  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-NEXT-TASK-v2.md'), `# CORVONERO RUN 004 — PHASE 4 NEXT TASK v2

**Status:** AWAITING OPERATOR REVIEW OF PHASE 3 CANARY ATTEMPT 2  
**Run ID:** \`${RUN_ID}\`  
**Prerequisite:** \`${canaryVerdict}\`

## Scope (NOT AUTHORIZED until operator approves)

- Full canonical corpus processing (2368 records)
- **Forbidden:** Wave 5, strategy, Campaign Architecture, Commander, import, launch

## Counters

\`\`\`text
attempt_1_canary_processed: 120
attempt_2_canary_processed: ${total}
full_production_processed: 0
cumulative_cost_usd: ${data.cost?.cumulative_cost_usd?.toFixed(4)}
\`\`\`
`);

  writeJson(path.join(GIT_RUN, 'sanitized-canary-attempt2-receipt-v1.json'), {
    run_id: RUN_ID,
    attempt_id: ATTEMPT_ID,
    canary_verdict: canaryVerdict,
    lifecycle_state: lifecycle,
    attempt_2_canary_processed: total,
    full_production_processed: 0,
    cumulative_cost_usd: data.cost?.cumulative_cost_usd,
    completed_at: data.completed_at,
  });

  console.log(JSON.stringify({ canary_verdict: canaryVerdict, outputs: 'finalized' }, null, 2));
}

main();
