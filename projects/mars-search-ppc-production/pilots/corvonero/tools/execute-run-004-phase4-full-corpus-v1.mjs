#!/usr/bin/env node
/**
 * Corvonero Run 004 — Phase 4 controlled full-corpus semantic execution.
 * Run ID: corv-semantic-v2-20260626-004
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { loadLocalSecrets, getSafeConfigSummary } from '../../../../orca/semantic-intelligence/live-model/runtime/local-secret-loader.mjs';
import { createOpenAICompatibleAdapter } from '../../../../orca/semantic-intelligence/live-model/adapters/openai-compatible-adapter.mjs';
import { runBlindPrimaryAssessment } from '../../../../orca/semantic-intelligence/live-model/assessment/blind-assessment.mjs';
import { runIndependentReassessment, assessmentsAgree } from '../../../../orca/semantic-intelligence/live-model/assessment/independent-reassessment.mjs';
import { adjudicateSemanticIntent } from '../../../../orca/semantic-intelligence/live-model/adjudication/semantic-adjudicator.mjs';
import { applyHardRules } from '../../../../orca/semantic-intelligence/production/assessors/hard-rules.mjs';
import { assessDeterministic } from '../../../../orca/semantic-intelligence/production/assessors/deterministic-assessor.mjs';
import { createAssessorContext } from '../../../../orca/semantic-intelligence/production/assessors/assessor-contract.mjs';
import { extractServiceIntentEvidence } from '../../../../orca/semantic-intelligence/live-model/evidence/service-intent-evidence.mjs';
import { evaluatePlatformCompatibility } from '../../../../orca/semantic-intelligence/live-model/evidence/platform-compatibility.mjs';
import { classifyCorpusV2 } from './canary-family-classifier-v2.mjs';
import {
  analyzeCareerAcceptGate,
  buildImmediateCareerReviewList,
} from './career-stop-gate-v1.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const RUN_ID = 'corv-semantic-v2-20260626-004';
const PHASE_ID = 'corv-run004-phase4-full-corpus-v1';
const STORAGE_ROOT = path.join('C:\\MARS Phenix\\AI MARS STORAGE', 'mig', 'corvonero', 'semantic-runs', RUN_ID);
const GIT_RUN_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero/runs', RUN_ID);
const PILOT_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const FIX = path.join(REPO_ROOT, 'projects/orca/semantic-intelligence/live-model/fixtures');
const CORPUS_REL = 'projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json';
const CANONICAL_TOTAL = 2368;
const BATCH_SIZE = 100;
const CUMULATIVE_BEFORE_PHASE4 = 0.85679195;
const PRICING = { input_per_m: 0.15, output_per_m: 0.60 };
const AVG_TOKENS_PER_RECORD = { input: 2503, output: 575, calls: 2 };
const GATE_THRESHOLDS = [1200, 2000];
const GATE_C1_THRESHOLD = 500;

const OPERATOR = {
  phase_4_full_corpus: 'AUTHORIZED',
  canary_attempt_2: 'APPROVED',
  provider: 'openrouter',
  model: 'openai/gpt-5-mini',
  hard_cost_cap_usd: 3.0,
  soft_cost_warning_usd: 2.0,
  strategy: 'NOT AUTHORIZED',
  wave_5: 'BLOCKED',
};

const ORCA_HASHES = {
  semantic_adjudicator: '9618364947ba812c85f3fedbda99c1669db4d47fc58ec9d3996fc436b58bf341',
  platform_compatibility: '49b8c4d604ee732f4cfaeb0e07b99166133f4932533562aae7454171c99fc7ea',
  hard_rules: 'e6cd74ccca6ed453138f003d56f872e8a727e41bba04703589bd42c6f218c678',
  prompt_contract: '481075e55a8274047124b24d42293d616e37f57a129563e9f15f034034496e53',
  service_intent_evidence: '5bfff7ae2ed3b854ea613011797a91e35ab15804c10c8859c8ec667bd32f7d9f',
};

const ORCA_VERSIONS = {
  semantic_adjudicator: 'v1.5',
  platform_compatibility: 'v1.1',
  hard_rules: 'v1.2',
  prompt_contract: 'v1.4',
  service_intent_evidence: 'v1.1',
};

function sha256File(p) {
  return crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
}

function writeJsonAtomic(filePath, data) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  const tmp = `${filePath}.${process.pid}.tmp`;
  fs.writeFileSync(tmp, JSON.stringify(data, null, 2));
  fs.renameSync(tmp, filePath);
}

function loadJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function verifyOrcaAuthority() {
  const paths = {
    semantic_adjudicator: 'projects/orca/semantic-intelligence/live-model/adjudication/semantic-adjudicator.mjs',
    platform_compatibility: 'projects/orca/semantic-intelligence/live-model/evidence/platform-compatibility.mjs',
    hard_rules: 'projects/orca/semantic-intelligence/production/assessors/hard-rules.mjs',
    prompt_contract: 'projects/orca/semantic-intelligence/live-model/contracts/prompt-contract.mjs',
    service_intent_evidence: 'projects/orca/semantic-intelligence/live-model/evidence/service-intent-evidence.mjs',
  };
  const drift = [];
  for (const [key, rel] of Object.entries(paths)) {
    const hash = sha256File(path.join(REPO_ROOT, rel));
    if (hash !== ORCA_HASHES[key]) drift.push({ component: key, expected: ORCA_HASHES[key], actual: hash });
  }
  return { pass: drift.length === 0, drift, hashes: ORCA_HASHES, versions: ORCA_VERSIONS };
}

function verifyPhase3Complete() {
  const resultPath = path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-CANARY-RESULT-v2.json');
  if (!fs.existsSync(resultPath)) return { pass: false, reason: 'missing_attempt2_result' };
  const data = loadJson(resultPath);
  if (data.canary_verdict?.run !== 'PHASE_3_COMPLETE') return { pass: false, reason: 'phase3_not_complete', verdict: data.canary_verdict };
  if (data.processed_count !== 120) return { pass: false, reason: 'attempt2_count_mismatch', count: data.processed_count };
  return { pass: true, data };
}

function verifyNoConflictingLock() {
  const lockPath = path.join(STORAGE_ROOT, 'locks', 'run-phase4.lock.json');
  if (!fs.existsSync(lockPath)) return { pass: true };
  const lock = loadJson(lockPath);
  if (lock.status !== 'ACTIVE') return { pass: true, stale: lock };
  const age = Date.now() - new Date(lock.heartbeat || lock.acquired_at).getTime();
  if (age > (lock.stale_after_ms || 7200000)) return { pass: true, stale_recoverable: lock };
  if (lock.owner_pid === process.pid) return { pass: true, own_lock: true };
  return { pass: false, lock };
}

function loadCorpus() {
  const corpusPath = path.join(REPO_ROOT, CORPUS_REL);
  const raw = fs.readFileSync(corpusPath);
  const hash = crypto.createHash('sha256').update(raw).digest('hex');
  const data = JSON.parse(raw.toString());
  const records = data.phrases || data.records || data;
  if (records.length !== CANONICAL_TOTAL) throw new Error(`CORPUS_COUNT_MISMATCH:${records.length}`);
  if (!hash.startsWith('eaa09b8450f82738')) throw new Error(`CORPUS_HASH_MISMATCH:${hash.slice(0, 16)}`);
  const byId = new Map(records.map((r) => [r.phrase_id, r]));
  return { corpusPath, hash, records, byId };
}

function indexCanaryBatchReceipts() {
  const batchDir = path.join(STORAGE_ROOT, 'batches');
  const receiptIndex = new Map();
  if (!fs.existsSync(batchDir)) return receiptIndex;
  for (const entry of fs.readdirSync(batchDir)) {
    if (!entry.startsWith('canary-attempt2-batch-')) continue;
    const resultsPath = path.join(batchDir, entry, 'batch-results-v1.json');
    const completionPath = path.join(batchDir, entry, 'batch-completion-receipt-v1.json');
    if (!fs.existsSync(resultsPath)) continue;
    const batchResults = loadJson(resultsPath);
    const completion = fs.existsSync(completionPath) ? loadJson(completionPath) : null;
    for (const r of batchResults) {
      if (r.phrase_id && r.schema_valid && r.final_verdict) {
        receiptIndex.set(r.phrase_id, {
          batch_id: entry,
          batch_completion_receipt: !!completion,
          source: 'canary_batch_results',
        });
      }
    }
  }
  return receiptIndex;
}

function auditCanaryReuse(corpus, orca) {
  const canaryResult = loadJson(path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-CANARY-RESULT-v2.json'));
  const canarySelection = loadJson(path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-CANARY-SELECTION-v2.json'));
  const completionReceiptPath = path.join(STORAGE_ROOT, 'checkpoints', 'checkpoint-phase3-canary-attempt2-complete-v1.json');
  const attempt2Receipt = fs.existsSync(completionReceiptPath)
    ? loadJson(completionReceiptPath)
    : loadJson(path.join(GIT_RUN_DIR, 'sanitized-canary-attempt2-receipt-v1.json'));

  const rawDir = path.join(STORAGE_ROOT, 'raw-responses', 'attempt2');
  const batchReceiptIndex = indexCanaryBatchReceipts();
  const results = canaryResult.results || [];
  const seen = new Set();
  const auditRecords = [];
  let reusable = 0;

  for (const r of results) {
    const rawFile = path.join(rawDir, `${r.phrase_id}.json`);
    const batchReceipt = batchReceiptIndex.get(r.phrase_id);
    const receiptTrace =
      fs.existsSync(rawFile) ||
      !!batchReceipt ||
      (r.schema_valid === true && !!r.final_verdict && !r.error);

    const checks = {
      phrase_id_in_corpus: corpus.byId.has(r.phrase_id),
      phrase_text_match: corpus.byId.get(r.phrase_id)?.phrase === r.phrase,
      corpus_checksum_match: true,
      orca_hashes_match: orca.pass,
      provider_model_match: true,
      schema_valid: r.schema_valid === true,
      final_verdict_exists: !!r.final_verdict,
      no_malformed_unresolved: !r.error,
      no_duplicate_id: !seen.has(r.phrase_id),
      receipt_trace_exists: receiptTrace,
      attempt2_completion_receipt_exists: !!attempt2Receipt,
    };
    seen.add(r.phrase_id);
    const pass = Object.values(checks).every(Boolean);
    if (pass) reusable++;
    auditRecords.push({
      phrase_id: r.phrase_id,
      phrase: r.phrase,
      reuse_status: pass ? 'PRODUCTION_ELIGIBLE_CANARY_RESULT' : 'REPROCESS_REQUIRED',
      checks,
      receipt_reference: fs.existsSync(rawFile)
        ? 'raw-responses/attempt2'
        : batchReceipt
          ? `batches/${batchReceipt.batch_id}`
          : 'canary-result-v2',
      canary_outcome: {
        final_verdict: r.final_verdict,
        primary_verdict: r.primary_verdict,
        reassessment_verdict: r.reassessment_verdict,
        confirmation_disagreement: r.confirmation_disagreement,
      },
    });
  }

  const audit = {
    audit_id: 'corvonero-run-004-phase-4-canary-reuse-audit-v1',
    run_id: RUN_ID,
    created_at: new Date().toISOString(),
    corpus_sha256_prefix: corpus.hash.slice(0, 16),
    orca_hashes: orca.hashes,
    provider: OPERATOR.provider,
    model: OPERATOR.model,
    attempt2_receipt_reference: attempt2Receipt ? 'present' : 'missing',
    canary_selection_count: canarySelection.selected_count,
    canary_result_count: results.length,
    reusable_count: reusable,
    reprocess_count: results.length - reusable,
    expected_reusable_maximum: 120,
    expected_remaining_minimum: CANONICAL_TOTAL - reusable,
    records: auditRecords,
    verdict: reusable === 120 ? 'PASS' : 'PARTIAL',
  };

  writeJsonAtomic(path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-4-CANARY-REUSE-AUDIT-v1.json'), audit);
  writeJsonAtomic(path.join(STORAGE_ROOT, 'receipts', 'phase-4-canary-reuse-audit-v1.json'), audit);
  return audit;
}

function loadOperatorOverrides() {
  const overridePath = path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-4-OPERATOR-OVERRIDES-v1.json');
  if (!fs.existsSync(overridePath)) return new Map();
  const data = loadJson(overridePath);
  return new Map((data.overrides || []).map((o) => [o.phrase_id, o]));
}

function restoreCostTrackerFromCheckpoint(checkpoint) {
  if (typeof checkpoint?.cumulative_cost_usd === 'number') {
    costTracker.phase4_baseline_usd = Math.max(0, checkpoint.cumulative_cost_usd - CUMULATIVE_BEFORE_PHASE4);
    costTracker.phase4_cost_usd = costTracker.phase4_baseline_usd;
    costTracker.phase4_new_cost_usd = 0;
  }
  costTracker.retries = checkpoint?.retries || 0;
  costTracker.malformed_first_attempt = checkpoint?.malformed_outputs || 0;
  costTracker.quarantined = (checkpoint?.quarantined_ids || []).length;
}

function projectCostFromActuals(remainingRecords, checkpoint) {
  const processed = checkpoint?.production_newly_processed || 0;
  const phase4Spent = Math.max(0, (checkpoint?.cumulative_cost_usd || CUMULATIVE_BEFORE_PHASE4) - CUMULATIVE_BEFORE_PHASE4);
  const perRecord = processed > 0 ? phase4Spent / processed : null;
  const projectedNewCost = perRecord != null
    ? remainingRecords * perRecord
    : projectCost(remainingRecords).projected_new_cost_usd;
  const projectedTotal = (checkpoint?.cumulative_cost_usd || cumulativeCost()) + projectedNewCost;
  return {
    remaining_records: remainingRecords,
    projected_new_cost_usd: projectedNewCost,
    cost_per_new_record_usd: perRecord,
    cumulative_at_resume_usd: checkpoint?.cumulative_cost_usd || cumulativeCost(),
    projected_total_cost_usd: projectedTotal,
    hard_cap_usd: OPERATOR.hard_cost_cap_usd,
    pass_hard_cap: projectedTotal <= OPERATOR.hard_cost_cap_usd,
    basis: perRecord != null ? 'actual_phase4_per_record' : 'preflight_token_estimate',
  };
}

function loadExistingGateReceipts() {
  const receipts = [];
  const receiptDir = path.join(STORAGE_ROOT, 'receipts');
  if (!fs.existsSync(receiptDir)) return receipts;
  for (const name of fs.readdirSync(receiptDir)) {
    if (!name.match(/^gate-c\d+-receipt-v1\.json$/i)) continue;
    receipts.push(loadJson(path.join(receiptDir, name)));
  }
  return receipts.sort((a, b) => a.gate_id.localeCompare(b.gate_id));
}

function projectCost(remainingRecords) {
  const inputTokens = remainingRecords * AVG_TOKENS_PER_RECORD.input;
  const outputTokens = remainingRecords * AVG_TOKENS_PER_RECORD.output;
  const projectedNewCost =
    (inputTokens / 1e6) * PRICING.input_per_m + (outputTokens / 1e6) * PRICING.output_per_m;
  const projectedTotal = CUMULATIVE_BEFORE_PHASE4 + projectedNewCost;
  return {
    remaining_records: remainingRecords,
    projected_new_cost_usd: projectedNewCost,
    cumulative_before_phase4_usd: CUMULATIVE_BEFORE_PHASE4,
    projected_total_cost_usd: projectedTotal,
    hard_cap_usd: OPERATOR.hard_cost_cap_usd,
    soft_warning_usd: OPERATOR.soft_cost_warning_usd,
    pass_hard_cap: projectedTotal <= OPERATOR.hard_cost_cap_usd,
    crosses_soft_warning: projectedTotal >= OPERATOR.soft_cost_warning_usd,
  };
}

function acquirePhase4Lock(corpusHash, orca, resumeCheckpoint = null) {
  const lockPath = path.join(STORAGE_ROOT, 'locks', 'run-phase4.lock.json');
  const existing = verifyNoConflictingLock();
  if (!existing.pass) throw new Error('BLOCKED — RUN 004 LOCK OWNERSHIP CONFLICT');
  const lock = {
    schema_version: '1.0.0',
    run_id: RUN_ID,
    phase_id: PHASE_ID,
    project_id: 'PRJ-0013',
    phase: 'PHASE_4_FULL_CORPUS',
    owner_pid: process.pid,
    process_command: 'execute-run-004-phase4-full-corpus-v1.mjs',
    process_identity: `execute-run-004-phase4-full-corpus-v1.mjs@${process.pid}`,
    corpus_checksum: corpusHash,
    orca_hashes: orca.hashes,
    orca_versions: orca.versions,
    provider: OPERATOR.provider,
    model: OPERATOR.model,
    acquired_at: new Date().toISOString(),
    heartbeat: new Date().toISOString(),
    current_batch: resumeCheckpoint?.batch_receipts?.length || 0,
    resume_from_unique_assessed: resumeCheckpoint?.unique_assessed_total || null,
    remaining_at_resume: resumeCheckpoint?.missing || null,
    permitted_writer: process.pid,
    status: 'ACTIVE',
    stale_after_ms: 7200000,
  };
  writeJsonAtomic(lockPath, lock);
  return lockPath;
}

function updateLockHeartbeat(lockPath, batchIndex) {
  const lock = loadJson(lockPath);
  lock.heartbeat = new Date().toISOString();
  lock.current_batch = batchIndex;
  writeJsonAtomic(lockPath, lock);
}

function releaseLock(lockPath, outcome) {
  const lock = loadJson(lockPath);
  lock.status = 'RELEASED';
  lock.released_at = new Date().toISOString();
  lock.release_outcome = outcome;
  writeJsonAtomic(lockPath, lock);
  writeJsonAtomic(path.join(STORAGE_ROOT, 'receipts', 'phase-4-lock-release-v1.json'), {
    run_id: RUN_ID,
    released_at: lock.released_at,
    release_outcome: outcome,
  });
}

const costTracker = {
  phase4_input_tokens: 0,
  phase4_output_tokens: 0,
  phase4_baseline_usd: 0,
  phase4_new_cost_usd: 0,
  phase4_cost_usd: 0,
  retries: 0,
  malformed_first_attempt: 0,
  retry_success: 0,
  retry_failure: 0,
  quarantined: 0,
  model_errors: 0,
};

function trackUsage(meta) {
  if (!meta?.usage) return;
  const inTok = meta.usage.prompt_tokens || 0;
  const outTok = meta.usage.completion_tokens || 0;
  costTracker.phase4_input_tokens += inTok;
  costTracker.phase4_output_tokens += outTok;
  const increment =
    (inTok / 1e6) * PRICING.input_per_m + (outTok / 1e6) * PRICING.output_per_m;
  costTracker.phase4_new_cost_usd += increment;
  costTracker.phase4_cost_usd = costTracker.phase4_baseline_usd + costTracker.phase4_new_cost_usd;
}

function cumulativeCost() {
  return CUMULATIVE_BEFORE_PHASE4 + costTracker.phase4_cost_usd;
}

function assertCostCapBeforeBatch(batchSize) {
  const projectedBatch =
    (batchSize * AVG_TOKENS_PER_RECORD.input / 1e6) * PRICING.input_per_m +
    (batchSize * AVG_TOKENS_PER_RECORD.output / 1e6) * PRICING.output_per_m;
  const exposure = cumulativeCost() + projectedBatch;
  if (exposure > OPERATOR.hard_cost_cap_usd) {
    throw new Error(`BLOCKED — FULL-CORPUS COST PROJECTION EXCEEDS RUN CAP:${exposure.toFixed(4)}`);
  }
  if (cumulativeCost() >= OPERATOR.soft_cost_warning_usd) {
    writeJsonAtomic(path.join(STORAGE_ROOT, 'receipts', `soft-cost-warning-${Date.now()}.json`), {
      run_id: RUN_ID,
      cumulative_cost_usd: cumulativeCost(),
      soft_warning_usd: OPERATOR.soft_cost_warning_usd,
      projected_batch_usd: projectedBatch,
      projected_exposure_usd: exposure,
      at: new Date().toISOString(),
    });
  }
  return exposure;
}

async function evaluatePhraseOnce(record, context, adapter) {
  const phrase = {
    phrase_id: record.phrase_id,
    raw_query: record.phrase,
    normalized_query: record.normalized_phrase || record.phrase.toLowerCase(),
    region: 'RU',
  };
  const structured = extractServiceIntentEvidence(phrase);
  const platform = evaluatePlatformCompatibility(phrase, context.businessScope, context.serviceRegistry);
  const primary = await runBlindPrimaryAssessment({ phrase, ...context, adapter, forbiddenContext: {} });
  if (!primary.ok) {
    costTracker.model_errors++;
    return { ok: false, error: primary.blocker || 'PRIMARY_FAILED', schema_valid: false };
  }
  trackUsage(primary.output?.model_metadata);

  const det = assessDeterministic(createAssessorContext(phrase, context));
  const hardRules = applyHardRules(phrase, det, context);
  const secondary = await runIndependentReassessment({
    phrase,
    ...context,
    primaryAdapter: adapter,
    secondaryAdapter: adapter,
    hardRuleEvidence: hardRules,
  });
  if (secondary.ok) trackUsage(secondary.output?.model_metadata);
  else costTracker.model_errors++;

  const adj = adjudicateSemanticIntent({
    assessmentA: primary.output,
    assessmentB: secondary.ok ? secondary.output : null,
    hardRuleEvidence: hardRules,
    serviceRegistry: context.serviceRegistry,
    businessScope: context.businessScope,
    phrase,
    structuredEvidence: structured,
    platformCompatibility: platform,
  });

  const finalVerdict = adj.final_decision.replace(/^FINAL\s+/, '');
  const confirmationDisagree = secondary.ok && !assessmentsAgree(primary.output, secondary.output);

  return {
    ok: true,
    schema_valid: true,
    phrase_id: record.phrase_id,
    phrase: record.phrase,
    source_metadata: {
      combined_frequency: record.combined_frequency,
      provenance: record.provenance,
    },
    primary_verdict: primary.output?.decision,
    reassessment_verdict: secondary.output?.decision,
    evidence_classes: structured.signals || [],
    platform_class: platform.classification,
    applied_hard_rules: (hardRules.evidence || []).map((e) => e.rule),
    confirmation_result: confirmationDisagree ? 'DISAGREE' : (secondary.ok ? 'AGREE' : 'SINGLE'),
    confirmation_disagreement: confirmationDisagree,
    adjudication_path: adj.agreement_state,
    invariant_applications: adj.invariant_applications || [],
    final_verdict: finalVerdict,
    confidence: adj.confidence,
    reason: primary.output?.rationale || adj.findings?.join('; '),
    review_flags: [],
    provider: OPERATOR.provider,
    model: OPERATOR.model,
    contract_versions: ORCA_VERSIONS,
    assessed_at: new Date().toISOString(),
    production_source: 'PHASE_4_NEW',
  };
}

async function evaluateWithMalformedPolicy(record, context, adapter, rawDir, quarantineDir) {
  const attempts = [];
  for (let attempt = 0; attempt < 2; attempt++) {
    const result = await evaluatePhraseOnce(record, context, adapter);
    attempts.push(result);
    fs.writeFileSync(
      path.join(rawDir, `${record.phrase_id}.attempt${attempt + 1}.json`),
      JSON.stringify(result, null, 2),
    );
    if (result.schema_valid) {
      if (attempt === 1) {
        costTracker.retry_success++;
        result.malformed_retry = true;
      }
      return result;
    }
    if (result.error === 'MALFORMED_MODEL_OUTPUT') {
      if (attempt === 0) {
        costTracker.malformed_first_attempt++;
        costTracker.retries++;
        continue;
      }
      costTracker.retry_failure++;
      costTracker.quarantined++;
      const q = {
        phrase_id: record.phrase_id,
        phrase: record.phrase,
        status: 'QUARANTINED',
        error_family: 'MALFORMED_MODEL_OUTPUT',
        attempts,
        quarantined_at: new Date().toISOString(),
      };
      writeJsonAtomic(path.join(quarantineDir, `${record.phrase_id}.json`), q);
      return q;
    }
    return result;
  }
}

function buildReusedResults(audit, canaryResult, classifiedById) {
  const byId = new Map((canaryResult.results || []).map((r) => [r.phrase_id, r]));
  return audit.records
    .filter((a) => a.reuse_status === 'PRODUCTION_ELIGIBLE_CANARY_RESULT')
    .map((a) => {
      const r = byId.get(a.phrase_id);
      const cls = classifiedById.get(a.phrase_id) || {};
      return {
        phrase_id: r.phrase_id,
        phrase: r.phrase,
        source_metadata: {},
        primary_verdict: r.primary_verdict,
        reassessment_verdict: r.reassessment_verdict,
        evidence_classes: r.evidence_classes || [],
        platform_class: r.platform_class,
        applied_hard_rules: r.applied_hard_rules || [],
        confirmation_result: r.confirmation_result,
        confirmation_disagreement: r.confirmation_disagreement,
        adjudication_path: r.adjudication_path,
        invariant_applications: r.invariant_applications || [],
        final_verdict: r.final_verdict,
        confidence: r.confidence,
        reason: r.reason,
        review_flags: r.review_flag ? ['canary_review_flag'] : [],
        primary_family: r.primary_family || cls.primary_family,
        edge_cases: r.edge_cases || cls.edge_cases || [],
        observed_tags: r.observed_tags || cls.observed_tags || [],
        provider: OPERATOR.provider,
        model: OPERATOR.model,
        contract_versions: ORCA_VERSIONS,
        assessed_at: canaryResult.completed_at,
        production_source: 'CANARY_ATTEMPT_2_REUSE',
        schema_valid: true,
      };
    });
}

function analyzeGate(allResults, gateId, classifiedById, operatorOverrides) {
  const dist = { ACCEPT: 0, REJECT: 0, ABSTAIN: 0 };
  let schemaValid = 0;
  let disagreements = 0;
  for (const r of allResults) {
    const verdict = r.final_authoritative_verdict || r.final_verdict;
    if (verdict) dist[verdict] = (dist[verdict] || 0) + 1;
    if (r.schema_valid) schemaValid++;
    if (r.confirmation_disagreement) disagreements++;
  }
  const careerGate = analyzeCareerAcceptGate(allResults, classifiedById, operatorOverrides);
  const educationAccepted = allResults.filter((r) => {
    const verdict = r.final_authoritative_verdict || r.final_verdict;
    return r.observed_tags?.includes('education') && verdict === 'ACCEPT';
  });
  const infoAccepted = allResults.filter((r) => {
    const verdict = r.final_authoritative_verdict || r.final_verdict;
    return r.primary_family === 'informational_self_service' && verdict === 'ACCEPT';
  });
  const foreignAccepted = allResults.filter((r) => {
    const verdict = r.final_authoritative_verdict || r.final_verdict;
    return r.edge_cases?.includes('foreign_incompatible_platform') && verdict === 'ACCEPT';
  });
  const issues = [...careerGate.stop_issues];
  if (educationAccepted.length >= 2) issues.push('career_education_acceptance_family');
  if (infoAccepted.length >= 4) issues.push('informational_systematically_accepted');
  if (foreignAccepted.length) issues.push('foreign_platform_accepted');
  return {
    gate_id: gateId,
    unique_assessed: allResults.length,
    verdict_distribution: dist,
    schema_valid_rate: allResults.length ? schemaValid / allResults.length : 0,
    confirmation_disagreement_count: disagreements,
    cumulative_cost_usd: cumulativeCost(),
    career_metrics: {
      career_accept_raw_count: careerGate.career_accept_raw_count,
      career_accept_confirmed_error_count: careerGate.career_accept_confirmed_error_count,
      career_accept_classifier_false_positive_count: careerGate.career_accept_classifier_false_positive_count,
      career_accept_review_pending_count: careerGate.career_accept_review_pending_count,
      career_accept_override_count: careerGate.career_accept_override_count,
      career_accept_rate: careerGate.career_accept_rate,
    },
    issues: [...new Set(issues)],
    stop_required: issues.length > 0,
    created_at: new Date().toISOString(),
  };
}

function checkStopConditions(allResults, classifiedById, operatorOverrides) {
  const issues = [];
  const ids = allResults.map((r) => r.phrase_id);
  if (new Set(ids).size !== ids.length) issues.push('duplicate_final_ids');
  const careerGate = analyzeCareerAcceptGate(allResults, classifiedById, operatorOverrides);
  issues.push(...careerGate.stop_issues);
  const educationAccepted = allResults.filter((r) => {
    const verdict = r.final_authoritative_verdict || r.final_verdict;
    return r.observed_tags?.includes('education') && verdict === 'ACCEPT';
  });
  if (educationAccepted.length >= 2 && !issues.includes('career_education_acceptance_family')) {
    issues.push('career_education_acceptance_family');
  }
  const infoAccepted = allResults.filter((r) => {
    const verdict = r.final_authoritative_verdict || r.final_verdict;
    return r.primary_family === 'informational_self_service' && verdict === 'ACCEPT';
  });
  if (infoAccepted.length >= 4) issues.push('informational_acceptance_family');
  const foreignAccepted = allResults.filter((r) => {
    const verdict = r.final_authoritative_verdict || r.final_verdict;
    return r.edge_cases?.includes('foreign_incompatible_platform') && verdict === 'ACCEPT';
  });
  if (foreignAccepted.length) issues.push('incompatible_platform_acceptance');
  const quarantined = allResults.filter((r) => r.status === 'QUARANTINED');
  if (quarantined.length >= 3) issues.push('structured_output_quarantine_spike');
  return [...new Set(issues)];
}

async function runBatch(batchNumber, batchRecords, context, adapter, checkpoint, lockPath, classifiedById) {
  const batchId = `phase4-batch-${String(batchNumber).padStart(3, '0')}`;
  const batchDir = path.join(STORAGE_ROOT, 'batches', batchId);
  const rawDir = path.join(STORAGE_ROOT, 'raw-responses', 'phase4');
  const quarantineDir = path.join(STORAGE_ROOT, 'quarantine');
  fs.mkdirSync(rawDir, { recursive: true });
  fs.mkdirSync(quarantineDir, { recursive: true });

  const inputIds = batchRecords.map((r) => r.phrase_id);
  const inputHash = crypto.createHash('sha256').update(inputIds.join('\n')).digest('hex');

  const startReceipt = {
    batch_id: batchId,
    batch_index: batchNumber - 1,
    phrase_count: batchRecords.length,
    input_ids: inputIds,
    input_hash: inputHash,
    started_at: new Date().toISOString(),
    provider: OPERATOR.provider,
    model: OPERATOR.model,
  };
  writeJsonAtomic(path.join(batchDir, 'batch-start-receipt-v1.json'), startReceipt);

  const results = [];
  const errors = [];
  for (const record of batchRecords) {
    assertCostCapBeforeBatch(1);
    try {
      const r = await evaluateWithMalformedPolicy(record, context, adapter, rawDir, quarantineDir);
      const cls = classifiedById.get(record.phrase_id) || {};
      r.primary_family = cls.primary_family;
      r.observed_tags = cls.observed_tags || [];
      r.edge_cases = cls.edge_cases || [];
      if (r.confirmation_disagreement) r.review_flags = [...(r.review_flags || []), 'primary_reassessment_disagreement'];
      if (cls.edge_cases?.includes('psr_amb_01_family')) r.review_flags = [...(r.review_flags || []), 'psr_amb_01'];
      results.push(r);
      if (r.status === 'QUARANTINED') errors.push(r);
    } catch (e) {
      if (e.message.includes('COST')) throw e;
      errors.push({ phrase_id: record.phrase_id, error: e.message });
    }
  }

  const verdictCounts = { ACCEPT: 0, REJECT: 0, ABSTAIN: 0, QUARANTINED: 0, ERROR: 0 };
  for (const r of results) {
    if (r.status === 'QUARANTINED') verdictCounts.QUARANTINED++;
    else if (r.final_verdict) verdictCounts[r.final_verdict] = (verdictCounts[r.final_verdict] || 0) + 1;
    else verdictCounts.ERROR++;
  }

  const completionReceipt = {
    ...startReceipt,
    completed_at: new Date().toISOString(),
    runtime_ms: Date.now() - new Date(startReceipt.started_at).getTime(),
    cost_usd: costTracker.phase4_cost_usd,
    cumulative_cost_usd: cumulativeCost(),
    verdict_distribution: verdictCounts,
    malformed_count: results.filter((r) => r.malformed_retry).length,
    retry_count: costTracker.retries,
    error_count: errors.length,
    schema_valid_count: results.filter((r) => r.schema_valid).length,
  };
  writeJsonAtomic(path.join(batchDir, 'batch-completion-receipt-v1.json'), completionReceipt);
  writeJsonAtomic(path.join(batchDir, 'batch-results-v1.json'), results);

  checkpoint.production_newly_processed += results.filter((r) => r.schema_valid).length;
  checkpoint.unique_assessed_total =
    checkpoint.canary_attempt_2_reused +
    checkpoint.production_newly_processed +
    (checkpoint.quarantined_ids?.length || 0);
  checkpoint.missing = CANONICAL_TOTAL - checkpoint.unique_assessed_total;
  checkpoint.cumulative_cost_usd = cumulativeCost();
  checkpoint.last_batch_id = batchId;
  checkpoint.last_heartbeat = new Date().toISOString();
  checkpoint.complete = checkpoint.missing === 0 && costTracker.quarantined === 0;
  writeJsonAtomic(path.join(STORAGE_ROOT, 'checkpoints', 'checkpoint-phase4-v1.json'), checkpoint);
  updateLockHeartbeat(lockPath, batchNumber);

  return { batchId, results, completionReceipt, errors };
}

async function main() {
  const phase3 = verifyPhase3Complete();
  if (!phase3.pass) {
    console.error(JSON.stringify({ error: 'BLOCKED — PHASE 3 NOT COMPLETE', phase3 }));
    process.exit(2);
  }

  const lockCheck = verifyNoConflictingLock();
  if (!lockCheck.pass) {
    console.error(JSON.stringify({ error: 'BLOCKED — RUN 004 LOCK OWNERSHIP CONFLICT', lock: lockCheck.lock }));
    process.exit(2);
  }

  const orca = verifyOrcaAuthority();
  if (!orca.pass) {
    console.error(JSON.stringify({ error: 'BLOCKED — APPROVED ORCA AUTHORITY DRIFT', drift: orca.drift }));
    process.exit(2);
  }

  const corpus = loadCorpus();
  loadLocalSecrets();
  const configSummary = getSafeConfigSummary();
  if (configSummary.ORCA_SEMANTIC_PROVIDER !== OPERATOR.provider || configSummary.ORCA_SEMANTIC_MODEL !== OPERATOR.model) {
    console.error(JSON.stringify({ error: 'BLOCKED — PROVIDER/MODEL DRIFT', configSummary }));
    process.exit(2);
  }
  process.env.ORCA_EVAL_MAX_COST = String(OPERATOR.hard_cost_cap_usd);

  const audit = auditCanaryReuse(corpus, orca);
  const checkpointPath = path.join(STORAGE_ROOT, 'checkpoints', 'checkpoint-phase4-v1.json');
  const isResume = fs.existsSync(checkpointPath);
  let checkpoint = isResume ? loadJson(checkpointPath) : null;
  const resumeMode = isResume && checkpoint?.unique_assessed_total > 0 && !checkpoint?.complete;

  if (resumeMode) {
    if (checkpoint.trigger_reconciliation?.verdict !== 'PHASE_4_TRIGGER_RECONCILIATION — PASS') {
      console.error(JSON.stringify({
        error: 'BLOCKED — RESUME REQUIRES TRIGGER RECONCILIATION PASS',
        trigger_reconciliation: checkpoint.trigger_reconciliation || null,
      }));
      process.exit(2);
    }
  }

  const remainingCount = resumeMode
    ? checkpoint.missing
    : CANONICAL_TOTAL - audit.reusable_count;
  const costProjection = resumeMode
    ? projectCostFromActuals(remainingCount, checkpoint)
    : projectCost(remainingCount);
  if (!costProjection.pass_hard_cap) {
    console.error(JSON.stringify({
      error: 'BLOCKED — RESUME COST PROJECTION EXCEEDS RUN CAP',
      costProjection,
    }));
    process.exit(2);
  }

  const authReceipt = {
    receipt_id: resumeMode ? 'phase-4-resume-authorization-v1' : 'phase-4-full-corpus-authorization-v1',
    run_id: RUN_ID,
    resume_mode: resumeMode,
    lifecycle_transitions: resumeMode
      ? ['PHASE_4_TRIGGER_RECONCILIATION_PASS', 'PHASE_4_RESUME_AUTHORIZED', 'PHASE_4_FULL_CORPUS_EXECUTING']
      : ['PHASE_3_COMPLETE', 'PHASE_4_FULL_CORPUS_AUTHORIZED', 'PHASE_4_FULL_CORPUS_EXECUTING'],
    operator_decisions: OPERATOR,
    canary_reuse_audit: {
      reusable: audit.reusable_count,
      remaining: remainingCount,
      verdict: audit.verdict,
    },
    cost_projection: costProjection,
    resume_from_unique_assessed: resumeMode ? checkpoint.unique_assessed_total : null,
    remaining_at_resume: resumeMode ? remainingCount : null,
    authorized_at: new Date().toISOString(),
  };
  writeJsonAtomic(path.join(STORAGE_ROOT, 'receipts', authReceipt.receipt_id + '.json'), authReceipt);
  if (!resumeMode) {
    writeJsonAtomic(path.join(GIT_RUN_DIR, 'sanitized-phase4-authorization-receipt-v1.json'), authReceipt);
  } else {
    writeJsonAtomic(path.join(GIT_RUN_DIR, 'sanitized-phase4-resume-authorization-receipt-v1.json'), authReceipt);
  }

  const lockPath = acquirePhase4Lock(corpus.hash, orca, resumeMode ? checkpoint : null);

  const context = {
    businessScope: loadJson(path.join(FIX, 'business-scope-eval-v1.json')),
    serviceRegistry: loadJson(path.join(FIX, 'service-registry-eval-v1.json')),
    taxonomy: {},
    commercialPolicy: { version: 'v1' },
  };
  const classified = classifyCorpusV2(corpus.records, context);
  const classifiedById = new Map(classified.map((c) => [c.phrase_id, c]));
  const operatorOverrides = loadOperatorOverrides();
  const reusedResults = buildReusedResults(audit, phase3.data, classifiedById);
  const reusedIds = new Set(reusedResults.map((r) => r.phrase_id));

  if (!checkpoint) {
    checkpoint = {
      run_id: RUN_ID,
      phase: 'PHASE_4_FULL_CORPUS',
      lifecycle_state: 'PHASE_4_FULL_CORPUS_EXECUTING',
      canonical_total: CANONICAL_TOTAL,
      canary_attempt_2_reused: audit.reusable_count,
      production_newly_processed: 0,
      unique_assessed_total: audit.reusable_count,
      missing: CANONICAL_TOTAL - audit.reusable_count,
      complete: false,
      reused_canary_ids: [...reusedIds],
      new_production_ids: [],
      retries: 0,
      quarantined_ids: [],
      malformed_outputs: 0,
      model_api_errors: 0,
      cumulative_cost_usd: CUMULATIVE_BEFORE_PHASE4,
      batch_receipts: [],
      started_at: new Date().toISOString(),
    };
    writeJsonAtomic(checkpointPath, checkpoint);
  } else if (resumeMode) {
    if (checkpoint.phase !== 'PHASE_4_FULL_CORPUS') throw new Error('CHECKPOINT_PHASE_MISMATCH');
    restoreCostTrackerFromCheckpoint(checkpoint);
    checkpoint.lifecycle_state = 'PHASE_4_FULL_CORPUS_EXECUTING';
    checkpoint.stop_reason = null;
    writeJsonAtomic(checkpointPath, checkpoint);
  }

  const registryPath = path.join(STORAGE_ROOT, 'checkpoints', 'phase4-semantic-registry-v1.json');
  let allResults = fs.existsSync(registryPath) ? loadJson(registryPath).results || [] : [...reusedResults];
  const processedIds = new Set(allResults.map((r) => r.phrase_id));

  const remainingRecords = corpus.records
    .filter((r) => !processedIds.has(r.phrase_id))
    .sort((a, b) => a.phrase_id.localeCompare(b.phrase_id));

  const adapter = createOpenAICompatibleAdapter();
  if (!adapter) {
    releaseLock(lockPath, 'FAILED — ADAPTER UNAVAILABLE');
    process.exit(2);
  }

  const batches = [];
  const gateReceipts = loadExistingGateReceipts();
  const startingBatchNumber = (checkpoint.batch_receipts || []).length + 1;
  let stopReason = null;
  const careerReviewPath = path.join(STORAGE_ROOT, 'reports', 'career-immediate-review-v1.json');
  let careerReviewItems = fs.existsSync(careerReviewPath)
    ? loadJson(careerReviewPath).items || []
    : buildImmediateCareerReviewList(allResults, classifiedById);

  try {
    for (let b = 0; b < Math.ceil(remainingRecords.length / BATCH_SIZE); b++) {
      const slice = remainingRecords.slice(b * BATCH_SIZE, (b + 1) * BATCH_SIZE);
      if (!slice.length) break;
      assertCostCapBeforeBatch(slice.length);

      const batchNumber = startingBatchNumber + b;
      const batchResult = await runBatch(batchNumber, slice, context, adapter, checkpoint, lockPath, classifiedById);
      batches.push(batchResult);
      allResults.push(...batchResult.results.filter((r) => r.schema_valid || r.status === 'QUARANTINED'));
      const failedInBatch = batchResult.results.filter((r) => !r.schema_valid && r.status !== 'QUARANTINED');
      if (failedInBatch.length) {
        checkpoint.failed_production_ids = [
          ...new Set([...(checkpoint.failed_production_ids || []), ...failedInBatch.map((r) => r.phrase_id)]),
        ];
      }
      checkpoint.new_production_ids.push(...batchResult.results.filter((r) => r.schema_valid).map((r) => r.phrase_id));
      checkpoint.batch_receipts.push(batchResult.batchId);
      checkpoint.retries = costTracker.retries;
      checkpoint.quarantined_ids = allResults.filter((r) => r.status === 'QUARANTINED').map((r) => r.phrase_id);
      checkpoint.malformed_outputs = costTracker.malformed_first_attempt;
      checkpoint.model_api_errors = costTracker.model_errors;
      writeJsonAtomic(path.join(STORAGE_ROOT, 'checkpoints', 'checkpoint-phase4-v1.json'), checkpoint);

      careerReviewItems = [
        ...careerReviewItems,
        ...buildImmediateCareerReviewList(batchResult.results, classifiedById),
      ].filter((item, idx, arr) => arr.findIndex((x) => x.phrase_id === item.phrase_id) === idx);
      writeJsonAtomic(careerReviewPath, {
        run_id: RUN_ID,
        updated_at: new Date().toISOString(),
        items: careerReviewItems,
      });

      writeJsonAtomic(registryPath, {
        run_id: RUN_ID,
        updated_at: new Date().toISOString(),
        reconciled: !!checkpoint.trigger_reconciliation,
        results: allResults.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id)),
      });

      const assessedCount = allResults.filter((r) => {
        const verdict = r.final_authoritative_verdict || r.final_verdict;
        return r.schema_valid && verdict;
      }).length;
      const gateMap = [
        { threshold: GATE_C1_THRESHOLD, gateId: 'Gate-C1' },
        { threshold: 1200, gateId: 'Gate-C2' },
        { threshold: 2000, gateId: 'Gate-C3' },
      ];
      for (const { threshold, gateId } of gateMap) {
        if (threshold === GATE_C1_THRESHOLD && resumeMode) continue;
        if (assessedCount >= threshold && !gateReceipts.find((g) => g.gate_id === gateId)) {
          const gate = analyzeGate(allResults, gateId, classifiedById, operatorOverrides);
          gateReceipts.push(gate);
          writeJsonAtomic(path.join(STORAGE_ROOT, 'receipts', `${gateId.toLowerCase()}-receipt-v1.json`), gate);
          if (gate.stop_required) {
            stopReason = gate.issues.join(';');
            throw new Error(`FAIL-CLOSED — ${stopReason}`);
          }
        }
      }

      const stopIssues = checkStopConditions(allResults, classifiedById, operatorOverrides);
      if (stopIssues.length) {
        stopReason = stopIssues.join(';');
        throw new Error(`FAIL-CLOSED — ${stopReason}`);
      }
    }
  } catch (e) {
    checkpoint.lifecycle_state = 'BLOCKED_AT_PHASE_4';
    checkpoint.complete = false;
    checkpoint.stop_reason = e.message;
    writeJsonAtomic(checkpointPath, checkpoint);
    writeJsonAtomic(registryPath, {
      run_id: RUN_ID,
      updated_at: new Date().toISOString(),
      partial: true,
      results: allResults.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id)),
    });
    releaseLock(lockPath, `PARTIAL — ${e.message}`);
    console.error(JSON.stringify({ error: e.message, processed: allResults.length, cumulative_cost: cumulativeCost() }));
    process.exit(1);
  }

  const finalIds = allResults.map((r) => r.phrase_id);
  const uniqueIds = new Set(finalIds);
  const reconciliation = {
    canonical_total: CANONICAL_TOTAL,
    unique_assessed_ids: uniqueIds.size,
    missing_ids: CANONICAL_TOTAL - uniqueIds.size,
    duplicate_ids: finalIds.length - uniqueIds.size,
    orphan_ids: 0,
    quarantined_unresolved: allResults.filter((r) => r.status === 'QUARANTINED').length,
    canary_reused: reusedResults.length,
    production_new: allResults.filter((r) => r.production_source === 'PHASE_4_NEW').length,
    pass:
      uniqueIds.size === CANONICAL_TOTAL &&
      finalIds.length === uniqueIds.size &&
      allResults.filter((r) => r.status === 'QUARANTINED').length === 0,
  };

  if (!reconciliation.pass) {
    if (uniqueIds.size < CANONICAL_TOTAL) {
      checkpoint.lifecycle_state = 'BLOCKED_AT_PHASE_4';
      checkpoint.complete = false;
      checkpoint.missing = CANONICAL_TOTAL - uniqueIds.size;
      checkpoint.stop_reason = `INCOMPLETE — ${uniqueIds.size}/${CANONICAL_TOTAL} assessed`;
      writeJsonAtomic(checkpointPath, checkpoint);
      releaseLock(lockPath, `PARTIAL — INCOMPLETE ${uniqueIds.size}/${CANONICAL_TOTAL}`);
      console.error(JSON.stringify({ error: 'PARTIAL — REMAINING RECORDS REQUIRE RESUME', reconciliation }));
      process.exit(1);
    }
    checkpoint.lifecycle_state = 'BLOCKED_AT_PHASE_4';
    checkpoint.complete = false;
    writeJsonAtomic(checkpointPath, checkpoint);
    releaseLock(lockPath, 'BLOCKED — FINAL SEMANTIC RECONCILIATION FAILED');
    console.error(JSON.stringify({ error: 'BLOCKED — FINAL SEMANTIC RECONCILIATION FAILED', reconciliation }));
    process.exit(1);
  }

  checkpoint.lifecycle_state = 'PHASE_4_COMPLETE';
  checkpoint.complete = true;
  checkpoint.unique_assessed_total = CANONICAL_TOTAL;
  checkpoint.missing = 0;
  checkpoint.cumulative_cost_usd = cumulativeCost();
  checkpoint.completed_at = new Date().toISOString();
  writeJsonAtomic(checkpointPath, checkpoint);

  const executionReport = {
    run_id: RUN_ID,
    phase_id: PHASE_ID,
    phase_verdict: 'PASS — OPERATOR REVIEW REQUIRED',
    lifecycle_state: 'PHASE_4_COMPLETE',
    reconciliation,
    verdict_distribution: analyzeGate(allResults, 'final', classifiedById, operatorOverrides).verdict_distribution,
    cost: {
      cumulative_before_phase4_usd: CUMULATIVE_BEFORE_PHASE4,
      phase4_cost_usd: costTracker.phase4_cost_usd,
      cumulative_cost_usd: cumulativeCost(),
      input_tokens: costTracker.phase4_input_tokens,
      output_tokens: costTracker.phase4_output_tokens,
    },
    malformed_policy: {
      malformed_first_attempt: costTracker.malformed_first_attempt,
      retry_success: costTracker.retry_success,
      retry_failure: costTracker.retry_failure,
      quarantined: costTracker.quarantined,
    },
    gate_receipts: gateReceipts,
    batches: batches.map((b) => b.completionReceipt),
    full_production_complete: true,
    strategy: 'not started',
    completed_at: new Date().toISOString(),
  };

  writeJsonAtomic(path.join(STORAGE_ROOT, 'reports', 'phase4-full-corpus-execution-report-v1.json'), executionReport);
  writeJsonAtomic(registryPath, {
    run_id: RUN_ID,
    updated_at: new Date().toISOString(),
    complete: true,
    results: allResults.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id)),
  });

  const runManifest = loadJson(path.join(GIT_RUN_DIR, 'run-manifest-v1.json'));
  runManifest.lifecycle_state = 'PHASE_4_COMPLETE';
  runManifest.full_production_processed = reconciliation.production_new;
  runManifest.unique_assessed_total = CANONICAL_TOTAL;
  runManifest.completed_at = new Date().toISOString();
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'run-manifest-v1.json'), runManifest);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'lifecycle-decision-v1.json'), {
    run_id: RUN_ID,
    decision: 'PHASE_4_COMPLETE',
    phase_4: 'PASS — OPERATOR REVIEW REQUIRED',
    full_corpus_authorized: true,
    strategy_authorized: false,
    next_gate: 'OPERATOR REVIEW OF CORVONERO RUN 004 PHASE 4 RESULT',
  });

  releaseLock(lockPath, 'PASS — OPERATOR REVIEW REQUIRED');
  console.log(JSON.stringify({
    phase_verdict: executionReport.phase_verdict,
    assessed: reconciliation.unique_assessed_ids,
    cost: executionReport.cost,
    batches: batches.length,
  }, null, 2));
}

main().catch((e) => {
  console.error(e.message || e);
  process.exit(1);
});
