#!/usr/bin/env node
/**
 * Freeze Corvonero Run 004 Phase 4 partial result (1599/2368).
 * No provider calls. No ORCA changes.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { analyzeCareerAcceptGate } from './career-stop-gate-v1.mjs';
import { classifyCorpusV2 } from './canary-family-classifier-v2.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');
const RUN_ID = 'corv-semantic-v2-20260626-004';
const PILOT = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/pilots/corvonero');
const REPORTS = path.join(REPO_ROOT, 'projects/mars-search-ppc-production/reports');
const STORAGE = path.join('C:\\MARS Phenix\\AI MARS STORAGE', 'mig', 'corvonero', 'semantic-runs', RUN_ID);
const GIT_RUN = path.join(PILOT, 'runs', RUN_ID);
const CORPUS_REL = 'projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-canonical-phrase-registry-v1.json';
const FIX = path.join(REPO_ROOT, 'projects/orca/semantic-intelligence/live-model/fixtures');

const CANONICAL_TOTAL = 2368;
const PHASE_VERDICT = 'PARTIAL ACCEPTED — OPERATOR REVIEW REQUIRED';
const RUN_LIFECYCLE = 'PHASE_4_PARTIAL_COMPLETE';
const PROJECT_LIFECYCLE = 'READY_FOR_PARTIAL_SEMANTIC_REVIEW';

const STATUS = {
  phase_4: PHASE_VERDICT,
  run_004: RUN_LIFECYCLE,
  project: PROJECT_LIFECYCLE,
  provider_calls: 'FROZEN — NO FURTHER OPENROUTER CALLS THIS CYCLE',
};

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

function authoritativeVerdict(r) {
  return r.final_authoritative_verdict || r.final_verdict;
}

function pct(n, d) {
  return d ? ((n / d) * 100).toFixed(1) : '0.0';
}

function buildReviewQueue(results, operatorOverrides, careerGate) {
  const queue = [];
  const add = (r, reason, extra = {}) => {
    if (!r?.phrase_id || queue.find((q) => q.phrase_id === r.phrase_id)) return;
    queue.push({
      phrase_id: r.phrase_id,
      phrase: r.phrase,
      review_reason: reason,
      primary_family: r.primary_family,
      final_verdict: authoritativeVerdict(r),
      model_verdict: r.model_verdict || r.final_verdict,
      review_state: 'REVIEW_QUEUE',
      partial_corpus_only: true,
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
    const r = results.find((x) => x.phrase_id === ov.phrase_id);
    add(r || { phrase_id: ov.phrase_id, phrase: ov.phrase }, `Operator override — ${ov.phrase_id}`, {
      operator_override: ov,
    });
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
    queue_id: 'corvonero-run-004-phase-4-partial-review-queue-v1',
    run_id: RUN_ID,
    corpus_scope: 'partial',
    processed_total: results.length,
    canonical_total: CANONICAL_TOTAL,
    mandatory_items: ['CR2-PHR-00200', 'CR2-PHR-00584'],
    total_items: queue.length,
    items: queue.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id)),
    created_at: new Date().toISOString(),
  };
}

function main() {
  const registryPath = path.join(STORAGE, 'checkpoints', 'phase4-semantic-registry-v1.json');
  const checkpointPath = path.join(STORAGE, 'checkpoints', 'checkpoint-phase4-v1.json');
  const overridePath = path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-OPERATOR-OVERRIDES-v1.json');
  const reconciliationPath = path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-TRIGGER-RECONCILIATION-v1.json');

  const registry = readJson(registryPath);
  const checkpoint = readJson(checkpointPath);
  const results = registry.results || [];
  const operatorOverrides = fs.existsSync(overridePath) ? readJson(overridePath).overrides || [] : [];
  const overrideMap = new Map(operatorOverrides.map((o) => [o.phrase_id, o]));
  const reconciliation = fs.existsSync(reconciliationPath) ? readJson(reconciliationPath) : null;

  const corpus = readJson(path.join(REPO_ROOT, CORPUS_REL));
  const phrases = corpus.phrases || corpus.records || corpus;
  const byId = new Map(phrases.map((p) => [p.phrase_id, p]));

  const processedIds = new Set(results.map((r) => r.phrase_id));
  if (processedIds.size !== results.length) {
    console.error('BLOCKED — duplicate IDs in registry');
    process.exit(2);
  }

  const unprocessed = phrases
    .filter((p) => !processedIds.has(p.phrase_id))
    .sort((a, b) => a.phrase_id.localeCompare(b.phrase_id));

  if (results.length !== 1599 || unprocessed.length !== 769) {
    console.error(JSON.stringify({
      error: 'COUNT_MISMATCH',
      processed: results.length,
      unprocessed: unprocessed.length,
      expected: { processed: 1599, unprocessed: 769 },
    }));
    process.exit(2);
  }

  const context = {
    businessScope: readJson(path.join(FIX, 'business-scope-eval-v1.json')),
    serviceRegistry: readJson(path.join(FIX, 'service-registry-eval-v1.json')),
  };
  const classifiedById = new Map(classifyCorpusV2(phrases, context).map((c) => [c.phrase_id, c]));
  const careerGate = analyzeCareerAcceptGate(results, classifiedById, overrideMap);

  const dist = { ACCEPT: 0, REJECT: 0, ABSTAIN: 0 };
  const acceptRecords = [];
  const rejectRecords = [];
  const abstainRecords = [];

  for (const r of results) {
    const v = authoritativeVerdict(r);
    if (v) dist[v] = (dist[v] || 0) + 1;
    const slim = {
      phrase_id: r.phrase_id,
      phrase: r.phrase,
      model_verdict: r.model_verdict ?? r.final_verdict,
      final_authoritative_verdict: authoritativeVerdict(r),
      primary_verdict: r.primary_verdict,
      reassessment_verdict: r.reassessment_verdict,
      primary_family: r.primary_family,
      observed_tags: r.observed_tags,
      production_source: r.production_source,
      operator_override: r.operator_override || overrideMap.get(r.phrase_id) || null,
      assessed_at: r.assessed_at,
    };
    if (v === 'ACCEPT') acceptRecords.push(slim);
    else if (v === 'REJECT') rejectRecords.push(slim);
    else if (v === 'ABSTAIN') abstainRecords.push(slim);
  }

  const processedManifest = {
    manifest_id: 'corvonero-run-004-phase-4-processed-ids-manifest-v1',
    run_id: RUN_ID,
    canonical_total: CANONICAL_TOTAL,
    processed_count: results.length,
    coverage_rate: Number((results.length / CANONICAL_TOTAL).toFixed(6)),
    provenance: {
      canary_attempt_2_reused: results.filter((r) => r.production_source === 'CANARY_ATTEMPT_2_REUSE').length,
      phase_4_new: results.filter((r) => r.production_source === 'PHASE_4_NEW').length,
    },
    batch_receipts: checkpoint.batch_receipts || [],
    records: results
      .map((r) => ({
        phrase_id: r.phrase_id,
        phrase: r.phrase,
        final_authoritative_verdict: authoritativeVerdict(r),
        model_verdict: r.model_verdict ?? r.final_verdict,
        production_source: r.production_source,
        operator_override_applied: !!r.operator_override || overrideMap.has(r.phrase_id),
      }))
      .sort((a, b) => a.phrase_id.localeCompare(b.phrase_id)),
    created_at: new Date().toISOString(),
  };

  const unprocessedManifest = {
    manifest_id: 'corvonero-run-004-phase-4-unprocessed-ids-manifest-v1',
    run_id: RUN_ID,
    canonical_total: CANONICAL_TOTAL,
    unprocessed_count: unprocessed.length,
    reason: 'ENDPOINT_FAILED on retry batches 024–031; operator freeze — no further provider calls this cycle',
    records: unprocessed.map((p) => ({
      phrase_id: p.phrase_id,
      phrase: p.phrase,
      combined_frequency: p.combined_frequency ?? null,
    })),
    created_at: new Date().toISOString(),
  };

  const reviewQueue = buildReviewQueue(results, operatorOverrides, careerGate);

  const limitation = {
    statement_id: 'corvonero-run-004-phase-4-partial-limitation-v1',
    run_id: RUN_ID,
    canonical_total: CANONICAL_TOTAL,
    processed_unique: results.length,
    unprocessed: unprocessed.length,
    coverage_percent: pct(results.length, CANONICAL_TOTAL),
    limitation:
      'All semantic verdicts, registries, review packages, and Phase 5 entry work in this cycle are based on 1599 of 2368 canonical records only. The remaining 769 IDs were not assessed and must not be inferred, imputed, or extrapolated.',
    provider_calls: 'FROZEN for this cycle',
    operator_override_preserved: ['CR2-PHR-00584'],
    created_at: new Date().toISOString(),
  };

  const partialResult = {
    run_id: RUN_ID,
    result_id: 'corvonero-run-004-phase-4-partial-result-v1',
    phase_verdict: PHASE_VERDICT,
    lifecycle_state: RUN_LIFECYCLE,
    project_lifecycle: PROJECT_LIFECYCLE,
    status: STATUS,
    reconciliation: {
      canonical_total: CANONICAL_TOTAL,
      unique_processed: results.length,
      unprocessed: unprocessed.length,
      duplicates: 0,
      orphans: 0,
      complete: false,
      partial_accepted: true,
      identity_equation: '120 canary reuse + 1479 phase4 new = 1599 processed (769 unprocessed)',
    },
    verdict_distribution: dist,
    career_gate: careerGate,
    operator_overrides: operatorOverrides,
    trigger_reconciliation: reconciliation,
    cost: { cumulative_cost_usd: checkpoint.cumulative_cost_usd },
    batch_count: (checkpoint.batch_receipts || []).length,
    frozen_at: new Date().toISOString(),
  };

  const freezeReceipt = {
    receipt_id: 'phase-4-partial-freeze-v1',
    run_id: RUN_ID,
    ...STATUS,
    processed: results.length,
    unprocessed: unprocessed.length,
    frozen_at: partialResult.frozen_at,
    checkpoint_preserved: true,
    provider_calls_after_freeze: 'PROHIBITED',
  };

  // Update checkpoint (preserve batches, no provider calls)
  checkpoint.lifecycle_state = RUN_LIFECYCLE;
  checkpoint.phase_verdict = PHASE_VERDICT;
  checkpoint.project_lifecycle = PROJECT_LIFECYCLE;
  checkpoint.canonical_total = CANONICAL_TOTAL;
  checkpoint.unique_assessed_total = results.length;
  checkpoint.missing = unprocessed.length;
  checkpoint.complete = false;
  checkpoint.partial_accepted = true;
  checkpoint.provider_calls_frozen = true;
  checkpoint.frozen_at = partialResult.frozen_at;
  checkpoint.stop_reason = null;
  writeJson(checkpointPath, checkpoint);

  writeJson(registryPath, {
    ...registry,
    run_id: RUN_ID,
    partial_accepted: true,
    complete: false,
    frozen_at: partialResult.frozen_at,
    processed_count: results.length,
    unprocessed_count: unprocessed.length,
    results: results.sort((a, b) => a.phrase_id.localeCompare(b.phrase_id)),
  });

  // Pilot artifacts
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-RESULT-v1.json'), partialResult);
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PROCESSED-IDS-MANIFEST-v1.json'), processedManifest);
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-UNPROCESSED-IDS-MANIFEST-v1.json'), unprocessedManifest);
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-ACCEPT-REGISTRY-v1.json'), {
    run_id: RUN_ID, count: acceptRecords.length, records: acceptRecords,
  });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-REJECT-REGISTRY-v1.json'), {
    run_id: RUN_ID, count: rejectRecords.length, records: rejectRecords,
  });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-ABSTAIN-REGISTRY-v1.json'), {
    run_id: RUN_ID, count: abstainRecords.length, records: abstainRecords,
  });
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-REVIEW-QUEUE-v1.json'), reviewQueue);
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-LIMITATION-v1.json'), limitation);

  // Storage mirrors
  writeJson(path.join(STORAGE, 'reports', 'partial-accept-registry-v1.json'), { run_id: RUN_ID, count: acceptRecords.length, records: acceptRecords });
  writeJson(path.join(STORAGE, 'reports', 'partial-reject-registry-v1.json'), { run_id: RUN_ID, count: rejectRecords.length, records: rejectRecords });
  writeJson(path.join(STORAGE, 'reports', 'partial-abstain-registry-v1.json'), { run_id: RUN_ID, count: abstainRecords.length, records: abstainRecords });
  writeJson(path.join(STORAGE, 'reports', 'partial-semantic-registry-v1.json'), { run_id: RUN_ID, processed: results.length, results });
  writeJson(path.join(STORAGE, 'receipts', 'phase-4-partial-freeze-v1.json'), freezeReceipt);

  const limitationMd = `# CORVONERO RUN 004 — PHASE 4 PARTIAL LIMITATION v1

**Run ID:** \`${RUN_ID}\`

## Scope limitation

This cycle's semantic output is based on **${results.length} of ${CANONICAL_TOTAL}** canonical records (**${pct(results.length, CANONICAL_TOTAL)}%** coverage).

- **Processed and saved:** ${results.length} unique IDs
- **Not assessed:** ${unprocessed.length} IDs
- **Duplicates:** 0
- **Orphans:** 0

The remaining ${unprocessed.length} records must **not** be inferred, imputed, extrapolated, or treated as assessed for strategy, campaign architecture, or import.

## Provider freeze

No further OpenRouter / model calls are authorized for Run 004 in this cycle.

## Preserved adjudication

- Original model verdicts preserved in registry
- Operator override for \`CR2-PHR-00584\`: model ACCEPT → authoritative REJECT
`;

  const partialResultMd = `# CORVONERO RUN 004 — PHASE 4 PARTIAL RESULT v1

**Run ID:** \`${RUN_ID}\`  
**Phase verdict:** \`${PHASE_VERDICT}\`  
**Run lifecycle:** \`${RUN_LIFECYCLE}\`  
**Project lifecycle:** \`${PROJECT_LIFECYCLE}\`

## Summary

| Metric | Value |
|--------|------:|
| Canonical total | ${CANONICAL_TOTAL} |
| Processed (unique) | ${results.length} |
| Unprocessed | ${unprocessed.length} |
| ACCEPT | ${dist.ACCEPT} (${pct(dist.ACCEPT, results.length)}%) |
| REJECT | ${dist.REJECT} (${pct(dist.REJECT, results.length)}%) |
| ABSTAIN | ${dist.ABSTAIN} (${pct(dist.ABSTAIN, results.length)}%) |
| Review queue | ${reviewQueue.total_items} |
| Cumulative cost (USD) | ${checkpoint.cumulative_cost_usd?.toFixed?.(4) ?? 'UNKNOWN'} |
| Batches completed | ${(checkpoint.batch_receipts || []).length} |

## Provenance

- Canary attempt 2 reuse: ${processedManifest.provenance.canary_attempt_2_reused}
- Phase 4 new production: ${processedManifest.provenance.phase_4_new}

**Provider calls frozen. Phase 5 not auto-started.**
`;

  const phase5PartialMd = `# CORVONERO RUN 004 — PHASE 5 NEXT TASK (PARTIAL CORPUS) v1

**Status:** AWAITING OPERATOR AUTHORIZATION — PARTIAL CORPUS ONLY  
**Run ID:** \`${RUN_ID}\`  
**Prerequisite:** \`${PHASE_VERDICT}\`

## Hard constraints

- Work **only** with the **1599** processed records in partial registries
- **No new OpenRouter / model calls**
- **No** inference or imputation for the **769** unprocessed IDs
- **No** canonical corpus, ORCA, or Run 002/003 changes
- **No** advertising strategy, Campaign Architecture, Commander, import, or Wave 5 without separate authorization

## Entry artifacts

- \`CORVONERO-RUN-004-PHASE-4-PARTIAL-RESULT-v1.json\`
- \`CORVONERO-RUN-004-PHASE-4-PROCESSED-IDS-MANIFEST-v1.json\`
- \`CORVONERO-RUN-004-PHASE-4-UNPROCESSED-IDS-MANIFEST-v1.json\`
- \`CORVONERO-RUN-004-PHASE-4-PARTIAL-ACCEPT-REGISTRY-v1.json\`
- \`CORVONERO-RUN-004-PHASE-4-PARTIAL-REJECT-REGISTRY-v1.json\`
- \`CORVONERO-RUN-004-PHASE-4-PARTIAL-ABSTAIN-REGISTRY-v1.json\`
- \`CORVONERO-RUN-004-PHASE-4-PARTIAL-REVIEW-QUEUE-v1.json\`
- \`CORVONERO-RUN-004-PHASE-4-PARTIAL-LIMITATION-v1.json\`

## Phase 5 partial scope (documentation / human review only)

1. Operator review of partial review queue (${reviewQueue.total_items} items)
2. Disposition of mandatory items: \`CR2-PHR-00200\`, \`CR2-PHR-00584\`
3. Partial semantic assembly pack for **1599** IDs only (accept/reject/abstain registries)
4. Explicit exclusion manifest for **769** unprocessed IDs in all downstream docs
5. Decision record: accept partial coverage for interim workflow **or** schedule separate authorized resume for remaining 769

## Not in scope

- Live model reassessment
- Full-corpus reconciliation (2368/2368)
- Strategy generation or campaign launch

## Next gate

\`\`\`text
OPERATOR REVIEW — CORVONERO RUN 004 PARTIAL PHASE 4 (1599/2368)
\`\`\`
`;

  const reviewPackageMd = `# CORVONERO RUN 004 — PHASE 4 PARTIAL REVIEW PACKAGE v1

**Verdict:** \`${PHASE_VERDICT}\`  
**Scope:** ${results.length}/${CANONICAL_TOTAL} canonical records

## Mandatory review

- **CR2-PHR-00200**
- **CR2-PHR-00584** (operator override preserved)

## Review queue

Total: **${reviewQueue.total_items}** items (partial corpus only)

## Limitation

See \`CORVONERO-RUN-004-PHASE-4-PARTIAL-LIMITATION-v1.md\`
`;

  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-LIMITATION-v1.md'), limitationMd);
  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-RESULT-v1.md'), partialResultMd);
  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-5-NEXT-TASK-PARTIAL-v1.md'), phase5PartialMd);
  writeText(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-REVIEW-PACKAGE-v1.md'), reviewPackageMd);
  writeJson(path.join(PILOT, 'CORVONERO-RUN-004-PHASE-4-PARTIAL-REVIEW-PACKAGE-v1.json'), {
    package_id: 'corvonero-run-004-phase-4-partial-review-package-v1',
    run_id: RUN_ID,
    phase_verdict: PHASE_VERDICT,
    lifecycle_state: RUN_LIFECYCLE,
    project_lifecycle: PROJECT_LIFECYCLE,
    processed: results.length,
    unprocessed: unprocessed.length,
    review_queue_size: reviewQueue.total_items,
    limitation_ref: 'CORVONERO-RUN-004-PHASE-4-PARTIAL-LIMITATION-v1.json',
    next_gate: 'OPERATOR REVIEW — CORVONERO RUN 004 PARTIAL PHASE 4 (1599/2368)',
  });

  const reportMd = `# REPORT — CORVONERO RUN 004 PHASE 4 PARTIAL FREEZE v1

**Run ID:** \`${RUN_ID}\`  
**Frozen at:** ${partialResult.frozen_at}

## Status

| Layer | Value |
|-------|-------|
| PHASE 4 | \`${PHASE_VERDICT}\` |
| Run 004 | \`${RUN_LIFECYCLE}\` |
| Project | \`${PROJECT_LIFECYCLE}\` |

## Counts

| Metric | Value |
|--------|------:|
| Canonical | ${CANONICAL_TOTAL} |
| Processed | ${results.length} |
| Unprocessed | ${unprocessed.length} |
| Duplicates | 0 |
| Orphans | 0 |

## Verdict distribution (1599)

| Verdict | Count | % |
|---------|------:|--:|
| ACCEPT | ${dist.ACCEPT} | ${pct(dist.ACCEPT, results.length)}% |
| REJECT | ${dist.REJECT} | ${pct(dist.REJECT, results.length)}% |
| ABSTAIN | ${dist.ABSTAIN} | ${pct(dist.ABSTAIN, results.length)}% |

## Review queue

${reviewQueue.total_items} items

## Actions taken

- Checkpoint and ${(checkpoint.batch_receipts || []).length} batch receipts preserved
- Provider calls frozen (no OpenRouter)
- ORCA unchanged
- Operator override CR2-PHR-00584 preserved

## Outputs

See \`pilots/corvonero/CORVONERO-RUN-004-PHASE-4-PARTIAL-*-v1.*\`
`;

  writeText(path.join(REPORTS, 'REPORT-corvonero-run-004-phase-4-partial-freeze-v1.md'), reportMd);

  if (fs.existsSync(GIT_RUN)) {
    writeJson(path.join(GIT_RUN, 'sanitized-phase4-partial-freeze-receipt-v1.json'), freezeReceipt);
    writeJson(path.join(GIT_RUN, 'lifecycle-decision-partial-v1.json'), {
      run_id: RUN_ID,
      decision: RUN_LIFECYCLE,
      phase_4: PHASE_VERDICT,
      project: PROJECT_LIFECYCLE,
      processed: results.length,
      unprocessed: unprocessed.length,
      provider_calls_frozen: true,
    });
  }

  // Lock note (already RELEASED)
  const lockPath = path.join(STORAGE, 'locks', 'run-phase4.lock.json');
  if (fs.existsSync(lockPath)) {
    const lock = readJson(lockPath);
    lock.freeze_note = 'PHASE_4_PARTIAL_COMPLETE — provider calls frozen';
    lock.frozen_at = partialResult.frozen_at;
    writeJson(lockPath, lock);
  }

  console.log(JSON.stringify({
    frozen: true,
    phase_verdict: PHASE_VERDICT,
    lifecycle: RUN_LIFECYCLE,
    processed: results.length,
    unprocessed: unprocessed.length,
    dist,
    review_queue: reviewQueue.total_items,
  }, null, 2));
}

main();
