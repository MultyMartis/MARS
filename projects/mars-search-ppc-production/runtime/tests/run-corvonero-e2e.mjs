#!/usr/bin/env node
/**
 * MARS Search PPC — Corvonero Frozen Project E2E Gate Test (Wave 1.1)
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

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../');
const MANIFEST = path.join(REPO_ROOT, 'projects/orca/projects/corvonero-direct-v2-clean-room/state/project-ppc-state-manifest-v1.json');
const RECEIPT_DIR = fs.mkdtempSync(path.join(os.tmpdir(), 'sppc-corv-e2e-'));

const SCENARIOS = [
  { name: 'MIG source inspection (read-only)', fn: () => authorizeAction({ manifestPath: MANIFEST, requestedAction: 'source_inspection', repoRoot: REPO_ROOT, receiptDir: RECEIPT_DIR }), expectAllowed: true },
  { name: 'MIG paid SERP collection', fn: () => authorizeMigAction({ manifestPath: MANIFEST, action: 'paid_serp', receiptDir: RECEIPT_DIR }), expectAllowed: false },
  { name: 'ORCA production admission', fn: () => authorizeOrcaAction({ manifestPath: MANIFEST, action: 'production_admission', receiptDir: RECEIPT_DIR }), expectAllowed: false },
  { name: 'ORCA clustering', fn: () => authorizeOrcaAction({ manifestPath: MANIFEST, action: 'clustering', receiptDir: RECEIPT_DIR }), expectAllowed: false },
  { name: 'ORCA negatives', fn: () => authorizeOrcaAction({ manifestPath: MANIFEST, action: 'negatives', receiptDir: RECEIPT_DIR }), expectAllowed: false },
  { name: 'Strategy', fn: () => authorizeAction({ manifestPath: MANIFEST, requestedStage: 'SPPC-13', requestedAction: 'strategy', repoRoot: REPO_ROOT, receiptDir: RECEIPT_DIR }), expectAllowed: false },
  { name: 'Campaign production', fn: () => authorizeCampaignAction({ manifestPath: MANIFEST, action: 'campaign_architecture', receiptDir: RECEIPT_DIR }), expectAllowed: false },
  { name: 'Commander export', fn: () => authorizeExportAction({ manifestPath: MANIFEST, exporter: 'triumph', receiptDir: RECEIPT_DIR }), expectAllowed: false },
  { name: 'Launch', fn: () => authorizeAction({ manifestPath: MANIFEST, requestedStage: 'SPPC-21', requestedAction: 'launch', repoRoot: REPO_ROOT, receiptDir: RECEIPT_DIR }), expectAllowed: false },
];

const results = SCENARIOS.map((s) => {
  const r = s.fn();
  const ok = s.expectAllowed ? r.allowed : !r.allowed;
  return {
    scenario: s.name,
    expect_allowed: s.expectAllowed,
    actual_allowed: r.allowed,
    blockers: (r.blockers || []).map((b) => b.code || b.message),
    receipt_id: r.evidence_record?.receipt_id,
    pass: ok,
  };
});

const passed = results.filter((r) => r.pass).length;
const out = {
  project_id: 'corvonero-direct-v2-clean-room',
  lifecycle_status: 'FROZEN',
  manifest: MANIFEST,
  receipt_dir: RECEIPT_DIR,
  summary: { total: results.length, passed, failed: results.length - passed },
  results,
};

const outPath = path.join(__dirname, '../reports/corvonero-e2e-gate-v1.json');
fs.writeFileSync(outPath, JSON.stringify(out, null, 2) + '\n');
console.log(`Corvonero E2E: ${passed}/${results.length} passed`);
process.exit(passed === results.length ? 0 : 1);
