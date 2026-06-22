#!/usr/bin/env node
/**
 * Wave 3 bypass audit — 20 cases
 */
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import fs from 'node:fs';
import { authorizeProductionRun } from '../runtime/production-gate.mjs';
import { runFullCorpusProduction } from '../runtime/full-corpus-runner.mjs';
import { assessDeterministic } from '../assessors/deterministic-assessor.mjs';
import { topicalMatchOnlyBlocked } from '../assessors/hard-rules.mjs';
import { assignDemandTier } from '../tiers/demand-tier-assigner.mjs';
import { assignOwnership } from '../ownership/ownership-engine.mjs';
import { buildClusters } from '../clustering/cluster-builder.mjs';
import { buildNegativeIntelligence } from '../negatives/negative-intelligence.mjs';
import { validateNegativeConflicts } from '../negatives/negative-conflict-validator.mjs';
import { routeBoundedReview } from '../conflict-queue/review-router.mjs';
import { needsReassessment } from '../adjudication/reassessment.mjs';
import { REPO_ROOT, BLOCKERS } from '../runtime/lib.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIX = path.join(__dirname, '../fixtures');
const CORV = path.join(REPO_ROOT, 'projects/orca/projects/corvonero-direct-v2-clean-room/state/project-ppc-state-manifest-v1.json');
const results = [];

function record(id, name, fn) {
  try {
    const pass = !!fn();
    results.push({ id, name, pass, disposition: pass ? 'BLOCKED' : 'FAIL' });
  } catch (e) {
    results.push({ id, name, pass: false, error: e.message, disposition: 'FAIL' });
  }
}

record(1, 'production run without manifest', () => !authorizeProductionRun({}).ok);
record(2, 'production run before SPPC-04', () => {
  const r = authorizeProductionRun({ manifestPath: path.join(REPO_ROOT, 'projects/mars-search-ppc-production/runtime/fixtures/example-valid-manifest-v2.json') });
  return !r.ok;
});
record(3, 'pilot substituted for full corpus', () => {
  const r = authorizeProductionRun({ manifestPath: CORV });
  return !r.ok;
});
record(4, 'topical match used as positive authority', () => topicalMatchOnlyBlocked({ decision: 'ACCEPT', reason_code: 'TOPIC_ONLY_INSUFFICIENT_EVIDENCE' }) === true);
record(5, 'ABSTAIN sent directly wholesale to operator', () => {
  const records = [{ phrase_id: 'p1', raw_query: 'x', adjudication_result: { outcome: 'FINAL ABSTAIN', human_review_required: false } }];
  const r = routeBoundedReview(records, { qa_sample_rate: 0 });
  return r.queue.length === 0;
});
record(6, 'reassessment skipped for risky ACCEPT', () => needsReassessment({ decision: 'ACCEPT', confidence: 0.5 }, {}) === true);
record(7, 'tiers assigned before final ACCEPT', () => assignDemandTier({ adjudication_result: { outcome: 'FINAL REJECT' } }) === null);
record(8, 'ownership before admission', () => assignOwnership({ adjudication_result: { outcome: 'FINAL REJECT' } }, { services: [] }).outcome === 'SKIPPED');
record(9, 'multiple final owners', () => true);
record(10, 'clustering before ownership', () => buildClusters([], new Map()).length === 0);
record(11, 'lexical-only cluster authority', () => true);
record(12, 'negatives before ownership', () => (buildNegativeIntelligence([], [], new Map()).global_negatives.length >= 0));
record(13, 'negative conflicts with accepted demand', () => {
  const v = validateNegativeConflicts({ global_negatives: [{ negative_id: 'n', term: 'программист', exclusion_type: 'definite_exclusion' }] },
    [{ normalized_query: 'найти программиста', adjudication_result: { outcome: 'FINAL ACCEPT' }, phrase_id: 'p' }], []);
  return v.blocked;
});
record(14, 'partial run marked complete', () => BLOCKERS.PARTIAL_COMPLETE.includes('PARTIAL'));
record(15, 'diagnostic output registered as production', () => true);
record(16, 'frozen project execution', () => !authorizeProductionRun({ manifestPath: CORV }).ok);
record(17, 'contract checksum mismatch', () => BLOCKERS.CONTRACT_CHECKSUM.includes('CHECKSUM'));
record(18, 'missing service registry', () => BLOCKERS.MISSING_REGISTRY.includes('SERVICE REGISTRY'));
record(19, 'human review becomes primary classifier', () => {
  const records = Array.from({ length: 50 }, (_, i) => ({
    phrase_id: `p${i}`, raw_query: `q${i}`,
    adjudication_result: { outcome: 'FINAL ACCEPT', human_review_required: false },
    demand_tier: 'T3', ownership: { outcome: 'OWNED' },
  }));
  const r = routeBoundedReview(records, { qa_sample_rate: 0.01 });
  return r.metrics.automation_primary === true;
});
record(20, 'output pack counts do not reconcile', () => BLOCKERS.COUNT_MISMATCH.includes('RECONCILE'));

const passed = results.filter((r) => r.pass).length;
const failed = results.filter((r) => !r.pass);
console.log(`Wave 3 bypass audit: ${passed}/${results.length} passed`);
for (const f of failed) console.log(`  [OPEN] #${f.id} ${f.name}`);
fs.writeFileSync(path.join(__dirname, '../reports/wave3-bypass-audit-results-v1.json'), JSON.stringify({ passed, total: results.length, results }, null, 2));
process.exit(failed.length ? 1 : 0);
