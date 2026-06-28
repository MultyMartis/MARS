#!/usr/bin/env node
/** Targeted SPPC-05 defect reproduction — CFM-PROD-UPD-02, PQR-ABSTAIN-03, PC-ABSTAIN-01. */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadLocalSecrets } from '../runtime/local-secret-loader.mjs';
import { createOpenAICompatibleAdapter } from '../adapters/openai-compatible-adapter.mjs';
import { runBlindPrimaryAssessment } from '../assessment/blind-assessment.mjs';
import { runIndependentReassessment } from '../assessment/independent-reassessment.mjs';
import { adjudicateSemanticIntent, ADJUDICATOR_VERSION } from '../adjudication/semantic-adjudicator.mjs';
import { applyHardRules, HARD_RULES_VERSION } from '../../production/assessors/hard-rules.mjs';
import { assessDeterministic } from '../../production/assessors/deterministic-assessor.mjs';
import { createAssessorContext } from '../../production/assessors/assessor-contract.mjs';
import { PROMPT_VERSION } from '../contracts/prompt-contract.mjs';
import { extractServiceIntentEvidence, SERVICE_INTENT_EVIDENCE_VERSION } from '../evidence/service-intent-evidence.mjs';
import { evaluatePlatformCompatibility, PLATFORM_COMPATIBILITY_VERSION } from '../evidence/platform-compatibility.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIX = path.join(__dirname, '../fixtures');
const OUT = path.join(__dirname, '../reports', `sppc05-defect-repro-${Date.now()}`);

const TARGETS = [
  { id: 'CFM-PROD-UPD-02', q: 'обновление sap business one до новой версии', expected: 'REJECT', mode: 'dual' },
  { id: 'PQR-ABSTAIN-03', q: 'как исправить ошибку 0x80004005 1с', expected: 'ABSTAIN', mode: 'single' },
  { id: 'PC-ABSTAIN-01', q: 'обновление erp до новой версии', expected: 'ABSTAIN', mode: 'single' },
];

function loadJson(p) { return JSON.parse(fs.readFileSync(p, 'utf8')); }

async function evaluate(target, context, adapter) {
  const phrase = { phrase_id: target.id, raw_query: target.q, normalized_query: target.q.toLowerCase(), region: 'RU' };
  const structured = extractServiceIntentEvidence(phrase);
  const platform = evaluatePlatformCompatibility(phrase, context.businessScope, context.serviceRegistry);
  const primary = await runBlindPrimaryAssessment({ phrase, ...context, adapter, forbiddenContext: {} });
  const det = assessDeterministic(createAssessorContext(phrase, context));
  const hardRules = applyHardRules(phrase, det, context);
  let secondary = null;
  if (target.mode === 'dual') {
    secondary = await runIndependentReassessment({
      phrase, ...context, primaryAdapter: adapter, secondaryAdapter: adapter,
      hardRuleEvidence: hardRules, primaryDecision: undefined, primaryRationale: undefined, expectedLabel: undefined,
    });
  }
  const adj = adjudicateSemanticIntent({
    assessmentA: primary.ok ? primary.output : { decision: 'ABSTAIN' },
    assessmentB: secondary?.ok ? secondary.output : null,
    hardRuleEvidence: hardRules,
    serviceRegistry: context.serviceRegistry,
    businessScope: context.businessScope,
    phrase,
  });
  return {
    record_id: target.id,
    query: target.q,
    expected: target.expected,
    final: adj.final_decision,
    match: adj.final_decision === target.expected,
    primary: primary.output?.decision,
    secondary: secondary?.output?.decision,
    confidence: adj.confidence,
    findings: adj.findings,
    decisive_evidence: adj.decisive_evidence,
    hard_rule: hardRules,
    structured_evidence: structured,
    platform_compatibility: platform,
    adjudication_branch: adj.agreement_state,
    invariant_applications: adj.invariant_applications,
    primary_rationale: primary.output?.rationale,
  };
}

async function main() {
  loadLocalSecrets();
  const adapter = createOpenAICompatibleAdapter();
  if (!adapter) throw new Error('ADAPTER_UNAVAILABLE');
  const context = {
    businessScope: loadJson(path.join(FIX, 'business-scope-eval-v1.json')),
    serviceRegistry: loadJson(path.join(FIX, 'service-registry-eval-v1.json')),
    taxonomy: {},
    commercialPolicy: { version: 'v1' },
  };

  const results = [];
  for (const t of TARGETS) {
    results.push(await evaluate(t, context, adapter));
  }

  const report = {
    prompt_contract_version: PROMPT_VERSION,
    adjudicator_version: ADJUDICATOR_VERSION,
    hard_rules_version: HARD_RULES_VERSION,
    service_intent_evidence_version: SERVICE_INTENT_EVIDENCE_VERSION,
    platform_compatibility_version: PLATFORM_COMPATIBILITY_VERSION,
    provider: process.env.ORCA_SEMANTIC_PROVIDER,
    model: process.env.ORCA_SEMANTIC_MODEL,
    results,
    all_match: results.every((r) => r.match),
  };

  fs.mkdirSync(OUT, { recursive: true });
  fs.writeFileSync(path.join(OUT, 'sppc05-defect-repro-v1.json'), JSON.stringify(report, null, 2));
  console.log(JSON.stringify(report, null, 2));
  process.exit(report.all_match ? 0 : 1);
}

main().catch((e) => { console.error(e.message || e); process.exit(1); });
