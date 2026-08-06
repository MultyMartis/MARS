/**
 * Offline Client Ops n8n validation harness.
 * No network. Synthetic auth secret only.
 */

import { readFileSync, readdirSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  AUTH_HEADER,
  AUTH_PLACEHOLDER,
  processClientOpsRequest,
  SYNTHETIC_HARNESS_SECRET,
} from './client-ops-validator.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const CASES_DIR = join(__dirname, 'cases');

function loadJson(path) {
  return JSON.parse(readFileSync(path, 'utf8'));
}

function deepClone(value) {
  return JSON.parse(JSON.stringify(value));
}

function assertEqual(actual, expected, label) {
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a !== e) {
    throw new Error(`${label}: expected ${e}, got ${a}`);
  }
}

function runCase(tc) {
  const input = {
    headers: tc.input.headers || {},
    body: tc.input.body,
    rawBodyBytes: tc.input.rawBodyBytes,
    expectedSecret:
      tc.input.expectedSecret === undefined
        ? SYNTHETIC_HARNESS_SECRET
        : tc.input.expectedSecret,
    forceDuplicateDeferredResponse: Boolean(
      tc.input.forceDuplicateDeferredResponse,
    ),
  };

  const out = processClientOpsRequest(input);

  if (tc.expect.http_status !== undefined) {
    assertEqual(out.http_status, tc.expect.http_status, 'http_status');
  }
  if (tc.expect.response) {
    for (const [key, value] of Object.entries(tc.expect.response)) {
      assertEqual(out.response[key], value, `response.${key}`);
    }
  }
  if (tc.expect.evidence_gate) {
    assertEqual(out.evidence?.gate, tc.expect.evidence_gate, 'evidence.gate');
  }
  if (tc.expect.evidence_code) {
    assertEqual(out.evidence?.code, tc.expect.evidence_code, 'evidence.code');
  }

  // Hard security: never echo synthetic secret or placeholder into response.
  const blob = JSON.stringify(out);
  if (blob.includes(SYNTHETIC_HARNESS_SECRET)) {
    throw new Error('secret leakage: synthetic harness secret in output');
  }
  if (blob.includes(AUTH_PLACEHOLDER)) {
    throw new Error('secret leakage: auth placeholder in output');
  }
  if (/Bearer\s+SYNTHETIC_/i.test(blob)) {
    throw new Error('secret leakage: bearer synthetic secret in output');
  }

  return out;
}

function main() {
  const files = readdirSync(CASES_DIR)
    .filter((f) => f.endsWith('.json'))
    .sort();

  let passed = 0;
  let failed = 0;
  const failures = [];

  for (const file of files) {
    const tc = loadJson(join(CASES_DIR, file));
    try {
      runCase(tc);
      passed += 1;
      console.log(`PASS  ${tc.id || file}`);
    } catch (err) {
      failed += 1;
      const msg = err instanceof Error ? err.message : String(err);
      failures.push({ id: tc.id || file, message: msg });
      console.log(`FAIL  ${tc.id || file}: ${msg}`);
    }
  }

  console.log('---');
  console.log(
    JSON.stringify(
      {
        harness: 'client-ops-n8n-offline',
        cases: files.length,
        passed,
        failed,
        auth_header: AUTH_HEADER,
        synthetic_secret_label: 'SYNTHETIC_CLIENT_OPS_HARNESS_SECRET_v1_NOT_A_REAL_CREDENTIAL',
        network: false,
      },
      null,
      2,
    ),
  );

  if (failed > 0) {
    process.exitCode = 1;
  }
}

main();
