import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

export const RUNTIME_VERSION = 'wave2-mig-evidence-v1';

export const SOURCE_CLASSES = [
  'OPERATOR PROVIDED KEYWORDS',
  'WORDSTAT EXPORT',
  'HISTORICAL CAMPAIGN',
  'SEARCH TERM REPORT',
  'ORGANIC SERP',
  'PAID SERP',
  'COMPETITOR LANDING',
  'BUSINESS INTAKE',
  'MANUAL SEED',
  'SYNTHETIC / TEST',
];

export const QUERY_OBSERVATION_STATES = [
  'ADS OBSERVED',
  'NO ADS OBSERVED',
  'CAPTCHA',
  'PAGE LOAD FAILURE',
  'REGION UNCONFIRMED',
  'LAYOUT UNPARSED',
  'SESSION STOPPED',
  'SAFE UNKNOWN',
];

export const BUSINESS_HOURS_STATUSES = [
  'WITHIN APPROVED BUSINESS-HOURS WINDOW',
  'OUTSIDE APPROVED WINDOW',
  'APPROVED EXCEPTION',
  'TIMEZONE UNRESOLVED',
  'WINDOW NOT CONFIGURED',
];

export const EVIDENCE_READINESS = [
  'MIG EVIDENCE READY',
  'MIG EVIDENCE PARTIAL',
  'MIG EVIDENCE BLOCKED',
  'STALE — RECOLLECTION REQUIRED',
];

export function loadJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

export function writeJson(filePath, data) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, `${JSON.stringify(data, null, 2)}\n`, 'utf8');
}

export function sha256Buffer(buf) {
  return crypto.createHash('sha256').update(buf).digest('hex');
}

export function sha256File(filePath) {
  if (!filePath || !fs.existsSync(filePath)) return null;
  return sha256Buffer(fs.readFileSync(filePath));
}

export function sha256Text(text) {
  return sha256Buffer(Buffer.from(String(text), 'utf8'));
}

export function stablePhraseId(normalizedQuery, region = '') {
  return sha256Text(`${normalizedQuery}|${region}`).slice(0, 16);
}

export function normalizeQuery(raw) {
  if (!raw) return '';
  return String(raw)
    .normalize('NFC')
    .toLowerCase()
    .replace(/\s+/g, ' ')
    .trim();
}

export function extractDomain(url) {
  if (!url) return null;
  try {
    const u = new URL(url.startsWith('http') ? url : `https://${url}`);
    return u.hostname.replace(/^www\./, '');
  } catch {
    return null;
  }
}

export function isYabsAdUrl(url) {
  return typeof url === 'string' && url.includes('yabs.yandex');
}

export function nowIso() {
  return new Date().toISOString();
}

export function localTimestampParts(date, timezone) {
  try {
    const fmt = new Intl.DateTimeFormat('en-GB', {
      timeZone: timezone,
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
      weekday: 'long',
      hour12: false,
    });
    const parts = Object.fromEntries(fmt.formatToParts(date).map((p) => [p.type, p.value]));
    return {
      local_date: `${parts.year}-${parts.month}-${parts.day}`,
      local_time: `${parts.hour}:${parts.minute}:${parts.second}`,
      weekday: parts.weekday,
      timezone,
    };
  } catch {
    return { local_date: null, local_time: null, weekday: null, timezone };
  }
}
