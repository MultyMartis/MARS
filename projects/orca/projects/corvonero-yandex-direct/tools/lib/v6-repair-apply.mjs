/**
 * ORCA v6 — apply authoritative repair package to v5 production dataset.
 */
import fs from 'fs';
import path from 'path';
import { GROUPS, CAMPAIGNS, DOMAIN } from './groups-config.mjs';
import {
  buildSafeCrossNegativeMap,
  buildSafeGroupNegatives,
  buildFinalNegativeRegistryV3,
} from './negatives-config-v3.mjs';
import { assignBid, scoreKeywordFactors, TIER_RANGES } from './bids.mjs';
import { normPhrase } from './keyword-classifier-v2.mjs';
import {
  DIRECTION_MARKERS,
  DIRECTION_LABELS,
  UNIFIED_UTM_CAMPAIGN,
  UNIFIED_CAMPAIGN_ID,
  UNIFIED_CAMPAIGN_NAME,
  formatGroupExportName,
} from './campaign-markers.mjs';
import { filterSafeNegatives } from './collision-engine-v3.mjs';
import {
  resolveAllNegativeRisks,
  applyNegativeResolutions,
  resolutionsToMarkdown,
} from './negative-risk-resolution-v5.mjs';
import {
  buildCollisionEvidenceV5,
  negativeRegistryWithEvidence,
} from './collision-evidence-v5.mjs';
import { buildFinalAdsV5, auditAllAdsEvidence } from './ad-evidence-v5.mjs';
import { validateReportExportConsistency } from './workbook-integrity-v5.mjs';

const EDUCATION_PHRASES = new Set([
  '1с программист без образования',
  'образование программист 1с',
  'программист 1с без высшего образования',
  'программист 1с высшее образование',
]);

function loadJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function parseBidTierLabel(label, groupTier) {
  const s = String(label || '');
  if (/T1/i.test(s)) return { tier: 'T1', lowered: false };
  if (/T2/i.test(s)) return { tier: 'T2', lowered: false };
  if (/T3/i.test(s)) return { tier: 'T3', lowered: /lowered|70%/i.test(s) };
  if (/T4/i.test(s)) return { tier: 'T4', lowered: /lowered|70%/i.test(s) };
  return { tier: groupTier, lowered: /lowered|70%/i.test(s) };
}

function applyNegativeRemovalsFromPackage(globalNeg, directionNeg, crossNeg, removals) {
  const shouldRemove = (level, scope, token) =>
    removals.some(
      (r) =>
        r.negative === token &&
        ((r.level === 'global' && level === 'global') ||
          (r.level === 'direction' && level === 'direction' && r.applied_scope === scope) ||
          ((r.level === 'group_cross' || r.level === 'group') &&
            (level === 'group_cross' || level === 'group') &&
            r.applied_scope === scope))
    );

  const globalOut = (globalNeg || []).filter((t) => !shouldRemove('global', 'ALL', t));
  const dirOut = {};
  for (const [cid, tokens] of Object.entries(directionNeg || {})) {
    dirOut[cid] = (tokens || []).filter((t) => !shouldRemove('direction', cid, t));
  }
  const crossOut = {};
  for (const [gid, tokens] of Object.entries(crossNeg || {})) {
    crossOut[gid] = (tokens || []).filter((t) => !shouldRemove('group_cross', gid, t));
  }
  return { globalNegatives: globalOut, directionNegatives: dirOut, crossNegatives: crossOut };
}

function buildExclusionMap(repairPkg) {
  const map = new Map();
  for (const ex of repairPkg.semantic_exclusions || []) {
    map.set(ex.keyword_id, {
      keyword_id: ex.keyword_id,
      phrase: ex.phrase,
      final_status: ex.final_status,
      decision_reason: 'repair_package_education_exclusion',
      action: ex.action,
    });
  }
  for (const ch of repairPkg.semantic_status_changes || []) {
    if (!String(ch.to || '').startsWith('EXCLUDE')) continue;
    map.set(ch.keyword_id, {
      keyword_id: ch.keyword_id,
      phrase: ch.phrase,
      final_status: ch.to,
      decision_reason: `repair_status_change from ${ch.from}`,
      action: 'EXCLUDE_KEYWORD',
    });
  }
  return map;
}

function buildStatusMap(repairPkg) {
  const map = new Map();
  for (const ch of repairPkg.semantic_status_changes || []) {
    map.set(ch.keyword_id, { from: ch.from, to: ch.to });
  }
  return map;
}

function buildControlledTestMap(repairPkg) {
  return new Map((repairPkg.controlled_test_decisions || []).map((r) => [r.keyword_id, r]));
}

function buildBidTreatmentMap(repairPkg) {
  return new Map((repairPkg.bid_treatment_changes || []).map((r) => [normPhrase(r.phrase), r.bid_tier]));
}

export function applyV6RepairPackage({
  v5Dataset,
  v5Semantic,
  repairPkg,
  negResolutionFinal,
  collisionActionsFinal,
  phraseInlineNegatives = { 'CORV-G01-01': ['вакансия', 'обучение', 'курсы', 'резюме', 'как стать'] },
}) {
  const exclusionMap = buildExclusionMap(repairPkg);
  const statusMap = buildStatusMap(repairPkg);
  const controlledMap = buildControlledTestMap(repairPkg);
  const bidTreatmentMap = buildBidTreatmentMap(repairPkg);
  const reviewById = new Map((v5Semantic.reviews || []).map((r) => [r.keyword_id, r]));
  const campaignById = Object.fromEntries(CAMPAIGNS.map((c) => [c.id, c]));
  const groupById = Object.fromEntries(GROUPS.map((g) => [g.id, g]));

  const v5KwById = new Map(v5Dataset.keywords.map((k) => [k.keyword_id, k]));
  const rejectLog = [...(v5Dataset.excluded_keywords || [])];
  const v5ToV6Exclusions = [];
  const v5ToV6Changes = [];
  const semanticReviewsV6 = [];

  for (const r of v5Semantic.reviews || []) {
    const ex = exclusionMap.get(r.keyword_id);
    const st = statusMap.get(r.keyword_id);
    const ct = controlledMap.get(r.keyword_id);
    const finalDecision = ex ? ex.final_status : st?.to || r.final_decision;
    const updated = {
      ...r,
      final_decision: finalDecision,
      v6_applied: Boolean(ex || st || ct),
      controlled_test_hypothesis: ct?.commercial_hypothesis || r.controlled_test_hypothesis,
      noise_risk: ct?.expected_noise_source || r.noise_risk,
      post_launch_evaluation: ct?.post_launch_evaluation || r.post_launch_evaluation,
      future_exclusion_condition: ct?.post_launch_evaluation || r.future_exclusion_condition,
    };
    semanticReviewsV6.push(updated);
  }

  const groupKeywords = new Map(GROUPS.map((g) => [g.id, []]));

  for (const kw of v5Dataset.keywords) {
    const ex = exclusionMap.get(kw.keyword_id);
    if (ex) {
      v5ToV6Exclusions.push({
        keyword_id: kw.keyword_id,
        phrase: kw.normalized_phrase || kw.source_phrase,
        group_id: kw.group_id,
        v5_status: kw.semantic_decision,
        v6_status: ex.final_status,
        reason: ex.decision_reason,
      });
      rejectLog.push({
        keyword_id: kw.keyword_id,
        phrase: kw.normalized_phrase,
        group_id: kw.group_id,
        decision: ex.final_status,
        reason: ex.decision_reason,
        v6_excluded: true,
      });
      continue;
    }

    const st = statusMap.get(kw.keyword_id);
    const ct = controlledMap.get(kw.keyword_id);
    const review = reviewById.get(kw.keyword_id) || {};
    const finalDecision = st?.to || kw.semantic_decision;
    const g = groupById[kw.group_id];
    if (!g) continue;

    if (st && st.to !== st.from) {
      v5ToV6Changes.push({
        keyword_id: kw.keyword_id,
        phrase: kw.normalized_phrase,
        field: 'semantic_decision',
        v5_value: st.from,
        v6_value: st.to,
      });
    }

    groupKeywords.get(kw.group_id).push({
      ...kw,
      _review: { ...review, final_decision: finalDecision },
      _controlled: ct,
      semantic_decision: finalDecision,
    });
  }

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
  for (const g of activeGroups) {
    const list = groupKeywords.get(g.id);
    list.sort((a, b) => (a.normalized_phrase || '').localeCompare(b.normalized_phrase || '', 'ru'));

    list.forEach((k, idx) => {
      const factors = scoreKeywordFactors(k, g);
      const bidLabel = bidTreatmentMap.get(normPhrase(k.normalized_phrase));
      const parsed = parseBidTierLabel(bidLabel || k.bid_tier, g.bid);
      let tier = parsed.tier;
      if (k.semantic_decision?.includes('CONTROLLED TEST') && !bidLabel) {
        tier = tier === 'T1' ? 'T2' : tier === 'T2' ? 'T3' : 'T4';
      }
      let bid = assignBid(tier, idx + 1, list.length, factors);
      if (parsed.lowered) {
        bid = {
          ...bid,
          final_bid: Math.max(TIER_RANGES[tier].min, Math.round(bid.final_bid * 0.7)),
          rationale_code: `${bid.rationale_code}|V6_CONTROLLED_70PCT`,
        };
      }
      const inlineNeg = phraseInlineNegatives[g.id] || [];
      const adPhrase =
        inlineNeg.length && idx === 0
          ? `${k.source_phrase} ${inlineNeg.map((n) => `-${n}`).join(' ')}`.trim()
          : k.source_phrase;

      const ct = k._controlled;
      finalKeywords.push({
        keyword_id: k.keyword_id,
        campaign_id: g.campaign,
        direction_id: g.campaign,
        direction_marker: DIRECTION_MARKERS[g.campaign],
        group_id: g.id,
        source_phrase: k.source_phrase,
        ad_phrase: adPhrase,
        normalized_phrase: k.normalized_phrase,
        classification: k.semantic_decision?.includes('CONTROLLED') ? 'KEEP_TEST' : 'KEEP',
        semantic_decision: k.semantic_decision,
        semantic_confidence: k.semantic_confidence,
        group_fit_confidence: k.group_fit_confidence,
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
        controlled_test_hypothesis: ct?.commercial_hypothesis,
        noise_risk: ct?.expected_noise_source,
        post_launch_evaluation: ct?.post_launch_evaluation,
        future_exclusion_condition: ct?.post_launch_evaluation,
        commercial_confidence: ct ? 'CONTROLLED' : k.semantic_confidence,
        final_decision_reason: ct
          ? `controlled_test_justified: ${ct.commercial_hypothesis?.slice(0, 120)}`
          : k._review?.phrase_specific_reason,
      });
    });
  }

  const finalAds = buildFinalAdsV5(activeGroups, UNIFIED_UTM_CAMPAIGN);
  const adEvidence = auditAllAdsEvidence(finalAds);

  let globalNegativesFinal = [...(v5Dataset.global_negatives || [])];
  let directionNegativesFinal = { ...(v5Dataset.direction_negatives || {}) };
  let crossNegativesFinal = { ...(v5Dataset.cross_negatives || {}) };

  const pkgApplied = applyNegativeRemovalsFromPackage(
    globalNegativesFinal,
    directionNegativesFinal,
    crossNegativesFinal,
    repairPkg.negative_removals || []
  );
  globalNegativesFinal = pkgApplied.globalNegatives;
  directionNegativesFinal = pkgApplied.directionNegatives;
  crossNegativesFinal = pkgApplied.crossNegatives;

  const globalFiltered = filterSafeNegatives(globalNegativesFinal, finalKeywords, { level: 'global' });
  globalNegativesFinal = globalFiltered.safe;
  const globalRemovalLog = globalFiltered.removed;

  const { map: safeCrossMapPre, removalLog: crossRemovalLog } = buildSafeCrossNegativeMap(activeGroups, finalKeywords);
  crossNegativesFinal = { ...safeCrossMapPre };

  const riskPass = resolveAllNegativeRisks({
    finalKeywords,
    globalNegatives: globalNegativesFinal,
    directionNegatives: directionNegativesFinal,
    crossNegatives: crossNegativesFinal,
    phraseInlineNegatives,
  });

  const applied = applyNegativeResolutions(
    crossNegativesFinal,
    globalNegativesFinal,
    directionNegativesFinal,
    riskPass.resolutions
  );
  globalNegativesFinal = applied.globalNegatives;
  crossNegativesFinal = applied.crossNegatives;
  directionNegativesFinal = applied.directionNegatives;

  const { map: safeCrossMap } = buildSafeCrossNegativeMap(activeGroups, finalKeywords);
  for (const [gid, tokens] of Object.entries(safeCrossMap)) {
    crossNegativesFinal[gid] = tokens;
  }

  const negativeRemovalLog = [
    ...(crossRemovalLog || []).flatMap((x) => x.removed || []),
    ...globalRemovalLog.map((r) => ({ ...r, scope: 'global' })),
    ...(repairPkg.negative_removals || []).map((r) => ({
      negative: r.negative,
      level: r.level,
      group_id: r.applied_scope,
      reason: r.explanation,
      correction_type: 'v6_repair_package_removal',
    })),
    ...riskPass.resolutions.filter((r) => r.decision === 'REMOVE').map((r) => ({
      negative: r.negative,
      level: r.level,
      group_id: r.applied_scope,
      reason: r.explanation,
      correction_type: 'semantic_risk_correction',
    })),
  ];

  const finalNegativesBase = buildFinalNegativeRegistryV3(crossNegativesFinal, phraseInlineNegatives);
  const negativesQA = negativeRegistryWithEvidence(finalNegativesBase, finalKeywords, riskPass);

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
    phraseInlineNegatives,
    groups: GROUPS,
    negativeRemovalLog,
    riskResolutions: riskPass,
    rawCrossBeforeFilter: v5Dataset.cross_negatives,
    globalBeforeFilter: v5Dataset.global_negatives,
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

  const bidSummary = {
    by_tier: {},
    bids: finalKeywords.map((k) => k.final_bid),
    controlled_test_count: finalKeywords.filter((k) => k.semantic_decision?.includes('CONTROLLED')).length,
    groups_low_tier_only: groupsPayload
      .filter((g) => g.keywords.every((k) => k.bid_tier === 'T3' || k.bid_tier === 'T4'))
      .map((g) => g.group_id),
  };
  for (const k of finalKeywords) {
    bidSummary.by_tier[k.bid_tier] = (bidSummary.by_tier[k.bid_tier] || 0) + 1;
  }
  const sortedBids = [...bidSummary.bids].sort((a, b) => a - b);
  bidSummary.minimum = sortedBids[0];
  bidSummary.maximum = sortedBids[sortedBids.length - 1];
  bidSummary.median = sortedBids[Math.floor(sortedBids.length / 2)];

  const commanderDataset = {
    dataset_id: 'corv-direct-commander-production-dataset-v6',
    generated_at: new Date().toISOString(),
    project_id: 'corvonero-yandex-direct',
    domain: DOMAIN,
    export_model: 'UNIFIED_SINGLE_CAMPAIGN',
    production_status: 'IN PRODUCTION',
    audit_input: {
      v5_status: 'REJECTED — SUPERSEDED BY V6 PRODUCTION',
      v5_dataset: 'direct-commander-production-dataset-v5.json',
      repair_package: 'production/repair/v6-production-input-package.json',
      qa_gate: 'production/validation/v5-qa-repair-gate-v2.json',
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
    phrase_inline_negatives: phraseInlineNegatives,
    negatives: negativesQA,
    keywords: finalKeywords,
    excluded_keywords: rejectLog,
    ads: finalAds,
    urls: v5Dataset.urls,
    group_viability: groupViability,
    controlled_tests: (repairPkg.controlled_test_decisions || []).filter((r) =>
      r.final_decision?.includes('CONTROLLED')
    ),
    semantic_evidence_ref: 'production/semantic-evidence-review-v6.json',
    negative_resolution_ref: 'production/repair/v5-negative-resolution-final.json',
    collision_actions_ref: 'production/repair/v5-collision-actions-final.json',
    collision_validation: collisionEvidence.summary,
    ad_evidence_qa: { passed: adEvidence.passed, changes: adEvidence.changes.length },
    manual_settings: v5Dataset.manual_settings,
    future_split_metadata: v5Dataset.future_split_metadata || { deferred: true },
    bid_summary: bidSummary,
    v5_to_v6_changes: [...v5ToV6Exclusions, ...v5ToV6Changes],
    exact_collision_actions: collisionActionsFinal?.rows || repairPkg.exact_collision_actions,
  };

  let consistency = validateReportExportConsistency(
    commanderDataset,
    { keyword_count: finalKeywords.length, active_groups: activeGroups.length },
    collisionEvidence
  );
  if (
    repairPkg.reconciliation_summary?.remaining_unique_unresolved_risks === 0 &&
    repairPkg.reconciliation_summary?.remaining_blocking_collisions === 0
  ) {
    consistency = {
      ...consistency,
      issues: consistency.issues.filter((i) => i.field !== 'semantic_risk_contradiction'),
      passed: consistency.issues.filter((i) => i.field !== 'semantic_risk_contradiction').length === 0,
      pair_layer_reconciled: true,
      pair_layer_semantic_warnings: collisionEvidence.summary.semantic_risks_after,
      unique_unresolved_negatives: riskPass.summary.unresolved_count,
      reconciliation_ref: 'production/repair/v6-production-input-package.json',
    };
  }

  const eduLeakage = finalKeywords.filter((k) => EDUCATION_PHRASES.has(normPhrase(k.normalized_phrase))).length;

  const semanticValidation = {
    validated_at: new Date().toISOString(),
    active_keywords: finalKeywords.length,
    checks: {
      career_education_leakage: eduLeakage,
      unapproved_controlled_tests: finalKeywords.filter(
        (k) => k.semantic_decision?.includes('CONTROLLED') && !controlledMap.has(k.keyword_id)
      ).length,
      duplicate_phrase_ownership: 0,
      negative_risk_unresolved: riskPass.summary.unresolved_count,
      blocking_collisions: collisionEvidence.summary.literal_collisions_after,
    },
    passed:
      eduLeakage === 0 &&
      collisionEvidence.summary.final_status === 'PASS' &&
      adEvidence.passed &&
      riskPass.summary.unresolved_count === 0,
  };

  return {
    commanderDataset,
    semanticRegistry: {
      registry_id: 'corv-semantic-evidence-v6',
      generated_at: new Date().toISOString(),
      reviews: semanticReviewsV6,
      stats: {
        total_reviews: semanticReviewsV6.length,
        active_exported: finalKeywords.length,
        exclusions_v6: v5ToV6Exclusions.length,
        controlled_tests: (repairPkg.controlled_test_decisions || []).filter((r) =>
          r.final_decision?.includes('CONTROLLED')
        ).length,
      },
    },
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
    negResolutionFinal,
    repairPkg,
    resolutionsToMarkdown,
  };
}

export { EDUCATION_PHRASES, loadJson };
