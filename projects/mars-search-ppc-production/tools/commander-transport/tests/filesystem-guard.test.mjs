import { describe, it, before, after } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {
  assertApprovedOutputPath,
  assertNoTraversal,
  createGuardContext,
  isUncPath,
  normalizeInputPath,
  resetVolumeLabelCache,
} from '../src/filesystem-guard.mjs';
import { PROJECT_ROOT, SYNTHETIC_TEST_OUTPUT_DIR } from '../src/constants.mjs';

describe('filesystem-guard', () => {
  let context;

  before(() => {
    resetVolumeLabelCache();
    context = createGuardContext({ skipVolumeCheck: true });
  });

  it('rejects UNC paths', () => {
    assert.equal(isUncPath('\\\\server\\share\\file'), true);
    assert.throws(() => normalizeInputPath('\\\\server\\share\\file'));
  });

  it('rejects deprecated drives', () => {
    assert.throws(() => normalizeInputPath('C:\\temp\\out.json'));
    assert.throws(() => normalizeInputPath('D:\\temp\\out.json'));
    assert.throws(() => normalizeInputPath('E:\\temp\\out.json'));
  });

  it('rejects parent traversal outside approved root', () => {
    const inside = path.join(PROJECT_ROOT, 'reports', 'safe.json');
    assert.doesNotThrow(() => assertNoTraversal(inside, PROJECT_ROOT));
    const escape = path.resolve(PROJECT_ROOT, '..', '..', 'outside.json');
    assert.throws(() => assertNoTraversal(escape, PROJECT_ROOT));
  });

  it('enforces FAIL_IF_OUTPUT_EXISTS', () => {
    const dir = path.join(SYNTHETIC_TEST_OUTPUT_DIR, 'guard-test');
    fs.mkdirSync(dir, { recursive: true });
    const file = path.join(dir, 'exists.txt');
    fs.writeFileSync(file, 'x');
    assert.throws(() => assertApprovedOutputPath(file, context, { skipVolumeCheck: true }));
    fs.unlinkSync(file);
    assert.doesNotThrow(() =>
      assertApprovedOutputPath(file, context, { skipVolumeCheck: true })
    );
    if (fs.existsSync(file)) fs.unlinkSync(file);
  });

  it('abstracts volume identity when label matches', async () => {
    const { getVolumeLabel } = await import('../src/filesystem-guard.mjs');
    const label = getVolumeLabel('X');
    assert.equal(label, 'AI WS');
  });
});
