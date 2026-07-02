#!/usr/bin/env node
/**
 * FW-07C-2C — Delivery capability tests (22 cases minimum).
 */
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  validateDeliveryTarget,
  DELIVERY_SURFACES,
  FP0002_SITE_ROOT,
  DENIED_DELIVERY_TARGETS,
} from '../src/delivery/delivery-path-policy.mjs';
import { planDelivery, DELIVERY_MODE } from '../src/delivery/delivery-planner.mjs';
import { applyAdditiveDelivery } from '../src/delivery/delivery-apply.mjs';
import { rollbackProofFiles } from '../src/delivery/delivery-rollback.mjs';
import { captureDirectoryManifest, sha256Text } from '../src/delivery/filesystem-manifest.mjs';
import { DELIVERY_REASON_CODES as RC } from '../src/delivery/delivery-reason-codes.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
let passed = 0;
let failed = 0;

function test(name, fn) {
  try {
    fn();
    passed += 1;
    console.log(`PASS ${name}`);
  } catch (err) {
    failed += 1;
    console.error(`FAIL ${name}: ${err.message}`);
  }
}

// 1-3: exact roots accepted
test('exact theme root accepted', () => {
  const r = validateDeliveryTarget(path.join(DELIVERY_SURFACES.theme.target_root, 'test.txt'));
  assert.equal(r.allowed, true);
  assert.equal(r.surface, 'theme');
});

test('exact Shpigovsky Core root accepted', () => {
  const r = validateDeliveryTarget(path.join(DELIVERY_SURFACES.plugin.target_root, 'test.txt'));
  assert.equal(r.allowed, true);
  assert.equal(r.surface, 'plugin');
});

test('exact ACF JSON root accepted', () => {
  const r = validateDeliveryTarget(path.join(DELIVERY_SURFACES.acf_json.target_root, 'proof.json'));
  assert.equal(r.allowed, true);
  assert.equal(r.surface, 'acf_json');
});

// 4-8: denied roots
test('WPilot plugin root rejected', () => {
  const r = validateDeliveryTarget(`${FP0002_SITE_ROOT}\\wp-content\\plugins\\metacode-wpilot\\x.php`);
  assert.equal(r.allowed, false);
});

test('MU-plugin root rejected', () => {
  const r = validateDeliveryTarget(`${FP0002_SITE_ROOT}\\wp-content\\mu-plugins\\x.php`);
  assert.equal(r.allowed, false);
});

test('uploads root rejected', () => {
  const r = validateDeliveryTarget(`${FP0002_SITE_ROOT}\\wp-content\\uploads\\x.jpg`);
  assert.equal(r.allowed, false);
});

test('WordPress core roots rejected', () => {
  assert.equal(validateDeliveryTarget(`${FP0002_SITE_ROOT}\\wp-admin\\index.php`).allowed, false);
  assert.equal(validateDeliveryTarget(`${FP0002_SITE_ROOT}\\wp-includes\\version.php`).allowed, false);
});

test('wp-config.php rejected', () => {
  const r = validateDeliveryTarget(`${FP0002_SITE_ROOT}\\wp-config.php`);
  assert.equal(r.allowed, false);
});

// 9-12: parent/sibling/legacy/traversal
test('parent project root rejected', () => {
  const r = validateDeliveryTarget('X:\\MARS-Localhost\\sites\\wordpress\\projects\\');
  assert.equal(r.allowed, false);
});

test('sibling project root rejected', () => {
  const r = validateDeliveryTarget('X:\\MARS-Localhost\\sites\\wordpress\\projects\\other-site\\file.txt');
  assert.equal(r.allowed, false);
});

test('C/D/E legacy roots rejected', () => {
  for (const root of ['C:\\', 'D:\\', 'E:\\']) {
    const r = validateDeliveryTarget(root + 'test.txt');
    assert.equal(r.allowed, false, root);
  }
});

test('traversal rejected', () => {
  const r = validateDeliveryTarget(`${FP0002_SITE_ROOT}\\wp-content\\themes\\..\\..\\wp-config.php`);
  assert.equal(r.allowed, false);
});

// 13: reparse - use policy check on valid path (escape tested in FW-07C-1)
test('reparse validation attached to allowed path', () => {
  const r = validateDeliveryTarget(DELIVERY_SURFACES.theme.target_root + '\\style.css');
  assert.ok(r.reparse);
});

// 14-15: overwrite/delete denied in additive mode
test('overwrite denied in additive mode', () => {
  const dst = path.join(DELIVERY_SURFACES.theme.target_root, 'style.css');
  const src = path.join(os.tmpdir(), `fw07c2c-src-${Date.now()}.txt`);
  fs.writeFileSync(src, 'new');
  const plan = planDelivery({
    entries: [{ source_path: src, destination_path: dst }],
    mode: DELIVERY_MODE.ADDITIVE_ONLY,
  });
  assert.equal(plan.summary.modifies, 1);
  assert.equal(plan.safe_to_apply, false);
  fs.unlinkSync(src);
});

test('delete denied in additive mode', () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'fw07c2c-'));
  fs.writeFileSync(path.join(tmp, 'unknown.txt'), 'x');
  const manifest = captureDirectoryManifest(tmp);
  const plan = planDelivery({
    entries: [],
    mode: DELIVERY_MODE.ADDITIVE_ONLY,
    target_manifest: { root: tmp, files: manifest.files },
    simulate_mirror: true,
  });
  assert.ok(plan.reason_codes.includes(RC.DL_UNKNOWN_FILE_CONFLICT));
  assert.equal(plan.safe_to_apply, false);
  fs.rmSync(tmp, { recursive: true });
});

// 16: unknown file conflict
test('unknown file conflict fails closed', () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'fw07c2c-'));
  fs.writeFileSync(path.join(tmp, 'extra.txt'), 'unexpected');
  const manifest = captureDirectoryManifest(tmp);
  const plan = planDelivery({
    entries: [{ source_path: path.join(tmp, 'new.txt'), destination_path: path.join(tmp, 'new.txt') }],
    target_manifest: { root: tmp, files: manifest.files },
    simulate_mirror: true,
  });
  assert.ok(plan.reason_codes.includes(RC.DL_UNKNOWN_FILE_CONFLICT));
  fs.rmSync(tmp, { recursive: true });
});

// 17-19: hash/exists failures
test('source hash mismatch fails closed', () => {
  const dst = path.join(DELIVERY_SURFACES.acf_json.target_root, `fw07c2c-hash-test-${Date.now()}.json`);
  const src = path.join(os.tmpdir(), `fw07c2c-src-hash-${Date.now()}.txt`);
  fs.writeFileSync(src, 'content');
  const plan = planDelivery({
    entries: [{ source_path: src, destination_path: dst, expected_sha256: 'deadbeef' }],
    mode: DELIVERY_MODE.ADDITIVE_ONLY,
  });
  assert.ok(plan.reason_codes.includes(RC.DL_SOURCE_HASH_MISMATCH));
  fs.unlinkSync(src);
});

test('destination already exists fails closed', () => {
  const dst = path.join(DELIVERY_SURFACES.theme.target_root, 'style.css');
  const src = path.join(os.tmpdir(), `fw07c2c-exists-${Date.now()}.txt`);
  fs.writeFileSync(src, 'x');
  const plan = planDelivery({
    entries: [{ source_path: src, destination_path: dst }],
    mode: DELIVERY_MODE.ADDITIVE_ONLY,
  });
  assert.equal(plan.safe_to_apply, false);
  fs.unlinkSync(src);
});

test('package hash mismatch equivalent via expected_sha256', () => {
  const dst = path.join(DELIVERY_SURFACES.acf_json.target_root, `fw07c2c-pkg-${Date.now()}.json`);
  const src = path.join(os.tmpdir(), `fw07c2c-pkg-src-${Date.now()}.txt`);
  fs.writeFileSync(src, 'a');
  const plan = planDelivery({
    entries: [{ source_path: src, destination_path: dst, expected_sha256: '0'.repeat(64) }],
  });
  assert.ok(plan.reason_codes.includes(RC.DL_SOURCE_HASH_MISMATCH));
  fs.unlinkSync(src);
});

// 20: rollback
test('exact rollback removes only owned proof files', () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'fw07c2c-'));
  const proofDir = path.join(tmp, '.forge-proof');
  fs.mkdirSync(proofDir);
  const proofFile = path.join(proofDir, 'proof.txt');
  const otherFile = path.join(tmp, 'keep.txt');
  fs.writeFileSync(proofFile, 'proof-content');
  fs.writeFileSync(otherFile, 'keep');
  const hash = sha256Text('proof-content');
  const uuid = 'test-uuid';
  const result = rollbackProofFiles({
    proof_files: [{ path: proofFile, expected_hash: hash, expected_uuid: uuid }],
    expected_uuid: uuid,
    remove_empty_proof_dirs: true,
  });
  assert.equal(result.success, true);
  assert.equal(fs.existsSync(proofFile), false);
  assert.equal(fs.existsSync(otherFile), true);
  assert.equal(fs.existsSync(proofDir), false);
  fs.rmSync(tmp, { recursive: true });
});

// 21: token paths
test('token/secret paths are rejected', () => {
  const r = validateDeliveryTarget('X:\\AI MARS\\local\\tokens\\wpilot-local-shpigovsky.token');
  assert.equal(r.allowed, false);
});

// 22: V9 source/dist never targets
test('V9 source/dist are never runtime delivery targets', () => {
  assert.equal(validateDeliveryTarget('X:\\AI MARS\\workspaces\\fp-0002-shpigovsky-v9\\src\\index.html').allowed, false);
  assert.equal(validateDeliveryTarget('X:\\AI MARS\\workspaces\\fp-0002-shpigovsky-v9\\dist\\index.html').allowed, false);
});

// Negative path table spot-check
test('all denied delivery targets rejected', () => {
  for (const target of DENIED_DELIVERY_TARGETS) {
    if (target.includes('projects\\') && target.endsWith('\\')) continue;
    const r = validateDeliveryTarget(target + (target.endsWith('.php') ? '' : '\\probe.txt'));
    assert.equal(r.allowed, false, target);
  }
});

console.log(`\n=== FW-07C-2C Delivery Tests: ${passed} passed, ${failed} failed ===`);
process.exit(failed > 0 ? 1 : 0);
