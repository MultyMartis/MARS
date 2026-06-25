/**
 * Observed fact / inference / recommendation model — Wave 4
 */

export const STATEMENT_TYPES = [
  'OBSERVED FACT',
  'DERIVED FINDING',
  'STRATEGIC RECOMMENDATION',
  'ASSUMPTION',
  'OPERATOR DECISION',
  'SAFE UNKNOWN',
];

export function createStatement(params) {
  const {
    statementId,
    statementType,
    text,
    supportingEvidenceIds = [],
    confidence = null,
    limitations = [],
    affectedStrategySections = [],
  } = params;

  if (!STATEMENT_TYPES.includes(statementType)) {
    throw new Error(`Invalid statement type: ${statementType}`);
  }
  if (statementType === 'STRATEGIC RECOMMENDATION' && !supportingEvidenceIds.length && !limitations.includes('explicit_assumption')) {
    throw new Error('Recommendation requires evidence IDs or explicit_assumption limitation');
  }

  return {
    statement_id: statementId,
    statement_type: statementType,
    text,
    supporting_evidence_ids: supportingEvidenceIds,
    confidence,
    limitations,
    affected_strategy_sections: affectedStrategySections,
  };
}

export function validateStatementSeparation(statements) {
  const violations = [];
  for (const s of statements) {
    if (s.statement_type === 'STRATEGIC RECOMMENDATION' && !s.supporting_evidence_ids?.length) {
      if (!s.limitations?.includes('explicit_assumption')) {
        violations.push({ statement_id: s.statement_id, issue: 'recommendation_without_evidence' });
      }
    }
    if (s.statement_type === 'OBSERVED FACT' && s.confidence === 1 && !s.supporting_evidence_ids?.length) {
      violations.push({ statement_id: s.statement_id, issue: 'observed_fact_without_evidence' });
    }
  }
  return { ok: violations.length === 0, violations };
}
