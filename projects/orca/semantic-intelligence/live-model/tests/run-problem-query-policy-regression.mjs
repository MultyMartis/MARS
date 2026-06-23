#!/usr/bin/env node
/** Adversarial problem-query policy regression (Wave 3.1E). */
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

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIX = path.join(__dirname, '../fixtures');
const OUT = path.join(__dirname, '../reports', `problem-policy-regression-${Date.now()}`);

const cases = [
  { id: 'PQR-ACCEPT-01', q: 'срочно нужен специалист 1с база не открывается', expected: 'ACCEPT', class: 'urgent_specialist' },
  { id: 'PQR-ABSTAIN-01', q: '1с не работает после обновления', expected: 'ABSTAIN', class: 'ordinary_troubleshooting' },
  { id: 'PQR-REJECT-01', q: 'как настроить 1с самостоятельно по инструкции', expected: 'REJECT', class: 'diy' },
  { id: 'PQR-REJECT-02', q: 'что такое 1с erp простыми словами', expected: 'REJECT', class: 'informational' },
  { id: 'PQR-ABSTAIN-02', q: 'ошибка 0x80004005 1с', expected: 'ABSTAIN', class: 'unclear_error' },
  { id: 'PQR-ACCEPT-02', q: 'заказать восстановление базы 1с после сбоя', expected: 'ACCEPT', class: 'service_object_problem' },
  { id: 'PQR-REJECT-03', q: 'как установить photoshop на mac самому', expected: 'REJECT', class: 'out_of_scope_diy' },
];

function loadJson(p) { return JSON.parse(fs.readFileSync(p, 'utf8')); }

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
    const phrase = { phrase_id: c.id, raw_query: c.q, normalized_query: c.q.toLowerCase(), region: 'RU' };
    const primary = await runBlindPrimaryAssessment({ phrase, ...context, adapter, forbiddenContext: {} });
    const det = assessDeterministic(createAssessorContext(phrase, context));
    const hardRules = applyHardRules(phrase, det);
    const adj = adjudicateSemanticIntent({
      assessmentA: primary.ok ? primary.output : { decision: 'ABSTAIN' },
      assessmentB: null,
      hardRuleEvidence: hardRules,
      serviceRegistry: context.serviceRegistry,
    });
    results.push({
      record_id: c.id,
      class: c.class,
      expected: c.expected,
      final: adj.final_decision,
      match: adj.final_decision === c.expected,
    });
  }

  const passCount = results.filter((r) => r.match).length;
  fs.mkdirSync(OUT, { recursive: true });
  fs.writeFileSync(path.join(OUT, 'problem-policy-regression-v1.json'), JSON.stringify({ results, pass_count: passCount, total: results.length }, null, 2));
  console.log(`Problem policy regression: ${passCount}/${results.length}`);
  process.exit(passCount === results.length ? 0 : 1);
}

main().catch((e) => { console.error(e.message || e); process.exit(1); });
