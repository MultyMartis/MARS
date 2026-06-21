#!/usr/bin/env node
/**
 * Generate Corvonero MIG Demand Surface artifacts (session mig-20260622-corv01).
 * Wordstat: records acquisition_blocked — no invented frequencies.
 */
import { writeFileSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const SESSION = join(__dirname, '..');
const CAPTURE_DATE = '2026-06-22';
const CAPTURE_ISO = '2026-06-22T16:00:00.000Z';

const WORDSTAT_MATRIX = [
  { query_id: 'ws-p1-001', phrase: 'программист 1С', cluster: 'A_broad_commercial', priority: 1, match_mode: 'exact', operator_syntax: '"программист 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: true },
  { query_id: 'ws-p1-002', phrase: 'программист 1С Новосибирск', cluster: 'A_broad_commercial', priority: 1, match_mode: 'exact', operator_syntax: '"программист 1С Новосибирск"', geography: 'Новосибирск + Новосибирская область', broad_compare: false },
  { query_id: 'ws-p1-003', phrase: 'сопровождение 1С', cluster: 'A_support', priority: 1, match_mode: 'exact', operator_syntax: '"сопровождение 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: true },
  { query_id: 'ws-p1-004', phrase: 'доработка 1С', cluster: 'A_modification', priority: 1, match_mode: 'exact', operator_syntax: '"доработка 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: true },
  { query_id: 'ws-p1-005', phrase: 'интеграция 1С с сайтом', cluster: 'C_integrations', priority: 1, match_mode: 'exact', operator_syntax: '"интеграция 1С с сайтом"', geography: 'Новосибирск + Новосибирская область', broad_compare: true },
  { query_id: 'ws-p1-006', phrase: 'интеграция 1С Битрикс', cluster: 'C_integrations', priority: 1, match_mode: 'exact', operator_syntax: '"интеграция 1С Битрикс"', geography: 'Новосибирск + Новосибирская область', broad_compare: true },
  { query_id: 'ws-p1-007', phrase: 'маркировка в 1С', cluster: 'D_labeling', priority: 1, match_mode: 'exact', operator_syntax: '"маркировка в 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: true },
  { query_id: 'ws-p1-008', phrase: 'Честный знак 1С', cluster: 'D_labeling', priority: 1, match_mode: 'exact', operator_syntax: '"Честный знак 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: true },
  { query_id: 'ws-p2-001', phrase: 'доработка отчёта 1С', cluster: 'B_reports', priority: 2, match_mode: 'exact', operator_syntax: '"доработка отчёта 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: true },
  { query_id: 'ws-p2-002', phrase: 'доработка печатной формы 1С', cluster: 'B_forms', priority: 2, match_mode: 'exact', operator_syntax: '"доработка печатной формы 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: true },
  { query_id: 'ws-p2-003', phrase: 'доработка РМК 1С', cluster: 'B_rmk', priority: 2, match_mode: 'exact', operator_syntax: '"доработка РМК 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: true },
  { query_id: 'ws-p2-004', phrase: 'настройка синхронизации 1С', cluster: 'C_integrations', priority: 2, match_mode: 'exact', operator_syntax: '"настройка синхронизации 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: true },
  { query_id: 'ws-p2-005', phrase: 'обновление доработанной 1С', cluster: 'A_support', priority: 2, match_mode: 'exact', operator_syntax: '"обновление доработанной 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: true },
  { query_id: 'ws-p2-006', phrase: 'срочно программист 1С', cluster: 'A_urgent', priority: 2, match_mode: 'exact', operator_syntax: '"срочно программист 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: true },
  { query_id: 'ws-p2-007', phrase: '1С не работает', cluster: 'A_urgent', priority: 2, match_mode: 'exact', operator_syntax: '"1С не работает"', geography: 'Новосибирск + Новосибирская область', broad_compare: true },
  { query_id: 'ws-p3-001', phrase: 'маркировка пива 1С', cluster: 'E_product_labeling', priority: 3, match_mode: 'exact', operator_syntax: '"маркировка пива 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: false },
  { query_id: 'ws-p3-002', phrase: 'маркировка воды 1С', cluster: 'E_product_labeling', priority: 3, match_mode: 'exact', operator_syntax: '"маркировка воды 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: false },
  { query_id: 'ws-p3-003', phrase: 'маркировка лекарств 1С', cluster: 'E_product_labeling', priority: 3, match_mode: 'exact', operator_syntax: '"маркировка лекарств 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: false },
  { query_id: 'ws-p3-004', phrase: 'ТС ПИОТ 1С', cluster: 'D_ts_piot', priority: 3, match_mode: 'exact', operator_syntax: '"ТС ПИОТ 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: true },
  { query_id: 'ws-p3-005', phrase: 'маркировка автозапчастей 1С', cluster: 'E_product_labeling', priority: 3, match_mode: 'exact', operator_syntax: '"маркировка автозапчастей 1С"', geography: 'Новосибирск + Новосибирская область', broad_compare: false },
];

const TASK_P1_EXTRA = { query_id: 'ws-task-p1-extra', phrase: 'услуги программиста 1С', cluster: 'A_broad_commercial', priority: 1, match_mode: 'exact', operator_syntax: '"услуги программиста 1С"', geography: 'Нovosibirsk + Новосибирская область', broad_compare: true, note: 'Task P1 list item — not separate matrix row; collected per operator task scope' };

const R1_QUERIES = [
  { r1_id: 'r1q01', query: 'программист 1С Новосибирск', lq_ref: 'lq01' },
  { r1_id: 'r1q02', query: 'сопровождение 1С Новосибирск', lq_ref: 'lq04' },
  { r1_id: 'r1q03', query: 'доработка 1С Новосибирск', lq_ref: 'lq03' },
  { r1_id: 'r1q04', query: 'доработка отчёта 1С Новосибирск', lq_ref: 'lq09' },
  { r1_id: 'r1q05', query: 'интеграция 1С с сайтом Новосибирск', lq_ref: 'lq13' },
  { r1_id: 'r1q06', query: 'интеграция 1С Битрикс Новосибирск', lq_ref: 'lq14' },
  { r1_id: 'r1q07', query: 'маркировка в 1С Новосибирск', lq_ref: 'lq17' },
  { r1_id: 'r1q08', query: 'Честный знак 1С Новосибирск', lq_ref: 'lq19' },
  { r1_id: 'r1q09', query: 'настройка ТС ПИОТ', lq_ref: 'lq21' },
  { r1_id: 'r1q10', query: 'программа 1С не работает Новосибирск', lq_ref: 'lq06' },
];

const SERP_MAP = {
  'ws-p1-001': 'lq01', 'ws-p1-002': 'lq01', 'ws-p1-003': 'lq04', 'ws-p1-004': 'lq03',
  'ws-p1-005': 'lq13', 'ws-p1-006': 'lq14', 'ws-p1-007': 'lq17', 'ws-p1-008': 'lq19',
  'ws-p2-001': 'lq09', 'ws-p2-002': 'lq10', 'ws-p2-003': 'lq12', 'ws-p2-004': 'lq15',
  'ws-p2-005': null, 'ws-p2-006': 'lq05', 'ws-p2-007': 'lq06',
  'ws-p3-001': 'lq23', 'ws-p3-002': 'lq24', 'ws-p3-003': 'lq25', 'ws-p3-004': 'lq21', 'ws-p3-005': 'lq26',
  'ws-task-p1-extra': 'lq02',
};

const INTENT_MAP = {
  A_broad_commercial: { intent: 'direct-commercial', commercial: 'high', noise: ['job-seeking'] },
  A_support: { intent: 'commercial-mixed', commercial: 'moderate', noise: ['informational', 'educational'] },
  A_modification: { intent: 'direct-commercial', commercial: 'high', noise: ['informational'] },
  A_urgent: { intent: 'troubleshooting', commercial: 'mixed', noise: ['job-seeking', 'informational', 'vacancy'] },
  B_reports: { intent: 'direct-commercial', commercial: 'high', noise: ['informational'] },
  B_forms: { intent: 'direct-commercial', commercial: 'high', noise: ['informational'] },
  B_rmk: { intent: 'direct-commercial', commercial: 'moderate', noise: ['informational'] },
  C_integrations: { intent: 'direct-commercial', commercial: 'high', noise: ['informational', 'software-download'] },
  D_labeling: { intent: 'commercial-mixed', commercial: 'moderate', noise: ['informational', 'regulatory', 'software-download'] },
  D_ts_piot: { intent: 'regulatory', commercial: 'low', noise: ['informational', 'regulatory'] },
  E_product_labeling: { intent: 'commercial-mixed', commercial: 'moderate', noise: ['informational', 'regulatory'] },
};

function writeJson(path, obj) {
  writeFileSync(path, JSON.stringify(obj, null, 2) + '\n', 'utf8');
}

// Wordstat snapshot
const wsRows = WORDSTAT_MATRIX.map((q, i) => ({
  row_id: `WS-${String(i + 1).padStart(2, '0')}`,
  query_id: q.query_id,
  phrase: q.phrase,
  region: 'Новосибирск + Новосибирская область',
  frequency: null,
  frequency_status: 'not_captured',
  match_mode: q.match_mode,
  operator_syntax: q.operator_syntax,
  collection_date: CAPTURE_DATE,
  evidence_grade: 'X_not_collected',
  screenshot_ref: null,
  acquisition_failure: 'af-006',
  safe_unknown: ['Wordstat UI requires authenticated human operator session — agent environment cannot complete manual export'],
}));

writeJson(join(SESSION, 'wordstat_snapshot.cap-20260622-corv01.json'), {
  schema_stub_version: 'keyword-snapshot-stub-v1',
  session_id: 'mig-20260622-corv01',
  capture_id: 'cap-20260622-corv01',
  snapshot_type: 'wordstat',
  import_method: 'manual_export_attempted',
  provider_label: 'yandex_wordstat',
  region_label: 'Новосибирск + Новосибирская область',
  period: 'unknown',
  exported_at: CAPTURE_DATE,
  captured_at: CAPTURE_ISO,
  operator_id: 'cursor-agent-supervised',
  source_file_ref: 'wordstat-export-manual-20260622-corv01.md',
  status: 'acquisition_blocked',
  column_mapping: { Query: 'phrase', Frequency: 'frequency' },
  session_safe_unknown: [
    'No Wordstat frequencies captured — af-006 Wordstat UI not accessible from agent environment',
    'Broad vs exact comparison not executed — requires Wordstat UI operator pass',
    'Nationwide reference values not collected — regional primary evidence only when collected',
  ],
  evidence_grade: 'X_not_collected',
  rows: wsRows,
});

// Normalized collection
const normalized = WORDSTAT_MATRIX.map((q) => ({
  query_id: q.query_id,
  exact_phrase: q.phrase,
  operator_syntax: q.operator_syntax,
  match_mode: q.match_mode,
  region: q.geography,
  collection_date: CAPTURE_DATE,
  primary_frequency: null,
  primary_frequency_status: 'not_captured',
  broad_frequency: null,
  broad_frequency_status: q.broad_compare ? 'not_captured' : 'not_applicable',
  nationwide_reference: null,
  nationwide_status: 'not_collected_separate',
  relevant_variants: [],
  irrelevant_variants: [],
  related_queries: [],
  commercial_intent_observations: [],
  informational_noise_observations: [],
  screenshot_ref: 'evidence/wordstat/acquisition-blocked-20260622.md',
  evidence_grade: 'X_not_collected',
  acquisition_limitations: ['af-006: Wordstat requires authenticated Yandex operator session with geo UI — not available in Cursor agent environment'],
  cluster: q.cluster,
  collection_priority: q.priority,
}));

writeJson(join(SESSION, 'wordstat-collection-normalized.json'), {
  schema_version: '1',
  artifact_id: 'corvonero-wordstat-collection-normalized-v1',
  session_id: 'mig-20260622-corv01',
  matrix_ref: 'corvonero-wordstat-collection-matrix-v1.json',
  generated_at: CAPTURE_ISO,
  status: 'acquisition_blocked',
  query_count: normalized.length,
  collected_count: 0,
  records: normalized,
});

// Broad/exact comparison stub
writeJson(join(SESSION, 'wordstat-broad-exact-comparison.json'), {
  schema_version: '1',
  session_id: 'mig-20260622-corv01',
  generated_at: CAPTURE_ISO,
  status: 'not_executed',
  reason: 'af-006 — Wordstat UI not accessible',
  comparisons: WORDSTAT_MATRIX.filter((q) => q.broad_compare).map((q) => ({
    query_id: q.query_id,
    phrase: q.phrase,
    broad_phrase_frequency: { status: 'not_captured', value: null },
    quoted_phrase_frequency: { status: 'not_captured', value: null },
    regional_result: { region: 'Новосибирск + Новосибирская область', status: 'not_captured' },
    nationwide_reference: { status: 'not_collected', value: null, note: 'Nationwide kept separate — not merged into primary regional evidence' },
    commercially_relevant_subset: { status: 'unknown', note: 'Requires Wordstat related-query review after primary capture' },
    interpretation_limitations: ['Broad Wordstat frequency must not be presented as expected advertising traffic', 'Exact phrase operator syntax not verified without UI capture'],
  })),
});

// R1 SERP
mkdirSync(join(SESSION, 'serp_results_r1'), { recursive: true });
const r1Results = R1_QUERIES.map((r) => {
  const artifact = {
    schema_version: '0.1',
    session_id: 'mig-20260622-corv01',
    query_id: r.r1_id,
    capture_pass: 'r1_human_browser_attempt',
    captured_at: CAPTURE_ISO,
    collection_date: CAPTURE_DATE,
    search_engine: 'yandex',
    region: 'Новосибирск',
    region_lr: 65,
    device: 'mobile',
    query: r.query,
    r1_capture_status: 'failed_captcha',
    evidence_grade: 'C',
    grade_upgrade_attempted: false,
    acquisition_failure: 'af-004',
    acquisition_limitations: [
      'Direct Yandex HTTP fetch returned captcha — not R1 human browser capture',
      'No SERP screenshots saved',
      'Personalization state: SAFE UNKNOWN',
    ],
    fallback_reference: {
      artifact: `serp_results_live/${r.lq_ref}.json`,
      evidence_grade: 'C',
      source_mode: 'bounded_web_search_stage2',
      note: 'Fallback only — does not upgrade R1 grade',
    },
    ads_blocks: 'SAFE UNKNOWN',
    maps_local_pack: 'SAFE UNKNOWN',
    screenshot_refs: [],
  };
  writeJson(join(SESSION, 'serp_results_r1', `${r.r1_id}.json`), artifact);
  return { ...r, artifact: `serp_results_r1/${r.r1_id}.json`, evidence_grade: 'C', r1_status: 'failed_captcha' };
});

writeJson(join(SESSION, 'serp_r1_index.json'), {
  schema_version: '0.1',
  session_id: 'mig-20260622-corv01',
  capture_pass: 'r1_priority_bounded',
  generated_at: CAPTURE_ISO,
  collection_date: CAPTURE_DATE,
  checklist_ref: '../../triumph-gruzotaxi-krasnodar/pilot-serp-capture-checklist.md',
  query_count: 10,
  r1_success_count: 0,
  evidence_grade: 'C',
  acquisition_failure: 'af-004',
  queries: r1Results,
});

// Query cleaning / noise registry
const noisePatterns = [
  { pattern_class: 'job-seeking', examples: ['вакансии программист 1С', 'работа программистом 1С', 'hh.ru'], observed_in: ['lq05', 'ws-p2-006'] },
  { pattern_class: 'educational', examples: ['курсы 1С', 'обучение 1С', 'с нуля'], observed_in: ['seed_matrix'] },
  { pattern_class: 'software-download', examples: ['скачать 1С', 'бесплатно 1С', 'демо версия'], observed_in: ['seed_matrix'] },
  { pattern_class: 'informational', examples: ['инструкция', 'как настроить', 'форум', 'документация'], observed_in: ['lq20', 'lq21', 'lq06'] },
  { pattern_class: 'regulatory', examples: ['государственные требования маркировки', 'закон о маркировке'], observed_in: ['lq17', 'lq21'] },
  { pattern_class: 'equipment_without_service', examples: ['купить сканер маркировки', 'оборудование Честный знак'], observed_in: ['seed_matrix'] },
  { pattern_class: 'operator_marking', examples: ['оператор маркировки', 'регистрация в системе без 1С'], observed_in: ['seed_matrix'] },
  { pattern_class: 'platform_self_update', examples: ['обновление платформы 1С своими руками'], observed_in: ['seed_matrix'] },
];

const phraseClassifications = WORDSTAT_MATRIX.map((q) => {
  const im = INTENT_MAP[q.cluster] || { intent: 'ambiguous', commercial: 'unknown', noise: [] };
  return {
    query_id: q.query_id,
    phrase: q.phrase,
    intent_class: im.intent,
    commercial_relevance: im.commercial,
    noise_classes: im.noise,
    classification_basis: SERP_MAP[q.query_id] ? `serp_inference_from_${SERP_MAP[q.query_id]}` : 'matrix_expected_ambiguity_only',
    evidence_grade: SERP_MAP[q.query_id] ? 'C' : 'D',
    note: 'Groundtruth classification from SERP signals and matrix — not final negative-keyword list',
  };
});

writeJson(join(SESSION, 'query_cleaning_noise_registry.json'), {
  schema_version: '1',
  session_id: 'mig-20260622-corv01',
  generated_at: CAPTURE_ISO,
  purpose: 'query_cleaning_groundtruth_only',
  forbidden_use: 'orca_negative_keyword_list',
  frequent_irrelevant_patterns: noisePatterns,
  phrase_classifications: phraseClassifications,
});

// Demand surface
const clusters = [
  { cluster_id: 'A_broad_1c', label: 'Broad 1C services', subclusters: ['programmer', 'support', 'modification', 'setup'], serp_refs: ['lq01', 'lq02', 'lq03', 'lq04'], wordstat_refs: ['ws-p1-001', 'ws-p1-002', 'ws-p1-003', 'ws-p1-004'] },
  { cluster_id: 'B_reports_forms', label: 'Reports and forms', subclusters: ['reports', 'print_forms', 'rmk'], serp_refs: ['lq09', 'lq10', 'lq12'], wordstat_refs: ['ws-p2-001', 'ws-p2-002', 'ws-p2-003'] },
  { cluster_id: 'C_integrations', label: 'Integrations', subclusters: ['website', 'bitrix', 'sync_exchange'], serp_refs: ['lq13', 'lq14', 'lq15'], wordstat_refs: ['ws-p1-005', 'ws-p1-006', 'ws-p2-004'] },
  { cluster_id: 'D_labeling', label: 'Labeling / Честный знак', subclusters: ['generic_marking', 'honest_sign', 'implementation_setup'], serp_refs: ['lq17', 'lq18', 'lq19', 'lq20'], wordstat_refs: ['ws-p1-007', 'ws-p1-008'] },
  { cluster_id: 'D_ts_piot', label: 'TS PIOT', subclusters: ['ts_piot_setup'], serp_refs: ['lq21', 'lq22'], wordstat_refs: ['ws-p3-004'] },
  { cluster_id: 'E_product_labeling', label: 'Product-specific labeling', subclusters: ['beer', 'water', 'medicines', 'auto_parts'], serp_refs: ['lq23', 'lq24', 'lq25', 'lq26'], wordstat_refs: ['ws-p3-001', 'ws-p3-002', 'ws-p3-003', 'ws-p3-005'] },
  { cluster_id: 'A_urgent', label: 'Troubleshooting / urgent', subclusters: ['not_working', 'errors', 'urgent_programmer'], serp_refs: ['lq05', 'lq06', 'lq07', 'lq08'], wordstat_refs: ['ws-p2-006', 'ws-p2-007'] },
];

function clusterAssessment(c) {
  const hasSerp = c.serp_refs.length > 0;
  const wsBlocked = true;
  return {
    cluster_id: c.cluster_id,
    label: c.label,
    subclusters: c.subclusters,
    collected_demand_evidence: wsBlocked ? 'wordstat_not_collected' : 'partial',
    direct_phrase_demand: 'SAFE UNKNOWN — Wordstat not captured (af-006)',
    broader_thematic_demand: hasSerp ? 'commercial demand observed in SERP synthesis (grade C)' : 'SAFE UNKNOWN',
    commercial_intent_density: c.cluster_id === 'A_urgent' ? 'mixed — vacancy noise on urgent formulations' : c.cluster_id === 'D_ts_piot' ? 'low — informational dominance observed' : c.cluster_id === 'C_integrations' ? 'high — web studios dominate SERP' : 'moderate to high where SERP commercial_signal strong',
    informational_noise_level: ['D_labeling', 'D_ts_piot', 'A_urgent'].includes(c.cluster_id) ? 'high to moderate' : 'low to moderate',
    geo_sensitivity: ['A_broad_1c'].includes(c.cluster_id) ? 'geo wording observed in SERP for head terms' : 'moderate — some clusters work without geo per matrix notes',
    query_diversity: 'multiple distinct formulations in seed matrix and live SERP pass',
    available_competitor_supply: 'local 1C firms, franchisees, web studios (integrations), labeling specialists — see competitors-shortlist-confirmed.json',
    evidence_strength: 'SERP grade C; Wordstat grade X_not_collected',
    uncertainty: ['Regional search volume unknown', 'Ad density unknown', 'R1 live SERP blocked by captcha (af-004)'],
    orca_review_suitability: wsBlocked ? 'conditional — SERP-only evidence insufficient for volume-based ORCA decisions; qualitative cluster separation supported' : 'ready',
    serp_evidence_refs: c.serp_refs.map((id) => `serp_results_live/${id}.json`),
    wordstat_evidence_refs: c.wordstat_refs.map((id) => `wordstat-collection-normalized.json#${id}`),
  };
}

writeJson(join(SESSION, 'demand_surface.json'), {
  schema_version: '1',
  artifact_id: 'corvonero-demand-surface-v1',
  session_id: 'mig-20260622-corv01',
  project_ref: 'PRJ-0013',
  generated_at: CAPTURE_ISO,
  geography_primary: { city: 'Новосибирск', region: 'Новосибирская область' },
  status: 'partial_serp_only',
  evidence_summary: {
    wordstat: { status: 'not_collected', grade: 'X_not_collected', failure: 'af-006' },
    serp_stage2: { status: 'collected', grade: 'C', query_count: 27 },
    serp_r1_priority: { status: 'failed_captcha', grade: 'C', failure: 'af-004' },
  },
  clusters: clusters.map(clusterAssessment),
  session_safe_unknown: ['CPC', 'CTR', 'conversion rate', 'CPL', 'lead quality', 'total market size', 'Wordstat regional volumes'],
});

// Keyword registry
const keywords = WORDSTAT_MATRIX.map((q, i) => {
  const im = INTENT_MAP[q.cluster] || {};
  const lq = SERP_MAP[q.query_id];
  let reviewStatus = 'needs_review';
  if (q.cluster === 'D_ts_piot') reviewStatus = 'informational-only';
  if (q.cluster === 'A_urgent' && q.query_id === 'ws-p2-006') reviewStatus = 'weak demand';
  if (im.commercial === 'high' && lq) reviewStatus = 'accepted for evidence';

  return {
    keyword_id: `kw-corv01-${String(i + 1).padStart(3, '0')}`,
    query_id: q.query_id,
    source_phrase: q.phrase,
    normalized_phrase: q.phrase.toLowerCase(),
    cluster: q.cluster,
    subcluster: q.cluster.split('_').slice(1).join('_'),
    geography: 'Новосибирск + Новосибирская область',
    wordstat_evidence: { status: 'not_captured', ref: `wordstat_snapshot.cap-20260622-corv01.json#WS-${String(i + 1).padStart(2, '0')}` },
    serp_evidence: lq ? { status: 'captured_grade_C', ref: `serp_results_live/${lq}.json` } : { status: 'not_mapped', ref: null },
    intent_class: im.intent || 'ambiguous',
    commercial_relevance: im.commercial || 'SAFE UNKNOWN',
    ambiguity: q.cluster === 'A_urgent' ? 'high' : 'low to moderate',
    noise_classes: im.noise || [],
    evidence_grade: lq ? 'C' : 'X_not_collected',
    source_references: [q.query_id, lq].filter(Boolean),
    review_status: reviewStatus,
    orca_handoff_eligibility: reviewStatus === 'accepted for evidence' ? 'eligible_with_volume_unknown' : reviewStatus === 'informational-only' ? 'defer' : 'needs_review',
    numeric_slots: {
      freq: { status: 'not_captured', value: null, safe_unknown: ['af-006 Wordstat not collected'] },
      trend: { status: 'not_captured' },
      share: { status: 'not_captured' },
    },
    safe_unknown: ['Wordstat frequency unknown', 'SERP grade C — not R1 live capture'],
    capture_time: CAPTURE_ISO,
  };
});

writeJson(join(SESSION, 'keyword_registry.json'), {
  registry_id: 'kr-mig-20260622-corv01-v1',
  session_id: 'mig-20260622-corv01',
  revision: 1,
  registry_state: 'draft_pending_operator_review',
  keyword_pass_status: 'partial',
  generated_at: CAPTURE_ISO,
  keywords,
  registry_safe_unknown: [
    'Wordstat volumes not captured — keyword_pass incomplete for volume groundtruth',
    'Registry is groundtruth evidence index — not final advertising keywords',
    'No ORCA negative-keyword list derived from this registry',
  ],
});

console.log('Generated Demand Surface artifacts in', SESSION);
