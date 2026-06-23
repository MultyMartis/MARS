/**
 * D3 quality gates computation.
 */
export function computeD3Metrics(results, options = {}) {
  const goldOnly = options.goldOnly !== false;
  const filtered = goldOnly
    ? results.filter((r) => r.expected_authority_class === 'gold')
    : results;

  const goldAccepts = filtered.filter((r) => r.expected_decision === 'ACCEPT');
  const goldAcceptCorrect = goldAccepts.filter((r) => r.final_decision === 'ACCEPT' && (r.confidence || 0) >= 0.7);
  const commercialPrecision = goldAccepts.length
    ? goldAcceptCorrect.length / goldAccepts.filter((r) => r.final_decision === 'ACCEPT').length || 0
    : null;

  const protectedClasses = ['protected_career', 'protected_education', 'protected_diy', 'protected_navigation', 'protected_download', 'protected_product', 'protected_informational'];
  const protectedMetrics = {};
  for (const cls of protectedClasses) {
    const stratumRecords = filtered.filter((r) => r.stratum === cls);
    const falseAccepts = stratumRecords.filter((r) => r.final_decision === 'ACCEPT');
    protectedMetrics[cls] = {
      total: stratumRecords.length,
      accept: stratumRecords.filter((r) => r.final_decision === 'ACCEPT').length,
      reject: stratumRecords.filter((r) => r.final_decision === 'REJECT').length,
      abstain: stratumRecords.filter((r) => r.final_decision === 'ABSTAIN').length,
      false_accept_candidates: falseAccepts.length,
      false_positive_rate: stratumRecords.length ? falseAccepts.length / stratumRecords.length : 0,
    };
  }

  const commercialStrata = filtered.filter((r) => r.stratum?.startsWith('commercial_'));
  const commercialMetrics = {
    total: commercialStrata.length,
    false_reject: commercialStrata.filter((r) => r.expected_decision === 'ACCEPT' && r.final_decision === 'REJECT').length,
    excessive_abstain: commercialStrata.filter((r) => r.expected_decision === 'ACCEPT' && r.final_decision === 'ABSTAIN').length,
    recall: commercialStrata.length
      ? commercialStrata.filter((r) => r.final_decision === 'ACCEPT').length / commercialStrata.filter((r) => r.expected_decision === 'ACCEPT').length
      : null,
  };

  const gates = {
    commercial_precision_gold_high_confidence: {
      target: 0.95,
      value: commercialPrecision,
      pass: commercialPrecision !== null && commercialPrecision >= 0.95,
      authority: 'gold_only',
    },
    protected_false_positive_rate: {
      target: 0.01,
      per_class: Object.fromEntries(
        Object.entries(protectedMetrics).map(([k, v]) => [k, { value: v.false_positive_rate, pass: v.false_positive_rate <= 0.01 }]),
      ),
      pass: Object.values(protectedMetrics).every((v) => v.false_positive_rate <= 0.01),
    },
  };

  return {
    commercial_precision: commercialPrecision,
    commercial_recall: commercialMetrics.recall,
    abstain_rate: filtered.length ? filtered.filter((r) => r.final_decision === 'ABSTAIN').length / filtered.length : 0,
    human_review_ratio: filtered.length ? filtered.filter((r) => r.human_review_required).length / filtered.length : 0,
    assessor_agreement: filtered.length ? filtered.filter((r) => r.assessor_agreement).length / filtered.length : 0,
    adjudicator_overturn_rate: filtered.length ? filtered.filter((r) => r.adjudicator_overturn).length / filtered.length : 0,
    protected_strata: protectedMetrics,
    positive_commercial_strata: commercialMetrics,
    gates,
    diagnostic_excluded_from_gates: goldOnly,
  };
}
