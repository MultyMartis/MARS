/**
 * Client Ops Telegram bot intake runner (Phase 1B-C / 1B-C0 / 1B-C0R2).
 *
 * Default: dry-run (no Telegram API calls).
 * Live read-only intake requires:
 *   --apply
 *   --confirm="VALIDATE CLIENT OPS TELEGRAM BOT INTAKE"
 *
 * Phase 1B-C0 chat-target discovery retry requires:
 *   --apply
 *   --confirm="DISCOVER CLIENT OPS TELEGRAM CHAT TARGET"
 *   [--skip-get-me]   // optional; default calls getMe once to reconfirm identity
 *
 * Phase 1B-C0R2 final chat-target discovery retry requires:
 *   --apply
 *   --confirm="FINAL DISCOVER CLIENT OPS TELEGRAM CHAT TARGET"
 *   [--skip-get-me]
 *
 * Loads TELEGRAM_BOT_TOKEN from gitignored local file into process memory only.
 * Never prints the token, never prints a Telegram API URL containing the token,
 * never invokes mutation / send methods.
 */

import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const CONFIRM_PHRASE_INTAKE = 'VALIDATE CLIENT OPS TELEGRAM BOT INTAKE';
const CONFIRM_PHRASE_DISCOVER = 'DISCOVER CLIENT OPS TELEGRAM CHAT TARGET';
const CONFIRM_PHRASE_DISCOVER_FINAL =
  'FINAL DISCOVER CLIENT OPS TELEGRAM CHAT TARGET';
const SECRET_PATH = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/telegram.secrets.local.env',
);
const TARGET_PATH = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/telegram.target.local.env',
);
const SECRET_KEY = 'TELEGRAM_BOT_TOKEN';
const REQUIRED_BOT_ID = 8852310960;
const REQUIRED_USERNAME = 'monitor_bzpm_metacode_bot';
const REQUIRED_FIRST_NAME = 'Монитор bzpm.ru — MetaCODE';
const LOCAL_EVIDENCE = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/evidence/phase-1b-c',
);
const LOCAL_EVIDENCE_C0 = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/evidence/phase-1b-c0',
);
const LOCAL_EVIDENCE_C0R2 = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/evidence/phase-1b-c0r2',
);
const TIMEOUT_MS = 15000;
const MAX_RESPONSE_BYTES = 64 * 1024;
const ALLOWED_METHODS = new Set(['getMe', 'getWebhookInfo', 'getUpdates']);
const FORBIDDEN_METHODS = new Set([
  'sendMessage',
  'sendPhoto',
  'sendDocument',
  'sendAudio',
  'sendVideo',
  'sendAnimation',
  'sendVoice',
  'sendVideoNote',
  'sendMediaGroup',
  'sendLocation',
  'sendVenue',
  'sendContact',
  'sendPoll',
  'sendDice',
  'sendChatAction',
  'sendInvoice',
  'sendSticker',
  'editMessageText',
  'editMessageCaption',
  'editMessageMedia',
  'editMessageReplyMarkup',
  'deleteMessage',
  'setWebhook',
  'deleteWebhook',
  'setMyCommands',
  'deleteMyCommands',
  'setMyName',
  'setMyDescription',
  'setMyShortDescription',
  'setChatPhoto',
  'setMyProfilePhoto',
  'leaveChat',
  'banChatMember',
  'unbanChatMember',
  'restrictChatMember',
  'promoteChatMember',
  'answerCallbackQuery',
]);

function parseArgs(argv) {
  const args = {
    apply: false,
    confirm: null,
    allowGetUpdates: true,
    skipGetMe: false,
  };
  for (const a of argv) {
    if (a === '--apply') args.apply = true;
    else if (a.startsWith('--confirm=')) args.confirm = a.slice('--confirm='.length);
    else if (a === '--no-get-updates') args.allowGetUpdates = false;
    else if (a === '--skip-get-me') args.skipGetMe = true;
  }
  return args;
}

function isStartLikeText(text) {
  if (typeof text !== 'string') return false;
  const t = text.trim().toLowerCase();
  // /start or /start@bot — inspect only; never persist text
  return t === '/start' || t.startsWith('/start@') || t === 'start';
}

/**
 * Persist confirmed private chat id into ignored local target file.
 * Refuses silent overwrite of a conflicting prior value.
 * @returns {{ ok: boolean, created: boolean, conflict: boolean, error?: string }}
 */
function writeLocalChatTarget(chatId) {
  const idStr = String(chatId);
  if (!/^-?\d+$/.test(idStr)) {
    return { ok: false, created: false, conflict: false, error: 'chat_id_not_numeric' };
  }
  if (existsSync(TARGET_PATH)) {
    const raw = readFileSync(TARGET_PATH, 'utf8');
    let existing = null;
    for (const line of raw.split(/\r?\n/)) {
      const t = line.trim();
      if (!t.startsWith('TELEGRAM_CHAT_ID=')) continue;
      existing = t.slice('TELEGRAM_CHAT_ID='.length).trim();
      break;
    }
    if (existing && existing !== idStr) {
      return { ok: false, created: false, conflict: true, error: 'existing_chat_id_conflict' };
    }
    if (existing === idStr) {
      return { ok: true, created: false, conflict: false };
    }
  }
  mkdirSync(dirname(TARGET_PATH), { recursive: true });
  writeFileSync(
    TARGET_PATH,
    `TELEGRAM_CHAT_ID=${idStr}\nTELEGRAM_CHAT_TYPE=private\n`,
    'utf8',
  );
  return { ok: true, created: true, conflict: false };
}

/**
 * @returns {{
 *   ok: boolean,
 *   exists: boolean,
 *   keyCount: number,
 *   lengthClass: string,
 *   plausible: boolean,
 *   value?: string,
 *   error?: string
 * }}
 */
function loadTokenFromLocalFile() {
  if (!existsSync(SECRET_PATH)) {
    return {
      ok: false,
      exists: false,
      keyCount: 0,
      lengthClass: 'missing',
      plausible: false,
      error: 'secret_file_missing',
    };
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
  if (keyCount !== 1) {
    return {
      ok: false,
      exists: true,
      keyCount,
      lengthClass: 'n/a',
      plausible: false,
      error: keyCount === 0 ? 'secret_key_missing' : 'secret_key_not_exact_once',
    };
  }
  if (!value) {
    return {
      ok: false,
      exists: true,
      keyCount,
      lengthClass: 'empty',
      plausible: false,
      error: 'secret_value_empty',
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
  const plausible = /^[0-9]{6,}:[A-Za-z0-9_-]{20,}$/.test(value);
  if (!plausible) {
    return {
      ok: false,
      exists: true,
      keyCount,
      lengthClass,
      plausible: false,
      error: 'secret_structure_implausible',
    };
  }
  return {
    ok: true,
    exists: true,
    keyCount,
    lengthClass,
    plausible: true,
    value,
  };
}

function normalizeName(s) {
  return String(s || '')
    .replace(/\u2014/g, '-') // em dash
    .replace(/\u2013/g, '-') // en dash
    .replace(/\s+/g, ' ')
    .trim()
    .toLowerCase();
}

function namesMatchMaterially(observed, required) {
  if (observed === required) return { exact: true, material: true };
  const a = normalizeName(observed);
  const b = normalizeName(required);
  return { exact: false, material: a === b };
}

/**
 * @param {string} method
 * @param {string} token
 * @param {Record<string, string|number|boolean>|undefined} query
 */
async function telegramReadonly(method, token, query) {
  if (!ALLOWED_METHODS.has(method)) {
    throw new Error(`Method not allowlisted: ${method}`);
  }
  if (FORBIDDEN_METHODS.has(method)) {
    throw new Error(`Forbidden mutation method: ${method}`);
  }
  // Build URL only in memory; never log.
  const url = new URL(`https://api.telegram.org/bot${token}/${method}`);
  if (query) {
    for (const [k, v] of Object.entries(query)) {
      url.searchParams.set(k, String(v));
    }
  }
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), TIMEOUT_MS);
  let response;
  try {
    response = await fetch(url.toString(), {
      method: 'GET',
      redirect: 'error',
      signal: controller.signal,
      headers: { Accept: 'application/json' },
    });
  } finally {
    clearTimeout(timer);
    // Drop token-bearing URL reference
    url.password = '';
  }

  const buf = Buffer.from(await response.arrayBuffer());
  if (buf.length > MAX_RESPONSE_BYTES) {
    throw new Error(`Response too large for ${method}`);
  }
  let data;
  try {
    data = JSON.parse(buf.toString('utf8'));
  } catch {
    throw new Error(`Invalid JSON from Telegram ${method}`);
  }
  return { httpStatus: response.status, data };
}

function sanitizeGetMe(result) {
  if (!result || typeof result !== 'object') return null;
  return {
    id: result.id ?? null,
    is_bot: result.is_bot ?? null,
    first_name: result.first_name ?? null,
    username: result.username ?? null,
    can_join_groups: result.can_join_groups ?? null,
    can_read_all_group_messages: result.can_read_all_group_messages ?? null,
    supports_inline_queries: result.supports_inline_queries ?? null,
    can_connect_to_business: result.can_connect_to_business ?? null,
    has_main_web_app: result.has_main_web_app ?? null,
  };
}

function sanitizeWebhookInfo(result) {
  if (!result || typeof result !== 'object') return null;
  const urlPresent = Boolean(result.url && String(result.url).length > 0);
  return {
    webhook_configured: urlPresent,
    url_exposed: false,
    url_value: urlPresent ? 'REDACTED' : '',
    has_custom_certificate: Boolean(result.has_custom_certificate),
    pending_update_count: result.pending_update_count ?? null,
    last_error_date: result.last_error_date ?? null,
    last_error_message_class: result.last_error_message
      ? String(result.last_error_message).slice(0, 80).replace(/https?:\/\/\S+/gi, 'URL_REDACTED')
      : null,
    max_connections: result.max_connections ?? null,
    ip_address_present: Boolean(result.ip_address),
  };
}

function sanitizeUpdates(result, opts = {}) {
  const requirePrivate = opts.requirePrivate !== false;
  const preferStart = opts.preferStart === true;
  const updates = Array.isArray(result) ? result : [];
  const chats = [];
  for (const u of updates) {
    const msg = u?.message || u?.edited_message || null;
    const member = u?.my_chat_member || null;
    const chat = msg?.chat || member?.chat || u?.channel_post?.chat || null;
    if (!chat || chat.id == null) continue;
    const text = typeof msg?.text === 'string' ? msg.text : null;
    const startLike = text ? isStartLikeText(text) : false;
    // my_chat_member to member status can also indicate Start without message text
    const memberStart =
      member &&
      member.new_chat_member &&
      (member.new_chat_member.status === 'member' ||
        member.new_chat_member.status === 'restricted');
    chats.push({
      chat_id: chat.id,
      chat_type: chat.type || null,
      start_like: Boolean(startLike || memberStart),
      update_kind: msg ? 'message' : member ? 'my_chat_member' : 'other',
      // Never record title/username/first_name/text
    });
  }
  // Dedupe by chat_id; keep start_like if any update for that chat was start-like
  const byId = new Map();
  for (const c of chats) {
    const prev = byId.get(c.chat_id);
    if (!prev) {
      byId.set(c.chat_id, {
        chat_id: c.chat_id,
        chat_type: c.chat_type,
        start_like: c.start_like,
        update_kind: c.update_kind,
      });
    } else {
      prev.start_like = prev.start_like || c.start_like;
    }
  }
  const unique = [...byId.values()];
  const privateCandidates = unique.filter((c) => c.chat_type === 'private');

  let verdict = 'TELEGRAM_CHAT_TARGET_NOT_YET_AVAILABLE';
  let selected = null;

  if (requirePrivate) {
    if (privateCandidates.length === 1) {
      const only = privateCandidates[0];
      if (!preferStart || only.start_like || privateCandidates.length === 1) {
        // Prefer start_like when available; still confirm single private chat
        // even if start flag absent (operator may have sent another message).
        verdict = 'TELEGRAM_CHAT_TARGET_CONFIRMED';
        selected = {
          chat_id: only.chat_id,
          chat_type: 'private',
          start_like: only.start_like,
          source_method: 'getUpdates',
        };
      }
    } else if (privateCandidates.length > 1) {
      verdict = 'TELEGRAM_CHAT_TARGET_AMBIGUOUS';
    }
  } else if (unique.length === 1) {
    verdict = 'TELEGRAM_CHAT_TARGET_CONFIRMED';
    selected = unique[0];
  } else if (unique.length > 1) {
    verdict = 'TELEGRAM_CHAT_TARGET_AMBIGUOUS';
  }

  return {
    update_count_observed: updates.length,
    unique_chat_count: unique.length,
    private_candidate_count: privateCandidates.length,
    candidates_sanitized: unique.map((c) => ({
      chat_id: c.chat_id,
      chat_type: c.chat_type,
      start_like: c.start_like,
      update_kind: c.update_kind,
    })),
    selected_chat: selected,
    verdict,
    raw_message_text_recorded: false,
    personal_names_recorded: false,
    phone_numbers_recorded: false,
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const isDiscoverFinal = args.confirm === CONFIRM_PHRASE_DISCOVER_FINAL;
  const isDiscover =
    args.confirm === CONFIRM_PHRASE_DISCOVER || isDiscoverFinal;
  const isIntake = args.confirm === CONFIRM_PHRASE_INTAKE;
  const confirmPhrase = isDiscoverFinal
    ? CONFIRM_PHRASE_DISCOVER_FINAL
    : isDiscover
      ? CONFIRM_PHRASE_DISCOVER
      : CONFIRM_PHRASE_INTAKE;
  const report = {
    runner: 'run-client-ops-telegram-intake',
    mode: args.apply
      ? isDiscoverFinal
        ? 'DISCOVER_FINAL_APPLY'
        : isDiscover
          ? 'DISCOVER_APPLY'
          : 'APPLY'
      : 'DRY_RUN',
    operation: isDiscoverFinal
      ? 'chat_target_discovery_final_retry'
      : isDiscover
        ? 'chat_target_discovery_retry'
        : 'telegram_bot_intake',
    confirmation_phrase_required: args.apply
      ? confirmPhrase
      : `${CONFIRM_PHRASE_INTAKE} | ${CONFIRM_PHRASE_DISCOVER} | ${CONFIRM_PHRASE_DISCOVER_FINAL}`,
    secret_source: SECRET_PATH.replace(/\\/g, '/'),
    secret_key: SECRET_KEY,
    secret_printed: false,
    secret_value_exposed: false,
    telegram_api_url_exposed: false,
    methods_called: [],
    mutation_calls: 0,
    messages_sent: 0,
  };

  const tokenInfo = loadTokenFromLocalFile();
  report.secret_boundary = {
    exists: tokenInfo.exists,
    key_count: tokenInfo.keyCount,
    length_class: tokenInfo.lengthClass,
    plausible_structure: tokenInfo.plausible,
    printed: false,
  };

  if (!tokenInfo.ok) {
    report.aborted = tokenInfo.error;
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  if (!args.apply) {
    report.note =
      'Dry-run only. Pass --apply and exact confirmation phrase to call Telegram Bot API read-only methods.';
    report.ready = true;
    console.log(JSON.stringify(report, null, 2));
    return;
  }

  if (!isIntake && !isDiscover) {
    report.aborted = 'confirmation_mismatch';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }

  let token = tokenInfo.value;
  tokenInfo.value = '';

  try {
    // 1) getMe — required for intake; optional for discovery (default once)
    const doGetMe = isIntake || !args.skipGetMe;
    if (doGetMe) {
      const meResp = await telegramReadonly('getMe', token);
      report.methods_called.push({ method: 'getMe', calls: 1, mutation: false });
      if (!meResp.data?.ok) {
        report.aborted = 'getMe_failed';
        report.getMe_http_status = meResp.httpStatus;
        console.log(JSON.stringify(report, null, 2));
        process.exitCode = 4;
        return;
      }
      const me = sanitizeGetMe(meResp.data.result);
      const nameCompare = namesMatchMaterially(me.first_name, REQUIRED_FIRST_NAME);
      report.bot_identity = {
        ...me,
        required_first_name: REQUIRED_FIRST_NAME,
        name_exact_match: nameCompare.exact,
        name_material_match: nameCompare.material,
        avatar_verification: 'SAFE_UNKNOWN',
      };
      if (
        !me.is_bot ||
        me.id !== REQUIRED_BOT_ID ||
        me.username !== REQUIRED_USERNAME ||
        !nameCompare.material
      ) {
        report.aborted = 'bot_identity_mismatch';
        console.log(JSON.stringify(report, null, 2));
        process.exitCode = 5;
        return;
      }
    } else {
      report.bot_identity = {
        skipped: true,
        note: 'getMe skipped by --skip-get-me; prior Phase 1B-C identity assumed',
      };
    }

    // 2) getWebhookInfo — exactly once
    const whResp = await telegramReadonly('getWebhookInfo', token);
    report.methods_called.push({
      method: 'getWebhookInfo',
      calls: 1,
      mutation: false,
    });
    if (!whResp.data?.ok) {
      report.aborted = 'getWebhookInfo_failed';
      console.log(JSON.stringify(report, null, 2));
      process.exitCode = 4;
      return;
    }
    const wh = sanitizeWebhookInfo(whResp.data.result);
    report.webhook_state = wh;
    if (wh.webhook_configured) {
      report.aborted = 'telegram_webhook_configured';
      report.chat_target = {
        verdict: 'TELEGRAM_CHAT_TARGET_BLOCKED',
        reason: 'webhook_configured_blocks_getUpdates',
      };
      console.log(JSON.stringify(report, null, 2));
      process.exitCode = 6;
      return;
    }

    // 3) getUpdates at most once, only if no webhook
    if (args.allowGetUpdates) {
      const upResp = await telegramReadonly('getUpdates', token, {
        limit: 10,
        timeout: 0,
      });
      report.methods_called.push({
        method: 'getUpdates',
        calls: 1,
        mutation: false,
        offset_supplied: false,
      });
      if (!upResp.data?.ok) {
        report.aborted = 'getUpdates_failed';
        console.log(JSON.stringify(report, null, 2));
        process.exitCode = 4;
        return;
      }
      report.chat_target = sanitizeUpdates(upResp.data.result, {
        requirePrivate: true,
        preferStart: isDiscover,
      });

      if (
        isDiscover &&
        report.chat_target.verdict === 'TELEGRAM_CHAT_TARGET_CONFIRMED' &&
        report.chat_target.selected_chat?.chat_id != null
      ) {
        const writeResult = writeLocalChatTarget(
          report.chat_target.selected_chat.chat_id,
        );
        report.local_target = {
          path: TARGET_PATH.replace(/\\/g, '/'),
          created: writeResult.created,
          conflict: writeResult.conflict,
          ok: writeResult.ok,
          personal_data_stored: false,
          token_stored: false,
          error: writeResult.error || null,
        };
        if (!writeResult.ok) {
          report.aborted = writeResult.conflict
            ? 'local_target_conflict'
            : 'local_target_write_failed';
          console.log(JSON.stringify(report, null, 2));
          process.exitCode = 7;
          return;
        }
      }
    } else {
      report.chat_target = {
        verdict: 'TELEGRAM_CHAT_TARGET_NOT_YET_AVAILABLE',
        reason: 'getUpdates_skipped',
      };
    }

    report.success = true;
  } finally {
    token = '';
  }

  const evidenceDir = isDiscoverFinal
    ? LOCAL_EVIDENCE_C0R2
    : isDiscover
      ? LOCAL_EVIDENCE_C0
      : LOCAL_EVIDENCE;
  mkdirSync(evidenceDir, { recursive: true });
  const outName = isDiscover
    ? 'telegram-chat-target-discovery-report.sanitized.json'
    : 'telegram-intake-report.sanitized.json';
  writeFileSync(resolve(evidenceDir, outName), JSON.stringify(report, null, 2), 'utf8');
  console.log(JSON.stringify(report, null, 2));
}

main().catch((err) => {
  console.error(
    JSON.stringify({
      runner: 'run-client-ops-telegram-intake',
      aborted: 'uncaught',
      error: err instanceof Error ? err.message.slice(0, 240) : String(err).slice(0, 240),
      secret_printed: false,
      telegram_api_url_exposed: false,
    }),
  );
  process.exitCode = 1;
});
