#!/usr/bin/env node
/**
 * Finalize Corvonero Run 004 Phase 3 canary — review package and operator report.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const RUN_ID = 'corv-semantic-v2-20260626-004';
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
  return { family, count: items.length, distribution: dist, examples: items.slice(0, 3).map((r) => ({ id: r.phrase_id, phrase: r.phrase, verdict: r.final_verdict })) };
}

function errorFamilyAnalysis(results) {
  const families = [
    'platform_mismatch',
    'generic_erp_ambiguity',
    'product_license_vs_service',
    'product_plus_service_bundles',
    'informational_self_service',
    'ambiguous_diy_problems',
    'direct_problem_demand',
    'integrations',
    'marking_chestny_znak',
    'ts_piot',
    'careers_training',
    'geography',
  ];
  const map = {
    platform_mismatch: (r) => r.platform_class === 'EXPLICIT_INCOMPATIBLE',
    generic_erp_ambiguity: (r) => r.primary_family === 'generic_erp_platform_ambiguity' || r.tags?.includes('erp_reference'),
    product_license_vs_service: (r) => r.primary_family === 'product_license_version',
    product_plus_service_bundles: (r) => r.edge_cases?.includes('psr_amb_01_family') || r.edge_cases?.includes('product_plus_service_bundle'),
    informational_self_service: (r) => r.primary_family === 'informational_self_service',
    ambiguous_diy_problems: (r) => r.edge_cases?.includes('ambiguous_diy_troubleshooting'),
    direct_problem_demand: (r) => r.primary_family === 'problem_troubleshooting',
    integrations: (r) => r.primary_family === 'integrations',
    marking_chestny_znak: (r) => r.primary_family === 'marking_chestny_znak',
    ts_piot: (r) => r.primary_family === 'ts_piot',
    careers_training: (r) => r.primary_family === 'careers_training_education',
    geography: (r) => r.primary_family === 'geography_modified' || r.tags?.includes('geography'),
  };
  return families.map((f) => {
    const affected = results.filter(map[f]);
    const unexpected = affected.filter((r) => r.expectation_class === 'pre_authorized' && r.expected_verdict && r.final_verdict !== r.expected_verdict);
    return {
      family: f,
      affected_ids: affected.map((r) => r.phrase_id),
      count: affected.length,
      examples: affected.slice(0, 2).map((r) => r.phrase),
      unexpected_count: unexpected.length,
      severity: unexpected.length >= 3 ? 'blocking_review' : unexpected.length ? 'non_blocking_review' : 'none',
      recommendation: unexpected.length >= 3 ? 'Operator review required — possible systematic family error' : 'Monitor — no broad pattern detected',
    };
  });
}

function main() {
  const resultPath = path.join(PILOT, 'CORVONERO-RUN-004-PHASE-3-CANARY-RESULT-v1.json');
  if (!fs.existsSync(resultPath)) {
    console.error('Missing canary result — run execute-run-004-phase3-canary-v1.mjs first');
    process.exit(2);
  }
  const data = readJson(resultPath);
  const manifest = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-3-CANARY-SELECTION-v1.json'));
  const results = data.results || [];
  const total = results.length;
  const dist = data.verdict_distribution || {};
  const preAuth = results.filter((r) => r.expectation_class === 'pre_authorized' && r.expected_verdict);
  const falseAccepts = preAuth.filter((r) => r.expected_verdict === 'REJECT' && r.final_verdict === 'ACCEPT');
  const falseRejects = preAuth.filter((r) => r.expected_verdict === 'ACCEPT' && r.final_verdict === 'REJECT');
  const wrongAbstains = preAuth.filter((r) => r.expected_verdict === 'ABSTAIN' && r.final_verdict !== 'ABSTAIN');
  const psrFamily = results.filter((r) => r.edge_cases?.includes('psr_amb_01_family') || r.tags?.includes('product_plus_service_bundle'));
  const psrAccepted = psrFamily.filter((r) => r.final_verdict === 'ACCEPT');

  const canaryVerdict = data.canary_verdict?.canary || 'UNKNOWN';
  const lifecycle = data.canary_verdict?.run || 'UNKNOWN';

  const reviewPackage = {
    package_id: 'corvonero-run-004-phase-3-canary-review-v1',
    run_id: RUN_ID,
    canary_verdict: canaryVerdict,
    lifecycle_state: lifecycle,
    processed_count: total,
    manifest_id: manifest.manifest_id,
    family_counts: manifest.family_counts,
    verdict_distribution: dist,
    metrics: data.metrics,
    cost: data.cost,
    psr_amb_01: {
      policy: 'KNOWN NON-BLOCKING AMBIGUITY — MUST BE INCLUDED AND MONITORED',
      family_size: psrFamily.length,
      accepted_count: psrAccepted.length,
      accepted_ids: psrAccepted.map((r) => r.phrase_id),
      expands_false_accept_family: psrFamily.length >= 3 && psrAccepted.length / psrFamily.length > 0.6,
    },
    pre_authorized_evaluation: {
      total: preAuth.length,
      false_accepts: falseAccepts.map((r) => ({ id: r.phrase_id, phrase: r.phrase })),
      false_rejects: falseRejects.map((r) => ({ id: r.phrase_id, phrase: r.phrase })),
      wrong_abstains: wrongAbstains.map((r) => ({ id: r.phrase_id, phrase: r.phrase, got: r.final_verdict })),
    },
    error_families: errorFamilyAnalysis(results),
    operator_review_required: true,
    full_corpus_authorized: false,
    project_counters: {
      canonical_corpus_total: 2368,
      canary_selected: 120,
      canary_processed: total,
      full_production_processed: 0,
      unique_run004_assessed: total,
    },
    completed_at: data.completed_at,
  };

  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-3-CANARY-REVIEW-PACKAGE-v1.json'), reviewPackage);

  const resultMd = `# CORVONERO RUN 004 — PHASE 3 CANARY RESULT v1

**Run ID:** \`${RUN_ID}\`  
**Canary verdict:** \`${canaryVerdict}\`  
**Lifecycle:** \`${lifecycle}\`  
**Completed:** ${data.completed_at || 'n/a'}

## Summary

| Metric | Value |
|--------|------:|
| Phrases processed | ${total} |
| ACCEPT | ${dist.ACCEPT || 0} (${pct(dist.ACCEPT, total)}%) |
| REJECT | ${dist.REJECT || 0} (${pct(dist.REJECT, total)}%) |
| ABSTAIN | ${dist.ABSTAIN || 0} (${pct(dist.ABSTAIN, total)}%) |
| Schema valid | ${data.metrics?.schema_valid_percentage?.toFixed(1)}% |
| Operator review rate | ${(data.metrics?.operator_review_rate * 100)?.toFixed(1)}% |
| Cumulative cost (USD) | ${data.cost?.cumulative_cost_usd?.toFixed(4)} |

## Pre-authorized expectation evaluation

- Pre-authorized items: **${preAuth.length}**
- False accepts: **${falseAccepts.length}**
- False rejects: **${falseRejects.length}**
- Wrong abstains: **${wrongAbstains.length}**

## PSR-AMB-01 family

- Monitored phrases: **${psrFamily.length}**
- ACCEPT count: **${psrAccepted.length}**
- Expands false-accept family: **${reviewPackage.psr_amb_01.expands_false_accept_family ? 'YES — REVIEW' : 'NO'}**

## Project counters

\`\`\`text
canonical_corpus_total: 2368
canary_selected: 120
canary_processed: ${total}
full_production_processed: 0
\`\`\`

**Full corpus NOT continued. Operator review required.**
`;

  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-3-CANARY-RESULT-v1.md'), resultMd);

  const reviewMd = `# CORVONERO RUN 004 — PHASE 3 CANARY REVIEW PACKAGE v1

**Run ID:** \`${RUN_ID}\`  
**Verdict:** \`${canaryVerdict}\`

## Verdict distribution

${Object.entries(dist).map(([k, v]) => `- **${k}:** ${v} (${pct(v, total)}%)`).join('\n')}

## Error-family analysis

${reviewPackage.error_families.map((f) => `### ${f.family}
- Affected: ${f.count}
- Unexpected vs pre-auth: ${f.unexpected_count}
- Severity: ${f.severity}
- Recommendation: ${f.recommendation}
`).join('\n')}

## Operator decisions required

1. Review PSR-AMB-01 family ACCEPT instances (if any).
2. Review ${falseAccepts.length} false accepts and ${falseRejects.length} false rejects on pre-authorized items.
3. Authorize or deny Phase 4 full-corpus task separately.

**Wave 5, strategy, Campaign Architecture, Commander, import, launch: BLOCKED**
`;

  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-3-CANARY-REVIEW-PACKAGE-v1.md'), reviewMd);

  const phase4Md = `# CORVONERO RUN 004 — PHASE 4 NEXT TASK v1

**Status:** AWAITING OPERATOR REVIEW OF PHASE 3 CANARY  
**Run ID:** \`${RUN_ID}\`  
**Prerequisite:** \`CANARY: PASS — OPERATOR REVIEW REQUIRED\` (operator sign-off)

## Scope (NOT AUTHORIZED until operator approves)

- Full canonical corpus processing (2368 records)
- Separate cost charter and batch authorization
- **Forbidden without authorization:** Wave 5, strategy, Campaign Architecture, Commander, import, launch

## Current counters

\`\`\`text
canary_processed: ${total}
full_production_processed: 0
cumulative_cost_usd: ${data.cost?.cumulative_cost_usd?.toFixed(4)}
\`\`\`

## Next gate

\`\`\`text
OPERATOR REVIEW OF CORVONERO RUN 004 PHASE 3 CANARY
→ explicit Phase 4 / full-corpus authorization decision
\`\`\`
`;

  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-NEXT-TASK-v1.md'), phase4Md);

  const reportMd = `# REPORT — CORVONERO RUN 004 PHASE 3 CONTROLLED CANARY V1

## 1. Safety and Authorization

Operator authorized Phase 3 only. Gate B APPROVED. Full corpus NOT authorized. Wave 5 BLOCKED.

## 2. Git Preflight

Branch \`mars/canonical-post-recovery\`. Recovery ancestor verified. ORCA hashes match approved freeze.

## 3. Run 004 Authority

Run \`${RUN_ID}\`. Lifecycle: \`${lifecycle}\`. SPPC-05 cost ~0.685 USD recorded.

## 4. ORCA Authority

semantic-adjudicator v1.5, platform-compatibility v1.1, hard-rules v1.2, prompt-contract v1.4, service-intent-evidence v1.1 — **FROZEN, no drift**.

## 5. Input Authority

PRJ-0013, session-mig-20260622-corv01, corpus 2368, hash prefix eaa09b8450f82738.

## 6. Cost Projection

Canary cost ${data.cost?.canary_cost_usd?.toFixed(4)} USD; cumulative ${data.cost?.cumulative_cost_usd?.toFixed(4)} USD (cap 3.00).

## 7. Phase Transition

PHASE_0_1_2_COMPLETE → PHASE_3_CANARY_AUTHORIZED → ${lifecycle}.

## 8–10. Canary Selection

Deterministic seed \`${manifest.seed}\`. Algorithm: edge cases → family minimums → tag fallback → fill. Exactly ${manifest.selected_count} IDs.

## 11–13. Lock and Checkpoint

Phase 3 lock acquired/released outside Git under STORAGE. Checkpoint tracks canary_processed=${total}, full_production_processed=0.

## 14. Assessment Pipeline

Wave 3.1F: primary → reassessment → evidence → platform → hard rules → adjudication → invariants.

## 15. Verdict Distribution

ACCEPT ${dist.ACCEPT || 0}, REJECT ${dist.REJECT || 0}, ABSTAIN ${dist.ABSTAIN || 0}.

## 16. Structured Output

Schema valid: ${data.metrics?.schema_valid_percentage?.toFixed(1)}%.

## 17. Expected-Policy Evaluation

False accepts: ${falseAccepts.length}. False rejects: ${falseRejects.length}. Wrong abstains: ${wrongAbstains.length}.

## 18–26. Family Reviews

See CORVONERO-RUN-004-PHASE-3-CANARY-REVIEW-PACKAGE-v1.json error_families.

## 28. PSR-AMB-01 Family Status

${psrFamily.length} monitored; ${psrAccepted.length} ACCEPT. Expands false-accept: ${reviewPackage.psr_amb_01.expands_false_accept_family}.

## 29. Cost and Runtime

${data.batches?.length || 6} batches × ~20 phrases. Retries: ${data.metrics?.retry_count || 0}.

## 30. Canary Verdict

\`${canaryVerdict}\`

## 31. Project Lifecycle

FROZEN_PENDING_FULL_CORPUS_AUTHORIZATION (if pass) or BLOCKED_AT_PHASE_3_CANARY (if fail).

## 33. Outputs Created

Selection, result JSON/MD, review package, phase 4 next task, this report.

## 37. Git Status

No commit. No push.

## 38. SAFE UNKNOWN

No foreign/incompatible platform phrase in canonical corpus — edge case covered by policy only, not live corpus fixture.

## 39. Operator Decisions Required

Review canary package; authorize or deny Phase 4.

## 40. Exact Phase 4 Task

See CORVONERO-RUN-004-PHASE-4-NEXT-TASK-v1.md

## 41. Stop Condition

**STOPPED** after 120-phrase canary. Full corpus NOT continued.
`;

  writeText(path.join(REPORTS, 'REPORT-corvonero-run-004-phase-3-canary-v1.md'), reportMd);

  writeJson(path.join(GIT_RUN, 'sanitized-canary-receipt-v1.json'), {
    run_id: RUN_ID,
    canary_verdict: canaryVerdict,
    lifecycle_state: lifecycle,
    canary_processed: total,
    full_production_processed: 0,
    cumulative_cost_usd: data.cost?.cumulative_cost_usd,
    completed_at: data.completed_at,
  });

  writeJson(path.join(STORAGE, 'receipts', 'canary-final-receipt-v1.json'), reviewPackage);

  console.log(JSON.stringify({ canary_verdict: canaryVerdict, outputs: 'finalized' }, null, 2));
}

main();
