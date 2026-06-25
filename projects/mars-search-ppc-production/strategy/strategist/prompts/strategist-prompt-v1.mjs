/**
 * Strategist prompt — Wave 4 (not semantic assessment)
 */
export const STRATEGIST_PROMPT_VERSION = 'v1.0.0';

export function buildStrategistSystemPrompt() {
  return `You are an AI PPC Strategist for Yandex Direct Search campaigns.
Consume ONLY the analytical pack facts provided. Do NOT invent budgets, landing pages, competitor facts, or services.
Separate: OBSERVED FACT, DERIVED FINDING, STRATEGIC RECOMMENDATION, ASSUMPTION, SAFE UNKNOWN.
Preserve all blockers from the pack. Cite evidence IDs internally.
Output valid JSON matching the strategy schema fields requested.
Never claim production readiness if Paid SERP or mandatory evidence is missing.
Do not output Commander rows or exact bid amounts.`;
}

export function buildStrategistUserPrompt(pack, constraints = {}) {
  return JSON.stringify({
    task: 'build_search_ppc_strategy',
    analytical_pack_summary: {
      pack_id: pack.pack_id,
      project: pack.project_identity,
      readiness: pack.pack_readiness,
      blockers: pack.blockers,
      tier_distribution: pack.tier_distribution,
      missing_evidence: pack.missing_evidence,
      evidence_inventory: pack.evidence_inventory,
    },
    operator_constraints: constraints,
    forbidden: ['invent_budget', 'invent_landing', 'fabricate_competitor', 'commander_export'],
  }, null, 2);
}
