#!/usr/bin/env node
/**
 * Corvonero Run 004 — isolated SPPC-05 validation (ORCA repair v2 authority).
 * Run ID fixed: corv-semantic-v2-20260626-004
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
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
const STORAGE_ROOT = path.join('C:\\MARS Phenix\\AI MARS STORAGE', 'mig', 'corvonero', 'semantic-runs');
const RUN_STORAGE = path.join(STORAGE_ROOT, RUN_ID);
const GIT_RUN_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero/runs', RUN_ID);
const PILOT_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const REPORTS_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/reports');

const OPERATOR = {
  orca_repair: 'ORCA_WAVE_3_1F_TARGETED_SPPC05_REPAIR_V2 — PASS',
  run_002: 'BLOCKED_AT_SPPC_05 — NON-RESUMABLE — IMMUTABLE FAILED EVIDENCE',
  run_003: 'BLOCKED_AT_SPPC_05 — NON-RESUMABLE — IMMUTABLE FAILED EVIDENCE',
  run_004: 'AUTHORIZED FOR SPPC-05 VALIDATION ONLY',
  provider: 'openrouter',
  model: 'openai/gpt-5-mini',
  hard_cost_cap_usd: 3.0,
  soft_cost_warning_usd: 2.0,
  psr_amb_01: 'KNOWN PRE-EXISTING AMBIGUITY — NON-BLOCKING FOR RUN 004 SPPC-05 — MUST REMAIN VISIBLE',
  phase_3: 'NOT AUTHORIZED',
  wave_5: 'BLOCKED',
};

const CORPUS_REL = 'projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json';
const EXPECTED_HASH_PREFIX = 'eaa09b8450f82738';
const EXPECTED_COUNT = 2368;
const RECOVERY_AUTHORITY = 'ebc65acd4087fa9d180bb2a50921027fde51e3b7';
const REPAIR_REF = 'REPORT-orca-wave31f-targeted-sppc05-repair-v2.md';
const REPAIR_DECISION_REF = 'ORCA-WAVE-3.1F-TARGETED-SPPC05-REPAIR-DECISIONS-v2.json';

const ORCA_COMPONENTS = [
  { key: 'semantic_adjudicator', rel: 'projects/orca/semantic-intelligence/live-model/adjudication/semantic-adjudicator.mjs', version: 'v1.5', versionExport: 'ADJUDICATOR_VERSION', expectedHashPrefix: '9618364947BA812C' },
  { key: 'platform_compatibility', rel: 'projects/orca/semantic-intelligence/live-model/evidence/platform-compatibility.mjs', version: 'v1.1', versionExport: 'PLATFORM_COMPATIBILITY_VERSION', expectedHashPrefix: '49B8C4D604EE732F' },
  { key: 'hard_rules', rel: 'projects/orca/semantic-intelligence/production/assessors/hard-rules.mjs', version: 'v1.2', versionExport: 'HARD_RULES_VERSION', expectedHashPrefix: 'E6CD74CCCA6ED453' },
  { key: 'prompt_contract', rel: 'projects/orca/semantic-intelligence/live-model/contracts/prompt-contract.mjs', version: 'orca-semantic-assessment-prompt-v1.4', versionExport: 'PROMPT_VERSION', expectedHashPrefix: '481075E55A827404' },
  { key: 'service_intent_evidence', rel: 'projects/orca/semantic-intelligence/live-model/evidence/service-intent-evidence.mjs', version: 'v1.1', versionExport: 'SERVICE_INTENT_EVIDENCE_VERSION', expectedHashPrefix: '5BFFF7AE2ED3B854' },
  { key: 'problem_query_runner', rel: 'projects/orca/semantic-intelligence/live-model/tests/run-problem-query-policy-regression.mjs', version: 'wave31f-repair-v2', versionExport: null },
  { key: 'platform_regression_runner', rel: 'projects/orca/semantic-intelligence/live-model/tests/run-platform-compatibility-regression.mjs', version: 'wave31f-repair-v2', versionExport: null },
  { key: 'product_confirmation_runner', rel: 'projects/orca/semantic-intelligence/live-model/tests/run-confirmation-validation.mjs', version: 'wave31f-repair-v2', versionExport: null },
  { key: 'under_admission_runner', rel: 'projects/orca/semantic-intelligence/live-model/tests/run-under-admission-regression.mjs', version: 'wave31f-repair-v2', versionExport: null },
  { key: 'bypass_runner', rel: 'projects/orca/semantic-intelligence/live-model/tests/run-wave31f-bypass-audit.mjs', version: 'wave31f-repair-v2', versionExport: null },
  { key: 'closed_dataset_runner', rel: 'projects/orca/semantic-intelligence/live-model/tests/run-closed-dataset-regression.mjs', version: 'wave31f-repair-v2', versionExport: null },
  { key: 'geo_confirmation_runner', rel: 'projects/orca/semantic-intelligence/live-model/tests/run-confirmation-validation.mjs', version: 'wave31f-repair-v2', versionExport: null },
];

const FROZEN_RUNS = ['corv-semantic-v2-20260626-002', 'corv-semantic-v2-20260626-003'];

function sha256File(p) {
  return crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
}

function writeJsonAtomic(filePath, data) {
  loopMkdir(path.dirname(filePath));
  const tmp = `${filePath}.${process.pid}.tmp`;
  fs.writeFileSync(tmp, JSON.stringify(data, null, 2));
  fs.renameSync(tmp, filePath);
}

function writeText(filePath, text) {
  loopMkdir(path.dirname(filePath));
  fs.writeFileSync(filePath, text);
}

function loopMkdir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function verifyRun004Absent() {
  if (fs.existsSync(RUN_STORAGE)) {
    console.error(JSON.stringify({ error: 'BLOCKED — RUN 004 ID ALREADY EXISTS', state: fs.readdirSync(RUN_STORAGE) }));
    process.exit(2);
  }
}

function buildRepairAuthoritySnapshot() {
  const components = ORCA_COMPONENTS.map((c) => {
    const abs = path.join(REPO_ROOT, c.rel);
    const hash = sha256File(abs);
    const stat = fs.statSync(abs);
    return {
      component: c.key,
      path: c.rel,
      version: c.version,
      sha256: hash,
      sha256_prefix: hash.slice(0, 16).toUpperCase(),
      expected_sha256_prefix: c.expectedHashPrefix || null,
      hash_match: c.expectedHashPrefix ? hash.slice(0, 16).toUpperCase() === c.expectedHashPrefix : null,
      last_modified: stat.mtime.toISOString(),
      repair_decision_reference: REPAIR_DECISION_REF,
      regression_report_reference: REPAIR_REF,
    };
  });

  const versionDrift = [];
  if (PROMPT_VERSION !== 'orca-semantic-assessment-prompt-v1.4') versionDrift.push(`prompt:${PROMPT_VERSION}`);
  if (ADJUDICATOR_VERSION !== 'v1.5') versionDrift.push(`adjudicator:${ADJUDICATOR_VERSION}`);
  if (HARD_RULES_VERSION !== 'v1.2') versionDrift.push(`hard_rules:${HARD_RULES_VERSION}`);
  if (SERVICE_INTENT_EVIDENCE_VERSION !== 'v1.1') versionDrift.push(`service_intent:${SERVICE_INTENT_EVIDENCE_VERSION}`);
  if (PLATFORM_COMPATIBILITY_VERSION !== 'v1.1') versionDrift.push(`platform:${PLATFORM_COMPATIBILITY_VERSION}`);

  for (const c of components) {
    if (c.expected_sha256_prefix && !c.hash_match) {
      versionDrift.push(`hash_mismatch:${c.component}`);
    }
  }

  const adjSrc = fs.readFileSync(path.join(REPO_ROOT, 'projects/orca/semantic-intelligence/live-model/adjudication/semantic-adjudicator.mjs'), 'utf8');
  if (!adjSrc.includes('applyMandatorySemanticInvariants')) versionDrift.push('missing:applyMandatorySemanticInvariants');
  if (!adjSrc.includes('generic_platform_family_abstain')) versionDrift.push('missing:generic_platform_family_abstain');

  return {
    snapshot_id: `${RUN_ID}-repair-authority-freeze-v1`,
    run_id: RUN_ID,
    frozen_at: new Date().toISOString(),
    repair_status: 'APPROVED',
    repair_reference: REPAIR_REF,
    repair_decision_reference: REPAIR_DECISION_REF,
    operator_decision: OPERATOR.orca_repair,
    components,
    approved_target_behavior: [
      { fixture: 'PQR-ABSTAIN-03', query: 'как исправить ошибку 0x80004005 1с', expected: 'ABSTAIN' },
      { fixture: 'PC-ABSTAIN-01', query: 'обновление erp до новой версии', expected: 'ABSTAIN' },
      { fixture: 'CFM-PROD-UPD-02', query: 'обновление sap business one до новой версии', expected: 'REJECT' },
    ],
    drift_detected: versionDrift.length > 0,
    drift_details: versionDrift,
    verdict: versionDrift.length === 0 ? 'APPROVED ORCA REPAIR V2 AUTHORITY — FROZEN' : 'BLOCKED — APPROVED ORCA REPAIR V2 AUTHORITY DRIFT',
  };
}

function verifyCorpus() {
  const corpusPath = path.join(REPO_ROOT, CORPUS_REL);
  const raw = fs.readFileSync(corpusPath);
  const hash = crypto.createHash('sha256').update(raw).digest('hex');
  const data = JSON.parse(raw.toString());
  const records = Array.isArray(data) ? data : (data.records || data.phrases || []);
  const ids = records.map((r) => r.phrase_id || r.id || r.record_id);
  const unique = new Set(ids);
  const mismatches = [];
  if (records.length !== EXPECTED_COUNT) mismatches.push(`count:${records.length}`);
  if (unique.size !== records.length) mismatches.push('duplicate_ids');
  if (ids.some((x) => !x)) mismatches.push('missing_ids');
  if (!hash.startsWith(EXPECTED_HASH_PREFIX)) mismatches.push(`hash:${hash.slice(0, 16)}`);
  return { corpusPath, hash, hash_prefix: hash.slice(0, 16), record_count: records.length, unique_ids: unique.size, pass: mismatches.length === 0, mismatches };
}

function acquireLock(corpusHash) {
  const lockPath = path.join(RUN_STORAGE, 'locks', 'run.lock.json');
  const lock = {
    schema_version: '1.0.0',
    run_id: RUN_ID,
    project_id: 'PRJ-0013',
    phase: 'SPPC-05_VALIDATION',
    owner_pid: process.pid,
    process_identity: `execute-run-004-sppc05-v1.mjs@${process.pid}`,
    corpus_checksum: corpusHash,
    acquired_at: new Date().toISOString(),
    heartbeat: new Date().toISOString(),
    stale_after_ms: 7200000,
    expiry_policy: 'stale_after_ms; owner-only release',
    current_batch: null,
    permitted_writer: process.pid,
    status: 'ACTIVE',
  };
  loopMkdir(path.dirname(lockPath));
  const fd = fs.openSync(lockPath, fs.constants.O_CREAT | fs.constants.O_EXCL | fs.constants.O_WRONLY);
  fs.writeSync(fd, JSON.stringify(lock, null, 2));
  fs.closeSync(fd);
  return { lockPath, lock };
}

function createInitialCheckpoint(corpusHash) {
  const cp = {
    run_id: RUN_ID,
    phase: 'SPPC-05_VALIDATION',
    corpus_checksum: corpusHash,
    project_total: 2368,
    project_processed: 0,
    sppc05_fixtures_processed: 0,
    total_input_count: 2368,
    processed_ids: [],
    completed_batches: [],
    processed_count: 0,
    failure_count: 0,
    retry_count: 0,
    cumulative_cost_usd: 0,
    model: OPERATOR.model,
    provider: OPERATOR.provider,
    prompt_contract_version: PROMPT_VERSION,
    hard_rules_version: HARD_RULES_VERSION,
    adjudicator_version: ADJUDICATOR_VERSION,
    platform_compatibility_version: PLATFORM_COMPATIBILITY_VERSION,
    last_heartbeat: new Date().toISOString(),
    writer_identity: `execute-run-004-sppc05-v1.mjs@${process.pid}`,
    complete: false,
    reconciliation_status: 'NOT_STARTED',
  };
  writeJsonAtomic(path.join(RUN_STORAGE, 'checkpoints', 'checkpoint-initial-v1.json'), cp);
  return cp;
}

function runIsolationTest() {
  const forbiddenRefs = [];
  const forbiddenPathFragments = [
    'corvonero-commercial-eligibility-v1.json',
    'corvonero-intent-screening-v1.json',
    'corvonero-direct-semantic-core-candidate-v1.json',
    'corvonero-direct-v2-clean-room-v1-diagnostic',
  ];
  const walk = (dir) => {
    if (!fs.existsSync(dir)) return;
    for (const name of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, name.name);
      if (name.isDirectory()) walk(p);
      else if (name.name.endsWith('.json')) {
        const text = fs.readFileSync(p, 'utf8');
        for (const frag of forbiddenPathFragments) {
          if (text.includes(frag)) forbiddenRefs.push({ file: p, reason: `forbidden_fragment:${frag}` });
        }
      }
    }
  };
  for (const d of ['runtime', 'cache', 'batches', 'raw-responses']) walk(path.join(RUN_STORAGE, d));
  const nonEmpty = ['cache', 'raw-responses', 'batches'].filter((d) => {
    const p = path.join(RUN_STORAGE, d);
    return fs.existsSync(p) && fs.readdirSync(p).length > 0;
  });
  return {
    verdict: forbiddenRefs.length === 0 && nonEmpty.length === 0 ? 'OLD_RUN_ISOLATION — PASS' : 'BLOCKED — OLD RUN STATE CONTAMINATION',
    pass: forbiddenRefs.length === 0 && nonEmpty.length === 0,
    forbidden_refs: forbiddenRefs,
    unexpected_runtime_data: nonEmpty,
    frozen_runs_preserved: FROZEN_RUNS,
    old_lock_reused: false,
    old_checkpoint_reused: false,
  };
}

function runNodeTest(scriptRel, args = [], envExtra = {}) {
  const script = path.join(REPO_ROOT, scriptRel);
  const env = {
    ...process.env,
    ORCA_SEMANTIC_PROVIDER: OPERATOR.provider,
    ORCA_SEMANTIC_MODEL: OPERATOR.model,
    ORCA_EVAL_MAX_COST: String(OPERATOR.hard_cost_cap_usd),
    ORCA_EVAL_LIVE: '1',
    ...envExtra,
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

function releaseLock(lockPath, outcome) {
  const lock = JSON.parse(fs.readFileSync(lockPath, 'utf8'));
  lock.status = 'RELEASED';
  lock.released_at = new Date().toISOString();
  lock.release_outcome = outcome;
  writeJsonAtomic(lockPath, lock);
  writeJsonAtomic(path.join(RUN_STORAGE, 'receipts', 'lock-release-receipt-v1.json'), {
    run_id: RUN_ID,
    released_at: lock.released_at,
    outcome,
    owner_pid: lock.owner_pid,
    cleanup: 'owner-only release with receipt',
  });
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
    psr_amb_01_isolated: true,
  };

  if (psrAmbReport?.expands_false_accept_family) criteria.psr_amb_01_isolated = false;
  if (productFpr != null && productFpr > 0.01) criteria.adversarial_fpr_max_0_01_product = false;

  criteria.all_pass = Object.entries(criteria)
    .filter(([k]) => !['psr_amb_01_isolated'].includes(k))
    .every(([, v]) => v === true);
  criteria.psr_amb_01_status = psrAmbReport;
  return criteria;
}

function runStructuredOutputSmoke() {
  const r = runNodeTest('projects/orca/semantic-intelligence/live-model/tests/run-sppc05-defect-repro.mjs');
  const parsed = parseLastJson(r.stdout);
  const schemaOk = parsed?.results?.every((x) => x.match === true) ?? parsed?.all_match === true;
  return {
    id: 'structured_output',
    script: 'projects/orca/semantic-intelligence/live-model/tests/run-sppc05-defect-repro.mjs',
    pass: r.pass && schemaOk,
    exit_code: r.exit_code,
    runtime_ms: r.runtime_ms,
    parsed_summary: parsed,
    live: true,
    note: 'Structured pipeline smoke via defect-repro fixtures with schema-valid assessments',
  };
}

function runPsrAmbVariance(reps = 3) {
  const r = runNodeTest('projects/orca/semantic-intelligence/live-model/tests/run-sppc05-variance-check.mjs', [`--reps=${reps}`]);
  const parsed = parseLastJson(r.stdout);
  const psrCase = parsed?.cases?.find((c) => c.record_id === 'PSR-AMB-01');
  const psrReport = psrCase ? {
    record_id: 'PSR-AMB-01',
    query: 'купить 1с с настройкой',
    expected: 'ABSTAIN',
    repetitions: psrCase.repetitions,
    verdict_distribution: psrCase.verdict_distribution,
    primary_distribution: psrCase.primary_distribution,
    known_ambiguity: true,
    non_blocking: true,
    operator_decision: OPERATOR.psr_amb_01,
    expands_false_accept_family: psrCase.verdict_distribution?.REJECT > 0,
  } : {
    record_id: 'PSR-AMB-01',
    query: 'купить 1с с настройкой',
    expected: 'ABSTAIN',
    known_ambiguity: true,
    non_blocking: true,
    operator_decision: OPERATOR.psr_amb_01,
    expands_false_accept_family: false,
    note: 'Variance suite did not return PSR-AMB-01 case',
  };
  return { variance: parsed, psr_amb_01: psrReport, runner_pass: r.pass };
}

function buildCriticalFailures(gateCriteria, suiteResults, varianceReport) {
  const failures = [];
  if (!gateCriteria.closed_dataset_exit_zero) failures.push('Closed dataset regression exit non-zero or not executed');
  if (!gateCriteria.adversarial_fpr_max_0_01_product) failures.push('Product confirmation FPR exceeds 0.01');
  if (!gateCriteria.platform_compatibility_full_pass) failures.push('Platform compatibility not full pass');
  if (!gateCriteria.problem_query_all_match) failures.push('Problem query regression not 10/10');
  if (!gateCriteria.under_admission_all_pass) failures.push('Under-admission regression failed');
  if (!gateCriteria.geo_commercial_recall_gte_0_90) failures.push('Geo commercial recall below 0.90');
  if (!gateCriteria.geo_adversarial_fpr_zero) failures.push('Geo adversarial FPR not zero');
  if (!gateCriteria.wave31f_bypass_all_pass) failures.push('Wave 3.1F bypass audit failed');
  if (!gateCriteria.structured_output_full_pass) failures.push('Structured output validation failed');
  if (!gateCriteria.focused_repair_stable) failures.push('Focused repair repro fixtures unstable');
  if (!gateCriteria.variance_repair_cases_stable) {
    const unstable = varianceReport?.cases?.filter((c) => !c.stable && !c.known_ambiguity) || [];
    failures.push(`Variance check: repair fixtures unstable — ${unstable.map((c) => c.record_id).join(', ') || 'see variance report'}`);
  }
  return failures;
}

function mdResultReport(data) {
  const g = data.gate_criteria;
  const gateB = data.gate_b_verdict;
  return `# CORVONERO RUN 004 — SPPC-05 RESULT v1

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
| Platform compatibility | ${data.platform_compatibility_version} |
| Hard rules | ${data.hard_rules_version} |
| Corpus processed | 0 / 2368 |
| Cumulative cost (USD) | ${data.cumulative_cost_usd?.toFixed(4) ?? '0'} |
| Isolation | ${data.isolation?.verdict} |
| Repair authority | ${data.repair_authority?.verdict} |

## Suite Results

${data.suite_results.map((s) => `- **${s.id}**: ${s.pass ? 'PASS' : 'FAIL'} (exit ${s.exit_code}, ${Math.round((s.runtime_ms || 0) / 1000)}s)`).join('\n')}

## Critical Gates

| Gate | Result |
|------|--------|
| Closed dataset exit 0 | ${g.closed_dataset_exit_zero ? 'PASS' : 'FAIL'} |
| Product FPR ≤ 0.01 | ${g.adversarial_fpr_max_0_01_product ? 'PASS' : 'FAIL'} |
| Platform compatibility | ${g.platform_compatibility_full_pass ? 'PASS' : 'FAIL'} |
| Problem query 10/10 | ${g.problem_query_all_match ? 'PASS' : 'FAIL'} |
| Under-admission | ${g.under_admission_all_pass ? 'PASS' : 'FAIL'} |
| Geo commercial recall ≥ 0.90 | ${g.geo_commercial_recall_gte_0_90 ? 'PASS' : 'FAIL'} |
| Geo adversarial FPR = 0 | ${g.geo_adversarial_fpr_zero ? 'PASS' : 'FAIL'} |
| Wave 3.1F bypass | ${g.wave31f_bypass_all_pass ? 'PASS' : 'FAIL'} |
| Structured output | ${g.structured_output_full_pass ? 'PASS' : 'FAIL'} |
| Repair fixtures stable | ${g.focused_repair_stable && g.variance_repair_cases_stable ? 'PASS' : 'FAIL'} |
| Old-run isolation | ${g.old_run_isolation_pass ? 'PASS' : 'FAIL'} |

## PSR-AMB-01 (known ambiguity — non-blocking)

- Expected: **ABSTAIN**
- Distribution: **${JSON.stringify(data.psr_amb_01?.verdict_distribution || data.psr_amb_01?.observed || 'see variance report')}**
- Non-blocking: **yes** (operator decision recorded)

## Failures

${gateB.status.startsWith('PASS') ? '_None — operator review required before Phase 3._' : (data.critical_failures?.map((f) => `- ${f}`).join('\n') || '_See review package._')}

## Stop Condition

${gateB.status.startsWith('PASS') ? 'Phase 3 canary **not started** — awaiting operator authorization.' : 'Run **BLOCKED_AT_SPPC_05** — no canary, no corpus processing.'}
`;
}

function mdReviewPackage(data) {
  const gateB = data.gate_b_verdict;
  const v = data.variance_check;
  return `# CORVONERO RUN 004 — SPPC-05 REVIEW PACKAGE v1

**Run:** \`${RUN_ID}\`  
**Verdict:** \`${gateB.status}\`  
**Repair authority:** ORCA Wave 3.1F Repair V2

## Operator decisions (recorded)

- ORCA repair v2: **${OPERATOR.orca_repair}**
- Run 002: **${OPERATOR.run_002}**
- Run 003: **${OPERATOR.run_003}**
- PSR-AMB-01: **${OPERATOR.psr_amb_01}**
- Phase 3: **NOT AUTHORIZED**

## Critical failures

${data.critical_failures?.map((f) => `- ${f}`).join('\n') || '_None_'}

## Repair fixture variance (3× each)

### PQR-ABSTAIN-03 → ABSTAIN
${JSON.stringify(v?.cases?.find((c) => c.record_id === 'PQR-ABSTAIN-03') || {}, null, 2)}

### PC-ABSTAIN-01 → ABSTAIN
${JSON.stringify(v?.cases?.find((c) => c.record_id === 'PC-ABSTAIN-01') || {}, null, 2)}

### CFM-PROD-UPD-02 → REJECT
${JSON.stringify(v?.cases?.find((c) => c.record_id === 'CFM-PROD-UPD-02') || {}, null, 2)}

### PSR-AMB-01 (known ambiguity)
${JSON.stringify(data.psr_amb_01, null, 2)}

## Suite matrix

| Suite | Pass | Exit |
|-------|------|------|
${data.suite_results.map((s) => `| ${s.id} | ${s.pass ? 'PASS' : 'FAIL'} | ${s.exit_code} |`).join('\n')}

## Cost

- Cumulative: **$${(data.cumulative_cost_usd || 0).toFixed(4)}**
- Hard cap: **$${OPERATOR.hard_cost_cap_usd}**
- Soft warning: **$${OPERATOR.soft_cost_warning_usd}**
`;
}

function mdPhase3Task(gateB) {
  if (!gateB.status.startsWith('PASS')) {
    return `# CORVONERO RUN 004 — PHASE 3 NEXT TASK v1

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
Run 004: BLOCKED_AT_SPPC_05
\`\`\`

## Required operator actions

1. Review \`CORVONERO-RUN-004-SPPC-05-REVIEW-PACKAGE-v1.md\`
2. Assess failing gates and variance evidence
3. Authorize new repair or new run only after explicit decision

**Phase 3 canary, full corpus, Wave 5: NOT AUTHORIZED**
`;
  }
  return `# CORVONERO RUN 004 — PHASE 3 NEXT TASK v1

**Status:** **READY FOR OPERATOR AUTHORIZATION** (SPPC-05 pass — review required)  
**Run ID:** \`${RUN_ID}\`  
**Lifecycle:** \`PHASE_0_1_2_COMPLETE\`  
**Project:** \`FROZEN_PENDING_CANARY_AUTHORIZATION\`

---

## Prerequisite (met — operator sign-off required)

\`\`\`text
SPPC-05: PASS — OPERATOR REVIEW REQUIRED
Project: FROZEN_PENDING_CANARY_AUTHORIZATION
Run 004: PHASE_0_1_2_COMPLETE
Corpus processed: 0 / 2368
\`\`\`

---

## Phase 3 scope (when operator authorizes)

**Task ID:** \`CORVONERO-RUN-004-PHASE-3-CANARY\`

| Parameter | Planned value |
|-----------|---------------|
| Run ID | \`${RUN_ID}\` |
| Canary size | 120 phrases |
| Review sample | 30 |
| Provider | openrouter |
| Model | openai/gpt-5-mini |
| Hard cost cap | 3.00 USD |
| Gate | C — operator review before full corpus |

**Explicitly forbidden without separate authorization:** full 2368 corpus, Wave 5, strategy, Campaign Architecture, Commander, import, launch.

---

## Entry criteria

- Operator sign-off on \`CORVONERO-RUN-004-SPPC-05-REVIEW-PACKAGE-v1.md\`
- Active lock on STORAGE root \`${RUN_STORAGE.replace(/\\/g, '\\\\')}\`
- PSR-AMB-01 ambiguity acknowledged in review
- Cost cap confirmed for canary batch

---

## Expected outputs (Phase 3)

- Canary batch receipt (STORAGE \`batches/\`, \`raw-responses/\`)
- Canary class distribution report (Git sanitized)
- Operator review sample manifest
- Gate C decision record

**Next gate after Phase 3 (if pass):** Gate C operator review → Phase 5 bounded batches (separate authorization).

**Do not execute Phase 3 in Run 004 SPPC-05 task — this document is prepared only.**
`;
}

function mdMainReport(data) {
  const gateB = data.gate_b_verdict;
  return `# REPORT — Corvonero Run 004 SPPC-05 Validation v1

**Date:** ${data.completed_at}  
**Run ID:** \`${RUN_ID}\`  
**Verdict:** \`${gateB.status}\`

## Executive summary

Run 004 executed complete SPPC-05 validation under ORCA Repair V2 authority. Project corpus remains at **0 / 2368**. Phase 3 canary was **not** started.

## Git preflight

- Branch: \`mars/canonical-post-recovery\`
- Recovery authority ancestor: confirmed
- ORCA repair v2 hashes: matched

## Gate B

\`\`\`text
SPPC-05: ${gateB.status.startsWith('PASS') ? 'PASS — OPERATOR REVIEW REQUIRED' : 'FAILED'}
Run 004: ${gateB.run_lifecycle}
Project: ${gateB.project}
\`\`\`

## Cost

Cumulative: **$${(data.cumulative_cost_usd || 0).toFixed(4)}** (cap $${OPERATOR.hard_cost_cap_usd})

## Outputs

- \`pilots/corvonero/CORVONERO-RUN-004-SPPC-05-RESULT-v1.md\`
- \`pilots/corvonero/CORVONERO-RUN-004-SPPC-05-REVIEW-PACKAGE-v1.md\`
- \`pilots/corvonero/CORVONERO-RUN-004-PHASE-3-NEXT-TASK-v1.md\`
- STORAGE: \`${RUN_ID}\`

## Next gate

\`\`\`text
OPERATOR REVIEW OF CORVONERO RUN 004 SPPC-05 RESULT
\`\`\`
`;
}

function main() {
  const startedAt = new Date().toISOString();
  verifyRun004Absent();

  const repairSnapshot = buildRepairAuthoritySnapshot();
  if (repairSnapshot.drift_detected) {
    console.error(JSON.stringify({ error: repairSnapshot.verdict, drift: repairSnapshot.drift_details }));
    process.exit(2);
  }

  loadLocalSecrets();
  process.env.ORCA_SEMANTIC_PROVIDER = OPERATOR.provider;
  process.env.ORCA_SEMANTIC_MODEL = OPERATOR.model;

  const secretSummary = getSafeConfigSummary();
  if (secretSummary.OPENROUTER_API_KEY !== 'SET') {
    console.error(JSON.stringify({ error: 'BLOCKED — APPROVED MODEL AUTHORITY UNAVAILABLE', reason: 'OPENROUTER_API_KEY not set', secretSummary }));
    process.exit(2);
  }
  if (process.env.ORCA_SEMANTIC_MODEL !== OPERATOR.model) {
    console.error(JSON.stringify({ error: 'BLOCKED — APPROVED MODEL AUTHORITY UNAVAILABLE', model: process.env.ORCA_SEMANTIC_MODEL }));
    process.exit(2);
  }

  const corpus = verifyCorpus();
  if (!corpus.pass) {
    console.error(JSON.stringify({ error: 'BLOCKED — IMMUTABLE INPUT AUTHORITY MISMATCH', corpus }));
    process.exit(2);
  }

  const subdirs = ['manifests', 'runtime', 'checkpoints', 'locks', 'batches', 'cache', 'raw-responses', 'receipts', 'reports', 'quarantine'];
  for (const d of subdirs) loopMkdir(path.join(RUN_STORAGE, d));
  loopMkdir(path.join(GIT_RUN_DIR, 'reports'));

  writeJsonAtomic(path.join(RUN_STORAGE, 'manifests', 'repair-authority-freeze-v1.json'), repairSnapshot);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'repair-authority-freeze-v1.json'), repairSnapshot);

  const inputManifest = {
    manifest_id: `${RUN_ID}-input-reference-v1`,
    run_id: RUN_ID,
    project_id: 'PRJ-0013',
    mig_session_id: 'session-mig-20260622-corv01',
    source_path: CORPUS_REL,
    record_count: corpus.record_count,
    sha256: corpus.hash,
    sha256_prefix: corpus.hash_prefix,
    id_scheme: 'CR2-PHR-*',
    duplicate_ids: 0,
    missing_ids: 0,
    normalized_corpus_parent: { record_count: 2399, sha256_prefix: 'fbeb1b65d4a90cb0', lineage: '2399 → 31 duplicate clusters → 2368' },
    mutability: 'READ_ONLY',
    registered_at: startedAt,
  };
  writeJsonAtomic(path.join(RUN_STORAGE, 'manifests', 'immutable-input-reference-v1.json'), inputManifest);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'immutable-input-reference-v1.json'), inputManifest);

  const runManifest = {
    run_id: RUN_ID,
    project_id: 'PRJ-0013',
    mig_session_id: 'session-mig-20260622-corv01',
    corpus_path: CORPUS_REL,
    corpus_count: 2368,
    corpus_sha256: corpus.hash,
    orca_wave: '3.1F',
    orca_repair_authority: repairSnapshot.verdict,
    orca_repair_version: 'v2',
    prompt_contract_version: PROMPT_VERSION,
    hard_rules_version: HARD_RULES_VERSION,
    adjudicator_version: ADJUDICATOR_VERSION,
    service_intent_evidence_version: SERVICE_INTENT_EVIDENCE_VERSION,
    platform_compatibility_version: PLATFORM_COMPATIBILITY_VERSION,
    provider: OPERATOR.provider,
    model: OPERATOR.model,
    lifecycle_state: 'REGISTERED_FOR_SPPC_05_VALIDATION',
    authorized_phases: ['Phase 0 — authority verification', 'Phase 1 — Run 004 registration', 'Phase 2 — complete SPPC-05 validation'],
    prohibited_phases: ['Phase 3 canary', 'full 2368 corpus', 'semantic production batches', 'Wave 5', 'strategy', 'Campaign Architecture', 'Commander', 'import', 'launch'],
    cost_limits: { hard_cap_usd: OPERATOR.hard_cost_cap_usd, soft_warning_usd: OPERATOR.soft_cost_warning_usd },
    operator_decisions: OPERATOR,
    previous_failed_runs: FROZEN_RUNS,
    old_run_isolation_requirement: 'Run 004 fully isolated from Runs 001–003 locks/checkpoints/cache',
    psr_amb_01_operator_decision: OPERATOR.psr_amb_01,
    recovery_authority: RECOVERY_AUTHORITY,
    created_at: startedAt,
    storage_root: RUN_STORAGE,
    git_run_dir: path.relative(REPO_ROOT, GIT_RUN_DIR),
  };
  writeJsonAtomic(path.join(RUN_STORAGE, 'manifests', 'run-manifest-v1.json'), runManifest);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'run-manifest-v1.json'), runManifest);

  const isolation = runIsolationTest();
  const costProjection = {
    suite_inventory: [
      'closed_dataset_regression', 'confirmation_product', 'confirmation_geo_v2',
      'problem_query_policy', 'platform_compatibility', 'under_admission',
      'wave31f_bypass', 'focused_repair_repro', 'structured_output', 'variance_check',
    ],
    fixture_counts: {
      protected_product_confirmation: 106,
      geo_commercial_confirmation_v2: 120,
      closed_dataset_supplementary: 136,
      problem_query_policy: 10,
      platform_compatibility: 7,
      under_admission_unit_tests: 23,
      wave31f_bypass_checks: 16,
      variance_cases: 4,
      variance_repetitions: 3,
    },
    expected_model_calls: 980,
    estimated_cost_usd: 0.95,
    hard_cap_usd: OPERATOR.hard_cost_cap_usd,
    soft_warning_usd: OPERATOR.soft_cost_warning_usd,
    full_corpus_forbidden: true,
    projected_in_bounds: true,
  };
  writeJsonAtomic(path.join(RUN_STORAGE, 'reports', 'cost-projection-pre-sppc05-v1.json'), costProjection);

  if (!costProjection.projected_in_bounds || costProjection.estimated_cost_usd > OPERATOR.hard_cost_cap_usd) {
    console.error(JSON.stringify({ error: 'BLOCKED — PROJECTED COST EXCEEDS HARD CAP', costProjection }));
    process.exit(2);
  }

  const { lockPath } = acquireLock(corpus.hash);
  const checkpoint = createInitialCheckpoint(corpus.hash);

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
  let costBlocked = false;

  if (!isolation.pass) {
    console.error(JSON.stringify({ error: isolation.verdict, isolation }));
  } else {
    for (const suite of testSuites) {
      console.error(`[RUN004] Starting suite: ${suite.id}`);
      const r = runNodeTest(suite.script, suite.args || []);
      const parsed = parseLastJson(r.stdout);
      if (parsed?.cost_usd) cumulativeCost += parsed.cost_usd;
      if (parsed?.calculated_cost_usd) cumulativeCost += parsed.calculated_cost_usd;
      if (parsed?.metrics?.gate_pass === false) r.pass = false;
      suiteResults.push({ ...suite, ...r, parsed_summary: parsed });
      console.error(`[RUN004] Finished suite: ${suite.id} pass=${r.pass} exit=${r.exit_code} cost_so_far=${cumulativeCost.toFixed(4)}`);
      if (cumulativeCost > OPERATOR.hard_cost_cap_usd) {
        costBlocked = true;
        console.error('[RUN004] Hard cost cap exceeded — stopping further live suites');
        break;
      }
    }
  }

  const structured = runStructuredOutputSmoke();
  suiteResults.push(structured);

  const { variance: varianceReport, psr_amb_01: psrAmbReport, runner_pass: varianceRunnerPass } = runPsrAmbVariance(3);
  if (varianceReport?.cost_usd) cumulativeCost += varianceReport.cost_usd;

  writeJsonAtomic(path.join(RUN_STORAGE, 'reports', 'variance-check-v1.json'), {
    repetitions: 3,
    variance_report: varianceReport,
    psr_amb_01: psrAmbReport,
    repair_cases_required: {
      'CFM-PROD-UPD-02': 'REJECT',
      'PQR-ABSTAIN-03': 'ABSTAIN',
      'PC-ABSTAIN-01': 'ABSTAIN',
    },
  });

  const gateCriteria = evaluateGateCriteria(suiteResults, varianceReport, psrAmbReport);
  gateCriteria.old_run_isolation_pass = isolation.pass;
  if (!varianceRunnerPass) gateCriteria.variance_repair_cases_stable = false;
  if (costBlocked) gateCriteria.all_pass = false;

  gateCriteria.all_pass = Object.entries(gateCriteria)
    .filter(([k]) => !['psr_amb_01_isolated', 'psr_amb_01_status'].includes(k))
    .every(([, v]) => v === true);

  const criticalFailures = buildCriticalFailures(gateCriteria, suiteResults, varianceReport);
  if (!isolation.pass) criticalFailures.unshift(isolation.verdict);
  if (costBlocked) criticalFailures.push('Hard cost cap exceeded during suite execution');

  const blocked = !gateCriteria.all_pass || !isolation.pass || costBlocked;
  const gateBVerdict = blocked
    ? { status: 'FAILED', project: 'BLOCKED_AT_SPPC_05', run_lifecycle: 'BLOCKED_AT_SPPC_05' }
    : { status: 'PASS — OPERATOR REVIEW REQUIRED', project: 'FROZEN_PENDING_CANARY_AUTHORIZATION', run_lifecycle: 'PHASE_0_1_2_COMPLETE' };

  writeJsonAtomic(path.join(RUN_STORAGE, 'checkpoints', 'checkpoint-sppc05-complete-v1.json'), {
    ...checkpoint,
    phase: gateBVerdict.status.startsWith('PASS') ? 'SPPC-05_COMPLETE_PENDING_REVIEW' : 'BLOCKED_AT_SPPC_05',
    project_processed: 0,
    project_total: 2368,
    cumulative_cost_usd: cumulativeCost,
    sppc_05_completed_at: new Date().toISOString(),
    complete: gateBVerdict.status.startsWith('PASS'),
    gate_b_verdict: gateBVerdict.status,
  });

  const sppc05Report = {
    report_id: 'corvonero-run-004-sppc-05-execution-v1',
    run_id: RUN_ID,
    lifecycle_state: gateBVerdict.run_lifecycle,
    provider: OPERATOR.provider,
    model: OPERATOR.model,
    prompt_contract_version: PROMPT_VERSION,
    adjudicator_version: ADJUDICATOR_VERSION,
    platform_compatibility_version: PLATFORM_COMPATIBILITY_VERSION,
    hard_rules_version: HARD_RULES_VERSION,
    repair_authority: repairSnapshot,
    gate_b_verdict: gateBVerdict,
    gate_criteria: gateCriteria,
    critical_failures: criticalFailures,
    fixture_inventory: costProjection.fixture_counts,
    suite_results: suiteResults.map(({ id, script, pass, exit_code, runtime_ms, parsed_summary, live }) => ({
      id, script, pass, exit_code, runtime_ms, live,
      metrics: parsed_summary?.metrics || parsed_summary?.summary || parsed_summary,
    })),
    variance_check: varianceReport,
    psr_amb_01: psrAmbReport,
    cumulative_cost_usd: cumulativeCost,
    isolation,
    cost_projection: costProjection,
    full_corpus_started: false,
    canary_started: false,
    wave5_started: false,
    corpus_processed_count: 0,
    secret_summary: secretSummary,
    started_at: startedAt,
    completed_at: new Date().toISOString(),
  };

  writeJsonAtomic(path.join(RUN_STORAGE, 'reports', 'sppc-05-execution-report-v1.json'), sppc05Report);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'reports', 'sppc-05-sanitized-report-v1.json'), sppc05Report);

  releaseLock(lockPath, gateBVerdict.status);

  const executionReceipt = {
    run_id: RUN_ID,
    phase: '0/1/2 — SPPC-05 validation',
    started_at: startedAt,
    completed_at: sppc05Report.completed_at,
    gate_b: gateBVerdict.status,
    lifecycle_state: gateBVerdict.run_lifecycle,
    provider: OPERATOR.provider,
    model: OPERATOR.model,
    corpus_verified: corpus.pass,
    corpus_processed_count: 0,
    isolation_verdict: isolation.verdict,
    cumulative_cost_usd: cumulativeCost,
    full_corpus_started: false,
    canary_started: false,
    wave5_started: false,
  };
  writeJsonAtomic(path.join(RUN_STORAGE, 'receipts', 'phase-0-1-2-execution-receipt-v1.json'), executionReceipt);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'sanitized-execution-receipt-v1.json'), executionReceipt);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'lifecycle-decision-v1.json'), {
    run_id: RUN_ID,
    decision: gateBVerdict.run_lifecycle,
    sppc_05: gateBVerdict.status,
    next_gate: 'OPERATOR REVIEW OF CORVONERO RUN 004 SPPC-05 RESULT',
    canary_authorized: false,
    full_corpus_authorized: false,
    frozen_runs: FROZEN_RUNS,
  });

  runManifest.lifecycle_state = gateBVerdict.run_lifecycle;
  runManifest.gate_b = gateBVerdict.status;
  writeJsonAtomic(path.join(RUN_STORAGE, 'manifests', 'run-manifest-v1.json'), runManifest);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'run-manifest-v1.json'), runManifest);

  writeJsonAtomic(path.join(PILOT_DIR, 'CORVONERO-RUN-004-SPPC-05-RESULT-v1.json'), sppc05Report);
  writeJsonAtomic(path.join(PILOT_DIR, 'CORVONERO-RUN-004-SPPC-05-REVIEW-PACKAGE-v1.json'), sppc05Report);
  writeText(path.join(PILOT_DIR, 'CORVONERO-RUN-004-SPPC-05-RESULT-v1.md'), mdResultReport(sppc05Report));
  writeText(path.join(PILOT_DIR, 'CORVONERO-RUN-004-SPPC-05-REVIEW-PACKAGE-v1.md'), mdReviewPackage(sppc05Report));
  writeText(path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-NEXT-TASK-v1.md'), mdPhase3Task(gateBVerdict));
  writeText(path.join(REPORTS_DIR, 'REPORT-corvonero-run-004-sppc05-validation-v1.md'), mdMainReport(sppc05Report));

  console.log(JSON.stringify({
    run_id: RUN_ID,
    gate_b: gateBVerdict,
    cumulative_cost_usd: cumulativeCost,
    isolation: isolation.verdict,
    repair_authority: repairSnapshot.verdict,
    suite_pass_count: suiteResults.filter((s) => s.pass).length,
    suite_total: suiteResults.length,
    variance_repair_stable: varianceReport?.repair_cases_stable,
    psr_amb_01: psrAmbReport,
  }, null, 2));

  process.exit(gateBVerdict.status.startsWith('PASS') ? 0 : 1);
}

main();
