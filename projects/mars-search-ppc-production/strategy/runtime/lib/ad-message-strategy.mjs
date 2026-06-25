/**
 * Ad message strategy principles — Wave 4
 */

export function buildAdMessageStrategy(pack, architecture) {
  const directions = [];

  for (const campaign of architecture.campaigns) {
    const service = (pack.service_ownership?.services || []).find((s) => s.service_id === campaign.service_direction);
    directions.push({
      service_id: campaign.service_direction,
      campaign_id: campaign.campaign_id,
      user_task: service?.user_task || 'SAFE UNKNOWN — derive from service registry',
      commercial_promise: service?.value_proposition || 'SAFE UNKNOWN',
      proof_requirements: service?.proof_requirements || ['case_study', 'certification'],
      cta: service?.primary_cta || 'request_consultation',
      geography_wording: pack.geography ? `explicit_geo:${pack.geography}` : 'national_neutral',
      price_wording_policy: 'no_unverified_price_claims',
      urgency_wording_policy: service?.urgency_allowed ? 'conditional' : 'prohibited_unless_evidence',
      prohibited_claims: ['unverified_competitor_facts', 'guaranteed_results', 'invented_discounts'],
      landing_consistency_required: true,
      evidence_support: [service?.service_id].filter(Boolean).map((id) => `service_ownership:${id}`),
      examples_marked_non_final: true,
    });
  }

  return {
    ad_message_strategy_id: `ams-${pack.project_identity?.project_id || 'unknown'}-v1`,
    directions,
    final_ads_authority: false,
  };
}
