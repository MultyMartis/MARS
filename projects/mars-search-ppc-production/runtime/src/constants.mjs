export const LIFECYCLE_VERSION = '1.0.0';
export const MANIFEST_SCHEMA_VERSION = '2.0.0';

export const STAGE_ORDER = [
  'SPPC-01', 'SPPC-02', 'SPPC-03', 'SPPC-04', 'SPPC-05', 'SPPC-06', 'SPPC-07', 'SPPC-08',
  'SPPC-09', 'SPPC-10', 'SPPC-11', 'SPPC-12', 'SPPC-13', 'SPPC-14', 'SPPC-15', 'SPPC-16',
  'SPPC-17', 'SPPC-18', 'SPPC-19', 'SPPC-20', 'SPPC-21', 'SPPC-22', 'SPPC-23',
];

export const STAGE_STATUSES = [
  'NOT STARTED', 'IN PROGRESS', 'BLOCKED', 'READY FOR REVIEW', 'APPROVED', 'COMPLETED',
  'COMPLETED WITH APPROVED DEGRADATION', 'SUPERSEDED', 'FAILED', 'FROZEN',
];

export const COMPLETE_STATUSES = new Set(['COMPLETED', 'COMPLETED WITH APPROVED DEGRADATION']);

export const CORPUS_MODES = [
  'PRODUCTION FULL CORPUS',
  'TECHNICAL PILOT',
  'BENCHMARK',
  'DIAGNOSTIC SAMPLE',
  'RANDOM QA SAMPLE',
  'HUMAN REVIEW SUBSET',
];

export const ARTIFACT_OWNERS = {
  business_scope_operator_authority: 'ATLAS / Operator',
  source_registry: 'MIG',
  full_semantic_corpus_intake: 'MIG',
  canonical_phrase_registry: 'ORCA Semantic Intelligence',
  commercial_admission_registry: 'ORCA Semantic Intelligence',
  demand_tier_registry: 'ORCA Semantic Intelligence',
  service_ownership_registry: 'ORCA Semantic Intelligence',
  semantic_cluster_registry: 'ORCA Semantic Intelligence',
  negative_intelligence_pack: 'ORCA Semantic Intelligence',
  paid_serp_business_hours_evidence: 'MIG',
  competitor_advertising_audit: 'MIG',
  dated_analytical_pack: 'Cross-system analytical pack',
  ppc_strategy_decision_record: 'AI PPC Strategist',
  campaign_architecture_registry: 'Campaign Production',
  keyword_negative_distribution: 'Campaign Production',
  ad_production_pack: 'Campaign Production',
  landing_alignment_report: 'QA',
  bidding_budget_strategy: 'Campaign Production',
  campaign_qa_report: 'QA / Validators',
  commander_export_artifact: 'Commander Export',
  operator_launch_approval: 'Operator',
  launch_evidence_pack: 'Operator / Platform',
  post_launch_learning_log: 'Post-Launch Learning',
};

export const FORBIDDEN_BEFORE = {
  'SPPC-08': ['semantic_cluster_registry'],
  'SPPC-09': ['negative_intelligence_pack'],
  'SPPC-12': ['ppc_strategy_decision_record', 'campaign_architecture_registry', 'commander_export_artifact'],
  'SPPC-13': ['campaign_architecture_registry', 'commander_export_artifact'],
  'SPPC-19': ['commander_export_artifact'],
  'SPPC-21': ['launch_evidence_pack'],
};

export const STAGE_TO_FORBIDDEN_ACTIONS = {
  'SPPC-08': ['Semantic Clustering'],
  'SPPC-09': ['Negative Keyword Intelligence'],
  'SPPC-12': ['AI PPC Strategist', 'Campaign Production', 'Commander Export'],
  'SPPC-13': ['Campaign Architecture', 'Commander Export'],
  'SPPC-14': ['Campaign Production'],
  'SPPC-19': ['Commander Export'],
  'SPPC-20': ['Import and Launch'],
  'SPPC-22': ['Launch'],
};

export const VALID_TRANSITIONS = {
  'NOT STARTED': ['IN PROGRESS', 'BLOCKED', 'FROZEN'],
  'IN PROGRESS': ['READY FOR REVIEW', 'BLOCKED', 'FAILED', 'FROZEN'],
  'READY FOR REVIEW': ['APPROVED', 'IN PROGRESS', 'BLOCKED', 'FAILED'],
  'APPROVED': ['COMPLETED', 'COMPLETED WITH APPROVED DEGRADATION', 'IN PROGRESS', 'BLOCKED', 'SUPERSEDED'],
  'COMPLETED': ['IN PROGRESS', 'SUPERSEDED'],
  'COMPLETED WITH APPROVED DEGRADATION': ['IN PROGRESS', 'SUPERSEDED'],
  'BLOCKED': ['IN PROGRESS', 'NOT STARTED', 'FROZEN'],
  'FAILED': ['IN PROGRESS', 'NOT STARTED'],
  'FROZEN': ['IN PROGRESS', 'BLOCKED'],
  'SUPERSEDED': [],
};

export const BLOCKER_CODES = {
  MISSING_MANIFEST: 'BLOCKED — LIFECYCLE REQUIREMENT NOT MET',
  INVALID_LIFECYCLE_VERSION: 'BLOCKED — LIFECYCLE REQUIREMENT NOT MET',
  MISSING_REQUIREMENTS: 'BLOCKED — LIFECYCLE REQUIREMENT NOT MET',
  FULL_CORPUS_NOT_REGISTERED: 'BLOCKED — FULL PRODUCTION CORPUS NOT REGISTERED',
  HUMAN_REVIEW_PRIMARY: 'BLOCKED — HUMAN REVIEW HAS BECOME PRIMARY CLASSIFICATION ENGINE',
  DEGRADED_NOT_APPROVED: 'BLOCKED — DEGRADED EVIDENCE MODE NOT APPROVED',
  PAID_SERP_MISSING: 'BLOCKED OR DEGRADED — PAID COMPETITIVE EVIDENCE MISSING',
  FORBIDDEN_TRANSITION: 'BLOCKED — LIFECYCLE REQUIREMENT NOT MET',
  FORBIDDEN_DOWNSTREAM: 'BLOCKED — LIFECYCLE REQUIREMENT NOT MET',
  PROJECT_FROZEN: 'BLOCKED — PROJECT FROZEN',
};

export const EXIT_CODES = {
  OK: 0,
  BLOCKED: 2,
  ERROR: 1,
};

export const DEFAULT_CONTRACT_REL = 'projects/mars-search-ppc-production/contracts/mars-search-ppc-lifecycle-contract-v1.json';
