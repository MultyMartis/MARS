import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { loadAuthority } from '../src/authority-loader.mjs';
import { buildPayloads, assertPayloadDeterminism } from '../src/payload-builder.mjs';
import { validateTransport } from '../src/transport-validator.mjs';
import { enrichSyntheticAuthority, writeFixtureManifest } from './fixture-helper.mjs';

describe('payload-builder', () => {
  it('builds deterministic per-campaign payloads', async () => {
    const manifestPath = await writeFixtureManifest('valid-synthetic');
    let loaded = await loadAuthority(manifestPath, { skipVolumeCheck: true });
    loaded = enrichSyntheticAuthority(loaded);
    const validation = validateTransport(loaded);
    assert.equal(validation.status, 'PASS');
    const payloads = buildPayloads(loaded, validation);
    assert.equal(payloads.length, 1);
    assert.equal(payloads[0].campaign_id, 'CA-01');
    assert.ok(payloads[0].rows.length > 0);
    assert.ok(assertPayloadDeterminism(payloads));
    const adRows = payloads[0].rows.filter((r) => r.row_type === 'AD');
    const kwRows = payloads[0].rows.filter((r) => r.row_type === 'KEYWORD');
    assert.equal(adRows.length, 2);
    assert.equal(kwRows.length, 6);
  });

  it('refuses payload build on failed validation', async () => {
    const manifestPath = await writeFixtureManifest('invalid-over-200');
    let loaded = await loadAuthority(manifestPath, { skipVolumeCheck: true });
    loaded = enrichSyntheticAuthority(loaded);
    const validation = validateTransport(loaded);
    assert.throws(() => buildPayloads(loaded, validation));
  });
});
