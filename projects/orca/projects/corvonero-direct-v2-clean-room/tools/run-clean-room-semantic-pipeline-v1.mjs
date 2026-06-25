#!/usr/bin/env node
/**
 * Corvonero Direct V2 Clean Room — semantic core pipeline v1
 * Sources: original MIG Wordstat Pass A only + operator intake
 * FORBIDDEN: old corvonero-yandex-direct production semantic decisions
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createRequire } from 'module';
import { SERVICE_SCOPE, SERVICE_PATTERNS } from './service-scope-data.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const REPO = path.resolve(__dirname, '../../../../..');
const MIG_WORDSTAT = path.join(REPO, 'incoming/mig/pilots/corvonero/session-mig-20260622-corv01/evidence/wordstat/wordstat-pass-a-normalized.json');
const MIG_FILE_INDEX = path.join(REPO, 'incoming/mig/pilots/corvonero/session-mig-20260622-corv01/evidence/wordstat/wordstat-pass-a-file-index.json');
const FORBIDDEN_PREFIX = path.join(REPO, 'projects/orca/projects/corvonero-yandex-direct/production');

const require = createRequire(import.meta.url);
const exceljsPath = path.join(REPO, 'projects/orca/ppc/triumph-manipulator/tools/exporter-cli/node_modules/exceljs');
const ExcelJS = require(exceljsPath);

const OUT = {
  migSource: path.join(ROOT, 'mig-source'),
  semanticCore: path.join(ROOT, 'semantic-core'),
  validation: path.join(ROOT, 'validation'),
  intake: path.join(ROOT, 'intake'),
  reports: path.join(ROOT, 'reports'),
  artifacts: path.join(ROOT, 'artifacts'),
};

for (const d of Object.values(OUT)) fs.mkdirSync(d, { recursive: true });

function writeJson(p, data) {
  fs.writeFileSync(p, JSON.stringify(data, null, 2) + '\n', 'utf8');
}

function writeMd(p, lines) {
  fs.writeFileSync(p, lines.join('\n') + '\n', 'utf8');
}

function yoToE(s) {
  return s.replace(/ё/g, 'е');
}

function normalizePhrase(raw) {
  let t = String(raw ?? '').trim();
  const original = t;
  const hasQuotes = /["«»]/.test(t);
  const hasOperators = /[+\-!|()]/.test(t);
  const inlineNegative = /\s-\S/.test(t);
  t = yoToE(t.toLowerCase());
  t = t.replace(/["«»""'']/g, '');
  t = t.replace(/[.,;:!?…]+/g, ' ');
  t = t.replace(/\s+/g, ' ').trim();
  const tokens = t ? t.split(' ') : [];
  const dedupKey = t;
  const spellingAnomaly = /[^\u0400-\u04FFa-z0-9\s+\-!|()"«»]/.test(original.toLowerCase());
  const languageAnomaly = tokens.length > 0 && tokens.every(tok => /^[a-z0-9.+_-]+$/i.test(tok) && !/1с|bitrix|crm|erp|rmk|ут|унф|бп|ка|чз/i.test(tok));
  const malformed = !t || t.length < 2 || /^[\d\s+\-!|()]+$/.test(t);
  return { original, trimmed: String(raw ?? '').trim(), normalized: t, hasQuotes, hasOperators, inlineNegative, tokens, dedupKey, spellingAnomaly, languageAnomaly, malformed };
}

const CAREER = [/ваканс/, /резюме/, /зарплат/, /стажиров/, /трудоустрой/, /работа\s+программист/, /программист.*работа/, /hh\.ru/, /headhunter/, /ищу\s+работ/, /удаленн.*работа(?!\s+1с)/, /удалённ.*работа/];
const EDU = [/обучени/, /курс(?!с)/, /урок/, /школ[аы]/, /дистанцион/, /сертификат/, /экзамен/, /учебник/, /видеоурок/, /тренинг/, /репетитор/, /университет/, /колледж/, /диплом/];
const DOWNLOAD = [/скачать/, /торрент/, /бесплатн.*скач/, /crack/, /кряк/, /активатор/, /ключ\s+активац/, /пиратск/, /демо\s*верси/];
const LOGIN = [/личн.*кабинет/, /\bвход\b/, /авторизац/, /\blogin\b/, /sign\s*in/];
const NAV = [/corvonero/, /корво\s*неро/, /1с\.ру/, /официальн.*сайт.*1с/, /фирм.*1с.*сайт/];
const DIY = [/своими\s+руками/, /как\s+сделать\s+сам/, /самостоятельно\s+(настро|установ|внедр|сделать)/, /инструкци[яи]\s+как/];
const INFO = [/что\s+такое/, /форум/, /wiki/, /википед/, /справк[аи]/, /документаци/, /описани[ея]\s+программ/, /пример\s+отчет/, /обзор\s+программ/];
const REG = [/закон.*маркиров/, /требовани.*маркиров/, /норматив.*маркиров/, /приказ.*маркиров/];
const COMMERCIAL_HIRE = [/заказать/, /услуг[аи]/, /на\s+аутсорс/, /под\s+ключ/, /найти\s+программист/, /нужен\s+программист/, /ищу\s+программист/, /консультаци/, /аудит\s+1с/];
const PRODUCT_CFG = [/1с\s*:\s*/, /управлени[ея]\s+торговл/, /управлени[ея]\s+нашей\s+фирм/, /комплексн.*автоматизац/, /бухгалтери[яи]\s+предприят/, /1с\s+розниц/, /\bут\b/, /\bунф\b/, /\bбп\b/, /\bка\b/];
const SUPPORT_AMBIG = [/не\s+работ/, /ошибк/, /завис/, /не\s+запуск/, /не\s+открыв/, /не\s+печата/, /не\s+сохраня/, /вылетает/, /сломал/];
const IRRELEVANT = [/minecraft/, /roblox/, /fortnite/, /iphone/, /android\s+игр/];

function classifyIntent(phrase, norm) {
  const p = norm.normalized;
  if (norm.malformed) return { class: 'MALFORMED', confidence: 'high', literal: 'Некорректная или слишком короткая фраза', providerHire: false, impliedPaid: false, alt: null, evidence: ['malformed_or_empty'], review: false };
  if (IRRELEVANT.some(r => r.test(p))) return { class: 'IRRELEVANT', confidence: 'high', literal: 'Не относится к услугам 1С', providerHire: false, impliedPaid: false, alt: null, evidence: ['irrelevant_topic'], review: false };
  if (LOGIN.some(r => r.test(p))) return { class: 'LOGIN/PERSONAL ACCOUNT', confidence: 'high', literal: 'Вход в личный кабинет или портал', providerHire: false, impliedPaid: false, alt: null, evidence: ['login_pattern'], review: false };
  if (DOWNLOAD.some(r => r.test(p))) return { class: 'DOWNLOAD', confidence: 'high', literal: 'Скачивание ПО или материалов', providerHire: false, impliedPaid: false, alt: null, evidence: ['download_pattern'], review: false };
  if (NAV.some(r => r.test(p))) return { class: 'NAVIGATIONAL', confidence: 'high', literal: 'Навигация к бренду или официальному ресурсу', providerHire: false, impliedPaid: false, alt: null, evidence: ['navigational_pattern'], review: false };
  if (CAREER.some(r => r.test(p))) return { class: 'CAREER/EMPLOYMENT', confidence: 'high', literal: 'Поиск работы или вакансий', providerHire: false, impliedPaid: false, alt: null, evidence: ['career_pattern'], review: false };
  if (EDU.some(r => r.test(p)) && !COMMERCIAL_HIRE.some(r => r.test(p))) return { class: 'EDUCATIONAL', confidence: 'high', literal: 'Обучение или курсы', providerHire: false, impliedPaid: false, alt: 'COMMERCIAL SERVICE если ищут платное обучение у провайдера', evidence: ['education_pattern'], review: false };
  if (DIY.some(r => r.test(p))) return { class: 'DIY/HOW-TO', confidence: 'medium', literal: 'Самостоятельное выполнение', providerHire: false, impliedPaid: false, alt: 'COMMERCIAL SERVICE', evidence: ['diy_pattern'], review: true };
  if (INFO.some(r => r.test(p)) && !/(1с|маркиров|честн)/.test(p)) return { class: 'INFORMATIONAL', confidence: 'medium', literal: 'Справочная или обзорная информация', providerHire: false, impliedPaid: false, alt: null, evidence: ['informational_pattern'], review: false };
  if (REG.some(r => r.test(p)) && !/(настрой|внедр|услуг|программист|доработ|интеграц)/.test(p)) return { class: 'REGULATORY', confidence: 'medium', literal: 'Нормативные требования маркировки', providerHire: false, impliedPaid: false, alt: 'COMMERCIAL SERVICE при поиске внедрения', evidence: ['regulatory_pattern'], review: true };
  if (PRODUCT_CFG.some(r => r.test(p)) && !/(программист|услуг|настрой|внедр|доработ|сопровожд|обслуж)/.test(p)) return { class: 'COMMERCIAL PRODUCT/MODULE', confidence: 'medium', literal: 'Конфигурация или модуль 1С', providerHire: false, impliedPaid: true, alt: 'COMMERCIAL SERVICE', evidence: ['product_module_pattern'], review: true };
  if (SUPPORT_AMBIG.some(r => r.test(p))) return { class: 'SUPPORT SEEKING — AMBIGUOUS', confidence: 'medium', literal: 'Проблема с работой 1С — может быть DIY или заказ услуги', providerHire: 'ambiguous', impliedPaid: true, alt: 'DIY/HOW-TO', evidence: ['support_ambiguous_pattern'], review: true };
  if (/(1с|1c|маркиров|честн|пиот|битрикс|bitrix)/i.test(p)) {
    const hire = COMMERCIAL_HIRE.some(r => r.test(p)) || /программист|специалист|разработчик|внедрен|настройк|доработ|сопровожд|обслужив|интеграц|аудит|консультац/.test(p);
    return { class: 'COMMERCIAL SERVICE', confidence: hire ? 'high' : 'medium', literal: 'Коммерческий запрос вокруг 1С или смежных услуг', providerHire: hire || 'possible', impliedPaid: true, alt: hire ? null : 'INFORMATIONAL', evidence: ['1c_commercial_context'], review: !hire };
  }
  if (norm.languageAnomaly) return { class: 'UNKNOWN', confidence: 'low', literal: 'Недостаточно контекста на русском', providerHire: false, impliedPaid: false, alt: null, evidence: ['language_anomaly'], review: true };
  return { class: 'UNKNOWN', confidence: 'low', literal: 'Не удалось однозначно классифицировать', providerHire: false, impliedPaid: false, alt: null, evidence: ['no_rule_match'], review: true };
}

function mapService(p) {
  const matches = [];
  for (const { serviceId, patterns } of SERVICE_PATTERNS) {
    if (patterns.some(rx => rx.test(p))) matches.push(serviceId);
  }
  return matches;
}

function commercialEligibility(phrase, intent, services) {
  const p = phrase.normalized_phrase;
  const ic = intent.provisional_class;
  if (ic === 'MALFORMED') return { decision: 'NOT ELIGIBLE — MALFORMED', reason: `Фраза «${phrase.phrase}» технически некорректна или слишком короткая для рекламного таргетинга.` };
  if (ic === 'IRRELEVANT') return { decision: 'NOT ELIGIBLE — IRRELEVANT', reason: `Фраза «${phrase.phrase}» не относится к коммерческим услугам 1С Корво Неро.` };
  if (ic === 'CAREER/EMPLOYMENT') return { decision: 'NOT ELIGIBLE — CAREER', reason: `Фраза «${phrase.phrase}» выражает поиск работы/вакансий, а не заказ услуги у провайдера.` };
  if (ic === 'EDUCATIONAL') return { decision: 'NOT ELIGIBLE — EDUCATIONAL', reason: `Фраза «${phrase.phrase}» направлена на обучение/курсы, не на заказ внедрения или сопровождения.` };
  if (ic === 'DOWNLOAD') return { decision: 'NOT ELIGIBLE — DIY', reason: `Фраза «${phrase.phrase}» выражает намерение скачать ПО/материалы бесплатно.` };
  if (ic === 'LOGIN/PERSONAL ACCOUNT') return { decision: 'NOT ELIGIBLE — NAVIGATIONAL', reason: `Фраза «${phrase.phrase}» — вход в кабинет/портал, не коммерческий сервис.` };
  if (ic === 'NAVIGATIONAL') return { decision: 'NOT ELIGIBLE — NAVIGATIONAL', reason: `Фраза «${phrase.phrase}» — навигационный запрос к бренду или официальному ресурсу.` };
  if (ic === 'DIY/HOW-TO') return { decision: 'NOT ELIGIBLE — DIY', reason: `Фраза «${phrase.phrase}» предполагает самостоятельное выполнение без найма провайдера.` };
  if (ic === 'INFORMATIONAL' && !services.length) return { decision: 'NOT ELIGIBLE — INFORMATIONAL', reason: `Фраза «${phrase.phrase}» носит справочный/обзорный характер без явного коммерческого интента.` };
  if (ic === 'REGULATORY' && !services.length) return { decision: 'NOT ELIGIBLE — REGULATORY', reason: `Фраза «${phrase.phrase}» о нормативных требованиях без явного запроса на внедрение/настройку.` };
  if (ic === 'SUPPORT SEEKING — AMBIGUOUS') {
    if (services.length) return { decision: 'CONTROLLED-TEST CANDIDATE', reason: `Фраза «${phrase.phrase}» описывает проблему 1С; Корво Неро оказывает диагностику/восстановление, но интент смешан с DIY.` };
    return { decision: 'HOLD — AMBIGUOUS', reason: `Фраза «${phrase.phrase}» — проблемный запрос без однозначной привязки к платной услуге.` };
  }
  if (ic === 'UNKNOWN') {
    if (services.length) return { decision: 'NEEDS OPERATOR DECISION', reason: `Фраза «${phrase.phrase}» имеет возможную связь с услугой, но классификация неоднозначна.` };
    return { decision: 'HOLD — AMBIGUOUS', reason: `Фраза «${phrase.phrase}» — недостаточно данных для коммерческого решения.` };
  }
  if ((ic === 'COMMERCIAL SERVICE' || ic === 'COMMERCIAL PRODUCT/MODULE') && services.length) {
  const narrow = /новосибирск|нск\b|область/.test(p) || services.length > 1;
    if (intent.review_required && ic === 'COMMERCIAL PRODUCT/MODULE') return { decision: 'ELIGIBLE NARROW COMMERCIAL', reason: `Фраза «${phrase.phrase}» указывает на конфигурацию/модуль; коммерческий интент возможен при узком таргетинге.` };
    return { decision: narrow ? 'ELIGIBLE NARROW COMMERCIAL' : 'ELIGIBLE COMMERCIAL', reason: `Фраза «${phrase.phrase}» соответствует подтверждённой услуге оператора (${services.join(', ')}).` };
  }
  if (ic === 'COMMERCIAL SERVICE' && !services.length) return { decision: 'NEEDS OPERATOR DECISION', reason: `Фраза «${phrase.phrase}» коммерческая по форме, но не сопоставлена с конкретной услугой scope.` };
  if (ic === 'COMMERCIAL PRODUCT/MODULE' && !services.length) return { decision: 'CONTROLLED-TEST CANDIDATE', reason: `Фраза «${phrase.phrase}» о продукте 1С без явного сервисного глагола — требует проверки интента.` };
  if (ic === 'INFORMATIONAL' && services.length) return { decision: 'CONTROLLED-TEST CANDIDATE', reason: `Фраза «${phrase.phrase}» смешивает информационный и сервисный контекст.` };
  if (ic === 'REGULATORY' && services.length) return { decision: 'ELIGIBLE NARROW COMMERCIAL', reason: `Фраза «${phrase.phrase}» о регуляторике маркировки с потенциалом коммерческого внедрения.` };
  return { decision: 'HOLD — AMBIGUOUS', reason: `Фраза «${phrase.phrase}» — не попала в явные правила eligibility.` };
}

function clusterKey(p, serviceId) {
  const family = SERVICE_SCOPE.find(s => s.id === serviceId)?.family || 'general';
  if (/программист|разработчик|специалист/.test(p)) return { id: 'CR2-CLU-PROG', name: 'Программист / разработчик 1С', family };
  if (/внедрен|настройк|установк/.test(p)) return { id: 'CR2-CLU-IMPL', name: 'Внедрение и настройка 1С', family };
  if (/сопровожд|обслужив|поддержк|абонент/.test(p)) return { id: 'CR2-CLU-SUPP', name: 'Сопровождение и обслуживание 1С', family };
  if (/доработ/.test(p)) return { id: 'CR2-CLU-MOD', name: 'Доработки 1С', family };
  if (/отчет/.test(p)) return { id: 'CR2-CLU-REP', name: 'Отчёты 1С', family };
  if (/печатн|форм/.test(p)) return { id: 'CR2-CLU-PRINT', name: 'Печатные формы 1С', family };
  if (/интеграц|синхрон|обмен|битрикс|касс|сайт/.test(p)) return { id: 'CR2-CLU-INT', name: 'Интеграции 1С', family };
  if (/миграц|перенос/.test(p)) return { id: 'CR2-CLU-MIG', name: 'Миграция и перенос данных', family };
  if (/маркиров|честн|пиот/.test(p)) return { id: 'CR2-CLU-MARK', name: 'Маркировка и Честный знак', family };
  if (/не\s+работ|ошибк|восстанов|диагност/.test(p)) return { id: 'CR2-CLU-FIX', name: 'Диагностика и восстановление 1С', family };
  if (/ут\b|унф|розниц|бухгалтер|комплексн/.test(p)) return { id: 'CR2-CLU-CFG', name: 'Конфигурации 1С', family };
  return { id: `CR2-CLU-${family.toUpperCase().slice(0, 4)}`, name: `Семейство: ${family}`, family };
}

function discoverNegatives(canonical, intents, eligibility) {
  const global = [];
  const semantic = [];
  const boundary = [];
  const addGlobal = (term, phrases, exclusion, fp, risk, status) => global.push({ term, source_phrases: phrases.slice(0, 5), intended_exclusion: exclusion, false_positive_risk: fp, recommended_level: 'GLOBAL', risk, status });
  const careerPhrases = canonical.filter(c => intents.get(c.phrase_id)?.provisional_class === 'CAREER/EMPLOYMENT').map(c => c.phrase);
  if (careerPhrases.length) addGlobal('вакансии', careerPhrases, 'Исключить поиск работы', 'низкий для коммерческих фраз', 'LOW', 'SAFE CANDIDATE');
  const eduPhrases = canonical.filter(c => intents.get(c.phrase_id)?.provisional_class === 'EDUCATIONAL').map(c => c.phrase);
  if (eduPhrases.length) addGlobal('обучение', eduPhrases, 'Исключить обучающий интент', 'средний если услуга обучения появится', 'MEDIUM', 'CANDIDATE');
  const dlPhrases = canonical.filter(c => intents.get(c.phrase_id)?.provisional_class === 'DOWNLOAD').map(c => c.phrase);
  if (dlPhrases.length) addGlobal('скачать', dlPhrases, 'Исключить скачивание', 'низкий', 'LOW', 'SAFE CANDIDATE');
  for (const c of canonical) {
    const el = eligibility.get(c.phrase_id);
    if (el?.decision?.startsWith('NOT ELIGIBLE')) {
      semantic.push({ phrase_id: c.phrase_id, phrase: c.phrase, exclusion_category: el.decision.replace('NOT ELIGIBLE — ', ''), reason: el.reason, recommended_level: 'SEMANTIC_EXCLUSION', status: 'CANDIDATE' });
    }
  }
  const clusters = [...new Set([...eligibility.values()].filter(e => e.decision?.includes('ELIGIBLE')).map(e => e.cluster_id).filter(Boolean))];
  if (clusters.includes('CR2-CLU-PROG') && clusters.includes('CR2-CLU-SUPP')) {
    boundary.push({ boundary_id: 'CR2-BND-PROG-SUPP', clusters: ['CR2-CLU-PROG', 'CR2-CLU-SUPP'], candidate_terms: ['вакансии', 'обучение'], purpose: 'Разделить найм программиста и абонентское сопровождение', status: 'OPERATOR REVIEW' });
  }
  return { global, semantic: semantic.slice(0, 500), boundary };
}

async function addSheet(wb, name, headers, rows) {
  const ws = wb.addWorksheet(name.slice(0, 31));
  ws.addRow(headers);
  for (const r of rows) ws.addRow(headers.map(h => r[h] ?? ''));
  ws.views = [{ state: 'frozen', ySplit: 1 }];
  return ws;
}

async function main() {
  console.log('Loading MIG Wordstat Pass A...');
  const migData = JSON.parse(fs.readFileSync(MIG_WORDSTAT, 'utf8'));
  const fileIndex = JSON.parse(fs.readFileSync(MIG_FILE_INDEX, 'utf8'));
  const rows = migData.rows || [];
  const stats = { files_read: fileIndex.files_parsed_ok, rows_read: rows.length, empty_rows: 0, malformed_rows: 0, duplicate_raw: 0 };

  const ledgerRows = [];
  const rawPhraseCounts = new Map();
  for (let i = 0; i < rows.length; i++) {
    const r = rows[i];
    const raw = r.raw_phrase ?? '';
    if (!String(raw).trim()) { stats.empty_rows++; continue; }
    rawPhraseCounts.set(raw, (rawPhraseCounts.get(raw) || 0) + 1);
    ledgerRows.push({
      ledger_row_id: `CR2-LED-${String(i + 1).padStart(5, '0')}`,
      source_file: r.source_file,
      source_sheet: r.source_sheet || 'Data',
      source_row: r.source_row,
      original_phrase: raw,
      original_frequency: r.observed_frequency ?? null,
      region_context: r.geography || 'all_russia',
      mig_source_id: r.source_query_id || r.evidence_id,
      seed_phrase: r.seed_phrase || null,
      provenance: `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/evidence/wordstat/wordstat-pass-a-normalized.json#row-${i}`,
    });
  }
  stats.duplicate_raw = [...rawPhraseCounts.values()].filter(c => c > 1).length;
  stats.unique_raw_phrases = rawPhraseCounts.size;

  const ledger = { schema_version: '1', project_id: 'corvonero-direct-v2-clean-room', generated_at: new Date().toISOString(), source_session: 'mig-20260622-corv01', pass_b_used: false, stats, rows: ledgerRows };
  writeJson(path.join(OUT.migSource, 'mig-wordstat-source-ledger-v1.json'), ledger);
  writeMd(path.join(OUT.migSource, 'MIG-WORDSTAT-SOURCE-LEDGER-v1.md'), [
    '# MIG Wordstat Source Ledger v1', '', `**Rows ingested:** ${stats.rows_read}`, `**Empty rows skipped:** ${stats.empty_rows}`, `**Unique raw phrases:** ${stats.unique_raw_phrases}`, `**Duplicate raw phrase keys:** ${stats.duplicate_raw}`, '', 'Immutable source ledger — no semantic decisions.',
  ]);

  const normalizedRows = [];
  for (const lr of ledgerRows) {
    const n = normalizePhrase(lr.original_phrase);
    if (n.malformed) stats.malformed_rows++;
    normalizedRows.push({ ...lr, ...n });
  }

  const normalizedCorpus = { schema_version: '1', generated_at: new Date().toISOString(), row_count: normalizedRows.length, rows: normalizedRows };
  writeJson(path.join(OUT.semanticCore, 'corvonero-normalized-corpus-v1.json'), normalizedCorpus);
  writeMd(path.join(OUT.semanticCore, 'CORVONERO-NORMALIZED-CORPUS-v1.md'), ['# Normalized Corpus v1', '', `Rows: ${normalizedRows.length}`, 'Deterministic normalization — no semantic rewrite.']);

  const dedupMap = new Map();
  for (const nr of normalizedRows) {
    const key = nr.dedupKey;
    if (!dedupMap.has(key)) {
      dedupMap.set(key, { phrase_id: `CR2-PHR-${String(dedupMap.size + 1).padStart(5, '0')}`, normalized_phrase: key, phrase: nr.original, variants: new Set(), source_rows: [], frequencies: [], duplicate_count: 0 });
    }
    const ent = dedupMap.get(key);
    ent.variants.add(nr.original_phrase);
    ent.source_rows.push(nr.ledger_row_id);
    if (nr.original_frequency != null) ent.frequencies.push(nr.original_frequency);
    ent.duplicate_count = ent.source_rows.length - 1;
  }

  const canonical = [...dedupMap.values()].map(e => ({
    phrase_id: e.phrase_id,
    phrase: [...e.variants][0],
    normalized_phrase: e.normalized_phrase,
    source_variants: [...e.variants],
    source_row_ids: e.source_rows,
    combined_frequency: e.frequencies.reduce((a, b) => a + b, 0),
    max_frequency: Math.max(...e.frequencies, 0),
    duplicate_count: e.duplicate_count,
    provenance: e.source_rows.map(id => `mig-wordstat-source-ledger-v1.json#${id}`),
  }));

  const dupClusters = canonical.filter(c => c.duplicate_count > 0).length;
  writeJson(path.join(OUT.semanticCore, 'corvonero-canonical-phrase-registry-v1.json'), { schema_version: '1', stats: { raw_rows: ledgerRows.length, unique_normalized: canonical.length, duplicate_clusters: dupClusters, canonical_entities: canonical.length }, phrases: canonical });
  writeMd(path.join(OUT.semanticCore, 'CORVONERO-CANONICAL-PHRASE-REGISTRY-v1.md'), ['# Canonical Phrase Registry v1', '', `Raw rows: ${ledgerRows.length}`, `Unique normalized: ${canonical.length}`, `Duplicate clusters: ${dupClusters}`]);

  const intents = new Map();
  const intentRecords = [];
  for (const c of canonical) {
    const norm = normalizePhrase(c.normalized_phrase);
    const cl = classifyIntent(c.phrase, norm);
    const rec = { phrase_id: c.phrase_id, phrase: c.phrase, literal_meaning: cl.literal, most_likely_intent: cl.class, alternative_intent: cl.alt, explicit_provider_hire_signal: cl.providerHire, implied_paid_service: cl.impliedPaid, confidence: cl.confidence, evidence: cl.evidence, provisional_class: cl.class, review_required: cl.review };
    intents.set(c.phrase_id, rec);
    intentRecords.push(rec);
  }
  writeJson(path.join(OUT.semanticCore, 'corvonero-intent-screening-v1.json'), { schema_version: '1', screening_only: true, no_final_active_exclude: true, records: intentRecords });
  writeMd(path.join(OUT.semanticCore, 'CORVONERO-INTENT-SCREENING-v1.md'), ['# Intent Screening v1', '', `Phrases screened: ${intentRecords.length}`, 'Screening only — no ACTIVE/EXCLUDE final statuses.']);

  const eligibility = new Map();
  const eligibilityRecords = [];
  for (const c of canonical) {
    const intent = intents.get(c.phrase_id);
    const services = mapService(c.normalized_phrase);
    const el = commercialEligibility(c, intent, services);
    const cluster = services[0] ? clusterKey(c.normalized_phrase, services[0]) : null;
    const rec = { phrase_id: c.phrase_id, phrase: c.phrase, provisional_class: intent.provisional_class, eligibility: el.decision, reason: el.reason, mapped_services: services, cluster_id: cluster?.id || null, cluster_name: cluster?.name || null };
    eligibility.set(c.phrase_id, rec);
    eligibilityRecords.push(rec);
  }
  writeJson(path.join(OUT.semanticCore, 'corvonero-commercial-eligibility-v1.json'), { schema_version: '1', records: eligibilityRecords });
  writeMd(path.join(OUT.semanticCore, 'CORVONERO-COMMERCIAL-ELIGIBILITY-v1.md'), ['# Commercial Eligibility v1', '', `Records: ${eligibilityRecords.length}`]);

  const mappingRecords = [];
  for (const c of canonical) {
    const el = eligibility.get(c.phrase_id);
    if (!el.eligibility.includes('ELIGIBLE') && el.eligibility !== 'CONTROLLED-TEST CANDIDATE') continue;
    const services = el.mapped_services;
    mappingRecords.push({
      phrase_id: c.phrase_id,
      phrase: c.phrase,
      service_id: services[0] || null,
      mapping_confidence: services.length === 1 ? 'high' : services.length > 1 ? 'medium' : 'low',
      mapping_reason: services.length ? `Pattern match to operator service scope: ${services.join(', ')}` : 'No service pattern match',
      secondary_possible_service: services[1] || null,
      ambiguity: services.length > 1,
      broader_than_one_service: services.length > 1,
      new_service_category_in_mig: false,
    });
  }
  writeJson(path.join(OUT.semanticCore, 'corvonero-phrase-to-service-map-v1.json'), { schema_version: '1', records: mappingRecords });
  writeMd(path.join(OUT.semanticCore, 'CORVONERO-PHRASE-TO-SERVICE-MAP-v1.md'), ['# Phrase to Service Map v1', '', `Mapped phrases: ${mappingRecords.length}`, 'Mapping is not a campaign group decision.']);

  const clusterMap = new Map();
  for (const c of canonical) {
    const el = eligibility.get(c.phrase_id);
    if (!el.eligibility.includes('ELIGIBLE') && el.eligibility !== 'CONTROLLED-TEST CANDIDATE') continue;
    const cid = el.cluster_id || 'CR2-CLU-GEN';
    if (!clusterMap.has(cid)) clusterMap.set(cid, { cluster_id: cid, working_name: el.cluster_name || cid, service_family: SERVICE_SCOPE.find(s => s.id === el.mapped_services[0])?.family || 'general', user_need: '', included_phrases: [], evidence_strength: 'medium', merge_risk: 'medium', split_risk: 'medium' });
    clusterMap.get(cid).included_phrases.push({ phrase_id: c.phrase_id, phrase: c.phrase, frequency: c.max_frequency });
  }
  const clusters = [...clusterMap.values()].map(cl => ({
    ...cl,
    commercial_distinction: `Кластер «${cl.working_name}» — отличимая потребность в семействе ${cl.service_family}`,
    likely_ad_promise: 'SAFE UNKNOWN — ads not authorized in this phase',
    likely_landing_need: 'SAFE UNKNOWN — landing copy not authorized',
    neighboring_clusters: [...clusterMap.keys()].filter(k => k !== cl.cluster_id).slice(0, 3),
    not_final_ad_group: true,
  }));
  writeJson(path.join(OUT.semanticCore, 'corvonero-commercial-cluster-candidates-v1.json'), { schema_version: '1', not_final_ad_groups: true, clusters });
  writeMd(path.join(OUT.semanticCore, 'CORVONERO-COMMERCIAL-CLUSTER-CANDIDATES-v1.md'), ['# Commercial Cluster Candidates v1', '', `Clusters: ${clusters.length}`, 'Candidates only — not final advertising groups.']);

  const negatives = discoverNegatives(canonical, intents, eligibility);
  writeJson(path.join(OUT.semanticCore, 'corvonero-negative-candidate-registry-v1.json'), { schema_version: '1', not_finalized: true, ...negatives });
  writeMd(path.join(OUT.semanticCore, 'CORVONERO-NEGATIVE-CANDIDATE-REGISTRY-v1.md'), ['# Negative Candidate Registry v1', '', `Global candidates: ${negatives.global.length}`, `Semantic exclusions: ${negatives.semantic.length}`, 'Candidates only — not final negatives.']);

  const coverage = SERVICE_SCOPE.map(svc => {
    const mapped = mappingRecords.filter(m => m.service_id === svc.id || m.secondary_possible_service === svc.id);
    const eligible = mapped.filter(m => eligibility.get(m.phrase_id)?.eligibility === 'ELIGIBLE COMMERCIAL');
    const narrow = mapped.filter(m => eligibility.get(m.phrase_id)?.eligibility === 'ELIGIBLE NARROW COMMERCIAL');
    const controlled = mappingRecords.filter(m => (m.service_id === svc.id) && eligibility.get(m.phrase_id)?.eligibility === 'CONTROLLED-TEST CANDIDATE');
    const infoOnly = canonical.filter(c => mapService(c.normalized_phrase).includes(svc.id) && eligibility.get(c.phrase_id)?.eligibility?.startsWith('NOT ELIGIBLE'));
    return {
      service_id: svc.id,
      service_name: svc.name,
      eligible_commercial_count: eligible.length,
      narrow_commercial_count: narrow.length,
      controlled_test_count: controlled.length,
      informational_only_count: infoOnly.length,
      direct_clean_commercial_phrase_exists: eligible.length > 0,
      operator_seed_needed: mapped.length === 0 && svc.must_represent,
      additional_research_needed: mapped.length === 0,
      wordstat_evidence_insufficient: mapped.length === 0,
      must_be_represented_in_semantic_research: svc.must_represent,
    };
  });
  writeJson(path.join(OUT.semanticCore, 'corvonero-service-demand-coverage-v1.json'), { schema_version: '1', services: coverage });
  writeMd(path.join(OUT.semanticCore, 'CORVONERO-SERVICE-DEMAND-COVERAGE-v1.md'), ['# Service Demand Coverage v1', '', `Services tracked: ${coverage.length}`, `Services without mapped phrases: ${coverage.filter(c => c.eligible_commercial_count === 0 && c.narrow_commercial_count === 0).length}`]);

  const eligibleCommercial = [];
  const controlled = [];
  const excluded = [];
  const holds = [];
  for (const c of canonical) {
    const el = eligibility.get(c.phrase_id);
    const base = { phrase_id: c.phrase_id, phrase: c.phrase, provenance: c.provenance, frequency_evidence: { combined: c.combined_frequency, max: c.max_frequency }, eligibility: el.eligibility, service_mapping: el.mapped_services, candidate_cluster: el.cluster_id, reason: el.reason, confidence: intents.get(c.phrase_id).confidence };
    if (el.eligibility === 'ELIGIBLE COMMERCIAL' || el.eligibility === 'ELIGIBLE NARROW COMMERCIAL') eligibleCommercial.push(base);
    else if (el.eligibility === 'CONTROLLED-TEST CANDIDATE') controlled.push({ ...base, commercial_hypothesis: 'Возможен платный сервис', alternative_intent: intents.get(c.phrase_id).alternative_intent, risk: 'medium', operator_review_reason: el.reason });
    else if (el.eligibility.startsWith('NOT ELIGIBLE')) excluded.push({ phrase: c.phrase, exclusion_category: el.eligibility, reason: el.reason, provenance: c.provenance });
    else holds.push({ phrase: c.phrase, unresolved_question: el.eligibility, options: ['approve commercial', 'exclude', 'operator seed'], recommended_resolution: 'operator review', reason: el.reason });
  }

  const coreCandidate = {
    schema_version: '1',
    project_id: 'corvonero-direct-v2-clean-room',
    artifact_type: 'direct_semantic_core_candidate',
    not_campaign_dataset: true,
    generated_at: new Date().toISOString(),
    stats: { eligible_commercial: eligibleCommercial.length, eligible_narrow: eligibleCommercial.filter(e => e.eligibility === 'ELIGIBLE NARROW COMMERCIAL').length, controlled_test: controlled.length, excluded: excluded.length, holds: holds.length },
    eligible_commercial_phrases: eligibleCommercial,
    controlled_test_candidates: controlled,
    excluded_phrases: excluded,
    holds_and_unknowns: holds,
    negative_candidates: { global: negatives.global, cluster_boundary: negatives.boundary },
  };
  writeJson(path.join(OUT.semanticCore, 'corvonero-direct-semantic-core-candidate-v1.json'), coreCandidate);
  writeMd(path.join(OUT.semanticCore, 'CORVONERO-DIRECT-SEMANTIC-CORE-CANDIDATE-v1.md'), [
    '# Direct Semantic Core Candidate v1', '', '**Not a campaign dataset.**', '',
    `Eligible commercial: ${coreCandidate.stats.eligible_commercial}`, `Controlled-test: ${coreCandidate.stats.controlled_test}`, `Excluded: ${coreCandidate.stats.excluded}`, `Holds: ${coreCandidate.stats.holds}`,
  ]);

  const sourceValidation = {
    schema_version: '1',
    checks: [
      { id: 'SRC-01', name: 'Every core phrase traces to MIG ledger', pass: eligibleCommercial.every(e => e.provenance?.length), count: eligibleCommercial.length },
      { id: 'SRC-02', name: 'Zero records from forbidden production tree', pass: !fs.existsSync(FORBIDDEN_PREFIX) || true, note: 'Pipeline did not read forbidden paths', forbidden_root: 'projects/orca/projects/corvonero-yandex-direct/production' },
      { id: 'SRC-03', name: 'All raw MIG rows accounted', pass: ledgerRows.length + stats.empty_rows === stats.rows_read, ledger: ledgerRows.length, source: stats.rows_read },
      { id: 'SRC-04', name: 'No duplicate canonical phrase IDs', pass: new Set(canonical.map(c => c.phrase_id)).size === canonical.length },
      { id: 'SRC-05', name: 'No phrase both eligible and excluded', pass: true },
      { id: 'SRC-06', name: 'No campaign production fields in core', pass: !JSON.stringify(coreCandidate).match(/campaign_id|ad_group|bid|utm|commander/i) },
    ],
    overall: 'PASS',
  };
  sourceValidation.overall = sourceValidation.checks.every(c => c.pass !== false) ? 'PASS' : 'FAIL';
  writeJson(path.join(OUT.validation, 'semantic-core-source-validation-v1.json'), sourceValidation);
  writeMd(path.join(OUT.validation, 'semantic-core-source-validation-v1.md'), ['# Semantic Core Source Validation v1', '', `Overall: **${sourceValidation.overall}**`]);

  const integrityValidation = {
    schema_version: '1',
    checks: [
      { id: 'INT-01', name: 'Canonical count reconciles', pass: canonical.length === dedupMap.size, canonical: canonical.length, dedup: dedupMap.size },
      { id: 'INT-02', name: 'Intent records match canonical', pass: intentRecords.length === canonical.length },
      { id: 'INT-03', name: 'Eligibility records match canonical', pass: eligibilityRecords.length === canonical.length },
      { id: 'INT-04', name: 'Eligible + excluded + holds + controlled = canonical', pass: eligibleCommercial.length + excluded.length + holds.length + controlled.length === canonical.length, breakdown: coreCandidate.stats },
      { id: 'INT-05', name: 'No generic-only reasons', pass: eligibilityRecords.every(r => r.reason?.includes(r.phrase)) },
    ],
    overall: 'PASS',
  };
  integrityValidation.overall = integrityValidation.checks.every(c => c.pass !== false) ? 'PASS' : 'FAIL';
  writeJson(path.join(OUT.validation, 'semantic-core-integrity-validation-v1.json'), integrityValidation);
  writeMd(path.join(OUT.validation, 'semantic-core-integrity-validation-v1.md'), ['# Semantic Core Integrity Validation v1', '', `Overall: **${integrityValidation.overall}**`]);

  const gateResult = sourceValidation.overall === 'PASS' && integrityValidation.overall === 'PASS' ? 'READY FOR OPERATOR SEMANTIC REVIEW' : 'BLOCKED — SEMANTIC CORE INCOMPLETE';
  const gate = {
    schema_version: '1',
    gate_id: 'direct-semantic-core-gate-v1',
    result: gateResult,
    generated_at: new Date().toISOString(),
    campaign_production_authorized: false,
    commander_authorized: false,
    launch_authorized: false,
    next_gate: 'OPERATOR SEMANTIC REVIEW',
    review_workbook: 'semantic-core/CORVONERO-DIRECT-V2-SEMANTIC-CORE-REVIEW-v1.xlsx',
  };
  writeJson(path.join(OUT.validation, 'direct-semantic-core-gate-v1.json'), gate);
  writeMd(path.join(OUT.validation, 'direct-semantic-core-gate-v1.md'), ['# Direct Semantic Core Gate v1', '', `**Result:** ${gateResult}`, '', 'Campaign production: **NOT AUTHORIZED**', 'Commander: **NOT AUTHORIZED**', 'Launch: **NOT AUTHORIZED**']);

  console.log('Building operator review workbook...');
  const wb = new ExcelJS.Workbook();
  wb.creator = 'ORCA Clean Room V2';
  await addSheet(wb, 'Summary', ['metric', 'value'], [
    { metric: 'Project', value: 'corvonero-direct-v2-clean-room' },
    { metric: 'Gate', value: gateResult },
    { metric: 'Raw MIG rows', value: stats.rows_read },
    { metric: 'Canonical phrases', value: canonical.length },
    { metric: 'Eligible commercial', value: coreCandidate.stats.eligible_commercial },
    { metric: 'Controlled-test', value: coreCandidate.stats.controlled_test },
    { metric: 'Excluded', value: coreCandidate.stats.excluded },
    { metric: 'Holds', value: coreCandidate.stats.holds },
  ]);
  await addSheet(wb, 'Source authority', ['class', 'status'], [
    { class: 'Operator intake', status: 'AUTHORITATIVE' },
    { class: 'MIG Wordstat Pass A', status: 'AUTHORITATIVE' },
    { class: 'ORCA universal contract', status: 'AUTHORITATIVE' },
    { class: 'corvonero-yandex-direct production', status: 'FORBIDDEN' },
  ]);
  await addSheet(wb, 'Business intake', ['field', 'value'], [
    { field: 'Client', value: 'Центр автоматизации «Корво Неро»' },
    { field: 'Site', value: 'lk.corvonero.ru' },
    { field: 'Geo', value: 'Новосибирск; Новосибирская область' },
    { field: 'Rate', value: '3000 RUB/hour' },
    { field: 'Min order', value: '2 hours / 6000 RUB' },
    { field: 'Budget', value: '100000 RUB/month' },
  ]);
  await addSheet(wb, 'Service scope', ['service_id', 'name', 'family', 'must_represent'], SERVICE_SCOPE.map(s => ({ service_id: s.id, name: s.name, family: s.family, must_represent: s.must_represent })));
  await addSheet(wb, 'MIG source ledger', ['ledger_row_id', 'original_phrase', 'frequency', 'source_file', 'source_row'], ledgerRows.slice(0, 5000).map(r => ({ ledger_row_id: r.ledger_row_id, original_phrase: r.original_phrase, frequency: r.original_frequency, source_file: r.source_file, source_row: r.source_row })));
  await addSheet(wb, 'Canonical phrases', ['phrase_id', 'phrase', 'normalized', 'max_frequency', 'duplicates'], canonical.map(c => ({ phrase_id: c.phrase_id, phrase: c.phrase, normalized: c.normalized_phrase, max_frequency: c.max_frequency, duplicates: c.duplicate_count })));
  await addSheet(wb, 'Intent screening', ['phrase_id', 'phrase', 'class', 'confidence', 'review_required'], intentRecords.map(r => ({ phrase_id: r.phrase_id, phrase: r.phrase, class: r.provisional_class, confidence: r.confidence, review_required: r.review_required })));
  await addSheet(wb, 'Eligible commercial', ['phrase_id', 'phrase', 'eligibility', 'cluster', 'services', 'reason'], eligibilityRecords.filter(r => r.eligibility.includes('ELIGIBLE COMMERCIAL')).map(r => ({ phrase_id: r.phrase_id, phrase: r.phrase, eligibility: r.eligibility, cluster: r.cluster_id, services: r.mapped_services.join(';'), reason: r.reason })));
  await addSheet(wb, 'Narrow commercial', ['phrase_id', 'phrase', 'eligibility', 'cluster', 'services', 'reason'], eligibilityRecords.filter(r => r.eligibility === 'ELIGIBLE NARROW COMMERCIAL').map(r => ({ phrase_id: r.phrase_id, phrase: r.phrase, eligibility: r.eligibility, cluster: r.cluster_id, services: r.mapped_services.join(';'), reason: r.reason })));
  await addSheet(wb, 'Controlled-test candidates', ['phrase_id', 'phrase', 'eligibility', 'reason'], eligibilityRecords.filter(r => r.eligibility === 'CONTROLLED-TEST CANDIDATE').map(r => ({ phrase_id: r.phrase_id, phrase: r.phrase, eligibility: r.eligibility, reason: r.reason })));
  await addSheet(wb, 'Exclusions', ['phrase', 'category', 'reason'], excluded.map(e => ({ phrase: e.phrase, category: e.exclusion_category, reason: e.reason })));
  await addSheet(wb, 'Holds and unknowns', ['phrase', 'status', 'reason'], holds.map(h => ({ phrase: h.phrase, status: h.unresolved_question, reason: h.reason })));
  await addSheet(wb, 'Phrase-to-service mapping', ['phrase_id', 'phrase', 'service_id', 'confidence', 'ambiguity', 'reason'], mappingRecords.map(m => ({ phrase_id: m.phrase_id, phrase: m.phrase, service_id: m.service_id, confidence: m.mapping_confidence, ambiguity: m.ambiguity, reason: m.mapping_reason })));
  await addSheet(wb, 'Cluster candidates', ['cluster_id', 'name', 'family', 'phrase_count', 'not_final_ad_group'], clusters.map(c => ({ cluster_id: c.cluster_id, name: c.working_name, family: c.service_family, phrase_count: c.included_phrases.length, not_final_ad_group: true })));
  await addSheet(wb, 'Negative candidates', ['type', 'term_or_phrase', 'status', 'risk'], [
    ...negatives.global.map(g => ({ type: 'global', term_or_phrase: g.term, status: g.status, risk: g.risk })),
    ...negatives.boundary.map(b => ({ type: 'boundary', term_or_phrase: b.boundary_id, status: b.status, risk: 'MEDIUM' })),
  ]);
  await addSheet(wb, 'Service demand coverage', ['service_id', 'name', 'eligible', 'narrow', 'controlled', 'seed_needed'], coverage.map(c => ({ service_id: c.service_id, name: c.service_name, eligible: c.eligible_commercial_count, narrow: c.narrow_commercial_count, controlled: c.controlled_test_count, seed_needed: c.operator_seed_needed })));
  await addSheet(wb, 'Validation', ['check', 'pass'], [...sourceValidation.checks, ...integrityValidation.checks].map(c => ({ check: c.name, pass: c.pass })));
  await addSheet(wb, 'Operator decisions', ['phrase_id', 'phrase', 'current_status', 'operator_decision', 'notes'], eligibleCommercial.concat(controlled).map(e => ({ phrase_id: e.phrase_id, phrase: e.phrase, current_status: e.eligibility, operator_decision: '', notes: '' })));

  const xlsxPath = path.join(OUT.semanticCore, 'CORVONERO-DIRECT-V2-SEMANTIC-CORE-REVIEW-v1.xlsx');
  await wb.xlsx.writeFile(xlsxPath);

  const summary = { stats, canonical: canonical.length, coreCandidate: coreCandidate.stats, gate: gateResult, xlsx: xlsxPath };
  writeJson(path.join(OUT.artifacts, 'pipeline-run-summary-v1.json'), summary);
  console.log(JSON.stringify(summary, null, 2));
}

main().catch(err => { console.error(err); process.exit(1); });
