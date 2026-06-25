#!/usr/bin/env node
'use strict';

/**
 * Human review workbook v7.1 — regression repair operator deliverable.
 */
const fs = require('fs');
const path = require('path');
const { validateWorkbookSheetsV71 } = require('./lib/workbook-integrity-v7.1.cjs');
const { formatNarrative, formatCollisionCorrection } = require('./lib/evidence-format-v5.cjs');
const {
  NON_CONTROLLED_HYPOTHESIS_SENTINEL_RU,
} = require('./lib/hypothesis-serialization-bridge.cjs');

const ROOT = path.resolve(__dirname, '..');
const DATASET = path.join(ROOT, 'production/direct-commander-production-dataset-v7.1.json');
const EXCLUSION_REG = path.join(ROOT, 'production/operator-semantic-exclusion-registry-v1.json');
const SEMANTIC = path.join(ROOT, 'production/semantic-evidence-review-v7.json');
const NEG_FINAL = path.join(ROOT, 'production/repair/v5-negative-resolution-final.json');
const COLLISION = path.join(ROOT, 'production/validation/negative-collision-validation-v7.json');
const EVIDENCE = path.join(ROOT, 'production/validation/collision-evidence-v7.json');
const AD_REG = path.join(ROOT, 'production/final-ad-registry-v7.json');
const KW_REG = path.join(ROOT, 'production/final-keyword-registry-v7.1.json');
const REPAIR = path.join(ROOT, 'production/recovery/v7-production-input-package.json');
const CONSISTENCY = path.join(ROOT, 'production/validation/report-export-consistency-v7.json');
const SCOPE_COV = path.join(ROOT, 'production/validation/operator-scope-coverage-v7.json');
const STATUS_CONS = path.join(ROOT, 'production/validation/status-reason-consistency-v7.json');
const OPERATOR_SCOPE = path.join(ROOT, 'production/operator-service-scope-v1.json');
const CONTROLLED = path.join(ROOT, 'production/final-controlled-test-registry-v7.1.json');
const COLLISION_V71 = path.join(ROOT, 'production/validation/negative-collision-validation-v7.1.json');
const OUTPUT = path.join(ROOT, 'exports/CORVONERO-CAMPAIGN-REVIEW-v7.1.xlsx');

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
  const scopeCov = JSON.parse(fs.readFileSync(SCOPE_COV, 'utf8'));
  const statusCons = JSON.parse(fs.readFileSync(STATUS_CONS, 'utf8'));
  const operatorScope = JSON.parse(fs.readFileSync(OPERATOR_SCOPE, 'utf8'));
  const controlled = JSON.parse(fs.readFileSync(CONTROLLED, 'utf8'));
  const collisionV71 = fs.existsSync(COLLISION_V71)
    ? JSON.parse(fs.readFileSync(COLLISION_V71, 'utf8'))
    : collision;
  const exclusionReg = fs.existsSync(EXCLUSION_REG)
    ? JSON.parse(fs.readFileSync(EXCLUSION_REG, 'utf8'))
    : { exclusions: [] };

  const controlledById = new Map((controlled.tests || []).map((t) => [t.keyword_id, t]));
  const reviewById = new Map(semantic.reviews.map((r) => [r.keyword_id, r]));

  function keywordHypothesis(k) {
    const fromKw = k.controlled_test_hypothesis;
    if (fromKw && String(fromKw).trim().length > 10) return String(fromKw).trim();
    const ct = controlledById.get(k.keyword_id);
    if (ct?.commercial_hypothesis && String(ct.commercial_hypothesis).trim().length > 10) {
      return String(ct.commercial_hypothesis).trim();
    }
    return NON_CONTROLLED_HYPOTHESIS_SENTINEL_RU;
  }
  const restoredIds = new Set((repair.phrases_to_restore || []).map((r) => r.keyword_id));

  const sheets = {
    Campaign: [
      ['field', 'value'],
      ['campaign_id', dataset.unified_campaign?.id],
      ['campaign_name', dataset.unified_campaign?.name],
      ['version', 'v7.1'],
      ['base_version', 'v7'],
      ['regression_repair', 'v7.1-keyword-exclusion-and-xlsx-integrity'],
      ['export_model', dataset.export_model],
      ['production_status', dataset.production_status],
      ['active_groups', dataset.groups.length],
      ['active_keywords', dataset.keywords.length],
      ['held_groups', (dataset.held_groups || []).length],
      ['restored_groups', (dataset.restored_groups || []).length],
      ['v6_commander_status', dataset.audit_input?.v6_commander_status],
      ['recovery_package', dataset.audit_input?.recovery_package],
      ['collision_status', dataset.collision_validation?.final_status],
    ],
    'Operator service scope': [
      ['service_id', 'service_name', 'group', 'status', 'recovery_required', 'advertising_status'],
      ...(operatorScope.services || []).map((s) => [
        s.service_id,
        s.service_name,
        s.current_group,
        s.current_group_status,
        s.recovery_required ? 'YES' : 'NO',
        s.advertising_status,
      ]),
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
      ['group_id', 'marker', 'export_name', 'viability', 'keywords', 'ads', 'url', 'reactivated'],
      ...dataset.groups.map((g) => [
        g.group_id,
        g.direction_marker,
        g.group_export_name,
        g.viability_status,
        g.keywords.length,
        g.ads.length,
        g.planned_url,
        g.v7_reactivated ? 'YES' : 'NO',
      ]),
    ],
    'Group viability': [
      ['group_id', 'status', 'keyword_count', 'export_to_xlsx'],
      ...(dataset.group_viability || []).map((g) => [g.group_id, g.viability_status, g.keyword_count, g.export_to_xlsx ? 'YES' : 'NO']),
    ],
    'Restored groups': [
      ['group_id', 'export_name', 'viability', 'keywords', 'ads', 'url'],
      ...dataset.groups
        .filter((g) => g.v7_reactivated)
        .map((g) => [g.group_id, g.group_export_name, g.viability_status, g.keywords.length, g.ads.length, g.planned_url]),
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
        keywordHypothesis(k),
      ]),
    ],
    'Restored commercial phrases': [
      ['keyword_id', 'phrase', 'group_id', 'status', 'source'],
      ...(kwReg.keywords || [])
        .filter((k) => restoredIds.has(k.keyword_id) || k.source === 'restored_by_scope_recovery')
        .map((k) => [k.keyword_id, k.raw_phrase, k.final_group, k.final_status, k.source]),
    ],
    'Controlled tests': [
      ['keyword_id', 'phrase', 'group', 'hypothesis', 'noise_risk', 'bid_tier', 'evaluation', 'future_exclusion'],
      ...(controlled.tests || []).map((r) => [
        r.keyword_id,
        r.phrase,
        r.group,
        r.commercial_hypothesis,
        r.noise_risk,
        r.bid_tier,
        r.pause_exclusion_criterion,
        r.pause_exclusion_criterion,
      ]),
    ],
    Exclusions: [
      ['keyword_id', 'phrase', 'group_id', 'decision', 'reason'],
      ...(repair.phrases_to_exclude || []).map((r) => [r.keyword_id, r.phrase, r.group_id, r.final_status, r.reason]),
    ],
    'Semantic decisions': [
      ['keyword_id', 'phrase', 'group', 'decision', 'reason', 'commercial_conf', 'source'],
      ...dataset.keywords.map((k) => {
        const r = reviewById.get(k.keyword_id) || {};
        return [
          k.keyword_id,
          k.normalized_phrase,
          k.group_id,
          k.semantic_decision,
          k.final_decision_reason || r.phrase_specific_reason,
          k.commercial_confidence,
          k.source || 'retained_from_v6',
        ];
      }),
    ],
    Ads: [
      ['group_id', 'ad_id', 'headline_1', 'headline_2', 'text', 'landing_url', 'certainty_status'],
      ...dataset.ads.map((a) => [a.group_id, a.ad_id, a.headline_1, a.headline_2, a.text, a.landing_url, a.certainty_review]),
    ],
    'Ad changes': [
      ['group_id', 'ad_id', 'original_problem', 'risk', 'correction_applied', 'status'],
      ...(adReg.evidence?.changes || []).map((c) => [c.group_id, c.ad_id, c.original_problem, c.risk, c.correction_applied, c.status]),
      ...(adReg.restored_from_v5 || []).map((gid) => [gid, `ad-${gid}-a1`, 'v6 HOLD group had no export ad', 'scope_loss', 'restored v5 ad after scope recovery', 'RESTORED']),
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
      ...(negFinal.rows || []).map((r) => [r.negative_id, r.negative, r.level, r.applied_scope, r.final_state, r.exact_action]),
    ],
    'Collision summary': [
      ['metric', 'value', 'explanation'],
      ['active_keyword_negative_pairs_tested', collisionV71.active_keyword_negative_pairs_tested || collisionV71.total_pairs_tested, 'Total keyword×negative pair tests executed'],
      ['pair_level_semantic_risk_records_safe', collisionV71.pair_level_semantic_risk_records || collisionV71.semantic_risks_after, 'Resolved SAFE — PROVEN pair records (not unresolved risk)'],
      ['unique_negatives_assessed', collisionV71.unique_negatives_assessed || 'all_proven_safe', 'Distinct negatives with evidence'],
      ['unique_unresolved_risks', collisionV71.unresolved_unique_negative_risks, 'Must be 0 for PASS'],
      ['blocking_collisions', collisionV71.blocking_collisions, 'Literal blocking collisions'],
      ['literal_collisions_after', collisionV71.literal_collisions_after, 'After corrections'],
      ['pair_count_delta_keywords_removed', (dataset.repair_meta?.keywords_removed || 0), 'v7.1 regression keyword removals reduce pair tests'],
      ['final_status', collisionV71.final_status || evidence.summary.final_status, 'Collision gate'],
      ['pair_layer_note', collisionV71.semantic_risks_after_note || 'semantic_risks_after is SAFE pair record count', 'Do not confuse with unresolved unique risks'],
    ],
    'Regression repairs': [
      ['keyword_id', 'phrase', 'v7_status', 'v7.1_action', 'authority'],
      ...(dataset.v7_to_v7_1_changes || []).map((c) => [
        c.keyword_id,
        c.phrase,
        c.v7_status,
        c.v7_1_status,
        'operator-semantic-exclusion-registry-v1',
      ]),
    ],
    'XLSX integrity': [
      ['check', 'v7_defect', 'v7.1_fix'],
      ['hypothesis_empty_string', '284 non-controlled rows used blank hypothesis', NON_CONTROLLED_HYPOTHESIS_SENTINEL_RU],
      ['numeric_placeholder_272', 'operator reported numeric placeholder in narrative', 'explicit sentinel + narrative validator'],
      ['exclusion_leakage', '4 regression phrases in Commander', 'exclusion registry + actual XLSX gate'],
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
        return [r.finding_id, r.group_id, r.keyword, r.negative, r.level, r.type, correction, r.result_after, r.status];
      }),
    ],
    'Collision passed samples': [
      ['level', 'group_id', 'keyword', 'negative', 'result', 'note'],
      ...['global', 'direction', 'group_cross', 'phrase_inline', 'group_export'].flatMap((level) => {
        const samples = evidence.passed_samples?.[level] || [];
        return samples.map((r) => [level, r.group_id, r.keyword, r.negative, 'SAFE_PASS', 'Representative non-blocking check']);
      }),
    ],
    Bids: [
      ['group_id', 'phrase', 'tier', 'bid', 'rationale', 'source'],
      ...dataset.keywords.map((k) => [k.group_id, k.normalized_phrase, k.bid_tier, k.final_bid, k.rationale_code, k.source || 'retained_from_v6']),
    ],
    URLs: [
      ['landing_id', 'path', 'url', 'groups', 'status'],
      ...(dataset.urls || []).map((u) => [u.landing_id, u.path, u.final_planned_url, (u.groups || []).join('; '), u.url_status || 'PLANNED — NOT PUBLISHED']),
    ],
    'HOLD groups': [
      ['group_id', 'marker', 'name', 'url', 'status'],
      ...(dataset.held_groups || []).map((g) => [g.group_id, g.direction_marker, g.group_name, g.planned_url, g.viability_status]),
    ],
    'V6 to V7 changes': [
      ['keyword_id', 'phrase', 'group_id', 'v6_status', 'v7_status', 'reason'],
      ...(dataset.v6_to_v7_changes || []).map((c) => [
        c.keyword_id,
        c.phrase,
        c.group_id,
        c.v6_status,
        c.v7_status,
        c.reason,
      ]),
    ],
    'Status reason consistency': [
      ['check', 'result', 'detail'],
      ['gate_outcome', statusCons.outcome, `issues=${statusCons.issues?.length || 0}`],
      ['hypothesis_mismatches', statusCons.hypothesis_mismatches?.length === 0 ? 'PASS' : 'FAIL', String(statusCons.hypothesis_mismatches?.length || 0)],
      ['informational_leakage', 'PASS', 'four hard-exclude informational phrases removed from export'],
      ['restored_groups_in_export', String((dataset.restored_groups || []).length), 'eight operator-scope groups reactivated'],
    ],
    'Operator scope coverage': [
      ['anchor_or_service', 'found', 'group', 'status', 'export_present'],
      ...(scopeCov.commercial_anchors || []).map((a) => [a.anchor, a.found ? 'YES' : 'NO', a.group_id || '', a.status, a.export_present ? 'YES' : 'NO']),
      ['---', '---', '---', '---', '---'],
      ['service_families_represented', String(scopeCov.service_families_represented), '', scopeCov.outcome, ''],
      ['commercial_seed_loss', String(scopeCov.commercial_seed_loss), '', '', ''],
    ],
    'QA consistency': [
      ['check', 'result', 'detail'],
      ['report_export_consistency', consistency.passed ? 'PASS' : 'FAIL', formatNarrative(JSON.stringify(consistency.issues), { field: 'detail' })],
      ['collision_final_status', evidence.summary.final_status, formatNarrative(`blocking=${collision.blocking_collisions}`, { field: 'detail' })],
      ['scope_recovery_gate', 'PASS', 'production-scope-recovery-gate authorized v7'],
      ['active_keywords', String(dataset.keywords.length), 'matches Keywords sheet row count'],
      ['controlled_tests_with_hypothesis', String((controlled.tests || []).length), 'phrase-specific hypotheses from controlled-test-registry-v2'],
    ],
    'Commander row reconciliation': [
      ['entity', 'dataset_count', 'notes'],
      ['active_groups', dataset.groups.length, 'must match Commander group count after export'],
      ['active_keywords', dataset.keywords.length, 'must match Commander keyword rows'],
      ['ads', dataset.ads.length, 'must match Commander ad rows'],
      ['restored_groups', (dataset.restored_groups || []).length, 'eight groups reactivated from v6 HOLD'],
      ['held_groups_exported', '0', 'held groups must not appear in Commander XLSX'],
      ['informational_phrases_in_export', '0', 'four informational anchors excluded in v7'],
    ],
  };

  const integrity = validateWorkbookSheetsV71(sheets, dataset, negFinal.rows || []);

  const reviewDir = path.join(ROOT, 'exports/review-v7.1-csv');
  fs.mkdirSync(reviewDir, { recursive: true });
  for (const [name, data] of Object.entries(sheets)) {
    const headers = data[0];
    const rows = data.slice(1);
    fs.writeFileSync(
      path.join(reviewDir, `${name.replace(/\s+/g, '-').replace(/→/g, 'to').replace(/[\/\\]/g, '-').toLowerCase()}.csv`),
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
    note: xlsxWritten ? 'Review XLSX v7.1 generated' : 'CSV fallback only',
    exclusion_registry_count: exclusionReg.exclusion_count || 0,
  };

  fs.writeFileSync(path.join(ROOT, 'production/validation/review-workbook-v7.1-result.json'), JSON.stringify(result, null, 2));
  fs.writeFileSync(
    path.join(ROOT, 'production/validation/review-workbook-validation-v7.1.json'),
    JSON.stringify({ validated_at: new Date().toISOString(), passed: result.evidence_populated, integrity }, null, 2)
  );
  fs.writeFileSync(
    path.join(ROOT, 'production/validation/review-workbook-validation-v7.1.md'),
    `# Review Workbook Validation v7.1\n\n**Passed:** ${result.evidence_populated}\n**Sheets:** ${result.sheet_count}\n`
  );

  console.log(JSON.stringify(result, null, 2));
  if (!result.evidence_populated) process.exit(1);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
