import { describe, it, before } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { loadAuthority } from '../src/authority-loader.mjs';
import { buildFixtureManifest, enrichSyntheticAuthority, writeFixtureManifest } from './fixture-helper.mjs';

describe('authority-loader', () => {
  let manifestPath;

  before(async () => {
    manifestPath = await writeFixtureManifest('valid-synthetic');
  });

  it('loads valid synthetic authority', async () => {
    const loaded = await loadAuthority(manifestPath, { skipVolumeCheck: true });
    enrichSyntheticAuthority(loaded);
    assert.ok(loaded.byRole.phrase_allocation);
    assert.ok(loaded.byRole.transport_config);
    assert.ok(loaded.byRole.bids);
  });

  it('rejects SHA mismatch', async () => {
    const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
    manifest.files[0].sha256 = '0'.repeat(64);
    const bad = path.join(path.dirname(manifestPath), 'bad-manifest.json');
    fs.writeFileSync(bad, JSON.stringify(manifest));
    await assert.rejects(() => loadAuthority(bad, { skipVolumeCheck: true }));
  });

  it('rejects forbidden authority role', async () => {
    const manifest = await buildFixtureManifest('valid-synthetic');
    manifest.files.push({
      role: 'semantic_cache',
      path: manifest.files[0].path,
      sha256: manifest.files[0].sha256,
      required: true,
    });
    const bad = path.join(path.dirname(manifestPath), 'forbidden-role.json');
    fs.writeFileSync(bad, JSON.stringify(manifest));
    await assert.rejects(() => loadAuthority(bad, { skipVolumeCheck: true }));
  });
});
