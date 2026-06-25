#!/usr/bin/env node
'use strict';
const fs = require('fs');
const path = require('path');
const { validateWorkbookSheetsV71 } = require('./lib/workbook-integrity-v7.1.cjs');
const {
  NON_CONTROLLED_HYPOTHESIS_SENTINEL_RU,
} = require('./lib/hypothesis-serialization-bridge.cjs');

const ROOT = path.resolve(__dirname, '..');
const XLSX = path.join(ROOT, 'exports/CORVONERO-CAMPAIGN-REVIEW-v7.1.xlsx');
const DATASET = path.join(ROOT, 'production/direct-commander-production-dataset-v7.1.json');
const EXCLUSION_REG = path.join(ROOT, 'production/operator-semantic-exclusion-registry-v1.json');
const OUT_JSON = path.join(ROOT, 'production/validation/review-workbook-validation-v7.1.json');
const OUT_MD = path.join(ROOT, 'production/validation/review-workbook-validation-v7.1.md');
const ExcelJS = require(path.join(ROOT, '../../ppc/triumph-manipulator/tools/exporter-cli/node_modules/exceljs'));

const NARRATIVE_FIELDS = new Set([
  'reason',
  'hypothesis',
  'risk',
  'evaluation rule',
  'correction',
  'evidence',
  'details',
  'explanation',
]);

function isNumericOnly(s) {
  return /^\d+$/.test(String(s || '').trim()) && String(s).trim().length >= 3;
}

async function main() {
  const errors = [];
  const dataset = JSON.parse(fs.readFileSync(DATASET, 'utf8'));
  const exclusion = JSON.parse(fs.readFileSync(EXCLUSION_REG, 'utf8'));

  const wb = new ExcelJS.Workbook();
  await wb.xlsx.readFile(XLSX);

  const kwSheet = wb.getWorksheet('Keywords');
  let kwRows = 0;
  let badHyp = 0;
  kwSheet.eachRow((row, i) => {
    if (i === 1) return;
    kwRows++;
    const hyp = String(row.getCell(8).value ?? '');
    if (!hyp || hyp === '272' || isNumericOnly(hyp)) badHyp++;
    if (hyp !== NON_CONTROLLED_HYPOTHESIS_SENTINEL_RU && hyp.length < 12 && !hyp.includes('Narrow test') && !hyp.includes('Paid ')) {
      if (!hyp.includes('test:')) badHyp++;
    }
  });
  if (kwRows !== dataset.keywords.length) errors.push(`keyword count ${kwRows} vs ${dataset.keywords.length}`);
  if (badHyp > 0) errors.push(`invalid hypothesis cells: ${badHyp}`);

  for (const e of exclusion.exclusions || []) {
    const found = [];
    kwSheet.eachRow((row, i) => {
      if (i === 1) return;
      const ph = String(row.getCell(3).value || '').toLowerCase().replace(/\s+-.*$/, '').trim();
      if (ph === e.normalized_phrase) found.push(i);
    });
    if (found.length) errors.push(`excluded phrase in Keywords sheet: ${e.normalized_phrase}`);
  }

  const passed = errors.length === 0;
  const report = {
    validated_at: new Date().toISOString(),
    file: XLSX,
    passed,
    errors,
    checks: { keyword_rows: kwRows, bad_hypothesis: badHyp, no_272: badHyp === 0 },
    actual_xlsx_reopened: true,
  };
  fs.writeFileSync(OUT_JSON, JSON.stringify(report, null, 2));
  fs.writeFileSync(OUT_MD, `# Review Workbook Actual XLSX Validation v7.1\n\n**Passed:** ${passed}\n\n${errors.map((e) => `- ${e}`).join('\n') || '- none'}\n`);
  console.log(JSON.stringify(report, null, 2));
  if (!passed) process.exit(1);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
