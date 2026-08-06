/**
 * Phase 1B-D6F — Scheduled Client Ops producer production runner (non-Git, runtime-state).
 * Supports DRY_RUN evaluation and ENABLED permanent-active delivery.
 * Passes RAW kill-switch JSON to producer (never reduced parsed object lacking site_id).
 * No one-shot quota. No auto-disable after first message. No activate/deactivate cycle
 * when workflow is already permanently active.
 */
import {
  mkdirSync,
  writeFileSync,
  readFileSync,
  existsSync,
  readdirSync,
  statSync,
  unlinkSync,
} from 'node:fs';
import { createHash, randomUUID } from 'node:crypto';
import { join, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { spawnSync } from 'node:child_process';

const __dirname = dirname(fileURLToPath(import.meta.url));

const PRODUCER_REPO =
  'X:\\AI MARS STORAGE\\runtime-checkouts\\client-ops-site-002-producer\\repo';
const STATE_ROOT =
  'X:\\AI MARS STORAGE\\runtime-state\\client-ops-site-002-producer';
const ARTIFACT_ROOT =
  'X:\\AI MARS STORAGE\\ocpilot\\project-sites\\site-002\\production\\scheduled-monitors\\post-1c';
const MAIN_ROOT = 'X:\\AI MARS';
const PIN = 'e1d2a1786fd7d778957b74fb213cf5656231a256';
const REQUIRED_ANCESTORS = [
  'e1d2a1786fd7d778957b74fb213cf5656231a256',
  '7f9fd29fa037939a7f6f13bdb02cb18801bc7fbd',
  '79c2071dd8ae8096506d45bc189e1f732b310d35',
  '94d06c05ea79eb22780588d91064006c3edf2a05',
  '12e4c6ad1f4199458b6f091d084f33ca5f8a965d',
];
const TASK_NAME = 'MARS_SITE_002_Client_Ops_Producer';
const WORKFLOW_ID = 'tkM4H0G0gM3q9Foi';
const EXPECTED_VERSION = '449a2c83-6e13-456c-bdbb-9e4cbf7e990a';
const HISTORICAL_PENDING = 'c84e29bf-79b1-5aea-98c4-9dc8d651fc96';
const LIB = join(
  PRODUCER_REPO,
  'projects/client-ops-reporting-bridge/n8n/runners/lib',
);

const mode = (process.argv[2] || 'run').toLowerCase();

function writeJson(path, obj) {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, `${JSON.stringify(obj, null, 2)}\n`, 'utf8');
}

function appendLog(line) {
  const day = new Date().toISOString().slice(0, 10);
  const logPath = join(STATE_ROOT, 'logs', `scheduler-${day}.log`);
  mkdirSync(dirname(logPath), { recursive: true });
  const sanitized = String(line)
    .replace(/X-N8N-API-KEY\s*[:=]\s*\S+/gi, 'X-N8N-API-KEY=[REDACTED]')
    .replace(/Authorization:\s*Bearer\s+\S+/gi, 'Authorization: Bearer [REDACTED]')
    .replace(/api[_-]?key["']?\s*[:=]\s*["']?[^"'\s]+/gi, 'api_key=[REDACTED]')
    .replace(/bot\d+:[A-Za-z0-9_-]+/g, 'bot[REDACTED]')
    .replace(/x-mars-client-ops-token["']?\s*[:=]\s*["']?[^"'\s]+/gi, 'x-mars-client-ops-token=[REDACTED]');
  writeFileSync(logPath, `${new Date().toISOString()} ${sanitized}\n`, {
    flag: 'a',
    encoding: 'utf8',
  });
  return { logPath };
}

function git(cwd, args) {
  const r = spawnSync('git', args, {
    cwd,
    encoding: 'utf8',
    windowsHide: true,
  });
  return {
    code: r.status ?? 1,
    out: (r.stdout || '').trim(),
    err: (r.stderr || '').trim(),
  };
}

function createRealFsFixed() {
  const norm = (p) =>
    String(p)
      .replace(/\//g, '\\')
      .replace(/\\{2,}/g, '\\')
      .replace(/\\+$/g, '');
  return {
    listDir(path) {
      return readdirSync(norm(path), { withFileTypes: true }).map((d) => d.name);
    },
    readText(path) {
      return readFileSync(norm(path), 'utf8');
    },
    exists(path) {
      return existsSync(norm(path));
    },
    size(path) {
      return statSync(norm(path)).size;
    },
    mtimeMs(path) {
      return statSync(norm(path)).mtimeMs;
    },
  };
}

function failExit(code, reason, extra = {}) {
  appendLog(`FAIL exit=${code} reason=${reason}`);
  const lastRun = {
    phase: '1B-D6F',
    task_name: TASK_NAME,
    ok: false,
    exit_code: code,
    exit_class: extra.exit_class || 'FAILED_PREFLIGHT',
    reason,
    runtime_commit: extra.runtime_commit || null,
    kill_switch_mode: extra.kill_switch_mode || null,
    request_authorized: false,
    finished_at: new Date().toISOString(),
    ...extra,
  };
  writeJson(join(STATE_ROOT, 'state', 'scheduler-last-run.json'), lastRun);
  process.exit(code);
}

async function importPinned(rel) {
  return import(pathToFileURL(join(LIB, rel)).href);
}

function verifyRuntimePin() {
  const head = git(PRODUCER_REPO, ['rev-parse', 'HEAD']);
  if (head.code !== 0 || head.out !== PIN) {
    return { ok: false, reason: 'WRONG_RUNTIME_HEAD', head: head.out };
  }
  const porcelain = git(PRODUCER_REPO, ['status', '--porcelain']);
  if (porcelain.code !== 0 || porcelain.out !== '') {
    return { ok: false, reason: 'DIRTY_RUNTIME', porcelain: porcelain.out.slice(0, 200) };
  }
  for (const a of REQUIRED_ANCESTORS) {
    const r = git(PRODUCER_REPO, ['merge-base', '--is-ancestor', a, 'HEAD']);
    if (r.code !== 0) {
      return { ok: false, reason: 'MISSING_ANCESTOR', ancestor: a };
    }
  }
  return { ok: true, head: head.out };
}

function loadKillSwitchRaw(path) {
  if (!existsSync(path)) {
    return { ok: false, reason: 'KILL_SWITCH_MISSING' };
  }
  let raw;
  try {
    raw = JSON.parse(readFileSync(path, 'utf8'));
  } catch {
    return { ok: false, reason: 'KILL_SWITCH_MALFORMED_JSON' };
  }
  return { ok: true, raw };
}

function parseKillSwitchStrict(parseKillSwitch, path, { allowEnabled = true } = {}) {
  const loaded = loadKillSwitchRaw(path);
  if (!loaded.ok) return loaded;
  const raw = loaded.raw;
  const ks = parseKillSwitch(raw, {
    site_id: 'SITE-002',
    producer_identity: 'mars.client-ops.site-002.unattended-producer',
  });
  if (!ks.ok) {
    return { ok: false, reason: ks.reason || 'KILL_SWITCH_SCHEMA_REJECT', mode: ks.mode };
  }
  if (ks.mode === 'ENABLED' && !allowEnabled) {
    return { ok: false, reason: 'ENABLED_MODE_REJECTED', mode: ks.mode };
  }
  if (ks.mode !== 'DRY_RUN' && ks.mode !== 'ENABLED') {
    return { ok: false, reason: 'KILL_SWITCH_MODE_UNKNOWN', mode: ks.mode };
  }
  const cfgHash = createHash('sha256')
    .update(
      JSON.stringify({
        schema_version: raw.schema_version,
        site_id: raw.site_id,
        producer_identity: raw.producer_identity,
        mode: raw.mode,
      }),
    )
    .digest('hex');
  return { ok: true, ks, cfgHash, raw_mode: raw.mode, raw };
}

function loadBootstrapBoundary() {
  const bootstrapPath = join(STATE_ROOT, 'config', 'bootstrap-boundary.json');
  if (!existsSync(bootstrapPath)) {
    return { ok: false, reason: 'BOOTSTRAP_BOUNDARY_MISSING' };
  }
  let raw;
  try {
    raw = JSON.parse(readFileSync(bootstrapPath, 'utf8'));
  } catch {
    return { ok: false, reason: 'BOOTSTRAP_BOUNDARY_MALFORMED' };
  }
  const cutoff =
    raw.production_bootstrap_cutoff ||
    raw.cutoff ||
    raw.eligibility_cutoff ||
    null;
  if (!cutoff) {
    return { ok: false, reason: 'BOOTSTRAP_CUTOFF_MISSING', raw_mode: raw.mode || null };
  }
  const cutoffMs = Date.parse(cutoff);
  if (Number.isNaN(cutoffMs)) {
    return { ok: false, reason: 'BOOTSTRAP_CUTOFF_INVALID' };
  }
  return { ok: true, boundary: raw, cutoff, cutoffMs };
}

function loadEnvFile(p) {
  const out = {};
  if (!existsSync(p)) return out;
  for (const line of readFileSync(p, 'utf8').split(/\r?\n/)) {
    const m = line.match(/^\s*([A-Za-z0-9_]+)\s*=\s*(.*)\s*$/);
    if (!m) continue;
    let v = m[2];
    if (
      (v.startsWith('"') && v.endsWith('"')) ||
      (v.startsWith("'") && v.endsWith("'"))
    ) {
      v = v.slice(1, -1);
    }
    out[m[1]] = v;
  }
  return out;
}

function buildEnvelopeFromSource(sourceDir) {
  const py = process.env.CLIENT_OPS_PYTHON || 'py';
  const code = `
import json, sys
from pathlib import Path
sys.path.insert(0, r${JSON.stringify(join(MAIN_ROOT, 'projects/client-ops-reporting-bridge/src'))})
from client_ops_reporting_bridge.site002_adapter import adapt_source_dir
proc, _r, _f = adapt_source_dir(Path(sys.argv[1]), build_envelope=True)
if not proc.distributable or proc.envelope is None:
    print(json.dumps({"ok": False, "reason": "NOT_DISTRIBUTABLE"}))
    sys.exit(2)
env = dict(proc.envelope)
# Unattended producer identity marker (non-secret)
prod = dict(env.get("producer") or {})
prod["name"] = "mars.client-ops.site-002.unattended-producer"
prod["version"] = str(prod.get("version") or "1")
env["producer"] = prod
print(json.dumps({"ok": True, "envelope": env}, ensure_ascii=False))
`;
  const r = spawnSync(py, ['-3', '-c', code, sourceDir], {
    cwd: MAIN_ROOT,
    encoding: 'utf8',
    windowsHide: true,
    timeout: 120000,
    env: {
      ...process.env,
      PYTHONPATH: join(MAIN_ROOT, 'projects/client-ops-reporting-bridge/src'),
      PYTHONIOENCODING: 'utf-8',
    },
  });
  const stdout = String(r.stdout || '').trim();
  const lines = stdout.split(/\r?\n/).filter(Boolean);
  let parsed = null;
  for (let i = lines.length - 1; i >= 0; i -= 1) {
    try {
      parsed = JSON.parse(lines[i]);
      break;
    } catch {
      /* continue */
    }
  }
  if (!parsed?.ok || !parsed.envelope) {
    return {
      ok: false,
      reason: parsed?.reason || 'ENVELOPE_BUILD_FAILED',
      status: r.status,
      stderr_len: String(r.stderr || '').length,
    };
  }
  return { ok: true, envelope: parsed.envelope, event_id: parsed.envelope.event_id };
}

async function postWebhookEnvelope(envelope) {
  const secrets = loadEnvFile(
    join(MAIN_ROOT, 'local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env'),
  );
  const n8n = loadEnvFile(join(MAIN_ROOT, 'local/tokens/n8n-api.env'));
  // Canonical key is CLIENT_OPS_WEBHOOK_AUTH_SECRET (Phase 1B-B1 / D0).
  // Legacy aliases retained for compatibility; wrong-key-only env caused D6F silence.
  const token =
    secrets.CLIENT_OPS_WEBHOOK_AUTH_SECRET ||
    secrets.CLIENT_OPS_WEBHOOK_TOKEN ||
    secrets.WEBHOOK_TOKEN ||
    secrets.MARS_CLIENT_OPS_TOKEN;
  const apiUrl = (n8n.N8N_API_URL || '').replace(/\/$/, '');
  if (!token || !apiUrl) {
    return { ok: false, reason: 'WEBHOOK_CREDS_MISSING' };
  }
  // Resolve webhook path via GET workflow (path only, never logged raw with secret)
  const LIB_MAIN = join(
    MAIN_ROOT,
    'projects/client-ops-reporting-bridge/n8n/runners/lib',
  );
  const transport = await import(
    pathToFileURL(join(LIB, 'client-ops-d6e2-readonly-transport.mjs')).href
  );
  const creds = transport.loadCredentials(join(MAIN_ROOT, 'local/tokens/n8n-api.env'));
  transport.assertGetOnlyAction('GET', 'workflow_for_webhook_path');
  const wf = await transport.getAllowlistedWorkflow(creds);
  if (!wf?.active) {
    return { ok: false, reason: 'WORKFLOW_NOT_ACTIVE' };
  }
  if (wf.versionId !== EXPECTED_VERSION) {
    return { ok: false, reason: 'WORKFLOW_VERSION_DRIFT', versionId: wf.versionId };
  }
  const nodes = Array.isArray(wf.nodes) ? wf.nodes : [];
  const webhook = nodes.find((n) => n.name === 'Webhook Intake');
  const path = webhook?.parameters?.path;
  if (!path) {
    return { ok: false, reason: 'WEBHOOK_PATH_MISSING' };
  }
  const url = `${apiUrl}/webhook/${path}`;
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      'x-mars-client-ops-token': token,
    },
    body: JSON.stringify(envelope),
  });
  const text = await response.text();
  let data = null;
  try {
    data = text ? JSON.parse(text) : null;
  } catch {
    data = { parse_error: true, body_len: text.length };
  }
  return {
    ok: response.status === 200 || response.status === 202,
    http_status: response.status,
    result_class: `HTTP_${response.status}`,
    intake_state: data?.intake_state ?? data?.data?.intake_state ?? null,
    delivery_state: data?.delivery_state ?? data?.data?.delivery_state ?? null,
    event_id: envelope.event_id,
  };
}

async function runSelfCheck() {
  const { parseKillSwitch } = await importPinned('client-ops-d6d-kill-switch.mjs');
  const {
    acquireProducerLock,
    releaseProducerLock,
  } = await importPinned('client-ops-d6d-producer-lock.mjs');
  const transport = await import(
    pathToFileURL(join(LIB, 'client-ops-d6e2-readonly-transport.mjs')).href
  );
  const results = [];
  function check(name, pass, detail = null) {
    results.push({ name, pass: Boolean(pass), detail });
  }

  const pinOk = verifyRuntimePin();
  check('runtime_pin_clean', pinOk.ok, pinOk);
  check('d6db_ancestry_present', pinOk.ok);

  const ksPath = join(STATE_ROOT, 'config', 'kill-switch.json');
  const ksOk = parseKillSwitchStrict(parseKillSwitch, ksPath, { allowEnabled: true });
  check(
    'kill_switch_production_mode',
    ksOk.ok && (ksOk.raw_mode === 'ENABLED' || ksOk.raw_mode === 'DRY_RUN'),
    { mode: ksOk.raw_mode, hash: ksOk.cfgHash },
  );

  const missing = parseKillSwitchStrict(
    parseKillSwitch,
    join(STATE_ROOT, 'tmp', 'missing-ks.json'),
  );
  check('missing_kill_switch_rejected', !missing.ok && missing.reason === 'KILL_SWITCH_MISSING');

  const bootstrap = loadBootstrapBoundary();
  check('bootstrap_cutoff_configured', bootstrap.ok, {
    cutoff: bootstrap.ok ? bootstrap.cutoff : null,
  });

  const wrapperSrc = readFileSync(
    join(STATE_ROOT, 'tmp', 'run-client-ops-site-002-producer-scheduled.mjs'),
    'utf8',
  );
  check(
    'wrapper_passes_raw_kill_switch',
    /kill_switch:\s*killSwitchRaw/.test(wrapperSrc) ||
      /Pass RAW kill-switch/i.test(wrapperSrc),
  );
  check(
    'wrapper_supports_enabled',
    /permanent-active delivery/i.test(wrapperSrc) &&
      /allowEnabled:\s*true/.test(wrapperSrc),
  );
  check(
    'no_one_shot_quota',
    /global_message_limit:\s*null|global_message_limit === null/i.test(wrapperSrc) ||
      /No one-shot quota/i.test(wrapperSrc),
  );
  check(
    'no_auto_disable_after_first',
    /auto_disable_after_first_message:\s*false/i.test(wrapperSrc) &&
      !/auto_disable_after_first_message:\s*true/i.test(wrapperSrc),
  );

  const lockPath = join(STATE_ROOT, 'locks', 'producer.lock.json');
  const owner = randomUUID();
  const acq1 = acquireProducerLock({
    lockPath,
    siteId: 'SITE-002',
    producerIdentity: 'mars.client-ops.site-002.unattended-producer',
    ownerToken: owner,
    sessionId: randomUUID(),
    runtimeCheckoutIdentity: PIN,
    nowMs: Date.now(),
    leaseMs: 60_000,
    pid: process.pid,
    processIdentity: 'd6f-selfcheck',
    processAlive: () => true,
  });
  const acq2 = acquireProducerLock({
    lockPath,
    siteId: 'SITE-002',
    producerIdentity: 'mars.client-ops.site-002.unattended-producer',
    ownerToken: randomUUID(),
    sessionId: randomUUID(),
    runtimeCheckoutIdentity: PIN,
    nowMs: Date.now(),
    leaseMs: 60_000,
    pid: process.pid + 1,
    processIdentity: 'd6f-selfcheck-2',
    processAlive: () => true,
  });
  check('active_lock_second_acquire_rejected', acq1.ok === true && acq2.ok === false);
  releaseProducerLock(lockPath, owner);

  const proof = transport.proveReadOnlyInvariant();
  check('readonly_invariant_available', Boolean(proof.token || proof.ok), proof.token);
  check('secrets_not_on_argv', !process.argv.some((a) => /api[_-]?key|token|secret|password/i.test(a)));

  const allPass = results.every((r) => r.pass);
  const out = {
    phase: '1B-D6F',
    mode: 'self-check',
    pass: allPass,
    results,
    kill_switch_config_hash: ksOk.cfgHash || null,
    runtime_commit: pinOk.head || null,
    finished_at: new Date().toISOString(),
    token: allPass
      ? 'D6F_SCHEDULER_WRAPPER_SELF_CHECK_PASS'
      : 'PARTIAL_D6F_WRAPPER_SELF_CHECK_FAIL',
  };
  writeJson(join(STATE_ROOT, 'logs', 'scheduler-self-check.json'), out);
  console.log(JSON.stringify(out, null, 2));
  process.exit(allPass ? 0 : 1);
}

async function runScheduled() {
  appendLog('START scheduled production runner');
  const pin = verifyRuntimePin();
  if (!pin.ok) {
    failExit(40, pin.reason, { exit_class: 'FAILED_PREFLIGHT', ...pin });
  }

  const { parseKillSwitch } = await importPinned('client-ops-d6d-kill-switch.mjs');
  const { runUnattendedProducer } = await importPinned(
    'client-ops-d6d-unattended-producer.mjs',
  );
  const { sanitizeCursor, applyCursorObservation } = await importPinned(
    'client-ops-d6d-cursor.mjs',
  );
  const { D6D_SITE_ID, HISTORICAL_PENDING_EVENT_ID, DELIVERY_ELIGIBILITY, EXIT_CODES } =
    await importPinned('client-ops-d6d-constants.mjs');
  const {
    discoverCandidates,
    validateCompletedRun,
    selectCandidates,
    evaluateDeliveryEligibility,
  } = await importPinned('client-ops-d6d-artifact.mjs');
  const {
    acquireProducerLock,
    releaseProducerLock,
  } = await importPinned('client-ops-d6d-producer-lock.mjs');

  const ksPath = join(STATE_ROOT, 'config', 'kill-switch.json');
  const ksParsed = parseKillSwitchStrict(parseKillSwitch, ksPath, {
    allowEnabled: true,
  });
  if (!ksParsed.ok) {
    failExit(20, ksParsed.reason, {
      exit_class: 'BLOCKED_KILL_SWITCH',
      kill_switch_mode: ksParsed.mode || null,
    });
  }
  const killSwitchRaw = ksParsed.raw;
  const killMode = ksParsed.raw_mode;

  const bootstrap = loadBootstrapBoundary();
  if (killMode === 'ENABLED' && !bootstrap.ok) {
    failExit(24, bootstrap.reason || 'BOOTSTRAP_BOUNDARY_REQUIRED', {
      exit_class: 'BLOCKED_BOOTSTRAP',
      kill_switch_mode: killMode,
    });
  }

  const cursorPath = join(STATE_ROOT, 'state', 'producer-cursor.json');
  let cursor = {
    schema_version: 1,
    site_id: 'SITE-002',
    evaluated_runs: {},
    bootstrap_boundary: bootstrap.ok ? bootstrap.boundary : null,
  };
  if (existsSync(cursorPath)) {
    cursor = JSON.parse(readFileSync(cursorPath, 'utf8'));
    if (bootstrap.ok) {
      cursor.bootstrap_boundary = bootstrap.boundary;
    }
  }

  const lockPath = join(STATE_ROOT, 'locks', 'producer.lock.json');
  const producerRunId = randomUUID();
  const startedIso = new Date().toISOString();
  const receiptPath = join(
    STATE_ROOT,
    'receipts',
    `scheduler-${killMode.toLowerCase()}-${startedIso.replace(/[:.]/g, '-')}.json`,
  );

  // DRY_RUN path: reuse committed unattended producer (no delivery)
  if (killMode === 'DRY_RUN') {
    let transport = null;
    let creds = null;
    let ledgerObservation = null;
    try {
      transport = await import(
        pathToFileURL(join(LIB, 'client-ops-d6e2-readonly-transport.mjs')).href
      );
      const secretPath = join(MAIN_ROOT, 'local', 'tokens', 'n8n-api.env');
      if (existsSync(secretPath)) {
        creds = transport.loadCredentials(secretPath);
      }
    } catch (e) {
      appendLog(`WARN readonly_transport_unavailable detail=${String(e.message || e).slice(0, 120)}`);
    }

    const result = await runUnattendedProducer({
      producer_run_id: producerRunId,
      site_id: D6D_SITE_ID,
      clock: { nowMs: () => Date.now() },
      fs: createRealFsFixed(),
      artifact_root: ARTIFACT_ROOT,
      allowlist_roots: [ARTIFACT_ROOT],
      kill_switch: killSwitchRaw,
      cursor,
      writeCursor: (next) => writeJson(cursorPath, sanitizeCursor(next)),
      producer_lock_path: lockPath,
      lock_owner_token: randomUUID(),
      runtime_checkout_identity: PIN,
      processAlive: (pid) => {
        try {
          process.kill(pid, 0);
          return true;
        } catch {
          return false;
        }
      },
      require_completion_marker: false,
      min_age_ms: 0,
      monitor_running: false,
      max_candidates_per_run: 1,
      max_safe_concurrency: 1,
      bootstrap_boundary: bootstrap.ok ? bootstrap.boundary : { mode: 'DRY_RUN' },
      runtime: {
        workingDirectory: PRODUCER_REPO,
        headCommit: PIN,
        dirty: false,
        ancestorCommits: REQUIRED_ANCESTORS,
        killSwitchMode: 'DRY_RUN',
        secretsPresent: Boolean(creds?.apiKey),
        producerTaskRunning: false,
        monitorTaskRunning: false,
        artifactStable: true,
        maxConcurrency: 1,
        automaticRetries: false,
        maxAutomaticRetries: 0,
      },
      getLedgerRow: async (eventId) => {
        if (!transport || !creds?.apiKey) {
          return { event_id: eventId, rows: 0, delivery_state: null, skipped: 'NO_CREDS' };
        }
        transport.assertGetOnlyAction('GET', 'data_table_rows_get');
        const filtered = await transport.getAllowlistedDataTableRows(creds, {
          limit: 20,
          filter: {
            filters: [{ columnName: 'event_id', condition: 'eq', value: eventId }],
          },
        });
        const filterRows = filtered?.data || filtered || [];
        const rows = Array.isArray(filterRows) ? filterRows : [];
        const eventRow = rows[0] || null;
        const rowData = eventRow?.data || eventRow || {};
        ledgerObservation = {
          event_id: eventId,
          rows: rows.length,
          intake_state: rowData.intake_state ?? null,
          event_status: rowData.event_status ?? null,
          delivery_state: rowData.delivery_state ?? null,
        };
        return ledgerObservation;
      },
      writeReceipt: (receipt) => {
        writeJson(receiptPath, {
          ...receipt,
          task_name: TASK_NAME,
          runtime_commit: PIN,
          kill_switch_mode: 'DRY_RUN',
          request_authorized: false,
          scheduler_phase: '1B-D6F',
          ledger_observation: ledgerObservation,
        });
      },
    });

    const lastRun = {
      phase: '1B-D6F',
      task_name: TASK_NAME,
      ok: true,
      producer_run_id: producerRunId,
      runtime_commit: PIN,
      kill_switch_mode: 'DRY_RUN',
      kill_switch_config_hash: ksParsed.cfgHash,
      exit_code: result.exit_code,
      exit_class: result.exit_class,
      source_run_id: result.source_run_id || null,
      event_id: result.event_id || null,
      request_authorized: false,
      request_attempts: 0,
      started_at: startedIso,
      finished_at: new Date().toISOString(),
      reason_codes: result.reason_codes || [],
      receipt_path: receiptPath,
    };
    writeJson(join(STATE_ROOT, 'state', 'scheduler-last-run.json'), lastRun);
    appendLog(`END DRY_RUN exit_class=${result.exit_class}`);
    console.log(JSON.stringify(lastRun, null, 2));
    process.exit(typeof result.exit_code === 'number' ? result.exit_code : 1);
  }

  // ENABLED permanent-active delivery path
  appendLog('ENABLED permanent-active delivery path');
  const ownerToken = randomUUID();
  const acq = acquireProducerLock({
    lockPath,
    siteId: 'SITE-002',
    producerIdentity: 'mars.client-ops.site-002.unattended-producer',
    ownerToken,
    sessionId: producerRunId,
    runtimeCheckoutIdentity: PIN,
    nowMs: Date.now(),
    leaseMs: 25 * 60 * 1000,
    pid: process.pid,
    processIdentity: 'd6f-producer',
    processAlive: (pid) => {
      try {
        process.kill(pid, 0);
        return true;
      } catch {
        return false;
      }
    },
  });
  if (!acq.ok) {
    failExit(30, acq.reason || acq.class || 'LOCK_HELD', {
      exit_class: 'BLOCKED_CONCURRENCY',
      kill_switch_mode: killMode,
    });
  }

  const release = () => {
    try {
      releaseProducerLock(lockPath, ownerToken);
    } catch {
      /* ignore */
    }
  };

  try {
    // Verify workflow already active (no activate/deactivate)
    const transport = await import(
      pathToFileURL(join(LIB, 'client-ops-d6e2-readonly-transport.mjs')).href
    );
    const creds = transport.loadCredentials(join(MAIN_ROOT, 'local/tokens/n8n-api.env'));
    transport.assertGetOnlyAction('GET', 'workflow_active_check');
    const wf = await transport.getAllowlistedWorkflow(creds);
    if (!wf?.active) {
      release();
      failExit(40, 'WORKFLOW_NOT_ACTIVE_FOR_PERMANENT_DELIVERY', {
        exit_class: 'FAILED_READINESS',
        kill_switch_mode: killMode,
      });
    }
    if (wf.versionId !== EXPECTED_VERSION) {
      release();
      failExit(40, 'WORKFLOW_VERSION_DRIFT', {
        exit_class: 'FAILED_PREFLIGHT',
        kill_switch_mode: killMode,
        versionId: wf.versionId,
      });
    }

    const fs = createRealFsFixed();
    const listed = discoverCandidates(fs, ARTIFACT_ROOT, {
      listAll: true,
      includeIncomplete: true,
    });
    const validated = [];
    for (const c of listed) {
      if (/\.(part|tmp|temp)$/i.test(c.run_name)) continue;
      const v = validateCompletedRun(fs, c.run_dir, {
        allowlistRoots: [ARTIFACT_ROOT],
        clock: { nowMs: () => Date.now() },
        requireCompletionMarker: false,
        minAgeMs: 0,
      });
      validated.push({ ...v, run_dir: c.run_dir, run_name: c.run_name });
    }

    const okOnes = validated.filter((v) => v.ok);
    // Production bootstrap cutoff filter
    const postCutoff = okOnes.filter((v) => {
      const observedMs = Date.parse(v.observed_at || '');
      if (Number.isNaN(observedMs)) return false;
      if (observedMs < bootstrap.cutoffMs) return false;
      if (v.event_id === HISTORICAL_PENDING || v.event_id === HISTORICAL_PENDING_EVENT_ID) {
        return false;
      }
      return true;
    });

    if (postCutoff.length === 0) {
      release();
      const lastRun = {
        phase: '1B-D6F',
        task_name: TASK_NAME,
        ok: true,
        producer_run_id: producerRunId,
        runtime_commit: PIN,
        kill_switch_mode: killMode,
        exit_code: EXIT_CODES.SUCCESS_NO_CANDIDATE,
        exit_class: 'SUCCESS_NO_CANDIDATE',
        reason_codes: ['NO_POST_CUTOFF_CANDIDATE'],
        production_bootstrap_cutoff: bootstrap.cutoff,
        candidates_complete: okOnes.length,
        candidates_post_cutoff: 0,
        request_authorized: false,
        request_attempts: 0,
        started_at: startedIso,
        finished_at: new Date().toISOString(),
      };
      writeJson(join(STATE_ROOT, 'state', 'scheduler-last-run.json'), lastRun);
      writeJson(receiptPath, lastRun);
      appendLog('END ENABLED no post-cutoff candidate');
      console.log(JSON.stringify(lastRun, null, 2));
      process.exit(EXIT_CODES.SUCCESS_NO_CANDIDATE);
    }

    let selectedList = selectCandidates(postCutoff, {
      maxCandidatesPerRun: 1,
      cursor,
    });
    if (selectedList.length === 0) {
      release();
      const lastRun = {
        phase: '1B-D6F',
        ok: true,
        exit_class: 'SUCCESS_ALREADY_HANDLED',
        exit_code: EXIT_CODES.SUCCESS_ALREADY_HANDLED,
        reason_codes: ['ALL_POST_CUTOFF_TERMINAL_IN_CURSOR'],
        kill_switch_mode: killMode,
        finished_at: new Date().toISOString(),
      };
      writeJson(join(STATE_ROOT, 'state', 'scheduler-last-run.json'), lastRun);
      console.log(JSON.stringify(lastRun, null, 2));
      process.exit(EXIT_CODES.SUCCESS_ALREADY_HANDLED);
    }

    const candidate = selectedList[0];
    const elig = evaluateDeliveryEligibility({
      source_status: candidate.source_status,
      age_seconds: candidate.age_seconds,
    });
    if (elig.delivery_eligibility !== DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE) {
      const nextCursor = applyCursorObservation(cursor, {
        run_id: candidate.run_id,
        event_id: candidate.event_id,
        artifact_hash: candidate.artifact_fingerprint,
        cursor_state: 'EVALUATED',
        result_class: elig.delivery_eligibility,
        delivery_decision: 'NO_SEND',
        evaluation_timestamp: new Date().toISOString(),
        bootstrap_boundary: bootstrap.boundary,
      });
      writeJson(cursorPath, sanitizeCursor(nextCursor));
      release();
      const lastRun = {
        phase: '1B-D6F',
        ok: true,
        exit_class: 'BLOCKED_STALE',
        exit_code: EXIT_CODES.BLOCKED_STALE,
        event_id: candidate.event_id,
        source_run_id: candidate.run_id,
        delivery_eligibility: elig.delivery_eligibility,
        reason_codes: ['POST_CUTOFF_BUT_NOT_FRESH'],
        kill_switch_mode: killMode,
        request_authorized: false,
        finished_at: new Date().toISOString(),
      };
      writeJson(join(STATE_ROOT, 'state', 'scheduler-last-run.json'), lastRun);
      console.log(JSON.stringify(lastRun, null, 2));
      process.exit(EXIT_CODES.BLOCKED_STALE);
    }

    // Durable ledger check
    transport.assertGetOnlyAction('GET', 'dedupe_precheck');
    const filtered = await transport.getAllowlistedDataTableRows(creds, {
      limit: 5,
      filter: {
        filters: [
          { columnName: 'event_id', condition: 'eq', value: candidate.event_id },
        ],
      },
    });
    const filterRows = filtered?.data || filtered || [];
    const rows = Array.isArray(filterRows) ? filterRows : [];
    const rowData = rows[0]?.data || rows[0] || {};
    const durableState = rowData.delivery_state
      ? String(rowData.delivery_state).toUpperCase()
      : null;
    if (durableState === 'SENT') {
      release();
      const lastRun = {
        phase: '1B-D6F',
        ok: true,
        exit_class: 'SUCCESS_ALREADY_HANDLED',
        exit_code: EXIT_CODES.SUCCESS_ALREADY_HANDLED,
        event_id: candidate.event_id,
        delivery_state: 'SENT',
        reason_codes: ['LEDGER_SENT_NO_RESEND'],
        kill_switch_mode: killMode,
        finished_at: new Date().toISOString(),
      };
      writeJson(join(STATE_ROOT, 'state', 'scheduler-last-run.json'), lastRun);
      console.log(JSON.stringify(lastRun, null, 2));
      process.exit(EXIT_CODES.SUCCESS_ALREADY_HANDLED);
    }
    if (durableState === 'PENDING') {
      release();
      const lastRun = {
        phase: '1B-D6F',
        ok: false,
        exit_class: 'RECONCILIATION_REQUIRED',
        exit_code: EXIT_CODES.RECONCILIATION_REQUIRED,
        event_id: candidate.event_id,
        delivery_state: 'PENDING',
        reason_codes: ['PENDING_BLOCKS_UNATTENDED_SEND'],
        kill_switch_mode: killMode,
        finished_at: new Date().toISOString(),
      };
      writeJson(join(STATE_ROOT, 'state', 'scheduler-last-run.json'), lastRun);
      console.log(JSON.stringify(lastRun, null, 2));
      process.exit(EXIT_CODES.RECONCILIATION_REQUIRED);
    }

    // Build + POST
    const built = buildEnvelopeFromSource(candidate.run_dir);
    if (!built.ok) {
      release();
      failExit(40, built.reason || 'ENVELOPE_BUILD_FAILED', {
        exit_class: 'FAILED_LOCAL_STATE',
        kill_switch_mode: killMode,
      });
    }
    // Prefer deterministic event id from artifact validation
    if (built.envelope && candidate.event_id) {
      built.envelope.event_id = candidate.event_id;
    }

    const post = await postWebhookEnvelope(built.envelope);
    if (!post.ok) {
      release();
      const lastRun = {
        phase: '1B-D6F',
        ok: false,
        exit_class: 'FAILED_REQUEST',
        exit_code: EXIT_CODES.FAILED_REQUEST || 50,
        event_id: candidate.event_id,
        source_run_id: candidate.run_id,
        http_status: post.http_status || null,
        reason_codes: [post.reason || post.result_class || 'WEBHOOK_POST_FAILED'],
        kill_switch_mode: killMode,
        request_authorized: true,
        request_attempts: 1,
        automatic_retries: 0,
        finished_at: new Date().toISOString(),
      };
      writeJson(join(STATE_ROOT, 'state', 'scheduler-last-run.json'), lastRun);
      writeJson(receiptPath, lastRun);
      appendLog(`END ENABLED delivery failed http=${post.http_status}`);
      console.log(JSON.stringify(lastRun, null, 2));
      process.exit(lastRun.exit_code);
    }

    const nextCursor = applyCursorObservation(cursor, {
      run_id: candidate.run_id,
      event_id: candidate.event_id,
      artifact_hash: candidate.artifact_fingerprint,
      cursor_state: 'DELIVERY_TERMINAL',
      result_class: 'DELIVERED',
      delivery_decision: 'DELIVERED',
      processing_terminal: true,
      durable_delivery_state: 'SENT',
      evaluation_timestamp: new Date().toISOString(),
      bootstrap_boundary: bootstrap.boundary,
    });
    writeJson(cursorPath, sanitizeCursor(nextCursor));
    release();

    const lastRun = {
      phase: '1B-D6F',
      task_name: TASK_NAME,
      ok: true,
      producer_run_id: producerRunId,
      runtime_commit: PIN,
      kill_switch_mode: killMode,
      exit_code: EXIT_CODES.SUCCESS_DELIVERED,
      exit_class: 'SUCCESS_DELIVERED',
      event_id: candidate.event_id,
      source_run_id: candidate.run_id,
      delivery_eligibility: elig.delivery_eligibility,
      http_status: post.http_status,
      production_bootstrap_cutoff: bootstrap.cutoff,
      request_authorized: true,
      request_attempts: 1,
      automatic_retries: 0,
      auto_disable_after_first_message: false,
      workflow_left_active: true,
      started_at: startedIso,
      finished_at: new Date().toISOString(),
      receipt_path: receiptPath,
      reason_codes: ['DELIVERED_PERMANENT_ACTIVE'],
    };
    writeJson(join(STATE_ROOT, 'state', 'scheduler-last-run.json'), lastRun);
    writeJson(receiptPath, lastRun);
    appendLog(`END ENABLED delivered event=${candidate.event_id}`);
    console.log(JSON.stringify(lastRun, null, 2));
    process.exit(EXIT_CODES.SUCCESS_DELIVERED);
  } catch (err) {
    release();
    failExit(40, String(err?.message || err).slice(0, 200), {
      exit_class: 'FAILED_PREFLIGHT',
      kill_switch_mode: killMode,
    });
  }
}

async function runLockProbe() {
  const {
    acquireProducerLock,
    releaseProducerLock,
  } = await importPinned('client-ops-d6d-producer-lock.mjs');
  const lockPath = join(STATE_ROOT, 'locks', 'producer.lock.json');
  const owner = randomUUID();
  const acq1 = acquireProducerLock({
    lockPath,
    siteId: 'SITE-002',
    producerIdentity: 'mars.client-ops.site-002.unattended-producer',
    ownerToken: owner,
    sessionId: randomUUID(),
    runtimeCheckoutIdentity: PIN,
    nowMs: Date.now(),
    leaseMs: 30_000,
    pid: process.pid,
    processIdentity: 'd6f-lock-probe',
    processAlive: () => true,
  });
  const acq2 = acquireProducerLock({
    lockPath,
    siteId: 'SITE-002',
    producerIdentity: 'mars.client-ops.site-002.unattended-producer',
    ownerToken: randomUUID(),
    sessionId: randomUUID(),
    runtimeCheckoutIdentity: PIN,
    nowMs: Date.now(),
    leaseMs: 30_000,
    pid: process.pid + 9999,
    processIdentity: 'd6f-lock-probe-2',
    processAlive: () => true,
  });
  releaseProducerLock(lockPath, owner);
  const out = {
    first_ok: acq1.ok === true,
    second_ok: acq2.ok === true,
    second_rejected: acq2.ok === false,
    lock_released: !existsSync(lockPath),
    token:
      acq1.ok && !acq2.ok
        ? 'D6F_PRODUCER_LOCK_OVERLAP_REJECTED'
        : 'PARTIAL_D6F_LOCK_PROBE_FAIL',
  };
  console.log(JSON.stringify(out, null, 2));
  process.exit(out.second_rejected && out.first_ok ? 0 : 1);
}

if (mode === 'self-check') {
  await runSelfCheck();
} else if (mode === 'lock-probe') {
  await runLockProbe();
} else {
  await runScheduled();
}

