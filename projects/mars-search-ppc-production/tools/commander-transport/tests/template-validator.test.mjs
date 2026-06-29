import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { validateTemplate } from '../src/template-validator.mjs';
import { COMMANDER_TEMPLATE_PATH, EXPECTED_TEMPLATE_SHA256 } from '../src/constants.mjs';

describe('template-validator', () => {
  it('validates authentic template SHA and structure', async () => {
    const result = await validateTemplate(COMMANDER_TEMPLATE_PATH, { skipVolumeCheck: true });
    assert.equal(result.ok, true, JSON.stringify(result.failures));
    assert.equal(result.sha256, EXPECTED_TEMPLATE_SHA256);
    assert.equal(result.header_row, 14);
    assert.equal(result.column_count, 78);
    assert.equal(result.required_region, 'Новосибирская область');
  });

  it('rejects SHA mismatch', async () => {
    const result = await validateTemplate(COMMANDER_TEMPLATE_PATH, {
      skipVolumeCheck: true,
      skipPathGuard: true,
    });
    if (!result.ok) {
      assert.equal(result.stop_code, 'STOP — COMMANDER TEMPLATE IDENTITY MISMATCH');
    }
  });
});
