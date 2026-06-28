#!/usr/bin/env node
/**
 * Corvonero Run 004 — Phase 3 controlled canary (120 phrases).
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
import { adjudicateSemanticIntent, ADJUDICATOR_VERSION } from '../../../../orca/semantic-intelligence/live-model/adjudication/semantic-adjudicator.mjs';
import { applyHardRules, HARD_RULES_VERSION } from '../../../../orca/semantic-intelligence/production/assessors/hard-rules.mjs';
import { assessDeterministic } from '../../../../orca/semantic-intelligence/production/assessors/deterministic-assessor.mjs';
import { createAssessorContext } from '../../../../orca/semantic-intelligence/production/assessors/assessor-contract.mjs';
import { PROMPT_VERSION } from '../../../../orca/semantic-intelligence/live-model/contracts/prompt-contract.mjs';
import { extractServiceIntentEvidence, SERVICE_INTENT_EVIDENCE_VERSION } from '../../../../orca/semantic-intelligence/live-model/evidence/service-intent-evidence.mjs';
import { evaluatePlatformCompatibility, PLATFORM_COMPATIBILITY_VERSION } from '../../../../orca/semantic-intelligence/live-model/evidence/platform-compatibility.mjs';
import {
  CANARY_SEED,
  CANARY_SIZE,
  FAMILY_MINIMUMS,
  classifyCorpus,
  classifyPhrase,
} from './canary-family-classifier.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const RUN_ID = 'corv-semantic-v2-20260626-004';
const STORAGE_ROOT = path.join('C:\\MARS Phenix\\AI MARS STORAGE', 'mig', 'corvonero', 'semantic-runs', RUN_ID);
const GIT_RUN_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero/runs', RUN_ID);
const PILOT_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const FIX = path.join(REPO_ROOT, 'projects/orca/semantic-intelligence/live-model/fixtures');
const CORPUS_REL = 'projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json';
const RECOVERY_AUTHORITY = 'ebc65acd4087fa9d180bb2a50921027fde51e3b7';
const SPPC05_COST_USD = 0.6852748999999999;
const BATCH_SIZE = 20;
const PRICING = { input_per_m: 0.15, output_per_m: 0.60 };

const OPERATOR = {
  gate_b: 'APPROVED',
  phase_3_canary: 'AUTHORIZED',
  canary_size: 120,
  full_corpus: 'NOT AUTHORIZED',
  provider: 'openrouter',
  model: 'openai/gpt-5-mini',
  hard_cost_cap_usd: 3.0,
  soft_cost_warning_usd: 2.0,
  psr_amb_01: 'KNOWN NON-BLOCKING AMBIGUITY — MUST BE INCLUDED AND MONITORED',
  phase_4_plus: 'OPERATOR REVIEW REQUIRED',
  wave_5: 'BLOCKED',
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

function rankBySeed(items, family) {
  return [...items].sort((a, b) => {
    const ha = crypto.createHash('sha256').update(`${CANARY_SEED}:${family}:${a.phrase_id}`).digest('hex');
    const hb = crypto.createHash('sha256').update(`${CANARY_SEED}:${family}:${b.phrase_id}`).digest('hex');
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

function verifyNoExistingCanary() {
  const markers = [
    path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-CANARY-RESULT-v1.json'),
    path.join(STORAGE_ROOT, 'checkpoints', 'checkpoint-phase3-canary-complete-v1.json'),
    path.join(STORAGE_ROOT, 'manifests', 'canary-selection-v1.json'),
  ];
  const existing = markers.filter((p) => fs.existsSync(p));
  return { blocked: existing.length > 0, existing };
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

function selectCanaryManifest(classified, context) {
  const selected = new Map();
  const selectionLog = [];

  const add = (item, reason) => {
    if (selected.has(item.phrase_id)) return false;
    selected.set(item.phrase_id, { ...item, selection_reason: reason });
    return true;
  };

  // Edge-case representatives first
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

  // Family minimums
  for (const [family, minCount] of Object.entries(FAMILY_MINIMUMS)) {
    const current = [...selected.values()].filter((s) => s.primary_family === family).length;
    const need = Math.max(0, minCount - current);
    if (!need) continue;
    let pool = rankBySeed(
      classified.filter((c) => c.primary_family === family && !selected.has(c.phrase_id)),
      family,
    );
    if (pool.length < need) {
      const tagFallback = {
        geography_modified: (c) => c.tags.includes('geography'),
        generic_erp_platform_ambiguity: (c) => c.tags.includes('erp_reference'),
        product_license_version: (c) => c.tags.includes('product_only')
          || c.evidence_summary?.product_only
          || (c.evidence_summary?.product_version_update && !c.evidence_summary?.product_plus_service),
      };
      const matcher = tagFallback[family];
      if (matcher) {
        pool = rankBySeed(
          classified.filter((c) => matcher(c) && !selected.has(c.phrase_id)),
          `${family}:tag`,
        );
      }
    }
    for (let i = 0; i < need && i < pool.length; i++) {
      const item = { ...pool[i], primary_family: family, selection_family_override: pool[i].primary_family !== family };
      add(item, pool[i].primary_family === family ? `family_minimum:${family}` : `family_minimum_tag_fallback:${family}`);
      selectionLog.push({ type: 'family_minimum', family, phrase_id: pool[i].phrase_id, tag_fallback: pool[i].primary_family !== family });
    }
  }

  // Fill to exactly 120 if short
  if (selected.size < CANARY_SIZE) {
    const remaining = rankBySeed(
      classified.filter((c) => !selected.has(c.phrase_id)),
      'fill_remainder',
    );
    for (const item of remaining) {
      if (selected.size >= CANARY_SIZE) break;
      add(item, 'deterministic_fill_remainder');
    }
  }

  if (selected.size !== CANARY_SIZE) {
    throw new Error(`SELECTION_COUNT_MISMATCH:${selected.size}`);
  }

  const items = [...selected.values()].sort((a, b) => a.phrase_id.localeCompare(b.phrase_id));
  const familyCounts = {};
  for (const item of items) {
    familyCounts[item.primary_family] = (familyCounts[item.primary_family] || 0) + 1;
  }

  return {
    manifest_id: 'corvonero-run-004-phase-3-canary-selection-v1',
    run_id: RUN_ID,
    seed: CANARY_SEED,
    algorithm: 'edge_case_first → family_minimums → deterministic SHA-256 rank fill',
    selected_count: items.length,
    family_minimums: FAMILY_MINIMUMS,
    family_counts: familyCounts,
    selection_log: selectionLog,
    items,
    created_at: new Date().toISOString(),
  };
}

function acquirePhase3Lock(corpusHash) {
  const lockPath = path.join(STORAGE_ROOT, 'locks', 'run.lock.json');
  if (fs.existsSync(lockPath)) {
    const existing = loadJson(lockPath);
    if (existing.status === 'ACTIVE' && existing.phase === 'PHASE_3_CANARY') {
      throw new Error('BLOCKED — LOCK OWNERSHIP CONFLICT');
    }
  }
  const lock = {
    schema_version: '1.0.0',
    run_id: RUN_ID,
    project_id: 'PRJ-0013',
    phase: 'PHASE_3_CANARY',
    owner_pid: process.pid,
    process_identity: `execute-run-004-phase3-canary-v1.mjs@${process.pid}`,
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
  writeJsonAtomic(path.join(STORAGE_ROOT, 'receipts', 'phase3-lock-release-receipt-v1.json'), {
    run_id: RUN_ID,
    released_at: lock.released_at,
    outcome,
    phase: 'PHASE_3_CANARY',
  });
}

const costTracker = {
  input_tokens: 0,
  output_tokens: 0,
  calculated_cost_usd: 0,
  retries: 0,
  model_errors: 0,
};

function trackUsage(meta) {
  if (!meta?.usage) return;
  costTracker.input_tokens += meta.usage.prompt_tokens || 0;
  costTracker.output_tokens += meta.usage.completion_tokens || 0;
  costTracker.calculated_cost_usd =
    (costTracker.input_tokens / 1e6) * PRICING.input_per_m +
    (costTracker.output_tokens / 1e6) * PRICING.output_per_m;
}

function assertCostCap() {
  const cumulative = SPPC05_COST_USD + costTracker.calculated_cost_usd;
  if (cumulative > OPERATOR.hard_cost_cap_usd) {
    throw new Error(`BLOCKED — CANARY COST PROJECTION EXCEEDS RUN CAP:${cumulative.toFixed(4)}`);
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

  const primary = await runBlindPrimaryAssessment({
    phrase,
    ...context,
    adapter,
    forbiddenContext: {},
  });
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
  const primaryVerdict = primary.output?.decision;
  const reassessmentVerdict = secondary.output?.decision;
  const confirmationDisagree = secondary.ok && !assessmentsAgree(primary.output, secondary.output);
  const reviewFlag = item.review_required
    || confirmationDisagree
    || item.expectation_class === 'review_required';

  let expectationMatch = null;
  if (item.expected_verdict) {
    expectationMatch = finalVerdict === item.expected_verdict;
  }

  return {
    phrase_id: item.phrase_id,
    phrase: item.phrase,
    primary_family: item.primary_family,
    tags: item.tags,
    edge_cases: item.edge_cases,
    expectation_class: item.expectation_class,
    expected_verdict: item.expected_verdict,
    review_required: item.review_required,
    selection_reason: item.selection_reason,
    primary_verdict: primaryVerdict,
    reassessment_verdict: reassessmentVerdict,
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
    schema_valid: true,
    structured_evidence: structured,
    platform_compatibility: platform,
    hard_rule: hardRules,
  };
}

async function runBatch(batchIndex, batchItems, context, adapter, manifestIds) {
  const batchId = `canary-batch-${String(batchIndex + 1).padStart(2, '0')}`;
  const batchDir = path.join(STORAGE_ROOT, 'batches', batchId);
  const inputIds = batchItems.map((i) => i.phrase_id);

  for (const id of inputIds) {
    if (!manifestIds.has(id)) throw new Error(`OUT_OF_MANIFEST:${id}`);
  }

  const startReceipt = {
    batch_id: batchId,
    batch_index: batchIndex,
    phrase_count: batchItems.length,
    input_ids: inputIds,
    started_at: new Date().toISOString(),
    provider: OPERATOR.provider,
    model: OPERATOR.model,
  };
  writeJsonAtomic(path.join(batchDir, 'batch-start-receipt-v1.json'), startReceipt);

  const results = [];
  const failures = [];
  for (const item of batchItems) {
    try {
      const r = await evaluatePhraseRecord(item, context, adapter);
      results.push(r);
      if (r.error) failures.push(r);
      fs.writeFileSync(
        path.join(STORAGE_ROOT, 'raw-responses', `${item.phrase_id}.json`),
        JSON.stringify(r, null, 2),
      );
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

function analyzeStopConditions(allResults, manifest) {
  const issues = [];
  const verdicts = { ACCEPT: 0, REJECT: 0, ABSTAIN: 0 };
  for (const r of allResults) {
    if (r.final_verdict) verdicts[r.final_verdict]++;
  }

  const preAuth = allResults.filter((r) => r.expectation_class === 'pre_authorized' && r.expected_verdict);
  const falseAccepts = preAuth.filter((r) => r.expected_verdict === 'REJECT' && r.final_verdict === 'ACCEPT');
  const falseRejects = preAuth.filter((r) => r.expected_verdict === 'ACCEPT' && r.final_verdict === 'REJECT');
  const wrongAbstains = preAuth.filter((r) => r.expected_verdict === 'ABSTAIN' && r.final_verdict !== 'ABSTAIN');

  if (falseAccepts.length >= 3) issues.push('broad_false_accept_family');
  if (falseRejects.length >= 5) issues.push('broad_false_reject_family');

  const directCommercial = allResults.filter((r) => r.primary_family === 'direct_commercial_1c_service');
  const directRejected = directCommercial.filter((r) => r.final_verdict === 'REJECT').length;
  if (directCommercial.length && directRejected / directCommercial.length > 0.5) {
    issues.push('direct_commercial_systematically_rejected');
  }

  const infoAccepted = allResults.filter(
    (r) => r.primary_family === 'informational_self_service' && r.final_verdict === 'ACCEPT',
  );
  if (infoAccepted.length >= 4) issues.push('informational_systematically_accepted');

  const genericErp = allResults.filter((r) => r.primary_family === 'generic_erp_platform_ambiguity');
  const genericRejected = genericErp.filter((r) => r.final_verdict === 'REJECT').length;
  if (genericErp.length && genericRejected / genericErp.length > 0.5) {
    issues.push('generic_erp_systematically_rejected');
  }

  const psrFamily = allResults.filter((r) => r.edge_cases?.includes('psr_amb_01_family') || r.tags?.includes('psr_amb_01_family'));
  const psrAccepted = psrFamily.filter((r) => r.final_verdict === 'ACCEPT').length;
  if (psrFamily.length >= 3 && psrAccepted / psrFamily.length > 0.6) {
    issues.push('product_plus_service_false_accept_family');
  }

  const foreignAccepted = allResults.filter(
    (r) => r.edge_cases?.includes('foreign_incompatible_platform') && r.final_verdict === 'ACCEPT',
  );
  if (foreignAccepted.length) issues.push('foreign_platform_accepted');

  return {
    issues,
    false_accepts: falseAccepts,
    false_rejects: falseRejects,
    wrong_abstains: wrongAbstains,
    verdicts,
    psr_family: { total: psrFamily.length, accepted: psrAccepted },
  };
}

async function main() {
  const existing = verifyNoExistingCanary();
  if (existing.blocked) {
    console.error(JSON.stringify({ error: 'BLOCKED — RUN 004 CANARY STATE ALREADY EXISTS', existing: existing.existing }));
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

  const classified = classifyCorpus(records, context);
  const manifest = selectCanaryManifest(classified, context);
  const manifestIds = new Set(manifest.items.map((i) => i.phrase_id));

  const projectedCanaryCost = CANARY_SIZE * 1600 / 1e6 * 0.15 * 2;
  const maxExposure = SPPC05_COST_USD + projectedCanaryCost;
  if (maxExposure > OPERATOR.hard_cost_cap_usd) {
    console.error(JSON.stringify({ error: 'BLOCKED — CANARY COST PROJECTION EXCEEDS RUN CAP', maxExposure }));
    process.exit(2);
  }

  // Phase transition receipt
  const authReceipt = {
    receipt_id: 'phase-3-canary-authorization-v1',
    run_id: RUN_ID,
    operator_decisions: OPERATOR,
    lifecycle_from: 'PHASE_0_1_2_COMPLETE',
    lifecycle_to: 'PHASE_3_CANARY_AUTHORIZED',
    canary_size: CANARY_SIZE,
    corpus_hash_prefix: corpusHash.slice(0, 16),
    orca_hashes: Object.fromEntries(Object.entries(ORCA_HASHES).map(([k, v]) => [k, v.slice(0, 16)])),
    cost_limits: { hard_cap_usd: 3, soft_warning_usd: 2, sppc05_recorded_usd: SPPC05_COST_USD },
    prohibited: ['full corpus', 'Wave 5', 'semantic assembly', 'strategy', 'Campaign Architecture', 'Commander', 'import', 'launch'],
    psr_amb_01_policy: OPERATOR.psr_amb_01,
    authorized_at: new Date().toISOString(),
  };
  writeJsonAtomic(path.join(STORAGE_ROOT, 'receipts', 'phase-3-authorization-receipt-v1.json'), authReceipt);
  writeJsonAtomic(path.join(STORAGE_ROOT, 'manifests', 'canary-selection-v1.json'), manifest);
  writeJsonAtomic(path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-CANARY-SELECTION-v1.json'), manifest);

  const lockPath = acquirePhase3Lock(corpusHash);
  const checkpoint = {
    run_id: RUN_ID,
    phase: 'PHASE_3_CANARY',
    lifecycle_state: 'PHASE_3_CANARY_AUTHORIZED',
    project_processed: 0,
    project_total: 2368,
    canary_selected: CANARY_SIZE,
    canary_processed: 0,
    full_production_processed: 0,
    processed_ids: [],
    cumulative_cost_usd: SPPC05_COST_USD,
    started_at: new Date().toISOString(),
  };
  writeJsonAtomic(path.join(STORAGE_ROOT, 'checkpoints', 'checkpoint-phase3-canary-v1.json'), checkpoint);

  const adapter = createOpenAICompatibleAdapter();
  if (!adapter) {
    releaseLock(lockPath, 'FAILED — ADAPTER UNAVAILABLE');
    process.exit(2);
  }

  const allResults = [];
  const batches = [];
  const items = manifest.items;

  try {
    for (let b = 0; b < Math.ceil(items.length / BATCH_SIZE); b++) {
      const slice = items.slice(b * BATCH_SIZE, (b + 1) * BATCH_SIZE);
      const batchResult = await runBatch(b, slice, context, adapter, manifestIds);
      batches.push(batchResult);
      allResults.push(...batchResult.results.filter((r) => !r.error));

      checkpoint.canary_processed = allResults.length;
      checkpoint.processed_ids = allResults.map((r) => r.phrase_id);
      checkpoint.cumulative_cost_usd = SPPC05_COST_USD + costTracker.calculated_cost_usd;
      checkpoint.last_heartbeat = new Date().toISOString();
      writeJsonAtomic(path.join(STORAGE_ROOT, 'checkpoints', 'checkpoint-phase3-canary-v1.json'), checkpoint);

      if (SPPC05_COST_USD + costTracker.calculated_cost_usd > OPERATOR.soft_cost_warning_usd) {
        checkpoint.soft_cost_warning = true;
      }
      assertCostCap();
    }
  } catch (e) {
    releaseLock(lockPath, `FAILED — ${e.message}`);
    throw e;
  }

  const analysis = analyzeStopConditions(allResults, manifest);
  const schemaValidPct = (allResults.filter((r) => r.schema_valid).length / allResults.length) * 100;
  const criticalFail = analysis.issues.length > 0 || allResults.length !== CANARY_SIZE;

  const canaryVerdict = criticalFail
    ? { canary: 'FAILED', run: 'BLOCKED_AT_PHASE_3_CANARY' }
    : { canary: 'PASS — OPERATOR REVIEW REQUIRED', run: 'PHASE_3_COMPLETE' };

  checkpoint.canary_processed = allResults.length;
  checkpoint.complete = !criticalFail;
  checkpoint.lifecycle_state = criticalFail ? 'BLOCKED_AT_PHASE_3_CANARY' : 'PHASE_3_COMPLETE';
  checkpoint.cumulative_cost_usd = SPPC05_COST_USD + costTracker.calculated_cost_usd;
  checkpoint.completed_at = new Date().toISOString();
  writeJsonAtomic(
    path.join(STORAGE_ROOT, 'checkpoints', criticalFail ? 'checkpoint-phase3-canary-failed-v1.json' : 'checkpoint-phase3-canary-complete-v1.json'),
    checkpoint,
  );

  const resultPayload = {
    run_id: RUN_ID,
    manifest_id: manifest.manifest_id,
    canary_verdict: canaryVerdict,
    processed_count: allResults.length,
    verdict_distribution: analysis.verdicts,
    metrics: {
      schema_valid_percentage: schemaValidPct,
      retry_count: costTracker.retries,
      model_error_count: costTracker.model_errors,
      confirmation_disagreement_rate: allResults.filter((r) => r.confirmation_disagreement).length / allResults.length,
      reassessment_disagreement_rate: allResults.filter((r) => r.primary_verdict !== r.reassessment_verdict && r.reassessment_verdict).length / allResults.length,
      adjudication_rate: allResults.filter((r) => r.adjudication_path === 'DISAGREE').length / allResults.length,
      invariant_application_rate: allResults.filter((r) => r.invariant_applications?.length).length / allResults.length,
      operator_review_rate: allResults.filter((r) => r.review_flag).length / allResults.length,
      pre_authorized_false_accepts: analysis.false_accepts.length,
      pre_authorized_false_rejects: analysis.false_rejects.length,
    },
    cost: {
      canary_cost_usd: costTracker.calculated_cost_usd,
      cumulative_cost_usd: SPPC05_COST_USD + costTracker.calculated_cost_usd,
      input_tokens: costTracker.input_tokens,
      output_tokens: costTracker.output_tokens,
    },
    psr_amb_01_family: analysis.psr_family,
    stop_analysis: analysis,
    batches: batches.map((b) => b.completionReceipt),
    results: allResults,
    completed_at: new Date().toISOString(),
  };

  writeJsonAtomic(path.join(STORAGE_ROOT, 'reports', 'canary-execution-report-v1.json'), resultPayload);
  writeJsonAtomic(path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-CANARY-RESULT-v1.json'), resultPayload);

  // Update git run manifest
  const runManifest = loadJson(path.join(GIT_RUN_DIR, 'run-manifest-v1.json'));
  runManifest.lifecycle_state = checkpoint.lifecycle_state;
  runManifest.gate_c = canaryVerdict.canary;
  runManifest.canary_processed = allResults.length;
  runManifest.completed_at = new Date().toISOString();
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'run-manifest-v1.json'), runManifest);
  writeJsonAtomic(path.join(GIT_RUN_DIR, 'lifecycle-decision-v1.json'), {
    run_id: RUN_ID,
    decision: checkpoint.lifecycle_state,
    canary: canaryVerdict.canary,
    next_gate: 'OPERATOR REVIEW OF CORVONERO RUN 004 PHASE 3 CANARY',
    canary_authorized: true,
    full_corpus_authorized: false,
  });

  releaseLock(lockPath, canaryVerdict.canary);

  console.log(JSON.stringify({
    canary_verdict: canaryVerdict,
    processed: allResults.length,
    cost: resultPayload.cost,
    verdicts: analysis.verdicts,
  }, null, 2));

  process.exit(criticalFail ? 1 : 0);
}

main().catch((e) => {
  console.error(e.message || e);
  process.exit(1);
});
