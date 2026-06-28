/**
 * Deterministic semantic-family classifier for Corvonero Run 004 Phase 3 canary.
 * Primary family assignment uses fixed priority; tags allow multi-label edge-case tracking.
 */
import { extractServiceIntentEvidence } from '../../../../orca/semantic-intelligence/live-model/evidence/service-intent-evidence.mjs';
import {
  evaluatePlatformCompatibility,
  PLATFORM_CLASSIFICATION,
} from '../../../../orca/semantic-intelligence/live-model/evidence/platform-compatibility.mjs';

export const CANARY_SEED = 'corv-run004-canary-v1-20260628';
export const CANARY_SIZE = 120;

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
const CAREER = /(?:ваканс|резюме|зарплат|работа\s+программист|устроиться|трудоустройств|стажер|без\s+опыта\s+работ)/i;
const EDUCATION = /(?:курс|обучен|тренинг|семинар|учеб|с\s+нуля(?!\s+(?:настрой|внедрен)))/i;
const PRODUCT = /(?:купить|приобрест|лицензи|поставк|дистрибутив|коробочн|скачать\s+1с)/i;
const SERVICE = /(?:услуг|программист|стоимость|цена|заказать|под\s+ключ)/i;
const SERVICE_TASK = /(?:внедрен|настрой|сопровожден|доработк|интеграц(?:ия|ии|ию)|обслуживан|ремонт|миграц|аудит|оптимизац|консультац)/i;
const PROBLEM = /(?:ошибк|не\s+работает|сбой|0x[\da-f]+|исправить|устранить|fault|exception)/i;
const DIY_INFO = /(?:инструкци|самостоятельно|самому|как\s+(?:обновить|настроить|установить|исправить|устранить)|пошагов|форум|tutorial)/i;
const PRODUCT_BUNDLE = /(?:купить|приобрест|лицензи|поставк).*(?:1[\s-]?с|1c).*(?:настрой|внедрен|сопровожден)|(?:настрой|внедрен|сопровожден).*(?:1[\s-]?с|1c).*(?:купить|приобрест|лицензи|поставк)/i;

function isDirectCommercial(text, evidence) {
  return ONE_C.test(text)
    && SERVICE.test(text)
    && !CAREER.test(text)
    && !EDUCATION.test(text)
    && !DIY_INFO.test(text)
    && !evidence.product_only;
}

function isProblemTroubleshooting(text, evidence) {
  return PROBLEM.test(text)
    && !CAREER.test(text)
    && !/ошибки\s+программиста/i.test(text)
    && !evidence.strong_commercial;
}

function isGeographyCommercial(text, evidence) {
  return GEO.test(text)
    && ONE_C.test(text)
    && (SERVICE.test(text) || evidence.strong_commercial || evidence.supporting_commercial_geo);
}

export function classifyPhrase(record, context = {}) {
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
  const tags = [];
  const edgeCases = [];

  if (TS_PIOT.test(text)) tags.push('ts_piot');
  if (MARKING.test(text)) tags.push('marking_chestny_znak');
  if (INTEGRATION.test(text)) tags.push('integrations');
  if (GEO.test(text)) tags.push('geography');
  if (PRODUCT.test(text) && !SERVICE_TASK.test(text) && !PRODUCT_BUNDLE.test(text)) tags.push('product_only');
  if (ERP.test(text)) tags.push('erp_reference');
  if (PRODUCT_BUNDLE.test(text) || evidence.product_plus_service) {
    tags.push('product_plus_service_bundle');
    edgeCases.push('product_plus_service_bundle');
    edgeCases.push('psr_amb_01_family');
  }
  if (platform.classification === PLATFORM_CLASSIFICATION.GENERIC_PLATFORM_FAMILY || (ERP.test(text) && !ONE_C.test(text))) {
    tags.push('generic_erp_platform');
    edgeCases.push('generic_erp_ambiguity');
  }
  if (ERP.test(text) && /(?:обновлен|верси|update)/i.test(text)) {
    edgeCases.push('generic_erp_ambiguity');
  }
  if (platform.classification === PLATFORM_CLASSIFICATION.EXPLICIT_INCOMPATIBLE) {
    tags.push('foreign_incompatible_platform');
    edgeCases.push('foreign_incompatible_platform');
  }
  if (evidence.ambiguous_diy_problem) {
    tags.push('ambiguous_diy');
    edgeCases.push('ambiguous_diy_troubleshooting');
  }
  if (evidence.product_version_update && ONE_C.test(text)) {
    edgeCases.push('direct_1c_version_update_service');
  }
  if (evidence.product_self_update) edgeCases.push('self_service_update_instructions');
  if (isProblemTroubleshooting(text, evidence) && !evidence.strong_commercial_problem) {
    edgeCases.push('problem_without_commercial_marker');
  }

  let primaryFamily = 'ambiguous_mixed_intent';

  if (TS_PIOT.test(text)) {
    primaryFamily = 'ts_piot';
  } else if (MARKING.test(text)) {
    primaryFamily = 'marking_chestny_znak';
  } else if (INTEGRATION.test(text) && !isProblemTroubleshooting(text, evidence)) {
    primaryFamily = 'integrations';
  } else if (CAREER.test(text) || (EDUCATION.test(text) && !SERVICE.test(text))) {
    primaryFamily = 'careers_training_education';
  } else if (
    platform.classification === PLATFORM_CLASSIFICATION.GENERIC_PLATFORM_FAMILY
    || (ERP.test(text) && /(?:обновлен|верси|систем)/i.test(text))
  ) {
    primaryFamily = 'generic_erp_platform_ambiguity';
  } else if (PRODUCT.test(text) && !SERVICE_TASK.test(text) && !PRODUCT_BUNDLE.test(text) && !CAREER.test(text)) {
    primaryFamily = 'product_license_version';
  } else if (DIY_INFO.test(text) || evidence.diy || evidence.informational || evidence.product_self_update) {
    primaryFamily = 'informational_self_service';
  } else if (isProblemTroubleshooting(text, evidence)) {
    primaryFamily = 'problem_troubleshooting';
  } else if (isDirectCommercial(text, evidence) || evidence.strong_commercial || evidence.strong_commercial_problem) {
    primaryFamily = 'direct_commercial_1c_service';
  } else if (isGeographyCommercial(text, evidence) || (GEO.test(text) && ONE_C.test(text))) {
    primaryFamily = 'geography_modified';
  } else if (PRODUCT.test(text) && SERVICE.test(text)) {
    primaryFamily = 'ambiguous_mixed_intent';
  } else if (ERP.test(text) && !INTEGRATION.test(text)) {
    primaryFamily = 'generic_erp_platform_ambiguity';
  }

  const expectation = deriveExpectation(evidence, platform, primaryFamily, edgeCases);

  return {
    phrase_id: record.phrase_id,
    phrase,
    normalized_phrase: text,
    primary_family: primaryFamily,
    tags: [...new Set(tags)],
    edge_cases: [...new Set(edgeCases)],
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
    ...expectation,
  };
}

function deriveExpectation(evidence, platform, primaryFamily, edgeCases) {
  if (platform.classification === PLATFORM_CLASSIFICATION.EXPLICIT_INCOMPATIBLE) {
    return {
      expectation_class: 'pre_authorized',
      expected_verdict: 'REJECT',
      review_required: false,
      selection_reason: 'explicit foreign/incompatible platform policy',
    };
  }
  if (platform.classification === PLATFORM_CLASSIFICATION.GENERIC_PLATFORM_FAMILY || primaryFamily === 'generic_erp_platform_ambiguity') {
    return {
      expectation_class: 'pre_authorized',
      expected_verdict: 'ABSTAIN',
      review_required: true,
      selection_reason: 'generic ERP/platform family — conservative abstain policy (operator review)',
    };
  }
  if (evidence.career || evidence.education || primaryFamily === 'careers_training_education') {
    return {
      expectation_class: 'pre_authorized',
      expected_verdict: 'REJECT',
      review_required: false,
      selection_reason: 'career/training exclusion policy',
    };
  }
  if (evidence.product_only && !evidence.product_plus_service) {
    return {
      expectation_class: 'pre_authorized',
      expected_verdict: 'REJECT',
      review_required: false,
      selection_reason: 'product/license-only demand separation',
    };
  }
  if (evidence.ambiguous_diy_problem) {
    return {
      expectation_class: 'pre_authorized',
      expected_verdict: 'ABSTAIN',
      review_required: false,
      selection_reason: 'ambiguous DIY troubleshooting — conservative abstain',
    };
  }
  if (evidence.strong_commercial || evidence.strong_commercial_problem || primaryFamily === 'direct_commercial_1c_service') {
    return {
      expectation_class: 'pre_authorized',
      expected_verdict: 'ACCEPT',
      review_required: false,
      selection_reason: 'direct commercial service demand protection',
    };
  }
  if (edgeCases.includes('psr_amb_01_family') || evidence.product_plus_service) {
    return {
      expectation_class: 'review_required',
      expected_verdict: null,
      review_required: true,
      selection_reason: 'PSR-AMB-01 monitored product-plus-service ambiguity family',
    };
  }
  if (primaryFamily === 'ambiguous_mixed_intent') {
    return {
      expectation_class: 'review_required',
      expected_verdict: null,
      review_required: true,
      selection_reason: 'mixed intent requires operator/adjudicator review',
    };
  }
  return {
    expectation_class: 'review_required',
    expected_verdict: null,
    review_required: true,
    selection_reason: 'no authoritative closed-policy mapping',
  };
}

export function classifyCorpus(records, context = {}) {
  return records.map((r) => classifyPhrase(r, context));
}
