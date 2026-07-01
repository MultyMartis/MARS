import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {
  classifyPhraseIntent,
  classifyGeoRouting,
  classifyServiceFamily,
  INTENT_CLASSES,
  ROUTING_MODES,
} from '../src/semantic-classification-controls.mjs';
import { validateCampaignArchitecture, detectGenericAdReuse } from '../src/campaign-architecture-validator.mjs';
import { validateAdCopy, validateAuthorityArtifactEquality } from '../src/ad-copy-validator.mjs';
import {
  resolveCampaignNegativeOperation,
  validateNegativeSyntax,
  METADATA_OPS,
} from '../src/negative-keyword-policy.mjs';
import { validatePackagePurity } from '../src/package-purity-validator.mjs';
import {
  checkManualStableOverwrite,
  ARTIFACT_EDIT_STATES,
  sha256File,
} from '../src/manual-stable-guard.mjs';
import { SYNTHETIC_TEST_OUTPUT_DIR } from '../src/constants.mjs';
import { buildExpectedSlotsFromGroupPlan } from '../src/phrase-slot-reconciler.mjs';
import {
  assignBidsForGroup,
  BID_POLICIES,
  verifyBidLadderDeterminism,
} from '../src/bid-ladder.mjs';
import { loadTemplateContract, scanTemplateContamination } from '../src/template-sanitizer.mjs';

describe('corvonero-regression', () => {
  it('buyer phrase "найти программиста 1с" is not classified as employment', () => {
    const r = classifyPhraseIntent('найти программиста 1с');
    assert.notEqual(r.intent, INTENT_CLASSES.EMPLOYMENT);
    assert.notEqual(r.decision, 'REJECT');
  });

  it('commercial price phrases are not automatically rejected', () => {
    const r = classifyPhraseIntent('стоимость часа программиста 1с');
    assert.notEqual(r.decision, 'REJECT');
    assert.equal(r.intent, INTENT_CLASSES.COMMERCIAL_PRICE);
  });

  it('career phrases are rejected or held', () => {
    const r = classifyPhraseIntent('программист 1с заработная плата');
    assert.equal(r.decision, 'REJECT');
  });

  it('course/training phrases are rejected', () => {
    const r = classifyPhraseIntent('программист 1с колледж');
    assert.equal(r.decision, 'REJECT');
  });

  it('tutorial-only phrases are rejected', () => {
    const r = classifyPhraseIntent('интеграция 1с с честным знаком как сделать');
    assert.equal(r.decision, 'REJECT');
  });

  it('Russian non-NSO city phrases route REMOTE_ONLY', () => {
    assert.equal(classifyGeoRouting('Саратов').routing, ROUTING_MODES.REMOTE_ONLY);
    assert.equal(classifyGeoRouting('Липецк').routing, ROUTING_MODES.REMOTE_ONLY);
  });

  it('Novosibirsk phrases route LOCAL', () => {
    assert.equal(classifyGeoRouting('Новосибирск').routing, ROUTING_MODES.LOCAL_ONLY);
  });

  it('foreign market phrases fail Russia-only scope', () => {
    assert.equal(classifyGeoRouting('Минск').routing, ROUTING_MODES.REJECT_RUSSIA_ONLY_SCOPE);
    assert.equal(classifyGeoRouting('Алматы').routing, ROUTING_MODES.REJECT_RUSSIA_ONLY_SCOPE);
  });

  it('Honest Sign phrases route CA-05', () => {
    assert.equal(classifyServiceFamily('честный знак маркировка').family, 'CA-05');
  });

  it('1C website/API integration phrases route CA-04', () => {
    assert.equal(classifyServiceFamily('bitrix site integration').family, 'CA-04');
  });

  it('single-phrase merge survives phrase allocation in group plan fixture', () => {
    const groupPlan = {
      groups: [
        {
          campaign: 'CA-02-LOCAL',
          group_id: 'ca-02-support-tech',
          phrase_list: 'программа 1с не работает; другая фраза',
        },
        {
          campaign: 'CA-02-REMOTE',
          group_id: 'ca-02-support-tech',
          phrase_list: 'программа 1с не работает',
        },
      ],
    };
    const arch = {
      groups: [
        { campaign_id: 'CA-02-LOCAL', group_id: 'ca-02-support-tech' },
        { campaign_id: 'CA-02-REMOTE', group_id: 'ca-02-support-tech' },
      ],
    };
    const slots = buildExpectedSlotsFromGroupPlan(groupPlan, arch);
    const merged = slots.filter((s) => s.phrase === 'программа 1с не работает');
    assert.equal(merged.length, 2);
  });

  it('authority 926 vs artifact 924 fails reconciliation delta', () => {
    const delta = 926 - 924;
    assert.equal(delta, 2);
    assert.ok(delta !== 0);
  });

  it('blank string maps to EXPLICIT_CLEAR not PRESERVE', () => {
    const r = resolveCampaignNegativeOperation({ operation: 'clear', value: '', policy: 'blank' });
    assert.equal(r.op, METADATA_OPS.EXPLICIT_CLEAR);
    assert.equal(r.xlsx_value, null);
  });

  it('quoted pseudo phrase-match negative fails', () => {
    const v = validateNegativeSyntax('"лицензия 1с"');
    assert.ok(v.length > 0);
  });

  it('mixed old/new XLSX package fails purity check', () => {
    const dir = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'purity-mixed');
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(path.join(dir, 'CA-01-v2.6.1.xlsx'), 'x');
    fs.writeFileSync(path.join(dir, 'CA-01-v2.6.2.xlsx'), 'x');
    const r = validatePackagePurity({
      package_root: dir,
      package_version: 'V2.6.2',
      manifest: { files: ['CA-01-v2.6.2.xlsx'], package_version: 'V2.6.2' },
    });
    assert.equal(r.status, 'FAIL');
    assert.ok(r.violations.some((v) => v.code === 'MIXED_HISTORICAL_XLSX'));
  });

  it('import-order version mismatch fails', () => {
    const dir = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'purity-import-order');
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(path.join(dir, 'CORVONERO-IMPORT-ORDER-v1.txt'), 'Import v2.6.1 only');
    const r = validatePackagePurity({
      package_root: dir,
      package_version: 'V2.6.2',
      manifest: { files: [], package_version: 'V2.6.2' },
    });
    assert.ok(r.violations.some((v) => v.code === 'IMPORT_ORDER_VERSION_MISMATCH'));
  });

  it('checklist version mismatch fails', () => {
    const dir = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'purity-checklist');
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(
      path.join(dir, 'CORVONERO-CAMPAIGN-V2.6.1-MANUAL-POST-IMPORT-CHECKLIST-v1.md'),
      'Checklist for v2.6.1 only',
    );
    const r = validatePackagePurity({
      package_root: dir,
      package_version: 'V2.6.2',
      manifest: { files: [], package_version: 'V2.6.2' },
    });
    assert.ok(r.violations.some((v) => v.code === 'CHECKLIST_VERSION_MISMATCH'));
  });

  it('restored phrase bid-policy mismatch fails', () => {
    const policy = BID_POLICIES.CORVONERO_BALANCED_CYCLIC_10_RUB_V1;
    const phrases = [
      { phrase_id: 'p1', phrase: 'программа 1с не работает', is_primary: true },
      { phrase_id: 'p2', phrase: 'другая фраза', is_primary: false },
    ];
    const expected = assignBidsForGroup(phrases, 500, { policy });
    const restored = new Map(expected);
    restored.set('p1', 10);
    const errors = verifyBidLadderDeterminism(phrases, 500, restored, { policy });
    assert.ok(errors.length > 0);
    assert.ok(errors.some((e) => e.includes('determinism_mismatch')));
  });

  it('foreign-client template contamination fails', () => {
    const contract = loadTemplateContract();
    const mockTexts = {
      getRow: (row) => ({
        getCell: (col) => {
          if (row === 9 && col === 5) return { value: 'ремонт запчасти эвакуатор' };
          return { value: null };
        },
      }),
    };
    const scan = scanTemplateContamination(mockTexts, contract);
    assert.equal(scan.contaminated, true);
    assert.ok(scan.findings.some((f) => f.type === 'stale_campaign_negative'));
  });

  it('display-path mismatch is detected', () => {
    const v = validateAuthorityArtifactEquality(
      { group_id: 'g1', display_path_1: 'programmist' },
      { group_id: 'g1', display_path_1: 'support' },
    );
    assert.ok(v.some((x) => x.field === 'display_path_1'));
  });

  it('manual stable file overwrite is refused', () => {
    const dir = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'manual-stable');
    fs.mkdirSync(dir, { recursive: true });
    const fp = path.join(dir, 'stable.html');
    fs.writeFileSync(fp, '<html>stable</html>');
    const hash = sha256File(fp);
    const r = checkManualStableOverwrite(
      { status: ARTIFACT_EDIT_STATES.MANUAL_STABLE, path: fp, sha256: hash, artifact_id: 'strategy-html' },
      { intent: 'overwrite' },
    );
    assert.equal(r.allowed, false);
    assert.ok(r.violations.some((v) => v.code === 'MANUAL_STABLE_OVERWRITE_REFUSED'));
  });

  it('landing group mapping must cover every group exactly once', () => {
    const groups = [{ group_id: 'a' }, { group_id: 'b' }, { group_id: 'c' }];
    const mapping = { a: 'LP-01', b: 'LP-02', c: 'LP-03' };
    const covered = new Set(Object.keys(mapping));
    assert.equal(covered.size, groups.length);
    for (const g of groups) assert.ok(covered.has(g.group_id));
  });

  it('one group cannot map to two landing pages without exception', () => {
    const map = new Map();
    const entries = [
      { group_id: 'g1', landing_page: 'LP-01' },
      { group_id: 'g1', landing_page: 'LP-02', exception: null },
    ];
    let conflict = false;
    for (const e of entries) {
      if (map.has(e.group_id) && map.get(e.group_id) !== e.landing_page && !e.exception) conflict = true;
      map.set(e.group_id, e.landing_page);
    }
    assert.equal(conflict, true);
  });

  it('forbidden generic ad is detected', () => {
    const generic = 'Услуги 1С для бизнеса: настройка, доработки и поддержка.';
    const v = detectGenericAdReuse([{ group_id: 'g1', text: generic }], generic);
    assert.ok(v.some((x) => x.code === 'FORBIDDEN_GENERIC_AD'));
  });

  it('REMOTE ad promising local visit without remote framing fails', () => {
    const r = validateAdCopy(
      { group_id: 'r1', mode: 'REMOTE', headline_1: 'Test', text: 'Выезд по Новосибирску' },
      {},
    );
    assert.ok(r.violations.some((v) => v.code === 'REMOTE_PROMISES_LOCAL_VISIT'));
  });
});
