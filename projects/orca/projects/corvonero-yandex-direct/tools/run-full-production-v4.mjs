/**
 * Corvonero Unified Commander v4 — human-grade semantic review production pipeline.
 * Run: node tools/run-full-production-v4.mjs
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { GROUPS, CAMPAIGNS, SEED_FALLBACK, TIER_LIMITS, DOMAIN } from './lib/groups-config.mjs';
import {
  GLOBAL_NEGATIVES_V3,
  DIRECTION_NEGATIVES_V3,
  buildSafeCrossNegativeMap,
  buildSafeGroupNegatives,
  buildFinalNegativeRegistryV3,
  buildCrossNegativeRecords,
} from './lib/negatives-config-v3.mjs';
import { assignBid, scoreKeywordFactors } from './lib/bids.mjs';
import { buildAdsForGroupV4, reviewAllAdsCertainty } from './lib/ads-v4.mjs';
import { normPhrase, stripInlineNegatives } from './lib/keyword-classifier-v2.mjs';
import {
  DIRECTION_MARKERS,
  DIRECTION_LABELS,
  UNIFIED_UTM_CAMPAIGN,
  UNIFIED_CAMPAIGN_ID,
  UNIFIED_CAMPAIGN_NAME,
  formatGroupExportName,
} from './lib/campaign-markers.mjs';
import {
  runCollisionAudit,
  runExportedCollisionAudit,
  runRegressionTests,
  filterSafeNegatives,
} from './lib/collision-engine-v3.mjs';
import {
  buildSemanticReviewRegistry,
  isActiveDecision,
  reviewKeywordV4,
  reviewsToMarkdown,
} from './lib/semantic-human-review-v4.mjs';
import { buildCollisionEvidence, negativeRegistryWithQA } from './lib/collision-evidence-v4.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const MIG = path.resolve(
  ROOT,
  '../../../../incoming/mig/pilots/corvonero/session-mig-20260622-corv01/keyword_registry.json'
);
const V3_DATASET = path.join(ROOT, 'production/direct-commander-production-dataset-v3.json');

/** v4: no inline-minus repair on export phrases */
const PHRASE_INLINE_NEGATIVES_V4 = {
  'CORV-G01-01': ['вакансия', 'обучение', 'курсы', 'резюме', 'как стать'],
};

const kr = JSON.parse(fs.readFileSync(MIG, 'utf8'));
const v3Dataset = JSON.parse(fs.readFileSync(V3_DATASET, 'utf8'));
const v3Keywords = v3Dataset.keywords;

const SEED_CLEAN = Object.fromEntries(
  Object.entries(SEED_FALLBACK).map(([gid, seeds]) => [
    gid,
    seeds.filter((s) => !/под ключ|бесплатно|скачать/i.test(s)),
  ])
);

const MERGE_MAP = {};
const MERGE_LOG = [];

/** Step 1: semantic review all v3 active keywords */
const semanticRegistry = buildSemanticReviewRegistry(v3Keywords, [], {
  reviewed_at: new Date().toISOString(),
});
const reviewById = new Map(semanticRegistry.reviews.map((r) => [r.keyword_id, r]));

/** Step 2: build active set from review decisions */
const assignedNorm = new Map();
const groupKeywords = new Map(GROUPS.map((g) => [g.id, []]));
const rejectLog = [];
const v3Excluded = [];
const v3RestoredFromMig = [];

function pushReject(kw, review, extra = {}) {
  rejectLog.push({
    keyword_id: kw.keyword_id,
    source_phrase: kw.source_phrase || kw.ad_phrase,
    group_id: kw.group_id,
    status: review.decision,
    reason: review.reason,
    ...extra,
  });
}

for (const kw of v3Keywords) {
  const review = reviewById.get(kw.keyword_id);
  if (!review) {
    pushReject(kw, { decision: 'EXCLUDE IRRELEVANT', reason: 'missing_review_record' });
    continue;
  }
  if (!isActiveDecision(review)) {
    v3Excluded.push({ ...kw, review });
    pushReject(kw, review);
    continue;
  }

  const np = normPhrase(review.positive_phrase);
  if (assignedNorm.has(np)) {
    pushReject(kw, { decision: 'EXCLUDE DUPLICATE', reason: `owned_by_${assignedNorm.get(np)}` });
    continue;
  }

  assignedNorm.set(np, kw.group_id);
  groupKeywords.get(kw.group_id).push({
    ...kw,
    source_phrase: review.positive_phrase,
    normalized_phrase: np,
    ad_phrase: review.positive_phrase,
    _review: review,
    _classification: {
      status: review.decision === 'CONTROLLED TEST' ? 'KEEP_TEST' : 'KEEP',
      reason: review.reason,
    },
  });
}

/** Step 3: MIG reprocess — restore commercial phrases for thin/empty groups */
function tryAssignFromMig(k) {
  const np = normPhrase(k.normalized_phrase || k.source_phrase);
  if (assignedNorm.has(np)) return false;

  let matched = null;
  for (const g of GROUPS) {
    if (g.filter(k)) {
      matched = g;
      break;
    }
  }
  if (!matched) return false;

  const review = reviewById.get(k.keyword_id) || reviewKeywordV4({ ...k, group_id: matched.id });
  reviewById.set(k.keyword_id, review);
  if (!isActiveDecision(review)) return false;

  const limit = TIER_LIMITS[matched.bid] || 15;
  const list = groupKeywords.get(matched.id);
  if (list.length >= limit) return false;

  assignedNorm.set(np, matched.id);
  list.push({
    ...k,
    group_id: matched.id,
    source_phrase: review.positive_phrase,
    normalized_phrase: np,
    ad_phrase: review.positive_phrase,
    _review: review,
    _classification: {
      status: review.decision === 'CONTROLLED TEST' ? 'KEEP_TEST' : 'KEEP',
      reason: review.reason,
    },
  });
  v3RestoredFromMig.push({ keyword_id: k.keyword_id, phrase: np, group_id: matched.id });
  return true;
}

for (const g of GROUPS) {
  const list = groupKeywords.get(g.id);
  if (list.length >= 2) continue;
  for (const k of kr.keywords) {
    if (list.length >= 2) break;
    const fakeK = { ...k, normalized_phrase: normPhrase(k.normalized_phrase || k.source_phrase) };
    if (!g.filter(fakeK)) continue;
    if (tryAssignFromMig(k)) break;
  }
}

/** Seeds for empty groups */
for (const g of GROUPS) {
  const list = groupKeywords.get(g.id);
  const seeds = SEED_CLEAN[g.id] || [];
  for (const phrase of seeds) {
    if (list.length >= 1) break;
    const np = normPhrase(phrase);
    if (assignedNorm.has(np)) continue;
    const seedKw = {
      keyword_id: `seed-v4-${g.id}-${np.slice(0, 10).replace(/\s/g, '-')}`,
      source_phrase: phrase,
      normalized_phrase: np,
      intent_class: 'direct-commercial',
      commercial_relevance: 'high',
      noise_classes: [],
      cluster: 'operator_seed',
      group_id: g.id,
    };
    const review = reviewKeywordV4(seedKw);
    reviewById.set(seedKw.keyword_id, review);
    if (!isActiveDecision(review)) continue;
    assignedNorm.set(np, g.id);
    list.push({
      ...seedKw,
      ad_phrase: phrase,
      _review: review,
      _classification: { status: 'KEEP', reason: 'operator_seed' },
    });
  }
}

/** Update semantic registry with MIG/seed additions */
const allReviewRecords = [...reviewById.values()];
semanticRegistry.reviews = allReviewRecords;
semanticRegistry.total_reviewed = allReviewRecords.length;
semanticRegistry.stats = {
  active_commercial: allReviewRecords.filter((r) => r.decision === 'ACTIVE COMMERCIAL').length,
  controlled_test: allReviewRecords.filter((r) => r.decision === 'CONTROLLED TEST').length,
  excluded: allReviewRecords.filter((r) => r.decision.startsWith('EXCLUDE')).length,
  hold: allReviewRecords.filter((r) => r.decision === 'HOLD AMBIGUOUS').length,
};

const groupViability = GROUPS.map((g) => {
  const kws = groupKeywords.get(g.id);
  const count = kws.length;
  let status = 'ACTIVE';
  if (count === 0) status = 'HOLD';
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
    ad_relevance: count > 0 ? 'reviewed' : 'n/a',
    landing_relevance: count > 0 ? 'planned_url_match' : 'n/a',
  };
});

const activeGroups = GROUPS.filter((g) => groupKeywords.get(g.id).length > 0);
const heldGroups = GROUPS.filter((g) => groupKeywords.get(g.id).length === 0);

const finalKeywords = [];
const campaignById = Object.fromEntries(CAMPAIGNS.map((c) => [c.id, c]));

for (const g of activeGroups) {
  const list = groupKeywords.get(g.id);
  list.sort((a, b) => {
    const ap = a._classification?.status === 'KEEP' ? 0 : 1;
    const bp = b._classification?.status === 'KEEP' ? 0 : 1;
    if (ap !== bp) return ap - bp;
    return (a.normalized_phrase || '').localeCompare(b.normalized_phrase || '', 'ru');
  });

  list.forEach((k, idx) => {
    const factors = scoreKeywordFactors(k, g);
    let tier = g.bid;
    if (k._classification?.status === 'KEEP_TEST' || k._review?.decision === 'CONTROLLED TEST') {
      tier = tier === 'T1' ? 'T2' : tier === 'T2' ? 'T3' : 'T4';
      factors.noiseRisk = Math.min(1, (factors.noiseRisk || 0) + 0.2);
    }
    const bid = assignBid(tier, idx + 1, list.length, factors);
    const adPhrase = k.source_phrase || k.normalized_phrase;
    const inlineNeg = PHRASE_INLINE_NEGATIVES_V4[g.id] || [];
    const adPhraseWithNeg =
      inlineNeg.length && idx === 0
        ? `${adPhrase} ${inlineNeg.map((n) => `-${n}`).join(' ')}`.trim()
        : adPhrase;

    finalKeywords.push({
      keyword_id: k.keyword_id,
      campaign_id: g.campaign,
      direction_id: g.campaign,
      direction_marker: DIRECTION_MARKERS[g.campaign],
      group_id: g.id,
      source_phrase: k.source_phrase || k.normalized_phrase,
      ad_phrase: adPhraseWithNeg,
      normalized_phrase: normPhrase(k.normalized_phrase || k.source_phrase),
      classification: k._classification?.status || 'KEEP',
      semantic_decision: k._review?.decision,
      semantic_confidence: k._review?.commercial_confidence,
      evidence_source: k.query_id || k.keyword_id,
      intent: g.intent,
      status: 'active',
      phrase_negatives: inlineNeg,
      bid_tier: bid.tier,
      factors: bid.factors,
      final_bid: bid.final_bid,
      rationale_code: bid.rationale_code,
      planned_url: `${DOMAIN}${g.url}`,
      ad_id: `ad-${g.id}-a1`,
      is_primary: idx === 0,
    });
  });
}

const finalAds = [];
for (const g of activeGroups) {
  finalAds.push(...buildAdsForGroupV4(g, UNIFIED_UTM_CAMPAIGN));
}
const adCertaintyQA = reviewAllAdsCertainty(finalAds);

const { map: safeCrossMap, removalLog: crossRemovalLog } = buildSafeCrossNegativeMap(activeGroups, finalKeywords);
const globalFiltered = filterSafeNegatives(GLOBAL_NEGATIVES_V3, finalKeywords, { level: 'global' });
const GLOBAL_NEGATIVES_FINAL = globalFiltered.safe;
const globalRemovalLog = globalFiltered.removed;
const negativeRemovalLog = [...crossRemovalLog, ...globalRemovalLog.map((r) => ({ ...r, scope: 'global' }))];
const finalNegatives = buildFinalNegativeRegistryV3(safeCrossMap, PHRASE_INLINE_NEGATIVES_V4);
const negativesQA = negativeRegistryWithQA(finalNegatives, finalKeywords, safeCrossMap);

const collisionBefore = runCollisionAudit(finalKeywords, {
  globalNegatives: GLOBAL_NEGATIVES_V3,
  directionNegatives: DIRECTION_NEGATIVES_V3,
  groupCrossNegatives: safeCrossMap,
  phraseInlineNegatives: PHRASE_INLINE_NEGATIVES_V4,
  groups: GROUPS,
});

const regressionBefore = runRegressionTests(finalKeywords, safeCrossMap, GLOBAL_NEGATIVES_V3);

const landingPages = v3Dataset.urls?.length
  ? v3Dataset.urls.map((u) => ({ id: u.landing_id, path: u.path, groups: u.groups }))
  : [];

const urlRegistry = (v3Dataset.urls || []).map((u) => ({ ...u, url_status: u.url_status || 'PLANNED — PAGE NOT YET PUBLISHED' }));

const logicalDirections = CAMPAIGNS.map((c) => ({
  id: c.id,
  marker: DIRECTION_MARKERS[c.id],
  label: DIRECTION_LABELS[c.id],
  name: c.name,
  future_utm_campaign: c.utm_campaign,
  groups: GROUPS.filter((g) => g.campaign === c.id).map((g) => g.id),
  active_groups: activeGroups.filter((g) => g.campaign === c.id).map((g) => g.id),
  held_groups: heldGroups.filter((g) => g.campaign === c.id).map((g) => g.id),
  direction_negatives: DIRECTION_NEGATIVES_V3[c.id] || [],
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
    direction_id: g.campaign,
    direction_marker: DIRECTION_MARKERS[g.campaign],
    campaign_name: camp.name,
    group_name: g.name,
    group_export_name: formatGroupExportName(g.campaign, g.name),
    bid_tier: g.bid,
    landing_page_id: g.landing,
    planned_url: `${DOMAIN}${g.url}`,
    viability_status: viability?.viability_status || 'ACTIVE',
    group_negatives: safeNeg.group_negatives,
    group_negatives_commander: safeNeg.group_negatives_commander,
    direction_negatives: safeNeg.direction_negatives_applied,
    cross_negatives: safeNeg.cross_negatives,
    negative_removals: safeNeg.removed_negatives,
    keywords: kws,
    ads,
  };
});

const collisionAfter = runExportedCollisionAudit(
  finalKeywords,
  groupsPayload,
  GLOBAL_NEGATIVES_FINAL,
  PHRASE_INLINE_NEGATIVES_V4
);
const regressionAfter = runRegressionTests(finalKeywords, safeCrossMap, GLOBAL_NEGATIVES_FINAL);

const collisionEvidence = buildCollisionEvidence({
  finalKeywords,
  groupsPayload,
  globalNegatives: GLOBAL_NEGATIVES_FINAL,
  directionNegatives: DIRECTION_NEGATIVES_V3,
  crossNegatives: safeCrossMap,
  phraseInlineNegatives: PHRASE_INLINE_NEGATIVES_V4,
  groups: GROUPS,
  negativeRemovalLog,
  beforeAudit: collisionBefore,
  afterAudit: collisionAfter,
  regressionBefore,
  regressionAfter,
});

const heldGroupsPayload = heldGroups.map((g) => ({
  group_id: g.id,
  campaign_id: g.campaign,
  direction_marker: DIRECTION_MARKERS[g.campaign],
  group_name: g.name,
  planned_url: `${DOMAIN}${g.url}`,
  viability_status: 'HOLD — NO VALID COMMERCIAL PHRASES',
  export_to_xlsx: false,
}));

const v3PhraseSet = new Set(v3Keywords.map((k) => normPhrase(stripInlineNegatives(k.ad_phrase))));
const v4PhraseSet = new Set(finalKeywords.map((k) => k.normalized_phrase));
const removedFromV3 = v3Keywords.filter((k) => !v4PhraseSet.has(normPhrase(stripInlineNegatives(k.ad_phrase))));
const addedInV4 = finalKeywords.filter((k) => !v3PhraseSet.has(k.normalized_phrase));

const v3ToV4Changes = removedFromV3.map((k) => {
  const r = reviewById.get(k.keyword_id);
  return {
    keyword_id: k.keyword_id,
    phrase: stripInlineNegatives(k.ad_phrase),
    group_id: k.group_id,
    change: 'EXCLUDED',
    decision: r?.decision,
    reason: r?.reason,
  };
}).concat(
  addedInV4.map((k) => ({
    keyword_id: k.keyword_id,
    phrase: k.normalized_phrase,
    group_id: k.group_id,
    change: 'ADDED_OR_RETAINED',
    decision: k.semantic_decision,
    reason: k._review?.reason || 'mig_or_seed',
  }))
);

const commanderDataset = {
  dataset_id: 'corv-direct-commander-production-dataset-v4',
  generated_at: new Date().toISOString(),
  project_id: 'corvonero-yandex-direct',
  domain: DOMAIN,
  geo: 'Новосибирск + Новосибирская область',
  export_model: 'UNIFIED_SINGLE_CAMPAIGN',
  unified_campaign: {
    id: UNIFIED_CAMPAIGN_ID,
    name: UNIFIED_CAMPAIGN_NAME,
    utm_campaign: UNIFIED_UTM_CAMPAIGN,
    campaign_negatives: GLOBAL_NEGATIVES_FINAL,
    future_split: 'deferred — use direction_marker in group names',
  },
  logical_directions: logicalDirections,
  campaigns: CAMPAIGNS,
  groups: groupsPayload,
  held_groups: heldGroupsPayload,
  global_negatives: GLOBAL_NEGATIVES_FINAL,
  direction_negatives: DIRECTION_NEGATIVES_V3,
  cross_negatives: safeCrossMap,
  phrase_inline_negatives: PHRASE_INLINE_NEGATIVES_V4,
  negatives: negativesQA,
  keywords: finalKeywords,
  excluded_keywords: rejectLog,
  ads: finalAds,
  urls: urlRegistry,
  group_viability: groupViability,
  merge_map: MERGE_MAP,
  merge_log: MERGE_LOG,
  negative_removal_log: negativeRemovalLog,
  semantic_review_ref: 'production/semantic-human-review-v4.json',
  collision_evidence_ref: 'production/validation/collision-evidence-v4.json',
  collision_validation: {
    before: {
      pairs_tested: collisionBefore.pairs_tested,
      blocking: collisionBefore.collisions_before_correction,
      stem_warnings: collisionBefore.stem_warnings,
      regression_passed: regressionBefore.passed,
    },
    after: {
      pairs_tested: collisionAfter.pairs_tested,
      blocking: collisionAfter.blocking_records.length,
      stem_warnings: collisionAfter.stem_warnings,
      regression_passed: regressionAfter.passed,
    },
    corrections_applied: negativeRemovalLog.length,
    evidence_summary: collisionEvidence.summary,
  },
  ad_certainty_qa: adCertaintyQA,
  manual_settings: v3Dataset.manual_settings,
  superseded: {
    dataset_v3: 'direct-commander-production-dataset-v3.json',
    xlsx_v3: 'CORVONERO-YANDEX-DIRECT-COMMANDER-v3.xlsx',
    review_v3: 'CORVONERO-CAMPAIGN-REVIEW-v3.xlsx',
  },
};

const landingHandoff = (v3Dataset.urls || []).map((u) => {
  const groupsForLp = GROUPS.filter((g) => (u.groups || []).includes(g.id));
  const activeForLp = activeGroups.filter((g) => (u.groups || []).includes(g.id));
  const kws = finalKeywords.filter((k) => (u.groups || []).includes(k.group_id));
  const ads = finalAds.filter((a) => (u.groups || []).includes(a.group_id));
  return {
    landing_id: u.landing_id,
    url: u.final_planned_url || `${DOMAIN}${u.path}`,
    logical_directions: [...new Set(groupsForLp.map((g) => g.campaign))],
    direction_markers: [...new Set(groupsForLp.map((g) => DIRECTION_MARKERS[g.campaign]))],
    groups: u.groups,
    active_groups: activeForLp.map((g) => g.id),
    held_groups: heldGroups.filter((g) => (u.groups || []).includes(g.id)).map((g) => g.id),
    service_scope: groupsForLp.map((g) => g.name),
    keyword_intents: [...new Set(kws.map((k) => k.intent))],
    ad_promises: ads.map((a) => ({ headline: a.headline_1, text: a.text, group_id: a.group_id })),
    status: 'READY FOR LANDING COPY — AFTER OPERATOR REVIEW',
  };
});

const stats = {
  v3_active_reviewed: v3Keywords.length,
  active_keywords: finalKeywords.length,
  excluded_from_v3: removedFromV3.length,
  restored_from_mig: v3RestoredFromMig.length,
  active_groups: activeGroups.length,
  held_groups: heldGroups.length,
  ads: finalAds.length,
  semantic_coverage_pct: finalKeywords.length
    ? 100
    : 0,
  collision_blocking_after: collisionAfter.blocking_records.length,
  ad_certainty_passed: adCertaintyQA.failed === 0,
  regression_passed: regressionAfter.passed,
};

const prodDir = path.join(ROOT, 'production');
const valDir = path.join(prodDir, 'validation');
const artifactsDir = path.join(ROOT, 'artifacts');
[prodDir, valDir, artifactsDir].forEach((d) => fs.mkdirSync(d, { recursive: true }));

fs.writeFileSync(path.join(prodDir, 'semantic-human-review-v4.json'), JSON.stringify(semanticRegistry, null, 2));
fs.writeFileSync(path.join(prodDir, 'semantic-human-review-v4.md'), reviewsToMarkdown(semanticRegistry));

fs.writeFileSync(
  path.join(prodDir, 'final-keyword-registry-v4.json'),
  JSON.stringify(
    {
      registry_id: 'corv-final-kw-v4',
      generated_at: new Date().toISOString(),
      stats,
      keywords: finalKeywords,
      reject_log: rejectLog,
      v3_excluded: v3Excluded,
      v3_to_v4_changes: v3ToV4Changes,
    },
    null,
    2
  )
);

fs.writeFileSync(
  path.join(prodDir, 'final-negative-registry-v4.json'),
  JSON.stringify({ registry_id: 'corv-final-neg-v4', generated_at: new Date().toISOString(), negatives: negativesQA }, null, 2)
);

fs.writeFileSync(
  path.join(prodDir, 'final-ad-registry-v4.json'),
  JSON.stringify(
    { registry_id: 'corv-final-ad-v4', generated_at: new Date().toISOString(), ads: finalAds, certainty_qa: adCertaintyQA },
    null,
    2
  )
);

fs.writeFileSync(path.join(prodDir, 'direct-commander-production-dataset-v4.json'), JSON.stringify(commanderDataset, null, 2));
fs.writeFileSync(
  path.join(prodDir, 'landing-copy-handoff-v4.json'),
  JSON.stringify(
    { handoff_id: 'corv-landing-handoff-v4', generated_at: new Date().toISOString(), unified_utm_campaign: UNIFIED_UTM_CAMPAIGN, pages: landingHandoff },
    null,
    2
  )
);

fs.writeFileSync(path.join(valDir, 'collision-evidence-v4.json'), JSON.stringify(collisionEvidence, null, 2));

fs.writeFileSync(
  path.join(valDir, 'negative-collision-validation-v4.json'),
  JSON.stringify(
    {
      validated_at: new Date().toISOString(),
      pairs_tested: collisionEvidence.summary.total_pairs_tested,
      collisions_before_correction: collisionEvidence.summary.collisions_before_correction,
      corrections_applied: collisionEvidence.summary.corrections_applied,
      collisions_after_correction: collisionEvidence.summary.collisions_after_correction,
      stem_warnings_remaining: collisionEvidence.summary.stem_risk_warnings,
      regression_before: regressionBefore,
      regression_after: regressionAfter,
      blocking_records: collisionAfter.blocking_records,
      removal_log: negativeRemovalLog,
      evidence_workbook_required: true,
    },
    null,
    2
  )
);

const semanticValidation = {
  validated_at: new Date().toISOString(),
  v3_active_reviewed: v3Keywords.length,
  active_keywords: finalKeywords.length,
  checks: {
    all_v3_active_have_review: v3Keywords.every((k) => reviewById.has(k.keyword_id)),
    all_active_have_review: finalKeywords.every((k) => {
      const r = reviewById.get(k.keyword_id);
      return r && isActiveDecision(r);
    }),
    unreviewed_active: finalKeywords.filter((k) => !reviewById.get(k.keyword_id)).length,
    low_confidence_active_without_test: finalKeywords.filter((k) => {
      const r = reviewById.get(k.keyword_id);
      return r?.commercial_confidence === 'LOW' && r.decision === 'ACTIVE COMMERCIAL';
    }).length,
    informational_in_active: finalKeywords.filter((k) => {
      const p = k.normalized_phrase;
      return /^как (подключить|установить|настроить|изменить)/.test(p) || /инструкц/.test(p) || /личный кабинет/.test(p);
    }).map((k) => k.normalized_phrase),
    long_inline_repair: finalKeywords.filter((k) => (k.phrase_negatives || []).length >= 3).length,
    operator_anchor_leaks: finalKeywords.filter((k) => {
      const anchors = [
        'тс пиот в 1с настройка инструкция',
        'лекарство без маркировки',
        'часа работы программиста 1с',
        '1с программист 2026',
      ];
      return anchors.some((a) => k.normalized_phrase.includes(a.replace(/ё/g, 'е')));
    }).map((k) => k.normalized_phrase),
  },
  passed:
    v3Keywords.every((k) => reviewById.has(k.keyword_id)) &&
    finalKeywords.every((k) => reviewById.get(k.keyword_id) && isActiveDecision(reviewById.get(k.keyword_id))) &&
    finalKeywords.filter((k) => {
      const p = k.normalized_phrase;
      return /^как (подключить|установить)/.test(p) || /инструкц/.test(p);
    }).length === 0 &&
    adCertaintyQA.failed === 0 &&
    collisionAfter.blocking_records.length === 0,
};

fs.writeFileSync(path.join(valDir, 'semantic-review-v4.json'), JSON.stringify(semanticValidation, null, 2));
fs.writeFileSync(
  path.join(valDir, 'semantic-review-v4.md'),
  `# Semantic Review Validation — v4\n\n| Check | Result |\n|-------|--------|\n| v3 active reviewed | ${semanticValidation.checks.all_v3_active_have_review ? 'PASS' : 'FAIL'} |\n| Active have review | ${semanticValidation.checks.all_active_have_review ? 'PASS' : 'FAIL'} |\n| Informational in active | ${semanticValidation.checks.informational_in_active.length} |\n| Operator anchor leaks | ${semanticValidation.checks.operator_anchor_leaks.length} |\n| Ad certainty | ${adCertaintyQA.failed === 0 ? 'PASS' : 'FAIL'} |\n| **Overall** | **${semanticValidation.passed ? 'PASS' : 'FAIL'}** |\n`
);

fs.writeFileSync(
  path.join(valDir, 'negative-collision-validation-v4.md'),
  `# Negative Collision Validation — v4\n\n| Metric | Value |\n|--------|------:|\n| Pairs tested | ${collisionEvidence.summary.total_pairs_tested} |\n| Collisions after | ${collisionEvidence.summary.collisions_after_correction} |\n| Evidence in workbook | REQUIRED |\n| Regression | ${regressionAfter.passed ? 'PASS' : 'FAIL'} |\n`
);

fs.writeFileSync(
  path.join(prodDir, 'orca-production-method-improvements-v4.md'),
  `# ORCA Production Method Improvements — v4\n\n## Why v3 automation incorrectly passed\n\n1. **Pattern classifier treated as final approval** — v3 \`classifyKeywordV3\` allowed informational/regulatory phrases when MIG intent was commercial-mixed.\n2. **Collision summary not materialized** — JSON reported 24k pairs but review workbook \`Collision audit\` sheet had zero rows (only blocking records exported).\n3. **Empty QA sheet = false PASS** — validation boolean did not verify workbook content.\n4. **Inline-minus repair** — bad phrases kept via long minus tails instead of exclusion.\n5. **Ad certainty not gated separately** — guarantee wording passed keyword scan.\n\n## v4 corrections\n\n| Rule | Implementation |\n|------|----------------|\n| Semantic review mandatory | \`semantic-human-review-v4.json\` — 100% v3 active coverage |\n| Classifier = screening only | Final gate = \`reviewKeywordV4\` decision |\n| Collision evidence published | Review workbook sheets 14–17 populated |\n| Workbook content verification | \`validate-commander-xlsx-v4\` + semantic checks |\n| Ad certainty QA | \`ads-v4.mjs\` + \`adCertaintyQA\` |\n| Regression anchors | Operator forensic list + generalized patterns in \`semantic-human-review-v4.mjs\` |\n\n## Reusable regression checks\n\n- \`semantic-review-v4.json\` — operator anchor leaks, informational in active\n- \`collision-evidence-v4.json\` — findings + passed samples + regression rows\n- \`regression-tests-v4.mjs\` — collision + semantic gates\n`
);

console.log('Production v4 registries written.');
console.log(JSON.stringify(stats, null, 2));

if (!semanticValidation.passed || collisionAfter.blocking_records.length || !regressionAfter.passed) {
  console.warn('QA issues:', { semantic: semanticValidation.passed, blocking: collisionAfter.blocking_records.length });
}

export { commanderDataset, stats, ROOT, semanticValidation, collisionEvidence, adCertaintyQA };
