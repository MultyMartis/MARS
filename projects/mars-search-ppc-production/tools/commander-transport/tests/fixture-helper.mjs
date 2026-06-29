import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { computeSha256 } from '../src/template-validator.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIXTURES_ROOT = path.join(__dirname, '../fixtures');

const ROLE_FILES = {
  phrase_allocation: 'phrase-allocation.json',
  campaign_architecture: 'campaign-architecture.json',
  primary_ads: 'primary-ads.json',
  callouts: 'callouts.json',
  campaign_negatives: 'campaign-negatives.json',
  group_negatives: 'group-negatives.json',
  cross_campaign_rules: 'cross-campaign-rules.json',
  utm_map: 'utm-map.json',
  campaign_settings: 'campaign-settings.json',
  transport_config: 'transport-config.json',
};

/**
 * @param {string} fixtureName
 * @param {object} [overrides]
 */
export async function buildFixtureManifest(fixtureName, overrides = {}) {
  const dir = path.join(FIXTURES_ROOT, fixtureName);
  const files = [];

  for (const [role, filename] of Object.entries(ROLE_FILES)) {
    const filePath = path.join(dir, filename);
    if (!fs.existsSync(filePath)) {
      if (overrides.optionalRoles?.includes(role)) continue;
      throw new Error(`Missing fixture file ${filePath}`);
    }
    const sha256 = await computeSha256(filePath);
    files.push({
      role,
      path: filePath.replace(/\\/g, '/'),
      sha256,
      required: overrides.requiredRoles?.[role] !== false,
    });
  }

  return {
    schema_version: '1.0.0',
    project_id: 'synthetic-test',
    pilot_id: fixtureName,
    authority_checkpoint: `synthetic-${fixtureName}`,
    campaign_scope: overrides.campaign_scope ?? ['CA-01'],
    operator_approval_state: overrides.operator_approval_state ?? 'OPERATOR_APPROVED',
    generated_at: '2026-06-30T12:00:00.000Z',
    files,
  };
}

export function fixtureDir(name) {
  return path.join(FIXTURES_ROOT, name);
}

export async function writeFixtureManifest(fixtureName, overrides = {}) {
  const manifest = await buildFixtureManifest(fixtureName, overrides);
  const out = path.join(fixtureDir(fixtureName), 'authority-manifest.json');
  fs.writeFileSync(out, `${JSON.stringify(manifest, null, 2)}\n`);
  return out;
}

export function enrichSyntheticAuthority(loaded) {
  const transportConfig = loaded.byRole.transport_config;
  if (!transportConfig) return loaded;
  if (transportConfig.bids) {
    loaded.byRole.bids = { campaign_bids: transportConfig.bids };
  }
  if (transportConfig.display_paths) {
    loaded.byRole.display_paths = transportConfig.display_paths;
  }
  if (transportConfig.group_negatives && !loaded.byRole.group_negatives) {
    loaded.byRole.group_negatives = transportConfig.group_negatives;
  }
  return loaded;
}
