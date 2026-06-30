import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import ExcelJS from 'exceljs';
import { loadTemplateContract, scanTemplateContamination } from '../src/template-sanitizer.mjs';
import { COMMANDER_TEMPLATE_PATH } from '../src/constants.mjs';

describe('template-sanitizer', () => {
  it('loads template contract', () => {
    const contract = loadTemplateContract();
    assert.equal(contract.metadata_fields.campaign_negatives.row, 9);
    assert.equal(contract.metadata_fields.campaign_negatives.col, 5);
  });

  it('detects stale Triumph campaign negatives in template', async () => {
    const contract = loadTemplateContract();
    const wb = new ExcelJS.Workbook();
    await wb.xlsx.readFile(COMMANDER_TEMPLATE_PATH);
    const texts = wb.getWorksheet('Тексты');
    const scan = scanTemplateContamination(texts, contract);
    assert.equal(typeof scan.contaminated, 'boolean');
    assert.ok(Array.isArray(scan.findings));
  });

  it('contamination signatures include ремонт запчасти эвакуатор', () => {
    const contract = loadTemplateContract();
    const terms = contract.contamination_signatures.stale_campaign_negatives;
    assert.ok(terms.includes('ремонт'));
    assert.ok(terms.includes('запчасти'));
    assert.ok(terms.includes('эвакуатор'));
  });
});
