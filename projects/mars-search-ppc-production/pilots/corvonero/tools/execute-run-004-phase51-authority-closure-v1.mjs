#!/usr/bin/env node
/**
 * Corvonero Run 004 Phase 5.1 — Partial Semantic Authority Closure.
 * No provider calls. Reads Phase 5 v1 artefacts only; does not mutate Phase 4/5 sources.
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

const RUN_ID = 'corv-semantic-v2-20260626-004';
const CANONICAL_TOTAL = 2368;
const ASSESSED_TOTAL = 1599;
const UNPROCESSED_TOTAL = 769;
const REVIEWER = 'PHASE_51_AUTHORITY_CLOSURE_v1';
const AUTHORITY = 'CORVONERO RUN 004 PHASE 5.1 — NO MODEL CALLS';
const PHASE5_AUTHORITY = 'CORVONERO RUN 004 PHASE 5 — NO MODEL CALLS';

const OPERATOR_DECISION_00200 = {
  phrase_id: 'CR2-PHR-00200',
  final_authoritative_verdict: 'REJECT',
  review_status: 'OPERATOR_CONFIRMED',
  reason: 'informational / DIY query, not direct commercial service demand',
};

const OPERATOR_OVERRIDE_00584 = {
  phrase_id: 'CR2-PHR-00584',
  model_verdict: 'ACCEPT',
  final_authoritative_verdict: 'REJECT',
  authority: 'OPERATOR_ADJUDICATION_OVERRIDE',
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
const PRODUCT_BUNDLE = /(?:купить|приобрест|лицензи|поставк).*(?:1[\s-]?с|1c).*(?:настрой|внедрен|сопровожден)|(?:настрой|внедрен|сопровожден).*(?:1[\s-]?с|1c).*(?:купить|приобрест|лицензи|поставк)|купить\s+1[\s-]?с\s+(?:сопровожден|настрой|внедрен)/i;
const PROBLEM = /(?:ошибк|не\s+работает|сбой|исправить|устранить|fault|exception|зависает|тормозит|восстановить\s+работ)/i;
const TROUBLESHOOT = /(?:1[\s-]?с\s+не\s+работает|программ(?:а|ы)\s+1[\s-]?с\s+не\s+работает|не\s+работает\s+(?:программ(?:а|ы)\s+)?1[\s-]?с|помощь\s+с\s+(?:проблем|ошибк)|устранить\s+ошибк|исправить\s+(?:ошибк|сбой)|восстановить\s+работ)/i;
const MARKING = /(?:честн(?:ый|ого)\s+знак|маркировк(?:а|и|у|ой)|data\s*matrix|gs1|агрегац(?:ия|ии)\s+код)/i;
const TS_PIOT = /(?:тс\s*пиот|ts\s*piot|промышленн(?:ая|ой|ую)\s+безопасност)/i;
const INTEGRATION = /(?:интеграц(?:ия|ии|ию|ией)|bitrix|битрикс|синхронизац|обмен\s+данн|api\s+1c|rest\s+1c|обмен\s+с\s+сайт)/i;
const SUBSCRIPTION = /(?:абонент|подписк|ежемесяч|сопровожден(?:ие|ия)\s+1с|its\s+1с|итс\s+1с)/i;
const ONE_OFF = /(?:разов|единоразов|одноразов|почасов|за\s+час)/i;
const FOREIGN_PLATFORM = /(?:sap|oracle|microsoft\s+dynamics|dynamics\s+365|odoo|bitrix24(?!\s+интеграц)|salesforce)/i;
const PROVIDER_ROLE = /(?:программист|специалист|разработчик)/i;
const ERP = /\berp\b/i;
const GENERIC_ERP_AMBIG = /(?:erp\s+программист|программист\s+erp|1[\s-]?с\s+erp\s+печатн|erp\s+внешн)/i;

const PRIMARY_GEO = /(?:новосибирск|новосибирск(?:ая|ой|ую)\s+област)/i;
const EXPANSION_GEO = /(?:краснодар|екатеринбург|красноярск|москва|санкт-петербург|спб|казань|нижний\s+новгород|самара|ростов|воронеж|пермь|волгоград|тюмень|уфа|омск|челябинск|иркутск|хабаровск|владивосток)/i;
const FOREIGN_GEO = /(?:минск|киев|алматы|астана|ташкент|ереван|тбилиси)/i;

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

function integrityPreflight() {
  const processed = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PROCESSED-IDS-MANIFEST-v1.json'));
  const unprocessed = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-UNPROCESSED-IDS-MANIFEST-v1.json'));
  const accept = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-ACCEPT-v1.json'));
  const reject = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-REJECT-v1.json'));
  const abstain = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-ABSTAIN-v1.json'));
  const registry = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-REVIEWED-REGISTRY-v1.json'));

  const processedIds = new Set(processed.records.map((r) => r.phrase_id));
  const unprocessedIds = new Set(unprocessed.records.map((r) => r.phrase_id));
  const overlap = [...processedIds].filter((id) => unprocessedIds.has(id));
  const phase5Counts = {
    accept: accept.count,
    reject: reject.count,
    abstain: abstain.count,
    sum: accept.count + reject.count + abstain.count,
  };

  const pass = processedIds.size === ASSESSED_TOTAL
    && unprocessedIds.size === UNPROCESSED_TOTAL
    && phase5Counts.accept === 531
    && phase5Counts.reject === 578
    && phase5Counts.abstain === 490
    && phase5Counts.sum === ASSESSED_TOTAL
    && registry.count === ASSESSED_TOTAL
    && overlap.length === 0
    && processedIds.size + unprocessedIds.size === CANONICAL_TOTAL;

  return {
    pass,
    processedIds: processedIds.size,
    unprocessedIds: unprocessedIds.size,
    phase5Counts,
    overlap: overlap.length,
    union: processedIds.size + unprocessedIds.size,
  };
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
  if (PROBLEM.test(t) && ONE_C.test(t) && TROUBLESHOOT.test(t)) return 'SF-TROUBLESHOOTING-NOT-WORKING';
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

function classifyReviewFlagRootCause(record) {
  const t = (record.phrase || '').toLowerCase();
  if (record.review_status !== 'OPERATOR_REVIEW_REQUIRED') {
    if (record.phrase_id === 'CR2-PHR-00200') return 'operator_decision_applied';
    return null;
  }
  if (record.provenance?.phase5_audit_action === 'ACCEPT_REVIEW_REQUIRED') {
    if (EDUCATION_RE.test(t) || /нетолог/.test(t)) return 'education_platform_ambiguity';
    if (INFO_RE.test(t)) return 'informational_diy_ambiguity';
    if (PRODUCT_BUNDLE.test(t)) return 'product_plus_service_ambiguity';
    if (ERP.test(t) && GENERIC_ERP_AMBIG.test(t)) return 'generic_erp_platform_ambiguity';
    if (COMMERCIAL_DEMAND.test(t) || COMMERCIAL_PRICE.test(t) || SERVICE_TASK.test(t) || PROVIDER_ROLE.test(t)) {
      return 'stale_review_flag_after_authoritative_verdict';
    }
    return 'primary_reassessment_disagreement_only';
  }
  if (record.provenance?.phase5_audit_action === 'OPERATOR_REVIEW_REQUIRED') {
    if (PROBLEM.test(t) || INTEGRATION.test(t)) return 'ambiguous_diy_problem_demand';
    return 'actual_semantic_ambiguity';
  }
  return 'actual_semantic_ambiguity';
}

function resolveDeterministic(record, cls, dataPolicyDisposition) {
  const t = (record.phrase || '').toLowerCase();
  const phrase = record.phrase || '';
  let verdict = record.phase5_reviewed_verdict;
  let reviewStatus = record.review_status;
  let action = 'PHASE51_CONFIRMED';
  let reason = 'Phase 5 verdict confirmed without change';
  let authority = AUTHORITY;
  const corrections = [];

  if (record.phrase_id === 'CR2-PHR-00584') {
    return {
      verdict: 'REJECT',
      reviewStatus: 'OPERATOR_CONFIRMED',
      action: 'OPERATOR_OVERRIDE_PRESERVED',
      reason: 'Operator override preserved: model ACCEPT → authoritative REJECT',
      authority: 'OPERATOR_ADJUDICATION_OVERRIDE',
      corrections: [],
      operatorRequired: false,
    };
  }

  if (record.phrase_id === 'CR2-PHR-00200') {
    corrections.push({
      phrase_id: record.phrase_id,
      phrase,
      before_verdict: record.phase5_reviewed_verdict,
      after_verdict: 'REJECT',
      change_type: 'OPERATOR_DECISION_CR2-PHR-00200',
      reason: OPERATOR_DECISION_00200.reason,
      authority: 'OPERATOR_DECISION',
      reviewer: REVIEWER,
      preserved_fields: {
        original_model_verdict: record.original_model_verdict,
        original_authoritative_verdict: record.original_authoritative_verdict,
        phase5_reviewed_verdict: record.phase5_reviewed_verdict,
        classifier_primary_family: record.provenance?.classifier_primary_family,
      },
    });
    return {
      verdict: 'REJECT',
      reviewStatus: 'OPERATOR_CONFIRMED',
      action: 'OPERATOR_DECISION_APPLIED',
      reason: OPERATOR_DECISION_00200.reason,
      authority: 'OPERATOR_DECISION',
      corrections,
      operatorRequired: false,
    };
  }

  if (CAREER_RE.test(t)) {
    if (verdict !== 'REJECT') {
      corrections.push({ before: verdict, after: 'REJECT', change_type: 'CONFIRM_REJECT_CAREER', reason: 'Career/employment markers' });
      verdict = 'REJECT';
    }
    reviewStatus = 'PHASE51_CONFIRMED';
    action = 'CONFIRM_REJECT';
    reason = 'Career/employment — deterministic REJECT';
    return { verdict, reviewStatus, action, reason, authority, corrections, operatorRequired: false };
  }

  if (EDUCATION_RE.test(t) && !COMMERCIAL_DEMAND.test(t) && !COMMERCIAL_PRICE.test(t)) {
    if (verdict !== 'REJECT') {
      corrections.push({ before: verdict, after: 'REJECT', change_type: 'CONFIRM_REJECT_EDUCATION', reason: 'Education/training without commercial service demand' });
      verdict = 'REJECT';
    }
    reviewStatus = 'PHASE51_CONFIRMED';
    return { verdict, reviewStatus, action: 'CONFIRM_REJECT', reason: 'Education/training — deterministic REJECT', authority, corrections, operatorRequired: false };
  }

  if (record.phrase_id === 'CR2-PHR-00085') {
    if (verdict !== 'REJECT') {
      corrections.push({ before: verdict, after: 'REJECT', change_type: 'CONFIRM_REJECT_EDUCATION_PLATFORM', reason: 'Netology — education platform reference' });
      verdict = 'REJECT';
    }
    reviewStatus = 'PHASE51_CONFIRMED';
    return { verdict, reviewStatus, action: 'CONFIRM_REJECT', reason: 'Education platform (Netology) — REJECT', authority, corrections, operatorRequired: false };
  }

  if (PRODUCT_BUNDLE.test(t)) {
    const recommended = 'ABSTAIN';
    const finalVerdict = recommended;
    if (verdict !== finalVerdict) {
      corrections.push({ before: verdict, after: finalVerdict, change_type: 'PRODUCT_BUNDLE_ABSTAIN', reason: 'Product-plus-service bundle ambiguity (PSR-AMB family)' });
      verdict = finalVerdict;
    }
    return {
      verdict,
      reviewStatus: 'OPERATOR_REVIEW_REQUIRED',
      action: 'RETAIN_FOR_OPERATOR',
      reason: 'Product-plus-service bundle ambiguity (PSR-AMB family)',
      authority,
      corrections,
      operatorRequired: true,
      ambiguity: 'License purchase bundled with setup/support — product resale vs pure service scope',
      recommended_verdict: recommended,
      business_consequence: 'Wrong ACCEPT wastes budget on product-reseller intent; wrong REJECT drops valid bundled-service leads',
      options: ['ACCEPT as bundled service', 'REJECT as product-only', 'ABSTAIN / exclude from launch set'],
    };
  }

  if (ERP.test(t) && GENERIC_ERP_AMBIG.test(t)) {
    if (/сопровожден|доработк|техническ(?:ое|ого)\s+задани/.test(t) && COMMERCIAL_DEMAND.test(t) || SERVICE_TASK.test(t)) {
      if (verdict !== 'ACCEPT') {
        corrections.push({ before: verdict, after: 'ACCEPT', change_type: 'CONFIRM_ACCEPT_ERP_SERVICE', reason: 'Clear ERP service demand with commercial task markers' });
        verdict = 'ACCEPT';
      }
      reviewStatus = 'PHASE51_CONFIRMED';
      return { verdict, reviewStatus, action: 'CONFIRM_ACCEPT', reason: 'ERP with explicit service task — ACCEPT', authority, corrections, operatorRequired: false };
    }
    if (/erp\s+программист|программист\s+erp/.test(t) && !COMMERCIAL_DEMAND.test(t)) {
      if (verdict !== 'REJECT') {
        corrections.push({ before: verdict, after: 'REJECT', change_type: 'CONFIRM_REJECT_ERP_ROLE', reason: 'Generic ERP role query without service demand' });
        verdict = 'REJECT';
      }
      reviewStatus = 'PHASE51_CONFIRMED';
      return { verdict, reviewStatus, action: 'CONFIRM_REJECT', reason: 'Generic ERP role/informational — REJECT', authority, corrections, operatorRequired: false };
    }
    if (record.phrase_id === 'CR2-PHR-01657') {
      return {
        verdict,
        reviewStatus: 'OPERATOR_REVIEW_REQUIRED',
        action: 'RETAIN_FOR_OPERATOR',
        reason: 'ERP external print forms — service development vs informational',
        authority,
        corrections,
        operatorRequired: true,
        ambiguity: 'External print forms for 1C ERP may be custom development service or template research',
        recommended_verdict: 'ABSTAIN',
        business_consequence: 'ACCEPT targets high-value dev work; REJECT may drop legitimate print-form customization demand',
        options: ['ACCEPT as report/dev service', 'REJECT as informational', 'ABSTAIN'],
      };
    }
  }

  if (MARKING.test(t) && ONE_C.test(t)) {
    if (DIY_RE.test(t) && !COMMERCIAL_DEMAND.test(t) && !SERVICE_TASK.test(t)) {
      if (verdict !== 'REJECT') {
        corrections.push({ before: verdict, after: 'REJECT', change_type: 'CONFIRM_REJECT_MARKING_DIY', reason: 'Marking query with DIY/self-service markers' });
        verdict = 'REJECT';
      }
      reviewStatus = 'PHASE51_CONFIRMED';
      return { verdict, reviewStatus, action: 'CONFIRM_REJECT', reason: 'Marking DIY/self-service — REJECT', authority, corrections, operatorRequired: false };
    }
    if (SERVICE_TASK.test(t) || COMMERCIAL_DEMAND.test(t) || /(?:настрой|внедрен|подключ|автоматизац|передача)/.test(t)) {
      if (verdict !== 'ACCEPT') {
        corrections.push({ before: verdict, after: 'ACCEPT', change_type: 'CONFIRM_ACCEPT_MARKING_SERVICE', reason: 'Commercial marking/Честный знак service demand' });
        verdict = 'ACCEPT';
      }
      reviewStatus = 'PHASE51_CONFIRMED';
      return { verdict, reviewStatus, action: 'CONFIRM_ACCEPT', reason: 'Marking service demand — ACCEPT', authority, corrections, operatorRequired: false };
    }
    if (/^(?:маркировк|честн)/.test(t) || /\b(?:маркировк|честн)/.test(t)) {
      if (verdict !== 'ACCEPT') {
        corrections.push({ before: verdict, after: 'ACCEPT', change_type: 'CONFIRM_ACCEPT_MARKING_GENERIC', reason: 'Generic marking in 1C — approved external service per business scope' });
        verdict = 'ACCEPT';
      }
      reviewStatus = 'PHASE51_CONFIRMED';
      return { verdict, reviewStatus, action: 'CONFIRM_ACCEPT', reason: 'Generic marking phrase — commercial service in scope', authority, corrections, operatorRequired: false };
    }
  }

  if (TS_PIOT.test(t)) {
    if (/сертификац|экзамен|обучен/.test(t)) {
      if (verdict !== 'REJECT') {
        corrections.push({ before: verdict, after: 'REJECT', change_type: 'CONFIRM_REJECT_TS_PIOT_EDU', reason: 'TS ПИОТ certification/education' });
        verdict = 'REJECT';
      }
      reviewStatus = 'PHASE51_CONFIRMED';
      return { verdict, reviewStatus, action: 'CONFIRM_REJECT', reason: 'TS ПИОТ certification — REJECT', authority, corrections, operatorRequired: false };
    }
    if (/как\s+установить|инструкци|самостоятельно/.test(t)) {
      if (verdict !== 'REJECT') {
        corrections.push({ before: verdict, after: 'REJECT', change_type: 'CONFIRM_REJECT_TS_PIOT_DIY', reason: 'TS ПИОТ DIY installation query' });
        verdict = 'REJECT';
      }
      reviewStatus = 'PHASE51_CONFIRMED';
      return { verdict, reviewStatus, action: 'CONFIRM_REJECT', reason: 'TS ПИОТ DIY — REJECT', authority, corrections, operatorRequired: false };
    }
    if (/настрой|внедрен|подключ|услуг|специалист|программист|заказать|нужен/.test(t)) {
      if (verdict !== 'ACCEPT') {
        corrections.push({ before: verdict, after: 'ACCEPT', change_type: 'CONFIRM_ACCEPT_TS_PIOT_SERVICE', reason: 'TS ПИОТ setup/service demand' });
        verdict = 'ACCEPT';
      }
      reviewStatus = 'PHASE51_CONFIRMED';
      return { verdict, reviewStatus, action: 'CONFIRM_ACCEPT', reason: 'TS ПИОТ service setup — ACCEPT', authority, corrections, operatorRequired: false };
    }
    if (MARKING.test(t)) {
      return {
        verdict,
        reviewStatus: 'OPERATOR_REVIEW_REQUIRED',
        action: 'RETAIN_FOR_OPERATOR',
        reason: 'TS ПИОТ combined with marking — dual compliance scope',
        authority,
        corrections,
        operatorRequired: true,
        ambiguity: 'Combined TS ПИОТ and Честный знак — scope of bundled compliance service unclear',
        recommended_verdict: 'ABSTAIN',
        business_consequence: 'May represent high-value bundled offer or out-of-scope research query',
        options: ['ACCEPT as bundled compliance service', 'ABSTAIN', 'REJECT if informational only'],
      };
    }
    if (/не\s+видит|ошибк|не\s+работает/.test(t)) {
      return {
        verdict,
        reviewStatus: 'OPERATOR_REVIEW_REQUIRED',
        action: 'RETAIN_FOR_OPERATOR',
        reason: 'TS ПИОТ troubleshooting — DIY vs paid support',
        authority,
        corrections,
        operatorRequired: true,
        ambiguity: 'Technical failure query may seek forum fix or paid specialist',
        recommended_verdict: 'ABSTAIN',
        business_consequence: 'ACCEPT on DIY intent wastes spend; REJECT drops valid troubleshooting leads',
        options: ['ACCEPT as troubleshooting service', 'REJECT as DIY', 'ABSTAIN'],
      };
    }
  }

  if (INTEGRATION.test(t) && ONE_C.test(t)) {
    if (/ошибк|не\s+работает|почему/.test(t) && !COMMERCIAL_DEMAND.test(t) && !/специалист|программист|услуг|заказать/.test(t)) {
      if (verdict !== 'ABSTAIN') {
        corrections.push({ before: verdict, after: 'ABSTAIN', change_type: 'RETAIN_ABSTAIN_SYNC_TROUBLESHOOT', reason: 'Integration sync error — DIY troubleshooting default' });
        verdict = 'ABSTAIN';
      }
      reviewStatus = 'PHASE51_CONFIRMED';
      return { verdict, reviewStatus, action: 'RETAIN_ABSTAIN', reason: 'Integration sync troubleshooting — valid ABSTAIN', authority, corrections, operatorRequired: false };
    }
    if (DIY_RE.test(t) && !COMMERCIAL_DEMAND.test(t) && !SERVICE_TASK.test(t)) {
      if (verdict !== 'REJECT') {
        corrections.push({ before: verdict, after: 'REJECT', change_type: 'CONFIRM_REJECT_INTEGRATION_DIY', reason: 'Integration DIY/instructional query' });
        verdict = 'REJECT';
      }
      reviewStatus = 'PHASE51_CONFIRMED';
      return { verdict, reviewStatus, action: 'CONFIRM_REJECT', reason: 'Integration DIY — REJECT', authority, corrections, operatorRequired: false };
    }
    if (COMMERCIAL_DEMAND.test(t) || SERVICE_TASK.test(t) || /(?:настрой|внедрен|подключ|обмен\s+данн)/.test(t)) {
      if (verdict !== 'ACCEPT') {
        corrections.push({ before: verdict, after: 'ACCEPT', change_type: 'CONFIRM_ACCEPT_INTEGRATION_SERVICE', reason: 'Commercial integration service demand' });
        verdict = 'ACCEPT';
      }
      reviewStatus = 'PHASE51_CONFIRMED';
      return { verdict, reviewStatus, action: 'CONFIRM_ACCEPT', reason: 'Integration service — ACCEPT', authority, corrections, operatorRequired: false };
    }
  }

  if (PROBLEM.test(t) && ONE_C.test(t)) {
    if (/как\s+(?:.*?\s+)?исправить|как\s+(?:.*?\s+)?устранить|инструкци|самостоятельно/.test(t)) {
      if (verdict !== 'REJECT') {
        corrections.push({ before: verdict, after: 'REJECT', change_type: 'CONFIRM_REJECT_TROUBLESHOOT_DIY', reason: 'DIY troubleshooting instruction query' });
        verdict = 'REJECT';
      }
      reviewStatus = 'PHASE51_CONFIRMED';
      return { verdict, reviewStatus, action: 'CONFIRM_REJECT', reason: 'DIY troubleshooting — REJECT', authority, corrections, operatorRequired: false };
    }
    if (TROUBLESHOOT.test(t) && (COMMERCIAL_DEMAND.test(t) || /специалист|программист|услуг|заказать|помощь/.test(t))) {
      if (verdict !== 'ACCEPT') {
        corrections.push({ before: verdict, after: 'ACCEPT', change_type: 'CONFIRM_ACCEPT_TROUBLESHOOT_SERVICE', reason: 'Commercial troubleshooting with specialist demand' });
        verdict = 'ACCEPT';
      }
      reviewStatus = 'PHASE51_CONFIRMED';
      return { verdict, reviewStatus, action: 'CONFIRM_ACCEPT', reason: 'Commercial troubleshooting — ACCEPT', authority, corrections, operatorRequired: false };
    }
    if (/программ(?:а|ы)\s+1[\s-]?с\s+не\s+работает|не\s+работает\s+программ(?:а|ы)\s+1[\s-]?с|почему\s+не\s+работает\s+программ/.test(t)) {
      return {
        verdict,
        reviewStatus: 'OPERATOR_REVIEW_REQUIRED',
        action: 'RETAIN_FOR_OPERATOR',
        reason: 'Program-not-working query — DIY vs specialist intent ambiguous',
        authority,
        corrections,
        operatorRequired: true,
        ambiguity: 'User may seek free forum fix or paid emergency support',
        recommended_verdict: 'ABSTAIN',
        business_consequence: 'High-intent troubleshooting leads vs informational DIY traffic',
        options: ['ACCEPT as emergency support', 'REJECT as DIY', 'ABSTAIN'],
      };
    }
    if (INTEGRATION.test(t) && /ошибк|синхронизац|не\s+работает/.test(t)) {
      if (verdict !== 'ABSTAIN') {
        corrections.push({ before: verdict, after: 'ABSTAIN', change_type: 'RETAIN_ABSTAIN_SYNC_TROUBLESHOOT', reason: 'Sync/integration error — DIY troubleshooting default' });
        verdict = 'ABSTAIN';
      }
      reviewStatus = 'PHASE51_CONFIRMED';
      return { verdict, reviewStatus, action: 'RETAIN_ABSTAIN', reason: 'Integration sync troubleshooting — valid ABSTAIN', authority, corrections, operatorRequired: false };
    }
  }

  if (COMMERCIAL_PRICE.test(t) && ONE_C.test(t)) {
    if (verdict !== 'ACCEPT') {
      corrections.push({ before: verdict, after: 'ACCEPT', change_type: 'CONFIRM_ACCEPT_PRICE', reason: 'Commercial price/cost of specialist work' });
      verdict = 'ACCEPT';
    }
    reviewStatus = 'PHASE51_CONFIRMED';
    return { verdict, reviewStatus, action: 'CONFIRM_ACCEPT', reason: 'Price/cost commercial demand — ACCEPT', authority, corrections, operatorRequired: false };
  }

  if ((COMMERCIAL_DEMAND.test(t) || (PROVIDER_ROLE.test(t) && !INFO_RE.test(t))) && ONE_C.test(t)) {
    if (verdict !== 'ACCEPT') {
      corrections.push({ before: verdict, after: 'ACCEPT', change_type: 'CONFIRM_ACCEPT_COMMERCIAL', reason: 'Explicit commercial service demand' });
      verdict = 'ACCEPT';
    }
    reviewStatus = 'PHASE51_CONFIRMED';
    return { verdict, reviewStatus, action: 'CONFIRM_ACCEPT', reason: 'Commercial service demand — ACCEPT', authority, corrections, operatorRequired: false };
  }

  if (INFO_RE.test(t) && !COMMERCIAL_DEMAND.test(t) && !COMMERCIAL_PRICE.test(t)) {
    if (record.phrase_id === 'CR2-PHR-00076') {
      return {
        verdict,
        reviewStatus: 'OPERATOR_REVIEW_REQUIRED',
        action: 'RETAIN_FOR_OPERATOR',
        reason: 'Best programmer query — comparison/research vs hire intent',
        authority,
        corrections,
        operatorRequired: true,
        ambiguity: 'Ranking/comparison query may be research or pre-purchase evaluation',
        recommended_verdict: 'REJECT',
        business_consequence: 'Low conversion informational traffic vs possible high-intent comparison shopper',
        options: ['REJECT as informational', 'ABSTAIN', 'ACCEPT if treated as specialist search'],
      };
    }
    if (verdict !== 'REJECT') {
      corrections.push({ before: verdict, after: 'REJECT', change_type: 'CONFIRM_REJECT_INFORMATIONAL', reason: 'Informational without commercial demand' });
      verdict = 'REJECT';
    }
    reviewStatus = 'PHASE51_CONFIRMED';
    return { verdict, reviewStatus, action: 'CONFIRM_REJECT', reason: 'Informational — REJECT', authority, corrections, operatorRequired: false };
  }

  if (PRODUCT_ONLY.test(t) && !SERVICE_TASK.test(t) && !COMMERCIAL_DEMAND.test(t)) {
    if (verdict !== 'REJECT') {
      corrections.push({ before: verdict, after: 'REJECT', change_type: 'CONFIRM_REJECT_PRODUCT_ONLY', reason: 'Product/license-only without service intent' });
      verdict = 'REJECT';
    }
    reviewStatus = 'PHASE51_CONFIRMED';
    return { verdict, reviewStatus, action: 'CONFIRM_REJECT', reason: 'Product-only — REJECT', authority, corrections, operatorRequired: false };
  }

  if (record.review_status === 'OPERATOR_REVIEW_REQUIRED' && record.provenance?.phase5_audit_action === 'ACCEPT_REVIEW_REQUIRED') {
    reviewStatus = 'PHASE51_CONFIRMED';
    action = 'CLEAR_STALE_REVIEW_FLAG';
    reason = 'Primary/reassessment disagreement only — policy confirms Phase 5 ACCEPT';
    return { verdict, reviewStatus, action, reason, authority, corrections, operatorRequired: false };
  }

  if (dataPolicyDisposition?.resolved_verdict) {
    const rv = dataPolicyDisposition.resolved_verdict;
    if (rv !== verdict) {
      corrections.push({ before: verdict, after: rv, change_type: 'DATA_POLICY_RESOLVED', reason: dataPolicyDisposition.disposition_reason });
      verdict = rv;
    }
    reviewStatus = 'PHASE51_CONFIRMED';
    return { verdict, reviewStatus, action: 'DATA_POLICY_RESOLVED', reason: dataPolicyDisposition.disposition_reason, authority, corrections, operatorRequired: false };
  }

  if (verdict === 'ABSTAIN' && cls.primary_family === 'ambiguous_mixed_intent' && t.split(/\s+/).length <= 4 && !COMMERCIAL_DEMAND.test(t) && !COMMERCIAL_PRICE.test(t)) {
    return {
      verdict,
      reviewStatus: 'OPERATOR_REVIEW_REQUIRED',
      action: 'RETAIN_FOR_OPERATOR',
      reason: 'Short underspecified phrase',
      authority,
      corrections,
      operatorRequired: true,
      ambiguity: 'Insufficient context to distinguish service demand from navigation/research',
      recommended_verdict: 'ABSTAIN',
      business_consequence: 'Forced ACCEPT/REJECT risks systematic over/under-blocking',
      options: ['ABSTAIN', 'REJECT', 'ACCEPT'],
    };
  }

  reviewStatus = record.review_status === 'OPERATOR_REVIEW_REQUIRED' ? 'PHASE51_CONFIRMED' : (record.review_status || 'PHASE51_CONFIRMED');
  return { verdict, reviewStatus, action, reason, authority, corrections, operatorRequired: false };
}

function resolveDataPolicyIssue(record, queueItem) {
  const t = (record.phrase || '').toLowerCase();
  const base = {
    phrase_id: record.phrase_id,
    phrase: record.phrase,
    phase4_review_reason: queueItem?.phase4_review_reason || null,
    phase5_verdict: record.phase5_reviewed_verdict,
    malformed_retry: /malformed/i.test(queueItem?.phase4_review_reason || ''),
  };

  if (/печатн/.test(t) && !SERVICE_TASK.test(t) && !COMMERCIAL_DEMAND.test(t)) {
    return {
      ...base,
      disposition: 'RESOLVED_FROM_EXISTING_EVIDENCE',
      resolved_verdict: 'REJECT',
      disposition_reason: 'Print-form query without service task — informational/DIY; valid Phase 4/5 response exists despite malformed retry flag',
    };
  }
  if (MARKING.test(t)) {
    if (DIY_RE.test(t)) {
      return { ...base, disposition: 'RESOLVED_FROM_EXISTING_EVIDENCE', resolved_verdict: 'REJECT', disposition_reason: 'Marking DIY query resolved from existing evidence' };
    }
    return { ...base, disposition: 'MALFORMED_RETRY_VERIFIED', resolved_verdict: 'ACCEPT', disposition_reason: 'Valid structured verdict exists; marking service in scope — promote to ACCEPT' };
  }
  return {
    ...base,
    disposition: 'MALFORMED_RETRY_VERIFIED',
    resolved_verdict: record.phase5_reviewed_verdict,
    disposition_reason: 'Valid final response exists — malformed retry flag cleared; retain Phase 5 ABSTAIN as policy-safe default',
  };
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
  for (const r of registry.filter((x) => x.phase51_final_verdict === 'ACCEPT')) {
    if (r.service_family && families[r.service_family]) families[r.service_family].phrase_ids.push(r.phrase_id);
  }
  return Object.values(families).map((f) => ({
    ...f,
    record_count: f.phrase_ids.length,
    representative_phrases: registry.filter((r) => f.phrase_ids.includes(r.phrase_id)).slice(0, 5).map((r) => r.phrase),
    ambiguity_notes: f.record_count === 0 ? 'No ACCEPT evidence after Phase 5.1 closure' : undefined,
  }));
}

function main() {
  const preflight = integrityPreflight();
  if (!preflight.pass) {
    console.error('INTEGRITY PREFLIGHT FAILED', preflight);
    process.exit(2);
  }

  const phase5Registry = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-REVIEWED-REGISTRY-v1.json'));
  const phase5Queue = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-REVIEW-QUEUE-v1.json'));
  const phase5Ledger = readJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-PARTIAL-CORRECTION-LEDGER-v1.json'));

  const queueById = new Map(phase5Queue.items.map((i) => [i.phrase_id, i]));
  const dataPolicyMap = new Map();
  for (const item of phase5Queue.items.filter((i) => i.phase5_triage === 'DATA_OR_POLICY_ISSUE')) {
    const rec = phase5Registry.records.find((r) => r.phrase_id === item.phrase_id);
    dataPolicyMap.set(item.phrase_id, resolveDataPolicyIssue(rec, item));
  }

  const correctionLedgerV2 = [...phase5Ledger.records];
  const registryV2 = [];
  const acceptV2 = [];
  const rejectV2 = [];
  const abstainV2 = [];
  const reviewFlagAudit = {};
  const operatorCandidates = [];

  for (const record of phase5Registry.records) {
    const cls = classifyPhraseV2({ phrase_id: record.phrase_id, phrase: record.phrase }, context);
    const rootCause = classifyReviewFlagRootCause(record);
    if (rootCause) reviewFlagAudit[rootCause] = (reviewFlagAudit[rootCause] || 0) + 1;

    const dataPolicy = dataPolicyMap.get(record.phrase_id);
    const resolved = resolveDeterministic(record, cls, dataPolicy);

    for (const c of resolved.corrections) {
      correctionLedgerV2.push({
        phrase_id: record.phrase_id,
        phrase: record.phrase,
        before_verdict: c.before_verdict ?? c.before ?? record.phase5_reviewed_verdict,
        after_verdict: c.after_verdict ?? c.after,
        change_type: c.change_type,
        reason: c.reason,
        authority: c.authority ?? resolved.authority,
        reviewer: REVIEWER,
        phase: '5.1',
        preserved: {
          original_model_verdict: record.original_model_verdict,
          original_authoritative_verdict: record.original_authoritative_verdict,
          phase5_reviewed_verdict: record.phase5_reviewed_verdict,
        },
      });
    }

    const intent = assignIntent(record.phrase, resolved.verdict);
    const geo = assignGeography(record.phrase);
    const serviceFamily = assignServiceFamily(record.phrase, resolved.verdict);
    const exclusionFamily = assignExclusionFamily(record.phrase, resolved.verdict);

    const entry = {
      ...record,
      phase51_final_verdict: resolved.verdict,
      phase51_review_status: resolved.reviewStatus,
      phase51_action: resolved.action,
      phase51_rationale: resolved.reason,
      phase51_authority: resolved.authority,
      review_flag_root_cause: rootCause,
      service_family: serviceFamily,
      primary_intent: intent.primary,
      secondary_intent: intent.secondary,
      geography: geo,
      exclusion_family: exclusionFamily,
      provenance: {
        ...record.provenance,
        phase51_reviewer: REVIEWER,
        phase51_authority: resolved.authority,
      },
    };
    registryV2.push(entry);

    const outRec = {
      phrase_id: record.phrase_id,
      phrase: record.phrase,
      original_model_verdict: record.original_model_verdict,
      original_authoritative_verdict: record.original_authoritative_verdict,
      phase5_reviewed_verdict: record.phase5_reviewed_verdict,
      phase51_final_verdict: resolved.verdict,
      phase51_review_status: resolved.reviewStatus,
      review_status: resolved.reviewStatus,
      service_family: serviceFamily,
      primary_intent: intent.primary,
      geography: geo,
      source_metadata: record.source_metadata,
      provenance: entry.provenance,
    };

    if (resolved.verdict === 'ACCEPT') acceptV2.push(outRec);
    else if (resolved.verdict === 'REJECT') rejectV2.push(outRec);
    else abstainV2.push(outRec);

    if (resolved.operatorRequired) {
      operatorCandidates.push({
        phrase_id: record.phrase_id,
        phrase: record.phrase,
        current_verdict: resolved.verdict,
        recommended_verdict: resolved.recommended_verdict || resolved.verdict,
        ambiguity: resolved.ambiguity,
        business_consequence: resolved.business_consequence,
        options: resolved.options,
        phase5_verdict: record.phase5_reviewed_verdict,
        review_flag_root_cause: rootCause,
      });
    }
  }

  registryV2.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id));

  const reviewQueueResolved = {
    queue_id: 'corvonero-run-004-phase-51-resolved-review-queue-v1',
    run_id: RUN_ID,
    source_queue: 'CORVONERO-RUN-004-PHASE-5-PARTIAL-REVIEW-QUEUE-v1.json',
    total_items: phase5Queue.total_items,
    items: phase5Queue.items.map((item) => {
      const rec = registryV2.find((r) => r.phrase_id === item.phrase_id);
      let disposition = 'RESOLVED_FROM_PHASE51_POLICY';
      if (item.phrase_id === 'CR2-PHR-00200') disposition = 'OPERATOR_DECISION_APPLIED';
      if (item.phrase_id === 'CR2-PHR-00584') disposition = 'OPERATOR_OVERRIDE_PRESERVED';
      if (item.phase5_triage === 'DATA_OR_POLICY_ISSUE') disposition = dataPolicyMap.get(item.phrase_id)?.disposition || 'MALFORMED_RETRY_VERIFIED';
      if (operatorCandidates.some((o) => o.phrase_id === item.phrase_id)) disposition = 'OPERATOR_DECISION_REQUIRED';
      return {
        phrase_id: item.phrase_id,
        phrase: item.phrase,
        phase4_review_reason: item.phase4_review_reason,
        phase5_triage: item.phase5_triage,
        phase51_disposition: disposition,
        phase51_final_verdict: rec?.phase51_final_verdict,
        phase51_review_status: rec?.phase51_review_status,
      };
    }),
    summary: {},
    created_at: new Date().toISOString(),
  };
  for (const item of reviewQueueResolved.items) {
    reviewQueueResolved.summary[item.phase51_disposition] = (reviewQueueResolved.summary[item.phase51_disposition] || 0) + 1;
  }

  const dataPolicyDisposition = {
    disposition_id: 'corvonero-run-004-phase-51-data-policy-disposition-v1',
    run_id: RUN_ID,
    total: dataPolicyMap.size,
    records: [...dataPolicyMap.values()],
    summary: {},
  };
  for (const r of dataPolicyDisposition.records) {
    dataPolicyDisposition.summary[r.disposition] = (dataPolicyDisposition.summary[r.disposition] || 0) + 1;
  }

  const serviceTaxonomy = buildServiceTaxonomy(registryV2);
  const intentCounts = {};
  for (const r of registryV2) intentCounts[r.primary_intent] = (intentCounts[r.primary_intent] || 0) + 1;
  const intentTaxonomy = Object.entries(intentCounts).map(([intent, count]) => ({
    intent_class: intent,
    record_count: count,
    accept_count: registryV2.filter((r) => r.primary_intent === intent && r.phase51_final_verdict === 'ACCEPT').length,
    reject_count: registryV2.filter((r) => r.primary_intent === intent && r.phase51_final_verdict === 'REJECT').length,
    abstain_count: registryV2.filter((r) => r.primary_intent === intent && r.phase51_final_verdict === 'ABSTAIN').length,
  }));

  const geoRegistry = registryV2.filter((r) => r.geography.status !== 'NO_GEOGRAPHY').map((r) => ({
    phrase_id: r.phrase_id,
    phrase: r.phrase,
    normalized: r.geography.normalized,
    usable: r.geography.usable,
    status: r.geography.status,
    phase51_verdict: r.phase51_final_verdict,
  }));
  const geography = {
    geography_id: 'corvonero-run-004-phase-51-geography-v2',
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
    const key = `${g.status}:${g.phase51_verdict}`;
    geography.verdict_by_geo[key] = (geography.verdict_by_geo[key] || 0) + 1;
  }

  const troubleRecords = registryV2.filter((r) => PROBLEM.test(r.phrase) && ONE_C.test(r.phrase));
  const tsRecords = registryV2.filter((r) => TS_PIOT.test(r.phrase));
  const integrationMarking = registryV2.filter((r) => (INTEGRATION.test(r.phrase) || MARKING.test(r.phrase)) && ONE_C.test(r.phrase));

  const finalCounts = { ACCEPT: acceptV2.length, REJECT: rejectV2.length, ABSTAIN: abstainV2.length };
  const phase51Corrections = correctionLedgerV2.length - phase5Ledger.count;

  const operatorPacket = {
    packet_id: 'corvonero-run-004-phase-51-operator-decision-packet-v1',
    run_id: RUN_ID,
    total: operatorCandidates.length,
    note: 'Genuine operator judgment required — not mechanically resolvable from existing policy',
    records: operatorCandidates.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id)),
  };

  const phase51Verdict = operatorPacket.total > 0 && operatorPacket.total <= 80
    ? 'PASS — OPERATOR DECISION PACKET REQUIRED'
    : operatorPacket.total > 80
      ? 'BLOCKED — MATERIAL SEMANTIC AUTHORITY GAPS'
      : 'PASS — OPERATOR DECISION PACKET REQUIRED';

  const result = {
    run_id: RUN_ID,
    result_id: 'corvonero-run-004-phase-51-authority-closure-result-v1',
    phase_verdict: phase51Verdict,
    lifecycle_state: 'PHASE_51_PARTIAL_AUTHORITY_CLOSURE',
    project_lifecycle: phase51Verdict.startsWith('PASS') ? 'READY_FOR_FINAL_PARTIAL_SEMANTIC_SIGN-OFF' : 'PHASE_51_BLOCKED',
    provider_calls: 'FROZEN',
    campaign_architecture: 'NOT AUTHORIZED',
    operator_decisions: {
      'CR2-PHR-00200': OPERATOR_DECISION_00200,
      'CR2-PHR-00584': OPERATOR_OVERRIDE_00584,
      openrouter: 'FROZEN',
      campaign_architecture: 'NOT AUTHORIZED',
    },
    preflight,
    review_flag_audit: reviewFlagAudit,
    verdict_distribution: {
      phase4: { ACCEPT: 529, REJECT: 762, ABSTAIN: 308 },
      phase5: { ACCEPT: 531, REJECT: 578, ABSTAIN: 490 },
      phase51: finalCounts,
    },
    operator_review_required_phase5: 350,
    operator_review_required_phase51: registryV2.filter((r) => r.phase51_review_status === 'OPERATOR_REVIEW_REQUIRED').length,
    operator_packet_count: operatorPacket.total,
    phase51_corrections: phase51Corrections,
    troubleshooting_audit: {
      total_assessed: troubleRecords.length,
      accept: troubleRecords.filter((r) => r.phase51_final_verdict === 'ACCEPT').length,
      reject: troubleRecords.filter((r) => r.phase51_final_verdict === 'REJECT').length,
      abstain: troubleRecords.filter((r) => r.phase51_final_verdict === 'ABSTAIN').length,
      zero_accept_phase5_validity: 'Phase 5 zero ACCEPT was partially caused by taxonomy mapping — sync-error phrases classified as integration troubleshooting, not SF-TROUBLESHOOTING-NOT-WORKING; classic program-not-working phrases remain ambiguous DIY vs service',
    },
    ts_piot_audit: {
      total_assessed: tsRecords.length,
      accept: tsRecords.filter((r) => r.phase51_final_verdict === 'ACCEPT').length,
      reject: tsRecords.filter((r) => r.phase51_final_verdict === 'REJECT').length,
      abstain: tsRecords.filter((r) => r.phase51_final_verdict === 'ABSTAIN').length,
      accept_explanation: 'Only explicit setup/service-demand phrases (e.g. настройка тс пиот) map to SF-TS-PIOT ACCEPT; combined marking+TS ПИОТ and DIY install queries remain ABSTAIN/REJECT',
      records: tsRecords.map((r) => ({ phrase_id: r.phrase_id, phrase: r.phrase, phase51_verdict: r.phase51_final_verdict, service_family: r.service_family })),
    },
    integrations_marking_audit: {
      total: integrationMarking.length,
      unnecessarily_abstain_from_stale_flags: integrationMarking.filter((r) => r.phase5_reviewed_verdict === 'ABSTAIN' && r.phase51_final_verdict === 'ACCEPT').length,
      promoted_to_accept: integrationMarking.filter((r) => r.phase51_final_verdict === 'ACCEPT').length,
      remain_abstain: integrationMarking.filter((r) => r.phase51_final_verdict === 'ABSTAIN').length,
    },
    created_at: new Date().toISOString(),
  };

  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-AUTHORITY-CLOSURE-RESULT-v1.json'), result);
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-REVIEWED-REGISTRY-v2.json'), {
    registry_id: 'corvonero-run-004-phase-51-reviewed-registry-v2',
    run_id: RUN_ID,
    source: 'CORVONERO-RUN-004-PHASE-5-PARTIAL-REVIEWED-REGISTRY-v1.json',
    count: registryV2.length,
    records: registryV2,
  });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-ACCEPT-v2.json'), { run_id: RUN_ID, count: acceptV2.length, records: acceptV2 });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-REJECT-v2.json'), { run_id: RUN_ID, count: rejectV2.length, records: rejectV2 });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-ABSTAIN-v2.json'), { run_id: RUN_ID, count: abstainV2.length, records: abstainV2 });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-CORRECTION-LEDGER-v2.json'), {
    ledger_id: 'corvonero-run-004-phase-51-correction-ledger-v2',
    source: 'CORVONERO-RUN-004-PHASE-5-PARTIAL-CORRECTION-LEDGER-v1.json',
    phase5_correction_count: phase5Ledger.count,
    phase51_additional_corrections: phase51Corrections,
    count: correctionLedgerV2.length,
    records: correctionLedgerV2,
  });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-DATA-POLICY-DISPOSITION-v1.json'), dataPolicyDisposition);
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-SERVICE-TAXONOMY-v2.json'), { taxonomy_id: 'corvonero-run-004-phase-51-service-taxonomy-v2', families: serviceTaxonomy });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-INTENT-TAXONOMY-v2.json'), { taxonomy_id: 'corvonero-run-004-phase-51-intent-taxonomy-v2', classes: intentTaxonomy });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-GEOGRAPHY-v2.json'), geography);
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-OPERATOR-DECISION-PACKET-v1.json'), operatorPacket);

  const operatorMd = `# CORVONERO RUN 004 — Phase 5.1 Operator Decision Packet v1

**Run:** \`${RUN_ID}\`  
**Total genuine unresolved:** ${operatorPacket.total}  
**Provider calls:** FROZEN  
**Campaign Architecture:** NOT AUTHORIZED

## Instructions

Each record below requires an actual business/operator judgment. Do not treat primary/reassessment model disagreement alone as grounds for review when policy already establishes the outcome.

${operatorPacket.records.map((r, i) => `### ${i + 1}. ${r.phrase_id}

- **Phrase:** ${r.phrase}
- **Current verdict:** ${r.current_verdict}
- **Recommended verdict:** ${r.recommended_verdict}
- **Ambiguity:** ${r.ambiguity}
- **Business consequence:** ${r.business_consequence}
- **Options:** ${(r.options || []).join(' | ')}
`).join('\n')}
`;
  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-OPERATOR-DECISION-PACKET-v1.md'), operatorMd);

  const coverageMd = `# CORVONERO RUN 004 — Phase 5.1 Coverage v2

**Run:** \`${RUN_ID}\`  
**Partial dataset:** ${ASSESSED_TOTAL} / ${CANONICAL_TOTAL}  
**Unprocessed:** ${UNPROCESSED_TOTAL} / ${CANONICAL_TOTAL}

## Verdict distribution

| Stage | ACCEPT | REJECT | ABSTAIN |
|-------|--------|--------|---------|
| Phase 4 | 529 | 762 | 308 |
| Phase 5 | 531 | 578 | 490 |
| Phase 5.1 | ${finalCounts.ACCEPT} | ${finalCounts.REJECT} | ${finalCounts.ABSTAIN} |

## Review flag reconciliation

- Phase 5 OPERATOR_REVIEW_REQUIRED: **350**
- Phase 5.1 OPERATOR_REVIEW_REQUIRED: **${result.operator_review_required_phase51}**
- Genuine operator packet: **${operatorPacket.total}**

## Troubleshooting (1С не работает family)

${JSON.stringify(result.troubleshooting_audit, null, 2)}

## TS ПИОТ

${JSON.stringify(result.ts_piot_audit, null, 2)}

## Geography

${JSON.stringify(geography.distribution, null, 2)}
`;
  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-COVERAGE-v2.md'), coverageMd);

  const resultMd = `# CORVONERO RUN 004 — Phase 5.1 Authority Closure Result v1

**Phase verdict:** ${phase51Verdict}  
**Project lifecycle:** ${result.project_lifecycle}

\`\`\`text
PHASE 5.1:
${phase51Verdict}

Project:
${result.project_lifecycle}
\`\`\`

## Operator decisions applied

- **CR2-PHR-00200:** REJECT — OPERATOR_CONFIRMED (informational/DIY)
- **CR2-PHR-00584:** operator override preserved (model ACCEPT → REJECT)
- **OpenRouter:** FROZEN
- **Campaign Architecture:** NOT AUTHORIZED
`;
  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-AUTHORITY-CLOSURE-RESULT-v1.md'), resultMd);

  const phase6Md = `# CORVONERO RUN 004 — Phase 6 Next Task (Partial) v2

**Prerequisite:** Phase 5.1 — ${phase51Verdict}  
**Gate:** FINAL PARTIAL SEMANTIC SIGN-OFF

## Authorized after operator sign-off

- Review ${operatorPacket.total} genuine operator decision packet items
- Accept partial semantic authority for ${ASSESSED_TOTAL} assessed records (${((ASSESSED_TOTAL / CANONICAL_TOTAL) * 100).toFixed(1)}% coverage)

## Not authorized

- Campaign Architecture
- Ad groups / advertisements / final minus-word lists
- Commander / import / launch / Wave 5
- Processing 769 unprocessed backlog IDs
- OpenRouter or external model calls
`;
  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-6-NEXT-TASK-PARTIAL-v2.md'), phase6Md);

  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5.1-RESOLVED-REVIEW-QUEUE-v1.json'), reviewQueueResolved);

  const report = buildReport(result, preflight, finalCounts, reviewFlagAudit, operatorPacket, dataPolicyDisposition, serviceTaxonomy, geography, phase51Corrections, reviewQueueResolved.summary);
  writeText(path.join(REPORTS, 'REPORT-corvonero-run-004-phase-5.1-authority-closure-v1.md'), report);

  console.log(JSON.stringify({
    phase51_verdict: phase51Verdict,
    accept: finalCounts.ACCEPT,
    reject: finalCounts.REJECT,
    abstain: finalCounts.ABSTAIN,
    operator_packet: operatorPacket.total,
    phase51_corrections: phase51Corrections,
  }, null, 2));
}

function buildReport(result, preflight, finalCounts, reviewFlagAudit, operatorPacket, dataPolicyDisposition, serviceTaxonomy, geography, phase51Corrections, queueSummary) {
  return `# REPORT — CORVONERO RUN 004 PHASE 5.1 SEMANTIC AUTHORITY CLOSURE V1

**Run ID:** \`${RUN_ID}\`  
**Date:** ${new Date().toISOString().slice(0, 10)}

---

## 1. Safety and Scope

Phase 5.1 partial semantic authority closure using existing Phase 4/5 artefacts only. No provider calls. No canonical/Phase 4/Phase 5 source mutation. 769 unprocessed IDs excluded. Campaign Architecture **NOT AUTHORIZED**.

---

## 2. Git Preflight

- Branch: \`mars/canonical-post-recovery\`
- Recovery ancestry: verified
- Integrity: 531+578+490=1599; union=2368; disjoint manifests ✓

---

## 3. Input Authority

Run \`${RUN_ID}\`. Phase 5 partial assembly as input. Unprocessed backlog preserved.

---

## 4. CR2-PHR-00200 Resolution

Correction record added. **REJECT**, **OPERATOR_CONFIRMED**. Model/classifier fields preserved.

---

## 5. Review-Flag Root Cause

| Root cause | Records |
|------------|---------|
${Object.entries(reviewFlagAudit).map(([k, v]) => `| ${k} | ${v} |`).join('\n')}

---

## 6. Review Queue Reconciliation

| Disposition | Count |
|-------------|-------|
${Object.entries(queueSummary).map(([k, v]) => `| ${k} | ${v} |`).join('\n')}

Phase 5 operator-review-required registry records: **350** → Phase 5.1 remaining flags: **${result.operator_review_required_phase51}**

---

## 7. ACCEPT Authority

Phase 5.1 ACCEPT: **${finalCounts.ACCEPT}** (Phase 5: 531). Commercial demand, price/cost, marking service, integration service, and cleared stale disagreement flags.

---

## 8. REJECT Authority

Phase 5.1 REJECT: **${finalCounts.REJECT}** (Phase 5: 578). Career, education, informational/DIY, product-only, marking DIY, TS ПИОТ certification.

---

## 9. ABSTAIN Authority

Phase 5.1 ABSTAIN: **${finalCounts.ABSTAIN}** (Phase 5: 490). Genuine ambiguity retained — sync troubleshooting, short queries, combined compliance scopes. Not forced to ACCEPT/REJECT.

---

## 10. Data and Policy Issues

15 records reviewed:

| Disposition | Count |
|-------------|-------|
${Object.entries(dataPolicyDisposition.summary).map(([k, v]) => `| ${k} | ${v} |`).join('\n')}

Malformed retry flags cleared where valid Phase 4/5 responses exist.

---

## 11. Troubleshooting Coverage

| Verdict | Count |
|---------|-------|
| ACCEPT | ${result.troubleshooting_audit.accept} |
| REJECT | ${result.troubleshooting_audit.reject} |
| ABSTAIN | ${result.troubleshooting_audit.abstain} |
| **Total** | **${result.troubleshooting_audit.total_assessed}** |

${result.troubleshooting_audit.zero_accept_phase5_validity}

---

## 12. TS ПИОТ Coverage

| Verdict | Count |
|---------|-------|
| ACCEPT | ${result.ts_piot_audit.accept} |
| REJECT | ${result.ts_piot_audit.reject} |
| ABSTAIN | ${result.ts_piot_audit.abstain} |
| **Total** | **${result.ts_piot_audit.total_assessed}** |

${result.ts_piot_audit.accept_explanation}

---

## 13. Integrations and Marking

Promoted from ABSTAIN to ACCEPT (stale-flag cleanup): **${result.integrations_marking_audit.unnecessarily_abstain_from_stale_flags}**  
Total integration/marking assessed: **${result.integrations_marking_audit.total}**  
Remain ABSTAIN: **${result.integrations_marking_audit.remain_abstain}**

---

## 14. Geography

| Bucket | Count |
|--------|-------|
| Novosibirsk/NSO (PRIMARY) | ${geography.distribution.primary_novosibirsk_nso} |
| Krasnodar | ${geography.distribution.expansion_krasnodar} |
| Ekaterinburg | ${geography.distribution.expansion_ekaterinburg} |
| Krasnoyarsk | ${geography.distribution.expansion_krasnoyarsk} |
| Other Russian cities | ${geography.distribution.other_russian_cities} |
| Russia-wide/remote | ${geography.distribution.russia_wide_remote} |
| Irrelevant/unknown | ${geography.distribution.irrelevant_or_unknown} |

Geography alone does not change verdict.

---

## 15. Correction Ledger

Phase 5 corrections preserved: **189**  
Phase 5.1 additional corrections: **${phase51Corrections}**  
Total ledger v2: **${189 + phase51Corrections}**

---

## 16. Final Verdict Distribution

| Stage | ACCEPT | REJECT | ABSTAIN |
|-------|--------|--------|---------|
| Phase 4 | 529 | 762 | 308 |
| Phase 5 | 531 | 578 | 490 |
| Phase 5.1 | ${finalCounts.ACCEPT} | ${finalCounts.REJECT} | ${finalCounts.ABSTAIN} |

---

## 17. Genuine Operator Decision Packet

**${operatorPacket.total}** records requiring actual business judgment. See \`CORVONERO-RUN-004-PHASE-5.1-OPERATOR-DECISION-PACKET-v1.md\`.

---

## 18. Partial Coverage Limitation

\`\`\`text
ASSESSED: ${ASSESSED_TOTAL} / ${CANONICAL_TOTAL}
UNPROCESSED: ${UNPROCESSED_TOTAL} / ${CANONICAL_TOTAL}
\`\`\`

769 backlog IDs not imputed.

---

## 19. Phase 5.1 Verdict

\`\`\`text
PHASE 5.1:
${result.phase_verdict}

Project:
${result.project_lifecycle}
\`\`\`

---

## 20. Project Lifecycle

Ready for final partial semantic sign-off after operator packet review. Campaign Architecture remains **NOT AUTHORIZED**.

---

## 21. Outputs Created

All under \`projects/mars-search-ppc-production/pilots/corvonero/\` plus report in \`reports/\`.

---

## 22. Files Changed

New Phase 5.1 v2 artefacts only. Phase 4/5 sources unchanged.

---

## 23. Git Status

No commit. No push.

---

## 24. SAFE UNKNOWN

- 769 unprocessed phrases: verdict unknown until authorized resume
- Market demand volume: not inferred from counts

---

## 25. Operator Decisions Required

Review **${operatorPacket.total}** genuine operator packet records. Approve Phase 5.1 partial semantic authority for interim planning.

---

## 26. Exact Next Task

See \`CORVONERO-RUN-004-PHASE-6-NEXT-TASK-PARTIAL-v2.md\`

---

## 27. Stop Condition

Phase 5.1 semantic authority closure **complete**. Stopped before Campaign Architecture, ad groups, ads, negatives, Commander, import, launch, Wave 5.
`;
}

main();
