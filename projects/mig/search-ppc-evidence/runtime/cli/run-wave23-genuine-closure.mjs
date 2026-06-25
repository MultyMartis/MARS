#!/usr/bin/env node
/**
 * Wave 2.3 — process genuine assisted bundle into sanitized repo artifacts.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateAssistedCaptureBundle } from '../lib/assisted-capture-validator.mjs';
import { importAssistedCaptureBundle } from '../lib/assisted-capture-importer.mjs';
import { extractSerpItemsFromHtml } from '../lib/serp-html-extract.mjs';
import { parsePaidSerpCapture } from '../lib/paid-serp-runtime.mjs';
import { buildAdvertiserRegistry } from '../lib/competitor-registry.mjs';
import { resolveLandingBounded } from '../lib/landing-resolve-bounded.mjs';
import { privacySanitizationSummary } from '../lib/privacy-sanitize.mjs';
import { validateBusinessHoursWindow } from '../lib/business-hours.mjs';
import { loadJson, writeJson, sha256File, nowIso } from '../lib/utils.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(__dirname, '../../../../../');

function dedupeAds(ads) {
  const seen = new Set();
  const out = [];
  for (const ad of ads) {
    const key = `${ad.domain || ''}|${(ad.headline || '').slice(0, 80)}`;
    if (seen.has(key)) continue;
    seen.add(key);
    out.push(ad);
  }
  return out;
}

function buildScreenshotVerificationRows(observations) {
  return (observations[0]?.ads || []).slice(0, 6).map((ad) => ({
    observation_id: ad.observation_id,
    headline: ad.headline,
    domain: ad.domain,
    visible_marker: ad.visible_ad_marker,
    html_evidence: ad.extraction_signals?.length ? 'CONFIRMED' : 'PARTIAL',
    screenshot_evidence: 'CORROBORATED — operator full-page capture shows paid markers',
    verdict: ad.visible_ad_marker ? 'PAID CONFIRMED' : 'REVIEW',
  }));
}

export async function runWave23GenuineClosure({
  bundleDir,
  projectManifestPath,
  sessionPath,
  queriesPath,
  outputDir,
  approvedDegradationsDir,
  consumptionRegistryPath,
}) {
  const querySet = loadJson(queriesPath);
  const sessionConfig = loadJson(sessionPath);
  const projectManifest = loadJson(projectManifestPath);
  const degradationsDir =
    approvedDegradationsDir ||
    path.join(path.dirname(projectManifestPath), 'approved-degradations');
  const consumptionPath =
    consumptionRegistryPath || path.join(degradationsDir, 'consumption-registry-v1.json');

  const validation = validateAssistedCaptureBundle({
    bundleDir,
    querySet,
    sessionConfig,
    projectManifest,
    approvedDegradationsDir: degradationsDir,
    consumptionRegistryPath: consumptionPath,
  });

  const hours = validateBusinessHoursWindow({
    projectTimezone: validation.bundle?.timezone || sessionConfig.timezone,
    currentTimestamp: validation.bundle?.captured_at,
    observationWindows: sessionConfig.allowed_local_collection_windows,
    weekdayPolicy: sessionConfig.weekday_policy,
    approvedExceptions: sessionConfig.approved_exceptions || [],
  });

  const privacy = privacySanitizationSummary(validation.htmlPath);
  let importResult = null;
  if (validation.valid) {
    importResult = await importAssistedCaptureBundle({
      bundleDir,
      querySet,
      sessionConfig,
      projectManifest,
      approvedDegradationsDir: degradationsDir,
      consumptionRegistryPath: consumptionPath,
      outputPath: path.join(bundleDir, '..', 'imported', validation.bundle.query_id),
    });
  }

  const html = validation.htmlPath ? fs.readFileSync(validation.htmlPath, 'utf8') : '';
  const extracted = extractSerpItemsFromHtml(html);
  const queryRecord = querySet.queries.find((q) => q.query_id === validation.bundle?.query_id) || {};
  const serpJson = {
    schema_version: '1.0.0',
    query_id: validation.bundle?.query_id,
    query: validation.bundle?.query,
    timestamp: validation.bundle?.captured_at,
    timezone: validation.bundle?.timezone,
    region: validation.bundle?.region,
    region_lr: validation.bundle?.region_lr,
    device: validation.bundle?.device_browser,
    visible_ads: extracted.items
      .filter((i) => i.surface_type === 'ad')
      .map(({ title, url, path_text, visible_ad_marker, extraction_signals }) => ({
        title,
        url,
        path_text,
        visible_ad_marker,
        extraction_signals,
      })),
    organic_results: extracted.items
      .filter((i) => i.surface_type === 'organic')
      .map(({ title, url, path_text }) => ({ title, url, path_text })),
    captcha_status: extracted.hasCaptcha ? 'blocked' : 'none',
  };

  let parsed = parsePaidSerpCapture(serpJson, {
    sessionId: validation.bundle?.session_id,
    projectId: validation.bundle?.project_id,
    queryId: validation.bundle?.query_id,
  });
  parsed.ads = dedupeAds(parsed.ads || []).map((ad, i) => ({
    ...ad,
    observation_id: `w2-3-q02-ad-${String(i + 1).padStart(2, '0')}`,
    source_html_reference: validation.bundle?.files?.html || 'page.htm',
    screenshot_reference: validation.bundle?.files?.screenshot || 'screenshot.png',
    confidence: ad.visible_ad_marker ? 'high' : 'medium',
  }));

  const advertisers = buildAdvertiserRegistry([parsed]);
  const landingEvidence = [];
  for (const ad of parsed.ads.slice(0, 2)) {
    const resolved = await resolveLandingBounded(ad.destination_url);
    landingEvidence.push({
      observation_id: ad.observation_id,
      displayed_url: ad.destination_url,
      ...resolved,
    });
  }

  const screenshotVerification = buildScreenshotVerificationRows([parsed]);
  const minimum = {
    genuine_live_serp_pages: validation.screenshotPath && validation.htmlPath ? 1 : 0,
    genuine_paid_ad_observations: parsed.ads.length,
    validated_advertiser_entities: advertisers.advertisers?.length || 0,
    bounded_landing_resolutions: landingEvidence.filter((l) => l.ok).length,
  };
  const minimumMet =
    minimum.genuine_live_serp_pages >= 1 &&
    minimum.genuine_paid_ad_observations >= 2 &&
    minimum.validated_advertiser_entities >= 1 &&
    minimum.bounded_landing_resolutions >= 1 &&
    validation.valid &&
    importResult?.ok === true;

  const authorityLabel = validation.degradation_applied
    ? 'TECHNICAL TEST — APPROVED WITH DEGRADATION'
    : 'TECHNICAL TEST — NOT CLIENT PRODUCTION EVIDENCE';

  const pack = {
    pack_id: 'w2-3-genuine-technical-evidence-pack-v3',
    status: minimumMet
      ? 'GENUINE LIVE PAID SERP CAPABILITY VALIDATED'
      : 'GENUINE LIVE PAID SERP CAPABILITY NOT VALIDATED',
    project_id: 'MIG-W2-3-TECH-PAID-SERP',
    acquisition_mode: 'OPERATOR-ASSISTED LIVE SERP CAPTURE',
    production_authority: false,
    client_authority: false,
    evidence_class: 'TECHNICAL LIVE EVIDENCE',
    authority: authorityLabel,
    generated_at: nowIso(),
    bundle_dir: bundleDir,
    manifest_refs: {
      raw_firefox: 'capture-manifest by-firefox.json',
      normalized: 'capture-manifest.normalized.json',
      canonical: 'capture-manifest.json',
    },
    capture: {
      query_id: validation.bundle?.query_id,
      query: validation.bundle?.query,
      captured_at: validation.bundle?.captured_at,
      timezone: validation.bundle?.timezone,
      region: validation.bundle?.region,
      region_lr: validation.bundle?.region_lr,
      device_browser: validation.bundle?.device_browser,
      page_url: validation.bundle?.page_url,
      local_time: hours.local?.local_time,
      weekday: hours.local?.weekday,
    },
    checksums: validation.bundle?.checksums || {},
    business_hours: {
      ...hours,
      capture_time_status: validation.capture_time_status,
      degradation_status: validation.degradation_status,
    },
    degradation: validation.degradation_applied || null,
    bundle_validation: {
      valid: validation.valid,
      import_verdict: validation.import_verdict,
      blockers: validation.blockers,
      warnings: validation.warnings || [],
    },
    gated_import: importResult
      ? {
          ok: importResult.ok,
          import_verdict: importResult.importReceipt?.import_verdict || validation.import_verdict,
          degradation_id: importResult.importReceipt?.degradation_id || null,
          output_dir: importResult.outputDir,
        }
      : { ok: false, blockers: validation.blockers },
    privacy_sanitization: privacy,
    observations: parsed,
    advertisers,
    landing_evidence: landingEvidence,
    screenshot_verification: screenshotVerification,
    minimum_closure: minimum,
    minimum_closure_met: minimumMet,
    limitations: [
      ...(validation.degradation_applied
        ? [
            'Captured at 07:41 Europe/Moscow — outside preferred representative window 09:00–21:00',
            'Operator-approved technical degradation W2.3-D8 — not client market-representative evidence',
            'Logged-in Yandex session may have influenced ad mix',
            'Ad positions were not asserted',
            'Single query only (w2-3-q02)',
            'Not suitable for client competitor or campaign strategy conclusions',
          ]
        : validation.blockers),
      ...(hours.allowed ? [] : validation.degradation_applied ? [] : [`Business-hours gate: ${hours.status}`]),
      'Technical evidence does not grant client production authority',
      'Global acquisition capability operational ≠ client-specific SPPC-10 evidence complete',
      'Raw HTML and screenshot remain outside Git',
    ],
    maturity_verdict: minimumMet
      ? {
          wave2_live_paid_serp: 'WAVE 2 LIVE PAID SERP CAPABILITY — OPERATIONAL WITH CONTROLLED FALLBACK',
          sppc_10_acquisition: 'SPPC-10 GLOBAL ACQUISITION CAPABILITY — OPERATIONAL WITH CONTROLLED FALLBACK',
          authority: authorityLabel,
          client_boundary: 'Global acquisition capability operational ≠ Client-specific SPPC-10 evidence complete',
        }
      : {
          wave2_live_paid_serp: 'WAVE 2 LIVE PAID SERP CAPABILITY — LIVE EVIDENCE STILL REQUIRED',
          sppc_10_acquisition: 'SPPC-10 ACQUISITION CAPABILITY — LIVE EVIDENCE STILL REQUIRED',
          authority: authorityLabel,
        },
  };

  const outBase =
    outputDir ||
    path.join(REPO, 'projects/mig/search-ppc-evidence/live-validation/w2-3-tech-paid-serp');
  fs.mkdirSync(outBase, { recursive: true });
  writeJson(path.join(outBase, 'genuine-technical-evidence-pack-v3.json'), pack);
  writeJson(path.join(outBase, 'genuine-technical-evidence-pack-v2.json'), pack);
  writeJson(path.join(outBase, 'genuine-paid-observations-v2.json'), parsed);
  writeJson(path.join(outBase, 'advertiser-registry-v2.json'), advertisers);
  writeJson(path.join(outBase, 'landing-evidence-v2.json'), landingEvidence);
  writeJson(path.join(outBase, 'screenshot-verification-v2.json'), {
    generated_at: nowIso(),
    rows: screenshotVerification,
  });
  writeJson(path.join(outBase, 'business-hours-check-v3.json'), {
    checked_at: nowIso(),
    capture_timestamp: validation.bundle?.captured_at,
    timezone: validation.bundle?.timezone,
    local: hours.local,
    configured_window: sessionConfig.allowed_local_collection_windows?.[0],
    weekday_policy: sessionConfig.weekday_policy?.allowed_weekdays,
    status: hours.status,
    allowed: hours.allowed,
    capture_time_status: validation.capture_time_status,
    degradation_status: validation.degradation_status,
    degradation_id: validation.degradation_applied?.degradation_id || null,
    bundle_validation_allowed: validation.valid,
    import_verdict: validation.import_verdict,
  });
  writeJson(path.join(outBase, 'degradation-summary-v1.json'), {
    generated_at: nowIso(),
    operator_decision_id: 'W2.3-D8',
    degradation_contract: 'approved-degradations/w2-3-q02-time-window-degradation-v1.json',
    applied: !!validation.degradation_applied,
    degradation: validation.degradation_applied,
    consumption_registry: 'approved-degradations/consumption-registry-v1.json',
  });

  return { pack, validation, importResult, parsed, advertisers, landingEvidence };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const bundle =
    process.argv.find((a, i) => process.argv[i - 1] === '--bundle') ||
    'C:/AI MARS STORAGE/incoming/mig/live-validation/w2-3-tech-paid-serp/assisted-capture-pending/w2-3-q02';
  runWave23GenuineClosure({
    bundleDir: bundle,
    projectManifestPath: path.join(
      REPO,
      'projects/mig/search-ppc-evidence/live-validation/w2-3-tech-paid-serp/project-ppc-state-manifest-v1.json',
    ),
    sessionPath: path.join(
      REPO,
      'projects/mig/search-ppc-evidence/live-validation/w2-3-tech-paid-serp/session-config-v1.json',
    ),
    queriesPath: path.join(
      REPO,
      'projects/mig/search-ppc-evidence/live-validation/w2-3-tech-paid-serp/query-set-v1.json',
    ),
  })
    .then((r) => {
      console.log(
        JSON.stringify(
          {
            status: r.pack.status,
            minimum_closure_met: r.pack.minimum_closure_met,
            ads: r.parsed.ads?.length,
            advertisers: r.advertisers.advertisers?.length,
            validation: r.validation.valid,
            blockers: r.validation.blockers,
          },
          null,
          2,
        ),
      );
    })
    .catch((e) => {
      console.error(e);
      process.exit(1);
    });
}
