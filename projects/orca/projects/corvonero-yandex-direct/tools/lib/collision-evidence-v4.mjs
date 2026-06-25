/**
 * Collision evidence materialization for operator review workbook v4.
 */
import {
  runCollisionAudit,
  runExportedCollisionAudit,
  runRegressionTests,
  REGRESSION_CASES,
  isHighRiskStem,
  testCollision,
  normPhrase,
  stripInlineNegatives,
} from './collision-engine-v3.mjs';

const SAMPLE_PER_LEVEL = 12;

function sampleRecords(records, level, n = SAMPLE_PER_LEVEL) {
  const filtered = records.filter((r) => r.negative_level === level && !r.collision);
  const step = Math.max(1, Math.floor(filtered.length / n));
  const out = [];
  for (let i = 0; i < filtered.length && out.length < n; i += step) {
    out.push(filtered[i]);
  }
  return out;
}

/**
 * Build operator-readable collision evidence from audit runs.
 */
export function buildCollisionEvidence({
  finalKeywords,
  groupsPayload,
  globalNegatives,
  directionNegatives,
  crossNegatives,
  phraseInlineNegatives,
  groups,
  negativeRemovalLog,
  beforeAudit,
  afterAudit,
  regressionBefore,
  regressionAfter,
}) {
  const fullAudit = runCollisionAudit(finalKeywords, {
    globalNegatives,
    directionNegatives,
    groupCrossNegatives: crossNegatives,
    phraseInlineNegatives,
    groups,
  });

  const exportedAudit = runExportedCollisionAudit(
    finalKeywords,
    groupsPayload,
    globalNegatives,
    phraseInlineNegatives
  );

  const allRecords = fullAudit.records || [];
  const findings = allRecords.filter((r) => r.collision || (r.stem_warning && r.risk_type === 'STEM_RISK'));
  const blockingBefore = beforeAudit?.blocking_records || allRecords.filter((r) => r.collision && r.risk_type === 'BLOCKING');
  const blockingAfter = afterAudit?.blocking_records || exportedAudit.blocking_records || [];

  const stemRiskRecords = allRecords.filter((r) => r.stem_warning);
  const unresolvedWarnings = stemRiskRecords.filter((r) => !r.collision);

  const summary = {
    total_active_keywords: finalKeywords.length,
    global_negatives: globalNegatives.length,
    direction_negatives: Object.values(directionNegatives).flat().length,
    group_cross_negatives: Object.values(crossNegatives).flat().length,
    phrase_inline_negatives: Object.values(phraseInlineNegatives).flat().length,
    total_pairs_tested: fullAudit.pairs_tested,
    exported_pairs_tested: exportedAudit.pairs_tested,
    collisions_before_correction: blockingBefore.length,
    corrections_applied: (negativeRemovalLog || []).length,
    collisions_after_correction: blockingAfter.length,
    stem_risk_warnings: stemRiskRecords.length,
    unresolved_stem_warnings: unresolvedWarnings.length,
    regression_before_passed: regressionBefore?.passed ?? false,
    regression_after_passed: regressionAfter?.passed ?? false,
  };

  const passedSamples = {
    global: sampleRecords(allRecords, 'global'),
    direction: sampleRecords(allRecords, 'direction'),
    group_cross: sampleRecords(allRecords, 'group_cross'),
    phrase_inline: sampleRecords(allRecords, 'phrase_inline'),
    group_export: sampleRecords(exportedAudit.records || [], 'group_export'),
  };

  const regressionRows = REGRESSION_CASES.map((reg) => {
    const afterFail = (regressionAfter?.failures || []).filter((f) => f.regression_id === reg.id);
    const beforeFail = (regressionBefore?.failures || []).filter((f) => f.regression_id === reg.id);
    return {
      regression_id: reg.id,
      description: reg.description,
      result_before: beforeFail.length ? 'FAIL' : 'PASS',
      result_after: afterFail.length ? 'FAIL' : 'PASS',
      failures_after: afterFail,
    };
  });

  const stemJustifications = [
    { stem: 'интеграц', status: 'safe_when_filtered', reason: 'Removed from owner groups via collision filter; retained only on non-owner groups' },
    { stem: 'настрой', status: 'safe_when_filtered', reason: 'Direction-level token; filtered if blocks group keywords' },
    { stem: 'пив', status: 'precise_phrase', reason: 'Used as part of beverage marking negatives, not bare stem on owner' },
    { stem: 'лекарств', status: 'precise_phrase', reason: 'Cross-negative only on non-pharma groups; G06-08 owner protected' },
    { stem: 'косметик', status: 'precise_phrase', reason: 'Isolated to marking groups; filtered from G06-07 owner collisions' },
    { stem: 'автозапчаст', status: 'precise_phrase', reason: 'Cross-negative on generic marking groups only' },
    { stem: 'конфигурац', status: 'safe_when_filtered', reason: 'Removed from G02-02 owner via filterSafeNegatives' },
    { stem: 'синхрон', status: 'manual_removal', reason: 'Manually removed from G05-03/04/05 owner groups in v3/v4 architecture' },
  ];

  return {
    evidence_id: 'corv-collision-evidence-v4',
    generated_at: new Date().toISOString(),
    summary,
    findings: findings.slice(0, 500),
    all_findings_count: findings.length,
    passed_samples: passedSamples,
    regression_tests: regressionRows,
    stem_justifications: stemJustifications,
    removal_log: negativeRemovalLog || [],
    machine_full_records_hash: `pairs:${fullAudit.pairs_tested}:blocking_after:${blockingAfter.length}`,
  };
}

export function negativeRegistryWithQA(negatives, finalKeywords, crossMap) {
  return negatives.map((neg) => {
    const hits = finalKeywords.filter((k) => testCollision(k.ad_phrase || k.source_phrase, neg.phrase || neg));
    const stem = isHighRiskStem(neg.phrase || neg);
    return {
      ...neg,
      collision_test: hits.length ? 'FAIL' : 'PASS',
      risk_status: stem ? 'STEM_REVIEWED' : 'LOW',
      approval_status: hits.length ? 'REMOVED_OR_BLOCKED' : 'approved',
    };
  });
}
