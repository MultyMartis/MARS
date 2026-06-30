import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import {
  resolveMetadataOperation,
  parseMetadataPatchMap,
  toLogicalMetadataPatches,
  shouldClearEmbeddedCampaignNegativesFromResolved,
  METADATA_OPERATIONS,
  METADATA_OPERATION_STATES,
} from '../src/metadata-operation-model.mjs';

describe('metadata-operation-model', () => {
  it('explicit clear via empty string maps to EXPLICIT_CLEAR', () => {
    const op = resolveMetadataOperation('campaign_negatives', '');
    assert.equal(op.state, METADATA_OPERATION_STATES.EXPLICIT_CLEAR);
    assert.equal(op.operation, METADATA_OPERATIONS.CLEAR);
  });

  it('typed clear operation', () => {
    const op = resolveMetadataOperation('campaign_negatives', { operation: 'clear' });
    assert.equal(op.state, METADATA_OPERATION_STATES.EXPLICIT_CLEAR);
  });

  it('preserve operation omits from logical patches', () => {
    const resolved = parseMetadataPatchMap(
      { 'Минус-фразы на кампанию:': '-stale' },
      { 'campaigns.campaign_negatives': { operation: 'preserve' } }
    );
    const patches = toLogicalMetadataPatches(resolved);
    assert.equal(patches['campaigns.campaign_negatives'], undefined);
  });

  it('set operation produces value in logical patches', () => {
    const resolved = parseMetadataPatchMap({
      'Минус-фразы на кампанию:': { operation: 'set', value: '-test' },
    });
    const patches = toLogicalMetadataPatches(resolved);
    assert.equal(patches['campaigns.campaign_negatives'], '-test');
  });

  it('missing property defaults to MISSING not preserve value', () => {
    const resolved = parseMetadataPatchMap({});
    assert.equal(resolved['campaigns.campaign_negatives'].state, METADATA_OPERATION_STATES.MISSING);
  });

  it('blank string must not silently become preserve', () => {
    const resolved = parseMetadataPatchMap({ 'Минус-фразы на кампанию:': '' });
    assert.equal(
      shouldClearEmbeddedCampaignNegativesFromResolved(resolved),
      true
    );
  });

  it('explicit clear organization', () => {
    const resolved = parseMetadataPatchMap({ 'Организация из Яндекс Бизнеса:': '' });
    const op = resolved['campaigns.organization'];
    assert.equal(op.state, METADATA_OPERATION_STATES.EXPLICIT_CLEAR);
  });

  it('set organization value', () => {
    const resolved = parseMetadataPatchMap({
      'Организация из Яндекс Бизнеса:': { operation: 'set', value: '12345' },
    });
    const patches = toLogicalMetadataPatches(resolved);
    assert.equal(patches['campaigns.organization'], '12345');
  });
});
