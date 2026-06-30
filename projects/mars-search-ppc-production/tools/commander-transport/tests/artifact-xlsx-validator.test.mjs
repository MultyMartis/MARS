import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { adapterAvailable, patchCommanderWorkbook } from '../src/commander-patcher-adapter.mjs';
import { loadAuthority } from '../src/authority-loader.mjs';
import { buildPayloads, validateTransport } from '../src/payload-builder.mjs';
import { validateArtifactXlsx } from '../src/artifact-xlsx-validator.mjs';
import { COMMANDER_TEMPLATE_PATH, SYNTHETIC_TEST_OUTPUT_DIR } from '../src/constants.mjs';
import { enrichSyntheticAuthority, writeFixtureManifest } from './fixture-helper.mjs';
import { sanitizationCellValue } from '../src/template-sanitizer.mjs';
import ExcelJS from 'exceljs';

describe('artifact-xlsx-validator', () => {
  it('detects populated E9 when policy blank', async () => {
    const wb = new ExcelJS.Workbook();
    const sheet = wb.addWorksheet('Тексты');
    sheet.getCell('E9').value = 'ремонт запчасти';
    const tmp = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'artifact-e9-fail.xlsx');
    fs.mkdirSync(path.dirname(tmp), { recursive: true });
    await wb.xlsx.writeFile(tmp);

    const result = await validateArtifactXlsx(tmp, {
      embedded_campaign_negatives_policy: 'blank',
    });
    assert.equal(result.script_status, 'SCRIPT_FAIL');
    assert.ok(result.violations.some((v) => v.code === 'E9_NOT_BLANK' || v.code === 'STALE_TEMPLATE_NEGATIVE'));
  });

  it('passes blank E9 when policy blank', async () => {
    const wb = new ExcelJS.Workbook();
    wb.addWorksheet('Тексты');
    wb.addWorksheet('Регионы');
    const tmp = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'artifact-e9-pass.xlsx');
    await wb.xlsx.writeFile(tmp);

    const result = await validateArtifactXlsx(tmp, {
      embedded_campaign_negatives_policy: 'blank',
    });
    const e9Violations = result.violations.filter((v) => v.code === 'E9_NOT_BLANK');
    assert.equal(e9Violations.length, 0);
  });

  it('validates synthetic patched workbook E9 cleared', async (t) => {
    if (!adapterAvailable()) {
      t.skip('Triumph exporter-cli not available');
      return;
    }

    const manifestPath = await writeFixtureManifest('valid-synthetic');
    let loaded = await loadAuthority(manifestPath, { skipVolumeCheck: true });
    loaded = enrichSyntheticAuthority(loaded);
    const validation = validateTransport(loaded);
    const payloads = buildPayloads(loaded, validation);
    payloads[0].metadata_patches = {
      ...payloads[0].metadata_patches,
      'Минус-фразы на кампанию:': '',
    };
    const outFile = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'artifact-validator-synthetic.xlsx');
    if (fs.existsSync(outFile)) fs.unlinkSync(outFile);

    await patchCommanderWorkbook({
      payload: payloads[0],
      templatePath: COMMANDER_TEMPLATE_PATH,
      outputPath: outFile,
      guardOptions: { skipVolumeCheck: true },
      allowSyntheticTestDir: true,
    });

    const wb = new ExcelJS.Workbook();
    await wb.xlsx.readFile(outFile);
    const texts = wb.getWorksheet('Тексты');
    const e9 = sanitizationCellValue(texts, 9, 5);
    assert.equal(e9, '');

    const result = await validateArtifactXlsx(outFile, {
      embedded_campaign_negatives_policy: 'blank',
    });
    assert.ok(
      result.violations.filter((v) => v.code === 'E9_NOT_BLANK').length === 0,
      'E9 should be blank in sanitized artifact'
    );
  });
});
