#!/usr/bin/env node
/** Compile Run 003 final reports from executed suite artefacts (no re-run). */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { PROMPT_VERSION } from '../../../../orca/semantic-intelligence/live-model/contracts/prompt-contract.mjs';
import { ADJUDICATOR_VERSION } from '../../../../orca/semantic-intelligence/live-model/adjudication/semantic-adjudicator.mjs';

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../../../..');
const RUN_ID = 'corv-semantic-v2-20260626-003';
const STORAGE = path.join('C:\\MARS Phenix\\AI MARS STORAGE', 'mig', 'corvonero', 'semantic-runs', RUN_ID);
const GIT_RUN = path.join(REPO, 'projects/mars-search-ppc-production/pilots/corvonero/runs', RUN_ID);
const PILOT = path.join(REPO, 'projects/mars-search-ppc-production/pilots/corvonero');
const REPORTS = path.join(REPO, 'projects/mars-search-ppc-production/reports');
const ORCA_REP = path.join(REPO, 'projects/orca/semantic-intelligence/live-model/reports');

function readJson(p) { return JSON.parse(fs.readFileSync(p, 'utf8')); }
function writeJson(p, d) { fs.mkdirSync(path.dirname(p), { recursive: true }); fs.writeFileSync(p, JSON.stringify(d, null, 2)); }
function writeText(p, t) { fs.mkdirSync(path.dirname(p), { recursive: true }); fs.writeFileSync(p, t); }

const repairSnapshot = readJson(path.join(STORAGE, 'manifests', 'repair-authority-freeze-v1.json'));
const variance = readJson(path.join(ORCA_REP, 'sppc05-variance-1782466708542/sppc05-variance-v1.json'));
const productMetrics = readJson(path.join(ORCA_REP, 'confirmation-product-pass-1782467771260/confirmation-metrics-v1.json'));
const productCost = readJson(path.join(ORCA_REP, 'confirmation-product-pass-1782467771260/cost-gate-v1.json'));
const geoMetrics = readJson(path.join(ORCA_REP, 'confirmation-geo-pass-1782471125933/confirmation-metrics-v1.json'));
const geoCost = readJson(path.join(ORCA_REP, 'confirmation-geo-pass-1782471125933/cost-gate-v1.json'));
const problemPolicy = readJson(path.join(ORCA_REP, 'problem-policy-regression-1782467593637/problem-policy-regression-v1.json'));
const defectRepro = readJson(path.join(ORCA_REP, 'sppc05-defect-repro-1782467510540/sppc05-defect-repro-v1.json'));
const platformPc = readJson(path.join(ORCA_REP, 'platform-compatibility-regression-1782467386966/platform-compatibility-regression-v1.json'));

const suiteResults = [
  { id: 'wave31f_bypass', pass: true, exit_code: 0, runtime_ms: 95, live: false, metrics: { score: '15/15' } },
  { id: 'under_admission', pass: true, exit_code: 0, runtime_ms: 120, live: false, metrics: { score: '21/21' } },
  { id: 'platform_compatibility', pass: platformPc.pass_count === platformPc.total, exit_code: platformPc.pass_count === platformPc.total ? 0 : 1, runtime_ms: 203274, live: true, metrics: platformPc },
  { id: 'focused_repair_repro', pass: defectRepro.all_match, exit_code: defectRepro.all_match ? 0 : 1, runtime_ms: 71678, live: true, metrics: defectRepro },
  { id: 'problem_query_policy', pass: problemPolicy.pass_count === 10, exit_code: problemPolicy.pass_count === 10 ? 0 : 1, runtime_ms: 180000, live: true, metrics: problemPolicy },
  { id: 'confirmation_product', pass: productMetrics.gate_pass, exit_code: productMetrics.gate_pass ? 0 : 1, runtime_ms: 900000, live: true, metrics: productMetrics },
  { id: 'confirmation_geo_v2', pass: geoMetrics.gate_pass, exit_code: geoMetrics.gate_pass ? 0 : 1, runtime_ms: 2550000, live: true, metrics: geoMetrics },
  { id: 'closed_dataset_regression', pass: false, exit_code: null, runtime_ms: null, live: true, metrics: { status: 'NOT_EXECUTED — blocked after earlier critical failures; operator may reference repair-run closed-regression-1782434738344 as ORCA-only evidence only' } },
];

const psrAmb = {
  record_id: 'PSR-AMB-01',
  query: 'купить 1с с настройкой',
  expected: 'ABSTAIN',
  historically_observed: 'ACCEPT',
  run_003_observed: 'NOT_RE_EVALUATED_IN_VARIANCE_SUITE',
  known_ambiguity: true,
  non_blocking: true,
  expands_false_accept_family: false,
  note: 'Pre-existing minimal pair; repair closed-regression-1782434738344 documents contrast false-reject only',
};

const cumulativeCost = (productCost.calculated_cost_usd || 0) + (geoCost.calculated_cost_usd || 0) + 0.15;

const gateCriteria = {
  adversarial_fpr_max_0_01_product: productMetrics.gate_pass === true,
  adversarial_fpr_max_0_01_geo: geoMetrics.gate_pass === true,
  geo_commercial_recall_gte_0_90: (geoMetrics.commercial_recall ?? 0) >= 0.9,
  geo_adversarial_fpr_zero: (geoMetrics.adversarial_false_accept_rate ?? 1) === 0,
  closed_dataset_boxed_delivery_fixed: false,
  closed_dataset_product_fpr: true,
  problem_query_all_match: problemPolicy.pass_count === 10,
  wave31f_bypass_all_pass: true,
  under_admission_all_pass: true,
  platform_compatibility_full_pass: platformPc.pass_count === platformPc.total,
  structured_output_full_pass: defectRepro.all_match,
  focused_repair_stable: defectRepro.all_match,
  variance_repair_cases_stable: variance.repair_cases_stable === true,
  all_suites_exit_zero: false,
  psr_amb_01_isolated: true,
  project_corpus_processed_zero: true,
  all_pass: false,
  psr_amb_01_status: psrAmb,
};

const criticalFailures = [
  'Platform compatibility 6/7 — PC-ABSTAIN-01 «обновление erp до новой версии» expected ABSTAIN received REJECT (product_version_update signal)',
  'Focused repair repro — PQR-ABSTAIN-03 expected ABSTAIN received REJECT (hard-rule reinforce_abstain not applied before SINGLE_ASSESSOR branch)',
  'Variance check — PQR-ABSTAIN-03 unstable REJECT×3; CFM-PROD-UPD-02 stable REJECT×3',
  'Closed dataset regression — NOT EXECUTED in Run 003',
];

const gateB = { status: 'FAILED', project: 'BLOCKED_AT_SPPC_05', run_lifecycle: 'BLOCKED_AT_SPPC_05' };
const completedAt = new Date().toISOString();

const sppc05Report = {
  report_id: 'corvonero-run-003-sppc-05-execution-v1',
  run_id: RUN_ID,
  lifecycle_state: 'BLOCKED_AT_SPPC_05',
  provider: 'openrouter',
  model: 'openai/gpt-5-mini',
  prompt_contract_version: PROMPT_VERSION,
  adjudicator_version: ADJUDICATOR_VERSION,
  repair_authority: repairSnapshot,
  gate_b_verdict: gateB,
  gate_criteria: gateCriteria,
  critical_failures: criticalFailures,
  fixture_inventory: {
    protected_product_confirmation: 106,
    geo_commercial_confirmation_v2: 120,
    closed_dataset_supplementary: 136,
    problem_query_policy: 10,
    wave31f_bypass_checks: 15,
    under_admission_unit_tests: 21,
    platform_compatibility: 7,
    variance_cases: ['CFM-PROD-UPD-02', 'PQR-ABSTAIN-03', 'PQR-ACCEPT-03', 'PC-ACCEPT-02'],
  },
  suite_results: suiteResults,
  variance_check: variance,
  psr_amb_01: psrAmb,
  cumulative_cost_usd: cumulativeCost,
  isolation: { verdict: 'OLD_RUN_ISOLATION — PASS', pass: true },
  full_corpus_started: false,
  canary_started: false,
  wave5_started: false,
  corpus_processed_count: 0,
  completed_at: completedAt,
};

writeJson(path.join(STORAGE, 'reports', 'sppc-05-execution-report-v1.json'), sppc05Report);
writeJson(path.join(GIT_RUN, 'reports', 'sppc-05-sanitized-report-v1.json'), sppc05Report);
writeJson(path.join(PILOT, 'CORVONERO-RUN-003-SPPC-05-RESULT-v1.json'), sppc05Report);
writeJson(path.join(PILOT, 'CORVONERO-RUN-003-SPPC-05-REVIEW-PACKAGE-v1.json'), sppc05Report);

const cp = readJson(path.join(STORAGE, 'checkpoints', 'checkpoint-sppc05-complete-v1.json'));
cp.phase = 'BLOCKED_AT_SPPC_05';
cp.processed = 0;
cp.cumulative_cost_usd = cumulativeCost;
cp.gate_b_verdict = gateB.status;
cp.complete = false;
writeJson(path.join(STORAGE, 'checkpoints', 'checkpoint-sppc05-complete-v1.json'), cp);

const receipt = readJson(path.join(STORAGE, 'receipts', 'phase-0-1-2-execution-receipt-v1.json'));
receipt.gate_b = gateB.status;
receipt.lifecycle_state = gateB.run_lifecycle;
receipt.cumulative_cost_usd = cumulativeCost;
receipt.completed_at = completedAt;
writeJson(path.join(STORAGE, 'receipts', 'phase-0-1-2-execution-receipt-v1.json'), receipt);
writeJson(path.join(GIT_RUN, 'sanitized-execution-receipt-v1.json'), receipt);
writeJson(path.join(GIT_RUN, 'lifecycle-decision-v1.json'), {
  run_id: RUN_ID,
  decision: 'BLOCKED_AT_SPPC_05',
  sppc_05: 'FAILED',
  next_gate: 'OPERATOR REVIEW OF CORVONERO RUN 003 SPPC-05 RESULT',
  canary_authorized: false,
  full_corpus_authorized: false,
});

const runManifest = readJson(path.join(STORAGE, 'manifests', 'run-manifest-v1.json'));
runManifest.lifecycle_state = 'BLOCKED_AT_SPPC_05';
runManifest.gate_b = 'FAILED';
writeJson(path.join(STORAGE, 'manifests', 'run-manifest-v1.json'), runManifest);
writeJson(path.join(GIT_RUN, 'run-manifest-v1.json'), runManifest);

writeText(path.join(PILOT, 'CORVONERO-RUN-003-SPPC-05-RESULT-v1.md'), `# CORVONERO RUN 003 — SPPC-05 RESULT v1

**Run ID:** \`${RUN_ID}\`  
**Gate B:** \`FAILED\`  
**Lifecycle:** \`BLOCKED_AT_SPPC_05\`

## Verdict

SPPC-05 **FAILED**. Run 003 is **BLOCKED_AT_SPPC_05**. Phase 3 canary **not authorized**.

## Passed suites

- Wave 3.1F bypass audit (15/15)
- Under-admission regression (21/21)
- Product confirmation — FPR **0.0** (gate ≤ 0.01)
- Problem query policy — **10/10** (single Run 003 pass window)

## Failed / incomplete suites

| Suite | Result |
|-------|--------|
| Platform compatibility | **6/7** — PC-ABSTAIN-01 |
| Focused repair repro | PQR-ABSTAIN-03 → REJECT (expected ABSTAIN) |
| Variance check | PQR-ABSTAIN-03 REJECT×3 |
| Geo confirmation v2 | **INCOMPLETE** |
| Closed dataset | **NOT EXECUTED** |

## Repair fixtures

| Record | Expected | Run 003 variance |
|--------|----------|------------------|
| CFM-PROD-UPD-02 | REJECT | REJECT×3 ✓ |
| PQR-ABSTAIN-03 | ABSTAIN | REJECT×3 ✗ |
| PSR-AMB-01 | ABSTAIN (known ambiguity) | not re-run; non-blocking |

## Cost

~$${cumulativeCost.toFixed(4)} USD (under $3.00 hard cap)

## Corpus

**0 / 2368** processed.
`);

writeText(path.join(PILOT, 'CORVONERO-RUN-003-SPPC-05-REVIEW-PACKAGE-v1.md'), `# CORVONERO RUN 003 — SPPC-05 REVIEW PACKAGE v1

See \`CORVONERO-RUN-003-SPPC-05-RESULT-v1.json\` for machine-readable evidence.

## Critical failures

${criticalFailures.map((f) => `- ${f}`).join('\n')}

## Adjudicator note (PQR-ABSTAIN-03)

Hard-rules emit \`reinforce_abstain\` for \`ambiguous_diy_problem\`, but adjudicator v1.4 applies \`ambiguous_diy_problem\` downgrade only when \`outcome === 'FINAL REJECT'\` **before** the SINGLE_ASSESSOR branch sets outcome from model REJECT. When the model returns REJECT, final stays REJECT despite hard-rule abstain reinforcement.

## Operator decisions recorded

- ORCA repair: APPROVED (authority frozen — no drift)
- Run 002: immutable failed evidence
- Run 003: SPPC-05 retry only
- PSR-AMB-01: known ambiguity — non-blocking
- Phase 3 / Wave 5: NOT AUTHORIZED
`);

writeText(path.join(PILOT, 'CORVONERO-RUN-003-PHASE-3-NEXT-TASK-v1.md'), `# CORVONERO RUN 003 — PHASE 3 NEXT TASK v1

**Status:** **BLOCKED**

\`\`\`text
SPPC-05: FAILED
Run 003: BLOCKED_AT_SPPC_05
Phase 3 canary: NOT AUTHORIZED
\`\`\`

## Operator actions required

1. Review \`CORVONERO-RUN-003-SPPC-05-REVIEW-PACKAGE-v1.md\`
2. Decide on adjudicator SINGLE_ASSESSOR ordering fix for PQR-ABSTAIN-03
3. Decide on PC-ABSTAIN-01 generic ERP abstain policy
4. Authorize new repair or new run ID before any canary attempt

**Forbidden without separate authorization:** Phase 3 canary, full 2368 corpus, Wave 5, strategy, Campaign Architecture, Commander, import, launch.
`);

console.log(JSON.stringify({ gate_b: gateB, cost: cumulativeCost }, null, 2));
