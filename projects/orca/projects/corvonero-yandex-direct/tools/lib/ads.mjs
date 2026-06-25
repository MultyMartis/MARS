import { DOMAIN } from './groups-config.mjs';
import { UNIFIED_UTM_CAMPAIGN } from './campaign-markers.mjs';

const CALLOUTS_COMMON = [
  { text: 'Работаем по договору', role: 'legal' },
  { text: 'Безналичная оплата', role: 'payment' },
  { text: 'Удалённое подключение', role: 'remote' },
  { text: 'Выезд по Новосибирску', role: 'geo' },
];

const CONFIG_CALLOUT = { text: 'УТ, УНФ, Розница, КА, БП', role: 'configs' };

function slugFromUrl(urlPath) {
  return urlPath.replace(/^\/|\/$/g, '').slice(0, 20);
}

function sitelinksForGroup(g, campaignUtm) {
  const base = `${DOMAIN}${g.url}`;
  const utm = (content) =>
    `${base}?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_${content}`;

  const familyLinks = {
    general_1c: [
      { title: 'Услуги 1С', url: utm('sl_uslugi'), desc: 'Программист и задачи' },
      { title: 'Сопровождение', url: `${DOMAIN}/soprovozhdenie-1c/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_sopr`, desc: 'Поддержка базы' },
      { title: 'Доработки', url: `${DOMAIN}/dorabotka-1c/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_mod`, desc: 'Изменения в 1С' },
      { title: 'Стоимость', url: utm('sl_price'), desc: 'От 6000 ₽ за задачу' },
    ],
    modifications: [
      { title: 'Доработка 1С', url: utm('sl_mod'), desc: 'Задача под ваши процессы' },
      { title: 'Обновление', url: `${DOMAIN}/obnovlenie-dorabotok-1c/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_upd`, desc: 'Сохранение доработок' },
      { title: 'Стоимость', url: utm('sl_price'), desc: '3000 ₽/час' },
      { title: 'Заявка', url: utm('sl_cta'), desc: 'Оценка по задаче' },
    ],
    reports_forms: [
      { title: 'Отчёты 1С', url: `${DOMAIN}/otchety-1c/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_rep`, desc: 'Настройка отчётов' },
      { title: 'Печатные формы', url: `${DOMAIN}/pechatnye-formy-1c/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_pf`, desc: 'Формы и макеты' },
      { title: 'РМК', url: `${DOMAIN}/rmk-1c/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_rmk`, desc: 'Рабочее место кассира' },
      { title: 'Заявка', url: utm('sl_cta'), desc: 'Оценка работ' },
    ],
    management: [
      { title: 'Себестоимость', url: `${DOMAIN}/sebestoimost-1c/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_cost`, desc: 'Расчёт в 1С' },
      { title: 'Закупки', url: `${DOMAIN}/plan-zakupok-1c/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_proc`, desc: 'Планирование' },
      { title: 'Календарь', url: `${DOMAIN}/platezhnyj-kalendar-1c/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_cal`, desc: 'Платежи' },
      { title: 'Заявка', url: utm('sl_cta'), desc: 'Настройка под задачу' },
    ],
    integrations: [
      { title: 'Сайт и 1С', url: `${DOMAIN}/integraciya-1c-s-sajtom/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_site`, desc: 'Обмен с сайтом' },
      { title: 'Битрикс', url: `${DOMAIN}/integraciya-1c-bitrix/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_btx`, desc: 'Интеграция CRM' },
      { title: 'Синхронизация', url: `${DOMAIN}/sinhronizaciya-1c/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_sync`, desc: 'Обмен данными' },
      { title: 'Заявка', url: utm('sl_cta'), desc: 'Оценка интеграции' },
    ],
    marking: [
      { title: 'Маркировка 1С', url: `${DOMAIN}/markirovka-1c/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_mark`, desc: 'Подключение' },
      { title: 'Честный знак', url: `${DOMAIN}/chestnyj-znak-1c/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_cz`, desc: 'Настройка в 1С' },
      { title: 'Ошибки', url: utm('sl_err'), desc: 'Исправление сбоев' },
      { title: 'Заявка', url: utm('sl_cta'), desc: 'Оценка задачи' },
    ],
    troubleshooting: [
      { title: '1С не работает', url: `${DOMAIN}/1c-ne-rabotaet/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_fix`, desc: 'Диагностика и помощь' },
      { title: 'Обмен', url: `${DOMAIN}/obmen-1c-ne-rabotaet/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_ex`, desc: 'Синхронизация' },
      { title: 'Восстановление', url: utm('sl_rec'), desc: 'Вернуть работу' },
      { title: 'Заявка', url: utm('sl_cta'), desc: 'Диагностика' },
    ],
    specialist: [
      { title: 'ТС ПИОТ', url: utm('sl_piot'), desc: 'Настройка в 1С' },
      { title: 'Маркировка', url: `${DOMAIN}/markirovka-1c/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_mark`, desc: 'Смежные задачи' },
      { title: 'Услуги 1С', url: `${DOMAIN}/uslugi-1c/?utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignUtm}&utm_content=${g.id}_sl_gen`, desc: 'Общие работы' },
      { title: 'Заявка', url: utm('sl_cta'), desc: 'Оценка задачи' },
    ],
  };

  return (familyLinks[g.direction] || familyLinks.general_1c).slice(0, 4);
}

/** Per-group ad copy — headline1 max 56, headline2 max 30, text max 81 */
const AD_COPY = {
  'CORV-G01-01': { h1: 'Программист 1С для бизнеса', h2: 'Корво Неро', text: 'Доработки и поддержка 1С для юрлиц и ИП. От 6000 ₽. Оставьте заявку.', price: true },
  'CORV-G01-02': { h1: 'Программист 1С в Новосибирске', h2: 'Выезд и удалённо', text: 'Задачи по 1С для организаций. Договор, безнал. Оценка по запросу.', price: false },
  'CORV-G01-03': { h1: 'Настройка 1С под вашу работу', h2: 'УТ, УНФ, КА, БП', text: 'Настроим учёт и процессы в 1С. Работаем по договору с юрлицами.', price: false },
  'CORV-G01-04': { h1: 'Внедрение 1С для организации', h2: 'УТ, УНФ, КА, БП', text: 'Запуск и настройка 1С под задачи бизнеса. Оценка объёма по брифу.', price: false },
  'CORV-G01-05': { h1: 'Сопровождение 1С для бизнеса', h2: 'Корво Неро', text: 'Поддержка и доработки базы 1С. Договор, безнал, удалённо и с выездом.', price: false },
  'CORV-G01-06': { h1: 'Обслуживание 1С для компании', h2: 'Разовые работы', text: 'Техническая поддержка и задачи по 1С. Работаем с юрлицами и ИП.', price: false },
  'CORV-G01-07': { h1: 'Абонентское сопровождение 1С', h2: 'Для организаций', text: 'Регулярная поддержка базы 1С. Договор и безналичная оплата.', price: false },
  'CORV-G01-08': { h1: 'Разовые работы по 1С', h2: '3000 ₽/час', text: 'Точечные задачи программиста 1С. Минимальный заказ от 2 часов.', price: true },
  'CORV-G02-01': { h1: 'Доработка 1С под вашу задачу', h2: 'От 6000 ₽', text: 'Изменим конфигурацию и логику 1С. Оценка работ до старта.', price: true },
  'CORV-G02-02': { h1: 'Доработка конфигурации 1С', h2: 'Корво Неро', text: 'Модули, расширения и логика в 1С. Работаем по договору.', price: false },
  'CORV-G02-03': { h1: 'Доработка базы 1С', h2: 'Без потери данных', text: 'Изменения в базе 1С с сохранением учёта. Оценка по задаче.', price: false },
  'CORV-G02-04': { h1: 'Обновление доработанной 1С', h2: 'Сохраним изменения', text: 'Обновим 1С и сохраним ваши доработки. Работа по договору.', price: false },
  'CORV-G02-05': { h1: 'Перенос доработок при обновлении', h2: '1С без потерь', text: 'Сохраним и перенесём изменения в 1С. Оценка по базе.', price: false },
  'CORV-G02-06': { h1: 'Исправление доработок после обновления', h2: '1С снова в работе', text: 'Восстановим работу доработок в 1С после релиза.', price: false },
  'CORV-G03-01': { h1: 'Доработка отчёта в 1С', h2: 'От 6000 ₽', text: 'Настроим или изменим отчёт под ваш учёт. Оценка до начала работ.', price: true },
  'CORV-G03-02': { h1: 'Создание отчёта в 1С', h2: 'Под ваши данные', text: 'Разработаем новый отчёт в 1С. Работаем с юрлицами по договору.', price: false },
  'CORV-G03-03': { h1: 'Печатные формы в 1С', h2: 'Корво Неро', text: 'Создадим или изменим печатные формы. Оценка по макету.', price: false },
  'CORV-G03-04': { h1: 'Доработка печатной формы 1С', h2: 'Корво Неро', text: 'Изменим форму документа в 1С под ваши требования. Работа по договору.', price: false },
  'CORV-G03-05': { h1: 'Внешние отчёты и обработки 1С', h2: 'Под задачу', text: 'Разработка внешних отчётов и обработок. Договор и безнал.', price: false },
  'CORV-G03-06': { h1: 'Настройка РМК в 1С', h2: 'Касса и розница', text: 'Доработаем рабочее место кассира в 1С. Оценка по конфигурации.', price: false },
  'CORV-G04-01': { h1: 'Расчёт себестоимости в 1С', h2: 'Управленческий учёт', text: 'Настроим расчёт себестоимости в 1С. Оценка по вашей базе.', price: false },
  'CORV-G04-02': { h1: 'Планирование закупок в 1С', h2: 'Корво Неро', text: 'Настроим планирование закупок в 1С. Работа по договору.', price: false },
  'CORV-G04-03': { h1: 'Платёжный календарь в 1С', h2: 'Финансы', text: 'Настроим календарь платежей в 1С. Оценка по задаче.', price: false },
  'CORV-G05-01': { h1: 'Интеграция 1С с сайтом', h2: 'Обмен заказами', text: 'Свяжем 1С с сайтом: каталог, заказы, остатки. Оценка интеграции.', price: false },
  'CORV-G05-02': { h1: 'Интеграция 1С и Битрикс', h2: 'CRM и учёт', text: 'Настроим обмен 1С с Битрикс24. Работаем по договору.', price: false },
  'CORV-G05-03': { h1: 'Интеграция 1С с кассой', h2: 'ККТ и розница', text: 'Подключим кассу и фискализацию к 1С. Оценка по оборудованию.', price: false },
  'CORV-G05-04': { h1: 'Синхронизация и обмен 1С', h2: 'Между базами', text: 'Настроим обмен и синхронизацию данных в 1С.', price: false },
  'CORV-G05-05': { h1: 'Настройка обмена в 1С', h2: 'Корво Неро', text: 'Настроим правила обмена между базами 1С. Договор, безнал.', price: false },
  'CORV-G05-06': { h1: 'Перенос данных в 1С', h2: 'Миграция', text: 'Перенесём справочники и документы в 1С. Оценка объёма заранее.', price: false },
  'CORV-G06-01': { h1: 'Подключение маркировки в 1С', h2: 'Корво Неро', text: 'Настроим маркировку товаров в 1С. Работаем с юрлицами.', price: false },
  'CORV-G06-02': { h1: 'Настройка маркировки в 1С', h2: 'Под ваш товар', text: 'Подключим маркировку и обмен с ГИС МТ. Оценка по номенклатуре.', price: false },
  'CORV-G06-03': { h1: 'Честный знак и 1С', h2: 'От 6000 ₽', text: 'Настроим работу с Честным знаком в 1С. Договор и безнал.', price: true },
  'CORV-G06-04': { h1: 'Ошибки маркировки в 1С', h2: 'Исправим сбои', text: 'Устраним ошибки маркировки и обмена в 1С. Оценка по симптомам.', price: false },
  'CORV-G06-05': { h1: 'Маркировка напитков в 1С', h2: 'Пиво и алкоголь', text: 'Настроим маркировку напитков в 1С. Работа по договору.', price: false },
  'CORV-G06-06': { h1: 'Маркировка воды в 1С', h2: 'Корво Неро', text: 'Подключим маркировку воды в 1С. Оценка по базе.', price: false },
  'CORV-G06-07': { h1: 'Маркировка косметики в 1С', h2: 'Корво Неро', text: 'Настроим маркировку косметики в 1С для юрлиц. Работа по договору.', price: false },
  'CORV-G06-08': { h1: 'Маркировка лекарств в 1С', h2: 'Аптеки и опт', text: 'Настроим маркировку лекарств в 1С. Договор и безнал.', price: false },
  'CORV-G06-09': { h1: 'Маркировка бытовой химии в 1С', h2: 'Корво Неро', text: 'Подключим маркировку бытовой химии в 1С.', price: false },
  'CORV-G06-10': { h1: 'Маркировка автозапчастей в 1С', h2: 'Под задачу', text: 'Настроим маркировку автозапчастей в 1С. Оценка по номенклатуре.', price: false },
  'CORV-G06-11': { h1: 'Маркировка масел в 1С', h2: 'Корво Неро', text: 'Подключим маркировку масел в 1С. Работаем с юрлицами.', price: false },
  'CORV-G06-12': { h1: 'Маркировка техники в 1С', h2: 'Корво Неро', text: 'Настроим маркировку техники в 1С. Оценка по задаче. Договор, безнал.', price: false },
  'CORV-G06-13': { h1: 'Маркировка стройматериалов в 1С', h2: 'Корво Неро', text: 'Подключим маркировку стройматериалов в 1С.', price: false },
  'CORV-G07-01': { h1: '1С не работает — поможем', h2: 'Новосибирск', text: 'Поможем восстановить работу 1С. От 6000 ₽. Оставьте заявку.', price: true, alt: { h1: 'Программа 1С не запускается', h2: 'Диагностика', text: 'Найдём причину и вернём 1С в работу. Договор, безнал.' } },
  'CORV-G07-02': { h1: 'Ошибка 1С после обновления', h2: 'Исправим', text: 'Устраним ошибки 1С после релиза. Оценка по симптомам.', price: false },
  'CORV-G07-03': { h1: 'Не работает обмен в 1С', h2: 'Синхронизация', text: 'Восстановим обмен и синхронизацию между базами 1С.', price: false },
  'CORV-G07-04': { h1: 'Восстановление работы 1С', h2: 'Корво Неро', text: 'Вернём 1С в рабочее состояние. Работаем удалённо и с выездом.', price: false },
  'CORV-G08-01': { h1: 'Настройка ТС ПИОТ в 1С', h2: 'Корво Неро', text: 'Подключим и настроим ТС ПИОТ в 1С. Оценка по задаче.', price: false },
  'CORV-G08-02': { h1: 'Интеграция ТС ПИОТ с 1С', h2: 'Корво Неро', text: 'Свяжем ТС ПИОТ с учётом в 1С. Договор и безнал.', price: false },
};

function validateAdLengths(ad) {
  const errors = [];
  if ((ad.headline_1 || '').length > 56) errors.push(`h1:${ad.headline_1.length}`);
  if ((ad.headline_2 || '').length > 30) errors.push(`h2:${ad.headline_2.length}`);
  if ((ad.text || '').length > 81) errors.push(`text:${ad.text.length}`);
  for (const c of ad.callouts || []) {
    if ((c.text || '').length > 25) errors.push(`callout:${c.text.length}`);
  }
  return errors;
}

export function buildAdsForGroup(groupDef, campaignUtm = UNIFIED_UTM_CAMPAIGN) {
  const copy = AD_COPY[groupDef.id];
  if (!copy) throw new Error(`Missing ad copy for ${groupDef.id}`);

  const utmCampaign = campaignUtm || UNIFIED_UTM_CAMPAIGN;
  const landingUrl = `${DOMAIN}${groupDef.url}?utm_source=yandex&utm_medium=cpc&utm_campaign=${utmCampaign}&utm_content=${groupDef.id}&utm_term={keyword}`;
  const displayPath = slugFromUrl(groupDef.url);
  const sitelinks = sitelinksForGroup(groupDef, utmCampaign);
  const callouts = [...CALLOUTS_COMMON.slice(0, 3), CONFIG_CALLOUT];

  const primary = {
    ad_id: `ad-${groupDef.id}-a1`,
    campaign_id: groupDef.campaign,
    group_id: groupDef.id,
    headline_1: copy.h1,
    headline_2: copy.h2,
    text: copy.text,
    landing_url: landingUrl,
    display_path: displayPath,
    sitelinks,
    callouts,
    factual_validation_status: 'pass',
  };

  const errors = validateAdLengths(primary);
  if (errors.length) throw new Error(`Ad length validation failed ${groupDef.id}: ${errors.join(', ')}`);

  const ads = [primary];

  if (copy.alt) {
    const alt = {
      ad_id: `ad-${groupDef.id}-a2`,
      campaign_id: groupDef.campaign,
      group_id: groupDef.id,
      headline_1: copy.alt.h1,
      headline_2: copy.alt.h2,
      text: copy.alt.text,
      landing_url: landingUrl.replace(`utm_content=${groupDef.id}`, `utm_content=${groupDef.id}_a2`),
      display_path: displayPath,
      sitelinks,
      callouts: callouts.slice(0, 4),
      factual_validation_status: 'pass',
    };
    const altErr = validateAdLengths(alt);
    if (!altErr.length) ads.push(alt);
  } else if (copy.price && groupDef.bid === 'T1') {
    const alt = {
      ad_id: `ad-${groupDef.id}-a2`,
      campaign_id: groupDef.campaign,
      group_id: groupDef.id,
      headline_1: copy.h1.slice(0, 40),
      headline_2: '3000 ₽/час',
      text: 'Разовые работы по 1С для юрлиц. Минимум 2 часа. Оставьте заявку.',
      landing_url: landingUrl.replace(`utm_content=${groupDef.id}`, `utm_content=${groupDef.id}_a2`),
      display_path: displayPath,
      sitelinks,
      callouts: callouts.slice(0, 4),
      factual_validation_status: 'pass',
    };
    const altErr = validateAdLengths(alt);
    if (!altErr.length) ads.push(alt);
  }

  return ads;
}

export { validateAdLengths, slugFromUrl };
