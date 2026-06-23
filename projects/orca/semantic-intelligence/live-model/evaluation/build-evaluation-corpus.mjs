/**
 * Build evaluation corpus (~400 records) with holdout split.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import crypto from 'node:crypto';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIX = path.join(__dirname, '../fixtures');
const OUT = path.join(FIX, 'evaluation-corpus-v1.json');
const HOLDOUT_OUT = path.join(FIX, 'evaluation-holdout-v1.json');

const STRATA = {
  commercial_provider_search: { authority: 'gold', expected: 'ACCEPT', count: 45 },
  commercial_order: { authority: 'gold', expected: 'ACCEPT', count: 40 },
  commercial_price_quote: { authority: 'gold', expected: 'ACCEPT', count: 35 },
  commercial_urgent_specialist: { authority: 'gold', expected: 'ACCEPT', count: 30 },
  commercial_geo: { authority: 'silver', expected: 'ACCEPT', count: 30 },
  commercial_implementation: { authority: 'gold', expected: 'ACCEPT', count: 35 },
  commercial_recurring: { authority: 'silver', expected: 'ACCEPT', count: 25 },
  protected_career: { authority: 'gold', expected: 'REJECT', count: 50 },
  protected_education: { authority: 'gold', expected: 'REJECT', count: 45 },
  protected_diy: { authority: 'gold', expected: 'REJECT', count: 45 },
  protected_navigation: { authority: 'gold', expected: 'REJECT', count: 35 },
  protected_download: { authority: 'gold', expected: 'REJECT', count: 30 },
  protected_product: { authority: 'silver', expected: 'REJECT', count: 35 },
  protected_informational: { authority: 'silver', expected: 'REJECT', count: 30 },
  problem_query: { authority: 'silver', expected: 'ABSTAIN', count: 35 },
  short_ambiguous: { authority: 'diagnostic', expected: 'ABSTAIN', count: 30 },
  mixed_intent: { authority: 'adversarial', expected: 'REJECT', count: 25 },
  ownership_ambiguity: { authority: 'adversarial', expected: 'ABSTAIN', count: 20 },
  corvonero_fp: { authority: 'diagnostic', expected: 'REJECT', count: 25 },
  minimal_pair: { authority: 'adversarial', expected: null, count: 20 },
};

const TEMPLATES = {
  commercial_provider_search: (i) => `найти программиста 1с ${i}`,
  commercial_order: (i) => `заказать доработку 1с ${i}`,
  commercial_price_quote: (i) => `стоимость внедрения 1с ${i}`,
  commercial_urgent_specialist: (i) => `срочно нужен специалист 1с ${i}`,
  commercial_geo: (i) => `программист 1с москва ${i}`,
  commercial_implementation: (i) => `внедрение 1с под ключ ${i}`,
  commercial_recurring: (i) => `абонентское обслуживание 1с ${i}`,
  protected_career: (i) => `вакансии программист 1с ${i}`,
  protected_education: (i) => `курсы 1с с нуля ${i}`,
  protected_diy: (i) => `как настроить 1с самостоятельно ${i}`,
  protected_navigation: (i) => `1с личный кабинет ${i}`,
  protected_download: (i) => `скачать 1с бесплатно ${i}`,
  protected_product: (i) => `купить лицензию 1с ${i}`,
  protected_informational: (i) => `что такое 1с ${i}`,
  problem_query: (i) => `1с не работает ${i}`,
  short_ambiguous: (i) => (i % 2 === 0 ? '1с' : 'программист'),
  mixed_intent: (i) => `программист 1с и вакансии ${i}`,
  ownership_ambiguity: (i) => `настройка 1с ${i}`,
  corvonero_fp: (i) => ['скачать 1с торрент', '1с управление торговлей бесплатно', '1с предприятие что это'][i % 3],
  minimal_pair: (i) => (i % 2 === 0 ? 'найти программиста 1с' : 'вакансия программист 1с'),
};

function stableId(stratum, i) {
  return `EVAL-${stratum.slice(0, 3).toUpperCase()}-${String(i).padStart(3, '0')}`;
}

function buildRecords() {
  const records = [];
  for (const [stratum, cfg] of Object.entries(STRATA)) {
    const tmpl = TEMPLATES[stratum];
    for (let i = 1; i <= cfg.count; i++) {
      const raw = typeof tmpl(i) === 'string' ? tmpl(i) : tmpl(i);
      const expected = cfg.expected ?? (stratum === 'minimal_pair' ? (i % 2 === 0 ? 'ACCEPT' : 'REJECT') : cfg.expected);
      records.push({
        record_id: stableId(stratum, i),
        phrase_id: crypto.createHash('sha256').update(`${stratum}:${i}:${raw}`).digest('hex').slice(0, 16),
        raw_query: raw,
        normalized_query: raw.toLowerCase().trim(),
        stratum,
        provenance: stratum.startsWith('corvonero') ? 'corvonero_diagnostic_failure' : `synthetic_${stratum}`,
        evidence_class: cfg.authority,
        expected_authority_class: cfg.authority,
        expected_decision: expected,
        region: 'RU',
      });
    }
  }
  return records;
}

function splitHoldout(records, holdoutRatio = 0.2) {
  const holdoutSize = Math.floor(records.length * holdoutRatio);
  const shuffled = [...records].sort((a, b) => a.phrase_id.localeCompare(b.phrase_id));
  const holdout = shuffled.slice(0, holdoutSize);
  const holdoutIds = new Set(holdout.map((r) => r.record_id));
  const calibration = records.filter((r) => !holdoutIds.has(r.record_id));
  return { calibration, holdout };
}

const allRecords = buildRecords();
const { calibration, holdout } = splitHoldout(allRecords);

fs.mkdirSync(FIX, { recursive: true });
fs.writeFileSync(OUT, JSON.stringify({
  corpus_id: 'orca-live-eval-corpus-v1',
  version: '1.0.0',
  record_count: calibration.length,
  holdout_reserved: holdout.length,
  note: 'Gold/silver/diagnostic/adversarial authority declared per record; diagnostic not used for D3 gate pass',
  records: calibration,
}, null, 2));

fs.writeFileSync(HOLDOUT_OUT, JSON.stringify({
  corpus_id: 'orca-live-eval-holdout-v1',
  version: '1.0.0',
  record_count: holdout.length,
  blind_holdout: true,
  note: 'Reserved before calibration — not used for prompt/rule tuning',
  records: holdout,
}, null, 2));

console.log(`Evaluation corpus: ${calibration.length} calibration + ${holdout.length} holdout = ${allRecords.length} total`);
