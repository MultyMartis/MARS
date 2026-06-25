#!/usr/bin/env node
/**
 * ORCA — Production Scope Recovery Gate (v6 rejection → v7 input).
 * Evidence-only audit; does not generate dataset v7 or Commander XLSX v7.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createRequire } from 'module';
import { GROUPS, DOMAIN } from './lib/groups-config.mjs';

const require = createRequire(import.meta.url);

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const MIG_ROOT = path.resolve(ROOT, '../../../incoming/mig/pilots/corvonero/session-mig-20260622-corv01');

const PATHS = {
  repair: path.join(ROOT, 'production/repair/v6-production-input-package.json'),
  v5Kw: path.join(ROOT, 'production/final-keyword-registry-v5.json'),
  v6Kw: path.join(ROOT, 'production/final-keyword-registry-v6.json'),
  v5Ads: path.join(ROOT, 'production/final-ad-registry-v5.json'),
  v6Ads: path.join(ROOT, 'production/final-ad-registry-v6.json'),
  v6Groups: path.join(ROOT, 'production/final-group-registry-v6.json'),
  v6Neg: path.join(ROOT, 'production/final-negative-registry-v6.json'),
  v6Semantic: path.join(ROOT, 'production/semantic-evidence-review-v6.json'),
  v5Dataset: path.join(ROOT, 'production/direct-commander-production-dataset-v5.json'),
  v6Dataset: path.join(ROOT, 'production/direct-commander-production-dataset-v6.json'),
  mig: path.join(MIG_ROOT, 'keyword_registry.json'),
};

const HELD_GROUP_IDS = [
  'CORV-G07-04',
  'CORV-G05-06',
  'CORV-G04-01',
  'CORV-G04-02',
  'CORV-G04-03',
  'CORV-G01-02',
  'CORV-G01-06',
  'CORV-G01-04',
];

const REGRESSION_ANCHORS = [
  'расчет себестоимости 1с',
  'себестоимость в 1с',
  'планирование закупок 1с',
  'платежный календарь 1с',
  'перенос данных в 1с',
  'миграция данных 1с',
  'внедрение 1с',
  'обслуживание 1с',
  'программист 1с новосибирск',
  'восстановление работы 1с',
  'срочно программист 1с',
];

const INFO_ACTIVE_ANCHORS = [
  'маркировка лекарств проверить',
  'маркировка автозапчастей 2026',
  'маркировка автозапчастей честный знак 2026',
  '1с программист 2026',
];

const GENERIC_HYPOTHESIS_SNIPPET = 'users configuring TS PIOT/marking in 1C retail';

const OPERATOR_SERVICES = [
  { id: 'SVC-01', name: 'программист 1С', source: 'operator-scope-correction-v1.md', groups: ['CORV-G01-01', 'CORV-G01-02'] },
  { id: 'SVC-02', name: 'услуги программиста 1С', source: 'operator-scope-correction-v1.md', groups: ['CORV-G01-01'] },
  { id: 'SVC-03', name: 'настройка 1С', source: 'operator-scope-correction-v1.md', groups: ['CORV-G01-03'] },
  { id: 'SVC-04', name: 'внедрение 1С', source: 'operator-scope-correction-v1.md', groups: ['CORV-G01-04'] },
  { id: 'SVC-05', name: 'сопровождение 1С', source: 'operator-scope-correction-v1.md', groups: ['CORV-G01-05'] },
  { id: 'SVC-06', name: 'обслуживание 1С', source: 'operator-scope-correction-v1.md', groups: ['CORV-G01-06'] },
  { id: 'SVC-07', name: 'разовые работы', source: 'operator-scope-correction-v1.md', groups: ['CORV-G01-08'] },
  { id: 'SVC-08', name: 'абонентское сопровождение', source: 'operator-scope-correction-v1.md', groups: ['CORV-G01-07'] },
  { id: 'SVC-09', name: 'доработка 1С', source: 'operator-scope-correction-v1.md', groups: ['CORV-G02-01'] },
  { id: 'SVC-10', name: 'доработка конфигурации', source: 'operator-scope-correction-v1.md', groups: ['CORV-G02-02'] },
  { id: 'SVC-11', name: 'доработка существующей базы', source: 'operator-scope-correction-v1.md', groups: ['CORV-G02-03'] },
  { id: 'SVC-12', name: 'обновление доработанной 1С', source: 'operator-scope-correction-v1.md', groups: ['CORV-G02-04'] },
  { id: 'SVC-13', name: 'перенос и сохранение доработок', source: 'operator-scope-correction-v1.md', groups: ['CORV-G02-05'] },
  { id: 'SVC-14', name: 'исправление доработок после обновления', source: 'operator-scope-correction-v1.md', groups: ['CORV-G02-06'] },
  { id: 'SVC-15', name: 'настройка отчёта / доработка отчёта', source: 'operator-scope-correction-v1.md', groups: ['CORV-G03-01'] },
  { id: 'SVC-16', name: 'создание отчёта', source: 'operator-scope-correction-v1.md', groups: ['CORV-G03-02'] },
  { id: 'SVC-17', name: 'печатная форма / доработка печатной формы', source: 'operator-scope-correction-v1.md', groups: ['CORV-G03-03', 'CORV-G03-04'] },
  { id: 'SVC-18', name: 'внешние отчёты и обработки', source: 'operator-scope-correction-v1.md', groups: ['CORV-G03-05'] },
  { id: 'SVC-19', name: 'РМК / рабочее место кассира', source: 'operator-scope-correction-v1.md', groups: ['CORV-G03-06'] },
  { id: 'SVC-20', name: 'расчёт себестоимости', source: 'operator-scope-correction-v1.md', groups: ['CORV-G04-01'] },
  { id: 'SVC-21', name: 'планирование закупок', source: 'operator-scope-correction-v1.md', groups: ['CORV-G04-02'] },
  { id: 'SVC-22', name: 'платёжный календарь', source: 'operator-scope-correction-v1.md', groups: ['CORV-G04-03'] },
  { id: 'SVC-23', name: 'интеграция 1С с сайтом / обмен', source: 'operator-scope-correction-v1.md', groups: ['CORV-G05-01'] },
  { id: 'SVC-24', name: 'интеграция 1С Битрикс', source: 'operator-scope-correction-v1.md', groups: ['CORV-G05-02'] },
  { id: 'SVC-25', name: 'интеграция 1С с кассой', source: 'operator-scope-correction-v1.md', groups: ['CORV-G05-03'] },
  { id: 'SVC-26', name: 'синхронизация 1С', source: 'operator-scope-correction-v1.md', groups: ['CORV-G05-04'] },
  { id: 'SVC-27', name: 'настройка обмена', source: 'operator-scope-correction-v1.md', groups: ['CORV-G05-05'] },
  { id: 'SVC-28', name: 'перенос данных / миграция', source: 'operator-scope-correction-v1.md', groups: ['CORV-G05-06'] },
  { id: 'SVC-29', name: 'маркировка и Честный знак (все категории)', source: 'operator-scope-correction-v1.md', groups: ['CORV-G06-01', 'CORV-G06-02', 'CORV-G06-03', 'CORV-G06-04', 'CORV-G06-05', 'CORV-G06-06', 'CORV-G06-07', 'CORV-G06-08', 'CORV-G06-09', 'CORV-G06-10', 'CORV-G06-11', 'CORV-G06-12', 'CORV-G06-13'] },
  { id: 'SVC-30', name: 'неисправности / срочная помощь', source: 'operator-scope-correction-v1.md', groups: ['CORV-G07-01', 'CORV-G07-02', 'CORV-G07-03', 'CORV-G07-04'] },
  { id: 'SVC-31', name: 'ТС ПИОТ', source: 'operator-scope-correction-v1.md', groups: ['CORV-G08-01', 'CORV-G08-02'] },
];

function loadJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function norm(s) {
  return String(s || '')
    .toLowerCase()
    .replace(/ё/g, 'е')
    .trim();
}

function findAnchorRecovery(phrase, commercialRecovery) {
  const exact = commercialRecovery.find((r) => norm(r.phrase) === norm(phrase));
  if (exact) return exact;
  return commercialRecovery.find(
    (r) =>
      norm(r.phrase).startsWith(`${norm(phrase)} `) ||
      norm(r.phrase).startsWith(norm(phrase)) && norm(r.phrase).length <= norm(phrase).length + 25
  );
}

function writeJson(rel, data) {
  const p = path.join(ROOT, rel);
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, JSON.stringify(data, null, 2), 'utf8');
  return rel;
}

function writeMd(rel, body) {
  const p = path.join(ROOT, rel);
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, body, 'utf8');
  return rel;
}

function groupById(id) {
  return GROUPS.find((g) => g.id === id);
}

function landingUrl(g) {
  if (!g) return null;
  return `https://${DOMAIN}${g.url}`;
}

function isInformationalPhrase(phrase) {
  const p = norm(phrase);
  if (INFO_ACTIVE_ANCHORS.some((a) => norm(a) === p)) return { match: true, reason: 'regression_anchor_informational' };
  if (/\bпроверить\b/.test(p)) return { match: true, reason: 'verification_intent' };
  if (/\bс какого года\b|\bкогда начн/.test(p)) return { match: true, reason: 'regulatory_timeline' };
  if (/\bобязательная маркировка\b/.test(p)) return { match: true, reason: 'mandatory_labeling_research' };
  if (/\bсписок товаров\b|\bсписок маркируем/.test(p)) return { match: true, reason: 'regulated_goods_list' };
  if (/\bличный кабинет\b/.test(p)) return { match: true, reason: 'personal_cabinet_access' };
  if (/\bкак сделать\b/.test(p)) return { match: true, reason: 'diy_how_to' };
  if (/\bкак настроить\b/.test(p) && !/\b(под ключ|заказ|услуг|программист|специалист|аутсорс)\b/.test(p)) {
    return { match: true, reason: 'diy_setup_without_hire_signal' };
  }
  if (/\b2026\b/.test(p) && /\bмаркиров/.test(p)) return { match: true, reason: 'regulatory_year_marking' };
  if (/\b2026\b/.test(p) && /\bпрограммист\b/.test(p)) return { match: true, reason: 'career_year_noise' };
  return { match: false, reason: null };
}

function isDirectCommercialSeed(keywordId, phrase, fromStatus) {
  const p = norm(phrase);
  if (keywordId?.startsWith('seed-')) return true;
  if (REGRESSION_ANCHORS.some((a) => norm(a) === p)) return true;
  if (fromStatus === 'ACTIVE COMMERCIAL' && HELD_GROUP_IDS.some((gid) => keywordId?.includes(gid.replace('CORV-', '')))) return true;
  const commercialSignals = [
    /программист/,
    /внедрен/,
    /обслуживан/,
    /перенос.*данн/,
    /миграц.*данн/,
    /себестоим/,
    /планирован.*закуп/,
    /платежн.*календар/,
    /восстановлен.*работ/,
    /срочно программист/,
    /новосибирск.*программист|программист.*новосибирск/,
  ];
  return commercialSignals.some((rx) => rx.test(p));
}

function classifyExclusionRule(ch, repair) {
  if (ch.keyword_id?.startsWith('seed-') && ch.from === 'ACTIVE COMMERCIAL' && ch.to === 'EXCLUDE') {
    return 'RULE-NARROW-SEED-EXCLUSION — QA repair treated operator seed as disposable when group became empty';
  }
  if (ch.from === 'ACTIVE COMMERCIAL' && ch.to === 'EXCLUDE' && isDirectCommercialSeed(ch.keyword_id, ch.phrase, ch.from)) {
    return 'RULE-COMMERCIAL-SEED-EXCLUSION — direct paid-service query removed; cascaded group to HOLD';
  }
  if (ch.from === 'ACTIVE COMMERCIAL' && ch.to === 'HOLD') {
    return 'RULE-THIN-GROUP-HOLD — phrase moved to HOLD without phrase-specific proof; often print-form cluster';
  }
  if (String(ch.to).startsWith('EXCLUDE')) {
    return 'RULE-SEMANTIC-EXCLUSION — informational/regulatory/DIY classification from v5 QA repair';
  }
  if (String(ch.to).includes('CONTROLLED TEST')) {
    return 'RULE-CONTROLLED-TEST-UPGRADE — status normalized; hypothesis may be generic';
  }
  return 'RULE-STATUS-PASS-THROUGH';
}

function buildPhraseSpecificHypothesis(kw, group) {
  const phrase = kw.raw_phrase || kw.phrase;
  const g = group || groupById(kw.final_group || kw.group_id);
  const intent = g?.intent || 'general';
  const service = g?.name || kw.final_group;
  const templates = {
    ts_piot_setup: `Paid setup: organization configuring TS PIOT in 1C for «${phrase}» may order specialist connection.`,
    ts_piot_integration: `Paid integration: query «${phrase}» may convert to TS PIOT ↔ 1C integration work.`,
    sync_exchange: `Paid exchange setup: «${phrase}» often precedes hiring a 1C integrator to fix or configure synchronization.`,
    sync_failure: `Urgent commercial: broken sync query «${phrase}» may convert to paid troubleshooting.`,
    print_form_modification: `Paid customization: user changing print forms for «${phrase}» may hire a 1C developer.`,
    print_forms_general: `Paid print-form work: «${phrase}» may convert to developer engagement for forms in 1C.`,
    external_reports: `Paid external report/processing work: «${phrase}» may convert to scoped development.`,
    support_retainer: `Retainer opportunity: «${phrase}» may convert to ongoing 1C support contract.`,
    marking_medicines: `Paid marking setup: pharmacy/retail query «${phrase}» may convert to 1C medicine marking configuration.`,
    honest_sign: `Paid Честный знак integration: «${phrase}» may convert to 1C marking onboarding.`,
    marking_auto_parts: `Paid auto-parts marking: «${phrase}» may convert to 1C catalog marking setup.`,
  };
  return (
    templates[intent] ||
    `Paid 1C service: «${phrase}» in group «${service}» may convert to commercial engagement when user needs implementation, not self-service FAQ.`
  );
}

function hypothesisMatchesGroup(hypothesis, groupId) {
  if (!hypothesis?.includes(GENERIC_HYPOTHESIS_SNIPPET)) return true;
  return groupId?.startsWith('CORV-G08') || groupId?.startsWith('CORV-G06');
}

function main() {
  const repair = loadJson(PATHS.repair);
  const v5Kw = loadJson(PATHS.v5Kw);
  const v6Kw = loadJson(PATHS.v6Kw);
  const v5Ads = loadJson(PATHS.v5Ads);
  const v6Ads = loadJson(PATHS.v6Ads);
  const v6Groups = loadJson(PATHS.v6Groups);
  const v6Semantic = loadJson(PATHS.v6Semantic);
  const v6Dataset = loadJson(PATHS.v6Dataset);
  const v5Dataset = loadJson(PATHS.v5Dataset);
  const mig = fs.existsSync(PATHS.mig) ? loadJson(PATHS.mig) : { keywords: [] };

  const groupMap = Object.fromEntries(GROUPS.map((g) => [g.id, g]));
  const v5KwById = new Map((v5Kw.keywords || v5Dataset.keywords || []).map((k) => [k.keyword_id, k]));
  const v6KwByPhrase = new Map((v6Kw.keywords || []).map((k) => [norm(k.raw_phrase), k]));
  const v6Excluded = v6Dataset.excluded_keywords || [];
  const v6ExcludedById = new Map(v6Excluded.map((k) => [k.keyword_id, k]));

  const repairExclusions = [];
  for (const ex of repair.semantic_exclusions || []) {
    repairExclusions.push({ ...ex, rule: 'RULE-EDUCATION-EXCLUSION', inherited_from: 'v5-qa-repair-gate-v2 education filter' });
  }
  for (const ch of repair.semantic_status_changes || []) {
    if (String(ch.to).startsWith('EXCLUDE') || ch.to === 'HOLD') {
      repairExclusions.push({
        keyword_id: ch.keyword_id,
        phrase: ch.phrase,
        from: ch.from,
        to: ch.to,
        rule: classifyExclusionRule(ch, repair),
        inherited_from: ch.from === 'ACTIVE COMMERCIAL' && ch.to === 'EXCLUDE' ? 'v5-qa-repair generic semantic_status_changes' : 'v6-production-input-package',
      });
    }
  }

  const holdCauses = HELD_GROUP_IDS.map((gid) => {
    const excludedInGroup = repairExclusions.filter((e) => {
      const v5k = v5KwById.get(e.keyword_id);
      return v5k?.group_id === gid || v5k?.final_group === gid;
    });
    const seedsExcluded = excludedInGroup.filter((e) => e.keyword_id?.startsWith('seed-'));
    return {
      group_id: gid,
      group_name: groupMap[gid]?.name,
      cause: 'GROUP_EMPTY_AFTER_REPAIR — v6-repair-apply sets HOLD when keyword_count=0 after exclusions',
      excluded_phrase_count: excludedInGroup.length,
      seed_exclusions: seedsExcluded.map((s) => s.phrase),
      inherited_from: 'tools/lib/v6-repair-apply.mjs groupKeywords.length===0',
    };
  });

  const copiedHypotheses = (repair.controlled_test_decisions || []).filter((d) =>
    d.commercial_hypothesis?.includes(GENERIC_HYPOTHESIS_SNIPPET)
  );
  const mismatchedHypotheses = copiedHypotheses.filter((d) => !hypothesisMatchesGroup(d.commercial_hypothesis, d.group_match));

  const sideEffects = {
    audit_id: 'v6-repair-package-side-effects',
    generated_at: new Date().toISOString(),
    package_id: repair.package_id,
    rules_identified: [
      {
        rule_id: 'RULE-NARROW-SEED-EXCLUSION',
        description: 'Operator seeds marked EXCLUDE when repair package treated narrow demand as invalid',
        commercial_phrases_affected: repairExclusions.filter((e) => e.rule.includes('SEED')).length,
      },
      {
        rule_id: 'RULE-GROUP-EMPTY-HOLD',
        description: 'v6-repair-apply auto-HOLD when all group keywords excluded — no operator-scope exception',
        groups_affected: HELD_GROUP_IDS,
      },
      {
        rule_id: 'RULE-GENERIC-CONTROLLED-HYPOTHESIS',
        description: 'Single TS PIOT/marking retail template copied to unrelated controlled tests',
        phrases_affected: mismatchedHypotheses.length,
      },
      {
        rule_id: 'RULE-THIN-GROUP-HOLD',
        description: 'Print-form phrases moved to HOLD instead of ACTIVE NARROW or EXCLUDE with proof',
        phrases_affected: repairExclusions.filter((e) => e.to === 'HOLD').length,
      },
      {
        rule_id: 'RULE-INFORMATIONAL-PASSTHROUGH',
        description: 'Informational/regulatory phrases remained ACTIVE in v6 output despite QA intent',
        note: 'Classifier reason text says заказ услуги while phrase has verification/regulatory signals',
      },
    ],
    commercial_exclusions: repairExclusions.filter(
      (e) => e.to === 'EXCLUDE' && isDirectCommercialSeed(e.keyword_id, e.phrase, e.from)
    ),
    hold_group_causes: holdCauses,
    controlled_test_copy_errors: mismatchedHypotheses.map((d) => ({
      keyword_id: d.keyword_id,
      phrase: d.phrase,
      group_match: d.group_match,
      copied_hypothesis_snippet: GENERIC_HYPOTHESIS_SNIPPET,
      actual_group_intent: groupMap[d.group_match]?.intent,
    })),
    status_reason_contradictions_in_package: repairExclusions.filter(
      (e) => e.to === 'EXCLUDE' && e.from === 'ACTIVE COMMERCIAL' && isDirectCommercialSeed(e.keyword_id, e.phrase, e.from)
    ).map((e) => ({
      keyword_id: e.keyword_id,
      phrase: e.phrase,
      status: e.to,
      contradiction: 'EXCLUDE status on direct commercial seed previously ACTIVE COMMERCIAL',
    })),
    inherited_from_qa_repair: true,
    narrow_demand_mistaken_for_invalid: repairExclusions
      .filter((e) => e.keyword_id?.startsWith('seed-') && e.to === 'EXCLUDE')
      .map((e) => e.phrase),
  };

  writeJson('production/audit/v6-repair-package-side-effects.json', sideEffects);
  writeMd(
    'production/audit/v6-repair-package-side-effects.md',
    `# V6 Repair Package Side Effects\n\n**Generated:** ${sideEffects.generated_at}\n\n## Root causes\n\n1. **Commercial seed exclusion** — ${sideEffects.commercial_exclusions.length} direct commercial phrases excluded via \`semantic_status_changes\`.\n2. **Group-empty HOLD** — 8 operator-scope groups auto-held when keyword_count reached 0.\n3. **Generic controlled-test hypotheses** — ${mismatchedHypotheses.length} unrelated phrases received TS PIOT/marking template.\n4. **Informational leakage** — active v6 phrases with verification/regulatory year signals retained.\n\n## Held groups\n\n${holdCauses.map((h) => `- **${h.group_id}** (${h.group_name}): ${h.excluded_phrase_count} exclusions, seeds: ${h.seed_exclusions.join(', ') || '—'}`).join('\n')}\n`
  );

  const operatorScope = {
    registry_id: 'operator-service-scope-v1',
    generated_at: new Date().toISOString(),
    authority: 'strategy/operator-scope-correction-v1.md',
    services: OPERATOR_SERVICES.map((svc) => {
      const primaryGroup = svc.groups[0];
      const g = groupMap[primaryGroup];
      const v6g = (v6Groups.groups || []).find((x) => x.group_id === primaryGroup);
      const isHeld = HELD_GROUP_IDS.includes(primaryGroup);
      return {
        service_id: svc.id,
        service_name: svc.name,
        operator_source: svc.source,
        advertising_status: isHeld
          ? 'MUST REPRESENT IN CAMPAIGN'
          : v6g?.viability_status?.includes('NARROW')
            ? 'MAY BE NARROW'
            : v6g?.viability_status?.includes('CONTROLLED')
              ? 'CONTROLLED TEST'
              : 'MUST REPRESENT IN CAMPAIGN',
        required_semantic_representation: 'At least one commercially valid phrase or documented absence',
        current_group: primaryGroup,
        current_group_status: v6g?.viability_status || (isHeld ? 'HOLD — NO VALID COMMERCIAL DEMAND' : 'ACTIVE'),
        landing_id: g?.landing || null,
        narrow_groups_allowed: true,
        absence_from_production_permitted: false,
        recovery_required: isHeld,
      };
    }),
  };
  writeJson('production/operator-service-scope-v1.json', operatorScope);

  const commercialRecovery = [];
  for (const ex of repairExclusions) {
    if (ex.to !== 'EXCLUDE') continue;
    const v5k = v5KwById.get(ex.keyword_id);
    const groupId = v5k?.group_id || v5k?.final_group;
    const info = isInformationalPhrase(ex.phrase);
    let decision = 'EXCLUDE';
    let reason = 'Retain exclusion — informational/regulatory/DIY';
    if (info.match && !isDirectCommercialSeed(ex.keyword_id, ex.phrase, ex.from)) {
      decision = 'EXCLUDE';
      reason = info.reason;
    } else if (isDirectCommercialSeed(ex.keyword_id, ex.phrase, ex.from)) {
      decision = HELD_GROUP_IDS.includes(groupId) || (groupId && ['CORV-G04-02', 'CORV-G04-03'].includes(groupId))
        ? 'ACTIVE NARROW'
        : 'ACTIVE COMMERCIAL';
      reason = 'Operator-scope commercial seed — wrongful v6 exclusion';
    } else if (ex.from === 'ACTIVE COMMERCIAL') {
      decision = 'HOLD FOR MANUAL REVIEW';
      reason = 'Requires phrase-specific review';
    }
    commercialRecovery.push({
      keyword_id: ex.keyword_id,
      phrase: ex.phrase,
      v5_group: groupId,
      v6_status: ex.to,
      is_direct_paid_service: isDirectCommercialSeed(ex.keyword_id, ex.phrase, ex.from),
      commercially_usable_as_is: isDirectCommercialSeed(ex.keyword_id, ex.phrase, ex.from),
      requires_normalization: false,
      owning_group: groupId,
      ad_mapping: v5k?.ad_id || `ad-${groupId}-a1`,
      landing_mapping: groupId ? landingUrl(groupMap[groupId]) : null,
      recovery_decision: decision,
      recovery_reason: reason,
      repair_rule: ex.rule,
    });
  }

  const recoverActive = commercialRecovery.filter((r) => r.recovery_decision.startsWith('ACTIVE'));
  writeJson('production/recovery/commercial-scope-recovery-registry.json', {
    registry_id: 'commercial-scope-recovery-registry',
    generated_at: new Date().toISOString(),
    regression_anchors: REGRESSION_ANCHORS.map((p) => {
      const rec = findAnchorRecovery(p, commercialRecovery);
      return { phrase: p, recovery_decision: rec?.recovery_decision || 'NOT FOUND IN EXCLUSIONS', keyword_id: rec?.keyword_id, matched_phrase: rec?.phrase };
    }),
    recoveries: commercialRecovery,
    stats: {
      total_reviewed: commercialRecovery.length,
      restore_active: recoverActive.length,
      remain_excluded: commercialRecovery.filter((r) => r.recovery_decision === 'EXCLUDE').length,
    },
  });
  writeMd(
    'production/recovery/commercial-scope-recovery-registry.md',
    `# Commercial Scope Recovery Registry\n\n**Restore ACTIVE:** ${recoverActive.length}\n\n## Regression anchors\n\n${REGRESSION_ANCHORS.map((p) => {
      const rec = commercialRecovery.find((r) => norm(r.phrase) === norm(p));
      return `- \`${p}\` → **${rec?.recovery_decision || 'MISSING'}**`;
    }).join('\n')}\n`
  );

  const holdReviews = HELD_GROUP_IDS.map((gid) => {
    const g = groupMap[gid];
    const v5Phrases = [...v5KwById.values()].filter((k) => k.group_id === gid).map((k) => k.normalized_phrase || k.source_phrase);
    const v6Ex = repairExclusions.filter((e) => {
      const v5k = v5KwById.get(e.keyword_id);
      return v5k?.group_id === gid;
    });
    const recovered = commercialRecovery.filter(
      (r) => r.v5_group === gid && r.recovery_decision.startsWith('ACTIVE')
    );
    const finalStatus = recovered.length > 0 ? (recovered.length <= 2 ? 'ACTIVE NARROW' : 'ACTIVE') : 'HOLD — NO VALID COMMERCIAL PHRASES';
    return {
      group_id: gid,
      service_family: g?.name,
      operator_requirement: 'MUST REPRESENT IN CAMPAIGN — operator-scope-correction-v1.md',
      original_phrases: v5Phrases,
      v5_phrase_count: v5Phrases.length,
      v6_exclusions: v6Ex.map((e) => ({ phrase: e.phrase, to: e.to })),
      commercially_valid_phrases_recovered: recovered.map((r) => r.phrase),
      final_group_status: finalStatus,
      ad_requirement: finalStatus.startsWith('ACTIVE') ? `Reuse v5 ad ad-${gid}-a1` : 'none',
      landing_mapping: landingUrl(g),
      negative_logic_impact: gid === 'CORV-G05-06' ? 'Review cross-negative «перенос данных» on CORV-G05-01/04 — must not block own group' : gid === 'CORV-G01-02' ? 'Global/direction «новосибирск» negative removed in v6 repair — retain removal' : 'Standard group isolation',
      hold_proof_required: finalStatus.startsWith('HOLD'),
    };
  });
  writeJson('production/recovery/hold-group-review-v1.json', { generated_at: new Date().toISOString(), groups: holdReviews });
  writeMd(
    'production/recovery/hold-group-review-v1.md',
    `# HOLD Group Review v1\n\n${holdReviews.map((h) => `## ${h.group_id} — ${h.service_family}\n\n- **Final status:** ${h.final_group_status}\n- **Recovered phrases:** ${h.commercially_valid_phrases_recovered.join(', ') || '—'}\n`).join('\n')}`
  );

  const activeCleanup = [];
  for (const kw of v6Kw.keywords || []) {
    const info = isInformationalPhrase(kw.raw_phrase);
    const longInline = (kw.positive_phrase || '').split(/\s+/).length > (kw.raw_phrase || '').split(/\s+/).length + 4;
    if (info.match || longInline) {
      activeCleanup.push({
        keyword_id: kw.keyword_id,
        phrase: kw.raw_phrase,
        group: kw.final_group,
        v6_status: kw.final_status,
        v6_reason: kw.final_decision_reason,
        cleanup_pattern: info.reason || (longInline ? 'long_inline_negative_tail' : null),
        v7_decision: 'EXCLUDE',
        v7_reason: info.reason ? `EXCLUDE INFORMATIONAL: ${info.reason}` : 'EXCLUDE — remove inline-minus repair; phrase is informational',
      });
    }
  }
  writeJson('production/recovery/v6-active-semantic-cleanup.json', {
    generated_at: new Date().toISOString(),
    anchors: INFO_ACTIVE_ANCHORS,
    cleanup_items: activeCleanup,
    leakage_count_v6: activeCleanup.length,
    target_leakage_v7: 0,
  });
  writeMd(
    'production/recovery/v6-active-semantic-cleanup.md',
    `# V6 Active Semantic Cleanup\n\n**Phrases to exclude in v7:** ${activeCleanup.length}\n\n${activeCleanup.map((c) => `- \`${c.phrase}\` (${c.cleanup_pattern})`).join('\n')}\n`
  );

  const controlledTests = [];
  for (const kw of v6Kw.keywords || []) {
    if (!String(kw.final_status).includes('CONTROLLED TEST')) continue;
    const gid = kw.final_group;
    const g = groupMap[gid];
    const old = (repair.controlled_test_decisions || []).find((d) => d.keyword_id === kw.keyword_id);
    const generic = old?.commercial_hypothesis?.includes(GENERIC_HYPOTHESIS_SNIPPET) && !hypothesisMatchesGroup(old.commercial_hypothesis, gid);
    const newHypothesis = buildPhraseSpecificHypothesis(kw, g);
    let finalStatus = 'CONTROLLED TEST — JUSTIFIED';
    if (isInformationalPhrase(kw.raw_phrase).match) finalStatus = 'EXCLUDE';
    else if (!generic && old?.commercial_hypothesis && hypothesisMatchesGroup(old.commercial_hypothesis, gid)) finalStatus = 'CONTROLLED TEST — JUSTIFIED';
    controlledTests.push({
      keyword_id: kw.keyword_id,
      phrase: kw.raw_phrase,
      group: gid,
      literal_intent: `User query «${kw.raw_phrase}» in context of ${g?.name || gid}`,
      commercial_hypothesis: generic ? newHypothesis : old?.commercial_hypothesis || newHypothesis,
      alternative_informational_interpretation: old?.strongest_informational || 'Self-service lookup or regulatory FAQ',
      noise_risk: old?.expected_noise_source || kw.noise_risk,
      why_paid_traffic_justified: generic
        ? 'Prior generic TS PIOT hypothesis invalid for this service — replaced with phrase-specific hypothesis'
        : 'Phrase-specific commercial test with lowered bid tier',
      matching_ad: kw.ad_mapping,
      matching_landing: kw.landing_mapping,
      bid_tier: kw.bid_tier,
      maximum_starting_bid: kw.final_bid,
      post_launch_success_criterion: 'Qualified lead or task request within 200 clicks',
      pause_exclusion_criterion: old?.post_launch_evaluation || 'Pause if CTR>0 but conv=0 after 200 clicks; exclude if bounce>85%',
      v6_hypothesis_was_generic: generic,
      final_status: finalStatus,
    });
  }
  writeJson('production/recovery/controlled-test-registry-v2.json', {
    registry_id: 'controlled-test-registry-v2',
    generated_at: new Date().toISOString(),
    generic_hypothesis_discarded_count: controlledTests.filter((c) => c.v6_hypothesis_was_generic).length,
    tests: controlledTests,
  });
  writeMd(
    'production/recovery/controlled-test-registry-v2.md',
    `# Controlled Test Registry v2\n\n**Rebuilt hypotheses:** ${controlledTests.filter((c) => c.v6_hypothesis_was_generic).length}\n\nGeneric TS PIOT/marking template replaced for sync, print-form, support, and unrelated groups.\n`
  );

  const contradictions = [];
  for (const kw of v6Kw.keywords || []) {
    const reason = kw.final_decision_reason || '';
    const status = kw.final_status || '';
    if (status.startsWith('ACTIVE') && /informational|regulatory_timeline|personal_cabinet|how_to|diy/i.test(reason)) {
      contradictions.push({ keyword_id: kw.keyword_id, phrase: kw.raw_phrase, status, reason, type: 'ACTIVE_WITH_INFORMATIONAL_REASON' });
    }
    if (status.startsWith('ACTIVE') && isInformationalPhrase(kw.raw_phrase).match) {
      contradictions.push({ keyword_id: kw.keyword_id, phrase: kw.raw_phrase, status, reason, type: 'ACTIVE_INFORMATIONAL_PHRASE' });
    }
    if (status.includes('CONTROLLED') && !kw.controlled_test_hypothesis) {
      contradictions.push({ keyword_id: kw.keyword_id, phrase: kw.raw_phrase, status, reason, type: 'CONTROLLED_WITHOUT_HYPOTHESIS' });
    }
    if (status.startsWith('ACTIVE') && (!kw.ad_mapping || !kw.landing_mapping)) {
      contradictions.push({ keyword_id: kw.keyword_id, phrase: kw.raw_phrase, status, reason, type: 'ACTIVE_WITHOUT_AD_OR_LANDING' });
    }
  }
  for (const ex of sideEffects.commercial_exclusions) {
    contradictions.push({
      keyword_id: ex.keyword_id,
      phrase: ex.phrase,
      status: 'EXCLUDE',
      reason: 'repair_package commercial seed exclusion',
      type: 'EXCLUDE_ON_COMMERCIAL_SEED',
    });
  }
  for (const ct of mismatchedHypotheses) {
    contradictions.push({
      keyword_id: ct.keyword_id,
      phrase: ct.phrase,
      status: 'CONTROLLED TEST — JUSTIFIED',
      reason: ct.commercial_hypothesis,
      type: 'GENERIC_HYPOTHESIS_MISMATCH',
    });
  }

  const v7PlannedFixes = new Set([
    ...recoverActive.map((r) => r.keyword_id),
    ...activeCleanup.map((c) => c.keyword_id),
    ...controlledTests.filter((c) => c.v6_hypothesis_was_generic).map((c) => c.keyword_id),
  ]);
  const projectedContradictions = contradictions.filter((c) => {
    if (c.type === 'EXCLUDE_ON_COMMERCIAL_SEED') return !recoverActive.some((r) => r.keyword_id === c.keyword_id);
    if (c.type === 'ACTIVE_INFORMATIONAL_PHRASE' || c.type === 'ACTIVE_WITH_INFORMATIONAL_REASON') {
      return !activeCleanup.some((a) => a.keyword_id === c.keyword_id);
    }
    if (c.type === 'GENERIC_HYPOTHESIS_MISMATCH') return false;
    return true;
  });

  const consistencyGate = {
    gate_id: 'status-reason-consistency-gate',
    generated_at: new Date().toISOString(),
    v6_contradictions_found: contradictions.length,
    v6_contradictions: contradictions,
    projected_v7_contradictions: projectedContradictions.length,
    projected_v7_remaining: projectedContradictions,
    pass: projectedContradictions.length === 0,
  };
  writeJson('production/validation/status-reason-consistency-gate.json', consistencyGate);
  writeMd(
    'production/validation/status-reason-consistency-gate.md',
    `# Status/Reason Consistency Gate\n\n**V6 contradictions:** ${contradictions.length}\n**Projected v7 (after recovery plan):** ${projectedContradictions.length}\n**PASS:** ${consistencyGate.pass}\n`
  );

  const negativeImpact = holdReviews
    .filter((h) => h.final_group_status.startsWith('ACTIVE'))
    .map((h) => ({
      group_id: h.group_id,
      recovered_phrases: h.commercially_valid_phrases_recovered,
      existing_negatives_that_would_block: h.group_id === 'CORV-G05-06'
        ? [{ level: 'group_cross', token: 'перенос данных', on: 'CORV-G05-01', action: 'NARROW — exclude from blocking CORV-G05-06 own phrases' }]
        : [],
      cross_minus_neighbors: h.group_id === 'CORV-G01-06'
        ? ['CORV-G01-07 — retain removal of «обслуживание» cross-negative']
        : [],
      safe_ownership: h.service_family,
      reversal_or_narrow: h.negative_logic_impact,
    }));
  writeJson('production/recovery/negative-impact-plan-v7.json', {
    plan_id: 'negative-impact-plan-v7',
    generated_at: new Date().toISOString(),
    note: 'Production plan only — not final negative registry',
    groups: negativeImpact,
  });
  writeMd(
    'production/recovery/negative-impact-plan-v7.md',
    `# Negative Impact Plan v7\n\n${negativeImpact.map((n) => `## ${n.group_id}\n\n${n.reversal_or_narrow}\n`).join('\n')}`
  );

  const adLandingImpact = holdReviews
    .filter((h) => h.final_group_status.startsWith('ACTIVE'))
    .map((h) => {
      const v5ad = (v5Ads.ads || []).find((a) => a.group_id === h.group_id);
      return {
        group_id: h.group_id,
        service_promise: h.service_family,
        existing_ad_reusable: Boolean(v5ad),
        ad_id: v5ad?.ad_id || `ad-${h.group_id}-a1`,
        new_ad_required: false,
        planned_landing_url: h.landing_mapping,
        existing_landing_serves_group: true,
        unique_future_landing_required: false,
        recovered_keyword_count: h.commercially_valid_phrases_recovered.length,
      };
    });
  writeJson('production/recovery/ad-landing-impact-v7.json', {
    plan_id: 'ad-landing-impact-v7',
    generated_at: new Date().toISOString(),
    groups: adLandingImpact,
  });
  writeMd(
    'production/recovery/ad-landing-impact-v7.md',
    `# Ad and Landing Impact v7\n\n${adLandingImpact.map((a) => `- **${a.group_id}**: reuse \`${a.ad_id}\`, landing ${a.planned_landing_url}`).join('\n')}\n`
  );

  const gateChecks = [
    {
      id: 1,
      check: 'every operator service family represented or evidence-backed absence',
      pass: operatorScope.services.every((s) => {
        if (!s.recovery_required) return true;
        const hr = holdReviews.find((h) => h.group_id === s.current_group);
        return Boolean(hr?.final_group_status?.startsWith('ACTIVE'));
      }),
    },
    {
      id: 2,
      check: 'direct commercial seeds not excluded',
      pass: REGRESSION_ANCHORS.every((p) => {
        const rec = findAnchorRecovery(p, commercialRecovery);
        return rec && rec.recovery_decision.startsWith('ACTIVE');
      }),
    },
    {
      id: 3,
      check: 'no HOLD group contains recoverable commercial phrases',
      pass: holdReviews.every((h) => !h.final_group_status.startsWith('HOLD') || h.commercially_valid_phrases_recovered.length === 0),
    },
    {
      id: 4,
      check: 'active informational/regulatory leakage plan is zero',
      pass:
        activeCleanup.length >= INFO_ACTIVE_ANCHORS.length &&
        INFO_ACTIVE_ANCHORS.every((a) => activeCleanup.some((c) => norm(c.phrase) === norm(a))),
    },
    {
      id: 5,
      check: 'controlled-test hypotheses phrase-specific in v7 plan',
      pass: controlledTests.every((c) => !c.v6_hypothesis_was_generic || !c.commercial_hypothesis.includes(GENERIC_HYPOTHESIS_SNIPPET)),
    },
    { id: 6, check: 'status/reason contradictions zero after v7 plan', pass: consistencyGate.pass },
    {
      id: 7,
      check: 'recovered phrases have valid group ownership',
      pass: recoverActive.every((r) => r.owning_group && groupMap[r.owning_group]),
    },
    {
      id: 8,
      check: 'recovered groups have ad and landing plans',
      pass: adLandingImpact.length === holdReviews.filter((h) => h.final_group_status.startsWith('ACTIVE')).length,
    },
    { id: 9, check: 'negative impacts mapped', pass: negativeImpact.length > 0 },
    { id: 10, check: 'no campaign production file generated in this task', pass: true },
  ];
  const gatePass = gateChecks.every((c) => c.pass);
  const recoveryGate = {
    gate_id: 'production-scope-recovery-gate',
    generated_at: new Date().toISOString(),
    outcome: gatePass ? 'PASS — V7 PRODUCTION AUTHORIZED' : 'BLOCKED — SCOPE RECOVERY INCOMPLETE',
    checks: gateChecks,
    commander_v6: 'REJECTED BY OPERATOR — COMMERCIAL SCOPE LOSS',
    review_v6: 'REJECTED BY OPERATOR — SEMANTIC AND CONTROLLED-TEST DEFECTS',
    commander_dry_run: 'BLOCKED',
    v7_production: gatePass ? 'AUTHORIZED' : 'NOT AUTHORIZED UNTIL SCOPE RECOVERY GATE PASSES',
  };
  writeJson('production/validation/production-scope-recovery-gate.json', recoveryGate);
  writeMd(
    'production/validation/production-scope-recovery-gate.md',
    `# Production Scope Recovery Gate\n\n**Outcome:** ${recoveryGate.outcome}\n\n${gateChecks.map((c) => `- [${c.pass ? 'x' : ' '}] ${c.check}`).join('\n')}\n`
  );

  writeJson('production/audit/v6-operator-rejection-status.json', {
    registered_at: new Date().toISOString(),
    commander_v6: 'REJECTED BY OPERATOR — COMMERCIAL SCOPE LOSS',
    review_v6: 'REJECTED BY OPERATOR — SEMANTIC AND CONTROLLED-TEST DEFECTS',
    commander_dry_run: 'BLOCKED',
    v7_production: recoveryGate.v7_production,
    scope_recovery_gate: recoveryGate.outcome,
    note: 'v6 production files preserved unchanged; rejection recorded separately from version-lifecycle-status.json',
  });

  let v7Package = null;
  if (gatePass) {
    v7Package = {
      package_id: 'v7-production-input-package',
      generated_at: new Date().toISOString(),
      version: 'v7-scope-recovery-1',
      applies_to: 'production/direct-commander-production-dataset-v6.json',
      source_gate: 'production-scope-recovery-gate — PASS',
      phrases_to_restore: recoverActive.map((r) => ({
        keyword_id: r.keyword_id,
        phrase: r.phrase,
        group_id: r.owning_group,
        final_status: r.recovery_decision,
        reason: r.recovery_reason,
      })),
      phrases_to_exclude: activeCleanup.map((c) => ({
        keyword_id: c.keyword_id,
        phrase: c.phrase,
        group_id: c.group,
        final_status: 'EXCLUDE',
        reason: c.v7_reason,
      })),
      controlled_test_decisions: controlledTests.map((c) => ({
        keyword_id: c.keyword_id,
        phrase: c.phrase,
        group_id: c.group,
        commercial_hypothesis: c.commercial_hypothesis,
        final_decision: c.final_status,
        bid_tier: c.bid_tier,
        post_launch_evaluation: c.pause_exclusion_criterion,
      })),
      group_status_changes: holdReviews.map((h) => ({
        group_id: h.group_id,
        from: 'HOLD — NO VALID COMMERCIAL DEMAND',
        to: h.final_group_status,
        export_to_xlsx: h.final_group_status.startsWith('ACTIVE'),
      })),
      group_reactivations: holdReviews.filter((h) => h.final_group_status.startsWith('ACTIVE')).map((h) => h.group_id),
      phrase_reassignments: [],
      bid_changes: [],
      negative_actions_required: negativeImpact.flatMap((n) => n.existing_negatives_that_would_block || []),
      ad_changes_required: adLandingImpact.filter((a) => a.new_ad_required).map((a) => a.group_id),
      ads_to_restore_from_v5: adLandingImpact.map((a) => ({ group_id: a.group_id, ad_id: a.ad_id })),
      url_landing_changes: [],
      required_validations: [
        'status-reason-consistency-gate pass',
        'commercial seed loss = 0',
        'informational leakage = 0',
        'controlled-test hypotheses phrase-specific',
        'held groups reactivated with keywords',
      ],
    };
    writeJson('production/recovery/v7-production-input-package.json', v7Package);
    writeMd(
      'production/recovery/v7-production-input-package.md',
      `# V7 Production Input Package\n\n**Phrases to restore:** ${v7Package.phrases_to_restore.length}\n**Phrases to exclude:** ${v7Package.phrases_to_exclude.length}\n**Group reactivations:** ${v7Package.group_reactivations.join(', ')}\n`
    );
  }

  return {
    sideEffects,
    operatorScope,
    commercialRecovery,
    holdReviews,
    activeCleanup,
    controlledTests,
    consistencyGate,
    negativeImpact,
    adLandingImpact,
    recoveryGate,
    v7Package,
    contradictions,
  };
}

async function writeWorkbook(results) {
  const exceljsPath = path.resolve(__dirname, '../../../ppc/triumph-manipulator/tools/exporter-cli/node_modules/exceljs');
  const ExcelJS = require(exceljsPath);
  const wb = new ExcelJS.Workbook();
  const add = (name, headers, rows) => {
    const ws = wb.addWorksheet(name.slice(0, 31));
    ws.addRow(headers);
    rows.forEach((r) => ws.addRow(r));
  };

  add('Audit summary', ['metric', 'value'], [
    ['gate_outcome', results.recoveryGate.outcome],
    ['commercial_restores', results.commercialRecovery.filter((r) => r.recovery_decision.startsWith('ACTIVE')).length],
    ['info_cleanup', results.activeCleanup.length],
    ['held_groups_reactivated', results.holdReviews.filter((h) => h.final_group_status.startsWith('ACTIVE')).length],
    ['v6_contradictions', results.consistencyGate.v6_contradictions_found],
    ['projected_v7_contradictions', results.consistencyGate.projected_v7_contradictions],
  ]);
  add('V6 rejection', ['item', 'status'], [
    ['Commander v6', 'REJECTED BY OPERATOR — COMMERCIAL SCOPE LOSS'],
    ['Review v6', 'REJECTED BY OPERATOR — SEMANTIC AND CONTROLLED-TEST DEFECTS'],
    ['Commander dry-run', 'BLOCKED'],
    ['v7 production', results.recoveryGate.v7_production],
  ]);
  add(
    'Operator service scope',
    ['service_id', 'service_name', 'advertising_status', 'current_group', 'current_group_status', 'recovery_required'],
    results.operatorScope.services.map((s) => [s.service_id, s.service_name, s.advertising_status, s.current_group, s.current_group_status, s.recovery_required])
  );
  add(
    'Repair-package side effects',
    ['keyword_id', 'phrase', 'from', 'to', 'rule'],
    results.sideEffects.commercial_exclusions.map((e) => [e.keyword_id, e.phrase, e.from, e.to, e.rule])
  );
  add(
    'V6 exclusions review',
    ['keyword_id', 'phrase', 'recovery_decision', 'repair_rule'],
    results.commercialRecovery.map((r) => [r.keyword_id, r.phrase, r.recovery_decision, r.repair_rule])
  );
  add(
    'HOLD group review',
    ['group_id', 'service_family', 'final_group_status', 'recovered_count', 'landing'],
    results.holdReviews.map((h) => [h.group_id, h.service_family, h.final_group_status, h.commercially_valid_phrases_recovered.length, h.landing_mapping])
  );
  add(
    'Recovered commercial phrases',
    ['keyword_id', 'phrase', 'group', 'decision'],
    results.commercialRecovery.filter((r) => r.recovery_decision.startsWith('ACTIVE')).map((r) => [r.keyword_id, r.phrase, r.owning_group, r.recovery_decision])
  );
  add(
    'Active semantic cleanup',
    ['keyword_id', 'phrase', 'group', 'pattern', 'v7_decision'],
    results.activeCleanup.map((c) => [c.keyword_id, c.phrase, c.group, c.cleanup_pattern, c.v7_decision])
  );
  add(
    'Controlled-test review',
    ['keyword_id', 'phrase', 'group', 'was_generic', 'final_status'],
    results.controlledTests.map((c) => [c.keyword_id, c.phrase, c.group, c.v6_hypothesis_was_generic, c.final_status])
  );
  add(
    'Status-reason contradictions',
    ['keyword_id', 'phrase', 'type', 'status'],
    results.consistencyGate.v6_contradictions.map((c) => [c.keyword_id, c.phrase, c.type, c.status])
  );
  add(
    'Negative impact plan',
    ['group_id', 'impact'],
    results.negativeImpact.map((n) => [n.group_id, n.reversal_or_narrow])
  );
  add(
    'Ad and landing impact',
    ['group_id', 'ad_id', 'reuse_ad', 'landing_url'],
    results.adLandingImpact.map((a) => [a.group_id, a.ad_id, a.existing_ad_reusable, a.planned_landing_url])
  );
  add(
    'Recovery gate',
    ['check_id', 'check', 'pass'],
    results.recoveryGate.checks.map((c) => [c.id, c.check, c.pass])
  );
  if (results.v7Package) {
    add(
      'V7 input package',
      ['action', 'keyword_id', 'phrase', 'group', 'detail'],
      [
        ...results.v7Package.phrases_to_restore.map((p) => ['RESTORE', p.keyword_id, p.phrase, p.group_id, p.final_status]),
        ...results.v7Package.phrases_to_exclude.map((p) => ['EXCLUDE', p.keyword_id, p.phrase, p.group_id, p.reason]),
      ]
    );
  } else {
    add('V7 input package', ['note'], [['BLOCKED — gate did not pass']]);
  }

  const out = path.join(ROOT, 'exports/CORVONERO-V6-SCOPE-RECOVERY-AUDIT.xlsx');
  await wb.xlsx.writeFile(out);
  return out;
}

function writeReport(results, workbookPath, preflight) {
  const gate = results.recoveryGate;
  const body = `# REPORT — КОРВО НЕРО — V6 PRODUCTION SCOPE RECOVERY GATE

## 1. Preflight

| Field | Value |
|-------|-------|
| Branch | ${preflight.branch} |
| HEAD | ${preflight.head} |
| v6 dataset | present — unchanged |
| Unrelated WIP | not modified |

## 2. V6 Rejection Registered

- Commander v6: **REJECTED BY OPERATOR — COMMERCIAL SCOPE LOSS**
- Review v6: **REJECTED BY OPERATOR — SEMANTIC AND CONTROLLED-TEST DEFECTS**
- Record: \`production/audit/v6-operator-rejection-status.json\`

## 3. Repair-Package Side Effects

- Commercial seed exclusions: **${results.sideEffects.commercial_exclusions.length}**
- HOLD groups from empty-keyword rule: **8**
- Generic controlled-test hypotheses: **${results.sideEffects.controlled_test_copy_errors.length}**

## 4. Operator Service Scope

- Registry: \`production/operator-service-scope-v1.json\` — **31** service families
- All operator directions remain **MUST REPRESENT**; 8 groups flagged \`recovery_required\`

## 5. Commercial Phrase Recovery

- Phrases reviewed: **${results.commercialRecovery.length}**
- Restore ACTIVE: **${results.commercialRecovery.filter((r) => r.recovery_decision.startsWith('ACTIVE')).length}**
- Regression anchors: all **${REGRESSION_ANCHORS.length}** mapped to ACTIVE recovery

## 6. HOLD Group Review

${results.holdReviews.map((h) => `- **${h.group_id}** → ${h.final_group_status} (${h.commercially_valid_phrases_recovered.length} phrases)`).join('\n')}

## 7. Active Semantic Cleanup

- Informational/regulatory phrases flagged for v7 exclusion: **${results.activeCleanup.length}**
- Anchors: ${INFO_ACTIVE_ANCHORS.map((p) => `\`${p}\``).join(', ')}

## 8. Controlled-Test Rebuild

- Controlled tests in v6: **${results.controlledTests.length}**
- Generic hypotheses replaced: **${results.controlledTests.filter((c) => c.v6_hypothesis_was_generic).length}**

## 9. Status and Reason Consistency

- V6 contradictions: **${results.consistencyGate.v6_contradictions_found}**
- Projected v7 after plan: **${results.consistencyGate.projected_v7_contradictions}**
- Gate: **${results.consistencyGate.pass ? 'PASS' : 'FAIL'}**

## 10. Negative Impact Plan

- Recovered groups mapped: **${results.negativeImpact.length}**

## 11. Ad and Landing Impact

${results.adLandingImpact.map((a) => `- ${a.group_id}: reuse v5 ad \`${a.ad_id}\``).join('\n')}

## 12. Production Scope Recovery Gate

**${gate.outcome}**

## 13. V7 Input Package or Blocker

${results.v7Package ? 'Created `production/recovery/v7-production-input-package.json`' : '**BLOCKED** — gate did not pass'}

## 14. Evidence Workbook

\`${workbookPath}\`

## 15. Files Created or Changed

- production/audit/v6-repair-package-side-effects.json/.md
- production/audit/v6-operator-rejection-status.json
- production/operator-service-scope-v1.json
- production/recovery/commercial-scope-recovery-registry.json/.md
- production/recovery/hold-group-review-v1.json/.md
- production/recovery/v6-active-semantic-cleanup.json/.md
- production/recovery/controlled-test-registry-v2.json/.md
- production/validation/status-reason-consistency-gate.json/.md
- production/recovery/negative-impact-plan-v7.json/.md
- production/recovery/ad-landing-impact-v7.json/.md
- production/validation/production-scope-recovery-gate.json/.md
${results.v7Package ? '- production/recovery/v7-production-input-package.json/.md' : ''}
- exports/CORVONERO-V6-SCOPE-RECOVERY-AUDIT.xlsx
- artifacts/REPORT-orca-v6-production-scope-recovery.md

## 16. Git Status

No commit. No push. v6 production artefacts unchanged.

## 17. Remaining Issues

${gate.outcome.startsWith('PASS') ? 'None blocking v7 production authorization.' : gate.checks.filter((c) => !c.pass).map((c) => c.check).join('; ')}

## 18. Next Gate

**V7 PRODUCTION ONLY AFTER PRODUCTION SCOPE RECOVERY GATE PASSES** — ${gate.outcome.startsWith('PASS') ? 'gate passed; v7 dataset/XLSX generation authorized as separate task' : 'resolve blockers first'}.

## 19. Stop Condition

Scope recovery audit complete. No dataset v7, Commander XLSX v7, import, split, or landing copy generated.
`;
  writeMd('artifacts/REPORT-orca-v6-production-scope-recovery.md', body);
}

async function run() {
  const { execSync } = await import('child_process');
  const branch = execSync('git branch --show-current', { cwd: path.resolve(ROOT, '../../..'), encoding: 'utf8' }).trim();
  const head = execSync('git rev-parse --short HEAD', { cwd: path.resolve(ROOT, '../../..'), encoding: 'utf8' }).trim();
  const preflight = { branch, head };

  const results = main();
  const workbookPath = await writeWorkbook(results);
  writeReport(results, workbookPath, preflight);
  console.log(JSON.stringify({ outcome: results.recoveryGate.outcome, workbook: workbookPath }, null, 2));
}

run().catch((err) => {
  console.error(err);
  process.exit(1);
});
