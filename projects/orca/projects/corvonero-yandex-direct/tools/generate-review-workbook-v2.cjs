#!/usr/bin/env node
'use strict';

/**
 * Human review workbook for operator verification (NOT Commander import).
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const DATASET = path.join(ROOT, 'production/direct-commander-production-dataset-v2.json');
const OUTPUT = path.join(ROOT, 'exports/CORVONERO-CAMPAIGN-REVIEW-v2.xlsx');

function escapeCsv(v) {
  const s = String(v ?? '').replace(/"/g, '""');
  return `"${s}"`;
}

function rowsToCsv(headers, rows) {
  return [headers.map(escapeCsv).join(','), ...rows.map((r) => r.map(escapeCsv).join(','))].join('\n');
}

async function main() {
  const dataset = JSON.parse(fs.readFileSync(DATASET, 'utf8'));

  const sheets = {
    Groups: [
      ['group_id', 'direction_marker', 'group_export_name', 'viability', 'keywords', 'ads', 'planned_url'],
      ...dataset.groups.map((g) => [
        g.group_id,
        g.direction_marker,
        g.group_export_name,
        g.viability_status,
        g.keywords.length,
        g.ads.length,
        g.planned_url,
      ]),
    ],
    Keywords: [
      ['group_id', 'direction_marker', 'phrase', 'bid', 'tier', 'classification'],
      ...dataset.keywords.map((k) => [
        k.group_id,
        k.direction_marker,
        k.ad_phrase,
        k.final_bid,
        k.bid_tier,
        k.classification,
      ]),
    ],
    Ads: [
      ['group_id', 'ad_id', 'headline_1', 'headline_2', 'text', 'landing_url'],
      ...dataset.ads.map((a) => [a.group_id, a.ad_id, a.headline_1, a.headline_2, a.text, a.landing_url]),
    ],
    'Global negatives': [['phrase'], ...(dataset.global_negatives || []).map((p) => [p])],
    'Cross-negatives': [
      ['group_id', 'token'],
      ...Object.entries(dataset.cross_negatives || {}).flatMap(([gid, tokens]) =>
        tokens.map((t) => [gid, t])
      ),
    ],
    URLs: [
      ['landing_id', 'path', 'url', 'groups'],
      ...(dataset.urls || []).map((u) => [u.landing_id, u.path, u.final_planned_url, (u.groups || []).join('; ')]),
    ],
    Bids: [
      ['group_id', 'phrase', 'tier', 'bid'],
      ...dataset.keywords.map((k) => [k.group_id, k.normalized_phrase, k.bid_tier, k.final_bid]),
    ],
    'Held groups': [
      ['group_id', 'direction_marker', 'group_name', 'planned_url', 'status'],
      ...(dataset.held_groups || []).map((g) => [
        g.group_id,
        g.direction_marker,
        g.group_name,
        g.planned_url,
        g.viability_status,
      ]),
    ],
    Exclusions: [
      ['keyword_id', 'phrase', 'status', 'reason'],
      ...(JSON.parse(fs.readFileSync(path.join(ROOT, 'production/final-keyword-registry-v2.json'), 'utf8')).reject_log || []).slice(
        0,
        500
      ).map((r) => [r.keyword_id, r.source_phrase, r.status, r.reason]),
    ],
  };

  // Write multi-sheet CSV bundle as folder (xlsx without exceljs — use csv zip alternative)
  // Use simple combined CSV export per sheet in review folder
  const reviewDir = path.join(ROOT, 'exports/review-v2-csv');
  fs.mkdirSync(reviewDir, { recursive: true });

  for (const [name, data] of Object.entries(sheets)) {
    const headers = data[0];
    const rows = data.slice(1);
    fs.writeFileSync(path.join(reviewDir, `${name.replace(/\s+/g, '-').toLowerCase()}.csv`), rowsToCsv(headers, rows), 'utf8');
  }

  // Try exceljs if available for xlsx
  let xlsxWritten = false;
  try {
    const exceljsPath = path.resolve(__dirname, '../../../ppc/triumph-manipulator/tools/exporter-cli/node_modules/exceljs');
    const ExcelJS = require(exceljsPath);
    const wb = new ExcelJS.Workbook();
    for (const [name, data] of Object.entries(sheets)) {
      const ws = wb.addWorksheet(name.slice(0, 31));
      data.forEach((row) => ws.addRow(row));
    }
    await wb.xlsx.writeFile(OUTPUT);
    xlsxWritten = true;
  } catch {
    // fallback documented below
  }

  const result = {
    review_xlsx: xlsxWritten ? OUTPUT : null,
    review_csv_dir: reviewDir,
    sheets: Object.keys(sheets),
    note: xlsxWritten ? 'Review XLSX generated' : 'exceljs not installed — CSV sheets in exports/review-v2-csv/',
  };

  fs.writeFileSync(path.join(ROOT, 'production/validation/review-workbook-v2-result.json'), JSON.stringify(result, null, 2));
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
