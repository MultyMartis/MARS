/**
 * Measurement contract — Wave 4
 */

export function buildMeasurementContract(pack, options = {}) {
  const tracking = options.trackingStatus || pack.tracking_status || {};
  const blockers = [];

  if (!tracking.metrica_counter || tracking.metrica_counter.status !== 'active') {
    blockers.push('BLOCKED — METRICA COUNTER MISSING');
  }
  if (!tracking.goals?.length) {
    blockers.push('BLOCKED — CONVERSION GOALS UNDEFINED');
  }

  return {
    contract_id: `meas-${pack.project_identity?.project_id || 'unknown'}-v1`,
    metrica_counter: tracking.metrica_counter || { status: 'unknown' },
    goals: tracking.goals || [],
    forms: tracking.forms || [],
    calls: tracking.calls || { enabled: false },
    messenger_conversions: tracking.messenger || null,
    utm_policy: tracking.utm_policy || 'required_on_all_paid',
    call_tracking_status: tracking.call_tracking || 'unknown',
    offline_conversion_readiness: tracking.offline_conversion || 'unknown',
    crm_status: tracking.crm || 'unknown',
    attribution_limitations: tracking.attribution_limitations || [],
    conversion_history: tracking.conversion_history || { count: 0 },
    blocks_strategy_activation: blockers.length > 0,
    blockers,
  };
}
