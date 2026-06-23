/**
 * Universal service-intent evidence layer — Wave 3.1F.
 * Project-independent patterns; not a closed 1С-only dictionary.
 */
export const SERVICE_INTENT_EVIDENCE_VERSION = 'v1.0';

const PROVIDER_NOUNS = /(?:программист|разработчик|специалист|мастер|юрист|бухгалтер|врач|инженер|консультант|администратор|аналитик|архитектор|дизайнер|монтажник|электрик|сантехник)/i;
const IMPLEMENTATION_TASKS = /(?:внедрен|настрой|интеграц|доработ|сопровожден|обслуживан|ремонт|установк|миграц|аудит|оптимизац|консультац|устран|исправ|восстанов)/i;
const PROCUREMENT_MODIFIERS = /(?:заказать|стоимость|цена|услуг|вызвать|нанять|под ключ|срочно|нужен|нужна|нужно)/i;
const PRICE_SERVICE = /(?:цена|стоимость|сколько стоит)\s+(?:настройк|внедрен|интеграц|обслуживан|сопровожден|ремонт|установк)/i;
const URGENT_PROBLEM = /(?:срочно|не работает|не открывается|ошибка.*(?:срочно|устранить|исправить)|восстановлен)/i;
const CAREER_MARKERS = /(?:ваканс|резюме|зарплат|устроиться|трудоустройств|ищу работу|работа программист)/i;
const EDUCATION_MARKERS = /(?:курс|обучен|тренинг|семинар|учеб)/i;
const DIY_MARKERS = /(?:самостоятельно|своими руками|как настроить|как установить|инструкция|самому)/i;
const INFORMATIONAL_GEO = /(?:где находится|адрес офиса|режим работы|как добраться)/i;
const PRODUCT_ACQUISITION = /(?:купить|скачать|лицензи(?:я|и|ю)|дистрибутив|коробочн)/i;
const GEOGRAPHY = /(?:москва|санкт-петербург|спб|екатеринбург|новосибирск|казань|нижний новгород|самара|ростов|краснодар|воронеж|пермь|волгоград|красноярск|тюмень|уфа|омск|челябинск|иркутск|хабаровск|владивосток)/i;
const BARE_ERROR = /^(?:ошибка|error)\s+[\w0x-]+/i;
const EXPLICIT_ERROR_RESOLUTION = /(?:устранить|исправить|специалист по ошибке|заказать.*ошибк|восстанов)/i;

export function extractServiceIntentEvidence(phrase) {
  const text = (phrase?.normalized_query || phrase?.raw_query || '').toLowerCase().trim();
  const signals = [];
  let strength = 'none';

  const hasGeo = GEOGRAPHY.test(text);
  const hasProvider = PROVIDER_NOUNS.test(text);
  const hasTask = IMPLEMENTATION_TASKS.test(text);
  const hasProcurement = PROCUREMENT_MODIFIERS.test(text);
  const hasPriceService = PRICE_SERVICE.test(text);
  const hasUrgent = URGENT_PROBLEM.test(text);
  const hasProductAcquisition = PRODUCT_ACQUISITION.test(text);
  const hasServiceScope = hasTask || hasProvider || hasPriceService || hasProcurement;
  const explicitErrorResolution = EXPLICIT_ERROR_RESOLUTION.test(text);
  const bareError = BARE_ERROR.test(text) || (/ошибка\s+[\w0x-]+/i.test(text) && !explicitErrorResolution);

  if (hasProvider) signals.push('provider_profession_noun');
  if (hasTask) signals.push('implementation_task');
  if (hasProcurement) signals.push('procurement_modifier');
  if (hasPriceService) signals.push('price_service_modifier');
  if (hasUrgent) signals.push('urgent_problem_resolution');
  if (hasGeo) signals.push('geography_modifier');

  const career = CAREER_MARKERS.test(text);
  const education = EDUCATION_MARKERS.test(text);
  const diy = DIY_MARKERS.test(text);
  const informational = INFORMATIONAL_GEO.test(text);
  const productOnly = hasProductAcquisition && !hasServiceScope;
  const productPlusService = hasProductAcquisition && hasServiceScope;
  const strongCommercialProblem = explicitErrorResolution && (hasUrgent || hasProvider || hasProcurement) && !diy;

  if (hasProvider && hasGeo && !career) {
    strength = 'strong';
    signals.push('provider_noun_plus_geography');
  } else if (hasTask && hasGeo && (hasProcurement || hasPriceService)) {
    strength = 'strong';
    signals.push('service_task_plus_geography');
  } else if (hasPriceService && hasGeo) {
    strength = 'strong';
    signals.push('price_service_plus_geography');
  } else if (hasUrgent && hasGeo && hasServiceScope) {
    strength = 'strong';
    signals.push('urgent_paid_problem_plus_geography');
  } else if (strongCommercialProblem) {
    strength = 'strong';
    signals.push('explicit_paid_error_resolution');
  } else if (productPlusService && hasGeo) {
    strength = 'strong';
    signals.push('product_plus_explicit_service_plus_geography');
  } else if (hasTask && hasGeo) {
    strength = 'supporting';
    signals.push('service_task_plus_geography_supporting');
  } else if (hasProvider && hasGeo) {
    strength = 'supporting';
  } else if (hasGeo && !hasServiceScope) {
    strength = 'insufficient';
    signals.push('geography_without_commercial_base');
  }

  const strongCommercial = (strength === 'strong' || strongCommercialProblem)
    && !career && !education && !diy && !informational && !productOnly;

  return {
    version: SERVICE_INTENT_EVIDENCE_VERSION,
    signals,
    evidence_strength: strength,
    strong_commercial_geo: strongCommercial && hasGeo,
    strong_commercial_problem: strongCommercialProblem,
    strong_commercial: strongCommercial,
    supporting_commercial_geo: strength === 'supporting' && !career && !productOnly,
    geography_alone: hasGeo && !hasServiceScope && !career && !education,
    career,
    education,
    diy,
    informational,
    product_only: productOnly,
    product_plus_service: productPlusService,
    bare_error_insufficient_context: bareError && !explicitErrorResolution && !hasProvider && !hasProcurement && !hasUrgent,
    provider_noun_detected: hasProvider,
    service_task_detected: hasTask,
    geography_detected: hasGeo,
    price_order_detected: hasProcurement || hasPriceService,
  };
}

export function resolveScopeFit(phrase, serviceRegistry) {
  const text = (phrase?.normalized_query || phrase?.raw_query || '').toLowerCase();
  const evidence = extractServiceIntentEvidence(phrase);
  const registryServices = serviceRegistry?.services || [];
  const is1cTopic = /(?:1с|1c|один[\s-]?эс)/i.test(text);

  if (!evidence.strong_commercial && !evidence.supporting_commercial_geo && !evidence.product_plus_service) {
    return { scope_fit: 'UNKNOWN', ownership: null, service_gap: false };
  }

  if (is1cTopic && registryServices.length > 0) {
    const task = evidence.service_task_detected ? 'svc-implementation' : 'svc-hire';
    return {
      scope_fit: 'IN_SCOPE',
      ownership: task,
      service_gap: false,
    };
  }

  if (evidence.strong_commercial || evidence.supporting_commercial_geo) {
    return {
      scope_fit: 'OUT_OF_SCOPE',
      ownership: 'SERVICE_GAP',
      service_gap: true,
    };
  }

  return { scope_fit: 'UNKNOWN', ownership: null, service_gap: false };
}
