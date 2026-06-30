import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import ExcelJS from 'exceljs';
import { differentialValidate, compareSnapshots, CHANGE_TYPES } from '../src/differential-validator.mjs';
import { SYNTHETIC_TEST_OUTPUT_DIR } from '../src/constants.mjs';

async function writeMinimalXlsx(filePath, { e9 = '', phrase = 'test phrase', bid = '100' } = {}) {
  const wb = new ExcelJS.Workbook();
  const sheet = wb.addWorksheet('Тексты');
  sheet.getCell('E9').value = e9;
  sheet.getRow(16).getCell(5).value = 'grp-a';
  sheet.getRow(16).getCell(8).value = phrase;
  sheet.getRow(16).getCell(10).value = 'Headline';
  sheet.getRow(16).getCell(48).value = 'https://example.com/';
  sheet.getRow(16).getCell(54).value = bid;
  sheet.getRow(16).getCell(52).value = 'Новосибирская область';
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  await wb.xlsx.writeFile(filePath);
}

describe('differential-validator', () => {
  it('allows E9-only technical hotfix in hotfix mode', async () => {
    const prev = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'diff-prev.xlsx');
    const curr = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'diff-curr.xlsx');
    await writeMinimalXlsx(prev, { e9: 'ремонт' });
    await writeMinimalXlsx(curr, { e9: '' });

    const result = await differentialValidate(prev, curr, { mode: 'hotfix' });
    assert.equal(result.status, 'SCRIPT_PASS');
    assert.ok(result.changes.some((c) => c.field === 'e9'));
  });

  it('rejects changed phrase in hotfix mode', async () => {
    const prev = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'diff-phrase-prev.xlsx');
    const curr = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'diff-phrase-curr.xlsx');
    await writeMinimalXlsx(prev, { phrase: 'нужен программист 1с' });
    await writeMinimalXlsx(curr, { phrase: 'другая фраза' });

    const result = await differentialValidate(prev, curr, { mode: 'hotfix' });
    assert.equal(result.status, 'SCRIPT_FAIL');
    assert.ok(result.forbidden_changes.some((c) => c.field === 'phrases'));
  });

  it('rejects changed bid', async () => {
    const prev = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'diff-bid-prev.xlsx');
    const curr = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'diff-bid-curr.xlsx');
    await writeMinimalXlsx(prev, { bid: '100' });
    await writeMinimalXlsx(curr, { bid: '200' });

    const result = await differentialValidate(prev, curr, { mode: 'hotfix' });
    assert.equal(result.status, 'SCRIPT_FAIL');
  });

  it('classifies metadata clear change type', () => {
    const result = compareSnapshots(
      { phrases: [], ads: [], bids: [], urls: [], regions: [], metadata: { e9: 'x', organization: '' } },
      { phrases: [], ads: [], bids: [], urls: [], regions: [], metadata: { e9: '', organization: '' } },
      { mode: 'hotfix' }
    );
    assert.equal(result.status, 'SCRIPT_PASS');
    assert.ok(result.changes.some((c) => c.type === CHANGE_TYPES.EXPECTED_METADATA_CLEAR));
  });
});
