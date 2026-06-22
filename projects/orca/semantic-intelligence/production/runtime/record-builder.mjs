import { createAssessorContext } from '../assessors/assessor-contract.mjs';
import { assessDeterministic } from '../assessors/deterministic-assessor.mjs';
import { applyHardRules } from '../assessors/hard-rules.mjs';
import { needsReassessment, runReassessment } from '../adjudication/reassessment.mjs';
import { adjudicate } from '../adjudication/adjudicator.mjs';
import { assignDemandTier } from '../tiers/demand-tier-assigner.mjs';
import { stablePhraseId, PRODUCTION_VERSION } from './lib.mjs';

export function buildProductionRecord(phrase, context, versions) {
  const now = new Date().toISOString();
  const assessorCtx = createAssessorContext(phrase, {
    businessScope: context.businessScope,
    serviceRegistry: context.serviceRegistry,
    geography: phrase.region,
    commercialPolicy: context.commercialPolicy || {},
  });

  const primary = assessDeterministic(assessorCtx);
  const hardRules = applyHardRules(phrase, primary);

  let reassessment = null;
  if (needsReassessment(primary, hardRules)) {
    reassessment = runReassessment(phrase, context, primary);
  }

  const adjudication = adjudicate({
    primary,
    reassessment,
    hardRules,
    invariantResults: [],
    businessScope: context.businessScope,
  });

  const record = {
    phrase_id: phrase.phrase_id || stablePhraseId(phrase.normalized_query),
    raw_query: phrase.raw_query,
    normalized_query: phrase.normalized_query,
    source_ids: phrase.source_ids || [],
    frequencies: phrase.frequencies || {},
    region: phrase.region,
    collection_period: phrase.collection_period,
    business_scope_version: versions.business_scope_version || 'v1',
    service_registry_version: versions.service_registry_version || 'v1',
    assessor_version: primary.assessor_version,
    policy_version: versions.policy_version || 'v1',
    primary_intent: primary.primary_intent,
    secondary_intent: primary.secondary_intent,
    commercial_eligibility: adjudication.outcome === 'FINAL ACCEPT',
    commercial_evidence: primary.commercial_evidence,
    non_commercial_evidence: primary.non_commercial_evidence,
    protected_intent_class: primary.protected_intent_class,
    likely_next_user_action: primary.likely_next_user_action,
    provider_hire_likelihood: primary.provider_hire_likelihood,
    diy_likelihood: primary.diy_likelihood,
    career_likelihood: primary.career_likelihood,
    education_likelihood: primary.education_likelihood,
    navigation_likelihood: primary.navigation_likelihood,
    product_only_likelihood: primary.product_only_likelihood,
    ambiguity_class: primary.ambiguity_class,
    confidence: adjudication.final_confidence,
    decision: adjudication.final_decision,
    rationale: primary.rationale,
    alternative_interpretation: reassessment?.alternative_interpretations_tested?.[0]?.interpretation?.label || primary.alternative_interpretation,
    invariant_results: [],
    reassessment_result: reassessment,
    adjudication_result: adjudication,
    final_authority: adjudication.outcome,
    output_class: 'PRODUCTION_SEMANTIC_RECORD',
    review_requirement: adjudication.human_review_required ? 'HUMAN_REVIEW' : 'AUTOMATED_FINAL',
    demand_tier: null,
    ownership: null,
    cluster_id: null,
    primary_assessment: primary,
    hard_rules: hardRules,
    timestamps: { created_at: now, assessed_at: now },
  };

  if (adjudication.outcome === 'FINAL ACCEPT') {
    record.demand_tier = assignDemandTier(record);
  }

  return record;
}

export { PRODUCTION_VERSION };
