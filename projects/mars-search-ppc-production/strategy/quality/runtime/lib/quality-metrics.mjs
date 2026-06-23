/**
 * Quality metrics aggregator — Wave 4.1
 */
export function aggregateQualityMetrics(runResults) {
  const n = runResults.length || 1;
  const schemaValid = runResults.filter((r) => r.schema_valid).length / n;
  const invariantPass = runResults.filter((r) => r.invariants?.critical_failures?.length === 0).length / n;
  const evidenceLink = runResults.filter((r) => (r.strategy?.supporting_evidence_ids || []).length > 0).length / n;
  const fabricated = runResults.filter((r) => r.reviewer?.invented_claims?.length > 0).length;
  const missingBlocker = runResults.filter((r) => r.reviewer?.missing_blockers?.length > 0).length;
  const falseBlocker = runResults.filter((r) => r.false_blocker).length;
  const landingAlign = runResults.filter((r) => r.reviewer?.landing_fit === 'PASS').length / n;
  const biddingMaturity = runResults.filter((r) => r.reviewer?.bidding_fit === 'PASS').length / n;
  const budgetHonesty = runResults.filter((r) => r.reviewer?.budget_honesty === 'PASS').length / n;
  const tierPolicy = runResults.filter((r) => r.invariants?.results?.find((i) => i.id === 't5_isolated')?.pass).length / n;
  const archCoherence = runResults.filter((r) => r.reviewer?.campaign_logic?.score >= 0.8).length / n;

  const reviewerVerdicts = {};
  for (const r of runResults) {
    const v = r.reviewer?.verdict || 'UNKNOWN';
    reviewerVerdicts[v] = (reviewerVerdicts[v] || 0) + 1;
  }

  const stabilityContradictions = runResults.filter((r) => r.stability === 'material_contradiction').length;
  const operatorDecisions = runResults.reduce((s, r) => s + (r.strategy?.operator_decisions_required?.length || 0), 0) / n;
  const totalCost = runResults.reduce((s, r) => s + (r.cost_usd || 0), 0);

  const criticalGates = {
    fabricated_production_facts: fabricated,
    invented_budget_authority: runResults.filter((r) => r.reviewer?.invented_claims?.includes('monthly_budget')).length,
    hidden_critical_blockers: runResults.filter((r) => r.reviewer?.missing_blockers?.some((b) => /PAID SERP|TRACKING/i.test(b))).length,
    rejected_demand_activation: runResults.filter((r) => !r.invariants?.results?.find((i) => i.id === 'rejected_phrases_not_activated')?.pass).length,
    campaign_without_landing_or_blocker: runResults.filter((r) => !r.invariants?.results?.find((i) => i.id === 'campaign_has_landing_or_blocker')?.pass).length,
    provisional_marked_production: runResults.filter((r) => !r.invariants?.results?.find((i) => i.id === 'provisional_not_production')?.pass).length,
  };

  const targetGates = {
    schema_valid_rate: schemaValid,
    evidence_link_validity: evidenceLink,
    critical_invariant_pass_rate: invariantPass,
    material_stability_contradiction_rate: stabilityContradictions / Math.max(1, runResults.filter((r) => r.stability).length),
  };

  const allCriticalPass = Object.values(criticalGates).every((v) => v === 0);

  return {
    case_count: n,
    schema_valid_rate: schemaValid,
    invariant_pass_rate: invariantPass,
    evidence_link_rate: evidenceLink,
    fabricated_fact_rate: fabricated / n,
    missing_blocker_rate: missingBlocker / n,
    false_blocker_rate: falseBlocker / n,
    landing_alignment_pass_rate: landingAlign,
    bidding_maturity_pass_rate: biddingMaturity,
    budget_honesty_pass_rate: budgetHonesty,
    tier_policy_pass_rate: tierPolicy,
    architecture_coherence_rate: archCoherence,
    reviewer_verdicts: reviewerVerdicts,
    stability_contradiction_rate: targetGates.material_stability_contradiction_rate,
    operator_decision_burden: operatorDecisions,
    average_cost_usd: totalCost / n,
    total_cost_usd: totalCost,
    critical_gates: criticalGates,
    target_gates: targetGates,
    all_critical_gates_pass: allCriticalPass,
    maturity_verdict: allCriticalPass && targetGates.critical_invariant_pass_rate >= 1.0
      ? 'AI PPC STRATEGIST QUALITY VALIDATED — OPERATOR REVIEW REQUIRED'
      : (runResults.some((r) => r.provider_failure) ? 'WAVE 4.1 — BLOCKED — INSUFFICIENT VALID EVIDENCE OR PROVIDER FAILURE' : 'WAVE 4.1 — STRATEGIST QUALITY REPAIR REQUIRED'),
  };
}

export function buildOperatorReviewPackage(runResults, constraintsMap) {
  const conflicts = [];
  for (const r of runResults) {
    const c = constraintsMap[r.case_id];
    if (!c) continue;
    if (r.reviewer?.verdict === 'REPAIR REQUIRED' || r.reviewer?.verdict === 'INVALID') {
      conflicts.push({
        case_id: r.case_id,
        scenario: r.scenario,
        verdict: r.reviewer.verdict,
        issues: [...(r.reviewer.invented_claims || []), ...(r.reviewer.missing_blockers || [])],
        campaign_count: r.strategy?.campaign_segmentation?.campaigns?.length,
        bidding: r.strategy?.bidding_approach?.primary_strategy,
        operator_decisions: r.strategy?.operator_decisions_required,
      });
    }
    if (r.stability === 'material_contradiction') {
      conflicts.push({ case_id: r.case_id, type: 'stability_contradiction', scenario: r.scenario });
    }
  }
  return {
    material_contradictions: conflicts.filter((c) => c.type === 'stability_contradiction'),
    repair_required: conflicts.filter((c) => c.verdict),
    total_conflicts: conflicts.length,
    cases_requiring_operator_policy: conflicts.filter((c) => c.operator_decisions?.length > 3),
  };
}
