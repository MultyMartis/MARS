/**
 * Phase 1B-D3 — static validator for controlled producer connection.
 * Offline. No live network. No secret printing.
 *
 * Usage:
 *   node validate-client-ops-d3-controlled-producer-connection.mjs
 */

import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const PROJECT = resolve(REPO_ROOT, 'projects/client-ops-reporting-bridge');
const PACK = resolve(PROJECT, 'evidence/phase-1b-d3-controlled-producer-connection');
const SRC = resolve(PROJECT, 'src/client_ops_reporting_bridge');
const RUNNER = resolve(__dirname, 'run-client-ops-d3-controlled-producer-connection.mjs');
const ACTIVATION = resolve(__dirname, 'lib/client-ops-n8n-activation-client.mjs');

const REQUIRED_PACK = [
  'README.md',
  'D3-CHARTER.json',
  'LIVE-TRANSPORT-DESIGN.md',
  'LIVE-ENDPOINT-ALLOWLIST.md',
  'LIVE-CONFIRMATION-GATES.md',
  'SYNTHETIC-EVENT-CONTRACT.md',
  'SECURITY-REVIEW.md',
  'TEST-RESULTS.md',
  'D3-DECISION.json',
];

const POST_LIVE_PACK = [
  'PRE-LIVE-MANIFEST.json',
  'FIRST-SEEN-PRODUCER-RESULT.json',
  'FIRST-SEEN-N8N-RESULT.json',
  'FIRST-SEEN-DATATABLE-RESULT.json',
  'FIRST-SEEN-TELEGRAM-RESULT.json',
  'CONTAINMENT-STATUS.md',
];

const OPTIONAL_REPLAY_PACK = [
  'EXACT-REPLAY-PRODUCER-RESULT.json',
  'EXACT-REPLAY-N8N-RESULT.json',
  'EXACT-REPLAY-DATATABLE-RESULT.json',
];

const SECRET_RES = [
  /\b\d{8,10}:[A-Za-z0-9_-]{30,}\b/,
  /api\.telegram\.org\/bot\d+/i,
  /CLIENT_OPS_WEBHOOK_AUTH_SECRET\s*=\s*\S+/i,
  /N8N_API_KEY\s*=\s*\S+/i,
  /https?:\/\/[^\s"'`]+\/webhook\/[^\s"'`]+/i,
];

const SITE002_RUNTIME_CONN = [
  /ftp:\/\//i,
  /sftp:\/\//i,
  /mysql:\/\//i,
  /postgres(ql)?:\/\//i,
  /mongodb(\+srv)?:\/\//i,
  /connection[_-]?string\s*=/i,
  /jdbc:/i,
  /ssh:\/\//i,
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

function main() {
  const gates = [];
  const pass = (id, detail = '') => gates.push({ id, ok: true, detail });
  const fail = (id, detail = '') => gates.push({ id, ok: false, detail });

  if (existsSync(RUNNER)) pass('runner_exists');
  else fail('runner_exists', 'missing orchestrator');

  for (const name of REQUIRED_PACK) {
    if (existsSync(resolve(PACK, name))) pass(`pack_${name}`);
    else fail(`pack_${name}`, 'missing');
  }

  const decisionPath = resolve(PACK, 'D3-DECISION.json');
  if (existsSync(decisionPath)) {
    try {
      const decision = JSON.parse(readFileSync(decisionPath, 'utf8'));
      if (decision.live_executed === true) {
        for (const name of POST_LIVE_PACK) {
          if (existsSync(resolve(PACK, name))) pass(`postlive_${name}`);
          else fail(`postlive_${name}`, 'missing after live');
        }
        if (decision.replay_executed === true) {
          for (const name of OPTIONAL_REPLAY_PACK) {
            if (existsSync(resolve(PACK, name))) pass(`replay_${name}`);
            else fail(`replay_${name}`, 'missing after replay');
          }
        } else {
          pass('replay_pack_optional_skipped');
        }
      } else {
        pass('postlive_deferred_until_live');
      }
    } catch {
      fail('d3_decision_parse', 'invalid JSON');
    }
  }

  const httpPath = resolve(SRC, 'producer_http.py');
  if (existsSync(httpPath)) {
    const http = readFileSync(httpPath, 'utf8');
    if (/class LiveHttpTransport/.test(http)) pass('live_http_transport');
    else fail('live_http_transport');
    if (/ssl\.create_default_context/.test(http)) pass('ssl_default_context');
    else fail('ssl_default_context');
    if (!/verify\s*=\s*False/.test(http) && !/CERT_NONE/.test(http)) {
      pass('no_tls_verify_disable');
    } else fail('no_tls_verify_disable');
  } else {
    fail('producer_http_py', 'missing');
  }

  const gatesPath = resolve(SRC, 'producer_d3_gates.py');
  if (existsSync(gatesPath)) {
    const g = readFileSync(gatesPath, 'utf8');
    if (/ENABLE CLIENT OPS CONTROLLED PRODUCER HTTP D3 BZPM/.test(g) || /D3_ENABLE_PHRASE/.test(g)) {
      pass('gates_enable_phrase');
    } else fail('gates_enable_phrase');
    if (/D3_SEND_FIRST_PHRASE|SEND ONE CLIENT OPS PRODUCER FIRST SEEN/.test(g)) {
      pass('gates_send_first');
    } else fail('gates_send_first');
    if (/D3_SEND_REPLAY_PHRASE|SEND ONE CLIENT OPS PRODUCER EXACT REPLAY/.test(g)) {
      pass('gates_send_replay');
    } else fail('gates_send_replay');
    if (/dry_run cannot reach live HTTP/.test(g)) pass('dry_run_blocked');
    else fail('dry_run_blocked');
    if (/concurrency must be 1/.test(g)) pass('concurrency_1');
    else fail('concurrency_1');
    if (/max_retries must be 0/.test(g)) pass('max_retries_0');
    else fail('max_retries_0');
  } else {
    fail('producer_d3_gates_py', 'missing');
  }

  if (existsSync(resolve(SRC, 'producer_d3.py'))) pass('producer_d3_py');
  else fail('producer_d3_py', 'missing');

  const constants = existsSync(resolve(SRC, 'producer_constants.py'))
    ? readFileSync(resolve(SRC, 'producer_constants.py'), 'utf8')
    : '';
  if (/D3_MAX_REAL_REQUESTS\s*[:=].*2/.test(constants) || /D3_MAX_REAL_REQUESTS:.*=\s*2/.test(constants)) {
    pass('d3_max_real_requests_2');
  } else fail('d3_max_real_requests_2');

  const cli = existsSync(resolve(SRC, 'cli.py'))
    ? readFileSync(resolve(SRC, 'cli.py'), 'utf8')
    : '';
  if (/producer-d3-controlled-live/.test(cli)) pass('cli_d3_command');
  else fail('cli_d3_command');
  if (/push-webhook/.test(cli) && /NETWORK_DISPATCH_NOT_AUTHORIZED_D2/.test(cli)) {
    pass('push_webhook_still_blocked');
  } else fail('push_webhook_still_blocked');
  if (!/Schedule|scheduler\.|crontab/.test(cli)) pass('no_scheduler_in_cli');
  else fail('no_scheduler_in_cli');

  const d3py = existsSync(resolve(SRC, 'producer_d3.py'))
    ? readFileSync(resolve(SRC, 'producer_d3.py'), 'utf8')
    : '';
  let connLeak = false;
  for (const re of SITE002_RUNTIME_CONN) {
    if (re.test(d3py)) {
      connLeak = true;
      fail('no_site002_runtime_conn', re.toString());
    }
  }
  if (!connLeak) pass('no_site002_runtime_conn');

  if (existsSync(ACTIVATION)) {
    const act = readFileSync(ACTIVATION, 'utf8');
    if (/ACTIVATE CLIENT OPS CONTROLLED PRODUCER TEST D3 BZPM/.test(act)) {
      pass('activation_d3_activate_phrase');
    } else fail('activation_d3_activate_phrase');
    if (/DEACTIVATE CLIENT OPS CONTROLLED PRODUCER TEST D3 BZPM/.test(act)) {
      pass('activation_d3_deactivate_phrase');
    } else fail('activation_d3_deactivate_phrase');
    if (/EMERGENCY DEACTIVATE CLIENT OPS PRODUCER D3 BZPM/.test(act)) {
      pass('activation_d3_emergency_phrase');
    } else fail('activation_d3_emergency_phrase');
    if (/D3_ACTIVATION_CONFIRM_PHRASE/.test(act)) pass('activation_exports_d3');
    else fail('activation_exports_d3');
  } else {
    fail('activation_client', 'missing');
  }

  if (existsSync(RUNNER)) {
    const runner = readFileSync(RUNNER, 'utf8');
    if (/--apply/.test(runner) && /dry-run|runDry/.test(runner)) pass('runner_default_dry');
    else fail('runner_default_dry');
    if (!/updateAllowlistedWorkflow|prepareWorkflowPutPayload/.test(runner)) {
      pass('runner_no_workflow_put');
    } else fail('runner_no_workflow_put');
    if (!/api\.telegram\.org/.test(runner)) pass('runner_no_telegram_api');
    else fail('runner_no_telegram_api');
    if (!/insertDataTableRows|createAllowlistedDataTable|deleteAllowlistedDataTable/.test(runner)) {
      pass('runner_no_datatable_admin_mutate');
    } else fail('runner_no_datatable_admin_mutate');
    if (/concurrency['"\s:=]+1/.test(runner) || /'1'/.test(runner)) pass('runner_concurrency_1');
    else fail('runner_concurrency_1');
    if (/max-retries/.test(runner) && /0/.test(runner)) pass('runner_max_retries_0');
    else fail('runner_max_retries_0');
    if (/finally/.test(runner) && /deactivateAllowlistedWorkflow/.test(runner)) {
      pass('runner_deactivate_finally');
    } else fail('runner_deactivate_finally');
    if (/spawnSync/.test(runner) && !/fetch\([^)]*method:\s*['"]POST['"].*webhook/i.test(runner)) {
      pass('runner_python_producer_not_fetch_post');
    } else fail('runner_python_producer_not_fetch_post');
  }

  let leak = false;
  if (existsSync(PACK)) {
    for (const file of walk(PACK)) {
      if (!/\.(md|json|txt)$/i.test(file)) continue;
      const text = readFileSync(file, 'utf8');
      for (const re of SECRET_RES) {
        if (re.test(text)) {
          if (/example\.invalid/.test(text)) continue;
          if (/https?:\/\/n8n\.example\.invalid\/webhook\//i.test(text)) continue;
          if (/\[REDACTED/.test(text) && /webhook/.test(text)) continue;
          leak = true;
          fail('secret_scan', file.replace(REPO_ROOT, '').replace(/\\/g, '/'));
        }
      }
    }
  }
  if (!leak) pass('secret_scan_clean');

  const passed = gates.filter((g) => g.ok).length;
  const failed = gates.filter((g) => !g.ok).length;
  const summary = {
    phase: '1B-D3',
    validator: 'validate-client-ops-d3-controlled-producer-connection',
    passed,
    failed,
    ok: failed === 0,
    gates,
  };
  console.log(JSON.stringify(summary, null, 2));
  process.exitCode = failed === 0 ? 0 : 1;
}

main();
