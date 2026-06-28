#!/usr/bin/env node
/**
 * Resume Corvonero Run 004 Phase 3 canary Attempt 2 — process missing phrase records only.
 */
import fs from 'node:fs';
import path from 'node:path';
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
import { EXPECTATION_STATUS } from './canary-family-classifier-v2.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const RUN_ID = 'corv-semantic-v2-20260626-004';
const ATTEMPT_ID = 'corv-run004-phase3-canary-attempt-002';
const STORAGE_ROOT = path.join('C:\\MARS Phenix\\AI MARS STORAGE', 'mig', 'corvonero', 'semantic-runs', RUN_ID);
const PILOT_DIR = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const FIX = path.join(REPO_ROOT, 'projects/orca/semantic-intelligence/live-model/fixtures');
const CUMULATIVE_BEFORE_ATTEMPT2 = 0.7703344999999999;
const HARD_CAP = 3.0;
const PRICING = { input_per_m: 0.15, output_per_m: 0.60 };
const SCORED_STATUSES = new Set([EXPECTATION_STATUS.AUTHORITATIVE_EXPECTATION, EXPECTATION_STATUS.POLICY_DERIVED_EXPECTATION]);

function loadJson(p) { return JSON.parse(fs.readFileSync(p, 'utf8')); }
function writeJsonAtomic(filePath, data) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  const tmp = `${filePath}.${process.pid}.tmp`;
  fs.writeFileSync(tmp, JSON.stringify(data, null, 2));
  fs.renameSync(tmp, filePath);
}

const costTracker = { input_tokens: 0, output_tokens: 0, calculated_cost_usd: 0 };

function trackUsage(meta) {
  if (!meta?.usage) return;
  costTracker.input_tokens += meta.usage.prompt_tokens || 0;
  costTracker.output_tokens += meta.usage.completion_tokens || 0;
  costTracker.calculated_cost_usd = (costTracker.input_tokens / 1e6) * PRICING.input_per_m + (costTracker.output_tokens / 1e6) * PRICING.output_per_m;
}

async function evaluatePhraseRecord(item, context, adapter) {
  const phrase = { phrase_id: item.phrase_id, raw_query: item.phrase, normalized_query: item.normalized_phrase || item.phrase.toLowerCase(), region: 'RU' };
  const structured = extractServiceIntentEvidence(phrase);
  const platform = evaluatePlatformCompatibility(phrase, context.businessScope, context.serviceRegistry);
  const primary = await runBlindPrimaryAssessment({ phrase, ...context, adapter, forbiddenContext: {} });
  if (!primary.ok) return { phrase_id: item.phrase_id, error: primary.blocker, schema_valid: false };
  trackUsage(primary.output?.model_metadata);
  const det = assessDeterministic(createAssessorContext(phrase, context));
  const hardRules = applyHardRules(phrase, det, context);
  const secondary = await runIndependentReassessment({ phrase, ...context, primaryAdapter: adapter, secondaryAdapter: adapter, hardRuleEvidence: hardRules });
  if (secondary.ok) trackUsage(secondary.output?.model_metadata);
  const adj = adjudicateSemanticIntent({ assessmentA: primary.output, assessmentB: secondary.ok ? secondary.output : null, hardRuleEvidence: hardRules, serviceRegistry: context.serviceRegistry, businessScope: context.businessScope, phrase, structuredEvidence: structured, platformCompatibility: platform });
  const finalVerdict = adj.final_decision.replace(/^FINAL\s+/, '');
  const confirmationDisagree = secondary.ok && !assessmentsAgree(primary.output, secondary.output);
  let errorClass = null;
  if (item.scored && SCORED_STATUSES.has(item.expectation_status) && item.expected_verdict) {
    if (finalVerdict !== item.expected_verdict) {
      if (item.expected_verdict === 'REJECT' && finalVerdict === 'ACCEPT') errorClass = 'confirmed_false_accept';
      else if (item.expected_verdict === 'ACCEPT' && finalVerdict === 'REJECT') errorClass = 'confirmed_false_reject';
      else if (item.expected_verdict === 'ABSTAIN' && finalVerdict !== 'ABSTAIN') errorClass = 'review_disagreement';
    }
  }
  return {
    phrase_id: item.phrase_id, phrase: item.phrase, observed_tags: item.observed_tags, primary_family: item.primary_family,
    tags: item.tags, edge_cases: item.edge_cases, expectation_status: item.expectation_status, expectation_class: item.expectation_class,
    expected_verdict: item.expected_verdict, authority_source: item.authority_source, scored: item.scored, review_required: item.review_required,
    selection_reason: item.selection_reason, primary_verdict: primary.output?.decision, reassessment_verdict: secondary.output?.decision,
    confirmation_disagreement: confirmationDisagree, confirmation_result: confirmationDisagree ? 'DISAGREE' : (secondary.ok ? 'AGREE' : 'SINGLE'),
    evidence_classes: structured.signals || [], platform_class: platform.classification,
    applied_hard_rules: (hardRules.evidence || []).map((e) => e.rule), adjudication_path: adj.agreement_state,
    invariant_applications: adj.invariant_applications || [], final_verdict: finalVerdict, confidence: adj.confidence,
    reason: primary.output?.rationale || adj.findings?.join('; '), review_flag: item.review_required || confirmationDisagree || !item.scored,
    expectation_match: item.scored && item.expected_verdict ? finalVerdict === item.expected_verdict : null,
    error_class: errorClass, schema_valid: true, structured_evidence: structured, platform_compatibility: platform, hard_rule: hardRules,
  };
}

function analyzeStopConditionsV2(allResults) {
  const issues = [];
  const verdicts = { ACCEPT: 0, REJECT: 0, ABSTAIN: 0 };
  for (const r of allResults) if (r.final_verdict) verdicts[r.final_verdict]++;
  const scored = allResults.filter((r) => r.scored && SCORED_STATUSES.has(r.expectation_status) && r.expected_verdict);
  const falseAccepts = scored.filter((r) => r.error_class === 'confirmed_false_accept');
  const falseRejects = scored.filter((r) => r.error_class === 'confirmed_false_reject');
  if (falseAccepts.length >= 3) issues.push('broad_false_accept_family');
  if (falseRejects.length >= 5) issues.push('broad_false_reject_family');
  const directCommercial = scored.filter((r) => r.primary_family === 'direct_commercial_1c_service' && r.expected_verdict === 'ACCEPT');
  if (directCommercial.length >= 5 && directCommercial.filter((r) => r.final_verdict === 'REJECT').length / directCommercial.length > 0.5) issues.push('direct_commercial_systematically_rejected');
  return { issues, false_accepts: falseAccepts, false_rejects: falseRejects, verdicts, scored_count: scored.length, review_required_count: allResults.filter((r) => !r.scored || r.review_required).length, psr_family: { total: 0, accepted: 0 } };
}

async function main() {
  const resultPath = path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-CANARY-RESULT-v2.json');
  const manifest = loadJson(path.join(PILOT_DIR, 'CORVONERO-RUN-004-PHASE-3-CANARY-SELECTION-v2.json'));
  const existing = loadJson(resultPath);
  const processed = new Set((existing.results || []).map((r) => r.phrase_id));
  const missing = manifest.items.filter((i) => !processed.has(i.phrase_id));
  if (!missing.length) { console.log('No missing records'); process.exit(0); }

  loadLocalSecrets();
  const priorAttempt2Cost = existing.cost?.attempt2_cost_usd || 0;
  const context = {
    businessScope: loadJson(path.join(FIX, 'business-scope-eval-v1.json')),
    serviceRegistry: loadJson(path.join(FIX, 'service-registry-eval-v1.json')),
    taxonomy: {}, commercialPolicy: { version: 'v1' },
  };
  const adapter = createOpenAICompatibleAdapter();
  if (!adapter) process.exit(2);

  const rawDir = path.join(STORAGE_ROOT, 'raw-responses', 'attempt2');
  fs.mkdirSync(rawDir, { recursive: true });

  const newResults = [];
  for (const item of missing) {
    if (CUMULATIVE_BEFORE_ATTEMPT2 + priorAttempt2Cost + costTracker.calculated_cost_usd > HARD_CAP) throw new Error('BLOCKED — RUN COST CAP RISK');
    let r = null;
    for (let attempt = 0; attempt < 3; attempt++) {
      r = await evaluatePhraseRecord(item, context, adapter);
      if (r.schema_valid) break;
      if (r.error !== 'MALFORMED_MODEL_OUTPUT') break;
    }
    if (!r?.schema_valid) { console.error('Failed', item.phrase_id, r?.error); process.exit(1); }
    newResults.push(r);
    fs.writeFileSync(path.join(rawDir, `${item.phrase_id}.json`), JSON.stringify(r, null, 2));
  }

  const allResults = [...existing.results, ...newResults].sort((a, b) => a.phrase_id.localeCompare(b.phrase_id));
  const analysis = analyzeStopConditionsV2(allResults);
  const attempt2TotalCost = priorAttempt2Cost + costTracker.calculated_cost_usd;
  const criticalFail = analysis.issues.length > 0 || allResults.length !== 120;
  const canaryVerdict = criticalFail ? { canary: 'FAILED', run: 'BLOCKED_AT_PHASE_3_CANARY_ATTEMPT_2' } : { canary: 'PASS — OPERATOR REVIEW REQUIRED', run: 'PHASE_3_COMPLETE' };

  const resultPayload = {
    ...existing,
    canary_verdict: canaryVerdict,
    processed_count: allResults.length,
    verdict_distribution: analysis.verdicts,
    metrics: {
      ...existing.metrics,
      scored_authoritative_count: allResults.filter((r) => r.scored && r.expected_verdict).length,
      confirmed_false_accepts: analysis.false_accepts.length,
      confirmed_false_rejects: analysis.false_rejects.length,
      resume_completed: true,
      resume_added: newResults.length,
    },
    cost: {
      attempt2_cost_usd: attempt2TotalCost,
      cumulative_before_attempt2_usd: CUMULATIVE_BEFORE_ATTEMPT2,
      cumulative_cost_usd: CUMULATIVE_BEFORE_ATTEMPT2 + attempt2TotalCost,
      input_tokens: (existing.cost?.input_tokens || 0) + costTracker.input_tokens,
      output_tokens: (existing.cost?.output_tokens || 0) + costTracker.output_tokens,
    },
    stop_analysis: analysis,
    results: allResults,
    completed_at: new Date().toISOString(),
  };

  writeJsonAtomic(resultPath, resultPayload);
  writeJsonAtomic(path.join(STORAGE_ROOT, 'reports', 'canary-attempt2-execution-report-v1.json'), resultPayload);
  console.log(JSON.stringify({ resumed: newResults.length, total: allResults.length, canary_verdict: canaryVerdict }, null, 2));
  process.exit(criticalFail ? 1 : 0);
}

main().catch((e) => { console.error(e); process.exit(1); });
