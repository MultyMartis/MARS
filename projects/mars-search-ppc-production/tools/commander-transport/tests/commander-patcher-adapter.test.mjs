import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { adapterAvailable, patchCommanderWorkbook } from '../src/commander-patcher-adapter.mjs';
import { loadAuthority } from '../src/authority-loader.mjs';
import { buildPayloads, validateTransport } from '../src/payload-builder.mjs';
import { COMMANDER_TEMPLATE_PATH, SYNTHETIC_TEST_OUTPUT_DIR } from '../src/constants.mjs';
import { enrichSyntheticAuthority, writeFixtureManifest } from './fixture-helper.mjs';

describe('commander-patcher-adapter', () => {
  it('reports adapter availability', () => {
    assert.equal(typeof adapterAvailable(), 'boolean');
  });

  it('patches synthetic workbook in isolated test directory', async (t) => {
    if (!adapterAvailable()) {
      t.skip('Triumph exporter-cli not available');
      return;
    }

    const manifestPath = await writeFixtureManifest('valid-synthetic');
    let loaded = await loadAuthority(manifestPath, { skipVolumeCheck: true });
    loaded = enrichSyntheticAuthority(loaded);
    const validation = validateTransport(loaded);
    const payloads = buildPayloads(loaded, validation);
    const outDir = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'adapter-test');
    fs.mkdirSync(outDir, { recursive: true });
    const outFile = path.join(outDir, 'synthetic-ca-01.xlsx');

    if (fs.existsSync(outFile)) fs.unlinkSync(outFile);

    const result = await patchCommanderWorkbook({
      payload: payloads[0],
      templatePath: COMMANDER_TEMPLATE_PATH,
      outputPath: outFile,
      guardOptions: { skipVolumeCheck: true },
      allowSyntheticTestDir: true,
    });

    assert.equal(result.ok, true);
    assert.ok(fs.existsSync(outFile));

    await assert.rejects(() =>
      patchCommanderWorkbook({
        payload: payloads[0],
        templatePath: COMMANDER_TEMPLATE_PATH,
        outputPath: outFile,
        guardOptions: { skipVolumeCheck: true },
        allowSyntheticTestDir: true,
      })
    );
  });
});
