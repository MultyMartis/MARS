import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import {
  cloneRowXml,
  extendSheetForExport,
  extractRowXml,
  shouldClearEmbeddedCampaignNegatives,
  translateMetadataPatches,
} from '../src/commander-patcher-adapter.mjs';
import { COMMANDER_CALLOUT_DELIMITER, serializeCallouts } from '../src/callout-serializer.mjs';

describe('commander-patcher-adapter helpers', () => {
  it('translates Russian metadata keys to logical keys', () => {
    const out = translateMetadataPatches({
      'Тип кампании:': 'Текстово-графическая кампания',
      'Минус-фразы на кампанию:': '-test',
      'Организация из Яндекс Бизнеса:': '',
    });
    assert.equal(out['campaigns.campaign_type'], 'Текстово-графическая кампания');
    assert.equal(out['campaigns.campaign_negatives'], '-test');
    assert.equal(out['campaigns.organization'], undefined);
  });

  it('detects explicit blank embedded campaign negatives', () => {
    assert.equal(
      shouldClearEmbeddedCampaignNegatives({ 'Минус-фразы на кампанию:': '' }),
      true,
    );
    assert.equal(
      shouldClearEmbeddedCampaignNegatives({ 'Минус-фразы на кампанию:': '-test' }),
      false,
    );
    assert.equal(shouldClearEmbeddedCampaignNegatives({}), false);
  });

  it('extends sheet rows for large exports', () => {
    const proto = '<worksheet><sheetData><row r="16"><c r="A16"/></row></sheetData></worksheet>';
    const extended = extendSheetForExport(proto, 5, 16);
    assert.ok(extended.includes('r="17"'));
    assert.ok(extended.includes('r="20"'));
  });

  it('clones row xml with new row number', () => {
    const row = '<row r="16"><c r="A16" t="str"><v>test</v></c></row>';
    const cloned = cloneRowXml(row, 16, 20);
    assert.ok(cloned.includes('r="20"'));
    assert.ok(cloned.includes('A20'));
  });

  it('extracts row xml by number', () => {
    const sheet = '<sheetData><row r="16"><c/></row><row r="17"><c/></row></sheetData>';
    assert.ok(extractRowXml(sheet, 16).includes('r="16"'));
  });

  it('fastlink clearing uses empty strings at patch boundary', () => {
    const fillRow = {
      fastlink_titles: '',
      fastlink_descriptions: '',
      fastlink_urls: '',
    };
    assert.equal(fillRow.fastlink_titles, '');
    assert.equal(fillRow.fastlink_descriptions, '');
    assert.equal(fillRow.fastlink_urls, '');
  });

  it('callout serialization uses authentic Commander delimiter', () => {
    const serialized = serializeCallouts(['A', 'B']);
    assert.equal(serialized, `A${COMMANDER_CALLOUT_DELIMITER}B`);
  });
});
