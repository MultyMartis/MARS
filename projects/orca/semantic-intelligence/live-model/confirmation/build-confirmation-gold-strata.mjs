#!/usr/bin/env node
/**
 * Build Wave 3.1E blind confirmation gold sets (product + geo-commercial).
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = __dirname;
const FREEZE_TS = new Date().toISOString();

function hashRecord(payload) {
  return crypto.createHash('sha256').update(JSON.stringify(payload)).digest('hex');
}

function phraseId(raw) {
  return crypto.createHash('sha256').update(raw).digest('hex').slice(0, 16);
}

function makeRecord({
  id, query, stratum, family, expectedDecision, protectedIntentClass,
  authorityBasis, rationale, ambiguity = 'CLEAR', contrast = false, geoClass = null,
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
    provenance: `confirmation_gold_${stratum}_${family}`,
    region: 'RU',
    contrast_positive: contrast,
    geo_class: geoClass,
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
    source_author: 'MARS-ORCA-CONFIRMATION-GOLD-DESIGNER-v1',
    reviewer_status: 'OPERATOR_REVIEW_PENDING',
    approval_status: 'FROZEN_PRE_RUN',
    evidence_class: 'gold',
    expected_authority_class: 'gold',
    checksum: hashRecord({ id, query, expectedDecision, protectedIntentClass }),
  };
  return { base, label };
}

const PRODUCTS = [
  'bitrix24', 'sap business one', 'autocad', 'adobe photoshop', 'microsoft office',
  'sql server', 'vmware vsphere', 'amoCRM', 'megaplan', 'mindbox crm',
  'контур диадок', 'крипто про', 'nano cad', 'solidworks', 'revit',
];

function pickProduct(n) { return PRODUCTS[(n - 1) % PRODUCTS.length]; }

function expand(prefix, template, family, count, decision, intent, basis, contrast = false, amb = 'CLEAR') {
  return Array.from({ length: count }, (_, i) => {
    const p = pickProduct(i + 1);
    const query = template.replace('{p}', p);
    return makeRecord({
      id: `${prefix}-${String(i + 1).padStart(2, '0')}`,
      query,
      stratum: 'protected_product_confirmation',
      family,
      expectedDecision: decision,
      protectedIntentClass: intent,
      authorityBasis: basis,
      rationale: `Confirmation product stratum: ${family}`,
      ambiguity: amb,
      contrast,
    });
  });
}

function buildProductConfirmation() {
  return [
    ...expand('CFM-PROD-BUY', 'купить коробку {p}', 'boxed_buy', 10, 'REJECT', 'product_only', 'confirmation gold policy'),
    ...expand('CFM-PROD-LIC', 'лицензия {p} купить официально', 'license_purchase', 10, 'REJECT', 'product_only', 'confirmation gold policy'),
    ...expand('CFM-PROD-VER', '{p} редакция professional цена', 'version_price', 8, 'REJECT', 'product_only', 'confirmation gold policy'),
    ...expand('CFM-PROD-DL', 'скачать дистрибутив {p}', 'download', 8, 'REJECT', 'product_only', 'confirmation gold policy'),
    ...expand('CFM-PROD-PRC', 'стоимость программы {p}', 'product_price', 10, 'REJECT', 'product_only', 'confirmation gold policy'),
    ...expand('CFM-PROD-CMP', 'сравнение {p} и конкурентов', 'product_compare', 8, 'REJECT', 'product_only', 'confirmation gold policy'),
    ...expand('CFM-PROD-UPD', 'обновление {p} до новой версии', 'product_update', 8, 'REJECT', 'product_only', 'confirmation gold policy'),
    ...expand('CFM-PROD-INS', 'установить {p} самостоятельно инструкция', 'self_install', 8, 'REJECT', 'diy', 'confirmation gold policy'),
    ...expand('CFM-PROD-BOX', 'коробочная поставка {p}', 'boxed_delivery', 10, 'REJECT', 'product_only', 'confirmation gold policy'),
    makeRecord({ id: 'CFM-PROD-AMB-01', query: 'autocad купить или заказать настройку', stratum: 'protected_product_confirmation', family: 'product_service_ambiguity', expectedDecision: 'ABSTAIN', protectedIntentClass: 'product_service', authorityBasis: 'confirmation gold policy', rationale: 'Dual intent', ambiguity: 'HARD_BORDERLINE' }),
    makeRecord({ id: 'CFM-PROD-AMB-02', query: 'нужна лицензия sql server или администратор', stratum: 'protected_product_confirmation', family: 'product_service_ambiguity', expectedDecision: 'ABSTAIN', protectedIntentClass: 'product_service', authorityBasis: 'confirmation gold policy', rationale: 'Dual intent', ambiguity: 'HARD_BORDERLINE' }),
    makeRecord({ id: 'CFM-PROD-AMB-03', query: 'bitrix24 цена коробка или абонентское обслуживание', stratum: 'protected_product_confirmation', family: 'product_service_ambiguity', expectedDecision: 'ABSTAIN', protectedIntentClass: 'product_service', authorityBasis: 'confirmation gold policy', rationale: 'Dual intent', ambiguity: 'ADVERSARIAL' }),
    makeRecord({ id: 'CFM-PROD-AMB-04', query: 'sap купить с внедрением', stratum: 'protected_product_confirmation', family: 'product_service_ambiguity', expectedDecision: 'ABSTAIN', protectedIntentClass: 'product_service', authorityBasis: 'confirmation gold policy', rationale: 'Dual intent', ambiguity: 'HARD_BORDERLINE' }),
    makeRecord({ id: 'CFM-PROD-AMB-05', query: 'офис microsoft лицензия или настройка exchange', stratum: 'protected_product_confirmation', family: 'product_service_ambiguity', expectedDecision: 'ABSTAIN', protectedIntentClass: 'product_service', authorityBasis: 'confirmation gold policy', rationale: 'Dual intent', ambiguity: 'ADVERSARIAL' }),
    makeRecord({ id: 'CFM-PROD-AMB-06', query: 'vmware лицензия стоимость', stratum: 'protected_product_confirmation', family: 'product_service_ambiguity', expectedDecision: 'REJECT', protectedIntentClass: 'product_only', authorityBasis: 'confirmation gold policy', rationale: 'Clear product price', ambiguity: 'CLEAR' }),
    ...expand('CFM-PROD-SVC', 'внедрение {p} под ключ', 'service_contrast', 10, 'ACCEPT', null, 'confirmation service contrast', true),
    ...expand('CFM-PROD-INT', 'интеграция {p} с сайтом заказать', 'integration_service', 10, 'ACCEPT', null, 'confirmation service contrast', true),
  ];
}

function buildGeoConfirmation() {
  const specs = [
    ...Array.from({ length: 15 }, (_, i) => makeRecord({
      id: `CFM-GEO-SVC-${String(i + 1).padStart(2, '0')}`,
      query: `заказать внедрение crm ${['москва', 'санкт-петербург', 'екатеринбург', 'новосибирск', 'казань'][i % 5]}`,
      stratum: 'geo_commercial_confirmation',
      family: 'explicit_service_geo',
      expectedDecision: 'ACCEPT',
      protectedIntentClass: null,
      authorityBasis: 'confirmation geo commercial gold',
      rationale: 'Service + geography',
      contrast: true,
      geoClass: 'commercial_geo',
    })),
    ...Array.from({ length: 15 }, (_, i) => makeRecord({
      id: `CFM-GEO-PRV-${String(i + 1).padStart(2, '0')}`,
      query: `программист bitrix ${['москва', 'екатеринбург', 'новосибирск', 'казань', 'самара'][i % 5]}`,
      stratum: 'geo_commercial_confirmation',
      family: 'provider_noun_geo',
      expectedDecision: 'ACCEPT',
      protectedIntentClass: null,
      authorityBasis: 'confirmation geo commercial gold',
      rationale: 'Provider noun + geo without career markers',
      contrast: true,
      geoClass: 'commercial_geo',
    })),
    ...Array.from({ length: 12 }, (_, i) => makeRecord({
      id: `CFM-GEO-ORD-${String(i + 1).padStart(2, '0')}`,
      query: `цена настройки sap ${['москва', 'санкт-петербург', 'нижний новгород'][i % 3]}`,
      stratum: 'geo_commercial_confirmation',
      family: 'price_order_geo',
      expectedDecision: 'ACCEPT',
      protectedIntentClass: null,
      authorityBasis: 'confirmation geo commercial gold',
      rationale: 'Price/order + geo',
      contrast: true,
      geoClass: 'commercial_geo',
    })),
    ...Array.from({ length: 10 }, (_, i) => makeRecord({
      id: `CFM-GEO-INF-${String(i + 1).padStart(2, '0')}`,
      query: `где находится офис amoCRM ${['москва', 'екатеринбург'][i % 2]}`,
      stratum: 'geo_commercial_confirmation',
      family: 'informational_geo',
      expectedDecision: 'REJECT',
      protectedIntentClass: 'informational',
      authorityBasis: 'confirmation geo adversarial gold',
      rationale: 'Informational geography',
      geoClass: 'noncommercial_geo',
    })),
    ...Array.from({ length: 10 }, (_, i) => makeRecord({
      id: `CFM-GEO-CAR-${String(i + 1).padStart(2, '0')}`,
      query: `вакансия программист 1с ${['москва', 'новосибирск', 'казань'][i % 3]}`,
      stratum: 'geo_commercial_confirmation',
      family: 'career_geo',
      expectedDecision: 'REJECT',
      protectedIntentClass: 'career',
      authorityBasis: 'confirmation geo adversarial gold',
      rationale: 'Career + geography',
      geoClass: 'noncommercial_geo',
    })),
    ...Array.from({ length: 8 }, (_, i) => makeRecord({
      id: `CFM-GEO-EDU-${String(i + 1).padStart(2, '0')}`,
      query: `курсы обучения autocad ${['москва', 'санкт-петербург'][i % 2]}`,
      stratum: 'geo_commercial_confirmation',
      family: 'education_geo',
      expectedDecision: 'REJECT',
      protectedIntentClass: 'education',
      authorityBasis: 'confirmation geo adversarial gold',
      rationale: 'Education + geography',
      geoClass: 'noncommercial_geo',
    })),
    ...Array.from({ length: 10 }, (_, i) => makeRecord({
      id: `CFM-GEO-PRD-${String(i + 1).padStart(2, '0')}`,
      query: `купить лицензию microsoft office ${['москва', 'екатеринбург', 'самара'][i % 3]}`,
      stratum: 'geo_commercial_confirmation',
      family: 'product_geo',
      expectedDecision: 'REJECT',
      protectedIntentClass: 'product_only',
      authorityBasis: 'confirmation geo adversarial gold',
      rationale: 'Product + geography not service hire',
      geoClass: 'noncommercial_geo',
    })),
    ...Array.from({ length: 8 }, (_, i) => makeRecord({
      id: `CFM-GEO-NAV-${String(i + 1).padStart(2, '0')}`,
      query: `адрес офиса контур ${['москва', 'новосибирск'][i % 2]}`,
      stratum: 'geo_commercial_confirmation',
      family: 'navigation_geo',
      expectedDecision: 'REJECT',
      protectedIntentClass: 'navigation',
      authorityBasis: 'confirmation geo adversarial gold',
      rationale: 'Navigation + geography',
      geoClass: 'noncommercial_geo',
    })),
    ...Array.from({ length: 12 }, (_, i) => makeRecord({
      id: `CFM-GEO-AMB-${String(i + 1).padStart(2, '0')}`,
      query: `${['москва', 'екатеринбург', 'казань', 'самара'][i % 4]}`,
      stratum: 'geo_commercial_confirmation',
      family: 'ambiguous_geo',
      expectedDecision: 'ABSTAIN',
      protectedIntentClass: 'ambiguous',
      authorityBasis: 'confirmation geo adversarial gold',
      rationale: 'Geography alone',
      ambiguity: 'HARD_BORDERLINE',
      geoClass: 'noncommercial_geo',
    })),
  ];
  return specs;
}

function writeStratum(name, records, setTitle) {
  const dir = path.join(ROOT, 'strata', name);
  fs.mkdirSync(dir, { recursive: true });
  const phrases = {
    corpus_id: `orca-confirmation-${name}-phrases-v1`,
    version: '1.0.0',
    confirmation_blind_validation: true,
    assessor_label_access: false,
    set_title: setTitle,
    record_count: records.length,
    records: records.map((r) => r.base),
  };
  const labels = {
    corpus_id: `orca-confirmation-${name}-gold-labels-v1`,
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
    set_title: setTitle,
    phrase_checksum: corpusChecksum,
    labels_checksum: labelsChecksum,
    combined_checksum: hashRecord({ corpusChecksum, labelsChecksum }),
    record_count: records.length,
    gold_record_count: records.length,
    contrast_positive_count: records.filter((r) => r.base.contrast_positive).length,
    frozen_at: FREEZE_TS,
    confirmation_blind_validation: true,
    calibration_forbidden: true,
    post_run_calibration_forbidden: true,
    model: 'openai/gpt-5-mini',
    provider: 'openrouter',
    prompt_version: 'orca-semantic-assessment-prompt-v1.2',
    policy_version: 'product-service-disambiguation-policy-v1',
    adjudicator_version: 'v1.2',
    author: 'MARS-ORCA-CONFIRMATION-GOLD-DESIGNER-v1',
    reviewer_status: 'FROZEN_PRE_RUN',
  };
  fs.writeFileSync(path.join(dir, 'phrases-blind-v1.json'), JSON.stringify(phrases, null, 2));
  fs.writeFileSync(path.join(dir, 'gold-labels-sealed-v1.json'), JSON.stringify(labels, null, 2));
  fs.writeFileSync(path.join(dir, 'manifest-v1.json'), JSON.stringify(manifest, null, 2));
  fs.writeFileSync(path.join(dir, 'freeze-record-v1.json'), JSON.stringify({
    freeze_timestamp: FREEZE_TS,
    phrase_checksum: corpusChecksum,
    labels_checksum: labelsChecksum,
    calibration_forbidden: true,
  }, null, 2));
  return manifest;
}

const productRecords = buildProductConfirmation();
const geoRecords = buildGeoConfirmation();
const productManifest = writeStratum('protected_product_confirmation', productRecords, 'PROTECTED PRODUCT BLIND CONFIRMATION SET V1');
const geoManifest = writeStratum('geo_commercial_confirmation', geoRecords, 'GEO COMMERCIAL BLIND CONFIRMATION SET V1');

console.log(JSON.stringify({
  product: { ...productManifest, record_count: productRecords.length },
  geo: { ...geoManifest, record_count: geoRecords.length },
  total: productRecords.length + geoRecords.length,
}, null, 2));
