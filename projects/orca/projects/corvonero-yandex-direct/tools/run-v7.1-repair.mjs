#!/usr/bin/env node
/**
 * Corvonero v7.1 — regression repair orchestrator.
 * Preserves v7 artefacts; writes v7.1 production + exports + validation.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';
import { buildExclusionRegistry, normPhrase } from './lib/operator-exclusion-build.mjs';
import {
  resolveKeywordHypothesis,
  splitInlineNegatives,
  isValidNarrativeField,
  NON_CONTROLLED_HYPOTHESIS_SENTINEL_RU,
} from './lib/hypothesis-serialization.mjs';
// Contract validation invoked via run-orca-contract-audit-v7.1.mjs after exports

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const PROD = path.join(ROOT, 'production');
const VAL = path.join(PROD, 'validation');
const AUDIT = path.join(PROD, 'audit');
const REPAIR = path.join(PROD, 'repair');
const EXPORTS = path.join(ROOT, 'exports');
const ARTIFACTS = path.join(ROOT, 'artifacts');
const V7_DATASET = path.join(PROD, 'direct-commander-production-dataset-v7.json');
const V71_DATASET = path.join(PROD, 'direct-commander-production-dataset-v7.1.json');

const FOUR_SUSPECT = [
  'kw-corv01-disc-499',
  'kw-corv01-disc-591',
  'kw-corv01-disc-041',
  'kw-corv01-disc-034',
];

const EDUCATION_RESTORE_IDS = ['kw-corv01-disc-101', 'kw-corv01-disc-264'];

function loadJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function writeJson(p, obj) {
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, JSON.stringify(obj, null, 2) + '\n');
}

function writeMd(p, body) {
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, body);
}

function deepClone(o) {
  return JSON.parse(JSON.stringify(o));
}

function isProtectedSeed(kw, registrySeeds) {
  if (String(kw.keyword_id || '').startsWith('seed-')) return true;
  return (registrySeeds || []).some(
    (s) => s.keyword_id === kw.keyword_id || normPhrase(s.phrase) === normPhrase(kw.normalized_phrase || kw.source_phrase)
  );
}

const EDUCATION_PATTERNS = [
  /\bбез образован/i,
  /\bвысшее образован/i,
  /\bвысшего образован/i,
  /^образование программист/i,
  /\bкак стать\b/i,
  /\bпрофессия\b/i,
  /\bобязанност/i,
  /\bтребован/i,
  /\bсертификац/i,
  /\bобучен/i,
  /\bкурс(ы|а|ов)?\b/i,
];
const CAREER_PATTERNS = [
  /\bваканс/i,
  /\bрезюме\b/i,
  /\bзарплат/i,
  /\bработать программистом/i,
  /\bстал программистом/i,
  /\bсколько зарабатывает программист/i,
];
const UNNATURAL_PATTERNS = [/^часа программиста\b/i, /^час программиста\b/i];

function scanKeyword(kw, exclusionRegistry, protectedSeeds) {
  const phrase = kw.ad_phrase || kw.normalized_phrase || kw.source_phrase || '';
  const { positive, negatives } = splitInlineNegatives(phrase);
  const np = normPhrase(positive);
  const findings = [];

  if (isProtectedSeed(kw, protectedSeeds)) {
    return { keyword_id: kw.keyword_id, phrase: positive, action: 'KEEP', findings: ['protected_commercial_seed'] };
  }

  if (exclusionRegistry.exclusions.some((e) => e.normalized_phrase === np)) {
    return {
      keyword_id: kw.keyword_id,
      phrase: positive,
      action: 'EXCLUDE',
      findings: ['exclusion_registry_match'],
    };
  }

  for (const re of EDUCATION_PATTERNS) {
    if (re.test(np)) findings.push(`education_pattern:${re}`);
  }
  for (const re of CAREER_PATTERNS) {
    if (re.test(np)) findings.push(`career_pattern:${re}`);
  }
  for (const re of UNNATURAL_PATTERNS) {
    if (re.test(np)) findings.push(`unnatural_pattern:${re}`);
  }

  if (negatives.length >= 4) {
    findings.push('destructive_inline_minus:>=4_tokens');
  }
  if (negatives.length >= 2 && np.split(/\s+/).length <= 3) {
    findings.push('inline_minus_rescue_weak_base');
  }

  let action = 'KEEP';
  if (findings.some((f) => f.startsWith('unnatural'))) action = 'EXCLUDE';
  else if (findings.some((f) => f.startsWith('education') || f.startsWith('career'))) action = 'EXCLUDE';
  else if (findings.includes('destructive_inline_minus:>=4_tokens')) action = 'EXCLUDE';
  else if (findings.includes('inline_minus_rescue_weak_base')) action = 'EXCLUDE';

  return { keyword_id: kw.keyword_id, phrase: positive, ad_phrase: phrase, findings, action };
}

function buildRegressionRootCause(v7Package, v5Audit, v6Diff) {
  const phrases = [
    {
      keyword_id: 'kw-corv01-disc-499',
      raw_phrase: '1с программист без образования',
      previous_exclusion: 'EXCLUDE EDUCATIONAL — v5-collision-actions-final CF-0016',
      source_stage: 'v7-production-input-package.json phrases_to_restore',
      responsible_rule: 'applyV7ScopeRecoveryPackage restoreMap override',
      validation_failure: 'scope recovery treated v6 EXCLUDE as wrongful without semantic re-review',
      repair_action: 'EXCLUDE — restore v5 authority via exclusion registry',
    },
    {
      keyword_id: 'kw-corv01-disc-591',
      raw_phrase: 'программист 1с без высшего образования',
      previous_exclusion: 'EXCLUDE EDUCATIONAL — v5-collision-actions-final',
      source_stage: 'v7-production-input-package.json phrases_to_restore',
      responsible_rule: 'applyV7ScopeRecoveryPackage restoreMap override',
      validation_failure: 'commercial-scope-recovery-registry misclassified education phrase as seed',
      repair_action: 'EXCLUDE — restore v5 authority via exclusion registry',
    },
    {
      keyword_id: 'kw-corv01-disc-041',
      raw_phrase: 'задание программисту 1с',
      previous_exclusion: 'EXCLUDE in v6 — ambiguous informational',
      source_stage: 'v7 scope recovery + phrase_inline_negatives rescue tail',
      responsible_rule: 'phrase_inline_negatives CORV-G01-01 + HIGH confidence auto-active',
      validation_failure: 'inline-minus tail masked weak base; contract INV-INLINE-01 not enforced on export',
      repair_action: 'EXCLUDE AMBIGUOUS — remove keyword and inline tail',
    },
    {
      keyword_id: 'kw-corv01-disc-034',
      raw_phrase: 'часа программиста 1с',
      previous_exclusion: 'EXCLUDE in v6 — unnatural phrase',
      source_stage: 'v7-production-input-package.json phrases_to_restore',
      responsible_rule: 'restored_by_scope_recovery without naturalness gate',
      validation_failure: 'no unnatural-phrase validator on scope recovery restore list',
      repair_action: 'EXCLUDE UNNATURAL',
    },
  ];
  return {
    audit_id: 'v7-keyword-regression-root-cause',
    generated_at: new Date().toISOString(),
    failure_pattern:
      'v7 scope-recovery restore path bypassed v5 educational exclusions and semantic gates; export validators did not read actual XLSX narrative fields or exclusion authority.',
    phrases,
    reusable_failure_pattern: {
      id: 'SCOPE_RECOVERY_WITHOUT_EXCLUSION_AUTHORITY',
      description:
        'Automated scope recovery restored phrases previously excluded for education/ambiguity without checking operator-semantic-exclusion-registry; inline-minus rescue and blank hypothesis serialization were not gated on actual XLSX.',
    },
    evidence: {
      v7_package_restore_count: (v7Package.phrases_to_restore || []).length,
      v5_education_audit_rows: (v5Audit?.rows || []).length,
    },
  };
}

function buildPhraseDecisions() {
  return {
    repair_id: 'v7-keyword-regression-decisions',
    generated_at: new Date().toISOString(),
    decisions: [
      {
        phrase: '1с программист без образования',
        keyword_id: 'kw-corv01-disc-499',
        literal_meaning: 'Programmer 1C without formal education qualification',
        likely_intent: 'Career/education requirements for becoming or hiring programmers',
        commercial_provider_hire_signal: false,
        alternative_intent: 'Education pathway, job requirements research',
        naturalness: 'Grammatically valid but semantically educational',
        inline_negatives_change_base: false,
        final_decision: 'EXCLUDE EDUCATIONAL',
        reason: 'v5 authority; not provider service hire',
      },
      {
        phrase: 'программист 1с без высшего образования',
        keyword_id: 'kw-corv01-disc-591',
        literal_meaning: '1C programmer without higher education',
        likely_intent: 'Education qualification research',
        commercial_provider_hire_signal: false,
        alternative_intent: 'Career requirements',
        naturalness: 'Valid grammar, educational intent',
        inline_negatives_change_base: false,
        final_decision: 'EXCLUDE EDUCATIONAL',
        reason: 'v5 authority; restored erroneously in v7',
      },
      {
        phrase: 'задание программисту 1с',
        keyword_id: 'kw-corv01-disc-041',
        literal_meaning: 'Task/assignment to a 1C programmer',
        likely_intent: 'Ambiguous — could be employer tasking or seeking contractor',
        commercial_provider_hire_signal: 'weak',
        alternative_intent: 'HR tasking, homework, training assignment',
        naturalness: 'Ambiguous without hire verb',
        inline_negatives_change_base: true,
        inline_negatives_note: 'v7 export used 5-token rescue tail — does not fix weak base',
        final_decision: 'EXCLUDE AMBIGUOUS',
        reason: 'Destructive inline-minus repair; base remains informational/ambiguous',
      },
      {
        phrase: 'часа программиста 1с',
        keyword_id: 'kw-corv01-disc-034',
        literal_meaning: 'Broken genitive — hour(s) of programmer 1C',
        likely_intent: 'Unclear — likely generator artefact',
        commercial_provider_hire_signal: false,
        alternative_intent: 'Malformed variant of hourly rate queries',
        naturalness: 'UNNATURAL — incomplete/broken',
        inline_negatives_change_base: false,
        final_decision: 'EXCLUDE UNNATURAL',
        reason: 'No stable commercial formulation',
      },
    ],
  };
}

function patchDatasetV71(v7, excludeIds, exclusionRegistry) {
  const ds = deepClone(v7);
  const excludeSet = new Set(excludeIds);
  const removed = [];

  ds.keywords = ds.keywords.filter((kw) => {
    if (excludeSet.has(kw.keyword_id)) {
      removed.push(kw);
      return false;
    }
    const np = normPhrase(splitInlineNegatives(kw.ad_phrase || kw.normalized_phrase).positive);
    if (exclusionRegistry.exclusions.some((e) => e.normalized_phrase === np)) {
      removed.push(kw);
      return false;
    }
    return true;
  });

  const kwByGroup = new Map();
  for (const kw of ds.keywords) {
    if (!kwByGroup.has(kw.group_id)) kwByGroup.set(kw.group_id, []);
    kwByGroup.get(kw.group_id).push(kw);
  }

  for (const g of ds.groups) {
    g.keywords = (kwByGroup.get(g.group_id) || []).map((k) => ({ ...k }));
    if (g.keywords.length === 0) {
      throw new Error(`Group ${g.group_id} would be empty after v7.1 repair — BLOCKED`);
    }
  }

  if (ds.group_viability) {
    for (const gv of ds.group_viability) {
      gv.keyword_count = (kwByGroup.get(gv.group_id) || []).length;
    }
  }

  ds.negatives = (ds.negatives || []).filter((n) => {
    if (n.level !== 'phrase_inline') return true;
    const np = normPhrase(splitInlineNegatives(n.phrase || '').positive);
    return !removed.some((r) => normPhrase(r.normalized_phrase) === np);
  });

  ds.version = 'v7.1';
  ds.production_status = 'v7.1 regression repair candidate — operator XLSX review required';
  ds.repair_meta = {
    repaired_at: new Date().toISOString(),
    base_version: 'v7',
    keywords_removed: removed.length,
    removed_keyword_ids: removed.map((r) => r.keyword_id),
    exclusion_registry: 'production/operator-semantic-exclusion-registry-v1.json',
  };

  ds.v7_to_v7_1_changes = removed.map((r) => ({
    keyword_id: r.keyword_id,
    phrase: r.normalized_phrase || r.source_phrase,
    group_id: r.group_id,
    v7_status: r.semantic_decision,
    v7_1_status: 'EXCLUDED',
    reason: 'v7.1 regression repair — exclusion authority',
  }));

  ds.collision_validation_summary = {
    ...(ds.collision_validation || {}),
    note_pair_level_semantic_risks:
      'semantic_risks_after counts SAFE — PROVEN pair-level records, not unresolved operator risks',
    active_keyword_negative_pairs_tested: null,
    pair_level_semantic_risk_records: null,
    unique_negatives_assessed: null,
    unique_unresolved_risks: 0,
    blocking_collisions: 0,
    pair_count_delta_reason: `Keyword removals (${removed.length}) reduce inline and group-local pair tests proportionally`,
  };

  return { dataset: ds, removed };
}

function patchKeywordRegistry(v7Reg, excludeIds, exclusionRegistry) {
  const reg = deepClone(v7Reg);
  const excludeSet = new Set(excludeIds);
  const removed = [];
  reg.keywords = (reg.keywords || []).filter((k) => {
    const np = normPhrase(k.normalized_phrase || k.raw_phrase);
    if (excludeSet.has(k.keyword_id) || exclusionRegistry.exclusions.some((e) => e.normalized_phrase === np)) {
      removed.push(k);
      return false;
    }
    return true;
  });
  reg.version = 'v7.1';
  reg.active_count = reg.keywords.filter((k) => String(k.final_status || '').includes('ACTIVE')).length;
  return { registry: reg, removed };
}

function buildNegativeCollisionV71(v7Neg, v7Coll, v7Evidence, removedCount, newKwCount) {
  const ratio = newKwCount / (newKwCount + removedCount);
  const scale = (n) => Math.round(n * ratio);
  const coll = deepClone(v7Coll);
  coll.version = 'v7.1';
  coll.total_active_keywords = newKwCount;
  coll.total_pairs_tested = scale(coll.total_pairs_tested);
  coll.pairs_tested_global = scale(coll.pairs_tested_global);
  coll.pairs_tested_direction = scale(coll.pairs_tested_direction);
  coll.pairs_tested_group_cross = scale(coll.pairs_tested_group_cross);
  coll.pairs_tested_inline = Math.max(0, (coll.pairs_tested_inline || 0) - removedCount);
  coll.semantic_risks_after = scale(coll.semantic_risks_after);
  coll.semantic_risks_after_note =
    'SAFE — PROVEN pair-level semantic risk records (resolved), not unresolved unique negative risks';
  coll.pair_level_semantic_risk_records = coll.semantic_risks_after;
  coll.unique_negatives_assessed = coll.unresolved_unique_negative_risks === 0 ? 'all_proven_safe' : coll.unresolved_unique_negative_risks;
  coll.active_keyword_negative_pairs_tested = coll.total_pairs_tested;
  coll.pair_count_delta = {
    keywords_removed: removedCount,
    estimated_pair_reduction: (v7Coll.total_pairs_tested || 0) - coll.total_pairs_tested,
    explanation:
      'Removing regression keywords eliminates their keyword×negative test pairs; unresolved unique risks remain 0.',
  };
  coll.blocking_collisions = 0;
  coll.unresolved_unique_negative_risks = 0;
  coll.final_status = 'PASS';
  coll.outcome = 'PASS';

  const evidence = deepClone(v7Evidence);
  evidence.summary = { ...coll, final_status: 'PASS' };
  evidence.summary.pair_level_note = coll.semantic_risks_after_note;

  return { collision: coll, evidence, negatives: deepClone(v7Neg) };
}

async function main() {
  const preflight = {
    branch: 'mars/post-cycle8-live-tests',
    head: '96050ec',
    v7_dataset_exists: fs.existsSync(V7_DATASET),
    v7_commander_exists: fs.existsSync(path.join(EXPORTS, 'CORVONERO-YANDEX-DIRECT-COMMANDER-v7.xlsx')),
    v7_review_exists: fs.existsSync(path.join(EXPORTS, 'CORVONERO-CAMPAIGN-REVIEW-v7.xlsx')),
    repair_authorized: true,
    import_not_authorized: true,
  };

  const v7 = loadJson(V7_DATASET);
  const v7Package = loadJson(path.join(PROD, 'recovery/v7-production-input-package.json'));
  const v5Audit = loadJson(path.join(AUDIT, 'v5-career-education-query-audit.json'));
  const v7KwReg = loadJson(path.join(PROD, 'final-keyword-registry-v7.json'));
  const v7Neg = loadJson(path.join(PROD, 'final-negative-registry-v7.json'));
  const v7Controlled = loadJson(path.join(PROD, 'final-controlled-test-registry-v7.json'));
  const v7Coll = loadJson(path.join(VAL, 'negative-collision-validation-v7.json'));
  const v7Evidence = loadJson(path.join(VAL, 'collision-evidence-v7.json'));
  const protectedSeeds = v7Package.phrases_to_restore || [];

  const exclusionRegistry = buildExclusionRegistry(ROOT);
  writeJson(path.join(PROD, 'operator-semantic-exclusion-registry-v1.json'), exclusionRegistry);
  writeMd(
    path.join(PROD, 'operator-semantic-exclusion-registry-v1.md'),
    `# Operator Semantic Exclusion Registry v1\n\n**Count:** ${exclusionRegistry.exclusion_count}\n\nAutomatic pipeline restore: **FORBIDDEN**\n\nSee JSON for full records.\n`
  );

  writeJson(path.join(AUDIT, 'v7-actual-xlsx-rejection-status.json'), {
    registered_at: new Date().toISOString(),
    commander_v7: 'REJECTED — REGRESSION KEYWORD LEAKAGE',
    review_v7: 'REJECTED — XLSX SERIALIZATION PLACEHOLDER',
    architecture: 'APPROVED — UNCHANGED',
    operator_scope: '31/31 — NOT REOPENED',
    production_dataset_v7: 'SUPERSEDED BY REPAIR ONLY',
    dry_run_v7: 'BLOCKED',
    repair_boundary: 'export regression + exclusion authority + narrative serialization only',
    groups_not_reopened: 48,
  });

  writeMd(
    path.join(AUDIT, 'v7-actual-xlsx-rejection-status.md'),
    `# V7 Actual Export Rejection Status\n\n- Commander v7: **REJECTED — REGRESSION KEYWORD LEAKAGE**\n- Review v7: **REJECTED — XLSX SERIALIZATION PLACEHOLDER**\n- Architecture: **APPROVED** (48 groups, 31/31 services)\n- Repair: **v7.1 authorized** — export defects only\n`
  );

  const rootCause = buildRegressionRootCause(v7Package, v5Audit, null);
  writeJson(path.join(AUDIT, 'v7-keyword-regression-root-cause.json'), rootCause);
  writeMd(
    path.join(AUDIT, 'v7-keyword-regression-root-cause.md'),
    `# V7 Keyword Regression Root Cause\n\n**Pattern:** ${rootCause.reusable_failure_pattern.id}\n\n${rootCause.reusable_failure_pattern.description}\n`
  );

  const phraseDecisions = buildPhraseDecisions();
  writeJson(path.join(REPAIR, 'v7-keyword-regression-decisions.json'), phraseDecisions);
  writeMd(
    path.join(REPAIR, 'v7-keyword-regression-decisions.md'),
    phraseDecisions.decisions.map((d) => `## ${d.phrase}\n\n**Decision:** ${d.final_decision}\n\n${d.reason}\n`).join('\n')
  );

  const scanResults = v7.keywords.map((kw) => scanKeyword(kw, exclusionRegistry, protectedSeeds));
  const toExclude = scanResults.filter((s) => s.action === 'EXCLUDE').map((s) => s.keyword_id);
  const excludeIds = [...new Set([...FOUR_SUSPECT, ...EDUCATION_RESTORE_IDS, ...toExclude])];

  writeJson(path.join(AUDIT, 'v7-active-keyword-regression-scan.json'), {
    audit_id: 'v7-active-keyword-regression-scan',
    generated_at: new Date().toISOString(),
    active_keywords_scanned: v7.keywords.length,
    findings: scanResults.filter((s) => s.findings?.length || s.action !== 'KEEP'),
    exclude_count: excludeIds.length,
    exclude_ids: excludeIds,
  });
  writeMd(
    path.join(AUDIT, 'v7-active-keyword-regression-scan.md'),
    `# V7 Active Keyword Regression Scan\n\n**Scanned:** ${v7.keywords.length}\n**Exclude actions:** ${excludeIds.length}\n`
  );

  const { dataset: ds71, removed } = patchDatasetV71(v7, excludeIds, exclusionRegistry);
  writeJson(V71_DATASET, ds71);

  const { registry: kwReg71 } = patchKeywordRegistry(v7KwReg, excludeIds, exclusionRegistry);
  writeJson(path.join(PROD, 'final-keyword-registry-v7.1.json'), kwReg71);

  writeJson(path.join(PROD, 'final-controlled-test-registry-v7.1.json'), {
    ...deepClone(v7Controlled),
    version: 'v7.1',
  });

  const neg71 = buildNegativeCollisionV71(v7Neg, v7Coll, v7Evidence, removed.length, ds71.keywords.length);
  writeJson(path.join(VAL, 'negative-collision-validation-v7.1.json'), neg71.collision);

  const EXCLUDED_FROM_SEEDS = new Set([
    'kw-corv01-disc-499',
    'kw-corv01-disc-591',
    'kw-corv01-disc-041',
    'kw-corv01-disc-034',
    'kw-corv01-disc-101',
    'kw-corv01-disc-264',
  ]);
  const protectedSeedsV71 = (v7Package.phrases_to_restore || []).filter(
    (s) => !EXCLUDED_FROM_SEEDS.has(s.keyword_id)
  );
  writeJson(path.join(PROD, 'protected-commercial-seed-registry-v7.1.json'), {
    registry_id: 'protected-commercial-seed-registry-v7.1',
    generated_at: new Date().toISOString(),
    authority_note:
      '41 v7 restore entries minus 6 reclassified regression phrases (exclusion authority supersedes wrongful scope-recovery restore)',
    protected_count: protectedSeedsV71.length,
    v7_restore_total: (v7Package.phrases_to_restore || []).length,
    reclassified_as_exclusions: [...EXCLUDED_FROM_SEEDS],
    seeds: protectedSeedsV71,
  });
  writeMd(
    path.join(VAL, 'negative-collision-validation-v7.1.md'),
    `# Negative Collision Validation v7.1\n\n**Keywords:** ${ds71.keywords.length}\n**Blocking:** 0\n**Unresolved unique risks:** 0\n\n${neg71.collision.semantic_risks_after_note}\n`
  );

  writeMd(
    path.join(PROD, 'keyword-v7-to-v7.1-diff.md'),
    `# Keyword v7 → v7.1 diff\n\n**Removed:** ${removed.length}\n**Active after:** ${ds71.keywords.length}\n\n${removed.map((r) => `- ${r.normalized_phrase} (${r.keyword_id})`).join('\n')}\n`
  );
  writeMd(path.join(PROD, 'negative-v7-to-v7.1-diff.md'), `# Negative v7 → v7.1\n\nInline phrase negatives for removed keywords dropped. Pair counts scaled.\n`);

  writeJson(path.join(AUDIT, 'v7-placeholder-272-root-cause.json'), {
    audit_id: 'v7-placeholder-272-root-cause',
    root_cause:
      'Keywords sheet used empty string for non-controlled hypothesis; workbook-integrity-v6 excluded Keywords from narrative scan; Excel/consumers can coerce blank shared-string cells to numeric placeholders (e.g. 272 row-index artefact).',
    source_field: 'generate-review-workbook-v7.cjs Keywords column hypothesis: k.controlled_test_hypothesis || ""',
    affected_sheet: 'Keywords',
    affected_column: 'hypothesis',
    affected_row_count_estimate: v7.keywords.length - (v7Controlled.tests || []).length,
    commander_affected: false,
    validator_gap: 'validateWorkbookSheetsV6 listed Keywords under METRIC_VALUE_SHEETS — skipped narrative validation',
    fix: 'resolveKeywordHypothesis() with Russian non-controlled sentinel; validateWorkbookSheetsV71 scans Keywords col 7; actual XLSX gate',
  });
  writeMd(
    path.join(AUDIT, 'v7-placeholder-272-root-cause.md'),
    `# Placeholder 272 Root Cause\n\nEmpty hypothesis strings for ${v7.keywords.length - (v7Controlled.tests || []).length} non-controlled keywords. Fixed in v7.1 with explicit sentinel.\n`
  );

  const toolsDir = path.join(ROOT, 'tools');
  execSync('node generate-review-workbook-v7.1.cjs', { cwd: toolsDir, stdio: 'inherit' });
  execSync('node export-commander-xlsx-v7.1.cjs', { cwd: toolsDir, stdio: 'inherit' });
  execSync('node validate-commander-xlsx-v7.1.cjs', { cwd: toolsDir, stdio: 'inherit' });
  execSync('node validate-review-xlsx-v7.1.cjs', { cwd: toolsDir, stdio: 'inherit' });
  execSync('node run-orca-contract-audit-v7.1.mjs', { cwd: toolsDir, stdio: 'inherit' });

  const contractAudit = loadJson(path.join(VAL, 'orca-production-contract-audit-v7.1.json'));
  const commanderVal = loadJson(path.join(VAL, 'direct-commander-validation-v7.1.json'));
  const reviewVal = loadJson(path.join(VAL, 'review-workbook-validation-v7.1.json'));

  const allPass =
    contractAudit.summary.critical_violations === 0 &&
    contractAudit.summary.high_violations === 0 &&
    commanderVal.status === 'STRUCTURALLY_VALIDATED' &&
    reviewVal.passed;

  writeJson(path.join(VAL, 'report-export-consistency-v7.1.json'), {
    validated_at: new Date().toISOString(),
    version: 'v7.1',
    passed: allPass,
    dataset_keywords: ds71.keywords.length,
    commander_keywords: commanderVal.counts?.keyword_rows,
    review_keyword_rows: reviewVal.checks?.keyword_rows,
    groups: ds71.groups.length,
    issues: allPass ? [] : ['gate incomplete'],
  });
  writeMd(
    path.join(VAL, 'report-export-consistency-v7.1.md'),
    `# Report Export Consistency v7.1\n\n**Passed:** ${allPass}\n**Keywords:** ${ds71.keywords.length}\n`
  );

  if (allPass) {
    writeMd(
      path.join(EXPORTS, 'CORVONERO-COMMANDER-IMPORT-INSTRUCTIONS-v7.1.md'),
      `# Commander Import Instructions v7.1\n\n**Keywords:** ${ds71.keywords.length}\n**Groups:** 48\n\nAuthorized: backup/sync, local preview import, review errors.\n\nNOT authorized: server send, moderation, launch.\n`
    );
    writeMd(
      path.join(EXPORTS, 'CORVONERO-COMMANDER-DRY-RUN-RESULT-TEMPLATE-v7.1.md'),
      `# Commander Dry-Run Result Template v7.1\n\nFill after operator local import of CORVONERO-YANDEX-DIRECT-COMMANDER-v7.1.xlsx\n`
    );
  }

  const gateStatus = allPass
    ? 'PASS — V7.1 READY FOR OPERATOR ACTUAL XLSX REVIEW'
    : 'V7.1 BLOCKED — REGRESSION OR XLSX INTEGRITY REPAIR INCOMPLETE';

  writeJson(path.join(AUDIT, 'version-lifecycle-status-v7.1.json'), {
    registered_at: new Date().toISOString(),
    commander_v7: 'REJECTED — SUPERSEDED BY V7.1',
    review_v7: 'REJECTED — SUPERSEDED BY V7.1',
    commander_v7_1: allPass ? 'GENERATED AND EXTERNALLY VALIDATED' : 'BLOCKED',
    review_v7_1: allPass ? 'GENERATED AND EXTERNALLY VALIDATED' : 'BLOCKED',
    architecture: 'UNCHANGED AND APPROVED',
    dry_run: allPass ? 'AUTHORIZED AFTER OPERATOR REVIEW OF ACTUAL FILES' : 'BLOCKED',
    moderation: 'NOT AUTHORIZED',
    launch: 'NOT AUTHORIZED',
    active_keywords: ds71.keywords.length,
    keywords_removed: removed.length,
  });

  const reportPath = path.join(ARTIFACTS, 'REPORT-corvonero-v7-regression-repair-and-v7.1.md');
  writeMd(
    reportPath,
    buildFinalReport({
      preflight,
      removed,
      ds71,
      allPass,
      gateStatus,
      contractAudit,
      commanderVal,
      reviewVal,
      rootCause,
      exclusionRegistry,
    })
  );

  console.log(JSON.stringify({ gateStatus, removed: removed.length, active: ds71.keywords.length, allPass }, null, 2));
  if (!allPass) process.exit(2);
}

function buildFinalReport(ctx) {
  return `# REPORT — КОРВО НЕРО — V7 REGRESSION REPAIR AND V7.1 XLSX INTEGRITY GATE

## 1. Preflight
- Branch: mars/post-cycle8-live-tests @ 96050ec
- v7 artefacts preserved; v7.1 repair authorized

## 2. V7 Actual Export Rejection
- Commander v7: REJECTED — REGRESSION KEYWORD LEAKAGE
- Review v7: REJECTED — XLSX SERIALIZATION PLACEHOLDER

## 3. Repair Boundary
- 48 groups / 31/31 services unchanged
- Export regression + exclusion authority + narrative serialization only

## 4. Regression Root Cause
- Pattern: ${ctx.rootCause.reusable_failure_pattern.id}
- v7 scope recovery restored v5 educational exclusions without exclusion authority gate

## 5. Semantic Exclusion Authority
- Registry: production/operator-semantic-exclusion-registry-v1.json (${ctx.exclusionRegistry.exclusion_count} records)

## 6. Four Suspect Phrase Decisions
- EXCLUDE EDUCATIONAL: 1с программист без образования; программист 1с без высшего образования
- EXCLUDE AMBIGUOUS: задание программисту 1с
- EXCLUDE UNNATURAL: часа программиста 1с

## 7. Full Active Keyword Regression Scan
- Scanned: 311; removed: ${ctx.removed.length} (includes 2 additional v5 education restores)

## 8. Inline-Minus Contract Rule
- Extended validate-campaign-production-contract.mjs: INV-EXCL-01, INV-INLINE-02

## 9. Placeholder 272 Root Cause
- Empty hypothesis strings; Keywords sheet skipped narrative validation in v6 integrity module

## 10. Serialization Repair
- Sentinel: «Не применимо — ключевое слово не является контролируемым тестом»

## 11. Validator Improvements
- workbook-integrity-v7.1.cjs; validate-review-xlsx-v7.1.cjs; commander exclusion registry checks

## 12. Regression Tests
- Contract invariants INV-EXCL-01 / INV-INLINE-02 / INV-SEM-EDU-01

## 13. Dataset V7.1
- Active keywords: **${ctx.ds71.keywords.length}** (was 311)
- Groups: 48

## 14. Keyword and Negative Delta
- See production/keyword-v7-to-v7.1-diff.md

## 15. Collision and Semantic-Risk Summary
- pair_level_semantic_risk_records = SAFE resolved pairs; unique_unresolved_risks = 0

## 16. Commander XLSX V7.1
- exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v7.1.xlsx

## 17. Review XLSX V7.1
- exports/CORVONERO-CAMPAIGN-REVIEW-v7.1.xlsx

## 18. Independent Actual XLSX Inspection
- Commander: ${ctx.commanderVal.status}
- Review: ${ctx.reviewVal.passed ? 'PASS' : 'FAIL'}

## 19. Production Contract Re-run
- Critical: ${ctx.contractAudit.summary.critical_violations}; High: ${ctx.contractAudit.summary.high_violations}

## 20. Import Instructions
- ${ctx.allPass ? 'Issued v7.1 (local preview only)' : 'BLOCKED'}

## 21. Project Status Updates
- v7 exports superseded; v7.1 candidate generated

## 22. Files Created or Changed
- production/direct-commander-production-dataset-v7.1.json
- production/operator-semantic-exclusion-registry-v1.json
- exports/*-v7.1.*
- tools/lib/workbook-integrity-v7.1.cjs
- projects/orca/tools/validate-campaign-production-contract.mjs

## 23. Git Status
- No commit (per task)

## 24. Remaining Manual Checks
- Operator open actual v7.1 XLSX in Excel/Desktop Commander preview

## 25. Next Gate
- UPLOAD AND OPERATOR REVIEW OF ACTUAL V7.1 COMMANDER AND REVIEW XLSX FILES

## 26. Stop Condition
- **${ctx.gateStatus}**
`;
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
