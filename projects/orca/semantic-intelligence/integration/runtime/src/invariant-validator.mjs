import { AUTHORITATIVE_DECISIONS, FORBIDDEN_ADMISSION_FIELDS, LEGACY_AUTHORITATIVE_LABELS, NUMERIC_SENTINELS } from './lib.mjs';

function finding(code, severity, fieldPath, evidence, message, blocking, remediation) {
  return { invariant_id: code, severity, field_path: fieldPath, evidence, message, blocking, remediation };
}

const COMMERCIAL_SIGNALS = new Set([
  'PROVIDER_HIRE', 'COMMERCIAL_INTENT', 'PAID_SERVICE', 'EXPLICIT_PROVIDER_REQUEST', 'IMPLIED_COMMERCIAL',
]);

export function validateInvariants(record, context = {}) {
  const findings = [];
  const decision = record.commercial_eligibility?.decision;
  const signals = record.signals || [];
  const ambiguity = record.ambiguity || {};
  const types = new Set(ambiguity.types || []);

  // SI-INV-001 topic-only ACCEPT
  if (decision === 'ACCEPT' && record.primary_intent && /TOPIC|INFORMATIONAL/i.test(record.primary_intent) && !hasCommercialEvidence(signals, record)) {
    findings.push(finding('SI-INV-001', 'BLOCKING', 'commercial_eligibility.decision',
      ['primary_intent', 'signals'], 'ACCEPT based only on topical/service match', true,
      'Require explicit commercial evidence or REJECT/ABSTAIN'));
  }

  // SI-INV-002 ACCEPT without positive commercial evidence
  if (decision === 'ACCEPT' && !hasCommercialEvidence(signals, record)) {
    findings.push(finding('SI-INV-002', 'BLOCKING', 'commercial_eligibility.decision',
      ['signals', 'supporting_evidence'], 'ACCEPT without positive commercial evidence', true,
      'Add EXPLICIT/STRONG commercial signals or change decision'));
  }

  // SI-INV-003 ACCEPT with unresolved high ambiguity
  if (decision === 'ACCEPT' && ['HIGH', 'CRITICAL'].includes(ambiguity.severity)) {
    findings.push(finding('SI-INV-003', 'BLOCKING', 'ambiguity.severity',
      [ambiguity.severity, ...(ambiguity.unresolved_questions || [])], 'ACCEPT with unresolved high ambiguity', true,
      'ABSTAIN or resolve ambiguity before ACCEPT'));
  }

  // SI-INV-004 provider-vs-DIY
  if (decision === 'ACCEPT' && types.has('PROVIDER_VS_DIY')) {
    findings.push(finding('SI-INV-004', 'BLOCKING', 'ambiguity.types',
      ['PROVIDER_VS_DIY'], 'ACCEPT with unresolved provider-vs-DIY conflict', true, 'ABSTAIN until conflict resolved'));
  }

  // SI-INV-005 career-vs-provider
  if (decision === 'ACCEPT' && types.has('CAREER_VS_PROVIDER')) {
    findings.push(finding('SI-INV-005', 'BLOCKING', 'ambiguity.types',
      ['CAREER_VS_PROVIDER'], 'ACCEPT with unresolved career-vs-provider conflict', true, 'REJECT or ABSTAIN'));
  }

  // SI-INV-006 product-vs-service
  if (decision === 'ACCEPT' && types.has('PRODUCT_VS_SERVICE')) {
    findings.push(finding('SI-INV-006', 'BLOCKING', 'ambiguity.types',
      ['PRODUCT_VS_SERVICE'], 'ACCEPT with unresolved product-vs-service conflict', true, 'ABSTAIN'));
  }

  // SI-INV-007 missing provenance
  if (!record.provenance_status || record.provenance_status === 'MISSING' || record.provenance_status === 'UNKNOWN') {
    findings.push(finding('SI-INV-007', 'BLOCKING', 'provenance_status',
      [record.provenance_status], 'missing provenance', true, 'Set COMPLETE or PARTIAL provenance'));
  }

  // SI-INV-008 missing versions
  const ver = record.versioning || {};
  if (!ver.taxonomy_version || !ver.schema_version || !ver.guideline_version) {
    findings.push(finding('SI-INV-008', 'FATAL', 'versioning',
      Object.keys(ver), 'missing taxonomy/schema/guideline versions', true, 'Attach contract versions'));
  }

  // SI-INV-009 service ownership before ACCEPT
  const mapping = record.service_candidate?.mapping_status;
  if (decision === 'ACCEPT' && mapping && mapping !== 'NOT_STARTED' && mapping !== 'CANDIDATE_ONLY') {
    findings.push(finding('SI-INV-009', 'BLOCKING', 'service_candidate.mapping_status',
      [mapping], 'final service ownership before ACCEPT', true, 'Defer ownership until post-admission'));
  }
  if (decision === 'ACCEPT' && record.service_candidate?.candidate_service_ids?.length && mapping === 'FINAL') {
    findings.push(finding('SI-INV-009', 'BLOCKING', 'service_candidate',
      record.service_candidate.candidate_service_ids, 'final service ownership before ACCEPT', true, 'Use NOT_STARTED'));
  }

  // SI-INV-010 campaign/export fields
  for (const field of FORBIDDEN_ADMISSION_FIELDS) {
    if (record[field] !== undefined) {
      findings.push(finding('SI-INV-010', 'BLOCKING', field, [field], 'cluster/campaign/export fields in admission output', true, 'Remove downstream fields'));
    }
  }

  // SI-INV-011 numeric narrative placeholders
  const narrativeFields = ['literal_interpretation', 'likely_user_goal', 'phrase_explanation'];
  for (const f of narrativeFields) {
    const val = f === 'phrase_explanation' ? record.commercial_eligibility?.phrase_explanation : record[f];
    if (typeof val === 'number' && NUMERIC_SENTINELS.has(val)) {
      findings.push(finding('SI-INV-011', 'BLOCKING', f, [String(val)], 'numeric narrative placeholders', true, 'Use textual evidence'));
    }
    if (String(val) === '-1' || String(val) === '999') {
      findings.push(finding('SI-INV-011', 'BLOCKING', f, [String(val)], 'numeric narrative placeholders', true, 'Use textual evidence'));
    }
  }

  // SI-INV-012 silent rewrite
  if (context.original_normalized && record.normalized_query !== context.original_normalized && !context.normalization_documented) {
    findings.push(finding('SI-INV-012', 'BLOCKING', 'normalized_query',
      [context.original_normalized, record.normalized_query], 'malformed phrase silently rewritten', true, 'Document normalization or preserve raw'));
  }

  // SI-INV-013 missing ABSTAIN route — system must support ABSTAIN (checked via context flag)
  if (context.abstain_supported === false) {
    findings.push(finding('SI-INV-013', 'BLOCKING', 'commercial_eligibility.decision',
      [], 'missing ABSTAIN route', true, 'Enable ABSTAIN in orchestrator config'));
  }

  // SI-INV-014 semantic mutation by export fields
  if (record.export_mutation_detected) {
    findings.push(finding('SI-INV-014', 'BLOCKING', 'audit',
      ['export_mutation_detected'], 'semantic mutation during export', true, 'Isolate export from admission'));
  }

  // SI-INV-015 required contract not consumed
  if (context.contracts_consumed === false) {
    findings.push(finding('SI-INV-015', 'FATAL', 'audit.contract_consumption',
      [], 'required semantic contract not consumed', true, 'Load all required contracts'));
  }

  // Legacy authoritative label rejection
  const legacyLabel = context.legacy_authoritative_label || assessorLegacyLabel(context.assessor);
  if (legacyLabel) {
    findings.push(finding('SI-INV-LEGACY', 'BLOCKING', 'assessor.legacy_label',
      [legacyLabel], 'legacy authoritative label rejected', true, 'Map to ACCEPT/REJECT/ABSTAIN only'));
  }

  const blocked = findings.some((f) => f.blocking);
  return { ok: !blocked, blocked, findings };
}

function hasCommercialEvidence(signals, record) {
  const strong = signals.some((s) => COMMERCIAL_SIGNALS.has(s.signal_id) && ['STRONG', 'EXPLICIT', 'MEDIUM'].includes(s.strength));
  const supporting = (record.commercial_eligibility?.supporting_evidence || []).length > 0;
  return strong || supporting;
}

function assessorLegacyLabel(assessor) {
  if (!assessor) return null;
  const candidates = [
    assessor.legacy_decision,
    assessor.semantic_decision,
    assessor.final_status,
    assessor.commercial_eligibility?.legacy_label,
  ].filter(Boolean);
  for (const c of candidates) {
    if (LEGACY_AUTHORITATIVE_LABELS.has(String(c).toUpperCase())) return String(c);
  }
  if (assessor.commercial_eligibility?.decision && !AUTHORITATIVE_DECISIONS.has(assessor.commercial_eligibility.decision)) {
    return assessor.commercial_eligibility.decision;
  }
  return null;
}
