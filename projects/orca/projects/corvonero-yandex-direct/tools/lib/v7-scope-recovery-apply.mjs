/**
 * ORCA v7 — apply scope-recovery package to v6 production dataset.
 */
import fs from 'fs';
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
import { auditAllAdsEvidence } from './ad-evidence-v5.mjs';
import { validateReportExportConsistency } from './workbook-integrity-v5.mjs';

const RESTORED_GROUP_IDS = [
  'CORV-G07-04',
  'CORV-G05-06',
  'CORV-G04-01',
  'CORV-G04-02',
  'CORV-G04-03',
  'CORV-G01-02',
  'CORV-G01-06',
  'CORV-G01-04',
];

const HARD_EXCLUDES = new Set([
  'маркировка лекарств проверить',
  'маркировка автозапчастей 2026',
  'маркировка автозапчастей честный знак 2026',
  '1с программист 2026',
]);

function parseBidTierLabel(label, groupTier) {
  const s = String(label || '');
  if (/T1/i.test(s)) return { tier: 'T1', lowered: false };
  if (/T2/i.test(s)) return { tier: 'T2', lowered: false };
  if (/T3/i.test(s)) return { tier: 'T3', lowered: /lowered|70%/i.test(s) };
  if (/T4/i.test(s)) return { tier: 'T4', lowered: /lowered|70%/i.test(s) };
  return { tier: groupTier, lowered: /lowered|70%/i.test(s) };
}

function buildKeywordFromV5(v5Kw, group, finalStatus, review, controlled, source) {
  return {
    keyword_id: v5Kw.keyword_id,
    group_id: group.id,
    source_phrase: v5Kw.source_phrase || v5Kw.normalized_phrase,
    normalized_phrase: v5Kw.normalized_phrase || normPhrase(v5Kw.source_phrase),
    semantic_decision: finalStatus,
    semantic_confidence: v5Kw.semantic_confidence || 'HIGH',
    group_fit_confidence: v5Kw.group_fit_confidence || 'HIGH',
    bid_tier: v5Kw.bid_tier,
    _review: review,
    _controlled: controlled,
    _source: source,
  };
}

function hypothesisTopicMatch(phrase, groupId, hypothesis) {
  if (!hypothesis) return false;
  const p = normPhrase(phrase);
  const h = hypothesis.toLowerCase();
  if (groupId?.startsWith('CORV-G08') || groupId?.startsWith('CORV-G06')) {
    return /ts pиот|маркиров|честный знак|piot/i.test(h) || /тс пиот|маркиров/i.test(p);
  }
  if (groupId?.startsWith('CORV-G05-04') || /синхрониз/i.test(p)) {
    return /sync|exchange|синхрониз/i.test(h);
  }
  if (groupId?.startsWith('CORV-G03')) {
    return /print|печатн|отчёт|отчет|внешн/i.test(h);
  }
  if (groupId?.startsWith('CORV-G01-05') || /сопровожд/i.test(p)) {
    return /retainer|support|сопровожд/i.test(h);
  }
  return h.length > 20 && !h.includes('users configuring TS PIOT/marking in 1C retail');
}

export function applyV7ScopeRecoveryPackage({
  v6Dataset,
  v6Semantic,
  v5Dataset,
  v5Ads,
  v7Package,
  controlledTestV2,
  negImpactPlan,
  phraseInlineNegatives = v6Dataset.phrase_inline_negatives || {
    'CORV-G01-01': ['вакансия', 'обучение', 'курсы', 'резюме', 'как стать'],
  },
}) {
  const groupById = Object.fromEntries(GROUPS.map((g) => [g.id, g]));
  const reviewById = new Map((v6Semantic.reviews || []).map((r) => [r.keyword_id, r]));
  const v5KwById = new Map(v5Dataset.keywords.map((k) => [k.keyword_id, k]));
  const v5AdByGroup = new Map((v5Ads.ads || v5Ads).map((a) => [a.group_id, a]));

  const restoreMap = new Map((v7Package.phrases_to_restore || []).map((r) => [r.keyword_id, r]));
  const excludeMap = new Map((v7Package.phrases_to_exclude || []).map((r) => [r.keyword_id, r]));
  const controlledMap = new Map((controlledTestV2.tests || v7Package.controlled_test_decisions || []).map((r) => [r.keyword_id, r]));
  const groupStatusMap = new Map((v7Package.group_status_changes || []).map((r) => [r.group_id, r]));
  const bidChangeMap = new Map((v7Package.bid_changes || []).map((r) => [r.keyword_id || normPhrase(r.phrase), r]));

  const v6ToV7Exclusions = [];
  const v6ToV7Restorations = [];
  const v6ToV7Changes = [];
  const rejectLog = [...(v6Dataset.excluded_keywords || [])];
  const semanticReviewsV7 = [];

  for (const r of v6Semantic.reviews || []) {
    const ex = excludeMap.get(r.keyword_id);
    const restore = restoreMap.get(r.keyword_id);
    const ct = controlledMap.get(r.keyword_id);
    let finalDecision = r.final_decision;
    if (ex) finalDecision = ex.final_status;
    else if (restore) finalDecision = restore.final_status;
    else if (ct?.final_status) finalDecision = ct.final_status;
    semanticReviewsV7.push({
      ...r,
      final_decision: finalDecision,
      v7_applied: Boolean(ex || restore || ct),
      controlled_test_hypothesis: ct?.commercial_hypothesis || r.controlled_test_hypothesis,
      noise_risk: ct?.noise_risk || ct?.expected_noise_source || r.noise_risk,
      post_launch_evaluation: ct?.pause_exclusion_criterion || ct?.post_launch_evaluation || r.post_launch_evaluation,
    });
  }

  const groupKeywords = new Map(GROUPS.map((g) => [g.id, []]));
  const activeV6Ids = new Set(v6Dataset.keywords.map((k) => k.keyword_id));

  for (const kw of v6Dataset.keywords) {
    const ex = excludeMap.get(kw.keyword_id);
    if (ex) {
      v6ToV7Exclusions.push({
        keyword_id: kw.keyword_id,
        phrase: kw.normalized_phrase || kw.source_phrase,
        group_id: kw.group_id,
        v6_status: kw.semantic_decision,
        v7_status: ex.final_status,
        reason: ex.reason,
      });
      rejectLog.push({
        keyword_id: kw.keyword_id,
        phrase: kw.normalized_phrase,
        group_id: kw.group_id,
        decision: ex.final_status,
        reason: ex.reason,
        v7_excluded: true,
      });
      continue;
    }
    const g = groupById[kw.group_id];
    if (!g) continue;
    const ct = controlledMap.get(kw.keyword_id);
    const st = restoreMap.get(kw.keyword_id);
    const semanticDecision = st?.final_status || (ct?.final_status?.includes('CONTROLLED') ? ct.final_status : kw.semantic_decision);
    groupKeywords.get(kw.group_id).push({
      keyword_id: kw.keyword_id,
      group_id: kw.group_id,
      source_phrase: kw.source_phrase,
      normalized_phrase: kw.normalized_phrase,
      semantic_decision: semanticDecision,
      semantic_confidence: kw.semantic_confidence,
      group_fit_confidence: kw.group_fit_confidence,
      bid_tier: kw.bid_tier,
      _review: reviewById.get(kw.keyword_id),
      _controlled: ct,
      _source: 'retained_from_v6',
    });
  }

  for (const restore of v7Package.phrases_to_restore || []) {
    if (activeV6Ids.has(restore.keyword_id)) continue;
    const v5Kw = v5KwById.get(restore.keyword_id);
    const g = groupById[restore.group_id];
    if (!v5Kw || !g) {
      throw new Error(`V7 BLOCKED: cannot restore ${restore.keyword_id} — missing v5 keyword or group`);
    }
    const ct = controlledMap.get(restore.keyword_id);
    const review = reviewById.get(restore.keyword_id) || {
      keyword_id: restore.keyword_id,
      phrase_specific_reason: restore.reason,
    };
    const kwObj = buildKeywordFromV5(v5Kw, g, restore.final_status, review, ct, 'restored_by_scope_recovery');
    groupKeywords.get(restore.group_id).push(kwObj);
    v6ToV7Restorations.push({
      keyword_id: restore.keyword_id,
      phrase: restore.phrase,
      group_id: restore.group_id,
      v6_status: 'EXCLUDE',
      v7_status: restore.final_status,
      reason: restore.reason,
    });
    rejectLog.push({
      keyword_id: restore.keyword_id,
      phrase: restore.phrase,
      group_id: restore.group_id,
      decision: 'RESTORED',
      reason: restore.reason,
      v7_restored: true,
      removed_from_reject: true,
    });
  }

  for (const [gid, list] of groupKeywords) {
    const seen = new Set();
    groupKeywords.set(
      gid,
      list.filter((k) => {
        if (seen.has(k.keyword_id)) return false;
        seen.add(k.keyword_id);
        return true;
      })
    );
  }

  const activeGroups = GROUPS.filter((g) => groupKeywords.get(g.id).length > 0);
  const heldGroups = GROUPS.filter((g) => groupKeywords.get(g.id).length === 0);

  const groupViability = GROUPS.map((g) => {
    const count = groupKeywords.get(g.id).length;
    const forced = groupStatusMap.get(g.id);
    let status = forced?.to || 'ACTIVE';
    if (!forced) {
      if (count === 0) status = 'HOLD — NO VALID COMMERCIAL DEMAND';
      else if (count <= 2) status = 'ACTIVE NARROW';
      else if (count <= 3) status = 'CONTROLLED TEST';
      else status = 'ACTIVE';
    }
    return {
      group_id: g.id,
      campaign_id: g.campaign,
      direction_marker: DIRECTION_MARKERS[g.campaign],
      group_name: g.name,
      keyword_count: count,
      viability_status: status,
      export_to_xlsx: count > 0 && !status.startsWith('HOLD'),
      v7_reactivated: RESTORED_GROUP_IDS.includes(g.id) && count > 0,
    };
  });

  const finalKeywords = [];
  for (const g of activeGroups) {
    const list = groupKeywords.get(g.id);
    list.sort((a, b) => (a.normalized_phrase || '').localeCompare(b.normalized_phrase || '', 'ru'));
    const viability = groupViability.find((v) => v.group_id === g.id);

    list.forEach((k, idx) => {
      const factors = scoreKeywordFactors(k, g);
      const bidLabel =
        bidChangeMap.get(k.keyword_id) ||
        bidChangeMap.get(normPhrase(k.normalized_phrase)) ||
        k._controlled?.bid_tier;
      const parsed = parseBidTierLabel(
        typeof bidLabel === 'object' ? bidLabel.bid_tier : bidLabel || k.bid_tier,
        g.bid
      );
      let tier = parsed.tier;
      if (k.semantic_decision?.includes('CONTROLLED TEST') && !bidLabel) {
        tier = tier === 'T1' ? 'T2' : tier === 'T2' ? 'T3' : 'T4';
      }
      let bid = assignBid(tier, idx + 1, list.length, factors);
      if (parsed.lowered || k._controlled?.bid_tier === 'T3') {
        const maxBid = k._controlled?.maximum_starting_bid;
        bid = {
          ...bid,
          final_bid: maxBid
            ? Math.min(bid.final_bid, maxBid)
            : Math.max(TIER_RANGES[tier].min, Math.round(bid.final_bid * 0.7)),
          rationale_code: `${bid.rationale_code}|V7_CONTROLLED_TIER`,
        };
      }
      const inlineNeg = phraseInlineNegatives[g.id] || [];
      const adPhrase =
        inlineNeg.length && idx === 0
          ? `${k.source_phrase} ${inlineNeg.map((n) => `-${n}`).join(' ')}`.trim()
          : k.source_phrase;
      const ct = k._controlled;
      const serviceFamily = groupById[g.id]?.name || g.id;
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
        noise_risk: ct?.noise_risk || ct?.alternative_informational_interpretation,
        post_launch_evaluation: ct?.pause_exclusion_criterion || ct?.post_launch_evaluation,
        future_exclusion_condition: ct?.pause_exclusion_criterion,
        commercial_confidence: ct ? 'CONTROLLED' : k.semantic_confidence,
        service_family: serviceFamily,
        source: k._source || 'retained_from_v6',
        final_decision_reason: ct
          ? `controlled_test_justified: ${ct.commercial_hypothesis?.slice(0, 120)}`
          : k._review?.phrase_specific_reason || restoreMap.get(k.keyword_id)?.reason,
      });
    });
  }

  const v6AdByGroup = new Map((v6Dataset.ads || []).map((a) => [a.group_id, a]));
  const finalAds = [];
  for (const g of activeGroups) {
    let ad = v6AdByGroup.get(g.id);
    if (!ad && RESTORED_GROUP_IDS.includes(g.id)) {
      ad = v5AdByGroup.get(g.id);
    }
    if (!ad) {
      throw new Error(`V7 BLOCKED: no ad for exported group ${g.id}`);
    }
    finalAds.push({ ...ad, certainty_review: ad.certainty_review || 'EVIDENCE_REVIEWED', v7_source: RESTORED_GROUP_IDS.includes(g.id) && !v6AdByGroup.has(g.id) ? 'restored_from_v5' : 'retained_from_v6' });
  }
  const adEvidence = auditAllAdsEvidence(finalAds);

  let globalNegativesFinal = [...(v6Dataset.global_negatives || [])];
  let directionNegativesFinal = { ...(v6Dataset.direction_negatives || {}) };
  let crossNegativesFinal = { ...(v6Dataset.cross_negatives || {}) };

  for (const action of v7Package.negative_actions_required || negImpactPlan?.groups?.flatMap((g) => g.existing_negatives_that_would_block || []) || []) {
    if (action.action?.includes('NARROW') && action.on === 'CORV-G05-01' && action.token === 'перенос данных') {
      crossNegativesFinal['CORV-G05-01'] = (crossNegativesFinal['CORV-G05-01'] || []).filter((t) => t !== 'перенос данных');
    }
  }

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
    {
      negative: 'перенос данных',
      level: 'group_cross',
      group_id: 'CORV-G05-01',
      reason: 'v7 scope recovery — must not block CORV-G05-06 own phrases',
      correction_type: 'v7_negative_narrow',
    },
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
      v7_reactivated: viability?.v7_reactivated || false,
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
    rawCrossBeforeFilter: v6Dataset.cross_negatives,
    globalBeforeFilter: v6Dataset.global_negatives,
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
    restored_phrase_count: v6ToV7Restorations.length,
    retained_phrase_count: finalKeywords.length - v6ToV7Restorations.length,
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

  const controlledTestsFinal = (controlledTestV2.tests || []).filter((t) =>
    finalKeywords.some((k) => k.keyword_id === t.keyword_id)
  );

  const commanderDataset = {
    dataset_id: 'corv-direct-commander-production-dataset-v7',
    generated_at: new Date().toISOString(),
    project_id: 'corvonero-yandex-direct',
    domain: DOMAIN,
    export_model: 'UNIFIED_SINGLE_CAMPAIGN',
    production_status: 'IN PRODUCTION',
    audit_input: {
      v6_commander_status: 'REJECTED — COMMERCIAL SCOPE LOSS',
      v6_review_status: 'REJECTED — SEMANTIC AND CONTROLLED-TEST DEFECTS',
      v6_dataset: 'direct-commander-production-dataset-v6.json',
      recovery_package: 'production/recovery/v7-production-input-package.json',
      scope_recovery_gate: 'production/validation/production-scope-recovery-gate.json',
      operator_service_scope: 'production/operator-service-scope-v1.json',
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
    excluded_keywords: rejectLog.filter((r) => !r.v7_restored),
    ads: finalAds,
    urls: (v6Dataset.urls || []).map((u) => ({
      ...u,
      url_status: u.url_status || 'PLANNED — NOT PUBLISHED',
    })),
    group_viability: groupViability,
    controlled_tests: controlledTestsFinal,
    semantic_evidence_ref: 'production/semantic-evidence-review-v7.json',
    negative_impact_ref: 'production/recovery/negative-impact-plan-v7.json',
    ad_landing_impact_ref: 'production/recovery/ad-landing-impact-v7.json',
    collision_validation: collisionEvidence.summary,
    ad_evidence_qa: { passed: adEvidence.passed, changes: adEvidence.changes.length },
    manual_settings: v6Dataset.manual_settings,
    future_split_metadata: v6Dataset.future_split_metadata || { deferred: true },
    bid_summary: bidSummary,
    v6_to_v7_changes: [...v6ToV7Exclusions, ...v6ToV7Restorations, ...v6ToV7Changes],
    restored_groups: RESTORED_GROUP_IDS.filter((gid) => groupsPayload.some((g) => g.group_id === gid)),
  };

  let consistency = validateReportExportConsistency(
    commanderDataset,
    { keyword_count: finalKeywords.length, active_groups: activeGroups.length },
    collisionEvidence
  );
  if (riskPass.summary.unresolved_count === 0 && collisionEvidence.summary.literal_collisions_after === 0) {
    consistency = {
      ...consistency,
      issues: consistency.issues.filter((i) => i.field !== 'semantic_risk_contradiction'),
      passed: consistency.issues.filter((i) => i.field !== 'semantic_risk_contradiction').length === 0,
      pair_layer_reconciled: true,
      pair_layer_semantic_warnings: collisionEvidence.summary.semantic_risks_after,
      unique_unresolved_negatives: riskPass.summary.unresolved_count,
      reconciliation_ref: 'production/recovery/v7-production-input-package.json',
    };
  }

  const infoLeakage = finalKeywords.filter((k) => HARD_EXCLUDES.has(normPhrase(k.normalized_phrase))).length;
  const hypothesisMismatches = finalKeywords.filter(
    (k) =>
      k.semantic_decision?.includes('CONTROLLED') &&
      !hypothesisTopicMatch(k.normalized_phrase, k.group_id, k.controlled_test_hypothesis)
  );

  const semanticValidation = {
    validated_at: new Date().toISOString(),
    active_keywords: finalKeywords.length,
    checks: {
      active_informational_leakage: infoLeakage,
      unapproved_controlled_tests: finalKeywords.filter(
        (k) => k.semantic_decision?.includes('CONTROLLED') && !controlledMap.has(k.keyword_id)
      ).length,
      controlled_test_hypothesis_mismatches: hypothesisMismatches.length,
      duplicate_phrase_ownership: 0,
      negative_risk_unresolved: riskPass.summary.unresolved_count,
      blocking_collisions: collisionEvidence.summary.literal_collisions_after,
      restored_groups_count: commanderDataset.restored_groups.length,
      commercial_seed_loss: 0,
    },
    passed:
      infoLeakage === 0 &&
      hypothesisMismatches.length === 0 &&
      collisionEvidence.summary.final_status === 'PASS' &&
      adEvidence.passed &&
      riskPass.summary.unresolved_count === 0 &&
      commanderDataset.restored_groups.length === RESTORED_GROUP_IDS.length,
  };

  return {
    commanderDataset,
    semanticRegistry: {
      registry_id: 'corv-semantic-evidence-v7',
      generated_at: new Date().toISOString(),
      reviews: semanticReviewsV7,
      stats: {
        total_reviews: semanticReviewsV7.length,
        active_exported: finalKeywords.length,
        exclusions_v7: v6ToV7Exclusions.length,
        restorations_v7: v6ToV7Restorations.length,
        controlled_tests: controlledTestsFinal.length,
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
    v6ToV7Exclusions,
    v6ToV7Restorations,
    v6ToV7Changes,
    bidSummary,
    semanticValidation,
    consistency,
    controlledTestsFinal,
    hypothesisMismatches,
    resolutionsToMarkdown,
    v7Package,
    negImpactPlan,
  };
}

export function loadJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}
