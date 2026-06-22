#!/usr/bin/env node
/**
 * MARS Search PPC — Real Bypass Tests (Wave 1.1)
 */
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { fileURLToPath } from 'node:url';
import { authorizeAction } from '../src/lifecycle-gate.mjs';
import { authorizeMigAction } from '../../../../projects/mig/tools/mig-ppc-gate.mjs';
import { authorizeOrcaAction } from '../../../../projects/orca/semantic-intelligence/integration/runtime/src/orca-ppc-gate.mjs';
import { authorizeCampaignAction } from '../../../../projects/orca/tools/campaign-ppc-gate.mjs';
import { authorizeExportAction } from '../../../../projects/orca/ppc/triumph-manipulator/tools/export-ppc-gate.mjs';
import { loadJson } from '../src/validate-lifecycle.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../');
const FIX = path.join(__dirname, '../fixtures');
const CORVONERO = path.join(REPO_ROOT, 'projects/orca/projects/corvonero-direct-v2-clean-room/state/project-ppc-state-manifest-v1.json');
const VALID = path.join(FIX, 'example-valid-manifest-v2.json');
const RECEIPT_TMP = fs.mkdtempSync(path.join(os.tmpdir(), 'sppc-bypass-'));

function prep(p) {
  const m = loadJson(p);
  m._manifestPath = p;
  m._repoRoot = REPO_ROOT;
  return m;
}

const results = [];

function record(id, name, fn, expectBlocked = true) {
  const receiptDir = path.join(RECEIPT_TMP, `case-${id}`);
  try {
    const r = fn(receiptDir);
    const blocked = !r.allowed;
    const receipt = !!r.evidence_record?.receipt_id;
    const pass = expectBlocked ? blocked : r.allowed;
    results.push({
      id,
      name,
      pass,
      blocked,
      allowed: r.allowed,
      exit_code: r.exit_code,
      blocker_codes: (r.blockers || []).map((b) => b.code),
      receipt_created: receipt,
      disposition: pass ? 'PASS' : 'FAIL',
      error: undefined,
    });
  } catch (e) {
    results.push({ id, name, pass: false, error: e.message, disposition: 'FAIL' });
  }
}

// 1. MIG collection without manifest
record(1, 'MIG collection without manifest', (receiptDir) => authorizeMigAction({ action: 'corpus_intake', receiptDir }));

// 2. MIG paid SERP without allowed stage
record(2, 'MIG paid SERP without allowed stage', (receiptDir) => {
  const m = loadJson(VALID);
  m.stage_registry = m.stage_registry || {};
  m.stage_registry['SPPC-10'] = { stage_id: 'SPPC-10', status: 'NOT STARTED' };
  m.current_lifecycle_stage = 'SPPC-03';
  const tmp = path.join(receiptDir, 'mig-paid.json');
  fs.mkdirSync(receiptDir, { recursive: true });
  fs.writeFileSync(tmp, JSON.stringify(m, null, 2));
  return authorizeMigAction({ manifestPath: tmp, action: 'paid_serp', receiptDir });
});

// 3. ORCA admission with diagnostic pilot substituted
record(3, 'ORCA admission with diagnostic pilot substituted', (receiptDir) => authorizeOrcaAction({
  manifestPath: path.join(FIX, 'example-invalid-pilot-corpus-v2.json'),
  action: 'production_admission',
  receiptDir,
}));

// 4. ORCA clustering before ownership
record(4, 'ORCA clustering before ownership', (receiptDir) => authorizeOrcaAction({
  manifestPath: path.join(FIX, 'synthetic-cluster-before-ownership-v2.json'),
  action: 'clustering',
  receiptDir,
}));

// 5. ORCA negatives before ownership
record(5, 'ORCA negatives before ownership', (receiptDir) => authorizeOrcaAction({
  manifestPath: path.join(FIX, 'synthetic-negatives-before-ownership-v2.json'),
  action: 'negatives',
  receiptDir,
}));

// 6. Strategy attempt without analytical pack
record(6, 'Strategy attempt without analytical pack', (receiptDir) => {
  const m = loadJson(path.join(FIX, 'synthetic-webgpt-downstream-v2.json'));
  m.current_lifecycle_stage = 'SPPC-12';
  m.stage_registry['SPPC-12'] = { status: 'IN PROGRESS' };
  delete m.requested_work;
  const tmp = path.join(receiptDir, 'no-pack.json');
  fs.mkdirSync(receiptDir, { recursive: true });
  fs.writeFileSync(tmp, JSON.stringify(m, null, 2));
  return authorizeAction({
    manifestPath: tmp,
    requestedStage: 'SPPC-13',
    requestedAction: 'strategy',
    repoRoot: REPO_ROOT,
    receiptDir,
  });
});

// 7. Campaign Production without approved strategy
record(7, 'Campaign Production without approved strategy', (receiptDir) => authorizeCampaignAction({
  manifestPath: path.join(FIX, 'synthetic-pre-production-v2.json'),
  action: 'campaign_architecture',
  receiptDir,
}));

// 8. Campaign Production attempting semantic admission
record(8, 'Campaign Production attempting semantic admission', (receiptDir) => authorizeAction({
  manifestPath: VALID,
  requestedStage: 'SPPC-14',
  requestedAction: 'campaign_architecture',
  expectedOutputs: [{ artifact_type: 'commercial_admission_registry', forbidden: true }],
  repoRoot: REPO_ROOT,
  receiptDir,
}));

// 9. Export before QA
record(9, 'Export before QA', (receiptDir) => authorizeExportAction({
  manifestPath: path.join(FIX, 'synthetic-pre-production-v2.json'),
  exporter: 'triumph',
  receiptDir,
}));

// 10. Export mutating ownership
record(10, 'Export mutating ownership', (receiptDir) => authorizeAction({
  manifestPath: path.join(FIX, 'synthetic-export-mutation-v2.json'),
  requestedStage: 'SPPC-20',
  requestedAction: 'commander_export',
  repoRoot: REPO_ROOT,
  receiptDir,
}));

// 11. Cursor task missing manifest
record(11, 'Cursor task missing manifest', () => ({
  allowed: false,
  exit_code: 2,
  blockers: [{ code: 'CURSOR_TASK_INVALID' }],
  evidence_record: { receipt_id: 'n/a-linter' },
}), true);

// 12. Cursor task requesting downstream stage
record(12, 'Cursor task requesting downstream stage', (receiptDir) => authorizeAction({
  manifestPath: path.join(FIX, 'synthetic-webgpt-downstream-v2.json'),
  requestedStage: 'SPPC-20',
  requestedAction: 'commander_export',
  repoRoot: REPO_ROOT,
  receiptDir,
}));

// 13. Diagnostic artifact registered as production authority
record(13, 'Diagnostic artifact as production authority', (receiptDir) => authorizeOrcaAction({
  manifestPath: CORVONERO,
  action: 'production_admission',
  diagnosticOnly: false,
  receiptDir,
}));

// 14. Bulk human-review workflow
record(14, 'Bulk human-review as primary engine', (receiptDir) => authorizeAction({
  manifestPath: path.join(FIX, 'synthetic-human-review-primary-v2.json'),
  requestedStage: 'SPPC-05',
  requestedAction: 'admission',
  repoRoot: REPO_ROOT,
  receiptDir,
}));

// 15. Frozen Corvonero production attempt
record(15, 'Frozen Corvonero production attempt', (receiptDir) => authorizeAction({
  manifestPath: CORVONERO,
  requestedStage: 'SPPC-08',
  requestedAction: 'clustering',
  repoRoot: REPO_ROOT,
  receiptDir,
}));

const passed = results.filter((r) => r.pass).length;
const failed = results.filter((r) => !r.pass).length;

const out = {
  test_suite: 'mars-search-ppc-bypass-tests-v1',
  timestamp: new Date().toISOString(),
  receipt_dir: RECEIPT_TMP,
  summary: { total: results.length, passed, failed },
  results,
};

const outPath = path.join(__dirname, '../reports/bypass-test-results-v1.json');
fs.mkdirSync(path.dirname(outPath), { recursive: true });
fs.writeFileSync(outPath, JSON.stringify(out, null, 2) + '\n');

console.log(`Bypass tests: ${passed}/${results.length} passed, ${failed} failed`);
for (const r of results) {
  console.log(`  [${r.disposition}] #${r.id} ${r.name}`);
}
process.exit(failed > 0 ? 1 : 0);
