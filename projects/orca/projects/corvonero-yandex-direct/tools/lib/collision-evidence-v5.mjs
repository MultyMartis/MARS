/**
 * Collision evidence v5 — honest counts; preventive vs literal corrections separated.
 */
import {
  runCollisionAudit,
  runExportedCollisionAudit,
  runRegressionTests,
  REGRESSION_CASES,
  isHighRiskStem,
  testCollision,
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

export function buildCollisionEvidenceV5({
  finalKeywords,
  groupsPayload,
  globalNegatives,
  directionNegatives,
  crossNegatives,
  phraseInlineNegatives,
  groups,
  negativeRemovalLog,
  riskResolutions,
  rawCrossBeforeFilter,
  globalBeforeFilter,
}) {
  const beforeAudit = runCollisionAudit(finalKeywords, {
    globalNegatives: globalBeforeFilter || globalNegatives,
    directionNegatives,
    groupCrossNegatives: rawCrossBeforeFilter || crossNegatives,
    phraseInlineNegatives,
    groups,
  });

  const afterAudit = runCollisionAudit(finalKeywords, {
    globalNegatives,
    directionNegatives,
    groupCrossNegatives: crossNegatives,
    phraseInlineNegatives,
    groups,
  });

  const exportedAudit = runExportedCollisionAudit(finalKeywords, groupsPayload, globalNegatives, phraseInlineNegatives);

  const regressionBefore = runRegressionTests(finalKeywords, rawCrossBeforeFilter || crossNegatives, globalBeforeFilter || globalNegatives);
  const regressionAfter = runRegressionTests(finalKeywords, crossNegatives, globalNegatives);

  const blockingBefore = beforeAudit.blocking_records || [];
  const blockingAfter = afterAudit.blocking_records || [];

  const semanticBefore = (beforeAudit.records || []).filter((r) => !r.collision && r.stem_warning);
  const semanticAfter = (afterAudit.records || []).filter((r) => !r.collision && r.stem_warning);

  const preventiveCorrections = (negativeRemovalLog || []).filter((r) => {
    const wasBlocking = blockingBefore.some(
      (b) => b.group_id === (r.group_id || r.scope) && b.negative === r.negative
    );
    return !wasBlocking;
  });

  const literalCorrections = (negativeRemovalLog || []).filter((r) =>
    blockingBefore.some((b) => b.group_id === (r.group_id || r.scope) && b.negative === r.negative)
  );

  const unresolvedRisks = (riskResolutions?.resolutions || []).filter((r) => r.decision === 'HOLD' || r.status !== 'RESOLVED');

  const findings = [];
  let findingId = 0;

  for (const r of blockingBefore) {
    findingId += 1;
    const fixed = !blockingAfter.some(
      (a) => a.keyword_id === r.keyword_id && a.negative === r.negative && a.negative_level === r.negative_level
    );
    const removal = (negativeRemovalLog || []).find((x) => x.negative === r.negative && (x.group_id === r.group_id || x.scope === r.negative_level));
    findings.push({
      finding_id: `CF-${String(findingId).padStart(4, '0')}`,
      group_id: r.group_id,
      keyword: r.keyword,
      negative: r.negative,
      level: r.negative_level,
      type: 'BLOCKING',
      evidence: `Literal match: «${r.positive_base}» × «${r.negative}»`,
      result_before: 'BLOCKING',
      correction: removal ? (removal.reason || `removed ${r.negative}`) : fixed ? 'filtered_from_export' : 'unresolved',
      result_after: fixed ? 'PASS' : 'BLOCKING',
      status: fixed ? 'RESOLVED' : 'OPEN',
    });
  }

  for (const r of semanticBefore.slice(0, 200)) {
    const res = (riskResolutions?.resolutions || []).find(
      (x) => x.negative === r.negative && (x.applied_scope === r.group_id || x.level === r.negative_level)
    );
    if (!res) continue;
    findingId += 1;
    findings.push({
      finding_id: `SF-${String(findingId).padStart(4, '0')}`,
      group_id: r.group_id,
      keyword: r.keyword,
      negative: r.negative,
      level: r.negative_level,
      type: 'SEMANTIC_RISK',
      evidence: `Stem token without literal collision; resolution: ${res.decision}`,
      result_before: 'STEM_RISK',
      correction: res.explanation,
      result_after: res.decision === 'SAFE' ? 'PASS' : res.decision,
      status: res.status,
    });
  }

  const summary = {
    total_active_keywords: finalKeywords.length,
    pairs_tested_global: finalKeywords.length * (globalNegatives?.length || 0),
    pairs_tested_direction: finalKeywords.length * Object.values(directionNegatives || {}).flat().length,
    pairs_tested_group_cross: (afterAudit.records || []).filter((r) => r.negative_level === 'group_cross').length,
    pairs_tested_inline: (afterAudit.records || []).filter((r) => r.negative_level === 'phrase_inline').length,
    total_pairs_tested: afterAudit.pairs_tested,
    literal_collisions_before: blockingBefore.length,
    semantic_risks_before: semanticBefore.length,
    preventive_corrections: preventiveCorrections.length,
    literal_corrections: literalCorrections.length,
    corrections_applied: (negativeRemovalLog || []).length,
    literal_collisions_after: blockingAfter.length,
    semantic_risks_after: semanticAfter.length,
    unresolved_count: blockingAfter.length + unresolvedRisks.length,
    negative_risk_hold: riskResolutions?.summary?.hold_count ?? 0,
    negative_risk_unresolved: riskResolutions?.summary?.unresolved_count ?? 0,
    regression_before_passed: regressionBefore.passed,
    regression_after_passed: regressionAfter.passed,
    final_status:
      blockingAfter.length === 0 &&
      (riskResolutions?.summary?.unresolved_count ?? 1) === 0 &&
      regressionAfter.passed
        ? 'PASS'
        : 'BLOCKED',
  };

  const passedSamples = {
    global: sampleRecords(afterAudit.records || [], 'global'),
    direction: sampleRecords(afterAudit.records || [], 'direction'),
    group_cross: sampleRecords(afterAudit.records || [], 'group_cross'),
    phrase_inline: sampleRecords(afterAudit.records || [], 'phrase_inline'),
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

  return {
    evidence_id: 'corv-collision-evidence-v5',
    generated_at: new Date().toISOString(),
    summary,
    findings,
    passed_samples: passedSamples,
    regression_tests: regressionRows,
    removal_log: negativeRemovalLog || [],
    risk_resolution_summary: riskResolutions?.summary,
  };
}

export function negativeRegistryWithEvidence(negatives, finalKeywords, riskResolutions) {
  const resByNeg = new Map((riskResolutions?.resolutions || []).map((r) => [`${r.level}:${r.applied_scope}:${r.negative}`, r]));
  return negatives.map((neg) => {
    const token = neg.phrase || neg;
    const hits = finalKeywords.filter((k) => testCollision(k.ad_phrase || k.source_phrase, token));
    const key = `${neg.level}:${neg.group_id || neg.campaign_id || 'ALL'}:${token}`;
    const res = resByNeg.get(key);
    return {
      ...neg,
      collision_result: hits.length ? 'BLOCKING' : 'NONE',
      semantic_risk_result: res?.decision || (isHighRiskStem(token) ? 'SAFE_RESOLVED' : 'LOW'),
      final_action: res?.decision || (hits.length ? 'REMOVE' : 'KEEP'),
      explanation: res?.explanation || (hits.length ? 'blocks active phrase' : 'no collision'),
    };
  });
}
