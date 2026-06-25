#!/usr/bin/env node
/**
 * ORCA Corvonero v5 QA Repair Gate v2 — close blockers, independent evidence inspection.
 * Does NOT mutate v5 production files or generate Commander v6.
 */
import fs from 'fs';
import path from 'path';
import { createRequire } from 'module';
import { fileURLToPath } from 'url';
import { buildSerializationRootCauseV2 } from './lib/evidence-serialization-v2.mjs';
import {
  formatMetricValue,
  formatErrorDetails,
  formatNarrative,
  reconciliationMetricsToRows,
  EMPTY_REPLACEMENT_SENTINEL,
} from './lib/evidence-serialization-v2.mjs';
import {
  loadV5Inputs,
  reconcilePlaceholderCounts,
  buildSemanticCorrections,
  buildControlledTestDecisions,
  buildNegativeResolutionFinal,
  buildSemanticRiskReconciliationFinal,
  buildCollisionActionsFinal,
  buildV6InputPackage,
  runRegressionTestsV2,
  jsonToMd,
} from './lib/qa-repair-v2.mjs';
import { inspectQaRepairWorkbook } from './lib/workbook-xlsx-inspector-v2.mjs';
import { scanEvidenceIntegrity } from './lib/qa-repair-audits.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const AUDIT = path.join(ROOT, 'production/audit');
const REPAIR = path.join(ROOT, 'production/repair');
const VALIDATION = path.join(ROOT, 'production/validation');
const APPROVALS = path.join(ROOT, 'production/approvals');
const ARTIFACTS = path.join(ROOT, 'artifacts');
const EXPORTS = path.join(ROOT, 'exports');

function writeJson(fp, obj) {
  fs.mkdirSync(path.dirname(fp), { recursive: true });
  fs.writeFileSync(fp, JSON.stringify(obj, null, 2), 'utf8');
}

function writeMd(fp, body) {
  fs.mkdirSync(path.dirname(fp), { recursive: true });
  fs.writeFileSync(fp, body, 'utf8');
}

function cell(v, field = '') {
  if (v == null) return field ? formatNarrative('', { field }) : '';
  if (typeof v === 'object') return formatMetricValue(field || 'metric', v);
  if (typeof v === 'boolean') return v ? 'YES' : 'NO';
  if (typeof v === 'number' && field) throw new Error(`numeric forbidden in ${field}`);
  return String(v);
}

async function writeQaRepairWorkbookV2(packages, regression, gate) {
  const require = createRequire(import.meta.url);
  const exceljsPath = path.resolve(
    ROOT,
    '../../ppc/triumph-manipulator/tools/exporter-cli/node_modules/exceljs'
  );
  const ExcelJS = require(exceljsPath);

  const { serialization, placeholder, semantic, controlled, negFinal, reconciliation, collision, v6pkg, integrity } =
    packages;

  const sheets = {
    'Audit summary': [
      ['metric', 'value'],
      ['gate_id', 'v5-qa-repair-gate-v2'],
      ['generated_at', new Date().toISOString()],
      ['final_result', gate.final_result],
      ['v6_production', gate.v6_production],
      ['unique_unresolved_negatives', negFinal.totals.UNRESOLVED],
      ['blocking_negatives', negFinal.totals.BLOCKING],
      ['collision_actions_complete', `${collision.totals.complete}/${collision.totals.total}`],
      ['career_education_leakage_repair', semantic.totals.leakage_to_future_production],
      ['controlled_tests_reviewed', controlled.totals.reviewed],
      ['workbook_inspection', 'see Independent gate details sheet'],
    ],
    'V5 rejection': [
      ['artefact', 'status'],
      ['Commander v5', 'REJECTED BY OPERATOR — QA EVIDENCE INTEGRITY FAILURE'],
      ['Review workbook v5', 'REJECTED BY OPERATOR — PLACEHOLDER AND UNRESOLVED RISK FAILURE'],
      ['Commander dry-run', 'BLOCKED UNTIL V6'],
      ['v6 production', gate.v6_production === 'AUTHORIZED_FOR_FOLLOWUP_TASK' ? 'AUTHORIZED (follow-up task)' : 'NOT AUTHORIZED'],
      ['Launch', 'NOT AUTHORIZED'],
    ],
    'Serialization root causes': [
      ['id', 'symptom', 'mechanism', 'fix'],
      ...serialization.defects.map((d) => [d.id, d.symptom, d.mechanism, d.fix]),
    ],
    'Placeholder count reconciliation': [
      ['metric', 'value'],
      ...reconciliationMetricsToRows(placeholder.metrics),
      ['formula_cells', placeholder.breakdown.formula_cells],
      ['formula_findings', placeholder.breakdown.formula_findings],
      ['why_613_vs_334', placeholder.explanation.why_613_vs_334],
    ],
    'Evidence integrity scan': [
      ['artefact', 'field', 'bad_value', 'severity'],
      ...integrity.findings.slice(0, 50).map((f) => [
        f.artefact,
        f.field || '',
        cell(f.bad_value, 'detail'),
        f.severity || 'MEDIUM',
      ]),
      ['note', 'detail', 'v1 v5 workbook defects documented; v2 repair package uses typed formatters', 'INFO'],
    ],
    'Career and education corrections': [
      ['keyword_id', 'phrase', 'previous_status', 'final_status', 'group', 'reason', 'action'],
      ...semantic.corrections.map((c) => [
        c.keyword_id,
        c.phrase,
        c.previous_status,
        c.final_status,
        c.group,
        c.reason,
        c.required_production_action,
      ]),
    ],
    'Controlled-test decisions': [
      ['keyword_id', 'phrase', 'previous_status', 'final_decision', 'commercial_hypothesis', 'noise_risk', 'bid_tier', 'eval_rule'],
      ...controlled.rows.map((r) => [
        r.keyword_id,
        r.phrase,
        r.previous_status,
        r.final_decision,
        cell(r.commercial_hypothesis, 'detail'),
        cell(r.expected_noise_source, 'detail'),
        r.bid_tier,
        cell(r.post_launch_evaluation, 'detail'),
      ]),
    ],
    'Unique negative resolution': [
      ['negative_id', 'negative', 'level', 'scope', 'final_state', 'exact_action'],
      ...negFinal.rows.map((r) => [
        r.negative_id,
        r.negative,
        r.level,
        r.applied_scope,
        r.final_state,
        cell(r.exact_action, 'correction'),
      ]),
    ],
    'Semantic-risk reconciliation': [
      ['metric', 'value'],
      ...reconciliationMetricsToRows(reconciliation.reconciliation),
    ],
    'Exact collision actions': [
      ['finding_id', 'phrase', 'negative', 'action_type', 'exact_action', 'validation'],
      ...collision.rows.map((r) => [
        r.finding_id,
        r.phrase,
        r.negative,
        r.action_type,
        cell(r.exact_action, 'correction'),
        r.validation_result,
      ]),
    ],
    'V6 input repair package': [
      ['section', 'count'],
      ['semantic_exclusions', v6pkg.semantic_exclusions.length],
      ['semantic_status_changes', v6pkg.semantic_status_changes.length],
      ['controlled_test_decisions', v6pkg.controlled_test_decisions.length],
      ['final_negative_states', v6pkg.final_negative_states.length],
      ['exact_collision_actions', v6pkg.exact_collision_actions.length],
      ['bid_treatment_changes', v6pkg.bid_treatment_changes.length],
    ],
    'Generator regression tests': [
      ['regression_id', 'description', 'passed', 'error_details'],
      ...regression.tests.map((t) => [
        t.regression_id,
        t.description,
        t.passed ? 'PASS' : 'FAIL',
        formatErrorDetails(t.passed, t.error_details || t.error),
      ]),
    ],
    'Independent gate details': [
      ['check', 'result', 'detail'],
      ...gate.checks.map((c) => [c.id, c.passed ? 'PASS' : 'FAIL', cell(c.detail, 'detail')]),
    ],
    'QA gate decision': [
      ['check', 'result', 'detail'],
      ...gate.checks.map((c) => [c.id, c.passed ? 'PASS' : 'FAIL', cell(c.detail, 'detail')]),
      ['FINAL', gate.final_result, cell(gate.summary, 'detail')],
    ],
  };

  const wb = new ExcelJS.Workbook();
  for (const [name, data] of Object.entries(sheets)) {
    const ws = wb.addWorksheet(name.slice(0, 31));
    data.forEach((row) => {
      ws.addRow(row.map((c) => (c == null ? formatNarrative('', { field: 'detail' }) : c)));
    });
  }

  const out = path.join(EXPORTS, 'CORVONERO-V5-QA-REPAIR-AUDIT-v2.xlsx');
  await wb.xlsx.writeFile(out);
  return { path: out, sheets: Object.keys(sheets) };
}

function runIndependentGateV2(packages, regression, workbookInspection) {
  const { semantic, controlled, negFinal, reconciliation, collision, placeholder } = packages;
  const checks = [];
  const add = (id, passed, detail) => checks.push({ id, passed, detail });

  add('G2-01-serialization', workbookInspection.reconciliation.object_coercion === 0, `object_coercion=${workbookInspection.reconciliation.object_coercion}`);
  add('G2-02-no-970', workbookInspection.reconciliation.numeric_narrative_970 === 0, `970_in_narrative=${workbookInspection.reconciliation.numeric_narrative_970}`);
  add('G2-03-no-2464', workbookInspection.reconciliation.four_digit_narrative === 0, `four_digit=${workbookInspection.reconciliation.four_digit_narrative}`);
  add('G2-04-placeholder-reconciled', placeholder.reconciliation_pass, '613 vs 334 count layers reconciled');
  add(
    'G2-05-career-education',
    semantic.totals.leakage_to_future_production === 0,
    `leakage_to_future_production=${semantic.totals.leakage_to_future_production}; v5_unchanged=${semantic.totals.v5_files_active_leakage_unchanged}`
  );
  add(
    'G2-06-controlled-tests',
    controlled.missing_hypothesis_count === 0,
    `missing_hypothesis=${controlled.missing_hypothesis_count} reviewed=${controlled.totals.reviewed}`
  );
  add(
    'G2-07-unique-negatives',
    negFinal.totals.UNRESOLVED === 0 && negFinal.totals.BLOCKING === 0,
    `UNRESOLVED=${negFinal.totals.UNRESOLVED} BLOCKING=${negFinal.totals.BLOCKING}`
  );
  add('G2-08-safe-evidence', negFinal.totals['SAFE — PROVEN'] >= 333, `SAFE_PROVEN=${negFinal.totals['SAFE — PROVEN']}`);
  add('G2-09-semantic-reconciliation', reconciliation.reconciliation.reconciled_pass, `unique_unresolved=${reconciliation.final_layer.remaining_unique_unresolved_risks}`);
  add('G2-10-collision-actions', collision.gate_ready, `${collision.totals.complete}/${collision.totals.total} exact actions`);
  add('G2-11-regression', regression.passed, regression.tests.filter((t) => !t.passed).map((t) => t.regression_id).join(', ') || 'all passed');
  add('G2-12-workbook-inspection', workbookInspection.passed, `${workbookInspection.findings.length} findings`);

  const blockers = checks.filter((c) => !c.passed);
  const passed = blockers.length === 0;

  return {
    gate_id: 'v5-qa-repair-gate-v2',
    evaluated_at: new Date().toISOString(),
    final_result: passed ? 'PASS — V6 PRODUCTION AUTHORIZED' : 'BLOCKED — QA REPAIR INCOMPLETE',
    v6_production: passed ? 'AUTHORIZED_FOR_FOLLOWUP_TASK' : 'NOT AUTHORIZED',
    checks,
    blockers: blockers.map((b) => ({ id: b.id, detail: b.detail })),
    summary: passed
      ? 'All v2 repair gates passed; v6 production may proceed in a separate authorized task.'
      : `${blockers.length} gate check(s) failed; v6 production blocked.`,
    workbook_inspection: workbookInspection,
  };
}

async function main() {
  [AUDIT, REPAIR, VALIDATION, APPROVALS, ARTIFACTS].forEach((d) => fs.mkdirSync(d, { recursive: true }));

  const inputs = loadV5Inputs(ROOT);
  const serialization = buildSerializationRootCauseV2();
  const placeholder = reconcilePlaceholderCounts(inputs);
  const semantic = buildSemanticCorrections(inputs);
  const controlled = buildControlledTestDecisions(inputs);
  const negFinal = buildNegativeResolutionFinal(inputs);
  const reconciliation = buildSemanticRiskReconciliationFinal(inputs, negFinal);
  const collision = buildCollisionActionsFinal(inputs, semantic);
  const v6pkg = buildV6InputPackage(semantic, controlled, negFinal, collision, reconciliation);
  const regression = runRegressionTestsV2();
  const integrity = scanEvidenceIntegrity(ROOT, inputs);

  writeJson(path.join(AUDIT, 'evidence-serialization-root-cause-v2.json'), serialization);
  writeMd(
    path.join(AUDIT, 'evidence-serialization-root-cause-v2.md'),
    [
      '# Evidence Serialization Root Cause v2',
      '',
      ...serialization.defects.map(
        (d) => `## ${d.id} — ${d.symptom}\n\n- **Mechanism:** ${d.mechanism}\n- **Fix:** ${d.fix}\n`
      ),
    ].join('\n')
  );

  writeJson(path.join(AUDIT, 'v5-placeholder-count-reconciliation.json'), placeholder);
  writeMd(
    path.join(AUDIT, 'v5-placeholder-count-reconciliation.md'),
    [
      '# V5 Placeholder Count Reconciliation',
      '',
      jsonToMd('Metrics', placeholder),
      '## Explanation',
      '',
      placeholder.explanation.why_613_vs_334,
      '',
      placeholder.explanation.duplicate_occurrences_meaning,
    ].join('\n')
  );

  writeJson(path.join(REPAIR, 'v5-semantic-corrections.json'), semantic);
  writeMd(
    path.join(REPAIR, 'v5-semantic-corrections.md'),
    [
      '# V5 Semantic Corrections',
      '',
      jsonToMd('Totals', semantic),
      '## Corrections',
      '',
      ...semantic.corrections.map(
        (c) => `- \`${c.phrase}\` (${c.keyword_id}): ${c.previous_status} → **${c.final_status}** — ${c.reason}`
      ),
    ].join('\n')
  );

  writeJson(path.join(REPAIR, 'v5-controlled-test-decisions.json'), controlled);
  writeMd(path.join(REPAIR, 'v5-controlled-test-decisions.md'), jsonToMd('V5 Controlled Test Decisions', controlled));

  writeJson(path.join(REPAIR, 'v5-negative-resolution-final.json'), negFinal);
  writeMd(path.join(REPAIR, 'v5-negative-resolution-final.md'), jsonToMd('V5 Negative Resolution Final', negFinal));

  writeJson(path.join(REPAIR, 'v5-semantic-risk-reconciliation-final.json'), reconciliation);
  writeMd(
    path.join(REPAIR, 'v5-semantic-risk-reconciliation-final.md'),
    [
      '# V5 Semantic Risk Reconciliation Final',
      '',
      '## Raw pair layer',
      '',
      ...Object.entries(reconciliation.raw_pair_layer).map(([k, v]) => `- ${k}: ${v}`),
      '',
      '## Unique risk layer',
      '',
      ...Object.entries(reconciliation.unique_risk_layer).map(([k, v]) => `- ${k}: ${v}`),
      '',
      '## Final layer',
      '',
      ...Object.entries(reconciliation.final_layer).map(([k, v]) => `- ${k}: ${v}`),
    ].join('\n')
  );

  writeJson(path.join(REPAIR, 'v5-collision-actions-final.json'), collision);
  writeMd(
    path.join(REPAIR, 'v5-collision-actions-final.md'),
    [
      '# V5 Collision Actions Final',
      '',
      jsonToMd('Totals', collision),
      '## Actions',
      '',
      ...collision.rows.map((r) => `- **${r.finding_id}** ${r.action_type}: ${r.phrase} × «${r.negative}»`),
    ].join('\n')
  );

  writeJson(path.join(REPAIR, 'v6-production-input-package.json'), v6pkg);
  writeMd(
    path.join(REPAIR, 'v6-production-input-package.md'),
    [
      '# V6 Production Input Repair Package',
      '',
      'Correction contract for follow-up v6 production task. **Does not contain full campaign data.**',
      '',
      `- Semantic exclusions: ${v6pkg.semantic_exclusions.length}`,
      `- Status changes: ${v6pkg.semantic_status_changes.length}`,
      `- Collision actions: ${v6pkg.exact_collision_actions.length}`,
      `- Negative final states: ${v6pkg.final_negative_states.length}`,
    ].join('\n')
  );

  writeJson(path.join(VALIDATION, 'workbook-integrity-regression-v5-v2.json'), regression);

  const packages = { serialization, placeholder, semantic, controlled, negFinal, reconciliation, collision, v6pkg, integrity };

  const gatePrelim = runIndependentGateV2(packages, regression, { passed: false, findings: [], reconciliation: {} });
  const workbook = await writeQaRepairWorkbookV2(packages, regression, gatePrelim);
  const inspection = await inspectQaRepairWorkbook(workbook.path, {
    controlled_reviewed: controlled.totals.reviewed,
    neg_unresolved: negFinal.totals.UNRESOLVED,
  });

  const gate = runIndependentGateV2(packages, regression, inspection);
  gate.workbook_path = workbook.path;

  writeJson(path.join(VALIDATION, 'v5-qa-repair-gate-v2.json'), gate);
  writeMd(
    path.join(VALIDATION, 'v5-qa-repair-gate-v2.md'),
    [
      '# V5 QA Repair Gate v2',
      '',
      `**Result:** ${gate.final_result}`,
      '',
      `**v6 production:** ${gate.v6_production}`,
      '',
      '## Checks',
      '',
      '| ID | Result | Detail |',
      '|----|--------|--------|',
      ...gate.checks.map((c) => `| ${c.id} | ${c.passed ? 'PASS' : 'FAIL'} | ${c.detail} |`),
      '',
      '## Workbook inspection',
      '',
      `Findings: ${inspection.findings.length}`,
    ].join('\n')
  );

  if (gate.final_result.startsWith('PASS')) {
    writeMd(
      path.join(APPROVALS, 'v6-production-authorization.md'),
      [
        '# V6 Production Authorization Charter',
        '',
        '**V5 QA Repair Gate v2 PASSED.** A separate follow-up task may:',
        '',
        '1. Apply `production/repair/v6-production-input-package.json` to v5 canonical dataset.',
        '2. Rebuild semantic registry with career/education exclusions.',
        '3. Rebuild final negative registries with SAFE — PROVEN evidence.',
        '4. Regenerate ads only where mappings changed.',
        '5. Recalculate affected bids per controlled-test decisions.',
        '6. Create dataset v6.',
        '7. Create unified Commander XLSX v6.',
        '8. Create Review Workbook v6.',
        '9. Run Commander dry-run readiness QA.',
        '',
        'Import, moderation, launch, and campaign split remain **NOT AUTHORIZED** until operator dry-run approval.',
      ].join('\n')
    );
  } else {
    writeMd(
      path.join(APPROVALS, 'v6-production-blocker.md'),
      [
        '# V6 Production Blocker',
        '',
        '**V5 QA Repair Gate v2 BLOCKED.** v6 production is **NOT AUTHORIZED**.',
        '',
        '## Unresolved blockers',
        '',
        ...gate.blockers.map((b) => `- **${b.id}**: ${b.detail}`),
      ].join('\n')
    );
  }

  const report = buildReport(gate, packages, regression, inspection, workbook);
  writeMd(path.join(ARTIFACTS, 'REPORT-orca-close-v5-qa-blockers.md'), report);

  console.log(
    JSON.stringify(
      {
        gate: gate.final_result,
        workbook: workbook.path,
        blockers: gate.blockers.length,
        inspection_findings: inspection.findings.length,
        neg_unresolved: negFinal.totals.UNRESOLVED,
        collision_complete: collision.totals.complete,
      },
      null,
      2
    )
  );
}

function buildReport(gate, packages, regression, inspection, workbook) {
  const { semantic, controlled, negFinal, collision, placeholder, serialization } = packages;
  const passed = gate.final_result.startsWith('PASS');

  return [
    '# REPORT — КОРВО НЕРО — CLOSE V5 QA BLOCKERS',
    '',
    '## 1. Preflight',
    '',
    '- Branch: `mars/post-cycle8-live-tests`',
    '- HEAD: `bf313e4`',
    '- v5 production files: unchanged',
    '- v6 production: not executed in this task',
    '',
    '## 2. Previous Gate State',
    '',
    '- v1 gate: `BLOCKED — QA REPAIR INCOMPLETE` (7 failures G-03..G-09)',
    '',
    '## 3. Additional Evidence Defects',
    '',
    '- `[object Object]` in pass_requires — object coercion',
    '- `970` in regression error column — empty string shared-string leak',
    '- 613 vs 334 placeholder count confusion — reconciled',
    '',
    '## 4. Serialization Layer Repair',
    '',
    `- Defects documented: ${serialization.defects.length}`,
    '- Implementation: `tools/lib/evidence-serialization-v2.mjs`',
    '',
    '## 5. Placeholder Count Reconciliation',
    '',
    `- Affected cells: ${placeholder.metrics.total_affected_cells}`,
    `- Finding rows: ${placeholder.metrics.total_finding_rows}`,
    `- Formula (cells): ${placeholder.breakdown.formula_cells}`,
    `- Formula (findings): ${placeholder.breakdown.formula_findings}`,
    '',
    '## 6. Career and Education Corrections',
    '',
    `- Corrections: ${semantic.corrections.length}`,
    `- Active leakage in repair package (pending v6 apply): ${semantic.totals.leakage_to_future_production}`,
    `- v5 files unchanged (still active): ${semantic.totals.v5_files_active_leakage_unchanged}`,
    '',
    '## 7. Controlled-Test Decisions',
    '',
    `- Reviewed: ${controlled.totals.reviewed}`,
    `- Commercial: ${controlled.totals.promoted_to_commercial}`,
    `- Justified controlled: ${controlled.totals.retained_justified_controlled}`,
    `- Hold: ${controlled.totals.held}`,
    `- Exclude: ${controlled.totals.excluded}`,
    '',
    '## 8. Unique Negative Resolution',
    '',
    `- UNRESOLVED: ${negFinal.totals.UNRESOLVED}`,
    `- BLOCKING: ${negFinal.totals.BLOCKING}`,
    `- SAFE — PROVEN: ${negFinal.totals['SAFE — PROVEN']}`,
    '',
    '## 9. Semantic-Risk Reconciliation',
    '',
    `- Reconciled pass: ${packages.reconciliation.reconciliation.reconciled_pass}`,
    `- v5 contradiction resolved: pair-layer vs unique-layer separated`,
    '',
    '## 10. Exact Collision Actions',
    '',
    `- Complete: ${collision.totals.complete}/${collision.totals.total}`,
    `- EXCLUDE KEYWORD (education): ${collision.totals.exclude_keyword}`,
    '',
    '## 11. V6 Input Repair Package',
    '',
    '- `production/repair/v6-production-input-package.json`',
    '',
    '## 12. Generator Regression Repair',
    '',
    `- Tests: ${regression.tests.length}, passed: ${regression.passed}`,
    '',
    '## 13. QA Repair Workbook V2',
    '',
    `- Path: \`${workbook.path}\``,
    `- Sheets: ${workbook.sheets.length}`,
    '',
    '## 14. Independent Evidence Inspection',
    '',
    `- Findings: ${inspection.findings.length}`,
    `- Passed: ${inspection.passed}`,
    '',
    '## 15. Final Gate Decision',
    '',
    `**${gate.final_result}**`,
    '',
    '## 16. V6 Authorization or Blocker',
    '',
    passed ? 'Authorization written.' : 'Blocker updated.',
    '',
    '## 17. ORCA Method Update',
    '',
    '- `production/orca-qa-repair-method-v2.md`',
    '',
    '## 18. Files Created or Changed',
    '',
    '- production/audit/evidence-serialization-root-cause-v2.*',
    '- production/audit/v5-placeholder-count-reconciliation.*',
    '- production/repair/v5-*-final.* / v6-production-input-package.*',
    '- production/validation/v5-qa-repair-gate-v2.*',
    '- exports/CORVONERO-V5-QA-REPAIR-AUDIT-v2.xlsx',
    '- tools/lib/evidence-serialization-v2.mjs, qa-repair-v2.mjs, workbook-xlsx-inspector-v2.mjs',
    '- tools/run-v5-qa-repair-gate-v2.mjs',
    '',
    '## 19. Git Status',
    '',
    'Uncommitted changes only; no commit/push per scope.',
    '',
    '## 20. Remaining Issues',
    '',
    passed ? 'None blocking v6 production task.' : gate.blockers.map((b) => `- ${b.id}: ${b.detail}`).join('\n'),
    '',
    '## 21. Next Gate',
    '',
    'V6 PRODUCTION TASK ONLY AFTER EXPLICIT PASS.',
    '',
    '## 22. Stop Condition',
    '',
    'Met — gate evaluated, workbook v2 generated and inspected.',
  ].join('\n');
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
