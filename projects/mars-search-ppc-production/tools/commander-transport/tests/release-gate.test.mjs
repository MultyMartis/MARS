import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { runReleaseGate } from '../src/release-gate.mjs';
import {
  generateApprovalReceiptForReview,
  RECEIPT_STATUSES,
} from '../src/operator-approval-receipt.mjs';
import { GATE_STATUS } from '../src/release-state.mjs';
import { SYNTHETIC_TEST_OUTPUT_DIR } from '../src/constants.mjs';
import ExcelJS from 'exceljs';

async function writeGateFixturePackage(dir) {
  fs.mkdirSync(dir, { recursive: true });
  const wb = new ExcelJS.Workbook();
  const texts = wb.addWorksheet('Тексты');
  wb.addWorksheet('Регионы');
  texts.getRow(16).getCell(5).value = 'grp-a';
  texts.getRow(16).getCell(8).value = 'нужен программист 1с';
  texts.getRow(16).getCell(10).value = 'Заголовок';
  texts.getRow(16).getCell(48).value = 'https://corvonero.ru/';
  texts.getRow(16).getCell(52).value = 'Новосибирская область';
  const xlsxPath = path.join(dir, 'synthetic-campaign.xlsx');
  await wb.xlsx.writeFile(xlsxPath);

  const authority = {
    authority_frozen: true,
    campaign_count: 1,
    group_count: 1,
    phrase_slot_count: 1,
    ad_count: 1,
    embedded_negative_policy: 'blank',
  };
  fs.writeFileSync(path.join(dir, 'authority-summary.json'), JSON.stringify(authority, null, 2));
  return { xlsxPath, authority };
}

describe('release-gate', () => {
  it('fails without operator approval receipt', async () => {
    const pkg = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'release-gate-no-receipt');
    await writeGateFixturePackage(pkg);

    const result = await runReleaseGate({
      project_id: 'synthetic-test',
      package_root: pkg,
      authority_path: path.join(pkg, 'authority-summary.json'),
      guardOptions: { skipVolumeCheck: true },
      template_path: null,
    });

    assert.equal(result.status, GATE_STATUS.FAIL);
    assert.ok(result.violations.some((v) => v.code === 'MISSING_OPERATOR_RECEIPT'));
  });

  it('fails when E9 repopulated', async () => {
    const pkg = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'release-gate-e9-fail');
    const { xlsxPath } = await writeGateFixturePackage(pkg);
    const wb = new ExcelJS.Workbook();
    await wb.xlsx.readFile(xlsxPath);
    wb.getWorksheet('Тексты').getCell('E9').value = 'ремонт';
    await wb.xlsx.writeFile(xlsxPath);

    const receiptPath = path.join(pkg, 'approval-receipt.json');
    const receipt = generateApprovalReceiptForReview({
      project_id: 'synthetic-test',
      campaign_program: 'test',
      release_version: 'v0',
      hold_count: 0,
    });
    receipt.status = RECEIPT_STATUSES.OPERATOR_SEMANTIC_APPROVED;
    receipt.approval_timestamp = new Date().toISOString();
    receipt.operator_identity_label = 'test-operator';
    receipt.generated_for_review_only = false;
    fs.writeFileSync(receiptPath, JSON.stringify(receipt, null, 2));

    const result = await runReleaseGate({
      project_id: 'synthetic-test',
      package_root: pkg,
      authority_path: path.join(pkg, 'authority-summary.json'),
      receipt_path: receiptPath,
      guardOptions: { skipVolumeCheck: true },
    });

    assert.equal(result.status, GATE_STATUS.FAIL);
    assert.ok(
      result.violations.some(
        (v) => v.code.includes('E9') || v.code.includes('STALE') || v.code.includes('ARTIFACT')
      )
    );
  });

  it('passes on clean fixture with valid approval', async () => {
    const pkg = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'release-gate-pass');
    await writeGateFixturePackage(pkg);

    const receiptPath = path.join(pkg, 'approval-receipt.json');
    const receipt = generateApprovalReceiptForReview({
      project_id: 'synthetic-test',
      campaign_program: 'test',
      release_version: 'v0',
      hold_count: 0,
      campaign_count: 1,
      group_count: 1,
      ad_count: 1,
      phrase_count: 1,
    });
    receipt.status = RECEIPT_STATUSES.OPERATOR_SEMANTIC_APPROVED;
    receipt.approval_timestamp = new Date().toISOString();
    receipt.operator_identity_label = 'test-operator';
    receipt.generated_for_review_only = false;
    fs.writeFileSync(receiptPath, JSON.stringify(receipt, null, 2));

    const result = await runReleaseGate({
      project_id: 'synthetic-test',
      package_root: pkg,
      authority_path: path.join(pkg, 'authority-summary.json'),
      receipt_path: receiptPath,
      xlsx_files: ['synthetic-campaign.xlsx'],
      guardOptions: { skipVolumeCheck: true },
    });

    assert.equal(result.status, GATE_STATUS.PASS);
  });
});
