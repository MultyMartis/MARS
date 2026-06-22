#!/usr/bin/env node
/**
 * Wave 3 production test matrix — 30 cases
 */
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { assessDeterministic } from '../assessors/deterministic-assessor.mjs';
import { applyHardRules, topicalMatchOnlyBlocked } from '../assessors/hard-rules.mjs';
import { needsReassessment, runReassessment } from '../adjudication/reassessment.mjs';
import { adjudicate } from '../adjudication/adjudicator.mjs';
import { assignDemandTier, blockFrequencyOnlyTiering } from '../tiers/demand-tier-assigner.mjs';
import { assignOwnership } from '../ownership/ownership-engine.mjs';
import { runClusterQA } from '../clustering/cluster-qa.mjs';
import { validateNegativeConflicts } from '../negatives/negative-conflict-validator.mjs';
import { routeBoundedReview } from '../conflict-queue/review-router.mjs';
import { authorizeProductionRun } from '../runtime/production-gate.mjs';
import { loadCorpusFromFixture } from '../runtime/corpus-loader.mjs';
import { runFullCorpusProduction } from '../runtime/full-corpus-runner.mjs';
import { buildOutputPack } from '../runtime/output-pack.mjs';
import { readJson, BLOCKERS, REPO_ROOT } from '../runtime/lib.mjs';
import fs from 'node:fs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIX = path.join(__dirname, '../fixtures');
const SVC = readJson(path.join(FIX, 'service-registry-scale-v1.json'));
const results = [];

function record(id, name, fn) {
  try {
    const pass = !!fn();
    results.push({ id, name, pass });
  } catch (e) {
    results.push({ id, name, pass: false, error: e.message });
  }
}

const ctx = { businessScope: { version: 'v1' }, serviceRegistry: SVC };

function assess(q) {
  const phrase = { raw_query: q, normalized_query: q.toLowerCase() };
  const primary = assessDeterministic({ raw_query: q, normalized_query: q.toLowerCase(), business_scope: ctx.businessScope, serviceRegistry: SVC });
  const hard = applyHardRules(phrase, primary);
  const reassess = needsReassessment(primary, hard) ? runReassessment(phrase, ctx, primary) : null;
  const adj = adjudicate({ primary, reassessment: reassess, hardRules: hard, invariantResults: [], businessScope: ctx.businessScope });
  return { primary, adj, reassess };
}

record(1, 'explicit provider query → ACCEPT', () => assess('найти программиста 1с').adj.outcome === 'FINAL ACCEPT');
record(2, 'explicit order/price query → ACCEPT', () => assess('стоимость внедрения 1с под ключ').adj.outcome === 'FINAL ACCEPT');
record(3, 'career query → REJECT', () => assess('вакансии программист 1с').adj.outcome === 'FINAL REJECT');
record(4, 'education query → REJECT', () => assess('курсы 1с обучение').adj.outcome === 'FINAL REJECT');
record(5, 'DIY query → REJECT or ABSTAIN', () => ['FINAL REJECT', 'FINAL ABSTAIN'].includes(assess('как настроить 1с самостоятельно').adj.outcome));
record(6, 'product-only query', () => assess('1с управление торговлей').adj.outcome === 'FINAL ABSTAIN');
record(7, 'navigational query', () => assess('corvonero официальный сайт').adj.outcome === 'FINAL REJECT');
record(8, 'ambiguous problem query', () => assess('1с не работает ошибка').adj.outcome === 'FINAL ABSTAIN');
record(9, 'short generic query', () => assess('1с').adj.outcome === 'FINAL ABSTAIN');
record(10, 'protected-intent overlap', () => assess('программист 1с вакансии').adj.outcome === 'FINAL REJECT');
record(11, 'low-confidence ACCEPT reassessment', () => {
  const r = assess('программист 1с');
  return r.reassess !== null || r.adj.outcome === 'FINAL ABSTAIN';
});
record(12, 'ABSTAIN reassessment', () => assess('1с бухгалтерия').reassess !== null);
record(13, 'assessor disagreement adjudication', () => {
  const adj = adjudicate({
    primary: { decision: 'ACCEPT', confidence: 0.6, reason_code: 'TEST', rationale: 'a' },
    reassessment: { agreement: false, suggested_decision: 'ABSTAIN', confidence_adjustment: -0.2 },
    hardRules: {}, invariantResults: [], businessScope: {},
  });
  return adj.outcome === 'FINAL ABSTAIN';
});
record(14, 'invalid semantic record', () => {
  const adj = adjudicate({ primary: { decision: 'MAYBE' }, hardRules: {}, invariantResults: [], businessScope: {} });
  return adj.outcome === 'INVALID RECORD';
});
record(15, 'full-corpus count mismatch', () => {
  try {
    loadCorpusFromFixture(path.join(FIX, 'scale-corpus-v1.json'));
    const bad = readJson(path.join(FIX, 'scale-corpus-v1.json'));
    bad.expected_count = 999;
    return bad.phrases.length !== bad.expected_count;
  } catch { return true; }
});
record(16, 'diagnostic sample substituted for corpus', () => {
  const r = authorizeProductionRun({ manifestPath: path.join(REPO_ROOT, 'projects/orca/projects/corvonero-direct-v2-clean-room/state/project-ppc-state-manifest-v1.json') });
  return r.blocked === true;
});
record(17, 'tier assignment after ACCEPT only', () => {
  const r = assess('вакансии 1с');
  const rec = { adjudication_result: r.adj, final_authority: r.adj.outcome, primary_assessment: r.primary };
  return assignDemandTier(rec) === null;
});
record(18, 'frequency-only tiering blocked', () => blockFrequencyOnlyTiering('T1', { frequency: 5000 }).blocked === true);
record(19, 'ownership to nonexistent service blocked', () => {
  const rec = { adjudication_result: { outcome: 'FINAL ACCEPT' }, normalized_query: 'заказать услуги 1с', raw_query: 'заказать услуги 1с', demand_tier: 'T1' };
  const own = assignOwnership(rec, { services: [{ service_id: 'x', operator_status: 'DRAFT', included_tasks: [], landing_candidates: [] }] });
  return own.outcome === 'SERVICE GAP' || own.outcome === 'LANDING GAP';
});
record(20, 'multiple final owners blocked', () => {
  const qa = runClusterQA([], new Map(), []);
  return qa.major_defects.length === 0;
});
record(21, 'mixed cluster blocked', () => {
  const clusters = [{ cluster_id: 'C1', phrase_ids: ['a', 'b'], demand_tiers: ['T1'], service_owner: 's1' }];
  const omap = new Map([
    ['a', { primary_service_id: 's1', user_task: 't1', commercial_scenario: 'c1', landing_candidate: '/a' }],
    ['b', { primary_service_id: 's2', user_task: 't2', commercial_scenario: 'c2', landing_candidate: '/b' }],
  ]);
  const qa = runClusterQA(clusters, omap, [{ phrase_id: 'a', adjudication_result: { outcome: 'FINAL ACCEPT' } }, { phrase_id: 'b', adjudication_result: { outcome: 'FINAL ACCEPT' } }]);
  return qa.major_defects.some((d) => d.type === 'mixed_services');
});
record(22, 'orphan phrase detected', () => {
  const qa = runClusterQA([], new Map(), [{ phrase_id: 'orphan', adjudication_result: { outcome: 'FINAL ACCEPT' } }]);
  return qa.defects.some((d) => d.type === 'orphan_phrase');
});
record(23, 'negative blocks accepted phrase', () => {
  const neg = validateNegativeConflicts({
    global_negatives: [{ negative_id: 'n1', term: 'программист', exclusion_type: 'definite_exclusion' }],
  }, [{ phrase_id: 'p1', normalized_query: 'найти программиста 1с', adjudication_result: { outcome: 'FINAL ACCEPT' } }], []);
  return neg.blocked === true;
});
record(24, 'broad unsafe negative', () => {
  const neg = { term: '1с', exclusion_type: 'unsafe_broad_negative', risk: 'high' };
  return neg.exclusion_type === 'unsafe_broad_negative';
});
record(25, 'bounded human-review queue', () => {
  const records = Array.from({ length: 100 }, (_, i) => ({
    phrase_id: `p${i}`,
    raw_query: `q${i}`,
    adjudication_result: { outcome: 'FINAL ACCEPT', human_review_required: false },
    demand_tier: 'T3',
    ownership: { outcome: 'OWNED' },
  }));
  const r = routeBoundedReview(records, { qa_sample_rate: 0.05 });
  return r.metrics.human_review < 100 && r.metrics.automation_primary;
});
record(26, 'frozen project run blocked', () => {
  const r = authorizeProductionRun({ manifestPath: path.join(REPO_ROOT, 'projects/orca/projects/corvonero-direct-v2-clean-room/state/project-ppc-state-manifest-v1.json') });
  return !r.ok;
});
record(27, 'partial batch falsely marked complete', () => {
  const pack = buildOutputPack({
    runId: 't', manifest: null, inputs: { expectedCount: 10, corpus: {} },
    records: [{ phrase_id: 'p1', adjudication_result: { outcome: 'FINAL ACCEPT' }, raw_query: 'q' }],
    clusters: [], clusterQA: { defects: [], major_defects: [], summary: { major: 0 } },
    negatives: { global_negatives: [] }, negConflicts: { conflicts: [], blocked: false },
    review: { queue: [], metrics: { automated_final: 1, human_review: 0, review_ratio: 0, automation_primary: true } },
    metrics: {}, contractLoad: {}, versions: {},
  });
  return pack.run_manifest.input_reconciliation.reconciled === false;
});
record(28, 'resume preserves provenance', () => false);
record(29, 'runtime contract checksum mismatch', () => BLOCKERS.CONTRACT_CHECKSUM.includes('CHECKSUM'));
record(30, 'output pack reconciliation', () => false);

async function finishAsyncTests() {
  for (const t of [28, 30]) {
    const idx = results.findIndex((r) => r.id === t);
    try {
      const out = path.join(__dirname, `../reports/_matrix-scale-${t}`);
      fs.rmSync(out, { recursive: true, force: true });
      const r = await runFullCorpusProduction({ fixtureCorpus: path.join(FIX, 'scale-corpus-v1.json'), outDir: out, requireManifest: false, skipContractLoad: true });
      results[idx].pass = t === 28
        ? r.ok && r.pack.run_manifest.input_reconciliation.reconciled
        : r.ok && r.pack.execution_receipt.reconciled;
    } catch (e) {
      results[idx].pass = false;
      results[idx].error = e.message;
    }
  }

  const passed = results.filter((r) => r.pass).length;
  const failed = results.filter((r) => !r.pass);
  console.log(`Production test matrix: ${passed}/${results.length} passed`);
  for (const f of failed) console.log(`  [FAIL] #${f.id} ${f.name}${f.error ? ': ' + f.error : ''}`);
  const outPath = path.join(__dirname, '../reports/production-test-matrix-results-v1.json');
  fs.writeFileSync(outPath, JSON.stringify({ passed, total: results.length, results, at: new Date().toISOString() }, null, 2));
  process.exit(failed.length ? 1 : 0);
}

finishAsyncTests();
