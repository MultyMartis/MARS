/**
 * Corvonero Stage 2B–2D full production pipeline.
 * Run: node tools/run-full-production.mjs
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { GROUPS, CAMPAIGNS, SEED_FALLBACK, TIER_LIMITS, DOMAIN } from './lib/groups-config.mjs';
import {
  GLOBAL_NEGATIVES,
  CAMPAIGN_NEGATIVES,
  GROUP_CROSS_NEGATIVES,
  PHRASE_INLINE_NEGATIVES,
  formatNegativesForCommander,
  mergeNegatives,
} from './lib/negatives-config.mjs';
import { assignBid, scoreKeywordFactors } from './lib/bids.mjs';
import { buildAdsForGroup } from './lib/ads.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const MIG = path.resolve(
  ROOT,
  '../../../../incoming/mig/pilots/corvonero/session-mig-20260622-corv01/keyword_registry.json'
);

const kr = JSON.parse(fs.readFileSync(MIG, 'utf8'));

function normPhrase(s) {
  return String(s || '')
    .toLowerCase()
    .replace(/ё/g, 'е')
    .replace(/\s+/g, ' ')
    .trim();
}

const REJECT_RULES = [
  { status: 'exclude_employment', test: (p, k) => /ваканс|резюме|зарплат|собеседован|стажер|стажировк|без опыта|работа программист|работа 1с|удаленная работа|удалённая работа|hh\.ru|superjob|работа на 1с/.test(p) && !/не работает|не работает/.test(p) },
  { status: 'exclude_training', test: (p) => /обучен|курс|урок|экзамен|сертифик|с нуля|школ|учебник|видеоурок|видео/.test(p) && !/настройк|доработ/.test(p) },
  { status: 'exclude_download', test: (p) => /скачать|торрент|кряк|crack|torrent|демо верс/.test(p) },
  { status: 'exclude_informational', test: (p, k) => k.intent_class === 'informational' || (/что такое|как работает|инструкция|документация|форум|реферат|диплом|курсовая/.test(p) && !/услуг|заказ|настройк|доработ/.test(p)) },
  { status: 'exclude_regulatory', test: (p, k) => k.intent_class === 'regulatory' && k.commercial_relevance !== 'high' },
  { status: 'exclude_irrelevant', test: (p) => /москва|санкт-петербург|екатеринбург|краснодар|спб/.test(p) && !/новосибирск/.test(p) },
];

function classifyKeyword(k) {
  const p = normPhrase(k.normalized_phrase || k.source_phrase);
  if (!p || p.length < 3) return { status: 'exclude_irrelevant', reason: 'empty' };

  for (const rule of REJECT_RULES) {
    if (rule.test(p, k)) return { status: rule.status, reason: rule.status };
  }

  if (k.intent_class === 'regulatory' && k.commercial_relevance !== 'high') {
    return { status: 'exclude_regulatory', reason: 'regulatory_non_service' };
  }

  const nc = k.noise_classes || [];
  const onlyNoise =
    nc.length > 0 &&
    nc.every((n) => ['job-seeking', 'training', 'salary', 'remote-work', 'informational'].includes(n));
  if (onlyNoise && k.intent_class !== 'direct-commercial' && k.intent_class !== 'troubleshooting') {
    return { status: 'exclude_employment', reason: 'noise_only' };
  }

  if (
    k.intent_class === 'direct-commercial' ||
    k.intent_class === 'troubleshooting' ||
    (k.intent_class === 'commercial-mixed' && k.commercial_relevance !== 'low')
  ) {
    return { status: 'active', reason: 'commercial' };
  }

  if (k.intent_class === 'commercial-mixed') return { status: 'deferred_ambiguous', reason: 'mixed_low' };
  return { status: 'exclude_informational', reason: 'non_commercial' };
}

function isCommercial(k) {
  return classifyKeyword(k).status === 'active';
}

/** Assign keywords to groups — one phrase one group */
const assignedNorm = new Map();
const groupKeywords = new Map(GROUPS.map((g) => [g.id, []]));
const rejectLog = [];

for (const k of kr.keywords) {
  const cls = classifyKeyword(k);
  if (cls.status !== 'active') {
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
      status: 'exclude_duplicate',
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
      status: 'deferred_ambiguous',
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
      status: 'exclude_duplicate',
      reason: `group_${matched.id}_full`,
    });
    continue;
  }

  assignedNorm.set(np, matched.id);
  list.push(k);
}

// Seed fallback for empty/thin groups
for (const g of GROUPS) {
  const list = groupKeywords.get(g.id);
  if (list.length >= 5) continue;
  const seeds = SEED_FALLBACK[g.id] || [];
  for (let i = 0; i < seeds.length && list.length < 8; i++) {
    const phrase = seeds[i];
    const np = normPhrase(phrase);
    if (assignedNorm.has(np)) continue;
    assignedNorm.set(np, g.id);
    list.push({
      keyword_id: `seed-${g.id}-${i + 1}`,
      source_phrase: phrase,
      normalized_phrase: np,
      intent_class: 'direct-commercial',
      commercial_relevance: 'high',
      noise_classes: [],
      cluster: 'operator_seed',
      query_id: 'operator_seed',
      evidence_grade: 'operator',
    });
  }
}

// Build final keyword records with bids
const finalKeywords = [];
const campaignById = Object.fromEntries(CAMPAIGNS.map((c) => [c.id, c]));

for (const g of GROUPS) {
  const list = groupKeywords.get(g.id);
  const camp = campaignById[g.campaign];
  list.sort((a, b) => {
    const ap = a.keyword_id.startsWith('kw-corv01-00') ? 0 : 1;
    const bp = b.keyword_id.startsWith('kw-corv01-00') ? 0 : 1;
    if (ap !== bp) return ap - bp;
    return (a.normalized_phrase || '').localeCompare(b.normalized_phrase || '', 'ru');
  });

  list.forEach((k, idx) => {
    const factors = scoreKeywordFactors(k, g);
    const bid = assignBid(g.bid, idx + 1, list.length, factors);
    const adPhrase = k.source_phrase || k.normalized_phrase;
    const inlineNeg = PHRASE_INLINE_NEGATIVES[g.id] || [];
    const adPhraseWithNeg =
      inlineNeg.length && idx === 0
        ? `${adPhrase} ${inlineNeg.map((n) => `-${n}`).join(' ')}`.trim()
        : adPhrase;

    finalKeywords.push({
      keyword_id: k.keyword_id,
      campaign_id: g.campaign,
      group_id: g.id,
      source_phrase: k.source_phrase || k.normalized_phrase,
      ad_phrase: adPhraseWithNeg,
      normalized_phrase: normPhrase(k.normalized_phrase || k.source_phrase),
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

// Ads
const finalAds = [];
for (const g of GROUPS) {
  const camp = campaignById[g.campaign];
  const ads = buildAdsForGroup(g, camp.utm_campaign);
  finalAds.push(...ads);
}

// Negatives registry
const finalNegatives = [];
for (const token of GLOBAL_NEGATIVES) {
  finalNegatives.push({
    level: 'global',
    phrase: token,
    source: 'negative-keyword-architecture-v1',
    reason: 'evidence_supported_noise',
    cross_risk: 'low',
    validation_status: 'pass',
  });
}

for (const [cid, tokens] of Object.entries(CAMPAIGN_NEGATIVES)) {
  for (const token of tokens) {
    finalNegatives.push({
      level: 'campaign',
      campaign_id: cid,
      phrase: token,
      source: 'negative-keyword-architecture-v1',
      reason: 'campaign_isolation',
      cross_risk: 'medium',
      validation_status: 'pass',
    });
  }
}

for (const [gid, tokens] of Object.entries(GROUP_CROSS_NEGATIVES)) {
  for (const token of tokens) {
    finalNegatives.push({
      level: 'group',
      group_id: gid,
      phrase: token,
      source: 'conflict-negative-matrix-v1',
      reason: 'sibling_discriminator',
      cross_risk: 'medium',
      validation_status: 'pass',
    });
  }
}

// URL / UTM registry
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

const urlRegistry = landingPages.map((lp) => {
  const groupsForLp = GROUPS.filter((g) => lp.groups.includes(g.id));
  const campaigns = [...new Set(groupsForLp.map((g) => g.campaign))];
  return {
    landing_id: lp.id,
    base_url: DOMAIN,
    path: lp.path,
    final_planned_url: `${DOMAIN}${lp.path}`,
    groups: lp.groups,
    campaigns,
    utm_source: 'yandex',
    utm_medium: 'cpc',
    utm_term_mechanism: '{keyword}',
    url_status: 'PLANNED — PAGE NOT YET PUBLISHED',
  };
});

// Commander dataset
const groupsPayload = GROUPS.map((g, idx) => {
  const camp = campaignById[g.campaign];
  const kws = finalKeywords.filter((k) => k.group_id === g.id);
  const ads = finalAds.filter((a) => a.group_id === g.id);
  const groupNegTokens = mergeNegatives(
    GROUP_CROSS_NEGATIVES[g.id] || [],
    CAMPAIGN_NEGATIVES[g.campaign] || []
  );

  return {
    group_id: g.id,
    group_number: idx + 1,
    campaign_id: g.campaign,
    campaign_name: camp.name,
    group_name: g.name,
    bid_tier: g.bid,
    landing_page_id: g.landing,
    planned_url: `${DOMAIN}${g.url}`,
    group_negatives: groupNegTokens,
    group_negatives_commander: formatNegativesForCommander(groupNegTokens),
    keywords: kws,
    ads,
  };
});

const commanderDataset = {
  dataset_id: 'corv-direct-commander-production-dataset-v1',
  generated_at: new Date().toISOString(),
  project_id: 'corvonero-yandex-direct',
  domain: DOMAIN,
  geo: 'Новосибирск + Новосибирская область',
  campaigns: CAMPAIGNS.map((c) => ({
    ...c,
    campaign_negatives: mergeNegatives(GLOBAL_NEGATIVES, CAMPAIGN_NEGATIVES[c.id] || []),
  })),
  groups: groupsPayload,
  global_negatives: GLOBAL_NEGATIVES,
  negatives: finalNegatives,
  keywords: finalKeywords,
  ads: finalAds,
  urls: urlRegistry,
  manual_settings: {
    region: 'Новосибирск и Новосибирская область',
    schedule: 'Mon–Fri 08:00–20:00 NSO (recommended)',
    strategy: 'Manual CPC search only',
    monthly_budget_context_rub: 100000,
    metrika: 'SAFE UNKNOWN — configure post-import',
    launch_authorized: false,
  },
  evidence_references: [
    'incoming/mig/pilots/corvonero/session-mig-20260622-corv01/keyword_registry.json',
    'production/ad-group-registry-v1.json',
    'production/campaign-architecture-v1.md',
  ],
};

// Landing handoff
const landingHandoff = landingPages.map((lp) => {
  const groupsForLp = GROUPS.filter((g) => lp.groups.includes(g.id));
  const kws = finalKeywords.filter((k) => lp.groups.includes(k.group_id));
  const ads = finalAds.filter((a) => lp.groups.includes(a.group_id));
  return {
    landing_id: lp.id,
    url: `${DOMAIN}${lp.path}`,
    campaigns: [...new Set(groupsForLp.map((g) => g.campaign))],
    groups: lp.groups,
    service_scope: groupsForLp.map((g) => g.name),
    keyword_intents: [...new Set(kws.map((k) => k.intent))],
    ad_promises: ads.map((a) => ({ headline: a.headline_1, text: a.text })),
    price_usage: ads.some((a) => /6000|3000/.test(a.text)),
    configurations: ['1С:УТ', '1С:УНФ', '1С:Розница', '1С:КА', '1С:Бухгалтерия предприятия'],
    required_blocks: ['hero', 'services', 'price_terms', 'configs', 'process', 'cta', 'contacts', 'legal'],
    related_pages: landingPages.filter((x) => x.id !== lp.id).slice(0, 5).map((x) => x.path),
    prohibited_unsupported_claims: [
      'official 1C partner', 'certificates', 'team size', 'years experience',
      'guaranteed deadlines', '24/7', 'free audit', 'case studies', 'SLA', 'VAT/NDS',
    ],
    status: 'READY FOR LANDING COPY PRODUCTION',
  };
});

// Write outputs
const prodDir = path.join(ROOT, 'production');
const valDir = path.join(prodDir, 'validation');
const exportDir = path.join(ROOT, 'exports');
const artDir = path.join(ROOT, 'artifacts');
[prodDir, valDir, exportDir, artDir].forEach((d) => fs.mkdirSync(d, { recursive: true }));

const stats = {
  campaigns: CAMPAIGNS.length,
  groups: GROUPS.length,
  active_keywords: finalKeywords.length,
  excluded_keywords: rejectLog.length,
  ads: finalAds.length,
  global_negatives: GLOBAL_NEGATIVES.length,
  campaign_negatives: Object.values(CAMPAIGN_NEGATIVES).flat().length,
  group_negatives: Object.values(GROUP_CROSS_NEGATIVES).flat().length,
  urls: urlRegistry.length,
  bids_by_tier: Object.fromEntries(
    ['T1', 'T2', 'T3', 'T4'].map((t) => [t, finalKeywords.filter((k) => k.bid_tier === t).length])
  ),
};

fs.writeFileSync(path.join(prodDir, 'final-keyword-registry-v1.json'), JSON.stringify({ registry_id: 'corv-final-kw-v1', generated_at: new Date().toISOString(), stats: { active: stats.active_keywords, excluded: stats.excluded_keywords }, keywords: finalKeywords, reject_log: rejectLog }, null, 2));

fs.writeFileSync(
  path.join(prodDir, 'final-keyword-registry-v1.md'),
  `# Final Keyword Registry — Корво Неро v1\n\n**Active:** ${stats.active_keywords} · **Excluded/deferred:** ${stats.excluded_keywords}\n\n## Tier distribution\n\n${Object.entries(stats.bids_by_tier).map(([t, n]) => `- ${t}: ${n}`).join('\n')}\n\n## Reject summary\n\n${[...new Set(rejectLog.map((r) => r.status))].map((s) => `- ${s}: ${rejectLog.filter((r) => r.status === s).length}`).join('\n')}\n`
);

fs.writeFileSync(path.join(prodDir, 'final-negative-registry-v1.json'), JSON.stringify({ registry_id: 'corv-final-neg-v1', generated_at: new Date().toISOString(), negatives: finalNegatives }, null, 2));

fs.writeFileSync(
  path.join(prodDir, 'final-conflict-negative-matrix-v1.md'),
  `# Final Conflict-Negative Matrix — v1\n\nGenerated from production pipeline.\n\n| Level | Count |\n|-------|-------|\n| Global | ${GLOBAL_NEGATIVES.length} |\n| Campaign | ${stats.campaign_negatives} |\n| Group cross | ${stats.group_negatives} |\n`
);

fs.writeFileSync(path.join(prodDir, 'final-ad-registry-v1.json'), JSON.stringify({ registry_id: 'corv-final-ad-v1', generated_at: new Date().toISOString(), ads: finalAds }, null, 2));

fs.writeFileSync(
  path.join(prodDir, 'final-ad-registry-v1.md'),
  `# Final Ad Registry — v1\n\n**Ads:** ${finalAds.length} across ${GROUPS.length} groups\n`
);

fs.writeFileSync(path.join(prodDir, 'final-url-utm-registry-v1.json'), JSON.stringify({ registry_id: 'corv-final-url-v1', generated_at: new Date().toISOString(), urls: urlRegistry, groups: groupsPayload.map((g) => ({ group_id: g.group_id, utm_campaign: campaignById[g.campaign_id].utm_campaign, utm_content: g.group_id, utm_term: '{keyword}' })) }, null, 2));

fs.writeFileSync(path.join(prodDir, 'direct-commander-production-dataset-v1.json'), JSON.stringify(commanderDataset, null, 2));

fs.writeFileSync(path.join(prodDir, 'landing-copy-handoff-v1.json'), JSON.stringify({ handoff_id: 'corv-landing-handoff-v1', generated_at: new Date().toISOString(), pages: landingHandoff }, null, 2));

// Validate groups have keywords and ads
const emptyGroups = GROUPS.filter((g) => !finalKeywords.some((k) => k.group_id === g.id));
if (emptyGroups.length) {
  console.error('BLOCKER: empty groups', emptyGroups.map((g) => g.id));
  process.exit(1);
}

console.log('Production registries written.');
console.log(JSON.stringify(stats, null, 2));

export { commanderDataset, stats, ROOT };
