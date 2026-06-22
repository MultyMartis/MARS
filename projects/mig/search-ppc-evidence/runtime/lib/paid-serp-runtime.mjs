import { loadJson, writeJson, nowIso, localTimestampParts, isYabsAdUrl, extractDomain } from './utils.mjs';

const REQUIRED_SESSION_FIELDS = [
  'project_id',
  'manifest_path',
  'lifecycle_stage',
  'lifecycle_action',
  'query_set',
  'region',
  'search_engine',
  'device_profile',
  'timezone',
  'allowed_local_collection_windows',
  'requested_date',
  'captcha_policy',
  'stop_policy',
  'capture_policy',
  'output_path',
];

export function validateSessionConfig(config) {
  const missing = REQUIRED_SESSION_FIELDS.filter((f) => config[f] == null || config[f] === '');
  return { valid: missing.length === 0, missing };
}

export function parsePaidSerpCapture(serpJson, { sessionId, projectId, queryId }) {
  const ts = serpJson.timestamp || nowIso();
  const tz = serpJson.timezone || 'UTC';
  const local = localTimestampParts(new Date(ts), tz);

  const captcha = serpJson.captcha_status;
  if (captcha && captcha !== 'none') {
    return {
      observation_state: captcha === 'blocked' ? 'CAPTCHA' : 'SESSION STOPPED',
      ads: [],
      organic_kept_separate: true,
      degraded: true,
    };
  }

  const paidFromField = (serpJson.visible_ads || []).map((ad, i) => mapAd(ad, i, 'top'));
  const paidFromOrganic = (serpJson.organic_results || [])
    .filter((r) => isYabsAdUrl(r.url))
    .map((ad, i) => mapAd(ad, i, 'top'));

  const ads = paidFromField.length ? paidFromField : paidFromOrganic;
  const organicOnly = (serpJson.organic_results || []).filter((r) => !isYabsAdUrl(r.url));

  return {
    observation_state: ads.length ? 'ADS OBSERVED' : 'NO ADS OBSERVED',
    ads: ads.map((a) => ({
      ...a,
      session_id: sessionId,
      project_id: projectId,
      query_id: queryId,
      query: serpJson.query,
      observed_timestamp: ts,
      timezone: tz,
      local_date: local.local_date,
      local_time: local.local_time,
      weekday: local.weekday,
      region: serpJson.region,
      device: serpJson.device,
      evidence_type: 'paid_serp',
      fact_vs_inference: 'observed_fact',
    })),
    organic_results: organicOnly,
    organic_kept_separate: true,
    degraded: false,
    no_ads_scope: ads.length ? null : {
      query: serpJson.query,
      timestamp: ts,
      region: serpJson.region,
      device: serpJson.device,
      note: 'NO ADS OBSERVED applies only to this query/timestamp/region/device — not market-wide',
    },
  };
}

function mapAd(ad, index, blockType) {
  return {
    observation_id: `ad-${index + 1}`,
    block_type: blockType,
    position: index + 1,
    advertiser_display_name: ad.path_text || extractDomain(ad.url) || null,
    domain: extractDomain(ad.url),
    headline: ad.title,
    text: ad.description || null,
    sitelinks: ad.sitelinks || [],
    displayed_url: ad.path_text || null,
    destination_url: ad.url,
    extraction_confidence: ad.url ? 'medium' : 'low',
    observed_fact: true,
  };
}

export function runPaidSerpSession({ sessionConfig, fixturePaths, receipt }) {
  const validation = validateSessionConfig(sessionConfig);
  if (!validation.valid) {
    return { ok: false, blockers: validation.missing.map((m) => `missing session field: ${m}`) };
  }

  const sessionId = sessionConfig.session_id || `paid-serp-${Date.now()}`;
  const results = [];
  let degraded = false;

  for (const fp of fixturePaths || []) {
    const serpJson = loadJson(fp);
    const parsed = parsePaidSerpCapture(serpJson, {
      sessionId,
      projectId: sessionConfig.project_id,
      queryId: serpJson.query_id || fp,
    });
    if (parsed.degraded) degraded = true;
    results.push({ fixture: fp, ...parsed });
  }

  const summary = {
    schema_version: '1.0.0',
    session_id: sessionId,
    mode: 'PAID SERP — BUSINESS HOURS',
    project_id: sessionConfig.project_id,
    generated_at: nowIso(),
    query_count: results.length,
    ads_observed: results.filter((r) => r.observation_state === 'ADS OBSERVED').length,
    no_ads_observed: results.filter((r) => r.observation_state === 'NO ADS OBSERVED').length,
    captcha_or_interrupted: results.filter((r) => ['CAPTCHA', 'SESSION STOPPED', 'PAGE LOAD FAILURE'].includes(r.observation_state)).length,
    collection_status: degraded ? 'COLLECTION DEGRADED' : 'COMPLETE',
    results,
    execution_receipt_id: receipt?.receipt_id || null,
  };

  writeJson(`${sessionConfig.output_path}/session-summary.json`, summary);
  return { ok: true, summary, session_path: `${sessionConfig.output_path}/session-summary.json` };
}
