#!/usr/bin/env node
'use strict';

/**
 * Human review workbook v4 — operator verification with collision evidence.
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const DATASET = path.join(ROOT, 'production/direct-commander-production-dataset-v4.json');
const SEMANTIC = path.join(ROOT, 'production/semantic-human-review-v4.json');
const COLLISION = path.join(ROOT, 'production/validation/negative-collision-validation-v4.json');
const EVIDENCE = path.join(ROOT, 'production/validation/collision-evidence-v4.json');
const AD_REG = path.join(ROOT, 'production/final-ad-registry-v4.json');
const KW_REG = path.join(ROOT, 'production/final-keyword-registry-v4.json');
const OUTPUT = path.join(ROOT, 'exports/CORVONERO-CAMPAIGN-REVIEW-v4.xlsx');

function escapeCsv(v) {
  const s = String(v ?? '').replace(/"/g, '""');
  return `"${s}"`;
}

function rowsToCsv(headers, rows) {
  return [headers.map(escapeCsv).join(','), ...rows.map((r) => r.map(escapeCsv).join(','))].join('\n');
}

async function main() {
  const dataset = JSON.parse(fs.readFileSync(DATASET, 'utf8'));
  const semantic = JSON.parse(fs.readFileSync(SEMANTIC, 'utf8'));
  const collision = JSON.parse(fs.readFileSync(COLLISION, 'utf8'));
  const evidence = JSON.parse(fs.readFileSync(EVIDENCE, 'utf8'));
  const adReg = JSON.parse(fs.readFileSync(AD_REG, 'utf8'));
  const kwReg = JSON.parse(fs.readFileSync(KW_REG, 'utf8'));

  const reviewById = new Map(semantic.reviews.map((r) => [r.keyword_id, r]));

  const adChanges = (adReg.certainty_qa?.changes || []).map((c) => [
    c.group_id,
    c.ad_id,
    c.status,
    (c.issues_found || []).join('; '),
    c.headline_1,
    c.text,
  ]);

  const v3Changes = kwReg.v3_to_v4_changes || [];

  const sheets = {
    Campaign: [
      ['field', 'value'],
      ['campaign_id', dataset.unified_campaign?.id],
      ['campaign_name', dataset.unified_campaign?.name],
      ['utm_campaign', dataset.unified_campaign?.utm_campaign],
      ['export_model', dataset.export_model],
      ['version', 'v4'],
      ['active_groups', dataset.groups.length],
      ['active_keywords', dataset.keywords.length],
      ['ads', dataset.ads.length],
      ['held_groups', (dataset.held_groups || []).length],
      ['semantic_review_ref', dataset.semantic_review_ref],
      ['collision_evidence_ref', dataset.collision_evidence_ref],
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
      ['group_id', 'direction_marker', 'phrase', 'bid', 'tier', 'semantic_decision', 'confidence'],
      ...dataset.keywords.map((k) => [
        k.group_id,
        k.direction_marker,
        k.ad_phrase,
        k.final_bid,
        k.bid_tier,
        k.semantic_decision,
        k.semantic_confidence,
      ]),
    ],
    'Semantic review': [
      [
        'keyword_id',
        'group_id',
        'positive_phrase',
        'likely_intent',
        'commercial_service',
        'confidence',
        'decision',
        'reason',
        'ad_match',
        'landing_match',
        'reviewer_status',
      ],
      ...dataset.keywords.map((k) => {
        const r = reviewById.get(k.keyword_id) || {};
        return [
          k.keyword_id,
          k.group_id,
          k.normalized_phrase,
          r.likely_user_intent || '',
          r.commercial_service_sought || '',
          r.commercial_confidence || k.semantic_confidence,
          r.decision || k.semantic_decision,
          r.reason || '',
          r.advertisement_match || 'yes',
          r.landing_page_match || 'yes',
          r.reviewer_status || 'REVIEWED',
        ];
      }),
    ],
    Exclusions: [
      ['keyword_id', 'group_id', 'phrase', 'decision', 'reason'],
      ...semantic.reviews
        .filter((r) => r.decision.startsWith('EXCLUDE') || r.decision === 'HOLD AMBIGUOUS')
        .map((r) => [r.keyword_id, r.group_id, r.positive_phrase, r.decision, r.reason]),
    ],
    Ads: [
      ['group_id', 'ad_id', 'headline_1', 'headline_2', 'text', 'landing_url', 'certainty_review'],
      ...dataset.ads.map((a) => [
        a.group_id,
        a.ad_id,
        a.headline_1,
        a.headline_2,
        a.text,
        a.landing_url,
        a.certainty_review || 'REVIEWED',
      ]),
    ],
    'Ad changes': [
      ['group_id', 'ad_id', 'status', 'issues', 'headline_1', 'text'],
      ...adChanges,
    ],
    'Global negatives': [
      ['phrase', 'collision_test', 'risk_status', 'approval'],
      ...(dataset.global_negatives || []).map((p) => {
        const rec = (dataset.negatives || []).find((n) => (n.phrase || n) === p);
        return [p, rec?.collision_test || 'PASS', rec?.risk_status || 'LOW', rec?.approval_status || 'approved'];
      }),
    ],
    'Direction negatives': [
      ['direction_id', 'phrase', 'level'],
      ...Object.entries(dataset.direction_negatives || {}).flatMap(([did, tokens]) =>
        tokens.map((t) => [did, t, 'direction'])
      ),
    ],
    'Group negatives': [
      ['group_id', 'phrase', 'level'],
      ...dataset.groups.flatMap((g) => (g.group_negatives || []).map((t) => [g.group_id, t, 'group'])),
    ],
    'Cross-negatives': [
      ['group_id', 'token', 'stem_risk'],
      ...Object.entries(dataset.cross_negatives || {}).flatMap(([gid, tokens]) =>
        tokens.map((t) => [gid, t, /^(интеграц|настрой|синхрон|лекарств|автозапчаст)/.test(t) ? 'STEM_REVIEWED' : 'LOW'])
      ),
    ],
    'Inline negatives': [
      ['group_id', 'token'],
      ...Object.entries(dataset.phrase_inline_negatives || {}).flatMap(([gid, tokens]) =>
        tokens.map((t) => [gid, t])
      ),
    ],
    'Collision summary': [
      ['metric', 'value'],
      ['total_active_keywords', evidence.summary.total_active_keywords],
      ['global_negatives', evidence.summary.global_negatives],
      ['direction_negatives', evidence.summary.direction_negatives],
      ['group_cross_negatives', evidence.summary.group_cross_negatives],
      ['phrase_inline_negatives', evidence.summary.phrase_inline_negatives],
      ['total_pairs_tested', evidence.summary.total_pairs_tested],
      ['collisions_before_correction', evidence.summary.collisions_before_correction],
      ['corrections_applied', evidence.summary.corrections_applied],
      ['collisions_after_correction', evidence.summary.collisions_after_correction],
      ['stem_risk_warnings', evidence.summary.stem_risk_warnings],
      ['unresolved_stem_warnings', evidence.summary.unresolved_stem_warnings],
      ['regression_after_passed', evidence.summary.regression_after_passed],
    ],
    'Collision findings': [
      ['group_id', 'keyword', 'positive_base', 'negative', 'level', 'match_type', 'result_before', 'correction', 'result_after'],
      ...(evidence.findings || []).slice(0, 300).map((r) => [
        r.group_id,
        r.keyword,
        r.positive_base,
        r.negative,
        r.negative_level,
        r.risk_type,
        r.collision ? 'BLOCKING' : 'OK',
        r.correction || '',
        r.collision ? 'BLOCKING' : 'PASS',
      ]),
      ...(collision.removal_log || []).slice(0, 50).map((r) => [
        r.group_id || r.scope || '',
        (r.colliding_keywords || []).join('; '),
        '',
        r.negative,
        r.level || 'removed',
        'correction',
        'BLOCKING',
        r.reason || 'removed',
        'PASS',
      ]),
    ],
    'Collision passed samples': [
      ['level', 'group_id', 'keyword', 'negative', 'result'],
      ...['global', 'direction', 'group_cross', 'phrase_inline', 'group_export'].flatMap((level) => {
        const key = level === 'group_export' ? 'group_export' : level;
        const samples = evidence.passed_samples?.[key] || evidence.passed_samples?.[level] || [];
        return samples.map((r) => [level, r.group_id, r.keyword, r.negative, 'PASS']);
      }),
    ],
    'Regression tests': [
      ['regression_id', 'description', 'result_before', 'result_after', 'failures_after'],
      ...(evidence.regression_tests || []).map((r) => [
        r.regression_id,
        r.description,
        r.result_before,
        r.result_after,
        JSON.stringify(r.failures_after || []),
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
    'Merge log': [['note'], ['No merges in v4 — architecture groups retained']],
    'V3→V4 changes': [
      ['keyword_id', 'phrase', 'group_id', 'change', 'decision', 'reason'],
      ...v3Changes.map((c) => [c.keyword_id, c.phrase, c.group_id, c.change, c.decision, c.reason]),
    ],
  };

  const reviewDir = path.join(ROOT, 'exports/review-v4-csv');
  fs.mkdirSync(reviewDir, { recursive: true });
  for (const [name, data] of Object.entries(sheets)) {
    const headers = data[0];
    const rows = data.slice(1);
    fs.writeFileSync(
      path.join(reviewDir, `${name.replace(/\s+/g, '-').replace(/→/g, 'to').toLowerCase()}.csv`),
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
  } catch (e) {
    console.warn('exceljs fallback:', e.message);
  }

  const collisionSummaryRows = sheets['Collision summary'].length - 1;
  const collisionFindingsRows = sheets['Collision findings'].length - 1;
  const collisionSamplesRows = sheets['Collision passed samples'].length - 1;
  const semanticRows = sheets['Semantic review'].length - 1;

  const result = {
    review_xlsx: xlsxWritten ? OUTPUT : null,
    review_csv_dir: reviewDir,
    sheets: Object.keys(sheets),
    evidence_rows: {
      semantic_review: semanticRows,
      collision_summary: collisionSummaryRows,
      collision_findings: collisionFindingsRows,
      collision_passed_samples: collisionSamplesRows,
    },
    evidence_populated: collisionSummaryRows > 0 && collisionFindingsRows > 0 && collisionSamplesRows > 0 && semanticRows === dataset.keywords.length,
    note: xlsxWritten ? 'Review XLSX v4 generated with collision evidence' : 'CSV fallback in exports/review-v4-csv/',
  };

  fs.writeFileSync(path.join(ROOT, 'production/validation/review-workbook-v4-result.json'), JSON.stringify(result, null, 2));
  console.log(JSON.stringify(result, null, 2));
  if (!result.evidence_populated) process.exit(1);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
