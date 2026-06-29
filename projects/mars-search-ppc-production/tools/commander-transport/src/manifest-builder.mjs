import fs from 'node:fs';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { REPO_ROOT, TOOL_ROOT } from './constants.mjs';
import { computeSha256 } from './template-validator.mjs';

/**
 * Build authority manifest with computed SHA-256 hashes.
 * @param {object} spec
 */
export async function buildAuthorityManifest(spec) {
  const files = [];
  for (const entry of spec.files) {
    const absPath = path.isAbsolute(entry.path)
      ? entry.path
      : path.join(REPO_ROOT, entry.path);
    const sha256 = await computeSha256(absPath);
    files.push({
      role: entry.role,
      path: absPath.replace(/\\/g, '/'),
      sha256,
      required: entry.required !== false,
    });
  }

  return {
    schema_version: '1.0.0',
    project_id: spec.project_id,
    pilot_id: spec.pilot_id,
    authority_checkpoint: spec.authority_checkpoint,
    campaign_scope: spec.campaign_scope,
    operator_approval_state: spec.operator_approval_state ?? 'OPERATOR_APPROVED',
    generated_at: spec.generated_at ?? new Date().toISOString(),
    files,
  };
}

/**
 * @param {object} validationResult
 * @param {string} outPath
 */
export function writeValidationReceipt(validationResult, outPath) {
  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  fs.writeFileSync(outPath, `${JSON.stringify(validationResult, null, 2)}\n`);
}

export function hashPayload(payload) {
  return createHash('sha256').update(JSON.stringify(payload)).digest('hex');
}

export const CORVONERO_FROZEN_AUTHORITY_SPEC = {
  project_id: 'mars-search-ppc-production',
  pilot_id: 'corvonero',
  authority_checkpoint: 'corvonero-production-extensions-final-checkpoint-v1',
  campaign_scope: ['CA-01', 'CA-02', 'CA-03', 'CA-04', 'CA-05'],
  operator_approval_state: 'OPERATOR_APPROVED',
  files: [
    {
      role: 'phrase_allocation',
      path: 'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-AD-WAVE-1-FINAL-PHRASE-ALLOCATION-v1.json',
    },
    {
      role: 'campaign_architecture',
      path: 'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-AD-WAVE-1-P1-FINAL-GROUP-REGISTER-v1.json',
    },
    {
      role: 'primary_ads',
      path: 'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-AD-WAVE-1-P1-FINAL-PRIMARY-ADS-v1.json',
    },
    {
      role: 'callouts',
      path: 'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-EXT-W1-CALLOUTS-v2.json',
    },
    {
      role: 'campaign_negatives',
      path: 'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-EXT-W1-NEGATIVE-DEPLOYMENT-v1.json',
    },
    {
      role: 'cross_campaign_rules',
      path: 'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-EXT-W1-CROSS-NEGATIVES-v2.json',
    },
    {
      role: 'utm_map',
      path: 'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-EXT-W1-UTM-POLICY-v2.json',
    },
    {
      role: 'campaign_settings',
      path: 'projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-EXT-W1-CAMPAIGN-SETTINGS-v2.json',
    },
    {
      role: 'transport_config',
      path: 'projects/mars-search-ppc-production/tools/commander-transport/fixtures/corvonero-frozen/transport-config-v1.json',
    },
  ],
};

export const CORVONERO_MANIFEST_PATH = path.join(
  TOOL_ROOT,
  'fixtures',
  'corvonero-frozen',
  'authority-manifest-v1.json'
);
