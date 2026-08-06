/**
 * Client Ops Header Auth credential create runner.
 *
 * Default: dry-run.
 * Live create requires:
 *   --apply
 *   --confirm="CREATE CLIENT OPS HEADER AUTH CREDENTIAL BZPM"
 *
 * Loads CLIENT_OPS_WEBHOOK_AUTH_SECRET from gitignored local file into process
 * memory only. Never prints the secret or request body.
 */

import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  createCredential,
  getCredentialSchema,
  listCredentialsMetadata,
  loadCredentialClientCredentials,
  sanitizeCredentialResponse,
} from './lib/client-ops-n8n-credential-client.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const EXPECTED_HOST = 'n8n.ai-metacode.com';
const CONFIRM_PHRASE = 'CREATE CLIENT OPS HEADER AUTH CREDENTIAL BZPM';
const CREDENTIAL_NAME = 'MARS Client Ops Webhook Auth — bzpm.ru';
const CREDENTIAL_TYPE = 'httpHeaderAuth';
const HEADER_NAME = 'X-MARS-Client-Ops-Token';
const SECRET_PATH = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env',
);
const SECRET_KEY = 'CLIENT_OPS_WEBHOOK_AUTH_SECRET';
const LOCAL_EVIDENCE = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/evidence/phase-1b-b1',
);

function parseArgs(argv) {
  const args = { apply: false, confirm: null };
  for (const a of argv) {
    if (a === '--apply') args.apply = true;
    else if (a.startsWith('--confirm=')) args.confirm = a.slice('--confirm='.length);
  }
  return args;
}

/**
 * Load secret into memory without printing it.
 * @returns {{ ok: boolean, lengthClass: string, value?: string, error?: string }}
 */
function loadSecretFromLocalFile() {
  if (!existsSync(SECRET_PATH)) {
    return { ok: false, lengthClass: 'missing', error: 'secret_file_missing' };
  }
  const raw = readFileSync(SECRET_PATH, 'utf8');
  let value = '';
  for (const line of raw.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    if (!trimmed.startsWith(`${SECRET_KEY}=`)) continue;
    value = trimmed.slice(`${SECRET_KEY}=`.length).trim();
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    break;
  }
  if (!value) {
    return { ok: false, lengthClass: 'empty', error: 'secret_key_missing_or_empty' };
  }
  const lengthClass =
    value.length >= 64
      ? 'gte64'
      : value.length >= 32
        ? 'gte32'
        : 'lt32';
  if (value.length < 32) {
    return { ok: false, lengthClass, error: 'secret_length_below_32' };
  }
  return { ok: true, lengthClass, value };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const report = {
    runner: 'run-client-ops-credential-create',
    mode: args.apply ? 'APPLY' : 'DRY_RUN',
    confirmation_phrase_required: CONFIRM_PHRASE,
    credential_name: CREDENTIAL_NAME,
    credential_type: CREDENTIAL_TYPE,
    header_name: HEADER_NAME,
    secret_source: SECRET_PATH.replace(/\\/g, '/'),
    secret_key: SECRET_KEY,
    secret_value_exposed: false,
    secret_printed: false,
    created: false,
    created_count: 0,
  };

  const secretInfo = loadSecretFromLocalFile();
  report.secret_file_exists = secretInfo.ok || secretInfo.error !== 'secret_file_missing';
  report.secret_key_present = secretInfo.ok || secretInfo.error !== 'secret_key_missing_or_empty';
  report.secret_length_class = secretInfo.lengthClass;
  if (!secretInfo.ok) {
    report.aborted = secretInfo.error;
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  const creds = loadCredentialClientCredentials();
  const host = new URL(creds.apiUrl).host;
  report.api_host = host;
  if (host !== EXPECTED_HOST) {
    report.aborted = `unexpected_api_host:${host}`;
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  const schema = await getCredentialSchema(CREDENTIAL_TYPE, creds);
  report.schema_ok = Boolean(
    schema &&
      schema.properties &&
      schema.properties.name &&
      schema.properties.value,
  );
  if (!report.schema_ok) {
    report.aborted = 'schema_mismatch';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  const listed = await listCredentialsMetadata(creds);
  const exact = listed.filter((c) => c.name === CREDENTIAL_NAME);
  report.pre_create_exact_name_count = exact.length;
  report.pre_create_types_sample = [...new Set(listed.map((c) => c.type))].sort();
  if (exact.length > 0) {
    report.aborted = 'NAME_COLLISION';
    report.exact_hits_sanitized = sanitizeCredentialResponse(exact);
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }

  if (!args.apply) {
    report.note =
      'Dry-run only. Pass --apply and exact confirmation phrase to create credential.';
    console.log(JSON.stringify(report, null, 2));
    return;
  }

  if (args.confirm !== CONFIRM_PHRASE) {
    report.aborted = 'confirmation_mismatch';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }

  const createPayload = {
    name: CREDENTIAL_NAME,
    type: CREDENTIAL_TYPE,
    data: {
      name: HEADER_NAME,
      value: secretInfo.value,
    },
  };

  let created;
  try {
    created = await createCredential(createPayload, creds);
  } catch (err) {
    // Clear secret from memory path as best-effort; do not print.
    createPayload.data.value = '';
    secretInfo.value = '';
    report.aborted = 'create_failed';
    report.error = err instanceof Error ? err.message.slice(0, 240) : 'create_failed';
    // Ambiguity check
    const afterFail = await listCredentialsMetadata(creds);
    const afterExact = afterFail.filter((c) => c.name === CREDENTIAL_NAME);
    report.post_fail_exact_name_count = afterExact.length;
    report.post_fail_hits_sanitized = sanitizeCredentialResponse(afterExact);
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 4;
    return;
  }

  // Drop secret from local variables
  createPayload.data.value = '';
  secretInfo.value = '';

  report.created = true;
  report.created_count = 1;
  report.sanitized_credential = sanitizeCredentialResponse(created);

  const after = await listCredentialsMetadata(creds);
  const afterExact = after.filter((c) => c.name === CREDENTIAL_NAME);
  report.post_create_exact_name_count = afterExact.length;
  report.duplicate_after = afterExact.length !== 1;

  mkdirSync(LOCAL_EVIDENCE, { recursive: true });
  writeFileSync(
    resolve(LOCAL_EVIDENCE, 'credential-create-report.sanitized.json'),
    JSON.stringify(report, null, 2),
    'utf8',
  );

  console.log(JSON.stringify(report, null, 2));
  if (report.duplicate_after || !created.id) {
    process.exitCode = 5;
  }
}

main().catch((err) => {
  console.error(
    JSON.stringify({
      runner: 'run-client-ops-credential-create',
      aborted: 'uncaught',
      error: err instanceof Error ? err.message.slice(0, 240) : String(err).slice(0, 240),
      secret_value_exposed: false,
    }),
  );
  process.exitCode = 1;
});
