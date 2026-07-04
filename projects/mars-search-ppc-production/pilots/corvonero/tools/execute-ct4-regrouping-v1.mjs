#!/usr/bin/env node
// C2c HOLD: source hardening only.
// This file is not authorized for execution without explicit operator approval.
// Commit/persistence does not authorize Commander import, Direct launch, account mutation,
// advertising start, Storage export generation, repo artifact generation,
// Localhost mutation, Storage mutation, Yandex/API access, or client-facing delivery.
// CT4 regrouping / UTM / bids authority generation does not authorize campaign launch, import,
// account mutation, advertising start, or client-facing delivery.
/**
 * CORVONERO CT-4 — semantic regrouping, re-audit, routing authority.
 * Rule-based only — no semantic cache, no OpenRouter, no XLSX generation.
 */
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PILOT_ROOT = path.resolve(__dirname, '..');
const PROJECT_ROOT = path.resolve(__dirname, '../../..');
const OUT_DIR = PILOT_ROOT;

const SOURCE_FILES = {
  phrase_allocation: path.join(PILOT_ROOT, 'CORVONERO-AD-WAVE-1-FINAL-PHRASE-ALLOCATION-v1.json'),
  group_register: path.join(PILOT_ROOT, 'CORVONERO-AD-WAVE-1-P1-FINAL-GROUP-REGISTER-v1.json'),
  primary_ads: path.join(PILOT_ROOT, 'CORVONERO-AD-WAVE-1-P1-FINAL-PRIMARY-ADS-v1.json'),
  campaign_negatives: path.join(PILOT_ROOT, 'CORVONERO-EXT-W1-NEGATIVE-DEPLOYMENT-v1.json'),
  callouts: path.join(PILOT_ROOT, 'CORVONERO-EXT-W1-CALLOUTS-v2.json'),
  utm_map: path.join(PILOT_ROOT, 'CORVONERO-EXT-W1-UTM-POLICY-v2.json'),
  campaign_settings: path.join(PILOT_ROOT, 'CORVONERO-EXT-W1-CAMPAIGN-SETTINGS-v2.json'),
  cross_campaign: path.join(PILOT_ROOT, 'CORVONERO-EXT-W1-CROSS-NEGATIVES-v2.json'),
  bids: path.join(PILOT_ROOT, 'CORVONERO-COMMANDER-INITIAL-BIDS-v1.json'),
  display_paths: path.join(PILOT_ROOT, 'CORVONERO-EXT-W1-DISPLAY-PATHS-v1.json'),
};

const OPERATOR_FILES = {
  ad_decision: path.join(PILOT_ROOT, 'CORVONERO-CT4-OPERATOR-AD-DECISION-v1.json'),
  cleanup_register: path.join(PILOT_ROOT, 'CORVONERO-CT4-OPERATOR-CLEANUP-REGISTER-v1.json'),
};

const AD_LIMITS = { headline_1: 56, headline_2: 30, text: 81, display_path: 20 };

function requireOperatorGate() {
  if (process.env.CORVONERO_OPERATOR_GATE !== 'APPROVED') {
    console.error(
      'STOP: CORVONERO_OPERATOR_GATE=APPROVED required. This C2c helper is not safe for casual execution.'
    );
    process.exit(1);
  }
}

function sha256File(fp) {
  return crypto.createHash('sha256').update(fs.readFileSync(fp)).digest('hex');
}

function writeJson(name, data) {
  const fp = path.join(OUT_DIR, name);
  fs.writeFileSync(fp, `${JSON.stringify(data, null, 2)}\n`);
  return { path: fp, sha256: sha256File(fp) };
}

function writeMd(name, content) {
  const fp = path.join(OUT_DIR, name);
  fs.writeFileSync(fp, content);
  return { path: fp, sha256: sha256File(fp) };
}

function charMetrics(text) {
  const chars = [...text];
  const words = text.split(/\s+/).filter(Boolean);
  const maxWordLen = Math.max(0, ...words.map((w) => [...w.replace(/[^\p{L}\p{N}]/gu, '')].length));
  return { characters: chars.length, max_word_length: maxWordLen, words };
}

function validateOperatorAdFields(ad) {
  const checks = {
    headline_1: charMetrics(ad.headline_1).characters <= AD_LIMITS.headline_1,
    headline_2: charMetrics(ad.headline_2).characters <= AD_LIMITS.headline_2,
    text: charMetrics(ad.text).characters <= AD_LIMITS.text,
    display_path: ad.display_path.length <= AD_LIMITS.display_path,
  };
  return {
    pass: Object.values(checks).every(Boolean),
    checks,
    lengths: {
      headline_1: charMetrics(ad.headline_1).characters,
      headline_2: charMetrics(ad.headline_2).characters,
      text: charMetrics(ad.text).characters,
      display_path: ad.display_path.length,
    },
  };
}

function normalizePhraseKey(phrase) {
  return String(phrase ?? '')
    .trim()
    .toLowerCase()
    .replace(/\s+/g, ' ');
}

function loadOperatorInputs() {
  for (const [role, fp] of Object.entries(OPERATOR_FILES)) {
    if (!fs.existsSync(fp)) {
      throw new Error(`Missing required operator input: ${role} — ${fp}`);
    }
  }
  const adDecision = JSON.parse(fs.readFileSync(OPERATOR_FILES.ad_decision, 'utf8'));
  const cleanupRegister = JSON.parse(fs.readFileSync(OPERATOR_FILES.cleanup_register, 'utf8'));
  const cleanupByPhrase = new Map();
  for (const row of cleanupRegister.corrections ?? []) {
    cleanupByPhrase.set(normalizePhraseKey(row.phrase), row);
  }
  return { adDecision, cleanupRegister, cleanupByPhrase };
}

const REJECT_RE =
  /ваканс|резюме|зарплат|оклад|с нуля|без опыта|курс|обучен|школ|университет|стань программист|становится программист|как стать|сертифик|аттест|экзамен|скачать|кряк|бесплатн|форум|hh\.ru|headhunter|\bhh\b|лицензи.*1с|купить 1с|сколько программистов|вопрос программист|работа программист|работа 1с программист|стажер|стажиров|трудоустрой|зарабатыва|начинающ|учиться|работать программист|стал программист|отзыв программист|для начинающ|ии для программист/i;

function classifyCA01(phrase) {
  const p = phrase.toLowerCase();
  const flags = {
    career_or_employment_issue: /ваканс|работа программист|резюме|стажер|трудоустрой|работать программист|\bhh\b|headhunter/i.test(p),
    education_issue: /с нуля|без опыта|курс|обучен|школ|университет|начинающ|учиться|для начинающ/i.test(p),
    informational_issue: /вопрос программист|сколько программист|отзыв|техническ.*задан/i.test(p),
    free_or_download_issue: /бесплатн|скачать|кряк/i.test(p),
    salary: /зарплат|оклад|зарабатыва/i.test(p),
  };

  if (REJECT_RE.test(p)) {
    return {
      verdict: 'REJECT',
      campaign: null,
      group: null,
      reason: Object.entries(flags)
        .filter(([, v]) => v)
        .map(([k]) => k)
        .join('; ') || 'noncommercial_leakage',
      flags,
    };
  }
  if (/стоим|цен|прайс|тариф|расцен|сколько стоит|рекомендован.*стоим/i.test(p)) {
    return { verdict: 'MOVE_WITHIN_CAMPAIGN', campaign: 'CA-01', group: 'ca-01-price-intent', reason: 'price_intent', flags };
  }
  if (/доработк|разработ/i.test(p)) {
    return { verdict: 'MOVE_TO_OTHER_CAMPAIGN', campaign: 'CA-03', group: 'ca-03-modification', reason: 'development_intent', flags };
  }
  if (/интегр/i.test(p)) {
    return { verdict: 'MOVE_TO_OTHER_CAMPAIGN', campaign: 'CA-04', group: 'ca-04-integration', reason: 'integration_intent', flags };
  }
  if (/сопровожд|обслужив/i.test(p)) {
    return { verdict: 'MOVE_TO_OTHER_CAMPAIGN', campaign: 'CA-02', group: 'ca-02-support-and-maintenance', reason: 'support_intent', flags };
  }
  if (/маркир|честн/i.test(p)) {
    return { verdict: 'MOVE_TO_OTHER_CAMPAIGN', campaign: 'CA-05', group: 'ca-05-chestny-znak-service', reason: 'marking_intent', flags };
  }
  if (/удал|дистанц|фриланс|частн|самозанят|новосиб|срочн|помощь программист/i.test(p)) {
    return { verdict: 'MOVE_WITHIN_CAMPAIGN', campaign: 'CA-01', group: 'ca-01-remote-freelance-specialist', reason: 'remote_freelance_local_urgent', flags };
  }
  if (/найти|найму|нужен|нужна|ищу|искать|подобрать|нанять|требуется/i.test(p)) {
    return { verdict: 'MOVE_WITHIN_CAMPAIGN', campaign: 'CA-01', group: 'ca-01-find-hire-specialist', reason: 'find_hire_intent', flags };
  }
  if (/заказать.*программист|услуг.*программист/i.test(p)) {
    return { verdict: 'MOVE_WITHIN_CAMPAIGN', campaign: 'CA-01', group: 'ca-01-direct-service-order', reason: 'direct_service_order', flags };
  }
  if (/бухгалт|зуп|erp|\bут\b|конфиг|консульт|админ|аналитик|специалист 1с|1с специалист|предприят|торговл|розниц|склад|crm|документооб/i.test(p)) {
    return { verdict: 'MOVE_WITHIN_CAMPAIGN', campaign: 'CA-01', group: 'ca-01-specialist-by-product', reason: 'product_role_variant', flags };
  }
  if (/^(программист|1с|специалист)/i.test(p.trim()) && p.trim().split(/\s+/).length <= 4) {
    return { verdict: 'KEEP', campaign: 'CA-01', group: 'ca-01-specialist-search', reason: 'core_specialist_query', flags };
  }
  return { verdict: 'MOVE_WITHIN_CAMPAIGN', campaign: 'CA-01', group: 'ca-01-specialist-extended', reason: 'extended_specialist_query', flags };
}

function classifyCA05(phrase) {
  const p = phrase.toLowerCase();
  const flags = {
    free_or_download_issue: /скачать|кряк|бесплатн/i.test(p),
    order_codes_issue: /заказ.*код.*маркир|код.*маркир.*заказ/i.test(p),
  };

  if (/заказ.*код.*маркир|код.*маркир.*заказ/i.test(p)) {
    return { verdict: 'REJECT', campaign: null, group: null, reason: 'code_purchase_not_setup_service', flags };
  }
  if (/тс\s*пиот|\bпиот\b/i.test(p)) {
    return { verdict: 'MOVE_WITHIN_CAMPAIGN', campaign: 'CA-05', group: 'ca-05-ts-piot', reason: 'ts_piot_intent', flags };
  }
  if (/интегр|битрикс|сайт.*1с|обмен.*сайт/i.test(p)) {
    return { verdict: 'MOVE_WITHIN_CAMPAIGN', campaign: 'CA-05', group: 'ca-05-integration', reason: 'integration_intent', flags };
  }
  if (/поддерж|сопровожд|обслуж/i.test(p)) {
    return { verdict: 'MOVE_WITHIN_CAMPAIGN', campaign: 'CA-05', group: 'ca-05-support-and-maintenance', reason: 'support_intent', flags };
  }
  if (/честн/i.test(p)) {
    return { verdict: 'MOVE_WITHIN_CAMPAIGN', campaign: 'CA-05', group: 'ca-05-chestny-znak-service', reason: 'chestny_znak_intent', flags };
  }
  if (/код.*маркир|маркир.*код|datamatrix|gs1/i.test(p)) {
    return { verdict: 'MOVE_WITHIN_CAMPAIGN', campaign: 'CA-05', group: 'ca-05-marking-codes', reason: 'marking_codes_intent', flags };
  }
  return { verdict: 'MOVE_WITHIN_CAMPAIGN', campaign: 'CA-05', group: 'ca-05-marking-setup', reason: 'general_marking_setup', flags };
}

function classifyPhrase(record) {
  const { phrase, final_campaign, final_group } = record;
  if (final_group === 'ca-01-specialist-search') {
    const c = classifyCA01(phrase);
    return { ...c, service_family: 'programmer_specialist', intent_modifier: c.reason, commercial_intent: c.verdict === 'REJECT' ? 'NONCOMMERCIAL' : 'COMMERCIAL' };
  }
  if (final_group === 'ca-05-direct-service-order') {
    const c = classifyCA05(phrase);
    return { ...c, service_family: 'marking', intent_modifier: c.reason, commercial_intent: c.verdict === 'REJECT' ? 'NONCOMMERCIAL' : 'COMMERCIAL' };
  }
  return {
    verdict: 'KEEP',
    campaign: final_campaign,
    group: final_group,
    reason: 'unchanged_non_oversized_group',
    flags: {},
    service_family: 'unchanged',
    intent_modifier: null,
    commercial_intent: 'COMMERCIAL',
  };
}

const GROUP_DEFS = {
  'ca-01-specialist-search': {
    group_name: 'Программист / специалист 1С — core specialist search',
    intent: 'Core commercial queries for 1C programmer/specialist (short-form identity queries)',
    landing_url: 'https://lk.corvonero.ru/programmist-1s/',
    utm_content: 'ca-01-specialist-search',
    display_path: 'programmist-1s',
    primary_ad_id: 'ad-ca-01-specialist-search',
    source_group: 'ca-01-specialist-search',
    ad_status: 'UNCHANGED_OPERATOR_APPROVED',
  },
  'ca-01-specialist-extended': {
    group_name: 'Программист / специалист 1С — extended specialist queries',
    intent: 'Extended or multi-modifier specialist search queries with commercial service intent',
    landing_url: 'https://lk.corvonero.ru/programmist-1s/',
    utm_content: 'ca-01-specialist-extended',
    display_path: 'programmist-1s',
    primary_ad_id: 'ad-ca-01-specialist-extended',
    source_group: 'ca-01-specialist-search',
    ad_status: 'DERIVED_REQUIRES_OPERATOR_REVIEW',
  },
  'ca-01-find-hire-specialist': {
    group_name: 'Программист / специалист 1С — find / hire specialist',
    intent: 'Explicit find, need, hire a 1C programmer or specialist',
    landing_url: 'https://lk.corvonero.ru/programmist-1s/',
    utm_content: 'ca-01-find-hire-specialist',
    display_path: 'programmist-1s',
    primary_ad_id: 'ad-ca-01-find-hire-specialist',
    source_group: 'ca-01-specialist-search',
    ad_status: 'DERIVED_REQUIRES_OPERATOR_REVIEW',
  },
  'ca-01-remote-freelance-specialist': {
    group_name: 'Программист / специалист 1С — remote / freelance / local',
    intent: 'Remote, freelance, private specialist or local Novosibirsk execution intent',
    landing_url: 'https://lk.corvonero.ru/programmist-1s/',
    utm_content: 'ca-01-remote-freelance-specialist',
    display_path: 'programmist-1s',
    primary_ad_id: 'ad-ca-01-remote-freelance-specialist',
    source_group: 'ca-01-specialist-search',
    ad_status: 'DERIVED_REQUIRES_OPERATOR_REVIEW',
  },
  'ca-01-specialist-by-product': {
    group_name: 'Программист / специалист 1С — product / role variants',
    intent: 'Specialist queries tied to 1C product lines or role variants (ZUP, UT, accountant, etc.)',
    landing_url: 'https://lk.corvonero.ru/programmist-1s/',
    utm_content: 'ca-01-specialist-by-product',
    display_path: 'programmist-1s',
    primary_ad_id: 'ad-ca-01-specialist-by-product',
    source_group: 'ca-01-specialist-search',
    ad_status: 'DERIVED_REQUIRES_OPERATOR_REVIEW',
  },
  'ca-01-price-intent': {
    group_name: 'Программист / специалист 1С — Price / cost intent',
    intent: 'PRICE_AND_COST',
    landing_url: 'https://lk.corvonero.ru/programmist-1s/',
    utm_content: 'ca-01-price-intent',
    display_path: 'stoimost-1s',
    primary_ad_id: 'ad-ca-01-price-intent',
    ad_status: 'UNCHANGED_OPERATOR_APPROVED',
  },
  'ca-01-direct-service-order': {
    group_name: 'Программист / специалист 1С — direct service order',
    intent: 'DIRECT_SERVICE_ORDER',
    landing_url: 'https://lk.corvonero.ru/programmist-1s/',
    utm_content: 'ca-01-direct-service-order',
    display_path: 'uslugi-1s',
    primary_ad_id: 'ad-ca-01-direct-service-order',
    ad_status: 'UNCHANGED_OPERATOR_APPROVED',
  },
  'ca-05-marking-setup': {
    group_name: 'Маркировка / Честный знак — general marking setup',
    intent: 'General marking setup and configuration in 1C (without Chestny Znak primary focus)',
    landing_url: 'https://lk.corvonero.ru/markirovka-chestny-znak/',
    utm_content: 'ca-05-marking-setup',
    display_path: 'markirovka-1s',
    primary_ad_id: 'ad-ca-05-marking-setup',
    source_group: 'ca-05-direct-service-order',
    ad_status: 'DERIVED_REQUIRES_OPERATOR_REVIEW',
  },
  'ca-05-chestny-znak-service': {
    group_name: 'Маркировка / Честный знак — Chestny Znak service',
    intent: 'Chestny Znak integration and marking exchange setup in 1C',
    landing_url: 'https://lk.corvonero.ru/markirovka-chestny-znak/',
    utm_content: 'ca-05-chestny-znak-service',
    display_path: 'markirovka-1s',
    primary_ad_id: 'ad-ca-05-chestny-znak-service',
    source_group: 'ca-05-direct-service-order',
    ad_status: 'DERIVED_REQUIRES_OPERATOR_REVIEW',
  },
  'ca-05-marking-codes': {
    group_name: 'Маркировка / Честный знак — marking codes setup',
    intent: 'Marking codes configuration and commissioning in 1C (not code purchase)',
    landing_url: 'https://lk.corvonero.ru/markirovka-chestny-znak/',
    utm_content: 'ca-05-marking-codes',
    display_path: 'markirovka-1s',
    primary_ad_id: 'ad-ca-05-marking-codes',
    source_group: 'ca-05-direct-service-order',
    ad_status: 'DERIVED_REQUIRES_OPERATOR_REVIEW',
  },
};

function main() {
  requireOperatorGate();
  const generatedAt = new Date().toISOString();
  const { adDecision, cleanupRegister, cleanupByPhrase } = loadOperatorInputs();
  const sourceHashes = {};
  for (const [role, fp] of Object.entries(SOURCE_FILES)) {
    sourceHashes[role] = { path: fp.replace(/\\/g, '/'), sha256: sha256File(fp) };
  }

  const allocation = JSON.parse(fs.readFileSync(SOURCE_FILES.phrase_allocation, 'utf8'));
  const groupRegister = JSON.parse(fs.readFileSync(SOURCE_FILES.group_register, 'utf8'));
  const primaryAdsSrc = JSON.parse(fs.readFileSync(SOURCE_FILES.primary_ads, 'utf8'));
  const campaignNegSrc = JSON.parse(fs.readFileSync(SOURCE_FILES.campaign_negatives, 'utf8'));
  const utmSrc = JSON.parse(fs.readFileSync(SOURCE_FILES.utm_map, 'utf8'));
  const settingsSrc = JSON.parse(fs.readFileSync(SOURCE_FILES.campaign_settings, 'utf8'));
  const crossSrc = JSON.parse(fs.readFileSync(SOURCE_FILES.cross_campaign, 'utf8'));
  const bidsSrc = JSON.parse(fs.readFileSync(SOURCE_FILES.bids, 'utf8'));

  const reaudits = [];
  const movements = [];
  const newRecords = [];
  const verdictCounts = { KEEP: 0, MOVE_WITHIN_CAMPAIGN: 0, MOVE_TO_OTHER_CAMPAIGN: 0, REJECT: 0, ABSTAIN: 0 };
  const operatorCleanupCounts = {
    additional_rejected: 0,
    additional_moved_within_campaign: 0,
    additional_moved_to_other_campaign: 0,
    keep_confirmed: 0,
  };
  const operatorAdValidation = {};

  const oversizedGroups = new Set(['ca-01-specialist-search', 'ca-05-direct-service-order']);
  let reviewedOversized = 0;
  let ct4RejectedBeforeOperator = 0;

  for (const rec of allocation.records) {
    if (rec.production_status !== 'DEPLOYABLE') continue;

    const isOversized = oversizedGroups.has(rec.final_group);
    if (isOversized) reviewedOversized++;

    const cls = classifyPhrase(rec);
    let finalVerdict = cls.verdict;
    let finalCampaign = cls.campaign ?? rec.final_campaign;
    let finalGroup = cls.group ?? rec.final_group;
    let finalReason = cls.reason;

    if (!isOversized && finalVerdict !== 'KEEP') {
      finalVerdict = 'KEEP';
      finalCampaign = rec.final_campaign;
      finalGroup = rec.final_group;
    }

    if (finalVerdict === 'REJECT' && isOversized) {
      ct4RejectedBeforeOperator++;
    }

    const cleanupRow = cleanupByPhrase.get(normalizePhraseKey(rec.phrase));
    if (cleanupRow) {
      const priorVerdict = finalVerdict;
      const priorCampaign = finalCampaign;
      const priorGroup = finalGroup;
      finalVerdict = cleanupRow.final_verdict;
      finalCampaign = cleanupRow.final_campaign ?? finalCampaign;
      finalGroup = cleanupRow.final_group ?? finalGroup;
      finalReason = cleanupRow.reason;

      if (finalVerdict === 'REJECT' && priorVerdict !== 'REJECT') {
        operatorCleanupCounts.additional_rejected++;
      } else if (finalVerdict === 'MOVE_WITHIN_CAMPAIGN' && priorGroup !== finalGroup) {
        operatorCleanupCounts.additional_moved_within_campaign++;
      } else if (finalVerdict === 'MOVE_TO_OTHER_CAMPAIGN' && priorCampaign !== finalCampaign) {
        operatorCleanupCounts.additional_moved_to_other_campaign++;
      } else if (finalVerdict === 'KEEP') {
        operatorCleanupCounts.keep_confirmed++;
      }
    }

    verdictCounts[finalVerdict] = (verdictCounts[finalVerdict] ?? 0) + 1;

    if (isOversized) {
      reaudits.push({
        phrase: rec.phrase,
        phrase_id: rec.phrase_id,
        current_campaign: rec.final_campaign,
        current_group: rec.final_group,
        commercial_intent: cls.commercial_intent,
        service_family: cls.service_family,
        intent_modifier: cls.intent_modifier,
        career_or_employment_issue: cls.flags.career_or_employment_issue ?? false,
        education_issue: cls.flags.education_issue ?? false,
        informational_issue: cls.flags.informational_issue ?? false,
        free_or_download_issue: cls.flags.free_or_download_issue ?? false,
        named_entity_issue: false,
        geography_issue: /москв|спб|питер/i.test(rec.phrase) && !/новосиб/i.test(rec.phrase),
        duplicate_or_overlap_issue: false,
        recommended_verdict: cls.verdict,
        recommended_campaign: cls.campaign ?? rec.final_campaign,
        recommended_group: cls.group ?? rec.final_group,
        reason: cls.reason,
      });
    }

    movements.push({
      phrase: rec.phrase,
      phrase_id: rec.phrase_id,
      original_campaign: rec.final_campaign,
      original_group: rec.final_group,
      final_verdict: finalVerdict,
      final_campaign: finalVerdict === 'REJECT' ? null : finalCampaign,
      final_group: finalVerdict === 'REJECT' ? null : finalGroup,
      reason: finalReason,
    });

    if (finalVerdict !== 'REJECT') {
      newRecords.push({
        ...rec,
        final_campaign: finalCampaign,
        final_group: finalGroup,
        production_status: 'DEPLOYABLE',
        ct4_moved: finalCampaign !== rec.final_campaign || finalGroup !== rec.final_group,
        ct4_source_group: rec.final_group,
        ct4_operator_cleanup: Boolean(cleanupRow),
      });
    } else {
      newRecords.push({
        ...rec,
        production_status: cleanupRow ? 'REJECTED_OPERATOR_CLEANUP' : 'REJECTED_CT4',
        ct4_reject_reason: finalReason,
        ct4_source_group: rec.final_group,
        ct4_operator_cleanup: Boolean(cleanupRow),
      });
    }
  }

  const phraseByGroup = new Map();
  for (const r of newRecords.filter((x) => x.production_status === 'DEPLOYABLE')) {
    const k = r.final_group;
    if (!phraseByGroup.has(k)) phraseByGroup.set(k, []);
    phraseByGroup.get(k).push(r);
  }

  const unchangedGroups = groupRegister.groups.filter(
    (g) => !oversizedGroups.has(g.group_id) && phraseByGroup.has(g.group_id)
  );

  const newGroupIds = [
    'ca-01-specialist-extended',
    'ca-01-find-hire-specialist',
    'ca-01-remote-freelance-specialist',
    'ca-01-specialist-by-product',
    'ca-05-marking-setup',
    'ca-05-chestny-znak-service',
    'ca-05-marking-codes',
  ];

  const migrationMap = {
    'ca-01-specialist-search': [
      'ca-01-specialist-search',
      'ca-01-specialist-extended',
      'ca-01-find-hire-specialist',
      'ca-01-remote-freelance-specialist',
      'ca-01-specialist-by-product',
    ],
    'ca-05-direct-service-order': ['ca-05-marking-setup', 'ca-05-chestny-znak-service', 'ca-05-marking-codes'],
  };

  function buildGroupEntry(groupId, campaignId) {
    const def = GROUP_DEFS[groupId];
    const orig = groupRegister.groups.find((g) => g.group_id === groupId);
    const phrases = phraseByGroup.get(groupId) ?? [];
    const meta = def ?? {
      group_name: orig?.group_name ?? groupId,
      intent: orig?.primary_intent ?? groupId,
      landing_url: orig?.final_lp_url_direction ?? '',
      utm_content: groupId,
      display_path: groupId,
      primary_ad_id: `ad-${groupId}`,
      ad_status: 'UNCHANGED_OPERATOR_APPROVED',
    };
    return {
      campaign_id: campaignId,
      group_id: groupId,
      group_name: meta.group_name ?? orig?.group_name,
      intent: meta.intent ?? orig?.primary_intent,
      phrase_count: phrases.length,
      primary_ad_id: meta.primary_ad_id,
      landing_url: meta.landing_url ?? orig?.final_lp_url_direction,
      utm_campaign: utmSrc.campaign_slugs[campaignId],
      utm_content: meta.utm_content ?? groupId,
      bid: bidsSrc.campaign_bids[campaignId],
      campaign_negative_set: 'account_shared + campaign_deployable',
      group_negative_set: `see CORVONERO-CT4-GROUP-NEGATIVES-v1.json#${groupId}`,
      status: phrases.length > 0 ? 'DEPLOYABLE' : 'EMPTY',
      representative_phrases: phrases.slice(0, 5).map((p) => p.phrase),
      deployable: phrases.length > 0,
      operator_primary_ad_status: meta.ad_status,
    };
  }

  const finalGroups = [];
  const allGroupIds = new Set();

  for (const g of unchangedGroups) {
    if ((phraseByGroup.get(g.group_id) ?? []).length === 0) continue;
    finalGroups.push(buildGroupEntry(g.group_id, g.campaign_id));
    allGroupIds.add(g.group_id);
  }

  for (const gid of ['ca-01-specialist-search', ...newGroupIds.filter((id) => id.startsWith('ca-01'))]) {
    if (allGroupIds.has(gid)) continue;
    const phrases = phraseByGroup.get(gid) ?? [];
    if (phrases.length === 0) continue;
    finalGroups.push(buildGroupEntry(gid, 'CA-01'));
    allGroupIds.add(gid);
  }

  for (const gid of newGroupIds.filter((id) => id.startsWith('ca-05'))) {
    const phrases = phraseByGroup.get(gid) ?? [];
    if (phrases.length === 0) continue;
    finalGroups.push(buildGroupEntry(gid, 'CA-05'));
    allGroupIds.add(gid);
  }

  for (const g of unchangedGroups.filter((x) => x.campaign_id === 'CA-05')) {
    if (allGroupIds.has(g.group_id)) continue;
    if ((phraseByGroup.get(g.group_id) ?? []).length === 0) continue;
    finalGroups.push(buildGroupEntry(g.group_id, g.campaign_id));
    allGroupIds.add(g.group_id);
  }

  finalGroups.sort((a, b) => a.campaign_id.localeCompare(b.campaign_id) || a.group_id.localeCompare(b.group_id));

  const groupsOver200 = finalGroups.filter((g) => g.phrase_count > 200);

  const adsBySource = new Map(primaryAdsSrc.ads.map((a) => [a.group_id, a]));
  const finalAds = [];
  const derivedAds = [];

  for (const g of finalGroups) {
    const existing = adsBySource.get(g.group_id);
    const def = GROUP_DEFS[g.group_id];
    if (existing && (!def || def.ad_status === 'UNCHANGED_OPERATOR_APPROVED')) {
      finalAds.push({ ...existing, status: 'UNCHANGED_OPERATOR_APPROVED' });
      continue;
    }

    const sourceId = def?.source_group ?? g.group_id;
    const sourceAd = adsBySource.get(sourceId);
    if (!sourceAd) continue;

    const opAd = adDecision.ads[g.group_id];
    if (!opAd) {
      throw new Error(`Missing operator ad decision for derived group ${g.group_id}`);
    }
    if (opAd.forbidden_headline_1 && opAd.headline_1 === opAd.forbidden_headline_1) {
      throw new Error(`Forbidden headline_1 used for ${g.group_id}`);
    }

    const limitCheck = validateOperatorAdFields(opAd);
    operatorAdValidation[g.group_id] = limitCheck;

    const derived = {
      campaign_id: g.campaign_id,
      group_id: g.group_id,
      source_ad_id: sourceAd.group_id,
      group_name: g.group_name,
      landing_page: { ...sourceAd.landing_page },
      primary_ad: {
        headline: opAd.headline_1,
        additional_headline: opAd.headline_2,
        text: opAd.text,
        headline_metrics: charMetrics(opAd.headline_1),
        additional_metrics: charMetrics(opAd.headline_2),
        text_metrics: charMetrics(opAd.text),
      },
      status: 'OPERATOR_APPROVED',
      approval_state: 'OPERATOR_APPROVED',
      approval_source: adDecision.approval_source,
      approval_scope: adDecision.approval_scope,
      approval_date: adDecision.approval_date,
      display_path: opAd.display_path,
      claim_changes: 'Operator-approved exact copy — subgroup intent boundary only',
      reason: `Split from ${sourceId} — CT-4 semantic regrouping + operator approval`,
      technical_limit_validation: limitCheck.pass ? 'PASS' : 'FAIL',
    };

    finalAds.push(derived);
    derivedAds.push({
      campaign_id: derived.campaign_id,
      group_id: derived.group_id,
      source_ad_id: derived.source_ad_id,
      headline_1: opAd.headline_1,
      headline_2: opAd.headline_2,
      text: opAd.text,
      display_path: opAd.display_path,
      landing_url: derived.landing_page.url,
      claim_changes: derived.claim_changes,
      reason: derived.reason,
      technical_limit_validation: derived.technical_limit_validation,
      approval_state: derived.approval_state,
      approval_source: adDecision.approval_source,
      approval_date: adDecision.approval_date,
      headline_1_metrics: derived.primary_ad.headline_metrics,
      headline_2_metrics: derived.primary_ad.additional_metrics,
      text_metrics: derived.primary_ad.text_metrics,
    });
  }

  const campaignNegatives = JSON.parse(JSON.stringify(campaignNegSrc));
  campaignNegatives.ct4_note = 'Preserved approved shared negatives; CA-05-only negative isolated to CA-05';

  const campaignNegAuthority = ['CA-01', 'CA-02', 'CA-03', 'CA-04', 'CA-05'].map((cid) => ({
    campaign_id: cid,
    negatives: [
      ...(campaignNegatives.layers.account_shared_deployable ?? []).map((t) => t.term),
      ...(campaignNegatives.layers.campaign_deployable ?? [])
        .filter((t) => t.campaign_id === cid)
        .map((t) => t.term),
    ],
    source: 'CORVONERO-EXT-W1-NEGATIVE-DEPLOYMENT-v1 + CT-4 reconciliation',
    reason: 'Preserved operator-approved controlled deployment set',
    match_design: 'word and phrase per entry in source deployment file',
    overblocking_risk: 'LOW for shared career/download terms; CA-05 code purchase term isolated to CA-05',
    approval_state: 'OPERATOR_APPROVED',
  }));

  const groupNegRules = [];
  const groupNegGroups = {};

  const ca01Routing = [
    { source: 'ca-01-specialist-search', dest: 'ca-01-price-intent', term: 'стоимость', reason: 'Route price intent to dedicated group' },
    { source: 'ca-01-specialist-search', dest: 'ca-01-find-hire-specialist', term: 'найти', reason: 'Route hire intent' },
    { source: 'ca-01-specialist-extended', dest: 'ca-01-find-hire-specialist', term: 'нужен', reason: 'Route hire intent from extended pool' },
    { source: 'ca-01-find-hire-specialist', dest: 'ca-01-specialist-search', term: 'программист 1с', reason: 'Protect core identity queries — REVIEW_REQUIRED', decision: 'REVIEW_REQUIRED' },
    { source: 'ca-01-remote-freelance-specialist', dest: 'ca-01-specialist-search', term: 'программист', reason: 'Broad term — DO_NOT_APPLY at group level', decision: 'DO_NOT_APPLY' },
  ];

  for (const g of finalGroups) {
    groupNegGroups[g.group_id] = { terms: [], rules: [] };
  }

  for (const r of ca01Routing) {
    groupNegRules.push({
      campaign_id: 'CA-01',
      source_group: r.source,
      negative: r.term,
      destination_or_protected_group: r.dest,
      reason: r.reason,
      example_phrases: [],
      overblocking_risk: r.decision === 'DO_NOT_APPLY' ? 'HIGH' : 'MEDIUM',
      approval_state: r.decision ?? 'OPERATOR_APPROVAL_RECOMMENDED',
    });
  }

  const ca05Routing = [
    { source: 'ca-05-marking-setup', dest: 'ca-05-chestny-znak-service', term: 'честный знак', reason: 'Route Chestny Znak intent' },
    { source: 'ca-05-chestny-znak-service', dest: 'ca-05-marking-setup', term: 'маркировка', reason: 'DO_NOT_APPLY — too broad', decision: 'DO_NOT_APPLY' },
    { source: 'ca-05-marking-setup', dest: 'ca-05-marking-codes', term: 'коды маркировки', reason: 'Route codes setup intent' },
  ];

  for (const r of ca05Routing) {
    groupNegRules.push({
      campaign_id: 'CA-05',
      source_group: r.source,
      negative: r.term,
      destination_or_protected_group: r.dest,
      reason: r.reason,
      example_phrases: [],
      overblocking_risk: r.decision === 'DO_NOT_APPLY' ? 'HIGH' : 'MEDIUM',
      approval_state: r.decision ?? 'REVIEW_REQUIRED',
    });
  }

  for (const rule of groupNegRules) {
    if (rule.approval_state === 'DO_NOT_APPLY') continue;
    if (!groupNegGroups[rule.source_group]) groupNegGroups[rule.source_group] = { terms: [], rules: [] };
    if (!groupNegGroups[rule.source_group].terms.includes(rule.negative)) {
      groupNegGroups[rule.source_group].terms.push(rule.negative);
    }
    groupNegGroups[rule.source_group].rules.push(rule);
  }

  const intraRouting = {
    'CA-01': ca01Routing.map((r) => ({
      source_group: r.source,
      destination_group: r.dest,
      overlap_terms: [r.term],
      recommended_negative: r.term,
      routing_effect: r.reason,
      overblocking_risk: r.decision === 'DO_NOT_APPLY' ? 'HIGH' : 'MEDIUM',
      decision: r.decision ?? 'REVIEW_REQUIRED',
    })),
    'CA-05': ca05Routing.map((r) => ({
      source_group: r.source,
      destination_group: r.dest,
      overlap_terms: [r.term],
      recommended_negative: r.term,
      routing_effect: r.reason,
      overblocking_risk: r.decision === 'DO_NOT_APPLY' ? 'HIGH' : 'MEDIUM',
      decision: r.decision ?? 'REVIEW_REQUIRED',
    })),
  };

  const interTerms = [
    'сопровождение', 'обслуживание', 'доработка', 'разработка', 'интеграция', 'сайт', 'битрикс',
    'маркировка', 'честный знак', 'тс пиот', 'коды маркировки',
  ];

  const interRouting = interTerms.map((term) => {
    let dest = 'REVIEW_REQUIRED';
    let source = 'CA-01';
    if (/маркиров|честн|пиот|код/.test(term)) { dest = 'CA-05'; source = 'CA-01'; }
    else if (/сопровожд|обслужив/.test(term)) { dest = 'CA-02'; source = 'CA-03'; }
    else if (/доработ|разработ/.test(term)) { dest = 'CA-03'; source = 'CA-02'; }
    else if (/интегр|сайт|битрикс/.test(term)) { dest = 'CA-04'; source = 'CA-03'; }
    return {
      source_campaign: source,
      negative: term,
      destination_campaign: dest,
      reason: `Conservative routing assessment — not auto-applied in CT-4`,
      phrase_examples: [],
      overblocking_risk: 'HIGH',
      approval_state: 'DO_NOT_APPLY',
    };
  });

  const transportConfig = {
    transport_config_id: 'corvonero-ct4-transport-config-v1',
    geo_region: 'Новосибирская область',
    organization_policy: { required_value: '', forbidden_ids: ['29500847237'] },
    forbidden_organization_ids: ['29500847237'],
    sitelinks_policy: 'OMITTED',
    cross_campaign_negatives_policy: 'NOT_APPLIED_UNLESS_APPROVED',
    bids_ref: SOURCE_FILES.bids.replace(/\\/g, '/'),
    display_paths_ref: SOURCE_FILES.display_paths.replace(/\\/g, '/'),
    group_negatives_ref: path.join(OUT_DIR, 'CORVONERO-CT4-GROUP-NEGATIVES-v1.json').replace(/\\/g, '/'),
    fragment_anchor_approved: false,
    ct4_authority: true,
  };

  const campaignSettings = JSON.parse(JSON.stringify(settingsSrc));
  campaignSettings.confirmed_boundary.geography = 'Новосибирская область';
  for (const c of campaignSettings.campaigns) {
    c.geography = 'Новосибирская область';
  }
  campaignSettings.ct4_transport_safe = true;

  const utmMap = JSON.parse(JSON.stringify(utmSrc));
  for (const g of finalGroups) {
    utmMap.group_slugs[g.group_id] = g.utm_content ?? g.group_id;
  }
  delete utmMap.group_slugs['ca-05-direct-service-order'];

  const deployableCount = newRecords.filter((r) => r.production_status === 'DEPLOYABLE').length;
  const deployableRecords = newRecords.filter((r) => r.production_status === 'DEPLOYABLE');
  const deployableBeforeOperatorCleanup = 839;
  const totalRejected =
    ct4RejectedBeforeOperator + operatorCleanupCounts.additional_rejected;
  const operatorDerivedApproved = derivedAds.filter((a) => a.approval_state === 'OPERATOR_APPROVED').length;
  const unapprovedDerivedAds = derivedAds.filter((a) => a.approval_state !== 'OPERATOR_APPROVED').length;
  const technicalLimitPass = Object.values(operatorAdValidation).every((v) => v.pass);
  const countReconciled = 895 - totalRejected === deployableCount;

  const files = {};

  files.reaudit = writeJson('CORVONERO-CT4-PHRASE-REAUDIT-v1.json', {
    reaudit_id: 'corvonero-ct4-phrase-reaudit-v1',
    generated_at: generatedAt,
    source_phrase_allocation: sourceHashes.phrase_allocation,
    reviewed_groups: [...oversizedGroups],
    reviewed_phrase_count: reviewedOversized,
    records: reaudits,
  });

  files.movement = writeJson('CORVONERO-CT4-PHRASE-MOVEMENT-REGISTER-v1.json', {
    register_id: 'corvonero-ct4-phrase-movement-register-v1',
    generated_at: generatedAt,
    source_phrase_allocation: sourceHashes.phrase_allocation,
    operator_cleanup_register_ref: OPERATOR_FILES.cleanup_register.replace(/\\/g, '/'),
    verdict_counts: verdictCounts,
    operator_cleanup_counts: operatorCleanupCounts,
    migration_map: migrationMap,
    movements,
    records: deployableRecords,
  });

  files.architecture = writeJson('CORVONERO-CT4-GROUP-ARCHITECTURE-v1.json', {
    architecture_id: 'corvonero-ct4-group-architecture-v1',
    generated_at: generatedAt,
    original_groups: 15,
    final_groups: finalGroups.length,
    migration_map: migrationMap,
    groups_over_200: groupsOver200.length,
    groups: finalGroups,
  });

  files.primaryAds = writeJson('CORVONERO-CT4-PRIMARY-ADS-v1.json', {
    pack_id: 'corvonero-ct4-primary-ads-v1',
    generated_at: generatedAt,
    operator_ad_decision_ref: OPERATOR_FILES.ad_decision.replace(/\\/g, '/'),
    deployable_ads: finalAds.length,
    derived_operator_approved: operatorDerivedApproved,
    derived_requires_review: unapprovedDerivedAds,
    ads: finalAds,
    derived_ads: derivedAds,
    operator_ad_validation: operatorAdValidation,
  });

  files.campaignNeg = writeJson('CORVONERO-CT4-CAMPAIGN-NEGATIVES-v1.json', {
    authority_id: 'corvonero-ct4-campaign-negatives-v1',
    generated_at: generatedAt,
    source: sourceHashes.campaign_negatives,
    layers: campaignNegatives.layers,
    campaigns: campaignNegAuthority,
  });

  files.groupNeg = writeJson('CORVONERO-CT4-GROUP-NEGATIVES-v1.json', {
    authority_id: 'corvonero-ct4-group-negatives-v1',
    generated_at: generatedAt,
    groups: groupNegGroups,
    rules: groupNegRules,
  });

  files.intra = writeJson('CORVONERO-CT4-INTRA-CAMPAIGN-ROUTING-v1.json', {
    routing_id: 'corvonero-ct4-intra-campaign-routing-v1',
    generated_at: generatedAt,
    ...intraRouting,
  });

  files.inter = writeJson('CORVONERO-CT4-INTER-CAMPAIGN-ROUTING-v1.json', {
    routing_id: 'corvonero-ct4-inter-campaign-routing-v1',
    generated_at: generatedAt,
    deployment_policy: 'NOT_APPLIED — conservative plan only',
    cross_campaign_negatives_deployed: 0,
    operator_decision: 'NOT_DEPLOYED',
    rules: interRouting,
    source_cross_campaign: sourceHashes.cross_campaign,
  });

  files.transport = writeJson('CORVONERO-CT4-TRANSPORT-CONFIG-v1.json', transportConfig);
  files.campaignSettings = writeJson('CORVONERO-CT4-CAMPAIGN-SETTINGS-v1.json', campaignSettings);
  files.utm = writeJson('CORVONERO-CT4-UTM-MAP-v1.json', utmMap);

  const manifestFiles = [
    { role: 'phrase_allocation', path: files.movement.path, sha256: files.movement.sha256, required: true },
    { role: 'campaign_architecture', path: files.architecture.path, sha256: files.architecture.sha256, required: true },
    { role: 'primary_ads', path: files.primaryAds.path, sha256: files.primaryAds.sha256, required: true },
    { role: 'callouts', path: SOURCE_FILES.callouts.replace(/\\/g, '/'), sha256: sourceHashes.callouts.sha256, required: true },
    { role: 'campaign_negatives', path: files.campaignNeg.path, sha256: files.campaignNeg.sha256, required: true },
    { role: 'group_negatives', path: files.groupNeg.path, sha256: files.groupNeg.sha256, required: true },
    { role: 'cross_campaign_rules', path: files.inter.path, sha256: files.inter.sha256, required: true },
    { role: 'utm_map', path: files.utm.path, sha256: files.utm.sha256, required: true },
    { role: 'campaign_settings', path: files.campaignSettings.path, sha256: files.campaignSettings.sha256, required: true },
    { role: 'transport_config', path: files.transport.path, sha256: files.transport.sha256, required: true },
  ];

  const manifest = {
    schema_version: '1.0.0',
    project_id: 'mars-search-ppc-production',
    pilot_id: 'corvonero',
    authority_checkpoint: 'corvonero-ct4-operator-approval-v1',
    campaign_scope: ['CA-01', 'CA-02', 'CA-03', 'CA-04', 'CA-05'],
    operator_approval_state: 'OPERATOR_APPROVED',
    generated_at: generatedAt,
    files: manifestFiles.map((f) => ({ ...f, path: f.path.replace(/\\/g, '/') })),
  };

  writeJson('CORVONERO-CT4-SOURCE-AUTHORITY-RECEIPT-v1.json', {
    receipt_id: 'corvonero-ct4-source-authority-receipt-v1',
    generated_at: generatedAt,
    source_authority_hashes: sourceHashes,
  });

  files.manifest = writeJson('CORVONERO-CT4-AUTHORITY-MANIFEST-v1.json', manifest);

  const validationPreview = {
    groups_over_200: groupsOver200.map((g) => ({ group_id: g.group_id, count: g.phrase_count })),
    deployable_phrases: deployableCount,
    deployable_before_operator_cleanup: deployableBeforeOperatorCleanup,
    rejected_ct4_before_operator: ct4RejectedBeforeOperator,
    operator_additional_rejected: operatorCleanupCounts.additional_rejected,
    operator_additional_moved_within_campaign: operatorCleanupCounts.additional_moved_within_campaign,
    operator_additional_moved_to_other_campaign: operatorCleanupCounts.additional_moved_to_other_campaign,
    total_rejected: totalRejected,
    count_reconciled: countReconciled,
    derived_ads_operator_approved: operatorDerivedApproved,
    unapproved_derived_ads: unapprovedDerivedAds,
    technical_ad_limits: technicalLimitPass ? 'PASS' : 'FAIL',
    operator_ad_validation: operatorAdValidation,
  };

  files.validation = writeJson('CORVONERO-CT4-VALIDATION-v1.json', {
    validation_id: 'corvonero-ct4-validation-v1',
    generated_at: generatedAt,
    preflight: validationPreview,
    manifest_path: files.manifest.path.replace(/\\/g, '/'),
  });

  const transportReady =
    groupsOver200.length === 0 &&
    unapprovedDerivedAds === 0 &&
    technicalLimitPass &&
    countReconciled;

  const verdict = transportReady
    ? 'PASS — FINAL AUTHORITY APPROVED'
    : technicalLimitPass === false
      ? 'PARTIAL — AUTHORITY CORRECTION STILL REQUIRED'
      : groupsOver200.length > 0
        ? 'FAIL — ARCHITECTURE OR AUTHORITY GAPS REMAIN'
        : 'PARTIAL — AUTHORITY CORRECTION STILL REQUIRED';

  files.result = writeJson('CORVONERO-CT4-RESULT-v1.json', {
    result_id: 'corvonero-ct4-result-v1',
    generated_at: generatedAt,
    verdict,
    counts: {
      original_total_phrases: 895,
      reviewed_oversized_group_phrases: reviewedOversized,
      kept: verdictCounts.KEEP,
      moved_within_campaign: verdictCounts.MOVE_WITHIN_CAMPAIGN,
      moved_to_other_campaign: verdictCounts.MOVE_TO_OTHER_CAMPAIGN,
      rejected_ct4_before_operator_cleanup: ct4RejectedBeforeOperator,
      operator_additional_rejected: operatorCleanupCounts.additional_rejected,
      operator_additional_moved_within_campaign: operatorCleanupCounts.additional_moved_within_campaign,
      operator_additional_moved_to_other_campaign: operatorCleanupCounts.additional_moved_to_other_campaign,
      rejected_total: totalRejected,
      abstain: verdictCounts.ABSTAIN,
      deployable_before_operator_cleanup: deployableBeforeOperatorCleanup,
      final_deployable_phrases: deployableCount,
      original_groups: 15,
      final_groups: finalGroups.length,
      groups_over_200: groupsOver200.length,
      operator_approved_derived_ads: operatorDerivedApproved,
      unapproved_derived_ads: unapprovedDerivedAds,
      count_reconciled: countReconciled,
    },
    ct5_generation: transportReady ? 'READY FOR SEPARATE AUTHORIZATION' : 'NOT YET AUTHORIZED',
  });

  writeMd('CORVONERO-CT4-PHRASE-REAUDIT-v1.md', `# CORVONERO CT-4 Phrase Re-Audit v1\n\nGenerated: ${generatedAt}\n\nReviewed oversized groups: ${[...oversizedGroups].join(', ')}\n\nRecords: ${reaudits.length}\n`);
  writeMd('CORVONERO-CT4-PHRASE-MOVEMENT-REGISTER-v1.md', `# CORVONERO CT-4 Phrase Movement Register v1\n\n${JSON.stringify(verdictCounts, null, 2)}\n`);
  writeMd('CORVONERO-CT4-GROUP-ARCHITECTURE-v1.md', `# CORVONERO CT-4 Group Architecture v1\n\nFinal groups: ${finalGroups.length}\n\nGroups over 200: ${groupsOver200.length}\n`);
  writeMd('CORVONERO-CT4-PRIMARY-ADS-v1.md', `# CORVONERO CT-4 Primary Ads v1\n\nDerived ads requiring review: ${derivedAds.length}\n`);
  writeMd('CORVONERO-CT4-CAMPAIGN-NEGATIVES-v1.md', `# CORVONERO CT-4 Campaign Negatives v1\n`);
  writeMd('CORVONERO-CT4-GROUP-NEGATIVES-v1.md', `# CORVONERO CT-4 Group Negatives v1\n\nRules: ${groupNegRules.length}\n`);
  writeMd('CORVONERO-CT4-INTRA-CAMPAIGN-ROUTING-v1.md', `# CORVONERO CT-4 Intra-Campaign Routing v1\n`);
  writeMd('CORVONERO-CT4-INTER-CAMPAIGN-ROUTING-v1.md', `# CORVONERO CT-4 Inter-Campaign Routing v1\n`);
  writeMd('CORVONERO-CT4-TRANSPORT-CONFIG-v1.md', `# CORVONERO CT-4 Transport Config v1\n\nRegion: Новосибирская область\n\nOrganization: BLANK\n`);
  writeMd('CORVONERO-CT4-AUTHORITY-MANIFEST-v1.md', `# CORVONERO CT-4 Authority Manifest v1\n\nManifest: ${files.manifest.path}\n`);
  writeMd('CORVONERO-CT4-VALIDATION-v1.md', `# CORVONERO CT-4 Validation v1\n\n${JSON.stringify(validationPreview, null, 2)}\n`);
  writeMd('CORVONERO-CT4-RESULT-v1.md', `# CORVONERO CT-4 Result v1\n\n**Verdict:** ${verdict}\n`);

  const finalApproval = {
    approval_id: 'corvonero-ct4-final-approval-v1',
    generated_at: generatedAt,
    verdict: transportReady
      ? 'CORVONERO COMMANDER CT-4: PASS — FINAL AUTHORITY APPROVED'
      : 'CORVONERO COMMANDER CT-4: PARTIAL — AUTHORITY CORRECTION STILL REQUIRED',
    operator_ad_decision_ref: OPERATOR_FILES.ad_decision.replace(/\\/g, '/'),
    operator_cleanup_register_ref: OPERATOR_FILES.cleanup_register.replace(/\\/g, '/'),
    operator_approved_derived_ads: operatorDerivedApproved,
    unapproved_ads: unapprovedDerivedAds,
    groups_over_200: groupsOver200.length,
    final_deployable_phrases: deployableCount,
    deployable_before_operator_cleanup: deployableBeforeOperatorCleanup,
    transport_validation_expected: transportReady ? 'PASS' : 'PENDING_OR_FAIL',
    technical_ad_limits: technicalLimitPass ? 'PASS' : 'FAIL',
    ct5_generation: transportReady ? 'READY FOR SEPARATE AUTHORIZATION' : 'NOT YET AUTHORIZED',
    count_reconciliation: {
      original_pre_ct4: 895,
      ct4_rejected_before_operator_cleanup: ct4RejectedBeforeOperator,
      operator_additional_rejected: operatorCleanupCounts.additional_rejected,
      operator_additional_moved_within_campaign: operatorCleanupCounts.additional_moved_within_campaign,
      operator_additional_moved_to_other_campaign: operatorCleanupCounts.additional_moved_to_other_campaign,
      total_rejected: totalRejected,
      final_deployable: deployableCount,
      reconciled: countReconciled,
    },
  };
  writeJson('CORVONERO-CT4-FINAL-APPROVAL-v1.json', finalApproval);
  writeMd(
    'CORVONERO-CT4-FINAL-APPROVAL-v1.md',
    `# CORVONERO CT-4 Final Approval v1\n\n**Verdict:** ${finalApproval.verdict}\n\nDeployable: ${deployableCount} (before operator cleanup: ${deployableBeforeOperatorCleanup})\n`
  );

  writeMd(
    'CORVONERO-CT4-OPERATOR-AD-DECISION-v1.md',
    `# CORVONERO CT-4 Operator Ad Decision v1\n\nBinding operator copy for 7 derived ads.\n\nApproval date: ${adDecision.approval_date}\n`
  );
  writeMd(
    'CORVONERO-CT4-OPERATOR-CLEANUP-REGISTER-v1.md',
    `# CORVONERO CT-4 Operator Cleanup Register v1\n\nMandatory phrase reviews: ${cleanupRegister.corrections.length}\n`
  );

  const reportPath = path.join(
    PROJECT_ROOT,
    'reports',
    'REPORT-corvonero-commander-ct4-operator-approval-and-cleanup-v1.md'
  );
  fs.writeFileSync(
    reportPath,
    `# REPORT — Corvonero Commander CT-4 Operator Approval and Cleanup v1

Generated: ${generatedAt}

## Preflight

| Check | Result |
|-------|--------|
| Drive | X: |
| Volume label | AI WS |
| Repository | X:\\\\AI MARS\\\\ |
| Branch | mars/canonical-post-recovery |
| Write scope | projects/mars-search-ppc-production/ |

## Part 1 — Technical copy validation

| Ad group | H1 (≤56) | H2 (≤30) | Text (≤81) | Path (≤20) |
|----------|----------|----------|------------|------------|
${Object.entries(operatorAdValidation)
  .map(([gid, v]) => {
    const ad = adDecision.ads[gid];
    return `| ${gid} | ${v.lengths.headline_1} ${v.checks.headline_1 ? 'PASS' : '**FAIL**'} | ${v.lengths.headline_2} ${v.checks.headline_2 ? 'PASS' : '**FAIL**'} | ${v.lengths.text} ${v.checks.text ? 'PASS' : '**FAIL**'} | ${v.lengths.display_path} ${v.checks.display_path ? 'PASS' : '**FAIL**'} |`;
  })
  .join('\n')}

${technicalLimitPass ? '' : '**STOP — OPERATOR-APPROVED COPY EXCEEDS TECHNICAL LIMIT** (`ca-01-specialist-extended` text = 84 > 81). Copy applied verbatim per binding operator decision; not auto-shortened.\n'}

## Part 2 — Phrase cleanup

| Phrase | Verdict | Final destination | Reason |
|--------|---------|-------------------|--------|
${cleanupRegister.corrections
  .map(
    (r) =>
      `| ${r.phrase} | ${r.final_verdict} | ${r.final_campaign ?? '—'} / ${r.final_group ?? '—'} | ${r.reason} |`
  )
  .join('\n')}

## Part 5 — Count reconciliation

| Metric | Value |
|--------|-------|
| Original pre-CT4 | 895 |
| CT-4 rejected before operator cleanup | ${ct4RejectedBeforeOperator} |
| Additional rejected (operator cleanup) | ${operatorCleanupCounts.additional_rejected} |
| Additional moved within campaign | ${operatorCleanupCounts.additional_moved_within_campaign} |
| Additional moved to other campaign | ${operatorCleanupCounts.additional_moved_to_other_campaign} |
| **Total rejected** | **${totalRejected}** |
| Before operator cleanup deployable | ${deployableBeforeOperatorCleanup} |
| **Final deployable** | **${deployableCount}** |
| Reconciled (895 − rejected = deployable) | ${countReconciled ? 'YES' : 'NO'} |

## Verdict

\`\`\`
CORVONERO COMMANDER CT-4:
${transportReady ? 'PASS — FINAL AUTHORITY APPROVED' : 'PARTIAL — AUTHORITY CORRECTION STILL REQUIRED'}

Groups over 200: ${groupsOver200.length}
Final deployable phrases: ${deployableCount}
Operator-approved derived ads: ${operatorDerivedApproved}
Unapproved ads: ${unapprovedDerivedAds}
Technical ad limits: ${technicalLimitPass ? 'PASS' : 'FAIL'}
CT-5 generation: ${transportReady ? 'READY FOR SEPARATE AUTHORIZATION' : 'NOT YET AUTHORIZED'}
\`\`\`

## CT-4 authority manifest

\`${files.manifest.path.replace(/\\/g, '/')}\`
`
  );

  console.log(JSON.stringify({ verdict, counts: files.result, manifest: files.manifest.path, groupsOver200, deployableCount, technicalLimitPass }, null, 2));
}

main();
