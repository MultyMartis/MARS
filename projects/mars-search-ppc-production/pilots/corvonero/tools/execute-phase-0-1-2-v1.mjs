#!/usr/bin/env node
/**
 * Corvonero new controlled semantic run — Phase 0/1/2 orchestrator.
 * SPPC-05 closed-dataset validation only; no full corpus.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { loadLocalSecrets, getSafeConfigSummary } from '../../../../orca/semantic-intelligence/live-model/runtime/local-secret-loader.mjs';
import { PROMPT_VERSION } from '../../../../orca/semantic-intelligence/live-model/contracts/prompt-contract.mjs';
import { ADJUDICATOR_VERSION } from '../../../../orca/semantic-intelligence/live-model/adjudication/semantic-adjudicator.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const STORAGE_ROOT = path.join('C:\\MARS Phenix\\AI MARS STORAGE', 'mig', 'corvonero', 'semantic-runs');
const DATE_TAG = '20260626';
const RUN_ID = resolveRunId();
const RUN_STORAGE = path.join(STORAGE_ROOT, RUN_ID);
const GIT_RUN_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero/runs', RUN_ID);

const OPERATOR = {
  provider: 'openrouter',
  model: 'openai/gpt-5-mini',
  hard_cost_cap_usd: 3.0,
  soft_cost_warning_usd: 2.0,
  old_run_resume: 'PROHIBITED',
  old_forensic_cache_reuse: 'PROHIBITED',
  missing_ts_piot_serp: 'NON_BLOCKING_FOR_PHASE_0_1_2',
  wave5: 'BLOCKED',
};

const OLD_RUN_ID = 'corvonero-direct-v2-clean-room-v1-diagnostic';
const CORPUS_REL = 'projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json';
const EXPECTED_HASH_PREFIX = 'eaa09b8450f82738';
const EXPECTED_COUNT = 2368;

function resolveRunId() {
  for (let seq = 1; seq <= 99; seq++) {
    const id = `corv-semantic-v2-${DATE_TAG}-${String(seq).padStart(3, '0')}`;
    if (!fs.existsSync(path.join(STORAGE_ROOT, id))) return id;
  }
  throw new Error('NO_AVAILABLE_RUN_ID_SEQUENCE');
}

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

function verifyCorpus() {
  const corpusPath = path.join(REPO_ROOT, CORPUS_REL);
  const raw = fs.readFileSync(corpusPath);
  const hash = crypto.createHash('sha256').update(raw).digest('hex');
  const data = JSON.parse(raw.toString());
  const records = Array.isArray(data) ? data : (data.records || data.phrases || []);
  const ids = records.map((r) => r.phrase_id || r.id || r.record_id);
  const unique = new Set(ids);
  const idRange = ids.length ? { min: ids[0], max: ids[ids.length - 1] } : null;
  const mismatches = [];
  if (records.length !== EXPECTED_COUNT) mismatches.push(`count:${records.length}`);
  if (unique.size !== records.length) mismatches.push('duplicate_ids');
  if (ids.some((x) => !x)) mismatches.push('missing_ids');
  if (!hash.startsWith(EXPECTED_HASH_PREFIX)) mismatches.push(`hash:${hash.slice(0, 16)}`);
  return {
    corpusPath,
    hash,
    hash_prefix: hash.slice(0, 16),
    record_count: records.length,
    unique_ids: unique.size,
    id_range: idRange,
    phrase_ids_registered: ids.length,
    pass: mismatches.length === 0,
    mismatches,
  };
}

function acquireLock(corpusHash) {
  const lockPath = path.join(RUN_STORAGE, 'locks', 'run.lock.json');
  if (fs.existsSync(lockPath)) {
    const existing = JSON.parse(fs.readFileSync(lockPath, 'utf8'));
    if (existing.status === 'ACTIVE' && Date.now() - new Date(existing.heartbeat).getTime() < existing.stale_after_ms) {
      throw new Error('LOCK_ALREADY_HELD');
    }
  }
  const lock = {
    schema_version: '1.0.0',
    run_id: RUN_ID,
    project_id: 'PRJ-0013',
    phase: 'SPPC-05_VALIDATION',
    owner_pid: process.pid,
    process_identity: `execute-phase-0-1-2-v1.mjs@${process.pid}`,
    corpus_checksum: corpusHash,
    acquired_at: new Date().toISOString(),
    heartbeat: new Date().toISOString(),
    stale_after_ms: 3600000,
    current_batch: null,
    permitted_writer: process.pid,
    status: 'ACTIVE',
  };
  loopMkdir(path.dirname(lockPath));
  try {
    const fd = fs.openSync(lockPath, fs.constants.O_CREAT | fs.constants.O_EXCL | fs.constants.O_WRONLY);
    fs.writeSync(fd, JSON.stringify(lock, null, 2));
    fs.closeSync(fd);
  } catch (e) {
    if (e.code === 'EEXIST') throw new Error('LOCK_ATOMIC_ACQUISITION_FAILED');
    throw e;
  }
  return { lockPath, lock };
}

function createInitialCheckpoint(corpusHash) {
  const cp = {
    run_id: RUN_ID,
    phase: 'SPPC-05_VALIDATION',
    corpus_checksum: corpusHash,
    total_input_count: EXPECTED_COUNT,
    processed_ids: [],
    completed_batches: [],
    processed_count: 0,
    failure_count: 0,
    retry_count: 0,
    cumulative_cost_usd: 0,
    model: OPERATOR.model,
    provider: OPERATOR.provider,
    prompt_contract_version: PROMPT_VERSION,
    hard_rules_version: 'hard-rules.mjs',
    adjudicator_version: ADJUDICATOR_VERSION,
    last_heartbeat: new Date().toISOString(),
    writer_identity: `execute-phase-0-1-2-v1.mjs@${process.pid}`,
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
    OLD_RUN_ID,
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
  walk(path.join(RUN_STORAGE, 'runtime'));
  walk(path.join(RUN_STORAGE, 'cache'));
  walk(path.join(RUN_STORAGE, 'batches'));
  walk(path.join(RUN_STORAGE, 'raw-responses'));
  const nonManifestDirs = ['cache', 'raw-responses', 'batches'].filter((d) => {
    const p = path.join(RUN_STORAGE, d);
    return fs.existsSync(p) && fs.readdirSync(p).length > 0;
  });
  return {
    verdict: forbiddenRefs.length === 0 && nonManifestDirs.length === 0 ? 'OLD_RUN_ISOLATION — PASS' : 'BLOCKED — OLD RUN STATE CONTAMINATION',
    pass: forbiddenRefs.length === 0 && nonManifestDirs.length === 0,
    forbidden_refs: forbiddenRefs,
    unexpected_runtime_data: nonManifestDirs,
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
    maxBuffer: 50 * 1024 * 1024,
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

function main() {
  const startedAt = new Date().toISOString();
  loadLocalSecrets();
  if (process.env.ORCA_SEMANTIC_MODEL !== OPERATOR.model || process.env.ORCA_SEMANTIC_PROVIDER !== OPERATOR.provider) {
    process.env.ORCA_SEMANTIC_PROVIDER = OPERATOR.provider;
    process.env.ORCA_SEMANTIC_MODEL = OPERATOR.model;
  }

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

  const inputManifest = {
    manifest_id: `${RUN_ID}-input-reference-v1`,
    run_id: RUN_ID,
    project_id: 'PRJ-0013',
    mig_session_id: 'session-mig-20260622-corv01',
    source_path: CORPUS_REL,
    source_corpus_id: 'corvonero-canonical-phrase-registry-v1',
    record_count: corpus.record_count,
    sha256: corpus.hash,
    sha256_prefix: corpus.hash_prefix,
    id_scheme: 'CR2-PHR-*',
    duplicate_ids: 0,
    missing_ids: 0,
    normalized_corpus_parent: {
      record_count: 2399,
      sha256_prefix: 'fbeb1b65d4a90cb0',
      lineage: '2399 → 31 duplicate clusters → 2368',
    },
    mutability: 'READ_ONLY',
    expected_consumer: 'SPPC-05 validation gate; future bounded production batches',
    registered_at: startedAt,
  };
  writeJsonAtomic(path.join(RUN_STORAGE, 'manifests', 'immutable-input-reference-v1.json'), inputManifest);

  const runManifest = {
    run_id: RUN_ID,
    project_id: 'PRJ-0013',
    mig_session_id: 'session-mig-20260622-corv01',
    corpus_id: 'corvonero-canonical-phrase-registry-v1',
    corpus_count: 2368,
    corpus_sha256: corpus.hash,
    orca_wave: '3.1F',
    prompt_contract_version: PROMPT_VERSION,
    hard_rules_version: 'hard-rules.mjs',
    adjudicator_version: ADJUDICATOR_VERSION,
    provider: OPERATOR.provider,
    model: OPERATOR.model,
    authority_class: 'CONTROLLED_SEMANTIC_RUN_V2',
    lifecycle_phase: 'SPPC-05_VALIDATION',
    created_at: startedAt,
    storage_root: RUN_STORAGE,
    git_run_dir: path.relative(REPO_ROOT, GIT_RUN_DIR),
    operator_decisions: OPERATOR,
    old_run_boundary: 'OLD_CORVONERO_RUN_NON_RESUMABLE',
  };
  writeJsonAtomic(path.join(RUN_STORAGE, 'manifests', 'run-manifest-v1.json'), runManifest);
  loopMkdir(GIT_RUN_DIR);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'run-manifest-v1.json'), runManifest);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'immutable-input-reference-v1.json'), inputManifest);

  const isolation = runIsolationTest();

  const costProjection = {
    fixture_live_records: 472,
    estimated_model_calls: 944,
    estimated_cost_usd: 0.23,
    hard_cap_usd: OPERATOR.hard_cost_cap_usd,
    soft_warning_usd: OPERATOR.soft_cost_warning_usd,
    sppc_05_allocation_usd: 1.0,
    full_corpus_forbidden: true,
    projected_in_bounds: true,
  };
  writeJsonAtomic(path.join(RUN_STORAGE, 'reports', 'cost-projection-pre-sppc05-v1.json'), costProjection);

  const { lockPath } = acquireLock(corpus.hash);
  const checkpoint = createInitialCheckpoint(corpus.hash);

  const testSuites = [
    { id: 'wave31f_bypass', script: 'projects/orca/semantic-intelligence/live-model/tests/run-wave31f-bypass-audit.mjs', live: false },
    { id: 'under_admission', script: 'projects/orca/semantic-intelligence/live-model/tests/run-under-admission-regression.mjs', live: false },
    { id: 'closed_dataset_regression', script: 'projects/orca/semantic-intelligence/live-model/tests/run-closed-dataset-regression.mjs', live: true },
    { id: 'confirmation_product', script: 'projects/orca/semantic-intelligence/live-model/tests/run-confirmation-validation.mjs', args: ['--stratum=protected_product_confirmation'], live: true },
    { id: 'confirmation_geo_v2', script: 'projects/orca/semantic-intelligence/live-model/tests/run-confirmation-validation.mjs', args: ['--stratum=geo_commercial_confirmation_v2'], live: true },
    { id: 'problem_query_policy', script: 'projects/orca/semantic-intelligence/live-model/tests/run-problem-query-policy-regression.mjs', live: true },
  ];

  const suiteResults = [];
  let cumulativeCost = 0;
  let blocked = false;

  if (!isolation.pass) {
    blocked = true;
  } else {
    for (const suite of testSuites) {
      const r = runNodeTest(suite.script, suite.args || []);
      const parsed = parseLastJson(r.stdout);
      if (parsed?.cost_usd) cumulativeCost += parsed.cost_usd;
      if (parsed?.metrics?.gate_pass === false) r.pass = false;
      suiteResults.push({ ...suite, ...r, parsed_summary: parsed });
      if (!r.pass) {
        blocked = true;
        break;
      }
      if (cumulativeCost > OPERATOR.hard_cost_cap_usd) {
        blocked = true;
        suiteResults.push({ error: 'COST_CAP_EXCEEDED', cumulativeCost });
        break;
      }
    }
  }

  const gateCriteria = evaluateGateCriteria(suiteResults);
  const gateBVerdict = blocked || !gateCriteria.all_pass
    ? { status: 'FAILED', project: 'BLOCKED_AT_SPPC_05' }
    : { status: 'PASS — OPERATOR REVIEW REQUIRED', project: 'FROZEN_PENDING_CANARY_AUTHORIZATION' };

  writeJsonAtomic(path.join(RUN_STORAGE, 'checkpoints', 'checkpoint-sppc05-complete-v1.json'), {
    ...checkpoint,
    phase: gateBVerdict.status.startsWith('PASS') ? 'SPPC-05_COMPLETE_PENDING_REVIEW' : 'BLOCKED_AT_SPPC_05',
    cumulative_cost_usd: cumulativeCost,
    sppc_05_completed_at: new Date().toISOString(),
    complete: gateBVerdict.status.startsWith('PASS'),
    gate_b_verdict: gateBVerdict.status,
  });

  const sppc05Report = {
    run_id: RUN_ID,
    provider: OPERATOR.provider,
    model: OPERATOR.model,
    prompt_contract_version: PROMPT_VERSION,
    adjudicator_version: ADJUDICATOR_VERSION,
    fixture_inventory: {
      protected_product_confirmation: 106,
      geo_commercial_confirmation_v2: 120,
      closed_dataset_supplementary: 136,
      problem_query_policy: 10,
      wave31f_bypass_checks: 12,
      under_admission_unit_tests: 18,
    },
    suite_results: suiteResults.map(({ script, pass, exit_code, runtime_ms, parsed_summary }) => ({
      script, pass, exit_code, runtime_ms, metrics: parsed_summary?.metrics || parsed_summary?.summary || parsed_summary,
    })),
    gate_criteria: gateCriteria,
    cumulative_cost_usd: cumulativeCost,
    gate_b_verdict: gateBVerdict,
    isolation,
    secret_summary: getSafeConfigSummary(),
    completed_at: new Date().toISOString(),
  };
  writeJsonAtomic(path.join(RUN_STORAGE, 'reports', 'sppc-05-execution-report-v1.json'), sppc05Report);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'reports', 'sppc-05-sanitized-report-v1.json'), sppc05Report);

  releaseLock(lockPath, gateBVerdict.status);

  const executionReceipt = {
    run_id: RUN_ID,
    phase: '0/1/2',
    started_at: startedAt,
    completed_at: new Date().toISOString(),
    gate_a: 'APPROVED',
    gate_b: gateBVerdict.status,
    lifecycle_state: gateBVerdict.project,
    provider: OPERATOR.provider,
    model: OPERATOR.model,
    corpus_verified: corpus.pass,
    isolation_verdict: isolation.verdict,
    cumulative_cost_usd: cumulativeCost,
    full_corpus_started: false,
    wave5_started: false,
  };
  writeJsonAtomic(path.join(RUN_STORAGE, 'receipts', 'phase-0-1-2-execution-receipt-v1.json'), executionReceipt);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'sanitized-execution-receipt-v1.json'), executionReceipt);

  console.log(JSON.stringify({
    run_id: RUN_ID,
    storage_root: RUN_STORAGE,
    gate_b: gateBVerdict,
    cumulative_cost_usd: cumulativeCost,
    isolation: isolation.verdict,
    suite_pass_count: suiteResults.filter((s) => s.pass).length,
    suite_total: suiteResults.length,
  }, null, 2));

  process.exit(gateBVerdict.status.startsWith('PASS') ? 0 : 1);
}

function evaluateGateCriteria(suiteResults) {
  const productConf = suiteResults.find((s) => s.id === 'confirmation_product');
  const geoConf = suiteResults.find((s) => s.id === 'confirmation_geo_v2');
  const closed = suiteResults.find((s) => s.id === 'closed_dataset_regression');
  const problem = suiteResults.find((s) => s.id === 'problem_query_policy');
  const bypass = suiteResults.find((s) => s.id === 'wave31f_bypass');
  const under = suiteResults.find((s) => s.id === 'under_admission');

  const productMetrics = productConf?.parsed_summary?.metrics;
  const geoMetrics = geoConf?.parsed_summary?.metrics;
  const closedSummary = closed?.parsed_summary?.summary;

  const criteria = {
    adversarial_fpr_max_0_01_product: productMetrics?.gate_pass === true,
    adversarial_fpr_max_0_01_geo: geoMetrics?.gate_pass === true,
    closed_dataset_boxed_delivery_fixed: closedSummary?.boxed_delivery_fixed === true,
    closed_dataset_product_fpr: closedSummary?.product_fpr === null || closedSummary?.product_fpr <= 0.01,
    problem_query_all_match: problem?.pass === true,
    wave31f_bypass_all_pass: bypass?.pass === true,
    under_admission_all_pass: under?.pass === true,
    all_suites_exit_zero: suiteResults.every((s) => s.pass),
  };
  criteria.all_pass = Object.values(criteria).every(Boolean);
  return criteria;
}

main();
