import { describe, it, before } from 'node:test';
import assert from 'node:assert/strict';
import { loadAuthority } from '../src/authority-loader.mjs';
import { validateTransport } from '../src/transport-validator.mjs';
import { GROUP_LIMIT_STOP_CODE } from '../src/constants.mjs';
import { enrichSyntheticAuthority, writeFixtureManifest } from './fixture-helper.mjs';

async function loadFixture(name) {
  const manifestPath = await writeFixtureManifest(name);
  const loaded = await loadAuthority(manifestPath, { skipVolumeCheck: true });
  return enrichSyntheticAuthority(loaded);
}

describe('transport-validator', () => {
  it('passes valid synthetic authority', async () => {
    const loaded = await loadFixture('valid-synthetic');
    const result = validateTransport(loaded);
    assert.equal(result.status, 'PASS', JSON.stringify(result.violations));
  });

  it('fails group count > 200', async () => {
    const loaded = await loadFixture('invalid-over-200');
    const result = validateTransport(loaded);
    assert.equal(result.status, 'FAIL');
    const limit = result.violations.find((v) => v.code === 'GROUP_PHRASE_LIMIT');
    assert.ok(limit);
    assert.equal(limit.actual_phrase_count, 201);
    assert.equal(result.stop_code, GROUP_LIMIT_STOP_CODE);
  });

  it('fails invalid region', async () => {
    const loaded = await loadFixture('invalid-region');
    const result = validateTransport(loaded);
    assert.ok(result.violations.some((v) => v.code === 'INVALID_REGION_AUTHORITY'));
  });

  it('fails nonblank organization', async () => {
    const loaded = await loadFixture('invalid-organization');
    const result = validateTransport(loaded);
    assert.ok(result.violations.some((v) => v.code === 'NONBLANK_ORGANIZATION_POLICY'));
  });

  it('fails negative duplicates and leakage', async () => {
    const loaded = await loadFixture('invalid-negatives');
    const result = validateTransport(loaded);
    assert.ok(result.violations.some((v) => v.code === 'DUPLICATE_NEGATIVE'));
    assert.ok(result.violations.some((v) => v.code === 'EMPTY_NEGATIVE'));
    assert.ok(result.violations.some((v) => v.code === 'CA05_NEGATIVE_LEAK'));
    assert.ok(result.violations.some((v) => v.code === 'UNKNOWN_GROUP_NEGATIVE_REF'));
  });

  it('fails unapproved ad', async () => {
    const loaded = await loadFixture('invalid-unapproved-ad');
    const result = validateTransport(loaded);
    assert.ok(result.violations.some((v) => v.code === 'UNAPPROVED_AD'));
  });

  it('reports cross-campaign rules absent as warning when not deployed', async () => {
    const loaded = await loadFixture('valid-synthetic');
    const result = validateTransport(loaded);
    assert.ok(result.warnings.some((w) => w.code === 'CROSS_CAMPAIGN_NOT_APPLIED'));
  });

  it('fails when bid policy is not explicitly selected', async () => {
    const manifestPath = await writeFixtureManifest('valid-synthetic');
    let loaded = await loadAuthority(manifestPath, { skipVolumeCheck: true });
    loaded = enrichSyntheticAuthority(loaded);
    delete loaded.byRole.transport_config.bid_policy;
    const result = validateTransport(loaded);
    assert.equal(result.status, 'FAIL');
    assert.ok(
      result.violations.some((v) => v.code === 'BID_POLICY_NOT_EXPLICITLY_SELECTED')
    );
  });
});
