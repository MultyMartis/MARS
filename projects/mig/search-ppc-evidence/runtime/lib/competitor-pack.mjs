import { writeJson, nowIso } from './utils.mjs';
import { buildAdvertiserRegistry } from './competitor-registry.mjs';

export function buildCompetitorEvidencePack({ sessionSummary, advertiserRegistry, landingEvidence, limitations }) {
  const pack = {
    schema_version: '1.0.0',
    lifecycle_stage: 'SPPC-11',
    generated_at: nowIso(),
    session_summary: {
      session_id: sessionSummary.session_id,
      query_count: sessionSummary.query_count,
      collection_period: sessionSummary.generated_at,
      mode: sessionSummary.mode,
    },
    query_coverage: (sessionSummary.results || []).map((r) => ({
      query: r.no_ads_scope?.query || r.ads?.[0]?.query,
      observation_state: r.observation_state,
    })),
    observed_advertisers: advertiserRegistry?.advertisers || [],
    observed_ads: (sessionSummary.results || []).flatMap((r) => r.ads || []),
    offer_patterns: extractOfferPatterns(sessionSummary),
    landing_evidence: landingEvidence || [],
    factual_comparison_fields: ['domain', 'headline', 'displayed_url', 'observation_state'],
    missing_evidence: collectMissing(sessionSummary, landingEvidence),
    collection_limitations: limitations || [],
    dates_and_windows: {
      session_generated_at: sessionSummary.generated_at,
      business_hours_mode: 'PAID SERP — BUSINESS HOURS',
    },
    strategy_declarations_forbidden: true,
    note: 'Evidence pack only — no best competitor or recommended strategy declarations',
  };

  return pack;
}

function extractOfferPatterns(summary) {
  const patterns = new Map();
  for (const r of summary.results || []) {
    for (const ad of r.ads || []) {
      const key = ad.headline || 'unknown';
      patterns.set(key, (patterns.get(key) || 0) + 1);
    }
  }
  return [...patterns.entries()].map(([pattern, count]) => ({ pattern, count }));
}

function collectMissing(summary, landing) {
  const missing = [];
  if (!summary.results?.length) missing.push('no paid SERP session results');
  if (!landing?.length) missing.push('landing evidence not collected');
  for (const r of summary.results || []) {
    if (r.observation_state === 'CAPTCHA') missing.push(`CAPTCHA on query: ${r.ads?.[0]?.query || 'unknown'}`);
  }
  return missing;
}

export function buildPackFromSession(sessionSummary, outputPath) {
  const registry = buildAdvertiserRegistry(sessionSummary.results || []);
  const pack = buildCompetitorEvidencePack({
    sessionSummary,
    advertiserRegistry: registry,
    landingEvidence: [],
    limitations: sessionSummary.collection_status === 'COLLECTION DEGRADED' ? ['degraded session'] : [],
  });
  writeJson(outputPath, pack);
  return pack;
}
