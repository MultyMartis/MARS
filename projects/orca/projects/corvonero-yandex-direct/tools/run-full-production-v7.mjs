/**
 * Corvonero Unified Commander v7 — apply scope recovery and rebuild production.
 * Run: node tools/run-full-production-v7.mjs
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { applyV7ScopeRecoveryPackage, loadJson } from './lib/v7-scope-recovery-apply.mjs';
import { normPhrase } from './lib/keyword-classifier-v2.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const PROD = path.join(ROOT, 'production');
const VAL = path.join(PROD, 'validation');
const AUDIT = path.join(PROD, 'audit');
const EXPORTS = path.join(ROOT, 'exports');
const ARTIFACTS = path.join(ROOT, 'artifacts');

[PROD, VAL, AUDIT, EXPORTS, ARTIFACTS].forEach((d) => fs.mkdirSync(d, { recursive: true }));

const scopeGate = loadJson(path.join(VAL, 'production-scope-recovery-gate.json'));
if (!String(scopeGate.outcome || '').includes('PASS')) {
  console.error('Production Scope Recovery Gate is not PASS — aborting v7 production.');
  process.exit(1);
}

const result = applyV7ScopeRecoveryPackage({
  v6Dataset: loadJson(path.join(PROD, 'direct-commander-production-dataset-v6.json')),
  v6Semantic: loadJson(path.join(PROD, 'semantic-evidence-review-v6.json')),
  v5Dataset: loadJson(path.join(PROD, 'direct-commander-production-dataset-v5.json')),
  v5Ads: loadJson(path.join(PROD, 'final-ad-registry-v5.json')),
  v7Package: loadJson(path.join(PROD, 'recovery/v7-production-input-package.json')),
  controlledTestV2: loadJson(path.join(PROD, 'recovery/controlled-test-registry-v2.json')),
  negImpactPlan: loadJson(path.join(PROD, 'recovery/negative-impact-plan-v7.json')),
});

const {
  commanderDataset,
  semanticRegistry,
  finalKeywords,
  finalAds,
  adEvidence,
  riskPass,
  collisionEvidence,
  negativesQA,
  groupsPayload,
  groupViability,
  heldGroupsPayload,
  v6ToV7Exclusions,
  v6ToV7Restorations,
  bidSummary,
  semanticValidation,
  consistency,
  controlledTestsFinal,
  hypothesisMismatches,
  resolutionsToMarkdown,
  v7Package,
} = result;

const lifecyclePath = path.join(AUDIT, 'version-lifecycle-status.json');
let priorLifecycle = {};
if (fs.existsSync(lifecyclePath)) priorLifecycle = loadJson(lifecyclePath);

fs.writeFileSync(
  lifecyclePath,
  JSON.stringify(
    {
      ...priorLifecycle,
      registered_at: new Date().toISOString(),
      commander_v6: 'REJECTED — COMMERCIAL SCOPE LOSS',
      review_v6: 'REJECTED — SEMANTIC AND CONTROLLED-TEST DEFECTS',
      production_scope_recovery_gate: 'PASSED',
      v7_production: 'IN PRODUCTION',
      commander_dry_run: 'AUTHORIZED — OPERATOR REVIEW PENDING',
      moderation: 'NOT AUTHORIZED',
      launch: 'NOT AUTHORIZED',
      campaign_split: 'DEFERRED',
      landing_copy: 'NOT STARTED',
      note: 'v1–v6 artefacts preserved unchanged; v7 is current production target after scope recovery.',
    },
    null,
    2
  )
);

const COMMERCIAL_ANCHORS = [
  'расчет себестоимости 1с',
  'себестоимость в 1с',
  'планирование закупок 1с',
  'платежный календарь 1с',
  'перенос данных в 1с',
  'миграция данных 1с',
  'внедрение 1с',
  'обслуживание 1с',
  'обслуживание 1с для организации',
  'программист 1с новосибирск',
  'восстановление работы 1с',
  'срочно программист 1с',
];

function findAnchorRecord(anchor) {
  const n = normPhrase(anchor);
  let kw = finalKeywords.find((k) => normPhrase(k.normalized_phrase) === n || normPhrase(k.source_phrase) === n);
  if (!kw && n === 'обслуживание 1с') {
    kw = finalKeywords.find((k) => normPhrase(k.normalized_phrase).startsWith('обслуживание 1с'));
  }
  return kw;
}

const anchorCoverage = COMMERCIAL_ANCHORS.map((anchor) => {
  const kw = findAnchorRecord(anchor);
  return {
    anchor,
    found: Boolean(kw),
    keyword_id: kw?.keyword_id || null,
    phrase: kw?.normalized_phrase || null,
    group_id: kw?.group_id || null,
    status: kw?.semantic_decision || 'MISSING',
    ad_id: kw?.ad_id || null,
    landing: kw?.planned_url || null,
    bid: kw?.final_bid || null,
    export_present: Boolean(kw),
  };
});

const operatorScope = loadJson(path.join(PROD, 'operator-service-scope-v1.json'));
const scopeCoverage = {
  validated_at: new Date().toISOString(),
  gate_id: 'operator-scope-coverage-v7',
  service_families_total: operatorScope.services.length,
  service_families_represented: operatorScope.services.filter((s) => {
    const gid = s.current_group;
    return groupsPayload.some((g) => g.group_id === gid);
  }).length,
  commercial_anchors: anchorCoverage,
  commercial_seed_loss: anchorCoverage.filter((a) => !a.found).length,
  restored_groups: commanderDataset.restored_groups,
  outcome:
    anchorCoverage.every((a) => a.found) && operatorScope.services.every((s) => groupsPayload.some((g) => g.group_id === s.current_group))
      ? 'PASS'
      : 'BLOCKED',
};

const statusConsistencyIssues = [];
for (const k of finalKeywords) {
  if (k.semantic_decision?.startsWith('EXCLUDE')) statusConsistencyIssues.push({ keyword_id: k.keyword_id, issue: 'EXCLUDE in export' });
  if (k.semantic_decision?.includes('CONTROLLED') && !k.controlled_test_hypothesis) {
    statusConsistencyIssues.push({ keyword_id: k.keyword_id, issue: 'controlled test without hypothesis' });
  }
}
for (const ex of v6ToV7Exclusions) {
  if (finalKeywords.some((k) => k.keyword_id === ex.keyword_id)) {
    statusConsistencyIssues.push({ keyword_id: ex.keyword_id, issue: 'excluded phrase still in export' });
  }
}

const statusConsistency = {
  validated_at: new Date().toISOString(),
  gate_id: 'status-reason-consistency-v7',
  issues: statusConsistencyIssues,
  hypothesis_mismatches: hypothesisMismatches.map((k) => ({
    keyword_id: k.keyword_id,
    phrase: k.normalized_phrase,
    group_id: k.group_id,
    hypothesis: k.controlled_test_hypothesis,
  })),
  passed: statusConsistencyIssues.length === 0 && hypothesisMismatches.length === 0,
  outcome: statusConsistencyIssues.length === 0 && hypothesisMismatches.length === 0 ? 'PASS' : 'BLOCKED',
};

const kwRegistry = {
  registry_id: 'corv-final-kw-v7',
  generated_at: new Date().toISOString(),
  stats: {
    active_keywords: finalKeywords.length,
    active_groups: groupsPayload.length,
    held_groups: heldGroupsPayload.length,
    exclusions_v7: v6ToV7Exclusions.length,
    restorations_v7: v6ToV7Restorations.length,
    controlled_tests: controlledTestsFinal.length,
    v6_active_before: commanderDataset.audit_input ? 274 : null,
  },
  keywords: finalKeywords.map((k) => ({
    keyword_id: k.keyword_id,
    raw_phrase: k.source_phrase,
    positive_phrase: k.ad_phrase,
    normalized_phrase: k.normalized_phrase,
    final_status: k.semantic_decision,
    final_group: k.group_id,
    service_family: k.service_family,
    final_decision_reason: k.final_decision_reason,
    commercial_confidence: k.commercial_confidence,
    controlled_test_status: k.semantic_decision?.includes('CONTROLLED') ? 'CONTROLLED TEST — JUSTIFIED' : null,
    controlled_test_hypothesis: k.controlled_test_hypothesis,
    noise_risk: k.noise_risk,
    bid_tier: k.bid_tier,
    final_bid: k.final_bid,
    ad_mapping: k.ad_id,
    landing_mapping: k.planned_url,
    source: k.source,
  })),
  reject_log: commanderDataset.excluded_keywords,
};
fs.writeFileSync(path.join(PROD, 'final-keyword-registry-v7.json'), JSON.stringify(kwRegistry, null, 2));
fs.writeFileSync(
  path.join(PROD, 'final-keyword-registry-v7.md'),
  [
    '# Final Keyword Registry v7',
    '',
    `Active keywords: **${finalKeywords.length}**`,
    `Restorations from v6: **${v6ToV7Restorations.length}**`,
    `Exclusions in v7: **${v6ToV7Exclusions.length}**`,
    `Controlled tests: **${controlledTestsFinal.length}**`,
    '',
    '## Hard exclusions (verified absent)',
    '',
    ...v6ToV7Exclusions.map((e) => `- \`${e.phrase}\` — ${e.v7_status}`),
  ].join('\n')
);
fs.writeFileSync(
  path.join(PROD, 'keyword-v6-to-v7-diff.md'),
  [
    '# Keyword v6→v7 diff',
    '',
    '| Metric | v6 | v7 |',
    '|--------|---:|---:|',
    `| Active keywords | 274 | ${finalKeywords.length} |`,
    `| Restored | — | ${v6ToV7Restorations.length} |`,
    `| New exclusions | — | ${v6ToV7Exclusions.length} |`,
    '',
    '## Restored',
    '',
    '| phrase | group | v7 status |',
    '|--------|-------|-----------|',
    ...v6ToV7Restorations.map((r) => `| ${r.phrase} | ${r.group_id} | ${r.v7_status} |`),
    '',
    '## Excluded',
    '',
    '| phrase | group | reason |',
    '|--------|-------|--------|',
    ...v6ToV7Exclusions.map((e) => `| ${e.phrase} | ${e.group_id} | ${e.reason} |`),
  ].join('\n')
);

const groupRegistry = {
  registry_id: 'corv-final-group-v7',
  generated_at: new Date().toISOString(),
  groups: groupsPayload.map((g) => ({
    group_id: g.group_id,
    direction_marker: g.direction_marker,
    export_name: g.group_export_name,
    viability_status: g.viability_status,
    keyword_count: g.keywords.length,
    ad_count: g.ads.length,
    planned_url: g.planned_url,
    export_to_xlsx: true,
    v7_reactivated: g.v7_reactivated || false,
  })),
  held_groups: heldGroupsPayload,
  viability: groupViability,
  restored_groups: commanderDataset.restored_groups,
};
fs.writeFileSync(path.join(PROD, 'final-group-registry-v7.json'), JSON.stringify(groupRegistry, null, 2));
fs.writeFileSync(
  path.join(PROD, 'final-group-registry-v7.md'),
  [
    '# Final Group Registry v7',
    '',
    `Active exported groups: **${groupsPayload.length}**`,
    `Held groups: **${heldGroupsPayload.length}**`,
    `Restored groups: **${commanderDataset.restored_groups.length}**`,
    '',
    '## Restored groups',
    '',
    ...commanderDataset.restored_groups.map((gid) => {
      const g = groupsPayload.find((x) => x.group_id === gid);
      return `- \`${gid}\` ${g?.group_export_name || ''} — ${g?.viability_status} (${g?.keywords.length || 0} kw)`;
    }),
  ].join('\n')
);
fs.writeFileSync(
  path.join(PROD, 'group-v6-to-v7-diff.md'),
  [
    '# Group v6→v7 diff',
    '',
    '| Metric | v6 | v7 |',
    '|--------|---:|---:|',
    `| Active groups | 40 | ${groupsPayload.length} |`,
    `| Held groups | 8 | ${heldGroupsPayload.length} |`,
    `| Restored | — | ${commanderDataset.restored_groups.length} |`,
    '',
    '## Reactivated groups',
    '',
    ...commanderDataset.restored_groups.map((gid) => `- ${gid}`),
  ].join('\n')
);

fs.writeFileSync(
  path.join(PROD, 'final-controlled-test-registry-v7.json'),
  JSON.stringify(
    {
      registry_id: 'corv-final-controlled-test-v7',
      generated_at: new Date().toISOString(),
      source: 'production/recovery/controlled-test-registry-v2.json',
      tests: controlledTestsFinal,
      hypothesis_mismatches: hypothesisMismatches.length,
    },
    null,
    2
  )
);
fs.writeFileSync(
  path.join(PROD, 'final-controlled-test-registry-v7.md'),
  `# Final Controlled Test Registry v7\n\nTests: **${controlledTestsFinal.length}**\nHypothesis mismatches: **${hypothesisMismatches.length}**\n`
);

fs.writeFileSync(
  path.join(PROD, 'final-negative-registry-v7.json'),
  JSON.stringify(
    {
      registry_id: 'corv-final-neg-v7',
      generated_at: new Date().toISOString(),
      recovery_refs: {
        negative_impact_plan: 'production/recovery/negative-impact-plan-v7.json',
        v6_negative_registry: 'production/final-negative-registry-v6.json',
      },
      stats: {
        global: commanderDataset.global_negatives.length,
        direction_tokens: Object.values(commanderDataset.direction_negatives).flat().length,
        cross_groups: Object.keys(commanderDataset.cross_negatives).length,
        unresolved: riskPass.summary.unresolved_count,
        blocking: collisionEvidence.summary.literal_collisions_after,
      },
      negatives: negativesQA,
    },
    null,
    2
  )
);
fs.writeFileSync(
  path.join(PROD, 'final-conflict-negative-matrix-v7.md'),
  [
    '# Conflict Negative Matrix v7',
    '',
    `Global negatives: ${commanderDataset.global_negatives.length}`,
    `Unresolved unique negatives: ${riskPass.summary.unresolved_count}`,
    `Blocking collisions after recovery: ${collisionEvidence.summary.literal_collisions_after}`,
    `Final status: **${collisionEvidence.summary.final_status}**`,
  ].join('\n')
);
fs.writeFileSync(
  path.join(PROD, 'negative-v6-to-v7-diff.md'),
  [
    '# Negative v6→v7 diff',
    '',
    'v7 scope recovery narrowed cross-negative «перенос данных» on CORV-G05-01 to protect CORV-G05-06.',
    `Global negatives v6→v7: ${(loadJson(path.join(PROD, 'direct-commander-production-dataset-v6.json')).global_negatives || []).length} → ${commanderDataset.global_negatives.length}`,
    'Full negative stack recalculated against final v7 phrase ownership.',
  ].join('\n')
);

fs.writeFileSync(path.join(PROD, 'semantic-evidence-review-v7.json'), JSON.stringify(semanticRegistry, null, 2));
fs.writeFileSync(
  path.join(PROD, 'semantic-evidence-review-v7.md'),
  `# Semantic Evidence Review v7\n\nReviews: ${semanticRegistry.reviews.length}\nActive exported: ${finalKeywords.length}\n`
);

fs.writeFileSync(
  path.join(PROD, 'final-ad-registry-v7.json'),
  JSON.stringify(
    {
      registry_id: 'corv-final-ad-v7',
      generated_at: new Date().toISOString(),
      ads: finalAds,
      evidence: adEvidence,
      restored_from_v5: finalAds.filter((a) => a.v7_source === 'restored_from_v5').map((a) => a.group_id),
    },
    null,
    2
  )
);
fs.writeFileSync(
  path.join(PROD, 'final-ad-registry-v7.md'),
  [
    '# Final Ad Registry v7',
    '',
    `Ads: ${finalAds.length}`,
    `Evidence passed: ${adEvidence.passed}`,
    `Restored from v5: ${finalAds.filter((a) => a.v7_source === 'restored_from_v5').length}`,
  ].join('\n')
);
fs.writeFileSync(
  path.join(PROD, 'ad-v6-to-v7-diff.md'),
  [
    '# Ad v6→v7 diff',
    '',
    'Restored v5 ads for 8 reactivated groups:',
    '',
    ...commanderDataset.restored_groups.map((gid) => `- ${gid}: ad-${gid}-a1 from v5 registry`),
  ].join('\n')
);

fs.writeFileSync(path.join(PROD, 'direct-commander-production-dataset-v7.json'), JSON.stringify(commanderDataset, null, 2));

const collisionVal = {
  validated_at: new Date().toISOString(),
  version: 'v7',
  ...collisionEvidence.summary,
  pairs_tested_by_level: {
    global: collisionEvidence.summary.pairs_tested_global,
    direction: collisionEvidence.summary.pairs_tested_direction,
    group_cross: collisionEvidence.summary.pairs_tested_group_cross,
    inline: collisionEvidence.summary.pairs_tested_inline,
  },
  findings_before_package: collisionEvidence.summary.literal_collisions_before,
  actions_applied: v6ToV7Restorations.length + v6ToV7Exclusions.length + 1,
  findings_after: collisionEvidence.summary.literal_collisions_after,
  final_status: collisionEvidence.summary.final_status,
  blocking_collisions: collisionEvidence.summary.literal_collisions_after,
  unresolved_semantic_risks: collisionEvidence.summary.semantic_risks_after,
  unresolved_unique_negative_risks: riskPass.summary.unresolved_count,
  outcome: collisionEvidence.summary.final_status === 'PASS' && riskPass.summary.unresolved_count === 0 ? 'PASS' : 'BLOCKED',
};
fs.writeFileSync(path.join(VAL, 'collision-evidence-v7.json'), JSON.stringify(collisionEvidence, null, 2));
fs.writeFileSync(path.join(VAL, 'negative-collision-validation-v7.json'), JSON.stringify(collisionVal, null, 2));
fs.writeFileSync(
  path.join(VAL, 'negative-collision-validation-v7.md'),
  [
    '# Negative Collision Validation v7',
    '',
    '| Metric | Value |',
    '|--------|------:|',
    `| Pairs tested | ${collisionEvidence.summary.total_pairs_tested} |`,
    `| Literal before | ${collisionEvidence.summary.literal_collisions_before} |`,
    `| Literal after | ${collisionEvidence.summary.literal_collisions_after} |`,
    `| Unresolved unique negatives | ${riskPass.summary.unresolved_count} |`,
    `| **Status** | **${collisionVal.outcome}** |`,
  ].join('\n')
);

fs.writeFileSync(path.join(VAL, 'semantic-validation-v7.json'), JSON.stringify(semanticValidation, null, 2));
fs.writeFileSync(path.join(VAL, 'semantic-validation-v7.md'), `# Semantic Validation v7\n\n**Passed:** ${semanticValidation.passed}\n`);

fs.writeFileSync(
  path.join(VAL, 'group-validation-v7.json'),
  JSON.stringify(
    {
      validated_at: new Date().toISOString(),
      active_groups: groupsPayload.length,
      held_groups: heldGroupsPayload.length,
      restored_groups: commanderDataset.restored_groups.length,
      checks: {
        every_group_has_keywords: groupsPayload.every((g) => g.keywords.length > 0),
        every_group_has_ads: groupsPayload.every((g) => g.ads.length > 0),
        every_group_has_url: groupsPayload.every((g) => g.planned_url),
        markers_present: groupsPayload.every((g) => g.direction_marker),
        all_restored_groups_exported: commanderDataset.restored_groups.every((gid) =>
          groupsPayload.some((g) => g.group_id === gid)
        ),
      },
      passed: groupsPayload.every((g) => g.keywords.length > 0 && g.ads.length > 0 && g.planned_url) && commanderDataset.restored_groups.length === 8,
    },
    null,
    2
  )
);
fs.writeFileSync(path.join(VAL, 'group-validation-v7.md'), `# Group Validation v7\n\nActive groups: ${groupsPayload.length}\nRestored: ${commanderDataset.restored_groups.length}\n`);

fs.writeFileSync(
  path.join(VAL, 'negative-validation-v7.json'),
  JSON.stringify(
    {
      validated_at: new Date().toISOString(),
      unresolved_unique_negatives: riskPass.summary.unresolved_count,
      blocking_collisions: collisionEvidence.summary.literal_collisions_after,
      unresolved_semantic_risks: collisionEvidence.summary.semantic_risks_after,
      passed: riskPass.summary.unresolved_count === 0 && collisionEvidence.summary.literal_collisions_after === 0,
    },
    null,
    2
  )
);
fs.writeFileSync(path.join(VAL, 'negative-validation-v7.md'), `# Negative Validation v7\n\nUnresolved: ${riskPass.summary.unresolved_count}\n`);

fs.writeFileSync(
  path.join(VAL, 'controlled-test-validation-v7.json'),
  JSON.stringify(
    {
      validated_at: new Date().toISOString(),
      controlled_tests: controlledTestsFinal.length,
      hypothesis_mismatches: hypothesisMismatches.length,
      passed: hypothesisMismatches.length === 0,
    },
    null,
    2
  )
);
fs.writeFileSync(path.join(VAL, 'controlled-test-validation-v7.md'), `# Controlled Test Validation v7\n\nMismatches: ${hypothesisMismatches.length}\n`);

fs.writeFileSync(
  path.join(VAL, 'ad-validation-v7.json'),
  JSON.stringify({ validated_at: new Date().toISOString(), passed: adEvidence.passed, ads: finalAds.length }, null, 2)
);
fs.writeFileSync(path.join(VAL, 'ad-validation-v7.md'), `# Ad Validation v7\n\n**Passed:** ${adEvidence.passed}\n`);

fs.writeFileSync(path.join(VAL, 'operator-scope-coverage-v7.json'), JSON.stringify(scopeCoverage, null, 2));
fs.writeFileSync(
  path.join(VAL, 'operator-scope-coverage-v7.md'),
  [
    '# Operator Scope Coverage v7',
    '',
    `**Outcome:** ${scopeCoverage.outcome}`,
    `Service families: ${scopeCoverage.service_families_represented}/${scopeCoverage.service_families_total}`,
    `Commercial seed loss: ${scopeCoverage.commercial_seed_loss}`,
    `Restored groups: ${scopeCoverage.restored_groups.length}`,
  ].join('\n')
);

fs.writeFileSync(path.join(VAL, 'status-reason-consistency-v7.json'), JSON.stringify(statusConsistency, null, 2));
fs.writeFileSync(
  path.join(VAL, 'status-reason-consistency-v7.md'),
  `# Status/Reason Consistency v7\n\n**Outcome:** ${statusConsistency.outcome}\nIssues: ${statusConsistency.issues.length}\n`
);

fs.writeFileSync(path.join(VAL, 'report-export-consistency-v7.json'), JSON.stringify(consistency, null, 2));
fs.writeFileSync(path.join(VAL, 'report-export-consistency-v7.md'), `# Report Export Consistency v7\n\n**Passed:** ${consistency.passed}\n`);

const allGatesPass =
  semanticValidation.passed &&
  consistency.passed &&
  riskPass.summary.unresolved_count === 0 &&
  adEvidence.passed &&
  collisionEvidence.summary.final_status === 'PASS' &&
  scopeCoverage.outcome === 'PASS' &&
  statusConsistency.passed &&
  hypothesisMismatches.length === 0;

fs.writeFileSync(
  path.join(VAL, 'direct-commander-v7-validation.json'),
  JSON.stringify(
    {
      validated_at: new Date().toISOString(),
      version: 'v7',
      status: allGatesPass ? 'PASS' : 'BLOCKED',
      gates: {
        semantic: semanticValidation.passed,
        group: groupsPayload.every((g) => g.keywords.length > 0 && g.ads.length > 0),
        operator_scope: scopeCoverage.outcome === 'PASS',
        status_reason: statusConsistency.passed,
        controlled_tests: hypothesisMismatches.length === 0,
        negative: riskPass.summary.unresolved_count === 0,
        collision: collisionEvidence.summary.final_status === 'PASS',
        ad_evidence: adEvidence.passed,
        consistency: consistency.passed,
      },
    },
    null,
    2
  )
);
fs.copyFileSync(
  path.join(VAL, 'direct-commander-v7-validation.json'),
  path.join(VAL, 'direct-commander-validation-v7.json')
);
fs.writeFileSync(
  path.join(VAL, 'direct-commander-validation-v7.md'),
  `# Direct Commander Validation v7\n\n**Status:** ${allGatesPass ? 'PASS' : 'BLOCKED'}\n`
);

const landingHandoff = {
  handoff_id: 'corv-landing-handoff-v7',
  generated_at: new Date().toISOString(),
  unified_utm_campaign: commanderDataset.unified_campaign.utm_campaign,
  status: 'NOT STARTED — AFTER OPERATOR V7 REVIEW AND DRY-RUN',
  prohibited_claims: [
    'официальный партнёр 1С',
    'сертифицированная команда',
    '24/7',
    'гарантированный результат',
    'гарантированные сроки',
    'бесплатно',
    'любой сложности',
    'без потери данных',
    'срочно',
  ],
  restored_groups: commanderDataset.restored_groups,
  pages: (commanderDataset.urls || []).map((u) => ({
    landing_id: u.landing_id,
    url: u.final_planned_url,
    groups: u.groups,
    active_groups: u.groups.filter((gid) => groupsPayload.some((g) => g.group_id === gid)),
    status: 'PLANNED URL — landing copy not started',
  })),
};
fs.writeFileSync(path.join(PROD, 'landing-copy-handoff-v7.json'), JSON.stringify(landingHandoff, null, 2));

console.log(
  JSON.stringify(
    {
      version: 'v7',
      active_keywords: finalKeywords.length,
      active_groups: groupsPayload.length,
      restored_groups: commanderDataset.restored_groups.length,
      exclusions_v7: v6ToV7Exclusions.length,
      restorations_v7: v6ToV7Restorations.length,
      collision_status: collisionEvidence.summary.final_status,
      scope_coverage: scopeCoverage.outcome,
      all_gates: allGatesPass,
    },
    null,
    2
  )
);

export { commanderDataset, allGatesPass, ROOT, result };
