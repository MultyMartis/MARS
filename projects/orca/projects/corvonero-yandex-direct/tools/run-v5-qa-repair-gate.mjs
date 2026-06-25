#!/usr/bin/env node
/**
 * ORCA Corvonero v5 QA Repair Gate — independent evidence audit package.
 * Does NOT mutate v5 production files or generate Commander v6.
 */
import fs from 'fs';
import path from 'path';
import { createRequire } from 'module';
import { fileURLToPath } from 'url';
import {
  loadV5Inputs,
  auditPlaceholderRootCause,
  scanEvidenceIntegrity,
  auditCareerEducationQueries,
  auditControlledTests,
  auditUniqueNegativeRisks,
  reconcileSemanticRisks,
  auditExactCollisionCorrections,
  jsonToMd,
} from './lib/qa-repair-audits.mjs';
import { runWorkbookIntegrityRegressionTests } from './lib/workbook-integrity-v5.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const AUDIT = path.join(ROOT, 'production/audit');
const VALIDATION = path.join(ROOT, 'production/validation');
const APPROVALS = path.join(ROOT, 'production/approvals');
const EXPORTS = path.join(ROOT, 'exports');

function writeJson(fp, obj) {
  fs.mkdirSync(path.dirname(fp), { recursive: true });
  fs.writeFileSync(fp, JSON.stringify(obj, null, 2), 'utf8');
}

function writeMd(fp, body) {
  fs.mkdirSync(path.dirname(fp), { recursive: true });
  fs.writeFileSync(fp, body, 'utf8');
}

async function writeQaRepairWorkbook(audits, regression, gate) {
  const require = createRequire(import.meta.url);
  const exceljsPath = path.resolve(
    ROOT,
    '../../ppc/triumph-manipulator/tools/exporter-cli/node_modules/exceljs'
  );
  const ExcelJS = require(exceljsPath);

  const sheets = {
    'Audit summary': [
      ['metric', 'value'],
      ['gate_id', 'v5-qa-repair-gate'],
      ['generated_at', new Date().toISOString()],
      ['final_result', gate.final_result],
      ['v6_production', gate.v6_production],
      ['placeholder_findings', audits.integrity.summary.critical],
      ['career_education_leakage', audits.career.active_leakage_count],
      ['unique_unresolved_negatives', audits.uniqueNegative.totals.unresolved],
      ['blocking_collisions_invalid_corrections', audits.collisionCorrections.invalid_or_generic],
      ['workbook_regression_passed', regression.passed],
    ],
    'V5 rejection': [
      ['artefact', 'status'],
      ['Commander v5', 'REJECTED BY OPERATOR — QA EVIDENCE INTEGRITY FAILURE'],
      ['Review workbook v5', 'REJECTED BY OPERATOR — PLACEHOLDER AND UNRESOLVED RISK FAILURE'],
      ['Commander dry-run', 'BLOCKED'],
      ['v6 production', 'NOT AUTHORIZED'],
      ['Launch', 'NOT AUTHORIZED'],
    ],
    'Placeholder findings': [
      ['artefact', 'field', 'bad_value', 'severity', 'entity_id'],
      ...audits.integrity.findings
        .filter((f) => f.bad_value?.includes('2464') || f.severity === 'CRITICAL')
        .slice(0, 500)
        .map((f) => [f.artefact, f.field, f.bad_value, f.severity, f.entity_id || '']),
    ],
    'Placeholder root causes': [
      ['source_file', 'function', 'field', 'defect', 'correction'],
      [
        audits.placeholder.root_cause.source_file,
        audits.placeholder.root_cause.function,
        audits.placeholder.root_cause.field,
        audits.placeholder.root_cause.exact_defect,
        audits.placeholder.root_cause.reusable_correction,
      ],
    ],
    'Career and education audit': [
      ['phrase', 'group', 'v5_decision', 'corrected', 'action', 'reason'],
      ...audits.career.rows.map((r) => [
        r.phrase,
        r.current_group,
        r.current_v5_decision,
        r.corrected_decision,
        r.required_downstream_action,
        r.reason,
      ]),
    ],
    'Controlled tests audit': [
      ['phrase', 'group', 'v5_decision', 'commercial_hypothesis', 'noise_risk', 'final_audit_decision', 'eval_rule'],
      ...audits.controlled.rows.map((r) => [
        r.phrase,
        r.group_id,
        r.current_v5_decision,
        r.commercial_hypothesis,
        r.noise_risk,
        r.final_audit_decision,
        r.post_launch_rule,
      ]),
    ],
    'Unique negative risks': [
      ['negative_id', 'negative', 'level', 'scope', 'v5_decision', 'final_state', 'exact_action'],
      ...audits.uniqueNegative.rows.map((r) => [
        r.negative_id,
        r.negative,
        r.level,
        r.applied_groups.join(';'),
        r.v5_decision,
        r.final_state,
        r.exact_action,
      ]),
    ],
    'Semantic-risk reconciliation': [
      ['metric', 'value'],
      ...Object.entries(audits.reconciliation.reconciliation).map(([k, v]) => [k, String(v)]),
    ],
    'Literal collision corrections': [
      ['finding_id', 'keyword', 'negative', 'v5_correction', 'exact_action', 'valid'],
      ...audits.collisionCorrections.rows.map((r) => [
        r.finding_id,
        r.active_keyword,
        r.offending_negative,
        r.v5_correction_field,
        r.exact_action,
        r.correction_valid ? 'YES' : 'NO',
      ]),
    ],
    'Evidence integrity findings': [
      ['artefact', 'field', 'bad_value', 'severity'],
      ...audits.integrity.findings.slice(0, 800).map((f) => [f.artefact, f.field, f.bad_value, f.severity || 'MEDIUM']),
    ],
    'Generator regression tests': [
      ['regression_id', 'description', 'passed', 'error'],
      ...regression.tests.map((t) => [t.regression_id, t.description, t.passed ? 'PASS' : 'FAIL', t.error || '']),
    ],
    'QA gate decision': [
      ['check', 'result', 'detail'],
      ...gate.checks.map((c) => [c.id, c.passed ? 'PASS' : 'FAIL', c.detail]),
      ['FINAL', gate.final_result, gate.summary],
    ],
  };

  const wb = new ExcelJS.Workbook();
  for (const [name, data] of Object.entries(sheets)) {
    const ws = wb.addWorksheet(name.slice(0, 31));
    data.forEach((row) => ws.addRow(row.map((c) => (c == null ? '' : c))));
  }
  const out = path.join(EXPORTS, 'CORVONERO-V5-QA-REPAIR-AUDIT.xlsx');
  await wb.xlsx.writeFile(out);
  return { path: out, sheets: Object.keys(sheets) };
}

function runIndependentGate(audits, regression) {
  const checks = [];

  const add = (id, passed, detail) => checks.push({ id, passed, detail });

  add(
    'G-01-no-placeholder-in-repair-package',
    audits.integrity.findings.filter((f) => f.severity === 'CRITICAL' && f.artefact.includes('QA-REPAIR')).length === 0,
    'Repair package JSON must not introduce new placeholder values'
  );
  add(
    'G-02-root-cause-documented',
    !!audits.placeholder.root_cause.exact_defect,
    '2464 shared-string index leak documented with reusable fix'
  );
  add(
    'G-03-career-education-leakage',
    audits.career.active_leakage_count === 0,
    `${audits.career.active_leakage_count} active v5 phrases require EXCLUDE (education/career/employment)`
  );
  add(
    'G-04-controlled-test-hypothesis',
    audits.controlled.missing_hypothesis_count === 0,
    `${audits.controlled.missing_hypothesis_count} controlled phrases lack commercial hypothesis`
  );
  add(
    'G-05-unique-negative-final-states',
    audits.uniqueNegative.totals.unresolved + audits.uniqueNegative.totals.blocking === 0,
    `UNRESOLVED=${audits.uniqueNegative.totals.unresolved} BLOCKING=${audits.uniqueNegative.totals.blocking}`
  );
  add(
    'G-06-safe-evidence-specific',
    audits.uniqueNegative.totals.unresolved === 0,
    `${audits.uniqueNegative.totals.unresolved} SAFE decisions still use generic template without phrase-specific proof`
  );
  add(
    'G-07-no-unresolved-semantic-risks',
    audits.reconciliation.reconciliation.reconciled_pass,
    `unique_unresolved_after=${audits.reconciliation.reconciliation.unique_unresolved_risks_after}`
  );
  add(
    'G-08-collision-exact-actions',
    audits.collisionCorrections.invalid_or_generic === 0,
    `${audits.collisionCorrections.invalid_or_generic} blocking findings still have generic correction field in v5 source`
  );
  add(
    'G-09-summary-reconciliation',
    !audits.reconciliation.misleading_v5_summary.contradiction,
    'v5 collision summary contradiction flagged (semantic_risks_after vs unresolved_count)'
  );
  add(
    'G-10-generator-regression',
    regression.passed,
    regression.tests.filter((t) => !t.passed).map((t) => t.regression_id).join(', ') || 'all passed'
  );

  const blockers = checks.filter((c) => !c.passed);
  const passed = blockers.length === 0;

  return {
    gate_id: 'v5-qa-repair-gate',
    evaluated_at: new Date().toISOString(),
    final_result: passed ? 'PASS — V6 PRODUCTION AUTHORIZED' : 'BLOCKED — QA REPAIR INCOMPLETE',
    v6_production: passed ? 'AUTHORIZED_FOR_FOLLOWUP_TASK' : 'NOT AUTHORIZED',
    checks,
    blockers: blockers.map((b) => ({ id: b.id, detail: b.detail })),
    summary: passed
      ? 'All repair gates passed; v6 production may proceed in a separate authorized task.'
      : `${blockers.length} gate check(s) failed; v6 production blocked.`,
  };
}

async function main() {
  fs.mkdirSync(AUDIT, { recursive: true });

  const rejection = {
    registered_at: new Date().toISOString(),
    commander_v5: 'REJECTED BY OPERATOR — QA EVIDENCE INTEGRITY FAILURE',
    review_workbook_v5: 'REJECTED BY OPERATOR — PLACEHOLDER AND UNRESOLVED RISK FAILURE',
    commander_dry_run: 'BLOCKED',
    v6_production: 'NOT AUTHORIZED',
    launch: 'NOT AUTHORIZED',
    note: 'v5 artefacts preserved unchanged; this package audits defects and repairs reusable generators only.',
  };
  writeJson(path.join(AUDIT, 'v5-rejection-status.json'), rejection);

  const inputs = loadV5Inputs(ROOT);
  const placeholder = auditPlaceholderRootCause();
  const integrity = scanEvidenceIntegrity(ROOT, inputs);
  const career = auditCareerEducationQueries(inputs);
  const controlled = auditControlledTests(inputs);
  const uniqueNegative = auditUniqueNegativeRisks(inputs);
  const reconciliation = reconcileSemanticRisks(inputs, uniqueNegative);
  const collisionCorrections = auditExactCollisionCorrections(inputs);
  const regression = runWorkbookIntegrityRegressionTests();

  writeJson(path.join(AUDIT, 'v5-placeholder-root-cause.json'), placeholder);
  writeMd(
    path.join(AUDIT, 'v5-placeholder-root-cause.md'),
    [
      '# V5 Placeholder Root Cause — 2464',
      '',
      `**Defect:** Operator-visible \`2464\` in narrative evidence fields.`,
      '',
      '## Root cause',
      '',
      placeholder.root_cause.exact_defect,
      '',
      '## Source',
      '',
      `- File: \`${placeholder.root_cause.source_file}\``,
      `- Function: \`${placeholder.root_cause.function}\``,
      `- Fields: ${placeholder.root_cause.field}`,
      '',
      '## Affected scope',
      '',
      `- Estimated cells: ${placeholder.evidence.xlsx_scan.cells_referencing_index_2464}`,
      `- Sheets: ${placeholder.root_cause.affected_sheets.join(', ')}`,
      '',
      '## Why validation failed',
      '',
      placeholder.root_cause.why_validation_failed,
      '',
      '## Reusable correction',
      '',
      placeholder.root_cause.reusable_correction,
    ].join('\n')
  );

  writeJson(path.join(AUDIT, 'v5-evidence-integrity-scan.json'), integrity);
  writeMd(
    path.join(AUDIT, 'v5-evidence-integrity-scan.md'),
    jsonToMd('V5 Evidence Integrity Scan', integrity) +
      `\n## Sample findings\n\n${integrity.findings
        .slice(0, 30)
        .map((f) => `- **${f.severity}** ${f.artefact} / ${f.field}: \`${String(f.bad_value).slice(0, 60)}\``)
        .join('\n')}`
  );

  writeJson(path.join(AUDIT, 'v5-career-education-query-audit.json'), career);
  writeMd(
    path.join(AUDIT, 'v5-career-education-query-audit.md'),
    [
      jsonToMd('V5 Career and Education Query Audit', {
        generated_at: career.generated_at,
        summary: {
          phrases_checked: career.phrases_checked,
          matched: career.matched_phrases,
          active_leakage: career.active_leakage_count,
        },
      }),
      '## Active leakage (must EXCLUDE in v6)',
      '',
      ...career.leakage.map((r) => `- \`${r.phrase}\` (${r.current_group}) → **${r.corrected_decision}**: ${r.reason}`),
    ].join('\n')
  );

  writeJson(path.join(AUDIT, 'v5-controlled-test-audit.json'), controlled);
  writeMd(path.join(AUDIT, 'v5-controlled-test-audit.md'), jsonToMd('V5 Controlled Test Audit', controlled));

  writeJson(path.join(AUDIT, 'v5-unique-negative-risk-audit.json'), uniqueNegative);
  writeMd(path.join(AUDIT, 'v5-unique-negative-risk-audit.md'), jsonToMd('V5 Unique Negative Risk Audit', uniqueNegative));

  writeJson(path.join(AUDIT, 'v5-semantic-risk-reconciliation.json'), reconciliation);
  writeMd(
    path.join(AUDIT, 'v5-semantic-risk-reconciliation.md'),
    [
      jsonToMd('V5 Semantic Risk Reconciliation', reconciliation),
      '',
      '## Misleading v5 summary',
      '',
      `- semantic_risks_after: ${reconciliation.misleading_v5_summary.semantic_risks_after}`,
      `- unresolved_count: ${reconciliation.misleading_v5_summary.unresolved_count}`,
      `- contradiction: **${reconciliation.misleading_v5_summary.contradiction}**`,
    ].join('\n')
  );

  writeJson(path.join(AUDIT, 'v5-exact-collision-correction-log.json'), collisionCorrections);
  writeMd(
    path.join(AUDIT, 'v5-exact-collision-correction-log.md'),
    jsonToMd('V5 Exact Collision Correction Log', {
      generated_at: collisionCorrections.generated_at,
      summary: {
        total: collisionCorrections.total_blocking_findings,
        valid: collisionCorrections.valid_exact_actions,
        invalid: collisionCorrections.invalid_or_generic,
      },
    })
  );

  const audits = { placeholder, integrity, career, controlled, uniqueNegative, reconciliation, collisionCorrections };
  const gate = runIndependentGate(audits, regression);

  writeJson(path.join(VALIDATION, 'v5-qa-repair-gate.json'), gate);
  writeMd(
    path.join(VALIDATION, 'v5-qa-repair-gate.md'),
    [
      '# V5 QA Repair Gate',
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
    ].join('\n')
  );

  writeJson(path.join(VALIDATION, 'workbook-integrity-regression-v5.json'), regression);

  fs.mkdirSync(APPROVALS, { recursive: true });
  if (gate.final_result.startsWith('PASS')) {
    writeMd(
      path.join(APPROVALS, 'v6-production-authorization.md'),
      [
        '# V6 Production Authorization Charter',
        '',
        'QA Repair Gate **PASSED**. A follow-up task may:',
        '',
        '1. Rebuild final semantic registry with career/education exclusions applied.',
        '2. Apply controlled-test decisions and resolved negative changes.',
        '3. Rebuild ads where mappings changed.',
        '4. Create dataset v6.',
        '5. Generate unified Commander XLSX v6.',
        '6. Generate final review workbook v6 with repaired generator.',
        '7. Run dry-run readiness validation.',
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
        'QA Repair Gate **BLOCKED**. v6 production is **NOT AUTHORIZED**.',
        '',
        '## Unresolved blockers',
        '',
        ...gate.blockers.map((b) => `- **${b.id}**: ${b.detail}`),
        '',
        '## Required before v6',
        '',
        '1. Apply career/education EXCLUDE decisions to semantic registry (4+ active leakage phrases).',
        '2. Upgrade 333 generic SAFE negative resolutions to SAFE — PROVEN with phrase-specific evidence.',
        '3. Regenerate collision evidence with exact DELETE NEGATIVE correction strings (not blocks_own_group_keyword).',
        '4. Reconcile semantic_risks_after pair metric vs unique unresolved risks.',
        '5. Regenerate review workbook using repaired generator (no empty narrative cells).',
        '6. Re-run this QA Repair Gate until PASS.',
      ].join('\n')
    );
  }

  const workbook = await writeQaRepairWorkbook(audits, regression, gate);

  console.log(
    JSON.stringify(
      {
        gate: gate.final_result,
        workbook: workbook.path,
        blockers: gate.blockers.length,
        regression_passed: regression.passed,
      },
      null,
      2
    )
  );
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
