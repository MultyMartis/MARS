/**
 * Phase 1B-D5 — First manual SITE-002 real-source connection validator.
 * No live n8n mutation. No secret printing. No network POST.
 *
 * Usage:
 *   node validate-client-ops-d5-first-manual-real-source-connection.mjs
 */
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const PROJECT = resolve(REPO_ROOT, 'projects/client-ops-reporting-bridge');
const PACK = resolve(
  PROJECT,
  'evidence/phase-1b-d5-first-manual-site002-real-source-connection',
);
const PHASE = resolve(
  PROJECT,
  'PHASE-1B-D5-FIRST-MANUAL-SITE002-REAL-SOURCE-CONNECTION-AND-CONTROLLED-LIVE-POST.md',
);
const SRC = resolve(PROJECT, 'src/client_ops_reporting_bridge');

const REQUIRED_PACK = [
  'README.md',
  'D5-CHARTER.json',
  'SOURCE-SELECTION-CONTRACT.md',
  'SELECTED-SOURCE-MANIFEST.json',
  'SOURCE-FRESHNESS-ASSESSMENT.md',
  'SOURCE-PREVIEW.json',
  'SOURCE-PREVIEW-DECISION.json',
  'D5-LIVE-GATES.md',
  'D5-ENDPOINT-AND-AUTH-BOUNDARY.md',
  'PRE-LIVE-CLIENT-OPS-STATE.json',
  'REAL-SOURCE-PRODUCER-RESULT.json',
  'REAL-SOURCE-N8N-RESULT.json',
  'REAL-SOURCE-DATATABLE-RESULT.json',
  'REAL-SOURCE-TELEGRAM-RESULT.json',
  'CONTAINMENT-STATUS.md',
  'ONE-TIME-CHARTER-STATUS.md',
  'SECURITY-REVIEW.md',
  'TEST-RESULTS.md',
  'D5-DECISION.json',
];

const REQUIRED_MODULES = [
  'producer_d5.py',
  'producer_d5_gates.py',
  'site002_adapter.py',
  'producer_http.py',
  'producer_d3.py',
  'cli.py',
];

const SECRET_RES = [
  /\b\d{8,10}:[A-Za-z0-9_-]{30,}\b/,
  /api\.telegram\.org\/bot\d+/i,
  /CLIENT_OPS_WEBHOOK_AUTH_SECRET\s*=\s*\S+/i,
  /N8N_API_KEY\s*=\s*\S+/i,
  /https?:\/\/[^\s"'`]+\/webhook\/[^\s"'`]+/i,
];

const FORBIDDEN = [
  /--latest\b/,
  /folder.?watch/i,
  /unattended/i,
];

function walk(p, out = []) {
  if (!existsSync(p)) return out;
  const st = statSync(p);
  if (st.isFile()) {
    out.push(p);
    return out;
  }
  for (const name of readdirSync(p)) {
    if (name === '__pycache__' || name === 'node_modules') continue;
    walk(join(p, name), out);
  }
  return out;
}

function read(p) {
  return readFileSync(p, 'utf8');
}

function main() {
  const failures = [];
  const notes = [];

  if (!existsSync(PHASE)) failures.push('missing D5 phase document');
  for (const name of REQUIRED_PACK) {
    if (!existsSync(join(PACK, name))) failures.push(`missing evidence ${name}`);
  }
  for (const name of REQUIRED_MODULES) {
    if (!existsSync(join(SRC, name))) failures.push(`missing module ${name}`);
  }

  const phaseText = existsSync(PHASE) ? read(PHASE) : '';
  if (phaseText && !/Pattern B/i.test(phaseText)) {
    failures.push('phase doc missing Pattern B');
  }
  if (phaseText && !/site002-controlled-live/.test(phaseText)) {
    failures.push('phase doc missing site002-controlled-live command');
  }

  const d5 = existsSync(join(SRC, 'producer_d5.py'))
    ? read(join(SRC, 'producer_d5.py'))
    : '';
  const gates = existsSync(join(SRC, 'producer_d5_gates.py'))
    ? read(join(SRC, 'producer_d5_gates.py'))
    : '';
  const cli = existsSync(join(SRC, 'cli.py')) ? read(join(SRC, 'cli.py')) : '';
  const http = existsSync(join(SRC, 'producer_http.py'))
    ? read(join(SRC, 'producer_http.py'))
    : '';
  const adapter = existsSync(join(SRC, 'site002_adapter.py'))
    ? read(join(SRC, 'site002_adapter.py'))
    : '';

  if (!/create_d5_live_transport/.test(http)) {
    failures.push('producer_http missing create_d5_live_transport');
  }
  if (!/create_d3_live_transport/.test(http)) {
    failures.push('D3 transport reuse missing');
  }
  if (!/adapt_source_dir/.test(d5)) {
    failures.push('D5 must reuse D4 adapt_source_dir');
  }
  if (!/REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4/.test(adapter)) {
    failures.push('D4 live block missing');
  }
  if (!/ENABLE ONE MANUAL SITE002 REAL SOURCE D5 BZPM/.test(gates) &&
      !/ENABLE ONE MANUAL SITE002 REAL SOURCE D5 BZPM/.test(
        read(join(SRC, 'producer_constants.py')),
      )) {
    failures.push('D5 enable phrase missing');
  }
  if (!/D5_ENABLE_PHRASE/.test(gates)) {
    failures.push('D5 enable phrase constant wiring missing in gates');
  }
  if (!/D5_MAX_REAL_REQUESTS/.test(read(join(SRC, 'producer_constants.py')))) {
    failures.push('D5 max request constant missing');
  }
  if (!/site002-controlled-live/.test(cli)) {
    failures.push('CLI missing site002-controlled-live');
  }
  if (/--latest/.test(cli) && !/forbidden/.test(cli)) {
    notes.push('CLI mentions --latest; ensure rejected');
  }

  const decisionPath = join(PACK, 'D5-DECISION.json');
  if (existsSync(decisionPath)) {
    const decision = JSON.parse(read(decisionPath));
    if (decision.pattern !== 'B') failures.push('D5-DECISION pattern must be B');
    if (decision.monitor_executed === true) {
      failures.push('monitor_executed must not be true');
    }
    if (decision.scheduler_connected === true) {
      failures.push('scheduler must remain disconnected');
    }
  }

  const packFiles = walk(PACK).filter((p) => /\.(md|json)$/i.test(p));
  for (const file of packFiles) {
    const text = read(file);
    for (const re of SECRET_RES) {
      if (re.test(text)) failures.push(`secret-like pattern in ${file}`);
    }
    if (/X:\\AI MARS STORAGE\\ocpilot\\project-sites\\site-002\\production\\scheduled-monitors\\post-1c\\20/.test(text)) {
      failures.push(`absolute selected source path leaked in ${file}`);
    }
  }

  // Activation phrases present
  const act = read(
    join(PROJECT, 'n8n/runners/lib/client-ops-n8n-activation-client.mjs'),
  );
  if (!/ACTIVATE CLIENT OPS MANUAL REAL SOURCE D5 BZPM/.test(act)) {
    failures.push('activation client missing D5 activate phrase');
  }
  if (!/DEACTIVATE CLIENT OPS MANUAL REAL SOURCE D5 BZPM/.test(act)) {
    failures.push('activation client missing D5 deactivate phrase');
  }

  const ok = failures.length === 0;
  console.log(
    JSON.stringify(
      {
        ok,
        phase: '1B-D5',
        failures,
        notes,
        pattern: 'B',
        checks: {
          evidence_files: REQUIRED_PACK.length,
          modules: REQUIRED_MODULES.length,
          pack_files_scanned: packFiles.length,
        },
      },
      null,
      2,
    ),
  );
  process.exit(ok ? 0 : 1);
}

main();
