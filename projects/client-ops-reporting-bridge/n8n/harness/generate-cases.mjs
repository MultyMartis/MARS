/**
 * One-shot generator for offline harness cases.
 * Run: node generate-cases.mjs
 */
import { writeFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  AUTH_HEADER,
  AUTH_PLACEHOLDER,
  SYNTHETIC_HARNESS_SECRET,
} from './client-ops-validator.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const dir = join(__dirname, 'cases');
mkdirSync(dir, { recursive: true });

const base = {
  schema_name: 'mars.client_ops.report',
  schema_version: '1.0',
  event_id: '703f19ac-92bd-5d6b-8664-d908b8de8b74',
  event_type: 'site.post_1c_monitor',
  generated_at: '2026-07-20T15:10:00Z',
  observed_at: '2026-07-20T15:05:00Z',
  environment: 'production',
  site: { site_id: 'SITE-002', site_name: 'ZPM', domain: 'bzpm.ru' },
  producer: { name: 'ocpilot.site-002.post-1c-exporter', version: '1.0' },
  run: {
    run_id: '2026-07-20_18-05-00',
    source_status: 'NO_ACTION_REQUIRED',
    normalized_status: 'OK',
    summary_code: 'NO_ACTION_REQUIRED',
    reason_codes: ['BASELINE_DELTA_ZERO'],
  },
  action: { required: false, code: 'NONE', text: 'none' },
  metrics: {
    baseline_count: 100,
    current_count: 100,
    added_urls: 0,
    removed_urls: 0,
    onboarding_needed_count: 0,
  },
  freshness: { age_seconds: 300, stale: false },
  security: {
    classification: 'internal',
    contains_secrets: false,
    redacted: true,
  },
};

function clone(o) {
  return JSON.parse(JSON.stringify(o));
}

function authHeaders(extra = {}) {
  return {
    'content-type': 'application/json',
    [AUTH_HEADER]: SYNTHETIC_HARNESS_SECRET,
    ...extra,
  };
}

const cases = [];

function add(id, title, mutate, expect) {
  const body = clone(base);
  const input = { headers: authHeaders(), body };
  mutate(input, body);
  cases.push({ id, title, input, expect });
}

add('01-valid-ok', 'Valid OK', () => {}, {
  http_status: 202,
  response: { ok: true, result: 'ACCEPTED', dedupe: 'DEFERRED_SANDBOX' },
  evidence_gate: 'accepted',
});

add(
  '02-valid-attention',
  'Valid ATTENTION',
  (_i, body) => {
    body.run.normalized_status = 'ATTENTION';
    body.run.source_status = 'ONBOARDING_REQUIRED';
    body.run.summary_code = 'ONBOARDING_REQUIRED';
    body.action = {
      required: true,
      code: 'REVIEW_ONBOARDING',
      text: 'review catalog branches',
    };
    body.metrics = {
      baseline_count: 1737,
      current_count: 1817,
      added_urls: 80,
      removed_urls: 0,
      onboarding_needed_count: 4,
    };
    body.event_id = '86ed33fb-c65f-594e-b0be-72afbe626de4';
  },
  { http_status: 202, response: { ok: true, result: 'ACCEPTED' } },
);

add(
  '03-valid-failed',
  'Valid FAILED',
  (_i, body) => {
    body.run.normalized_status = 'FAILED';
    body.run.source_status = 'FAILURE_REVIEW_REQUIRED';
    body.run.summary_code = 'SOURCE_EXECUTION_FAILED';
    body.action = {
      required: true,
      code: 'REVIEW_SOURCE_FAILURE',
      text: 'review monitor failure',
    };
    body.event_id = '702b3d9b-7f88-599e-8c97-ab67aba8e668';
  },
  { http_status: 202, response: { ok: true, result: 'ACCEPTED' } },
);

add(
  '04-valid-blocked',
  'Valid BLOCKED distributable',
  (_i, body) => {
    body.run.normalized_status = 'BLOCKED';
    body.run.source_status = 'SOURCE_ARTIFACT_CONFLICT';
    body.run.summary_code = 'SOURCE_ARTIFACT_CONFLICT';
    body.action = {
      required: true,
      code: 'REVIEW_SOURCE_ARTIFACTS',
      text: 'review source artifacts',
    };
    body.event_id = '8a2435c4-6755-56b8-adfc-e7f562409c27';
  },
  { http_status: 202, response: { ok: true, result: 'ACCEPTED' } },
);

add(
  '05-invalid-schema-name',
  'Invalid schema_name',
  (_i, b) => {
    b.schema_name = 'wrong.schema';
  },
  {
    http_status: 400,
    response: { ok: false, result: 'REJECTED', code: 'INVALID_SCHEMA' },
  },
);

add(
  '06-unsupported-schema-major',
  'Unsupported schema major',
  (_i, b) => {
    b.schema_version = '2.0';
  },
  { http_status: 400, response: { code: 'INVALID_SCHEMA' } },
);

add(
  '07-missing-required-field',
  'Missing required field',
  (_i, b) => {
    delete b.producer;
  },
  { http_status: 400, response: { code: 'INVALID_SCHEMA' } },
);

add(
  '08-wrong-site-id',
  'Wrong site_id',
  (_i, b) => {
    b.site.site_id = 'SITE-999';
  },
  { http_status: 400, response: { code: 'INVALID_SCHEMA' } },
);

add(
  '09-wrong-domain',
  'Wrong domain',
  (_i, b) => {
    b.site.domain = 'example.com';
  },
  { http_status: 400, response: { code: 'INVALID_SCHEMA' } },
);

add(
  '10-wrong-event-type',
  'Wrong event_type',
  (_i, b) => {
    b.event_type = 'other.event';
  },
  { http_status: 400, response: { code: 'INVALID_SCHEMA' } },
);

add(
  '11-invalid-normalized-status',
  'Invalid normalized_status',
  (_i, b) => {
    b.run.normalized_status = 'WARN';
  },
  { http_status: 400, response: { code: 'INVALID_SCHEMA' } },
);

add(
  '12-contains-secrets-true',
  'contains_secrets=true',
  (_i, b) => {
    b.security.contains_secrets = true;
  },
  { http_status: 400, response: { code: 'SECURITY_REJECTED' } },
);

add(
  '13-redacted-false',
  'redacted=false',
  (_i, b) => {
    b.security.redacted = false;
  },
  { http_status: 400, response: { code: 'SECURITY_REJECTED' } },
);

add(
  '14-invalid-uuid',
  'Invalid UUID',
  (_i, b) => {
    b.event_id = 'not-a-uuid';
  },
  { http_status: 400, response: { code: 'INVALID_SCHEMA' } },
);

add(
  '15-bool-metric',
  'Bool metric',
  (_i, b) => {
    b.metrics.added_urls = true;
  },
  { http_status: 400, response: { code: 'INVALID_SCHEMA' } },
);

add(
  '16-negative-metric',
  'Negative metric',
  (_i, b) => {
    b.metrics.removed_urls = -1;
  },
  { http_status: 400, response: { code: 'INVALID_SCHEMA' } },
);

add(
  '17-windows-path',
  'Windows path',
  (_i, b) => {
    b.action.text = 'see X:\\AI MARS\\secret';
  },
  { http_status: 400, response: { code: 'SECURITY_REJECTED' } },
);

add(
  '18-unc-path',
  'UNC path',
  (_i, b) => {
    b.action.text = 'see \\\\fileserver\\share\\run';
  },
  { http_status: 400, response: { code: 'SECURITY_REJECTED' } },
);

add(
  '19-embedded-credentials-uri',
  'Embedded credentials URI',
  (_i, b) => {
    b.action.text = 'https://user:pass@example.com/x';
  },
  { http_status: 400, response: { code: 'SECURITY_REJECTED' } },
);

add(
  '20-token-like-marker',
  'Token-like marker',
  (_i, b) => {
    b.action.text = 'api_key=abc123shouldreject';
  },
  { http_status: 400, response: { code: 'SECURITY_REJECTED' } },
);

add(
  '21-stack-trace',
  'Stack trace',
  (_i, b) => {
    b.action.text =
      'Traceback (most recent call last):\n  File "x.py", line 1';
  },
  { http_status: 400, response: { code: 'SECURITY_REJECTED' } },
);

add(
  '22-oversized-payload',
  'Oversized payload simulation',
  (i) => {
    i.rawBodyBytes = 300 * 1024;
  },
  { http_status: 413, response: { code: 'PAYLOAD_TOO_LARGE' } },
);

add(
  '23-invalid-content-type',
  'Invalid content type',
  (i) => {
    i.headers['content-type'] = 'text/plain';
  },
  { http_status: 415, response: { code: 'UNSUPPORTED_MEDIA_TYPE' } },
);

add(
  '24-missing-auth',
  'Missing auth',
  (i) => {
    delete i.headers[AUTH_HEADER];
  },
  { http_status: 401, response: { code: 'UNAUTHORIZED' } },
);

add(
  '25-wrong-auth',
  'Wrong auth',
  (i) => {
    i.headers[AUTH_HEADER] = 'WRONG_SYNTHETIC_VALUE';
  },
  { http_status: 401, response: { code: 'UNAUTHORIZED' } },
);

add('26-valid-auth-interface', 'Valid auth interface synthetic', () => {}, {
  http_status: 202,
  response: { ok: true, result: 'ACCEPTED' },
});

add(
  '27-duplicate-deferred-sandbox',
  'Duplicate-deferred sandbox response',
  (i) => {
    i.forceDuplicateDeferredResponse = true;
  },
  {
    http_status: 200,
    response: {
      ok: true,
      result: 'DUPLICATE',
      dedupe: 'DEFERRED_SANDBOX',
    },
    evidence_code: 'DEDUPE_NOT_ENABLED_SANDBOX',
  },
);

cases.push({
  id: '28-auth-placeholder-unresolved',
  title: 'Unresolved HITL auth placeholder',
  input: {
    headers: authHeaders(),
    body: clone(base),
    expectedSecret: AUTH_PLACEHOLDER,
  },
  expect: {
    http_status: 401,
    response: { code: 'UNAUTHORIZED' },
    evidence_code: 'AUTH_BINDING_UNRESOLVED',
  },
});

for (const c of cases) {
  writeFileSync(join(dir, `${c.id}.json`), `${JSON.stringify(c, null, 2)}\n`);
}

console.log(`wrote ${cases.length} cases`);
