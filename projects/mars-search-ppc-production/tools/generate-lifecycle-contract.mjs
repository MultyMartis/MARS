#!/usr/bin/env node
/**
 * Generate mars-search-ppc-lifecycle-contract-v1.json from stage definitions.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '..');

const STATUSES = [
  'NOT STARTED',
  'IN PROGRESS',
  'BLOCKED',
  'READY FOR REVIEW',
  'APPROVED',
  'COMPLETED',
  'COMPLETED WITH APPROVED DEGRADATION',
  'SUPERSEDED',
  'FAILED',
  'FROZEN',
];

const STAGES = [
  { id: 'SPPC-01', name: 'Business Intake and Operator Authority', owner: 'ATLAS', next: ['SPPC-02'], artifacts: ['business_scope_operator_authority'], operatorGate: true },
  { id: 'SPPC-02', name: 'Source Registration', owner: 'MIG', next: ['SPPC-03'], artifacts: ['source_registry'], prereq: ['SPPC-01'] },
  { id: 'SPPC-03', name: 'Full Semantic Corpus Intake', owner: 'MIG', next: ['SPPC-04'], artifacts: ['full_semantic_corpus_intake'], prereq: ['SPPC-02'] },
  { id: 'SPPC-04', name: 'Normalization and Canonical Registry', owner: 'ORCA', next: ['SPPC-05'], artifacts: ['canonical_phrase_registry'], prereq: ['SPPC-03'] },
  { id: 'SPPC-05', name: 'Commercial Intent Admission', owner: 'ORCA Semantic Intelligence', next: ['SPPC-06'], artifacts: ['commercial_admission_registry'], prereq: ['SPPC-04'] },
  { id: 'SPPC-06', name: 'Demand Priority Segmentation', owner: 'ORCA Semantic Intelligence', next: ['SPPC-07'], artifacts: ['demand_tier_registry'], prereq: ['SPPC-05'] },
  { id: 'SPPC-07', name: 'Service and Meaning Ownership', owner: 'ORCA Semantic Intelligence', next: ['SPPC-08'], artifacts: ['service_ownership_registry'], prereq: ['SPPC-06'] },
  { id: 'SPPC-08', name: 'Semantic Clustering', owner: 'ORCA Semantic Intelligence', next: ['SPPC-09'], artifacts: ['semantic_cluster_registry'], prereq: ['SPPC-07'] },
  { id: 'SPPC-09', name: 'Negative Keyword Intelligence', owner: 'ORCA Semantic Intelligence', next: ['SPPC-10'], artifacts: ['negative_intelligence_pack'], prereq: ['SPPC-08'] },
  { id: 'SPPC-10', name: 'Daytime Paid SERP Intelligence', owner: 'MIG', next: ['SPPC-11'], artifacts: ['paid_serp_business_hours_evidence'], prereq: ['SPPC-09'], degradedAllowed: true },
  { id: 'SPPC-11', name: 'Competitor Advertising Audit', owner: 'MIG', next: ['SPPC-12'], artifacts: ['competitor_advertising_audit'], prereq: ['SPPC-10'] },
  { id: 'SPPC-12', name: 'Dated Analytical Pack', owner: 'Cross-system', next: ['SPPC-13'], artifacts: ['dated_analytical_pack'], prereq: ['SPPC-11'] },
  { id: 'SPPC-13', name: 'AI PPC Strategist', owner: 'AI PPC Strategist', next: ['SPPC-14'], artifacts: ['ppc_strategy_decision_record'], prereq: ['SPPC-12'], operatorGate: true },
  { id: 'SPPC-14', name: 'Campaign Architecture', owner: 'Campaign Production', next: ['SPPC-15'], artifacts: ['campaign_architecture_registry'], prereq: ['SPPC-13'] },
  { id: 'SPPC-15', name: 'Keyword and Negative Distribution', owner: 'Campaign Production', next: ['SPPC-16'], artifacts: ['keyword_negative_distribution'], prereq: ['SPPC-14'] },
  { id: 'SPPC-16', name: 'Ad Production', owner: 'Campaign Production', next: ['SPPC-17'], artifacts: ['ad_production_pack'], prereq: ['SPPC-15'] },
  { id: 'SPPC-17', name: 'Landing and Offer Alignment', owner: 'QA', next: ['SPPC-18'], artifacts: ['landing_alignment_report'], prereq: ['SPPC-16'] },
  { id: 'SPPC-18', name: 'Bidding and Budget Strategy', owner: 'Campaign Production', next: ['SPPC-19'], artifacts: ['bidding_budget_strategy'], prereq: ['SPPC-17'] },
  { id: 'SPPC-19', name: 'Campaign QA', owner: 'QA / Validators', next: ['SPPC-20'], artifacts: ['campaign_qa_report'], prereq: ['SPPC-18'] },
  { id: 'SPPC-20', name: 'Commander Export', owner: 'Commander Export', next: ['SPPC-21'], artifacts: ['commander_export_artifact'], prereq: ['SPPC-19'], transportOnly: true },
  { id: 'SPPC-21', name: 'Dry Run and Operator Approval', owner: 'Operator', next: ['SPPC-22'], artifacts: ['operator_launch_approval'], prereq: ['SPPC-20'], operatorGate: true },
  { id: 'SPPC-22', name: 'Import and Launch', owner: 'Operator / Platform', next: ['SPPC-23'], artifacts: ['launch_evidence_pack'], prereq: ['SPPC-21'] },
  { id: 'SPPC-23', name: 'Post-Launch Learning', owner: 'Post-Launch Learning', next: [], artifacts: ['post_launch_learning_log'], prereq: ['SPPC-22'] },
];

const DOWNSTREAM_PROHIBITIONS = {
  'before_SPPC-12': ['ppc_strategy_decision_record', 'campaign_architecture_registry', 'commander_export_artifact'],
  'before_SPPC-13': ['campaign_architecture_registry', 'commander_export_artifact'],
  'before_SPPC-19': ['commander_export_artifact'],
  'before_SPPC-21': ['launch_evidence_pack'],
};

const contract = {
  contract_id: 'mars-search-ppc-lifecycle-contract-v1',
  version: '1.0.0',
  status: 'PROPOSED — OPERATOR APPROVAL REQUIRED',
  lifecycle_statuses: STATUSES,
  platform: 'Yandex Direct',
  campaign_type: 'search',
  stages: STAGES.map((s) => ({
    stage_id: s.id,
    name: s.name,
    owning_system: s.owner,
    prerequisites: (s.prereq || []).map((p) => ({ stage_id: p, required_status: ['COMPLETED', 'COMPLETED WITH APPROVED DEGRADATION'] })),
    required_artifacts: s.artifacts.map((a) => ({
      artifact_type: a,
      must_exist: true,
      path_field: `artifacts.${a}.path`,
    })),
    allowed_next_stages: s.next,
    operator_approval_required: Boolean(s.operatorGate),
    degraded_mode_allowed: Boolean(s.degradedAllowed),
    transport_only: Boolean(s.transportOnly),
    completion_requires_registered_artifacts: true,
    report_claim_alone_insufficient: true,
  })),
  downstream_prohibitions: DOWNSTREAM_PROHIBITIONS,
  blocking_behavior: {
    on_missing_prerequisite: 'BLOCKED',
    on_missing_artifact: 'BLOCKED',
    on_forbidden_downstream_artifact: 'BLOCKED',
    fabricate_missing_evidence: false,
  },
  degraded_evidence_mode: {
    requires_operator_approval: true,
    applicable_stages: ['SPPC-10'],
    silent_degradation_forbidden: true,
  },
};

const out = path.join(root, 'contracts', 'mars-search-ppc-lifecycle-contract-v1.json');
fs.mkdirSync(path.dirname(out), { recursive: true });
fs.writeFileSync(out, JSON.stringify(contract, null, 2) + '\n');
console.log('Wrote', out);
