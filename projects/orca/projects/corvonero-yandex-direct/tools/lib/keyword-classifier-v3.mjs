/**
 * Forensic keyword classification v3 — commercial intent first, no inline-minus repair.
 */
import {
  normPhrase,
  stripInlineNegatives,
  isActiveClassification as isActiveV2,
  classifyKeywordV2,
} from './keyword-classifier-v2.mjs';

export { normPhrase, stripInlineNegatives } from './keyword-classifier-v2.mjs';

/** Additional v3 exclusions — informational/regulatory not rescued by inline negatives */
const V3_HARD_EXCLUDE = new Set(
  [
    'как сделать печатную форму в 1с',
    'как изменить печатную форму в 1с',
    'как настроить печатную форму в 1с',
    'как настроить маркировку в 1с бухгалтерия',
    'как настроить маркировку в 1с розница',
    'как настроить маркировку в 1с ут',
    'как в 1с настроить маркировку товара',
    'как подключить маркировку в 1с',
    'маркировка автозапчастей сроки',
    'какие автозапчасти подлежат маркировке',
    'какие автозапчасти подлежат маркировке честный знак',
    'лекарства подлежащие маркировке',
    'знак маркировки на лекарствах',
    'исмет маркировка лекарств',
    'код маркировки лекарства',
    'программист 1с hh',
    'программист 1с бесплатно',
    'программист 1с скачать',
    '1с программист вакансии',
    'работа программист 1с',
    'удаленная работа программист 1с',
  ].map(normPhrase)
);

const V3_INFORMATIONAL_EXTRA = [
  /^как подключить/,
  /^как включить/,
  /^как выгрузить/,
  /^как загрузить/,
  /инструкция по/,
  /пошагов/,
  /видео как/,
  /образец документ/,
  /шаблон бесплатно/,
  /личный кабинет честный знак/,
  /проверить код маркировки/,
  /справочник маркируем/,
  /перечень товаров.*маркиров/,
  /норматив.*1с/,
  /закон.*маркиров/,
];

const V3_COMMERCIAL_SERVICE_SIGNALS =
  /услуг|заказ|специалист|аутсорс|для организац|для бизнес|для юрлиц|вызов|вызвать|найм|нанять|заказать|программист.*1с|1с.*программист|не работает|ошибк|восстанов|доработ|сопровож|внедрен|настрой|интеграц|маркиров|честный знак|обмен|синхрон|перенос.*данн|отчет|печатн|рмк|себестоим|закуп|календар|битрикс|касс|тс пиот|пиот/;

/**
 * @param {object} k MIG keyword record
 */
export function classifyKeywordV3(k) {
  const raw = k.source_phrase || k.normalized_phrase || '';
  const p = stripInlineNegatives(raw);

  if (V3_HARD_EXCLUDE.has(p)) {
    return { status: 'EXCLUDE_INFORMATIONAL', reason: 'v3_hard_exclude_list' };
  }

  const base = classifyKeywordV2(k);

  if (!isActiveV2(base)) return base;

  if (V3_INFORMATIONAL_EXTRA.some((re) => re.test(p)) && !V3_COMMERCIAL_SERVICE_SIGNALS.test(p)) {
    return { status: 'EXCLUDE_INFORMATIONAL', reason: 'v3_informational_pattern' };
  }

  if (base.status === 'KEEP_TEST' && (/^как /.test(p) || /подлеж.*маркиров/.test(p))) {
    return { status: 'EXCLUDE_INFORMATIONAL', reason: 'v3_no_test_on_informational_risk' };
  }

  if (/^как (сделать|изменить|настроить)/.test(p) && !/доработк|программист|услуг|заказ/.test(p)) {
    return { status: 'EXCLUDE_INFORMATIONAL', reason: 'v3_diy_howto' };
  }

  if (/подлеж.*маркиров|маркиров.*подлеж|сроки.*маркиров|какие .*маркиров/.test(p)) {
    return { status: 'EXCLUDE_REGULATORY', reason: 'v3_regulatory_listing' };
  }

  return base;
}

export function isActiveClassification(cls) {
  return isActiveV2(cls);
}
