/**
 * Independent strategy reviewer — Wave 4.1
 * Does NOT receive evaluation constraints or expected answers.
 */
import { runStrategyInvariants } from './strategy-invariants.mjs';

export function reviewStrategy({ pack, strategy, context = {} }) {
  const invariants = runStrategyInvariants(strategy, pack, context);
  const riskFlags = [];
  const missingBlockers = [];
  const inventedClaims = [];
  const notes = { groundedness: [], consistency: [], campaign_logic: [] };

  if (!strategy.supporting_evidence_ids?.length && pack.pack_readiness === 'COMPLETE') {
    riskFlags.push('no_evidence_linkage');
    notes.groundedness.push('Strategy lacks supporting evidence IDs on complete pack');
  }

  const packBlockers = (pack.blockers || []).map((b) => (typeof b === 'string' ? b : b.code || String(b)));
  const stratBlockerText = JSON.stringify(strategy.blockers || []);
  for (const pb of packBlockers) {
    if (!stratBlockerText.includes(pb.slice(0, 20))) {
      missingBlockers.push(pb);
    }
  }

  if (strategy.budget_framework?.total_monthly_budget && pack.business_authority?.monthly_budget == null) {
    inventedClaims.push('monthly_budget');
    riskFlags.push('budget_invention');
  }

  const campaigns = strategy.campaign_segmentation?.campaigns || [];
  if (campaigns.length > 12) {
    notes.campaign_logic.push('High campaign count — verify segmentation rationale');
  }
  if (campaigns.length === 1 && (pack.service_ownership?.services || []).length > 2) {
    notes.campaign_logic.push('Possible under-segmentation for multi-service pack');
  }

  let biddingFit = 'PASS';
  if (invariants.critical_failures.includes('tracking_blocks_auto_bidding') || invariants.critical_failures.includes('no_auto_bidding_without_conversions')) {
    biddingFit = 'FAIL';
  } else if (strategy.bidding_approach?.primary_strategy === 'manual' && !strategy.bidding_approach?.operating_policy) {
    biddingFit = 'WARN';
  }

  let budgetHonesty = inventedClaims.includes('monthly_budget') ? 'FAIL' : 'PASS';
  if (pack.business_authority?.monthly_budget == null && !strategy.operator_decisions_required?.includes('monthly_budget')) {
    budgetHonesty = 'WARN';
  }

  let landingFit = 'PASS';
  const landingGaps = strategy.landing_requirements?.results?.filter((r) => r.outcome === 'LANDING GAP') || [];
  if (landingGaps.length && !strategy.blockers?.some((b) => (b.code || b).includes('LANDING'))) {
    landingFit = 'FAIL';
  }

  let measurementFit = 'PASS';
  if (strategy.measurement_requirements?.blockers?.length && strategy.bidding_approach?.primary_strategy === 'automated_conversion') {
    measurementFit = 'FAIL';
  }

  const hasCritical = invariants.critical_failures.length > 0 || inventedClaims.length > 0 || missingBlockers.some((b) => /PAID SERP/i.test(b));
  const hasWarn = riskFlags.length > 0 || biddingFit === 'WARN' || budgetHonesty === 'WARN' || notes.campaign_logic.length > 0;

  let verdict = 'PASS';
  if (hasCritical) verdict = inventedClaims.length ? 'INVALID' : 'REPAIR REQUIRED';
  else if (hasWarn) verdict = 'PASS WITH WARNINGS';

  const repairRecommendations = [];
  if (missingBlockers.length) repairRecommendations.push('Preserve pack blockers in strategy output');
  if (inventedClaims.length) repairRecommendations.push('Remove invented budget/conversion claims');
  if (biddingFit === 'FAIL') repairRecommendations.push('Align bidding with tracking and conversion maturity');

  return {
    verdict,
    groundedness: { score: inventedClaims.length ? 0 : (missingBlockers.length ? 0.7 : 1), notes: notes.groundedness },
    internal_consistency: { score: invariants.pass_rate, notes: notes.consistency },
    campaign_logic: { score: notes.campaign_logic.length ? 0.8 : 1, notes: notes.campaign_logic },
    risk_flags: riskFlags,
    missing_blockers: missingBlockers,
    invented_claims: inventedClaims,
    bidding_fit: biddingFit,
    budget_honesty: budgetHonesty,
    landing_fit: landingFit,
    measurement_fit: measurementFit,
    repair_recommendations: repairRecommendations,
    invariants,
  };
}
