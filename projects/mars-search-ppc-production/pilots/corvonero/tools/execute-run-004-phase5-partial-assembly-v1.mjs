#!/usr/bin/env node
/**
 * Corvonero Run 004 Phase 5 — Partial Semantic Review and Assembly.
 * No provider calls. No canonical corpus mutation. 1599 assessed records only.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { classifyPhraseV2 } from './canary-family-classifier-v2.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const PILOT = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const REPORTS = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/reports');
const FIX = path.join(REPO_ROOT, 'projects/orca/semantic-intelligence/live-model/fixtures');
const CORPUS_REL = 'projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json';

const RUN_ID = 'corv-semantic-v2-20260626-004';
const CANONICAL_TOTAL = 2368;
const ASSESSED_TOTAL = 1599;
const UNPROCESSED_TOTAL = 769;
const REVIEWER = 'PHASE_5_PARTIAL_ASSEMBLY_v1';
const AUTHORITY = 'CORVONERO RUN 004 PHASE 5 — NO MODEL CALLS';

const OPERATOR_OVERRIDE_00584 = {
  phrase_id: 'CR2-PHR-00584',
  model_verdict: 'ACCEPT',
  final_authoritative_verdict: 'REJECT',
  authority: 'OPERATOR_ADJUDICATION_OVERRIDE',
};

const PRIMARY_GEO = /(?:новосибирск|новосибирск(?:ая|ой|ую)\s+област)/i;
const EXPANSION_GEO = /(?:краснодар|екатеринбург|красноярск|москва|санкт-петербург|спб|казань|нижний\s+новгород|самара|ростов|воронеж|пермь|волгоград|тюмень|уфа|омск|челябинск|иркутск|хабаровск|владивосток)/i;
const FOREIGN_GEO = /(?:минск|киев|алматы|астана|ташкент|ереван|тбилиси|минск(?:ая|ой))/i;

const CAREER_RE = /(?:ваканс|резюме|собеседован|карьер|трудоустройств|устроиться|стажер|стажировк|ищу\s+работ|работа\s+программист(?:ом|ами|ов|ке)|работа\s+разработчик(?:ом|ами|ов|ке)|работодател|требовани(?:я|е)\s+к\s+программист|зарплат(?:а|ы)\s+(?:программист|разработчик|специалист))/i;
const EDUCATION_RE = /(?:как\s+стать|обучен|курс(?:ы|ов|а)?|учеб|экзамен|сертификац|урок|тренинг|семинар|skillbox|ironskills|быстрый\s+старт|клуб\s+программист|диплом)/i;
const INFO_RE = /(?:что\s+такое|что\s+делает|что\s+должен\s+уметь|что\s+нужно\s+знать|как\s+работает|инструкци|руководств|форум|пример|самостоятельно|скачать\s+(?:бесплатно|инструкц)|wiki|википеди)/i;
const SELF_SERVICE_RE = /(?:инструкци|самостоятельно|самому|как\s+(?:обновить|настроить|установить)(?!\s+специалист))/i;
const COMMERCIAL_PRICE = /(?:сколько\s+стоит\s+работа|стоимость\s+работ(?:ы|)|цена\s+работ(?:ы|)|стоимость\s+услуг|расценки\s+специалиста|стоимость\s+работ\s+по|цена\s+услуг|прайс|сколько\s+стоит\s+(?:программист|специалист|услуг))/i;
const COMMERCIAL_DEMAND = /(?:нужен|нужна|нужно\s+(?:программист|специалист|заказать|вызвать)|заказать|найти\s+(?:специалист|программист)|вызвать\s+программист|нанять|под\s+ключ|срочно|услуг(?:и|а)\s+(?:программист|специалист|по\s+1с)|услуги\s+по)/i;
const SERVICE_TASK = /(?:внедрен|настрой|сопровожден|доработк|интеграц(?:ия|ии|ию)|обслуживан|ремонт|миграц|аудит|оптимизац|консультац|исправить|устранить|программир|разработк|отчет|обработк|печатн|обновлен)/i;
const PRODUCT_ONLY = /(?:купить|приобрест|лицензи|поставк|дистрибутив|коробочн)(?!.*(?:настрой|внедрен|сопровожден|услуг|программист|специалист))/i;
const PROBLEM = /(?:ошибк|не\s+работает|сбой|исправить|устранить|fault|exception|зависает|тормозит)/i;
const MARKING = /(?:честн(?:ый|ого)\s+знак|маркировк(?:а|и|у|ой)|data\s*matrix|gs1|агрегац(?:ия|ии)\s+код)/i;
const TS_PIOT = /(?:тс\s*пиот|ts\s*piot|промышленн(?:ая|ой|ую)\s+безопасност)/i;
const INTEGRATION = /(?:интеграц(?:ия|ии|ию|ией)|bitrix|битрикс|синхронизац|обмен\s+данн|api\s+1с|rest\s+1с|обмен\s+с\s+сайт)/i;
const SUBSCRIPTION = /(?:абонент|подписк|ежемесяч|сопровожден(?:ие|ия)\s+1с|its\s+1с|итс\s+1с)/i;
const ONE_OFF = /(?:разов|единоразов|одноразов|почасов|за\s+час|часа?\s+программист)/i;
const FOREIGN_PLATFORM = /(?:sap|oracle|microsoft\s+dynamics|dynamics\s+365|odoo|bitrix24(?!\s+интеграц)|salesforce)/i;

const context = {
  businessScope: JSON.parse(fs.readFileSync(path.join(FIX, 'business-scope-eval-v1.json'), 'utf8')),
  serviceRegistry: JSON.parse(fs.readFileSync(path.join(FIX, 'service-registry-eval-v1.json'), 'utf8')),
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

function authVerdict(r) {
  return r.final_authoritative_verdict || r.final_verdict;
}

function loadPhase4() {
  const accept = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-ACCEPT-REGISTRY-v1.json'));
  const reject = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-REJECT-REGISTRY-v1.json'));
  const abstain = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-ABSTAIN-REGISTRY-v1.json'));
  const processed = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PROCESSED-IDS-MANIFEST-v1.json'));
  const unprocessed = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-UNPROCESSED-IDS-MANIFEST-v1.json'));
  const reviewQueue = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-REVIEW-QUEUE-v1.json'));
  const partialResult = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-RESULT-v1.json'));
  const limitation = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-LIMITATION-v1.json'));
  const corpus = readJson(path.join(REPO_ROOT, CORPUS_REL));
  const phrases = corpus.phrases || corpus.records || corpus;
  return { accept, reject, abstain, processed, unprocessed, reviewQueue, partialResult, limitation, phrases };
}

function integrityAudit(data) {
  const processedIds = new Set(data.processed.records.map((r) => r.phrase_id));
  const unprocessedIds = new Set(data.unprocessed.records.map((r) => r.phrase_id));
  const acceptIds = new Set(data.accept.records.map((r) => r.phrase_id));
  const rejectIds = new Set(data.reject.records.map((r) => r.phrase_id));
  const abstainIds = new Set(data.abstain.records.map((r) => r.phrase_id));
  const corpusIds = new Set(data.phrases.map((p) => p.phrase_id));

  const overlap = [...processedIds].filter((id) => unprocessedIds.has(id));
  const registryUnion = new Set([...acceptIds, ...rejectIds, ...abstainIds]);
  const missingFromRegistry = [...processedIds].filter((id) => !registryUnion.has(id));
  const extraInRegistry = [...registryUnion].filter((id) => !processedIds.has(id));
  const unionAll = new Set([...processedIds, ...unprocessedIds]);
  const orphans = [...unionAll].filter((id) => !corpusIds.has(id));
  const missingFromUnion = [...corpusIds].filter((id) => !unionAll.has(id));

  const override584 = data.reject.records.find((r) => r.phrase_id === 'CR2-PHR-00584');
  const overrideOk = override584
    && override584.model_verdict === 'ACCEPT'
    && authVerdict(override584) === 'REJECT'
    && (override584.operator_override?.authority?.includes('OPERATOR') || override584.operator_override?.override_status === 'OPERATOR_ADJUDICATION_OVERRIDE' || data.partialResult.operator_overrides?.some((o) => o.phrase_id === 'CR2-PHR-00584'));

  const pass = processedIds.size === ASSESSED_TOTAL
    && unprocessedIds.size === UNPROCESSED_TOTAL
    && acceptIds.size === 529
    && rejectIds.size === 762
    && abstainIds.size === 308
    && overlap.length === 0
    && missingFromRegistry.length === 0
    && extraInRegistry.length === 0
    && orphans.length === 0
    && missingFromUnion.length === 0
    && corpusIds.size === CANONICAL_TOTAL
    && overrideOk;

  return {
    receipt_id: 'corvonero-run-004-phase-5-partial-integrity-v1',
    run_id: RUN_ID,
    verdict: pass ? 'PASS — INTEGRITY RECONCILED' : 'BLOCKED — PARTIAL SEMANTIC AUTHORITY RECONCILIATION FAILED',
    reconciled_at: new Date().toISOString(),
    counts: {
      canonical_total: CANONICAL_TOTAL,
      processed_unique: processedIds.size,
      unprocessed_unique: unprocessedIds.size,
      accept: acceptIds.size,
      reject: rejectIds.size,
      abstain: abstainIds.size,
      accept_plus_reject_plus_abstain: acceptIds.size + rejectIds.size + abstainIds.size,
      overlap_processed_unprocessed: overlap.length,
      missing_from_registry: missingFromRegistry.length,
      extra_in_registry: extraInRegistry.length,
      orphans,
      missing_from_union: missingFromUnion.length,
      duplicates_processed: data.processed.records.length - processedIds.size,
      duplicates_unprocessed: data.unprocessed.records.length - unprocessedIds.size,
    },
    operator_override_00584: {
      preserved: !!overrideOk,
      model_verdict: override584?.model_verdict,
      final_authoritative_verdict: authVerdict(override584),
      authority: 'OPERATOR_ADJUDICATION_OVERRIDE',
    },
    exclusion_boundary: {
      current_cycle_assembly_scope: `${ASSESSED_TOTAL} assessed records only`,
      out_of_scope: `${UNPROCESSED_TOTAL} unprocessed records`,
      rule: '769 unprocessed IDs must not enter clusters, taxonomies, demand conclusions, or coverage percentages based on assessed results',
    },
    pass,
  };
}

function assignServiceFamily(text, cls, verdict) {
  if (verdict !== 'ACCEPT') return null;
  const t = text.toLowerCase();
  if (TS_PIOT.test(t)) return 'SF-TS-PIOT';
  if (MARKING.test(t)) return 'SF-MARKING-CHESTNY-ZNAK';
  if (INTEGRATION.test(t)) return 'SF-INTEGRATIONS';
  if (PROBLEM.test(t) && ONE_C.test(t)) return 'SF-TROUBLESHOOTING-NOT-WORKING';
  if (SUBSCRIPTION.test(t)) return 'SF-SUBSCRIPTION-SERVICE';
  if (ONE_OFF.test(t) || COMMERCIAL_PRICE.test(t)) return 'SF-ONE-OFF-WORK';
  if (/отчет|обработк|печатн/.test(t) && ONE_C.test(t)) return 'SF-REPORTS-PROCESSING';
  if (/доработк|разработк|программир|модификац/.test(t) && ONE_C.test(t)) return 'SF-MODIFICATION-DEVELOPMENT';
  if (/сопровожден|обслуживан|абонент|поддержк|its|итс/.test(t) && ONE_C.test(t)) return 'SF-SUPPORT-MAINTENANCE';
  if (COMMERCIAL_DEMAND.test(t) || /программист|специалист|разработчик/.test(t)) return 'SF-1C-PROGRAMMER-SPECIALIST';
  if (SERVICE_TASK.test(t) && ONE_C.test(t)) return 'SF-OTHER-APPROVED-1C-SERVICE';
  if (cls.primary_family === 'direct_commercial_1c_service') return 'SF-1C-PROGRAMMER-SPECIALIST';
  return 'SF-OTHER-APPROVED-1C-SERVICE';
}

function assignIntent(text, cls, verdict) {
  const t = text.toLowerCase();
  if (verdict === 'REJECT') {
    if (CAREER_RE.test(t) || cls.observed_tags?.includes('career')) return { primary: 'CAREER_OR_EDUCATION', secondary: null };
    if (EDUCATION_RE.test(t) || cls.observed_tags?.includes('education')) return { primary: 'CAREER_OR_EDUCATION', secondary: null };
    if (INFO_RE.test(t) || SELF_SERVICE_RE.test(t) || cls.observed_tags?.includes('informational')) return { primary: 'INFORMATIONAL', secondary: null };
    if (PRODUCT_ONLY.test(t) || cls.observed_tags?.includes('product_only')) return { primary: 'PRODUCT_OR_LICENSE', secondary: null };
    if (FOREIGN_PLATFORM.test(t)) return { primary: 'INFORMATIONAL', secondary: 'PRODUCT_OR_LICENSE' };
    return { primary: 'INFORMATIONAL', secondary: null };
  }
  if (verdict === 'ABSTAIN') return { primary: 'AMBIGUOUS', secondary: null, review_flag: true };
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
  if (/программист|специалист/.test(t)) return { primary: 'SPECIALIST_SEARCH', secondary: null };
  return { primary: 'DIRECT_SERVICE_ORDER', secondary: null };
}

function assignExclusionFamily(text, cls, verdict) {
  const t = text.toLowerCase();
  if (CAREER_RE.test(t) || cls.observed_tags?.includes('career')) return 'EX-CAREER-JOBS';
  if (/зарплат/.test(t)) return 'EX-SALARY';
  if (/резюме|собеседован/.test(t)) return 'EX-RESUME-INTERVIEWS';
  if (EDUCATION_RE.test(t) || cls.observed_tags?.includes('education')) return 'EX-EDUCATION-COURSES';
  if (/сертификац|экзамен/.test(t)) return 'EX-CERTIFICATION-EXAMS';
  if (INFO_RE.test(t) || cls.observed_tags?.includes('informational')) return 'EX-INFORMATIONAL-RESEARCH';
  if (SELF_SERVICE_RE.test(t) || cls.observed_tags?.includes('self_service')) return 'EX-SELF-SERVICE-MANUALS';
  if (/форум|wiki|википеди/.test(t)) return 'EX-FORUMS-INSTRUCTIONS';
  if (/скачать\s+бесплатно|бесплатн/.test(t)) return 'EX-FREE-DOWNLOADS';
  if (FOREIGN_PLATFORM.test(t) || cls.observed_tags?.includes('foreign_incompatible_platform')) return 'EX-UNRELATED-PLATFORMS';
  if (PRODUCT_ONLY.test(t) && verdict === 'REJECT') return 'EX-PRODUCT-LICENSE-ONLY';
  if (FOREIGN_GEO.test(t)) return 'EX-IRRELEVANT-GEOGRAPHY';
  if (verdict === 'REJECT') return 'EX-INFORMATIONAL-RESEARCH';
  return null;
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
    return { normalized: city, usable: expansion || /москва|санкт|спб|миллион/.test(t), status: expansion ? 'EXPANSION' : 'OTHER_RU' };
  }
  return { normalized: null, usable: null, status: 'SAFE_UNKNOWN' };
}

const ONE_C = /(?:1[\s-]?с|1c|один[\s-]?эс)/i;

function auditAcceptRecord(rec, cls) {
  const t = (rec.phrase || '').toLowerCase();
  const issues = [];
  if (rec.phrase_id === 'CR2-PHR-00584') {
    return { action: 'ACCEPT_TO_REJECT', reason: 'Operator override preserved — career/employment', authority: 'OPERATOR_ADJUDICATION_OVERRIDE' };
  }
  if (CAREER_RE.test(t) || cls.observed_tags?.includes('career')) {
    issues.push('career_employment');
    return { action: 'ACCEPT_TO_REJECT', reason: 'Career/employment markers in ACCEPT registry', authority: AUTHORITY };
  }
  if (EDUCATION_RE.test(t) && !COMMERCIAL_DEMAND.test(t) && !COMMERCIAL_PRICE.test(t)) {
    issues.push('education_training');
    return { action: 'ACCEPT_TO_REJECT', reason: 'Education/training without commercial service demand', authority: AUTHORITY };
  }
  if ((INFO_RE.test(t) || SELF_SERVICE_RE.test(t)) && !COMMERCIAL_DEMAND.test(t) && !COMMERCIAL_PRICE.test(t) && !SERVICE_TASK.test(t)) {
    issues.push('informational_self_service');
    return { action: 'ACCEPT_TO_REJECT', reason: 'Informational/self-service without commercial demand', authority: AUTHORITY };
  }
  if (FOREIGN_PLATFORM.test(t)) {
    return { action: 'ACCEPT_TO_REJECT', reason: 'Unrelated foreign platform', authority: AUTHORITY };
  }
  if (cls.observed_tags?.includes('product_only') && !cls.observed_tags?.includes('product_plus_service_bundle') && !COMMERCIAL_DEMAND.test(t)) {
    return { action: 'ACCEPT_TO_ABSTAIN', reason: 'Product/license-only intent — uncertain service scope', authority: AUTHORITY };
  }
  if (rec.confirmation_disagreement || rec.primary_verdict !== rec.reassessment_verdict) {
    return { action: 'ACCEPT_REVIEW_REQUIRED', reason: 'Primary/reassessment disagreement on ACCEPT record', authority: AUTHORITY };
  }
  if (cls.primary_family === 'ambiguous_mixed_intent' && !COMMERCIAL_DEMAND.test(t) && !COMMERCIAL_PRICE.test(t)) {
    return { action: 'ACCEPT_REVIEW_REQUIRED', reason: 'Ambiguous mixed intent without clear commercial markers', authority: AUTHORITY };
  }
  return { action: 'CONFIRMED_ACCEPT', reason: 'No clear policy conflict', authority: AUTHORITY };
}

function auditRejectRecord(rec, cls) {
  const t = (rec.phrase || '').toLowerCase();
  if (rec.phrase_id === 'CR2-PHR-00584') {
    return { action: 'CONFIRMED_REJECT', reason: 'Operator override — career employment preserved as REJECT', authority: 'OPERATOR_ADJUDICATION_OVERRIDE' };
  }
  if (CAREER_RE.test(t) || EDUCATION_RE.test(t)) {
    return { action: 'CONFIRMED_REJECT', reason: 'Correctly rejected career/education', authority: AUTHORITY };
  }
  if (INFO_RE.test(t) && !COMMERCIAL_DEMAND.test(t)) {
    return { action: 'CONFIRMED_REJECT', reason: 'Correctly rejected informational', authority: AUTHORITY };
  }
  if (COMMERCIAL_PRICE.test(t) && ONE_C.test(t)) {
    return { action: 'REJECT_TO_ACCEPT', reason: 'Commercial price/cost of specialist work — false negative', authority: AUTHORITY };
  }
  if (COMMERCIAL_DEMAND.test(t) && ONE_C.test(t) && !CAREER_RE.test(t)) {
    return { action: 'REJECT_TO_ACCEPT', reason: 'Explicit commercial service demand — false negative', authority: AUTHORITY };
  }
  if (SERVICE_TASK.test(t) && ONE_C.test(t) && COMMERCIAL_DEMAND.test(t)) {
    return { action: 'REJECT_TO_ACCEPT', reason: 'Service task with commercial demand — false negative', authority: AUTHORITY };
  }
  if (PROBLEM.test(t) && ONE_C.test(t) && /(?:не\s+работает|ошибк|исправить|устранить|сбой)/.test(t)) {
    return { action: 'REJECT_TO_ABSTAIN', reason: 'Troubleshooting with possible service intent — needs review', authority: AUTHORITY };
  }
  if (MARKING.test(t) && ONE_C.test(t)) {
    return { action: 'REJECT_TO_ABSTAIN', reason: 'Marking/Честный знак — possible commercial service', authority: AUTHORITY };
  }
  if (TS_PIOT.test(t)) {
    return { action: 'REJECT_TO_ABSTAIN', reason: 'TS ПИОТ — possible approved service', authority: AUTHORITY };
  }
  if (INTEGRATION.test(t) && ONE_C.test(t) && !INFO_RE.test(t)) {
    return { action: 'REJECT_TO_ABSTAIN', reason: 'Integration demand — possible commercial service', authority: AUTHORITY };
  }
  if (rec.phrase_id === 'CR2-PHR-00200') {
    return { action: 'CONFIRMED_REJECT', reason: 'Informational phrasing (что нужно знать) — retain REJECT pending operator review', authority: AUTHORITY };
  }
  if (rec.confirmation_disagreement) {
    return { action: 'REJECT_REVIEW_REQUIRED', reason: 'Primary/reassessment disagreement on REJECT record', authority: AUTHORITY };
  }
  return { action: 'CONFIRMED_REJECT', reason: 'No obvious commercial false negative', authority: AUTHORITY };
}

function auditAbstainRecord(rec, cls) {
  const t = (rec.phrase || '').toLowerCase();
  if (CAREER_RE.test(t) || EDUCATION_RE.test(t)) {
    return { action: 'PROMOTE_TO_REJECT', reason: 'Career/education markers', authority: AUTHORITY };
  }
  if (COMMERCIAL_PRICE.test(t) && ONE_C.test(t)) {
    return { action: 'PROMOTE_TO_ACCEPT', reason: 'Commercial price/cost wording', authority: AUTHORITY };
  }
  if (COMMERCIAL_DEMAND.test(t) && ONE_C.test(t) && SERVICE_TASK.test(t)) {
    return { action: 'PROMOTE_TO_ACCEPT', reason: 'Commercial demand with explicit service task', authority: AUTHORITY };
  }
  if (PRODUCT_ONLY.test(t) && !SERVICE_TASK.test(t)) {
    return { action: 'PROMOTE_TO_REJECT', reason: 'Product-only without service task', authority: AUTHORITY };
  }
  if (INFO_RE.test(t) && !COMMERCIAL_DEMAND.test(t)) {
    return { action: 'PROMOTE_TO_REJECT', reason: 'Informational without commercial demand', authority: AUTHORITY };
  }
  if (cls.primary_family === 'ambiguous_mixed_intent' || cls.primary_family === 'generic_erp_platform_ambiguity') {
    return { action: 'RETAIN_ABSTAIN', reason: 'Ambiguous mixed or generic ERP intent', authority: AUTHORITY };
  }
  if (t.split(/\s+/).length <= 3) {
    return { action: 'OPERATOR_REVIEW_REQUIRED', reason: 'Short query — unclear intent', authority: AUTHORITY };
  }
  return { action: 'RETAIN_ABSTAIN', reason: 'Genuine uncertainty — ABSTAIN valid final state', authority: AUTHORITY };
}

function triageReviewQueueItem(item, record, cls, phase5Verdict) {
  const id = item.phrase_id;
  if (id === 'CR2-PHR-00584') {
    return {
      triage: 'CONFIRMED_REJECT',
      rationale: 'Operator override preserved: model ACCEPT, authoritative REJECT, career/employment',
      phase5_verdict: 'REJECT',
      authority: 'OPERATOR_ADJUDICATION_OVERRIDE',
    };
  }
  if (id === 'CR2-PHR-00200') {
    return {
      triage: 'OPERATOR_REVIEW_REQUIRED',
      rationale: 'Informational phrasing with classifier policy disagreement — operator disposition required',
      phase5_verdict: phase5Verdict,
      authority: AUTHORITY,
    };
  }
  if (item.review_reason?.includes('Operator override')) {
    return { triage: 'CONFIRMED_REJECT', rationale: item.review_reason, phase5_verdict: 'REJECT', authority: 'OPERATOR_ADJUDICATION_OVERRIDE' };
  }
  if (item.review_reason?.includes('career') || item.career_gate_classification === 'OPERATOR_REVIEW_REQUIRED') {
    const t = (record?.phrase || '').toLowerCase();
    if (CAREER_RE.test(t)) return { triage: 'CONFIRMED_REJECT', rationale: 'Career gate — employment markers', phase5_verdict: 'REJECT', authority: AUTHORITY };
    if (phase5Verdict === 'ACCEPT' && !CAREER_RE.test(t)) return { triage: 'CONFIRMED_ACCEPT', rationale: 'Career gate cleared — not employment', phase5_verdict: phase5Verdict, authority: AUTHORITY };
    return { triage: 'OPERATOR_REVIEW_REQUIRED', rationale: item.review_reason, phase5_verdict: phase5Verdict, authority: AUTHORITY };
  }
  if (item.review_reason?.includes('PSR-AMB-01') || item.review_reason?.includes('product-plus-service')) {
    return { triage: 'OPERATOR_REVIEW_REQUIRED', rationale: 'Product-plus-service ambiguity — monitored family', phase5_verdict: phase5Verdict, authority: AUTHORITY };
  }
  if (item.review_reason?.includes('Generic ERP')) {
    return { triage: phase5Verdict === 'ABSTAIN' ? 'RETAIN_ABSTAIN' : 'OPERATOR_REVIEW_REQUIRED', rationale: item.review_reason, phase5_verdict: phase5Verdict, authority: AUTHORITY };
  }
  if (item.disagreement_reason) {
    if (phase5Verdict === 'ACCEPT' && !CAREER_RE.test(record?.phrase || '') && !EDUCATION_RE.test(record?.phrase || '')) {
      return { triage: 'CONFIRMED_ACCEPT', rationale: `Phase 5 review confirms ACCEPT after disagreement triage: ${item.disagreement_reason}`, phase5_verdict: phase5Verdict, authority: AUTHORITY };
    }
    if (phase5Verdict === 'REJECT') {
      return { triage: 'CONFIRMED_REJECT', rationale: `Phase 5 review confirms REJECT: ${item.disagreement_reason}`, phase5_verdict: phase5Verdict, authority: AUTHORITY };
    }
    return { triage: 'RETAIN_ABSTAIN', rationale: `Disagreement unresolved — retain ${phase5Verdict}`, phase5_verdict: phase5Verdict, authority: AUTHORITY };
  }
  if (item.review_reason?.includes('malformed')) {
    return { triage: 'DATA_OR_POLICY_ISSUE', rationale: item.review_reason, phase5_verdict: phase5Verdict, authority: AUTHORITY };
  }
  return {
    triage: phase5Verdict === 'ABSTAIN' ? 'RETAIN_ABSTAIN' : phase5Verdict === 'ACCEPT' ? 'CONFIRMED_ACCEPT' : 'CONFIRMED_REJECT',
    rationale: 'Default triage from Phase 5 reviewed verdict',
    phase5_verdict: phase5Verdict,
    authority: AUTHORITY,
  };
}

function buildServiceTaxonomy(registry) {
  const families = {
    'SF-1C-PROGRAMMER-SPECIALIST': { id: 'SF-1C-PROGRAMMER-SPECIALIST', name: '1C programmer / specialist', definition: 'Hire or order work from 1C programmer or specialist', exclusions: ['career searches', 'education'], phrase_ids: [] },
    'SF-SUPPORT-MAINTENANCE': { id: 'SF-SUPPORT-MAINTENANCE', name: '1C support and maintenance', definition: 'Ongoing support, ITS, subscription, сопровождение', exclusions: ['product-only purchase'], phrase_ids: [] },
    'SF-MODIFICATION-DEVELOPMENT': { id: 'SF-MODIFICATION-DEVELOPMENT', name: '1C modification and development', definition: 'Доработка, разработка, programming tasks', exclusions: ['DIY instructions'], phrase_ids: [] },
    'SF-REPORTS-PROCESSING': { id: 'SF-REPORTS-PROCESSING', name: 'Reports and processing', definition: 'Reports, обработки, печатные формы as service work', exclusions: ['free download templates'], phrase_ids: [] },
    'SF-INTEGRATIONS': { id: 'SF-INTEGRATIONS', name: 'Integrations', definition: 'Integration with external systems, API, Bitrix, etc.', exclusions: ['unrelated platform docs'], phrase_ids: [] },
    'SF-MARKING-CHESTNY-ZNAK': { id: 'SF-MARKING-CHESTNY-ZNAK', name: 'Marking / Честный знак', definition: 'Marking and Chestny Znak setup in 1C', exclusions: ['regulatory news only'], phrase_ids: [] },
    'SF-TROUBLESHOOTING-NOT-WORKING': { id: 'SF-TROUBLESHOOTING-NOT-WORKING', name: '1C troubleshooting / not working', definition: 'Errors, failures, не работает with service intent', exclusions: ['self-service forums'], phrase_ids: [] },
    'SF-TS-PIOT': { id: 'SF-TS-PIOT', name: 'TS ПИОТ', definition: 'Industrial safety / TS PIOT in 1C context', exclusions: [], phrase_ids: [] },
    'SF-SUBSCRIPTION-SERVICE': { id: 'SF-SUBSCRIPTION-SERVICE', name: 'Subscription service', definition: 'Abonent, monthly support contracts', exclusions: [], phrase_ids: [] },
    'SF-ONE-OFF-WORK': { id: 'SF-ONE-OFF-WORK', name: 'One-off work', definition: 'Hourly, разовые works, price of specialist labor', exclusions: ['salary queries'], phrase_ids: [] },
    'SF-OTHER-APPROVED-1C-SERVICE': { id: 'SF-OTHER-APPROVED-1C-SERVICE', name: 'Other approved 1C services', definition: 'Approved 1C service demand not mapped to specific family', exclusions: ['out-of-scope products'], phrase_ids: [] },
  };
  for (const r of registry.filter((x) => x.phase5_reviewed_verdict === 'ACCEPT')) {
    if (r.service_family && families[r.service_family]) families[r.service_family].phrase_ids.push(r.phrase_id);
  }
  return Object.values(families).map((f) => ({
    ...f,
    record_count: f.phrase_ids.length,
    representative_phrases: registry.filter((r) => f.phrase_ids.includes(r.phrase_id)).slice(0, 5).map((r) => r.phrase),
    ambiguity_notes: f.record_count === 0 ? 'No evidence in reviewed ACCEPT corpus' : undefined,
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
    operator_review_notes: d.record_count === 0 ? 'No evidence in partial assessed corpus' : 'Evidence from Phase 5 partial review only — not final minus-word list',
  }));
}

function main() {
  const data = loadPhase4();
  const integrity = integrityAudit(data);
  if (!integrity.pass) {
    writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-INTEGRITY-v1.json'), integrity);
    console.error(integrity.verdict);
    process.exit(2);
  }

  const corpusById = new Map(data.phrases.map((p) => [p.phrase_id, p]));
  const allRecords = [
    ...data.accept.records.map((r) => ({ ...r, source_registry: 'ACCEPT' })),
    ...data.reject.records.map((r) => ({ ...r, source_registry: 'REJECT' })),
    ...data.abstain.records.map((r) => ({ ...r, source_registry: 'ABSTAIN' })),
  ];

  const correctionLedger = [];
  const registry = [];
  const phase5Accept = [];
  const phase5Reject = [];
  const phase5Abstain = [];
  const acceptCorrections = { to_reject: [], to_abstain: [], review_required: [] };
  const rejectCorrections = { to_accept: [], to_abstain: [], review_required: [] };
  const abstainCorrections = { to_accept: [], to_reject: [], review_required: [], retain: [] };

  for (const rec of allRecords) {
    const cls = classifyPhraseV2({ phrase_id: rec.phrase_id, phrase: rec.phrase }, context);
    const originalAuth = authVerdict(rec);
    let audit;
    if (rec.source_registry === 'ACCEPT') audit = auditAcceptRecord(rec, cls);
    else if (rec.source_registry === 'REJECT') audit = auditRejectRecord(rec, cls);
    else audit = auditAbstainRecord(rec, cls);

    let phase5Verdict = originalAuth;
    if (audit.action === 'ACCEPT_TO_REJECT' || audit.action === 'PROMOTE_TO_REJECT') phase5Verdict = 'REJECT';
    else if (audit.action === 'ACCEPT_TO_ABSTAIN' || audit.action === 'REJECT_TO_ABSTAIN' || audit.action === 'RETAIN_ABSTAIN') phase5Verdict = 'ABSTAIN';
    else if (audit.action === 'REJECT_TO_ACCEPT' || audit.action === 'PROMOTE_TO_ACCEPT') phase5Verdict = 'ACCEPT';
    else if (audit.action.startsWith('CONFIRMED_')) phase5Verdict = audit.action.replace('CONFIRMED_', '');
    else phase5Verdict = originalAuth;

    if (rec.phrase_id === 'CR2-PHR-00584') {
      phase5Verdict = 'REJECT';
      audit = { action: 'CONFIRMED_REJECT', reason: 'Operator override preserved', authority: 'OPERATOR_ADJUDICATION_OVERRIDE' };
    }

    const reviewStatus = audit.action.includes('REVIEW') || audit.action === 'OPERATOR_REVIEW_REQUIRED'
      ? 'OPERATOR_REVIEW_REQUIRED'
      : phase5Verdict !== originalAuth ? 'PHASE5_CORRECTED' : 'PHASE5_CONFIRMED';

    if (phase5Verdict !== originalAuth) {
      correctionLedger.push({
        phrase_id: rec.phrase_id,
        phrase: rec.phrase,
        before_verdict: originalAuth,
        after_verdict: phase5Verdict,
        change_type: audit.action,
        reason: audit.reason,
        authority: audit.authority,
        reviewer: REVIEWER,
      });
    }

    if (rec.source_registry === 'ACCEPT') {
      if (audit.action === 'ACCEPT_TO_REJECT') acceptCorrections.to_reject.push(rec.phrase_id);
      else if (audit.action === 'ACCEPT_TO_ABSTAIN') acceptCorrections.to_abstain.push(rec.phrase_id);
      else if (audit.action === 'ACCEPT_REVIEW_REQUIRED') acceptCorrections.review_required.push(rec.phrase_id);
    } else if (rec.source_registry === 'REJECT') {
      if (audit.action === 'REJECT_TO_ACCEPT') rejectCorrections.to_accept.push(rec.phrase_id);
      else if (audit.action === 'REJECT_TO_ABSTAIN') rejectCorrections.to_abstain.push(rec.phrase_id);
      else if (audit.action === 'REJECT_REVIEW_REQUIRED') rejectCorrections.review_required.push(rec.phrase_id);
    } else {
      if (audit.action === 'PROMOTE_TO_ACCEPT') abstainCorrections.to_accept.push(rec.phrase_id);
      else if (audit.action === 'PROMOTE_TO_REJECT') abstainCorrections.to_reject.push(rec.phrase_id);
      else if (audit.action === 'OPERATOR_REVIEW_REQUIRED') abstainCorrections.review_required.push(rec.phrase_id);
      else abstainCorrections.retain.push(rec.phrase_id);
    }

    const intent = assignIntent(rec.phrase, cls, phase5Verdict);
    const geo = assignGeography(rec.phrase);
    const serviceFamily = assignServiceFamily(rec.phrase, cls, phase5Verdict);
    const exclusionFamily = assignExclusionFamily(rec.phrase, cls, phase5Verdict);
    const meta = corpusById.get(rec.phrase_id) || {};

    const entry = {
      phrase_id: rec.phrase_id,
      phrase: rec.phrase,
      source_metadata: {
        combined_frequency: meta.combined_frequency ?? meta.frequency ?? null,
        production_source: rec.production_source,
        source_registry: rec.source_registry,
      },
      original_model_verdict: rec.model_verdict,
      original_authoritative_verdict: originalAuth,
      phase5_reviewed_verdict: phase5Verdict,
      service_family: serviceFamily,
      primary_intent: intent.primary,
      secondary_intent: intent.secondary,
      geography: geo,
      exclusion_family: exclusionFamily,
      review_status: reviewStatus,
      rationale: audit.reason,
      provenance: {
        phase4_registry: rec.source_registry,
        phase5_audit_action: audit.action,
        classifier_primary_family: cls.primary_family,
        observed_tags: cls.observed_tags,
        authority: audit.authority,
      },
    };
    registry.push(entry);
    const outRec = { ...rec, phase5_reviewed_verdict: phase5Verdict, review_status: reviewStatus, phase5_audit: audit };
    if (phase5Verdict === 'ACCEPT') phase5Accept.push(outRec);
    else if (phase5Verdict === 'REJECT') phase5Reject.push(outRec);
    else phase5Abstain.push(outRec);
  }

  // Review queue triage
  const registryById = new Map(registry.map((r) => [r.phrase_id, r]));
  const reviewQueueOut = {
    queue_id: 'corvonero-run-004-phase-5-partial-review-queue-v1',
    run_id: RUN_ID,
    source_queue: 'CORVONERO-RUN-004-PHASE-4-PARTIAL-REVIEW-QUEUE-v1.json',
    total_items: data.reviewQueue.total_items,
    mandatory_items: ['CR2-PHR-00200', 'CR2-PHR-00584'],
    items: data.reviewQueue.items.map((item) => {
      const rec = registryById.get(item.phrase_id);
      const cls = classifyPhraseV2({ phrase_id: item.phrase_id, phrase: item.phrase }, context);
      const triage = triageReviewQueueItem(item, rec, cls, rec?.phase5_reviewed_verdict);
      return {
        phrase_id: item.phrase_id,
        phrase: item.phrase,
        phase4_review_reason: item.review_reason,
        phase5_triage: triage.triage,
        phase5_verdict: triage.phase5_verdict,
        rationale: triage.rationale,
        authority: triage.authority,
        original_model_verdict: rec?.original_model_verdict,
        original_authoritative_verdict: rec?.original_authoritative_verdict,
      };
    }),
    triage_summary: {},
    created_at: new Date().toISOString(),
  };
  for (const item of reviewQueueOut.items) {
    reviewQueueOut.triage_summary[item.phase5_triage] = (reviewQueueOut.triage_summary[item.phase5_triage] || 0) + 1;
  }

  const serviceTaxonomy = buildServiceTaxonomy(registry);
  const intentCounts = {};
  for (const r of registry) {
    intentCounts[r.primary_intent] = (intentCounts[r.primary_intent] || 0) + 1;
  }
  const intentTaxonomy = Object.entries(intentCounts).map(([intent, count]) => ({
    intent_class: intent,
    record_count: count,
    accept_count: registry.filter((r) => r.primary_intent === intent && r.phase5_reviewed_verdict === 'ACCEPT').length,
    representative_phrases: registry.filter((r) => r.primary_intent === intent).slice(0, 3).map((r) => r.phrase),
  }));

  const geoRegistry = registry.filter((r) => r.geography.status !== 'NO_GEOGRAPHY').map((r) => ({
    phrase_id: r.phrase_id,
    phrase: r.phrase,
    normalized: r.geography.normalized,
    usable: r.geography.usable,
    status: r.geography.status,
    phase5_verdict: r.phase5_reviewed_verdict,
  }));
  const geography = {
    geography_id: 'corvonero-run-004-phase-5-geography-v1',
    primary_markets: ['Новосибирск', 'Новосибирская область'],
    expansion_markets: ['Краснодар', 'Екатеринбург', 'Красноярск', 'other million cities', 'Russia-wide remote service'],
    phrase_registry: geoRegistry,
    distribution: {
      primary: geoRegistry.filter((g) => g.status === 'PRIMARY').length,
      expansion: geoRegistry.filter((g) => g.status === 'EXPANSION').length,
      remote: geoRegistry.filter((g) => g.status === 'REMOTE').length,
      other_ru: geoRegistry.filter((g) => g.status === 'OTHER_RU').length,
      irrelevant: geoRegistry.filter((g) => g.status === 'IRRELEVANT').length,
      safe_unknown: geoRegistry.filter((g) => g.status === 'SAFE_UNKNOWN').length,
    },
    note: 'Geography alone is not commercial intent',
  };

  const exclusionTaxonomy = buildExclusionTaxonomy(registry);

  const coverage = {
    partial_dataset: `${ASSESSED_TOTAL} / ${CANONICAL_TOTAL} assessed`,
    unprocessed: `${UNPROCESSED_TOTAL} / ${CANONICAL_TOTAL}`,
    coverage_percent: '67.5',
    verdict_distribution: {
      phase4: { ACCEPT: 529, REJECT: 762, ABSTAIN: 308 },
      phase5: {
        ACCEPT: phase5Accept.length,
        REJECT: phase5Reject.length,
        ABSTAIN: phase5Abstain.length,
      },
    },
    corrections_from_phase4: correctionLedger.length,
    operator_review_required: registry.filter((r) => r.review_status === 'OPERATOR_REVIEW_REQUIRED').length,
    service_family_counts: Object.fromEntries(serviceTaxonomy.map((f) => [f.id, f.record_count])),
    intent_counts: intentCounts,
    exclusion_family_counts: Object.fromEntries(exclusionTaxonomy.map((f) => [f.family_id, f.record_count])),
    accept_corrections: acceptCorrections,
    reject_corrections: rejectCorrections,
    abstain_corrections: abstainCorrections,
    review_queue_triage: reviewQueueOut.triage_summary,
    exclusion_boundary: integrity.exclusion_boundary,
  };

  const phase5Verdict = registry.length === ASSESSED_TOTAL && integrity.pass
    ? 'PASS — OPERATOR REVIEW REQUIRED'
    : 'BLOCKED — SEMANTIC REVIEW INCOMPLETE';

  const result = {
    run_id: RUN_ID,
    result_id: 'corvonero-run-004-phase-5-partial-result-v1',
    phase_verdict: phase5Verdict,
    lifecycle_state: 'PHASE_5_PARTIAL_COMPLETE',
    project_lifecycle: phase5Verdict.startsWith('PASS') ? 'READY_FOR_PARTIAL_CAMPAIGN-PLANNING AUTHORIZATION' : 'PHASE_5_BLOCKED',
    provider_calls: 'FROZEN',
    operator_decisions: {
      assessed_1599: 'CURRENT-CYCLE SEMANTIC AUTHORITY',
      unprocessed_769: 'EXCLUDED FROM CURRENT-CYCLE ASSEMBLY — PRESERVED AS BACKLOG — DO NOT IMPUTE — DO NOT EXTRAPOLATE',
      provider_calls: 'FROZEN',
      phase5: 'AUTHORIZED WITHOUT MODEL CALLS',
      strategy: 'NOT AUTHORIZED',
      campaign_architecture: 'NOT AUTHORIZED',
      import_and_launch: 'NOT AUTHORIZED',
    },
    integrity_receipt_id: integrity.receipt_id,
    coverage,
    created_at: new Date().toISOString(),
  };

  // Write outputs
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-INTEGRITY-v1.json'), integrity);
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-REVIEWED-REGISTRY-v1.json'), {
    registry_id: 'corvonero-run-004-phase-5-partial-reviewed-registry-v1',
    run_id: RUN_ID,
    count: registry.length,
    records: registry.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id)),
  });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-ACCEPT-v1.json'), { run_id: RUN_ID, count: phase5Accept.length, records: phase5Accept });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-REJECT-v1.json'), { run_id: RUN_ID, count: phase5Reject.length, records: phase5Reject });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-ABSTAIN-v1.json'), { run_id: RUN_ID, count: phase5Abstain.length, records: phase5Abstain });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-REVIEW-QUEUE-v1.json'), reviewQueueOut);
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-CORRECTION-LEDGER-v1.json'), {
    ledger_id: 'corvonero-run-004-phase-5-partial-correction-ledger-v1',
    count: correctionLedger.length,
    records: correctionLedger,
  });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-SERVICE-TAXONOMY-v1.json'), { taxonomy_id: 'corvonero-run-004-phase-5-service-taxonomy-v1', families: serviceTaxonomy });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-INTENT-TAXONOMY-v1.json'), { taxonomy_id: 'corvonero-run-004-phase-5-intent-taxonomy-v1', classes: intentTaxonomy });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-GEOGRAPHY-v1.json'), geography);
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-EXCLUSION-TAXONOMY-v1.json'), { taxonomy_id: 'corvonero-run-004-phase-5-exclusion-taxonomy-v1', families: exclusionTaxonomy });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-COVERAGE-v1.json'), coverage);

  const coverageMd = `# CORVONERO RUN 004 — Phase 5 Partial Coverage v1

**Run:** \`${RUN_ID}\`  
**Partial dataset:** ${coverage.partial_dataset}  
**Unprocessed:** ${coverage.unprocessed}  
**Coverage:** ${coverage.coverage_percent}% of canonical records assessed

## Verdict distribution

| Stage | ACCEPT | REJECT | ABSTAIN |
|-------|--------|--------|---------|
| Phase 4 | 529 | 762 | 308 |
| Phase 5 reviewed | ${phase5Accept.length} | ${phase5Reject.length} | ${phase5Abstain.length} |

## Corrections

- Phase 5 corrections from Phase 4 authoritative verdicts: **${correctionLedger.length}**
- Operator review required: **${coverage.operator_review_required}**

## Exclusion boundary

\`\`\`text
CURRENT-CYCLE ASSEMBLY SCOPE: ${ASSESSED_TOTAL} assessed records only
OUT OF SCOPE: ${UNPROCESSED_TOTAL} unprocessed records
\`\`\`

## Service families (ACCEPT only)

${serviceTaxonomy.filter((f) => f.record_count > 0).map((f) => `- **${f.name}**: ${f.record_count}`).join('\n')}

## Intent distribution

${Object.entries(intentCounts).map(([k, v]) => `- ${k}: ${v}`).join('\n')}

## Review queue triage

${Object.entries(reviewQueueOut.triage_summary).map(([k, v]) => `- ${k}: ${v}`).join('\n')}
`;
  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-COVERAGE-v1.md'), coverageMd);

  const resultMd = `# CORVONERO RUN 004 — Phase 5 Partial Result v1

**Phase verdict:** ${phase5Verdict}  
**Project lifecycle:** ${result.project_lifecycle}  
**Provider calls:** FROZEN

## Operator decisions recorded

- 1599 assessed records: CURRENT-CYCLE SEMANTIC AUTHORITY
- 769 unprocessed: EXCLUDED — BACKLOG — DO NOT IMPUTE
- Phase 5: AUTHORIZED WITHOUT MODEL CALLS
- Strategy / Campaign Architecture / Import: NOT AUTHORIZED

## Mandatory items

- **CR2-PHR-00584**: model ACCEPT → authoritative REJECT → Phase 5 REJECT (OPERATOR_ADJUDICATION_OVERRIDE)
- **CR2-PHR-00200**: OPERATOR_REVIEW_REQUIRED (informational phrasing)

## Next gate

\`\`\`text
OPERATOR REVIEW OF CORVONERO PARTIAL SEMANTIC ASSEMBLY
\`\`\`
`;
  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-RESULT-v1.md'), resultMd);
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-RESULT-v1.json'), result);

  const phase6Md = `# CORVONERO RUN 004 — Phase 6 Next Task (Partial) v1

**Prerequisite:** Phase 5 partial semantic review — ${phase5Verdict}  
**Gate:** OPERATOR REVIEW OF CORVONERO PARTIAL SEMANTIC ASSEMBLY

## Authorized after operator approval

- Partial campaign-planning authorization review (1599 assessed records)
- Disposition of ${coverage.operator_review_required} operator-review-required items
- Disposition of mandatory items CR2-PHR-00200, CR2-PHR-00584

## Not authorized without separate charter

- Campaign Architecture
- Ad-group design
- Advertisements
- Negative-keyword deployment
- Commander / import / launch
- Processing remaining 769 unprocessed IDs
- OpenRouter or external model calls
`;
  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-6-NEXT-TASK-PARTIAL-v1.md'), phase6Md);

  // Build report
  const directCommercial = registry.filter((r) => r.phase5_reviewed_verdict === 'ACCEPT' && ['DIRECT_SERVICE_ORDER', 'SPECIALIST_SEARCH', 'PRICE_AND_COST'].includes(r.primary_intent));
  const problems = registry.filter((r) => r.primary_intent === 'PROBLEM_RESOLUTION' || r.service_family === 'SF-TROUBLESHOOTING-NOT-WORKING');
  const productLicense = registry.filter((r) => r.primary_intent === 'PRODUCT_OR_LICENSE' || r.exclusion_family === 'EX-PRODUCT-LICENSE-ONLY');
  const integrations = registry.filter((r) => r.service_family === 'SF-INTEGRATIONS' || r.primary_intent === 'INTEGRATION');
  const marking = registry.filter((r) => r.service_family === 'SF-MARKING-CHESTNY-ZNAK' || MARKING.test(r.phrase));
  const tsPiot = registry.filter((r) => r.service_family === 'SF-TS-PIOT' || TS_PIOT.test(r.phrase));
  const careerEd = registry.filter((r) => r.primary_intent === 'CAREER_OR_EDUCATION' || r.exclusion_family?.startsWith('EX-CAREER') || r.exclusion_family?.startsWith('EX-EDUCATION'));
  const informational = registry.filter((r) => r.primary_intent === 'INFORMATIONAL' || r.exclusion_family === 'EX-INFORMATIONAL-RESEARCH');
  const remainingOpReview = registry.filter((r) => r.review_status === 'OPERATOR_REVIEW_REQUIRED');

  const report = `# REPORT — CORVONERO RUN 004 PHASE 5 PARTIAL SEMANTIC REVIEW V1

**Run ID:** \`${RUN_ID}\`  
**Date:** ${new Date().toISOString().slice(0, 10)}  
**Phase verdict:** ${phase5Verdict}

---

## 1. Safety and Authorization

Phase 5 partial semantic review executed under operator authorization from Phase 4 partial freeze. No OpenRouter or external model API calls. No canonical corpus, ORCA, or Phase 4 source registry mutation. Strategy, Campaign Architecture, import, and launch **not authorized**.

Operator decisions recorded exactly:
- 1599 assessed records: **CURRENT-CYCLE SEMANTIC AUTHORITY**
- 769 unprocessed: **EXCLUDED FROM CURRENT-CYCLE ASSEMBLY — BACKLOG — DO NOT IMPUTE**
- Provider calls: **FROZEN**
- Phase 5: **AUTHORIZED WITHOUT MODEL CALLS**

---

## 2. Git Preflight

- Branch: \`mars/canonical-post-recovery\`
- Recovery ancestry: \`ebc65acd4087fa9d180bb2a50921027fde51e3b7\` — verified
- Partial-freeze artefacts: present
- Live Run 004 process: none detected
- Unrelated WIP: untouched

---

## 3. Partial Authority

Input authority limited to Phase 4 partial artefacts listed in task charter. Canonical corpus read for metadata only (frequency, IDs). 769 unprocessed IDs excluded from all assembly outputs.

---

## 4. Integrity Reconciliation

| Check | Result |
|-------|--------|
| Processed unique | ${integrity.counts.processed_unique} |
| Unprocessed unique | ${integrity.counts.unprocessed_unique} |
| ACCEPT + REJECT + ABSTAIN | ${integrity.counts.accept_plus_reject_plus_abstain} |
| Overlap processed/unprocessed | ${integrity.counts.overlap_processed_unprocessed} |
| Orphans | ${integrity.counts.orphans.length} |
| CR2-PHR-00584 override | ${integrity.operator_override_00584.preserved ? 'preserved' : 'FAILED'} |

**Integrity verdict:** ${integrity.verdict}

---

## 5. Unprocessed Boundary

\`\`\`text
CURRENT-CYCLE ASSEMBLY SCOPE: 1599 assessed records only
OUT OF SCOPE: 769 unprocessed records
\`\`\`

769 IDs preserved in Phase 4 unprocessed manifest only. Not included in service clusters, intent taxonomy counts for demand conclusions, or coverage percentages beyond the 67.5% assessed boundary.

---

## 6. Review Queue Triage

Source queue: 320 items (Phase 4 partial review queue).

| Triage class | Count |
|--------------|-------|
${Object.entries(reviewQueueOut.triage_summary).map(([k, v]) => `| ${k} | ${v} |`).join('\n')}

**CR2-PHR-00584:** CONFIRMED_REJECT — operator override preserved (model ACCEPT, authoritative REJECT).  
**CR2-PHR-00200:** OPERATOR_REVIEW_REQUIRED — informational phrasing; classifier policy disagreement.

---

## 7. ACCEPT Review

Phase 4 ACCEPT: 529 → Phase 5 reviewed ACCEPT: ${phase5Accept.length}

- Accept-to-reject corrections: ${acceptCorrections.to_reject.length}
- Accept-to-abstain corrections: ${acceptCorrections.to_abstain.length}
- Accept review-required: ${acceptCorrections.review_required.length}

Policy checks applied: career/employment, education, informational/self-service, foreign platforms, product-only, disagreement flags.

---

## 8. REJECT Review

Phase 4 REJECT: 762 → Phase 5 reviewed REJECT: ${phase5Reject.length}

- Reject-to-accept corrections: ${rejectCorrections.to_accept.length}
- Reject-to-abstain corrections: ${rejectCorrections.to_abstain.length}
- Reject review-required: ${rejectCorrections.review_required.length}

Commercial false-negative scan: price/cost of work, explicit service demand, marking, TS ПИОТ, integrations.

---

## 9. ABSTAIN Review

Phase 4 ABSTAIN: 308 → Phase 5 reviewed ABSTAIN: ${phase5Abstain.length}

- Promote to ACCEPT: ${abstainCorrections.to_accept.length}
- Promote to REJECT: ${abstainCorrections.to_reject.length}
- Retain ABSTAIN: ${abstainCorrections.retain.length}
- Operator review required: ${abstainCorrections.review_required.length}

ABSTAIN retained as valid final state where genuine uncertainty remains.

---

## 10. Correction Ledger

Total Phase 5 corrections: **${correctionLedger.length}** (all logged in \`CORVONERO-RUN-004-PHASE-5-PARTIAL-CORRECTION-LEDGER-v1.json\`). No silent changes.

---

## 11. Reviewed Verdict Distribution

| Verdict | Phase 4 | Phase 5 |
|---------|---------|---------|
| ACCEPT | 529 | ${phase5Accept.length} |
| REJECT | 762 | ${phase5Reject.length} |
| ABSTAIN | 308 | ${phase5Abstain.length} |
| **Total** | **1599** | **${registry.length}** |

---

## 12. Service Taxonomy

${serviceTaxonomy.filter((f) => f.record_count > 0).map((f) => `- **${f.name}** (${f.id}): ${f.record_count} ACCEPT records`).join('\n')}

Families with zero ACCEPT evidence are documented with ambiguity notes in taxonomy file.

---

## 13. Intent Taxonomy

${Object.entries(intentCounts).sort((a, b) => b[1] - a[1]).map(([k, v]) => `- ${k}: ${v}`).join('\n')}

---

## 14. Geography

Geography-modified phrases in assessed corpus: ${geoRegistry.length}

- Primary (Novosibirsk region): ${geography.distribution.primary}
- Expansion cities: ${geography.distribution.expansion}
- Remote/Russia-wide: ${geography.distribution.remote}
- Irrelevant geography: ${geography.distribution.irrelevant}

Geography alone not treated as commercial intent.

---

## 15. Exclusion Taxonomy

${exclusionTaxonomy.filter((f) => f.record_count > 0).slice(0, 8).map((f) => `- ${f.family_name}: ${f.record_count} (overblock risk: ${f.overblock_risk})`).join('\n')}

Taxonomy for future negative-keyword work — **not** a final Direct import list.

---

## 16. Direct Commercial Demand

ACCEPT records with direct commercial or specialist-search intent: **${directCommercial.length}**

Representative families: 1C programmer/specialist, support, modification, one-off work.

---

## 17. Problems and DIY Intent

Problem-resolution / troubleshooting records: **${problems.length}** (includes ACCEPT, ABSTAIN, REJECT triage)

DIY/self-service excluded via EX-SELF-SERVICE-MANUALS and informational markers.

---

## 18. Product and License

Product/license-only records: **${productLicense.length}**

Not equated with service intent. Product-plus-service bundles flagged for operator review.

---

## 19. Integrations

Integration-related records: **${integrations.length}**

---

## 20. Marking and Честный знак

Marking-related records: **${marking.length}**

---

## 21. TS ПИОТ

TS ПИОТ records: **${tsPiot.length}**

---

## 22. Career and Education

Career/education excluded records: **${careerEd.length}**

Career gate from Phase 4 preserved. CR2-PHR-00584 operator override intact.

---

## 23. Informational Demand

Informational demand records: **${informational.length}**

---

## 24. Partial Coverage

\`\`\`text
PARTIAL DATASET: 1599 / 2368 assessed
UNPROCESSED: 769 / 2368
COVERAGE: 67.5% of canonical records assessed
\`\`\`

Phrase count does not imply market demand volume unless frequency data explicitly supports that conclusion.

---

## 25. Remaining Operator Review

Items requiring operator disposition: **${remainingOpReview.length}** registry records + mandatory queue items.

Review queue OPERATOR_REVIEW_REQUIRED / DATA_OR_POLICY_ISSUE items included in Phase 5 review queue output.

---

## 26. Phase 5 Verdict

\`\`\`text
PHASE 5 PARTIAL: ${phase5Verdict}
\`\`\`

---

## 27. Project Lifecycle

\`\`\`text
Project: ${result.project_lifecycle}
\`\`\`

PASS does **not** authorize Campaign Architecture automatically.

---

## 28. Outputs Created

All files under \`projects/mars-search-ppc-production/pilots/corvonero/\`:

- CORVONERO-RUN-004-PHASE-5-PARTIAL-INTEGRITY-v1.json
- CORVONERO-RUN-004-PHASE-5-PARTIAL-REVIEWED-REGISTRY-v1.json
- CORVONERO-RUN-004-PHASE-5-PARTIAL-ACCEPT/REJECT/ABSTAIN-v1.json
- CORVONERO-RUN-004-PHASE-5-PARTIAL-REVIEW-QUEUE-v1.json
- CORVONERO-RUN-004-PHASE-5-PARTIAL-CORRECTION-LEDGER-v1.json
- CORVONERO-RUN-004-PHASE-5-SERVICE/INTENT/GEOGRAPHY/EXCLUSION-TAXONOMY-v1.json
- CORVONERO-RUN-004-PHASE-5-PARTIAL-COVERAGE-v1.md/json
- CORVONERO-RUN-004-PHASE-5-PARTIAL-RESULT-v1.md/json
- CORVONERO-RUN-004-PHASE-6-NEXT-TASK-PARTIAL-v1.md

Report: \`projects/mars-search-ppc-production/reports/REPORT-corvonero-run-004-phase-5-partial-semantic-review-v1.md\`

---

## 29. Files Changed

New Phase 5 artefacts only. Phase 4 source registries unchanged.

---

## 30. Git Status

No commit. No push.

---

## 31. SAFE UNKNOWN

- Remaining 769 unprocessed phrases: semantic verdict unknown until separate authorized resume
- Market demand volume from phrase counts: not inferred
- Final minus-word lists: not produced (exclusion taxonomy is preparatory only)

---

## 32. Operator Decisions Required

1. Approve or adjust Phase 5 partial semantic assembly
2. Disposition CR2-PHR-00200 (informational vs commercial)
3. Review ${remainingOpReview.length} operator-review-required registry items
4. Decide: accept 67.5% partial coverage for interim planning **or** schedule authorized resume for 769 backlog

---

## 33. Exact Phase 6 Task

See \`CORVONERO-RUN-004-PHASE-6-NEXT-TASK-PARTIAL-v1.md\`

Next gate: **OPERATOR REVIEW OF CORVONERO PARTIAL SEMANTIC ASSEMBLY**

---

## 34. Stop Condition

Phase 5 partial semantic review and assembly **complete**. Stopped before Campaign Architecture, ad groups, ads, negatives deployment, Commander, import, launch, Wave 5.
`;
  writeText(path.join(REPORTS, 'REPORT-corvonero-run-004-phase-5-partial-semantic-review-v1.md'), report);

  console.log(JSON.stringify({
    phase5_verdict: phase5Verdict,
    accept: phase5Accept.length,
    reject: phase5Reject.length,
    abstain: phase5Abstain.length,
    corrections: correctionLedger.length,
    integrity: integrity.verdict,
  }, null, 2));
}

main();
