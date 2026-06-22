import crypto from 'node:crypto';
import { FORBIDDEN_ADMISSION_FIELDS } from './lib.mjs';

const UNKNOWN = 'UNKNOWN';
const NOT_ASSESSED = 'NOT_ASSESSED';

export function stableQueryId(normalizedQuery, sourceType = 'fixture') {
  const hash = crypto.createHash('sha256').update(`${sourceType}::${normalizedQuery}`).digest('hex').slice(0, 16);
  return `q-${hash}`;
}

export function createInitialRecord(input, contractLoad) {
  const now = new Date().toISOString();
  const raw = input.raw_query;
  const normalized = input.normalized_query || raw;
  const provenance = input.provenance || {};

  const record = {
    query_id: input.query_id || stableQueryId(normalized, provenance.source_type || 'fixture'),
    record_version: '1.0.0',
    schema_version: 'v1',
    created_at: now,
    updated_at: now,
    raw_query: raw,
    normalized_query: normalized,
    language: input.language || 'ru',
    source_type: provenance.source_type || 'fixture',
    provenance_status: provenance.status || UNKNOWN,
    literal_interpretation: input.query_understanding?.literal_interpretation || NOT_ASSESSED,
    likely_user_goal: input.query_understanding?.likely_user_goal || UNKNOWN,
    primary_intent: UNKNOWN,
    secondary_intents: [],
    entities: [],
    actions: [],
    objects: [],
    problems: [],
    desired_outcomes: [],
    modifiers: [],
    geography: null,
    product_or_module: null,
    configuration_or_version: null,
    industry_context: null,
    signals: [],
    ambiguity: {
      types: ['UNKNOWN'],
      severity: 'LOW',
      competing_interpretations: [],
      unresolved_questions: [],
    },
    commercial_eligibility: {
      decision: 'ABSTAIN',
      reason_code: 'NOT_ASSESSED',
      phrase_explanation: NOT_ASSESSED,
      supporting_evidence: [],
      opposing_evidence: [],
      confidence: 0,
      threshold_profile: null,
      reviewer_required: true,
    },
    risk: {
      overall_risk: 'LOW',
      dimensions: {},
      blocking_conditions: [],
    },
    service_candidate: {
      candidate_service_ids: [],
      mapping_status: 'NOT_STARTED',
      mapping_confidence: null,
      mapping_conflicts: [],
    },
    review: {
      workflow_status: 'UNPROCESSED',
      automated_assessors: [],
      human_reviewers: [],
      adjudicator: null,
      operator_override: false,
      review_notes: null,
    },
    versioning: {
      taxonomy_version: 'v1',
      schema_version: 'v1',
      guideline_version: 'v1',
      rule_version: NOT_ASSESSED,
      model_version: null,
      prompt_version: null,
      contract_bundle: contractLoad?.bundleVersion || 'p0-i-bundle-v1',
    },
    audit: {
      decision_history: [],
      change_reasons: [],
      immutable_evidence_references: [],
      validation_results: [],
      contract_consumption: {
        manifest_version: contractLoad?.manifest?.lock_version || 'v1',
        contracts_loaded: contractLoad?.load_order || [],
        consumed_at: now,
      },
    },
  };

  for (const field of FORBIDDEN_ADMISSION_FIELDS) {
    if (field in record) {
      throw new Error(`forbidden field in generator: ${field}`);
    }
  }

  return record;
}

export function applyAssessorOutput(record, assessor) {
  if (!assessor) return record;
  if (assessor.primary_intent) record.primary_intent = assessor.primary_intent;
  if (assessor.likely_user_goal) record.likely_user_goal = assessor.likely_user_goal;
  if (assessor.literal_interpretation) record.literal_interpretation = assessor.literal_interpretation;
  if (assessor.signals) record.signals = assessor.signals;
  if (assessor.ambiguity) record.ambiguity = assessor.ambiguity;
  if (assessor.risk) record.risk = { ...record.risk, ...assessor.risk };
  if (assessor.commercial_eligibility) {
    record.commercial_eligibility = { ...record.commercial_eligibility, ...assessor.commercial_eligibility };
  }
  if (assessor.service_candidate) record.service_candidate = { ...record.service_candidate, ...assessor.service_candidate };
  record.updated_at = new Date().toISOString();
  return record;
}

export function validateRecordShape(record) {
  const required = [
    'query_id', 'record_version', 'schema_version', 'raw_query', 'normalized_query',
    'provenance_status', 'commercial_eligibility', 'versioning', 'audit',
  ];
  const errors = [];
  for (const key of required) {
    if (record[key] === undefined || record[key] === null || record[key] === '') {
      errors.push(`missing required field: ${key}`);
    }
  }
  const decision = record.commercial_eligibility?.decision;
  if (decision && !['ACCEPT', 'REJECT', 'ABSTAIN'].includes(decision)) {
    errors.push(`invalid admission decision: ${decision}`);
  }
  return errors;
}
