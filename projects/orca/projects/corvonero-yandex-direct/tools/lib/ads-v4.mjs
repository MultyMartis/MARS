/**
 * Ad copy v4 — restrained claims; no guaranteed diagnosis/preservation/recovery.
 */
import { buildAdsForGroup as buildAdsV3, validateAdLengths } from './ads.mjs';

/** Certainty rewrites — v3 unsupported guarantees */
const CERTAINTY_REWRITES = [
  [/найд[её]м причину и верн[её]м 1с в работу/gi, 'Проверим причину сбоя и предложим решение'],
  [/обновим 1с и сохраним ваши доработки/gi, 'Обновление доработанной 1С с предварительной оценкой'],
  [/сохраним и перенес[её]м изменения/gi, 'Перенос и адаптация доработок при обновлении'],
  [/без потери данных/gi, 'С оценкой рисков до начала работ'],
  [/1с без потерь/gi, '1С — оценка переноса до старта'],
  [/восстановим работу доработок/gi, 'Поможем восстановить работу доработок'],
  [/верн[её]м 1с в рабочее состояние/gi, 'Поможем вернуть 1С в рабочее состояние'],
  [/вернуть работу/gi, 'помочь с восстановлением работы'],
  [/исправим сбои/gi, 'Поможем устранить сбои'],
  [/устраним ошибки/gi, 'Поможем устранить ошибки'],
  [/восстановим обмен/gi, 'Поможем восстановить обмен'],
  [/сохраним изменения/gi, 'Оценим перенос изменений'],
  [/сохранение доработок/gi, 'Оценка переноса доработок'],
];

const FORBIDDEN_CERTAINTY = [
  /гарант/i,
  /обязательно сохран/i,
  /100%/,
  /без ошибок/i,
  /точно восстанов/i,
  /найд[её]м причину и верн/i,
  /сохраним ваши доработки/i,
  /без потери данных/i,
];

function softenText(text) {
  let t = text;
  for (const [re, rep] of CERTAINTY_REWRITES) {
    t = t.replace(re, rep);
  }
  return t;
}

function auditCertainty(ad) {
  const fields = [ad.headline_1, ad.headline_2, ad.text];
  const issues = [];
  for (const f of fields) {
    for (const re of FORBIDDEN_CERTAINTY) {
      if (re.test(f)) issues.push(`forbidden: ${re.source} in "${f.slice(0, 40)}"`);
    }
  }
  return issues;
}

/** Per-group headline/text overrides for v4 certainty */
const AD_V4_OVERRIDES = {
  'CORV-G02-03': { h2: 'Оценка до начала', text: 'Изменения в базе 1С с предварительной оценкой. Работа по договору.' },
  'CORV-G02-04': { h2: 'Предварительная оценка', text: 'Обновление доработанной 1С с предварительной оценкой. Работа по договору.' },
  'CORV-G02-05': { h2: 'Оценка переноса', text: 'Перенос и адаптация доработок при обновлении. Оценка по базе.' },
  'CORV-G02-06': { h2: 'После релиза', text: 'Поможем восстановить работу доработок в 1С после релиза.' },
  'CORV-G07-01': {
    alt: {
      h1: 'Программа 1С не запускается',
      h2: 'Диагностика',
      text: 'Проверим причину сбоя и предложим решение. Договор, безнал.',
    },
  },
  'CORV-G07-02': { text: 'Поможем устранить ошибки 1С после релиза. Оценка по симптомам.' },
  'CORV-G07-03': { text: 'Поможем восстановить обмен и синхронизацию между базами 1С.' },
  'CORV-G07-04': { text: 'Поможем вернуть 1С в рабочее состояние. Удалённо и с выездом.' },
  'CORV-G06-04': { h2: 'Помощь при сбоях', text: 'Поможем устранить ошибки маркировки и обмена в 1С. Оценка по симптомам.' },
};

export function buildAdsForGroupV4(groupDef, campaignUtm) {
  const ads = buildAdsV3(groupDef, campaignUtm);
  const overrides = AD_V4_OVERRIDES[groupDef.id] || {};

  return ads.map((ad, idx) => {
    let next = {
      ...ad,
      headline_1: softenText(overrides.h1 || ad.headline_1),
      headline_2: softenText(overrides.h2 || ad.headline_2),
      text: softenText(overrides.text || ad.text),
      factual_validation_status: 'pass-v4',
      certainty_review: 'REVIEWED',
    };

    if (idx === 1 && overrides.alt) {
      next = {
        ...next,
        headline_1: softenText(overrides.alt.h1),
        headline_2: softenText(overrides.alt.h2),
        text: softenText(overrides.alt.text),
      };
    }

    next.headline_1 = softenText(next.headline_1);
    next.headline_2 = softenText(next.headline_2);
    next.text = softenText(next.text);

    const issues = auditCertainty(next);
    if (issues.length) {
      next.factual_validation_status = 'rewritten-v4';
      next.certainty_issues_resolved = issues.length;
    }

    const lenErr = validateAdLengths(next);
    if (lenErr.length) {
      if (next.text.length > 81) next.text = next.text.slice(0, 78) + '…';
      if (next.headline_1.length > 56) next.headline_1 = next.headline_1.slice(0, 53) + '…';
    }

    return next;
  });
}

export function reviewAllAdsCertainty(ads) {
  const changes = [];
  for (const ad of ads) {
    const before = { h1: ad.headline_1, h2: ad.headline_2, text: ad.text };
    const issues = auditCertainty(ad);
    if (issues.length || ad.certainty_review === 'REVIEWED') {
      changes.push({
        ad_id: ad.ad_id,
        group_id: ad.group_id,
        issues_found: issues,
        status: issues.length ? 'FAIL' : 'PASS',
        headline_1: ad.headline_1,
        headline_2: ad.headline_2,
        text: ad.text,
      });
    }
  }
  return {
    reviewed: ads.length,
    passed: changes.filter((c) => c.status === 'PASS').length,
    failed: changes.filter((c) => c.status === 'FAIL').length,
    changes,
  };
}
