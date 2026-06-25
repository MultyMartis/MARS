/**
 * Strategic objective engine — Wave 4
 */

export const OBJECTIVE_TYPES = [
  'lead_generation',
  'direct_sale',
  'recurring_contract',
  'urgent_service',
  'consultation',
  'dealer_wholesale',
  'local_service',
  'remote_national_service',
];

export function deriveStrategicObjective(businessAuthority) {
  if (!businessAuthority) {
    return { objective: null, blocker: 'BLOCKED — BUSINESS AUTHORITY MISSING', source: 'SAFE UNKNOWN' };
  }
  const declared = businessAuthority.strategic_objective || businessAuthority.primary_objective;
  if (declared && OBJECTIVE_TYPES.includes(declared)) {
    return { objective: declared, source: 'operator_declared', evidence_ids: [businessAuthority.authority_id].filter(Boolean) };
  }
  const model = businessAuthority.business_model || '';
  const geo = businessAuthority.geography_scope || businessAuthority.geography;
  if (/dealer|wholesale|дилер|опт/i.test(model)) {
    return { objective: 'dealer_wholesale', source: 'derived_from_business_model', evidence_ids: [] };
  }
  if (/urgent|срочн|аварийн/i.test(model)) {
    return { objective: 'urgent_service', source: 'derived_from_business_model', evidence_ids: [] };
  }
  if (geo === 'local' || /локальн|город/i.test(String(geo))) {
    return { objective: 'local_service', source: 'derived_from_geography', evidence_ids: [] };
  }
  if (geo === 'national' || /вся россия|федеральн/i.test(String(geo))) {
    return { objective: 'remote_national_service', source: 'derived_from_geography', evidence_ids: [] };
  }
  return { objective: 'lead_generation', source: 'default_conservative', evidence_ids: [], assumption: true };
}
