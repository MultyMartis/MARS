#!/usr/bin/env node
'use strict';

/**
 * Human review workbook v3 — operator verification (NOT Commander import).
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const DATASET = path.join(ROOT, 'production/direct-commander-production-dataset-v3.json');
const KW_REG = path.join(ROOT, 'production/final-keyword-registry-v3.json');
const COLLISION = path.join(ROOT, 'production/validation/negative-collision-validation-v3.json');
const OUTPUT = path.join(ROOT, 'exports/CORVONERO-CAMPAIGN-REVIEW-v3.xlsx');

function escapeCsv(v) {
  const s = String(v ?? '').replace(/"/g, '""');
  return `"${s}"`;
}

function rowsToCsv(headers, rows) {
  return [headers.map(escapeCsv).join(','), ...rows.map((r) => r.map(escapeCsv).join(','))].join('\n');
}

async function main() {
  const dataset = JSON.parse(fs.readFileSync(DATASET, 'utf8'));
  const kwData = JSON.parse(fs.readFileSync(KW_REG, 'utf8'));
  const collision = JSON.parse(fs.readFileSync(COLLISION, 'utf8'));

  const v2Diff = fs.existsSync(path.join(ROOT, 'production/keyword-v2-to-v3-diff.md'))
    ? fs.readFileSync(path.join(ROOT, 'production/keyword-v2-to-v3-diff.md'), 'utf8')
    : '';

  const sheets = {
    Campaign: [
      ['field', 'value'],
      ['campaign_id', dataset.unified_campaign?.id],
      ['campaign_name', dataset.unified_campaign?.name],
      ['utm_campaign', dataset.unified_campaign?.utm_campaign],
      ['export_model', dataset.export_model],
      ['active_groups', dataset.groups.length],
      ['active_keywords', dataset.keywords.length],
      ['ads', dataset.ads.length],
      ['held_groups', (dataset.held_groups || []).length],
      ['future_split', dataset.unified_campaign?.future_split],
    ],
    Directions: [
      ['direction_id', 'marker', 'label', 'name', 'active_groups', 'held_groups', 'direction_negatives_count'],
      ...(dataset.logical_directions || []).map((d) => [
        d.id,
        d.marker,
        d.label,
        d.name,
        (d.active_groups || []).length,
        (d.held_groups || []).length,
        (d.direction_negatives || []).length,
      ]),
    ],
    Groups: [
      ['group_id', 'direction_marker', 'group_export_name', 'viability', 'keywords', 'ads', 'planned_url', 'group_negatives_count'],
      ...dataset.groups.map((g) => [
        g.group_id,
        g.direction_marker,
        g.group_export_name,
        g.viability_status,
        g.keywords.length,
        g.ads.length,
        g.planned_url,
        (g.group_negatives || []).length,
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
    Exclusions: [
      ['keyword_id', 'phrase', 'status', 'reason'],
      ...(kwData.reject_log || []).slice(0, 800).map((r) => [r.keyword_id, r.source_phrase, r.status, r.reason]),
    ],
    Ads: [
      ['group_id', 'ad_id', 'headline_1', 'headline_2', 'text', 'landing_url'],
      ...dataset.ads.map((a) => [a.group_id, a.ad_id, a.headline_1, a.headline_2, a.text, a.landing_url]),
    ],
    'Global negatives': [['phrase'], ...(dataset.global_negatives || []).map((p) => [p])],
    'Direction negatives': [
      ['direction_id', 'phrase'],
      ...Object.entries(dataset.direction_negatives || {}).flatMap(([did, tokens]) => tokens.map((t) => [did, t])),
    ],
    'Group negatives': [
      ['group_id', 'phrase'],
      ...dataset.groups.flatMap((g) => (g.group_negatives || []).map((t) => [g.group_id, t])),
    ],
    'Cross-negatives': [
      ['group_id', 'token'],
      ...Object.entries(dataset.cross_negatives || {}).flatMap(([gid, tokens]) => tokens.map((t) => [gid, t])),
    ],
    'Inline negatives': [
      ['group_id', 'token'],
      ...Object.entries(dataset.phrase_inline_negatives || {}).flatMap(([gid, tokens]) => tokens.map((t) => [gid, t])),
    ],
    'Collision audit': [
      ['keyword', 'group_id', 'negative', 'level', 'collision', 'risk_type'],
      ...(collision.blocking_records || []).map((r) => [
        r.keyword,
        r.group_id,
        r.negative,
        r.negative_level,
        r.collision,
        r.risk_type,
      ]),
    ],
    Bids: [
      ['group_id', 'phrase', 'tier', 'bid'],
      ...dataset.keywords.map((k) => [k.group_id, k.normalized_phrase, k.bid_tier, k.final_bid]),
    ],
    URLs: [
      ['landing_id', 'path', 'url', 'groups', 'status'],
      ...(dataset.urls || []).map((u) => [
        u.landing_id,
        u.path,
        u.final_planned_url,
        (u.groups || []).join('; '),
        u.url_status,
      ]),
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
    'Merge log': [
      ['note'],
      ['No merges in v3 — architecture groups retained'],
      ...(dataset.merge_log || []).map((m) => [JSON.stringify(m)]),
    ],
    'V2 to V3 change log': [
      ['metric', 'v2', 'v3'],
      ['active_keywords', '341', String(dataset.keywords.length)],
      ['global_negatives', '57', String((dataset.global_negatives || []).length)],
      ['phrase_inline', '27', String(Object.values(dataset.phrase_inline_negatives || {}).flat().length)],
      ['collision_blocking_after', '0 (warnings 26)', String(collision.collisions_after_correction || 0)],
      ['regression_passed', 'partial', String(collision.regression_after?.passed)],
      ['diff_ref', 'production/keyword-v2-to-v3-diff.md', v2Diff.split('\n')[0] || ''],
    ],
  };

  const reviewDir = path.join(ROOT, 'exports/review-v3-csv');
  fs.mkdirSync(reviewDir, { recursive: true });
  for (const [name, data] of Object.entries(sheets)) {
    const headers = data[0];
    const rows = data.slice(1);
    fs.writeFileSync(
      path.join(reviewDir, `${name.replace(/\s+/g, '-').toLowerCase()}.csv`),
      rowsToCsv(headers, rows),
      'utf8'
    );
  }

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
    /* csv fallback */
  }

  const result = {
    review_xlsx: xlsxWritten ? OUTPUT : null,
    review_csv_dir: reviewDir,
    sheets: Object.keys(sheets),
    note: xlsxWritten ? 'Review XLSX v3 generated' : 'exceljs not installed — CSV in exports/review-v3-csv/',
  };

  fs.writeFileSync(path.join(ROOT, 'production/validation/review-workbook-v3-result.json'), JSON.stringify(result, null, 2));
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
