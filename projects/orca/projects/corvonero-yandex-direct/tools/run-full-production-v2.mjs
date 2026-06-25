/**
 * Corvonero Unified Commander v2 production pipeline.
 * Run: node tools/run-full-production-v2.mjs
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { GROUPS, CAMPAIGNS, SEED_FALLBACK, TIER_LIMITS, DOMAIN } from './lib/groups-config.mjs';
import {
  GLOBAL_NEGATIVES_V2,
  DIRECTION_NEGATIVES_V2,
  GROUP_CROSS_NEGATIVES_V2,
  PHRASE_INLINE_NEGATIVES_V2,
  formatNegativesForCommander,
  mergeNegatives,
  buildCrossNegativeRecords,
  buildGlobalNegativeRegistry,
  buildDirectionNegativeRegistry,
} from './lib/negatives-config-v2.mjs';
import { assignBid, scoreKeywordFactors } from './lib/bids.mjs';
import { buildAdsForGroup } from './lib/ads.mjs';
import {
  classifyKeywordV2,
  isActiveClassification,
  normPhrase,
  stripInlineNegatives,
} from './lib/keyword-classifier-v2.mjs';
import {
  DIRECTION_MARKERS,
  DIRECTION_LABELS,
  UNIFIED_UTM_CAMPAIGN,
  UNIFIED_CAMPAIGN_ID,
  UNIFIED_CAMPAIGN_NAME,
  formatGroupExportName,
} from './lib/campaign-markers.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const MIG = path.resolve(
  ROOT,
  '../../../../incoming/mig/pilots/corvonero/session-mig-20260622-corv01/keyword_registry.json'
);

const kr = JSON.parse(fs.readFileSync(MIG, 'utf8'));

/** Clean seeds — no unsupported "под ключ" padding phrases */
const SEED_CLEAN = Object.fromEntries(
  Object.entries(SEED_FALLBACK).map(([gid, seeds]) => [
    gid,
    seeds.filter((s) => !/под ключ/i.test(s)),
  ])
);

/** Groups that may merge for export when intent overlaps */
const MERGE_MAP = {};

function collisionTest(keywordPhrase, negativeToken) {
  const p = normPhrase(stripInlineNegatives(keywordPhrase));
  const neg = normPhrase(negativeToken);
  if (!neg) return false;
  const words = p.split(/\s+/);
  if (neg.includes(' ')) return p.includes(neg);
  return words.includes(neg) || p.includes(` ${neg} `) || p.startsWith(`${neg} `) || p.endsWith(` ${neg}`);
}

function testKeywordAgainstNegatives(phrase, negatives) {
  const hits = [];
  for (const neg of negatives) {
    if (collisionTest(phrase, neg)) hits.push(neg);
  }
  return hits;
}

/** Assign keywords — one phrase one group */
const assignedNorm = new Map();
const groupKeywords = new Map(GROUPS.map((g) => [g.id, []]));
const rejectLog = [];
const classificationLog = [];

for (const k of kr.keywords) {
  const cls = classifyKeywordV2(k);
  classificationLog.push({
    keyword_id: k.keyword_id,
    source_phrase: k.source_phrase || k.normalized_phrase,
    classification: cls.status,
    reason: cls.reason,
    intent_class: k.intent_class,
  });

  if (!isActiveClassification(cls)) {
    rejectLog.push({
      keyword_id: k.keyword_id,
      source_phrase: k.source_phrase || k.normalized_phrase,
      status: cls.status,
      reason: cls.reason,
      intent_class: k.intent_class,
    });
    continue;
  }

  const np = normPhrase(k.normalized_phrase || k.source_phrase);
  if (assignedNorm.has(np)) {
    rejectLog.push({
      keyword_id: k.keyword_id,
      source_phrase: k.source_phrase,
      status: 'EXCLUDE_DUPLICATE',
      reason: `owned_by_${assignedNorm.get(np)}`,
    });
    continue;
  }

  let matched = null;
  for (const g of GROUPS) {
    if (g.filter(k)) {
      matched = g;
      break;
    }
  }

  if (!matched) {
    rejectLog.push({
      keyword_id: k.keyword_id,
      source_phrase: k.source_phrase,
      status: 'DEFER_AMBIGUOUS',
      reason: 'no_group_match',
      intent_class: k.intent_class,
      cluster: k.cluster,
    });
    continue;
  }

  const limit = TIER_LIMITS[matched.bid] || 15;
  const list = groupKeywords.get(matched.id);
  if (list.length >= limit) {
    rejectLog.push({
      keyword_id: k.keyword_id,
      source_phrase: k.source_phrase,
      status: 'EXCLUDE_DUPLICATE',
      reason: `group_${matched.id}_tier_limit`,
    });
    continue;
  }

  assignedNorm.set(np, matched.id);
  list.push({ ...k, _classification: cls });
}

// Ensure operator core seeds (max 2 per group) when missing — not bulk padding
for (const g of GROUPS) {
  const list = groupKeywords.get(g.id);
  const seeds = SEED_CLEAN[g.id] || [];
  for (const phrase of seeds.slice(0, 2)) {
    const np = normPhrase(phrase);
    if (assignedNorm.has(np) || list.some((k) => normPhrase(k.normalized_phrase || k.source_phrase) === np)) continue;
    const limit = TIER_LIMITS[g.bid] || 15;
    if (list.length >= limit) break;
    const seedKw = {
      keyword_id: `seed-${g.id}-core-${np.slice(0, 12).replace(/\s/g, '-')}`,
      source_phrase: phrase,
      normalized_phrase: np,
      intent_class: 'direct-commercial',
      commercial_relevance: 'high',
      noise_classes: [],
      cluster: 'operator_seed',
      query_id: 'operator_seed',
      evidence_grade: 'operator',
    };
    const cls = classifyKeywordV2(seedKw);
    if (!isActiveClassification(cls)) continue;
    assignedNorm.set(np, g.id);
    list.push({ ...seedKw, _classification: cls });
  }
}

// Seed fallback ONLY for empty groups
for (const g of GROUPS) {
  const list = groupKeywords.get(g.id);
  if (list.length > 0) continue;
  const seeds = SEED_CLEAN[g.id] || [];
  for (let i = 0; i < seeds.length; i++) {
    const phrase = seeds[i];
    const np = normPhrase(phrase);
    if (assignedNorm.has(np)) continue;
    const seedKw = {
      keyword_id: `seed-${g.id}-${i + 1}`,
      source_phrase: phrase,
      normalized_phrase: np,
      intent_class: 'direct-commercial',
      commercial_relevance: 'high',
      noise_classes: [],
      cluster: 'operator_seed',
      query_id: 'operator_seed',
      evidence_grade: 'operator',
    };
    const cls = classifyKeywordV2(seedKw);
    if (!isActiveClassification(cls)) continue;
    assignedNorm.set(np, g.id);
    list.push({ ...seedKw, _classification: cls });
    break;
  }
}

// Group viability
const groupViability = GROUPS.map((g) => {
  const kws = groupKeywords.get(g.id);
  const count = kws.length;
  let status = 'ACTIVE';
  if (count === 0) status = 'HOLD — NO VALID COMMERCIAL PHRASES';
  else if (count <= 2) status = 'ACTIVE NARROW';
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

const activeGroups = GROUPS.filter((g) => groupKeywords.get(g.id).length > 0);
const heldGroups = GROUPS.filter((g) => groupKeywords.get(g.id).length === 0);

// Build final keywords with bids
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
    if (k._classification?.status === 'KEEP_TEST') {
      tier = tier === 'T1' ? 'T2' : tier === 'T2' ? 'T3' : 'T4';
      factors.noiseRisk = Math.min(1, (factors.noiseRisk || 0) + 0.2);
    }
    const bid = assignBid(tier, idx + 1, list.length, factors);
    const adPhrase = k.source_phrase || k.normalized_phrase;
    const inlineNeg = PHRASE_INLINE_NEGATIVES_V2[g.id] || [];
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

// Ads — only for active groups
const finalAds = [];
for (const g of activeGroups) {
  const ads = buildAdsForGroup(g, UNIFIED_UTM_CAMPAIGN);
  finalAds.push(...ads);
}

// Negatives registry v2
const finalNegatives = [
  ...buildGlobalNegativeRegistry(),
  ...buildDirectionNegativeRegistry(),
];

for (const [gid, tokens] of Object.entries(GROUP_CROSS_NEGATIVES_V2)) {
  for (const token of tokens) {
    finalNegatives.push({
      level: 'group',
      group_id: gid,
      phrase: token,
      source: 'conflict-negative-matrix-v2',
      reason: 'sibling_discriminator',
      cross_risk: 'medium',
      approved_status: 'approved',
    });
  }
}

for (const [gid, tokens] of Object.entries(PHRASE_INLINE_NEGATIVES_V2)) {
  for (const token of tokens) {
    finalNegatives.push({
      level: 'phrase_inline',
      group_id: gid,
      phrase: token,
      source: 'phrase_inline_v2',
      reason: 'noisy_head_term_protection',
      cross_risk: 'low',
      approved_status: 'approved',
    });
  }
}

const crossNegativeRecords = buildCrossNegativeRecords(GROUPS);

// Collision validation
const collisionErrors = [];
const collisionWarnings = [];

for (const kw of finalKeywords) {
  const g = GROUPS.find((x) => x.id === kw.group_id);
  const groupNegs = mergeNegatives(
    GLOBAL_NEGATIVES_V2,
    DIRECTION_NEGATIVES_V2[g.campaign] || [],
    GROUP_CROSS_NEGATIVES_V2[g.id] || []
  );
  const globalHits = testKeywordAgainstNegatives(kw.ad_phrase, GLOBAL_NEGATIVES_V2);
  const dirHits = testKeywordAgainstNegatives(kw.ad_phrase, DIRECTION_NEGATIVES_V2[g.campaign] || []);
  const groupHits = testKeywordAgainstNegatives(kw.ad_phrase, GROUP_CROSS_NEGATIVES_V2[g.id] || []);
  const inlineHits = (kw.phrase_negatives || []).filter((n) => {
    const stripped = stripInlineNegatives(kw.ad_phrase);
    return collisionTest(stripped, n);
  });

  if (globalHits.length) {
    collisionErrors.push({ keyword_id: kw.keyword_id, phrase: kw.ad_phrase, level: 'global', hits: globalHits });
  }
  if (dirHits.length) {
    collisionWarnings.push({ keyword_id: kw.keyword_id, phrase: kw.ad_phrase, level: 'direction', hits: dirHits });
  }
  if (groupHits.length) {
    collisionWarnings.push({ keyword_id: kw.keyword_id, phrase: kw.ad_phrase, level: 'group', hits: groupHits });
  }
  if (inlineHits.length) {
    collisionErrors.push({ keyword_id: kw.keyword_id, phrase: kw.ad_phrase, level: 'inline', hits: inlineHits });
  }
}

// URL registry
const landingPages = [
  { id: 'LP-01', path: '/uslugi-1c/', groups: ['CORV-G01-01', 'CORV-G01-02', 'CORV-G01-08'] },
  { id: 'LP-02', path: '/nastroyka-1c/', groups: ['CORV-G01-03'] },
  { id: 'LP-03', path: '/vnedrenie-1c/', groups: ['CORV-G01-04'] },
  { id: 'LP-04', path: '/soprovozhdenie-1c/', groups: ['CORV-G01-05', 'CORV-G01-06', 'CORV-G01-07'] },
  { id: 'LP-05', path: '/dorabotka-1c/', groups: ['CORV-G02-01', 'CORV-G02-02', 'CORV-G02-03'] },
  { id: 'LP-06', path: '/obnovlenie-dorabotok-1c/', groups: ['CORV-G02-04', 'CORV-G02-05', 'CORV-G02-06'] },
  { id: 'LP-07', path: '/otchety-1c/', groups: ['CORV-G03-01', 'CORV-G03-02', 'CORV-G03-05'] },
  { id: 'LP-08', path: '/pechatnye-formy-1c/', groups: ['CORV-G03-03', 'CORV-G03-04'] },
  { id: 'LP-09', path: '/rmk-1c/', groups: ['CORV-G03-06'] },
  { id: 'LP-10', path: '/sebestoimost-1c/', groups: ['CORV-G04-01'] },
  { id: 'LP-11', path: '/plan-zakupok-1c/', groups: ['CORV-G04-02'] },
  { id: 'LP-12', path: '/platezhnyj-kalendar-1c/', groups: ['CORV-G04-03'] },
  { id: 'LP-13', path: '/integraciya-1c-s-sajtom/', groups: ['CORV-G05-01'] },
  { id: 'LP-14', path: '/integraciya-1c-bitrix/', groups: ['CORV-G05-02'] },
  { id: 'LP-15', path: '/integraciya-1c-kassa/', groups: ['CORV-G05-03'] },
  { id: 'LP-16', path: '/sinhronizaciya-1c/', groups: ['CORV-G05-04', 'CORV-G05-05'] },
  { id: 'LP-17', path: '/perenos-dannyh-1c/', groups: ['CORV-G05-06'] },
  { id: 'LP-18', path: '/markirovka-1c/', groups: ['CORV-G06-01', 'CORV-G06-02', 'CORV-G06-04'] },
  { id: 'LP-19', path: '/chestnyj-znak-1c/', groups: ['CORV-G06-03'] },
  { id: 'LP-20', path: '/markirovka-napitkov-1c/', groups: ['CORV-G06-05'] },
  { id: 'LP-21', path: '/markirovka-vody-1c/', groups: ['CORV-G06-06'] },
  { id: 'LP-22', path: '/markirovka-kosmetiki-1c/', groups: ['CORV-G06-07'] },
  { id: 'LP-23', path: '/markirovka-lekarstv-1c/', groups: ['CORV-G06-08'] },
  { id: 'LP-24', path: '/markirovka-byt-himii-1c/', groups: ['CORV-G06-09'] },
  { id: 'LP-25', path: '/markirovka-avtozapchastej-1c/', groups: ['CORV-G06-10'] },
  { id: 'LP-26', path: '/markirovka-masel-1c/', groups: ['CORV-G06-11'] },
  { id: 'LP-27', path: '/markirovka-tehniki-1c/', groups: ['CORV-G06-12'] },
  { id: 'LP-28', path: '/markirovka-stroymaterialov-1c/', groups: ['CORV-G06-13'] },
  { id: 'LP-29', path: '/1c-ne-rabotaet/', groups: ['CORV-G07-01', 'CORV-G07-02', 'CORV-G07-04'] },
  { id: 'LP-30', path: '/obmen-1c-ne-rabotaet/', groups: ['CORV-G07-03'] },
  { id: 'LP-31', path: '/ts-piot-1c/', groups: ['CORV-G08-01', 'CORV-G08-02'] },
];

const urlRegistry = landingPages.map((lp) => ({
  landing_id: lp.id,
  base_url: DOMAIN,
  path: lp.path,
  final_planned_url: `${DOMAIN}${lp.path}`,
  groups: lp.groups,
  utm_source: 'yandex',
  utm_medium: 'cpc',
  utm_campaign: UNIFIED_UTM_CAMPAIGN,
  utm_term_mechanism: '{keyword}',
  url_status: 'PLANNED — PAGE NOT YET PUBLISHED',
}));

// Logical directions for future split
const logicalDirections = CAMPAIGNS.map((c) => ({
  id: c.id,
  marker: DIRECTION_MARKERS[c.id],
  label: DIRECTION_LABELS[c.id],
  name: c.name,
  future_utm_campaign: c.utm_campaign,
  groups: GROUPS.filter((g) => g.campaign === c.id).map((g) => g.id),
  active_groups: activeGroups.filter((g) => g.campaign === c.id).map((g) => g.id),
  held_groups: heldGroups.filter((g) => g.campaign === c.id).map((g) => g.id),
  direction_negatives: DIRECTION_NEGATIVES_V2[c.id] || [],
}));

let exportGroupNumber = 0;
const groupsPayload = activeGroups.map((g) => {
  exportGroupNumber += 1;
  const camp = campaignById[g.campaign];
  const kws = finalKeywords.filter((k) => k.group_id === g.id);
  const ads = finalAds.filter((a) => a.group_id === g.id);
  const groupNegTokens = mergeNegatives(
    DIRECTION_NEGATIVES_V2[g.campaign] || [],
    GROUP_CROSS_NEGATIVES_V2[g.id] || []
  );
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
    group_negatives: groupNegTokens,
    group_negatives_commander: formatNegativesForCommander(groupNegTokens),
    direction_negatives: DIRECTION_NEGATIVES_V2[g.campaign] || [],
    cross_negatives: GROUP_CROSS_NEGATIVES_V2[g.id] || [],
    keywords: kws,
    ads,
  };
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

const commanderDataset = {
  dataset_id: 'corv-direct-commander-production-dataset-v2',
  generated_at: new Date().toISOString(),
  project_id: 'corvonero-yandex-direct',
  domain: DOMAIN,
  geo: 'Новосибирск + Новосибирская область',
  export_model: 'UNIFIED_SINGLE_CAMPAIGN',
  unified_campaign: {
    id: UNIFIED_CAMPAIGN_ID,
    name: UNIFIED_CAMPAIGN_NAME,
    utm_campaign: UNIFIED_UTM_CAMPAIGN,
    campaign_negatives: GLOBAL_NEGATIVES_V2,
    future_split: 'deferred — use direction_marker in group names',
  },
  logical_directions: logicalDirections,
  campaigns: CAMPAIGNS,
  groups: groupsPayload,
  held_groups: heldGroupsPayload,
  global_negatives: GLOBAL_NEGATIVES_V2,
  direction_negatives: DIRECTION_NEGATIVES_V2,
  cross_negatives: GROUP_CROSS_NEGATIVES_V2,
  phrase_inline_negatives: PHRASE_INLINE_NEGATIVES_V2,
  negatives: finalNegatives,
  keywords: finalKeywords,
  ads: finalAds,
  urls: urlRegistry,
  group_viability: groupViability,
  merge_map: MERGE_MAP,
  collision_validation: {
    errors: collisionErrors,
    warnings: collisionWarnings,
  },
  manual_settings: {
    region: 'Новосибирск и Новосибирская область',
    schedule: 'Mon–Fri 08:00–20:00 NSO (recommended)',
    strategy: 'Manual CPC search only',
    monthly_budget_context_rub: 100000,
    metrika: 'SAFE UNKNOWN — configure post-import',
    launch_authorized: false,
  },
  superseded: {
    dataset_v1: 'direct-commander-production-dataset-v1.json',
    xlsx_v1: 'CORVONERO-YANDEX-DIRECT-COMMANDER-v1.xlsx',
  },
};

// Keyword band stats
const kwByGroup = {};
finalKeywords.forEach((k) => {
  kwByGroup[k.group_id] = (kwByGroup[k.group_id] || 0) + 1;
});
const bands = { '1': 0, '2': 0, '3-4': 0, '5-9': 0, '10+': 0 };
Object.values(kwByGroup).forEach((n) => {
  if (n === 1) bands['1']++;
  else if (n === 2) bands['2']++;
  else if (n <= 4) bands['3-4']++;
  else if (n <= 9) bands['5-9']++;
  else bands['10+']++;
});

const bids = finalKeywords.map((k) => k.final_bid);
const stats = {
  logical_directions: CAMPAIGNS.length,
  architecture_groups: GROUPS.length,
  active_groups: activeGroups.length,
  held_groups: heldGroups.length,
  active_keywords: finalKeywords.length,
  excluded_keywords: rejectLog.length,
  keep_test: finalKeywords.filter((k) => k.classification === 'KEEP_TEST').length,
  ads: finalAds.length,
  global_negatives: GLOBAL_NEGATIVES_V2.length,
  direction_negatives: Object.values(DIRECTION_NEGATIVES_V2).flat().length,
  group_cross_negatives: Object.values(GROUP_CROSS_NEGATIVES_V2).flat().length,
  phrase_inline_negatives: Object.values(PHRASE_INLINE_NEGATIVES_V2).flat().length,
  urls: urlRegistry.length,
  keyword_bands: bands,
  bids_by_tier: Object.fromEntries(
    ['T1', 'T2', 'T3', 'T4'].map((t) => [t, finalKeywords.filter((k) => k.bid_tier === t).length])
  ),
  bid_min: bids.length ? Math.min(...bids) : 0,
  bid_max: bids.length ? Math.max(...bids) : 0,
  bid_median: bids.length ? bids.sort((a, b) => a - b)[Math.floor(bids.length / 2)] : 0,
  collision_errors: collisionErrors.length,
  collision_warnings: collisionWarnings.length,
};

// v1 diff
const v1Kw = JSON.parse(
  fs.readFileSync(path.join(ROOT, 'production/final-keyword-registry-v1.json'), 'utf8')
);
const v1Phrases = new Set(v1Kw.keywords.map((k) => normPhrase(k.normalized_phrase || k.ad_phrase)));
const v2Phrases = new Set(finalKeywords.map((k) => k.normalized_phrase));
const removedFromV1 = v1Kw.keywords.filter((k) => !v2Phrases.has(normPhrase(k.normalized_phrase || k.ad_phrase)));
const addedInV2 = finalKeywords.filter((k) => !v1Phrases.has(k.normalized_phrase));

// Landing handoff v2
const landingHandoff = landingPages.map((lp) => {
  const groupsForLp = GROUPS.filter((g) => lp.groups.includes(g.id));
  const activeForLp = activeGroups.filter((g) => lp.groups.includes(g.id));
  const kws = finalKeywords.filter((k) => lp.groups.includes(k.group_id));
  const ads = finalAds.filter((a) => lp.groups.includes(a.group_id));
  return {
    landing_id: lp.id,
    url: `${DOMAIN}${lp.path}`,
    logical_directions: [...new Set(groupsForLp.map((g) => g.campaign))],
    direction_markers: [...new Set(groupsForLp.map((g) => DIRECTION_MARKERS[g.campaign]))],
    groups: lp.groups,
    active_groups: activeForLp.map((g) => g.id),
    held_groups: heldGroups.filter((g) => lp.groups.includes(g.id)).map((g) => g.id),
    merged_groups: [],
    service_scope: groupsForLp.map((g) => g.name),
    keyword_intents: [...new Set(kws.map((k) => k.intent))],
    ad_promises: ads.map((a) => ({ headline: a.headline_1, text: a.text, group_id: a.group_id })),
    price_usage: ads.some((a) => /6000|3000/.test(a.text)),
    configurations: ['1С:УТ', '1С:УНФ', '1С:Розница', '1С:КА', '1С:Бухгалтерия предприятия'],
    status: 'READY FOR LANDING COPY — AFTER OPERATOR REVIEW',
  };
});

// Write outputs
const prodDir = path.join(ROOT, 'production');
const valDir = path.join(prodDir, 'validation');
[prodDir, valDir].forEach((d) => fs.mkdirSync(d, { recursive: true }));

fs.writeFileSync(
  path.join(prodDir, 'final-keyword-registry-v2.json'),
  JSON.stringify(
    {
      registry_id: 'corv-final-kw-v2',
      generated_at: new Date().toISOString(),
      stats: {
        active: stats.active_keywords,
        excluded: stats.excluded_keywords,
        keep_test: stats.keep_test,
        keyword_bands: bands,
      },
      keywords: finalKeywords,
      reject_log: rejectLog,
      classification_log: classificationLog,
    },
    null,
    2
  )
);

fs.writeFileSync(
  path.join(prodDir, 'final-keyword-registry-v2.md'),
  `# Final Keyword Registry — Корво Неро v2\n\n**Active:** ${stats.active_keywords} · **Excluded:** ${stats.excluded_keywords} · **KEEP_TEST:** ${stats.keep_test}\n\n## Distribution by group size\n\n${Object.entries(bands).map(([k, v]) => `- ${k} phrase(s): ${v} groups`).join('\n')}\n\n## Tier distribution\n\n${Object.entries(stats.bids_by_tier).map(([t, n]) => `- ${t}: ${n}`).join('\n')}\n\n## Reject summary\n\n${[...new Set(rejectLog.map((r) => r.status))].map((s) => `- ${s}: ${rejectLog.filter((r) => r.status === s).length}`).join('\n')}\n`
);

fs.writeFileSync(
  path.join(prodDir, 'keyword-v1-to-v2-diff.md'),
  `# Keyword v1 → v2 Diff\n\n**Removed from active (${removedFromV1.length}):**\n\n${removedFromV1.slice(0, 80).map((k) => `- \`${k.ad_phrase || k.source_phrase}\` (${k.group_id})`).join('\n')}${removedFromV1.length > 80 ? `\n\n… and ${removedFromV1.length - 80} more` : ''}\n\n**Added in v2 (${addedInV2.length}):**\n\n${addedInV2.map((k) => `- \`${k.ad_phrase}\` (${k.group_id})`).join('\n') || '- none'}\n`
);

fs.writeFileSync(
  path.join(prodDir, 'final-negative-registry-v2.json'),
  JSON.stringify({ registry_id: 'corv-final-neg-v2', generated_at: new Date().toISOString(), negatives: finalNegatives }, null, 2)
);

const crossMd = `# Final Conflict-Negative Matrix — v2\n\nUnified campaign — direction negatives emulated per group.\n\n| Level | Count |\n|-------|-------|\n| Global | ${GLOBAL_NEGATIVES_V2.length} |\n| Direction | ${stats.direction_negatives} |\n| Group cross | ${stats.group_cross_negatives} |\n| Phrase inline | ${stats.phrase_inline_negatives} |\n\n## Cross-negative pairs\n\n${crossNegativeRecords.slice(0, 30).map((r) => `- ${r.source_group} → -${r.negative_token}`).join('\n')}\n\n… total ${crossNegativeRecords.length} records — see cross-negative-validation-v2.json\n`;
fs.writeFileSync(path.join(prodDir, 'final-conflict-negative-matrix-v2.md'), crossMd);

fs.writeFileSync(
  path.join(prodDir, 'cross-negative-validation-v2.json'),
  JSON.stringify(
    {
      validated_at: new Date().toISOString(),
      records: crossNegativeRecords,
      collision_errors: collisionErrors,
      collision_warnings: collisionWarnings,
    },
    null,
    2
  )
);

const v1Ads = JSON.parse(fs.readFileSync(path.join(ROOT, 'production/final-ad-registry-v1.json'), 'utf8'));
const adDiffs = [];
for (const ad of finalAds) {
  const old = v1Ads.ads.find((a) => a.ad_id === ad.ad_id);
  if (!old) {
    adDiffs.push({ ad_id: ad.ad_id, change: 'new' });
    continue;
  }
  if (old.headline_1 !== ad.headline_1 || old.headline_2 !== ad.headline_2 || old.text !== ad.text) {
    adDiffs.push({
      ad_id: ad.ad_id,
      group_id: ad.group_id,
      old: { h1: old.headline_1, h2: old.headline_2, text: old.text },
      new: { h1: ad.headline_1, h2: ad.headline_2, text: ad.text },
    });
  }
}

fs.writeFileSync(
  path.join(prodDir, 'final-ad-registry-v2.json'),
  JSON.stringify({ registry_id: 'corv-final-ad-v2', generated_at: new Date().toISOString(), ads: finalAds }, null, 2)
);

fs.writeFileSync(
  path.join(prodDir, 'final-ad-registry-v2.md'),
  `# Final Ad Registry — v2\n\n**Ads:** ${finalAds.length} across ${activeGroups.length} active groups (${heldGroups.length} held)\n\n## Unsupported claims removed\n\n- «Под ключ» in h2\n- «Срочно восстановим»\n- «Быстро и точно»\n\n## Changed ads: ${adDiffs.length}\n`
);

fs.writeFileSync(
  path.join(prodDir, 'ad-v1-to-v2-diff.md'),
  `# Ad v1 → v2 Diff\n\n${adDiffs.map((d) => (d.old ? `### ${d.ad_id}\n- h1: \`${d.old.h1}\` → \`${d.new.h1}\`\n- h2: \`${d.old.h2}\` → \`${d.new.h2}\`\n- text: \`${d.old.text}\` → \`${d.new.text}\`` : `### ${d.ad_id} — new`)).join('\n\n')}\n`
);

fs.writeFileSync(path.join(prodDir, 'direct-commander-production-dataset-v2.json'), JSON.stringify(commanderDataset, null, 2));
fs.writeFileSync(
  path.join(prodDir, 'landing-copy-handoff-v2.json'),
  JSON.stringify({ handoff_id: 'corv-landing-handoff-v2', generated_at: new Date().toISOString(), unified_utm_campaign: UNIFIED_UTM_CAMPAIGN, pages: landingHandoff, held_groups: heldGroupsPayload }, null, 2)
);

console.log('Production v2 registries written.');
console.log(JSON.stringify(stats, null, 2));

if (collisionErrors.length) {
  console.warn('COLLISION ERRORS:', collisionErrors.length);
  collisionErrors.slice(0, 5).forEach((e) => console.warn(e));
}

export { commanderDataset, stats, ROOT, collisionErrors };
