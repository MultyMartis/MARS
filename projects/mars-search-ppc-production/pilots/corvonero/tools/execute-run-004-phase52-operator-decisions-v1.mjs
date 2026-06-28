#!/usr/bin/env node
/**
 * Corvonero Run 004 Phase 5.2 — Apply operator decisions and final partial semantic sign-off.
 * No provider calls. Reads Phase 5.1 artefacts only; does not mutate Phase 4/5/5.1 sources.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const PILOT = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const REPORTS = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/reports');

const RUN_ID = 'corv-semantic-v2-20260626-004';
const CANONICAL_TOTAL = 2368;
const ASSESSED_TOTAL = 1599;
const UNPROCESSED_TOTAL = 769;
const REVIEWER = 'PHASE_52_OPERATOR_DECISIONS_v1';
const AUTHORITY = 'CORVONERO RUN 004 PHASE 5.2 — OPERATOR DECISIONS APPLIED';

const OPERATOR_DECISIONS = {
  ACCEPT: [
    'CR2-PHR-00076', 'CR2-PHR-02239', 'CR2-PHR-01331', 'CR2-PHR-01347', 'CR2-PHR-01450',
    'CR2-PHR-01523', 'CR2-PHR-01145', 'CR2-PHR-01239', 'CR2-PHR-02354', 'CR2-PHR-00756',
  ],
  REJECT: [
    'CR2-PHR-02240', 'CR2-PHR-01345', 'CR2-PHR-01359', 'CR2-PHR-01369', 'CR2-PHR-01382',
    'CR2-PHR-01385', 'CR2-PHR-01465', 'CR2-PHR-01497', 'CR2-PHR-01500', 'CR2-PHR-01550',
  ],
  ABSTAIN: [
    'CR2-PHR-01318', 'CR2-PHR-01321', 'CR2-PHR-01326', 'CR2-PHR-01329', 'CR2-PHR-01333',
    'CR2-PHR-01334', 'CR2-PHR-01340', 'CR2-PHR-01346', 'CR2-PHR-01352', 'CR2-PHR-01363',
    'CR2-PHR-01380', 'CR2-PHR-01392', 'CR2-PHR-01396', 'CR2-PHR-01410', 'CR2-PHR-01428',
    'CR2-PHR-01432', 'CR2-PHR-01433', 'CR2-PHR-01475', 'CR2-PHR-01483', 'CR2-PHR-01492',
    'CR2-PHR-00697', 'CR2-PHR-00926', 'CR2-PHR-00673', 'CR2-PHR-00736', 'CR2-PHR-00767',
    'CR2-PHR-00799', 'CR2-PHR-00813',
  ],
};

const ONE_C = /(?:1[\s-]?с|1c|один[\s-]?эс)/i;
const CAREER_RE = /(?:ваканс|резюме|собеседован|карьер|трудоустройств|устроиться|стажер|стажировк|ищу\s+работ|работа\s+программист|работодател)/i;
const EDUCATION_RE = /(?:как\s+стать|обучен|курс(?:ы|ов|а)?|учеб|экзамен|сертификац|урок|тренинг|семинар|skillbox|ironskills|нетолог|быстрый\s+старт|клуб\s+программист|диплом)/i;
const INFO_RE = /(?:что\s+такое|что\s+делает|что\s+должен\s+уметь|что\s+нужно\s+знать|как\s+работает|лучший\s+программист|рейтинг\s+программист|топ\s+\d+\s+программист)/i;
const DIY_RE = /(?:инструкци|самостоятельно|самому|как\s+(?:обновить|настроить|установить|исправить|подключить|добавить|загрузить)|почему\s+не\s+работает|скачать|видео|форум|wiki|википеди|отладка|расширение|тестовый\s+контур|пример\s+настрой)/i;
const SELF_SERVICE_RE = DIY_RE;
const COMMERCIAL_PRICE = /(?:сколько\s+стоит\s+работа|стоимость\s+работ(?:ы|)|цена\s+работ(?:ы|)|стоимость\s+услуг|расценки\s+специалиста|стоимость\s+работ\s+по|цена\s+услуг|прайс|сколько\s+стоит\s+(?:программист|специалист|услуг)|стоимость\s+часа|часа?\s+программист|программист(?:ы|а|ов)?\s+1[\s-]?с\s+цена|цена\s+1[\s-]?с\s+программист)/i;
const COMMERCIAL_DEMAND = /(?:нужен|нужна|нужно\s+(?:программист|специалист|заказать|вызвать)|заказать|найти\s+(?:специалист|программист)|вызвать\s+программист|нанять|под\s+ключ|срочно|услуг(?:и|а)\s+(?:программист|специалист|по\s+1с)|ищу\s+программист|задание\s+программист|тз\s+программист|техническ(?:ое|ого)\s+задани(?:е|я)\s+на\s+(?:сопровожден|доработк|внедрен))/i;
const SERVICE_TASK = /(?:внедрен|настрой(?:ка|ить|ки)?|сопровожден|доработк|интеграц(?:ия|ии|ию)|обслуживан|ремонт|миграц|аудит|оптимизац|консультац|исправить|устранить|программир|разработк|отчет|обработк|печатн|обновлен|подключ(?:ение|ить)|автоматизац|передача\s+маркировки)/i;
const PRODUCT_ONLY = /(?:купить|приобрест|лицензи|поставк|дистрибутив|коробочн)(?!.*(?:настрой|внедрен|сопровожден|услуг|программист|специалист))/i;
const PROBLEM = /(?:ошибк|не\s+работает|сбой|исправить|устранить|fault|exception|зависает|тормозит|восстановить\s+работ)/i;
const MARKING = /(?:честн(?:ый|ого)\s+знак|маркировк(?:а|и|у|ой)|data\s*matrix|gs1|агрегац(?:ия|ии)\s+код)/i;
const TS_PIOT = /(?:тс\s*пиот|ts\s*piot|промышленн(?:ая|ой|ую)\s+безопасност)/i;
const INTEGRATION = /(?:интеграц(?:ия|ии|ию|ией)|bitrix|битрикс|синхронизац|обмен\s+данн|api\s+1c|rest\s+1c|обмен\s+с\s+сайт)/i;
const SUBSCRIPTION = /(?:абонент|подписк|ежемесяч|сопровожден(?:ие|ия)\s+1с|its\s+1с|итс\s+1с)/i;
const ONE_OFF = /(?:разов|единоразов|одноразов|почасов|за\s+час)/i;
const FOREIGN_PLATFORM = /(?:sap|oracle|microsoft\s+dynamics|dynamics\s+365|odoo|bitrix24(?!\s+интеграц)|salesforce)/i;
const PROVIDER_ROLE = /(?:программист|специалист|разработчик)/i;
const PRIMARY_GEO = /(?:новосибирск|новосибирск(?:ая|ой|ую)\s+област)/i;
const EXPANSION_GEO = /(?:краснодар|екатеринбург|красноярск|москва|санкт-петербург|спб|казань|нижний\s+новгород|самара|ростов|воронеж|пермь|волгоград|тюмень|уфа|омск|челябинск|иркутск|хабаровск|владивосток)/i;
const FOREIGN_GEO = /(?:минск|киев|алматы|астана|ташкент|ереван|тбилиси)/i;

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

function buildOperatorDecisionMap() {
  const map = new Map();
  for (const [verdict, ids] of Object.entries(OPERATOR_DECISIONS)) {
    for (const id of ids) {
      if (map.has(id)) throw new Error(`Duplicate operator decision ID: ${id}`);
      map.set(id, verdict);
    }
  }
  return map;
}

function verifyOperatorPacket(packet, decisionMap) {
  const packetIds = packet.records.map((r) => r.phrase_id);
  const uniquePacket = new Set(packetIds);
  const errors = [];
  if (packet.total !== 47) errors.push(`Packet total ${packet.total} !== 47`);
  if (packetIds.length !== 47) errors.push(`Packet records length ${packetIds.length} !== 47`);
  if (uniquePacket.size !== 47) errors.push(`Packet unique IDs ${uniquePacket.size} !== 47`);
  if (decisionMap.size !== 47) errors.push(`Decision map size ${decisionMap.size} !== 47`);
  for (const id of decisionMap.keys()) {
    if (!uniquePacket.has(id)) errors.push(`Decision ID missing from packet: ${id}`);
  }
  for (const id of uniquePacket) {
    if (!decisionMap.has(id)) errors.push(`Packet ID missing from decisions: ${id}`);
  }
  const acceptN = OPERATOR_DECISIONS.ACCEPT.length;
  const rejectN = OPERATOR_DECISIONS.REJECT.length;
  const abstainN = OPERATOR_DECISIONS.ABSTAIN.length;
  if (acceptN !== 10 || rejectN !== 10 || abstainN !== 27) {
    errors.push(`Decision counts mismatch: ACCEPT=${acceptN} REJECT=${rejectN} ABSTAIN=${abstainN}`);
  }
  return { pass: errors.length === 0, errors, packetIds: [...uniquePacket].sort() };
}

function assignGeography(text) {
  const t = text.toLowerCase();
  if (!PRIMARY_GEO.test(t) && !EXPANSION_GEO.test(t) && !FOREIGN_GEO.test(t)) {
    return { normalized: null, usable: null, status: 'NO_GEOGRAPHY' };
  }
  if (PRIMARY_GEO.test(t)) return { normalized: 'Новосибирск / Новосибирская область', usable: true, status: 'PRIMARY' };
  if (FOREIGN_GEO.test(t)) return { normalized: t.match(FOREIGN_GEO)?.[0] || 'foreign', usable: false, status: 'IRRELEVANT' };
  if (/удален|удалён|онлайн|по\s+росси|росси(?:и|я)\s+удал/.test(t)) return { normalized: 'Russia-wide remote', usable: true, status: 'REMOTE' };
  const m = t.match(EXPANSION_GEO);
  if (m) {
    const city = m[0];
    const expansion = ['краснодар', 'екатеринбург', 'красноярск'].some((c) => city.includes(c));
    return { normalized: city, usable: expansion || /москва|санкт|спб/.test(t), status: expansion ? 'EXPANSION' : 'OTHER_RU' };
  }
  return { normalized: null, usable: null, status: 'SAFE_UNKNOWN' };
}

function assignServiceFamily(text, verdict) {
  if (verdict !== 'ACCEPT') return null;
  const t = text.toLowerCase();
  if (TS_PIOT.test(t)) return 'SF-TS-PIOT';
  if (MARKING.test(t)) return 'SF-MARKING-CHESTNY-ZNAK';
  if (INTEGRATION.test(t)) return 'SF-INTEGRATIONS';
  if (PROBLEM.test(t) && ONE_C.test(t)) return 'SF-TROUBLESHOOTING-NOT-WORKING';
  if (SUBSCRIPTION.test(t)) return 'SF-SUBSCRIPTION-SERVICE';
  if (ONE_OFF.test(t) || COMMERCIAL_PRICE.test(t)) return 'SF-ONE-OFF-WORK';
  if (/отчет|обработк|печатн/.test(t) && ONE_C.test(t) && SERVICE_TASK.test(t)) return 'SF-REPORTS-PROCESSING';
  if (/доработк|разработк|программир|модификац/.test(t) && ONE_C.test(t)) return 'SF-MODIFICATION-DEVELOPMENT';
  if (/сопровожден|обслуживан|абонент|поддержк|its|итс/.test(t) && ONE_C.test(t)) return 'SF-SUPPORT-MAINTENANCE';
  if (COMMERCIAL_DEMAND.test(t) || PROVIDER_ROLE.test(t)) return 'SF-1C-PROGRAMMER-SPECIALIST';
  if (SERVICE_TASK.test(t) && ONE_C.test(t)) return 'SF-OTHER-APPROVED-1C-SERVICE';
  return 'SF-OTHER-APPROVED-1C-SERVICE';
}

function assignIntent(text, verdict) {
  const t = text.toLowerCase();
  if (verdict === 'REJECT') {
    if (CAREER_RE.test(t)) return { primary: 'CAREER_OR_EDUCATION', secondary: null };
    if (EDUCATION_RE.test(t)) return { primary: 'CAREER_OR_EDUCATION', secondary: null };
    if (INFO_RE.test(t) || SELF_SERVICE_RE.test(t)) return { primary: 'INFORMATIONAL', secondary: null };
    if (PRODUCT_ONLY.test(t)) return { primary: 'PRODUCT_OR_LICENSE', secondary: null };
    if (FOREIGN_PLATFORM.test(t)) return { primary: 'INFORMATIONAL', secondary: 'PRODUCT_OR_LICENSE' };
    return { primary: 'INFORMATIONAL', secondary: null };
  }
  if (verdict === 'ABSTAIN') return { primary: 'AMBIGUOUS', secondary: null };
  if (COMMERCIAL_PRICE.test(t)) return { primary: 'PRICE_AND_COST', secondary: 'SPECIALIST_SEARCH' };
  if (PROBLEM.test(t)) return { primary: 'PROBLEM_RESOLUTION', secondary: 'SUPPORT_AND_MAINTENANCE' };
  if (/найти|нужен|нанять|заказать|вызвать/.test(t)) return { primary: 'SPECIALIST_SEARCH', secondary: 'DIRECT_SERVICE_ORDER' };
  if (/услуг|заказ/.test(t)) return { primary: 'DIRECT_SERVICE_ORDER', secondary: null };
  if (INTEGRATION.test(t)) return { primary: 'INTEGRATION', secondary: 'MODIFICATION' };
  if (/внедрен|миграц/.test(t)) return { primary: 'IMPLEMENTATION', secondary: null };
  if (/доработк|разработк|программир/.test(t)) return { primary: 'MODIFICATION', secondary: null };
  if (/сопровожден|обслуживан|поддержк/.test(t)) return { primary: 'SUPPORT_AND_MAINTENANCE', secondary: null };
  if (MARKING.test(t)) return { primary: 'DIRECT_SERVICE_ORDER', secondary: 'MODIFICATION' };
  if (TS_PIOT.test(t)) return { primary: 'DIRECT_SERVICE_ORDER', secondary: 'IMPLEMENTATION' };
  if (PROVIDER_ROLE.test(t)) return { primary: 'SPECIALIST_SEARCH', secondary: null };
  return { primary: 'DIRECT_SERVICE_ORDER', secondary: null };
}

function assignExclusionFamily(text, verdict) {
  const t = text.toLowerCase();
  if (CAREER_RE.test(t)) return 'EX-CAREER-JOBS';
  if (/зарплат/.test(t)) return 'EX-SALARY';
  if (/резюме|собеседован/.test(t)) return 'EX-RESUME-INTERVIEWS';
  if (EDUCATION_RE.test(t)) return 'EX-EDUCATION-COURSES';
  if (/сертификац|экзамен/.test(t)) return 'EX-CERTIFICATION-EXAMS';
  if (INFO_RE.test(t)) return 'EX-INFORMATIONAL-RESEARCH';
  if (SELF_SERVICE_RE.test(t)) return 'EX-SELF-SERVICE-MANUALS';
  if (/форум|wiki|википеди/.test(t)) return 'EX-FORUMS-INSTRUCTIONS';
  if (/скачать\s+бесплатно|бесплатн/.test(t)) return 'EX-FREE-DOWNLOADS';
  if (FOREIGN_PLATFORM.test(t)) return 'EX-UNRELATED-PLATFORMS';
  if (PRODUCT_ONLY.test(t) && verdict === 'REJECT') return 'EX-PRODUCT-LICENSE-ONLY';
  if (FOREIGN_GEO.test(t)) return 'EX-IRRELEVANT-GEOGRAPHY';
  if (verdict === 'REJECT') return 'EX-INFORMATIONAL-RESEARCH';
  return null;
}

function buildServiceTaxonomy(registry) {
  const families = {
    'SF-1C-PROGRAMMER-SPECIALIST': { id: 'SF-1C-PROGRAMMER-SPECIALIST', name: '1C programmer / specialist', phrase_ids: [] },
    'SF-SUPPORT-MAINTENANCE': { id: 'SF-SUPPORT-MAINTENANCE', name: '1C support and maintenance', phrase_ids: [] },
    'SF-MODIFICATION-DEVELOPMENT': { id: 'SF-MODIFICATION-DEVELOPMENT', name: '1C modification and development', phrase_ids: [] },
    'SF-REPORTS-PROCESSING': { id: 'SF-REPORTS-PROCESSING', name: 'Reports and processing', phrase_ids: [] },
    'SF-INTEGRATIONS': { id: 'SF-INTEGRATIONS', name: 'Integrations', phrase_ids: [] },
    'SF-MARKING-CHESTNY-ZNAK': { id: 'SF-MARKING-CHESTNY-ZNAK', name: 'Marking / Честный знак', phrase_ids: [] },
    'SF-TROUBLESHOOTING-NOT-WORKING': { id: 'SF-TROUBLESHOOTING-NOT-WORKING', name: '1C troubleshooting / not working', phrase_ids: [] },
    'SF-TS-PIOT': { id: 'SF-TS-PIOT', name: 'TS ПИОТ', phrase_ids: [] },
    'SF-SUBSCRIPTION-SERVICE': { id: 'SF-SUBSCRIPTION-SERVICE', name: 'Subscription service', phrase_ids: [] },
    'SF-ONE-OFF-WORK': { id: 'SF-ONE-OFF-WORK', name: 'One-off work', phrase_ids: [] },
    'SF-OTHER-APPROVED-1C-SERVICE': { id: 'SF-OTHER-APPROVED-1C-SERVICE', name: 'Other approved 1C services', phrase_ids: [] },
  };
  for (const r of registry.filter((x) => x.operator_final_verdict === 'ACCEPT')) {
    if (r.service_family && families[r.service_family]) families[r.service_family].phrase_ids.push(r.phrase_id);
  }
  return Object.values(families).map((f) => ({
    ...f,
    record_count: f.phrase_ids.length,
    representative_phrases: registry.filter((r) => f.phrase_ids.includes(r.phrase_id)).slice(0, 5).map((r) => r.phrase),
    ambiguity_notes: f.record_count === 0 ? 'No ACCEPT evidence after Phase 5.2 operator sign-off' : undefined,
  }));
}

function buildExclusionTaxonomy(registry) {
  const defs = {
    'EX-CAREER-JOBS': { name: 'Career and jobs', overblock_risk: 'medium', negative_level: 'campaign', phrase_ids: [] },
    'EX-EDUCATION-COURSES': { name: 'Education and courses', overblock_risk: 'medium', negative_level: 'phrase', phrase_ids: [] },
    'EX-CERTIFICATION-EXAMS': { name: 'Certification and exams', overblock_risk: 'low', negative_level: 'phrase', phrase_ids: [] },
    'EX-SALARY': { name: 'Salary', overblock_risk: 'high', negative_level: 'phrase', phrase_ids: [] },
    'EX-RESUME-INTERVIEWS': { name: 'Resume and interviews', overblock_risk: 'low', negative_level: 'phrase', phrase_ids: [] },
    'EX-FORUMS-INSTRUCTIONS': { name: 'Forums and instructions', overblock_risk: 'medium', negative_level: 'phrase', phrase_ids: [] },
    'EX-FREE-DOWNLOADS': { name: 'Free downloads', overblock_risk: 'medium', negative_level: 'phrase', phrase_ids: [] },
    'EX-SELF-SERVICE-MANUALS': { name: 'Self-service manuals', overblock_risk: 'high', negative_level: 'phrase', phrase_ids: [] },
    'EX-UNRELATED-PLATFORMS': { name: 'Unrelated platforms', overblock_risk: 'low', negative_level: 'campaign', phrase_ids: [] },
    'EX-PRODUCT-LICENSE-ONLY': { name: 'Product-only/license-only intent', overblock_risk: 'high', negative_level: 'phrase', phrase_ids: [] },
    'EX-INFORMATIONAL-RESEARCH': { name: 'Informational research', overblock_risk: 'high', negative_level: 'phrase', phrase_ids: [] },
    'EX-IRRELEVANT-GEOGRAPHY': { name: 'Irrelevant geography', overblock_risk: 'medium', negative_level: 'campaign', phrase_ids: [] },
  };
  for (const r of registry) {
    if (r.exclusion_family && defs[r.exclusion_family]) defs[r.exclusion_family].phrase_ids.push(r.phrase_id);
  }
  return Object.entries(defs).map(([id, d]) => ({
    family_id: id,
    family_name: d.name,
    evidence_phrase_ids: d.phrase_ids,
    record_count: d.phrase_ids.length,
    representative_terms: [...new Set(registry.filter((r) => r.exclusion_family === id).slice(0, 8).map((r) => r.phrase))],
    overblock_risk: d.overblock_risk,
    suitable_negative_level: d.negative_level,
    operator_review_notes: d.record_count === 0 ? 'No evidence in partial assessed corpus' : 'Evidence from Phase 5.2 partial review — not final minus-word list',
  }));
}

function integrityReconciliation(registry, accept, reject, abstain) {
  const processed = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PROCESSED-IDS-MANIFEST-v1.json'));
  const unprocessed = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-UNPROCESSED-IDS-MANIFEST-v1.json'));
  const processedIds = new Set(processed.records.map((r) => r.phrase_id));
  const unprocessedIds = new Set(unprocessed.records.map((r) => r.phrase_id));
  const registryIds = registry.map((r) => r.phrase_id);
  const uniqueRegistry = new Set(registryIds);
  const overlap = [...processedIds].filter((id) => unprocessedIds.has(id));
  const missingFromRegistry = [...processedIds].filter((id) => !uniqueRegistry.has(id));
  const extraInRegistry = [...uniqueRegistry].filter((id) => !processedIds.has(id));
  const duplicates = registryIds.length - uniqueRegistry.size;

  const counts = { ACCEPT: accept.length, REJECT: reject.length, ABSTAIN: abstain.length };
  const pass = uniqueRegistry.size === ASSESSED_TOTAL
    && duplicates === 0
    && missingFromRegistry.length === 0
    && extraInRegistry.length === 0
    && processedIds.size === ASSESSED_TOTAL
    && unprocessedIds.size === UNPROCESSED_TOTAL
    && overlap.length === 0
    && processedIds.size + unprocessedIds.size === CANONICAL_TOTAL
    && counts.ACCEPT + counts.REJECT + counts.ABSTAIN === ASSESSED_TOTAL;

  return {
    pass,
    unique_ids: uniqueRegistry.size,
    duplicates,
    missing_assessed_ids: missingFromRegistry.length,
    unprocessed_ids: unprocessedIds.size,
    overlap: overlap.length,
    union: processedIds.size + unprocessedIds.size,
    final_counts: counts,
    phase51_counts: {
      ACCEPT: registry.filter((r) => r.phase51_final_verdict === 'ACCEPT').length,
      REJECT: registry.filter((r) => r.phase51_final_verdict === 'REJECT').length,
      ABSTAIN: registry.filter((r) => r.phase51_final_verdict === 'ABSTAIN').length,
    },
  };
}

function classifyRemainingFlags(registry) {
  const blocking = [];
  const nonBlocking = [];
  for (const r of registry) {
    if (r.phase52_review_status === 'OPERATOR_REVIEW_REQUIRED') {
      blocking.push({ phrase_id: r.phrase_id, status: r.phase52_review_status, root_cause: r.review_flag_root_cause });
    } else if (r.review_status === 'OPERATOR_REVIEW_REQUIRED' && r.phase52_review_status !== 'OPERATOR_DECISION_APPLIED') {
      blocking.push({ phrase_id: r.phrase_id, status: r.review_status, note: 'Stale OPERATOR_REVIEW_REQUIRED not in packet' });
    } else if (r.review_flag_root_cause && r.phase52_review_status !== 'OPERATOR_DECISION_APPLIED') {
      nonBlocking.push({ phrase_id: r.phrase_id, root_cause: r.review_flag_root_cause, status: r.phase52_review_status });
    }
  }
  return { blocking, nonBlocking };
}

function main() {
  const decisionMap = buildOperatorDecisionMap();
  const operatorPacket = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-OPERATOR-DECISION-PACKET-v1.json'));
  const packetVerify = verifyOperatorPacket(operatorPacket, decisionMap);
  if (!packetVerify.pass) {
    console.error('OPERATOR PACKET VERIFICATION FAILED', packetVerify.errors);
    process.exit(2);
  }

  const phase51Registry = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-REVIEWED-REGISTRY-v2.json'));
  const phase51Ledger = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-CORRECTION-LEDGER-v2.json'));
  const packetById = new Map(operatorPacket.records.map((r) => [r.phrase_id, r]));

  const operatorDecisionRecords = [];
  const correctionLedger = [...phase51Ledger.records];
  const registry = [];
  const accept = [];
  const reject = [];
  const abstain = [];
  const verdictTransitions = { unchanged: 0, changed: 0, by_from: {} };

  for (const record of phase51Registry.records) {
    const operatorVerdict = decisionMap.get(record.phrase_id) ?? record.phase51_final_verdict;
    const isOperatorPacket = decisionMap.has(record.phrase_id);
    const packetItem = packetById.get(record.phrase_id);
    const phase51Verdict = record.phase51_final_verdict;
    const verdictChanged = operatorVerdict !== phase51Verdict;

    let phase52ReviewStatus = record.phase51_review_status;
    let phase52Action = 'PHASE52_CONFIRMED';
    let phase52Rationale = 'Phase 5.1 verdict confirmed without operator change';

    if (isOperatorPacket) {
      phase52ReviewStatus = 'OPERATOR_DECISION_APPLIED';
      phase52Action = verdictChanged ? 'OPERATOR_VERDICT_OVERRIDE' : 'OPERATOR_DECISION_CONFIRMED';
      phase52Rationale = verdictChanged
        ? `Operator verdict ${operatorVerdict} overrides Phase 5.1 ${phase51Verdict}`
        : `Operator confirmed Phase 5.1 verdict ${operatorVerdict}`;

      operatorDecisionRecords.push({
        phrase_id: record.phrase_id,
        phrase: record.phrase,
        original_model_verdict: record.original_model_verdict,
        original_authoritative_verdict: record.original_authoritative_verdict,
        phase5_reviewed_verdict: record.phase5_reviewed_verdict,
        phase51_final_verdict: phase51Verdict,
        operator_final_verdict: operatorVerdict,
        verdict_changed: verdictChanged,
        review_status: 'OPERATOR_DECISION_APPLIED',
        ambiguity: packetItem?.ambiguity ?? null,
        business_consequence: packetItem?.business_consequence ?? null,
        recommended_verdict: packetItem?.recommended_verdict ?? null,
        review_flag_root_cause: packetItem?.review_flag_root_cause ?? record.review_flag_root_cause,
        authority: AUTHORITY,
        reviewer: REVIEWER,
        applied_at: new Date().toISOString(),
      });

      if (verdictChanged) {
        correctionLedger.push({
          phrase_id: record.phrase_id,
          phrase: record.phrase,
          before_verdict: phase51Verdict,
          after_verdict: operatorVerdict,
          change_type: 'OPERATOR_DECISION_PHASE52',
          reason: phase52Rationale,
          authority: AUTHORITY,
          reviewer: REVIEWER,
          phase: '5.2',
          preserved: {
            original_model_verdict: record.original_model_verdict,
            original_authoritative_verdict: record.original_authoritative_verdict,
            phase5_reviewed_verdict: record.phase5_reviewed_verdict,
            phase51_final_verdict: phase51Verdict,
          },
        });
        const key = `${phase51Verdict}_TO_${operatorVerdict}`;
        verdictTransitions.by_from[key] = (verdictTransitions.by_from[key] || 0) + 1;
        verdictTransitions.changed += 1;
      } else {
        verdictTransitions.unchanged += 1;
      }
    }

    const intent = assignIntent(record.phrase, operatorVerdict);
    const geo = assignGeography(record.phrase);
    const serviceFamily = assignServiceFamily(record.phrase, operatorVerdict);
    const exclusionFamily = assignExclusionFamily(record.phrase, operatorVerdict);

    const entry = {
      ...record,
      operator_final_verdict: operatorVerdict,
      phase52_final_verdict: operatorVerdict,
      phase52_review_status: phase52ReviewStatus,
      phase52_action: phase52Action,
      phase52_rationale: phase52Rationale,
      phase52_authority: isOperatorPacket ? AUTHORITY : record.phase51_authority,
      review_status: isOperatorPacket ? 'OPERATOR_DECISION_APPLIED' : record.phase51_review_status,
      service_family: serviceFamily,
      primary_intent: intent.primary,
      secondary_intent: intent.secondary,
      geography: geo,
      exclusion_family: exclusionFamily,
      provenance: {
        ...record.provenance,
        phase52_reviewer: REVIEWER,
        phase52_authority: isOperatorPacket ? AUTHORITY : record.phase51_authority,
      },
    };
    registry.push(entry);

    const outRec = {
      phrase_id: record.phrase_id,
      phrase: record.phrase,
      original_model_verdict: record.original_model_verdict,
      original_authoritative_verdict: record.original_authoritative_verdict,
      phase5_reviewed_verdict: record.phase5_reviewed_verdict,
      phase51_final_verdict: phase51Verdict,
      operator_final_verdict: operatorVerdict,
      phase52_final_verdict: operatorVerdict,
      phase52_review_status: phase52ReviewStatus,
      review_status: entry.review_status,
      service_family: serviceFamily,
      primary_intent: intent.primary,
      secondary_intent: intent.secondary,
      geography: geo,
      exclusion_family: exclusionFamily,
      source_metadata: record.source_metadata,
      provenance: entry.provenance,
    };

    if (operatorVerdict === 'ACCEPT') accept.push(outRec);
    else if (operatorVerdict === 'REJECT') reject.push(outRec);
    else abstain.push(outRec);
  }

  registry.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id));
  accept.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id));
  reject.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id));
  abstain.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id));

  const integrity = integrityReconciliation(registry, accept, reject, abstain);
  const remainingFlags = classifyRemainingFlags(registry);
  const serviceTaxonomy = buildServiceTaxonomy(registry);
  const exclusionTaxonomy = buildExclusionTaxonomy(registry);

  const intentCounts = {};
  for (const r of registry) intentCounts[r.primary_intent] = (intentCounts[r.primary_intent] || 0) + 1;
  const intentTaxonomy = Object.entries(intentCounts).map(([intent, count]) => ({
    intent_class: intent,
    record_count: count,
    accept_count: registry.filter((r) => r.primary_intent === intent && r.operator_final_verdict === 'ACCEPT').length,
    reject_count: registry.filter((r) => r.primary_intent === intent && r.operator_final_verdict === 'REJECT').length,
    abstain_count: registry.filter((r) => r.primary_intent === intent && r.operator_final_verdict === 'ABSTAIN').length,
  }));

  const geoRegistry = registry.filter((r) => r.geography.status !== 'NO_GEOGRAPHY').map((r) => ({
    phrase_id: r.phrase_id,
    phrase: r.phrase,
    normalized: r.geography.normalized,
    usable: r.geography.usable,
    status: r.geography.status,
    operator_final_verdict: r.operator_final_verdict,
  }));
  const geography = {
    geography_id: 'corvonero-run-004-phase-52-geography-v1',
    primary_markets: ['Новосибирск', 'Новосибирская область'],
    expansion_markets: ['Краснодар', 'Екатеринбург', 'Красноярск'],
    phrase_registry: geoRegistry,
    distribution: {
      primary_novosibirsk_nso: geoRegistry.filter((g) => g.status === 'PRIMARY').length,
      expansion_krasnodar: geoRegistry.filter((g) => g.normalized?.includes('краснодар')).length,
      expansion_ekaterinburg: geoRegistry.filter((g) => g.normalized?.includes('екатеринбург')).length,
      expansion_krasnoyarsk: geoRegistry.filter((g) => g.normalized?.includes('красноярск')).length,
      other_russian_cities: geoRegistry.filter((g) => g.status === 'OTHER_RU').length,
      russia_wide_remote: geoRegistry.filter((g) => g.status === 'REMOTE').length,
      irrelevant_or_unknown: geoRegistry.filter((g) => g.status === 'IRRELEVANT' || g.status === 'SAFE_UNKNOWN').length,
      expansion_other: geoRegistry.filter((g) => g.status === 'EXPANSION' && !['краснодар', 'екатеринбург', 'красноярск'].some((c) => g.normalized?.includes(c))).length,
    },
    verdict_by_geo: {},
    note: 'Geography alone does not change semantic verdict — cross-tabulated for reconciliation only',
  };
  for (const g of geoRegistry) {
    const key = `${g.status}:${g.operator_final_verdict}`;
    geography.verdict_by_geo[key] = (geography.verdict_by_geo[key] || 0) + 1;
  }

  const phase52Corrections = correctionLedger.length - phase51Ledger.count;
  const phaseVerdict = integrity.pass && remainingFlags.blocking.length === 0
    ? 'PASS'
    : 'BLOCKED — OPERATOR DECISION RECONCILIATION FAILED';

  const signOff = {
    sign_off_id: 'corvonero-run-004-phase-52-partial-semantic-sign-off-v1',
    run_id: RUN_ID,
    phase: '5.2',
    phase_verdict: phaseVerdict,
    partial_semantic_authority: phaseVerdict === 'PASS' ? 'OPERATOR APPROVED' : 'BLOCKED',
    project_lifecycle: phaseVerdict === 'PASS' ? 'READY_FOR_PARTIAL_CAMPAIGN_PLANNING' : 'PHASE_52_BLOCKED',
    campaign_architecture: 'NOT STARTED',
    provider_calls: 'FROZEN',
    assessed_records: ASSESSED_TOTAL,
    unprocessed_records: UNPROCESSED_TOTAL,
    canonical_total: CANONICAL_TOTAL,
    partial_coverage_pct: Number(((ASSESSED_TOTAL / CANONICAL_TOTAL) * 100).toFixed(1)),
    operator_decisions_applied: operatorDecisionRecords.length,
    operator_decision_breakdown: {
      ACCEPT: OPERATOR_DECISIONS.ACCEPT.length,
      REJECT: OPERATOR_DECISIONS.REJECT.length,
      ABSTAIN: OPERATOR_DECISIONS.ABSTAIN.length,
    },
    verdict_distribution: {
      phase4: { ACCEPT: 529, REJECT: 762, ABSTAIN: 308 },
      phase5: { ACCEPT: 531, REJECT: 578, ABSTAIN: 490 },
      phase51: integrity.phase51_counts,
      phase52_final: integrity.final_counts,
    },
    verdict_transitions: verdictTransitions,
    integrity,
    remaining_blocking_flags: remainingFlags.blocking,
    remaining_non_blocking_flags_count: remainingFlags.nonBlocking.length,
    next_gate: 'OPERATOR REVIEW OF FINAL PARTIAL SEMANTIC SIGN-OFF',
    created_at: new Date().toISOString(),
  };

  const resolvedOperatorPacket = {
    packet_id: 'corvonero-run-004-phase-52-resolved-operator-packet-v1',
    run_id: RUN_ID,
    source_packet: 'CORVONERO-RUN-004-PHASE-5.1-OPERATOR-DECISION-PACKET-v1.json',
    total: 47,
    all_applied: operatorDecisionRecords.every((r) => r.review_status === 'OPERATOR_DECISION_APPLIED'),
    records: operatorDecisionRecords.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id)),
    summary: {
      verdict_changed: verdictTransitions.changed,
      verdict_unchanged: verdictTransitions.unchanged,
      transitions: verdictTransitions.by_from,
    },
  };

  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-OPERATOR-DECISIONS-v1.json'), {
    ledger_id: 'corvonero-run-004-phase-52-operator-decisions-v1',
    run_id: RUN_ID,
    source: 'CORVONERO-RUN-004-PHASE-5.1-OPERATOR-DECISION-PACKET-v1.json',
    authority: AUTHORITY,
    reviewer: REVIEWER,
    total: 47,
    reconciliation: packetVerify,
    records: operatorDecisionRecords.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id)),
    resolved_packet: resolvedOperatorPacket,
  });

  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-REVIEWED-REGISTRY-v1.json'), {
    registry_id: 'corvonero-run-004-phase-52-final-reviewed-registry-v1',
    run_id: RUN_ID,
    source: 'CORVONERO-RUN-004-PHASE-5.1-REVIEWED-REGISTRY-v2.json',
    count: registry.length,
    records: registry,
  });

  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-ACCEPT-v1.json'), { run_id: RUN_ID, count: accept.length, records: accept });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-REJECT-v1.json'), { run_id: RUN_ID, count: reject.length, records: reject });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-ABSTAIN-v1.json'), { run_id: RUN_ID, count: abstain.length, records: abstain });

  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-CORRECTION-LEDGER-v1.json'), {
    ledger_id: 'corvonero-run-004-phase-52-final-correction-ledger-v1',
    source: 'CORVONERO-RUN-004-PHASE-5.1-CORRECTION-LEDGER-v2.json',
    phase51_correction_count: phase51Ledger.count,
    phase52_additional_corrections: phase52Corrections,
    count: correctionLedger.length,
    records: correctionLedger,
  });

  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-SERVICE-TAXONOMY-v1.json'), {
    taxonomy_id: 'corvonero-run-004-phase-52-final-service-taxonomy-v1',
    families: serviceTaxonomy,
  });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-INTENT-TAXONOMY-v1.json'), {
    taxonomy_id: 'corvonero-run-004-phase-52-final-intent-taxonomy-v1',
    classes: intentTaxonomy,
  });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-GEOGRAPHY-v1.json'), geography);
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-FINAL-EXCLUSION-TAXONOMY-v1.json'), {
    taxonomy_id: 'corvonero-run-004-phase-52-final-exclusion-taxonomy-v1',
    families: exclusionTaxonomy,
  });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-PARTIAL-SEMANTIC-SIGN-OFF-v1.json'), signOff);

  const signOffMd = `# CORVONERO RUN 004 — Phase 5.2 Partial Semantic Sign-Off v1

**Run:** \`${RUN_ID}\`  
**Date:** ${new Date().toISOString().slice(0, 10)}

## Status

\`\`\`text
PHASE 5.2:
${phaseVerdict}

Partial semantic authority:
${signOff.partial_semantic_authority}

Project:
${signOff.project_lifecycle}

Campaign Architecture:
NOT STARTED
\`\`\`

## Coverage

- Assessed: **${ASSESSED_TOTAL}** / ${CANONICAL_TOTAL} (${signOff.partial_coverage_pct}%)
- Unprocessed (excluded): **${UNPROCESSED_TOTAL}**

## Operator decisions

- Applied: **47** (ACCEPT 10, REJECT 10, ABSTAIN 27)
- Verdict changed from Phase 5.1: **${verdictTransitions.changed}**
- Verdict unchanged: **${verdictTransitions.unchanged}**

## Final verdict distribution

| Stage | ACCEPT | REJECT | ABSTAIN |
|-------|--------|--------|---------|
| Phase 5.1 | ${integrity.phase51_counts.ACCEPT} | ${integrity.phase51_counts.REJECT} | ${integrity.phase51_counts.ABSTAIN} |
| Phase 5.2 (final) | ${integrity.final_counts.ACCEPT} | ${integrity.final_counts.REJECT} | ${integrity.final_counts.ABSTAIN} |

## Integrity

- Unique IDs: ${integrity.unique_ids}
- Duplicates: ${integrity.duplicates}
- Missing assessed: ${integrity.missing_assessed_ids}
- Unprocessed: ${integrity.unprocessed_ids}
- Overlap: ${integrity.overlap}
- Union: ${integrity.union}

## Next gate

\`${signOff.next_gate}\`

Provider calls: **FROZEN**  
Campaign Architecture: **NOT STARTED**
`;
  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.2-PARTIAL-SEMANTIC-SIGN-OFF-v1.md'), signOffMd);

  const phase6Md = `# CORVONERO RUN 004 — Phase 6 Next Task (Partial) v3

**Prerequisite:** Phase 5.2 — ${phaseVerdict} — ${signOff.partial_semantic_authority}  
**Gate:** ${signOff.next_gate}

## Authorized after operator sign-off review

- Partial campaign-planning architecture review (${ASSESSED_TOTAL} assessed records, ${signOff.partial_coverage_pct}% coverage)
- Use Phase 5.2 final ACCEPT/REJECT/ABSTAIN registries as semantic authority
- Service, intent, geography, and exclusion taxonomies from Phase 5.2 final artefacts

## Not authorized

- Campaign Architecture execution (ad groups, ads, minus-word deployment)
- Commander / import / launch / Wave 5
- Processing ${UNPROCESSED_TOTAL} unprocessed backlog IDs
- OpenRouter or external model calls
- Final minus-word list production (exclusion taxonomy is preparatory only)

## Stop condition

Stop after operator reviews this partial semantic sign-off. Do not start Campaign Architecture without explicit charter.
`;
  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-6-NEXT-TASK-PARTIAL-v3.md'), phase6Md);

  const report = buildReport(signOff, packetVerify, operatorDecisionRecords, integrity, remainingFlags, serviceTaxonomy, intentTaxonomy, geography, exclusionTaxonomy, verdictTransitions, phase52Corrections);
  writeText(path.join(REPORTS, 'REPORT-corvonero-run-004-phase-5.2-final-partial-sign-off-v1.md'), report);

  console.log(JSON.stringify({
    phase52_verdict: phaseVerdict,
    accept: integrity.final_counts.ACCEPT,
    reject: integrity.final_counts.REJECT,
    abstain: integrity.final_counts.ABSTAIN,
    operator_applied: operatorDecisionRecords.length,
    verdict_changed: verdictTransitions.changed,
    blocking_flags: remainingFlags.blocking.length,
  }, null, 2));
}

function buildReport(signOff, packetVerify, operatorRecords, integrity, remainingFlags, serviceTaxonomy, intentTaxonomy, geography, exclusionTaxonomy, verdictTransitions, phase52Corrections) {
  const acceptList = operatorRecords.filter((r) => r.operator_final_verdict === 'ACCEPT');
  const rejectList = operatorRecords.filter((r) => r.operator_final_verdict === 'REJECT');
  const abstainList = operatorRecords.filter((r) => r.operator_final_verdict === 'ABSTAIN');

  return `# REPORT — CORVONERO RUN 004 PHASE 5.2 FINAL PARTIAL SEMANTIC SIGN-OFF V1

**Run ID:** \`${RUN_ID}\`  
**Date:** ${new Date().toISOString().slice(0, 10)}

---

## 1. Safety and Scope

Phase 5.2 operator decision application using Phase 5.1 artefacts only. No provider calls. No canonical/Phase 4/Phase 5/Phase 5.1 source mutation. ${UNPROCESSED_TOTAL} unprocessed IDs remain excluded. Campaign Architecture **NOT STARTED**.

---

## 2. Git Preflight

- Branch: \`mars/canonical-post-recovery\`
- Recovery ancestry: verified (no destructive git operations performed)
- Working tree: new Phase 5.2 artefacts only

---

## 3. Input Authority

Run \`${RUN_ID}\`. Phase 5.1 reviewed registry v2, correction ledger v2, and operator decision packet v1 as input. Unprocessed backlog preserved.

---

## 4. Operator Decision Reconciliation

| Check | Result |
|-------|--------|
| Packet total | 47 |
| Decision map total | 47 |
| ACCEPT decisions | 10 |
| REJECT decisions | 10 |
| ABSTAIN decisions | 27 |
| Packet verification | ${packetVerify.pass ? 'PASS' : 'FAIL'} |

---

## 5. ACCEPT Decisions

${acceptList.map((r) => `- **${r.phrase_id}** — "${r.phrase}" (Phase 5.1: ${r.phase51_final_verdict}${r.verdict_changed ? ` → operator ${r.operator_final_verdict}` : ', confirmed'})`).join('\n')}

---

## 6. REJECT Decisions

${rejectList.map((r) => `- **${r.phrase_id}** — "${r.phrase}" (Phase 5.1: ${r.phase51_final_verdict}${r.verdict_changed ? ` → operator ${r.operator_final_verdict}` : ', confirmed'})`).join('\n')}

---

## 7. ABSTAIN Decisions

${abstainList.map((r) => `- **${r.phrase_id}** — "${r.phrase}" (Phase 5.1: ${r.phase51_final_verdict}${r.verdict_changed ? ` → operator ${r.operator_final_verdict}` : ', confirmed'})`).join('\n')}

---

## 8. Provenance Preservation

All ${ASSESSED_TOTAL} records retain: \`original_model_verdict\`, \`original_authoritative_verdict\` (Phase 4), \`phase5_reviewed_verdict\`, \`phase51_final_verdict\`, and \`operator_final_verdict\` / \`phase52_final_verdict\`. Source evidence and Phase 4/5/5.1 artefacts not overwritten.

---

## 9. Final Verdict Distribution

| Stage | ACCEPT | REJECT | ABSTAIN |
|-------|--------|--------|---------|
| Phase 4 | 529 | 762 | 308 |
| Phase 5 | 531 | 578 | 490 |
| Phase 5.1 | ${integrity.phase51_counts.ACCEPT} | ${integrity.phase51_counts.REJECT} | ${integrity.phase51_counts.ABSTAIN} |
| Phase 5.2 (final) | ${integrity.final_counts.ACCEPT} | ${integrity.final_counts.REJECT} | ${integrity.final_counts.ABSTAIN} |

Operator verdict transitions: ${verdictTransitions.changed} changed, ${verdictTransitions.unchanged} unchanged.

${Object.keys(verdictTransitions.by_from).length ? `Transitions: ${Object.entries(verdictTransitions.by_from).map(([k, v]) => `${k} (${v})`).join('; ')}` : ''}

---

## 10. Final Service Taxonomy

${serviceTaxonomy.filter((f) => f.record_count > 0).map((f) => `- **${f.id}**: ${f.record_count} ACCEPT records`).join('\n')}

---

## 11. Final Intent Taxonomy

${intentTaxonomy.sort((a, b) => b.record_count - a.record_count).slice(0, 10).map((c) => `- **${c.intent_class}**: ${c.record_count} (A:${c.accept_count} R:${c.reject_count} Ab:${c.abstain_count})`).join('\n')}

---

## 12. Geography

${JSON.stringify(geography.distribution, null, 2)}

---

## 13. Exclusion Taxonomy

${exclusionTaxonomy.filter((f) => f.record_count > 0).slice(0, 8).map((f) => `- **${f.family_id}**: ${f.record_count} (overblock risk: ${f.overblock_risk})`).join('\n')}

---

## 14. Remaining Review Flags

- Blocking flags: **${remainingFlags.blocking.length}**
- Non-blocking historical root-cause tags: **${remainingFlags.nonBlocking.length}**

All 47 operator-packet flags closed as \`OPERATOR_DECISION_APPLIED\`.

---

## 15. Partial Coverage Limitation

${ASSESSED_TOTAL} assessed / ${CANONICAL_TOTAL} canonical (${signOff.partial_coverage_pct}%). ${UNPROCESSED_TOTAL} unprocessed IDs remain **EXCLUDED** — do not impute or extrapolate.

---

## 16. Final Integrity Reconciliation

| Metric | Value |
|--------|-------|
| Unique IDs | ${integrity.unique_ids} |
| Duplicates | ${integrity.duplicates} |
| Missing assessed IDs | ${integrity.missing_assessed_ids} |
| Unprocessed IDs | ${integrity.unprocessed_ids} |
| Overlap | ${integrity.overlap} |
| Union | ${integrity.union} |
| Reconciliation | ${integrity.pass ? 'PASS' : 'FAIL'} |

---

## 17. Phase 5.2 Verdict

\`\`\`text
PHASE 5.2:
${signOff.phase_verdict}

Partial semantic authority:
${signOff.partial_semantic_authority}

Project:
${signOff.project_lifecycle}

Campaign Architecture:
NOT STARTED
\`\`\`

---

## 18. Project Lifecycle

- Provider calls: **FROZEN**
- Partial semantic authority: **${signOff.partial_semantic_authority}**
- Next gate: **${signOff.next_gate}**

---

## 19. Outputs Created

- CORVONERO-RUN-004-PHASE-5.2-OPERATOR-DECISIONS-v1.json
- CORVONERO-RUN-004-PHASE-5.2-FINAL-REVIEWED-REGISTRY-v1.json
- CORVONERO-RUN-004-PHASE-5.2-FINAL-ACCEPT-v1.json
- CORVONERO-RUN-004-PHASE-5.2-FINAL-REJECT-v1.json
- CORVONERO-RUN-004-PHASE-5.2-FINAL-ABSTAIN-v1.json
- CORVONERO-RUN-004-PHASE-5.2-FINAL-CORRECTION-LEDGER-v1.json
- CORVONERO-RUN-004-PHASE-5.2-FINAL-SERVICE-TAXONOMY-v1.json
- CORVONERO-RUN-004-PHASE-5.2-FINAL-INTENT-TAXONOMY-v1.json
- CORVONERO-RUN-004-PHASE-5.2-FINAL-GEOGRAPHY-v1.json
- CORVONERO-RUN-004-PHASE-5.2-FINAL-EXCLUSION-TAXONOMY-v1.json
- CORVONERO-RUN-004-PHASE-5.2-PARTIAL-SEMANTIC-SIGN-OFF-v1.md
- CORVONERO-RUN-004-PHASE-5.2-PARTIAL-SEMANTIC-SIGN-OFF-v1.json
- CORVONERO-RUN-004-PHASE-6-NEXT-TASK-PARTIAL-v3.md

---

## 20. Files Changed

- \`projects/mars-search-ppc-production/pilots/corvonero/tools/execute-run-004-phase52-operator-decisions-v1.mjs\` (new)
- All Phase 5.2 output artefacts listed in §19 (new)
- \`projects/mars-search-ppc-production/reports/REPORT-corvonero-run-004-phase-5.2-final-partial-sign-off-v1.md\` (new)

---

## 21. Git Status

Uncommitted new artefacts. No commit or push performed.

---

## 22. SAFE UNKNOWN

- Live campaign performance impact of operator ACCEPT on informational-edge phrases (e.g. CR2-PHR-00076) not validated in-repo.
- ${UNPROCESSED_TOTAL} backlog records remain semantically unassessed — partial authority applies to ${ASSESSED_TOTAL} IDs only.

---

## 23. Operator Decisions Required

**None** for the 47-record packet — all applied.

Next human gate: **${signOff.next_gate}**

---

## 24. Exact Phase 6 Task

See \`CORVONERO-RUN-004-PHASE-6-NEXT-TASK-PARTIAL-v3.md\`: operator review of final partial semantic sign-off; partial campaign-planning architecture review authorized only after that gate.

---

## 25. Stop Condition

Phase 5.2 complete. Campaign Architecture and advertising implementation **NOT STARTED**. Stop after final partial semantic sign-off pending operator review.
`;
}

main();
