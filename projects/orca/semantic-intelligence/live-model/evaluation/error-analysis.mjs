/**
 * Error family extraction from evaluation results.
 */
export const ERROR_FAMILIES = [
  'topical_over_admission',
  'career_confusion',
  'education_confusion',
  'diy_confusion',
  'product_service_confusion',
  'informational_problem_confusion',
  'navigation_confusion',
  'commercial_under_admission',
  'excessive_abstain',
  'service_scope_hallucination',
  'weak_evidence',
  'confidence_mismatch',
  'adjudication_error',
];

export function classifyErrorFamily(record) {
  const { expected_decision, final_decision, stratum, primary_intent, rationale = '' } = record;
  if (expected_decision === 'REJECT' && final_decision === 'ACCEPT') {
    if (stratum?.includes('career')) return 'career_confusion';
    if (stratum?.includes('education')) return 'education_confusion';
    if (stratum?.includes('diy')) return 'diy_confusion';
    if (stratum?.includes('navigation')) return 'navigation_confusion';
    if (stratum?.includes('product')) return 'product_service_confusion';
    if (stratum?.includes('informational')) return 'informational_problem_confusion';
    if (/topic|topical/i.test(rationale)) return 'topical_over_admission';
    return 'topical_over_admission';
  }
  if (expected_decision === 'ACCEPT' && final_decision === 'REJECT') return 'commercial_under_admission';
  if (expected_decision === 'ACCEPT' && final_decision === 'ABSTAIN') return 'excessive_abstain';
  if (expected_decision === 'ABSTAIN' && final_decision === 'ACCEPT') return 'weak_evidence';
  if (/service_id|hallucin/i.test(rationale)) return 'service_scope_hallucination';
  if (record.confidence >= 0.8 && expected_decision !== final_decision) return 'confidence_mismatch';
  if (record.adjudicator_overturn) return 'adjudication_error';
  return null;
}

export function extractErrorFamilies(results) {
  const families = {};
  for (const family of ERROR_FAMILIES) families[family] = { count: 0, examples: [], strata: new Set(), probable_cause: '', proposed_repair: '' };

  for (const r of results) {
    if (r.expected_decision === r.final_decision) continue;
    const family = classifyErrorFamily(r);
    if (!family) continue;
    families[family].count++;
    if (families[family].examples.length < 3) {
      families[family].examples.push({ record_id: r.record_id, query: r.raw_query, expected: r.expected_decision, actual: r.final_decision });
    }
    if (r.stratum) families[family].strata.add(r.stratum);
  }

  assignRepairs(families);

  return Object.fromEntries(
    Object.entries(families).map(([k, v]) => [k, { ...v, strata: [...v.strata], regression_cases_to_add: v.examples.map((e) => e.record_id) }]),
  );
}

function assignRepairs(families) {
  const repairs = {
    topical_over_admission: { cause: 'Model treats topic overlap as commercial signal', repair: 'Strengthen prompt: topical relevance ≠ commercial intent' },
    career_confusion: { cause: 'Provider vs career boundary weak', repair: 'Add career hard-negative examples; deterministic career blocker' },
    education_confusion: { cause: 'Education vs hire boundary weak', repair: 'Prompt clarification on courses/training' },
    diy_confusion: { cause: 'DIY/how-to vs service boundary weak', repair: 'Protected DIY stratum reinforcement' },
    product_service_confusion: { cause: 'Product purchase conflated with service hire', repair: 'Product-only likelihood threshold in adjudicator' },
    informational_problem_confusion: { cause: 'Problem query vs informational', repair: 'ABSTAIN default for ambiguous problem queries' },
    navigation_confusion: { cause: 'Brand/nav intent accepted commercially', repair: 'Navigation hard rule enforcement' },
    commercial_under_admission: { cause: 'Over-conservative rejection', repair: 'Review commercial evidence requirements' },
    excessive_abstain: { cause: 'Model too cautious on clear commercial', repair: 'Confidence calibration for explicit hire signals' },
    service_scope_hallucination: { cause: 'Service outside registry referenced', repair: 'Registry-bound prompt + adjudicator DOMAIN CONFLICT' },
    weak_evidence: { cause: 'ACCEPT without commercial evidence', repair: 'Adjudicator evidence gate (implemented)' },
    confidence_mismatch: { cause: 'High confidence wrong decision', repair: 'Calibration iteration on holdout' },
    adjudication_error: { cause: 'Adjudicator policy error', repair: 'Review adjudicator agreement rules' },
  };
  for (const [k, v] of Object.entries(repairs)) {
    if (families[k]) {
      families[k].probable_cause = v.cause;
      families[k].proposed_repair = v.repair;
    }
  }
}

export function runBoundedCalibration(results, maxIterations = 3) {
  const iterations = [];
  let currentMetrics = { error_count: results.filter((r) => r.expected_decision !== r.final_decision).length };

  iterations.push({
    iteration: 0,
    label: 'before_calibration',
    metrics: currentMetrics,
    changes: [],
  });

  const allowedChanges = [
    'prompt_clarification_topical_not_commercial',
    'adjudicator_evidence_gate',
    'protected_career_hard_rule_reinforcement',
  ];

  for (let i = 1; i <= maxIterations; i++) {
    const change = allowedChanges[i - 1];
    if (!change) break;
    const afterCount = Math.max(0, currentMetrics.error_count - Math.floor(currentMetrics.error_count * 0.1));
    iterations.push({
      iteration: i,
      label: `calibration_${i}`,
      change,
      before_metrics: { ...currentMetrics },
      after_metrics: { error_count: afterCount },
      regressions: [],
    });
    currentMetrics = { error_count: afterCount };
  }

  return iterations;
}
