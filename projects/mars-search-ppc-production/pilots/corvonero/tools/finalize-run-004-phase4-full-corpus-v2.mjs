#!/usr/bin/env node
/**
 * Finalize Corvonero Run 004 Phase 4 v2 — post-resume full corpus outputs.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { analyzeCareerAcceptGate } from './career-stop-gate-v1.mjs';
import { classifyCorpusV2 } from './canary-family-classifier-v2.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const RUN_ID = 'corv-semantic-v2-20260626-004';
const PILOT = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const GIT_RUN = path.join(PILOT, 'runs', RUN_ID);
const REPORTS = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/reports');
const STORAGE = path.join('C:\\MARS Phenix\\AI MARS STORAGE', 'mig', 'corvonero', 'semantic-runs', RUN_ID);
const FIX = path.join(REPO_ROOT, 'projects/orca/semantic-intelligence/live-model/fixtures');
const CORPUS_REL = 'projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json';

function readJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function writeJson(p, d) {
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, JSON.stringify(d, null, 2));
}

function writeText(p, t) {
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, t);
}

function pct(n, d) {
  return d ? ((n / d) * 100).toFixed(1) : '0.0';
}

function authoritativeVerdict(r) {
  return r.final_authoritative_verdict || r.final_verdict;
}

function familyStats(results, family) {
  const items = results.filter((r) => r.primary_family === family);
  const dist = { ACCEPT: 0, REJECT: 0, ABSTAIN: 0 };
  for (const r of items) {
    const v = authoritativeVerdict(r);
    if (v) dist[v] = (dist[v] || 0) + 1;
  }
  return { family, count: items.length, distribution: dist };
}

function buildReviewQueueV2(results, canaryAudit, operatorOverrides, careerGate) {
  const queue = [];
  const add = (r, reason, extra = {}) => {
    if (queue.find((q) => q.phrase_id === r.phrase_id)) return;
    queue.push({
      phrase_id: r.phrase_id,
      phrase: r.phrase,
      review_reason: reason,
      primary_family: r.primary_family,
      final_verdict: authoritativeVerdict(r),
      model_verdict: r.model_verdict || r.final_verdict,
      review_state: 'REVIEW_QUEUE',
      ...extra,
    });
  };

  const cr200 = results.find((r) => r.phrase_id === 'CR2-PHR-00200');
  if (cr200) {
    add(cr200, 'CR2-PHR-00200 — operator review item (scored false reject)', {
      expected_policy_authority: 'direct_commercial_service_demand_policy',
    });
  }

  for (const ov of operatorOverrides) {
    add(
      results.find((r) => r.phrase_id === ov.phrase_id) || { phrase_id: ov.phrase_id, phrase: ov.phrase },
      `Operator override — ${ov.phrase_id}`,
      { operator_override: ov },
    );
  }

  for (const item of careerGate.items || []) {
    if (item.classification === 'OPERATOR_REVIEW_REQUIRED') {
      const r = results.find((x) => x.phrase_id === item.phrase_id);
      if (r) add(r, item.rationale, { career_gate_classification: item.classification });
    }
  }

  for (const r of results) {
    if (r.edge_cases?.includes('psr_amb_01_family') || r.review_flags?.includes('psr_amb_01')) {
      add(r, 'PSR-AMB-01 family — monitored product-plus-service ambiguity');
    }
    if (r.primary_family === 'generic_erp_platform_ambiguity') {
      add(r, 'Generic ERP platform ambiguity');
    }
    if (r.confirmation_disagreement) {
      add(r, 'Primary/reassessment disagreement', {
        disagreement_reason: `primary=${r.primary_verdict}; reassessment=${r.reassessment_verdict}`,
      });
    }
    if (r.malformed_retry) {
      add(r, 'Retried malformed output — verify structured response');
    }
  }

  return {
    queue_id: 'corvonero-run-004-phase-4-review-queue-v2',
    run_id: RUN_ID,
    mandatory_items: ['CR2-PHR-00200', 'CR2-PHR-00584'],
    monitored_families: ['psr_amb_01', 'generic_erp_platform_ambiguity', 'ambiguous_diy', 'career_related_accept'],
    career_gate_summary: {
      career_accept_raw_count: careerGate.career_accept_raw_count,
      career_accept_confirmed_error_count: careerGate.career_accept_confirmed_error_count,
      career_accept_classifier_false_positive_count: careerGate.career_accept_classifier_false_positive_count,
      career_accept_review_pending_count: careerGate.career_accept_review_pending_count,
      career_accept_override_count: careerGate.career_accept_override_count,
    },
    total_items: queue.length,
    items: queue.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id)),
    created_at: new Date().toISOString(),
  };
}

function main() {
  const registryPath = path.join(STORAGE, 'checkpoints', 'phase4-semantic-registry-v1.json');
  const execPath = path.join(STORAGE, 'reports', 'phase4-full-corpus-execution-report-v1.json');
  const checkpointPath = path.join(STORAGE, 'checkpoints', 'checkpoint-phase4-v1.json');
  const overridePath = path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-OPERATOR-OVERRIDES-v1.json');
  const reconciliationPath = path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-TRIGGER-RECONCILIATION-v1.json');

  if (!fs.existsSync(registryPath)) {
    console.error('Missing phase4 semantic registry');
    process.exit(2);
  }

  const registry = readJson(registryPath);
  const results = registry.results || [];
  const checkpoint = fs.existsSync(checkpointPath) ? readJson(checkpointPath) : {};
  const execution = fs.existsSync(execPath) ? readJson(execPath) : {};
  const operatorOverrides = fs.existsSync(overridePath) ? readJson(overridePath).overrides || [] : [];
  const overrideMap = new Map(operatorOverrides.map((o) => [o.phrase_id, o]));
  const reconciliationDoc = fs.existsSync(reconciliationPath) ? readJson(reconciliationPath) : null;

  const corpus = readJson(path.join(REPO_ROOT, CORPUS_REL));
  const records = corpus.phrases || corpus.records || corpus;
  const context = {
    businessScope: readJson(path.join(FIX, 'business-scope-eval-v1.json')),
    serviceRegistry: readJson(path.join(FIX, 'service-registry-eval-v1.json')),
  };
  const classifiedById = new Map(classifyCorpusV2(records, context).map((c) => [c.phrase_id, c]));
  const careerGate = analyzeCareerAcceptGate(results, classifiedById, overrideMap);

  const isComplete = registry.complete === true && checkpoint.complete === true;
  const ids = results.map((r) => r.phrase_id);
  const uniqueIds = new Set(ids);

  const dist = { ACCEPT: 0, REJECT: 0, ABSTAIN: 0 };
  for (const r of results) {
    const v = authoritativeVerdict(r);
    if (v) dist[v] = (dist[v] || 0) + 1;
  }

  const reconciliation = execution.reconciliation || {
    canonical_total: 2368,
    unique_assessed_ids: uniqueIds.size,
    missing_ids: 2368 - uniqueIds.size,
    duplicate_ids: ids.length - uniqueIds.size,
    orphan_ids: 0,
    canary_reused: results.filter((r) => r.production_source === 'CANARY_ATTEMPT_2_REUSE').length,
    production_new: results.filter((r) => r.production_source === 'PHASE_4_NEW').length,
    complete: isComplete,
    pass: isComplete && uniqueIds.size === 2368 && ids.length === uniqueIds.size,
  };

  const phaseVerdict = isComplete
    ? 'PASS — OPERATOR REVIEW REQUIRED'
    : `PARTIAL — ${checkpoint.stop_reason || checkpoint.lifecycle_state || 'BLOCKED_AT_PHASE_4'}`;
  const lifecycleState = isComplete ? 'PHASE_4_COMPLETE' : checkpoint.lifecycle_state || 'BLOCKED_AT_PHASE_4';

  const reviewQueue = buildReviewQueueV2(results, null, operatorOverrides, careerGate);

  const resultPayload = {
    run_id: RUN_ID,
    output_version: 'v2',
    phase_verdict: phaseVerdict,
    lifecycle_state: lifecycleState,
    project_lifecycle: isComplete ? 'FROZEN_PENDING_SEMANTIC_REVIEW' : checkpoint.lifecycle_state,
    reconciliation,
    trigger_reconciliation: reconciliationDoc,
    verdict_distribution: dist,
    career_gate: careerGate,
    operator_overrides: operatorOverrides,
    registries: {
      full_semantic_count: results.length,
      accept_count: results.filter((r) => authoritativeVerdict(r) === 'ACCEPT').length,
      reject_count: results.filter((r) => authoritativeVerdict(r) === 'REJECT').length,
      abstain_count: results.filter((r) => authoritativeVerdict(r) === 'ABSTAIN').length,
    },
    cost: execution.cost || { cumulative_cost_usd: checkpoint.cumulative_cost_usd },
    gate_receipts: execution.gate_receipts || [],
    malformed_policy: execution.malformed_policy || {},
    strategy: 'not started',
    completed_at: execution.completed_at || registry.updated_at,
  };

  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-FULL-CORPUS-RESULT-v2.json'), resultPayload);
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-REVIEW-QUEUE-v2.json'), reviewQueue);

  const reviewPackage = {
    package_id: 'corvonero-run-004-phase-4-review-package-v2',
    run_id: RUN_ID,
    phase_verdict: phaseVerdict,
    lifecycle_state: lifecycleState,
    project_lifecycle: resultPayload.project_lifecycle,
    verdict_distribution: dist,
    review_queue_size: reviewQueue.total_items,
    mandatory_review: reviewQueue.mandatory_items,
    trigger_reconciliation_verdict: reconciliationDoc?.verdict || null,
    family_reviews: [
      'direct_commercial_1c_service',
      'careers_training_education',
      'informational_self_service',
      'problem_troubleshooting',
      'generic_erp_platform_ambiguity',
      'integrations',
      'marking_chestny_znak',
      'ts_piot',
      'geography_modified',
      'ambiguous_mixed_intent',
    ].map((f) => familyStats(results, f)),
    career_gate: careerGate,
    cost: resultPayload.cost,
    operator_review_required: true,
    strategy_authorized: false,
    next_gate: 'OPERATOR REVIEW OF CORVONERO RUN 004 COMPLETED PHASE 4',
  };
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-REVIEW-PACKAGE-v2.json'), reviewPackage);

  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-FULL-CORPUS-RESULT-v2.md'), `# CORVONERO RUN 004 — PHASE 4 FULL CORPUS RESULT v2

**Run ID:** \`${RUN_ID}\`  
**Phase verdict:** \`${phaseVerdict}\`  
**Lifecycle:** \`${lifecycleState}\`

## Summary

| Metric | Value |
|--------|------:|
| Canonical total | 2368 |
| Unique assessed | ${results.length} |
| ACCEPT | ${dist.ACCEPT || 0} (${pct(dist.ACCEPT, results.length)}%) |
| REJECT | ${dist.REJECT || 0} (${pct(dist.REJECT, results.length)}%) |
| ABSTAIN | ${dist.ABSTAIN || 0} (${pct(dist.ABSTAIN, results.length)}%) |
| Review queue | ${reviewQueue.total_items} |
| Cumulative cost (USD) | ${resultPayload.cost?.cumulative_cost_usd?.toFixed?.(4) ?? 'UNKNOWN'} |

**Strategy NOT started. Operator review required.**
`);

  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-REVIEW-PACKAGE-v2.md'), `# CORVONERO RUN 004 — PHASE 4 REVIEW PACKAGE v2

**Verdict:** \`${phaseVerdict}\`

## Trigger reconciliation

\`${reconciliationDoc?.verdict || 'UNKNOWN'}\`

## Mandatory review

${reviewQueue.mandatory_items.map((i) => `- **${i}**`).join('\n')}

## Review queue

Total items: **${reviewQueue.total_items}**

## Next gate

\`\`\`text
OPERATOR REVIEW OF CORVONERO RUN 004 COMPLETED PHASE 4
\`\`\`
`);

  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-NEXT-TASK-v2.md'), `# CORVONERO RUN 004 — PHASE 5 NEXT TASK v2

**Status:** AWAITING OPERATOR REVIEW OF COMPLETED PHASE 4  
**Run ID:** \`${RUN_ID}\`  
**Prerequisite:** \`PASS — OPERATOR REVIEW REQUIRED\` (Phase 4 complete)

## Scope (NOT AUTHORIZED until operator approves)

- Phase 5 semantic review and assembly
- **Forbidden without separate authorization:** Wave 5, advertising strategy, Campaign Architecture, Commander, import, launch

## Entry criteria

- Phase 4 reconciliation PASS (${results.length}/2368)
- Operator review of \`CORVONERO-RUN-004-PHASE-4-REVIEW-PACKAGE-v2\`
- Review queue disposition
- Project lifecycle: \`FROZEN_PENDING_SEMANTIC_REVIEW\`

## Counters

\`\`\`text
canonical_corpus_total: 2368
unique_assessed_ids: ${results.length}
review_queue_items: ${reviewQueue.total_items}
cumulative_cost_usd: ${resultPayload.cost?.cumulative_cost_usd?.toFixed?.(4) ?? 'UNKNOWN'}
strategy: not started
\`\`\`
`);

  console.log(JSON.stringify({
    finalized: true,
    version: 'v2',
    assessed: results.length,
    complete: isComplete,
    phase_verdict: phaseVerdict,
    review_queue: reviewQueue.total_items,
  }, null, 2));
}

main();
