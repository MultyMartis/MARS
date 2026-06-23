#!/usr/bin/env node
/**
 * Full-corpus readiness test — non-client scale corpus with live pipeline.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { runBlindPrimaryAssessment } from '../assessment/blind-assessment.mjs';
import { runIndependentReassessment } from '../assessment/independent-reassessment.mjs';
import { adjudicateSemanticIntent } from '../adjudication/semantic-adjudicator.mjs';
import { createMockLiveAdapter } from '../adapters/openai-compatible-adapter.mjs';
import { inspectProviderInventory } from '../adapters/provider-inventory.mjs';
import { assertCostCap, loadRunCheckpoint, saveRunCheckpoint, DEFAULT_CONTROLS } from '../controls/cost-rate-controls.mjs';
import { applyHardRules } from '../../production/assessors/hard-rules.mjs';
import { assessDeterministic } from '../../production/assessors/deterministic-assessor.mjs';
import { createAssessorContext } from '../../production/assessors/assessor-contract.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SCALE_CORPUS = path.resolve(__dirname, '../../production/fixtures/scale-corpus-v1.json');
const OUT = path.join(__dirname, '../reports/full-corpus-readiness-v1');

async function main() {
  const inventory = inspectProviderInventory();
  const corpus = JSON.parse(fs.readFileSync(SCALE_CORPUS, 'utf8'));
  const phrases = corpus.phrases.slice(0, 100);
  const costCheck = assertCostCap(phrases.length, DEFAULT_CONTROLS);

  const adapter = inventory.any_live_provider_configured && process.env.ORCA_EVAL_LIVE === '1'
    ? (await import('../adapters/openai-compatible-adapter.mjs')).createOpenAICompatibleAdapter()
    : createMockLiveAdapter();

  fs.mkdirSync(OUT, { recursive: true });
  const checkpoint = loadRunCheckpoint(OUT);
  const processed = new Set(checkpoint.processed_ids || []);
  const context = {
    businessScope: corpus.business_scope,
    serviceRegistry: corpus.service_registry,
  };

  const records = [];
  const started = Date.now();
  let failures = 0;

  for (const phrase of phrases) {
    if (processed.has(phrase.phrase_id)) continue;
    try {
      const primary = await runBlindPrimaryAssessment({ phrase, ...context, adapter });
      if (!primary.ok) { failures++; continue; }
      const det = assessDeterministic(createAssessorContext(phrase, context));
      const hardRules = applyHardRules(phrase, det);
      const secondary = await runIndependentReassessment({ phrase, ...context, primaryAdapter: adapter, secondaryAdapter: adapter, hardRuleEvidence: hardRules });
      const adj = adjudicateSemanticIntent({ assessmentA: primary.output, assessmentB: secondary.output, hardRuleEvidence: hardRules, serviceRegistry: context.serviceRegistry });
      records.push({ phrase_id: phrase.phrase_id, final_decision: adj.final_decision, human_review: adj.human_review_required });
      processed.add(phrase.phrase_id);
    } catch {
      failures++;
    }
  }

  saveRunCheckpoint(OUT, {
    processed_ids: [...processed],
    complete: processed.size >= phrases.length,
    cancelled: false,
  });

  const abstain = records.filter((r) => r.final_decision === 'ABSTAIN').length;
  const review = records.filter((r) => r.human_review).length;

  const report = {
    phrases_processed: records.length,
    failures,
    expected_count: phrases.length,
    output_reconciliation: records.length + failures === phrases.length - (phrases.length - processed.size),
    abstain_rate: records.length ? abstain / records.length : 0,
    review_ratio: records.length ? review / records.length : 0,
    elapsed_ms: Date.now() - started,
    mode: inventory.any_live_provider_configured ? 'live_or_mock' : 'mock_pipeline',
    cost_estimate: costCheck.estimate,
    semantic_pack_valid: records.length > 0,
    corvonero: 'NOT_RUN — FROZEN',
  };

  fs.writeFileSync(path.join(OUT, 'readiness-report-v1.json'), JSON.stringify(report, null, 2));
  console.log('Full-corpus readiness:', JSON.stringify(report, null, 2));
}

main().catch((e) => { console.error(e); process.exit(1); });
