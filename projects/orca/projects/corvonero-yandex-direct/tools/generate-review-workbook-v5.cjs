#!/usr/bin/env node
'use strict';

/**
 * Human review workbook v5 — evidence-populated operator deliverable.
 */
const fs = require('fs');
const path = require('path');
const { validateWorkbookSheets } = require('./lib/workbook-integrity-v5.cjs');
const {
  formatNarrative,
  formatRiskResolutionRow,
  formatCollisionCorrection,
  EMPTY_DETAIL_SENTINEL,
} = require('./lib/evidence-format-v5.cjs');

const ROOT = path.resolve(__dirname, '..');
const DATASET = path.join(ROOT, 'production/direct-commander-production-dataset-v5.json');
const SEMANTIC = path.join(ROOT, 'production/semantic-evidence-review-v5.json');
const GROUP_AUDIT = path.join(ROOT, 'production/group-assignment-audit-v5.json');
const NEG_RISK = path.join(ROOT, 'production/negative-risk-resolution-v5.json');
const COLLISION = path.join(ROOT, 'production/validation/negative-collision-validation-v5.json');
const EVIDENCE = path.join(ROOT, 'production/validation/collision-evidence-v5.json');
const AD_AUDIT = path.join(ROOT, 'production/ad-evidence-audit-v5.json');
const AD_REG = path.join(ROOT, 'production/final-ad-registry-v5.json');
const KW_REG = path.join(ROOT, 'production/final-keyword-registry-v5.json');
const CONSISTENCY = path.join(ROOT, 'production/validation/report-export-consistency-v5.json');
const OUTPUT = path.join(ROOT, 'exports/CORVONERO-CAMPAIGN-REVIEW-v5.xlsx');

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
  const groupAudit = JSON.parse(fs.readFileSync(GROUP_AUDIT, 'utf8'));
  const negRisk = JSON.parse(fs.readFileSync(NEG_RISK, 'utf8'));
  const collision = JSON.parse(fs.readFileSync(COLLISION, 'utf8'));
  const evidence = JSON.parse(fs.readFileSync(EVIDENCE, 'utf8'));
  const adAudit = JSON.parse(fs.readFileSync(AD_AUDIT, 'utf8'));
  const adReg = JSON.parse(fs.readFileSync(AD_REG, 'utf8'));
  const kwReg = JSON.parse(fs.readFileSync(KW_REG, 'utf8'));
  const consistency = JSON.parse(fs.readFileSync(CONSISTENCY, 'utf8'));

  const reviewById = new Map(semantic.reviews.map((r) => [r.keyword_id, r]));

  const sheets = {
    Campaign: [
      ['field', 'value'],
      ['campaign_id', dataset.unified_campaign?.id],
      ['campaign_name', dataset.unified_campaign?.name],
      ['version', 'v5'],
      ['export_model', dataset.export_model],
      ['active_groups', dataset.groups.length],
      ['active_keywords', dataset.keywords.length],
      ['held_groups', (dataset.held_groups || []).length],
      ['v4_audit_status', dataset.audit_input?.v4_status],
      ['semantic_evidence_ref', dataset.semantic_evidence_ref],
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
      ...(dataset.group_viability || []).map((g) => [g.group_id, g.viability_status, g.keyword_count, g.export_to_xlsx]),
    ],
    Keywords: [
      ['group_id', 'marker', 'phrase', 'bid', 'tier', 'decision', 'commercial_conf', 'group_fit'],
      ...dataset.keywords.map((k) => [
        k.group_id,
        k.direction_marker,
        k.ad_phrase,
        k.final_bid,
        k.bid_tier,
        k.semantic_decision,
        k.semantic_confidence,
        k.group_fit_confidence,
      ]),
    ],
    'Semantic evidence review': [
      [
        'keyword_id',
        'phrase',
        'assigned_group',
        'literal_interpretation',
        'user_need',
        'paid_service',
        'alt_interpretation',
        'commercial_conf',
        'group_fit_conf',
        'ad_fit',
        'landing_fit',
        'decision',
        'phrase_reason',
        'review_status',
      ],
      ...dataset.keywords.map((k) => {
        const r = reviewById.get(k.keyword_id) || {};
        return [
          k.keyword_id,
          k.normalized_phrase,
          k.group_id,
          r.literal_interpretation,
          r.likely_user_need,
          r.paid_service_implied,
          r.alternative_interpretation,
          r.commercial_confidence,
          r.group_fit_confidence,
          r.ad_fit_result,
          r.landing_fit_result,
          r.final_decision,
          r.phrase_specific_reason,
          r.review_status,
        ];
      }),
    ],
    Exclusions: [
      ['keyword_id', 'phrase', 'group_id', 'decision', 'reason', 'review_status'],
      ...semantic.reviews
        .filter((r) => r.final_decision.startsWith('EXCLUDE') || r.final_decision === 'HOLD AMBIGUOUS')
        .map((r) => [r.keyword_id, r.positive_phrase, r.current_group, r.final_decision, r.phrase_specific_reason, r.review_status]),
    ],
    'Group reassignments': [
      ['keyword_id', 'phrase', 'previous_group', 'new_group', 'semantic_reason', 'ad_landing_impact', 'negative_impact'],
      ...(groupAudit.reassignments || []).map((r) => [
        r.keyword_id,
        r.phrase,
        r.previous_group,
        r.new_group,
        r.semantic_reason,
        r.ad_landing_impact,
        r.negative_logic_impact,
      ]),
    ],
    Ads: [
      ['group_id', 'ad_id', 'headline_1', 'headline_2', 'text', 'landing_url', 'certainty_status'],
      ...dataset.ads.map((a) => [a.group_id, a.ad_id, a.headline_1, a.headline_2, a.text, a.landing_url, a.certainty_review]),
    ],
    'Ad evidence audit': [
      ['ad_id', 'group_id', 'h1', 'h2', 'text', 'factual_risk', 'certainty_risk', 'unsupported', 'action', 'final_status'],
      ...(adAudit.records || []).map((r) => [
        r.ad_id,
        r.group_id,
        r.current_headline_1,
        r.current_headline_2,
        r.current_text,
        r.factual_risk,
        r.certainty_risk,
        r.unsupported_promise,
        r.exact_action,
        r.final_status,
      ]),
    ],
    'Ad changes': [
      ['group_id', 'ad_id', 'original_problem', 'risk', 'correction_applied', 'final_h1', 'final_h2', 'final_text', 'status'],
      ...(adAudit.changes || []).map((c) => [
        c.group_id,
        c.ad_id,
        c.original_problem,
        c.risk,
        c.correction_applied,
        c.final_headline_1,
        c.final_headline_2,
        c.final_text,
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
        .filter((n) => n.level === 'group')
        .map((n) => [n.group_id, n.phrase, n.final_action, n.explanation]),
    ],
    'Inline negatives': [
      ['group_id', 'token', 'final_action'],
      ...(dataset.negatives || [])
        .filter((n) => n.level === 'phrase_inline')
        .map((n) => [n.group_id, n.phrase, n.final_action]),
    ],
    'Negative risk resolution': [
      ['negative', 'level', 'scope', 'token_type', 'decision', 'replacement', 'risk', 'representative_phrases', 'explanation', 'status'],
      ...(negRisk.resolutions || []).map((r) => {
        const fmt = formatRiskResolutionRow(r);
        return [
          r.negative,
          r.level,
          r.applied_scope,
          r.token_type,
          r.decision,
          fmt.replacement,
          r.risk,
          fmt.representative_phrases,
          fmt.explanation,
          r.status,
        ];
      }),
    ],
    'Collision summary': [
      ['metric', 'value'],
      ['total_pairs_tested', evidence.summary.total_pairs_tested],
      ['literal_collisions_before', evidence.summary.literal_collisions_before],
      ['semantic_risks_before', evidence.summary.semantic_risks_before],
      ['preventive_corrections', evidence.summary.preventive_corrections],
      ['literal_corrections', evidence.summary.literal_corrections],
      ['corrections_applied', evidence.summary.corrections_applied],
      ['literal_collisions_after', evidence.summary.literal_collisions_after],
      ['semantic_risks_after', evidence.summary.semantic_risks_after],
      ['unresolved_count', evidence.summary.unresolved_count],
      ['final_status', evidence.summary.final_status],
    ],
    'Collision findings': [
      ['finding_id', 'group_id', 'keyword', 'negative', 'level', 'type', 'evidence', 'result_before', 'correction', 'result_after', 'status'],
      ...(evidence.findings || []).map((r) => {
        const removal = (evidence.removal_log || []).find(
          (x) => x.negative === r.negative && (x.group_id === r.group_id || x.scope === r.level)
        );
        const correction =
          r.type === 'BLOCKING' && removal
            ? formatCollisionCorrection(removal, r)
            : r.correction
              ? formatNarrative(r.correction, { field: 'correction', fallback: r.correction })
              : formatNarrative('', { field: 'correction' });
        return [
          r.finding_id,
          r.group_id,
          r.keyword,
          r.negative,
          r.level,
          r.type,
          formatNarrative(r.evidence, { field: 'evidence', fallback: String(r.evidence || '') }),
          r.result_before,
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
        return samples.map((r) => [
          level,
          r.group_id,
          r.keyword,
          r.negative,
          'SAFE_PASS',
          'Representative non-blocking check',
        ]);
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
      ...(dataset.urls || []).map((u) => [u.landing_id, u.path, u.final_planned_url, (u.groups || []).join('; '), u.url_status]),
    ],
    'Held groups': [
      ['group_id', 'marker', 'name', 'url', 'status'],
      ...(dataset.held_groups || []).map((g) => [g.group_id, g.direction_marker, g.group_name, g.planned_url, g.viability_status]),
    ],
    'Merge log': [['note'], ['No merges in v5 — architecture groups retained']],
    'V4→V5 change log': [
      ['keyword_id', 'phrase', 'group_id', 'change', 'decision', 'reason'],
      ...(dataset.v4_to_v5_changes || []).slice(0, 500).map((c) => [
        c.keyword_id,
        c.phrase,
        c.group_id,
        c.change,
        c.decision,
        (c.reason || '').slice(0, 200),
      ]),
    ],
    'QA consistency': [
      ['check', 'result', 'detail'],
      [
        'report_export_consistency',
        consistency.passed ? 'PASS' : 'FAIL',
        formatNarrative(JSON.stringify(consistency.issues), { field: 'detail' }),
      ],
      [
        'collision_final_status',
        evidence.summary.final_status,
        formatNarrative(
          `semantic_risks_after=${evidence.summary.semantic_risks_after}; unresolved=${evidence.summary.unresolved_count}`,
          { field: 'detail' }
        ),
      ],
      [
        'negative_risk_unresolved',
        negRisk.summary?.unresolved_count === 0 ? 'PASS' : 'FAIL',
        formatNarrative(String(negRisk.summary?.unresolved_count ?? 'unknown'), { field: 'detail' }),
      ],
      [
        'active_keywords',
        String(dataset.keywords.length),
        formatNarrative('matches Keywords sheet row count', { field: 'detail' }),
      ],
      [
        'risk_resolution_rows',
        String((negRisk.resolutions || []).length),
        formatNarrative('matches Negative risk resolution sheet row count', { field: 'detail' }),
      ],
    ],
  };

  const integrity = validateWorkbookSheets(sheets, dataset, semantic.reviews, negRisk, adAudit);

  const reviewDir = path.join(ROOT, 'exports/review-v5-csv');
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
    evidence_populated: integrity.passed && xlsxWritten,
    note: xlsxWritten ? 'Review XLSX v5 generated with evidence' : 'CSV fallback only',
  };

  fs.writeFileSync(path.join(ROOT, 'production/validation/review-workbook-v5-result.json'), JSON.stringify(result, null, 2));
  fs.writeFileSync(
    path.join(ROOT, 'production/validation/review-workbook-validation-v5.json'),
    JSON.stringify({ validated_at: new Date().toISOString(), passed: result.evidence_populated, integrity }, null, 2)
  );

  console.log(JSON.stringify(result, null, 2));
  if (!result.evidence_populated) process.exit(1);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
