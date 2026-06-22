/**
 * Bounded human review — only escalations, conflicts, QA sample.
 * Does NOT receive whole corpus, routine ACCEPT/REJECT, or pre-reassessment ABSTAIN.
 */
import crypto from 'node:crypto';

export function routeBoundedReview(records, config = {}) {
  const queue = [];
  const metrics = {
    total_corpus: records.length,
    automated_final: 0,
    human_review: 0,
    reason_families: {},
    protected_classes: {},
    high_value_conflicts: 0,
  };

  const qaSampleRate = config.qa_sample_rate ?? 0.02;
  const qaSeed = config.qa_seed || 'wave3-qa';

  for (const rec of records) {
    const adj = rec.adjudication_result || {};
    const routes = [];

    if (adj.outcome === 'ESCALATE POLICY CONFLICT') routes.push('POLICY_CONFLICT');
    if (adj.outcome === 'ESCALATE DOMAIN CONFLICT') routes.push('DOMAIN_CONFLICT');
    if (adj.outcome === 'INVALID RECORD') routes.push('INVALID_RECORD');
    if (adj.human_review_required && routes.length) routes.push('ADJUDICATION_ESCALATION');

    if (rec.demand_tier === 'T1' && adj.outcome === 'FINAL ACCEPT' && rec.ownership?.outcome === 'OWNERSHIP CONFLICT') {
      routes.push('HIGH_VALUE_OWNERSHIP_CONFLICT');
      metrics.high_value_conflicts += 1;
    }

    if (deterministicQaBucket(rec.phrase_id, qaSeed) < qaSampleRate && adj.outcome?.startsWith('FINAL')) {
      routes.push('BOUNDED_QA_SAMPLE');
    }

    if (routes.length) {
      metrics.human_review += 1;
      for (const r of routes) metrics.reason_families[r] = (metrics.reason_families[r] || 0) + 1;
      if (rec.protected_intent_class) {
        metrics.protected_classes[rec.protected_intent_class] = (metrics.protected_classes[rec.protected_intent_class] || 0) + 1;
      }
      queue.push({
        phrase_id: rec.phrase_id,
        raw_query: rec.raw_query,
        routes,
        adjudication_outcome: adj.outcome,
        automated_decision: adj.final_decision,
        created_at: new Date().toISOString(),
      });
    } else {
      metrics.automated_final += 1;
    }
  }

  metrics.review_ratio = metrics.total_corpus ? metrics.human_review / metrics.total_corpus : 0;
  metrics.automation_primary = metrics.automated_final > metrics.human_review;

  return { queue, metrics };
}

function deterministicQaBucket(phraseId, seed) {
  const h = crypto.createHash('sha256').update(`${seed}:${phraseId}`).digest();
  return h[0] / 255;
}
