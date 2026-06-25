/**
 * Corvonero Unified Commander v6 — apply repair package and rebuild production.
 * Run: node tools/run-full-production-v6.mjs
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { applyV6RepairPackage, loadJson, EDUCATION_PHRASES } from './lib/v6-repair-apply.mjs';
import { normPhrase } from './lib/keyword-classifier-v2.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const PROD = path.join(ROOT, 'production');
const VAL = path.join(PROD, 'validation');
const AUDIT = path.join(PROD, 'audit');
const EXPORTS = path.join(ROOT, 'exports');
const ARTIFACTS = path.join(ROOT, 'artifacts');

[PROD, VAL, AUDIT, EXPORTS, ARTIFACTS].forEach((d) => fs.mkdirSync(d, { recursive: true }));

const v5Dataset = loadJson(path.join(PROD, 'direct-commander-production-dataset-v5.json'));
const v5Semantic = loadJson(path.join(PROD, 'semantic-evidence-review-v5.json'));
const repairPkg = loadJson(path.join(PROD, 'repair/v6-production-input-package.json'));
const negResolutionFinal = loadJson(path.join(PROD, 'repair/v5-negative-resolution-final.json'));
const collisionActionsFinal = loadJson(path.join(PROD, 'repair/v5-collision-actions-final.json'));
const qaGate = loadJson(path.join(VAL, 'v5-qa-repair-gate-v2.json'));

if (!String(qaGate.final_result || '').includes('PASS')) {
  console.error('V5 QA Repair Gate v2 is not PASS — aborting v6 production.');
  process.exit(1);
}

const result = applyV6RepairPackage({
  v5Dataset,
  v5Semantic,
  repairPkg,
  negResolutionFinal,
  collisionActionsFinal,
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
  v5ToV6Exclusions,
  v5ToV6Changes,
  bidSummary,
  semanticValidation,
  consistency,
  resolutionsToMarkdown,
} = result;

fs.writeFileSync(
  path.join(AUDIT, 'version-lifecycle-status.json'),
  JSON.stringify(
    {
      registered_at: new Date().toISOString(),
      v5_qa_repair_gate_v2: 'PASSED',
      commander_v5: 'REJECTED — SUPERSEDED BY V6 PRODUCTION',
      review_workbook_v5: 'REJECTED — SUPERSEDED BY V6 PRODUCTION',
      v6_production: 'IN PRODUCTION',
      commander_dry_run: 'AUTHORIZED — OPERATOR REVIEW PENDING',
      moderation: 'NOT AUTHORIZED',
      launch: 'NOT AUTHORIZED',
      campaign_split: 'DEFERRED',
      landing_copy: 'NOT STARTED',
      note: 'v1–v5 artefacts preserved unchanged; v6 is current production target.',
    },
    null,
    2
  )
);

const kwRegistry = {
  registry_id: 'corv-final-kw-v6',
  generated_at: new Date().toISOString(),
  stats: {
    active_keywords: finalKeywords.length,
    active_groups: groupsPayload.length,
    held_groups: heldGroupsPayload.length,
    exclusions_v6: v5ToV6Exclusions.length,
    controlled_tests: commanderDataset.controlled_tests.length,
    v5_active_before: v5Dataset.keywords.length,
  },
  keywords: finalKeywords.map((k) => ({
    keyword_id: k.keyword_id,
    raw_phrase: k.source_phrase,
    positive_phrase: k.ad_phrase,
    final_status: k.semantic_decision,
    final_group: k.group_id,
    final_decision_reason: k.final_decision_reason,
    commercial_confidence: k.commercial_confidence,
    controlled_test_hypothesis: k.controlled_test_hypothesis,
    noise_risk: k.noise_risk,
    bid_tier: k.bid_tier,
    final_bid: k.final_bid,
    ad_mapping: k.ad_id,
    landing_mapping: k.planned_url,
  })),
  reject_log: commanderDataset.excluded_keywords,
};
fs.writeFileSync(path.join(PROD, 'final-keyword-registry-v6.json'), JSON.stringify(kwRegistry, null, 2));
fs.writeFileSync(
  path.join(PROD, 'final-keyword-registry-v6.md'),
  [
    '# Final Keyword Registry v6',
    '',
    `Active keywords: **${finalKeywords.length}**`,
    `Exclusions applied from v5: **${v5ToV6Exclusions.length}**`,
    `Controlled tests: **${commanderDataset.controlled_tests.length}**`,
    '',
    '## Education exclusions (verified absent from export)',
    '',
    ...[...EDUCATION_PHRASES].map((p) => `- \`${p}\` — EXCLUDED`),
  ].join('\n')
);
fs.writeFileSync(
  path.join(PROD, 'keyword-v5-to-v6-diff.md'),
  [
    '# Keyword v5→v6 diff',
    '',
    '| Metric | v5 | v6 |',
    '|--------|---:|---:|',
    `| Active keywords | ${v5Dataset.keywords.length} | ${finalKeywords.length} |`,
    `| Exclusions added | — | ${v5ToV6Exclusions.length} |`,
    '',
    '## Excluded in v6',
    '',
    '| phrase | group | v5 status | v6 status | reason |',
    '|--------|-------|-----------|-----------|--------|',
    ...v5ToV6Exclusions.map(
      (e) => `| ${e.phrase} | ${e.group_id} | ${e.v5_status} | ${e.v6_status} | ${e.reason} |`
    ),
  ].join('\n')
);

const groupRegistry = {
  registry_id: 'corv-final-group-v6',
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
  })),
  held_groups: heldGroupsPayload,
  viability: groupViability,
};
fs.writeFileSync(path.join(PROD, 'final-group-registry-v6.json'), JSON.stringify(groupRegistry, null, 2));
fs.writeFileSync(
  path.join(PROD, 'final-group-registry-v6.md'),
  [
    '# Final Group Registry v6',
    '',
    `Active exported groups: **${groupsPayload.length}**`,
    `Held groups: **${heldGroupsPayload.length}**`,
    '',
    ...groupsPayload.map(
      (g) => `- \`${g.group_id}\` ${g.group_export_name} — ${g.viability_status} (${g.keywords.length} kw)`
    ),
  ].join('\n')
);
fs.writeFileSync(
  path.join(PROD, 'group-v5-to-v6-diff.md'),
  [
    '# Group v5→v6 diff',
    '',
    `| Metric | v5 | v6 |`,
    `|--------|---:|---:|`,
    `| Active groups | ${v5Dataset.groups.length} | ${groupsPayload.length} |`,
    `| Held groups | ${(v5Dataset.held_groups || []).length} | ${heldGroupsPayload.length} |`,
    '',
    'No group merges in repair package; viability recalculated after keyword exclusions.',
  ].join('\n')
);

fs.writeFileSync(
  path.join(PROD, 'final-negative-registry-v6.json'),
  JSON.stringify(
    {
      registry_id: 'corv-final-neg-v6',
      generated_at: new Date().toISOString(),
      repair_refs: {
        v5_negative_resolution_final: 'production/repair/v5-negative-resolution-final.json',
        collision_actions: 'production/repair/v5-collision-actions-final.json',
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
  path.join(PROD, 'final-conflict-negative-matrix-v6.md'),
  [
    '# Conflict Negative Matrix v6',
    '',
    `Global negatives: ${commanderDataset.global_negatives.length}`,
    `Unresolved unique negatives: ${riskPass.summary.unresolved_count}`,
    `Blocking collisions after repair: ${collisionEvidence.summary.literal_collisions_after}`,
    `Final status: **${collisionEvidence.summary.final_status}**`,
  ].join('\n')
);
fs.writeFileSync(
  path.join(PROD, 'negative-v5-to-v6-diff.md'),
  [
    '# Negative v5→v6 diff',
    '',
    `Repair package removals applied: ${(repairPkg.negative_removals || []).length}`,
    `Exact collision actions: ${(repairPkg.exact_collision_actions || []).length}`,
    `Global negatives v5→v6: ${v5Dataset.global_negatives.length} → ${commanderDataset.global_negatives.length}`,
  ].join('\n')
);

fs.writeFileSync(path.join(PROD, 'semantic-evidence-review-v6.json'), JSON.stringify(semanticRegistry, null, 2));
fs.writeFileSync(
  path.join(PROD, 'semantic-evidence-review-v6.md'),
  `# Semantic Evidence Review v6\n\nReviews: ${semanticRegistry.reviews.length}\nActive exported: ${finalKeywords.length}\n`
);

fs.writeFileSync(
  path.join(PROD, 'final-ad-registry-v6.json'),
  JSON.stringify(
    { registry_id: 'corv-final-ad-v6', generated_at: new Date().toISOString(), ads: finalAds, evidence: adEvidence },
    null,
    2
  )
);
fs.writeFileSync(
  path.join(PROD, 'final-ad-registry-v6.md'),
  [
    '# Final Ad Registry v6',
    '',
    `Ads: ${finalAds.length}`,
    `Evidence passed: ${adEvidence.passed}`,
    `Changes from v5: ${adEvidence.changes.length}`,
  ].join('\n')
);
fs.writeFileSync(
  path.join(PROD, 'ad-v5-to-v6-diff.md'),
  adEvidence.changes.length
    ? adEvidence.changes.map((c) => `- ${c.group_id}/${c.ad_id}: ${c.original_problem}`).join('\n')
    : '# Ad v5→v6 diff\n\nNo ad text changes required — group mappings unchanged after repair.'
);

fs.writeFileSync(path.join(PROD, 'direct-commander-production-dataset-v6.json'), JSON.stringify(commanderDataset, null, 2));

fs.writeFileSync(path.join(VAL, 'collision-evidence-v6.json'), JSON.stringify(collisionEvidence, null, 2));
fs.writeFileSync(
  path.join(VAL, 'negative-collision-validation-v6.json'),
  JSON.stringify(
    {
      validated_at: new Date().toISOString(),
      version: 'v6',
      ...collisionEvidence.summary,
      pairs_tested_by_level: {
        global: collisionEvidence.summary.pairs_tested_global,
        direction: collisionEvidence.summary.pairs_tested_direction,
        group_cross: collisionEvidence.summary.pairs_tested_group_cross,
        inline: collisionEvidence.summary.pairs_tested_inline,
      },
      findings_before_package: collisionEvidence.summary.literal_collisions_before,
      actions_applied: (repairPkg.exact_collision_actions || []).length + (repairPkg.negative_removals || []).length,
      findings_after: collisionEvidence.summary.literal_collisions_after,
      final_status: collisionEvidence.summary.final_status,
      blocking_collisions: collisionEvidence.summary.literal_collisions_after,
      unresolved_semantic_risks: collisionEvidence.summary.semantic_risks_after,
      unresolved_unique_negative_risks: riskPass.summary.unresolved_count,
    },
    null,
    2
  )
);
fs.writeFileSync(
  path.join(VAL, 'negative-collision-validation-v6.md'),
  [
    '# Negative Collision Validation v6',
    '',
    '| Metric | Value |',
    '|--------|------:|',
    `| Pairs tested | ${collisionEvidence.summary.total_pairs_tested} |`,
    `| Literal before | ${collisionEvidence.summary.literal_collisions_before} |`,
    `| Literal after | ${collisionEvidence.summary.literal_collisions_after} |`,
    `| Semantic risks after | ${collisionEvidence.summary.semantic_risks_after} |`,
    `| Unresolved unique negatives | ${riskPass.summary.unresolved_count} |`,
    `| **Status** | **${collisionEvidence.summary.final_status}** |`,
  ].join('\n')
);

fs.writeFileSync(path.join(VAL, 'semantic-validation-v6.json'), JSON.stringify(semanticValidation, null, 2));
fs.writeFileSync(
  path.join(VAL, 'semantic-validation-v6.md'),
  `# Semantic Validation v6\n\n**Passed:** ${semanticValidation.passed}\n`
);

fs.writeFileSync(
  path.join(VAL, 'group-validation-v6.json'),
  JSON.stringify(
    {
      validated_at: new Date().toISOString(),
      active_groups: groupsPayload.length,
      held_groups: heldGroupsPayload.length,
      checks: {
        every_group_has_keywords: groupsPayload.every((g) => g.keywords.length > 0),
        every_group_has_ads: groupsPayload.every((g) => g.ads.length > 0),
        every_group_has_url: groupsPayload.every((g) => g.planned_url),
        markers_present: groupsPayload.every((g) => g.direction_marker),
      },
      passed: groupsPayload.every((g) => g.keywords.length > 0 && g.ads.length > 0 && g.planned_url),
    },
    null,
    2
  )
);
fs.writeFileSync(
  path.join(VAL, 'group-validation-v6.md'),
  `# Group Validation v6\n\nActive groups: ${groupsPayload.length}\n`
);

fs.writeFileSync(
  path.join(VAL, 'negative-validation-v6.json'),
  JSON.stringify(
    {
      validated_at: new Date().toISOString(),
      unresolved_unique_negatives: riskPass.summary.unresolved_count,
      blocking_collisions: collisionEvidence.summary.literal_collisions_after,
      unresolved_semantic_risks: collisionEvidence.summary.semantic_risks_after,
      passed:
        riskPass.summary.unresolved_count === 0 && collisionEvidence.summary.literal_collisions_after === 0,
    },
    null,
    2
  )
);
fs.writeFileSync(
  path.join(VAL, 'negative-validation-v6.md'),
  `# Negative Validation v6\n\nUnresolved: ${riskPass.summary.unresolved_count}\nBlocking: ${collisionEvidence.summary.literal_collisions_after}\n`
);

fs.writeFileSync(
  path.join(VAL, 'ad-validation-v6.json'),
  JSON.stringify(
    { validated_at: new Date().toISOString(), passed: adEvidence.passed, ads: finalAds.length },
    null,
    2
  )
);
fs.writeFileSync(path.join(VAL, 'ad-validation-v6.md'), `# Ad Validation v6\n\n**Passed:** ${adEvidence.passed}\n`);

fs.writeFileSync(path.join(VAL, 'report-export-consistency-v6.json'), JSON.stringify(consistency, null, 2));
fs.writeFileSync(
  path.join(VAL, 'report-export-consistency-v6.md'),
  `# Report Export Consistency v6\n\n**Passed:** ${consistency.passed}\n`
);

const allGatesPass =
  semanticValidation.passed &&
  consistency.passed &&
  riskPass.summary.unresolved_count === 0 &&
  adEvidence.passed &&
  collisionEvidence.summary.final_status === 'PASS';

fs.writeFileSync(
  path.join(VAL, 'direct-commander-v6-validation.json'),
  JSON.stringify(
    {
      validated_at: new Date().toISOString(),
      version: 'v6',
      status: allGatesPass ? 'PASS' : 'BLOCKED',
      gates: {
        semantic: semanticValidation.passed,
        group: groupsPayload.every((g) => g.keywords.length > 0 && g.ads.length > 0),
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

// Landing copy handoff v6
const landingHandoff = {
  handoff_id: 'corv-landing-handoff-v6',
  generated_at: new Date().toISOString(),
  unified_utm_campaign: commanderDataset.unified_campaign.utm_campaign,
  status: 'NOT STARTED — AFTER OPERATOR V6 REVIEW AND DRY-RUN',
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
    'под ключ (unless separately confirmed)',
  ],
  pages: (commanderDataset.urls || []).map((u) => ({
    landing_id: u.landing_id,
    url: u.final_planned_url,
    groups: u.groups,
    active_groups: u.groups.filter((gid) => groupsPayload.some((g) => g.group_id === gid)),
    status: 'PLANNED URL — landing copy not started',
  })),
};
fs.writeFileSync(path.join(PROD, 'landing-copy-handoff-v6.json'), JSON.stringify(landingHandoff, null, 2));

console.log(
  JSON.stringify(
    {
      version: 'v6',
      active_keywords: finalKeywords.length,
      exclusions_v6: v5ToV6Exclusions.length,
      active_groups: groupsPayload.length,
      education_leakage: semanticValidation.checks.career_education_leakage,
      collision_status: collisionEvidence.summary.final_status,
      all_gates: allGatesPass,
    },
    null,
    2
  )
);

export { commanderDataset, allGatesPass, ROOT, result };
