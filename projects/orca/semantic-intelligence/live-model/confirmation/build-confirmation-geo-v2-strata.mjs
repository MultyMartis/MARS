#!/usr/bin/env node
/**
 * Build GEO COMMERCIAL BLIND CONFIRMATION SET V2 — Wave 3.1F.
 * New IDs, new formulations, no V1 false-reject phrases.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.join(__dirname, 'strata', 'geo_commercial_confirmation_v2');
const FREEZE_TS = new Date().toISOString();

const CITIES = ['краснодар', 'ростов-на-дону', 'воронеж', 'пермь', 'тюмень', 'уфа', 'омск', 'челябинск', 'иркутск', 'хабаровск', 'владивосток', 'ярославль', 'томск', 'барнаул'];

function hashRecord(payload) {
  return crypto.createHash('sha256').update(JSON.stringify(payload)).digest('hex');
}
function phraseId(raw) {
  return crypto.createHash('sha256').update(raw).digest('hex').slice(0, 16);
}

function rec(id, query, family, decision, intent, basis, contrast, geoClass, scopeFit = null, amb = 'CLEAR') {
  const pid = phraseId(query);
  return {
    base: {
      record_id: id, phrase_id: pid, raw_query: query, normalized_query: query.toLowerCase().trim(),
      protected_class: 'geo_commercial_confirmation_v2', stratum: 'geo_commercial_confirmation_v2',
      family, provenance: `confirmation_v2_${family}`, region: 'RU', contrast_positive: contrast,
      geo_class: geoClass,
    },
    label: {
      record_id: id, phrase_id: pid, protected_class: 'geo_commercial_confirmation_v2',
      expected_decision: decision,
      expected_scope_fit: scopeFit || (decision === 'ACCEPT' ? 'VARIES' : 'N/A'),
      expected_protected_intent_class: intent,
      gold_authority_basis: basis,
      rationale: `Geo V2 stratum: ${family}`,
      ambiguity_status: amb,
      source_author: 'MARS-ORCA-CONFIRMATION-GOLD-DESIGNER-v2',
      reviewer_status: 'OPERATOR_REVIEW_PENDING',
      approval_status: 'FROZEN_PRE_RUN',
      evidence_class: 'gold',
      expected_authority_class: 'gold',
      checksum: hashRecord({ id, query, decision, intent, scopeFit }),
    },
  };
}

function build() {
  const out = [];
  let n = 0;
  const next = (prefix) => `${prefix}-${String(++n).padStart(3, '0')}`;

  const providers = [
    ['разработчик django', 'provider_profession_geo'],
    ['специалист по wordpress', 'provider_profession_geo'],
    ['мастер по ремонту холодильников', 'provider_profession_geo'],
    ['юрист по недвижимости', 'provider_profession_geo'],
    ['бухгалтер аутсорс', 'provider_profession_geo'],
  ];
  for (const [p, fam] of providers) {
    for (let i = 0; i < 4; i++) {
      const city = CITIES[(n + i) % CITIES.length];
      out.push(rec(next('CFM2-GEO-PRV'), `${p} ${city}`, fam, 'ACCEPT', null, 'geo v2 commercial gold', true, 'commercial_geo', 'OUT_OF_SCOPE'));
    }
  }

  const providers2 = [
    ['инженер по вентиляции', 'provider_profession_geo'],
    ['дизайнер интерьера', 'provider_profession_geo'],
    ['консультант по crm', 'provider_profession_geo'],
    ['администратор linux', 'provider_profession_geo'],
  ];
  for (const [p, fam] of providers2) {
    for (let i = 0; i < 3; i++) {
      out.push(rec(next('CFM2-GEO-PRV'), `${p} ${CITIES[(n + i) % CITIES.length]}`, fam, 'ACCEPT', null, 'geo v2 commercial gold', true, 'commercial_geo', 'OUT_OF_SCOPE'));
    }
  }

  const tasks = [
    ['заказать интеграцию odoo', 'implementation_task_geo'],
    ['внедрение hubspot под ключ', 'implementation_task_geo'],
    ['настройка zabbix мониторинг', 'implementation_task_geo'],
    ['доработка laravel приложения', 'implementation_task_geo'],
    ['сопровождение kubernetes кластера', 'implementation_task_geo'],
    ['миграция данных mysql', 'implementation_task_geo'],
    ['аудит безопасности сети', 'implementation_task_geo'],
  ];
  for (const [t, fam] of tasks) {
    for (let i = 0; i < 3; i++) {
      out.push(rec(next('CFM2-GEO-TSK'), `${t} ${CITIES[n % CITIES.length]}`, fam, 'ACCEPT', null, 'geo v2 commercial gold', true, 'commercial_geo'));
    }
  }

  const prices = [
    ['стоимость внедрения oracle', 'price_order_geo'],
    ['цена настройки joomla', 'price_order_geo'],
    ['сколько стоит интеграция salesforce', 'price_order_geo'],
    ['цена обслуживания asterisk', 'price_order_geo'],
    ['цена доработки magento', 'price_order_geo'],
    ['стоимость миграции exchange', 'price_order_geo'],
  ];
  for (const [p, fam] of prices) {
    for (let i = 0; i < 3; i++) {
      out.push(rec(next('CFM2-GEO-PRC'), `${p} ${CITIES[(n + i) % CITIES.length]}`, fam, 'ACCEPT', null, 'geo v2 commercial gold', true, 'commercial_geo', 'OUT_OF_SCOPE'));
    }
  }

  const prodSvc = [
    ['настройка figma корпоративный аккаунт', 'product_service_geo'],
    ['внедрение slack для команды', 'product_service_geo'],
    ['интеграция trello с crm', 'product_service_geo'],
    ['специалист adobe premiere', 'product_service_geo'],
  ];
  for (const [p, fam] of prodSvc) {
    for (let i = 0; i < 3; i++) {
      out.push(rec(next('CFM2-GEO-PSV'), `${p} ${CITIES[n % CITIES.length]}`, fam, 'ACCEPT', null, 'geo v2 commercial gold', true, 'commercial_geo'));
    }
  }

  const urgent = [
    ['срочно восстановить базу postgresql', 'urgent_problem_geo'],
    ['не работает vpn офис срочно мастер', 'urgent_problem_geo'],
    ['срочно настроить почтовый сервер', 'urgent_problem_geo'],
  ];
  for (const [u, fam] of urgent) {
    for (let i = 0; i < 2; i++) {
      out.push(rec(next('CFM2-GEO-URG'), `${u} ${CITIES[n % CITIES.length]}`, fam, 'ACCEPT', null, 'geo v2 commercial gold', true, 'commercial_geo'));
    }
  }

  const oos = [
    ['заказать клининг офиса', 'out_of_scope_commercial'],
    ['вызвать электрика', 'out_of_scope_commercial'],
    ['нанять маркетолога', 'out_of_scope_commercial'],
  ];
  for (const [q, fam] of oos) {
    for (let i = 0; i < 2; i++) {
      out.push(rec(next('CFM2-GEO-OOS'), `${q} ${CITIES[n % CITIES.length]}`, fam, 'ACCEPT', null, 'geo v2 out-of-scope commercial', true, 'commercial_geo', 'OUT_OF_SCOPE'));
    }
  }

  const svcNoun = [
    ['seo продвижение', 'service_noun_geo'],
    ['видеонаблюдение установка', 'service_noun_geo'],
    ['облачный хостинг', 'service_noun_geo'],
  ];
  for (const [s, fam] of svcNoun) {
    for (let i = 0; i < 2; i++) {
      out.push(rec(next('CFM2-GEO-SNV'), `${s} ${CITIES[n % CITIES.length]}`, fam, 'ACCEPT', null, 'geo v2 supporting commercial', true, 'commercial_geo', null, 'ADVERSARIAL'));
    }
  }

  const adversarial = [
    ['вакансия разработчик python', 'career_geo', 'REJECT', 'career'],
    ['курсы data science', 'education_geo', 'REJECT', 'education'],
    ['купить лицензию autocad', 'product_geo', 'REJECT', 'product_only'],
    ['адрес офиса яндекс', 'navigation_geo', 'REJECT', 'navigation'],
    ['где находится склад ozon', 'informational_geo', 'REJECT', 'informational'],
    ['краснодар', 'ambiguous_geo', 'ABSTAIN', 'ambiguous'],
  ];
  for (const [q, fam, dec, intent] of adversarial) {
    for (let i = 0; i < (fam === 'ambiguous_geo' ? 4 : 3); i++) {
      const city = fam === 'ambiguous_geo' ? q : `${q} ${CITIES[n % CITIES.length]}`;
      out.push(rec(next('CFM2-GEO-ADV'), city, fam, dec, intent, 'geo v2 adversarial gold', false, 'noncommercial_geo', 'N/A', fam === 'ambiguous_geo' ? 'HARD_BORDERLINE' : 'CLEAR'));
    }
  }

  return out;
}

const records = build();
fs.mkdirSync(ROOT, { recursive: true });
const phrases = {
  corpus_id: 'orca-confirmation-geo-commercial-v2-phrases',
  version: '2.0.0',
  confirmation_blind_validation: true,
  commercial_intent_label_separate_from_scope_fit: true,
  assessor_label_access: false,
  set_title: 'GEO COMMERCIAL BLIND CONFIRMATION SET V2',
  record_count: records.length,
  records: records.map((r) => r.base),
};
const labels = {
  corpus_id: 'orca-confirmation-geo-commercial-v2-gold-labels',
  version: '2.0.0',
  sealed: true,
  commercial_intent_label_separate_from_scope_fit: true,
  assessor_label_access: false,
  record_count: records.length,
  records: records.map((r) => r.label),
};
const corpusChecksum = hashRecord(phrases.records);
const labelsChecksum = hashRecord(labels.records);
const manifest = {
  stratum: 'geo_commercial_confirmation_v2',
  set_title: 'GEO COMMERCIAL BLIND CONFIRMATION SET V2',
  phrase_checksum: corpusChecksum,
  labels_checksum: labelsChecksum,
  combined_checksum: hashRecord({ corpusChecksum, labelsChecksum }),
  record_count: records.length,
  gold_record_count: records.length,
  contrast_positive_count: records.filter((r) => r.base.contrast_positive).length,
  frozen_at: FREEZE_TS,
  confirmation_blind_validation: true,
  commercial_intent_label_separate_from_scope_fit: true,
  calibration_forbidden: true,
  post_run_calibration_forbidden: true,
  model: 'openai/gpt-5-mini',
  provider: 'openrouter',
  prompt_version: 'orca-semantic-assessment-prompt-v1.3',
  policy_version: 'geo-evidence-policy-v2',
  adjudicator_version: 'v1.3',
  author: 'MARS-ORCA-CONFIRMATION-GOLD-DESIGNER-v2',
  reviewer_status: 'FROZEN_PRE_RUN',
  v1_phrase_exclusion: true,
};
fs.writeFileSync(path.join(ROOT, 'phrases-blind-v2.json'), JSON.stringify(phrases, null, 2));
fs.writeFileSync(path.join(ROOT, 'gold-labels-sealed-v2.json'), JSON.stringify(labels, null, 2));
fs.writeFileSync(path.join(ROOT, 'manifest-v2.json'), JSON.stringify(manifest, null, 2));
fs.writeFileSync(path.join(ROOT, 'freeze-record-v2.json'), JSON.stringify({
  freeze_timestamp: FREEZE_TS,
  phrase_checksum: corpusChecksum,
  labels_checksum: labelsChecksum,
  calibration_forbidden: true,
  commercial_intent_label_separate_from_scope_fit: true,
}, null, 2));
console.log(JSON.stringify({ record_count: records.length, manifest }, null, 2));
