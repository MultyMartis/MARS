#!/usr/bin/env node
/**
 * Corvonero Run 004 — Phase 3 controlled canary Attempt 2 (120 phrases).
 * Run ID: corv-semantic-v2-20260626-004
 * Attempt ID: corv-run004-phase3-canary-attempt-002
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
import {
  CANARY_SEED_V2,
  CANARY_SIZE,
  FAMILY_MINIMUMS,
  EXPECTATION_STATUS,
  classifyCorpusV2,
  validateExpectationPreflight,
} from './canary-family-classifier-v2.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const RUN_ID = 'corv-semantic-v2-20260626-004';
const ATTEMPT_ID = 'corv-run004-phase3-canary-attempt-002';
const STORAGE_ROOT = path.join('C:\\MARS Phenix\\AI MARS STORAGE', 'mig', 'corvonero', 'semantic-runs', RUN_ID);
const GIT_RUN_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero/runs', RUN_ID);
const PILOT_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const FIX = path.join(REPO_ROOT, 'projects/orca/semantic-intelligence/live-model/fixtures');
const CORPUS_REL = 'projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json';
const SPPC05_COST_USD = 0.6852748999999999;
const ATTEMPT1_CANARY_COST_USD = 0.0850596;
const CUMULATIVE_BEFORE_ATTEMPT2 = SPPC05_COST_USD + ATTEMPT1_CANARY_COST_USD;
const BATCH_SIZE = 20;
const PRICING = { input_per_m: 0.15, output_per_m: 0.60 };

const OPERATOR = {
  gate_b: 'APPROVED',
  phase_3_canary_attempt_2: 'AUTHORIZED',
  canary_size: 120,
  full_corpus: 'NOT AUTHORIZED',
  provider: 'openrouter',
  model: 'openai/gpt-5-mini',
  hard_cost_cap_usd: 3.0,
  soft_cost_warning_usd: 2.0,
  psr_amb_01: 'KNOWN NON-BLOCKING AMBIGUITY — MUST BE INCLUDED AND MONITORED',
};

const ORCA_HASHES = {
  semantic_adjudicator: '9618364947ba812c85f3fedbda99c1669db4d47fc58ec9d3996fc436b58bf341',
  platform_compatibility: '49b8c4d604ee732f4cfaeb0e07b99166133f4932533562aae7454171c99fc7ea',
  hard_rules: 'e6cd74ccca6ed453138f003d56f872e8a727e41bba04703589bd42c6f218c678',
  prompt_contract: '481075e55a8274047124b24d42293d616e37f57a129563e9f15f034034496e53',
  service_intent_evidence: '5bfff7ae2ed3b854ea613011797a91e35ab15804c10c8859c8ec667bd32f7d9f',
};

const EDGE_CASE_REQUIREMENTS = [
  'product_plus_service_bundle',
  'generic_erp_ambiguity',
  'ambiguous_diy_troubleshooting',
  'foreign_incompatible_platform',
  'direct_1c_version_update_service',
  'self_service_update_instructions',
  'problem_without_commercial_marker',
  'psr_amb_01_family',
];

const SCORED_STATUSES = new Set([
  EXPECTATION_STATUS.AUTHORITATIVE_EXPECTATION,
  EXPECTATION_STATUS.POLICY_DERIVED_EXPECTATION,
]);

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

function rankBySeed(items, family, seed = CANARY_SEED_V2) {
  return [...items].sort((a, b) => {
    const ha = crypto.createHash('sha256').update(`${seed}:${family}:${a.phrase_id}`).digest('hex');
    const hb = crypto.createHash('sha256').update(`${seed}:${family}:${b.phrase_id}`).digest('hex');
    return ha.localeCompare(hb);
  });
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
  return { pass: drift.length === 0, drift };
}

function verifyAttemptBoundaries() {
  const attempt1Markers = [
    path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-CANARY-RESULT-v1.json'),
    path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-CANARY-SELECTION-v1.json'),
  ];
  const attempt2Markers = [
    path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-CANARY-RESULT-v2.json'),
    path.join(STORAGE_ROOT, 'checkpoints', 'checkpoint-phase3-canary-attempt2-complete-v1.json'),
  ];
  const missingAttempt1 = attempt1Markers.filter((p) => !fs.existsSync(p));
  const existingAttempt2 = attempt2Markers.filter((p) => fs.existsSync(p));
  return {
    attempt1_complete: missingAttempt1.length === 0,
    missing_attempt1: missingAttempt1,
    attempt2_blocked: existingAttempt2.length > 0,
    existing_attempt2: existingAttempt2,
  };
}

function loadCorpus() {
  const corpusPath = path.join(REPO_ROOT, CORPUS_REL);
  const raw = fs.readFileSync(corpusPath);
  const hash = crypto.createHash('sha256').update(raw).digest('hex');
  const data = JSON.parse(raw.toString());
  const records = data.phrases || data.records || data;
  if (records.length !== 2368) throw new Error(`CORPUS_COUNT_MISMATCH:${records.length}`);
  if (!hash.startsWith('eaa09b8450f82738')) throw new Error(`CORPUS_HASH_MISMATCH:${hash.slice(0, 16)}`);
  return { corpusPath, hash, records };
}

function selectCanaryManifestV2(classified) {
  const selected = new Map();
  const selectionLog = [];

  const add = (item, reason) => {
    if (selected.has(item.phrase_id)) return false;
    selected.set(item.phrase_id, { ...item, selection_reason: reason });
    return true;
  };

  for (const edge of EDGE_CASE_REQUIREMENTS) {
    const pool = rankBySeed(
      classified.filter((c) => c.edge_cases.includes(edge) && !selected.has(c.phrase_id)),
      `edge:${edge}`,
    );
    if (pool.length) {
      add(pool[0], `edge_case_required:${edge}`);
      selectionLog.push({ type: 'edge_case', edge, phrase_id: pool[0].phrase_id });
    }
  }

  for (const [family, minCount] of Object.entries(FAMILY_MINIMUMS)) {
    const current = [...selected.values()].filter((s) => s.primary_family === family).length;
    const need = Math.max(0, minCount - current);
    if (!need) continue;
    const pool = rankBySeed(
      classified.filter((c) => c.primary_family === family && !selected.has(c.phrase_id)),
      family,
    );
    for (let i = 0; i < need && i < pool.length; i++) {
      add(pool[i], `family_minimum:${family}`);
      selectionLog.push({ type: 'family_minimum', family, phrase_id: pool[i].phrase_id });
    }
  }

  if (selected.size < CANARY_SIZE) {
    const remaining = rankBySeed(classified.filter((c) => !selected.has(c.phrase_id)), 'fill_remainder');
    for (const item of remaining) {
      if (selected.size >= CANARY_SIZE) break;
      add(item, 'deterministic_fill_remainder');
    }
  }

  if (selected.size !== CANARY_SIZE) throw new Error(`SELECTION_COUNT_MISMATCH:${selected.size}`);

  const items = [...selected.values()].sort((a, b) => a.phrase_id.localeCompare(b.phrase_id));
  const familyCounts = {};
  for (const item of items) {
    familyCounts[item.primary_family] = (familyCounts[item.primary_family] || 0) + 1;
  }

  let attempt1Overlap = [];
  const attempt1Path = path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-CANARY-SELECTION-v1.json');
  if (fs.existsSync(attempt1Path)) {
    const attempt1 = loadJson(attempt1Path);
    const attempt1Ids = new Set((attempt1.items || []).map((i) => i.phrase_id));
    attempt1Overlap = items.filter((i) => attempt1Ids.has(i.phrase_id)).map((i) => i.phrase_id);
  }

  return {
    manifest_id: 'corvonero-run-004-phase-3-canary-selection-v2',
    run_id: RUN_ID,
    attempt_id: ATTEMPT_ID,
    seed: CANARY_SEED_V2,
    algorithm: 'edge_case_first → family_minimums (no tag override) → deterministic SHA-256 rank fill',
    selected_count: items.length,
    family_minimums: FAMILY_MINIMUMS,
    family_counts: familyCounts,
    attempt_1_overlap_count: attempt1Overlap.length,
    attempt_1_overlap_ids: attempt1Overlap,
    new_ids_count: items.length - attempt1Overlap.length,
    selection_log: selectionLog,
    items,
    created_at: new Date().toISOString(),
  };
}

function buildExpectationAudit(manifest) {
  const records = manifest.items.map((item) => ({
    phrase_id: item.phrase_id,
    phrase: item.phrase,
    observed_tags: item.observed_tags,
    coverage_family: item.primary_family,
    expectation_status: item.expectation_status,
    expected_verdict: item.expected_verdict,
    authority_source: item.authority_source,
    review_required: item.review_required,
    scored: item.scored,
    conflict_flags: [],
  }));
  const preflight = validateExpectationPreflight(manifest.items);
  return {
    audit_id: 'corvonero-run-004-phase-3-canary-expectation-audit-v2',
    run_id: RUN_ID,
    attempt_id: ATTEMPT_ID,
    records,
    preflight,
    created_at: new Date().toISOString(),
  };
}

function acquireAttempt2Lock(corpusHash) {
  const lockPath = path.join(STORAGE_ROOT, 'locks', 'run-attempt2.lock.json');
  if (fs.existsSync(lockPath)) {
    const existing = loadJson(lockPath);
    if (existing.status === 'ACTIVE') throw new Error('BLOCKED — ATTEMPT 2 LOCK OWNERSHIP CONFLICT');
  }
  const lock = {
    schema_version: '1.0.0',
    run_id: RUN_ID,
    attempt_id: ATTEMPT_ID,
    project_id: 'PRJ-0013',
    phase: 'PHASE_3_CANARY_ATTEMPT_2',
    owner_pid: process.pid,
    process_identity: `execute-run-004-phase3-canary-v2.mjs@${process.pid}`,
    corpus_checksum: corpusHash,
    acquired_at: new Date().toISOString(),
    heartbeat: new Date().toISOString(),
    stale_after_ms: 7200000,
    status: 'ACTIVE',
  };
  writeJsonAtomic(lockPath, lock);
  return lockPath;
}

function releaseLock(lockPath, outcome) {
  const lock = loadJson(lockPath);
  lock.status = 'RELEASED';
  lock.released_at = new Date().toISOString();
  lock.release_outcome = outcome;
  writeJsonAtomic(lockPath, lock);
}

const costTracker = { input_tokens: 0, output_tokens: 0, calculated_cost_usd: 0, retries: 0, model_errors: 0 };

function trackUsage(meta) {
  if (!meta?.usage) return;
  costTracker.input_tokens += meta.usage.prompt_tokens || 0;
  costTracker.output_tokens += meta.usage.completion_tokens || 0;
  costTracker.calculated_cost_usd =
    (costTracker.input_tokens / 1e6) * PRICING.input_per_m +
    (costTracker.output_tokens / 1e6) * PRICING.output_per_m;
}

function assertCostCap() {
  const cumulative = CUMULATIVE_BEFORE_ATTEMPT2 + costTracker.calculated_cost_usd;
  if (cumulative > OPERATOR.hard_cost_cap_usd) {
    throw new Error(`BLOCKED — RUN COST CAP RISK:${cumulative.toFixed(4)}`);
  }
  return cumulative;
}

async function evaluatePhraseRecord(item, context, adapter) {
  const phrase = {
    phrase_id: item.phrase_id,
    raw_query: item.phrase,
    normalized_query: item.normalized_phrase || item.phrase.toLowerCase(),
    region: 'RU',
  };
  const structured = extractServiceIntentEvidence(phrase);
  const platform = evaluatePlatformCompatibility(phrase, context.businessScope, context.serviceRegistry);

  const primary = await runBlindPrimaryAssessment({ phrase, ...context, adapter, forbiddenContext: {} });
  if (!primary.ok) {
    costTracker.model_errors++;
    return { phrase_id: item.phrase_id, error: primary.blocker, schema_valid: false };
  }
  trackUsage(primary.output?.model_metadata);
  assertCostCap();

  const det = assessDeterministic(createAssessorContext(phrase, context));
  const hardRules = applyHardRules(phrase, det, context);

  const secondary = await runIndependentReassessment({
    phrase,
    ...context,
    primaryAdapter: adapter,
    secondaryAdapter: adapter,
    hardRuleEvidence: hardRules,
    primaryDecision: undefined,
    primaryRationale: undefined,
    expectedLabel: undefined,
  });
  if (secondary.ok) trackUsage(secondary.output?.model_metadata);
  else costTracker.model_errors++;
  assertCostCap();

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
  const reviewFlag = item.review_required || confirmationDisagree || !item.scored;

  let expectationMatch = null;
  let errorClass = null;
  if (item.scored && SCORED_STATUSES.has(item.expectation_status) && item.expected_verdict) {
    expectationMatch = finalVerdict === item.expected_verdict;
    if (!expectationMatch) {
      if (item.expected_verdict === 'REJECT' && finalVerdict === 'ACCEPT') errorClass = 'confirmed_false_accept';
      else if (item.expected_verdict === 'ACCEPT' && finalVerdict === 'REJECT') errorClass = 'confirmed_false_reject';
      else if (item.expected_verdict === 'ABSTAIN' && finalVerdict !== 'ABSTAIN') errorClass = 'review_disagreement';
    }
  } else if (!item.scored) {
    errorClass = 'unscored_ambiguity';
  }

  return {
    phrase_id: item.phrase_id,
    phrase: item.phrase,
    observed_tags: item.observed_tags,
    primary_family: item.primary_family,
    tags: item.tags,
    edge_cases: item.edge_cases,
    expectation_status: item.expectation_status,
    expectation_class: item.expectation_class,
    expected_verdict: item.expected_verdict,
    authority_source: item.authority_source,
    scored: item.scored,
    review_required: item.review_required,
    selection_reason: item.selection_reason,
    primary_verdict: primary.output?.decision,
    reassessment_verdict: secondary.output?.decision,
    confirmation_disagreement: confirmationDisagree,
    confirmation_result: confirmationDisagree ? 'DISAGREE' : (secondary.ok ? 'AGREE' : 'SINGLE'),
    evidence_classes: structured.signals || [],
    platform_class: platform.classification,
    applied_hard_rules: (hardRules.evidence || []).map((e) => e.rule),
    adjudication_path: adj.agreement_state,
    invariant_applications: adj.invariant_applications || [],
    final_verdict: finalVerdict,
    confidence: adj.confidence,
    reason: primary.output?.rationale || adj.findings?.join('; '),
    review_flag: reviewFlag,
    expectation_match: expectationMatch,
    error_class: errorClass,
    schema_valid: true,
    structured_evidence: structured,
    platform_compatibility: platform,
    hard_rule: hardRules,
  };
}

async function runBatch(batchIndex, batchItems, context, adapter, manifestIds) {
  const batchId = `canary-attempt2-batch-${String(batchIndex + 1).padStart(2, '0')}`;
  const batchDir = path.join(STORAGE_ROOT, 'batches', batchId);
  const inputIds = batchItems.map((i) => i.phrase_id);
  for (const id of inputIds) {
    if (!manifestIds.has(id)) throw new Error(`OUT_OF_MANIFEST:${id}`);
  }

  const startReceipt = {
    batch_id: batchId,
    attempt_id: ATTEMPT_ID,
    batch_index: batchIndex,
    phrase_count: batchItems.length,
    input_ids: inputIds,
    started_at: new Date().toISOString(),
    provider: OPERATOR.provider,
    model: OPERATOR.model,
  };
  writeJsonAtomic(path.join(batchDir, 'batch-start-receipt-v1.json'), startReceipt);

  const rawResponseDir = path.join(STORAGE_ROOT, 'raw-responses', 'attempt2');
  fs.mkdirSync(rawResponseDir, { recursive: true });

  const rawResponseDir = path.join(STORAGE_ROOT, 'raw-responses', 'attempt2');
  fs.mkdirSync(rawResponseDir, { recursive: true });

  const results = [];
  const failures = [];
  for (const item of batchItems) {
    try {
      const r = await evaluatePhraseRecord(item, context, adapter);
      results.push(r);
      if (r.error) failures.push(r);
      fs.writeFileSync(path.join(rawResponseDir, `${item.phrase_id}.json`), JSON.stringify(r, null, 2));
    } catch (e) {
      costTracker.retries++;
      failures.push({ phrase_id: item.phrase_id, error: e.message });
      if (e.message.includes('COST')) throw e;
    }
  }

  const verdictCounts = { ACCEPT: 0, REJECT: 0, ABSTAIN: 0, ERROR: 0 };
  for (const r of results) {
    if (r.error) verdictCounts.ERROR++;
    else verdictCounts[r.final_verdict] = (verdictCounts[r.final_verdict] || 0) + 1;
  }

  const completionReceipt = {
    ...startReceipt,
    completed_at: new Date().toISOString(),
    cost_usd: costTracker.calculated_cost_usd,
    verdict_distribution: verdictCounts,
    failed_records: failures,
    schema_valid_count: results.filter((r) => r.schema_valid).length,
    retries: costTracker.retries,
  };
  writeJsonAtomic(path.join(batchDir, 'batch-completion-receipt-v1.json'), completionReceipt);
  writeJsonAtomic(path.join(batchDir, 'batch-results-v1.json'), results);
  return { batchId, results, completionReceipt, failures };
}

function analyzeStopConditionsV2(allResults) {
  const issues = [];
  const verdicts = { ACCEPT: 0, REJECT: 0, ABSTAIN: 0 };
  for (const r of allResults) {
    if (r.final_verdict) verdicts[r.final_verdict]++;
  }

  const scored = allResults.filter((r) => r.scored && SCORED_STATUSES.has(r.expectation_status) && r.expected_verdict);
  const falseAccepts = scored.filter((r) => r.error_class === 'confirmed_false_accept');
  const falseRejects = scored.filter((r) => r.error_class === 'confirmed_false_reject');

  if (falseAccepts.length >= 3) issues.push('broad_false_accept_family');
  if (falseRejects.length >= 5) issues.push('broad_false_reject_family');

  const careerAccepted = allResults.filter(
    (r) => r.observed_tags?.includes('career') && r.final_verdict === 'ACCEPT',
  );
  if (careerAccepted.length >= 2) issues.push('career_education_queries_accepted');

  const educationAccepted = allResults.filter(
    (r) => r.observed_tags?.includes('education') && r.final_verdict === 'ACCEPT',
  );
  if (educationAccepted.length >= 2) issues.push('career_education_queries_accepted');

  const infoAccepted = allResults.filter(
    (r) => r.primary_family === 'informational_self_service' && r.final_verdict === 'ACCEPT',
  );
  if (infoAccepted.length >= 4) issues.push('informational_systematically_accepted');

  const directCommercial = scored.filter(
    (r) => r.primary_family === 'direct_commercial_1c_service' && r.expected_verdict === 'ACCEPT',
  );
  const directRejected = directCommercial.filter((r) => r.final_verdict === 'REJECT');
  if (directCommercial.length >= 5 && directRejected.length / directCommercial.length > 0.5) {
    issues.push('direct_commercial_systematically_rejected');
  }

  const foreignAccepted = allResults.filter(
    (r) => r.edge_cases?.includes('foreign_incompatible_platform') && r.final_verdict === 'ACCEPT',
  );
  if (foreignAccepted.length) issues.push('foreign_platform_accepted');

  const psrFamily = allResults.filter((r) => r.edge_cases?.includes('psr_amb_01_family'));
  const psrAccepted = psrFamily.filter((r) => r.final_verdict === 'ACCEPT').length;
  if (psrFamily.length >= 3 && psrAccepted / psrFamily.length > 0.6) {
    issues.push('product_plus_service_false_accept_family');
  }

  return {
    issues,
    false_accepts: falseAccepts,
    false_rejects: falseRejects,
    verdicts,
    scored_count: scored.length,
    review_required_count: allResults.filter((r) => !r.scored || r.review_required).length,
    psr_family: { total: psrFamily.length, accepted: psrAccepted },
  };
}

async function main() {
  const boundaries = verifyAttemptBoundaries();
  if (!boundaries.attempt1_complete) {
    console.error(JSON.stringify({ error: 'BLOCKED — ATTEMPT 1 EVIDENCE INCOMPLETE', missing: boundaries.missing_attempt1 }));
    process.exit(2);
  }
  if (boundaries.attempt2_blocked) {
    console.error(JSON.stringify({ error: 'BLOCKED — PHASE 3 CANARY ATTEMPT 2 ALREADY EXISTS', existing: boundaries.existing_attempt2 }));
    process.exit(2);
  }

  const orca = verifyOrcaAuthority();
  if (!orca.pass) {
    console.error(JSON.stringify({ error: 'BLOCKED — APPROVED ORCA AUTHORITY DRIFT', drift: orca.drift }));
    process.exit(2);
  }

  const { hash: corpusHash, records } = loadCorpus();
  loadLocalSecrets();
  const configSummary = getSafeConfigSummary();
  if (configSummary.ORCA_SEMANTIC_PROVIDER !== OPERATOR.provider || configSummary.ORCA_SEMANTIC_MODEL !== OPERATOR.model) {
    console.error(JSON.stringify({ error: 'BLOCKED — PROVIDER/MODEL DRIFT', configSummary }));
    process.exit(2);
  }
  process.env.ORCA_EVAL_MAX_COST = String(OPERATOR.hard_cost_cap_usd);

  const context = {
    businessScope: loadJson(path.join(FIX, 'business-scope-eval-v1.json')),
    serviceRegistry: loadJson(path.join(FIX, 'service-registry-eval-v1.json')),
    taxonomy: {},
    commercialPolicy: { version: 'v1' },
  };

  const classified = classifyCorpusV2(records, context);
  const manifest = selectCanaryManifestV2(classified);
  const audit = buildExpectationAudit(manifest);

  writeJsonAtomic(path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-CANARY-SELECTION-v2.json'), manifest);
  writeJsonAtomic(path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-CANARY-EXPECTATION-AUDIT-v2.json'), audit);
  writeJsonAtomic(path.join(STORAGE_ROOT, 'manifests', 'canary-selection-v2.json'), manifest);
  writeJsonAtomic(path.join(STORAGE_ROOT, 'manifests', 'canary-expectation-audit-v2.json'), audit);

  if (!audit.preflight.pass) {
    console.error(JSON.stringify({ error: 'BLOCKED — CANARY V2 EXPECTATION AUDIT FAILED', preflight: audit.preflight }));
    process.exit(2);
  }

  const projectedAttempt2Cost = CANARY_SIZE * 1600 / 1e6 * 0.15 * 2;
  const maxExposure = CUMULATIVE_BEFORE_ATTEMPT2 + projectedAttempt2Cost;
  if (maxExposure > OPERATOR.hard_cost_cap_usd) {
    console.error(JSON.stringify({ error: 'BLOCKED — RUN COST CAP RISK', maxExposure, cumulative_before: CUMULATIVE_BEFORE_ATTEMPT2 }));
    process.exit(2);
  }

  const authReceipt = {
    receipt_id: 'phase-3-canary-attempt-2-authorization-v1',
    run_id: RUN_ID,
    attempt_id: ATTEMPT_ID,
    lifecycle_state: 'PHASE_3_CANARY_ATTEMPT_2_AUTHORIZED',
    operator_decisions: OPERATOR,
    expectation_audit_pass: true,
    cost_projection: {
      cumulative_before_attempt2_usd: CUMULATIVE_BEFORE_ATTEMPT2,
      projected_attempt2_usd: projectedAttempt2Cost,
      max_exposure_usd: maxExposure,
      hard_cap_usd: OPERATOR.hard_cost_cap_usd,
    },
    authorized_at: new Date().toISOString(),
  };
  writeJsonAtomic(path.join(STORAGE_ROOT, 'receipts', 'phase-3-canary-attempt-2-authorization-v1.json'), authReceipt);

  const lockPath = acquireAttempt2Lock(corpusHash);
  const checkpoint = {
    run_id: RUN_ID,
    attempt_id: ATTEMPT_ID,
    phase: 'PHASE_3_CANARY_ATTEMPT_2',
    lifecycle_state: 'PHASE_3_CANARY_ATTEMPT_2_AUTHORIZED',
    attempt_1_canary_processed: 120,
    attempt_2_canary_selected: CANARY_SIZE,
    attempt_2_canary_processed: 0,
    full_production_processed: 0,
    cumulative_cost_usd: CUMULATIVE_BEFORE_ATTEMPT2,
    started_at: new Date().toISOString(),
  };
  writeJsonAtomic(path.join(STORAGE_ROOT, 'checkpoints', 'checkpoint-phase3-canary-attempt2-v1.json'), checkpoint);

  const adapter = createOpenAICompatibleAdapter();
  if (!adapter) {
    releaseLock(lockPath, 'FAILED — ADAPTER UNAVAILABLE');
    process.exit(2);
  }

  const manifestIds = new Set(manifest.items.map((i) => i.phrase_id));
  const allResults = [];
  const batches = [];

  try {
    for (let b = 0; b < Math.ceil(manifest.items.length / BATCH_SIZE); b++) {
      const slice = manifest.items.slice(b * BATCH_SIZE, (b + 1) * BATCH_SIZE);
      const batchResult = await runBatch(b, slice, context, adapter, manifestIds);
      batches.push(batchResult);
      allResults.push(...batchResult.results.filter((r) => !r.error));

      checkpoint.attempt_2_canary_processed = allResults.length;
      checkpoint.processed_ids = allResults.map((r) => r.phrase_id);
      checkpoint.cumulative_cost_usd = CUMULATIVE_BEFORE_ATTEMPT2 + costTracker.calculated_cost_usd;
      checkpoint.last_heartbeat = new Date().toISOString();
      writeJsonAtomic(path.join(STORAGE_ROOT, 'checkpoints', 'checkpoint-phase3-canary-attempt2-v1.json'), checkpoint);
      assertCostCap();
    }
  } catch (e) {
    releaseLock(lockPath, `FAILED — ${e.message}`);
    throw e;
  }

  const analysis = analyzeStopConditionsV2(allResults);
  const schemaValidPct = (allResults.filter((r) => r.schema_valid).length / allResults.length) * 100;
  const criticalFail = analysis.issues.length > 0 || allResults.length !== CANARY_SIZE;

  const canaryVerdict = criticalFail
    ? { canary: 'FAILED', run: 'BLOCKED_AT_PHASE_3_CANARY_ATTEMPT_2' }
    : { canary: 'PASS — OPERATOR REVIEW REQUIRED', run: 'PHASE_3_COMPLETE' };

  checkpoint.attempt_2_canary_processed = allResults.length;
  checkpoint.complete = !criticalFail;
  checkpoint.lifecycle_state = criticalFail ? 'BLOCKED_AT_PHASE_3_CANARY_ATTEMPT_2' : 'PHASE_3_COMPLETE';
  checkpoint.cumulative_cost_usd = CUMULATIVE_BEFORE_ATTEMPT2 + costTracker.calculated_cost_usd;
  checkpoint.completed_at = new Date().toISOString();
  writeJsonAtomic(
    path.join(STORAGE_ROOT, 'checkpoints', criticalFail ? 'checkpoint-phase3-canary-attempt2-failed-v1.json' : 'checkpoint-phase3-canary-attempt2-complete-v1.json'),
    checkpoint,
  );

  const scored = allResults.filter((r) => r.scored && SCORED_STATUSES.has(r.expectation_status) && r.expected_verdict);
  const resultPayload = {
    run_id: RUN_ID,
    attempt_id: ATTEMPT_ID,
    manifest_id: manifest.manifest_id,
    canary_verdict: canaryVerdict,
    processed_count: allResults.length,
    verdict_distribution: analysis.verdicts,
    metrics: {
      schema_valid_percentage: schemaValidPct,
      retry_count: costTracker.retries,
      model_error_count: costTracker.model_errors,
      scored_authoritative_count: scored.length,
      review_required_count: analysis.review_required_count,
      confirmed_false_accepts: analysis.false_accepts.length,
      confirmed_false_rejects: analysis.false_rejects.length,
      operator_review_rate: allResults.filter((r) => r.review_flag).length / allResults.length,
    },
    cost: {
      attempt2_cost_usd: costTracker.calculated_cost_usd,
      cumulative_before_attempt2_usd: CUMULATIVE_BEFORE_ATTEMPT2,
      cumulative_cost_usd: CUMULATIVE_BEFORE_ATTEMPT2 + costTracker.calculated_cost_usd,
      input_tokens: costTracker.input_tokens,
      output_tokens: costTracker.output_tokens,
    },
    attempt_1_overlap: {
      count: manifest.attempt_1_overlap_count,
      new_ids: manifest.new_ids_count,
    },
    psr_amb_01_family: analysis.psr_family,
    stop_analysis: analysis,
    batches: batches.map((b) => b.completionReceipt),
    results: allResults,
    completed_at: new Date().toISOString(),
  };

  writeJsonAtomic(path.join(STORAGE_ROOT, 'reports', 'canary-attempt2-execution-report-v1.json'), resultPayload);
  writeJsonAtomic(path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-CANARY-RESULT-v2.json'), resultPayload);

  const runManifest = loadJson(path.join(GIT_RUN_DIR, 'run-manifest-v1.json'));
  runManifest.lifecycle_state = checkpoint.lifecycle_state;
  runManifest.gate_c = canaryVerdict.canary;
  runManifest.canary_attempt_2_processed = allResults.length;
  runManifest.completed_at = new Date().toISOString();
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'run-manifest-v1.json'), runManifest);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'lifecycle-decision-v1.json'), {
    run_id: RUN_ID,
    attempt_id: ATTEMPT_ID,
    decision: checkpoint.lifecycle_state,
    canary: canaryVerdict.canary,
    next_gate: 'OPERATOR REVIEW OF CORVONERO RUN 004 PHASE 3 CANARY ATTEMPT 2',
    canary_attempt_2_authorized: true,
    full_corpus_authorized: false,
  });

  releaseLock(lockPath, canaryVerdict.canary);
  console.log(JSON.stringify({ canary_verdict: canaryVerdict, processed: allResults.length, cost: resultPayload.cost, verdicts: analysis.verdicts }, null, 2));
  process.exit(criticalFail ? 1 : 0);
}

main().catch((e) => {
  console.error(e.message || e);
  process.exit(1);
});
