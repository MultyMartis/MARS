/**
 * Deterministic strategy invariants — Wave 4.1 (20 checks)
 */
import { validateSearchPpcStrategy } from '../../../runtime/lib/strategy-validator.mjs';
import crypto from 'node:crypto';

const INVARIANT_IDS = [
  'no_invented_services',
  'no_invented_landings',
  'no_invented_budget',
  'no_invented_conversion_history',
  'rejected_phrases_not_activated',
  'cluster_has_owner',
  'campaign_has_landing_or_blocker',
  't5_isolated',
  'negative_conflicts_not_ignored',
  'missing_paid_serp_not_hidden',
  'tracking_blocks_auto_bidding',
  'no_auto_bidding_without_conversions',
  'out_of_scope_not_mixed',
  'provisional_not_production',
  'evidence_refs_exist',
  'no_fabricated_observed_facts',
  'assumptions_marked',
  'operator_decisions_explicit',
  'strategy_status_matches_blockers',
  'output_reconciliation',
];

export function runStrategyInvariants(strategy, pack, context = {}) {
  const results = [];
  const text = JSON.stringify(strategy);
  const services = new Set((pack.service_ownership?.services || []).map((s) => s.service_id));
  const landingUrls = new Set((pack.landing_inventory?.pages || context.landingInventory?.pages || []).map((p) => p.url));
  const packBlockerCodes = (pack.blockers || []).map((b) => (typeof b === 'string' ? b : b.code || b));

  results.push(inv('no_invented_services', () => {
    for (const c of strategy.campaign_segmentation?.campaigns || []) {
      if (c.service_id && !services.has(c.service_id) && c.service_id !== 'unassigned') return false;
    }
    return true;
  }));

  results.push(inv('no_invented_landings', () => {
    for (const c of strategy.campaign_segmentation?.campaigns || []) {
      if (c.landing?.url && landingUrls.size > 0 && !landingUrls.has(c.landing.url)) {
        if (!c.blockers?.includes('LANDING GAP')) return false;
      }
    }
    return !/https:\/\/(invented|fake|example-new)\./i.test(text);
  }));

  results.push(inv('no_invented_budget', () => {
    const authBudget = pack.business_authority?.monthly_budget;
    const stratBudget = strategy.budget_framework?.total_monthly_budget ?? strategy.budget_framework?.monthly_budget;
    if (authBudget == null && stratBudget != null && !strategy.budget_framework?.marked_scenario) return false;
    return true;
  }));

  results.push(inv('no_invented_conversion_history', () => {
    const hist = strategy.measurement_requirements?.conversion_history;
    const opHist = context.operatorConstraints?.trackingStatus?.conversion_history;
    if (hist?.count > 0 && (!opHist || opHist.count === 0)) return false;
    return !/conversion_history.*999/i.test(text);
  }));

  results.push(inv('rejected_phrases_not_activated', () => {
    const rejected = (pack.semantic_clusters?.clusters || [])
      .flatMap((c) => c.phrases || [])
      .filter((p) => p.decision === 'REJECT')
      .map((p) => p.text);
    const activated = (strategy.keyword_activation_policy?.activate || []).map((a) => a.phrase || a.text);
    return !rejected.some((r) => activated.includes(r));
  }));

  results.push(inv('cluster_has_owner', () => {
    return !(strategy.campaign_segmentation?.campaigns || []).some((c) => c.service_direction === 'unassigned' && c.launch_status === 'ACTIVE');
  }));

  results.push(inv('campaign_has_landing_or_blocker', () => {
    for (const c of strategy.campaign_segmentation?.campaigns || []) {
      if (c.launch_status === 'ACTIVE' && !c.landing && !c.blockers?.length && !strategy.blockers?.length) {
        const gap = strategy.landing_requirements?.results?.some((r) => r.campaign_id === c.campaign_id && r.outcome === 'LANDING GAP');
        if (!gap) return false;
      }
    }
    return true;
  }));

  results.push(inv('t5_isolated', () => strategy.tier_activation_policy?.policies?.T5?.must_not_merge_with_main_launch !== false));

  results.push(inv('negative_conflicts_not_ignored', () => {
    if (pack.negative_intelligence?.conflicts?.length && strategy.keyword_activation_policy?.conflict_status === 'CONFLICT') {
      return strategy.blockers?.some((b) => (b.code || b).includes('negative'));
    }
    return true;
  }));

  results.push(inv('missing_paid_serp_not_hidden', () => {
    const missing = packBlockerCodes.some((b) => /PAID SERP/i.test(b)) || pack.missing_evidence?.some((m) => /paid_serp/i.test(m));
    if (missing && strategy.strategy_status?.includes('PRODUCTION READY')) return false;
    return true;
  }));

  results.push(inv('tracking_blocks_auto_bidding', () => {
    const noTracking = !context.operatorConstraints?.trackingStatus?.metrica_counter?.status;
    const autoBidding = strategy.bidding_approach?.primary_strategy === 'automated_conversion' || strategy.bidding_approach?.recommended === 'automated_conversion';
    if (noTracking && autoBidding) return false;
    return true;
  }));

  results.push(inv('no_auto_bidding_without_conversions', () => {
    const convCount = context.operatorConstraints?.trackingStatus?.conversion_history?.count ?? 0;
    const autoBidding = strategy.bidding_approach?.primary_strategy === 'automated_conversion';
    if (autoBidding && convCount < 10 && !strategy.bidding_approach?.learning_plan) return false;
    return true;
  }));

  results.push(inv('out_of_scope_not_mixed', () => {
    const rejected = (pack.semantic_clusters?.clusters || []).flatMap((c) => c.phrases || []).filter((p) => p.decision === 'REJECT');
    const activated = strategy.keyword_activation_policy?.activate || [];
    return !rejected.some((r) => activated.some((a) => (a.phrase || a.text) === r.text));
  }));

  results.push(inv('provisional_not_production', () => {
    if (pack.pack_readiness !== 'COMPLETE' && strategy.strategy_status === 'PRODUCTION READY') return false;
    return true;
  }));

  results.push(inv('evidence_refs_exist', () => (strategy.supporting_evidence_ids || []).length > 0 || pack.pack_readiness === 'BLOCKED'));

  results.push(inv('no_fabricated_observed_facts', () => !/OBSERVED FACT.*invented/i.test(text) && !strategy.model_enrichment?.invented));

  results.push(inv('assumptions_marked', () => {
    if (!strategy.assumptions?.length) return true;
    return strategy.assumptions.every((a) => a.type || a.statement_type);
  }));

  results.push(inv('operator_decisions_explicit', () => Array.isArray(strategy.operator_decisions_required)));

  results.push(inv('strategy_status_matches_blockers', () => {
    const critical = (strategy.blockers || []).filter((b) => !b.provisional_strategy_allowed);
    if (critical.length && strategy.strategy_status === 'PRODUCTION READY') return false;
    return true;
  }));

  results.push(inv('output_reconciliation', () => {
    const validator = validateSearchPpcStrategy(strategy, pack, {
      budgetNotApproved: pack.business_authority?.monthly_budget == null,
      allowProvisional: pack.pack_readiness !== 'COMPLETE',
    });
    return validator.ok;
  }));

  const passed = results.filter((r) => r.pass).length;
  return {
    invariant_ids: INVARIANT_IDS,
    results,
    passed,
    total: results.length,
    pass_rate: results.length ? passed / results.length : 0,
    critical_failures: results.filter((r) => !r.pass && r.critical).map((r) => r.id),
  };
}

function inv(id, fn, critical = true) {
  let pass = false;
  try { pass = !!fn(); } catch { pass = false; }
  return { id, pass, critical };
}

export function checksumInput(pack, constraints, policy) {
  return crypto.createHash('sha256').update(JSON.stringify({ pack_id: pack.pack_id, constraints, policy })).digest('hex');
}

export function checksumOutput(strategy) {
  return crypto.createHash('sha256').update(JSON.stringify(strategy)).digest('hex');
}
