/**
 * Budget framework — Wave 4
 */

export function buildBudgetFramework(businessAuthority, activationPolicy, options = {}) {
  const monthly = businessAuthority?.monthly_budget || businessAuthority?.budget?.monthly_total;

  if (!monthly && !options.budgetDeclared) {
    return {
      status: 'BUDGET DECISION REQUIRED',
      blockers: ['BUDGET DECISION REQUIRED'],
      provisional: true,
      framework: null,
    };
  }

  if (options.inventBudget) {
    return {
      status: 'BLOCKED',
      blockers: ['BLOCKED — BUDGET INVENTED NOT PERMITTED'],
      provisional: false,
      framework: null,
    };
  }

  const total = Number(monthly);
  const t5Cap = Math.round(total * 0.05);
  const testBudget = Math.round(total * 0.1);
  const protectedReserve = Math.round(total * 0.15);
  const learningReserve = Math.round(total * 0.1);

  return {
    status: 'APPROVED',
    blockers: [],
    provisional: false,
    framework: {
      total_monthly_budget: total,
      test_budget: testBudget,
      t1_t2_priority_share: 0.6,
      t3_t4_allocation_share: 0.2,
      t5_experimental_cap: t5Cap,
      geographic_allocation: options.geoAllocation || 'proportional_to_demand',
      protected_reserve: protectedReserve,
      learning_period_reserve: learningReserve,
      stop_loss: { enabled: true, threshold_pct: 0.2 },
      expansion_gate: 'operator_approval_required',
    },
  };
}
