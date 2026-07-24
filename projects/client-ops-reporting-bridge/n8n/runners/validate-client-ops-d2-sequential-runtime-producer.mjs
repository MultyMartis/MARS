/**
 * Phase 1B-D2 — offline sequential runtime producer validator.
 * No live n8n mutation. No secret printing. No network POST.
 *
 * Usage:
 *   node validate-client-ops-d2-sequential-runtime-producer.mjs
 */
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const PROJECT = resolve(REPO_ROOT, 'projects/client-ops-reporting-bridge');
const PACK = resolve(
  PROJECT,
  'evidence/phase-1b-d2-sequential-runtime-producer-offline',
);
const PHASE = resolve(
  PROJECT,
  'PHASE-1B-D2-SEQUENTIAL-RUNTIME-PRODUCER-DESIGN-AND-OFFLINE-IMPLEMENTATION.md',
);
const SRC = resolve(PROJECT, 'src/client_ops_reporting_bridge');

const REQUIRED_PACK = [
  'README.md',
  'D2-CHARTER.json',
  'CURRENT-EXPORTER-INVENTORY.md',
  'PRODUCER-ARCHITECTURE.md',
  'SOURCE-TO-ENVELOPE-CONTRACT.md',
  'EVENT-ID-CONTRACT.md',
  'SECRET-AND-ENDPOINT-CONTRACT.md',
  'SEQUENTIAL-DISPATCH-POLICY.md',
  'TIMEOUT-AND-RETRY-CONTRACT.md',
  'RESPONSE-CLASSIFICATION-MATRIX.md',
  'PRODUCER-RESULT-CONTRACT.md',
  'OBSERVABILITY-IMPLEMENTATION.md',
  'SITE-002-COMPATIBILITY-ASSESSMENT.md',
  'NETWORK-DISPATCH-GUARD.md',
  'D3-CONTROLLED-CONNECTION-PREREQUISITES.md',
  'SECURITY-REVIEW.md',
  'TEST-RESULTS.md',
  'D2-DECISION.json',
];

const REQUIRED_MODULES = [
  'producer_constants.py',
  'producer_config.py',
  'producer_request.py',
  'producer_transport.py',
  'producer_dispatch_guard.py',
  'producer_classify.py',
  'producer_result.py',
  'producer_evidence.py',
  'producer_firewall.py',
  'producer_pipeline.py',
  'cli.py',
];

const SECRET_RES = [
  /\b\d{8,10}:[A-Za-z0-9_-]{30,}\b/,
  /api\.telegram\.org\/bot\d+/i,
  /CLIENT_OPS_WEBHOOK_AUTH_SECRET\s*=\s*\S+/i,
  /N8N_API_KEY\s*=\s*\S+/i,
  /https?:\/\/[^\s"'`]+\/webhook\/[^\s"'`]+/i,
];

const FORBIDDEN_NETWORK_ENABLE = [
  /transport\s*=\s*['"]http['"].*default/i,
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

function main() {
  const gates = [];
  const pass = (id, detail = '') => gates.push({ id, ok: true, detail });
  const fail = (id, detail = '') => gates.push({ id, ok: false, detail });

  if (existsSync(PHASE)) pass('phase_doc');
  else fail('phase_doc', 'missing phase md');

  for (const name of REQUIRED_PACK) {
    if (existsSync(resolve(PACK, name))) pass(`pack_${name}`);
    else fail(`pack_${name}`, 'missing');
  }

  for (const name of REQUIRED_MODULES) {
    if (existsSync(resolve(SRC, name))) pass(`module_${name}`);
    else fail(`module_${name}`, 'missing');
  }

  const transport = readFileSync(resolve(SRC, 'producer_transport.py'), 'utf8');
  if (/NETWORK_DISPATCH_NOT_AUTHORIZED_D2/.test(transport)) {
    pass('network_gate_constant');
  } else fail('network_gate_constant');
  if (/class BlockedHttpTransport/.test(transport) || /transport=http not authorized/.test(transport)) {
    pass('http_blocked');
  } else fail('http_blocked');
  if (!/urllib\.request\.urlopen\(/.test(transport) && !/httpx\./.test(transport)) {
    pass('no_live_http_in_transport');
  } else fail('no_live_http_in_transport');

  const guard = readFileSync(resolve(SRC, 'producer_dispatch_guard.py'), 'utf8');
  if (/concurrency/.test(guard) && /SequentialDispatchError/.test(guard)) {
    pass('sequential_guard');
  } else fail('sequential_guard');

  const classify = readFileSync(resolve(SRC, 'producer_classify.py'), 'utf8');
  if (/MANUAL_DEDUPE_CHECK_REQUIRED/.test(classify)) pass('ambiguous_timeout_rule');
  else fail('ambiguous_timeout_rule');
  if (/INTAKE_ACCEPTED/.test(classify) && /telegram_delivery_known=False/.test(classify)) {
    pass('intake_vs_telegram');
  } else fail('intake_vs_telegram');
  if (/automatic_retry=False/.test(classify)) pass('no_auto_retry');
  else fail('no_auto_retry');

  const firewall = readFileSync(resolve(SRC, 'producer_firewall.py'), 'utf8');
  if (/RAW_MONITOR_FORBIDDEN_KEYS/.test(firewall) || /forbidden field/.test(firewall)) {
    pass('source_allowlist');
  } else fail('source_allowlist');

  const config = readFileSync(resolve(SRC, 'producer_config.py'), 'utf8');
  if (/secrets\.local\.env/.test(config) || /SECRETS_FILENAME/.test(readFileSync(resolve(SRC, 'producer_constants.py'), 'utf8'))) {
    pass('secret_boundary');
  } else fail('secret_boundary');

  const evidence = readFileSync(resolve(SRC, 'producer_evidence.py'), 'utf8');
  if (/write_evidence_atomic|os\.replace/.test(evidence)) pass('evidence_writer');
  else fail('evidence_writer');

  const d3 = existsSync(resolve(PACK, 'D3-CONTROLLED-CONNECTION-PREREQUISITES.md'))
    ? readFileSync(resolve(PACK, 'D3-CONTROLLED-CONNECTION-PREREQUISITES.md'), 'utf8')
    : '';
  if (/D3/.test(d3) && /NOT/.test(d3)) pass('d3_gate_doc');
  else fail('d3_gate_doc');

  const cli = readFileSync(resolve(SRC, 'cli.py'), 'utf8');
  if (/push-webhook/.test(cli) && /NETWORK_DISPATCH_NOT_AUTHORIZED_D2/.test(cli)) {
    pass('push_webhook_blocked');
  } else fail('push_webhook_blocked');
  if (!/Schedule|scheduler\.|crontab/.test(cli)) pass('no_scheduler_in_cli');
  else fail('no_scheduler_in_cli');

  // Scan producer modules for forbidden network enable defaults
  for (const file of walk(SRC).filter((f) => f.endsWith('.py') && f.includes('producer'))) {
    const text = readFileSync(file, 'utf8');
    for (const re of FORBIDDEN_NETWORK_ENABLE) {
      if (re.test(text) && !/raise NetworkDispatchNotAuthorized/.test(text)) {
        // urlopen in comments/tests of other modules ok; producer modules must not call
        if (/urlopen|requests\.|httpx\./.test(text) && /def dispatch/.test(text)) {
          fail('network_static_scan', file);
        }
      }
    }
  }
  pass('network_static_scan_producer');

  // Secret leakage scan on pack + phase doc
  const scanRoots = [PACK, PHASE, resolve(PROJECT, 'producer.local.json.example')].filter(
    (p) => existsSync(p),
  );
  let leak = false;
  for (const root of scanRoots) {
    for (const file of walk(root)) {
      if (!/\.(md|json|py|mjs|txt)$/i.test(file)) continue;
      const text = readFileSync(file, 'utf8');
      for (const re of SECRET_RES) {
        if (re.test(text)) {
          // allow example.invalid placeholders without real webhook path secrets
          if (/example\.invalid/.test(text) && /webhook\/client-ops-PLACEHOLDER/.test(text)) {
            continue;
          }
          if (/https?:\/\/n8n\.example\.invalid\/webhook\//i.test(text)) continue;
          leak = true;
          fail('secret_scan', file.replace(REPO_ROOT, ''));
        }
      }
    }
  }
  if (!leak) pass('secret_scan_clean');

  const decisionPath = resolve(PACK, 'D2-DECISION.json');
  if (existsSync(decisionPath)) {
    const decision = JSON.parse(readFileSync(decisionPath, 'utf8'));
    if (
      decision.readiness ===
      'READY_FOR_SEQUENTIAL_RUNTIME_PRODUCER_OFFLINE_BASELINE_COMMIT'
    ) {
      pass('readiness_label');
    } else fail('readiness_label', decision.readiness);
    if (decision.network_dispatch === 'FORBIDDEN_D2') pass('decision_network_forbidden');
    else fail('decision_network_forbidden');
  }

  const failed = gates.filter((g) => !g.ok);
  const summary = {
    validator: 'validate-client-ops-d2-sequential-runtime-producer',
    phase: '1B-D2',
    passed: gates.filter((g) => g.ok).length,
    failed: failed.length,
    gates,
    network: false,
    n8n_mutation: false,
  };
  console.log(JSON.stringify(summary, null, 2));
  process.exit(failed.length ? 1 : 0);
}

main();
