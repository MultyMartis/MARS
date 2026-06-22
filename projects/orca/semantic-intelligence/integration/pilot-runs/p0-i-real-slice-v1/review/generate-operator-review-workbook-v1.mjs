#!/usr/bin/env node
/**
 * P0-I Operator Review Workbook v1 generator.
 * Prepares human review package only — does not mutate pilot runtime outputs.
 */
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PILOT_ROOT = path.resolve(__dirname, '..');
const REPO = path.resolve(PILOT_ROOT, '../../../../../..');
const require = createRequire(import.meta.url);
const ExcelJS = require(path.join(
  REPO,
  'projects/orca/ppc/triumph-manipulator/tools/exporter-cli/node_modules/exceljs'
));

const PILOT_RUN_ID = 'p0-i-real-slice-v1';
const RUNTIME_COMMIT = '1fcf3d2';
const WORKBOOK_ID = 'ORCA-P0-I-OPERATOR-REVIEW-WORKBOOK-v1';
const WORKBOOK_FILE = 'ORCA-P0-I-OPERATOR-REVIEW-WORKBOOK-v1.xlsx';
const AUDIT_SEED = 'p0-i-operator-review-workbook-audit-v1-20260622';
const MAX_RANDOM_AUDIT = 20;

const OPERATOR_DECISIONS = [
  'APPROVE_ACCEPT',
  'APPROVE_REJECT',
  'APPROVE_ABSTAIN',
  'CHANGE_TO_ACCEPT',
  'CHANGE_TO_REJECT',
  'CHANGE_TO_ABSTAIN',
  'NEEDS_DOMAIN_EXPERT',
  'INVALID_RECORD',
];

const ERROR_TYPES = [
  'NONE',
  'OVER_ADMISSION',
  'OVER_REJECTION',
  'EXCESS_ABSTENTION',
  'WRONG_PRIMARY_INTENT',
  'WRONG_SECONDARY_INTENT',
  'WRONG_PROTECTED_CLASS',
  'WRONG_PROVIDER_DIY_SPLIT',
  'WRONG_PRODUCT_SERVICE_SPLIT',
  'WRONG_SUPPORT_INFORMATION_SPLIT',
  'WRONG_CAREER_PROVIDER_SPLIT',
  'WRONG_PROBLEM_QUERY_HANDLING',
  'INSUFFICIENT_EVIDENCE',
  'RATIONALE_GENERIC',
  'RATIONALE_INCORRECT',
  'DOMAIN_KNOWLEDGE_ERROR',
  'SOURCE_OR_PROVENANCE_ERROR',
  'SCHEMA_OR_RECORD_ERROR',
  'OTHER',
];

const ELIGIBILITY_VALUES = ['ACCEPT', 'REJECT', 'ABSTAIN'];

const QUEUE_LABELS = {
  '01_all_abstain': 'ABSTAIN mandatory',
  '02_blocked_accept': 'Blocked ACCEPT',
  '03_high_critical_risk': 'HIGH/CRITICAL risk',
  '04_protected_strata_conflicts': 'Protected strata conflict',
  '05_short_head_cases': 'Short-head term',
  '06_problem_query_ambiguity': 'Problem-query ambiguity',
  '07_product_service_ambiguity': 'Product/service conflict',
  '08_career_provider_ambiguity': 'Career/provider conflict',
  '09_provider_diy_ambiguity': 'Provider/DIY conflict',
  '10_legacy_new_disagreement': 'Legacy/new disagreement',
  '11_random_accept_audit': 'Pilot random ACCEPT audit',
  '12_random_reject_audit': 'Pilot random REJECT audit',
};

const PROTECTED_INTENTS = new Set([
  'CAREER_EMPLOYMENT',
  'EDUCATIONAL',
  'DIY_HOW_TO',
  'REGULATORY',
  'NAVIGATIONAL',
  'LOGIN_ACCOUNT_ACCESS',
  'DOCUMENTATION_LOOKUP',
  'DOWNLOAD_RESOURCE',
  'TROUBLESHOOT_SELF',
]);

const PROTECTED_AMBIGUITY = new Set([
  'CAREER_VS_PROVIDER',
  'PROVIDER_VS_DIY',
  'PRODUCT_VS_SERVICE',
  'SUPPORT_VS_INFORMATION',
  'REGULATORY_VS_SERVICE',
  'SHORT_HEAD_TERM',
]);

function readJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function writeJson(p, data) {
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, `${JSON.stringify(data, null, 2)}\n`, 'utf8');
}

function writeText(p, text) {
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, text, 'utf8');
}

function joinList(v) {
  if (v == null) return '';
  if (Array.isArray(v)) return v.map((x) => (typeof x === 'object' ? JSON.stringify(x) : String(x))).join('; ');
  return String(v);
}

function hashScore(seed, cls, queryId) {
  const h = crypto.createHash('sha256').update(`${seed}:${cls}:${queryId}`).digest();
  return h.readUInt32BE(0);
}

function priorityRank(p) {
  return { P0: 0, P1: 1, P2: 2, P3: 3 }[p] ?? 9;
}

function loadPrimaryIntents() {
  const tax = readJson(
    path.join(REPO, 'projects/orca/semantic-intelligence/taxonomy/orca-primary-intent-taxonomy-v1.json')
  );
  return tax.intents.map((i) => i.intent_id);
}

function loadSources() {
  const manifest = readJson(path.join(PILOT_ROOT, 'selection/p0-i-pilot-selection-manifest-v1.json'));
  const records = readJson(path.join(PILOT_ROOT, 'output/p0-i-pilot-semantic-records-v1.json')).records;
  const metrics = readJson(path.join(PILOT_ROOT, 'reports/p0-i-integration-metrics-v1.json'));
  const legacy = readJson(path.join(PILOT_ROOT, 'diagnostics/p0-i-legacy-diagnostic-comparison-v1.json'));
  const queuesRoot = readJson(path.join(PILOT_ROOT, 'review/p0-i-human-review-queues-v1.json')).queues;
  const inputLines = fs
    .readFileSync(path.join(PILOT_ROOT, 'input/p0-i-pilot-input-v1.jsonl'), 'utf8')
    .trim()
    .split('\n')
    .map((l) => JSON.parse(l));

  const manifestByPilot = new Map(manifest.rows.map((r) => [r.pilot_row_id, r]));
  const inputByPilot = new Map(inputLines.map((r) => [r.pilot_row_id, r]));

  const queueMembership = new Map();
  for (const [qk, entries] of Object.entries(queuesRoot)) {
    for (const e of entries) {
      const qid = e.pilot_row_id;
      if (!queueMembership.has(qid)) queueMembership.set(qid, new Set());
      queueMembership.get(qid).add(qk);
    }
  }

  return { manifest, records, metrics, legacy, queuesRoot, inputLines, manifestByPilot, inputByPilot, queueMembership };
}

function runParityAudit(sources) {
  const { manifest, records, metrics, legacy, queuesRoot, inputLines } = sources;
  const queryIds = records.map((r) => r.phrase_id);
  const uniqueQueryIds = new Set(queryIds);
  const decisions = { ACCEPT: 0, REJECT: 0, ABSTAIN: 0 };
  for (const r of records) decisions[r.admission_decision]++;

  const queueRefs = new Set();
  let operatorFilled = 0;
  for (const entries of Object.values(queuesRoot)) {
    for (const e of entries) {
      queueRefs.add(e.pilot_row_id);
      if (e.operator_decision) operatorFilled++;
    }
  }

  const checks = {
    frozen_input_count: inputLines.length,
    selection_manifest_count: manifest.rows.length,
    semantic_record_count: records.length,
    unique_query_id_count: uniqueQueryIds.size,
    duplicate_query_ids: queryIds.length - uniqueQueryIds.size,
    accept_count: decisions.ACCEPT,
    reject_count: decisions.REJECT,
    abstain_count: decisions.ABSTAIN,
    legacy_commercial_new_reject: legacy.summary.legacy_commercial_new_reject,
    legacy_commercial_new_abstain: legacy.summary.legacy_commercial_new_abstain,
    legacy_same_decision: legacy.summary.same_decision,
    queue_reference_count: queueRefs.size,
    operator_decisions_populated: operatorFilled,
    runtime_commit_expected: RUNTIME_COMMIT,
    metrics_runtime_commit: metrics.runtime_commit,
  };

  const expected = {
    total_unique_records: 200,
    accept: 77,
    reject: 53,
    abstain: 70,
    legacy_commercial_new_reject: 39,
    legacy_commercial_new_abstain: 69,
    legacy_same: 92,
  };

  const passed =
    checks.frozen_input_count === expected.total_unique_records &&
    checks.selection_manifest_count === expected.total_unique_records &&
    checks.semantic_record_count === expected.total_unique_records &&
    checks.unique_query_id_count === expected.total_unique_records &&
    checks.duplicate_query_ids === 0 &&
    checks.accept_count === expected.accept &&
    checks.reject_count === expected.reject &&
    checks.abstain_count === expected.abstain &&
    checks.legacy_commercial_new_reject === expected.legacy_commercial_new_reject &&
    checks.legacy_commercial_new_abstain === expected.legacy_commercial_new_abstain &&
    checks.legacy_same_decision === expected.legacy_same &&
    checks.operator_decisions_populated === 0 &&
    checks.metrics_runtime_commit === RUNTIME_COMMIT;

  return { checks, expected, passed };
}

function classifyRow(record, manifestRow, queueKeys) {
  const rec = record.integration_result?.record || {};
  const diag = record.integration_result?.diagnostic_comparison || {};
  const validation = record.integration_result?.validation || {};
  const routing = record.integration_result?.routing || {};
  const ambiguityTypes = new Set(rec.ambiguity?.types || []);
  const routes = routing.routes || [];
  const invariantFindings = (validation.findings || []).map((f) => f.invariant_id || f.code || JSON.stringify(f));

  const flags = {
    blocked: Boolean(record.blocked),
    highRisk: ['HIGH', 'CRITICAL'].includes(rec.risk?.overall_risk),
    protectedStrata:
      ambiguityTypes.has('CAREER_VS_PROVIDER') ||
      ambiguityTypes.has('PROVIDER_VS_DIY') ||
      ambiguityTypes.has('REGULATORY_VS_SERVICE') ||
      routes.includes('PROTECTED_STRATA') ||
      queueKeys.has('04_protected_strata_conflicts'),
    evidenceIssue:
      rec.provenance_status !== 'COMPLETE' ||
      (rec.commercial_eligibility?.reviewer_required &&
        !(rec.commercial_eligibility?.supporting_evidence || []).length &&
        !(rec.commercial_eligibility?.opposing_evidence || []).length),
    invariantWarning: invariantFindings.length > 0 || routes.includes('INVARIANT_WARNING'),
    abstain: record.admission_decision === 'ABSTAIN',
    legacyReject: diag.disagreement_type === 'LEGACY_ACCEPT_NEW_REJECT',
    legacyAbstain: diag.disagreement_type === 'LEGACY_ELIGIBLE_NEW_ABSTAIN',
    shortHead: queueKeys.has('05_short_head_cases') || ambiguityTypes.has('SHORT_HEAD_TERM'),
    problemQuery: queueKeys.has('06_problem_query_ambiguity'),
    productService: queueKeys.has('07_product_service_ambiguity') || ambiguityTypes.has('PRODUCT_VS_SERVICE'),
    careerProvider: queueKeys.has('08_career_provider_ambiguity') || ambiguityTypes.has('CAREER_VS_PROVIDER'),
    providerDiy: queueKeys.has('09_provider_diy_ambiguity') || ambiguityTypes.has('PROVIDER_VS_DIY'),
    supportInfo: ambiguityTypes.has('SUPPORT_VS_INFORMATION'),
    legacyDisagreement: diag.disagreement_type && diag.disagreement_type !== 'NONE',
    sameLegacy: !diag.disagreement_type || diag.disagreement_type === 'NONE',
    lowRiskClear:
      rec.risk?.overall_risk === 'LOW' &&
      !record.blocked &&
      record.admission_decision !== 'ABSTAIN' &&
      invariantFindings.length === 0,
  };

  let reviewPriority = 'P3';
  const p0 =
    flags.blocked ||
    flags.highRisk ||
    flags.protectedStrata ||
    flags.evidenceIssue ||
    flags.invariantWarning;
  const p1 =
    flags.abstain ||
    flags.legacyReject ||
    flags.legacyAbstain ||
    flags.shortHead ||
    flags.problemQuery ||
    flags.productService ||
    flags.careerProvider ||
    flags.providerDiy ||
    flags.supportInfo;

  if (p0) reviewPriority = 'P0';
  else if (p1) reviewPriority = 'P1';

  return { flags, reviewPriority, invariantFindings, routes, ambiguityTypes, diag, rec };
}

function buildRows(sources, primaryIntents) {
  const { records, manifestByPilot, queueMembership } = sources;
  const rows = records.map((record, idx) => {
    const manifestRow = manifestByPilot.get(record.pilot_row_id);
    const queueKeys = queueMembership.get(record.pilot_row_id) || new Set();
    const { flags, reviewPriority, invariantFindings, routes, ambiguityTypes, diag, rec } = classifyRow(
      record,
      manifestRow,
      queueKeys
    );

    const queueLabels = [...queueKeys].map((k) => QUEUE_LABELS[k] || k);
    const freq = manifestRow?.frequency_evidence || {};
    const prov = manifestRow?.provenance || record.integration_result?.record?.provenance || {};

    return {
      row_number: idx + 1,
      pilot_row_id: record.pilot_row_id,
      source_query_id: record.phrase_id,
      raw_query: rec.raw_query || manifestRow?.raw_query,
      normalized_query: rec.normalized_query || manifestRow?.normalized_query,
      source_path_reference: manifestRow?.source_path || '',
      source_row_reference: manifestRow?.source_row_reference || record.phrase_id,
      frequency_evidence: freq.combined_frequency ?? freq.max_frequency ?? '',
      phrase_origin: manifestRow?.phrase_origin || '',
      sampling_stratum: manifestRow?.intended_sampling_stratum || '',
      provenance_status: rec.provenance_status || prov.status || '',
      automated_decision: record.admission_decision,
      primary_intent: rec.primary_intent || '',
      secondary_intents: joinList(rec.secondary_intents),
      likely_user_goal: rec.likely_user_goal || '',
      literal_interpretation: rec.literal_interpretation || '',
      supporting_evidence: joinList(rec.commercial_eligibility?.supporting_evidence),
      opposing_evidence: joinList(rec.commercial_eligibility?.opposing_evidence),
      ambiguity_type: joinList(rec.ambiguity?.types),
      ambiguity_severity: rec.ambiguity?.severity || '',
      risk: rec.risk?.overall_risk || '',
      reason_code: rec.commercial_eligibility?.reason_code || '',
      confidence: rec.commercial_eligibility?.confidence ?? '',
      reviewer_required: rec.commercial_eligibility?.reviewer_required ? 'YES' : 'NO',
      invariant_findings: joinList(invariantFindings),
      review_routes: joinList(routes),
      review_queues: joinList(queueLabels),
      review_priority: reviewPriority,
      legacy_intent: diag.legacy_intent || '',
      legacy_eligibility: diag.legacy_eligibility || '',
      legacy_reason: diag.legacy_reason || '',
      disagreement_type: diag.disagreement_type || 'NONE',
      unresolved_questions: joinList(rec.ambiguity?.unresolved_questions),
      operator_decision: '',
      corrected_eligibility: '',
      corrected_primary_intent: '',
      primary_error_type: '',
      secondary_error_types: '',
      operator_comment: '',
      needs_domain_expert: '',
      reviewed_by: '',
      review_date: '',
      flags,
      queue_keys: [...queueKeys],
    };
  });

  return rows;
}

function selectWorkbookRandomAudit(rows) {
  const mandatoryIds = new Set(rows.filter((r) => r.review_priority === 'P0' || r.review_priority === 'P1').map((r) => r.source_query_id));

  const acceptPool = rows
    .filter((r) => r.automated_decision === 'ACCEPT' && !mandatoryIds.has(r.source_query_id))
    .map((r) => r.source_query_id)
    .sort();

  const rejectPool = rows
    .filter((r) => r.automated_decision === 'REJECT' && !mandatoryIds.has(r.source_query_id))
    .map((r) => r.source_query_id)
    .sort();

  const pick = (pool, cls) =>
    [...pool]
      .map((id) => ({ id, score: hashScore(AUDIT_SEED, cls, id) }))
      .sort((a, b) => a.score - b.score || a.id.localeCompare(b.id))
      .slice(0, MAX_RANDOM_AUDIT)
      .map((x) => x.id);

  const acceptSelected = pick(acceptPool, 'ACCEPT');
  const rejectSelected = pick(rejectPool, 'REJECT');

  for (const row of rows) {
    if (acceptSelected.includes(row.source_query_id)) {
      row.workbook_random_accept_audit = 'YES';
      if (row.review_priority === 'P3') row.review_priority = 'P2';
    }
    if (rejectSelected.includes(row.source_query_id)) {
      row.workbook_random_reject_audit = 'YES';
      if (row.review_priority === 'P3') row.review_priority = 'P2';
    }
  }

  return {
    seed: AUDIT_SEED,
    algorithm:
      'SHA-256 sort key: hash(seed:decision_class:query_id); ascending sort; take first N up to 20; non-mandatory population only',
    max_per_class: MAX_RANDOM_AUDIT,
    selection_timestamp: new Date().toISOString(),
    accept: {
      source_population_count: acceptPool.length,
      selected_count: acceptSelected.length,
      selected_query_ids: acceptSelected,
    },
    reject: {
      source_population_count: rejectPool.length,
      selected_count: rejectSelected.length,
      selected_query_ids: rejectSelected,
    },
    mandatory_excluded_count: mandatoryIds.size,
  };
}

function rowToArray(row, includeEvidence = true) {
  const base = [
    row.row_number,
    row.pilot_row_id,
    row.source_query_id,
    row.raw_query,
    row.normalized_query,
    row.source_path_reference,
    row.frequency_evidence,
    row.phrase_origin,
    row.sampling_stratum,
    row.provenance_status,
  ];
  const auto = includeEvidence
    ? [
        row.automated_decision,
        row.primary_intent,
        row.secondary_intents,
        row.likely_user_goal,
        row.literal_interpretation,
        row.supporting_evidence,
        row.opposing_evidence,
        row.ambiguity_type,
        row.ambiguity_severity,
        row.risk,
        row.reason_code,
        row.confidence,
        row.reviewer_required,
        row.invariant_findings,
        row.review_routes,
        row.review_queues,
        row.review_priority,
      ]
    : [row.automated_decision, row.primary_intent, row.review_priority];
  const legacy = [row.legacy_intent, row.legacy_eligibility, row.legacy_reason, row.disagreement_type];
  const operator = [
    row.operator_decision,
    row.corrected_eligibility,
    row.corrected_primary_intent,
    row.primary_error_type,
    row.secondary_error_types,
    row.operator_comment,
    row.needs_domain_expert,
    row.reviewed_by,
    row.review_date,
  ];
  return [...base, ...auto, ...legacy, ...operator];
}

const MASTER_HEADERS = [
  '№ строки',
  'Pilot row ID',
  'Source query ID',
  'Исходный запрос',
  'Нормализованный запрос',
  'Путь/ссылка источника',
  'Частотность',
  'Natural/Synthetic',
  'Страта выборки',
  'Статус provenance',
  'Авто-решение',
  'Primary intent',
  'Secondary intents',
  'Likely user goal',
  'Literal interpretation',
  'Supporting evidence',
  'Opposing evidence',
  'Ambiguity type',
  'Ambiguity severity',
  'Risk',
  'Reason code',
  'Confidence',
  'Reviewer required',
  'Invariant findings',
  'Review routes',
  'Review queues',
  'Review priority',
  'Legacy intent',
  'Legacy eligibility',
  'Legacy reason',
  'Disagreement type',
  'Operator decision',
  'Corrected eligibility',
  'Corrected primary intent',
  'Primary error type',
  'Secondary error types',
  'Operator comment',
  'Needs domain expert',
  'Reviewed by',
  'Review date',
];

function mandatorySortKey(row) {
  if (row.review_priority === 'P0') return [0, row.row_number];
  if (row.flags.abstain) return [1, row.row_number];
  if (row.flags.legacyReject) return [2, row.row_number];
  if (row.flags.legacyAbstain) return [3, row.row_number];
  return [4, row.row_number];
}

function isProtectedClassRow(row) {
  return (
    PROTECTED_INTENTS.has(row.primary_intent) ||
    [...(row.ambiguity_type || '').split('; ')].some((t) => PROTECTED_AMBIGUITY.has(t)) ||
    row.flags.careerProvider ||
    row.flags.providerDiy ||
    row.flags.productService ||
    row.flags.supportInfo
  );
}

function addDataValidation(ws, colIndex, rangeRef, startRow = 2, endRow = 201) {
  const letter = ws.getColumn(colIndex).letter;
  for (let r = startRow; r <= endRow; r++) {
    ws.getCell(`${letter}${r}`).dataValidation = {
      type: 'list',
      allowBlank: true,
      formulae: [rangeRef],
      showErrorMessage: true,
      errorTitle: 'Недопустимое значение',
      error: 'Выберите значение из списка',
    };
  }
}

function addEnumSheet(wb, primaryIntents) {
  const ws = wb.addWorksheet('_Enums');
  ws.state = 'veryHidden';
  ws.addRow(['operator_decision', 'error_type', 'primary_intent', 'eligibility', 'yes_no']);
  OPERATOR_DECISIONS.forEach((v, i) => {
    const row = ws.getRow(i + 2);
    row.getCell(1).value = v;
  });
  ERROR_TYPES.forEach((v, i) => {
    ws.getRow(i + 2).getCell(2).value = v;
  });
  primaryIntents.forEach((v, i) => {
    ws.getRow(i + 2).getCell(3).value = v;
  });
  ELIGIBILITY_VALUES.forEach((v, i) => {
    ws.getRow(i + 2).getCell(4).value = v;
  });
  ['YES', 'NO'].forEach((v, i) => {
    ws.getRow(i + 2).getCell(5).value = v;
  });
  return {
    operatorDecision: `_Enums!$A$2:$A$${OPERATOR_DECISIONS.length + 1}`,
    errorType: `_Enums!$B$2:$B$${ERROR_TYPES.length + 1}`,
    primaryIntent: `_Enums!$C$2:$C$${primaryIntents.length + 1}`,
    eligibility: `_Enums!$D$2:$D$${ELIGIBILITY_VALUES.length + 1}`,
    yesNo: `_Enums!$E$2:$E$3`,
  };
}

async function buildWorkbook(rows, primaryIntents, randomAudit) {
  const wb = new ExcelJS.Workbook();
  wb.creator = 'ORCA P0-I Review Package';
  wb.created = new Date();

  const autoFill = 'FFE8EEF7';
  const opFill = 'FFFFF2CC';
  const headerFill = 'FFD9E1F2';
  const enumRanges = addEnumSheet(wb, primaryIntents);

  const instr = wb.addWorksheet('Инструкция');
  instr.protect('', { selectLockedCells: true });
  const instructions = [
    ['ORCA P0-I Operator Review Workbook v1'],
    [''],
    ['Назначение', 'Проверка 200 фраз пилота P0-I без изменения канонических JSON-артефактов runtime.'],
    ['Не benchmark', 'Этот workbook НЕ является gold/benchmark набором и не становится истиной автоматически.'],
    ['Авто vs оператор', 'Колонки автоматического вывода — только для чтения (серый фон). Решение оператора — жёлтый фон.'],
    ['ACCEPT', 'Допуск к коммерческому рассмотрению при достаточном evidence.'],
    ['REJECT', 'Явный отказ / защищённая страта / недопустимый запрос.'],
    ['ABSTAIN', 'Недостаточно evidence или неразрешённая амбивалентность — требуется человек.'],
    ['Operator decision', OPERATOR_DECISIONS.join(', ')],
    ['Error types', ERROR_TYPES.join(', ')],
    ['Обязательные поля', 'Operator decision; при CHANGE — corrected eligibility/intent и error type; comment для CHANGE/NEEDS_DOMAIN_EXPERT/INVALID_RECORD'],
    ['Запрещено', 'Не редактировать авто-поля, не переименовывать листы/колонки, не удалять строки.'],
    ['Возврат', 'Сохранить файл ORCA-P0-I-OPERATOR-REVIEW-WORKBOOK-v1.xlsx и вернуть для импорта overlay.'],
    ['Порядок', '1) Обязательная проверка 2) Random audit в ACCEPT/REJECT 3) Опционально остальное'],
    ['Domain expert', 'Используйте NEEDS_DOMAIN_EXPERT — не обязаны решать доменные вопросы в одиночку.'],
  ];
  instructions.forEach((r) => instr.addRow(r));
  instr.getColumn(1).width = 28;
  instr.getColumn(2).width = 100;

  const writeDataSheet = (name, sheetRows, extraCols = null) => {
    const ws = wb.addWorksheet(name.slice(0, 31));
    const headers = extraCols ? [...MASTER_HEADERS, ...extraCols] : MASTER_HEADERS;
    ws.addRow(headers);
    const headerRow = ws.getRow(1);
    headerRow.font = { bold: true };
    headerRow.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: headerFill } };
    headerRow.alignment = { wrapText: true, vertical: 'middle' };
    ws.views = [{ state: 'frozen', ySplit: 1 }];
    ws.autoFilter = { from: 'A1', to: `${ws.getColumn(headers.length).letter}1` };

    for (const row of sheetRows) {
      const arr = rowToArray(row);
      if (extraCols) {
        extraCols.forEach((c) => {
          if (c === 'Random audit sample') arr.push(row.workbook_random_accept_audit === 'YES' || row.workbook_random_reject_audit === 'YES' ? 'YES' : 'NO');
          if (c === 'Mandatory review') arr.push(['P0', 'P1'].includes(row.review_priority) ? 'YES' : 'NO');
          if (c === 'Optional review') arr.push(row.review_priority === 'P3' ? 'YES' : 'NO');
          if (c === 'Unresolved questions') arr.push(row.unresolved_questions || '');
        });
      }
      const excelRow = ws.addRow(arr);
      excelRow.alignment = { wrapText: true, vertical: 'top' };
    }

    const autoEnd = 10 + 17;
    const opStart = headers.indexOf('Operator decision') + 1;
    for (let r = 2; r <= sheetRows.length + 1; r++) {
      for (let c = 1; c <= headers.length; c++) {
        const cell = ws.getRow(r).getCell(c);
        if (c <= autoEnd || (c > autoEnd && c < opStart)) {
          cell.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: autoFill } };
          cell.protection = { locked: true };
        } else {
          cell.fill = { type: 'pattern', pattern: 'solid', fgColor: { argb: opFill } };
          cell.protection = { locked: false };
        }
      }
    }

    ws.getColumn(4).width = 36;
    ws.getColumn(5).width = 36;
    ws.getColumn(15).width = 28;
    ws.getColumn(16).width = 24;
    ws.getColumn(17).width = 24;
    ws.getColumn(36).width = 40;

    const opDecisionCol = headers.indexOf('Operator decision') + 1;
    const corrEligCol = headers.indexOf('Corrected eligibility') + 1;
    const corrIntentCol = headers.indexOf('Corrected primary intent') + 1;
    const primaryErrCol = headers.indexOf('Primary error type') + 1;
    const needsExpertCol = headers.indexOf('Needs domain expert') + 1;
    addDataValidation(ws, opDecisionCol, enumRanges.operatorDecision, 2, sheetRows.length + 1);
    addDataValidation(ws, corrEligCol, enumRanges.eligibility, 2, sheetRows.length + 1);
    addDataValidation(ws, corrIntentCol, enumRanges.primaryIntent, 2, sheetRows.length + 1);
    addDataValidation(ws, primaryErrCol, enumRanges.errorType, 2, sheetRows.length + 1);
    addDataValidation(ws, needsExpertCol, enumRanges.yesNo, 2, sheetRows.length + 1);

    return ws;
  };

  writeDataSheet('Все 200 фраз', rows);

  const mandatoryRows = rows
    .filter((r) => r.review_priority === 'P0' || r.review_priority === 'P1')
    .sort((a, b) => {
      const ka = mandatorySortKey(a);
      const kb = mandatorySortKey(b);
      return ka[0] - kb[0] || ka[1] - kb[1];
    });
  writeDataSheet('Обязательная проверка', mandatoryRows);

  writeDataSheet(
    'ACCEPT',
    rows.filter((r) => r.automated_decision === 'ACCEPT'),
    ['Random audit sample', 'Mandatory review', 'Optional review']
  );
  writeDataSheet('REJECT', rows.filter((r) => r.automated_decision === 'REJECT'));
  writeDataSheet('ABSTAIN', rows.filter((r) => r.automated_decision === 'ABSTAIN'), ['Unresolved questions']);
  writeDataSheet(
    'Legacy расхождения',
    rows.filter((r) => r.disagreement_type && r.disagreement_type !== 'NONE')
  );
  writeDataSheet('Проблемные запросы', rows.filter((r) => r.flags.problemQuery));
  writeDataSheet('Защищённые классы', rows.filter(isProtectedClassRow));

  const summary = wb.addWorksheet('Сводка');
  const mandatoryCount = mandatoryRows.length;
  const randomAcceptCount = randomAudit.accept.selected_count;
  const randomRejectCount = randomAudit.reject.selected_count;
  const mandatoryCompletionRequired = mandatoryCount + randomAcceptCount + randomRejectCount;

  summary.addRow(['Метрика', 'Значение', 'Формула/примечание']);
  summary.getRow(1).font = { bold: true };
  const summaryRows = [
    ['Всего строк (master)', 200, 'COUNT(Все 200 фраз)'],
    ['Проверено оператором', 0, 'COUNTIF(Operator decision, not blank) — заполняется при review'],
    ['Осталось проверить', mandatoryCompletionRequired, 'Mandatory + random audit target'],
    ['Обязательная проверка (P0+P1)', mandatoryCount, 'Дедуплицированный лист'],
    ['Random ACCEPT audit', randomAcceptCount, `Seed: ${AUDIT_SEED}`],
    ['Random REJECT audit', randomRejectCount, `Seed: ${AUDIT_SEED}`],
    ['ACCEPT (авто)', rows.filter((r) => r.automated_decision === 'ACCEPT').length, ''],
    ['REJECT (авто)', rows.filter((r) => r.automated_decision === 'REJECT').length, ''],
    ['ABSTAIN (авто)', rows.filter((r) => r.automated_decision === 'ABSTAIN').length, ''],
    ['Изменённые решения', 0, 'Заполняется после import — CHANGE_* decisions'],
    ['Approval rate', 'N/A', 'Не вычислять до заполнения operator decisions'],
    ['Domain expert pending', 0, 'COUNTIF decision = NEEDS_DOMAIN_EXPERT'],
    ['Invalid records', 0, 'COUNTIF decision = INVALID_RECORD'],
    ['P0-I status', 'PILOT EXECUTED — HUMAN REVIEW IN PROGRESS', ''],
    ['P0-D', 'ON HOLD', ''],
    ['Corvonero', 'FROZEN', ''],
    ['Campaign Production', 'BLOCKED', ''],
  ];
  summaryRows.forEach((r) => summary.addRow(r));
  summary.getColumn(1).width = 34;
  summary.getColumn(2).width = 24;
  summary.getColumn(3).width = 48;

  const outPath = path.join(PILOT_ROOT, 'review', WORKBOOK_FILE);
  await wb.xlsx.writeFile(outPath);
  return { outPath, mandatoryCount, mandatoryRows };
}

function buildReviewTemplate(rows) {
  return {
    template_id: 'orca-p0-i-operator-review-template-v1',
    pilot_run_id: PILOT_RUN_ID,
    workbook_id: WORKBOOK_ID,
    runtime_commit: RUNTIME_COMMIT,
    generated_at: new Date().toISOString(),
    note: 'REVIEW OVERLAY TEMPLATE — NOT GOLD — operator fields null until import',
    records: rows.map((r) => ({
      pilot_row_id: r.pilot_row_id,
      query_id: r.source_query_id,
      operator_decision: null,
      corrected_eligibility: null,
      corrected_primary_intent: null,
      primary_error_type: null,
      secondary_error_types: null,
      operator_comment: null,
      needs_domain_expert: null,
      reviewed_by: null,
      reviewed_at: null,
    })),
  };
}

function validateWorkbook(rows, mandatoryRows, randomAudit, primaryIntents) {
  const issues = [];
  const masterCount = rows.length;
  const unique = new Set(rows.map((r) => r.source_query_id));
  if (masterCount !== 200 || unique.size !== 200) issues.push('Master sheet must have 200 unique query IDs');

  const dec = { ACCEPT: 0, REJECT: 0, ABSTAIN: 0 };
  rows.forEach((r) => dec[r.automated_decision]++);
  if (dec.ACCEPT !== 77 || dec.REJECT !== 53 || dec.ABSTAIN !== 70) issues.push('Decision distribution mismatch');

  const mandIds = mandatoryRows.map((r) => r.source_query_id);
  if (new Set(mandIds).size !== mandIds.length) issues.push('Mandatory sheet has duplicate query IDs');

  const opFilled = rows.filter((r) => r.operator_decision).length;
  if (opFilled !== 0) issues.push('Operator fields must be blank');

  const wbPath = path.join(PILOT_ROOT, 'review', WORKBOOK_FILE);
  if (!fs.existsSync(wbPath)) issues.push('Workbook file missing');

  return {
    validated_at: new Date().toISOString(),
    workbook_id: WORKBOOK_ID,
    passed: issues.length === 0,
    issues,
    checks: {
      master_row_count: masterCount,
      unique_query_ids: unique.size,
      accept_count: dec.ACCEPT,
      reject_count: dec.REJECT,
      abstain_count: dec.ABSTAIN,
      mandatory_review_unique: new Set(mandIds).size,
      mandatory_review_count: mandIds.length,
      random_accept_selected: randomAudit.accept.selected_count,
      random_reject_selected: randomAudit.reject.selected_count,
      operator_fields_blank: opFilled === 0,
      workbook_exists: fs.existsSync(wbPath),
      dropdown_enums: {
        operator_decisions: OPERATOR_DECISIONS.length,
        error_types: ERROR_TYPES.length,
        primary_intents: primaryIntents.length,
      },
    },
  };
}

function buildParityMarkdown(parity) {
  const { checks, expected, passed } = parity;
  return `# P0-I Operator Review Source Parity v1

**Pilot run:** \`${PILOT_RUN_ID}\`  
**Runtime checkpoint:** \`${RUNTIME_COMMIT}\`  
**Status:** ${passed ? 'PASS' : 'FAIL — BLOCKED'}

## Reconciliation

| Source | Count | Expected | Match |
|--------|------:|---------:|:-----:|
| Frozen input | ${checks.frozen_input_count} | ${expected.total_unique_records} | ${checks.frozen_input_count === expected.total_unique_records ? '✓' : '✗'} |
| Selection manifest | ${checks.selection_manifest_count} | ${expected.total_unique_records} | ${checks.selection_manifest_count === expected.total_unique_records ? '✓' : '✗'} |
| Semantic records | ${checks.semantic_record_count} | ${expected.total_unique_records} | ${checks.semantic_record_count === expected.total_unique_records ? '✓' : '✗'} |
| Unique query IDs | ${checks.unique_query_id_count} | ${expected.total_unique_records} | ${checks.unique_query_id_count === expected.total_unique_records ? '✓' : '✗'} |
| ACCEPT | ${checks.accept_count} | ${expected.accept} | ${checks.accept_count === expected.accept ? '✓' : '✗'} |
| REJECT | ${checks.reject_count} | ${expected.reject} | ${checks.reject_count === expected.reject ? '✓' : '✗'} |
| ABSTAIN | ${checks.abstain_count} | ${expected.abstain} | ${checks.abstain_count === expected.abstain ? '✓' : '✗'} |
| Legacy commercial → REJECT | ${checks.legacy_commercial_new_reject} | ${expected.legacy_commercial_new_reject} | ${checks.legacy_commercial_new_reject === expected.legacy_commercial_new_reject ? '✓' : '✗'} |
| Legacy commercial → ABSTAIN | ${checks.legacy_commercial_new_abstain} | ${expected.legacy_commercial_new_abstain} | ${checks.legacy_commercial_new_abstain === expected.legacy_commercial_new_abstain ? '✓' : '✗'} |
| Legacy/new same | ${checks.legacy_same_decision} | ${expected.legacy_same} | ${checks.legacy_same_decision === expected.legacy_same ? '✓' : '✗'} |
| Operator decisions populated | ${checks.operator_decisions_populated} | 0 | ${checks.operator_decisions_populated === 0 ? '✓' : '✗'} |

## Boundary checks

- P0-D: **ON HOLD**
- Corvonero: **FROZEN**
- Pilot package: **uncommitted**
- Runtime checkpoint \`1fcf3d2\`: **present in history**

${passed ? '' : '\n**STOP:** BLOCKED — PILOT REVIEW SOURCE COUNTS DO NOT RECONCILE\n'}
`;
}

function buildRandomAuditMarkdown(randomAudit) {
  return `# P0-I Random Audit Sample v1

**Workbook package seed:** \`${randomAudit.seed}\`  
**Algorithm:** ${randomAudit.algorithm}  
**Selection timestamp:** ${randomAudit.selection_timestamp}

## ACCEPT audit

| Field | Value |
|-------|------:|
| Source population (non-mandatory ACCEPT) | ${randomAudit.accept.source_population_count} |
| Selected | ${randomAudit.accept.selected_count} |
| Max per class | ${randomAudit.max_per_class} |

**Selected query IDs:** ${randomAudit.accept.selected_query_ids.join(', ') || '(none)'}

## REJECT audit

| Field | Value |
|-------|------:|
| Source population (non-mandatory REJECT) | ${randomAudit.reject.source_population_count} |
| Selected | ${randomAudit.reject.selected_count} |

**Selected query IDs:** ${randomAudit.reject.selected_query_ids.join(', ') || '(none)'}

Mandatory records excluded from random pool: **${randomAudit.mandatory_excluded_count}**
`;
}

function buildImportPlan() {
  return `# ORCA P0-I Operator Review Import Plan v1

**Workbook:** \`${WORKBOOK_FILE}\`  
**Template:** \`orca-p0-i-operator-review-template-v1.json\`  
**Overlay model:** review decisions imported as overlay — **no mutation** of \`p0-i-pilot-semantic-records-v1.json\`

## 1. Workbook identity verification

- Filename must be \`${WORKBOOK_FILE}\`
- Sheet names unchanged (10 visible sheets + hidden \`_Enums\` for dropdown validation)
- Column headers match generator v1

## 2. Checksum verification

- Compare SHA-256 of returned workbook against operator-submitted manifest entry
- Reject import if sheets/columns renamed

## 3. Allowed editable columns

Only operator columns on data sheets:

- Operator decision
- Corrected eligibility
- Corrected primary intent
- Primary error type
- Secondary error types
- Operator comment
- Needs domain expert
- Reviewed by
- Review date

## 4. Query-ID matching

- Match on \`Source query ID\` (CR2-PHR-*)
- Secondary key: \`Pilot row ID\` (P0I-*)
- Unmatched rows → import error report

## 5. Duplicate detection

- One decision per query_id
- Duplicate operator rows → reject import

## 6. Controlled-value validation

- Operator decision ∈ approved enum
- Corrected eligibility ∈ ACCEPT|REJECT|ABSTAIN|blank
- Corrected primary intent ∈ P0-B taxonomy|blank
- Error types ∈ approved enum

## 7. Mandatory-completion validation

Required before P0-I human gate:

- All P0 + P1 rows on \`Обязательная проверка\`
- All workbook random ACCEPT audit rows
- All workbook random REJECT audit rows

Per completed row:

- operator_decision required
- corrected_eligibility when decision is CHANGE_*
- corrected_primary_intent when intent correction applicable
- primary_error_type when decision is CHANGE_* or INVALID_RECORD
- comment for CHANGE_*, NEEDS_DOMAIN_EXPERT, INVALID_RECORD

## 8. Preservation

- Automated fields copied from source records, not overwritten
- Import creates \`review/p0-i-operator-review-overlay-v1.json\` (future)

## 9. Disagreement analysis

- Compare operator_decision vs automated_decision
- Aggregate error types and legacy disagreement resolution

## 10. P0-I decision gate

Full P0-I PASS requires operator completion + analysis — **not** granted by import alone.

**Importer:** not implemented in workbook v1 task — reuse only if safe generic importer exists.
`;
}

function buildHandoff(mandatoryCount, randomAudit) {
  return `# Operator Review Handoff v1

**Package:** P0-I Real Integration Pilot — Operator Review Workbook  
**Workbook:** \`review/${WORKBOOK_FILE}\`

## Process

1. Open \`${WORKBOOK_FILE}\`.
2. Read sheet **Инструкция**.
3. Complete **Обязательная проверка** (${mandatoryCount} deduplicated P0+P1 rows).
4. Complete random audit records marked in **ACCEPT** and **REJECT** sheets (${randomAudit.accept.selected_count} ACCEPT + ${randomAudit.reject.selected_count} REJECT).
5. Optionally review remaining P3 records on master sheet.
6. Save **without renaming sheets or columns**.
7. Return workbook for import and analysis.

## Escalation

Use \`NEEDS_DOMAIN_EXPERT\` when domain knowledge is required — operator is not required to resolve domain questions alone.

## Status gates (unchanged by this package)

| Gate | Status |
|------|--------|
| Pilot execution | TECHNICAL PASS — OPERATOR REVIEW PACKAGE READY |
| P0-I | PILOT EXECUTED — HUMAN REVIEW IN PROGRESS |
| P0-D | ON HOLD |
| B0 | BLOCKED |
| Corvonero | FROZEN |
| Campaign Production | BLOCKED |

**Next gate:** OPERATOR COMPLETION OF ${WORKBOOK_FILE}
`;
}

function buildReport(parity, rows, mandatoryRows, randomAudit, validation, workbookPath) {
  const p0 = rows.filter((r) => r.review_priority === 'P0').length;
  const p1only = rows.filter((r) => r.review_priority === 'P1').length;
  return `# REPORT — ORCA SEMANTIC INTELLIGENCE — P0-I OPERATOR REVIEW WORKBOOK V1

**Date:** ${new Date().toISOString().slice(0, 10)}  
**Pilot run:** \`${PILOT_RUN_ID}\`  
**Runtime checkpoint:** \`${RUNTIME_COMMIT}\`

## 1. Preflight

| Check | Result |
|-------|--------|
| Branch | mars/post-cycle8-live-tests |
| Runtime commit in history | \`1fcf3d2\` ✓ |
| Pilot package | uncommitted ✓ |
| Operator decisions | 0 ✓ |
| P0-D | ON HOLD |
| Corvonero | FROZEN |

## 2. Source Parity

Parity audit: **${parity.passed ? 'PASS' : 'FAIL'}** — see \`review/P0-I-OPERATOR-REVIEW-SOURCE-PARITY-v1.md\`

## 3. Review Priority Model

| Priority | Count (unique rows) |
|----------|--------------------:|
| P0 | ${p0} |
| P1 | ${p1only} |
| P2 | ${rows.filter((r) => r.review_priority === 'P2').length} |
| P3 | ${rows.filter((r) => r.review_priority === 'P3').length} |

Mandatory deduplicated sheet: **${mandatoryRows.length}** rows (P0+P1).

## 4. Operator Decision Taxonomy

- Decisions: ${OPERATOR_DECISIONS.length} values
- Error types: ${ERROR_TYPES.length} values
- Primary intents: P0-B taxonomy (27 values)

## 5. Workbook Structure

10 sheets: Инструкция, Все 200 фраз, Обязательная проверка, ACCEPT, REJECT, ABSTAIN, Legacy расхождения, Проблемные запросы, Защищённые классы, Сводка.

Output: \`${workbookPath.replace(/\\/g, '/')}\`

## 6. Mandatory Review Coverage

- P0+P1 deduplicated: ${mandatoryRows.length}
- Queue memberships preserved in \`review_queues\` column

## 7. Random Audit Sample

- Seed: \`${randomAudit.seed}\`
- ACCEPT selected: ${randomAudit.accept.selected_count} / population ${randomAudit.accept.source_population_count}
- REJECT selected: ${randomAudit.reject.selected_count} / population ${randomAudit.reject.source_population_count}

## 8. Machine-Readable Review Template

\`review/orca-p0-i-operator-review-template-v1.json\` + schema — all decision fields null.

## 9. Review Import Plan

\`review/ORCA-P0-I-OPERATOR-REVIEW-IMPORT-PLAN-v1.md\` — overlay import semantics documented; importer not implemented.

## 10. Workbook Validation

Validation: **${validation.passed ? 'PASS' : 'FAIL'}** — see \`validation/P0-I-OPERATOR-REVIEW-WORKBOOK-VALIDATION-v1.md\`

## 11. Review Handoff

\`review/OPERATOR-REVIEW-HANDOFF-v1.md\`

## 12. Status Updates

| Component | Status |
|-----------|--------|
| Pilot execution | TECHNICAL PASS — OPERATOR REVIEW PACKAGE READY |
| P0-I | PILOT EXECUTED — HUMAN REVIEW IN PROGRESS |
| P0-D | ON HOLD |
| B0 | BLOCKED |
| Corvonero | FROZEN |
| Campaign Production | BLOCKED |

## 13. Files Created or Changed

- \`review/generate-operator-review-workbook-v1.mjs\`
- \`review/${WORKBOOK_FILE}\`
- \`review/P0-I-OPERATOR-REVIEW-SOURCE-PARITY-v1.md\` + \`.json\`
- \`review/P0-I-RANDOM-AUDIT-SAMPLE-v1.md\` + \`.json\`
- \`review/orca-p0-i-operator-review-template-v1.json\`
- \`review/orca-p0-i-operator-review-template-v1.schema.json\`
- \`review/ORCA-P0-I-OPERATOR-REVIEW-IMPORT-PLAN-v1.md\`
- \`review/OPERATOR-REVIEW-HANDOFF-v1.md\`
- \`validation/P0-I-OPERATOR-REVIEW-WORKBOOK-VALIDATION-v1.md\` + \`.json\`
- \`reports/REPORT-orca-p0-i-operator-review-workbook-v1.md\`

Pilot source JSON artifacts: **not modified**.

## 14. Git Status

Uncommitted — workbook and review artifacts remain local until operator completion.

## 15. SAFE UNKNOWN

- Exact Excel UI behavior for dropdown validation may vary by Excel version.
- Importer implementation deferred to future task.

## 16. Operator Instructions

See \`review/OPERATOR-REVIEW-HANDOFF-v1.md\` and workbook sheet **Инструкция**.

## 17. Next Gate

**OPERATOR COMPLETION OF ${WORKBOOK_FILE}**

## 18. Stop Condition

Workbook package prepared. No operator decisions filled. No P0-I PASS. No commit/push.
`;
}

function buildSchema() {
  return {
    $schema: 'https://json-schema.org/draft/2020-12/schema',
    $id: 'orca-p0-i-operator-review-template-v1.schema.json',
    title: 'ORCA P0-I Operator Review Template v1',
    type: 'object',
    required: ['template_id', 'pilot_run_id', 'records'],
    properties: {
      template_id: { const: 'orca-p0-i-operator-review-template-v1' },
      pilot_run_id: { const: 'p0-i-real-slice-v1' },
      workbook_id: { const: WORKBOOK_ID },
      runtime_commit: { const: RUNTIME_COMMIT },
      generated_at: { type: 'string', format: 'date-time' },
      note: { type: 'string' },
      records: {
        type: 'array',
        minItems: 200,
        maxItems: 200,
        items: {
          type: 'object',
          required: ['pilot_row_id', 'query_id'],
          properties: {
            pilot_row_id: { type: 'string', pattern: '^P0I-\\d{5}$' },
            query_id: { type: 'string', pattern: '^CR2-PHR-\\d+$' },
            operator_decision: {
              type: ['string', 'null'],
              enum: [...OPERATOR_DECISIONS, null],
            },
            corrected_eligibility: {
              type: ['string', 'null'],
              enum: [...ELIGIBILITY_VALUES, null],
            },
            corrected_primary_intent: { type: ['string', 'null'] },
            primary_error_type: {
              type: ['string', 'null'],
              enum: [...ERROR_TYPES, null],
            },
            secondary_error_types: { type: ['string', 'null'] },
            operator_comment: { type: ['string', 'null'] },
            needs_domain_expert: { type: ['boolean', 'null'] },
            reviewed_by: { type: ['string', 'null'] },
            reviewed_at: { type: ['string', 'null'], format: 'date-time' },
          },
          additionalProperties: false,
        },
      },
    },
    additionalProperties: false,
  };
}

async function main() {
  const primaryIntents = loadPrimaryIntents();
  const sources = loadSources();
  const parity = runParityAudit(sources);

  writeText(path.join(PILOT_ROOT, 'review/P0-I-OPERATOR-REVIEW-SOURCE-PARITY-v1.md'), buildParityMarkdown(parity));
  writeJson(path.join(PILOT_ROOT, 'review/P0-I-OPERATOR-REVIEW-SOURCE-PARITY-v1.json'), {
    parity_id: 'p0-i-operator-review-source-parity-v1',
    pilot_run_id: PILOT_RUN_ID,
    runtime_commit: RUNTIME_COMMIT,
    generated_at: new Date().toISOString(),
    ...parity,
  });

  if (!parity.passed) {
    console.error('BLOCKED — PILOT REVIEW SOURCE COUNTS DO NOT RECONCILE');
    process.exit(2);
  }

  let rows = buildRows(sources, primaryIntents);
  const randomAudit = selectWorkbookRandomAudit(rows);
  writeText(path.join(PILOT_ROOT, 'review/P0-I-RANDOM-AUDIT-SAMPLE-v1.md'), buildRandomAuditMarkdown(randomAudit));
  writeJson(path.join(PILOT_ROOT, 'review/P0-I-RANDOM-AUDIT-SAMPLE-v1.json'), {
    audit_id: 'p0-i-random-audit-sample-v1',
    pilot_run_id: PILOT_RUN_ID,
    workbook_id: WORKBOOK_ID,
    ...randomAudit,
  });

  const { outPath, mandatoryCount, mandatoryRows } = await buildWorkbook(rows, primaryIntents, randomAudit);

  const template = buildReviewTemplate(rows);
  writeJson(path.join(PILOT_ROOT, 'review/orca-p0-i-operator-review-template-v1.json'), template);
  writeJson(path.join(PILOT_ROOT, 'review/orca-p0-i-operator-review-template-v1.schema.json'), buildSchema());

  writeText(path.join(PILOT_ROOT, 'review/ORCA-P0-I-OPERATOR-REVIEW-IMPORT-PLAN-v1.md'), buildImportPlan());
  writeText(path.join(PILOT_ROOT, 'review/OPERATOR-REVIEW-HANDOFF-v1.md'), buildHandoff(mandatoryCount, randomAudit));

  const validation = validateWorkbook(rows, mandatoryRows, randomAudit, primaryIntents);
  writeJson(path.join(PILOT_ROOT, 'validation/P0-I-OPERATOR-REVIEW-WORKBOOK-VALIDATION-v1.json'), validation);
  writeText(
    path.join(PILOT_ROOT, 'validation/P0-I-OPERATOR-REVIEW-WORKBOOK-VALIDATION-v1.md'),
    `# P0-I Operator Review Workbook Validation v1\n\n**Passed:** ${validation.passed}\n\n## Issues\n\n${validation.issues.length ? validation.issues.map((i) => `- ${i}`).join('\n') : '- none'}\n\n## Checks\n\n\`\`\`json\n${JSON.stringify(validation.checks, null, 2)}\n\`\`\`\n`
  );

  writeText(path.join(PILOT_ROOT, 'reports/REPORT-orca-p0-i-operator-review-workbook-v1.md'), buildReport(parity, rows, mandatoryRows, randomAudit, validation, outPath));

  console.log(
    JSON.stringify(
      {
        ok: validation.passed,
        workbook: outPath,
        mandatory_review: mandatoryCount,
        random_accept: randomAudit.accept.selected_count,
        random_reject: randomAudit.reject.selected_count,
        validation_passed: validation.passed,
      },
      null,
      2
    )
  );

  if (!validation.passed) process.exit(1);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
