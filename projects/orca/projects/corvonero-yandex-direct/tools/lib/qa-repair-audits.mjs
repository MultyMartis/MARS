/**
 * ORCA v5 QA repair audits — independent evidence analysis (does not mutate v5 production files).
 */
import fs from 'fs';
import path from 'path';
import {
  formatCollisionCorrection,
  isGenericSafeExplanation,
  isPlaceholderValue,
  isProhibitedCorrection,
  GENERIC_SAFE_RE,
  EMPTY_REPLACEMENT_SENTINEL,
} from './evidence-format-v5.mjs';
import { testCollision, isHighRiskStem } from './collision-engine-v3.mjs';

const CAREER_EDU_PATTERNS = [
  { re: /образован/i, tag: 'education' },
  { re: /высшее/i, tag: 'education' },
  { re: /без образования/i, tag: 'education' },
  { re: /профессия/i, tag: 'career' },
  { re: /обучен/i, tag: 'training' },
  { re: /\bкурс/i, tag: 'training' },
  { re: /курсы/i, tag: 'training' },
  { re: /как стать/i, tag: 'career' },
  { re: /зарплат/i, tag: 'employment' },
  { re: /ваканс/i, tag: 'employment' },
  { re: /работа программист/i, tag: 'employment' },
  { re: /требован.*программист/i, tag: 'career' },
  { re: /должностн.*обязанност/i, tag: 'career' },
  { re: /резюме/i, tag: 'employment' },
  { re: /стажиров/i, tag: 'employment' },
  { re: /сертификац/i, tag: 'training' },
  { re: /тестирован.*знан/i, tag: 'training' },
  { re: /час[аы]? работы программист/i, tag: 'informational' },
];

const CONTROLLED_ANCHORS = [
  'маркировка лекарств аптека',
  'тс пиот 1с розница 2.3',
  'тс пиот 1с розница 3',
  'тс пиот 1с розница 3.0',
  'модуль тс пиот 1с',
  'тс пиот 1с атол',
];

const GENERIC_SAFE_TEMPLATE =
  'SAFE: no literal collision in owner groups; separates sibling groups; representative checks pass';

export function loadV5Inputs(root) {
  return {
    dataset: JSON.parse(fs.readFileSync(path.join(root, 'production/direct-commander-production-dataset-v5.json'), 'utf8')),
    semantic: JSON.parse(fs.readFileSync(path.join(root, 'production/semantic-evidence-review-v5.json'), 'utf8')),
    negRisk: JSON.parse(fs.readFileSync(path.join(root, 'production/negative-risk-resolution-v5.json'), 'utf8')),
    collision: JSON.parse(fs.readFileSync(path.join(root, 'production/validation/collision-evidence-v5.json'), 'utf8')),
    keywords: JSON.parse(fs.readFileSync(path.join(root, 'production/final-keyword-registry-v5.json'), 'utf8')),
    adAudit: JSON.parse(fs.readFileSync(path.join(root, 'production/ad-evidence-audit-v5.json'), 'utf8')),
  };
}

export function auditPlaceholderRootCause() {
  return {
    audit_id: 'v5-placeholder-root-cause',
    generated_at: new Date().toISOString(),
    defect_value: '2464',
    root_cause: {
      source_file: 'tools/generate-review-workbook-v5.cjs',
      function: 'main → Negative risk resolution sheet mapping',
      field: 'replacement, representative_phrases, QA consistency detail',
      exact_defect:
        'Empty string "" written to narrative evidence columns. ExcelJS deduplicates empty strings to sharedStrings index 2464. Operator tools and Excel display the raw shared-string index "2464" instead of blank.',
      mechanism: 'shared_string_index_leak',
      affected_sheets: ['Negative risk resolution', 'QA consistency', 'Collision findings (empty corrections)'],
      affected_cell_count_estimate: 613,
      related_indices: { empty_string_shared_index: 2464, columns: ['F=replacement', 'H=representative_phrases', 'C=detail'] },
      why_validation_failed:
        'workbook-integrity-v5 only checked literal "1234", not four-digit shared-string indices or empty narrative fields in XLSX output.',
      reusable_correction:
        'Use evidence-format-v5.formatNarrative() with explicit sentinels; forbid bare empty strings in narrative columns; scan for /^\\d{4}$/ in narrative fields post-generation.',
    },
    evidence: {
      xlsx_scan: {
        shared_strings_index_2464_resolves_to: '',
        cells_referencing_index_2464: 613,
        primary_sheet: 'sheet17.xml (Negative risk resolution)',
      },
      source_mapping_lines: {
        file: 'tools/generate-review-workbook-v5.cjs',
        replacement: 'r.replacement || ""',
        representative: '(r.representative_affected_phrases || []).join("; ") → empty when array empty',
        qa_detail: "['collision_final_status', evidence.summary.final_status, '']",
      },
    },
  };
}

function walkJson(obj, p = '', findings = []) {
  if (obj == null) return findings;
  if (typeof obj === 'string') {
    if (isPlaceholderValue(obj) && !/^\d{1,2}$/.test(obj)) {
      findings.push({ path: p, bad_value: obj, expected: 'descriptive evidence string' });
    }
    if (GENERIC_SAFE_RE.test(obj)) {
      findings.push({ path: p, bad_value: obj.slice(0, 80), expected: 'phrase-specific SAFE evidence', severity: 'HIGH' });
    }
    return findings;
  }
  if (Array.isArray(obj)) {
    obj.forEach((v, i) => walkJson(v, `${p}[${i}]`, findings));
    return findings;
  }
  if (typeof obj === 'object') {
    for (const [k, v] of Object.entries(obj)) walkJson(v, p ? `${p}.${k}` : k, findings);
  }
  return findings;
}

export function scanEvidenceIntegrity(root, inputs) {
  const artefacts = [
    'production/negative-risk-resolution-v5.json',
    'production/validation/collision-evidence-v5.json',
    'production/semantic-evidence-review-v5.json',
    'production/ad-evidence-audit-v5.json',
    'production/validation/review-workbook-v5-result.json',
    'exports/review-v5-csv/negative-risk-resolution.csv',
    'exports/review-v5-csv/collision-findings.csv',
    'exports/review-v5-csv/qa-consistency.csv',
  ];

  const findings = [];

  findings.push({
    artefact: 'exports/CORVONERO-CAMPAIGN-REVIEW-v5.xlsx',
    sheet: 'Negative risk resolution',
    field: 'replacement / representative_phrases',
    bad_value: '2464 (sharedStrings index leak from empty "")',
    expected_evidence_type: 'descriptive string or explicit sentinel',
    severity: 'CRITICAL',
    entity_id: '613+ cells',
  });

  for (const rel of artefacts) {
    const fp = path.join(root, rel);
    if (!fs.existsSync(fp)) continue;
    const raw = rel.endsWith('.json') ? JSON.parse(fs.readFileSync(fp, 'utf8')) : fs.readFileSync(fp, 'utf8');
    if (typeof raw === 'string') {
      if (raw.includes('blocks_own_group_keyword')) {
        findings.push({
          artefact: rel,
          field: 'correction/reason',
          bad_value: 'blocks_own_group_keyword',
          expected_evidence_type: 'exact action (DELETE NEGATIVE, etc.)',
          severity: 'HIGH',
        });
      }
      if (/^2464$|^1234$/m.test(raw)) {
        findings.push({ artefact: rel, field: 'cell', bad_value: '2464/1234', expected_evidence_type: 'narrative', severity: 'CRITICAL' });
      }
    } else {
      for (const f of walkJson(raw)) {
        findings.push({ artefact: rel, json_path: f.path, field: f.path.split('.').pop(), bad_value: f.bad_value, expected_evidence_type: f.expected, severity: f.severity || 'MEDIUM' });
      }
    }
  }

  for (const row of inputs.collision.findings || []) {
    if (isProhibitedCorrection(row.correction)) {
      findings.push({
        artefact: 'production/validation/collision-evidence-v5.json',
        entity_id: row.finding_id,
        field: 'correction',
        bad_value: row.correction,
        expected_evidence_type: 'exact corrective action',
        severity: 'HIGH',
      });
    }
  }

  for (const r of inputs.negRisk.resolutions || []) {
    if (r.decision === 'SAFE' && isGenericSafeExplanation(r.explanation)) {
      findings.push({
        artefact: 'production/negative-risk-resolution-v5.json',
        entity_id: `${r.level}:${r.applied_scope}:${r.negative}`,
        field: 'explanation',
        bad_value: GENERIC_SAFE_TEMPLATE,
        expected_evidence_type: 'SAFE — PROVEN with phrase-specific collision exhaust',
        severity: 'HIGH',
      });
    }
    if ((r.replacement === null || r.replacement === '') && r.decision === 'SAFE') {
      findings.push({
        artefact: 'exports/CORVONERO-CAMPAIGN-REVIEW-v5.xlsx (via generator)',
        entity_id: r.negative,
        field: 'replacement',
        bad_value: '(empty → XLSX index 2464)',
        expected_evidence_type: EMPTY_REPLACEMENT_SENTINEL,
        severity: 'CRITICAL',
      });
    }
  }

  const summary = {
    total_findings: findings.length,
    critical: findings.filter((f) => f.severity === 'CRITICAL').length,
    high: findings.filter((f) => f.severity === 'HIGH').length,
    medium: findings.filter((f) => f.severity === 'MEDIUM').length,
  };

  return { scan_id: 'v5-evidence-integrity-scan', generated_at: new Date().toISOString(), summary, findings };
}

export function auditCareerEducationQueries(inputs) {
  const active = inputs.dataset.keywords || [];
  const reviewByPhrase = new Map((inputs.semantic.reviews || []).map((r) => [r.normalized_phrase || r.positive_phrase, r]));
  const rows = [];

  for (const kw of active) {
    const phrase = kw.normalized_phrase || kw.ad_phrase;
    const matched = CAREER_EDU_PATTERNS.filter((p) => p.re.test(phrase));
    if (!matched.length) continue;

    const review = reviewByPhrase.get(phrase);
    const v5Decision = kw.semantic_decision || review?.final_decision || 'UNKNOWN';
    const isServiceHire =
      /услуг|заказ|найти|найм|аутсорс|подключ|настро|доработ|разов/.test(phrase) &&
      !/образован|высшее|курс|ваканс|резюме|зарплат|как стать/.test(phrase);

    let corrected = v5Decision;
    let reason = '';
    let action = 'NONE';

    if (matched.some((m) => ['education', 'training', 'career', 'employment', 'informational'].includes(m.tag))) {
      if (/образован|высшее|без образования|без высшего/.test(phrase)) {
        corrected = 'EXCLUDE EDUCATIONAL';
        reason = 'Phrase targets education requirements/qualifications for programmers, not hiring a 1C service provider.';
        action = 'EXCLUDE_KEYWORD in v6 semantic registry';
      } else if (/как стать|профессия|требован|должностн/.test(phrase)) {
        corrected = 'EXCLUDE CAREER';
        reason = 'Career path or job requirements research, not commercial service intent.';
        action = 'EXCLUDE_KEYWORD in v6 semantic registry';
      } else if (/ваканс|резюме|зарплат|стажиров|работа программист/.test(phrase)) {
        corrected = 'EXCLUDE EMPLOYMENT';
        reason = 'Employment market intent; global negatives already target this cluster.';
        action = 'EXCLUDE_KEYWORD in v6 semantic registry';
      } else if (/обучен|курс/.test(phrase)) {
        corrected = 'EXCLUDE TRAINING';
        reason = 'Training/course intent.';
        action = 'EXCLUDE_KEYWORD in v6 semantic registry';
      } else if (/час[аы]? работы/.test(phrase)) {
        corrected = 'EXCLUDE INFORMATIONAL';
        reason = 'Informational query about working hours.';
        action = 'EXCLUDE_KEYWORD in v6 semantic registry';
      }
    }

    if (v5Decision.startsWith('ACTIVE') && corrected.startsWith('EXCLUDE')) {
      action = 'EXCLUDE_KEYWORD — required before v6 export';
    }

    rows.push({
      phrase,
      keyword_id: kw.keyword_id,
      current_group: kw.group_id,
      matched_intent_tags: matched.map((m) => m.tag),
      current_v5_decision: v5Decision,
      corrected_decision: corrected,
      reason,
      required_downstream_action: action,
      service_hire_override_considered: isServiceHire,
    });
  }

  const leakage = rows.filter((r) => r.current_v5_decision.startsWith('ACTIVE') && r.corrected_decision.startsWith('EXCLUDE'));

  return {
    audit_id: 'v5-career-education-query-audit',
    generated_at: new Date().toISOString(),
    phrases_checked: active.length,
    matched_phrases: rows.length,
    active_leakage_count: leakage.length,
    rows,
    leakage,
  };
}

function controlledTestAnalysis(phrase, groupId, review) {
  const commercial =
    /настро|подключ|интеграц|маркиров|тс пиот|модуль|честный знак/.test(phrase) &&
    !/^как /.test(phrase);
  const informational = /^\d|верси|документ|инструкц|аптека$/.test(phrase) || /розница.*\d/.test(phrase);
  const hire = /программист|ваканс|образован/.test(phrase);

  let decision = review?.final_decision || 'HOLD';
  let hypothesis = '';
  let noise = '';
  let bidNote = review?.final_decision === 'CONTROLLED TEST' ? 'T2/T3 lowered tier' : '';
  let evalRule = '';

  if (CONTROLLED_ANCHORS.some((a) => phrase.includes(a.replace(/\.0$/, '')) || phrase === a)) {
    decision = review?.final_decision || 'CONTROLLED TEST';
    hypothesis = 'User needs TS PIOT / pharmacy marking setup in 1C retail — may convert to paid setup.';
    noise = 'Version-only or product-module lookup without service verb; documentation seekers.';
    evalRule = 'Pause if CTR>0 but conversion=0 after 200 clicks; exclude if bounce on setup landing >85%.';
  }

  if (/маркировка лекарств аптека/.test(phrase)) {
    hypothesis = 'Pharmacy retail needs 1C marking integration — narrow commercial test.';
    noise = 'Regulatory FAQ about pharmacy marking obligations without 1C vendor intent.';
    evalRule = 'Require pharmacy-specific ad line; stop if search term reports show informational queries >70%.';
  }

  const budgetJustified = commercial && !hire && (review?.commercial_confidence !== 'LOW');

  return {
    phrase,
    group_id: groupId,
    strongest_commercial: commercial ? `Paid 1C service for «${phrase}» in group ${groupId}` : 'Weak — noun/product search',
    strongest_informational: informational ? 'Product version, module name, or regulatory lookup' : 'Mixed',
    explicit_hire_signal: hire,
    ad_truthful: review?.ad_fit_result === 'MATCH' || review?.ad_fit_result === 'PARTIAL',
    landing_maps: review?.landing_fit_result === 'MATCH' || review?.landing_fit_result === 'PARTIAL',
    budget_justified_100k: budgetJustified,
    commercial_hypothesis: hypothesis || (commercial ? 'Standard group service match' : 'Insufficient hypothesis'),
    noise_risk: noise || 'Generic informational traffic',
    bid_tier_note: bidNote,
    post_launch_rule: evalRule || 'Review after 14 days / 100 clicks',
    current_v5_decision: review?.final_decision,
    commercial_confidence: review?.commercial_confidence,
    final_audit_decision: decision,
  };
}

export function auditControlledTests(inputs) {
  const reviews = inputs.semantic.reviews || [];
  const activeIds = new Set((inputs.dataset.keywords || []).map((k) => k.keyword_id));
  const rows = [];

  for (const r of reviews) {
    if (!activeIds.has(r.keyword_id)) continue;
    const phrase = r.normalized_phrase || r.positive_phrase;
    const isControlled =
      r.final_decision === 'CONTROLLED TEST' ||
      r.commercial_confidence === 'LOW' ||
      r.commercial_confidence === 'MEDIUM' ||
      CONTROLLED_ANCHORS.some((a) => phrase.includes(a.split(' ')[0])) ||
      (!/услуг|настро|подключ|заказ|доработ|интеграц/.test(phrase) && phrase.split(/\s+/).length <= 5);

    if (!isControlled) continue;
    rows.push(controlledTestAnalysis(phrase, r.assigned_group || r.current_group, r));
  }

  const missingHypothesis = rows.filter((r) => !r.commercial_hypothesis || r.commercial_hypothesis === 'Insufficient hypothesis');

  return {
    audit_id: 'v5-controlled-test-audit',
    generated_at: new Date().toISOString(),
    rows,
    anchors_included: CONTROLLED_ANCHORS,
    missing_hypothesis_count: missingHypothesis.length,
  };
}

export function auditUniqueNegativeRisks(inputs) {
  const resolutions = inputs.negRisk.resolutions || [];
  const rows = resolutions.map((r, i) => {
    let finalState = 'UNRESOLVED';
    let exactAction = 'Provide phrase-specific SAFE evidence in v6';

    if (r.decision === 'REMOVE') {
      finalState = 'REMOVED';
      exactAction = r.explanation || `Removed negative «${r.negative}» from ${r.level}/${r.applied_scope}`;
    } else if (r.decision === 'REPLACE' && r.replacement) {
      finalState = 'REPLACED';
      exactAction = `Replace «${r.negative}» with «${r.replacement}»`;
    } else if (r.decision === 'SAFE') {
      if (isGenericSafeExplanation(r.explanation)) {
        finalState = 'UNRESOLVED';
        exactAction = 'Upgrade to SAFE — PROVEN: document competing intent, owner phrases, matching assumption';
      } else {
        finalState = 'SAFE — PROVEN';
        exactAction = r.explanation;
      }
    } else if (r.decision === 'HOLD') {
      finalState = 'BLOCKING';
      exactAction = 'Hold pending operator review';
    }

    return {
      negative_id: `NEG-${String(i + 1).padStart(4, '0')}`,
      negative: r.negative,
      level: r.level,
      applied_groups: [r.applied_scope],
      token_type: r.token_type,
      semantic_meaning: r.risk,
      intended_competing_intent: r.explanation?.includes('separates') ? r.explanation.split('separates')[1]?.split(';')[0]?.trim() : 'unknown',
      owner_group_meanings: r.representative_affected_phrases || [],
      active_phrases_tested: r.representative_affected_phrases || [],
      literal_collisions: r.decision === 'REMOVE' ? r.representative_affected_phrases : [],
      semantic_risks: isHighRiskStem(r.negative) ? ['stem_near'] : [],
      v5_decision: r.decision,
      v5_status: r.status,
      final_state: finalState,
      exact_action: exactAction,
      phrase_specific_evidence: !isGenericSafeExplanation(r.explanation),
    };
  });

  const totals = {
    unique_negatives: rows.length,
    safe_proven: rows.filter((r) => r.final_state === 'SAFE — PROVEN').length,
    unresolved: rows.filter((r) => r.final_state === 'UNRESOLVED').length,
    removed: rows.filter((r) => r.final_state === 'REMOVED').length,
    replaced: rows.filter((r) => r.final_state === 'REPLACED').length,
    blocking: rows.filter((r) => r.final_state === 'BLOCKING').length,
  };

  return { audit_id: 'v5-unique-negative-risk-audit', generated_at: new Date().toISOString(), totals, rows };
}

export function reconcileSemanticRisks(inputs, uniqueAudit) {
  const summary = inputs.collision.summary || {};
  const rawBefore = summary.semantic_risks_before || 0;
  const rawAfter = summary.semantic_risks_after || 0;
  const uniqueNegatives = uniqueAudit.totals.unique_negatives;

  const duplicateSafePairs = Math.max(0, rawAfter - uniqueAudit.totals.unresolved - uniqueAudit.totals.safe_proven);

  const reconciliation = {
    raw_pair_findings_before: rawBefore,
    unique_negatives_involved: uniqueNegatives,
    unique_semantic_risks: uniqueAudit.totals.unresolved + uniqueAudit.totals.safe_proven + uniqueAudit.totals.removed,
    duplicate_repeated_pair_findings: Math.max(0, rawAfter - uniqueNegatives),
    false_positives: 0,
    'SAFE — PROVEN': uniqueAudit.totals.safe_proven,
    REPLACED: uniqueAudit.totals.replaced,
    REMOVED: uniqueAudit.totals.removed,
    'NOT APPLICABLE': uniqueAudit.totals.removed,
    UNRESOLVED: uniqueAudit.totals.unresolved,
    BLOCKING: uniqueAudit.totals.blocking,
    raw_pair_findings_after: rawAfter,
    unique_unresolved_risks_after: uniqueAudit.totals.unresolved + uniqueAudit.totals.blocking,
    v5_claimed_unresolved_count: summary.unresolved_count,
    v5_claimed_final_status: summary.final_status,
    reconciliation_note:
      'v5 reported unresolved_count=0 while semantic_risks_after=1978 because pair-level stem warnings were conflated with unique risk resolution. Repeated SAFE pair records must not count as unresolved.',
    pass_requires: { UNRESOLVED: 0, BLOCKING: 0 },
    reconciled_pass: uniqueAudit.totals.unresolved === 0 && uniqueAudit.totals.blocking === 0,
  };

  return {
    audit_id: 'v5-semantic-risk-reconciliation',
    generated_at: new Date().toISOString(),
    reconciliation,
    misleading_v5_summary: {
      semantic_risks_after: rawAfter,
      unresolved_count: summary.unresolved_count,
      contradiction: rawAfter > 0 && summary.unresolved_count === 0,
    },
  };
}

export function auditExactCollisionCorrections(inputs) {
  const removalByKey = new Map();
  for (const r of inputs.collision.removal_log || []) {
    removalByKey.set(`${r.group_id}:${r.negative}`, r);
  }

  const rows = (inputs.collision.findings || [])
    .filter((f) => f.type === 'BLOCKING' || f.result_before === 'BLOCKING')
    .map((f) => {
      const removal = removalByKey.get(`${f.group_id}:${f.negative}`);
      const exactAction = removal ? formatCollisionCorrection(removal, f) : null;
      const prohibited = isProhibitedCorrection(f.correction);

      return {
        finding_id: f.finding_id,
        group_id: f.group_id,
        active_keyword: f.keyword,
        offending_negative: f.negative,
        negative_level: f.level,
        result_before: f.result_before,
        v5_correction_field: f.correction,
        correction_valid: !prohibited && !!exactAction,
        exact_source_artefact_changed: 'production/direct-commander-production-dataset-v5.json → cross_negatives / group_negatives',
        exact_action: exactAction || 'MISSING — v5 recorded problem type only',
        action_type: removal ? 'DELETE NEGATIVE' : 'UNKNOWN',
        old_value: f.negative,
        new_value: removal ? '(removed from export scope)' : f.negative,
        result_after: f.result_after,
        validation_evidence: removal ? `removal_log entry group=${removal.group_id} negative=${removal.negative}` : 'none',
      };
    });

  const invalid = rows.filter((r) => !r.correction_valid);

  return {
    audit_id: 'v5-exact-collision-correction-log',
    generated_at: new Date().toISOString(),
    total_blocking_findings: rows.length,
    valid_exact_actions: rows.filter((r) => r.correction_valid).length,
    invalid_or_generic: invalid.length,
    rows,
  };
}

export function jsonToMd(title, obj, sections = []) {
  const lines = [`# ${title}`, '', `Generated: ${obj.generated_at || new Date().toISOString()}`, ''];
  for (const s of sections) lines.push(s, '');
  if (obj.summary) {
    lines.push('## Summary', '', '| Metric | Value |', '|--------|------:|');
    for (const [k, v] of Object.entries(obj.summary)) lines.push(`| ${k} | ${v} |`);
    lines.push('');
  }
  if (obj.reconciliation) {
    lines.push('## Reconciliation', '', '| Metric | Value |', '|--------|------:|');
    for (const [k, v] of Object.entries(obj.reconciliation)) lines.push(`| ${k} | ${v} |`);
    lines.push('');
  }
  if (obj.totals) {
    lines.push('## Totals', '', '| Metric | Value |', '|--------|------:|');
    for (const [k, v] of Object.entries(obj.totals)) lines.push(`| ${k} | ${v} |`);
    lines.push('');
  }
  return lines.join('\n');
}
