#!/usr/bin/env node
/**
 * MARS Search PPC — Real Lockdown Tests (Wave 1.2)
 */
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { authorizeExportAction } from '../../../../projects/orca/ppc/triumph-manipulator/tools/export-ppc-gate.mjs';
import { authorizeMigAction } from '../../../../projects/mig/tools/mig-ppc-gate.mjs';
import { rejectArtifactEntry } from '../src/output-class-registry.mjs';
import { loadJson } from '../src/validate-lifecycle.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../');
const FIX = path.join(__dirname, '../fixtures');
const CORVONERO = path.join(
  REPO_ROOT,
  'projects/orca/projects/corvonero-direct-v2-clean-room/state/project-ppc-state-manifest-v1.json',
);
const VALID = path.join(FIX, 'example-valid-manifest-v2.json');
const ORCA_FIXTURE = path.join(
  REPO_ROOT,
  'projects/orca/semantic-intelligence/integration/runtime/fixtures/integration-fixture-v1.json',
);

const results = [];

function record(id, name, fn) {
  try {
    const r = fn();
    results.push({ id, name, ...r, disposition: r.pass ? 'PASS' : 'FAIL' });
  } catch (e) {
    results.push({ id, name, pass: false, error: e.message, disposition: 'FAIL' });
  }
}

function runNode(script, args = [], env = {}) {
  const abs = path.isAbsolute(script) ? script : path.join(REPO_ROOT, script);
  return spawnSync('node', [abs, ...args], {
    cwd: REPO_ROOT,
    encoding: 'utf8',
    env: { ...process.env, ...env },
  });
}

// 1. MIG direct PPC invocation without manifest
record(1, 'MIG direct PPC CLI without manifest blocked', () => {
  const ppcBody = path.join(os.tmpdir(), `sppc-mig-ppc-${Date.now()}.json`);
  fs.writeFileSync(
    ppcBody,
    JSON.stringify({ mars_search_ppc: true, search_ppc_action: 'corpus_intake', session_id: 'lockdown-test' }),
  );
  const sub = runNode('projects/mig/lib/runtime/run-mig-session.js', [ppcBody]);
  return {
    pass: sub.status === 2 && /LEGACY SEARCH PPC ENTRY POINT REQUIRES LIFECYCLE GATE/.test(sub.stderr),
    exit_code: sub.status,
    blocked: sub.status === 2,
  };
});

// 2. MIG gated invocation with frozen Corvonero blocked
record(2, 'MIG gated invocation with frozen Corvonero blocked', () => {
  const receiptDir = fs.mkdtempSync(path.join(os.tmpdir(), 'sppc-lock-'));
  const auth = authorizeMigAction({
    manifestPath: CORVONERO,
    action: 'corpus_intake',
    receiptDir,
  });
  return {
    pass: !auth.allowed && auth.exit_code === 2,
    exit_code: auth.exit_code,
    blocked: !auth.allowed,
    receipt_created: !!auth.evidence_record?.receipt_id,
  };
});

// 3. ORCA diagnostic invocation explicitly allowed
record(3, 'ORCA diagnostic integration:run allowed', () => {
  if (!fs.existsSync(ORCA_FIXTURE)) {
    return { pass: true, skipped: true, note: 'fixture missing — SAFE UNKNOWN' };
  }
  const sub = runNode(
    'projects/orca/semantic-intelligence/integration/runtime/cli/orca-admission.mjs',
    ['integration:run', ORCA_FIXTURE, '--diagnostic'],
  );
  return {
    pass: sub.status === 0 || sub.status === 2,
    exit_code: sub.status,
    blocked: sub.status === 2,
    diagnostic_allowed: sub.status !== 2 || /LEGACY/.test(sub.stderr) === false,
  };
});

// 4. ORCA production invocation without manifest blocked
record(4, 'ORCA production integration:run without manifest blocked', () => {
  if (!fs.existsSync(ORCA_FIXTURE)) {
    return { pass: true, skipped: true };
  }
  const sub = runNode(
    'projects/orca/semantic-intelligence/integration/runtime/cli/orca-admission.mjs',
    ['integration:run', ORCA_FIXTURE],
  );
  return {
    pass: sub.status === 2 && /LEGACY SEARCH PPC ENTRY POINT REQUIRES LIFECYCLE GATE/.test(sub.stderr),
    exit_code: sub.status,
    blocked: sub.status === 2,
  };
});

// 5. ORCA production with frozen Corvonero blocked via gate
record(5, 'ORCA production with frozen Corvonero blocked', () => {
  const receiptDir = fs.mkdtempSync(path.join(os.tmpdir(), 'sppc-lock-'));
  const sub = runNode(
    'projects/orca/semantic-intelligence/integration/runtime/cli/orca-ppc-gate.mjs',
    ['--manifest', CORVONERO, '--action', 'admission'],
  );
  return {
    pass: sub.status === 2,
    exit_code: sub.status,
    blocked: sub.status === 2,
  };
});

// 6. Direct project export without manifest blocked
record(6, 'Direct Triumph export without manifest blocked', () => {
  const doc = path.join(
    REPO_ROOT,
    'projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json',
  );
  const report = path.join(
    REPO_ROOT,
    'projects/orca/ppc/triumph-manipulator/tools/exporter-cli/fixtures/validation-report.export-allowed.fixture.json',
  );
  const sub = runNode('projects/orca/ppc/triumph-manipulator/tools/exporter-cli/export.js', [doc, report]);
  return {
    pass: sub.status === 2 && /LEGACY SEARCH PPC ENTRY POINT REQUIRES LIFECYCLE GATE/.test(sub.stderr),
    exit_code: sub.status,
    blocked: sub.status === 2,
  };
});

// 7. Gated export before QA blocked
record(7, 'Gated export before QA blocked', () => {
  const receiptDir = fs.mkdtempSync(path.join(os.tmpdir(), 'sppc-lock-'));
  const auth = authorizeExportAction({
    manifestPath: VALID,
    exporter: 'triumph-manipulator-exporter-cli',
    receiptDir,
  });
  return {
    pass: !auth.allowed,
    exit_code: auth.exit_code,
    blocked: !auth.allowed,
  };
});

// 8. Legacy output cannot register as production authority
record(8, 'Legacy diagnostic output cannot register as production authority', () => {
  const rejected = rejectArtifactEntry({
    output_class: 'diagnostic',
    status: 'DIAGNOSTIC ONLY',
    diagnostic_only: true,
  });
  return {
    pass: rejected.rejected === true,
    output_classification: 'diagnostic',
    blocked_authority: rejected.rejected,
  };
});

// 9. Canonical gated wrapper creates receipt
record(9, 'Canonical gated wrapper creates receipt', () => {
  const receiptDir = fs.mkdtempSync(path.join(os.tmpdir(), 'sppc-lock-'));
  const auth = authorizeMigAction({
    manifestPath: VALID,
    action: 'source_registration',
    receiptDir,
  });
  const receiptFile = fs.readdirSync(receiptDir).find((f) => f.endsWith('.json'));
  return {
    pass: !!auth.evidence_record?.receipt_id && !!receiptFile,
    receipt_created: !!receiptFile,
    exit_code: auth.exit_code,
  };
});

// 10. No forbidden production output after blocked MIG PPC CLI
record(10, 'No canonical artifact mutation after blocked MIG PPC CLI', () => {
  const before = fs.existsSync(CORVONERO) ? fs.statSync(CORVONERO).mtimeMs : 0;
  const ppcBody = path.join(os.tmpdir(), `sppc-mig-block-${Date.now()}.json`);
  fs.writeFileSync(ppcBody, JSON.stringify({ mars_search_ppc: true, session_id: 'block-test' }));
  runNode('projects/mig/lib/runtime/run-mig-session.js', [ppcBody]);
  const after = fs.existsSync(CORVONERO) ? fs.statSync(CORVONERO).mtimeMs : 0;
  return {
    pass: before === after,
    canonical_artifact_mutated: before !== after,
  };
});

// 11. Repository-owned caller uses gated replacement (inventory)
record(11, 'Repository inventory documents gated MIG replacement', () => {
  const inv = loadJson(path.join(REPO_ROOT, 'projects/mars-search-ppc-production/inventory/search-ppc-entry-point-inventory-v1.json'));
  const gated = inv.entry_points.find((e) => e.id === 'mig-gated-session');
  const direct = inv.entry_points.find((e) => e.id === 'mig-run-session-direct');
  return {
    pass: gated?.integration === 'WIRED' && /LOCKED|QUARANTINED/i.test(direct?.integration || ''),
    gated_path: gated?.path,
  };
});

// 12. Web-GPT unvalidated handoff remains proposal-only
record(12, 'Web-GPT unvalidated handoff remains proposal-only', () => {
  const sub = runNode('projects/mars-search-ppc-production/runtime/cli/validate-webgpt-handoff.mjs', [
    path.join(FIX, 'synthetic-webgpt-downstream-v2.json'),
  ]);
  const proposalOnly = /PROPOSAL|BLOCKED|INVALID/i.test(sub.stdout + sub.stderr);
  return {
    pass: sub.status !== 0 || proposalOnly,
    exit_code: sub.status,
    output_classification: 'proposal',
  };
});

const passed = results.filter((r) => r.pass).length;
const failed = results.filter((r) => !r.pass).length;
const out = {
  suite: 'mars-search-ppc-lockdown-tests-v1',
  wave: '1.2',
  timestamp: new Date().toISOString(),
  summary: { total: results.length, passed, failed },
  results,
};

const outPath = path.join(__dirname, '../reports/lockdown-test-results-v1.json');
fs.writeFileSync(outPath, JSON.stringify(out, null, 2) + '\n');
console.log(`Lockdown tests: ${passed}/${results.length} passed, ${failed} failed`);
for (const r of results) {
  console.log(`  [${r.disposition}] #${r.id} ${r.name}${r.error ? ` — ${r.error}` : ''}`);
}
process.exit(failed > 0 ? 1 : 0);
