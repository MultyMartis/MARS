#!/usr/bin/env node
/**
 * Finalize Corvonero Run 004 Phase 4 — registries, review queue, operator report.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const RUN_ID = 'corv-semantic-v2-20260626-004';
const PILOT = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const GIT_RUN = path.join(PILOT, 'runs', RUN_ID);
const REPORTS = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/reports');
const STORAGE = path.join('C:\\MARS Phenix\\AI MARS STORAGE', 'mig', 'corvonero', 'semantic-runs', RUN_ID);

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

function familyStats(results, family) {
  const items = results.filter((r) => r.primary_family === family);
  const dist = { ACCEPT: 0, REJECT: 0, ABSTAIN: 0 };
  for (const r of items) if (r.final_verdict) dist[r.final_verdict] = (dist[r.final_verdict] || 0) + 1;
  return { family, count: items.length, distribution: dist };
}

function buildReviewQueue(results, canaryAudit) {
  const queue = [];
  const add = (r, reason, extra = {}) => {
    if (queue.find((q) => q.phrase_id === r.phrase_id)) return;
    queue.push({
      phrase_id: r.phrase_id,
      phrase: r.phrase,
      review_reason: reason,
      primary_family: r.primary_family,
      expected_policy_authority: extra.expected_policy_authority || null,
      canary_outcome: extra.canary_outcome || null,
      disagreement_reason: extra.disagreement_reason || null,
      final_verdict: r.final_verdict,
      confidence: r.confidence,
      review_state: 'REVIEW_QUEUE',
      ...extra,
    });
  };

  const cr200 = results.find((r) => r.phrase_id === 'CR2-PHR-00200');
  if (cr200) {
    const auditRec = canaryAudit?.records?.find((a) => a.phrase_id === 'CR2-PHR-00200');
    add(cr200, 'CR2-PHR-00200 — operator review item (scored false reject)', {
      expected_policy_authority: 'direct_commercial_service_demand_policy',
      canary_outcome: auditRec?.canary_outcome || null,
      disagreement_reason: 'Classifier expected ACCEPT; model REJECT — educational phrasing',
    });
  }

  for (const r of results) {
    if (r.edge_cases?.includes('psr_amb_01_family') || r.review_flags?.includes('psr_amb_01')) {
      add(r, 'PSR-AMB-01 family — monitored product-plus-service ambiguity');
    }
    if (r.observed_tags?.includes('career') && r.final_verdict === 'ACCEPT') {
      add(r, 'Career-tagged phrase ACCEPT — fail-closed trigger candidate');
    }
    if (r.primary_family === 'generic_erp_platform_ambiguity') {
      add(r, 'Generic ERP platform ambiguity');
    }
    if (r.edge_cases?.includes('ambiguous_diy_troubleshooting') || r.observed_tags?.includes('ambiguous_diy')) {
      add(r, 'Ambiguous DIY problem query');
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
    queue_id: 'corvonero-run-004-phase-4-review-queue-v1',
    run_id: RUN_ID,
    mandatory_items: ['CR2-PHR-00200'],
    monitored_families: ['psr_amb_01', 'generic_erp_platform_ambiguity', 'ambiguous_diy'],
    total_items: queue.length,
    items: queue.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id)),
    created_at: new Date().toISOString(),
  };
}

function buildErrorFamilyReport(results, execution) {
  const families = {};
  for (const r of results) {
    if (r.status === 'QUARANTINED') {
      families.MALFORMED_MODEL_OUTPUT = (families.MALFORMED_MODEL_OUTPUT || 0) + 1;
    }
    if (r.malformed_retry) {
      families.MALFORMED_RETRY_SUCCESS = (families.MALFORMED_RETRY_SUCCESS || 0) + 1;
    }
  }
  return {
    report_id: 'corvonero-run-004-phase-4-error-family-v1',
    run_id: RUN_ID,
    malformed_policy: execution?.malformed_policy || {},
    families,
    model_api_errors: execution?.cost ? undefined : 0,
    created_at: new Date().toISOString(),
  };
}

function main() {
  const registryPath = path.join(STORAGE, 'checkpoints', 'phase4-semantic-registry-v1.json');
  const execPath = path.join(STORAGE, 'reports', 'phase4-full-corpus-execution-report-v1.json');
  const auditPath = path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-CANARY-REUSE-AUDIT-v1.json');

  if (!fs.existsSync(registryPath)) {
    console.error('Missing phase4 semantic registry — run execute-run-004-phase4-full-corpus-v1.mjs first');
    process.exit(2);
  }

  const registry = readJson(registryPath);
  const results = registry.results || [];
  const isComplete = registry.complete === true;
  const execution = fs.existsSync(execPath) ? readJson(execPath) : {};
  const canaryAudit = fs.existsSync(auditPath) ? readJson(auditPath) : null;
  const checkpoint = fs.existsSync(path.join(STORAGE, 'checkpoints', 'checkpoint-phase4-v1.json'))
    ? readJson(path.join(STORAGE, 'checkpoints', 'checkpoint-phase4-v1.json'))
    : {};

  const phaseVerdict = isComplete
    ? (execution.phase_verdict || 'PASS — OPERATOR REVIEW REQUIRED')
    : `PARTIAL — ${checkpoint.stop_reason || checkpoint.lifecycle_state || 'BLOCKED_AT_PHASE_4'}`;
  const lifecycleState = isComplete
    ? (execution.lifecycle_state || 'PHASE_4_COMPLETE')
    : (checkpoint.lifecycle_state || 'BLOCKED_AT_PHASE_4');

  const dist = { ACCEPT: 0, REJECT: 0, ABSTAIN: 0 };
  for (const r of results) if (r.final_verdict) dist[r.final_verdict] = (dist[r.final_verdict] || 0) + 1;

  const acceptRegistry = results.filter((r) => r.final_verdict === 'ACCEPT');
  const rejectRegistry = results.filter((r) => r.final_verdict === 'REJECT');
  const abstainRegistry = results.filter((r) => r.final_verdict === 'ABSTAIN');
  const reviewQueue = buildReviewQueue(results, canaryAudit);
  const errorFamily = buildErrorFamilyReport(results, execution);

  const resultPayload = {
    run_id: RUN_ID,
    phase_verdict: phaseVerdict,
    lifecycle_state: lifecycleState,
    reconciliation: execution.reconciliation || {
      canonical_total: 2368,
      unique_assessed_ids: results.length,
      missing_ids: 2368 - results.length,
      complete: isComplete,
    },
    verdict_distribution: dist,
    registries: {
      full_semantic_count: results.length,
      accept_count: acceptRegistry.length,
      reject_count: rejectRegistry.length,
      abstain_count: abstainRegistry.length,
    },
    cost: execution.cost || { cumulative_cost_usd: checkpoint.cumulative_cost_usd },
    malformed_policy: execution.malformed_policy || {},
    gate_receipts: execution.gate_receipts || [],
    batch_count: (execution.batches || []).length,
    full_production_complete: isComplete,
    partial_stop_reason: checkpoint.stop_reason || null,
    resume_from_checkpoint: !isComplete,
    strategy: 'not started',
    completed_at: execution.completed_at || registry.updated_at,
  };

  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-FULL-CORPUS-RESULT-v1.json'), resultPayload);
  writeJson(path.join(STORAGE, 'reports', 'full-semantic-registry-v1.json'), { run_id: RUN_ID, results });
  writeJson(path.join(STORAGE, 'reports', 'accept-registry-v1.json'), { run_id: RUN_ID, count: acceptRegistry.length, records: acceptRegistry });
  writeJson(path.join(STORAGE, 'reports', 'reject-registry-v1.json'), { run_id: RUN_ID, count: rejectRegistry.length, records: rejectRegistry });
  writeJson(path.join(STORAGE, 'reports', 'abstain-registry-v1.json'), { run_id: RUN_ID, count: abstainRegistry.length, records: abstainRegistry });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-REVIEW-QUEUE-v1.json'), reviewQueue);
  writeJson(path.join(STORAGE, 'reports', 'error-family-report-v1.json'), errorFamily);
  writeJson(path.join(STORAGE, 'reports', 'batch-index-v1.json'), {
    run_id: RUN_ID,
    batches: execution.batches || checkpoint.batch_receipts || [],
  });
  writeJson(path.join(STORAGE, 'reports', 'cost-report-v1.json'), {
    run_id: RUN_ID,
    ...resultPayload.cost,
    malformed_policy: resultPayload.malformed_policy,
  });
  writeJson(path.join(STORAGE, 'receipts', 'phase-4-final-reconciliation-v1.json'), resultPayload.reconciliation);
  writeJson(path.join(STORAGE, 'receipts', 'phase-4-final-execution-receipt-v1.json'), resultPayload);

  const reviewPackage = {
    package_id: 'corvonero-run-004-phase-4-review-package-v1',
    run_id: RUN_ID,
    phase_verdict: resultPayload.phase_verdict,
    verdict_distribution: dist,
    review_queue_size: reviewQueue.total_items,
    mandatory_review: ['CR2-PHR-00200'],
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
    cost: resultPayload.cost,
    operator_review_required: true,
    strategy_authorized: false,
    next_gate: 'OPERATOR REVIEW OF CORVONERO RUN 004 PHASE 4 RESULT',
  };
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-REVIEW-PACKAGE-v1.json'), reviewPackage);

  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-FULL-CORPUS-RESULT-v1.md'), `# CORVONERO RUN 004 — PHASE 4 FULL CORPUS RESULT v1

**Run ID:** \`${RUN_ID}\`  
**Phase verdict:** \`${resultPayload.phase_verdict}\`  
**Lifecycle:** \`${resultPayload.lifecycle_state}\`

## Summary

| Metric | Value |
|--------|------:|
| Canonical total | 2368 |
| Unique assessed | ${results.length} |
| ACCEPT | ${dist.ACCEPT || 0} (${pct(dist.ACCEPT, results.length)}%) |
| REJECT | ${dist.REJECT || 0} (${pct(dist.REJECT, results.length)}%) |
| ABSTAIN | ${dist.ABSTAIN || 0} (${pct(dist.ABSTAIN, results.length)}%) |
| Review queue items | ${reviewQueue.total_items} |
| Cumulative cost (USD) | ${resultPayload.cost?.cumulative_cost_usd?.toFixed?.(4) ?? 'UNKNOWN'} |

**Strategy NOT started. Operator review required.**
`);

  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-REVIEW-PACKAGE-v1.md'), `# CORVONERO RUN 004 — PHASE 4 REVIEW PACKAGE v1

**Verdict:** \`${resultPayload.phase_verdict}\`

## Mandatory review

- **CR2-PHR-00200** — classifier/policy vs model disagreement (canary residual)

## Review queue

Total items: **${reviewQueue.total_items}**

## Next gate

\`\`\`text
OPERATOR REVIEW OF CORVONERO RUN 004 PHASE 4 RESULT
\`\`\`
`);

  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-NEXT-TASK-v1.md'), `# CORVONERO RUN 004 — PHASE 5 NEXT TASK v1

**Status:** AWAITING OPERATOR REVIEW OF PHASE 4 FULL CORPUS  
**Run ID:** \`${RUN_ID}\`  
**Prerequisite:** \`PASS — OPERATOR REVIEW REQUIRED\` (Phase 4)

## Scope (NOT AUTHORIZED until operator approves)

- Phase 5 semantic review and assembly
- **Forbidden without separate authorization:** Wave 5, advertising strategy, Campaign Architecture, Commander, import, launch

## Entry criteria

- Phase 4 reconciliation PASS
- Operator review of \`CORVONERO-RUN-004-PHASE-4-REVIEW-PACKAGE-v1\`
- Review queue disposition for CR2-PHR-00200 and PSR-AMB-01 family
- Project lifecycle: \`FROZEN_PENDING_SEMANTIC_REVIEW\`

## Counters at Phase 4 close

\`\`\`text
canonical_corpus_total: 2368
unique_assessed_ids: ${results.length}
review_queue_items: ${reviewQueue.total_items}
cumulative_cost_usd: ${resultPayload.cost?.cumulative_cost_usd?.toFixed?.(4) ?? 'UNKNOWN'}
strategy: not started
\`\`\`
`);

  writeJson(path.join(GIT_RUN, 'sanitized-phase4-completion-receipt-v1.json'), {
    run_id: RUN_ID,
    phase_verdict: resultPayload.phase_verdict,
    unique_assessed: results.length,
    cumulative_cost_usd: resultPayload.cost?.cumulative_cost_usd,
    completed_at: resultPayload.completed_at,
  });

  console.log(JSON.stringify({ finalized: true, assessed: results.length, review_queue: reviewQueue.total_items }, null, 2));
}

main();
