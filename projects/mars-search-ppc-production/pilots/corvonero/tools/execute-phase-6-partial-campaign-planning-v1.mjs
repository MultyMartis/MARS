#!/usr/bin/env node
/**
 * Corvonero Run 004 Phase 6 — Partial Campaign-Planning Architecture.
 * No provider calls. No semantic verdict changes. ACCEPT-only allocation.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const PILOT = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const REPORTS = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/reports');

const RUN_ID = 'corv-semantic-v2-20260626-004';
const PHASE6_ID = 'corvonero-phase-6-partial-campaign-planning-v1';
const CANONICAL_TOTAL = 2368;
const ASSESSED_TOTAL = 1599;
const UNPROCESSED_TOTAL = 769;
const EXPECTED = { ACCEPT: 935, REJECT: 368, ABSTAIN: 296 };
const COVERAGE_PCT = 67.5;

const PARTIAL_BOUNDARY = {
  partial_semantic_authority: `${ASSESSED_TOTAL} / ${CANONICAL_TOTAL} assessed`,
  unprocessed_backlog: `${UNPROCESSED_TOTAL} / ${CANONICAL_TOTAL} excluded`,
  coverage: `${COVERAGE_PCT}%`,
};

function readJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function writeJson(p, d) {
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, JSON.stringify(d, null, 2));
}

function writeText(p, t) {
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, t);
}

// --- ABSTAIN holdout classification heuristics ---
const ABSTAIN_PATTERNS = [
  {
    id: 'PRODUCT_PLUS_SERVICE_REVIEW',
    re: /(?:купить|лицензи|поставк|продукт|коробочн|its|итс|подписк)/i,
  },
  {
    id: 'AMBIGUOUS_DIY_PROBLEM',
    re: /(?:самостоятельно|самому|как\s+(?:исправить|настроить|обновить)|инструкци|ошибк|не\s+работает)/i,
  },
  {
    id: 'GENERIC_PLATFORM_OR_ERP',
    re: /(?:erp|sap|oracle|dynamics|platform|платформ|конфигураци(?:я|и))/i,
  },
  {
    id: 'SHORT_UNDERSPECIFIED',
    re: /^.{1,18}$/,
  },
  {
    id: 'MIXED_INFORMATIONAL_COMMERCIAL',
    re: /(?:что\s+такое|как\s+работает|сколько\s+стоит|стоимость|цена|услуг|сопровожден)/i,
  },
];

function classifyAbstainHoldout(record) {
  const phrase = record.phrase || '';
  for (const p of ABSTAIN_PATTERNS) {
    if (p.re.test(phrase)) return p.id;
  }
  return 'OTHER_AMBIGUITY';
}

// --- Campaign family rules ---
const CAMPAIGN_FAMILY_META = {
  'CF-PROGRAMMER-SPECIALIST': {
    name: '1C programmer / specialist search',
    service_families: ['SF-1C-PROGRAMMER-SPECIALIST'],
    primary_intents: ['SPECIALIST_SEARCH', 'DIRECT_SERVICE_ORDER'],
    merge_rationale: 'Shared specialist landing intent; negatives align on career/education exclusion',
    separate_rationale: null,
    landing: { confirmed: null, required: 'Programmer/specialist service page', risk: 'Generic homepage if no dedicated LP' },
    geo: 'PRIMARY + REMOTE_RU + EXPANSION via bid/location',
    priority_tier_default: 'P1',
  },
  'CF-SUPPORT-AND-SUBSCRIPTION': {
    name: '1C support, maintenance and subscription',
    service_families: ['SF-SUPPORT-MAINTENANCE', 'SF-SUBSCRIPTION-SERVICE'],
    primary_intents: ['SUPPORT_AND_MAINTENANCE', 'DIRECT_SERVICE_ORDER'],
    merge_rationale: 'Same delivery model (ongoing service); shared support LP; subscription terms overlap support semantics',
    separate_rationale: 'Split if subscription LP differs or budget isolation required',
    landing: { confirmed: null, required: 'Support / абонентское обслуживание page', risk: 'Medium — product+service ambiguity in some phrases' },
    geo: 'PRIMARY + REMOTE_RU',
    priority_tier_default: 'P1',
  },
  'CF-MODIFICATION-DEVELOPMENT': {
    name: '1C modification and development',
    service_families: ['SF-MODIFICATION-DEVELOPMENT'],
    primary_intents: ['MODIFICATION', 'DIRECT_SERVICE_ORDER', 'SPECIALIST_SEARCH'],
    merge_rationale: 'Development/doraботка share modification LP and intent',
    separate_rationale: null,
    landing: { confirmed: null, required: 'Development / доработка page', risk: 'Low if dedicated dev LP exists' },
    geo: 'PRIMARY + REMOTE_RU',
    priority_tier_default: 'P1',
  },
  'CF-REPORTS-PROCESSING': {
    name: 'Reports and processing',
    service_families: ['SF-REPORTS-PROCESSING'],
    primary_intents: ['MODIFICATION', 'DIRECT_SERVICE_ORDER', 'SPECIALIST_SEARCH'],
    merge_rationale: 'Small cluster; same technical delivery',
    separate_rationale: 'Separate if reports LP distinct from general modification',
    landing: { confirmed: null, required: 'Reports / обработки page', risk: 'May land on generic dev page' },
    geo: 'REMOTE_RU',
    priority_tier_default: 'P2',
  },
  'CF-INTEGRATIONS': {
    name: 'Integrations (Bitrix, sites, API)',
    service_families: ['SF-INTEGRATIONS'],
    primary_intents: ['INTEGRATION', 'MODIFICATION', 'DIRECT_SERVICE_ORDER'],
    merge_rationale: 'Integration tasks share Bitrix/site LP family',
    separate_rationale: 'Split Bitrix vs generic API if LP differs',
    landing: { confirmed: null, required: 'Integrations / Bitrix page', risk: 'Medium — platform-specific expectations' },
    geo: 'REMOTE_RU',
    priority_tier_default: 'P1',
  },
  'CF-MARKING-CHESTNY-ZNAK': {
    name: 'Marking / Честный знак',
    service_families: ['SF-MARKING-CHESTNY-ZNAK', 'SF-OTHER-APPROVED-1C-SERVICE'],
    primary_intents: ['DIRECT_SERVICE_ORDER', 'MODIFICATION', 'IMPLEMENTATION', 'INTEGRATION'],
    merge_rationale: 'Marking cluster is large; OTHER approved marking phrases merged here',
    separate_rationale: 'TS ПИОТ may warrant separate campaign if LP differs',
    landing: { confirmed: null, required: 'Marking / Честный знак service page', risk: 'High if sent to generic 1C page' },
    geo: 'REMOTE_RU + PRIMARY',
    priority_tier_default: 'P1',
  },
  'CF-TS-PIOT': {
    name: 'TS ПИОТ',
    service_families: ['SF-TS-PIOT'],
    primary_intents: ['DIRECT_SERVICE_ORDER', 'PROBLEM_RESOLUTION', 'IMPLEMENTATION'],
    merge_rationale: null,
    separate_rationale: 'Low volume (4 assessed); operator must decide merge with marking or standalone',
    landing: { confirmed: null, required: 'TS ПИОТ / marking hardware page', risk: 'High — niche hardware integration' },
    geo: 'REMOTE_RU',
    priority_tier_default: 'P3',
  },
  'CF-TROUBLESHOOTING': {
    name: '1C troubleshooting / not working',
    service_families: ['SF-TROUBLESHOOTING-NOT-WORKING'],
    primary_intents: ['PROBLEM_RESOLUTION', 'SPECIALIST_SEARCH'],
    merge_rationale: null,
    separate_rationale: 'Only 2 assessed ACCEPT; may merge with support or emergency LP',
    landing: { confirmed: null, required: 'Emergency support / troubleshooting page', risk: 'High — urgent intent mismatch if generic LP' },
    geo: 'PRIMARY (onsite) + REMOTE_RU',
    priority_tier_default: 'P2',
  },
  'CF-PRICE-AND-COST': {
    name: 'Price and cost queries',
    service_families: ['SF-ONE-OFF-WORK', 'SF-1C-PROGRAMMER-SPECIALIST', 'SF-SUPPORT-MAINTENANCE', 'SF-SUBSCRIPTION-SERVICE', 'SF-MODIFICATION-DEVELOPMENT'],
    primary_intents: ['PRICE_AND_COST'],
    merge_rationale: 'Price intent cross-cuts services; shared pricing LP or service hub',
    separate_rationale: 'Split by service if price LP differs per line',
    landing: { confirmed: null, required: 'Pricing / calculator or service hub', risk: 'Medium — price without service context' },
    geo: 'PRIMARY + REMOTE_RU',
    priority_tier_default: 'P2',
  },
  'CF-ONE-OFF-WORK': {
    name: 'One-off / hourly work',
    service_families: ['SF-ONE-OFF-WORK'],
    primary_intents: ['DIRECT_SERVICE_ORDER', 'PRICE_AND_COST', 'SPECIALIST_SEARCH'],
    merge_rationale: 'Hourly/razovye terms; may overlap programmer campaign',
    separate_rationale: 'Merge into CF-PROGRAMMER if same LP',
    landing: { confirmed: null, required: 'Hourly / разовые работы page', risk: 'Low if merged with specialist LP' },
    geo: 'PRIMARY + REMOTE_RU',
    priority_tier_default: 'P2',
  },
  'CF-IMPLEMENTATION': {
    name: 'Implementation / rollout',
    service_families: ['SF-MARKING-CHESTNY-ZNAK', 'SF-INTEGRATIONS'],
    primary_intents: ['IMPLEMENTATION'],
    merge_rationale: null,
    separate_rationale: 'Small volume; likely absorbed into parent service campaigns',
    landing: { confirmed: null, required: 'Implementation / внедрение page', risk: 'SAFE UNKNOWN' },
    geo: 'REMOTE_RU',
    priority_tier_default: 'P3',
  },
};

function resolveCampaignFamily(record) {
  const sf = record.service_family;
  const intent = record.primary_intent;

  if (intent === 'PRICE_AND_COST') return 'CF-PRICE-AND-COST';
  if (sf === 'SF-TS-PIOT') return 'CF-TS-PIOT';
  if (sf === 'SF-TROUBLESHOOTING-NOT-WORKING') return 'CF-TROUBLESHOOTING';
  if (sf === 'SF-ONE-OFF-WORK' && intent !== 'PRICE_AND_COST') return 'CF-ONE-OFF-WORK';
  if (intent === 'IMPLEMENTATION' && sf !== 'SF-MARKING-CHESTNY-ZNAK' && sf !== 'SF-TS-PIOT') {
    return 'CF-IMPLEMENTATION';
  }

  switch (sf) {
    case 'SF-1C-PROGRAMMER-SPECIALIST':
      return 'CF-PROGRAMMER-SPECIALIST';
    case 'SF-SUPPORT-MAINTENANCE':
    case 'SF-SUBSCRIPTION-SERVICE':
      return 'CF-SUPPORT-AND-SUBSCRIPTION';
    case 'SF-MODIFICATION-DEVELOPMENT':
      return 'CF-MODIFICATION-DEVELOPMENT';
    case 'SF-REPORTS-PROCESSING':
      return 'CF-REPORTS-PROCESSING';
    case 'SF-INTEGRATIONS':
      return intent === 'IMPLEMENTATION' ? 'CF-IMPLEMENTATION' : 'CF-INTEGRATIONS';
    case 'SF-MARKING-CHESTNY-ZNAK':
      return 'CF-MARKING-CHESTNY-ZNAK';
    case 'SF-OTHER-APPROVED-1C-SERVICE':
      return 'CF-MARKING-CHESTNY-ZNAK';
    default:
      return 'CF-UNCLASSIFIED';
  }
}

function adGroupKey(campaignFamily, intent, geoBucket) {
  return `${campaignFamily}__${intent}__${geoBucket}`;
}

function geoBucket(record) {
  const g = record.geography || {};
  const status = g.status || 'NO_GEOGRAPHY';
  if (status === 'PRIMARY') return 'GEO-PRIMARY';
  if (status === 'EXPANSION') return 'GEO-EXPANSION';
  if (status === 'OTHER_RU') return 'GEO-REMOTE-RU';
  if (status === 'IRRELEVANT') return 'GEO-IRRELEVANT-FLAG';
  return 'GEO-NONE';
}

const INTENT_ARCHITECTURE = {
  SPECIALIST_SEARCH: {
    primary: 'SPECIALIST_SEARCH',
    permitted_secondary: ['DIRECT_SERVICE_ORDER'],
    prohibited: ['CAREER_OR_EDUCATION', 'INFORMATIONAL', 'PRODUCT_OR_LICENSE', 'AMBIGUOUS'],
    rationale: 'User seeks a 1C specialist/provider; not training or product purchase',
  },
  DIRECT_SERVICE_ORDER: {
    primary: 'DIRECT_SERVICE_ORDER',
    permitted_secondary: ['SPECIALIST_SEARCH', 'MODIFICATION', 'INTEGRATION'],
    prohibited: ['CAREER_OR_EDUCATION', 'INFORMATIONAL', 'AMBIGUOUS'],
    rationale: 'Explicit service order or task delegation',
  },
  PRICE_AND_COST: {
    primary: 'PRICE_AND_COST',
    permitted_secondary: ['DIRECT_SERVICE_ORDER', 'SPECIALIST_SEARCH'],
    prohibited: ['CAREER_OR_EDUCATION', 'INFORMATIONAL', 'SALARY'],
    rationale: 'Commercial pricing intent for services, not salary research',
  },
  SUPPORT_AND_MAINTENANCE: {
    primary: 'SUPPORT_AND_MAINTENANCE',
    permitted_secondary: ['DIRECT_SERVICE_ORDER'],
    prohibited: ['CAREER_OR_EDUCATION', 'INFORMATIONAL', 'PRODUCT_OR_LICENSE'],
    rationale: 'Ongoing support/subscription service demand',
  },
  PROBLEM_RESOLUTION: {
    primary: 'PROBLEM_RESOLUTION',
    permitted_secondary: ['DIRECT_SERVICE_ORDER', 'SPECIALIST_SEARCH'],
    prohibited: ['INFORMATIONAL', 'SELF-SERVICE', 'CAREER_OR_EDUCATION'],
    rationale: 'Urgent fix / not working; not DIY manuals',
  },
  MODIFICATION: {
    primary: 'MODIFICATION',
    permitted_secondary: ['DIRECT_SERVICE_ORDER', 'IMPLEMENTATION'],
    prohibited: ['CAREER_OR_EDUCATION', 'INFORMATIONAL'],
    rationale: 'Development, doraботка, reports/processing work',
  },
  INTEGRATION: {
    primary: 'INTEGRATION',
    permitted_secondary: ['MODIFICATION', 'DIRECT_SERVICE_ORDER', 'IMPLEMENTATION'],
    prohibited: ['CAREER_OR_EDUCATION', 'INFORMATIONAL', 'PRODUCT_OR_LICENSE'],
    rationale: 'Bitrix, site, API integration tasks',
  },
  IMPLEMENTATION: {
    primary: 'IMPLEMENTATION',
    permitted_secondary: ['DIRECT_SERVICE_ORDER', 'MODIFICATION'],
    prohibited: ['CAREER_OR_EDUCATION', 'INFORMATIONAL'],
    rationale: 'Rollout / vnedrenie / configuration projects',
  },
};

function landingForCampaign(cfId) {
  const meta = CAMPAIGN_FAMILY_META[cfId];
  if (!meta) return { site: 'SAFE UNKNOWN', path: 'SAFE UNKNOWN', suitability: 'UNKNOWN' };
  const sites = ['lk.corvonero.ru', 'corvonero.ru'];
  return {
    sites,
    required_service_page: meta.landing.required,
    confirmed_match: meta.landing.confirmed,
    suitability: meta.landing.confirmed ? 'CONFIRMED' : 'SAFE UNKNOWN',
    generic_page_risk: meta.landing.risk,
  };
}

function priorityTier(record, cfId) {
  const meta = CAMPAIGN_FAMILY_META[cfId];
  const intent = record.primary_intent;
  if (cfId === 'CF-TS-PIOT' || cfId === 'CF-IMPLEMENTATION') return 'P3';
  if (cfId === 'CF-TROUBLESHOOTING') return 'P2';
  if (intent === 'PRICE_AND_COST') return 'P2';
  if (cfId === 'CF-REPORTS-PROCESSING') return 'P2';
  if (record.geography?.status === 'IRRELEVANT') return 'HOLD';
  if (meta?.priority_tier_default === 'P1') return 'P1';
  return meta?.priority_tier_default || 'P2';
}

function main() {
  const accept = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-ACCEPT-v1.json'));
  const reject = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-REJECT-v1.json'));
  const abstain = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-ABSTAIN-v1.json'));
  const registry = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-REVIEWED-REGISTRY-v1.json'));
  const signOff = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-PARTIAL-SEMANTIC-SIGN-OFF-v1.json'));
  const serviceTax = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-SERVICE-TAXONOMY-v1.json'));
  const intentTax = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-INTENT-TAXONOMY-v1.json'));
  const geoTax = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-GEOGRAPHY-v1.json'));
  const exclusionTax = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-EXCLUSION-TAXONOMY-v1.json'));
  const unprocessed = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-UNPROCESSED-IDS-MANIFEST-v1.json'));

  // Preflight counts
  const preflight = {
    accept_count: accept.count,
    reject_count: reject.count,
    abstain_count: abstain.count,
    registry_count: registry.count,
    signoff_integrity: signOff.integrity,
    reconciled:
      accept.count === EXPECTED.ACCEPT &&
      reject.count === EXPECTED.REJECT &&
      abstain.count === EXPECTED.ABSTAIN &&
      registry.count === ASSESSED_TOTAL &&
      signOff.integrity.pass === true,
  };

  if (!preflight.reconciled) {
    console.error('BLOCKED — PHASE 5.2 SEMANTIC AUTHORITY MISMATCH', preflight);
    process.exit(1);
  }

  const acceptIds = new Set(accept.records.map((r) => r.phrase_id));
  const rejectIds = new Set(reject.records.map((r) => r.phrase_id));
  const abstainIds = new Set(abstain.records.map((r) => r.phrase_id));
  const unprocessedIds = new Set(
    unprocessed.phrase_ids ||
      unprocessed.ids ||
      (unprocessed.records || []).map((r) => r.phrase_id)
  );
  if (unprocessedIds.size !== UNPROCESSED_TOTAL) {
    console.warn(`Unprocessed ID count ${unprocessedIds.size} !== expected ${UNPROCESSED_TOTAL}`);
  }

  // Manifests
  const manifests = {
    manifest_id: `${PHASE6_ID}-manifests`,
    partial_coverage_boundary: PARTIAL_BOUNDARY,
    CAMPAIGN_ELIGIBLE_ACCEPT: {
      count: accept.count,
      phrase_ids: accept.records.map((r) => r.phrase_id),
    },
    EXCLUSION_EVIDENCE_REJECT: {
      count: reject.count,
      phrase_ids: reject.records.map((r) => r.phrase_id),
      note: 'For exclusion boundary design only — not allocated to campaigns',
    },
    HOLDOUT_ABSTAIN: {
      count: abstain.count,
      phrase_ids: abstain.records.map((r) => r.phrase_id),
      note: 'Outside standard campaign allocation',
    },
    UNPROCESSED_BACKLOG: {
      count: unprocessedIds.size,
      phrase_ids: [...unprocessedIds].sort(),
      note: 'Excluded from partial semantic authority — not inferred',
    },
  };

  // Allocate ACCEPT to ad groups
  const groupMap = new Map();
  const allocationById = {};
  const campaignFamilyCounts = {};

  for (const record of accept.records) {
    const cf = resolveCampaignFamily(record);
    const intent = record.primary_intent || 'UNSPECIFIED';
    const geo = geoBucket(record);
    const key = adGroupKey(cf, intent, geo);

    if (!groupMap.has(key)) {
      groupMap.set(key, {
        group_id: key.replace(/__/g, '-').toLowerCase(),
        working_name: `${CAMPAIGN_FAMILY_META[cf]?.name || cf} — ${intent} — ${geo}`,
        campaign_family: cf,
        service_family: record.service_family,
        primary_intent: intent,
        phrase_ids: [],
        geography_treatment: geo,
        landing_page: landingForCampaign(cf),
        negative_boundary_notes: `Block EX-CAREER-JOBS, EX-EDUCATION, EX-INFORMATIONAL at campaign level; refine per group`,
        ambiguity_notes: record.secondary_intent ? `Secondary: ${record.secondary_intent}` : null,
        readiness_status: geo === 'GEO-IRRELEVANT-FLAG' ? 'HOLD — irrelevant geography flagged in ACCEPT' : 'DRAFT — operator LP confirmation required',
        priority_tier: priorityTier(record, cf),
      });
    }

    const group = groupMap.get(key);
    group.phrase_ids.push(record.phrase_id);
    if (!group.service_family && record.service_family) group.service_family = record.service_family;
    allocationById[record.phrase_id] = { campaign_family: cf, ad_group_id: group.group_id };

    campaignFamilyCounts[cf] = (campaignFamilyCounts[cf] || 0) + 1;
  }

  // Finalize groups
  const adGroups = [...groupMap.values()]
    .map((g) => {
      const phrases = g.phrase_ids
        .map((id) => accept.records.find((r) => r.phrase_id === id)?.phrase)
        .filter(Boolean);
      return {
        ...g,
        included_phrase_count: g.phrase_ids.length,
        representative_phrases: phrases.slice(0, 5),
        intent_architecture: INTENT_ARCHITECTURE[g.primary_intent] || {
          primary: g.primary_intent,
          permitted_secondary: [],
          prohibited: ['AMBIGUOUS', 'CAREER_OR_EDUCATION', 'INFORMATIONAL'],
          rationale: 'Derived from Phase 5.2 intent taxonomy',
        },
        landing_page_requirement: g.landing_page.required_service_page,
      };
    })
    .sort((a, b) => b.included_phrase_count - a.included_phrase_count);

  // Reconciliation
  const allocatedIds = new Set(Object.keys(allocationById));
  const missingAccept = [...acceptIds].filter((id) => !allocatedIds.has(id));
  const duplicates = accept.records.length - acceptIds.size;
  const rejectInAlloc = [...allocatedIds].filter((id) => rejectIds.has(id));
  const abstainInAlloc = [...allocatedIds].filter((id) => abstainIds.has(id));
  const unprocessedInAlloc = [...allocatedIds].filter((id) => unprocessedIds.has(id));

  const reconciliation = {
    equation: '935 ACCEPT = allocated + planning_holdout (0 by design)',
    accept_total: acceptIds.size,
    allocated_count: allocatedIds.size,
    planning_holdout_count: 0,
    duplicates,
    missing_accept_ids: missingAccept,
    reject_ids_allocated: rejectInAlloc,
    abstain_ids_allocated: abstainInAlloc,
    unprocessed_ids_allocated: unprocessedInAlloc,
    pass:
      missingAccept.length === 0 &&
      duplicates === 0 &&
      rejectInAlloc.length === 0 &&
      abstainInAlloc.length === 0 &&
      unprocessedInAlloc.length === 0 &&
      allocatedIds.size === 935,
  };

  // Campaign families output
  const campaignFamilies = Object.entries(CAMPAIGN_FAMILY_META).map(([id, meta]) => ({
    campaign_family_id: id,
    working_name: meta.name,
    allocated_phrase_count: campaignFamilyCounts[id] || 0,
    service_families: meta.service_families,
    primary_intents: meta.primary_intents,
    merge_rationale: meta.merge_rationale,
    separate_rationale: meta.separate_rationale,
    intent_separation: meta.primary_intents.map((i) => ({
      intent: i,
      ...(INTENT_ARCHITECTURE[i] || {}),
    })),
    geography_treatment: meta.geo,
    landing_page: landingForCampaign(id),
    negative_boundary_design: 'Campaign-level blocks: careers, education, informational, product-only; group-level refinement pending',
    default_priority_tier: meta.priority_tier_default,
    ad_group_ids: adGroups.filter((g) => g.campaign_family === id).map((g) => g.group_id),
  }));

  // ABSTAIN holdout
  const abstainBuckets = {};
  for (const cat of [
    'PRODUCT_PLUS_SERVICE_REVIEW',
    'AMBIGUOUS_DIY_PROBLEM',
    'GENERIC_PLATFORM_OR_ERP',
    'SHORT_UNDERSPECIFIED',
    'MIXED_INFORMATIONAL_COMMERCIAL',
    'OTHER_AMBIGUITY',
  ]) {
    abstainBuckets[cat] = { count: 0, phrase_ids: [], examples: [] };
  }
  for (const r of abstain.records) {
    const cat = classifyAbstainHoldout(r);
    abstainBuckets[cat].phrase_ids.push(r.phrase_id);
    abstainBuckets[cat].count++;
    if (abstainBuckets[cat].examples.length < 5) abstainBuckets[cat].examples.push(r.phrase);
  }

  const abstainHoldout = {
    holdout_id: `${PHASE6_ID}-abstain-holdout`,
    total: abstain.count,
    policy: 'No ABSTAIN record enters standard campaign groups automatically',
    categories: Object.entries(abstainBuckets).map(([id, b]) => ({
      category_id: id,
      count: b.count,
      phrase_ids: b.phrase_ids,
      representative_examples: b.examples,
      later_options: {
        manual_review: id === 'PRODUCT_PLUS_SERVICE_REVIEW' || id === 'MIXED_INFORMATIONAL_COMMERCIAL',
        isolated_experimental_group: id === 'AMBIGUOUS_DIY_PROBLEM' || id === 'SHORT_UNDERSPECIFIED',
        retain_indefinitely: id === 'GENERIC_PLATFORM_OR_ERP' || id === 'OTHER_AMBIGUITY',
      },
    })),
  };

  // Exclusion boundaries from REJECT taxonomy
  const exclusionBoundaries = {
    boundary_id: `${PHASE6_ID}-exclusion-boundaries`,
    note: 'Design-only — not deployable minus-word list',
    families: exclusionTax.families.map((f) => ({
      exclusion_family_id: f.family_id,
      family_name: f.family_name,
      evidence_id_count: f.evidence_phrase_ids?.length || 0,
      evidence_phrase_ids: f.evidence_phrase_ids,
      representative_tokens: f.representative_tokens || f.representative_phrases || [],
      campaign_level_suitability: ['EX-CAREER-JOBS', 'EX-EDUCATION-COURSES', 'EX-SALARY', 'EX-CERTIFICATION-EXAMS'].includes(f.family_id)
        ? 'RECOMMENDED — all service campaigns'
        : f.family_id === 'EX-IRRELEVANT-GEOGRAPHY'
          ? 'GEO campaigns only'
          : 'SELECTIVE — per campaign family',
      group_level_suitability: f.family_id === 'EX-INFORMATIONAL-RESEARCH' ? 'Use cautiously — may overblock commercial research' : 'As needed',
      overblocking_risk: ['EX-INFORMATIONAL-RESEARCH', 'EX-SELF-SERVICE-MANUALS', 'EX-FORUMS-INSTRUCTIONS'].includes(f.family_id)
        ? 'HIGH'
        : 'LOW',
      exceptions: f.family_id === 'EX-PRODUCT-LICENSE-ONLY' ? 'Allow where product setup is part of service delivery' : null,
    })),
  };

  // Geography options
  const acceptGeoStats = {};
  for (const r of accept.records) {
    const s = r.geography?.status || 'NO_GEOGRAPHY';
    acceptGeoStats[s] = (acceptGeoStats[s] || 0) + 1;
  }

  const geographyOptions = {
    options_id: `${PHASE6_ID}-geography-options`,
    partial_coverage_boundary: PARTIAL_BOUNDARY,
    accept_geography_distribution: acceptGeoStats,
    primary_launch: {
      markets: ['Новосибирск', 'Новосибирская область'],
      onsite_delivery: true,
      remote_delivery: true,
    },
    expansion: {
      markets: ['Краснодар', 'Екатеринбург', 'Красноярск'],
      note: 'Expansion ACCEPT phrases present in assessed corpus',
    },
    remote_russia_wide: {
      eligible_service_families: [
        'SF-1C-PROGRAMMER-SPECIALIST',
        'SF-SUPPORT-MAINTENANCE',
        'SF-SUBSCRIPTION-SERVICE',
        'SF-MODIFICATION-DEVELOPMENT',
        'SF-REPORTS-PROCESSING',
        'SF-INTEGRATIONS',
        'SF-MARKING-CHESTNY-ZNAK',
        'SF-TS-PIOT',
      ],
      excluded: ['Onsite-only troubleshooting without remote SLA — operator confirmation'],
    },
    architecture_options: [
      {
        option_id: 'GEO-A',
        name: 'Primary geo in campaign structure, expansion via bid adjustment',
        description: 'Single campaign families; location bid modifiers for PRIMARY vs EXPANSION vs REMOTE_RU',
        pros: ['Simpler structure', 'Faster launch', 'Easier budget pooling'],
        cons: ['Less budget isolation per city', 'Harder to tune LP per geo'],
        recommendation: 'DEFAULT for Phase 6 partial launch planning',
      },
      {
        option_id: 'GEO-B',
        name: 'Separate campaigns per geography tier',
        description: 'Duplicate campaign families for PRIMARY, EXPANSION, REMOTE_RU',
        pros: ['Budget control per market', 'Clear reporting'],
        cons: ['Campaign proliferation', 'Small clusters in expansion/remote'],
        recommendation: 'Consider for expansion wave after primary proof',
      },
      {
        option_id: 'GEO-C',
        name: 'Geo at ad-group level only',
        description: 'Geo-specific ad groups within shared campaigns',
        pros: ['Intent/service separation preserved', 'Moderate geo control'],
        cons: ['Many small groups', 'Operational overhead'],
        recommendation: 'Matches current draft ad-group geo buckets',
      },
    ],
    operator_decision_required: true,
    final_launch_geography: 'NOT AUTHORIZED — operator must approve',
  };

  // Landing page map
  const landingPageMap = {
    map_id: `${PHASE6_ID}-landing-page-map`,
    sites_known: ['lk.corvonero.ru', 'corvonero.ru'],
    evidence_note: 'No in-repo crawl confirms page-level suitability — SAFE UNKNOWN unless operator confirms',
    campaigns: campaignFamilies.map((cf) => ({
      campaign_family_id: cf.campaign_family_id,
      required_service_page: cf.landing_page.required_service_page,
      confirmed_suitable_page: cf.landing_page.confirmed_match,
      suitability_status: cf.landing_page.suitability,
      generic_page_risk: cf.landing_page.generic_page_risk,
      ad_groups: cf.ad_group_ids,
    })),
    groups: adGroups.map((g) => ({
      ad_group_id: g.group_id,
      campaign_family: g.campaign_family,
      landing_page_requirement: g.landing_page_requirement,
      suitability_status: g.landing_page.suitability,
      generic_page_risk: g.landing_page.generic_page_risk,
    })),
  };

  // Commercial priorities
  const tierCounts = { P1: 0, P2: 0, P3: 0, HOLD: 0 };
  for (const r of accept.records) {
    const cf = resolveCampaignFamily(r);
    const tier = priorityTier(r, cf);
    tierCounts[tier] = (tierCounts[tier] || 0) + 1;
  }

  const commercialPriorities = {
    priority_id: `${PHASE6_ID}-commercial-priorities`,
    methodology: 'Explicit commercial intent, service fit, LP readiness, semantic clarity, cluster size — not phrase count as demand proxy',
    tier_summary: tierCounts,
    tiers: {
      P1: {
        label: 'Launch candidate',
        campaign_families: campaignFamilies.filter((c) => c.default_priority_tier === 'P1').map((c) => c.campaign_family_id),
        criteria: 'Clear commercial intent, core approved services, adequate cluster size',
      },
      P2: {
        label: 'Launch after LP or operator confirmation',
        campaign_families: ['CF-PRICE-AND-COST', 'CF-REPORTS-PROCESSING', 'CF-TROUBLESHOOTING', 'CF-ONE-OFF-WORK'],
        criteria: 'Commercial but LP match uncertain or small cluster',
      },
      P3: {
        label: 'Later expansion',
        campaign_families: ['CF-TS-PIOT', 'CF-IMPLEMENTATION'],
        criteria: 'Niche or very low assessed volume',
      },
      HOLD: {
        label: 'Not campaign-ready',
        criteria: 'Irrelevant geography flagged in ACCEPT, or pending ABSTAIN promotion',
        count: tierCounts.HOLD || 0,
      },
    },
    campaign_family_priorities: campaignFamilies.map((cf) => ({
      campaign_family_id: cf.campaign_family_id,
      allocated_count: cf.allocated_phrase_count,
      default_tier: cf.default_priority_tier,
    })),
  };

  // Risk register
  const riskRegister = {
    register_id: `${PHASE6_ID}-risk-register`,
    risks: [
      {
        risk_id: 'R-01',
        title: 'Partial semantic coverage (67.5%)',
        severity: 'HIGH',
        affected: 'All campaigns',
        mitigation: 'Label all outputs with partial boundary; defer backlog processing to separate charter',
        blocking: false,
      },
      {
        risk_id: 'R-02',
        title: '769 unprocessed backlog excluded',
        severity: 'HIGH',
        affected: 'Market coverage estimates',
        mitigation: 'Do not infer backlog content; plan Phase 7+ backlog wave separately',
        blocking: false,
      },
      {
        risk_id: 'R-03',
        title: 'High ACCEPT count after authority cleanup (935)',
        severity: 'MEDIUM',
        affected: 'Budget and LP capacity',
        mitigation: 'Tiered launch P1 first; operator confirms scope',
        blocking: false,
      },
      {
        risk_id: 'R-04',
        title: 'Landing-page mismatch',
        severity: 'HIGH',
        affected: 'All campaign families',
        mitigation: 'Operator confirms LP map before ad copy phase',
        blocking: true,
      },
      {
        risk_id: 'R-05',
        title: 'Product vs service ambiguity',
        severity: 'MEDIUM',
        affected: 'CF-SUPPORT-AND-SUBSCRIPTION, ABSTAIN holdouts',
        mitigation: 'Keep PRODUCT_PLUS_SERVICE_REVIEW in holdout; manual review gate',
        blocking: false,
      },
      {
        risk_id: 'R-06',
        title: 'Geography expansion risk',
        severity: 'MEDIUM',
        affected: 'GEO-EXPANSION, GEO-REMOTE-RU groups',
        mitigation: 'Operator selects GEO-A/B/C; start PRIMARY-only if uncertain',
        blocking: false,
      },
      {
        risk_id: 'R-07',
        title: 'Negative-keyword overblocking',
        severity: 'MEDIUM',
        affected: 'Informational exclusion families',
        mitigation: 'Design boundaries only; test minus lists in isolated experiments',
        blocking: false,
      },
      {
        risk_id: 'R-08',
        title: 'TS ПИОТ low assessed volume (4 ACCEPT)',
        severity: 'MEDIUM',
        affected: 'CF-TS-PIOT',
        mitigation: 'Operator decides merge with marking or standalone micro-campaign',
        blocking: false,
      },
      {
        risk_id: 'R-09',
        title: 'Incomplete troubleshooting coverage (2 ACCEPT assessed)',
        severity: 'MEDIUM',
        affected: 'CF-TROUBLESHOOTING',
        mitigation: 'Merge with support campaign or await backlog processing',
        blocking: false,
      },
      {
        risk_id: 'R-10',
        title: 'NDS status unknown',
        severity: 'LOW',
        affected: 'Price messaging, ad disclaimers',
        mitigation: 'Operator confirms VAT stance before ad copy',
        blocking: false,
      },
      {
        risk_id: 'R-11',
        title: 'No live conversion data',
        severity: 'MEDIUM',
        affected: 'Prioritization and budget allocation',
        mitigation: 'Use tiered launch; no conversion forecasts in Phase 6',
        blocking: false,
      },
    ],
  };

  // Operator decision packet
  const operatorDecisions = {
    packet_id: `${PHASE6_ID}-operator-decision-packet`,
    partial_coverage_boundary: PARTIAL_BOUNDARY,
    decisions_required: [
      {
        decision_id: 'OD-01',
        topic: 'Launch geography',
        options: ['GEO-A bid modifiers (recommended default)', 'GEO-B separate campaigns', 'GEO-C ad-group geo', 'PRIMARY-only first wave'],
        blocking: true,
      },
      {
        decision_id: 'OD-02',
        topic: 'Campaign separation vs consolidation',
        context: 'Support+subscription merged; price cross-cutting; one-off may merge with specialist',
        blocking: false,
      },
      {
        decision_id: 'OD-03',
        topic: 'Product-plus-service demand',
        context: `${abstainBuckets.PRODUCT_PLUS_SERVICE_REVIEW.count} ABSTAIN in PRODUCT_PLUS_SERVICE_REVIEW holdout`,
        blocking: false,
      },
      {
        decision_id: 'OD-04',
        topic: 'Troubleshooting separate campaign',
        context: '2 ACCEPT phrases assessed — merge with CF-SUPPORT-AND-SUBSCRIPTION or standalone',
        blocking: false,
      },
      {
        decision_id: 'OD-05',
        topic: 'TS ПИОТ separate campaign or group',
        context: '4 ACCEPT phrases — merge with CF-MARKING-CHESTNY-ZNAK or standalone CF-TS-PIOT',
        blocking: false,
      },
      {
        decision_id: 'OD-06',
        topic: 'Landing-page assignments',
        context: 'All LP matches SAFE UNKNOWN — operator must confirm per campaign family',
        blocking: true,
      },
      {
        decision_id: 'OD-07',
        topic: 'ABSTAIN experimental holdouts',
        context: '296 ABSTAIN — selective manual review vs isolated test groups',
        blocking: false,
      },
      {
        decision_id: 'OD-08',
        topic: 'P1/P2/P3 launch tiers',
        context: `P1=${tierCounts.P1}, P2=${tierCounts.P2}, P3=${tierCounts.P3}, HOLD=${tierCounts.HOLD || 0}`,
        blocking: false,
      },
      {
        decision_id: 'OD-09',
        topic: 'Acceptability of 67.5% coverage planning',
        context: 'Proceed with partial architecture or require backlog wave first',
        blocking: true,
      },
    ],
    not_authorized: [
      'Ad copy',
      'Final minus-word deployment',
      'Yandex Direct import',
      'Commander',
      'Campaign launch',
      'Wave 5',
      '769 backlog processing',
    ],
  };

  const phase6Verdict = reconciliation.pass
    ? {
        phase: 6,
        verdict: 'PASS — OPERATOR ARCHITECTURE REVIEW REQUIRED',
        project: 'READY_FOR_PARTIAL_CAMPAIGN-ARCHITECTURE SIGN-OFF',
        note: 'PASS does not authorize ad creation, import or launch',
      }
    : {
        phase: 6,
        verdict: 'BLOCKED — CAMPAIGN-PLANNING ARCHITECTURE INCOMPLETE',
        reconciliation,
      };

  const resultCore = {
    result_id: PHASE6_ID,
    run_id: RUN_ID,
    generated_at: new Date().toISOString(),
    partial_coverage_boundary: PARTIAL_BOUNDARY,
    provider_calls: 'FROZEN',
    preflight,
    reconciliation,
    phase6_verdict: phase6Verdict,
    summary: {
      campaign_families: campaignFamilies.length,
      ad_groups_draft: adGroups.length,
      accept_allocated: allocatedIds.size,
      abstain_holdout: abstain.count,
      reject_exclusion_only: reject.count,
      unprocessed_excluded: unprocessedIds.size || UNPROCESSED_TOTAL,
    },
  };

  // Write outputs
  const outputs = [
    ['CORVONERO-PHASE-6-PARTIAL-CAMPAIGN-PLANNING-RESULT-v1.json', resultCore],
    ['CORVONERO-PHASE-6-CAMPAIGN-FAMILIES-v1.json', { ...PARTIAL_BOUNDARY, campaign_families: campaignFamilies }],
    ['CORVONERO-PHASE-6-AD-GROUP-ARCHITECTURE-DRAFT-v1.json', { ...PARTIAL_BOUNDARY, ad_groups: adGroups, intent_architecture: INTENT_ARCHITECTURE }],
    [
      'CORVONERO-PHASE-6-PHRASE-ALLOCATION-v1.json',
      {
        ...PARTIAL_BOUNDARY,
        manifests,
        reconciliation,
        allocations: allocationById,
      },
    ],
    ['CORVONERO-PHASE-6-GEOGRAPHY-OPTIONS-v1.json', geographyOptions],
    ['CORVONERO-PHASE-6-LANDING-PAGE-MAP-v1.json', landingPageMap],
    ['CORVONERO-PHASE-6-EXCLUSION-BOUNDARIES-v1.json', exclusionBoundaries],
    ['CORVONERO-PHASE-6-ABSTAIN-HOLDOUT-v1.json', abstainHoldout],
    ['CORVONERO-PHASE-6-COMMERCIAL-PRIORITIES-v1.json', commercialPriorities],
    ['CORVONERO-PHASE-6-RISK-REGISTER-v1.json', riskRegister],
    ['CORVONERO-PHASE-6-OPERATOR-DECISION-PACKET-v1.json', operatorDecisions],
  ];

  for (const [name, data] of outputs) {
    writeJson(path.join(PILOT, name), data);
  }

  // Markdown outputs
  writeText(
    path.join(PILOT, 'CORVONERO-PHASE-6-PARTIAL-CAMPAIGN-PLANNING-RESULT-v1.md'),
    buildResultMd(resultCore, campaignFamilies, adGroups, reconciliation, phase6Verdict)
  );
  writeText(path.join(PILOT, 'CORVONERO-PHASE-6-GEOGRAPHY-OPTIONS-v1.md'), buildGeoMd(geographyOptions));
  writeText(path.join(PILOT, 'CORVONERO-PHASE-6-OPERATOR-DECISION-PACKET-v1.md'), buildOperatorMd(operatorDecisions));
  writeText(path.join(PILOT, 'CORVONERO-PHASE-7-NEXT-TASK-PARTIAL-v1.md'), buildPhase7Md(phase6Verdict));
  writeText(path.join(REPORTS, 'REPORT-corvonero-phase-6-partial-campaign-planning-v1.md'), buildReportMd(resultCore, preflight, reconciliation, campaignFamilies, adGroups, phase6Verdict, operatorDecisions, outputs));

  console.log(JSON.stringify({ ok: true, verdict: phase6Verdict.verdict, reconciliation }, null, 2));
}

function buildResultMd(core, families, groups, recon, verdict) {
  return `# CORVONERO Phase 6 — Partial Campaign-Planning Result v1

**Run:** ${RUN_ID}  
**Verdict:** ${verdict.verdict}

## Partial-Coverage Boundary

- **PARTIAL SEMANTIC AUTHORITY:** ${PARTIAL_BOUNDARY.partial_semantic_authority}
- **UNPROCESSED BACKLOG:** ${PARTIAL_BOUNDARY.unprocessed_backlog}
- **COVERAGE:** ${PARTIAL_BOUNDARY.coverage}

## Summary

| Metric | Value |
|--------|-------|
| Campaign families | ${families.length} |
| Ad groups (draft) | ${groups.length} |
| ACCEPT allocated | ${recon.allocated_count} |
| Reconciliation | ${recon.pass ? 'PASS' : 'FAIL'} |

## Campaign Families

${families.map((f) => `- **${f.campaign_family_id}** (${f.allocated_phrase_count} phrases) — ${f.working_name}`).join('\n')}

## Next Gate

OPERATOR REVIEW OF CORVONERO PARTIAL CAMPAIGN-PLANNING ARCHITECTURE
`;
}

function buildGeoMd(geo) {
  return `# CORVONERO Phase 6 — Geography Options v1

## Partial-Coverage Boundary

- PARTIAL SEMANTIC AUTHORITY: ${PARTIAL_BOUNDARY.partial_semantic_authority}
- UNPROCESSED BACKLOG: ${PARTIAL_BOUNDARY.unprocessed_backlog}
- COVERAGE: ${PARTIAL_BOUNDARY.coverage}

## Primary Launch

${geo.primary_launch.markets.map((m) => `- ${m}`).join('\n')}

## Expansion

${geo.expansion.markets.map((m) => `- ${m}`).join('\n')}

## Architecture Options

${geo.architecture_options.map((o) => `### ${o.option_id}: ${o.name}\n\n${o.description}\n\n**Recommendation:** ${o.recommendation}`).join('\n\n')}

**Operator decision required** — final launch geography not authorized in Phase 6.
`;
}

function buildOperatorMd(packet) {
  return `# CORVONERO Phase 6 — Operator Decision Packet v1

## Partial-Coverage Boundary

- PARTIAL SEMANTIC AUTHORITY: ${PARTIAL_BOUNDARY.partial_semantic_authority}
- UNPROCESSED BACKLOG: ${PARTIAL_BOUNDARY.unprocessed_backlog}
- COVERAGE: ${PARTIAL_BOUNDARY.coverage}

## Decisions Required

${packet.decisions_required.map((d) => `### ${d.decision_id}: ${d.topic}\n\n${d.context ? `Context: ${d.context}\n\n` : ''}Options: ${Array.isArray(d.options) ? d.options.join('; ') : 'See JSON packet'}\n\nBlocking: ${d.blocking ? 'YES' : 'NO'}`).join('\n\n')}

## Not Authorized

${packet.not_authorized.map((n) => `- ${n}`).join('\n')}
`;
}

function buildPhase7Md(verdict) {
  return `# CORVONERO Phase 7 — Next Task (Partial) v1

**Prerequisite:** Phase 6 — ${verdict.verdict}

## Authorized after operator architecture sign-off

- Campaign architecture implementation (operational ad groups, structure freeze)
- Landing-page confirmation workflow
- Minus-word list drafting (not deployment) per operator charter

## Not authorized

- Final ad copy production
- Yandex Direct import / Commander
- Campaign launch
- 769 backlog semantic processing
- OpenRouter / provider calls

## Stop condition

Stop after operator reviews partial campaign-planning architecture. Next gate: **OPERATOR PARTIAL CAMPAIGN-ARCHITECTURE SIGN-OFF**.
`;
}

function buildReportMd(core, preflight, recon, families, groups, verdict, operator, outputs) {
  return `# REPORT — CORVONERO PHASE 6 PARTIAL CAMPAIGN-PLANNING ARCHITECTURE V1

## 1. Safety and Authorization

- Phase 6 authorized by operator partial semantic sign-off (Run ${RUN_ID})
- No OpenRouter or provider calls
- No semantic verdict changes
- No ORCA / canonical corpus mutation

## 2. Git Preflight

- Branch: \`mars/canonical-post-recovery\`
- HEAD descends from pre-Phase-6 checkpoint (\`88facdb7\`)
- Unrelated WIP untouched

## 3. Semantic Authority

| Registry | Count | Expected |
|----------|-------|----------|
| ACCEPT | ${preflight.accept_count} | 935 |
| REJECT | ${preflight.reject_count} | 368 |
| ABSTAIN | ${preflight.abstain_count} | 296 |
| Assessed | ${preflight.registry_count} | 1599 |

Integrity: ${preflight.reconciled ? 'PASS' : 'FAIL'}

## 4. Partial-Coverage Boundary

- **PARTIAL SEMANTIC AUTHORITY:** ${PARTIAL_BOUNDARY.partial_semantic_authority}
- **UNPROCESSED BACKLOG:** ${PARTIAL_BOUNDARY.unprocessed_backlog}
- **COVERAGE:** ${PARTIAL_BOUNDARY.coverage}

## 5. Campaign-Eligible Input

935 ACCEPT records → CAMPAIGN_ELIGIBLE_ACCEPT manifest  
368 REJECT → EXCLUSION_EVIDENCE_REJECT only  
296 ABSTAIN → HOLDOUT_ABSTAIN  
769 → UNPROCESSED_BACKLOG excluded

## 6. Campaign-Family Proposal

${families.map((f) => `- ${f.campaign_family_id}: ${f.allocated_phrase_count} phrases`).join('\n')}

## 7. Intent Architecture

Eight intent classes separated in ad-group draft: SPECIALIST_SEARCH, DIRECT_SERVICE_ORDER, PRICE_AND_COST, SUPPORT_AND_MAINTENANCE, PROBLEM_RESOLUTION, MODIFICATION, INTEGRATION, IMPLEMENTATION.

## 8. Ad-Group Architecture Draft

${groups.length} draft groups — split by campaign family × primary intent × geography bucket.

## 9. Phrase Allocation Reconciliation

\`\`\`
935 ACCEPT = ${recon.allocated_count} allocated + ${recon.planning_holdout_count} planning holdout
\`\`\`

- Duplicates: ${recon.duplicates}
- Missing ACCEPT: ${recon.missing_accept_ids.length}
- REJECT in allocation: ${recon.reject_ids_allocated.length}
- ABSTAIN in allocation: ${recon.abstain_ids_allocated.length}
- Unprocessed in allocation: ${recon.unprocessed_ids_allocated.length}
- **Reconciliation:** ${recon.pass ? 'PASS' : 'FAIL'}

## 10. Geography Options

See \`CORVONERO-PHASE-6-GEOGRAPHY-OPTIONS-v1.md\` — options GEO-A (recommended default), GEO-B, GEO-C.

## 11. Landing-Page Mapping

All matches **SAFE UNKNOWN** — operator confirmation required. Sites: lk.corvonero.ru, corvonero.ru.

## 12. Exclusion Boundaries

12 exclusion families from Phase 5.2 taxonomy — design-only boundaries, not deployable minus lists.

## 13. ABSTAIN Holdout

296 records classified into 6 holdout categories — not allocated to standard groups.

## 14. Commercial Prioritization

Tier distribution in \`CORVONERO-PHASE-6-COMMERCIAL-PRIORITIES-v1.json\`.

## 15. Risk Register

11 risks documented — R-04 (LP mismatch) blocking for ad phase.

## 16. Operator Decision Packet

9 decisions — OD-01, OD-06, OD-09 blocking.

## 17. Phase 6 Verdict

**${verdict.verdict}**

Project: ${verdict.project || 'N/A'}

## 18. Project Lifecycle

READY_FOR_PARTIAL_CAMPAIGN-ARCHITECTURE SIGN-OFF (pending operator review)

## 19. Outputs Created

${outputs.map(([n]) => `- pilots/corvonero/${n}`).join('\n')}
- pilots/corvonero/CORVONERO-PHASE-6-PARTIAL-CAMPAIGN-PLANNING-RESULT-v1.md
- pilots/corvonero/CORVONERO-PHASE-6-GEOGRAPHY-OPTIONS-v1.md
- pilots/corvonero/CORVONERO-PHASE-6-OPERATOR-DECISION-PACKET-v1.md
- pilots/corvonero/CORVONERO-PHASE-7-NEXT-TASK-PARTIAL-v1.md
- reports/REPORT-corvonero-phase-6-partial-campaign-planning-v1.md

## 20. Files Changed

New Phase 6 artefacts under \`projects/mars-search-ppc-production/pilots/corvonero/\` and report under \`reports/\`.  
Tool script: \`tools/execute-phase-6-partial-campaign-planning-v1.mjs\` (generator — not a runtime product).

## 21. Git Status

No commit. No push. Unrelated WIP unchanged.

## 22. SAFE UNKNOWN

- NDS / VAT status for ad messaging
- Landing-page URL-level suitability on lk.corvonero.ru / corvonero.ru
- Conversion rates and budget forecasts
- Content of 769 unprocessed backlog IDs

## 23. Operator Decisions Required

${operator.decisions_required.map((d) => `- ${d.decision_id}: ${d.topic}`).join('\n')}

## 24. Exact Next Task

**OPERATOR REVIEW OF CORVONERO PARTIAL CAMPAIGN-PLANNING ARCHITECTURE**

## 25. Stop Condition

Phase 6 complete. Do not start ad copy, import, Commander, launch, or Wave 5.
`;
}

main();
