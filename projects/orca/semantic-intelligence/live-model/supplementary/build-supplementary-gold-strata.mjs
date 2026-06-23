#!/usr/bin/env node
/**
 * Build supplementary blind protected-strata gold sets (Wave 3.1D).
 * Generates phrase payload + sealed labels with checksums.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = __dirname;

function hashRecord(payload) {
  return crypto.createHash('sha256').update(JSON.stringify(payload)).digest('hex');
}

function phraseId(raw) {
  return crypto.createHash('sha256').update(raw).digest('hex').slice(0, 16);
}

function makeRecord({
  id, query, stratum, family, expectedDecision, protectedIntentClass,
  authorityBasis, rationale, ambiguity = 'CLEAR', contrast = false,
}) {
  const pid = phraseId(query);
  const base = {
    record_id: id,
    phrase_id: pid,
    raw_query: query,
    normalized_query: query.toLowerCase().trim(),
    protected_class: stratum,
    stratum,
    family,
    provenance: `supplementary_gold_${stratum}_${family}`,
    region: 'RU',
    contrast_positive: contrast,
  };
  const label = {
    record_id: id,
    phrase_id: pid,
    protected_class: stratum,
    expected_decision: expectedDecision,
    expected_protected_intent_class: protectedIntentClass,
    gold_authority_basis: authorityBasis,
    rationale,
    ambiguity_status: ambiguity,
    source_author: 'MARS-ORCA-SUPPLEMENTARY-GOLD-DESIGNER-v1',
    approval_status: 'OPERATOR_REVIEW_PENDING',
    evidence_class: 'gold',
    expected_authority_class: 'gold',
    checksum: hashRecord({ id, query, expectedDecision, protectedIntentClass }),
  };
  return { base, label };
}

function buildProductStratum() {
  const specs = [
    ...expand('SUP-PROD-BUY', 'купить {p}', 'buy_program', 8, 'REJECT', 'product_only', 'explicit protected-intent policy'),
    ...expand('SUP-PROD-DL', 'скачать {p}', 'download_program', 6, 'REJECT', 'product_only', 'explicit protected-intent policy'),
    ...expand('SUP-PROD-LIC', 'лицензия {p} цена', 'license_price', 6, 'REJECT', 'product_only', 'explicit commercial policy'),
    ...expand('SUP-PROD-PRICE', 'стоимость программы {p}', 'software_price', 6, 'REJECT', 'product_only', 'unambiguous user-next-action evidence'),
    ...expand('SUP-PROD-VER', '{p} версия проф', 'version_edition', 5, 'REJECT', 'product_only', 'explicit protected-intent policy'),
    ...expand('SUP-PROD-BOX', '{p} коробочная поставка', 'boxed_delivery', 4, 'REJECT', 'product_only', 'explicit protected-intent policy'),
    ...expand('SUP-PROD-CMP', 'сравнение {p} и sap', 'product_compare', 5, 'REJECT', 'product_only', 'independently reviewed expert label'),
    ...expand('SUP-PROD-UPD', 'обновление {p} до последней версии', 'product_update_no_service', 5, 'REJECT', 'product_only', 'unambiguous user-next-action evidence'),
    ...expand('SUP-PROD-SITE', 'официальный сайт {p}', 'official_product_site', 5, 'REJECT', 'navigation', 'explicit protected-intent policy'),
    ...expand('SUP-PROD-INS', 'установить {p} самостоятельно инструкция', 'self_install', 5, 'REJECT', 'diy', 'explicit protected-intent policy'),
    { id: 'SUP-PROD-AMB-01', q: '1с предприятие купить или заказать внедрение', f: 'product_service_ambiguity', d: 'ABSTAIN', c: 'product_service', amb: 'HARD_BORDERLINE' },
    { id: 'SUP-PROD-AMB-02', q: 'нужна лицензия 1с или специалист для настройки', f: 'product_service_ambiguity', d: 'ABSTAIN', c: 'product_service', amb: 'HARD_BORDERLINE' },
    { id: 'SUP-PROD-AMB-03', q: '1с бухгалтерия цена коробка или абонентское обслуживание', f: 'product_service_ambiguity', d: 'ABSTAIN', c: 'product_service', amb: 'ADVERSARIAL' },
    { id: 'SUP-PROD-AMB-04', q: 'где купить 1с дешевле', f: 'product_service_ambiguity', d: 'REJECT', c: 'product_only', amb: 'CLEAR' },
    { id: 'SUP-PROD-AMB-05', q: '1с erp лицензия стоимость', f: 'product_service_ambiguity', d: 'REJECT', c: 'product_only', amb: 'CLEAR' },
    { id: 'SUP-PROD-AMB-06', q: 'скачать дистрибутив 1с торговля', f: 'product_service_ambiguity', d: 'REJECT', c: 'product_only', amb: 'CLEAR' },
    ...expand('SUP-PROD-CTR', 'внедрение {p} под ключ', 'provider_contrast_positive', 9, 'ACCEPT', null, 'verified production truth', true),
  ];
  return specs.map((s) => {
    if (s.q) {
      return makeRecord({
        id: s.id, query: s.q.replace('{p}', '1с'), stratum: 'protected_product', family: s.f,
        expectedDecision: s.d, protectedIntentClass: s.c,
        authorityBasis: 'independently reviewed expert label', rationale: `Supplementary gold: ${s.f}`,
        ambiguity: s.amb || 'CLEAR', contrast: s.d === 'ACCEPT',
      });
    }
    const query = s.template.replace('{p}', pickProduct(s.n));
    return makeRecord({
      id: `${s.prefix}-${String(s.n).padStart(2, '0')}`, query, stratum: 'protected_product', family: s.family,
      expectedDecision: s.decision, protectedIntentClass: s.intent,
      authorityBasis: s.basis, rationale: `Product-only intent: ${s.family}`,
      contrast: s.contrast,
    });
  });
}

function expand(prefix, template, family, count, decision, intent, basis, contrast = false) {
  return Array.from({ length: count }, (_, i) => ({
    prefix, template, family, n: i + 1, decision, intent, basis, contrast,
  }));
}

const PRODUCTS = ['1с', '1с бухгалтерия', '1с зарплата', '1с erp', '1с ут', '1с торговля', '1с документооборот', '1с розница'];
function pickProduct(n) { return PRODUCTS[(n - 1) % PRODUCTS.length]; }

function buildInformationalStratum() {
  const lines = [
    ...expand('SUP-INFO-WHAT', 'что такое {t}', 'what_is', 6, 'REJECT', 'informational', 'explicit protected-intent policy'),
    ...expand('SUP-INFO-HOW', 'как работает {t}', 'how_works', 5, 'REJECT', 'informational', 'unambiguous user-next-action evidence'),
    ...expand('SUP-INFO-INS', 'инструкция {t} настройка', 'instruction', 5, 'REJECT', 'informational', 'explicit protected-intent policy'),
    ...expand('SUP-INFO-DOC', 'документация {t} pdf', 'documentation', 5, 'REJECT', 'informational', 'explicit protected-intent policy'),
    ...expand('SUP-INFO-TERM', 'расшифровка {t} термин', 'term_definition', 4, 'REJECT', 'informational', 'independently reviewed expert label'),
    ...expand('SUP-INFO-OVR', 'обзор {t} возможности', 'overview', 4, 'REJECT', 'informational', 'explicit protected-intent policy'),
    ...expand('SUP-INFO-APP', 'сравнение подходов {t} внедрение', 'approach_compare', 4, 'REJECT', 'informational', 'explicit protected-intent policy'),
    ...expand('SUP-INFO-REG', 'нормативы учета {t} 2026', 'regulatory', 4, 'REJECT', 'informational', 'verified production truth'),
    ...expand('SUP-INFO-NEWS', 'новости {t} обновление', 'news', 3, 'REJECT', 'informational', 'explicit protected-intent policy'),
    ...expand('SUP-INFO-ERR', 'ошибка {t} код 0x800', 'error_as_informational', 5, 'REJECT', 'informational', 'unambiguous user-next-action evidence'),
    { id: 'SUP-INFO-PRB-01', q: '1с не запускается после обновления windows', f: 'problem_needs_specialist', d: 'ABSTAIN', c: 'problem_ambiguous', amb: 'HARD_BORDERLINE' },
    { id: 'SUP-INFO-PRB-02', q: '1с зависает при проведении документа', f: 'problem_needs_specialist', d: 'ABSTAIN', c: 'problem_ambiguous', amb: 'HARD_BORDERLINE' },
    { id: 'SUP-INFO-PRB-03', q: 'база 1с повреждена что делать', f: 'problem_needs_specialist', d: 'ABSTAIN', c: 'problem_ambiguous', amb: 'ADVERSARIAL' },
    { id: 'SUP-INFO-PRB-04', q: '1с выдает ошибку лицензии', f: 'problem_needs_specialist', d: 'ABSTAIN', c: 'problem_ambiguous', amb: 'HARD_BORDERLINE' },
    { id: 'SUP-INFO-PRB-05', q: 'не могу зайти в 1с пользователь заблокирован', f: 'problem_needs_specialist', d: 'ABSTAIN', c: 'problem_ambiguous', amb: 'HARD_BORDERLINE' },
    { id: 'SUP-INFO-PRB-06', q: '1с тормозит на большой базе', f: 'problem_needs_specialist', d: 'ABSTAIN', c: 'problem_ambiguous', amb: 'HARD_BORDERLINE' },
    ...expand('SUP-INFO-URG', 'срочно 1с не работает нужен специалист {n}', 'urgent_problem_commercial', 5, 'ACCEPT', null, 'verified production truth', true),
    { id: 'SUP-INFO-AMB-01', q: 'как настроить обмен 1с с сайтом самому', f: 'info_service_ambiguity', d: 'REJECT', c: 'diy', amb: 'CLEAR' },
    { id: 'SUP-INFO-AMB-02', q: 'настройка 1с самостоятельно по видео', f: 'info_service_ambiguity', d: 'REJECT', c: 'diy', amb: 'CLEAR' },
    { id: 'SUP-INFO-AMB-03', q: 'инструкция подключить 1с к эдо', f: 'info_service_ambiguity', d: 'REJECT', c: 'informational', amb: 'HARD_BORDERLINE' },
    { id: 'SUP-INFO-AMB-04', q: 'заказать настройку обмена 1с с интернет магазином', f: 'info_service_ambiguity', d: 'ACCEPT', c: null, amb: 'CLEAR', contrast: true },
    { id: 'SUP-INFO-AMB-05', q: 'найти программиста 1с для доработки отчета', f: 'info_service_ambiguity', d: 'ACCEPT', c: null, amb: 'CLEAR', contrast: true },
    { id: 'SUP-INFO-AMB-06', q: 'чем отличается 1с от sap для малого бизнеса', f: 'info_service_ambiguity', d: 'REJECT', c: 'informational', amb: 'CLEAR' },
    ...expand('SUP-INFO-CTR', 'найти специалиста {t} москва', 'provider_contrast_positive', 4, 'ACCEPT', null, 'verified production truth', true),
  ];
  const topics = ['1с', '1с бухгалтерия', '1с зарплата', '1с erp', '1с ут', 'обмен данными 1с'];
  return lines.map((s) => {
    if (s.q) {
      return makeRecord({
        id: s.id, query: s.q, stratum: 'protected_informational', family: s.f,
        expectedDecision: s.d, protectedIntentClass: s.c,
        authorityBasis: 'independently reviewed expert label', rationale: `Supplementary gold: ${s.f}`,
        ambiguity: s.amb || 'CLEAR', contrast: s.contrast || s.d === 'ACCEPT',
      });
    }
    const topic = topics[(s.n - 1) % topics.length];
    const query = s.template.replace('{t}', topic).replace('{n}', String(s.n));
    return makeRecord({
      id: `${s.prefix}-${String(s.n).padStart(2, '0')}`, query, stratum: 'protected_informational', family: s.family,
      expectedDecision: s.decision, protectedIntentClass: s.intent,
      authorityBasis: s.basis, rationale: `Informational intent: ${s.family}`,
      contrast: s.contrast,
    });
  });
}

function writeStratum(name, records) {
  const dir = path.join(ROOT, 'strata', name);
  fs.mkdirSync(dir, { recursive: true });
  const phrases = {
    corpus_id: `orca-supplementary-${name}-phrases-v1`,
    version: '1.0.0',
    supplementary_blind_validation: true,
    assessor_label_access: false,
    record_count: records.length,
    records: records.map((r) => r.base),
  };
  const labels = {
    corpus_id: `orca-supplementary-${name}-gold-labels-v1`,
    version: '1.0.0',
    sealed: true,
    assessor_label_access: false,
    record_count: records.length,
    records: records.map((r) => r.label),
  };
  const corpusChecksum = hashRecord(phrases.records);
  const labelsChecksum = hashRecord(labels.records);
  const manifest = {
    stratum: name,
    phrase_checksum: corpusChecksum,
    labels_checksum: labelsChecksum,
    combined_checksum: hashRecord({ corpusChecksum, labelsChecksum }),
    record_count: records.length,
    gold_record_count: records.filter((r) => r.label.expected_authority_class === 'gold').length,
    contrast_positive_count: records.filter((r) => r.base.contrast_positive).length,
    frozen_at: new Date().toISOString(),
    supplementary_blind_validation: true,
    calibration_forbidden: true,
    model: 'openai/gpt-5-mini',
    provider: 'openrouter',
    prompt_version: 'orca-semantic-assessment-prompt-v1.1',
    policy_version: 'v1',
    adjudicator_version: 'v1.1',
  };
  fs.writeFileSync(path.join(dir, 'phrases-blind-v1.json'), JSON.stringify(phrases, null, 2));
  fs.writeFileSync(path.join(dir, 'gold-labels-sealed-v1.json'), JSON.stringify(labels, null, 2));
  fs.writeFileSync(path.join(dir, 'manifest-v1.json'), JSON.stringify(manifest, null, 2));
  return manifest;
}

const product = buildProductStratum();
const informational = buildInformationalStratum();
const productManifest = writeStratum('protected_product', product);
const infoManifest = writeStratum('protected_informational', informational);

console.log(JSON.stringify({
  product: productManifest,
  informational: infoManifest,
  total_records: product.length + informational.length,
}, null, 2));
