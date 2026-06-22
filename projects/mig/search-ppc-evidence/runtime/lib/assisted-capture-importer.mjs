import fs from 'node:fs';
import path from 'node:path';
import { validateAssistedCaptureBundle } from './assisted-capture-validator.mjs';
import { buildSerpJsonFromAssistedBundle, extractSerpItemsFromHtml } from './serp-html-extract.mjs';
import { parsePaidSerpCapture } from './paid-serp-runtime.mjs';
import { buildAdvertiserRegistry } from './competitor-registry.mjs';
import { captureLandingEvidence } from './landing-evidence.mjs';
import { buildDegradedRecord } from './freshness.mjs';
import { loadJson, writeJson, nowIso, sha256File } from './utils.mjs';

export function importAssistedCaptureBundle({
  bundleDir,
  querySet,
  sessionConfig,
  projectManifest,
  receipt,
  outputPath,
}) {
  const validation = validateAssistedCaptureBundle({
    bundleDir,
    querySet,
    sessionConfig,
    projectManifest,
  });

  if (!validation.valid) {
    return { ok: false, blockers: validation.blockers };
  }

  const { bundle, screenshotPath, htmlPath } = validation;
  const html = htmlPath ? fs.readFileSync(htmlPath, 'utf8') : '';
  const extracted = extractSerpItemsFromHtml(html);
  const queryRecord = querySet?.queries?.find((q) => q.query_id === bundle.query_id) || {};

  const serpJson = buildSerpJsonFromAssistedBundle(bundle, extracted, queryRecord);
  const sessionId = bundle.session_id || sessionConfig?.session_id || `assisted-${Date.now()}`;

  const outDir = outputPath || path.join(bundleDir, '..', 'imported', bundle.query_id);
  fs.mkdirSync(outDir, { recursive: true });

  if (screenshotPath) fs.copyFileSync(screenshotPath, path.join(outDir, 'screenshot.png'));
  if (htmlPath) fs.copyFileSync(htmlPath, path.join(outDir, 'page.html'));

  serpJson.screenshot_reference = screenshotPath ? 'screenshot.png' : null;
  serpJson.html_reference = htmlPath ? 'page.html' : null;
  writeJson(path.join(outDir, 'serp.json'), serpJson);

  const parsed = parsePaidSerpCapture(serpJson, {
    sessionId,
    projectId: bundle.project_id,
    queryId: bundle.query_id,
  });
  parsed.acquisition_mode = 'OPERATOR-ASSISTED LIVE SERP CAPTURE';
  parsed.production_authority = false;
  writeJson(path.join(outDir, 'observation.json'), parsed);

  const landingEvidence = [];
  for (const ad of (parsed.ads || []).slice(0, 2)) {
    landingEvidence.push(
      captureLandingEvidence({
        destinationUrl: ad.destination_url,
        pageData: {
          final_url: ad.destination_url,
          page_title: null,
          redirect_chain: [],
        },
        evidenceLinks: {},
      }),
    );
  }
  if (landingEvidence.length) writeJson(path.join(outDir, 'landing-evidence.json'), landingEvidence);

  const observations = [parsed];
  const advertisers = buildAdvertiserRegistry(observations);

  const importReceipt = {
    schema_version: '1.0.0',
    import_id: `assisted-import-${bundle.query_id}-${Date.now()}`,
    imported_at: nowIso(),
    acquisition_mode: 'OPERATOR-ASSISTED LIVE SERP CAPTURE',
    evidence_class: 'TECHNICAL LIVE EVIDENCE',
    production_authority: false,
    bundle_dir: bundleDir,
    bundle_manifest_sha256: sha256File(path.join(bundleDir, 'capture-manifest.json')),
    output_dir: outDir,
    observation_state: parsed.observation_state,
    ads_count: parsed.ads?.length || 0,
    execution_receipt_id: receipt?.receipt_id || null,
    operator_attestation: bundle.operator_attestation,
  };
  writeJson(path.join(outDir, 'import-receipt.json'), importReceipt);

  return {
    ok: true,
    observation: parsed,
    advertisers,
    landingEvidence,
    importReceipt,
    outputDir: outDir,
    serpJson,
  };
}

export function requireDegradedRecordForFallback({ automatedAttempted, automatedOutcome, assistedUsed, outputPath }) {
  if (!automatedAttempted || !assistedUsed) return { ok: true };

  const degradedPath = path.join(outputPath, 'degraded-evidence-record-v1.json');
  if (!fs.existsSync(degradedPath)) {
    return {
      ok: false,
      blockers: ['BLOCKED — ASSISTED LIVE CAPTURE BUNDLE INVALID: fallback used without degraded record'],
    };
  }
  return { ok: true, path: degradedPath };
}

export function writeDegradedEvidenceRecord({
  outputPath,
  automatedSessionId,
  automatedOutcome,
  captchaEvidencePath,
  fallbackReason,
  assistedSessionId,
  limitations,
  lifecycleImpact,
  sufficientForCompetitorAudit,
  recollectionRecommended,
}) {
  const record = buildDegradedRecord({
    completedQueries: automatedOutcome?.completed || [],
    incompleteQueries: automatedOutcome?.incomplete || [],
    reason: fallbackReason || 'CAPTCHA on automated acquisition',
    evidence: {
      automated_session_id: automatedSessionId,
      automated_outcome: automatedOutcome,
      captcha_evidence_path: captchaEvidencePath,
      assisted_session_id: assistedSessionId,
    },
    impact: lifecycleImpact || 'Automated acquisition blocked; assisted fallback used for technical validation',
    retryRecommendation: recollectionRecommended ? 'Operator-assisted capture during approved window' : 'Environment review before retry',
    lifecycleContinuationPermitted: false,
    operatorApprovalRequired: true,
  });

  record.schema_version = '1.1.0';
  record.acquisition_degradation = {
    automated_attempt: true,
    assisted_fallback: true,
    limitations: limitations || [],
    sufficient_for_factual_competitor_audit: sufficientForCompetitorAudit ?? false,
    recollection_recommended: recollectionRecommended ?? true,
    approved_degradation: true,
    concealment: false,
  };

  const out = path.join(outputPath, 'degraded-evidence-record-v1.json');
  writeJson(out, record);
  return record;
}
