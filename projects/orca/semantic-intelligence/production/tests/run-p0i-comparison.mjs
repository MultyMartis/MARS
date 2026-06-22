#!/usr/bin/env node
/**
 * P0-I diagnostic comparison — automated diff report
 */
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import fs from 'node:fs';
import { assessDeterministic } from '../assessors/deterministic-assessor.mjs';
import { runReassessment, needsReassessment } from '../adjudication/reassessment.mjs';
import { adjudicate } from '../adjudication/adjudicator.mjs';
import { applyHardRules } from '../assessors/hard-rules.mjs';
import { routeBoundedReview } from '../conflict-queue/review-router.mjs';
import { REPO_ROOT } from '../runtime/lib.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const P0I = path.join(REPO_ROOT, 'projects/orca/semantic-intelligence/integration/pilot-runs/p0-i-real-slice-v1/output/p0-i-pilot-semantic-records-v1.json');
const OUT = path.join(__dirname, '../reports/p0i-diagnostic-comparison-v1.json');

const p0i = JSON.parse(fs.readFileSync(P0I, 'utf8'));
const records = p0i.records || [];
const diffs = [];
const reasonFamilies = {};
let agree = 0;

for (const row of records) {
  const raw = row.integration_result?.record?.raw_query || row.raw_query;
  const prev = row.admission_decision || row.integration_result?.admission_decision;
  const phrase = { raw_query: raw, normalized_query: raw?.toLowerCase() };
  const primary = assessDeterministic({ raw_query: raw, normalized_query: raw?.toLowerCase(), business_scope: {}, serviceRegistry: { services: [] } });
  const hard = applyHardRules(phrase, primary);
  const reassess = needsReassessment(primary, hard) ? runReassessment(phrase, {}, primary) : null;
  const adj = adjudicate({ primary, reassessment: reassess, hardRules: hard, invariantResults: [], businessScope: {} });
  const newDecision = adj.final_decision;
  if (newDecision === prev) agree += 1;
  else {
    const family = `${prev}_to_${newDecision}`;
    reasonFamilies[family] = (reasonFamilies[family] || 0) + 1;
    diffs.push({ phrase_id: row.phrase_id, raw_query: raw, previous: prev, new_primary: primary.decision, new_final: newDecision, adjudication: adj.outcome });
  }
}

const prodRecords = records.map((row) => {
  const raw = row.integration_result?.record?.raw_query;
  const phrase = { raw_query: raw, normalized_query: raw?.toLowerCase(), phrase_id: row.phrase_id };
  const primary = assessDeterministic({ raw_query: raw, normalized_query: raw?.toLowerCase(), business_scope: {}, serviceRegistry: { services: [] } });
  const hard = applyHardRules(phrase, primary);
  const reassess = needsReassessment(primary, hard) ? runReassessment(phrase, {}, primary) : null;
  const adj = adjudicate({ primary, reassessment: reassess, hardRules: hard, invariantResults: [], businessScope: {} });
  return { phrase_id: row.phrase_id, raw_query: raw, adjudication_result: adj, demand_tier: null };
});
const review = routeBoundedReview(prodRecords, { qa_sample_rate: 0.02 });

const boundedSample = diffs.slice(0, 15);

const report = {
  comparison_id: 'p0i-production-diagnostic-comparison-v1',
  generated_at: new Date().toISOString(),
  input_count: records.length,
  agreement_count: agree,
  disagreement_count: diffs.length,
  reason_families: reasonFamilies,
  previous_abstain: records.filter((r) => r.admission_decision === 'ABSTAIN').length,
  new_review_queue_size: review.metrics.human_review,
  review_ratio: review.metrics.review_ratio,
  automation_primary: review.metrics.automation_primary,
  bounded_review_sample: boundedSample,
  note: 'DIAGNOSTIC COMPARISON ONLY — NOT OPERATOR LABELING TASK',
};

fs.writeFileSync(OUT, JSON.stringify(report, null, 2));
console.log(`P0-I comparison: ${agree}/${records.length} agreement, review queue ${review.metrics.human_review} (${(review.metrics.review_ratio * 100).toFixed(1)}%)`);
console.log(`Report: ${OUT}`);
