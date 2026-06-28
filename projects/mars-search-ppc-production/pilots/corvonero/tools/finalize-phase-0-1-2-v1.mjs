#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const RUN_ID = 'corv-semantic-v2-20260626-002';
const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../../../..');
const STORAGE = path.join('C:\\MARS Phenix\\AI MARS STORAGE', 'mig', 'corvonero', 'semantic-runs', RUN_ID);
const GIT_RUN = path.join(REPO, 'projects/mars-search-ppc-production/pilots/corvonero/runs', RUN_ID);
const PILOT = path.join(REPO, 'projects/mars-search-ppc-production/pilots/corvonero');
const REPORTS = path.join(REPO, 'projects/mars-search-ppc-production/reports');

function write(p, data) {
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, typeof data === 'string' ? data : JSON.stringify(data, null, 2));
}

const suiteResults = {
  wave31f_bypass: { pass: true, score: '12/12', live: false },
  under_admission: { pass: true, score: '16/16', live: false },
  closed_dataset_regression: {
    pass: true,
    run_id: 'closed-regression-1782418950653',
    product_fpr: 0,
    boxed_delivery_fixed: true,
    cost_usd: 0.2844255,
  },
  confirmation_product: {
    pass: false,
    run_id: 'confirmation-product-pass-1782425250184',
    gate_pass: false,
    false_positive_rate: 0.0125,
    false_accepts: [{ record_id: 'CFM-PROD-UPD-02', query: 'обновление sap business one до новой версии' }],
    cost_usd: 0.2175288,
  },
  confirmation_geo_v2: {
    pass: true,
    run_id: 'confirmation-geo-pass-1782429005975',
    gate_pass: true,
    adversarial_false_accept_rate: 0,
    commercial_recall: 1,
    cost_usd: 0.243093,
  },
  problem_query_policy: {
    pass: false,
    run_id: 'problem-policy-regression-1782429006146',
    score: '9/10',
    failure: { record_id: 'PQR-ABSTAIN-03', query: 'как исправить ошибку 0x80004005 1с', expected: 'ABSTAIN', final: 'REJECT' },
  },
};

const cumulativeCost = 0.2844255 + 0.2175288 + 0.243093 + 0.05;
const gateB = { status: 'FAILED', project: 'BLOCKED_AT_SPPC_05' };
const gateCriteria = {
  adversarial_fpr_max_0_01_product: false,
  adversarial_fpr_max_0_01_geo: true,
  closed_dataset_boxed_delivery_fixed: true,
  closed_dataset_product_fpr: true,
  problem_query_all_match: false,
  wave31f_bypass_all_pass: true,
  under_admission_all_pass: true,
  all_pass: false,
  critical_failures: [
    'Product confirmation adversarial FPR 0.0125 exceeds canonical threshold 0.01 (CFM-PROD-UPD-02)',
    'Problem query policy 9/10 — PQR-ABSTAIN-03 expected ABSTAIN received REJECT',
  ],
};

const lockPath = path.join(STORAGE, 'locks', 'run.lock.json');
const lock = JSON.parse(fs.readFileSync(lockPath, 'utf8'));
lock.status = 'RELEASED';
lock.released_at = new Date().toISOString();
lock.release_outcome = gateB.status;
write(lockPath, lock);
write(path.join(STORAGE, 'receipts', 'lock-release-receipt-v1.json'), {
  run_id: RUN_ID,
  released_at: lock.released_at,
  outcome: gateB.status,
  reason: 'SPPC-05 critical criteria failure — fail-closed',
});

const sppc05Report = {
  report_id: 'corvonero-new-controlled-sppc-05-execution-v1',
  run_id: RUN_ID,
  provider: 'openrouter',
  model: 'openai/gpt-5-mini',
  prompt_contract_version: 'orca-semantic-assessment-prompt-v1.3',
  adjudicator_version: 'v1.3',
  gate_b_verdict: gateB,
  gate_criteria: gateCriteria,
  suite_results: suiteResults,
  cumulative_cost_usd: cumulativeCost,
  isolation_verdict: 'OLD_RUN_ISOLATION — PASS',
  full_corpus_started: false,
  wave5_started: false,
  completed_at: new Date().toISOString(),
};
write(path.join(STORAGE, 'reports', 'sppc-05-execution-report-v1.json'), sppc05Report);

const runManifest = JSON.parse(fs.readFileSync(path.join(STORAGE, 'manifests', 'run-manifest-v1.json'), 'utf8'));
runManifest.lifecycle_phase = 'BLOCKED_AT_SPPC_05';
runManifest.gate_b = gateB.status;
write(path.join(STORAGE, 'manifests', 'run-manifest-v1.json'), runManifest);

write(path.join(STORAGE, 'checkpoints', 'checkpoint-sppc05-complete-v1.json'), {
  run_id: RUN_ID,
  phase: 'BLOCKED_AT_SPPC_05',
  corpus_checksum: runManifest.corpus_sha256,
  total_input_count: 2368,
  processed_ids: [],
  processed_count: 0,
  cumulative_cost_usd: cumulativeCost,
  complete: false,
  gate_b_verdict: gateB.status,
  sppc_05_completed_at: new Date().toISOString(),
});

const receipt = {
  run_id: RUN_ID,
  phase: '0/1/2',
  gate_a: 'APPROVED',
  gate_b: gateB.status,
  lifecycle_state: gateB.project,
  provider: 'openrouter',
  model: 'openai/gpt-5-mini',
  cumulative_cost_usd: cumulativeCost,
  full_corpus_started: false,
  completed_at: new Date().toISOString(),
};
write(path.join(STORAGE, 'receipts', 'phase-0-1-2-execution-receipt-v1.json'), receipt);

write(path.join(GIT_RUN, 'run-manifest-v1.json'), runManifest);
write(path.join(GIT_RUN, 'immutable-input-reference-v1.json'), JSON.parse(fs.readFileSync(path.join(STORAGE, 'manifests', 'immutable-input-reference-v1.json'), 'utf8')));
write(path.join(GIT_RUN, 'sanitized-execution-receipt-v1.json'), receipt);
write(path.join(GIT_RUN, 'reports', 'sppc-05-sanitized-report-v1.json'), sppc05Report);
write(path.join(GIT_RUN, 'lifecycle-decision-v1.json'), {
  run_id: RUN_ID,
  decision: 'BLOCKED_AT_SPPC_05',
  next_gate: 'OPERATOR REVIEW OF CORVONERO NEW CONTROLLED RUN SPPC-05 RESULT',
  canary_authorized: false,
  full_corpus_authorized: false,
});

write(path.join(PILOT, 'CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-PHASE-0-1-2-RESULT-v1.json'), {
  result_id: 'corvonero-new-controlled-semantic-run-phase-0-1-2-result-v1',
  run_id: RUN_ID,
  gate_a: 'APPROVED',
  gate_b: gateB,
  lifecycle_state: gateB.project,
  cumulative_cost_usd: cumulativeCost,
  suites: suiteResults,
  gate_criteria: gateCriteria,
});
write(path.join(PILOT, 'CORVONERO-NEW-CONTROLLED-SEMANTIC-RUN-SPPC-05-REVIEW-PACKAGE-v1.json'), sppc05Report);

console.log(JSON.stringify({ run_id: RUN_ID, gate_b: gateB, cost: cumulativeCost }, null, 2));
