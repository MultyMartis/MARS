import { loadContracts } from './contract-loader.mjs';
import { createInitialRecord, applyAssessorOutput, validateRecordShape } from './record-generator.mjs';
import { validateInvariants } from './invariant-validator.mjs';
import { routeHumanReview } from './human-review-router.mjs';
import { buildLegacyComparison } from './legacy-comparison-adapter.mjs';
import { AUTHORITATIVE_DECISIONS, LEGACY_AUTHORITATIVE_LABELS, readJson } from './lib.mjs';
import fs from 'node:fs';

const STAGES = [
  'Contract Load',
  'Semantic Record Initialization',
  'Query Understanding Input',
  'Candidate Signals',
  'Intent Candidate',
  'Eligibility Candidate',
  'Invariant Validation',
  'Human Review Routing',
  'Integration Result',
];

export function runAdmissionIntegration(fixtureInput, options = {}) {
  const trace = { stages: [], started_at: new Date().toISOString() };
  const config = options.config || (options.configPath && fs.existsSync(options.configPath)
    ? readJson(options.configPath)
    : defaultConfig());
  if (fixtureInput.disable_abstain) config.abstain_supported = false;

  // Stage 1 — Contract Load
  const contractLoad = loadContracts({ lockPath: options.lockPath });
  trace.stages.push({ stage: STAGES[0], ok: contractLoad.ok, detail: contractLoad.message || 'loaded' });
  if (!contractLoad.ok) {
    return blockedResult(trace, contractLoad.message, contractLoad);
  }

  const input = fixtureInput.input || fixtureInput;
  const assessor = input.assessor || {};

  // Reject legacy authoritative labels in assessor
  const legacyDecision = assessor.commercial_eligibility?.decision;
  if (legacyDecision && LEGACY_AUTHORITATIVE_LABELS.has(String(legacyDecision).toUpperCase())) {
    return blockedResult(trace, 'legacy authoritative label in assessor output', {
      legacy_label: legacyDecision,
    });
  }
  if (legacyDecision && !AUTHORITATIVE_DECISIONS.has(legacyDecision)) {
    return blockedResult(trace, 'non-tri-state assessor decision', { decision: legacyDecision });
  }

  // Stage 2 — Record init
  let record = createInitialRecord(input, contractLoad);
  trace.stages.push({ stage: STAGES[1], ok: true, query_id: record.query_id });

  // Stage 3 — Query understanding
  if (input.query_understanding) {
    record.literal_interpretation = input.query_understanding.literal_interpretation || record.literal_interpretation;
    record.likely_user_goal = input.query_understanding.likely_user_goal || record.likely_user_goal;
  }
  trace.stages.push({ stage: STAGES[2], ok: true });

  // Stage 4 — Candidate signals (fixture/diagnostic)
  if (input.candidate_signals) record.signals = [...record.signals, ...input.candidate_signals];
  if (assessor.signals) record.signals = assessor.signals;
  trace.stages.push({ stage: STAGES[3], ok: true, signal_count: record.signals.length });

  // Stage 5 — Intent candidate
  if (assessor.primary_intent) record.primary_intent = assessor.primary_intent;
  trace.stages.push({ stage: STAGES[4], ok: true, primary_intent: record.primary_intent });

  // Stage 6 — Eligibility candidate
  record = applyAssessorOutput(record, assessor);
  trace.stages.push({ stage: STAGES[5], ok: true, decision: record.commercial_eligibility.decision });

  // Stage 7 — Invariant validation
  const invContext = {
    original_normalized: input.original_normalized || input.normalized_query || input.raw_query,
    normalization_documented: input.normalization_documented ?? true,
    abstain_supported: config.abstain_supported !== false,
    contracts_consumed: contractLoad.ok,
    assessor,
    protected_strata_conflict: input.protected_strata_conflict || false,
    assessor_disagreement: input.assessor_disagreement || false,
    invariant_warnings: input.invariant_warnings || [],
  };
  if (input.extra_fields) Object.assign(record, input.extra_fields);
  const validation = validateInvariants(record, invContext);
  trace.stages.push({ stage: STAGES[6], ok: validation.ok, findings: validation.findings });
  record.audit.validation_results = validation.findings;

  const shapeErrors = validateRecordShape(record);
  if (shapeErrors.length) {
    return {
      ok: false,
      blocked: true,
      message: 'record shape invalid',
      detail: { shapeErrors },
      validation,
      trace,
    };
  }

  // Stage 8 — Human review routing
  const routing = routeHumanReview(record, config.review_router || {}, invContext);
  record.review.workflow_status = routing.workflow_status;
  trace.stages.push({ stage: STAGES[7], ok: true, routed: routing.routed, routes: routing.routes });

  // Legacy comparison (diagnostic only)
  let diagnostic = null;
  if (input.enable_legacy_comparison !== false) {
    diagnostic = buildLegacyComparison(
      input.raw_query,
      record.commercial_eligibility.decision,
      validation.findings,
      routing.routed ? routing.routes : null,
    );
  }

  const blocked = validation.blocked;
  const integrationResult = {
    ok: !blocked,
    blocked,
    admission_decision: blocked ? null : record.commercial_eligibility.decision,
    record,
    validation,
    routing,
    diagnostic_comparison: diagnostic?.diagnostic_comparison || null,
    contract_load: { ok: true, load_order: contractLoad.load_order },
    trace,
  };

  trace.stages.push({
    stage: STAGES[8],
    ok: !blocked,
    admission_decision: integrationResult.admission_decision,
    review_routed: routing.routed,
  });
  trace.completed_at = new Date().toISOString();

  return integrationResult;
}

function blockedResult(trace, message, detail) {
  trace.stages.push({ stage: 'Integration Result', ok: false, message, detail });
  return { ok: false, blocked: true, message, detail, trace };
}

function defaultConfig() {
  return {
    abstain_supported: true,
    review_router: {
      random_accept_audit_rate: 0,
      random_reject_audit_rate: 0,
      audit_seed: 'fixture-non-production',
    },
  };
}
