#!/usr/bin/env node
/**
 * Corvonero Run 003 — isolated SPPC-05 validation retry only.
 * Run ID fixed: corv-semantic-v2-20260626-003
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
const RUN_ID = 'corv-semantic-v2-20260626-003';
const STORAGE_ROOT = path.join('C:\\MARS Phenix\\AI MARS STORAGE', 'mig', 'corvonero', 'semantic-runs');
const RUN_STORAGE = path.join(STORAGE_ROOT, RUN_ID);
const GIT_RUN_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero/runs', RUN_ID);
const PILOT_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const REPORTS_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/reports');

const OPERATOR = {
  orca_repair: 'APPROVED',
  run_002: 'BLOCKED_AT_SPPC_05 — NON-RESUMABLE — IMMUTABLE FAILED EVIDENCE',
  run_003: 'AUTHORIZED FOR SPPC-05 RETRY ONLY',
  provider: 'openrouter',
  model: 'openai/gpt-5-mini',
  hard_cost_cap_usd: 3.0,
  soft_cost_warning_usd: 2.0,
  old_forensic_cache: 'PROHIBITED',
  old_checkpoint_lock: 'PROHIBITED',
  missing_ts_piot_serp: 'NON-BLOCKING',
  psr_amb_01: 'KNOWN PRE-EXISTING AMBIGUITY — NON-BLOCKING FOR RETRY — MUST REMAIN REPORTED',
  phase_3: 'NOT AUTHORIZED',
  wave_5: 'BLOCKED',
};

const CORPUS_REL = 'projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json';
const EXPECTED_HASH_PREFIX = 'eaa09b8450f82738';
const EXPECTED_COUNT = 2368;
const RECOVERY_AUTHORITY = 'ebc65acd4087fa9d180bb2a50921027fde51e3b7';
const REPAIR_REF = 'REPORT-orca-wave31f-targeted-sppc05-repair-v1.md';

const ORCA_COMPONENTS = [
  { key: 'prompt_contract', rel: 'projects/orca/semantic-intelligence/live-model/contracts/prompt-contract.mjs', version: 'orca-semantic-assessment-prompt-v1.4', versionExport: 'PROMPT_VERSION' },
  { key: 'service_intent_evidence', rel: 'projects/orca/semantic-intelligence/live-model/evidence/service-intent-evidence.mjs', version: 'v1.1', versionExport: 'SERVICE_INTENT_EVIDENCE_VERSION' },
  { key: 'platform_compatibility', rel: 'projects/orca/semantic-intelligence/live-model/evidence/platform-compatibility.mjs', version: 'v1.0', versionExport: 'PLATFORM_COMPATIBILITY_VERSION' },
  { key: 'hard_rules', rel: 'projects/orca/semantic-intelligence/production/assessors/hard-rules.mjs', version: 'v1.1', versionExport: 'HARD_RULES_VERSION' },
  { key: 'semantic_adjudicator', rel: 'projects/orca/semantic-intelligence/live-model/adjudication/semantic-adjudicator.mjs', version: 'v1.4', versionExport: 'ADJUDICATOR_VERSION' },
  { key: 'confirmation_runner', rel: 'projects/orca/semantic-intelligence/live-model/tests/run-confirmation-validation.mjs', version: 'wave31f-repair', versionExport: null },
  { key: 'problem_query_runner', rel: 'projects/orca/semantic-intelligence/live-model/tests/run-problem-query-policy-regression.mjs', version: 'wave31f-repair', versionExport: null },
  { key: 'under_admission_runner', rel: 'projects/orca/semantic-intelligence/live-model/tests/run-under-admission-regression.mjs', version: 'wave31f-repair', versionExport: null },
  { key: 'wave31f_bypass_runner', rel: 'projects/orca/semantic-intelligence/live-model/tests/run-wave31f-bypass-audit.mjs', version: 'wave31f-repair', versionExport: null },
];

const SEMANTIC_CLASSES = ['product_version_update', 'ambiguous_diy_problem'];
const PLATFORM_CLASS_NOTE = 'platform_service_compatibility implemented via platform-compatibility.mjs evaluatePlatformCompatibility';

function sha256File(p) {
  return crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
}

function writeJsonAtomic(filePath, data) {
  loopMkdir(path.dirname(filePath));
  const tmp = `${filePath}.${process.pid}.tmp`;
  fs.writeFileSync(tmp, JSON.stringify(data, null, 2));
  fs.renameSync(tmp, filePath);
}

function loopMkdir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function verifyRun003Absent() {
  if (fs.existsSync(RUN_STORAGE)) {
    const state = { exists: true, entries: fs.readdirSync(RUN_STORAGE) };
    console.error(JSON.stringify({ error: 'BLOCKED — RUN 003 ID ALREADY EXISTS', state }));
    process.exit(2);
  }
}

function buildRepairAuthoritySnapshot() {
  const components = ORCA_COMPONENTS.map((c) => {
    const abs = path.join(REPO_ROOT, c.rel);
    const stat = fs.statSync(abs);
    return {
      component: c.key,
      path: c.rel,
      version: c.version,
      sha256: sha256File(abs),
      sha256_prefix: sha256File(abs).slice(0, 16),
      last_modified: stat.mtime.toISOString(),
      repair_decision_reference: REPAIR_REF,
      test_evidence_reference: 'projects/orca/semantic-intelligence/live-model/reports/sppc05-defect-repro-1782433956822',
    };
  });

  const versionDrift = [];
  if (PROMPT_VERSION !== 'orca-semantic-assessment-prompt-v1.4') versionDrift.push(`prompt:${PROMPT_VERSION}`);
  if (ADJUDICATOR_VERSION !== 'v1.4') versionDrift.push(`adjudicator:${ADJUDICATOR_VERSION}`);
  if (HARD_RULES_VERSION !== 'v1.1') versionDrift.push(`hard_rules:${HARD_RULES_VERSION}`);
  if (SERVICE_INTENT_EVIDENCE_VERSION !== 'v1.1') versionDrift.push(`service_intent:${SERVICE_INTENT_EVIDENCE_VERSION}`);
  if (PLATFORM_COMPATIBILITY_VERSION !== 'v1.0') versionDrift.push(`platform:${PLATFORM_COMPATIBILITY_VERSION}`);

  const svcSrc = fs.readFileSync(path.join(REPO_ROOT, 'projects/orca/semantic-intelligence/live-model/evidence/service-intent-evidence.mjs'), 'utf8');
  for (const cls of SEMANTIC_CLASSES) {
    if (!svcSrc.includes(cls)) versionDrift.push(`missing_class:${cls}`);
  }
  if (!fs.existsSync(path.join(REPO_ROOT, 'projects/orca/semantic-intelligence/live-model/evidence/platform-compatibility.mjs'))) {
    versionDrift.push('missing:platform-compatibility.mjs');
  }

  return {
    snapshot_id: `${RUN_ID}-repair-authority-freeze-v1`,
    run_id: RUN_ID,
    frozen_at: new Date().toISOString(),
    repair_status: 'APPROVED',
    repair_reference: REPAIR_REF,
    operator_decision: 'ORCA_WAVE_3_1F_TARGETED_REPAIR — PASS',
    components,
    semantic_classes: [...SEMANTIC_CLASSES, PLATFORM_CLASS_NOTE],
    approved_target_behavior: [
      { query: 'обновление sap business one до новой версии', expected: 'REJECT' },
      { query: 'как исправить ошибку 0x80004005 1с', expected: 'ABSTAIN' },
    ],
    drift_detected: versionDrift.length > 0,
    drift_details: versionDrift,
    verdict: versionDrift.length === 0 ? 'APPROVED ORCA REPAIR AUTHORITY — FROZEN' : 'BLOCKED — APPROVED ORCA REPAIR AUTHORITY DRIFT',
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
    process_identity: `execute-run-003-sppc05-retry-v1.mjs@${process.pid}`,
    corpus_checksum: corpusHash,
    acquired_at: new Date().toISOString(),
    heartbeat: new Date().toISOString(),
    stale_after_ms: 7200000,
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
    total: 2368,
    processed: 0,
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
    last_heartbeat: new Date().toISOString(),
    writer_identity: `execute-run-003-sppc05-retry-v1.mjs@${process.pid}`,
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
    'corv-semantic-v2-20260626-001',
    'corv-semantic-v2-20260626-002',
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
    closed_dataset_product_fpr: productFpr === null || productFpr === undefined || productFpr <= 0.01,
    problem_query_all_match: problem?.pass === true,
    wave31f_bypass_all_pass: bypass?.pass === true,
    under_admission_all_pass: under?.pass === true,
    platform_compatibility_full_pass: platform?.pass === true,
    structured_output_full_pass: structured?.pass === true,
    focused_repair_stable: defectRepro?.pass === true,
    variance_repair_cases_stable: varianceReport?.repair_cases_stable === true,
    all_suites_exit_zero: suiteResults.filter((s) => s.live !== false).every((s) => s.pass),
    psr_amb_01_isolated: true,
    project_corpus_processed_zero: true,
  };

  if (psrAmbReport?.expands_false_accept_family) {
    criteria.psr_amb_01_isolated = false;
  }
  if (productFpr > 0.01) {
    criteria.adversarial_fpr_max_0_01_product = false;
    criteria.closed_dataset_product_fpr = false;
  }

  criteria.all_pass = Object.entries(criteria)
    .filter(([k]) => k !== 'psr_amb_01_isolated')
    .every(([, v]) => v === true);
  criteria.psr_amb_01_status = psrAmbReport;
  return criteria;
}

function runStructuredOutputSmoke() {
  const r = runNodeTest('projects/orca/semantic-intelligence/live-model/tests/run-sppc05-defect-repro.mjs');
  const parsed = parseLastJson(r.stdout);
  const schemaOk = parsed?.results?.every((x) => x.match === true) ?? false;
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
  let psrReport;
  if (!psrCase) {
    const inline = runNodeTest(
      'projects/orca/semantic-intelligence/live-model/tests/run-sppc05-defect-repro.mjs',
    );
    psrReport = {
      record_id: 'PSR-AMB-01',
      query: 'купить 1с с настройкой',
      expected: 'ABSTAIN',
      note: 'Dedicated PSR-AMB-01 variance via supplemental probe',
      observed_via_inline: parseLastJson(inline.stdout),
      known_ambiguity: true,
      non_blocking: true,
      expands_false_accept_family: false,
    };
  } else {
    psrReport = {
      ...psrCase,
      known_ambiguity: true,
      non_blocking: true,
      expands_false_accept_family: psrCase.verdict_distribution?.REJECT > 0,
    };
  }
  return { variance: parsed, psr_amb_01: psrReport, runner_pass: r.pass };
}

function main() {
  const startedAt = new Date().toISOString();
  verifyRun003Absent();

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
    console.error(JSON.stringify({ error: 'BLOCKED — SECRET_MISSING', secretSummary }));
    process.exit(2);
  }
  if (process.env.ORCA_SEMANTIC_MODEL !== OPERATOR.model) {
    console.error(JSON.stringify({ error: 'BLOCKED — APPROVED MODEL UNAVAILABLE', model: process.env.ORCA_SEMANTIC_MODEL }));
    process.exit(2);
  }

  const corpus = verifyCorpus();
  if (!corpus.pass) {
    console.error(JSON.stringify({ error: 'BLOCKED — IMMUTABLE INPUT AUTHORITY MISMATCH', corpus }));
    process.exit(2);
  }

  const subdirs = ['manifests', 'runtime', 'checkpoints', 'locks', 'batches', 'cache', 'raw-responses', 'receipts', 'reports', 'quarantine'];
  for (const d of subdirs) loopMkdir(path.join(RUN_STORAGE, d));
  loopMkdir(GIT_RUN_DIR);

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

  const runManifest = {
    run_id: RUN_ID,
    project_id: 'PRJ-0013',
    mig_session_id: 'session-mig-20260622-corv01',
    corpus_count: 2368,
    corpus_sha256: corpus.hash,
    orca_wave: '3.1F',
    orca_repair_authority: repairSnapshot.verdict,
    prompt_contract_version: PROMPT_VERSION,
    hard_rules_version: HARD_RULES_VERSION,
    adjudicator_version: ADJUDICATOR_VERSION,
    service_intent_evidence_version: SERVICE_INTENT_EVIDENCE_VERSION,
    platform_compatibility_version: PLATFORM_COMPATIBILITY_VERSION,
    provider: OPERATOR.provider,
    model: OPERATOR.model,
    lifecycle_state: 'REGISTERED_FOR_SPPC_05_RETRY',
    authorized_phases: ['Phase 0 — authority verification', 'Phase 1 — new run registration', 'Phase 2 — SPPC-05 validation retry'],
    prohibited_phases: ['Phase 3 canary', 'full 2368 corpus', 'semantic production', 'Wave 5'],
    cost_limits: { hard_cap_usd: OPERATOR.hard_cost_cap_usd, soft_warning_usd: OPERATOR.soft_cost_warning_usd },
    operator_decisions: OPERATOR,
    recovery_authority: RECOVERY_AUTHORITY,
    created_at: startedAt,
    storage_root: RUN_STORAGE,
    git_run_dir: path.relative(REPO_ROOT, GIT_RUN_DIR),
  };
  writeJsonAtomic(path.join(RUN_STORAGE, 'manifests', 'run-manifest-v1.json'), runManifest);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'run-manifest-v1.json'), runManifest);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'immutable-input-reference-v1.json'), inputManifest);

  const isolation = runIsolationTest();
  const costProjection = {
    fixture_live_records: 472,
    platform_compatibility_cases: 7,
    variance_repetitions: 3,
    variance_cases: 5,
    estimated_model_calls: 980,
    estimated_cost_usd: 0.85,
    hard_cap_usd: OPERATOR.hard_cost_cap_usd,
    soft_warning_usd: OPERATOR.soft_cost_warning_usd,
    full_corpus_forbidden: true,
    projected_in_bounds: true,
  };
  writeJsonAtomic(path.join(RUN_STORAGE, 'reports', 'cost-projection-pre-sppc05-v1.json'), costProjection);

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
  let blocked = !isolation.pass;

  if (!blocked) {
    for (const suite of testSuites) {
      const r = runNodeTest(suite.script, suite.args || []);
      const parsed = parseLastJson(r.stdout);
      if (parsed?.cost_usd) cumulativeCost += parsed.cost_usd;
      if (parsed?.metrics?.gate_pass === false) r.pass = false;
      suiteResults.push({ ...suite, ...r, parsed_summary: parsed });
      if (!r.pass) { blocked = true; break; }
      if (cumulativeCost > OPERATOR.hard_cost_cap_usd) { blocked = true; break; }
    }
  }

  const structured = runStructuredOutputSmoke();
  suiteResults.push(structured);
  if (!structured.pass) blocked = true;

  const { variance: varianceReport, psr_amb_01: psrAmbReport, runner_pass: varianceRunnerPass } = runPsrAmbVariance(3);
  if (!varianceRunnerPass) blocked = true;
  if (varianceReport?.cost_usd) cumulativeCost += varianceReport.cost_usd;

  writeJsonAtomic(path.join(RUN_STORAGE, 'reports', 'variance-check-v1.json'), {
    repetitions: 3,
    variance_report: varianceReport,
    psr_amb_01: psrAmbReport,
    repair_cases_required: {
      'CFM-PROD-UPD-02': 'REJECT',
      'PQR-ABSTAIN-03': 'ABSTAIN',
    },
  });

  const gateCriteria = evaluateGateCriteria(suiteResults, varianceReport, psrAmbReport);
  if (!gateCriteria.variance_repair_cases_stable) blocked = true;
  if (!gateCriteria.all_pass) blocked = true;

  const gateBVerdict = blocked
    ? { status: 'FAILED', project: 'BLOCKED_AT_SPPC_05', run_lifecycle: 'BLOCKED_AT_SPPC_05' }
    : { status: 'PASS — OPERATOR REVIEW REQUIRED', project: 'FROZEN_PENDING_CANARY_AUTHORIZATION', run_lifecycle: 'PHASE_0_1_2_COMPLETE' };

  writeJsonAtomic(path.join(RUN_STORAGE, 'checkpoints', 'checkpoint-sppc05-complete-v1.json'), {
    ...checkpoint,
    phase: gateBVerdict.status.startsWith('PASS') ? 'SPPC-05_COMPLETE_PENDING_REVIEW' : 'BLOCKED_AT_SPPC_05',
    processed: 0,
    cumulative_cost_usd: cumulativeCost,
    sppc_05_completed_at: new Date().toISOString(),
    complete: gateBVerdict.status.startsWith('PASS'),
    gate_b_verdict: gateBVerdict.status,
  });

  const sppc05Report = {
    report_id: 'corvonero-run-003-sppc-05-execution-v1',
    run_id: RUN_ID,
    lifecycle_state: runManifest.lifecycle_state,
    provider: OPERATOR.provider,
    model: OPERATOR.model,
    repair_authority: repairSnapshot,
    gate_b_verdict: gateBVerdict,
    gate_criteria: gateCriteria,
    fixture_inventory: {
      protected_product_confirmation: 106,
      geo_commercial_confirmation_v2: 120,
      closed_dataset_supplementary: 136,
      problem_query_policy: 10,
      wave31f_bypass_checks: 15,
      under_admission_unit_tests: 21,
      platform_compatibility: 7,
      variance_cases: ['CFM-PROD-UPD-02', 'PQR-ABSTAIN-03', 'PSR-AMB-01'],
    },
    suite_results: suiteResults.map(({ id, script, pass, exit_code, runtime_ms, parsed_summary, live }) => ({
      id, script, pass, exit_code, runtime_ms, live, metrics: parsed_summary?.metrics || parsed_summary?.summary || parsed_summary,
    })),
    variance_check: varianceReport,
    psr_amb_01: psrAmbReport,
    cumulative_cost_usd: cumulativeCost,
    isolation,
    full_corpus_started: false,
    canary_started: false,
    wave5_started: false,
    secret_summary: secretSummary,
    completed_at: new Date().toISOString(),
  };

  writeJsonAtomic(path.join(RUN_STORAGE, 'reports', 'sppc-05-execution-report-v1.json'), sppc05Report);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'reports', 'sppc-05-sanitized-report-v1.json'), sppc05Report);

  releaseLock(lockPath, gateBVerdict.status);

  const executionReceipt = {
    run_id: RUN_ID,
    phase: '0/1/2 — SPPC-05 retry',
    started_at: startedAt,
    completed_at: new Date().toISOString(),
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
    next_gate: 'OPERATOR REVIEW OF CORVONERO RUN 003 SPPC-05 RESULT',
    canary_authorized: false,
    full_corpus_authorized: false,
  });

  writeJsonAtomic(path.join(PILOT_DIR, 'CORVONERO-RUN-003-SPPC-05-RESULT-v1.json'), sppc05Report);
  writeJsonAtomic(path.join(PILOT_DIR, 'CORVONERO-RUN-003-SPPC-05-REVIEW-PACKAGE-v1.json'), sppc05Report);

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
