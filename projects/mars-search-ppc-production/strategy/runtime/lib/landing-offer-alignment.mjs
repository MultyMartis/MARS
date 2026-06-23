/**
 * Landing and offer alignment — Wave 4
 */

export const ALIGNMENT_OUTCOMES = [
  'ALIGNED',
  'ALIGNMENT REPAIR REQUIRED',
  'LANDING GAP',
  'OFFER GAP',
  'TRACKING GAP',
  'BLOCKED',
];

export function assessLandingOfferAlignment(pack, architecture, measurement) {
  const results = [];
  const landings = pack.landing_inventory?.pages || pack.landing_inventory?.landings || [];
  const offers = pack.offer_inventory?.offers || [];

  for (const campaign of architecture.campaigns) {
    const landing = landings.find((l) => l.service_id === campaign.service_direction);
    const offer = offers.find((o) => o.service_id === campaign.service_direction);
    const checks = {
      service_fit: landing?.service_id === campaign.service_direction,
      geo_fit: !pack.geography || landing?.geo?.includes(pack.geography) || landing?.geo === 'all',
      offer_fit: !!offer,
      conversion_availability: measurement?.goals?.length > 0,
      pricing_consistency: offer?.pricing_declared !== false,
      proof_trust: landing?.trust_signals?.length > 0,
      cta: !!landing?.cta,
      mobile_readiness: landing?.mobile_ready !== false,
      page_availability: landing?.status === 'available',
      tracking_readiness: measurement?.metrica_counter?.status === 'active',
    };

    let outcome = 'ALIGNED';
    if (!landing) outcome = 'LANDING GAP';
    else if (!offer) outcome = 'OFFER GAP';
    else if (!checks.tracking_readiness) outcome = 'TRACKING GAP';
    else if (Object.values(checks).some((v) => v === false)) outcome = 'ALIGNMENT REPAIR REQUIRED';

    results.push({
      campaign_id: campaign.campaign_id,
      service_id: campaign.service_direction,
      outcome,
      checks,
      blocks_activation: ['LANDING GAP', 'OFFER GAP', 'TRACKING GAP', 'BLOCKED'].includes(outcome),
    });
  }

  return {
    alignment_id: `align-${pack.project_identity?.project_id || 'unknown'}-v1`,
    results,
    any_blocked: results.some((r) => r.blocks_activation),
  };
}
