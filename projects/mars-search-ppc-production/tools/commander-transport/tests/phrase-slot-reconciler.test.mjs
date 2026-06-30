import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import ExcelJS from 'exceljs';
import {
  buildExpectedSlotsFromGroupPlan,
  reconcilePhraseSlotSets,
  reconcilePackagePhraseSlots,
  extractArtifactSlotsFromXlsx,
} from '../src/phrase-slot-reconciler.mjs';
import { runReleaseGate } from '../src/release-gate.mjs';
import {
  generateApprovalReceiptForReview,
  RECEIPT_STATUSES,
} from '../src/operator-approval-receipt.mjs';
import { GATE_STATUS } from '../src/release-state.mjs';
import { SYNTHETIC_TEST_OUTPUT_DIR } from '../src/constants.mjs';
import { DATA_START_ROW, FORENSIC_COL } from '../src/workbook-forensic-verifier.mjs';

const GROUP_PLAN_FIXTURE = {
  groups: [
    {
      campaign: 'CA-01-LOCAL',
      mode: 'LOCAL',
      group_id: 'grp-a',
      group_name: 'Group A',
      phrase_list: 'alpha one; alpha two',
      commercial_intent: 'CA-01',
    },
    {
      campaign: 'CA-01-REMOTE',
      mode: 'REMOTE',
      group_id: 'grp-a',
      group_name: 'Group A',
      phrase_list: 'alpha one',
      commercial_intent: 'CA-01',
    },
  ],
};

const ARCH_FIXTURE = {
  groups: [
    { campaign_id: 'CA-01-LOCAL', group_id: 'grp-a', group_name: 'Group A' },
    { campaign_id: 'CA-01-REMOTE', group_id: 'grp-a', group_name: 'Group A' },
  ],
};

async function writeSyntheticXlsx(dir, filename, campaignId, phrases) {
  fs.mkdirSync(dir, { recursive: true });
  const wb = new ExcelJS.Workbook();
  const texts = wb.addWorksheet('Тексты');
  wb.addWorksheet('Регионы');
  let row = DATA_START_ROW;
  for (const p of phrases) {
    texts.getRow(row).getCell(FORENSIC_COL.group_name).value = 'Group A';
    texts.getRow(row).getCell(FORENSIC_COL.phrase).value = p.phrase;
    texts.getRow(row).getCell(FORENSIC_COL.headline_1).value = p.ad ? 'Ad title' : '';
    texts.getRow(row).getCell(FORENSIC_COL.landing_url).value = p.ad ? 'https://example.test/' : '';
    texts.getRow(row).getCell(FORENSIC_COL.bid).value = p.bid ?? 100;
    texts.getRow(row).getCell(FORENSIC_COL.region).value = campaignId.endsWith('LOCAL')
      ? 'Новосибирская область'
      : 'Россия';
    row += 1;
  }
  const fp = path.join(dir, filename);
  await wb.xlsx.writeFile(fp);
  return fp;
}

async function writeGatePackage(dir, options = {}) {
  const { authoritySlots = 3, artifactPhrases, groupPlan = GROUP_PLAN_FIXTURE } = options;
  const localFile = 'synthetic-ca-01-local.xlsx';
  const remoteFile = 'synthetic-ca-01-remote.xlsx';
  await writeSyntheticXlsx(dir, localFile, 'CA-01-LOCAL', artifactPhrases?.local ?? [
    { phrase: 'alpha one', ad: true },
    { phrase: 'alpha two' },
  ]);
  await writeSyntheticXlsx(dir, remoteFile, 'CA-01-REMOTE', artifactPhrases?.remote ?? [
    { phrase: 'alpha one', ad: true },
  ]);

  const groupPlanPath = path.join(dir, 'group-plan.json');
  fs.writeFileSync(groupPlanPath, JSON.stringify(groupPlan, null, 2));
  const archPath = path.join(dir, 'architecture.json');
  fs.writeFileSync(archPath, JSON.stringify(ARCH_FIXTURE, null, 2));

  const authority = {
    authority_frozen: true,
    campaign_count: 2,
    group_count: 2,
    phrase_slot_count: authoritySlots,
    ad_count: 2,
    embedded_negative_policy: 'blank',
  };
  fs.writeFileSync(path.join(dir, 'authority-summary.json'), JSON.stringify(authority, null, 2));

  const receiptPath = path.join(dir, 'approval-receipt.json');
  const receipt = generateApprovalReceiptForReview({
    project_id: 'synthetic-test',
    campaign_program: 'test',
    release_version: 'v0',
    hold_count: 0,
    campaign_count: 2,
    group_count: 2,
    ad_count: 2,
    phrase_count: 2,
    phrase_slot_count: authoritySlots,
  });
  receipt.status = RECEIPT_STATUSES.OPERATOR_SEMANTIC_APPROVED;
  receipt.approval_timestamp = new Date().toISOString();
  receipt.operator_identity_label = 'test-operator';
  receipt.generated_for_review_only = false;
  receipt.authority_artifact_paths = [groupPlanPath.replace(/\\/g, '/')];
  fs.writeFileSync(receiptPath, JSON.stringify(receipt, null, 2));

  return { localFile, remoteFile, groupPlanPath, archPath, receiptPath };
}

describe('phrase-slot-reconciler', () => {
  it('builds expected slots from group plan phrase_list', () => {
    const slots = buildExpectedSlotsFromGroupPlan(GROUP_PLAN_FIXTURE);
    assert.equal(slots.length, 3);
    assert.equal(slots[0].slot_key, 'CA-01-LOCAL|LOCAL|grp-a|alpha one');
  });

  it('detects exact multi-campaign match', async () => {
    const dir = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'phrase-slot-exact-match');
    const { localFile, remoteFile } = await writeGatePackage(dir);
    const result = await reconcilePackagePhraseSlots({
      group_plan: GROUP_PLAN_FIXTURE,
      architecture: ARCH_FIXTURE,
      package_root: dir,
      xlsx_files: [localFile, remoteFile],
    });
    assert.equal(result.phrase_slot_reconciliation_pass, true);
    assert.equal(result.authority_phrase_slots, 3);
    assert.equal(result.artifact_phrase_slots, 3);
    assert.equal(result.phrase_slot_delta, 0);
  });

  it('fails authority 926 vs artifact 924 pattern (aggregate mismatch)', () => {
    const expected = buildExpectedSlotsFromGroupPlan({
      groups: Array.from({ length: 926 }, (_, i) => ({
        campaign: 'CA-01-LOCAL',
        mode: 'LOCAL',
        group_id: 'g',
        group_name: 'G',
        phrase_list: `phrase ${i}`,
      })),
    });
    const artifact = expected.slice(0, 924).map((e, i) => ({
      filename: 'f.xlsx',
      campaign_id: e.campaign_id,
      mode: e.mode,
      group_id: e.group_id,
      group_name: e.group_name,
      phrase: e.phrase,
      normalized_phrase: e.normalized_phrase,
      slot_key: e.slot_key,
      xlsx_row: 16 + i,
    }));
    const result = reconcilePhraseSlotSets(expected, artifact);
    assert.equal(result.phrase_slot_reconciliation_pass, false);
    assert.equal(result.authority_phrase_slots, 926);
    assert.equal(result.artifact_phrase_slots, 924);
    assert.equal(result.phrase_slot_delta, -2);
    assert.equal(result.missing_slots, 2);
  });

  it('fails one missing phrase in one XLSX', async () => {
    const dir = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'phrase-slot-one-missing');
    const { localFile, remoteFile } = await writeGatePackage(dir, {
      artifactPhrases: {
        local: [{ phrase: 'alpha one', ad: true }],
        remote: [{ phrase: 'alpha one', ad: true }],
      },
    });
    const result = await reconcilePackagePhraseSlots({
      group_plan: GROUP_PLAN_FIXTURE,
      architecture: ARCH_FIXTURE,
      package_root: dir,
      xlsx_files: [localFile, remoteFile],
    });
    assert.equal(result.missing_slots, 1);
    assert.equal(result.phrase_slot_reconciliation_pass, false);
  });

  it('fails two missing phrases across campaigns', async () => {
    const dir = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'phrase-slot-two-missing');
    const { localFile, remoteFile } = await writeGatePackage(dir, {
      artifactPhrases: { local: [], remote: [] },
    });
    const result = await reconcilePackagePhraseSlots({
      group_plan: GROUP_PLAN_FIXTURE,
      architecture: ARCH_FIXTURE,
      package_root: dir,
      xlsx_files: [localFile, remoteFile],
    });
    assert.equal(result.missing_slots, 3);
    assert.equal(result.phrase_slot_reconciliation_pass, false);
  });

  it('fails one extra artifact phrase', async () => {
    const dir = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'phrase-slot-extra');
    const { localFile, remoteFile } = await writeGatePackage(dir, {
      artifactPhrases: {
        local: [
          { phrase: 'alpha one', ad: true },
          { phrase: 'alpha two' },
          { phrase: 'unexpected extra' },
        ],
        remote: [{ phrase: 'alpha one', ad: true }],
      },
    });
    const result = await reconcilePackagePhraseSlots({
      group_plan: GROUP_PLAN_FIXTURE,
      architecture: ARCH_FIXTURE,
      package_root: dir,
      xlsx_files: [localFile, remoteFile],
    });
    assert.equal(result.unexpected_slots, 1);
    assert.equal(result.phrase_slot_reconciliation_pass, false);
  });

  it('fails duplicate phrase even when totals match', () => {
    const expected = buildExpectedSlotsFromGroupPlan({
      groups: [
        {
          campaign: 'CA-01-LOCAL',
          mode: 'LOCAL',
          group_id: 'grp-a',
          group_name: 'Group A',
          phrase_list: 'alpha one; alpha two',
        },
      ],
    });
    const artifact = [
      {
        filename: 'f.xlsx',
        campaign_id: 'CA-01-LOCAL',
        mode: 'LOCAL',
        group_id: 'grp-a',
        group_name: 'Group A',
        phrase: 'alpha one',
        normalized_phrase: 'alpha one',
        slot_key: 'CA-01-LOCAL|LOCAL|grp-a|alpha one',
        xlsx_row: 16,
      },
      {
        filename: 'f.xlsx',
        campaign_id: 'CA-01-LOCAL',
        mode: 'LOCAL',
        group_id: 'grp-a',
        group_name: 'Group A',
        phrase: 'alpha one',
        normalized_phrase: 'alpha one',
        slot_key: 'CA-01-LOCAL|LOCAL|grp-a|alpha one',
        xlsx_row: 17,
      },
      {
        filename: 'f.xlsx',
        campaign_id: 'CA-01-LOCAL',
        mode: 'LOCAL',
        group_id: 'grp-a',
        group_name: 'Group A',
        phrase: 'alpha two',
        normalized_phrase: 'alpha two',
        slot_key: 'CA-01-LOCAL|LOCAL|grp-a|alpha two',
        xlsx_row: 18,
      },
    ];
    const result = reconcilePhraseSlotSets(expected, artifact);
    assert.equal(result.authority_phrase_slots, 2);
    assert.equal(result.artifact_phrase_slots, 2);
    assert.equal(result.phrase_slot_delta, 0);
    assert.equal(result.duplicate_slots, 1);
    assert.equal(result.phrase_slot_reconciliation_pass, false);
  });

  it('fails wrong group assignment for same phrase', () => {
    const expected = buildExpectedSlotsFromGroupPlan({
      groups: [
        {
          campaign: 'CA-01-LOCAL',
          mode: 'LOCAL',
          group_id: 'grp-a',
          group_name: 'Group A',
          phrase_list: 'alpha one',
        },
      ],
    });
    const artifact = [
      {
        filename: 'f.xlsx',
        campaign_id: 'CA-01-LOCAL',
        mode: 'LOCAL',
        group_id: 'grp-b',
        group_name: 'Group B',
        phrase: 'alpha one',
        normalized_phrase: 'alpha one',
        slot_key: 'CA-01-LOCAL|LOCAL|grp-b|alpha one',
        xlsx_row: 16,
      },
    ];
    const result = reconcilePhraseSlotSets(expected, artifact);
    assert.equal(result.missing_slots, 1);
    assert.equal(result.unexpected_slots, 1);
    assert.equal(result.phrase_slot_reconciliation_pass, false);
  });

  it('fails wrong mode assignment', () => {
    const expected = buildExpectedSlotsFromGroupPlan({
      groups: [
        {
          campaign: 'CA-01-LOCAL',
          mode: 'LOCAL',
          group_id: 'grp-a',
          group_name: 'Group A',
          phrase_list: 'alpha one',
        },
      ],
    });
    const artifact = [
      {
        filename: 'f.xlsx',
        campaign_id: 'CA-01-REMOTE',
        mode: 'REMOTE',
        group_id: 'grp-a',
        group_name: 'Group A',
        phrase: 'alpha one',
        normalized_phrase: 'alpha one',
        slot_key: 'CA-01-REMOTE|REMOTE|grp-a|alpha one',
        xlsx_row: 16,
      },
    ];
    const result = reconcilePhraseSlotSets(expected, artifact);
    assert.equal(result.missing_slots, 1);
    assert.equal(result.unexpected_slots, 1);
  });

  it('fails per-campaign mismatch with equal package total', () => {
    const groupPlan = {
      groups: [
        {
          campaign: 'CA-01-LOCAL',
          mode: 'LOCAL',
          group_id: 'grp-a',
          group_name: 'Group A',
          phrase_list: 'alpha one; alpha two',
        },
        {
          campaign: 'CA-01-REMOTE',
          mode: 'REMOTE',
          group_id: 'grp-a',
          group_name: 'Group A',
          phrase_list: 'alpha one',
        },
      ],
    };
    const expected = buildExpectedSlotsFromGroupPlan(groupPlan);
    const artifact = [
      {
        filename: 'local.xlsx',
        campaign_id: 'CA-01-LOCAL',
        mode: 'LOCAL',
        group_id: 'grp-a',
        group_name: 'Group A',
        phrase: 'alpha one',
        normalized_phrase: 'alpha one',
        slot_key: 'CA-01-LOCAL|LOCAL|grp-a|alpha one',
        xlsx_row: 16,
      },
      {
        filename: 'local.xlsx',
        campaign_id: 'CA-01-LOCAL',
        mode: 'LOCAL',
        group_id: 'grp-a',
        group_name: 'Group A',
        phrase: 'alpha two',
        normalized_phrase: 'alpha two',
        slot_key: 'CA-01-LOCAL|LOCAL|grp-a|alpha two',
        xlsx_row: 17,
      },
      {
        filename: 'remote.xlsx',
        campaign_id: 'CA-01-REMOTE',
        mode: 'REMOTE',
        group_id: 'grp-a',
        group_name: 'Group A',
        phrase: 'alpha two',
        normalized_phrase: 'alpha two',
        slot_key: 'CA-01-REMOTE|REMOTE|grp-a|alpha two',
        xlsx_row: 16,
      },
    ];
    const result = reconcilePhraseSlotSets(expected, artifact);
    assert.equal(result.authority_phrase_slots, 3);
    assert.equal(result.artifact_phrase_slots, 3);
    assert.equal(result.phrase_slot_delta, 0);
    assert.equal(result.phrase_slot_reconciliation_pass, false);
    assert.equal(result.missing_slots, 1);
    assert.equal(result.unexpected_slots, 1);
  });
});

describe('release-gate phrase-slot enforcement', () => {
  it('fails gate on phrase-slot mismatch (926 vs 924 pattern)', async () => {
    const dir = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'release-gate-phrase-mismatch');
    const groupPlan = {
      groups: Array.from({ length: 4 }, (_, i) => ({
        campaign: i < 2 ? 'CA-01-LOCAL' : 'CA-01-REMOTE',
        mode: i < 2 ? 'LOCAL' : 'REMOTE',
        group_id: 'grp-a',
        group_name: 'Group A',
        phrase_list: `slot ${i}`,
      })),
    };
    const { localFile, remoteFile, groupPlanPath, archPath, receiptPath } = await writeGatePackage(dir, {
      authoritySlots: 4,
      groupPlan,
      artifactPhrases: {
        local: [{ phrase: 'slot 0', ad: true }, { phrase: 'slot 1' }],
        remote: [{ phrase: 'slot 2', ad: true }],
      },
    });

    const result = await runReleaseGate({
      project_id: 'synthetic-test',
      package_root: dir,
      authority_path: path.join(dir, 'authority-summary.json'),
      receipt_path: receiptPath,
      group_plan_path: groupPlanPath,
      architecture_path: archPath,
      xlsx_files: [localFile, remoteFile],
      guardOptions: { skipVolumeCheck: true },
    });

    assert.equal(result.status, GATE_STATUS.FAIL);
    assert.ok(result.violations.some((v) => v.code === 'PHRASE_SLOT_RECONCILIATION_FAIL'));
    assert.equal(result.phrase_slot_reconciliation?.missing_slots, 1);
  });

  it('passes gate on exact phrase-slot match', async () => {
    const dir = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'release-gate-phrase-match');
    const { localFile, remoteFile, groupPlanPath, archPath, receiptPath } = await writeGatePackage(dir, {});

    const result = await runReleaseGate({
      project_id: 'synthetic-test',
      package_root: dir,
      authority_path: path.join(dir, 'authority-summary.json'),
      receipt_path: receiptPath,
      group_plan_path: groupPlanPath,
      architecture_path: archPath,
      xlsx_files: [localFile, remoteFile],
      guardOptions: { skipVolumeCheck: true },
    });

    assert.equal(result.status, GATE_STATUS.PASS);
    assert.equal(result.phrase_slot_reconciliation?.phrase_slot_reconciliation_pass, true);
  });
});
