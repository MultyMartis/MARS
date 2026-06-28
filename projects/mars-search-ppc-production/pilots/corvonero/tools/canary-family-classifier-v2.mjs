/**
 * Corvonero Run 004 Phase 3 canary — classifier v2.
 * Separates observable tags, coverage family, expectation authority, and review requirement.
 */
import { extractServiceIntentEvidence } from '../../../../orca/semantic-intelligence/live-model/evidence/service-intent-evidence.mjs';
import {
  evaluatePlatformCompatibility,
  PLATFORM_CLASSIFICATION,
} from '../../../../orca/semantic-intelligence/live-model/evidence/platform-compatibility.mjs';

export const CANARY_SEED_V2 = 'corv-run004-canary-v2-20260628';
export const CANARY_SIZE = 120;
export const CLASSIFIER_VERSION = 'v2.0.1';

export const EXPECTATION_STATUS = {
  AUTHORITATIVE_EXPECTATION: 'AUTHORITATIVE_EXPECTATION',
  POLICY_DERIVED_EXPECTATION: 'POLICY_DERIVED_EXPECTATION',
  REVIEW_REQUIRED: 'REVIEW_REQUIRED',
  NO_GOLD_LABEL: 'NO_GOLD_LABEL',
};

export const FAMILY_MINIMUMS = {
  direct_commercial_1c_service: 20,
  problem_troubleshooting: 15,
  integrations: 10,
  marking_chestny_znak: 8,
  ts_piot: 5,
  product_license_version: 12,
  informational_self_service: 12,
  careers_training_education: 8,
  generic_erp_platform_ambiguity: 8,
  geography_modified: 10,
  ambiguous_mixed_intent: 12,
};

const TS_PIOT = /(?:тс\s*пиот|ts\s*piot|промышленн(?:ая|ой|ую)\s+безопасност)/i;
const MARKING = /(?:честн(?:ый|ого)\s+знак|маркировк(?:а|и|у|ой)|data\s*matrix|gs1)/i;
const INTEGRATION = /(?:интеграц(?:ия|ии|ию|ией)|bitrix|битрикс|синхронизац|обмен\s+данн|api\s+1с|rest\s+1с)/i;
const GEO = /(?:москва|санкт-петербург|спб|екатеринбург|новосибирск|казань|нижний\s+новгород|самара|ростов|краснодар|воронеж|пермь|волгоград|красноярск|тюмень|уфа|омск|челябинск|иркутск|хабаровск|владивосток)/i;
const ONE_C = /(?:1[\s-]?с|1c|один[\s-]?эс)/i;
const ERP = /\berp\b/i;
const PROVIDER_ROLE = /(?:программист|разработчик|специалист)/i;

const COMMERCIAL_PRICE_WORK =
  /(?:сколько\s+стоит\s+работа|стоимость\s+работ(?:ы|)|цена\s+работ(?:ы|)|стоимость\s+услуг|расценки\s+специалиста|стоимость\s+работ\s+по)/i;
const PAYROLL_MODULE_SERVICE =
  /(?:(?:сопровожден|настройк|внедрен|обслуживан|доработк|конфигурац|модул|подсистем|обновлен|установк|подключ).{0,40}(?:зарплат|кадр)|(?:зарплат|кадр)\s+и\s+кадр)/i;
const CAREER_SALARY_MARKER =
  /(?:зарплат(?:а|ы)\s+(?:программист(?:а|ом|у|ы|ов|ами|е)?|разработчик(?:а|ом|у|ы|ов|ами|е)?|специалист(?:а|ом|у|ы|ов|ами|е)?)|зарплат(?:а|ы).{0,20}(?:ваканс|работ(?:а|у)\s+программист))/i;
const CAREER_MARKERS =
  /(?:ваканс|резюме|собеседован|карьер|трудоустройств|устроиться|стажер|стажировк|ищу\s+работ|работа\s+программист(?:ом|ами|ов|ке)|работа\s+разработчик(?:ом|ами|ов|ке)|работодател|требовани(?:я|е)\s+к\s+программист)/i;
const EDUCATION_MARKERS = /(?:как\s+стать|обучен|курс|учеб|экзамен|сертификац|урок|тренинг|семинар|skillbox|ironskills|быстрый\s+старт|клуб\s+программист)/i;
const INFORMATIONAL_MARKERS = /(?:что\s+такое|что\s+делает|что\s+должен\s+уметь|что\s+нужно\s+знать|как\s+работает|инструкци|руководств|форум|пример|самостоятельно|вопрос\s+программист|техническ(?:ое|ого)\s+задани(?:е|я)\s+на\s+пример)/i;
const SELF_SERVICE = /(?:инструкци|самостоятельно|самому|как\s+(?:обновить|настроить|установить)(?!\s+специалист))/i;

const COMMERCIAL_DEMAND =
  /(?:нужен|нужна|нужно\s+(?:программист|специалист|заказать|вызвать)|заказать|найти\s+специалист|стоимость\s+услуг|цена\s+работ|сколько\s+стоит\s+работа|стоимость\s+работ(?:ы|)|цена\s+работ(?:ы|)|расценки\s+специалиста|вызвать\s+программист|нанять|под\s+ключ|срочно)/i;
const SERVICE_TASK = /(?:внедрен|настрой|сопровожден|доработк|интеграц(?:ия|ии|ию)|обслуживан|ремонт|миграц|аудит|оптимизац|консультац|исправить|устранить)/i;
const PRODUCT = /(?:купить|приобрест|лицензи|поставк|дистрибутив|коробочн|скачать\s+1с)/i;
const PROBLEM = /(?:ошибк|не\s+работает|сбой|0x[\da-f]+|исправить|устранить|fault|exception)/i;
const PRODUCT_BUNDLE = /(?:купить|приобрест|лицензи|поставк).*(?:1[\s-]?с|1c).*(?:настрой|внедрен|сопровожден)|(?:настрой|внедрен|сопровожден).*(?:1[\s-]?с|1c).*(?:купить|приобрест|лицензи|поставк)/i;
const BARE_ROLE_QUERY = /^(?:программист|разработчик|специалист)(?:\s+(?:1[\s-]?с|1c|разработчик))?(?:\s+\w+)?$/i;
const AMBIGUOUS_SHORT = /^(?:программист\s+1[\s-]?с|1[\s-]?с\s+программист|обновление\s+1[\s-]?с)$/i;
const PSR_AMB_01 = /купить\s+1[\s-]?с\s+с\s+настрой/i;

function hasCareerEvidence(text, evidence) {
  if (COMMERCIAL_PRICE_WORK.test(text)) return false;
  if (PAYROLL_MODULE_SERVICE.test(text)) return false;
  if (CAREER_SALARY_MARKER.test(text)) return true;
  return CAREER_MARKERS.test(text) || evidence.career;
}

function extractObservableTags(text, evidence, platform) {
  const tags = [];
  if (TS_PIOT.test(text)) tags.push('ts_piot');
  if (MARKING.test(text)) tags.push('marking_chestny_znak');
  if (INTEGRATION.test(text)) tags.push('integrations');
  if (GEO.test(text)) tags.push('geography');
  if (ONE_C.test(text)) tags.push('one_c');
  if (ERP.test(text)) tags.push('erp_reference');
  if (hasCareerEvidence(text, evidence)) tags.push('career');
  if (COMMERCIAL_PRICE_WORK.test(text)) tags.push('commercial_price_work');
  if (EDUCATION_MARKERS.test(text) || evidence.education) tags.push('education');
  if (INFORMATIONAL_MARKERS.test(text) || evidence.informational) tags.push('informational');
  if (SELF_SERVICE.test(text) || evidence.diy || evidence.product_self_update) tags.push('self_service');
  if (PRODUCT.test(text) && !SERVICE_TASK.test(text) && !PRODUCT_BUNDLE.test(text)) tags.push('product_only');
  if (COMMERCIAL_DEMAND.test(text) || evidence.price_order_detected) tags.push('commercial_demand');
  if (SERVICE_TASK.test(text) || evidence.service_task_detected) tags.push('service_task');
  if (PROVIDER_ROLE.test(text) || evidence.provider_noun_detected) tags.push('provider_role');
  if (evidence.strong_commercial || evidence.strong_commercial_problem) tags.push('strong_commercial');
  if (PRODUCT_BUNDLE.test(text) || evidence.product_plus_service) tags.push('product_plus_service_bundle');
  if (platform.classification === PLATFORM_CLASSIFICATION.GENERIC_PLATFORM_FAMILY) tags.push('generic_erp_platform');
  if (platform.classification === PLATFORM_CLASSIFICATION.EXPLICIT_INCOMPATIBLE) tags.push('foreign_incompatible_platform');
  if (evidence.ambiguous_diy_problem) tags.push('ambiguous_diy');
  if (PSR_AMB_01.test(text)) tags.push('psr_amb_01');
  return [...new Set(tags)];
}

function hasPositiveCommercialEvidence(text, evidence) {
  if (evidence.strong_commercial || evidence.strong_commercial_problem) return true;
  if (COMMERCIAL_PRICE_WORK.test(text)) return true;
  if (COMMERCIAL_DEMAND.test(text)) return true;
  if (SERVICE_TASK.test(text) && (COMMERCIAL_DEMAND.test(text) || evidence.price_order_detected)) return true;
  if (SERVICE_TASK.test(text) && PROVIDER_ROLE.test(text) && !CAREER_MARKERS.test(text) && !EDUCATION_MARKERS.test(text) && !INFORMATIONAL_MARKERS.test(text)) {
    return COMMERCIAL_DEMAND.test(text);
  }
  return false;
}

function isCareerOrEducation(text, evidence, tags) {
  if (COMMERCIAL_PRICE_WORK.test(text)) {
    return tags.includes('education') || evidence.education;
  }
  return tags.includes('career') || tags.includes('education') || hasCareerEvidence(text, evidence) || evidence.education;
}

function isInformationalExclusion(text, evidence, tags) {
  if (tags.includes('informational') || evidence.informational) return !hasPositiveCommercialEvidence(text, evidence);
  if (INFORMATIONAL_MARKERS.test(text) && !COMMERCIAL_DEMAND.test(text)) return true;
  if (tags.includes('self_service') && !hasPositiveCommercialEvidence(text, evidence)) return true;
  return false;
}

function isDirectCommercial(text, evidence, tags) {
  if (!ONE_C.test(text) && !evidence.strong_commercial) return false;
  if (isCareerOrEducation(text, evidence, tags)) return false;
  if (isInformationalExclusion(text, evidence, tags)) return false;
  if (tags.includes('product_only') && !tags.includes('product_plus_service_bundle')) return false;
  if (BARE_ROLE_QUERY.test(text.trim()) || AMBIGUOUS_SHORT.test(text.trim())) return false;
  return hasPositiveCommercialEvidence(text, evidence)
    || (SERVICE_TASK.test(text) && COMMERCIAL_DEMAND.test(text))
    || evidence.strong_commercial_problem;
}

function isProblemTroubleshooting(text, evidence, tags) {
  return PROBLEM.test(text)
    && !tags.includes('career')
    && !/ошибки\s+программиста/i.test(text)
    && !evidence.strong_commercial;
}

function isGeographyCommercial(text, evidence, tags) {
  return tags.includes('geography')
    && ONE_C.test(text)
    && (hasPositiveCommercialEvidence(text, evidence) || evidence.supporting_commercial_geo);
}

function assignCoverageFamily(text, evidence, platform, tags) {
  if (TS_PIOT.test(text)) return 'ts_piot';
  if (MARKING.test(text)) return 'marking_chestny_znak';
  if (INTEGRATION.test(text) && !isProblemTroubleshooting(text, evidence, tags)) return 'integrations';
  if (isCareerOrEducation(text, evidence, tags)) return 'careers_training_education';
  if (PSR_AMB_01.test(text) || (tags.includes('product_plus_service_bundle') && !hasPositiveCommercialEvidence(text, evidence))) {
    return 'ambiguous_mixed_intent';
  }
  if (
    platform.classification === PLATFORM_CLASSIFICATION.GENERIC_PLATFORM_FAMILY
    && !hasPositiveCommercialEvidence(text, evidence)
    && !(SERVICE_TASK.test(text) && ONE_C.test(text))
  ) {
    return 'generic_erp_platform_ambiguity';
  }
  if (ERP.test(text) && /(?:обновлен|верси|систем)/i.test(text) && !hasPositiveCommercialEvidence(text, evidence)) {
    return 'generic_erp_platform_ambiguity';
  }
  if (PRODUCT.test(text) && !SERVICE_TASK.test(text) && !PRODUCT_BUNDLE.test(text) && !tags.includes('career')) {
    return 'product_license_version';
  }
  if (tags.includes('self_service') || tags.includes('informational') || evidence.diy || evidence.informational || evidence.product_self_update) {
    if (!hasPositiveCommercialEvidence(text, evidence)) return 'informational_self_service';
  }
  if (isProblemTroubleshooting(text, evidence, tags)) return 'problem_troubleshooting';
  if (isDirectCommercial(text, evidence, tags) || evidence.strong_commercial_problem) {
    return 'direct_commercial_1c_service';
  }
  if (isGeographyCommercial(text, evidence, tags) || (tags.includes('geography') && ONE_C.test(text))) {
    return 'geography_modified';
  }
  if (PRODUCT.test(text) && tags.includes('service_task')) return 'ambiguous_mixed_intent';
  if (ERP.test(text) && !INTEGRATION.test(text) && !hasPositiveCommercialEvidence(text, evidence)) {
    return 'generic_erp_platform_ambiguity';
  }
  if (BARE_ROLE_QUERY.test(text.trim()) || AMBIGUOUS_SHORT.test(text.trim()) || (!hasPositiveCommercialEvidence(text, evidence) && PROVIDER_ROLE.test(text))) {
    return 'ambiguous_mixed_intent';
  }
  return 'ambiguous_mixed_intent';
}

function deriveExpectationAuthority(text, evidence, platform, primaryFamily, tags) {
  const edgeCases = [];
  if (tags.includes('psr_amb_01')) edgeCases.push('psr_amb_01_family');
  if (tags.includes('product_plus_service_bundle')) edgeCases.push('product_plus_service_bundle');
  if (tags.includes('ambiguous_diy')) edgeCases.push('ambiguous_diy_troubleshooting');
  if (tags.includes('foreign_incompatible_platform')) edgeCases.push('foreign_incompatible_platform');
  if (tags.includes('generic_erp_platform')) edgeCases.push('generic_erp_ambiguity');
  if (evidence.product_version_update && ONE_C.test(text)) edgeCases.push('direct_1c_version_update_service');
  if (evidence.product_self_update) edgeCases.push('self_service_update_instructions');
  if (isProblemTroubleshooting(text, evidence, tags) && !evidence.strong_commercial_problem) {
    edgeCases.push('problem_without_commercial_marker');
  }

  if (platform.classification === PLATFORM_CLASSIFICATION.EXPLICIT_INCOMPATIBLE) {
    return {
      expectation_status: EXPECTATION_STATUS.AUTHORITATIVE_EXPECTATION,
      expectation_class: 'pre_authorized',
      expected_verdict: 'REJECT',
      authority_source: 'foreign_incompatible_platform_policy',
      review_required: false,
      scored: true,
      selection_reason: 'explicit foreign/incompatible platform policy',
      edge_cases: [...new Set(edgeCases)],
    };
  }

  if (isCareerOrEducation(text, evidence, tags)) {
    return {
      expectation_status: EXPECTATION_STATUS.POLICY_DERIVED_EXPECTATION,
      expectation_class: 'pre_authorized',
      expected_verdict: 'REJECT',
      authority_source: 'career_training_exclusion_policy',
      review_required: false,
      scored: true,
      selection_reason: 'career/training exclusion policy',
      edge_cases: [...new Set(edgeCases)],
    };
  }

  if (isInformationalExclusion(text, evidence, tags)) {
    const ambiguousInfo = /как\s+работает/i.test(text) && !COMMERCIAL_DEMAND.test(text);
    return {
      expectation_status: ambiguousInfo ? EXPECTATION_STATUS.REVIEW_REQUIRED : EXPECTATION_STATUS.POLICY_DERIVED_EXPECTATION,
      expectation_class: ambiguousInfo ? 'review_required' : 'pre_authorized',
      expected_verdict: ambiguousInfo ? null : 'REJECT',
      authority_source: 'informational_self_service_exclusion_policy',
      review_required: ambiguousInfo,
      scored: !ambiguousInfo,
      selection_reason: ambiguousInfo ? 'informational framing with plausible service ambiguity' : 'informational/self-service exclusion policy',
      edge_cases: [...new Set(edgeCases)],
    };
  }

  if (evidence.product_only && !evidence.product_plus_service) {
    return {
      expectation_status: EXPECTATION_STATUS.POLICY_DERIVED_EXPECTATION,
      expectation_class: 'pre_authorized',
      expected_verdict: 'REJECT',
      authority_source: 'product_license_only_policy',
      review_required: false,
      scored: true,
      selection_reason: 'product/license-only demand separation',
      edge_cases: [...new Set(edgeCases)],
    };
  }

  if (evidence.ambiguous_diy_problem) {
    return {
      expectation_status: EXPECTATION_STATUS.POLICY_DERIVED_EXPECTATION,
      expectation_class: 'pre_authorized',
      expected_verdict: 'ABSTAIN',
      authority_source: 'ambiguous_diy_troubleshooting_policy',
      review_required: false,
      scored: true,
      selection_reason: 'ambiguous DIY troubleshooting — conservative abstain',
      edge_cases: [...new Set(edgeCases)],
    };
  }

  if (hasPositiveCommercialEvidence(text, evidence) && primaryFamily === 'direct_commercial_1c_service') {
    return {
      expectation_status: EXPECTATION_STATUS.POLICY_DERIVED_EXPECTATION,
      expectation_class: 'pre_authorized',
      expected_verdict: 'ACCEPT',
      authority_source: 'direct_commercial_service_demand_policy',
      review_required: false,
      scored: true,
      selection_reason: 'direct commercial service demand with positive evidence',
      edge_cases: [...new Set(edgeCases)],
    };
  }

  if (
    primaryFamily === 'generic_erp_platform_ambiguity'
    && !hasPositiveCommercialEvidence(text, evidence)
    && !(SERVICE_TASK.test(text) && ONE_C.test(text))
  ) {
    return {
      expectation_status: EXPECTATION_STATUS.POLICY_DERIVED_EXPECTATION,
      expectation_class: 'pre_authorized',
      expected_verdict: 'ABSTAIN',
      authority_source: 'generic_erp_platform_policy',
      review_required: true,
      scored: true,
      selection_reason: 'generic ERP/platform family — conservative abstain policy',
      edge_cases: [...new Set(edgeCases)],
    };
  }

  if (SERVICE_TASK.test(text) && ONE_C.test(text) && hasPositiveCommercialEvidence(text, evidence)) {
    return {
      expectation_status: EXPECTATION_STATUS.POLICY_DERIVED_EXPECTATION,
      expectation_class: 'pre_authorized',
      expected_verdict: 'ACCEPT',
      authority_source: 'explicit_service_task_with_1c_scope',
      review_required: false,
      scored: true,
      selection_reason: 'explicit 1C service task with commercial scope',
      edge_cases: [...new Set(edgeCases)],
    };
  }

  if (edgeCases.includes('psr_amb_01_family') || PSR_AMB_01.test(text)) {
    return {
      expectation_status: EXPECTATION_STATUS.REVIEW_REQUIRED,
      expectation_class: 'review_required',
      expected_verdict: null,
      authority_source: 'psr_amb_01_monitored_ambiguity',
      review_required: true,
      scored: false,
      selection_reason: 'PSR-AMB-01 monitored product-plus-service ambiguity family',
      edge_cases: [...new Set(edgeCases)],
    };
  }

  if (primaryFamily === 'ambiguous_mixed_intent' || BARE_ROLE_QUERY.test(text.trim()) || AMBIGUOUS_SHORT.test(text.trim())) {
    return {
      expectation_status: EXPECTATION_STATUS.REVIEW_REQUIRED,
      expectation_class: 'review_required',
      expected_verdict: null,
      authority_source: 'ambiguous_intent_policy',
      review_required: true,
      scored: false,
      selection_reason: 'mixed or insufficient commercial evidence — operator review',
      edge_cases: [...new Set(edgeCases)],
    };
  }

  return {
    expectation_status: EXPECTATION_STATUS.NO_GOLD_LABEL,
    expectation_class: 'review_required',
    expected_verdict: null,
    authority_source: null,
    review_required: true,
    scored: false,
    selection_reason: 'no authoritative closed-policy mapping',
    edge_cases: [...new Set(edgeCases)],
  };
}

export function classifyPhraseV2(record, context = {}) {
  const phrase = record.phrase || record.normalized_phrase || '';
  const text = (record.normalized_phrase || phrase).toLowerCase();
  const evidence = extractServiceIntentEvidence({
    raw_query: phrase,
    normalized_query: text,
  });
  const platform = evaluatePlatformCompatibility(
    { raw_query: phrase, normalized_query: text },
    context.businessScope,
    context.serviceRegistry,
  );
  const observed_tags = extractObservableTags(text, evidence, platform);
  const primary_family = assignCoverageFamily(text, evidence, platform, observed_tags);
  const expectation = deriveExpectationAuthority(text, evidence, platform, primary_family, observed_tags);

  return {
    classifier_version: CLASSIFIER_VERSION,
    phrase_id: record.phrase_id,
    phrase,
    normalized_phrase: text,
    observed_tags,
    primary_family,
    tags: observed_tags,
    edge_cases: expectation.edge_cases,
    evidence_summary: {
      strong_commercial: evidence.strong_commercial,
      strong_commercial_problem: evidence.strong_commercial_problem,
      product_only: evidence.product_only,
      product_plus_service: evidence.product_plus_service,
      product_version_update: evidence.product_version_update,
      ambiguous_diy_problem: evidence.ambiguous_diy_problem,
      career: evidence.career,
      education: evidence.education,
      diy: evidence.diy,
      informational: evidence.informational,
    },
    platform_classification: platform.classification,
    expectation_status: expectation.expectation_status,
    expectation_class: expectation.expectation_class,
    expected_verdict: expectation.expected_verdict,
    authority_source: expectation.authority_source,
    review_required: expectation.review_required,
    scored: expectation.scored,
    selection_reason: expectation.selection_reason,
  };
}

export function classifyCorpusV2(records, context = {}) {
  return records.map((r) => classifyPhraseV2(r, context));
}

export function validateExpectationPreflight(classified) {
  const violations = [];
  let careerAccept = 0;
  let educationAccept = 0;
  let informationalUnsupportedAccept = 0;
  let noAuthority = 0;
  const ids = new Set();

  for (const item of classified) {
    if (ids.has(item.phrase_id)) violations.push({ type: 'duplicate_id', phrase_id: item.phrase_id });
    ids.add(item.phrase_id);

    if (item.observed_tags?.includes('career') && item.expected_verdict === 'ACCEPT') careerAccept++;
    if (item.observed_tags?.includes('education') && item.expected_verdict === 'ACCEPT') educationAccept++;
    if (
      item.observed_tags?.includes('informational')
      && item.expected_verdict === 'ACCEPT'
      && !item.observed_tags?.includes('commercial_demand')
      && !item.observed_tags?.includes('strong_commercial')
    ) {
      informationalUnsupportedAccept++;
    }
    if (
      item.scored
      && item.expected_verdict
      && !item.authority_source
    ) {
      noAuthority++;
      violations.push({ type: 'no_authority_source', phrase_id: item.phrase_id });
    }
    if (
      item.primary_family === 'careers_training_education'
      && item.expected_verdict === 'ACCEPT'
    ) {
      violations.push({ type: 'career_education_accept_conflict', phrase_id: item.phrase_id });
    }
  }

  return {
    pass: careerAccept === 0
      && educationAccept === 0
      && informationalUnsupportedAccept === 0
      && noAuthority === 0
      && ids.size === classified.length,
    career_records_with_expected_accept: careerAccept,
    education_records_with_expected_accept: educationAccept,
    informational_unsupported_accept: informationalUnsupportedAccept,
    expectations_without_authority_source: noAuthority,
    selected_ids: ids.size,
    duplicate_ids: classified.length - ids.size,
    violations,
  };
}
