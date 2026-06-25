/**
 * Provisional strategy mode — Wave 4
 */

export function wrapProvisionalStrategy(strategy, pack, blockers) {
  return {
    ...strategy,
    strategy_status: 'PROVISIONAL STRATEGY DRAFT',
    production_authority: false,
    commander_generation_allowed: false,
    launch_readiness: false,
    missing_evidence_prominent: pack.missing_evidence || [],
    stale_evidence: pack.stale_evidence || [],
    blockers,
    assumptions: [
      ...(strategy.assumptions || []),
      { text: 'Mandatory production evidence incomplete — draft for architecture testing only', type: 'provisional_mode' },
    ],
    budget_framework: strategy.budget_framework?.provisional
      ? { status: 'BUDGET DECISION REQUIRED', values_withheld: true }
      : strategy.budget_framework,
    bidding_approach: strategy.bidding_approach?.map?.((b) => ({ ...b, exact_bids: null })) || strategy.bidding_approach,
  };
}

export function isProvisionalAllowed(readiness) {
  return readiness?.provisional_allowed === true
    || readiness?.readiness === 'PARTIAL — PROVISIONAL ONLY';
}
