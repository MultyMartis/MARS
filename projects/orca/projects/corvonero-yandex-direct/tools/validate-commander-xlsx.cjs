#!/usr/bin/env node
'use strict';

/**
 * Structural validation for Corvonero Commander XLSX.
 */
const fs = require('fs');
const path = require('path');
const { readZipEntryUtf8 } = require(path.resolve(
  __dirname,
  '../../../ppc/triumph-manipulator/tools/exporter-cli/xlsx-zip-patch'
));

const ROOT = path.resolve(__dirname, '..');
const XLSX = path.join(ROOT, 'exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v1.xlsx');
const DATASET = path.join(ROOT, 'production/direct-commander-production-dataset-v1.json');
const OUT_JSON = path.join(ROOT, 'production/validation/direct-commander-xlsx-validation-v1.json');
const OUT_MD = path.join(ROOT, 'production/validation/direct-commander-xlsx-validation-v1.md');

const DATA_START = 16;
const COL = { groupName: 5, phrase: 8, h1: 10, h2: 11, text: 12, url: 48, bid: 54, groupNeg: 68, adType: 2 };

function colToLetter(col) {
  let n = col;
  let s = '';
  while (n > 0) {
    s = String.fromCharCode(65 + ((n - 1) % 26)) + s;
    n = Math.floor((n - 1) / 26);
  }
  return s;
}

function cellValue(rowXml, ref) {
  const re = new RegExp(`<c\\s+r="${ref}"[^>]*>[\\s\\S]*?<v>([\\s\\S]*?)</v>`, 'i');
  const m = rowXml.match(re);
  if (!m) return '';
  return m[1]
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&apos;/g, "'");
}

function rowXml(sheet, rowNum) {
  const re = new RegExp(`<row r="${rowNum}"[^>]*>[\\s\\S]*?</row>`);
  const m = sheet.match(re);
  return m ? m[0] : null;
}

function getCell(sheet, row, col) {
  const rx = rowXml(sheet, row);
  if (!rx) return '';
  return cellValue(rx, `${colToLetter(col)}${row}`);
}

function listRows(sheet) {
  const rows = [];
  const re = /<row r="(\d+)"/g;
  let m;
  while ((m = re.exec(sheet)) !== null) rows.push(parseInt(m[1], 10));
  return rows.sort((a, b) => a - b);
}

function main() {
  const errors = [];
  const warnings = [];
  const fixed = [];

  if (!fs.existsSync(XLSX)) {
    errors.push('XLSX file missing');
    writeReport(errors, warnings, fixed, {});
    process.exit(1);
  }

  const dataset = JSON.parse(fs.readFileSync(DATASET, 'utf8'));
  let sheet;
  try {
    sheet = readZipEntryUtf8(XLSX, 'xl/worksheets/sheet1.xml');
  } catch (e) {
    errors.push(`Cannot read sheet1: ${e.message}`);
    writeReport(errors, warnings, fixed, {});
    process.exit(1);
  }

  const dataRows = listRows(sheet).filter((r) => r >= DATA_START);
  const groupsSeen = new Set();
  const phrases = [];
  const h1set = new Set();
  let adRows = 0;
  let kwRows = 0;
  let triumphRefs = 0;

  for (const r of dataRows) {
    const gn = getCell(sheet, r, COL.groupName);
    const ph = getCell(sheet, r, COL.phrase);
    const h1 = getCell(sheet, r, COL.h1);
    const url = getCell(sheet, r, COL.url);
    const bid = getCell(sheet, r, COL.bid);
    const blob = `${gn}${ph}${h1}${url}${bid}`;

    if (/triumph|manipulator-triumph|gruzotaxi/i.test(blob)) triumphRefs++;

    if (gn) groupsSeen.add(gn);
    if (h1) {
      adRows++;
      h1set.add(h1);
      if (h1.length > 56) errors.push(`row ${r}: h1 length ${h1.length}`);
      const h2 = getCell(sheet, r, COL.h2);
      const tx = getCell(sheet, r, COL.text);
      if (h2.length > 30) errors.push(`row ${r}: h2 length ${h2.length}`);
      if (tx.length > 81) errors.push(`row ${r}: text length ${tx.length}`);
      if (url && !/^https:\/\/lk\.corvonero\.ru\//.test(url)) errors.push(`row ${r}: bad url ${url.slice(0, 60)}`);
    }
    if (ph) {
      kwRows++;
      phrases.push(ph);
      if (parseFloat(bid) <= 0) errors.push(`row ${r}: zero bid`);
    }
  }

  if (triumphRefs > 0) errors.push(`Triumph legacy references: ${triumphRefs}`);
  if (groupsSeen.size !== 48) errors.push(`Expected 48 groups, found ${groupsSeen.size}`);
  if (kwRows !== dataset.keywords.length) warnings.push(`Keyword rows ${kwRows} vs dataset ${dataset.keywords.length}`);
  if (adRows < 48) errors.push(`Ad rows ${adRows} < 48`);
  if (h1set.size < 40) warnings.push(`Only ${h1set.size} unique headlines — check duplication`);

  const dupPhrases = phrases.filter((p, i) => phrases.indexOf(p) !== i);
  if (dupPhrases.length) errors.push(`Duplicate phrases: ${dupPhrases.slice(0, 5).join('; ')}`);

  for (const g of dataset.groups) {
    const hasKw = phrases.some((p) => g.keywords.some((k) => k.ad_phrase === p));
    if (!hasKw && g.keywords.length) warnings.push(`Group ${g.group_id} keywords not found in sheet sample`);
  }

  const metaType = getCell(sheet, 7, 5);
  if (!metaType.includes('перфоманс') && !metaType.includes('Текстово')) {
    warnings.push(`Campaign type cell: ${metaType}`);
  }
  const promo = getCell(sheet, 11, 5);
  if (!promo.includes('lk.corvonero.ru')) errors.push(`Promotion URL wrong: ${promo}`);

  const counts = {
    data_rows: dataRows.length,
    groups_in_sheet: groupsSeen.size,
    ad_rows: adRows,
    keyword_rows: kwRows,
    unique_headlines: h1set.size,
  };

  const ok = errors.length === 0;
  writeReport(errors, warnings, fixed, counts, ok);
  console.log(ok ? 'VALIDATION PASS' : 'VALIDATION FAIL', counts);
  if (!ok) process.exit(1);
}

function writeReport(errors, warnings, fixed, counts, ok = false) {
  fs.mkdirSync(path.dirname(OUT_JSON), { recursive: true });
  const report = {
    validated_at: new Date().toISOString(),
    file: XLSX,
    status: ok ? 'STRUCTURALLY_VALIDATED' : 'FAILED',
    errors,
    warnings,
    fixed_errors: fixed,
    counts,
    manual_import_check_required: true,
  };
  fs.writeFileSync(OUT_JSON, JSON.stringify(report, null, 2));
  fs.writeFileSync(
    OUT_MD,
    `# Direct Commander XLSX Validation — v1\n\n**Status:** ${report.status}\n\n## Counts\n\n${Object.entries(counts).map(([k, v]) => `- ${k}: ${v}`).join('\n')}\n\n## Errors\n\n${errors.length ? errors.map((e) => `- ${e}`).join('\n') : '- none'}\n\n## Warnings\n\n${warnings.length ? warnings.map((w) => `- ${w}`).join('\n') : '- none'}\n\n**Manual Commander import check required.**\n`
  );
}

main();
