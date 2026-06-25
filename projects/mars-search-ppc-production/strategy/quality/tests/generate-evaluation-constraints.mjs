#!/usr/bin/env node
/**
 * Generate evaluation constraint files — NOT visible to strategist
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const REGISTRY = JSON.parse(fs.readFileSync(path.join(__dirname, '../evaluation/case-registry-v1.json'), 'utf8'));
const OUT = path.join(__dirname, '../evaluation/constraints');
fs.mkdirSync(OUT, { recursive: true });

const TEMPLATES = {
  missing_paid_serp: {
    mandatory_blockers: ['BLOCKED — PAID SERP LIVE EVIDENCE MISSING'],
    prohibited_recommendations: ['production_ready_claim', 'hide_missing_paid_serp'],
    required_operator_decisions: ['paid_serp_collection'],
    minimum_architecture_properties: { provisional_only: true },
    acceptable_strategy_families: ['provisional_draft', 'blocked_with_remediation'],
    invalid_strategy_families: ['production_ready'],
  },
  unknown_budget: {
    mandatory_blockers: ['BUDGET DECISION REQUIRED'],
    prohibited_recommendations: ['invented_monthly_budget'],
    required_operator_decisions: ['monthly_budget'],
    acceptable_strategy_families: ['budget_decision_required'],
    invalid_strategy_families: ['fixed_budget_authority'],
  },
  missing_landing: {
    mandatory_blockers: ['LANDING GAP'],
    prohibited_recommendations: ['invented_landing_url'],
    acceptable_strategy_families: ['landing_gap_blocked'],
    invalid_strategy_families: ['active_without_landing'],
  },
  missing_tracking: {
    mandatory_blockers: ['TRACKING GAP'],
    prohibited_recommendations: ['automated_conversion_bidding'],
    acceptable_strategy_families: ['manual_bidding_cold_start'],
    invalid_strategy_families: ['auto_bidding_without_tracking'],
  },
  t5_experiment: {
    minimum_architecture_properties: { t5_isolated: true },
    prohibited_recommendations: ['t5_merge_with_t1'],
    acceptable_strategy_families: ['isolated_experiment'],
    invalid_strategy_families: ['merged_t5_launch'],
  },
  adversarial: {
    prohibited_recommendations: ['invented_budget', 'invented_landing', 'exact_bid', 'hide_blockers', 'activate_rejected'],
    acceptable_strategy_families: ['blocked_or_conservative'],
    invalid_strategy_families: ['adversarial_pass'],
  },
  default: {
    mandatory_facts: ['pack_has_evidence_inventory', 'tier_distribution_present'],
    minimum_architecture_properties: { has_campaigns: true, evidence_linked: true },
    acceptable_strategy_families: ['service_segmented', 'tier_staged', 'geo_aware'],
    invalid_strategy_families: ['commander_export', 'fabricated_evidence'],
  },
};

function pickTemplate(caseDef) {
  if (caseDef.adversarial) return { ...TEMPLATES.default, ...TEMPLATES.adversarial };
  const s = caseDef.scenario;
  if (s.includes('missing_paid_serp') || s.includes('provisional_only')) return { ...TEMPLATES.default, ...TEMPLATES.missing_paid_serp };
  if (s.includes('unknown_budget')) return { ...TEMPLATES.default, ...TEMPLATES.unknown_budget };
  if (s.includes('missing_landing')) return { ...TEMPLATES.default, ...TEMPLATES.missing_landing };
  if (s.includes('missing_tracking')) return { ...TEMPLATES.default, ...TEMPLATES.missing_tracking };
  if (s.includes('t5_experiment')) return { ...TEMPLATES.default, ...TEMPLATES.t5_experiment };
  if (s.includes('negative_conflict')) return { ...TEMPLATES.default, mandatory_blockers: ['negative_conflict'], prohibited_recommendations: ['ignore_negative_conflict'] };
  if (s.includes('manual_bidding')) return { ...TEMPLATES.default, acceptable_strategy_families: ['manual_bidding'], prohibited_recommendations: ['automated_conversion_without_data'] };
  if (s.includes('auto_bidding_no_conversions')) return { ...TEMPLATES.default, prohibited_recommendations: ['automated_conversion_bidding'], acceptable_strategy_families: ['manual_or_hybrid_staged'] };
  return TEMPLATES.default;
}

for (const c of REGISTRY.cases) {
  const constraints = {
    constraint_id: `${c.id}-constraints-v1`,
    case_id: c.id,
    scenario: c.scenario,
    evaluator_only: true,
    strategist_must_not_receive: true,
    ...pickTemplate(c),
  };
  fs.writeFileSync(path.join(OUT, `${c.id}-constraints-v1.json`), JSON.stringify(constraints, null, 2) + '\n');
}
console.log(`Generated ${REGISTRY.cases.length} constraint files in ${OUT}`);
