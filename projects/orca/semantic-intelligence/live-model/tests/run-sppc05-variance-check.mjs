#!/usr/bin/env node
/** Bounded model variance check for SPPC-05 repair fixtures. */
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
const REPS = Number(process.argv.find((a) => a.startsWith('--reps='))?.split('=')[1] || 3);
const OUT = path.join(__dirname, '../reports', `sppc05-variance-${Date.now()}`);

const CASES = [
  { id: 'CFM-PROD-UPD-02', q: 'обновление sap business one до новой версии', expected: 'REJECT' },
  { id: 'PQR-ABSTAIN-03', q: 'как исправить ошибку 0x80004005 1с', expected: 'ABSTAIN' },
  { id: 'PC-ABSTAIN-01', q: 'обновление erp до новой версии', expected: 'ABSTAIN' },
  { id: 'PSR-AMB-01', q: 'купить 1с с настройкой', expected: 'ABSTAIN', known_ambiguity: true },
];

function loadJson(p) { return JSON.parse(fs.readFileSync(p, 'utf8')); }

async function runOnce(c, context, adapter) {
  const phrase = { phrase_id: c.id, raw_query: c.q, normalized_query: c.q.toLowerCase(), region: 'RU' };
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
    primary: primary.output?.decision,
    final: adj.final_decision,
    confidence: adj.confidence,
    adjudication_branch: adj.agreement_state,
    invariant_applications: adj.invariant_applications,
    match: adj.final_decision === c.expected,
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

  const summary = [];
  let totalCostEstimate = 0;
  for (const c of CASES) {
    const runs = [];
    for (let i = 0; i < REPS; i++) {
      runs.push(await runOnce(c, context, adapter));
    }
    const verdicts = {};
    for (const r of runs) verdicts[r.final] = (verdicts[r.final] || 0) + 1;
    summary.push({
      record_id: c.id,
      expected: c.expected,
      repetitions: REPS,
      verdict_distribution: verdicts,
      confidence_values: runs.map((r) => r.confidence),
      primary_distribution: runs.reduce((acc, r) => { acc[r.primary] = (acc[r.primary] || 0) + 1; return acc; }, {}),
      stable: runs.every((r) => r.final === c.expected),
      all_match: runs.every((r) => r.match),
    });
    totalCostEstimate += REPS;
  }

  const report = {
    repetitions_per_case: REPS,
    provider: process.env.ORCA_SEMANTIC_PROVIDER,
    model: process.env.ORCA_SEMANTIC_MODEL,
    cases: summary,
    policy_stable: summary.every((s) => s.stable),
    repair_cases_stable: summary.filter((s) => ['CFM-PROD-UPD-02', 'PQR-ABSTAIN-03', 'PC-ABSTAIN-01'].includes(s.record_id)).every((s) => s.stable),
    psr_amb_01: summary.find((s) => s.record_id === 'PSR-AMB-01') || null,
  };

  fs.mkdirSync(OUT, { recursive: true });
  fs.writeFileSync(path.join(OUT, 'sppc05-variance-v1.json'), JSON.stringify(report, null, 2));
  console.log(JSON.stringify(report, null, 2));
  process.exit(report.repair_cases_stable ? 0 : 1);
}

main().catch((e) => { console.error(e.message || e); process.exit(1); });
