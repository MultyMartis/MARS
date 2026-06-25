/**
 * Corvonero Unified Commander v5 — evidence audit production pipeline.
 * Run: node tools/run-full-production-v5.mjs
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { GROUPS, CAMPAIGNS, TIER_LIMITS, DOMAIN } from './lib/groups-config.mjs';
import {
  GLOBAL_NEGATIVES_V3,
  DIRECTION_NEGATIVES_V3,
  buildSafeCrossNegativeMap,
  buildSafeGroupNegatives,
  buildFinalNegativeRegistryV3,
  BASE_CROSS_NEGATIVES_V3,
} from './lib/negatives-config-v3.mjs';
import { assignBid, scoreKeywordFactors } from './lib/bids.mjs';
import { normPhrase, stripInlineNegatives } from './lib/keyword-classifier-v2.mjs';
import {
  DIRECTION_MARKERS,
  DIRECTION_LABELS,
  UNIFIED_UTM_CAMPAIGN,
  UNIFIED_CAMPAIGN_ID,
  UNIFIED_CAMPAIGN_NAME,
  formatGroupExportName,
} from './lib/campaign-markers.mjs';
import { filterSafeNegatives } from './lib/collision-engine-v3.mjs';
import {
  buildSemanticEvidenceRegistry,
  isActiveDecision,
  reviewsToMarkdown,
} from './lib/semantic-evidence-v5.mjs';
import {
  resolveAllNegativeRisks,
  applyNegativeResolutions,
  resolutionsToMarkdown,
} from './lib/negative-risk-resolution-v5.mjs';
import {
  buildCollisionEvidenceV5,
  negativeRegistryWithEvidence,
} from './lib/collision-evidence-v5.mjs';
import {
  buildFinalAdsV5,
  auditAllAdsEvidence,
  buildGroupAssignmentAudit,
} from './lib/ad-evidence-v5.mjs';
import { validateReportExportConsistency } from './lib/workbook-integrity-v5.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const V4_DATASET = path.join(ROOT, 'production/direct-commander-production-dataset-v4.json');
const V4_SEMANTIC = path.join(ROOT, 'production/semantic-human-review-v4.json');

const PHRASE_INLINE_NEGATIVES_V5 = {
  'CORV-G01-01': ['вакансия', 'обучение', 'курсы', 'резюме', 'как стать'],
};

const v4Dataset = JSON.parse(fs.readFileSync(V4_DATASET, 'utf8'));
const v4Semantic = JSON.parse(fs.readFileSync(V4_SEMANTIC, 'utf8'));
const v4KwById = new Map(v4Dataset.keywords.map((k) => [k.keyword_id, k]));

/** Audit input: all v4-reviewed phrases */
const inputKeywords = v4Semantic.reviews.map((r) => {
  const kw = v4KwById.get(r.keyword_id) || {
    keyword_id: r.keyword_id,
    group_id: r.group_id,
    source_phrase: r.positive_phrase,
    ad_phrase: r.positive_phrase,
    normalized_phrase: normPhrase(r.positive_phrase),
  };
  return { ...kw, group_id: r.group_id, source_phrase: r.positive_phrase || kw.source_phrase };
});

const semanticRegistry = buildSemanticEvidenceRegistry(inputKeywords, {
  reviewed_at: new Date().toISOString(),
});
const reviewById = new Map(semanticRegistry.reviews.map((r) => [r.keyword_id, r]));

const assignedNorm = new Map();
const groupKeywords = new Map(GROUPS.map((g) => [g.id, []]));
const rejectLog = [];
const v4ToV5Exclusions = [];

for (const kw of inputKeywords) {
  const review = reviewById.get(kw.keyword_id);
  if (!review || !isActiveDecision(review)) {
    if (review) v4ToV5Exclusions.push(review);
    rejectLog.push({
      keyword_id: kw.keyword_id,
      phrase: review?.positive_phrase || kw.source_phrase,
      group_id: kw.group_id,
      decision: review?.final_decision || 'EXCLUDE IRRELEVANT',
      reason: review?.phrase_specific_reason || 'no_review',
    });
    continue;
  }

  const gid = review.assigned_group;
  const np = review.normalized_phrase;
  if (assignedNorm.has(np)) {
    rejectLog.push({
      keyword_id: kw.keyword_id,
      phrase: np,
      group_id: gid,
      decision: 'EXCLUDE DUPLICATE',
      reason: `owned_by_${assignedNorm.get(np)}`,
    });
    continue;
  }

  assignedNorm.set(np, gid);
  const g = GROUPS.find((x) => x.id === gid);
  if (!g) continue;

  groupKeywords.get(gid).push({
    ...kw,
    group_id: gid,
    source_phrase: review.positive_phrase,
    normalized_phrase: np,
    ad_phrase: review.positive_phrase,
    _review: review,
    _classification: {
      status: review.final_decision === 'CONTROLLED TEST' ? 'KEEP_TEST' : 'KEEP',
      reason: review.phrase_specific_reason,
    },
  });
}

const { audits: groupAssignmentAudits, reassignments } = buildGroupAssignmentAudit(semanticRegistry.reviews);

const activeGroups = GROUPS.filter((g) => groupKeywords.get(g.id).length > 0);
const heldGroups = GROUPS.filter((g) => groupKeywords.get(g.id).length === 0);

const groupViability = GROUPS.map((g) => {
  const count = groupKeywords.get(g.id).length;
  let status = 'ACTIVE';
  if (count === 0) status = 'HOLD — NO VALID COMMERCIAL DEMAND';
  else if (count <= 2) status = 'ACTIVE NARROW';
  else if (count <= 3) status = 'CONTROLLED TEST';
  return {
    group_id: g.id,
    campaign_id: g.campaign,
    direction_marker: DIRECTION_MARKERS[g.campaign],
    group_name: g.name,
    keyword_count: count,
    viability_status: status,
    export_to_xlsx: count > 0,
  };
});

const finalKeywords = [];
const campaignById = Object.fromEntries(CAMPAIGNS.map((c) => [c.id, c]));

for (const g of activeGroups) {
  const list = groupKeywords.get(g.id);
  list.sort((a, b) => (a.normalized_phrase || '').localeCompare(b.normalized_phrase || '', 'ru'));

  list.forEach((k, idx) => {
    const factors = scoreKeywordFactors(k, g);
    let tier = g.bid;
    if (k._classification?.status === 'KEEP_TEST' || k._review?.final_decision === 'CONTROLLED TEST') {
      tier = tier === 'T1' ? 'T2' : tier === 'T2' ? 'T3' : 'T4';
    }
    const bid = assignBid(tier, idx + 1, list.length, factors);
    const inlineNeg = PHRASE_INLINE_NEGATIVES_V5[g.id] || [];
    const adPhrase =
      inlineNeg.length && idx === 0
        ? `${k.source_phrase} ${inlineNeg.map((n) => `-${n}`).join(' ')}`.trim()
        : k.source_phrase;

    finalKeywords.push({
      keyword_id: k.keyword_id,
      campaign_id: g.campaign,
      direction_id: g.campaign,
      direction_marker: DIRECTION_MARKERS[g.campaign],
      group_id: g.id,
      source_phrase: k.source_phrase,
      ad_phrase: adPhrase,
      normalized_phrase: k.normalized_phrase,
      classification: k._classification?.status || 'KEEP',
      semantic_decision: k._review?.final_decision,
      semantic_confidence: k._review?.commercial_confidence,
      group_fit_confidence: k._review?.group_fit_confidence,
      evidence_source: k.keyword_id,
      intent: g.intent,
      status: 'active',
      phrase_negatives: inlineNeg,
      bid_tier: bid.tier,
      final_bid: bid.final_bid,
      rationale_code: bid.rationale_code,
      planned_url: `${DOMAIN}${g.url}`,
      ad_id: `ad-${g.id}-a1`,
      is_primary: idx === 0,
    });
  });
}

const finalAds = buildFinalAdsV5(activeGroups, UNIFIED_UTM_CAMPAIGN);
const adEvidence = auditAllAdsEvidence(finalAds);

const rawCrossMap = { ...BASE_CROSS_NEGATIVES_V3 };
const { map: safeCrossMapPre, removalLog: crossRemovalLog } = buildSafeCrossNegativeMap(activeGroups, finalKeywords);
const globalFiltered = filterSafeNegatives(GLOBAL_NEGATIVES_V3, finalKeywords, { level: 'global' });
const globalRemovalLog = globalFiltered.removed;

let globalNegativesFinal = globalFiltered.safe;
let crossNegativesFinal = { ...safeCrossMapPre };
let directionNegativesFinal = { ...DIRECTION_NEGATIVES_V3 };

const riskPass1 = resolveAllNegativeRisks({
  finalKeywords,
  globalNegatives: globalNegativesFinal,
  directionNegatives: directionNegativesFinal,
  crossNegatives: crossNegativesFinal,
  phraseInlineNegatives: PHRASE_INLINE_NEGATIVES_V5,
});

const applied = applyNegativeResolutions(
  crossNegativesFinal,
  globalNegativesFinal,
  directionNegativesFinal,
  riskPass1.resolutions
);
globalNegativesFinal = applied.globalNegatives;
crossNegativesFinal = applied.crossNegatives;
directionNegativesFinal = applied.directionNegatives;

const { map: safeCrossMap, removalLog: crossRemovalLog2 } = buildSafeCrossNegativeMap(activeGroups, finalKeywords);
for (const [gid, tokens] of Object.entries(safeCrossMap)) {
  crossNegativesFinal[gid] = tokens;
}

const negativeRemovalLog = [
  ...crossRemovalLog.flatMap((x) => x.removed || []),
  ...crossRemovalLog2.flatMap((x) => x.removed || []),
  ...globalRemovalLog.map((r) => ({ ...r, scope: 'global' })),
  ...riskPass1.resolutions.filter((r) => r.decision === 'REMOVE').map((r) => ({
    negative: r.negative,
    level: r.level,
    group_id: r.applied_scope,
    reason: r.explanation,
    correction_type: r.decision === 'REMOVE' && r.explanation.includes('Literal') ? 'literal_collision' : 'semantic_risk_correction',
  })),
];

const finalNegativesBase = buildFinalNegativeRegistryV3(crossNegativesFinal, PHRASE_INLINE_NEGATIVES_V5);
const negativesQA = negativeRegistryWithEvidence(finalNegativesBase, finalKeywords, riskPass1);

const logicalDirections = CAMPAIGNS.map((c) => ({
  id: c.id,
  marker: DIRECTION_MARKERS[c.id],
  label: DIRECTION_LABELS[c.id],
  name: c.name,
  groups: GROUPS.filter((g) => g.campaign === c.id).map((g) => g.id),
  active_groups: activeGroups.filter((g) => g.campaign === c.id).map((g) => g.id),
  held_groups: heldGroups.filter((g) => g.campaign === c.id).map((g) => g.id),
  direction_negatives: directionNegativesFinal[c.id] || [],
}));

let exportGroupNumber = 0;
const groupsPayload = activeGroups.map((g) => {
  exportGroupNumber += 1;
  const camp = campaignById[g.campaign];
  const kws = finalKeywords.filter((k) => k.group_id === g.id);
  const ads = finalAds.filter((a) => a.group_id === g.id);
  const safeNeg = buildSafeGroupNegatives(g.id, kws, g.campaign);
  const viability = groupViability.find((v) => v.group_id === g.id);

  return {
    group_id: g.id,
    group_number: exportGroupNumber,
    campaign_id: g.campaign,
    direction_marker: DIRECTION_MARKERS[g.campaign],
    group_export_name: formatGroupExportName(g.campaign, g.name),
    bid_tier: g.bid,
    landing_page_id: g.landing,
    planned_url: `${DOMAIN}${g.url}`,
    viability_status: viability?.viability_status || 'ACTIVE',
    group_negatives: safeNeg.group_negatives,
    group_negatives_commander: safeNeg.group_negatives_commander,
    direction_negatives: safeNeg.direction_negatives_applied,
    cross_negatives: safeNeg.cross_negatives,
    keywords: kws,
    ads,
  };
});

const collisionEvidence = buildCollisionEvidenceV5({
  finalKeywords,
  groupsPayload,
  globalNegatives: globalNegativesFinal,
  directionNegatives: directionNegativesFinal,
  crossNegatives: crossNegativesFinal,
  phraseInlineNegatives: PHRASE_INLINE_NEGATIVES_V5,
  groups: GROUPS,
  negativeRemovalLog,
  riskResolutions: riskPass1,
  rawCrossBeforeFilter: rawCrossMap,
  globalBeforeFilter: GLOBAL_NEGATIVES_V3,
});

const heldGroupsPayload = heldGroups.map((g) => ({
  group_id: g.id,
  campaign_id: g.campaign,
  direction_marker: DIRECTION_MARKERS[g.campaign],
  group_name: g.name,
  planned_url: `${DOMAIN}${g.url}`,
  viability_status: 'HOLD — NO VALID COMMERCIAL DEMAND',
  export_to_xlsx: false,
}));

const v4PhraseSet = new Set(v4Dataset.keywords.map((k) => k.normalized_phrase));
const v5PhraseSet = new Set(finalKeywords.map((k) => k.normalized_phrase));

const v4ToV5Changes = [
  ...v4Dataset.keywords
    .filter((k) => !v5PhraseSet.has(k.normalized_phrase))
    .map((k) => {
      const r = reviewById.get(k.keyword_id);
      return {
        keyword_id: k.keyword_id,
        phrase: k.normalized_phrase,
        group_id: k.group_id,
        change: 'EXCLUDED_OR_REASSIGNED_OUT',
        v5_group: r?.assigned_group,
        decision: r?.final_decision,
        reason: r?.phrase_specific_reason?.slice(0, 200),
      };
    }),
  ...finalKeywords
    .filter((k) => !v4PhraseSet.has(k.normalized_phrase))
    .map((k) => ({
      keyword_id: k.keyword_id,
      phrase: k.normalized_phrase,
      group_id: k.group_id,
      change: 'ADDED_OR_RETAINED',
      decision: k.semantic_decision,
    })),
  ...reassignments.map((r) => ({
    keyword_id: r.keyword_id,
    phrase: r.phrase,
    group_id: r.new_group,
    change: 'REASSIGNED',
    previous_group: r.previous_group,
    reason: r.semantic_reason,
  })),
];

const commanderDataset = {
  dataset_id: 'corv-direct-commander-production-dataset-v5',
  generated_at: new Date().toISOString(),
  project_id: 'corvonero-yandex-direct',
  domain: DOMAIN,
  export_model: 'UNIFIED_SINGLE_CAMPAIGN',
  audit_input: {
    v4_status: 'REJECTED BY OPERATOR — EVIDENCE QA FAILURE',
    v4_dataset: 'direct-commander-production-dataset-v4.json',
  },
  unified_campaign: {
    id: UNIFIED_CAMPAIGN_ID,
    name: UNIFIED_CAMPAIGN_NAME,
    utm_campaign: UNIFIED_UTM_CAMPAIGN,
    campaign_negatives: globalNegativesFinal,
  },
  logical_directions: logicalDirections,
  campaigns: CAMPAIGNS,
  groups: groupsPayload,
  held_groups: heldGroupsPayload,
  global_negatives: globalNegativesFinal,
  direction_negatives: directionNegativesFinal,
  cross_negatives: crossNegativesFinal,
  phrase_inline_negatives: PHRASE_INLINE_NEGATIVES_V5,
  negatives: negativesQA,
  keywords: finalKeywords,
  excluded_keywords: rejectLog,
  ads: finalAds,
  urls: v4Dataset.urls,
  group_viability: groupViability,
  semantic_evidence_ref: 'production/semantic-evidence-review-v5.json',
  group_assignment_ref: 'production/group-assignment-audit-v5.json',
  negative_risk_ref: 'production/negative-risk-resolution-v5.json',
  collision_evidence_ref: 'production/validation/collision-evidence-v5.json',
  ad_evidence_ref: 'production/ad-evidence-audit-v5.json',
  collision_validation: collisionEvidence.summary,
  ad_evidence_qa: { passed: adEvidence.passed, changes: adEvidence.changes.length },
  manual_settings: v4Dataset.manual_settings,
  v4_to_v5_changes: v4ToV5Changes,
};

const prodDir = path.join(ROOT, 'production');
const valDir = path.join(prodDir, 'validation');
const auditDir = path.join(prodDir, 'audit');
[prodDir, valDir, auditDir].forEach((d) => fs.mkdirSync(d, { recursive: true }));

fs.writeFileSync(path.join(prodDir, 'semantic-evidence-review-v5.json'), JSON.stringify(semanticRegistry, null, 2));
fs.writeFileSync(path.join(prodDir, 'semantic-evidence-review-v5.md'), reviewsToMarkdown(semanticRegistry));

fs.writeFileSync(
  path.join(prodDir, 'group-assignment-audit-v5.json'),
  JSON.stringify(
    {
      audit_id: 'corv-group-assignment-v5',
      generated_at: new Date().toISOString(),
      audits: groupAssignmentAudits,
      reassignments,
      unresolved: groupAssignmentAudits.filter((a) => a.verdict === 'NEEDS_REVIEW').length,
    },
    null,
    2
  )
);

fs.writeFileSync(
  path.join(prodDir, 'group-assignment-audit-v5.md'),
  `# Group Assignment Audit v5\n\nReassignments: ${reassignments.length}\n\n${reassignments.map((r) => `- \`${r.phrase}\` ${r.previous_group} → ${r.new_group}: ${r.semantic_reason}`).join('\n')}\n`
);

fs.writeFileSync(
  path.join(prodDir, 'group-reassignment-log-v5.md'),
  reassignments.map((r) => `| ${r.phrase} | ${r.previous_group} | ${r.new_group} | ${r.semantic_reason} | ${r.negative_logic_impact} |`).join('\n')
);

fs.writeFileSync(
  path.join(prodDir, 'negative-risk-resolution-v5.json'),
  JSON.stringify({ resolution_id: 'corv-neg-risk-v5', ...riskPass1 }, null, 2)
);
fs.writeFileSync(path.join(prodDir, 'negative-risk-resolution-v5.md'), resolutionsToMarkdown(riskPass1));

fs.writeFileSync(
  path.join(prodDir, 'final-negative-registry-v5.json'),
  JSON.stringify({ registry_id: 'corv-final-neg-v5', generated_at: new Date().toISOString(), negatives: negativesQA }, null, 2)
);

fs.writeFileSync(
  path.join(prodDir, 'final-keyword-registry-v5.json'),
  JSON.stringify(
    {
      registry_id: 'corv-final-kw-v5',
      generated_at: new Date().toISOString(),
      stats: {
        active_keywords: finalKeywords.length,
        active_groups: activeGroups.length,
        held_groups: heldGroups.length,
        reassignments: reassignments.length,
        exclusions_v5: rejectLog.length,
      },
      keywords: finalKeywords,
      reject_log: rejectLog,
    },
    null,
    2
  )
);

fs.writeFileSync(
  path.join(prodDir, 'final-ad-registry-v5.json'),
  JSON.stringify({ registry_id: 'corv-final-ad-v5', generated_at: new Date().toISOString(), ads: finalAds, evidence: adEvidence }, null, 2)
);

fs.writeFileSync(
  path.join(prodDir, 'ad-evidence-audit-v5.json'),
  JSON.stringify({ audit_id: 'corv-ad-evidence-v5', generated_at: new Date().toISOString(), ...adEvidence }, null, 2)
);

fs.writeFileSync(
  path.join(prodDir, 'ad-v4-to-v5-diff.md'),
  `# Ad v4→v5 diff\n\n${adEvidence.changes.map((c) => `- ${c.group_id}/${c.ad_id}: ${c.original_problem} → ${c.correction_applied}`).join('\n') || 'No ad text changes required.'}\n`
);

fs.writeFileSync(
  path.join(prodDir, 'final-conflict-negative-matrix-v5.md'),
  `# Conflict Negative Matrix v5\n\nGlobal: ${globalNegativesFinal.length}\nCross groups: ${Object.keys(crossNegativesFinal).length}\nRisk resolved: ${riskPass1.summary.unresolved_count === 0 ? 'YES' : 'NO'}\n`
);

fs.writeFileSync(path.join(prodDir, 'direct-commander-production-dataset-v5.json'), JSON.stringify(commanderDataset, null, 2));

fs.writeFileSync(path.join(valDir, 'collision-evidence-v5.json'), JSON.stringify(collisionEvidence, null, 2));
fs.writeFileSync(
  path.join(valDir, 'negative-collision-validation-v5.json'),
  JSON.stringify(
    {
      validated_at: new Date().toISOString(),
      ...collisionEvidence.summary,
      blocking_records_after: collisionEvidence.summary.literal_collisions_after,
      evidence_workbook_required: true,
    },
    null,
    2
  )
);

fs.writeFileSync(
  path.join(valDir, 'negative-collision-validation-v5.md'),
  `# Negative Collision Validation v5\n\n| Metric | Value |\n|--------|------:|\n| Pairs tested | ${collisionEvidence.summary.total_pairs_tested} |\n| Literal before | ${collisionEvidence.summary.literal_collisions_before} |\n| Literal after | ${collisionEvidence.summary.literal_collisions_after} |\n| Semantic risks after | ${collisionEvidence.summary.semantic_risks_after} |\n| Unresolved | ${collisionEvidence.summary.unresolved_count} |\n| **Status** | **${collisionEvidence.summary.final_status}** |\n`
);

const templateOnlyActive = semanticRegistry.reviews.filter(
  (r) =>
    isActiveDecision(r) &&
    (!r.phrase_specific_reason || r.phrase_specific_reason.length < 30 || r.review_status === 'RULE-SCREENED')
);

const semanticValidation = {
  validated_at: new Date().toISOString(),
  active_keywords: finalKeywords.length,
  checks: {
    all_active_phrase_specific: templateOnlyActive.length === 0,
    template_only_active_count: templateOnlyActive.length,
    low_confidence_active_commercial: finalKeywords.filter((k) => {
      const r = reviewById.get(k.keyword_id);
      return r?.commercial_confidence === 'LOW' && r?.final_decision === 'ACTIVE COMMERCIAL';
    }).length,
    unresolved_group_assignment: groupAssignmentAudits.filter((a) => a.verdict === 'NEEDS_REVIEW').length,
    negative_risk_unresolved: riskPass1.summary.unresolved_count,
    blocking_collisions: collisionEvidence.summary.literal_collisions_after,
  },
  passed:
    templateOnlyActive.length === 0 &&
    collisionEvidence.summary.final_status === 'PASS' &&
    adEvidence.passed &&
    riskPass1.summary.unresolved_count === 0,
};

fs.writeFileSync(path.join(valDir, 'semantic-evidence-validation-v5.json'), JSON.stringify(semanticValidation, null, 2));
fs.writeFileSync(
  path.join(valDir, 'group-assignment-validation-v5.json'),
  JSON.stringify(
    {
      validated_at: new Date().toISOString(),
      reassignments: reassignments.length,
      unresolved: groupAssignmentAudits.filter((a) => a.verdict === 'NEEDS_REVIEW').length,
      passed: groupAssignmentAudits.filter((a) => a.verdict === 'NEEDS_REVIEW').length === 0,
    },
    null,
    2
  )
);

fs.writeFileSync(
  path.join(valDir, 'negative-risk-validation-v5.json'),
  JSON.stringify({ validated_at: new Date().toISOString(), ...riskPass1.summary, passed: riskPass1.summary.unresolved_count === 0 }, null, 2)
);

fs.writeFileSync(
  path.join(valDir, 'ad-evidence-validation-v5.json'),
  JSON.stringify({ validated_at: new Date().toISOString(), passed: adEvidence.passed, failed_ads: adEvidence.records.filter((r) => r.final_status.includes('FAIL')).length }, null, 2)
);

const consistency = validateReportExportConsistency(
  commanderDataset,
  { keyword_count: finalKeywords.length, active_groups: activeGroups.length },
  collisionEvidence
);
fs.writeFileSync(path.join(valDir, 'report-export-consistency-v5.json'), JSON.stringify(consistency, null, 2));
fs.writeFileSync(
  path.join(valDir, 'report-export-consistency-v5.md'),
  `# Report Export Consistency v5\n\n**Passed:** ${consistency.passed}\n\nIssues: ${consistency.issues.length}\n`
);

const allGatesPass =
  semanticValidation.passed && consistency.passed && riskPass1.summary.unresolved_count === 0 && adEvidence.passed;

fs.writeFileSync(
  path.join(valDir, 'direct-commander-v5-validation.json'),
  JSON.stringify(
    {
      validated_at: new Date().toISOString(),
      version: 'v5',
      status: allGatesPass ? 'PASS' : 'BLOCKED',
      gates: {
        semantic: semanticValidation.passed,
        group_assignment: groupAssignmentAudits.filter((a) => a.verdict === 'NEEDS_REVIEW').length === 0,
        negative_risk: riskPass1.summary.unresolved_count === 0,
        collision: collisionEvidence.summary.final_status === 'PASS',
        ad_evidence: adEvidence.passed,
        consistency: consistency.passed,
      },
    },
    null,
    2
  )
);

fs.writeFileSync(
  path.join(prodDir, 'orca-production-method-improvements-v5.md'),
  `# ORCA Production Method Improvements — v5\n\n1. Generated per-phrase record ≠ human evidence unless phrase-specific reason.\n2. Confidence cannot default HIGH from group membership.\n3. Commerciality and group ownership are separate gates.\n4. Literal collision and semantic-risk checks are separate.\n5. Preventive negative changes classified as semantic_risk_correction.\n6. Unresolved warnings block PASS.\n7. Operator workbooks are controlled deliverables.\n8. Placeholder/debug data invalidates QA.\n9. Report claims must reconcile with rows and XLSX.\n10. Final QA validates exported artefacts.\n`
);

console.log('Production v5 registries written.');
console.log(
  JSON.stringify(
    {
      active_keywords: finalKeywords.length,
      reassignments: reassignments.length,
      exclusions: rejectLog.length,
      negative_risk_unresolved: riskPass1.summary.unresolved_count,
      collision_status: collisionEvidence.summary.final_status,
      all_gates: allGatesPass,
    },
    null,
    2
  )
);

export { commanderDataset, allGatesPass, ROOT, semanticValidation, collisionEvidence, adEvidence, riskPass1 };
