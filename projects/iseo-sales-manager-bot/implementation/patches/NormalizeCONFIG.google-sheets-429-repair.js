// Phase Google Sheets 429 repair — Normalize CONFIG + cache (Operational.dev)
// SYNC: implementation/patches/NormalizeCONFIG.google-sheets-429-repair.js

const TTL_MS = 5 * 60 * 1000;
const STALE_MAX_MS = 24 * 60 * 60 * 1000;
const sd = $getWorkflowStaticData('global');
const now = Date.now();

let rows = $input.all().map((i) => i.json).filter((r) => r && r.key != null);

const cache = sd.configSheetRows;
const fetchedAt = Number(sd.configSheetFetchedAt || 0);
const cacheFresh = Array.isArray(cache) && cache.length && now - fetchedAt < TTL_MS;
const cacheStaleOk =
  Array.isArray(cache) && cache.length && now - fetchedAt < STALE_MAX_MS;

if (!rows.length && cacheFresh) {
  rows = cache.map((r) => ({ key: r.key, value: r.value }));
} else if (!rows.length && cacheStaleOk) {
  rows = cache.map((r) => ({ key: r.key, value: r.value }));
  sd.configCacheStaleUsedAt = now;
}

if (!rows.length) {
  throw new Error('CONFIG unavailable: live read empty and no usable cache');
}

if (rows.length && rows.some((r) => r.key != null)) {
  sd.configSheetRows = rows
    .filter((r) => r.key != null)
    .map((r) => ({ key: String(r.key), value: r.value }));
  sd.configSheetFetchedAt = now;
}

const map = {};
for (const r of rows) {
  if (r.key != null) map[String(r.key)] = r.value;
}
const bool = (v, d = false) => {
  if (v === true || v === 'true' || v === '1') return true;
  if (v === false || v === 'false' || v === '0') return false;
  return d;
};
const lead = $('Parse Lead').first().json;
const config = {
  ai_enabled: bool(map.ai_enabled, false),
  ai_model: map.ai_model || '',
  environment: map.environment || 'dev',
  telegram_manager_chat_id: String(map.telegram_manager_chat_id || ''),
  telegram_admin_chat_id: String(map.telegram_admin_chat_id || ''),
  admin_user_ids: String(map.admin_user_ids || ''),
  message_format_version: map.message_format_version || 'sm-msg-v2.1',
  reply_template_version: map.reply_template_version || 'sm-reply-v1',
  parser_version: map.parser_version || 'sm-parser-v3.2',
  health_ai_probe_enabled: bool(map.health_ai_probe_enabled, false),
  dedupe_contact_window_days: Number(map.dedupe_contact_window_days || 365),
  gmail_query_limit: Number(map.gmail_query_limit || 10),
  stats_days_default: Number(map.stats_days_default || 7),
};
return [
  {
    json: {
      ...lead,
      config,
      ai_enabled: config.ai_enabled,
      telegram_manager_chat_id: config.telegram_manager_chat_id,
    },
  },
];
