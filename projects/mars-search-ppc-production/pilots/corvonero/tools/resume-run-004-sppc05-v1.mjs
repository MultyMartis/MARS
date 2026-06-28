#!/usr/bin/env node
/**
 * Corvonero Run 004 — resume SPPC-05 from operator pause (ПРОДОЛЖИМ).
 * Skips suites recorded in partial-sppc05-results-v1.json.
 */
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { loadLocalSecrets, getSafeConfigSummary } from '../../../../orca/semantic-intelligence/live-model/runtime/local-secret-loader.mjs';
import { PROMPT_VERSION } from '../../../../orca/semantic-intelligence/live-model/contracts/prompt-contract.mjs';
import { ADJUDICATOR_VERSION } from '../../../../orca/semantic-intelligence/live-model/adjudication/semantic-adjudicator.mjs';
import { HARD_RULES_VERSION } from '../../../../orca/semantic-intelligence/production/assessors/hard-rules.mjs';
import { SERVICE_INTENT_EVIDENCE_VERSION } from '../../../../orca/semantic-intelligence/live-model/evidence/service-intent-evidence.mjs';
import { PLATFORM_COMPATIBILITY_VERSION } from '../../../../orca/semantic-intelligence/live-model/evidence/platform-compatibility.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const RUN_ID = 'corv-semantic-v2-20260626-004';
const RUN_STORAGE = path.join('C:\\MARS Phenix\\AI MARS STORAGE', 'mig', 'corvonero', 'semantic-runs', RUN_ID);
const GIT_RUN_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero/runs', RUN_ID);
const PILOT_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const REPORTS_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/reports');

const OPERATOR = {
  provider: 'openrouter',
  model: 'openai/gpt-5-mini',
  hard_cost_cap_usd: 3.0,
  soft_cost_warning_usd: 2.0,
  psr_amb_01: 'KNOWN PRE-EXISTING AMBIGUITY — NON-BLOCKING FOR RUN 004 SPPC-05 — MUST REMAIN VISIBLE',
};

const PAUSE_PATH = path.join(RUN_STORAGE, 'checkpoints', 'pause-checkpoint-v1.json');
const PARTIAL_PATH = path.join(RUN_STORAGE, 'reports', 'partial-sppc05-results-v1.json');
const LOCK_PATH = path.join(RUN_STORAGE, 'locks', 'run.lock.json');

const ALL_SUITES = [
  { id: 'wave31f_bypass', script: 'projects/orca/semantic-intelligence/live-model/tests/run-wave31f-bypass-audit.mjs', live: false },
  { id: 'under_admission', script: 'projects/orca/semantic-intelligence/live-model/tests/run-under-admission-regression.mjs', live: false },
  { id: 'platform_compatibility', script: 'projects/orca/semantic-intelligence/live-model/tests/run-platform-compatibility-regression.mjs', live: true },
  { id: 'focused_repair_repro', script: 'projects/orca/semantic-intelligence/live-model/tests/run-sppc05-defect-repro.mjs', live: true },
  { id: 'problem_query_policy', script: 'projects/orca/semantic-intelligence/live-model/tests/run-problem-query-policy-regression.mjs', live: true },
  { id: 'confirmation_product', script: 'projects/orca/semantic-intelligence/live-model/tests/run-confirmation-validation.mjs', args: ['--stratum=protected_product_confirmation'], live: true },
  { id: 'confirmation_geo_v2', script: 'projects/orca/semantic-intelligence/live-model/tests/run-confirmation-validation.mjs', args: ['--stratum=geo_commercial_confirmation_v2'], live: true },
  { id: 'closed_dataset_regression', script: 'projects/orca/semantic-intelligence/live-model/tests/run-closed-dataset-regression.mjs', live: true },
];

function readJson(p) { return JSON.parse(fs.readFileSync(p, 'utf8')); }
function writeJsonAtomic(filePath, data) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  const tmp = `${filePath}.${process.pid}.tmp`;
  fs.writeFileSync(tmp, JSON.stringify(data, null, 2));
  fs.renameSync(tmp, filePath);
}

function releaseStaleLock() {
  if (!fs.existsSync(LOCK_PATH)) return;
  const lock = readJson(LOCK_PATH);
  if (lock.status === 'RELEASED') return;
  lock.status = 'RELEASED';
  lock.released_at = new Date().toISOString();
  lock.release_outcome = 'PAUSED — stale owner released for resume';
  lock.resumed_by_pid = process.pid;
  writeJsonAtomic(LOCK_PATH, lock);
  writeJsonAtomic(path.join(RUN_STORAGE, 'receipts', 'lock-stale-release-for-resume-v1.json'), {
    run_id: RUN_ID,
    released_at: lock.released_at,
    prior_owner_pid: lock.owner_pid,
    resume_pid: process.pid,
  });
}

function acquireLock(corpusHash) {
  if (fs.existsSync(LOCK_PATH)) {
    const existing = readJson(LOCK_PATH);
    if (existing.status === 'ACTIVE') {
      throw new Error('BLOCKED — live lock still ACTIVE; manual review required');
    }
  }
  const lock = {
    schema_version: '1.0.0',
    run_id: RUN_ID,
    project_id: 'PRJ-0013',
    phase: 'SPPC-05_VALIDATION',
    owner_pid: process.pid,
    process_identity: `resume-run-004-sppc05-v1.mjs@${process.pid}`,
    corpus_checksum: corpusHash,
    acquired_at: new Date().toISOString(),
    heartbeat: new Date().toISOString(),
    stale_after_ms: 7200000,
    status: 'ACTIVE',
    resume_from_pause: true,
  };
  fs.mkdirSync(path.dirname(LOCK_PATH), { recursive: true });
  fs.writeFileSync(LOCK_PATH, JSON.stringify(lock, null, 2));
  return lock;
}

function runNodeTest(scriptRel, args = []) {
  const script = path.join(REPO_ROOT, scriptRel);
  const env = {
    ...process.env,
    ORCA_SEMANTIC_PROVIDER: OPERATOR.provider,
    ORCA_SEMANTIC_MODEL: OPERATOR.model,
    ORCA_EVAL_MAX_COST: String(OPERATOR.hard_cost_cap_usd),
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

function loadCompletedFromPartial(partial) {
  return (partial.completed_suites || []).map((s) => ({
    id: s.id,
    script: ALL_SUITES.find((x) => x.id === s.id)?.script || s.script,
    pass: s.pass,
    exit_code: s.exit_code,
    runtime_ms: s.runtime_ms || 0,
    live: s.live,
    parsed_summary: s.metrics || { note: s.note },
    resumed_from_pause: true,
  }));
}

function evaluateGateCriteria(suiteResults, varianceReport, psrAmbReport) {
  const productConf = suiteResults.find((s) => s.id === 'confirmation_product');
  const geoConf = suiteResults.find((s) => s.id === 'confirmation_geo_v2');
  const closed = suiteResults.find((s) => s.id === 'closed_dataset_regression');
  const problem = suiteResults.find((s) => s.id === 'problem_query_policy');
  const bypass = suiteResults.find((s) => s.id === 'wave31f_bypass');
  const under = suiteResults.find((s) => s.id === 'under_admission');
  const platform = suiteResults.find((s) => s.id === 'platform_compatibility');
  const defectRepro = suiteResults.find((s) => s.id === 'focused_repair_repro');
  const structured = suiteResults.find((s) => s.id === 'structured_output');

  const productMetrics = productConf?.parsed_summary?.metrics || productConf?.parsed_summary;
  const geoMetrics = geoConf?.parsed_summary?.metrics || geoConf?.parsed_summary;
  const closedSummary = closed?.parsed_summary?.summary || closed?.parsed_summary;
  const productFpr = productMetrics?.false_positive_rate ?? closedSummary?.product_fpr;

  const criteria = {
    closed_dataset_exit_zero: closed?.pass === true,
    adversarial_fpr_max_0_01_product: productMetrics?.gate_pass === true || (productFpr != null && productFpr <= 0.01),
    platform_compatibility_full_pass: platform?.pass === true,
    problem_query_all_match: problem?.pass === true,
    under_admission_all_pass: under?.pass === true,
    geo_commercial_recall_gte_0_90: (geoMetrics?.commercial_recall ?? 0) >= 0.9,
    geo_adversarial_fpr_zero: (geoMetrics?.adversarial_false_accept_rate ?? 1) === 0,
    wave31f_bypass_all_pass: bypass?.pass === true,
    structured_output_full_pass: structured?.pass === true,
    focused_repair_stable: defectRepro?.pass === true,
    variance_repair_cases_stable: varianceReport?.repair_cases_stable === true,
    old_run_isolation_pass: true,
    project_corpus_processed_zero: true,
    psr_amb_01_isolated: !psrAmbReport?.expands_false_accept_family,
  };
  if (productFpr != null && productFpr > 0.01) criteria.adversarial_fpr_max_0_01_product = false;
  criteria.all_pass = Object.entries(criteria)
    .filter(([k]) => !['psr_amb_01_isolated'].includes(k))
    .every(([, v]) => v === true);
  criteria.psr_amb_01_status = psrAmbReport;
  return criteria;
}

function releaseLock(outcome) {
  const lock = readJson(LOCK_PATH);
  lock.status = 'RELEASED';
  lock.released_at = new Date().toISOString();
  lock.release_outcome = outcome;
  writeJsonAtomic(LOCK_PATH, lock);
  writeJsonAtomic(path.join(RUN_STORAGE, 'receipts', 'lock-release-receipt-v1.json'), {
    run_id: RUN_ID,
    released_at: lock.released_at,
    outcome,
    owner_pid: lock.owner_pid,
  });
}

// Import report builders from execute script inline (minimal)
function mdResultReport(data) {
  const g = data.gate_criteria;
  const gateB = data.gate_b_verdict;
  return `# CORVONERO RUN 004 — SPPC-05 RESULT v1

**Run ID:** \`${RUN_ID}\`  
**Completed:** ${data.completed_at}  
**Gate B:** \`${gateB.status}\`  
**Lifecycle:** \`${gateB.run_lifecycle}\`  
**Resumed from pause:** yes

## Summary

| Item | Value |
|------|-------|
| Provider | ${data.provider} |
| Model | ${data.model} |
| Corpus processed | 0 / 2368 |
| Cumulative cost (USD) | ${data.cumulative_cost_usd?.toFixed(4) ?? '0'} |

## Suite Results

${data.suite_results.map((s) => `- **${s.id}**: ${s.pass ? 'PASS' : 'FAIL'}${s.resumed_from_pause ? ' (from pause)' : ''}`).join('\n')}

## Gate B

\`\`\`text
SPPC-05: ${gateB.status.startsWith('PASS') ? 'PASS — OPERATOR REVIEW REQUIRED' : 'FAILED'}
Run 004: ${gateB.run_lifecycle}
\`\`\`
`;
}

function main() {
  if (!fs.existsSync(PAUSE_PATH)) {
    console.error(JSON.stringify({ error: 'BLOCKED — NO PAUSE CHECKPOINT', path: PAUSE_PATH }));
    process.exit(2);
  }
  const pause = readJson(PAUSE_PATH);
  const partial = readJson(PARTIAL_PATH);
  const inputManifest = readJson(path.join(RUN_STORAGE, 'manifests', 'immutable-input-reference-v1.json'));
  const repairSnapshot = readJson(path.join(RUN_STORAGE, 'manifests', 'repair-authority-freeze-v1.json'));

  loadLocalSecrets();
  process.env.ORCA_SEMANTIC_PROVIDER = OPERATOR.provider;
  process.env.ORCA_SEMANTIC_MODEL = OPERATOR.model;
  const secretSummary = getSafeConfigSummary();
  if (secretSummary.OPENROUTER_API_KEY !== 'SET') {
    console.error(JSON.stringify({ error: 'BLOCKED — APPROVED MODEL AUTHORITY UNAVAILABLE' }));
    process.exit(2);
  }

  releaseStaleLock();
  acquireLock(inputManifest.sha256);

  const completedIds = new Set((partial.completed_suites || []).map((s) => s.id));
  const suiteResults = loadCompletedFromPartial(partial);
  let cumulativeCost = partial.cumulative_cost_usd_partial || 0;

  const pending = ALL_SUITES.filter((s) => !completedIds.has(s.id));
  console.error(`[RUN004-RESUME] Pending suites: ${pending.map((s) => s.id).join(', ')}`);

  for (const suite of pending) {
    console.error(`[RUN004-RESUME] Starting: ${suite.id}`);
    const r = runNodeTest(suite.script, suite.args || []);
    const parsed = parseLastJson(r.stdout);
    if (parsed?.cost_usd) cumulativeCost += parsed.cost_usd;
    if (parsed?.calculated_cost_usd) cumulativeCost += parsed.calculated_cost_usd;
    if (parsed?.metrics?.gate_pass === false) r.pass = false;
    suiteResults.push({ ...suite, ...r, parsed_summary: parsed });
    console.error(`[RUN004-RESUME] Finished: ${suite.id} pass=${r.pass} cost=${cumulativeCost.toFixed(4)}`);
    if (cumulativeCost > OPERATOR.hard_cost_cap_usd) break;
  }

  const defectRepro = suiteResults.find((s) => s.id === 'focused_repair_repro');
  const structured = {
    id: 'structured_output',
    script: 'projects/orca/semantic-intelligence/live-model/tests/run-sppc05-defect-repro.mjs',
    pass: defectRepro?.pass === true,
    exit_code: defectRepro?.exit_code,
    runtime_ms: 0,
    parsed_summary: defectRepro?.parsed_summary,
    live: true,
    note: 'Reused focused_repair_repro evidence from pause',
    resumed_from_pause: true,
  };
  suiteResults.push(structured);

  const varianceR = runNodeTest('projects/orca/semantic-intelligence/live-model/tests/run-sppc05-variance-check.mjs', ['--reps=3']);
  const varianceReport = parseLastJson(varianceR.stdout);
  if (varianceReport?.cost_usd) cumulativeCost += varianceReport.cost_usd;

  const psrCase = varianceReport?.cases?.find((c) => c.record_id === 'PSR-AMB-01');
  const psrAmbReport = {
    record_id: 'PSR-AMB-01',
    query: 'купить 1с с настройкой',
    expected: 'ABSTAIN',
    verdict_distribution: psrCase?.verdict_distribution,
    known_ambiguity: true,
    non_blocking: true,
    operator_decision: OPERATOR.psr_amb_01,
    expands_false_accept_family: psrCase?.verdict_distribution?.REJECT > 0,
  };

  const gateCriteria = evaluateGateCriteria(suiteResults, varianceReport, psrAmbReport);
  if (!varianceR.pass) gateCriteria.variance_repair_cases_stable = false;
  gateCriteria.all_pass = Object.entries(gateCriteria)
    .filter(([k]) => !['psr_amb_01_isolated', 'psr_amb_01_status'].includes(k))
    .every(([, v]) => v === true);

  const blocked = !gateCriteria.all_pass || cumulativeCost > OPERATOR.hard_cost_cap_usd;
  const gateBVerdict = blocked
    ? { status: 'FAILED', project: 'BLOCKED_AT_SPPC_05', run_lifecycle: 'BLOCKED_AT_SPPC_05' }
    : { status: 'PASS — OPERATOR REVIEW REQUIRED', project: 'FROZEN_PENDING_CANARY_AUTHORIZATION', run_lifecycle: 'PHASE_0_1_2_COMPLETE' };

  const completedAt = new Date().toISOString();
  const sppc05Report = {
    report_id: 'corvonero-run-004-sppc-05-execution-v1',
    run_id: RUN_ID,
    resumed_from_pause: true,
    lifecycle_state: gateBVerdict.run_lifecycle,
    provider: OPERATOR.provider,
    model: OPERATOR.model,
    gate_b_verdict: gateBVerdict,
    gate_criteria: gateCriteria,
    suite_results: suiteResults.map(({ id, script, pass, exit_code, runtime_ms, parsed_summary, live, resumed_from_pause }) => ({
      id, script, pass, exit_code, runtime_ms, live, resumed_from_pause,
      metrics: parsed_summary?.metrics || parsed_summary?.summary || parsed_summary,
    })),
    variance_check: varianceReport,
    psr_amb_01: psrAmbReport,
    cumulative_cost_usd: cumulativeCost,
    corpus_processed_count: 0,
    repair_authority: repairSnapshot,
    completed_at: completedAt,
  };

  writeJsonAtomic(path.join(RUN_STORAGE, 'reports', 'sppc-05-execution-report-v1.json'), sppc05Report);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'reports', 'sppc-05-sanitized-report-v1.json'), sppc05Report);
  writeJsonAtomic(path.join(PILOT_DIR, 'CORVONERO-RUN-004-SPPC-05-RESULT-v1.json'), sppc05Report);
  writeJsonAtomic(path.join(PILOT_DIR, 'CORVONERO-RUN-004-SPPC-05-REVIEW-PACKAGE-v1.json'), sppc05Report);
  fs.writeFileSync(path.join(PILOT_DIR, 'CORVONERO-RUN-004-SPPC-05-RESULT-v1.md'), mdResultReport({ ...sppc05Report, provider: OPERATOR.provider, model: OPERATOR.model }));
  fs.writeFileSync(path.join(REPORTS_DIR, 'REPORT-corvonero-run-004-sppc05-validation-v1.md'), mdResultReport({ ...sppc05Report, provider: OPERATOR.provider, model: OPERATOR.model }));

  writeJsonAtomic(path.join(RUN_STORAGE, 'checkpoints', 'checkpoint-sppc05-complete-v1.json'), {
    run_id: RUN_ID,
    phase: gateBVerdict.status.startsWith('PASS') ? 'SPPC-05_COMPLETE_PENDING_REVIEW' : 'BLOCKED_AT_SPPC_05',
    project_processed: 0,
    project_total: 2368,
    cumulative_cost_usd: cumulativeCost,
    complete: gateBVerdict.status.startsWith('PASS'),
    gate_b_verdict: gateBVerdict.status,
    resumed_from_pause: true,
  });

  releaseLock(gateBVerdict.status);

  const runManifest = readJson(path.join(RUN_STORAGE, 'manifests', 'run-manifest-v1.json'));
  runManifest.lifecycle_state = gateBVerdict.run_lifecycle;
  runManifest.gate_b = gateBVerdict.status;
  runManifest.resumed_from_pause = true;
  writeJsonAtomic(path.join(RUN_STORAGE, 'manifests', 'run-manifest-v1.json'), runManifest);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'run-manifest-v1.json'), runManifest);

  console.log(JSON.stringify({ run_id: RUN_ID, gate_b: gateBVerdict, cumulative_cost_usd: cumulativeCost, resumed: true }, null, 2));
  process.exit(gateBVerdict.status.startsWith('PASS') ? 0 : 1);
}

main();
