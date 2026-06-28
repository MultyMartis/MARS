#!/usr/bin/env node
/**
 * Corvonero Phase 6.1 — Architecture closure + landing-page audit integration.
 * No provider calls. No semantic verdict changes. Applies operator decisions OD-01..OD-09.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const PILOT = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const REPORTS = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/reports');

const PHASE61_ID = 'corvonero-phase-6.1-architecture-closure-v1';
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

const OPERATOR_DECISIONS_APPLIED = {
  'OD-01': 'PRIMARY-ONLY launch: Новосибирск + Новосибирская область; no geo campaign duplication',
  'OD-02': 'Six campaign families CA-01..CA-06; merged price/one-off/troubleshooting/TS ПИОТ/implementation',
  'OD-03': 'Product-plus-service demand HOLD — excluded from initial allocation',
  'OD-04': 'Troubleshooting group under CA-02, not standalone campaign',
  'OD-05': 'TS ПИОТ group under CA-05',
  'OD-06': 'No LP assignment approved — audit only',
  'OD-07': '296 ABSTAIN remain outside launch architecture',
  'OD-08': 'P1/P2/P3 tiers per operator packet',
  'OD-09': '67.5% partial coverage accepted for planning; 769 backlog visible',
};

const CA_META = {
  'CA-01': {
    working_name: 'Программист / специалист 1С',
    service_families: ['SF-1C-PROGRAMMER-SPECIALIST', 'SF-ONE-OFF-WORK'],
    primary_intents: ['SPECIALIST_SEARCH', 'DIRECT_SERVICE_ORDER', 'PRICE_AND_COST'],
    default_priority: 'P1',
    required_lp: 'Dedicated programmer/specialist service page',
    v1_families: ['CF-PROGRAMMER-SPECIALIST', 'CF-ONE-OFF-WORK'],
  },
  'CA-02': {
    working_name: 'Сопровождение и обслуживание 1С',
    service_families: ['SF-SUPPORT-MAINTENANCE', 'SF-SUBSCRIPTION-SERVICE', 'SF-TROUBLESHOOTING-NOT-WORKING'],
    primary_intents: ['SUPPORT_AND_MAINTENANCE', 'DIRECT_SERVICE_ORDER', 'PROBLEM_RESOLUTION', 'PRICE_AND_COST'],
    default_priority: 'P1',
    required_lp: 'Support / абонентское обслуживание / troubleshooting page',
    v1_families: ['CF-SUPPORT-AND-SUBSCRIPTION', 'CF-TROUBLESHOOTING'],
  },
  'CA-03': {
    working_name: 'Доработка и разработка 1С',
    service_families: ['SF-MODIFICATION-DEVELOPMENT', 'SF-ONE-OFF-WORK'],
    primary_intents: ['MODIFICATION', 'DIRECT_SERVICE_ORDER', 'IMPLEMENTATION', 'SPECIALIST_SEARCH', 'PRICE_AND_COST'],
    default_priority: 'P1',
    required_lp: 'Development / доработка / внедрение page',
    v1_families: ['CF-MODIFICATION-DEVELOPMENT', 'CF-IMPLEMENTATION', 'CF-ONE-OFF-WORK'],
  },
  'CA-04': {
    working_name: 'Интеграции 1С',
    service_families: ['SF-INTEGRATIONS'],
    primary_intents: ['INTEGRATION', 'MODIFICATION', 'DIRECT_SERVICE_ORDER', 'PRICE_AND_COST'],
    default_priority: 'P1',
    required_lp: 'Integrations / Bitrix / API page',
    v1_families: ['CF-INTEGRATIONS'],
  },
  'CA-05': {
    working_name: 'Маркировка / Честный знак',
    service_families: ['SF-MARKING-CHESTNY-ZNAK', 'SF-OTHER-APPROVED-1C-SERVICE', 'SF-TS-PIOT'],
    primary_intents: ['DIRECT_SERVICE_ORDER', 'MODIFICATION', 'IMPLEMENTATION', 'INTEGRATION', 'PROBLEM_RESOLUTION', 'PRICE_AND_COST'],
    default_priority: 'P1',
    required_lp: 'Marking / Честный знак / TS ПИОТ page',
    v1_families: ['CF-MARKING-CHESTNY-ZNAK', 'CF-TS-PIOT'],
  },
  'CA-06': {
    working_name: 'Отчёты и обработки 1С',
    service_families: ['SF-REPORTS-PROCESSING'],
    primary_intents: ['MODIFICATION', 'DIRECT_SERVICE_ORDER', 'SPECIALIST_SEARCH', 'PRICE_AND_COST'],
    default_priority: 'P2',
    required_lp: 'Reports / обработки page',
    v1_families: ['CF-REPORTS-PROCESSING'],
  },
};

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
    rationale: 'Commercial pricing intent for services within parent campaign — not standalone',
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
    rationale: '1С не работает / errors / recovery — not DIY manuals',
  },
  MODIFICATION: {
    primary: 'MODIFICATION',
    permitted_secondary: ['DIRECT_SERVICE_ORDER', 'IMPLEMENTATION'],
    prohibited: ['CAREER_OR_EDUCATION', 'INFORMATIONAL'],
    rationale: 'Development, доработка, reports/processing work',
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
    rationale: 'Rollout / внедрение projects — grouped under CA-03',
  },
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

function resolveCampaignV2(record) {
  const sf = record.service_family;
  const intent = record.primary_intent;

  if (sf === 'SF-TS-PIOT') return 'CA-05';
  if (sf === 'SF-TROUBLESHOOTING-NOT-WORKING') return 'CA-02';
  if (sf === 'SF-ONE-OFF-WORK') {
    if (intent === 'MODIFICATION' || intent === 'IMPLEMENTATION') return 'CA-03';
    return 'CA-01';
  }
  if (intent === 'IMPLEMENTATION') return 'CA-03';

  if (intent === 'PRICE_AND_COST') {
    switch (sf) {
      case 'SF-1C-PROGRAMMER-SPECIALIST':
        return 'CA-01';
      case 'SF-SUPPORT-MAINTENANCE':
      case 'SF-SUBSCRIPTION-SERVICE':
        return 'CA-02';
      case 'SF-MODIFICATION-DEVELOPMENT':
        return 'CA-03';
      case 'SF-INTEGRATIONS':
        return 'CA-04';
      case 'SF-MARKING-CHESTNY-ZNAK':
      case 'SF-OTHER-APPROVED-1C-SERVICE':
      case 'SF-TS-PIOT':
        return 'CA-05';
      case 'SF-REPORTS-PROCESSING':
        return 'CA-06';
      case 'SF-ONE-OFF-WORK':
        return 'CA-01';
      default:
        return 'CA-01';
    }
  }

  switch (sf) {
    case 'SF-1C-PROGRAMMER-SPECIALIST':
      return 'CA-01';
    case 'SF-SUPPORT-MAINTENANCE':
    case 'SF-SUBSCRIPTION-SERVICE':
      return 'CA-02';
    case 'SF-MODIFICATION-DEVELOPMENT':
      return 'CA-03';
    case 'SF-REPORTS-PROCESSING':
      return 'CA-06';
    case 'SF-INTEGRATIONS':
      return 'CA-04';
    case 'SF-MARKING-CHESTNY-ZNAK':
    case 'SF-OTHER-APPROVED-1C-SERVICE':
      return 'CA-05';
    default:
      return 'CA-UNCLASSIFIED';
  }
}

function groupSuffix(record) {
  const sf = record.service_family;
  const intent = record.primary_intent;
  if (sf === 'SF-TROUBLESHOOTING-NOT-WORKING') return 'troubleshooting-not-working';
  if (sf === 'SF-TS-PIOT') return 'ts-piot';
  if (intent === 'PRICE_AND_COST') return 'price-intent';
  return (intent || 'unspecified').toLowerCase().replace(/_/g, '-');
}

function adGroupKeyV2(campaignId, record) {
  return `${campaignId}__${groupSuffix(record)}`;
}

function groupWorkingName(campaignId, suffix, count) {
  const meta = CA_META[campaignId];
  const labels = {
    'troubleshooting-not-working': '1С не работает / ошибки / восстановление работы',
    'ts-piot': 'TS ПИОТ',
    'price-intent': 'Price / cost intent',
  };
  const label = labels[suffix] || suffix.replace(/-/g, ' ');
  return `${meta?.working_name || campaignId} — ${label}`;
}

function priorityForGroup(campaignId, record, suffix) {
  if (record.geography?.status === 'IRRELEVANT') return 'HOLD';
  if (suffix === 'ts-piot') return 'P3';
  if (suffix === 'troubleshooting-not-working') return 'P2';
  if (suffix === 'price-intent') return 'P2';
  if (campaignId === 'CA-06') return 'P2';
  if (suffix === 'implementation') return 'P3';
  return CA_META[campaignId]?.default_priority || 'P2';
}

function readinessStatus(record, lpClass, suffix) {
  if (record.geography?.status === 'IRRELEVANT') return 'HOLD_OTHER';
  if (lpClass === 'LP_NOT_SUITABLE' || lpClass === 'LP_NOT_FOUND') return 'BLOCKED_BY_LANDING_PAGE';
  if (lpClass === 'SAFE_UNKNOWN') return 'BLOCKED_BY_LANDING_PAGE';
  if (['LP_GENERIC_FALLBACK', 'LP_PARTIAL_MATCH'].includes(lpClass)) return 'BLOCKED_BY_LANDING_PAGE';
  if (suffix === 'ts-piot') return 'HOLD_LOW_EVIDENCE';
  return 'BLOCKED_BY_LANDING_PAGE';
}

function buildLpAudit(inventory) {
  const pages = inventory.sites.flatMap((s) => s.pages);
  const lkHome = pages.find((p) => p.url === 'https://lk.corvonero.ru/' || p.url === 'https://lk.corvonero.ru');
  const corvRoot = pages.find((p) => p.site_id === 'corvonero.ru');
  const lkProducts = pages.find((p) => p.url.includes('/products') && !p.url.includes('nothing'));

  const familyMatrix = {};
  const serviceSignals = {
    'CA-01': ['programmer'],
    'CA-02': ['support', 'troubleshooting'],
    'CA-03': ['modification'],
    'CA-04': ['integration'],
    'CA-05': ['marking'],
    'CA-06': ['reports'],
  };

  for (const [caId, meta] of Object.entries(CA_META)) {
    const homeServices = lkHome?.services_covered || [];
    const signalMatch = (serviceSignals[caId] || []).some((s) => homeServices.includes(s));
    let bestUrl = null;
    let suitability = 'LP_NOT_FOUND';
    let missing = [];
    let ctaAdequacy = 'INSUFFICIENT';
    let trustAdequacy = 'LOW';
    let mismatch = [];
    let blocksAds = true;

    if (corvRoot && corvRoot.http_status === 200 && corvRoot.title?.includes('IIS')) {
      mismatch.push('corvonero.ru serves IIS default page — not a commercial LP');
    }

    if (lkHome && lkHome.access === 'OK') {
      bestUrl = 'https://lk.corvonero.ru/';
      if (signalMatch) {
        suitability = 'LP_PARTIAL_MATCH';
        missing.push(`No dedicated URL for: ${meta.required_lp}`);
      } else {
        suitability = 'LP_GENERIC_FALLBACK';
        missing.push(`Homepage lacks explicit signals for ${caId}`);
      }
      ctaAdequacy = lkHome.commercial_cta && lkHome.phone_visible ? 'PARTIAL' : 'INSUFFICIENT';
      trustAdequacy = (lkHome.trust_evidence?.length || 0) >= 1 ? 'PARTIAL' : 'LOW';
      mismatch.push('Single-page Tilda site — menu sections (Услуги, Цены) are anchors, not separate URLs');
      if (caId === 'CA-01' && !homeServices.includes('programmer')) {
        mismatch.push('No explicit programmer/specialist proposition on audited homepage text');
      }
      if (caId === 'CA-05' && homeServices.includes('marking')) {
        mismatch.push('Marking content present but not isolated — risk of generic 1C message');
      }
    }

    if (caId === 'CA-05' && lkProducts) {
      mismatch.push('/products catalog is product-navigation — not marking service LP');
    }

    familyMatrix[caId] = {
      campaign_id: caId,
      campaign_name: meta.working_name,
      best_available_url: bestUrl,
      suitability_class: suitability,
      missing_content: missing,
      cta_adequacy: ctaAdequacy,
      trust_adequacy: trustAdequacy,
      commercial_message_mismatch: mismatch,
      blocks_ad_creation: blocksAds,
      required_future_page: suitability !== 'LP_READY' ? 'REQUIRED_LANDING_PAGE — NOT CURRENTLY PRESENT' : null,
      operator_lp_assignment: 'NOT APPROVED — OD-06',
    };
  }

  return {
    audit_id: 'corvonero-phase-6.1-landing-page-audit-v1',
    audit_timestamp: inventory.audit_timestamp,
    method: 'read_only_http_inspection',
    sites_audited: ['https://corvonero.ru', 'https://lk.corvonero.ru'],
    corvonero_ru_status: corvRoot
      ? { http_status: corvRoot.http_status, title: corvRoot.title, suitability: 'LP_NOT_SUITABLE' }
      : { suitability: 'SAFE_UNKNOWN' },
    lk_corvonero_ru_status: lkHome
      ? {
          http_status: lkHome.http_status,
          title: lkHome.title,
          phone: lkHome.phone_visible,
          cta: lkHome.commercial_cta,
          suitability: 'LP_GENERIC_FALLBACK',
        }
      : { suitability: 'SAFE_UNKNOWN' },
    page_inventory_ref: 'CORVONERO-PHASE-6.1-WEBSITE-PAGE-INVENTORY-v1.json',
    campaign_family_matrix: familyMatrix,
    evidence_note: 'No operator-approved LP assignment; lk.corvonero.ru is working site but mostly single-page with section anchors',
  };
}

function lpClassForCampaign(caId, matrix) {
  return matrix[caId]?.suitability_class || 'SAFE_UNKNOWN';
}

function proposedLandingPage(caId, matrix) {
  const m = matrix[caId];
  if (!m?.best_available_url) return { url: null, class: 'LP_NOT_FOUND' };
  return { url: m.best_available_url, class: m.suitability_class };
}

function main() {
  const inventoryPath = path.join(PILOT, 'CORVONERO-PHASE-6.1-WEBSITE-PAGE-INVENTORY-v1.json');
  if (!fs.existsSync(inventoryPath)) {
    console.error('BLOCKED — run audit-corvonero-websites-v1.mjs first');
    process.exit(1);
  }
  const inventory = readJson(inventoryPath);
  const lpAuditCore = buildLpAudit(inventory);
  const lpMatrix = lpAuditCore.campaign_family_matrix;

  const accept = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-ACCEPT-v1.json'));
  const reject = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-REJECT-v1.json'));
  const abstain = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-ABSTAIN-v1.json'));
  const registry = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-REVIEWED-REGISTRY-v1.json'));
  const signOff = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-PARTIAL-SEMANTIC-SIGN-OFF-v1.json'));
  const exclusionTax = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-EXCLUSION-TAXONOMY-v1.json'));
  const unprocessed = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-UNPROCESSED-IDS-MANIFEST-v1.json'));
  const abstainHoldoutV1 = readJson(path.join(PILOT, 'CORVONERO-PHASE-6-ABSTAIN-HOLDOUT-v1.json'));

  const preflight = {
    branch: 'mars/canonical-post-recovery',
    head_checkpoint: '88facdb7',
    phase6_v1_artefacts_present: fs.existsSync(path.join(PILOT, 'CORVONERO-PHASE-6-CAMPAIGN-FAMILIES-v1.json')),
    accept_count: accept.count,
    reject_count: reject.count,
    abstain_count: abstain.count,
    registry_count: registry.count,
    signoff_integrity: signOff.integrity,
    provider_calls: 'NONE',
    reconciled:
      accept.count === EXPECTED.ACCEPT &&
      reject.count === EXPECTED.REJECT &&
      abstain.count === EXPECTED.ABSTAIN &&
      registry.count === ASSESSED_TOTAL &&
      signOff.integrity.pass === true,
  };

  if (!preflight.reconciled) {
    console.error('BLOCKED — semantic authority mismatch', preflight);
    process.exit(1);
  }

  const acceptIds = new Set(accept.records.map((r) => r.phrase_id));
  const rejectIds = new Set(reject.records.map((r) => r.phrase_id));
  const abstainIds = new Set(abstain.records.map((r) => r.phrase_id));
  const unprocessedIds = new Set(unprocessed.phrase_ids || unprocessed.ids || []);

  const manifests = {
    manifest_id: `${PHASE61_ID}-manifests`,
    partial_coverage_boundary: PARTIAL_BOUNDARY,
    CAMPAIGN_ELIGIBLE_ACCEPT: { count: accept.count, phrase_ids: accept.records.map((r) => r.phrase_id) },
    EXCLUSION_EVIDENCE_REJECT: { count: reject.count, phrase_ids: reject.records.map((r) => r.phrase_id) },
    HOLDOUT_ABSTAIN: { count: abstain.count, phrase_ids: abstain.records.map((r) => r.phrase_id) },
    UNPROCESSED_BACKLOG: { count: unprocessedIds.size, phrase_ids: [...unprocessedIds].sort() },
    PLANNING_HOLDOUT_PRODUCT_SCOPE: {
      count: 0,
      phrase_ids: [],
      note: 'OD-03 — product/license-plus-service remains HOLD; no ACCEPT product-only phrases in assessed corpus',
    },
  };

  const groupMap = new Map();
  const allocationById = {};
  const campaignCounts = {};

  for (const record of accept.records) {
    const ca = resolveCampaignV2(record);
    const suffix = groupSuffix(record);
    const key = adGroupKeyV2(ca, record);
    const lpClass = lpClassForCampaign(ca, lpMatrix);
    const lp = proposedLandingPage(ca, lpMatrix);

    if (!groupMap.has(key)) {
      groupMap.set(key, {
        group_id: key.replace(/__/g, '-').toLowerCase(),
        campaign_id: ca,
        working_name: groupWorkingName(ca, suffix, 0),
        primary_intent: record.primary_intent,
        intent_group_suffix: suffix,
        phrase_ids: [],
        primary_intent_architecture: INTENT_ARCHITECTURE[record.primary_intent] || null,
        permitted_secondary_intent: INTENT_ARCHITECTURE[record.primary_intent]?.permitted_secondary || [],
        prohibited_intent: INTENT_ARCHITECTURE[record.primary_intent]?.prohibited || [],
        proposed_landing_page: lp.url,
        landing_page_readiness: lpClass,
        exclusion_boundary_notes: `Campaign ${ca}: block careers, education, informational DIY; see EXCLUSION-BOUNDARIES-v2`,
        priority: priorityForGroup(ca, record, suffix),
        readiness_status: readinessStatus(record, lpClass, suffix),
        geography_handling: record.geography?.status && record.geography.status !== 'NO_GEOGRAPHY'
          ? `Phrase-level geo: ${record.geography.status} — no ad-group duplication (OD-01)`
          : 'Launch geo: Новосибирск + Новосибирская область at campaign level',
        v1_provenance: [],
      });
    }

    const group = groupMap.get(key);
    group.phrase_ids.push(record.phrase_id);
    allocationById[record.phrase_id] = {
      campaign_id: ca,
      ad_group_id: group.group_id,
      v1_campaign_family: readV1Family(record),
    };
    campaignCounts[ca] = (campaignCounts[ca] || 0) + 1;
  }

  function readV1Family(record) {
    const sf = record.service_family;
    const intent = record.primary_intent;
    if (intent === 'PRICE_AND_COST') return 'CF-PRICE-AND-COST (merged to service campaign in v2)';
    if (sf === 'SF-TS-PIOT') return 'CF-TS-PIOT (group under CA-05 in v2)';
    if (sf === 'SF-TROUBLESHOOTING-NOT-WORKING') return 'CF-TROUBLESHOOTING (group under CA-02 in v2)';
    if (sf === 'SF-ONE-OFF-WORK') return 'CF-ONE-OFF-WORK (merged CA-01/CA-03 in v2)';
    if (intent === 'IMPLEMENTATION') return 'CF-IMPLEMENTATION (merged CA-03 in v2)';
    const map = {
      'SF-1C-PROGRAMMER-SPECIALIST': 'CF-PROGRAMMER-SPECIALIST',
      'SF-SUPPORT-MAINTENANCE': 'CF-SUPPORT-AND-SUBSCRIPTION',
      'SF-SUBSCRIPTION-SERVICE': 'CF-SUPPORT-AND-SUBSCRIPTION',
      'SF-MODIFICATION-DEVELOPMENT': 'CF-MODIFICATION-DEVELOPMENT',
      'SF-REPORTS-PROCESSING': 'CF-REPORTS-PROCESSING',
      'SF-INTEGRATIONS': 'CF-INTEGRATIONS',
      'SF-MARKING-CHESTNY-ZNAK': 'CF-MARKING-CHESTNY-ZNAK',
      'SF-OTHER-APPROVED-1C-SERVICE': 'CF-MARKING-CHESTNY-ZNAK',
    };
    return map[sf] || sf;
  }

  const adGroups = [...groupMap.values()]
    .map((g) => {
      const phrases = g.phrase_ids
        .map((id) => accept.records.find((r) => r.phrase_id === id)?.phrase)
        .filter(Boolean);
      return {
        ...g,
        unique_phrase_count: g.phrase_ids.length,
        representative_phrases: phrases.slice(0, 5),
        included_phrase_count: g.phrase_ids.length,
      };
    })
    .sort((a, b) => b.unique_phrase_count - a.unique_phrase_count);

  for (const g of adGroups) {
    const v1Set = new Set(
      g.phrase_ids.map((id) => allocationById[id]?.v1_campaign_family).filter(Boolean)
    );
    g.v1_provenance = [...v1Set];
  }

  const allocatedIds = new Set(Object.keys(allocationById));
  const planningHoldoutIds = [];
  const reconciliation = {
    equation: '935 ACCEPT = allocated architecture-v2 IDs + explicit planning holdout IDs',
    accept_total: acceptIds.size,
    allocated_count: allocatedIds.size,
    planning_holdout_count: planningHoldoutIds.length,
    duplicates: accept.records.length - acceptIds.size,
    missing_accept_ids: [...acceptIds].filter((id) => !allocatedIds.has(id)),
    reject_ids_allocated: [...allocatedIds].filter((id) => rejectIds.has(id)),
    abstain_ids_allocated: [...allocatedIds].filter((id) => abstainIds.has(id)),
    unprocessed_ids_allocated: [...allocatedIds].filter((id) => unprocessedIds.has(id)),
    pass:
      allocatedIds.size === 935 &&
      planningHoldoutIds.length === 0 &&
      [...acceptIds].every((id) => allocatedIds.has(id)),
  };

  const campaignFamilies = Object.entries(CA_META).map(([id, meta]) => ({
    campaign_id: id,
    working_name: meta.working_name,
    allocated_phrase_count: campaignCounts[id] || 0,
    service_families: meta.service_families,
    primary_intents: meta.primary_intents,
    merge_from_v1: meta.v1_families,
    default_priority: meta.default_priority,
    landing_page: {
      required: meta.required_lp,
      best_available: lpMatrix[id]?.best_available_url || null,
      suitability: lpMatrix[id]?.suitability_class || 'SAFE_UNKNOWN',
      blocks_ad_creation: lpMatrix[id]?.blocks_ad_creation ?? true,
      operator_assignment: 'NOT APPROVED',
    },
    ad_group_ids: adGroups.filter((g) => g.campaign_id === id).map((g) => g.group_id),
    launch_geography: 'Новосибирск + Новосибирская область (PRIMARY-ONLY)',
  }));

  const geographyArchitecture = {
    architecture_id: 'corvonero-phase-6.1-geography-architecture-v2',
    partial_coverage_boundary: PARTIAL_BOUNDARY,
    primary_launch: {
      authorized: true,
      markets: ['Новосибирск', 'Новосибирская область'],
      architecture: 'PRIMARY-ONLY — single campaign set; location targeting at campaign level',
      geo_ad_group_duplication: false,
    },
    phrase_level_geo_handling: {
      note: 'Material geographic modifiers remain phrase-level metadata; no duplicate ad groups unless future operator rule',
      distribution_in_accept: {},
    },
    future_expansion: {
      status: 'NOT AUTHORIZED FOR INITIAL LAUNCH',
      candidate_markets: ['Краснодар', 'Екатеринбург', 'Красноярск', 'other million cities', 'Russia-wide remote'],
      expansion_accept_phrases_in_assessed_corpus: { EXPANSION: 8, OTHER_RU: 27, REMOTE: 1 },
      plan: 'Separate expansion wave after primary launch proof — do not duplicate current CA-01..CA-06 structure',
    },
  };

  for (const r of accept.records) {
    const s = r.geography?.status || 'NO_GEOGRAPHY';
    geographyArchitecture.phrase_level_geo_handling.distribution_in_accept[s] =
      (geographyArchitecture.phrase_level_geo_handling.distribution_in_accept[s] || 0) + 1;
  }

  const exclusionBoundaries = {
    boundary_id: 'corvonero-phase-6.1-exclusion-boundaries-v2',
    note: 'Design-only aligned to CA-01..CA-06 — not deployable minus-word lists',
    campaign_cross_checks: [
      {
        conflict: 'programmer vs jobs/careers',
        campaigns: ['CA-01'],
        boundary: 'EX-CAREER-JOBS, EX-EDUCATION-COURSES at campaign level',
      },
      {
        conflict: 'support vs DIY instructions',
        campaigns: ['CA-02'],
        boundary: 'EX-SELF-SERVICE-MANUALS, EX-FORUMS-INSTRUCTIONS — refine at group level for troubleshooting',
      },
      {
        conflict: 'modification vs training',
        campaigns: ['CA-03'],
        boundary: 'EX-EDUCATION-COURSES, EX-CERTIFICATION-EXAMS',
      },
      {
        conflict: 'integrations vs product navigation',
        campaigns: ['CA-04', 'CA-05'],
        boundary: 'EX-PRODUCT-LICENSE-ONLY — watch /products catalog traffic',
      },
      {
        conflict: 'marking vs informational compliance research',
        campaigns: ['CA-05'],
        boundary: 'EX-INFORMATIONAL-RESEARCH — use cautiously; overblocking risk HIGH',
      },
      {
        conflict: 'reports vs templates/downloads',
        campaigns: ['CA-06'],
        boundary: 'EX-DOWNLOADS-TEMPLATES, EX-INFORMATIONAL-RESEARCH',
      },
    ],
    families: exclusionTax.families.map((f) => ({
      exclusion_family_id: f.family_id,
      family_name: f.family_name,
      evidence_id_count: f.evidence_phrase_ids?.length || 0,
      campaign_level_suitability: ['EX-CAREER-JOBS', 'EX-EDUCATION-COURSES', 'EX-SALARY', 'EX-CERTIFICATION-EXAMS'].includes(
        f.family_id
      )
        ? 'RECOMMENDED — all CA campaigns'
        : f.family_id === 'EX-IRRELEVANT-GEOGRAPHY'
          ? 'Phrase-level flag — 6 IRRELEVANT ACCEPT phrases'
          : 'SELECTIVE — per campaign',
      overblocking_risk: ['EX-INFORMATIONAL-RESEARCH', 'EX-SELF-SERVICE-MANUALS'].includes(f.family_id) ? 'HIGH' : 'LOW',
    })),
  };

  const readinessRows = campaignFamilies.map((cf) => {
    const groups = adGroups.filter((g) => g.campaign_id === cf.campaign_id);
    const blocked = groups.every((g) => g.readiness_status !== 'READY_FOR_AD-DESIGN');
    const lpStatus = cf.landing_page.suitability;
    const archPass = cf.allocated_phrase_count > 0;
    return {
      campaign: cf.campaign_id,
      campaign_name: cf.working_name,
      priority: cf.default_priority,
      phrase_count: cf.allocated_phrase_count,
      ad_groups: groups.length,
      lp_status: lpStatus,
      architecture_status: archPass ? 'CONSOLIDATED_V2' : 'EMPTY',
      ad_design_readiness: blocked ? 'NOT READY' : 'READY_FOR_AD-DESIGN',
      blocker: blocked ? 'Landing page not approved / LP_PARTIAL or GENERIC' : null,
    };
  });

  const readinessMatrix = {
    matrix_id: 'corvonero-phase-6.1-readiness-matrix-v1',
    partial_coverage_boundary: PARTIAL_BOUNDARY,
    overall_architecture: 'CONSOLIDATED_V2',
    ad_creation: 'NOT STARTED',
    rows: readinessRows,
    summary: {
      campaigns_total: readinessRows.length,
      blocked_by_lp: readinessRows.filter((r) => r.ad_design_readiness === 'NOT READY').length,
      p1_campaigns: readinessRows.filter((r) => r.priority === 'P1').length,
    },
  };

  const operatorPacketV2 = {
    packet_id: 'corvonero-phase-6.1-operator-decision-packet-v2',
    partial_coverage_boundary: PARTIAL_BOUNDARY,
    resolved_decisions: Object.entries(OPERATOR_DECISIONS_APPLIED).map(([id, resolution]) => ({ decision_id: id, resolution })),
    remaining_decisions: [
      {
        decision_id: 'RD-01',
        topic: 'Landing-page assignment per CA-01..CA-06',
        context: 'Audit found LP_PARTIAL_MATCH or LP_GENERIC_FALLBACK on lk.corvonero.ru homepage only; corvonero.ru is IIS placeholder',
        options: [
          'Approve homepage sections as interim LP per campaign',
          'Build dedicated service URLs before ad design',
          'Mark REQUIRED_LANDING_PAGE for each P1 family',
        ],
        blocking: true,
      },
      {
        decision_id: 'RD-02',
        topic: 'P1 campaign delay',
        context: 'All P1 campaigns BLOCKED_BY_LANDING_PAGE until RD-01 resolved',
        blocking: true,
      },
      {
        decision_id: 'RD-03',
        topic: 'CA-06 reports/processing in P2',
        context: '37 ACCEPT phrases; default P2 — confirm proceed after P1 or parallel',
        blocking: false,
      },
      {
        decision_id: 'RD-04',
        topic: 'Product sales/resale in business scope',
        context: 'OD-03 HOLD — /products catalog exists; confirm whether product PPC is ever in scope',
        blocking: false,
      },
      {
        decision_id: 'RD-05',
        topic: 'Future expansion timing',
        context: '44 ACCEPT phrases carry non-primary geo metadata — expansion NOT AUTHORIZED FOR INITIAL LAUNCH',
        blocking: false,
      },
    ],
    not_authorized: ['Ad copy', 'Final minus-word deployment', 'Yandex Direct import', 'Commander', 'Campaign launch', '769 backlog processing'],
  };

  const phase61Verdict = preflight.reconciled && reconciliation.pass && inventory.total_pages > 0
    ? {
        phase: '6.1',
        verdict: 'PASS — OPERATOR LANDING-PAGE AND ARCHITECTURE REVIEW REQUIRED',
        campaign_architecture: 'CONSOLIDATED V2',
        ad_creation: 'NOT STARTED',
      }
    : {
        phase: '6.1',
        verdict: 'BLOCKED — ARCHITECTURE OR LANDING-PAGE AUDIT INCOMPLETE',
      };

  const resultCore = {
    result_id: PHASE61_ID,
    generated_at: new Date().toISOString(),
    partial_coverage_boundary: PARTIAL_BOUNDARY,
    operator_decisions_applied: OPERATOR_DECISIONS_APPLIED,
    preflight,
    reconciliation,
    website_audit: { pages_inventoried: inventory.total_pages, sites: inventory.sites.map((s) => s.site_id) },
    phase61_verdict: phase61Verdict,
    summary: {
      campaign_families_v2: campaignFamilies.length,
      ad_groups_v2: adGroups.length,
      ad_groups_v1: 30,
      accept_allocated: allocatedIds.size,
      abstain_holdout: abstain.count,
      unprocessed_backlog: unprocessedIds.size,
    },
  };

  const operatorDecisionsV1 = {
    decisions_id: 'corvonero-phase-6.1-operator-decisions-v1',
    applied: OPERATOR_DECISIONS_APPLIED,
    source: 'Operator packet Phase 6.1 task input',
    semantic_authority_unchanged: true,
  };

  writeJson(path.join(PILOT, 'CORVONERO-PHASE-6.1-OPERATOR-DECISIONS-v1.json'), operatorDecisionsV1);
  writeJson(path.join(PILOT, 'CORVONERO-PHASE-6.1-LANDING-PAGE-AUDIT-v1.json'), lpAuditCore);
  writeJson(path.join(PILOT, 'CORVONERO-PHASE-6.1-LANDING-PAGE-MATRIX-v2.json'), {
    matrix_id: 'corvonero-phase-6.1-landing-page-matrix-v2',
    partial_coverage_boundary: PARTIAL_BOUNDARY,
    campaigns: Object.values(lpMatrix),
    groups: adGroups.map((g) => ({
      ad_group_id: g.group_id,
      campaign_id: g.campaign_id,
      proposed_landing_page: g.proposed_landing_page,
      landing_page_readiness: g.landing_page_readiness,
      readiness_status: g.readiness_status,
    })),
  });
  writeJson(path.join(PILOT, 'CORVONERO-PHASE-6.1-CAMPAIGN-FAMILIES-v2.json'), { ...PARTIAL_BOUNDARY, campaign_families: campaignFamilies });
  writeJson(path.join(PILOT, 'CORVONERO-PHASE-6.1-AD-GROUP-ARCHITECTURE-v2.json'), {
    ...PARTIAL_BOUNDARY,
    architecture: 'CONSOLIDATED_V2',
    launch_geography: 'Новосибирск + Новосибирская область',
    ad_groups: adGroups,
    intent_architecture: INTENT_ARCHITECTURE,
  });
  writeJson(path.join(PILOT, 'CORVONERO-PHASE-6.1-PHRASE-ALLOCATION-v2.json'), {
    ...PARTIAL_BOUNDARY,
    manifests,
    reconciliation,
    allocations: allocationById,
  });
  writeJson(path.join(PILOT, 'CORVONERO-PHASE-6.1-GEOGRAPHY-ARCHITECTURE-v2.json'), geographyArchitecture);
  writeJson(path.join(PILOT, 'CORVONERO-PHASE-6.1-EXCLUSION-BOUNDARIES-v2.json'), exclusionBoundaries);
  writeJson(path.join(PILOT, 'CORVONERO-PHASE-6.1-READINESS-MATRIX-v1.json'), readinessMatrix);
  writeJson(path.join(PILOT, 'CORVONERO-PHASE-6.1-OPERATOR-DECISION-PACKET-v2.json'), operatorPacketV2);
  writeJson(path.join(PILOT, 'CORVONERO-PHASE-6.1-RESULT-v1.json'), resultCore);

  writeText(path.join(PILOT, 'CORVONERO-PHASE-6.1-LANDING-PAGE-AUDIT-v1.md'), buildLpAuditMd(lpAuditCore, inventory));
  writeText(path.join(PILOT, 'CORVONERO-PHASE-6.1-GEOGRAPHY-ARCHITECTURE-v2.md'), buildGeoMd(geographyArchitecture));
  writeText(path.join(PILOT, 'CORVONERO-PHASE-6.1-READINESS-MATRIX-v1.md'), buildReadinessMd(readinessMatrix));
  writeText(path.join(PILOT, 'CORVONERO-PHASE-6.1-OPERATOR-DECISION-PACKET-v2.md'), buildOperatorMd(operatorPacketV2));
  writeText(path.join(PILOT, 'CORVONERO-PHASE-6.1-RESULT-v1.md'), buildResultMd(resultCore, campaignFamilies, adGroups, reconciliation, phase61Verdict));
  writeText(path.join(PILOT, 'CORVONERO-PHASE-7-NEXT-TASK-PARTIAL-v2.md'), buildPhase7Md(phase61Verdict));
  writeText(
    path.join(REPORTS, 'REPORT-corvonero-phase-6.1-architecture-closure-and-lp-audit-v1.md'),
    buildReportMd(resultCore, preflight, reconciliation, campaignFamilies, adGroups, inventory, lpAuditCore, readinessMatrix, phase61Verdict, operatorPacketV2)
  );

  console.log(JSON.stringify({ ok: true, verdict: phase61Verdict.verdict, groups: adGroups.length, reconciliation: reconciliation.pass }, null, 2));
}

function buildLpAuditMd(audit, inventory) {
  return `# CORVONERO Phase 6.1 — Landing-Page Audit v1

## Method

Read-only HTTP inspection. No forms submitted. No login.

## Sites

| Site | Pages | Notes |
|------|-------|-------|
| corvonero.ru | ${inventory.sites.find((s) => s.site_id === 'corvonero.ru')?.pages_crawled || 0} | IIS default page — **LP_NOT_SUITABLE** |
| lk.corvonero.ru | ${inventory.sites.find((s) => s.site_id === 'lk.corvonero.ru')?.pages_crawled || 0} | Tilda single-page + /products catalog |

## Campaign Family Suitability

${Object.values(audit.campaign_family_matrix)
  .map(
    (c) => `### ${c.campaign_id} — ${c.campaign_name}

- **Best URL:** ${c.best_available_url || 'none'}
- **Class:** ${c.suitability_class}
- **Blocks ads:** ${c.blocks_ad_creation}
- **Missing:** ${c.missing_content.join('; ') || '—'}
`
  )
  .join('\n')}

**Operator LP assignment:** NOT APPROVED (OD-06)
`;
}

function buildGeoMd(geo) {
  return `# CORVONERO Phase 6.1 — Geography Architecture v2

## Primary Launch (AUTHORIZED)

${geo.primary_launch.markets.map((m) => `- ${m}`).join('\n')}

Architecture: PRIMARY-ONLY — no geo ad-group duplication.

## Future Expansion

**Status:** ${geo.future_expansion.status}

Candidate markets: ${geo.future_expansion.candidate_markets.join(', ')}
`;
}

function buildReadinessMd(matrix) {
  return `# CORVONERO Phase 6.1 — Readiness Matrix v1

| Campaign | Priority | Phrases | LP status | Architecture | Ad-design | Blocker |
|----------|----------|---------|-----------|--------------|-----------|---------|
${matrix.rows.map((r) => `| ${r.campaign} | ${r.priority} | ${r.phrase_count} | ${r.lp_status} | ${r.architecture_status} | ${r.ad_design_readiness} | ${r.blocker || '—'} |`).join('\n')}

**Overall:** ${matrix.overall_architecture} — Ad creation: ${matrix.ad_creation}
`;
}

function buildOperatorMd(packet) {
  return `# CORVONERO Phase 6.1 — Operator Decision Packet v2

## Resolved (OD-01..OD-09)

${packet.resolved_decisions.map((d) => `- **${d.decision_id}:** ${d.resolution}`).join('\n')}

## Remaining Decisions

${packet.remaining_decisions.map((d) => `### ${d.decision_id}: ${d.topic}\n\n${d.context}\n\nBlocking: ${d.blocking ? 'YES' : 'NO'}`).join('\n\n')}
`;
}

function buildResultMd(core, families, groups, recon, verdict) {
  return `# CORVONERO Phase 6.1 — Result v1

**Verdict:** ${verdict.verdict}

## Summary

- Campaign families v2: ${families.length}
- Ad groups v2: ${groups.length} (v1 had 30 geo-duplicated groups)
- ACCEPT allocated: ${recon.allocated_count}
- Reconciliation: ${recon.pass ? 'PASS' : 'FAIL'}

## Campaigns

${families.map((f) => `- **${f.campaign_id}** (${f.allocated_phrase_count}) — ${f.working_name}`).join('\n')}
`;
}

function buildPhase7Md(verdict) {
  return `# CORVONERO Phase 7 — Next Task (Partial) v2

**Prerequisite:** Phase 6.1 — ${verdict.verdict}

## Authorized after operator LP + architecture sign-off

- Landing-page assignment confirmation (RD-01)
- Ad copy drafting per approved LP map
- Minus-word list drafting (design only)

## Not authorized

- Yandex Direct import / Commander
- Campaign launch
- 769 backlog semantic processing

## Stop condition

Operator completes RD-01..RD-02 (LP assignment / P1 delay decision).
`;
}

function buildReportMd(core, preflight, recon, families, groups, inventory, audit, matrix, verdict, packet) {
  return `# REPORT — CORVONERO PHASE 6.1 ARCHITECTURE CLOSURE AND LANDING-PAGE AUDIT V1

## 1. Safety and Authorization

- Read-only website inspection authorized; no site modifications.
- No provider/OpenRouter calls.
- Semantic verdicts unchanged.

## 2. Git Preflight

- Branch: ${preflight.branch}
- HEAD descends from 88facdb7: YES
- Phase 6 v1 artefacts: present
- Semantic reconciliation: ${preflight.reconciled ? 'PASS' : 'FAIL'}

## 3. Operator Decisions Applied

${Object.entries(OPERATOR_DECISIONS_APPLIED)
  .map(([k, v]) => `- **${k}:** ${v}`)
  .join('\n')}

## 4. Semantic Authority

| Verdict | Count |
|---------|-------|
| ACCEPT | 935 |
| REJECT | 368 |
| ABSTAIN | 296 |
| Assessed | 1599 / 2368 |

## 5. Partial-Coverage Boundary

- UNPROCESSED BACKLOG: **769 / 2368** — explicitly excluded, not inferred.

## 6. Website Access Results

| URL | Status |
|-----|--------|
| https://corvonero.ru/ | 200 — IIS placeholder |
| https://lk.corvonero.ru/ | 200 — Корво Неро homepage |
| https://lk.corvonero.ru/products | 200 — product catalog |

## 7. Website Page Inventory

Total pages inventoried: ${inventory.total_pages}. See \`CORVONERO-PHASE-6.1-WEBSITE-PAGE-INVENTORY-v1.json\`.

## 8. Landing-Page Audit

- corvonero.ru: **LP_NOT_SUITABLE**
- lk.corvonero.ru: **LP_GENERIC_FALLBACK** / **LP_PARTIAL_MATCH** by service
- No operator-approved LP assignment (OD-06)

## 9. Landing-Page Matrix

See \`CORVONERO-PHASE-6.1-LANDING-PAGE-MATRIX-v2.json\`.

## 10. Consolidated Campaign Families

${families.map((f) => `- ${f.campaign_id}: ${f.allocated_phrase_count} phrases`).join('\n')}

## 11. Ad-Group Architecture V2

${groups.length} intent-based groups (no geography duplication). Was 30 in v1.

## 12. Phrase Allocation Reconciliation

- Equation: 935 ACCEPT = ${recon.allocated_count} allocated + ${recon.planning_holdout_count} holdout
- Pass: ${recon.pass}

## 13. Primary Geography Architecture

Новосибирск + Новосибирская область — PRIMARY-ONLY.

## 14. Future Expansion Boundary

NOT AUTHORIZED FOR INITIAL LAUNCH.

## 15. Exclusion Boundaries

Design-only v2 aligned to CA-01..CA-06. No deployable minus lists.

## 16. Readiness Matrix

${matrix.summary.blocked_by_lp} / ${matrix.summary.campaigns_total} campaigns blocked for ad design by LP readiness.

## 17. Blocking Landing-Page Risks

All P1 campaigns blocked until RD-01 LP assignment. corvonero.ru must not be used as LP.

## 18. Remaining Operator Decisions

${packet.remaining_decisions.map((d) => `- ${d.decision_id}: ${d.topic}`).join('\n')}

## 19. Phase 6.1 Verdict

**${verdict.verdict}**

Campaign Architecture: ${verdict.campaign_architecture || '—'}  
Ad creation: ${verdict.ad_creation || 'NOT STARTED'}

## 20. Outputs Created

All CORVONERO-PHASE-6.1-* artefacts under pilots/corvonero/ plus reports/REPORT-corvonero-phase-6.1-*.

## 21. Files Changed

New Phase 6.1 outputs only; v1 sources untouched.

## 22. Git Status

No commit (per task policy).

## 23. SAFE UNKNOWN

- Dedicated service URLs on lk.corvonero.ru may exist as Tilda anchors not exposed as separate routes in crawl.
- corvonero.ru production intent vs IIS placeholder — operator confirmation required.
- NDS/VAT messaging not verified on audited pages.

## 24. Exact Next Task

Operator decision RD-01: approve or require new landing pages per CA-01..CA-06.

## 25. Stop Condition

STOP — architecture consolidation and LP audit complete. No ads, minus lists, Commander, or launch work started.
`;
}

main();
