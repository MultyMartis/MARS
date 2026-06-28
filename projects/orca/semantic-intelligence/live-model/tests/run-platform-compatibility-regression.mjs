#!/usr/bin/env node
/** Platform compatibility + SPPC-05 repair focused regression (Wave 3.1F). */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadLocalSecrets } from '../runtime/local-secret-loader.mjs';
import { createOpenAICompatibleAdapter } from '../adapters/openai-compatible-adapter.mjs';
import { runBlindPrimaryAssessment } from '../assessment/blind-assessment.mjs';
import { adjudicateSemanticIntent } from '../adjudication/semantic-adjudicator.mjs';
import { applyHardRules } from '../../production/assessors/hard-rules.mjs';
import { assessDeterministic } from '../../production/assessors/deterministic-assessor.mjs';
import { createAssessorContext } from '../../production/assessors/assessor-contract.mjs';
import { extractServiceIntentEvidence } from '../evidence/service-intent-evidence.mjs';
import { evaluatePlatformCompatibility } from '../evidence/platform-compatibility.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIX = path.join(__dirname, '../fixtures');
const OUT = path.join(__dirname, '../reports', `platform-compatibility-regression-${Date.now()}`);

const cases = [
  { id: 'PC-ACCEPT-01', q: 'специалист обновить конфигурацию 1с', expected: 'ACCEPT', class: '1c_service_update' },
  { id: 'PC-REJECT-01', q: 'обновление sap business one до новой версии', expected: 'REJECT', class: 'foreign_product_update' },
  { id: 'PC-REJECT-02', q: 'обновление microsoft dynamics до новой версии', expected: 'REJECT', class: 'foreign_product_update' },
  { id: 'PC-REJECT-03', q: 'как обновить 1с самостоятельно инструкция', expected: 'REJECT', class: '1c_self_update' },
  { id: 'PC-ACCEPT-02', q: 'обновление базы 1с заказать специалиста', expected: 'ACCEPT', class: '1c_service_update' },
  { id: 'PC-ABSTAIN-01', q: 'обновление erp до новой версии', expected: 'ABSTAIN', class: 'generic_erp_update' },
  { id: 'PC-ABSTAIN-02', q: 'обновить erp систему', expected: 'ABSTAIN', class: 'generic_erp_update' },
  { id: 'PC-REJECT-04', q: 'обновление oracle erp cloud до новой версии', expected: 'REJECT', class: 'foreign_product_update' },
  { id: 'PC-ACCEPT-03', q: 'обновление 1с специалистом', expected: 'ACCEPT', class: '1c_service_update' },
];

function loadJson(p) { return JSON.parse(fs.readFileSync(p, 'utf8')); }

async function evaluateCase(c, context, adapter) {
  const phrase = { phrase_id: c.id, raw_query: c.q, normalized_query: c.q.toLowerCase(), region: 'RU' };
  const structured = extractServiceIntentEvidence(phrase);
  const platform = evaluatePlatformCompatibility(phrase, context.businessScope, context.serviceRegistry);
  const primary = await runBlindPrimaryAssessment({ phrase, ...context, adapter, forbiddenContext: {} });
  const det = assessDeterministic(createAssessorContext(phrase, context));
  const hardRules = applyHardRules(phrase, det, context);
  const adj = adjudicateSemanticIntent({
    assessmentA: primary.ok ? primary.output : { decision: 'ABSTAIN' },
    assessmentB: null,
    hardRuleEvidence: hardRules,
    serviceRegistry: context.serviceRegistry,
    businessScope: context.businessScope,
    phrase,
  });
  return {
    record_id: c.id,
    class: c.class,
    expected: c.expected,
    final: adj.final_decision,
    match: adj.final_decision === c.expected,
    primary: primary.output?.decision,
    hard_rule: hardRules.override_decision || null,
    structured_signals: structured.signals,
    platform,
    findings: adj.findings,
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
  for (const c of cases) {
    results.push(await evaluateCase(c, context, adapter));
  }

  const passCount = results.filter((r) => r.match).length;
  fs.mkdirSync(OUT, { recursive: true });
  fs.writeFileSync(path.join(OUT, 'platform-compatibility-regression-v1.json'), JSON.stringify({
    results,
    pass_count: passCount,
    total: results.length,
  }, null, 2));
  console.log(`Platform compatibility regression: ${passCount}/${results.length}`);
  process.exit(passCount === results.length ? 0 : 1);
}

main().catch((e) => { console.error(e.message || e); process.exit(1); });
