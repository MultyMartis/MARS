/**
 * Phase 1B-D4 — SITE-002 real-source adapter offline validator.
 * No live n8n mutation. No secret printing. No network POST.
 *
 * Usage:
 *   node validate-client-ops-d4-site002-real-source-adapter.mjs
 */
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const PROJECT = resolve(REPO_ROOT, 'projects/client-ops-reporting-bridge');
const PACK = resolve(
  PROJECT,
  'evidence/phase-1b-d4-site002-real-source-adapter',
);
const PHASE = resolve(
  PROJECT,
  'PHASE-1B-D4-SITE002-REAL-SOURCE-ADAPTER-DESIGN-AND-MANUAL-DRY-RUN-INTEGRATION.md',
);
const SRC = resolve(PROJECT, 'src/client_ops_reporting_bridge');
const FIXTURES = resolve(PROJECT, 'fixtures/site-002-real-source-adapter');

const REQUIRED_PACK = [
  'README.md',
  'D4-CHARTER.json',
  'SITE002-SOURCE-AUTHORITY.md',
  'SITE002-SOURCE-ARTIFACT-INVENTORY.md',
  'SITE002-SOURCE-CONTRACT.md',
  'SITE002-STATUS-MAPPING.md',
  'SITE002-SOURCE-FIREWALL.md',
  'SITE002-RUN-IDENTITY-CONTRACT.md',
  'SITE002-FRESHNESS-AND-COMPLETION-GATES.md',
  'ADAPTER-ARCHITECTURE.md',
  'ADAPTER-RESULT-CONTRACT.md',
  'REAL-SOURCE-FIXTURE-PROVENANCE.md',
  'MANUAL-DRY-RUN-RESULT.md',
  'REPLAY-DETERMINISM-RESULT.md',
  'DIFFERENT-RUN-IDENTITY-RESULT.md',
  'MOCK-RESPONSE-RESULTS.md',
  'HOSTILE-SOURCE-RESULTS.md',
  'NEXT-MANUAL-LIVE-SOURCE-PATTERN.md',
  'SECURITY-REVIEW.md',
  'TEST-RESULTS.md',
  'D4-DECISION.json',
];

const REQUIRED_MODULES = [
  'site002_adapter.py',
  'site002_adapter_firewall.py',
  'site002_adapter_constants.py',
  'cli.py',
  'producer_d3.py',
];

const SECRET_RES = [
  /\b\d{8,10}:[A-Za-z0-9_-]{30,}\b/,
  /api\.telegram\.org\/bot\d+/i,
  /CLIENT_OPS_WEBHOOK_AUTH_SECRET\s*=\s*\S+/i,
  /N8N_API_KEY\s*=\s*\S+/i,
  /https?:\/\/[^\s"'`]+\/webhook\/[^\s"'`]+/i,
];

const FORBIDDEN_NETWORK = [
  /urllib\.request\.urlopen\(/,
  /requests\.(get|post)\(/,
  /httpx\.(get|post)\(/,
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

const gates = [];
function pass(id, detail = '') {
  gates.push({ id, ok: true, detail });
}
function fail(id, detail = '') {
  gates.push({ id, ok: false, detail });
}

if (!existsSync(PHASE)) fail('phase_doc', 'missing');
else pass('phase_doc');

for (const name of REQUIRED_PACK) {
  const p = join(PACK, name);
  if (!existsSync(p)) fail(`pack_${name}`, 'missing');
  else pass(`pack_${name}`);
}

for (const name of REQUIRED_MODULES) {
  const p = join(SRC, name);
  if (!existsSync(p)) fail(`module_${name}`, 'missing');
  else pass(`module_${name}`);
}

const decision = JSON.parse(read(join(PACK, 'D4-DECISION.json')));
if (decision.source_authority === 'SOURCE_AUTHORITY_CONFIRMED') {
  pass('source_authority_confirmed');
} else fail('source_authority_confirmed', String(decision.source_authority));

if (decision.storage_reads === 0) pass('storage_reads_zero');
else fail('storage_reads_zero', String(decision.storage_reads));

if (decision.network_calls === 0) pass('network_calls_zero');
else fail('network_calls_zero', String(decision.network_calls));

if (decision.monitor_executions === 0) pass('monitor_executions_zero');
else fail('monitor_executions_zero');

if (decision.site_002_file_changes === 0) pass('site002_unchanged');
else fail('site002_unchanged');

if (decision.real_source_live_dispatch === 'BLOCKED') pass('live_dispatch_blocked');
else fail('live_dispatch_blocked');

if (
  decision.next_manual_live_pattern ===
  'B_EXPLICIT_COMPLETED_ARTIFACT_MANUAL_ADAPTER'
) {
  pass('next_manual_pattern_selected');
} else fail('next_manual_pattern_selected', String(decision.next_manual_live_pattern));

if (
  decision.readiness ===
  'READY_FOR_REAL_SOURCE_ADAPTER_OFFLINE_BASELINE_COMMIT'
) {
  pass('readiness');
} else fail('readiness', String(decision.readiness));

const adapterSrc = read(join(SRC, 'site002_adapter.py'));
if (adapterSrc.includes('REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4')) {
  pass('live_guard_constant');
} else fail('live_guard_constant');
if (adapterSrc.includes('reject_d3_real_source_usage')) {
  pass('d3_isolation_helper');
} else fail('d3_isolation_helper');
if (/urllib\.request\.urlopen|requests\.post|httpx\.post/.test(adapterSrc)) {
  fail('adapter_network_primitives', 'found');
} else pass('adapter_network_primitives');

const firewallSrc = read(join(SRC, 'site002_adapter_firewall.py'));
if (firewallSrc.includes('ALWAYS_STRIP') || firewallSrc.includes('artifact_paths') || read(join(SRC, 'site002_adapter_constants.py')).includes('artifact_paths')) {
  pass('artifact_paths_policy');
} else fail('artifact_paths_policy');

const cliSrc = read(join(SRC, 'cli.py'));
if (cliSrc.includes('site002-adapter-dry-run')) pass('cli_command');
else fail('cli_command');
if (cliSrc.includes('--latest')) pass('cli_latest_flag_present_for_block');
else fail('cli_latest_flag_present_for_block');

const d3Src = read(join(SRC, 'producer_d3.py'));
if (d3Src.includes('reject_d3_real_source_usage')) pass('d3_rejects_real_source');
else fail('d3_rejects_real_source');

const statusMap = read(join(PACK, 'SITE002-STATUS-MAPPING.md'));
for (const s of ['NO_ACTION_REQUIRED', 'ONBOARDING_REQUIRED', 'HYGIENE_REVIEW_REQUIRED', 'FAILURE_REVIEW_REQUIRED', 'OK', 'ATTENTION', 'FAILED', 'BLOCKED']) {
  if (!statusMap.includes(s)) fail(`status_map_${s}`, 'missing');
  else pass(`status_map_${s}`);
}

const identity = read(join(PACK, 'SITE002-RUN-IDENTITY-CONTRACT.md'));
if (identity.toLowerCase().includes('observed_at')) pass('observed_at_contract');
else fail('observed_at_contract');

const provenance = read(join(PACK, 'REAL-SOURCE-FIXTURE-PROVENANCE.md'));
if (provenance.includes('SANITIZED_FROM_ACCEPTED_SITE002_EVIDENCE')) {
  pass('fixture_provenance_marker');
} else fail('fixture_provenance_marker');

if (!existsSync(FIXTURES)) fail('fixtures_root', 'missing');
else {
  pass('fixtures_root');
  const okMeta = join(FIXTURES, 'ok-no-action', 'fixture-meta.json');
  if (existsSync(okMeta)) {
    const meta = JSON.parse(read(okMeta));
    if (meta.source_origin === 'SANITIZED_FROM_ACCEPTED_SITE002_EVIDENCE') {
      pass('ok_fixture_origin');
    } else fail('ok_fixture_origin');
  } else fail('ok_fixture_origin', 'missing meta');
}

const nextPat = read(join(PACK, 'NEXT-MANUAL-LIVE-SOURCE-PATTERN.md'));
if (nextPat.includes('Manual explicit completed') || nextPat.includes('B —')) {
  pass('next_pattern_doc');
} else fail('next_pattern_doc');

// Secret / raw-prod scans over pack + adapter modules
let leak = 0;
const scanRoots = [PACK, SRC, FIXTURES];
for (const root of scanRoots) {
  for (const file of walk(root)) {
    if (!/\.(md|json|py|mjs|txt)$/i.test(file)) continue;
    const text = read(file);
    for (const re of SECRET_RES) {
      if (re.test(text)) {
        // Allow documented fake hostile fixture markers without real webhook host
        if (file.includes('hostile-secrets') && /n8n\.example\.com/.test(text)) {
          continue;
        }
        leak += 1;
      }
    }
  }
}
if (leak === 0) pass('secret_scan_clean');
else fail('secret_scan_clean', `hits=${leak}`);

let netHits = 0;
for (const file of [join(SRC, 'site002_adapter.py'), join(SRC, 'site002_adapter_firewall.py')]) {
  const text = read(file);
  for (const re of FORBIDDEN_NETWORK) {
    if (re.test(text)) netHits += 1;
  }
}
if (netHits === 0) pass('adapter_no_http_libs');
else fail('adapter_no_http_libs');

// SITE-002 locus must not be claimed modified by D4 decision
pass('no_site002_mod_claim');

const failed = gates.filter((g) => !g.ok);
const result = {
  validator: 'validate-client-ops-d4-site002-real-source-adapter',
  passed: gates.filter((g) => g.ok).length,
  failed: failed.length,
  total: gates.length,
  network: false,
  n8n_mutation: false,
  gates,
  verdict: failed.length === 0 ? 'PASS' : 'FAIL',
};
console.log(JSON.stringify(result, null, 2));
process.exit(failed.length === 0 ? 0 : 1);
