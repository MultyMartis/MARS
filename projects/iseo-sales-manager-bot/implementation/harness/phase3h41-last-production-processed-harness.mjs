/**
 * Phase 3H.4.1 — offline harness for iseo-last-production-processed-v1.0 resolver.
 * No PII. No hardcoded production display date assertions as source; verifies conversion dynamically.
 */
import assert from 'assert';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PROJECT = path.resolve(__dirname, '../..');
const OUT = path.join(PROJECT, 'evidence', 'phase3h4-1');
const PATCH = path.join(PROJECT, 'implementation', 'patches', 'Status.phase3h41.js');
fs.mkdirSync(OUT, { recursive: true });

const EPOCH = '2026-08-05T13:02:57.000Z';
const PROD_TS = '2026-08-05T14:22:55.186Z'; // expected Moscow 17:22
const SYNTH_TS = '2026-08-05T19:23:37.997Z'; // expected Moscow 22:23 — must never win

function formatMoscow(v) {
  if (v instanceof Date) {
    if (Number.isNaN(v.getTime())) return '';
    return formatMoscow(v.toISOString());
  }
  const s = String(v || '').trim();
  if (!s) return '';
  const d = new Date(s);
  if (Number.isNaN(d.getTime())) return '';
  const parts = new Intl.DateTimeFormat('ru-RU', {
    timeZone: 'Europe/Moscow',
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
  }).formatToParts(d);
  const get = (t) => parts.find((p) => p.type === t)?.value || '';
  return `${get('day')}.${get('month')}.${get('year')} ${get('hour')}:${get('minute')} МСК`;
}

function isTestishId(id) {
  const s = String(id || '').toLowerCase();
  return /synth|synthetic|probe_|test_|msg_synth|fixture|archive.?test|probable_test/.test(s);
}

function isExcludedLeadHint(row) {
  if (!row || typeof row !== 'object') return true;
  if (isTestishId(row.lead_id || row.id)) return true;
  if (String(row.is_probable_test).toLowerCase() === 'true') return true;
  if (String(row.is_real_lead).toLowerCase() === 'false') return true;
  const arch = String(row.archive_state || '').toLowerCase();
  if (/test|synth|fixture/.test(arch)) return true;
  return false;
}

function isExcludedEventHint(ev) {
  if (!ev || typeof ev !== 'object') return true;
  const t = String(ev.event_type || ev.type || '').toLowerCase();
  if (!t) return true;
  if (/delivery|reminder|profile|generated.?reply|telegram|technical|synth|test|fixture/.test(t)) return true;
  if (/spam|pending/.test(t) && !/processed/.test(t)) return true;
  if (!/processed/.test(t)) return true;
  if (isTestishId(ev.lead_id)) return true;
  return false;
}

function parseTs(v) {
  if (v instanceof Date) return Number.isNaN(v.getTime()) ? 0 : v.getTime();
  const s = String(v || '').trim();
  if (!s) return 0;
  const ms = Date.parse(s);
  return Number.isFinite(ms) ? ms : 0;
}

function resolveLastProcessed(j) {
  const m = j.config_map || {};
  const CONTRACT = 'iseo-last-production-processed-v1.0';

  function resolveFromEventHints() {
    const rows = Array.isArray(j.lead_events) ? j.lead_events : (Array.isArray(j.events) ? j.events : []);
    const epochMs = parseTs(m.production_stats_epoch);
    const candidates = [];
    for (const ev of rows) {
      if (isExcludedEventHint(ev)) continue;
      const ts = ev.ts || ev.event_at || ev.created_at || '';
      const ms = parseTs(ts);
      if (!ms) continue;
      if (epochMs && ms < epochMs) continue;
      candidates.push({ ts, ms, source: 'lead_events_hint' });
    }
    candidates.sort((a, b) => b.ms - a.ms);
    return candidates[0] || null;
  }

  function resolveFromLeadsHints() {
    const rows = Array.isArray(j.leads_rows) ? j.leads_rows : (Array.isArray(j.leads) ? j.leads : []);
    const epochMs = parseTs(m.production_stats_epoch);
    const candidates = [];
    for (const row of rows) {
      if (isExcludedLeadHint(row)) continue;
      if (String(row.lifecycle_status || row.status || '').toLowerCase() !== 'processed') continue;
      const ts = row.lifecycle_changed_at || row.processed_at || row.status_changed_at || '';
      const ms = parseTs(ts);
      if (!ms) continue;
      if (epochMs && ms < epochMs) continue;
      candidates.push({ ts, ms, source: 'leads_hint' });
    }
    candidates.sort((a, b) => b.ms - a.ms);
    return candidates[0] || null;
  }

  const fromEvents = resolveFromEventHints();
  if (fromEvents) return { ts: fromEvents.ts, source: fromEvents.source, contract: CONTRACT };
  const fromLeads = resolveFromLeadsHints();
  if (fromLeads) return { ts: fromLeads.ts, source: fromLeads.source, contract: CONTRACT };

  const prodAt = String(m.last_production_processed_at || '').trim();
  if (prodAt) {
    const id = m.last_production_processed_lead_id || '';
    if (!isTestishId(id) && parseTs(prodAt)) {
      return { ts: prodAt, source: 'last_production_processed_at', contract: CONTRACT };
    }
  }

  const processedAt = String(m.last_processed_at || '').trim();
  if (processedAt && parseTs(processedAt)) {
    const id = m.last_processed_lead_id || '';
    const epochMs = parseTs(m.production_stats_epoch);
    const tsMs = parseTs(processedAt);
    if (!isTestishId(id) && (!epochMs || tsMs >= epochMs)) {
      return { ts: processedAt, source: 'last_processed_at', contract: CONTRACT };
    }
  }
  return { ts: '', source: 'none', contract: CONTRACT };
}

function display(j) {
  const r = resolveLastProcessed(j);
  return formatMoscow(r.ts) || 'нет данных';
}

const results = [];
function check(name, fn) {
  try {
    fn();
    results.push({ name, pass: true });
  } catch (e) {
    results.push({ name, pass: false, error: String(e && e.message ? e.message : e) });
  }
}

const baseMap = {
  environment: 'production',
  production_stats_epoch: EPOCH,
  last_lead_success_at: SYNTH_TS,
  last_success_at: SYNTH_TS,
};

check('1 Valid ISO UTC → Moscow', () => {
  const out = formatMoscow(PROD_TS);
  assert.ok(out.includes('17:22'));
  assert.ok(out.includes('05.08.2026'));
  assert.ok(out.includes('МСК'));
});

check('2 Valid Date object converts', () => {
  const out = formatMoscow(new Date(PROD_TS));
  assert.ok(out.includes('17:22'));
});

check('3 LEAD_EVENTS processed wins', () => {
  const out = display({
    config_map: { ...baseMap, last_production_processed_at: '2026-08-05T10:00:00.000Z' },
    lead_events: [{ event_type: 'status_processed', ts: PROD_TS, lead_id: 'lead_prod_a' }],
  });
  assert.ok(out.includes('17:22'));
});

check('4 LEADS processed_at fallback', () => {
  const out = display({
    config_map: { ...baseMap, last_production_processed_at: '' },
    leads_rows: [{
      lead_id: 'lead_prod_a',
      lifecycle_status: 'processed',
      lifecycle_changed_at: PROD_TS,
      is_real_lead: 'true',
      is_probable_test: 'false',
      archive_state: 'active',
      production_generation: 'v2',
    }],
  });
  assert.ok(out.includes('17:22'));
});

check('5 CONFIG cache fallback', () => {
  const out = display({
    config_map: {
      ...baseMap,
      last_production_processed_at: PROD_TS,
      last_production_processed_lead_id: 'lead_prod_a',
    },
  });
  assert.ok(out.includes('17:22'));
});

check('6 Test event excluded', () => {
  const out = display({
    config_map: { ...baseMap },
    lead_events: [{ event_type: 'test_processed', ts: SYNTH_TS, lead_id: 'lead_test_1' }],
  });
  assert.strictEqual(out, 'нет данных');
});

check('7 Synthetic event excluded', () => {
  const out = display({
    config_map: { ...baseMap },
    lead_events: [{ event_type: 'processed', ts: SYNTH_TS, lead_id: 'msg_synth_3g11d_t1_x' }],
  });
  assert.strictEqual(out, 'нет данных');
});

check('8 Archive test event excluded', () => {
  const out = display({
    config_map: { ...baseMap },
    leads_rows: [{
      lead_id: 'lead_arch',
      lifecycle_status: 'processed',
      lifecycle_changed_at: SYNTH_TS,
      archive_state: 'archive_test',
      is_real_lead: 'true',
      is_probable_test: 'false',
    }],
  });
  assert.strictEqual(out, 'нет данных');
});

check('9 Pre-epoch event excluded', () => {
  const out = display({
    config_map: { ...baseMap },
    lead_events: [{ event_type: 'processed', ts: '2026-08-04T10:00:00.000Z', lead_id: 'lead_old' }],
  });
  assert.strictEqual(out, 'нет данных');
});

check('10 Delivery event excluded', () => {
  const out = display({
    config_map: { ...baseMap },
    lead_events: [{ event_type: 'telegram_delivery', ts: SYNTH_TS, lead_id: 'lead_prod_a' }],
  });
  assert.strictEqual(out, 'нет данных');
});

check('11 Reminder event excluded', () => {
  const out = display({
    config_map: { ...baseMap },
    lead_events: [{ event_type: 'reminder_sent', ts: SYNTH_TS, lead_id: 'lead_prod_a' }],
  });
  assert.strictEqual(out, 'нет данных');
});

check('12 Spam transition excluded', () => {
  const out = display({
    config_map: { ...baseMap },
    lead_events: [{ event_type: 'marked_spam', ts: SYNTH_TS, lead_id: 'lead_prod_a' }],
  });
  assert.strictEqual(out, 'нет данных');
});

check('13 Pending transition excluded', () => {
  const out = display({
    config_map: { ...baseMap },
    lead_events: [{ event_type: 'status_pending', ts: SYNTH_TS, lead_id: 'lead_prod_a' }],
  });
  assert.strictEqual(out, 'нет данных');
});

check('14 Invalid timestamp → no value', () => {
  const out = display({
    config_map: {
      ...baseMap,
      last_production_processed_at: 'not-a-date',
      last_production_processed_lead_id: 'lead_prod_a',
    },
  });
  assert.strictEqual(out, 'нет данных');
});

check('15 Missing value → нет данных', () => {
  const out = display({ config_map: { ...baseMap, last_production_processed_at: '' } });
  assert.strictEqual(out, 'нет данных');
});

check('16 Later production processed replaces earlier', () => {
  const later = '2026-08-06T10:00:00.000Z';
  const out = display({
    config_map: { ...baseMap },
    lead_events: [
      { event_type: 'processed', ts: PROD_TS, lead_id: 'lead_a' },
      { event_type: 'processed', ts: later, lead_id: 'lead_b' },
    ],
  });
  assert.ok(out.includes('13:00') || out.includes('10:00') || out.includes('06.08.2026'));
  assert.ok(!out.includes('17:22'));
});

check('17 Duplicate callback does not invent later false ts', () => {
  const out = display({
    config_map: { ...baseMap },
    lead_events: [
      { event_type: 'processed', ts: PROD_TS, lead_id: 'lead_a' },
      { event_type: 'processed', ts: PROD_TS, lead_id: 'lead_a' },
    ],
  });
  assert.ok(out.includes('17:22'));
});

check('18 Timezone Europe/Moscow', () => {
  const out = formatMoscow(PROD_TS);
  assert.ok(out.endsWith('МСК'));
});

check('19 No hardcoded display date in Status patch', () => {
  const code = fs.readFileSync(PATCH, 'utf8');
  assert.ok(!code.includes('05.08.2026'));
  assert.ok(!code.includes('17:22'));
  assert.ok(!code.includes('lead_19fd'));
});

check('20 No hardcoded lead identity in Status patch', () => {
  const code = fs.readFileSync(PATCH, 'utf8');
  assert.ok(!/lead_[0-9a-f]{8,}/i.test(code));
});

check('21 Synthetic CONFIG stamp ignored when production empty', () => {
  const out = display({
    config_map: {
      ...baseMap,
      last_production_processed_at: '',
      last_lead_success_at: SYNTH_TS,
    },
  });
  assert.strictEqual(out, 'нет данных');
  assert.ok(!out.includes('22:23'));
});

check('22 Empty string CONFIG treated as missing', () => {
  const r = resolveLastProcessed({
    config_map: { ...baseMap, last_production_processed_at: '   ' },
  });
  assert.strictEqual(r.source, 'none');
});

check('23 Status patch node --check syntax', () => {
  const code = fs.readFileSync(PATCH, 'utf8');
  // wrap as module-ish eval without n8n globals by parsing only
  new Function('const $input={first:()=>({json:{config_map:{environment:"production"}}})}; ' + code);
});

const passed = results.filter((r) => r.pass).length;
const failed = results.filter((r) => !r.pass);
const summary = {
  harness: 'phase3h41-last-production-processed',
  contract: 'iseo-last-production-processed-v1.0',
  total: results.length,
  passed,
  failed: failed.length,
  results,
};
fs.writeFileSync(path.join(OUT, 'HARNESS-RESULTS-RAW.json'), JSON.stringify(summary, null, 2));
console.log(JSON.stringify(summary, null, 2));
if (failed.length) process.exit(1);

