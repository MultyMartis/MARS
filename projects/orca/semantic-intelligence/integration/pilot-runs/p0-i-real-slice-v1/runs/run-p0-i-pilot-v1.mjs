#!/usr/bin/env node
/**
 * P0-I real integration pilot runner v1 — batch execution, queues, metrics.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';
import { runAdmissionIntegration } from '../../../runtime/src/admission-orchestrator.mjs';
import { loadContracts } from '../../../runtime/src/contract-loader.mjs';
import { assessPhrase, sha256Json, sha256FileContent } from './pilot-assessor-v1.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PILOT_ROOT = path.resolve(__dirname, '..');
const RUNTIME_ROOT = path.resolve(PILOT_ROOT, '../../runtime');
const REPO = path.resolve(PILOT_ROOT, '../../../../../..');

const PILOT_RUN_ID = 'p0-i-real-slice-v1';
const RANDOM_SEED = 'p0-i-audit-20260622';
const ACCEPT_AUDIT_RATE = 20 / 200;
const REJECT_AUDIT_RATE = 20 / 200;

function readJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function writeJson(p, data) {
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, JSON.stringify(data, null, 2) + '\n', 'utf8');
}

function gitHead() {
  try {
    return execSync('git rev-parse --short HEAD', { cwd: REPO, encoding: 'utf8' }).trim();
  } catch {
    return 'UNKNOWN';
  }
}

function buildReviewEntry(row, result) {
  const rec = result.record || {};
  const diag = result.diagnostic_comparison || {};
  return {
    pilot_row_id: row.pilot_row_id,
    phrase: row.raw_query,
    automated_output: {
      admission_decision: result.admission_decision,
      blocked: result.blocked,
      primary_intent: rec.primary_intent,
      commercial_eligibility: rec.commercial_eligibility,
      risk: rec.risk,
    },
    supporting_evidence: rec.commercial_eligibility?.supporting_evidence || [],
    opposing_evidence: rec.commercial_eligibility?.opposing_evidence || [],
    risk: rec.risk?.overall_risk,
    invariant_findings: (result.validation?.findings || []).map((f) => f.invariant_id),
    legacy_comparison: diag,
    review_questions: [
      'Подтвердить или отклонить автоматическое решение?',
      'Достаточно ли evidence для tri-state?',
    ],
    source_provenance: row.provenance,
    operator_decision: null,
    operator_notes: null,
    adjudicator: null,
  };
}

function queueKey(route) {
  const map = {
    ABSTAIN_MANDATORY: '01_all_abstain',
    BLOCKED_ACCEPT: '02_blocked_accept',
    HIGH_RISK: '03_high_critical_risk',
    PROTECTED_STRATA: '04_protected_strata_conflicts',
    SHORT_HEAD: '05_short_head_cases',
    PROBLEM_QUERY: '06_problem_query_ambiguity',
    PRODUCT_SERVICE: '07_product_service_ambiguity',
    CAREER_PROVIDER: '08_career_provider_ambiguity',
    PROVIDER_DIY: '09_provider_diy_ambiguity',
    ASSESSOR_DISAGREEMENT: '10_legacy_new_disagreement',
    RANDOM_ACCEPT_AUDIT: '11_random_accept_audit',
    RANDOM_REJECT_AUDIT: '12_random_reject_audit',
  };
  return map[route] || null;
}

function main() {
  const head = gitHead();
  const manifestPath = path.join(PILOT_ROOT, 'selection/p0-i-pilot-selection-manifest-v1.json');
  const manifest = readJson(manifestPath);
  const lockPath = path.join(RUNTIME_ROOT, 'config/orca-semantic-contract-runtime-lock-v1.json');
  const configPath = path.join(PILOT_ROOT, 'config/P0-I-PILOT-RUN-CONFIG-v1.json');
  const pilotConfig = readJson(configPath);

  const contractLoad = loadContracts({ lockPath });
  if (!contractLoad.ok) {
    console.error('BLOCKED — contracts failed', contractLoad.message);
    process.exit(2);
  }

  const runConfig = {
    abstain_supported: true,
    review_router: {
      random_accept_audit_rate: ACCEPT_AUDIT_RATE,
      random_reject_audit_rate: REJECT_AUDIT_RATE,
      audit_seed: RANDOM_SEED,
    },
  };

  const outputs = [];
  const queues = {};
  const initQueue = (k) => { if (!queues[k]) queues[k] = []; };

  let processed = 0;
  let successful = 0;
  let blocked = 0;
  let failed = 0;
  const decisionCounts = { ACCEPT: 0, REJECT: 0, ABSTAIN: 0, null: 0 };
  let legacyDisagreements = 0;
  let downstreamLeakage = 0;
  const forbiddenFields = ['campaign_id', 'ad_group_id', 'cluster_id', 'negative_list_id', 'commander_export'];

  for (const row of manifest.rows) {
    processed++;
    const assessed = assessPhrase(row.raw_query, row.normalized_query);
    const fixtureInput = {
      input: {
        query_id: row.source_query_id,
        raw_query: row.raw_query,
        normalized_query: row.normalized_query,
        provenance: row.provenance,
        assessor: assessed.assessor,
        protected_strata_conflict: assessed.protected_strata_conflict,
        assessor_disagreement: assessed.assessor_disagreement,
        enable_legacy_comparison: true,
      },
    };

    let result;
    try {
      result = runAdmissionIntegration(fixtureInput, { lockPath, config: runConfig });
    } catch (err) {
      failed++;
      outputs.push({ pilot_row_id: row.pilot_row_id, ok: false, error: String(err) });
      continue;
    }

    const assessorDecision = assessed.assessor.commercial_eligibility.decision;
    if (result.blocked && assessorDecision === 'ACCEPT') {
      initQueue('02_blocked_accept');
      queues['02_blocked_accept'].push(buildReviewEntry(row, { ...result, admission_decision: null }));
    }

    if (result.ok) successful++;
    if (result.blocked) blocked++;

    const dec = result.admission_decision;
    if (decisionCounts[dec] !== undefined) decisionCounts[dec]++;
    else decisionCounts.null++;

    if (result.diagnostic_comparison?.disagreement_type && result.diagnostic_comparison.disagreement_type !== 'NONE') {
      legacyDisagreements++;
    }

    for (const ff of forbiddenFields) {
      if (result.record && result.record[ff] !== undefined) downstreamLeakage++;
    }

    const routing = result.routing || {};
    for (const route of routing.routes || []) {
      const qk = queueKey(route);
      if (qk) {
        initQueue(qk);
        queues[qk].push(buildReviewEntry(row, result));
      }
    }

    if (result.diagnostic_comparison?.disagreement_type && result.diagnostic_comparison.disagreement_type !== 'NONE') {
      initQueue('10_legacy_new_disagreement');
      queues['10_legacy_new_disagreement'].push(buildReviewEntry(row, result));
    }

    if (['HIGH', 'CRITICAL'].includes(result.record?.risk?.overall_risk)) {
      initQueue('03_high_critical_risk');
      queues['03_high_critical_risk'].push(buildReviewEntry(row, result));
    }

    outputs.push({
      pilot_run_id: PILOT_RUN_ID,
      pilot_row_id: row.pilot_row_id,
      phrase_id: row.source_query_id,
      admission_decision: result.admission_decision,
      blocked: result.blocked,
      ok: result.ok,
      integration_result: result,
    });
  }

  const metrics = {
    metrics_id: 'p0-i-integration-metrics-v1',
    pilot_run_id: PILOT_RUN_ID,
    generated_at: new Date().toISOString(),
    runtime_commit: head,
    input_count: manifest.actual_count,
    processed_count: processed,
    successful_count: successful,
    blocked_count: blocked,
    failed_count: failed,
    unprocessed_count: manifest.actual_count - processed,
    schema_valid_count: outputs.filter((o) => o.integration_result?.record && !o.error).length,
    accept_count: decisionCounts.ACCEPT,
    reject_count: decisionCounts.REJECT,
    abstain_count: decisionCounts.ABSTAIN,
    review_routed_count: outputs.filter((o) => o.integration_result?.routing?.routed).length,
    contract_consumption_success: contractLoad.ok,
    invariant_execution_success: outputs.every((o) => o.integration_result?.validation),
    decision_trace_completeness: outputs.filter((o) => o.integration_result?.trace?.stages?.length >= 8).length,
    provenance_completeness: manifest.rows.filter((r) => r.provenance?.status === 'COMPLETE').length,
    legacy_disagreement_count: legacyDisagreements,
    downstream_field_leakage_count: downstreamLeakage,
    runtime_errors: failed,
    note: 'INTEGRATION METRICS ONLY — NOT BENCHMARK METRICS',
  };

  const runDir = path.join(PILOT_ROOT, 'runs', `run-${new Date().toISOString().slice(0, 10)}`);
  const outDir = path.join(PILOT_ROOT, 'output');
  fs.mkdirSync(outDir, { recursive: true });
  fs.mkdirSync(path.join(PILOT_ROOT, 'review'), { recursive: true });
  fs.mkdirSync(path.join(PILOT_ROOT, 'diagnostics'), { recursive: true });

  writeJson(path.join(outDir, 'p0-i-pilot-semantic-records-v1.json'), { pilot_run_id: PILOT_RUN_ID, records: outputs });
  writeJson(path.join(PILOT_ROOT, 'review', 'p0-i-human-review-queues-v1.json'), { pilot_run_id: PILOT_RUN_ID, queues });
  writeJson(path.join(PILOT_ROOT, 'diagnostics', 'p0-i-legacy-diagnostic-comparison-v1.json'), {
    pilot_run_id: PILOT_RUN_ID,
    summary: summarizeLegacy(outputs),
  });
  writeJson(path.join(PILOT_ROOT, 'reports', 'p0-i-integration-metrics-v1.json'), metrics);

  // Per-queue markdown workbooks
  for (const [qk, entries] of Object.entries(queues)) {
    writeJson(path.join(PILOT_ROOT, 'review', `${qk}.json`), { queue_id: qk, count: entries.length, entries });
  }

  const operatorReview = {
    pilot_run_id: PILOT_RUN_ID,
    mandatory_review_rows: Object.values(queues).flat().length,
    operator_decisions_recorded: 0,
    status: 'HUMAN REVIEW PENDING',
    queues: Object.fromEntries(Object.entries(queues).map(([k, v]) => [k, v.length])),
  };
  writeJson(path.join(PILOT_ROOT, 'review', 'OPERATOR-REVIEW-SUMMARY-v1.json'), operatorReview);

  const technicalPass =
    manifest.actual_count === processed &&
    failed === 0 &&
    contractLoad.ok &&
    decisionCounts.ACCEPT > 0 &&
    decisionCounts.REJECT > 0 &&
    decisionCounts.ABSTAIN > 0 &&
    downstreamLeakage === 0;

  writeJson(path.join(PILOT_ROOT, 'validation', 'p0-i-technical-pilot-assessment-v1.json'), {
    status: technicalPass ? 'P0-I TECHNICAL PILOT PASS — HUMAN REVIEW PENDING' : 'P0-I TECHNICAL PILOT INCOMPLETE',
    criteria: {
      frozen_input_processed: manifest.actual_count === processed,
      contracts_consumed: contractLoad.ok,
      schema_validity: metrics.schema_valid_count === processed,
      validators_executed: metrics.invariant_execution_success,
      three_outcomes: decisionCounts.ACCEPT > 0 && decisionCounts.REJECT > 0 && decisionCounts.ABSTAIN > 0,
      review_queues_created: Object.keys(queues).length > 0,
      no_downstream_outputs: downstreamLeakage === 0,
      no_silent_failures: failed === 0,
    },
    metrics,
  });

  console.log(JSON.stringify({ technicalPass, metrics, queueCounts: operatorReview.queues, exit: technicalPass ? 0 : 2 }, null, 2));
  process.exit(technicalPass ? 0 : 2);
}

function summarizeLegacy(outputs) {
  const counts = {
    legacy_commercial_new_reject: 0,
    legacy_commercial_new_abstain: 0,
    legacy_reject_new_accept: 0,
    same_decision: 0,
    missing_legacy_decision: 0,
    disagreement_families: {},
  };
  for (const o of outputs) {
    const d = o.integration_result?.diagnostic_comparison;
    if (!d) { counts.missing_legacy_decision++; continue; }
    const dt = d.disagreement_type || 'NONE';
    if (dt === 'LEGACY_ACCEPT_NEW_REJECT') counts.legacy_commercial_new_reject++;
    else if (dt === 'LEGACY_ELIGIBLE_NEW_ABSTAIN') counts.legacy_commercial_new_abstain++;
    else if (dt === 'LEGACY_REJECT_NEW_ACCEPT') counts.legacy_reject_new_accept++;
    else if (dt === 'NONE') counts.same_decision++;
    if (dt !== 'NONE') counts.disagreement_families[dt] = (counts.disagreement_families[dt] || 0) + 1;
  }
  return counts;
}

main();
