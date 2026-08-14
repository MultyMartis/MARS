/**
 * iseo-sheets-429-retry-v1.0
 *
 * Bounded retry for reminder-critical Google Sheets reads.
 * Pure helper: no n8n, no PII, no mutations.
 *
 * Live n8n Google Sheets nodes cannot vary waitBetweenTries per attempt.
 * This helper implements the logical contract (5s / 15s / 30s + Retry-After).
 * Admin.dev mirrors the bound with native retryOnFail (see SHEETS-429-RETRY-CONTRACT-v1.md).
 */

export const SHEETS_429_RETRY_CONTRACT = 'iseo-sheets-429-retry-v1.0';
export const MAX_ATTEMPTS = 4;
/** Milliseconds to wait BEFORE attempts 2, 3, 4 (attempt 1 is immediate). */
export const DEFAULT_BACKOFF_MS = [5000, 15000, 30000];
export const MAX_RETRY_AFTER_MS = 120000;
export const MIN_RETRY_AFTER_MS = 1000;

export class SheetsReadError extends Error {
  constructor(fields = {}) {
    super(fields.message || 'sheets_read_error');
    this.name = 'SheetsReadError';
    this.httpStatus = fields.httpStatus ?? null;
    this.errorClass = fields.errorClass || 'SHEETS_ERROR';
    this.stage = fields.stage || null;
    this.retryable = fields.retryable === true;
    this.retryAfterMs = fields.retryAfterMs ?? null;
    this.attempt = fields.attempt ?? null;
    this.attempts = fields.attempts ?? null;
    this.detailsSafe = fields.detailsSafe || '';
  }
}

export function parseRetryAfterMs(value) {
  if (value == null || value === '') return null;
  if (typeof value === 'number' && Number.isFinite(value)) {
    const ms = value > 1000 ? value : value * 1000;
    if (ms < MIN_RETRY_AFTER_MS || ms > MAX_RETRY_AFTER_MS) return null;
    return Math.round(ms);
  }
  const s = String(value).trim();
  if (!s) return null;
  if (/^\d+(\.\d+)?$/.test(s)) {
    const sec = Number(s);
    if (!Number.isFinite(sec)) return null;
    const ms = sec * 1000;
    if (ms < MIN_RETRY_AFTER_MS || ms > MAX_RETRY_AFTER_MS) return null;
    return Math.round(ms);
  }
  const asDate = Date.parse(s);
  if (!Number.isNaN(asDate)) {
    const ms = asDate - Date.now();
    if (ms < MIN_RETRY_AFTER_MS || ms > MAX_RETRY_AFTER_MS) return null;
    return ms;
  }
  return null;
}

export function classifySheetsError(err, stage = null) {
  if (err instanceof SheetsReadError) {
    if (stage && !err.stage) err.stage = stage;
    return err;
  }
  const http = Number(err?.httpStatus || err?.httpCode || err?.status || err?.code || 0) || null;
  const msg = String(err?.message || err?.description || err || '');
  const name = String(err?.name || '');
  const retryAfterMs = parseRetryAfterMs(
    err?.retryAfterMs || err?.retryAfter || err?.headers?.['retry-after'] || err?.headers?.['Retry-After'],
  );

  if (http === 429 || /quota|rate.?limit|RESOURCE_EXHAUSTED|userRateLimitExceeded|too many requests/i.test(msg)) {
    return new SheetsReadError({
      message: 'sheets_http_429',
      httpStatus: 429,
      errorClass: 'SHEETS_429',
      stage,
      retryable: true,
      retryAfterMs,
      detailsSafe: 'лимит Google Sheets API',
    });
  }
  if (http === 401 || http === 403 || /invalid.?grant|unauthorized|insufficient.?permission|auth/i.test(msg + name)) {
    return new SheetsReadError({
      message: 'sheets_credentials',
      httpStatus: http,
      errorClass: 'SHEETS_CREDENTIALS',
      stage,
      retryable: false,
      detailsSafe: 'ошибка доступа к таблице',
    });
  }
  if (/schema|missing.?column|unknown.?sheet|Unable to parse range|sheet.*not found/i.test(msg)) {
    return new SheetsReadError({
      message: 'sheets_schema',
      httpStatus: http,
      errorClass: 'SHEETS_SCHEMA',
      stage,
      retryable: false,
      detailsSafe: 'ошибка схемы таблицы',
    });
  }
  if (/malformed|unexpected token|json/i.test(msg) && http !== 429) {
    return new SheetsReadError({
      message: 'sheets_malformed',
      httpStatus: http,
      errorClass: 'SHEETS_MALFORMED',
      stage,
      retryable: false,
      detailsSafe: 'некорректный ответ таблицы',
    });
  }
  return new SheetsReadError({
    message: 'sheets_permanent',
    httpStatus: http,
    errorClass: 'SHEETS_PERMANENT',
    stage,
    retryable: false,
    detailsSafe: 'ошибка чтения таблицы',
  });
}

export function backoffBeforeAttempt(attemptNumber, classified, policy = {}) {
  if (attemptNumber <= 1) return 0;
  const seq = policy.backoffMs || DEFAULT_BACKOFF_MS;
  const idx = attemptNumber - 2;
  let wait = seq[Math.min(idx, seq.length - 1)] ?? 30000;
  if (classified?.errorClass === 'SHEETS_429' && classified.retryAfterMs != null) {
    wait = classified.retryAfterMs;
  }
  const cap = policy.maxBackoffMs ?? MAX_RETRY_AFTER_MS;
  return Math.max(0, Math.min(wait, cap));
}

/**
 * Retry a single logical read. Does not restart a larger workflow.
 * @param {() => Promise<any>} readFn
 * @param {{ stage?: string, maxAttempts?: number, sleep?: (ms:number)=>Promise<void>, now?: ()=>number }} opts
 */
export async function readWith429Retry(readFn, opts = {}) {
  const stage = opts.stage || 'UNKNOWN';
  const maxAttempts = opts.maxAttempts ?? MAX_ATTEMPTS;
  const sleep = opts.sleep || ((ms) => new Promise((r) => setTimeout(r, ms)));
  let last = null;
  const delays = [];
  for (let attempt = 1; attempt <= maxAttempts; attempt += 1) {
    const wait = backoffBeforeAttempt(attempt, last, opts);
    if (wait > 0) {
      delays.push(wait);
      await sleep(wait);
    }
    try {
      const value = await readFn({ attempt, stage });
      return {
        ok: true,
        value,
        attempt,
        attempts: attempt,
        retries: attempt - 1,
        delaysMs: delays,
        stage,
        contract: SHEETS_429_RETRY_CONTRACT,
      };
    } catch (err) {
      last = classifySheetsError(err, stage);
      last.attempt = attempt;
      last.attempts = attempt;
      if (!last.retryable || last.errorClass !== 'SHEETS_429') {
        last.attempts = attempt;
        throw last;
      }
      if (attempt >= maxAttempts) {
        last.attempts = attempt;
        last.message = stage === 'ACCESS_CONTROL' ? 'ERROR_SHEETS_429_ACCESS' : `ERROR_SHEETS_429_${stage}`;
        throw last;
      }
    }
  }
  throw last || new SheetsReadError({ errorClass: 'SHEETS_429', stage, retryable: true });
}

export function decisionForSheetsError(err) {
  const c = classifySheetsError(err, err?.stage);
  if (c.errorClass === 'SHEETS_429' && c.stage === 'ACCESS_CONTROL') return 'ERROR_SHEETS_429_ACCESS';
  if (c.errorClass === 'SHEETS_429') return `ERROR_SHEETS_429_${c.stage || 'READ'}`;
  return 'ERROR';
}

export function errorObservability(err, extra = {}) {
  const c = classifySheetsError(err, extra.stage || err?.stage);
  const decision = extra.decision || decisionForSheetsError(c);
  return {
    last_evaluation_at: extra.nowIso || new Date().toISOString(),
    last_decision: 'ERROR',
    last_error_class: c.errorClass,
    last_error_stage: c.stage || extra.stage || '',
    last_error_at: extra.nowIso || new Date().toISOString(),
    last_error_safe: c.detailsSafe || 'ошибка чтения таблицы',
    retry_attempts: c.attempts != null ? c.attempts : extra.retryAttempts ?? 0,
    business_date: extra.businessDate || '',
    pending_count: extra.pendingCount != null ? extra.pendingCount : 'not_computed',
    reminder_decision: decision,
    reminder_send: false,
    reminder_mark_window_complete: false,
    last_successful_send: extra.lastSuccessfulSend || '',
    sent_date: '',
    sent_recipient_count: '',
  };
}

export function formatReminderErrorStatusLines(obs) {
  const stageLabel = {
    ACCESS_CONTROL: 'ACCESS_CONTROL',
    CLEAN: 'CLEAN',
    CONFIG: 'CONFIG',
    REMINDER_DELIVERIES: 'REMINDER_DELIVERIES',
  }[String(obs.last_error_stage || '')] || (obs.last_error_stage || 'не подтверждено');
  const reason = obs.last_error_class === 'SHEETS_429'
    ? 'лимит Google Sheets API'
    : (obs.last_error_safe || 'ошибка чтения таблицы');
  return {
    decisionLine: 'Ошибка',
    stageLine: stageLabel,
    reasonLine: reason,
    retriesLine: String(obs.retry_attempts ?? 0),
  };
}
