/**
 * AI PPC Strategist contract — Wave 4 SPPC-13
 */
import { deriveStrategicObjective } from './strategic-objective-engine.mjs';
import { buildDemandActivationPolicy } from './demand-activation-policy.mjs';
import { recommendCampaignArchitecture } from './campaign-architecture.mjs';
import { recommendKeywordNegativeDistribution } from './keyword-negative-policy.mjs';
import { buildAdMessageStrategy } from './ad-message-strategy.mjs';
import { assessLandingOfferAlignment } from './landing-offer-alignment.mjs';
import { recommendBiddingFramework } from './bidding-framework.mjs';
import { buildBudgetFramework } from './budget-framework.mjs';
import { buildMeasurementContract } from './measurement-contract.mjs';
import { collectStrategyBlockers } from './strategy-blocker-engine.mjs';
import { wrapProvisionalStrategy, isProvisionalAllowed } from './provisional-strategy.mjs';
import crypto from 'node:crypto';

const BLIND_FORBIDDEN_KEYS = [
  'expected_campaign_architecture',
  'commander_export',
  'answer_key',
  'historical_output_as_authority',
];

export function buildSearchPpcStrategy(params) {
  const {
    analyticalPack,
    businessAuthority,
    operatorConstraints = {},
    campaignPlatform = 'Yandex Direct',
    strategyPolicy = {},
    modelOutput = null,
  } = params;

  for (const key of BLIND_FORBIDDEN_KEYS) {
    if (params[key] || analyticalPack?.[key]) {
      return { ok: false, blocker: `BLOCKED — BLIND AUTHORITY VIOLATION: ${key}`, exit_code: 2 };
    }
  }

  if (!analyticalPack?.pack_id) {
    return { ok: false, blocker: 'BLOCKED — ANALYTICAL PACK MISSING', exit_code: 2 };
  }

  const pack = analyticalPack;
  const readiness = pack.readiness_assessment || pack.pack_readiness;
  const objective = deriveStrategicObjective(businessAuthority || pack.business_authority);
  const activationPolicy = buildDemandActivationPolicy(pack.tier_distribution, {
    launchMode: operatorConstraints.launchMode,
    projectId: pack.project_identity?.project_id,
    t5MixedIntoMain: strategyPolicy.t5MixedIntoMain,
  });
  const architecture = recommendCampaignArchitecture(pack, activationPolicy, operatorConstraints);
  const keywordPolicy = recommendKeywordNegativeDistribution(pack, architecture);
  const measurement = buildMeasurementContract(pack, { trackingStatus: operatorConstraints.trackingStatus });
  const alignment = assessLandingOfferAlignment(pack, architecture, measurement);
  const bidding = recommendBiddingFramework(pack, architecture, measurement, strategyPolicy);
  const budget = buildBudgetFramework(businessAuthority || pack.business_authority, activationPolicy, strategyPolicy);
  const adMessage = buildAdMessageStrategy(pack, architecture);

  const provisional = isProvisionalAllowed(readiness) || strategyPolicy.forceProvisional;
  let strategyStatus = readiness?.readiness === 'COMPLETE' || readiness?.readiness === 'COMPLETE WITH APPROVED DEGRADATION'
    ? 'STRATEGY DRAFT — OPERATOR REVIEW REQUIRED'
    : 'PROVISIONAL STRATEGY DRAFT';

  const blockers = collectStrategyBlockers({
    pack,
    readiness,
    architecture,
    alignment,
    measurement,
    budget,
    keywordPolicy,
    provisionalMode: provisional,
    claimsProduction: strategyPolicy.claimsProduction,
  });

  if (blockers.production_blocked && !provisional) {
    strategyStatus = 'BLOCKED';
  }

  const strategy = {
    strategy_id: `sps-${pack.project_identity?.project_id}-${Date.now()}`,
    version: '1.0.0',
    project: pack.project_identity,
    analysis_period: pack.analysis_period,
    strategy_status: strategyStatus,
    strategic_objective: objective.objective,
    primary_conversion: businessAuthority?.primary_conversion || pack.business_authority?.primary_conversion || null,
    secondary_conversions: businessAuthority?.secondary_conversions || [],
    demand_priorities: pack.tier_distribution,
    tier_activation_policy: activationPolicy,
    services_directions: pack.service_ownership,
    campaign_segmentation: architecture,
    geography: pack.geography,
    schedule: operatorConstraints.schedule || 'default',
    devices: operatorConstraints.devices || ['desktop', 'mobile'],
    audience_constraints: operatorConstraints.audience || [],
    keyword_activation_policy: keywordPolicy,
    negative_strategy: { global: keywordPolicy.global_negatives, conflicts: keywordPolicy.conflict_status },
    ad_message_principles: adMessage,
    offer_requirements: pack.offer_inventory,
    landing_requirements: alignment,
    bidding_approach: bidding,
    budget_framework: budget.framework || budget,
    measurement_requirements: measurement,
    experiment_policy: { t5_isolated: true, operator_approval: true },
    exclusions: operatorConstraints.exclusions || [],
    blockers: blockers.blockers,
    assumptions: objective.assumption ? [{ text: 'Strategic objective derived conservatively', type: 'objective_derivation' }] : [],
    operator_decisions_required: collectOperatorDecisions(budget, measurement, blockers),
    supporting_evidence_ids: pack.evidence_inventory?.map((e) => e.artifact_id) || [],
    model_enrichment: modelOutput ? sanitizeModelOutput(modelOutput) : null,
  };

  const finalStrategy = provisional ? wrapProvisionalStrategy(strategy, pack, blockers.blockers) : strategy;

  return {
    ok: strategyStatus !== 'BLOCKED' || provisional,
    strategy: finalStrategy,
    blockers,
    exit_code: blockers.production_blocked && !provisional ? 2 : 0,
    receipt: {
      receipt_id: `sppc-receipt-strategy-${crypto.randomBytes(4).toString('hex')}`,
      stage: 'SPPC-13',
      strategy_id: strategy.strategy_id,
      status: finalStrategy.strategy_status,
      generated_at: new Date().toISOString(),
    },
  };
}

function collectOperatorDecisions(budget, measurement, blockers) {
  const decisions = [];
  if (budget.status === 'BUDGET DECISION REQUIRED') decisions.push('monthly_budget');
  if (measurement.blocks_strategy_activation) decisions.push('tracking_setup');
  if (blockers.blocker_count) decisions.push('resolve_blockers');
  return decisions;
}

function sanitizeModelOutput(output) {
  const forbidden = ['commander', 'exact_bid', 'invented_competitor'];
  const text = JSON.stringify(output);
  for (const f of forbidden) {
    if (text.toLowerCase().includes(f) && output.invented) return null;
  }
  return output;
}
