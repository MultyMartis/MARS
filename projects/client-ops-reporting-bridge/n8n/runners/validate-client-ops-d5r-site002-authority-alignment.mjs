/**
 * Phase 1B-D5R — SITE-002 authority alignment validator.
 * No live n8n mutation. No secret printing. No network POST.
 *
 * Usage:
 *   node validate-client-ops-d5r-site002-authority-alignment.mjs
 */
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const PROJECT = resolve(REPO_ROOT, 'projects/client-ops-reporting-bridge');
const PACK = resolve(
  PROJECT,
  'evidence/phase-1b-d5r-site002-authority-alignment',
);
const PHASE = resolve(
  PROJECT,
  'PHASE-1B-D5R-SITE002-MONITOR-CLASSIFICATION-AUTHORITY-ALIGNMENT-AND-FRESH-SAFE-SOURCE-REASSESSMENT.md',
);
const SITE002_MONITOR = resolve(
  REPO_ROOT,
  'projects/ocpilot/sites/site-002/tools/site-002-prod-post-1c-catalog-onboarding-monitor-02.py',
);
const SITE002_RUNNER = resolve(
  REPO_ROOT,
  'projects/ocpilot/sites/site-002/tools/site-002-post-1c-monitor-runner.ps1',
);

const REQUIRED_PACK = [
  'README.md',
  'D5R-CHARTER.json',
  'SOURCE-WRITER-CODE-PATH.md',
  'ARTIFACT-SEMANTICS-MATRIX.md',
  'DOCUMENTATION-PRECEDENCE-REVIEW.md',
  'ROOT-CAUSE-ANALYSIS.md',
  'CANONICAL-NOTIFICATION-AUTHORITY.md',
  'STATUS-PRECEDENCE-CONTRACT.md',
  'FRESHNESS-SEMANTICS.md',
  'EVENT-ID-IMPACT.json',
  'D5-CANDIDATE-REASSESSMENT.json',
  'D5-CHARTER-STATE.md',
  'SITE002-REPAIR-REQUIREMENT.md',
  'SECURITY-REVIEW.md',
  'TEST-RESULTS.md',
  'D5R-DECISION.json',
  'LIVE-GET-ONLY-STATE.json',
];

const SECRET_RES = [
  /\b\d{8,10}:[A-Za-z0-9_-]{30,}\b/,
  /api\.telegram\.org\/bot\d+/i,
  /CLIENT_OPS_WEBHOOK_AUTH_SECRET\s*=\s*\S+/i,
  /N8N_API_KEY\s*=\s*\S+/i,
  /https?:\/\/[^\s"'`]+\/webhook\/[^\s"'`]+/i,
  /X:\\AI MARS STORAGE\\/i,
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

  if (!existsSync(PHASE)) failures.push('missing D5R phase document');
  for (const name of REQUIRED_PACK) {
    if (!existsSync(join(PACK, name))) failures.push(`missing evidence ${name}`);
  }

  const decisionPath = join(PACK, 'D5R-DECISION.json');
  let decision = null;
  if (existsSync(decisionPath)) {
    decision = JSON.parse(read(decisionPath));
    if (decision.primary_root_cause !== 'MONITOR_ARTIFACT_GENERATION_BUG') {
      failures.push('primary root-cause classification missing/wrong');
    }
    if (decision.root_cause_standard !== 'ROOT_CAUSE_CONFIRMED') {
      failures.push('root cause not confirmed in decision');
    }
    if (
      decision.canonical_notification_authority !==
      'CANONICAL_SITE002_NOTIFICATION_AUTHORITY_CONFIRMED'
    ) {
      failures.push('canonical authority decision missing');
    }
    if (decision.client_ops_repair !== 'NOT_APPLIED') {
      failures.push('Client Ops repair must remain NOT_APPLIED for Outcome B');
    }
    if (decision.site002_monitor_repair !== 'SITE002_MONITOR_REPAIR_REQUIRED') {
      failures.push('SITE-002 repair requirement missing');
    }
    if (
      decision.freshness_semantics !==
      'FRESHNESS_STATUS_SEMANTICS_REQUIRES_SEPARATE_REPAIR'
    ) {
      failures.push('freshness semantics decision missing');
    }
    if (decision.live_post !== false) failures.push('live_post must be false');
    if (decision.monitor_executions !== 0) {
      failures.push('monitor_executions must be 0');
    }
    if (decision.site002_repo_edits !== 0) {
      failures.push('site002_repo_edits must be 0');
    }
    if (decision.d5_charter?.charter_consumed !== false) {
      failures.push('D5 charter must remain unused');
    }
    if (decision.d5_charter?.real_http_requests !== 0) {
      failures.push('D5 real_http_requests must be 0');
    }
    if (
      decision.readiness !==
      'READY_FOR_SITE002_MONITOR_ARTIFACT_AUTHORITY_REPAIR_CHARTER'
    ) {
      failures.push('readiness token mismatch');
    }
  } else {
    failures.push('missing D5R-DECISION.json');
  }

  const writer = existsSync(join(PACK, 'SOURCE-WRITER-CODE-PATH.md'))
    ? read(join(PACK, 'SOURCE-WRITER-CODE-PATH.md'))
    : '';
  if (!/export_scheduled_artifacts/.test(writer)) {
    failures.push('writer path missing export_scheduled_artifacts');
  }
  if (!/Finish-Summary/.test(writer)) {
    failures.push('writer path missing Finish-Summary');
  }

  const authority = existsSync(join(PACK, 'CANONICAL-NOTIFICATION-AUTHORITY.md'))
    ? read(join(PACK, 'CANONICAL-NOTIFICATION-AUTHORITY.md'))
    : '';
  if (!/monitor-classification\.json/.test(authority)) {
    failures.push('canonical authority missing monitor-classification');
  }

  const precedence = existsSync(join(PACK, 'STATUS-PRECEDENCE-CONTRACT.md'))
    ? read(join(PACK, 'STATUS-PRECEDENCE-CONTRACT.md'))
    : '';
  if (!/site002-monitor-result-v1/.test(precedence)) {
    failures.push('status precedence missing v1 contract');
  }

  const impact = existsSync(join(PACK, 'EVENT-ID-IMPACT.json'))
    ? JSON.parse(read(join(PACK, 'EVENT-ID-IMPACT.json')))
    : null;
  if (!impact || impact.candidates?.length !== 3) {
    failures.push('event ID impact must cover exactly 3 candidates');
  }

  const reassessment = existsSync(join(PACK, 'D5-CANDIDATE-REASSESSMENT.json'))
    ? JSON.parse(read(join(PACK, 'D5-CANDIDATE-REASSESSMENT.json')))
    : null;
  if (!reassessment || reassessment.candidates?.length !== 3) {
    failures.push('candidate reassessment must cover exactly 3 candidates');
  }
  if (reassessment?.d5r_raw_source_log_reads !== 0) {
    failures.push('raw logs must remain 0');
  }

  const live = existsSync(join(PACK, 'LIVE-GET-ONLY-STATE.json'))
    ? JSON.parse(read(join(PACK, 'LIVE-GET-ONLY-STATE.json')))
    : null;
  if (live?.precheck?.active !== false) failures.push('workflow must be inactive');
  if (live?.precheck?.executions_count !== 31) {
    failures.push('executions must remain 31');
  }
  if (live?.datatable?.rows !== 2) failures.push('datatable rows must remain 2');
  if (live?.mutations?.activation_changes !== 0) {
    failures.push('activation mutations must be 0');
  }

  // SITE-002 tools exist (read-only proof target) — D5R must not claim edits applied
  if (!existsSync(SITE002_MONITOR) || !existsSync(SITE002_RUNNER)) {
    failures.push('SITE-002 monitor/runner missing for authority trace');
  }
  notes.push('SITE-002 tools present; D5R decision asserts repo edits=0');

  // Security scan over D5R pack only
  for (const file of walk(PACK)) {
    if (!/\.(md|json|mjs|py|txt)$/i.test(file)) continue;
    const text = read(file);
    for (const re of SECRET_RES) {
      if (re.test(text)) {
        failures.push(`secret/path leak pattern in ${file}`);
      }
    }
  }

  const phaseText = existsSync(PHASE) ? read(PHASE) : '';
  if (phaseText && !/MONITOR_ARTIFACT_GENERATION_BUG/.test(phaseText)) {
    failures.push('phase doc missing primary root cause');
  }
  if (
    phaseText &&
    !/PARTIAL — MANUAL SITE-002 REAL-SOURCE CONNECTION NOT STARTED; PRE-LIVE GATE BLOCKED/.test(
      phaseText,
    )
  ) {
    failures.push('phase doc must preserve D5 historical verdict');
  }

  const ok = failures.length === 0;
  const result = {
    validator: 'validate-client-ops-d5r-site002-authority-alignment',
    ok,
    failures,
    notes,
    decision_readiness: decision?.readiness || null,
  };
  console.log(JSON.stringify(result, null, 2));
  process.exit(ok ? 0 : 1);
}

main();
