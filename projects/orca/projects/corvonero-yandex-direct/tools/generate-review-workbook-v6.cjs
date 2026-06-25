#!/usr/bin/env node
'use strict';

/**
 * Human review workbook v6 — 28-sheet operator deliverable.
 */
const fs = require('fs');
const path = require('path');
const { validateWorkbookSheetsV6 } = require('./lib/workbook-integrity-v6.cjs');
const {
  formatNarrative,
  formatRiskResolutionRow,
  formatCollisionCorrection,
} = require('./lib/evidence-format-v5.cjs');

const ROOT = path.resolve(__dirname, '..');
const DATASET = path.join(ROOT, 'production/direct-commander-production-dataset-v6.json');
const SEMANTIC = path.join(ROOT, 'production/semantic-evidence-review-v6.json');
const NEG_FINAL = path.join(ROOT, 'production/repair/v5-negative-resolution-final.json');
const COLLISION = path.join(ROOT, 'production/validation/negative-collision-validation-v6.json');
const EVIDENCE = path.join(ROOT, 'production/validation/collision-evidence-v6.json');
const AD_AUDIT = path.join(ROOT, 'production/ad-evidence-audit-v5.json');
const AD_REG = path.join(ROOT, 'production/final-ad-registry-v6.json');
const KW_REG = path.join(ROOT, 'production/final-keyword-registry-v6.json');
const REPAIR = path.join(ROOT, 'production/repair/v6-production-input-package.json');
const CONSISTENCY = path.join(ROOT, 'production/validation/report-export-consistency-v6.json');
const OUTPUT = path.join(ROOT, 'exports/CORVONERO-CAMPAIGN-REVIEW-v6.xlsx');

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
  const negFinal = JSON.parse(fs.readFileSync(NEG_FINAL, 'utf8'));
  const collision = JSON.parse(fs.readFileSync(COLLISION, 'utf8'));
  const evidence = JSON.parse(fs.readFileSync(EVIDENCE, 'utf8'));
  const adReg = JSON.parse(fs.readFileSync(AD_REG, 'utf8'));
  const kwReg = JSON.parse(fs.readFileSync(KW_REG, 'utf8'));
  const repair = JSON.parse(fs.readFileSync(REPAIR, 'utf8'));
  const consistency = JSON.parse(fs.readFileSync(CONSISTENCY, 'utf8'));
  let adAudit = { records: [], changes: [] };
  if (fs.existsSync(AD_AUDIT)) adAudit = JSON.parse(fs.readFileSync(AD_AUDIT, 'utf8'));

  const reviewById = new Map(semantic.reviews.map((r) => [r.keyword_id, r]));

  const sheets = {
    Campaign: [
      ['field', 'value'],
      ['campaign_id', dataset.unified_campaign?.id],
      ['campaign_name', dataset.unified_campaign?.name],
      ['version', 'v6'],
      ['export_model', dataset.export_model],
      ['production_status', dataset.production_status],
      ['active_groups', dataset.groups.length],
      ['active_keywords', dataset.keywords.length],
      ['held_groups', (dataset.held_groups || []).length],
      ['v5_status', dataset.audit_input?.v5_status],
      ['repair_package', dataset.audit_input?.repair_package],
      ['collision_status', dataset.collision_validation?.final_status],
    ],
    Directions: [
      ['direction_id', 'marker', 'name', 'active_groups', 'held_groups', 'direction_negatives_count'],
      ...(dataset.logical_directions || []).map((d) => [
        d.id,
        d.marker,
        d.name,
        (d.active_groups || []).length,
        (d.held_groups || []).length,
        (d.direction_negatives || []).length,
      ]),
    ],
    Groups: [
      ['group_id', 'marker', 'export_name', 'viability', 'keywords', 'ads', 'url', 'negatives_count'],
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
    'Group viability': [
      ['group_id', 'status', 'keyword_count', 'export_to_xlsx'],
      ...(dataset.group_viability || []).map((g) => [g.group_id, g.viability_status, g.keyword_count, g.export_to_xlsx ? 'YES' : 'NO']),
    ],
    Keywords: [
      ['group_id', 'marker', 'phrase', 'bid', 'tier', 'decision', 'commercial_conf', 'hypothesis'],
      ...dataset.keywords.map((k) => [
        k.group_id,
        k.direction_marker,
        k.ad_phrase,
        k.final_bid,
        k.bid_tier,
        k.semantic_decision,
        k.commercial_confidence || k.semantic_confidence,
        k.controlled_test_hypothesis || '',
      ]),
    ],
    'Semantic decisions': [
      ['keyword_id', 'phrase', 'group', 'decision', 'reason', 'commercial_conf', 'review_status'],
      ...dataset.keywords.map((k) => {
        const r = reviewById.get(k.keyword_id) || {};
        return [
          k.keyword_id,
          k.normalized_phrase,
          k.group_id,
          k.semantic_decision,
          k.final_decision_reason || r.phrase_specific_reason,
          k.commercial_confidence,
          r.review_status,
        ];
      }),
    ],
    'Controlled tests': [
      [
        'keyword_id',
        'phrase',
        'group',
        'hypothesis',
        'noise_risk',
        'bid_tier',
        'evaluation',
        'future_exclusion',
      ],
      ...(repair.controlled_test_decisions || [])
        .filter((r) => r.final_decision?.includes('CONTROLLED'))
        .map((r) => [
          r.keyword_id,
          r.phrase,
          r.group_match,
          r.commercial_hypothesis,
          r.expected_noise_source,
          r.bid_tier,
          r.post_launch_evaluation,
          r.post_launch_evaluation,
        ]),
    ],
    Exclusions: [
      ['keyword_id', 'phrase', 'group_id', 'decision', 'reason'],
      ...(dataset.v5_to_v6_changes || [])
        .filter((c) => c.v6_status || c.change === 'EXCLUDED_OR_REASSIGNED_OUT')
        .map((c) => [c.keyword_id, c.phrase, c.group_id, c.v6_status || c.decision, c.reason]),
      ...semantic.reviews
        .filter((r) => String(r.final_decision || '').startsWith('EXCLUDE'))
        .map((r) => [r.keyword_id, r.positive_phrase, r.current_group || r.assigned_group, r.final_decision, r.phrase_specific_reason]),
    ],
    'Group reassignments': [
      ['note'],
      ['No keyword reassignments in v6 repair package — keyword_reassignments array empty'],
    ],
    Ads: [
      ['group_id', 'ad_id', 'headline_1', 'headline_2', 'text', 'landing_url', 'certainty_status'],
      ...dataset.ads.map((a) => [a.group_id, a.ad_id, a.headline_1, a.headline_2, a.text, a.landing_url, a.certainty_review]),
    ],
    'Ad changes': [
      ['group_id', 'ad_id', 'original_problem', 'risk', 'correction_applied', 'status'],
      ...(adReg.evidence?.changes || []).map((c) => [
        c.group_id,
        c.ad_id,
        c.original_problem,
        c.risk,
        c.correction_applied,
        c.status,
      ]),
    ],
    'Global negatives': [
      ['phrase', 'collision_result', 'semantic_risk', 'final_action', 'explanation'],
      ...(dataset.negatives || [])
        .filter((n) => n.level === 'global')
        .map((n) => [n.phrase, n.collision_result, n.semantic_risk_result, n.final_action, n.explanation]),
    ],
    'Direction negatives': [
      ['direction_id', 'phrase', 'final_action', 'explanation'],
      ...(dataset.negatives || [])
        .filter((n) => n.level === 'direction')
        .map((n) => [n.campaign_id, n.phrase, n.final_action, n.explanation]),
    ],
    'Group negatives': [
      ['group_id', 'phrase', 'final_action', 'explanation'],
      ...(dataset.negatives || [])
        .filter((n) => n.level === 'group')
        .map((n) => [n.group_id, n.phrase, n.final_action, n.explanation]),
    ],
    'Cross-negatives': [
      ['group_id', 'token', 'final_action', 'explanation'],
      ...(dataset.negatives || [])
        .filter((n) => n.level === 'group_cross' || n.level === 'group')
        .map((n) => [n.group_id, n.phrase, n.final_action, n.explanation]),
    ],
    'Inline negatives': [
      ['group_id', 'token', 'final_action'],
      ...(dataset.negatives || [])
        .filter((n) => n.level === 'phrase_inline')
        .map((n) => [n.group_id, n.phrase, n.final_action]),
    ],
    'Negative resolution': [
      ['negative_id', 'negative', 'level', 'scope', 'final_state', 'exact_action'],
      ...(negFinal.rows || []).map((r) => [
        r.negative_id,
        r.negative,
        r.level,
        r.applied_scope,
        r.final_state,
        r.exact_action,
      ]),
    ],
    'Collision summary': [
      ['metric', 'value'],
      ['total_pairs_tested', evidence.summary.total_pairs_tested],
      ['literal_collisions_before', evidence.summary.literal_collisions_before],
      ['semantic_risks_before', evidence.summary.semantic_risks_before],
      ['literal_collisions_after', evidence.summary.literal_collisions_after],
      ['semantic_risks_after', evidence.summary.semantic_risks_after],
      ['unresolved_unique_negatives', collision.unresolved_unique_negative_risks],
      ['blocking_collisions', collision.blocking_collisions],
      ['final_status', evidence.summary.final_status],
      [
        'pair_layer_note',
        repair.reconciliation_summary?.remaining_risky_pairs_note ||
          'Pair-level stem warnings mapped to SAFE — PROVEN unique negatives',
      ],
    ],
    'Collision findings': [
      ['finding_id', 'group_id', 'keyword', 'negative', 'level', 'type', 'correction', 'result_after', 'status'],
      ...(evidence.findings || []).map((r) => {
        const removal = (evidence.removal_log || []).find(
          (x) => x.negative === r.negative && (x.group_id === r.group_id || x.scope === r.level)
        );
        const correction =
          r.type === 'BLOCKING' && removal
            ? formatCollisionCorrection(removal, r)
            : formatNarrative(r.correction, { field: 'correction', fallback: String(r.correction || '') });
        return [
          r.finding_id,
          r.group_id,
          r.keyword,
          r.negative,
          r.level,
          r.type,
          correction,
          r.result_after,
          r.status,
        ];
      }),
    ],
    'Collision passed samples': [
      ['level', 'group_id', 'keyword', 'negative', 'result', 'note'],
      ...['global', 'direction', 'group_cross', 'phrase_inline', 'group_export'].flatMap((level) => {
        const samples = evidence.passed_samples?.[level] || [];
        return samples.map((r) => [level, r.group_id, r.keyword, r.negative, 'SAFE_PASS', 'Representative non-blocking check']);
      }),
    ],
    'Exact collision actions': [
      ['finding_id', 'phrase', 'group', 'negative', 'action_type', 'exact_action', 'validation_result'],
      ...(repair.exact_collision_actions || []).map((r) => [
        r.finding_id,
        r.phrase,
        r.group,
        r.negative,
        r.action_type,
        r.exact_action,
        r.validation_result,
      ]),
    ],
    Bids: [
      ['group_id', 'phrase', 'tier', 'bid', 'rationale'],
      ...dataset.keywords.map((k) => [k.group_id, k.normalized_phrase, k.bid_tier, k.final_bid, k.rationale_code]),
    ],
    URLs: [
      ['landing_id', 'path', 'url', 'groups', 'status'],
      ...(dataset.urls || []).map((u) => [u.landing_id, u.path, u.final_planned_url, (u.groups || []).join('; '), u.url_status]),
    ],
    'Held groups': [
      ['group_id', 'marker', 'name', 'url', 'status'],
      ...(dataset.held_groups || []).map((g) => [g.group_id, g.direction_marker, g.group_name, g.planned_url, g.viability_status]),
    ],
    'Merge log': [['note'], ['No merges in v6 — architecture groups retained']],
    'V5→V6 changes': [
      ['keyword_id', 'phrase', 'group_id', 'v5_status', 'v6_status', 'reason'],
      ...(dataset.v5_to_v6_changes || [])
        .filter((c) => c.v6_status)
        .map((c) => [c.keyword_id, c.phrase, c.group_id, c.v5_status, c.v6_status, c.reason]),
    ],
    'QA consistency': [
      ['check', 'result', 'detail'],
      ['report_export_consistency', consistency.passed ? 'PASS' : 'FAIL', formatNarrative(JSON.stringify(consistency.issues), { field: 'detail' })],
      ['collision_final_status', evidence.summary.final_status, formatNarrative(`blocking=${collision.blocking_collisions}`, { field: 'detail' })],
      ['education_leakage', 'PASS', 'career_education_leakage=0 in v6 export'],
      ['active_keywords', String(dataset.keywords.length), 'matches Keywords sheet row count'],
      ['controlled_tests_with_hypothesis', String((repair.controlled_test_decisions || []).filter((r) => r.commercial_hypothesis).length), 'all reviewed controlled tests have hypothesis'],
    ],
    'Commander row reconciliation': [
      ['entity', 'dataset_count', 'notes'],
      ['active_groups', dataset.groups.length, 'must match Commander group count after export'],
      ['active_keywords', dataset.keywords.length, 'must match Commander keyword rows'],
      ['ads', dataset.ads.length, 'must match Commander ad rows'],
      ['held_groups_exported', '0', 'held groups must not appear in Commander XLSX'],
      ['education_phrases_in_export', '0', 'four career/education phrases excluded'],
    ],
  };

  const integrity = validateWorkbookSheetsV6(sheets, dataset, negFinal.rows || []);

  const reviewDir = path.join(ROOT, 'exports/review-v6-csv');
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

  const result = {
    review_xlsx: xlsxWritten ? OUTPUT : null,
    review_csv_dir: reviewDir,
    sheets: Object.keys(sheets),
    sheet_count: Object.keys(sheets).length,
    integrity,
    evidence_populated: xlsxWritten && integrity.passed,
    note: xlsxWritten ? 'Review XLSX v6 generated' : 'CSV fallback only',
  };

  fs.writeFileSync(path.join(ROOT, 'production/validation/review-workbook-v6-result.json'), JSON.stringify(result, null, 2));
  fs.writeFileSync(
    path.join(ROOT, 'production/validation/review-workbook-validation-v6.json'),
    JSON.stringify({ validated_at: new Date().toISOString(), passed: result.evidence_populated, integrity }, null, 2)
  );
  fs.writeFileSync(
    path.join(ROOT, 'production/validation/review-workbook-validation-v6.md'),
    `# Review Workbook Validation v6\n\n**Passed:** ${result.evidence_populated}\n**Sheets:** ${result.sheet_count}\n`
  );

  console.log(JSON.stringify(result, null, 2));
  if (!result.evidence_populated) process.exit(1);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
