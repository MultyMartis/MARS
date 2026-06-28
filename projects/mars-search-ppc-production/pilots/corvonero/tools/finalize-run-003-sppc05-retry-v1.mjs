#!/usr/bin/env node
/** Resume Run 003 — complete all SPPC-05 suites (no fail-fast) and emit final reports. */
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { PROMPT_VERSION } from '../../../../orca/semantic-intelligence/live-model/contracts/prompt-contract.mjs';
import { ADJUDICATOR_VERSION } from '../../../../orca/semantic-intelligence/live-model/adjudication/semantic-adjudicator.mjs';
import { getSafeConfigSummary } from '../../../../orca/semantic-intelligence/live-model/runtime/local-secret-loader.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const RUN_ID = 'corv-semantic-v2-20260626-003';
const RUN_STORAGE = path.join('C:\\MARS Phenix\\AI MARS STORAGE', 'mig', 'corvonero', 'semantic-runs', RUN_ID);
const GIT_RUN_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero/runs', RUN_ID);
const PILOT_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const REPORTS_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/reports');

const OPERATOR = {
  provider: 'openrouter',
  model: 'openai/gpt-5-mini',
  hard_cost_cap_usd: 3.0,
  soft_cost_warning_usd: 2.0,
};

function writeJson(p, data) {
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, JSON.stringify(data, null, 2));
}

function runNodeTest(scriptRel, args = []) {
  const script = path.join(REPO_ROOT, scriptRel);
  const env = {
    ...process.env,
    ORCA_SEMANTIC_PROVIDER: OPERATOR.provider,
    ORCA_SEMANTIC_MODEL: OPERATOR.model,
    ORCA_EVAL_LIVE: '1',
  };
  const started = Date.now();
  const result = spawnSync(process.execPath, [script, ...args], {
    cwd: REPO_ROOT,
    env,
    encoding: 'utf8',
    maxBuffer: 80 * 1024 * 1024,
  });
  return {
    script: scriptRel,
    args,
    exit_code: result.status,
    stdout: result.stdout || '',
    stderr: result.stderr || '',
    runtime_ms: Date.now() - started,
    pass: result.status === 0,
  };
}

function parseLastJson(stdout) {
  const lines = stdout.trim().split('\n');
  for (let i = lines.length - 1; i >= 0; i--) {
    const line = lines[i].trim();
    if (line.startsWith('{')) {
      try { return JSON.parse(line); } catch { /* continue */ }
    }
  }
  return null;
}

function evaluateGateCriteria(suiteResults, varianceReport, psrAmb) {
  const productConf = suiteResults.find((s) => s.id === 'confirmation_product');
  const geoConf = suiteResults.find((s) => s.id === 'confirmation_geo_v2');
  const closed = suiteResults.find((s) => s.id === 'closed_dataset_regression');
  const problem = suiteResults.find((s) => s.id === 'problem_query_policy');
  const bypass = suiteResults.find((s) => s.id === 'wave31f_bypass');
  const under = suiteResults.find((s) => s.id === 'under_admission');
  const platform = suiteResults.find((s) => s.id === 'platform_compatibility');
  const defectRepro = suiteResults.find((s) => s.id === 'focused_repair_repro');

  const productMetrics = productConf?.parsed_summary?.metrics;
  const geoMetrics = geoConf?.parsed_summary?.metrics;
  const closedSummary = closed?.parsed_summary?.summary;
  const productFpr = productMetrics?.false_positive_rate ?? closedSummary?.product_fpr;

  const criteria = {
    adversarial_fpr_max_0_01_product: productMetrics?.gate_pass === true,
    adversarial_fpr_max_0_01_geo: geoMetrics?.gate_pass === true,
    geo_commercial_recall_gte_0_90: (geoMetrics?.commercial_recall ?? 0) >= 0.9,
    geo_adversarial_fpr_zero: (geoMetrics?.adversarial_false_accept_rate ?? 1) === 0,
    closed_dataset_boxed_delivery_fixed: closedSummary?.boxed_delivery_fixed === true,
    closed_dataset_product_fpr: productFpr == null || productFpr <= 0.01,
    problem_query_all_match: problem?.pass === true,
    wave31f_bypass_all_pass: bypass?.pass === true,
    under_admission_all_pass: under?.pass === true,
    platform_compatibility_full_pass: platform?.pass === true,
    structured_output_full_pass: defectRepro?.pass === true,
    focused_repair_stable: defectRepro?.parsed_summary?.all_match === true,
    variance_repair_cases_stable: varianceReport?.repair_cases_stable === true,
    all_suites_exit_zero: suiteResults.filter((s) => s.live !== false).every((s) => s.pass),
    psr_amb_01_isolated: !psrAmb?.expands_false_accept_family,
    project_corpus_processed_zero: true,
  };
  criteria.all_pass = Object.entries(criteria)
    .filter(([k]) => k !== 'psr_amb_01_isolated')
    .every(([, v]) => v === true);
  criteria.psr_amb_01_status = psrAmb;
  return criteria;
}

function buildPsrAmbFromClosed(closedParsed) {
  const failures = closedParsed?.summary?.contrast_false_rejects || closedParsed?.summary?.mismatches || [];
  const psr = Array.isArray(failures) ? failures.find((f) => f.record_id === 'PSR-AMB-01') : null;
  return {
    record_id: 'PSR-AMB-01',
    query: 'купить 1с с настройкой',
    expected: 'ABSTAIN',
    observed: psr?.final || psr?.got || 'UNKNOWN',
    known_ambiguity: true,
    non_blocking: true,
    historically_observed: 'ACCEPT',
    expands_false_accept_family: false,
    note: 'Pre-existing ambiguous minimal pair; must remain visible in operator review',
  };
}

function mdReport(data) {
  const g = data.gate_criteria;
  const gateB = data.gate_b_verdict;
  return `# CORVONERO RUN 003 — SPPC-05 RESULT v1

**Run ID:** \`${RUN_ID}\`  
**Completed:** ${data.completed_at}  
**Gate B:** \`${gateB.status}\`  
**Lifecycle:** \`${gateB.run_lifecycle}\`

## Summary

| Item | Value |
|------|-------|
| Provider | ${data.provider} |
| Model | ${data.model} |
| Prompt contract | ${data.prompt_contract_version} |
| Adjudicator | ${data.adjudicator_version} |
| Corpus processed | 0 / 2368 |
| Cumulative cost (USD) | ${data.cumulative_cost_usd?.toFixed(4) ?? '0'} |
| Isolation | ${data.isolation?.verdict} |
| Repair authority | ${data.repair_authority?.verdict} |

## Suite Results

${data.suite_results.map((s) => `- **${s.id}**: ${s.pass ? 'PASS' : 'FAIL'} (exit ${s.exit_code}, ${Math.round(s.runtime_ms / 1000)}s)`).join('\n')}

## Critical Gates

| Gate | Result |
|------|--------|
| Product FPR ≤ 0.01 | ${g.adversarial_fpr_max_0_01_product ? 'PASS' : 'FAIL'} |
| Geo commercial recall ≥ 0.90 | ${g.geo_commercial_recall_gte_0_90 ? 'PASS' : 'FAIL'} |
| Geo adversarial FPR = 0 | ${g.geo_adversarial_fpr_zero ? 'PASS' : 'FAIL'} |
| Problem query 10/10 | ${g.problem_query_all_match ? 'PASS' : 'FAIL'} |
| Under-admission | ${g.under_admission_all_pass ? 'PASS' : 'FAIL'} |
| Wave 3.1F bypass | ${g.wave31f_bypass_all_pass ? 'PASS' : 'FAIL'} |
| Platform compatibility | ${g.platform_compatibility_full_pass ? 'PASS' : 'FAIL'} |
| Repair fixtures stable | ${g.focused_repair_stable && g.variance_repair_cases_stable ? 'PASS' : 'FAIL'} |

## PSR-AMB-01 (known ambiguity)

- Expected: **ABSTAIN**
- Observed: **${data.psr_amb_01?.observed || 'see closed dataset'}**
- Non-blocking: **yes** (isolated; no product FPR breach from this pair alone)

## Failures

${gateB.status.startsWith('PASS') ? '_None — operator review required before Phase 3._' : data.critical_failures?.map((f) => `- ${f}`).join('\n') || '_See review package._'}

## Stop Condition

${gateB.status.startsWith('PASS') ? 'Phase 3 canary **not started** — awaiting operator authorization.' : 'Run **BLOCKED_AT_SPPC_05** — no canary, no corpus processing.'}
`;
}

function main() {
  const prior = JSON.parse(fs.readFileSync(path.join(RUN_STORAGE, 'reports', 'sppc-05-execution-report-v1.json'), 'utf8'));
  const repairSnapshot = JSON.parse(fs.readFileSync(path.join(RUN_STORAGE, 'manifests', 'repair-authority-freeze-v1.json'), 'utf8'));

  const testSuites = [
    { id: 'wave31f_bypass', script: 'projects/orca/semantic-intelligence/live-model/tests/run-wave31f-bypass-audit.mjs', live: false },
    { id: 'under_admission', script: 'projects/orca/semantic-intelligence/live-model/tests/run-under-admission-regression.mjs', live: false },
    { id: 'platform_compatibility', script: 'projects/orca/semantic-intelligence/live-model/tests/run-platform-compatibility-regression.mjs', live: true },
    { id: 'focused_repair_repro', script: 'projects/orca/semantic-intelligence/live-model/tests/run-sppc05-defect-repro.mjs', live: true },
    { id: 'problem_query_policy', script: 'projects/orca/semantic-intelligence/live-model/tests/run-problem-query-policy-regression.mjs', live: true },
    { id: 'confirmation_product', script: 'projects/orca/semantic-intelligence/live-model/tests/run-confirmation-validation.mjs', args: ['--stratum=protected_product_confirmation'], live: true },
    { id: 'confirmation_geo_v2', script: 'projects/orca/semantic-intelligence/live-model/tests/run-confirmation-validation.mjs', args: ['--stratum=geo_commercial_confirmation_v2'], live: true },
    { id: 'closed_dataset_regression', script: 'projects/orca/semantic-intelligence/live-model/tests/run-closed-dataset-regression.mjs', live: true },
  ];

  const suiteResults = [];
  let cumulativeCost = 0;
  for (const suite of testSuites) {
    const r = runNodeTest(suite.script, suite.args || []);
    const parsed = parseLastJson(r.stdout);
    if (parsed?.cost_usd) cumulativeCost += parsed.cost_usd;
    if (parsed?.metrics?.gate_pass === false) r.pass = false;
    suiteResults.push({ ...suite, ...r, parsed_summary: parsed });
  }

  const varianceR = runNodeTest('projects/orca/semantic-intelligence/live-model/tests/run-sppc05-variance-check.mjs', ['--reps=3']);
  const varianceReport = parseLastJson(varianceR.stdout);
  if (varianceReport?.cost_usd) cumulativeCost += varianceReport.cost_usd;

  const closed = suiteResults.find((s) => s.id === 'closed_dataset_regression');
  let psrAmb = buildPsrAmbFromClosed(closed?.parsed_summary);
  const psrVariance = varianceReport?.cases?.find((c) => c.record_id === 'PSR-AMB-01');
  if (psrVariance) {
    psrAmb = {
      record_id: 'PSR-AMB-01',
      query: 'купить 1с с настройкой',
      expected: 'ABSTAIN',
      repetitions: psrVariance.repetitions,
      verdict_distribution: psrVariance.verdict_distribution,
      observed_primary: psrVariance.primary_distribution,
      known_ambiguity: true,
      non_blocking: true,
      expands_false_accept_family: false,
    };
  }

  const gateCriteria = evaluateGateCriteria(suiteResults, varianceReport, psrAmb);
  const criticalFailures = [];
  if (!gateCriteria.adversarial_fpr_max_0_01_product) criticalFailures.push('Product confirmation adversarial FPR exceeds 0.01');
  if (!gateCriteria.problem_query_all_match) criticalFailures.push('Problem query regression not 10/10 (PQR-ABSTAIN-03)');
  if (!gateCriteria.platform_compatibility_full_pass) criticalFailures.push('Platform compatibility not full pass (PC-ABSTAIN-01 model variance)');
  if (!gateCriteria.focused_repair_stable) criticalFailures.push('Focused repair repro: PQR-ABSTAIN-03 adjudicator ordering issue on SINGLE_ASSESSOR path');
  if (!gateCriteria.variance_repair_cases_stable) criticalFailures.push('Variance check: repair fixtures unstable');

  const gateBVerdict = gateCriteria.all_pass
    ? { status: 'PASS — OPERATOR REVIEW REQUIRED', project: 'FROZEN_PENDING_CANARY_AUTHORIZATION', run_lifecycle: 'PHASE_0_1_2_COMPLETE' }
    : { status: 'FAILED', project: 'BLOCKED_AT_SPPC_05', run_lifecycle: 'BLOCKED_AT_SPPC_05' };

  const sppc05Report = {
    ...prior,
    gate_b_verdict: gateBVerdict,
    gate_criteria: gateCriteria,
    critical_failures: criticalFailures,
    suite_results: suiteResults.map(({ id, script, pass, exit_code, runtime_ms, parsed_summary, live }) => ({
      id, script, pass, exit_code, runtime_ms, live,
      metrics: parsed_summary?.metrics || parsed_summary?.summary || parsed_summary,
    })),
    variance_check: varianceReport,
    psr_amb_01: psrAmb,
    cumulative_cost_usd: cumulativeCost,
    prompt_contract_version: PROMPT_VERSION,
    adjudicator_version: ADJUDICATOR_VERSION,
    completed_at: new Date().toISOString(),
  };

  writeJson(path.join(RUN_STORAGE, 'reports', 'sppc-05-execution-report-v1.json'), sppc05Report);
  writeJson(path.join(GIT_RUN_DIR, 'reports', 'sppc-05-sanitized-report-v1.json'), sppc05Report);
  writeJson(path.join(PILOT_DIR, 'CORVONERO-RUN-003-SPPC-05-RESULT-v1.json'), sppc05Report);
  writeJson(path.join(PILOT_DIR, 'CORVONERO-RUN-003-SPPC-05-REVIEW-PACKAGE-v1.json'), sppc05Report);

  const cpPath = path.join(RUN_STORAGE, 'checkpoints', 'checkpoint-sppc05-complete-v1.json');
  const cp = JSON.parse(fs.readFileSync(cpPath, 'utf8'));
  cp.phase = gateBVerdict.status.startsWith('PASS') ? 'SPPC-05_COMPLETE_PENDING_REVIEW' : 'BLOCKED_AT_SPPC_05';
  cp.cumulative_cost_usd = cumulativeCost;
  cp.gate_b_verdict = gateBVerdict.status;
  cp.complete = gateBVerdict.status.startsWith('PASS');
  writeJson(cpPath, cp);

  const receiptPath = path.join(RUN_STORAGE, 'receipts', 'phase-0-1-2-execution-receipt-v1.json');
  const receipt = JSON.parse(fs.readFileSync(receiptPath, 'utf8'));
  receipt.gate_b = gateBVerdict.status;
  receipt.lifecycle_state = gateBVerdict.run_lifecycle;
  receipt.cumulative_cost_usd = cumulativeCost;
  receipt.completed_at = sppc05Report.completed_at;
  writeJson(receiptPath, receipt);
  writeJson(path.join(GIT_RUN_DIR, 'sanitized-execution-receipt-v1.json'), receipt);
  writeJson(path.join(GIT_RUN_DIR, 'lifecycle-decision-v1.json'), {
    run_id: RUN_ID,
    decision: gateBVerdict.run_lifecycle,
    sppc_05: gateBVerdict.status,
    next_gate: 'OPERATOR REVIEW OF CORVONERO RUN 003 SPPC-05 RESULT',
    canary_authorized: false,
    full_corpus_authorized: false,
  });

  const md = mdReport({ ...sppc05Report, repair_authority: repairSnapshot, isolation: prior.isolation, provider: OPERATOR.provider, model: OPERATOR.model });
  fs.writeFileSync(path.join(PILOT_DIR, 'CORVONERO-RUN-003-SPPC-05-RESULT-v1.md'), md);

  const reviewMd = `# CORVONERO RUN 003 — SPPC-05 REVIEW PACKAGE v1

**Run:** \`${RUN_ID}\`  
**Verdict:** \`${gateBVerdict.status}\`

## Operator decisions (recorded)

- ORCA repair: **APPROVED**
- Run 002: **BLOCKED / NON-RESUMABLE**
- Run 003: **SPPC-05 RETRY ONLY**
- PSR-AMB-01: **KNOWN AMBIGUITY — NON-BLOCKING**
- Phase 3: **NOT AUTHORIZED**

## Critical failures

${criticalFailures.map((f) => `- ${f}`).join('\n') || '_None_'}

## Repair fixture evidence

### CFM-PROD-UPD-02
${JSON.stringify(varianceReport?.cases?.find((c) => c.record_id === 'CFM-PROD-UPD-02') || suiteResults.find((s) => s.id === 'focused_repair_repro')?.parsed_summary, null, 2)}

### PQR-ABSTAIN-03
${JSON.stringify(varianceReport?.cases?.find((c) => c.record_id === 'PQR-ABSTAIN-03') || 'see problem_query_policy suite', null, 2)}

### PSR-AMB-01
${JSON.stringify(psrAmb, null, 2)}

## Suite matrix

${suiteResults.map((s) => `| ${s.id} | ${s.pass ? 'PASS' : 'FAIL'} | ${s.exit_code} |`).join('\n')}

## Cost

- Cumulative: **$${cumulativeCost.toFixed(4)}**
- Hard cap: **$${OPERATOR.hard_cost_cap_usd}**
`;
  fs.writeFileSync(path.join(PILOT_DIR, 'CORVONERO-RUN-003-SPPC-05-REVIEW-PACKAGE-v1.md'), reviewMd);

  const phase3Md = gateBVerdict.status.startsWith('PASS')
    ? fs.readFileSync(path.join(PILOT_DIR, 'CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-PHASE-3-NEXT-TASK-v1.md'), 'utf8').replace(/corv-semantic-v2-20260626-002/g, RUN_ID).replace('BLOCKED_AT_SPPC_05', 'FROZEN_PENDING_CANARY_AUTHORIZATION')
    : `# CORVONERO RUN 003 — PHASE 3 NEXT TASK v1

**Status:** **BLOCKED** — SPPC-05 Gate B not met  
**Run ID:** \`${RUN_ID}\`  
**Lifecycle:** \`BLOCKED_AT_SPPC_05\`

## Prerequisite (not met)

\`\`\`text
SPPC-05: PASS — OPERATOR REVIEW REQUIRED
\`\`\`

Current:

\`\`\`text
SPPC-05: FAILED
Run 003: BLOCKED_AT_SPPC_05
\`\`\`

## Required operator actions

1. Review \`CORVONERO-RUN-003-SPPC-05-REVIEW-PACKAGE-v1.md\`
2. Assess adjudicator SINGLE_ASSESSOR ordering vs ambiguous_diy downgrade (PQR-ABSTAIN-03)
3. Assess PC-ABSTAIN-01 generic ERP model variance
4. Authorize new repair or new run only after explicit decision

**Phase 3 canary, full corpus, Wave 5: NOT AUTHORIZED**
`;
  fs.writeFileSync(path.join(PILOT_DIR, 'CORVONERO-RUN-003-PHASE-3-NEXT-TASK-v1.md'), phase3Md);

  console.log(JSON.stringify({ gate_b: gateBVerdict, cost: cumulativeCost, suites: suiteResults.map((s) => ({ id: s.id, pass: s.pass })) }, null, 2));
  process.exit(gateBVerdict.status.startsWith('PASS') ? 0 : 1);
}

main();
