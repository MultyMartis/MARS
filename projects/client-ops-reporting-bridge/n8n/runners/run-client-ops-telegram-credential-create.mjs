/**
 * Client Ops Telegram credential create runner (Phase 1B-C).
 *
 * Default: dry-run.
 * Live create requires:
 *   --apply
 *   --confirm="CREATE CLIENT OPS TELEGRAM CREDENTIAL BZPM"
 *
 * Loads TELEGRAM_BOT_TOKEN from gitignored local file into process memory only.
 * Never prints the token or request body. Does not send Telegram messages.
 * Does not update workflows.
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
const CONFIRM_PHRASE = 'CREATE CLIENT OPS TELEGRAM CREDENTIAL BZPM';
const CREDENTIAL_NAME = 'MARS Client Ops Telegram — bzpm.ru';
const CREDENTIAL_TYPE = 'telegramApi';
const TOKEN_FIELD = 'accessToken';
const SECRET_PATH = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/telegram.secrets.local.env',
);
const SECRET_KEY = 'TELEGRAM_BOT_TOKEN';
const LOCAL_EVIDENCE = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/evidence/phase-1b-c',
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
 * @returns {{ ok: boolean, lengthClass: string, value?: string, error?: string, keyCount?: number }}
 */
function loadTokenFromLocalFile() {
  if (!existsSync(SECRET_PATH)) {
    return { ok: false, lengthClass: 'missing', error: 'secret_file_missing', keyCount: 0 };
  }
  const raw = readFileSync(SECRET_PATH, 'utf8');
  let keyCount = 0;
  let value = '';
  for (const line of raw.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    if (!trimmed.startsWith(`${SECRET_KEY}=`)) continue;
    keyCount += 1;
    if (keyCount === 1) {
      value = trimmed.slice(`${SECRET_KEY}=`.length).trim();
      if (
        (value.startsWith('"') && value.endsWith('"')) ||
        (value.startsWith("'") && value.endsWith("'"))
      ) {
        value = value.slice(1, -1);
      }
    }
  }
  if (keyCount !== 1 || !value) {
    return {
      ok: false,
      lengthClass: value ? 'n/a' : 'empty',
      error: keyCount === 0 ? 'secret_key_missing' : 'secret_key_count_invalid',
      keyCount,
    };
  }
  const lengthClass =
    value.length >= 64
      ? 'gte64'
      : value.length >= 45
        ? 'gte45_lt64'
        : value.length >= 30
          ? 'gte30_lt45'
          : 'lt30';
  if (!/^[0-9]{6,}:[A-Za-z0-9_-]{20,}$/.test(value)) {
    return { ok: false, lengthClass, error: 'secret_structure_implausible', keyCount };
  }
  return { ok: true, lengthClass, value, keyCount };
}

function schemaOk(schema) {
  const props = schema?.properties || {};
  return Boolean(
    schema &&
      props[TOKEN_FIELD] &&
      (props[TOKEN_FIELD].type === 'string' || typeof props[TOKEN_FIELD] === 'object'),
  );
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const report = {
    runner: 'run-client-ops-telegram-credential-create',
    mode: args.apply ? 'APPLY' : 'DRY_RUN',
    confirmation_phrase_required: CONFIRM_PHRASE,
    credential_name: CREDENTIAL_NAME,
    credential_type: CREDENTIAL_TYPE,
    token_field: TOKEN_FIELD,
    secret_source: SECRET_PATH.replace(/\\/g, '/'),
    secret_key: SECRET_KEY,
    secret_value_exposed: false,
    secret_printed: false,
    raw_request_printed: false,
    created: false,
    created_count: 0,
    workflow_mutations: 0,
    telegram_messages: 0,
  };

  const tokenInfo = loadTokenFromLocalFile();
  report.secret_length_class = tokenInfo.lengthClass;
  report.secret_key_count = tokenInfo.keyCount ?? 0;
  if (!tokenInfo.ok) {
    report.aborted = tokenInfo.error;
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
  report.schema_property_keys = Object.keys(schema?.properties || {});
  report.schema_ok = schemaOk(schema);
  report.schema_verdict = report.schema_ok
    ? 'TELEGRAM_N8N_CREDENTIAL_SCHEMA_CONFIRMED'
    : 'TELEGRAM_N8N_CREDENTIAL_SCHEMA_BLOCKED';
  if (!report.schema_ok) {
    report.aborted = 'schema_mismatch';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  const listed = await listCredentialsMetadata(creds);
  const exact = listed.filter((c) => c.name === CREDENTIAL_NAME);
  const sameType = listed.filter((c) => c.type === CREDENTIAL_TYPE);
  report.pre_create_exact_name_count = exact.length;
  report.pre_create_telegramApi_count = sameType.length;
  report.similar_telegram_credentials = sameType.map((c) => ({
    id: c.id,
    name: c.name,
    type: c.type,
  }));

  if (exact.length > 1) {
    report.aborted = 'NAME_COLLISION_AMBIGUOUS';
    report.exact_hits_sanitized = sanitizeCredentialResponse(exact);
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }
  if (exact.length === 1) {
    report.aborted = 'NAME_COLLISION_EXISTS';
    report.exact_hits_sanitized = sanitizeCredentialResponse(exact);
    report.reuse_safe = false;
    report.note =
      'Exact-name credential already exists. Do not create another. Do not update/delete.';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }

  if (!args.apply) {
    report.note =
      'Dry-run only. Pass --apply and exact confirmation phrase to create Telegram credential.';
    report.ready = true;
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
      [TOKEN_FIELD]: tokenInfo.value,
    },
  };

  let created;
  try {
    created = await createCredential(createPayload, creds);
  } catch (err) {
    createPayload.data[TOKEN_FIELD] = '';
    tokenInfo.value = '';
    report.aborted = 'create_failed';
    report.error = err instanceof Error ? err.message.slice(0, 240) : 'create_failed';
    const afterFail = await listCredentialsMetadata(creds);
    const afterExact = afterFail.filter((c) => c.name === CREDENTIAL_NAME);
    report.post_fail_exact_name_count = afterExact.length;
    report.post_fail_hits_sanitized = sanitizeCredentialResponse(afterExact);
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 4;
    return;
  }

  createPayload.data[TOKEN_FIELD] = '';
  tokenInfo.value = '';

  report.created = true;
  report.created_count = 1;
  report.sanitized_credential = sanitizeCredentialResponse(created);

  const after = await listCredentialsMetadata(creds);
  const afterExact = after.filter((c) => c.name === CREDENTIAL_NAME);
  report.post_create_exact_name_count = afterExact.length;
  report.duplicate_after = afterExact.length !== 1;
  report.token_visible_in_metadata = afterExact.some(
    (c) => c && Object.prototype.hasOwnProperty.call(c, 'data'),
  );

  mkdirSync(LOCAL_EVIDENCE, { recursive: true });
  writeFileSync(
    resolve(LOCAL_EVIDENCE, 'telegram-credential-create-report.sanitized.json'),
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
      runner: 'run-client-ops-telegram-credential-create',
      aborted: 'uncaught',
      error: err instanceof Error ? err.message.slice(0, 240) : String(err).slice(0, 240),
      secret_value_exposed: false,
      raw_request_printed: false,
    }),
  );
  process.exitCode = 1;
});
