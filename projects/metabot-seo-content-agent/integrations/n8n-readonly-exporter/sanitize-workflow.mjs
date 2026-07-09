/**
 * Recursive n8n workflow JSON sanitizer.
 * Redacts credentials, tokens, webhook IDs, personal IDs, execution/pin data.
 */

export const MARKERS = Object.freeze({
  CREDENTIAL: 'REDACTED_CREDENTIAL',
  CREDENTIAL_ID: 'REDACTED_CREDENTIAL_ID',
  TOKEN: 'REDACTED_TOKEN',
  WEBHOOK_URL: 'REDACTED_WEBHOOK_URL',
  WEBHOOK_ID: 'REDACTED_WEBHOOK_ID',
  SHEET_ID: 'REDACTED_SHEET_ID',
  PRIVATE_DATA: 'REDACTED_PRIVATE_DATA',
  PERSONAL_ID: 'REDACTED_PERSONAL_ID',
  EXECUTION_DATA: 'REDACTED_EXECUTION_DATA',
  PINNED_DATA: 'REDACTED_PINNED_DATA',
});

const TELEGRAM_BOT_TOKEN_RE = /\b\d{8,10}:[A-Za-z0-9_-]{30,}\b/g;
const OPENAI_SK_RE = /\bsk-[A-Za-z0-9_-]{10,}\b/g;
const BEARER_RE = /\bBearer\s+[A-Za-z0-9._-]{10,}\b/gi;
const WEBHOOK_URL_RE = /https?:\/\/[^\s"'`]+?\/webhook[^\s"'`]*/gi;
const PRIVATE_URL_TOKEN_RE = /https?:\/\/[^\s"'`]*[?&](?:token|access_token|api_key|key)=[^\s"'`&]+/gi;
const GOOGLE_SHEET_ID_VALUE_RE = /^[a-zA-Z0-9_-]{20,}$/;

/** @type {ReadonlyArray<{ regex: RegExp, replace: (match: string, id: string) => string }>} */
const GOOGLE_SHEET_URL_PATTERNS = [
  {
    regex: /(?:https?:)?\/\/docs\.google\.com\/spreadsheets\/d\/([a-zA-Z0-9_-]+)/gi,
    replace: (match, id) => match.replace(id, MARKERS.SHEET_ID),
  },
  {
    regex: /\/spreadsheets\/d\/([a-zA-Z0-9_-]+)/gi,
    replace: (match, id) => match.replace(id, MARKERS.SHEET_ID),
  },
  {
    regex: /spreadsheets%2Fd%2F([a-zA-Z0-9_-]+)/gi,
    replace: (match, id) => match.replace(id, MARKERS.SHEET_ID),
  },
  {
    regex:
      /docs\.google\.com(?:\\\/|\/)+spreadsheets(?:\\\/|\/)+d(?:\\\/|\/)+([a-zA-Z0-9_-]+)/gi,
    replace: (match, id) => match.replace(id, MARKERS.SHEET_ID),
  },
];

/** @type {ReadonlySet<string>} */
const SENSITIVE_KEYS = new Set([
  'credentials',
  'credential',
  'credentialId',
  'credential_id',
  'credentialsId',
  'apiKey',
  'api_key',
  'accessToken',
  'access_token',
  'refreshToken',
  'refresh_token',
  'clientSecret',
  'client_secret',
  'authorization',
  'cookie',
  'cookies',
  'pinData',
  'executionData',
  'binary',
  'binaryData',
  'webhookId',
  'webhook_id',
  'chatId',
  'chat_id',
  'userId',
  'user_id',
  'telegramChatId',
  'telegramUserId',
  'botToken',
  'bot_token',
  'openRouterApiKey',
  'openrouter_api_key',
]);

/** @type {ReadonlySet<string>} */
const PERSONAL_ID_KEYS = new Set([
  'chat_id',
  'chatId',
  'user_id',
  'userId',
  'telegramChatId',
  'telegramUserId',
  'from_id',
  'fromId',
]);

/**
 * @typedef {Object} SanitizationStats
 * @property {number} credentialsRedacted
 * @property {number} tokensRedacted
 * @property {number} webhookUrlsRedacted
 * @property {number} webhookIdsRedacted
 * @property {number} sheetIdsRedacted
 * @property {number} personalIdsRedacted
 * @property {number} pinDataRemoved
 * @property {number} executionDataRemoved
 * @property {string[]} riskyPatternsRemaining
 * @property {string[]} reviewLabelsOnly
 */

/**
 * @returns {SanitizationStats}
 */
function createStats() {
  return {
    credentialsRedacted: 0,
    tokensRedacted: 0,
    webhookUrlsRedacted: 0,
    webhookIdsRedacted: 0,
    sheetIdsRedacted: 0,
    personalIdsRedacted: 0,
    pinDataRemoved: 0,
    executionDataRemoved: 0,
    riskyPatternsRemaining: [],
    reviewLabelsOnly: [],
  };
}

/**
 * @param {string} id
 * @returns {boolean}
 */
function isRedactionMarker(id) {
  return id === MARKERS.SHEET_ID || id.startsWith('REDACTED_');
}

/**
 * @param {string} text
 * @param {SanitizationStats} stats
 * @returns {string}
 */
function redactGoogleSheetUrls(text, stats) {
  let out = text;
  for (const { regex, replace } of GOOGLE_SHEET_URL_PATTERNS) {
    out = out.replace(regex, (match, id) => {
      if (isRedactionMarker(id)) return match;
      stats.sheetIdsRedacted += 1;
      return replace(match, id);
    });
  }
  return out;
}

/**
 * @param {unknown} value
 * @param {SanitizationStats} stats
 * @returns {unknown}
 */
function redactDocumentIdObject(value, stats) {
  if (!value || typeof value !== 'object' || Array.isArray(value)) return value;

  const obj = /** @type {Record<string, unknown>} */ ({ ...value });
  if (
    typeof obj.value === 'string' &&
    GOOGLE_SHEET_ID_VALUE_RE.test(obj.value) &&
    !isRedactionMarker(obj.value)
  ) {
    stats.sheetIdsRedacted += 1;
    obj.value = MARKERS.SHEET_ID;
  }

  return obj;
}

/**
 * @param {string} text
 * @param {SanitizationStats} stats
 * @returns {string}
 */
function scanString(text, stats) {
  if (typeof text !== 'string' || !text) return text;

  let out = text;
  const before = out;

  out = out.replace(TELEGRAM_BOT_TOKEN_RE, () => {
    stats.tokensRedacted += 1;
    return MARKERS.TOKEN;
  });
  out = out.replace(OPENAI_SK_RE, () => {
    stats.tokensRedacted += 1;
    return MARKERS.TOKEN;
  });
  out = out.replace(BEARER_RE, () => {
    stats.tokensRedacted += 1;
    return MARKERS.TOKEN;
  });
  out = out.replace(WEBHOOK_URL_RE, () => {
    stats.webhookUrlsRedacted += 1;
    return MARKERS.WEBHOOK_URL;
  });
  out = out.replace(PRIVATE_URL_TOKEN_RE, () => {
    stats.tokensRedacted += 1;
    return MARKERS.PRIVATE_DATA;
  });
  out = redactGoogleSheetUrls(out, stats);

  if (out !== before) {
    recordRemainingRiskyPatterns(out, stats);
  }

  return out;
}

/**
 * @param {string} text
 * @param {SanitizationStats} stats
 */
function recordRemainingRiskyPatterns(text, stats) {
  const blockerChecks = [
    { pattern: /\bsk-[A-Za-z0-9_-]{10,}\b/, label: 'sk- token pattern' },
    { pattern: /\bBearer\s+[A-Za-z0-9._-]{10,}\b/i, label: 'Bearer header value' },
    { pattern: /\bX-N8N-API-KEY\s*[:=]\s*\S+/i, label: 'X-N8N-API-KEY value' },
    {
      pattern: /"api_key"\s*:\s*"(?!REDACTED)[^"]{8,}"/i,
      label: 'api_key JSON field with value',
    },
    {
      pattern: /"access_token"\s*:\s*"(?!REDACTED)[^"]{8,}"/i,
      label: 'access_token JSON field with value',
    },
    {
      pattern: /"refresh_token"\s*:\s*"(?!REDACTED)[^"]{8,}"/i,
      label: 'refresh_token JSON field with value',
    },
    {
      pattern: /"client_secret"\s*:\s*"(?!REDACTED)[^"]{8,}"/i,
      label: 'client_secret JSON field with value',
    },
    {
      pattern: /"webhookId"\s*:\s*"(?!REDACTED_WEBHOOK_ID)[0-9a-f-]{8,}"/i,
      label: 'webhookId UUID value',
    },
    {
      pattern:
        /docs\.google\.com\/spreadsheets\/d\/(?!REDACTED_SHEET_ID)[a-zA-Z0-9_-]{10,}/i,
      label: 'Google Sheets document ID in URL',
    },
    {
      pattern:
        /"documentId"\s*:\s*\{[^}]*"value"\s*:\s*"(?!REDACTED_SHEET_ID)[a-zA-Z0-9_-]{20,}"/i,
      label: 'Google Sheets documentId value',
    },
    {
      pattern: /"chat_id"\s*:\s*"?-?\d{5,}"?/i,
      label: 'chat_id numeric value',
    },
    {
      pattern: /"user_id"\s*:\s*"?-?\d{5,}"?/i,
      label: 'user_id numeric value',
    },
    {
      pattern: /n8n\.ai-metacode\.com\/webhook[^\s"'`]*/i,
      label: 'production webhook URL',
    },
    { pattern: /\d{8,10}:[A-Za-z0-9_-]{20,}/, label: 'Telegram bot token pattern' },
    {
      pattern: /"credentials"\s*:\s*\{[^}]*"id"\s*:\s*"[^"]+"/i,
      label: 'inline credentials object with id',
    },
  ];

  const reviewLabelChecks = [
    { pattern: /\bwebhookId\b/i, label: 'webhookId reference' },
    { pattern: /\bchat_id\b/i, label: 'chat_id reference' },
    { pattern: /\buser_id\b/i, label: 'user_id reference' },
    { pattern: /"name"\s*:\s*"Authorization"/i, label: 'Authorization reference' },
    { pattern: /\bapi_key\b/i, label: 'api_key reference' },
    { pattern: /\baccess_token\b/i, label: 'access_token reference' },
    { pattern: /\brefresh_token\b/i, label: 'refresh_token reference' },
    { pattern: /\bclient_secret\b/i, label: 'client_secret reference' },
    { pattern: /\bcredential\b/i, label: 'credential reference' },
    {
      pattern: /docs\.google\.com\/spreadsheets\/d\/REDACTED_SHEET_ID/i,
      label: 'Google Sheets URL (redacted)',
    },
    {
      pattern: /docs\.google\.com\/spreadsheets/i,
      label: 'Google Sheets URL host',
    },
  ];

  for (const { pattern, label } of blockerChecks) {
    if (pattern.test(text) && !stats.riskyPatternsRemaining.includes(label)) {
      stats.riskyPatternsRemaining.push(label);
    }
  }

  for (const { pattern, label } of reviewLabelChecks) {
    if (stats.riskyPatternsRemaining.includes(label)) continue;
    if (pattern.test(text) && !stats.reviewLabelsOnly.includes(label)) {
      stats.reviewLabelsOnly.push(label);
    }
  }
}

/**
 * @param {string} key
 * @returns {string | null}
 */
function redactByKey(key) {
  const lower = key.toLowerCase();
  if (lower === 'credentials' || lower === 'credential') return MARKERS.CREDENTIAL;
  if (lower.includes('credentialid') || lower === 'credential_id') {
    return MARKERS.CREDENTIAL_ID;
  }
  if (lower === 'webhookid' || lower === 'webhook_id') return MARKERS.WEBHOOK_ID;
  if (lower === 'pindata') return MARKERS.PINNED_DATA;
  if (lower === 'executiondata') return MARKERS.EXECUTION_DATA;
  if (lower === 'binary' || lower === 'binarydata') return MARKERS.EXECUTION_DATA;
  if (
    lower.includes('apikey') ||
    lower.includes('token') ||
    lower === 'authorization' ||
    lower === 'cookie' ||
    lower === 'cookies' ||
    lower.includes('secret')
  ) {
    return MARKERS.TOKEN;
  }
  if (PERSONAL_ID_KEYS.has(key) || PERSONAL_ID_KEYS.has(lower)) {
    return MARKERS.PERSONAL_ID;
  }
  if (SENSITIVE_KEYS.has(key) || SENSITIVE_KEYS.has(lower)) {
    return MARKERS.PRIVATE_DATA;
  }
  return null;
}

/**
 * @param {unknown} value
 * @param {string | undefined} key
 * @param {SanitizationStats} stats
 * @returns {unknown}
 */
function sanitizeValue(value, key, stats) {
  if (value === null || value === undefined) return value;

  if (typeof value === 'string') {
    if (key) {
      const redacted = redactByKey(key);
      if (redacted) {
        if (redacted === MARKERS.CREDENTIAL) stats.credentialsRedacted += 1;
        else if (redacted === MARKERS.CREDENTIAL_ID) stats.credentialsRedacted += 1;
        else if (redacted === MARKERS.WEBHOOK_ID) stats.webhookIdsRedacted += 1;
        else if (redacted === MARKERS.PERSONAL_ID) stats.personalIdsRedacted += 1;
        else if (redacted === MARKERS.PINNED_DATA) stats.pinDataRemoved += 1;
        else if (redacted === MARKERS.EXECUTION_DATA) stats.executionDataRemoved += 1;
        else if (redacted === MARKERS.TOKEN) stats.tokensRedacted += 1;
        return redacted;
      }
    }
    return scanString(value, stats);
  }

  if (Array.isArray(value)) {
    return value.map((item, index) =>
      sanitizeValue(item, key ? `${key}[${index}]` : undefined, stats),
    );
  }

  if (typeof value === 'object') {
    /** @type {Record<string, unknown>} */
    const out = {};
    for (const [childKey, childValue] of Object.entries(
      /** @type {Record<string, unknown>} */ (value),
    )) {
      const forced = redactByKey(childKey);
      if (forced === MARKERS.PINNED_DATA) {
        stats.pinDataRemoved += 1;
        out[childKey] = forced;
        continue;
      }
      if (forced === MARKERS.EXECUTION_DATA) {
        stats.executionDataRemoved += 1;
        out[childKey] = forced;
        continue;
      }
      if (forced) {
        if (forced === MARKERS.CREDENTIAL || forced === MARKERS.CREDENTIAL_ID) {
          stats.credentialsRedacted += 1;
        } else if (forced === MARKERS.WEBHOOK_ID) {
          stats.webhookIdsRedacted += 1;
        } else if (forced === MARKERS.PERSONAL_ID) {
          stats.personalIdsRedacted += 1;
        } else if (forced === MARKERS.TOKEN) {
          stats.tokensRedacted += 1;
        }
        out[childKey] = forced;
        continue;
      }
      if (childKey === 'documentId') {
        out[childKey] = redactDocumentIdObject(
          sanitizeValue(childValue, childKey, stats),
          stats,
        );
        continue;
      }
      out[childKey] = sanitizeValue(childValue, childKey, stats);
    }
    return out;
  }

  return value;
}

/**
 * @param {unknown} workflow
 * @returns {{ sanitized: unknown, stats: SanitizationStats }}
 */
export function sanitizeWorkflow(workflow) {
  const stats = createStats();
  const sanitized = sanitizeValue(workflow, undefined, stats);

  const serialized = JSON.stringify(sanitized);
  recordRemainingRiskyPatterns(serialized, stats);

  return { sanitized, stats };
}

/**
 * Post-export safety scan on written evidence files.
 * @param {string} content
 * @returns {{ safe: boolean, findings: Array<{ pattern: string }> }}
 */
export function scanForObviousSecrets(content) {
  const checks = [
    { regex: /\bsk-[A-Za-z0-9_-]{10,}\b/, pattern: 'sk- API key pattern' },
    { regex: /\bBearer\s+[A-Za-z0-9._-]{10,}\b/i, pattern: 'Bearer token' },
    { regex: /\bAuthorization:\s*\S+/i, pattern: 'Authorization header value' },
    { regex: /\bX-N8N-API-KEY\b/i, pattern: 'X-N8N-API-KEY reference' },
    { regex: /\b\d{8,10}:[A-Za-z0-9_-]{30,}\b/, pattern: 'Telegram bot token pattern' },
    { regex: /"api_key"\s*:\s*"[^"]+"/i, pattern: 'api_key JSON field with value' },
    { regex: /"access_token"\s*:\s*"[^"]+"/i, pattern: 'access_token JSON field with value' },
    { regex: /"refresh_token"\s*:\s*"[^"]+"/i, pattern: 'refresh_token JSON field with value' },
    { regex: /"client_secret"\s*:\s*"[^"]+"/i, pattern: 'client_secret JSON field with value' },
    {
      regex: /"webhookId"\s*:\s*"[0-9a-f-]{8,}"/i,
      pattern: 'webhookId UUID value',
    },
    {
      regex:
        /docs\.google\.com\/spreadsheets\/d\/(?!REDACTED_SHEET_ID)[a-zA-Z0-9_-]{10,}/i,
      pattern: 'Google Sheets document ID in URL',
    },
    {
      regex:
        /"documentId"\s*:\s*\{[^}]*"value"\s*:\s*"(?!REDACTED_SHEET_ID)[a-zA-Z0-9_-]{20,}"/i,
      pattern: 'Google Sheets documentId value',
    },
    {
      regex: /"chat_id"\s*:\s*"?-?\d{5,}"?/i,
      pattern: 'chat_id numeric value',
    },
    {
      regex: /"user_id"\s*:\s*"?-?\d{5,}"?/i,
      pattern: 'user_id numeric value',
    },
    {
      regex: /n8n\.ai-metacode\.com\/webhook[^\s"'`]*/i,
      pattern: 'production webhook URL',
    },
    {
      regex: /"credentials"\s*:\s*\{[^}]*"id"\s*:\s*"[^"]+"/i,
      pattern: 'inline credentials object with id',
    },
  ];

  /** @type {Array<{ pattern: string }>} */
  const findings = [];
  for (const { regex, pattern } of checks) {
    if (regex.test(content)) {
      findings.push({ pattern });
    }
  }

  return { safe: findings.length === 0, findings };
}
