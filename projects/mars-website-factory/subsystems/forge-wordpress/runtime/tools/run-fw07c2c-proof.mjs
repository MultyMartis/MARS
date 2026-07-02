#!/usr/bin/env node
/**
 * FP-0002 FW-07C-2C — controlled filesystem delivery proof orchestrator.
 */
import { execSync, spawnSync } from 'node:child_process';
import crypto from 'node:crypto';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { captureDirectoryManifest, sha256Text, aggregateHash } from '../src/delivery/filesystem-manifest.mjs';
import { validateDeliveryTarget, validateVolumeLabel, DELIVERY_SURFACES, FP0002_SITE_ROOT, FP0002_SITE_ID, DENIED_DELIVERY_TARGETS } from '../src/delivery/delivery-path-policy.mjs';
import { planDelivery, DELIVERY_MODE } from '../src/delivery/delivery-planner.mjs';
import { applyAdditiveDelivery } from '../src/delivery/delivery-apply.mjs';
import { rollbackProofFiles } from '../src/delivery/delivery-rollback.mjs';
import { checkEquivalence } from '../src/delivery/delivery-equivalence.mjs';
import { createCheckpoint } from '../src/delivery/delivery-checkpoint.mjs';
import { validatePostDelivery } from '../src/delivery/delivery-validator.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO = 'X:\\AI MARS';
const LOCALHOST = 'X:\\MARS-Localhost';
const SITE_ROOT = path.join(LOCALHOST, 'sites', 'wordpress', 'projects', 'shpigovsky');
const SOURCE_ROOT = path.join(REPO, 'workspaces', 'website-factory-operations', 'FP-0002-SHPIGOVSKY', 'WORDPRESS');
const WP_CMD = path.join(LOCALHOST, 'tools', 'wp-cli', 'wp.cmd');
const MYSQL_BIN = path.join(LOCALHOST, 'laragon', 'bin', 'mysql', 'mysql-8.4.3-winx64', 'bin');
const TS = new Date().toISOString().replace(/[-:]/g, '').replace(/\.\d+Z$/, 'Z');
const PROOF_UUID = crypto.randomUUID();
const BUILD_ID = `fw07c2c-${TS}`;
const CHECKPOINT_ROOT = path.join(LOCALHOST, 'backups', 'wordpress', 'projects', 'shpigovsky', `fw07c2c-filesystem-delivery-pre-${TS}`);
const REPORT_ROOT = path.join(REPO, 'projects', 'mars-website-factory', 'subsystems', 'forge-wordpress', 'runtime', 'reports', 'fp0002-fw07c2c-proof');
const RECEIPTS = path.join(REPORT_ROOT, 'receipts');

const THEME_RT = path.join(SITE_ROOT, 'wp-content', 'themes', 'shpigovsky');
const PLUGIN_RT = path.join(SITE_ROOT, 'wp-content', 'plugins', 'shpigovsky-core');
const ACF_RT = path.join(SITE_ROOT, 'wp-content', 'acf-json');

const PROOF_THEME_REL = `.forge-proof\\fw07c2c-theme-${PROOF_UUID}.txt`;
const PROOF_PLUGIN_REL = `.forge-proof\\fw07c2c-plugin-${PROOF_UUID}.txt`;
const PROOF_ACF_NAME = `fw07c2c-acf-${PROOF_UUID}.proof.json`;

const summary = { proof_uuid: PROOF_UUID, build_id: BUILD_ID, started_at: new Date().toISOString(), steps: {} };

function writeReceipt(name, data) {
  fs.mkdirSync(RECEIPTS, { recursive: true });
  const p = path.join(RECEIPTS, name);
  fs.writeFileSync(p, JSON.stringify(data, null, 2), 'utf8');
  return p;
}

function getVolumeLabel() {
  const out = execSync('powershell -NoProfile -Command "(Get-Volume -DriveLetter X).FileSystemLabel"', { encoding: 'utf8' });
  return out.trim();
}

function wp(...args) {
  const env = { ...process.env, PATH: `${MYSQL_BIN};${process.env.PATH}` };
  const proc = spawnSync(`"${WP_CMD}"`, args, { cwd: SITE_ROOT, encoding: 'utf8', env, shell: true });
  if (proc.status !== 0) throw new Error(`wp ${args.join(' ')} failed: ${proc.stderr || proc.stdout}`);
  return proc.stdout.trim();
}

function httpStatus(url) {
  const proc = spawnSync('curl', ['-s', '-o', 'NUL', '-w', '%{http_code}', url], { encoding: 'utf8', shell: true });
  return proc.stdout.trim();
}

function copyDir(src, dest, exclude = []) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const s = path.join(src, entry.name);
    const d = path.join(dest, entry.name);
    if (exclude.includes(entry.name)) continue;
    if (entry.isDirectory()) copyDir(s, d, exclude);
    else fs.copyFileSync(s, d);
  }
}

function adoptFoundationSource() {
  const themeSrc = path.join(SOURCE_ROOT, 'theme', 'shpigovsky');
  const pluginSrc = path.join(SOURCE_ROOT, 'plugins', 'shpigovsky-core');
  const acfSrc = path.join(SOURCE_ROOT, 'acf-json');
  copyDir(THEME_RT, themeSrc);
  copyDir(PLUGIN_RT, pluginSrc);
  if (fs.existsSync(ACF_RT)) {
    fs.mkdirSync(acfSrc, { recursive: true });
    for (const f of fs.readdirSync(ACF_RT)) {
      if (f === '.gitkeep') fs.copyFileSync(path.join(ACF_RT, f), path.join(acfSrc, f));
    }
  } else {
    fs.mkdirSync(acfSrc, { recursive: true });
    fs.writeFileSync(path.join(acfSrc, '.gitkeep'), '');
  }
}

function createProofFixturePackage() {
  const fixtureRoot = path.join(SOURCE_ROOT, 'delivery', 'fixtures', 'fw07c2c', BUILD_ID);
  fs.mkdirSync(fixtureRoot, { recursive: true });

  const themeProof = `FW-07C-2C THEME DELIVERY PROOF\nUUID: ${PROOF_UUID}\nTARGET: shpigovsky theme\nDISPOSABLE: true\n`;
  const pluginProof = `FW-07C-2C PROJECT PLUGIN DELIVERY PROOF\nUUID: ${PROOF_UUID}\nTARGET: shpigovsky-core\nDISPOSABLE: true\n`;
  const acfProof = JSON.stringify({
    proof_type: 'FW-07C-2C',
    uuid: PROOF_UUID,
    target: 'acf-json',
    disposable: true,
    wordpress_loadable_acf_group: false,
  }, null, 2);

  const themeSrc = path.join(fixtureRoot, 'theme-proof.txt');
  const pluginSrc = path.join(fixtureRoot, 'plugin-proof.txt');
  const acfSrc = path.join(fixtureRoot, 'acf-proof.json');
  fs.writeFileSync(themeSrc, themeProof, 'utf8');
  fs.writeFileSync(pluginSrc, pluginProof, 'utf8');
  fs.writeFileSync(acfSrc, acfProof, 'utf8');

  return {
    fixtureRoot,
    themeSrc,
    pluginSrc,
    acfSrc,
    themeDest: path.join(THEME_RT, PROOF_THEME_REL),
    pluginDest: path.join(PLUGIN_RT, PROOF_PLUGIN_REL),
    acfDest: path.join(ACF_RT, PROOF_ACF_NAME),
    themeHash: sha256Text(themeProof),
    pluginHash: sha256Text(pluginProof),
    acfHash: sha256Text(acfProof),
  };
}

function captureWpState() {
  const siteurl = wp('option', 'get', 'siteurl');
  const theme = wp('theme', 'list', '--status=active', '--field=name');
  const pluginsRaw = wp('plugin', 'list', '--status=active', '--format=json');
  const plugins = JSON.parse(pluginsRaw || '[]');
  const pages = wp('post', 'list', '--post_type=page', '--format=count');
  const posts = wp('post', 'list', '--post_type=post', '--format=count');
  let acfGroups = 0;
  try {
    const raw = wp('eval', 'echo function_exists("acf_get_field_groups") ? count(acf_get_field_groups()) : 0;');
    acfGroups = Number(raw);
  } catch {
    acfGroups = 0;
  }

  return {
    frontend_http: httpStatus('http://shpigovsky.test/'),
    wp_login_http: httpStatus('http://shpigovsky.test/wp-login.php'),
    siteurl,
    active_theme: theme,
    active_plugins: plugins.map((p) => p.name),
    pages_count: Number(pages),
    posts_count: Number(posts),
    acf_group_count: acfGroups,
    wpilot_write_enabled: false,
  };
}

function main() {
  console.log('=== FP-0002 FW-07C-2C Filesystem Delivery Proof ===');
  console.log(`UUID: ${PROOF_UUID}`);

  // Preflight
  const volumeLabel = getVolumeLabel();
  const volumeCheck = validateVolumeLabel(volumeLabel);
  if (!volumeCheck.allowed) throw new Error(`Volume mismatch: ${volumeLabel}`);
  summary.volume = { label: volumeLabel, result: 'PASS' };

  const resolved = fs.realpathSync.native(SITE_ROOT);
  if (resolved !== SITE_ROOT) throw new Error(`Runtime path mismatch: ${resolved}`);
  summary.runtime_identity = { site_root: SITE_ROOT, resolved, result: 'PASS' };

  // Adopt foundation source
  adoptFoundationSource();
  summary.foundation_adopted = true;

  // Baselines
  const themeBaseline = captureDirectoryManifest(THEME_RT);
  const pluginBaseline = captureDirectoryManifest(PLUGIN_RT);
  const acfBaseline = captureDirectoryManifest(ACF_RT);
  const wpStateBefore = captureWpState();
  writeReceipt('runtime-baseline-before.json', { theme: themeBaseline, plugin: pluginBaseline, acf_json: acfBaseline, wordpress: wpStateBefore });
  summary.steps.baseline = 'PASS';

  // Checkpoint
  createCheckpoint({
    checkpoint_root: CHECKPOINT_ROOT,
    surfaces: [
      { key: 'theme', source_dir: THEME_RT, snapshot_subdir: 'theme' },
      { key: 'plugin', source_dir: PLUGIN_RT, snapshot_subdir: 'plugin' },
      { key: 'acf_json', source_dir: ACF_RT, snapshot_subdir: 'acf-json' },
    ],
    rollback_instructions: {
      mode: 'exact_owned_proof_files_only',
      proof_uuid: PROOF_UUID,
      no_tree_restore: true,
    },
    safe_runtime_state: wpStateBefore,
  });
  summary.steps.checkpoint = { root: CHECKPOINT_ROOT, result: 'PASS' };

  // Negative path validation
  const negTargets = [
    `${SITE_ROOT}\\wp-admin`,
    `${SITE_ROOT}\\wp-includes`,
    `${SITE_ROOT}\\wp-content\\plugins\\metacode-wpilot`,
    `${SITE_ROOT}\\wp-content\\mu-plugins`,
    `${SITE_ROOT}\\wp-content\\uploads`,
    `${SITE_ROOT}\\wp-config.php`,
    'X:\\MARS-Localhost\\sites\\wordpress\\projects\\',
    'X:\\MARS-Localhost\\',
    'C:\\',
    'D:\\',
    'E:\\',
    'X:\\MARS-Localhost\\sites\\wordpress\\projects\\other-project',
    `${SITE_ROOT}\\wp-content\\themes\\..\\..\\wp-config.php`,
  ];
  const negResults = negTargets.map((t) => ({
    target: t,
    expected: 'DENIED',
    actual: validateDeliveryTarget(t).allowed ? 'ALLOWED' : 'DENIED',
    write_attempted: false,
    result: validateDeliveryTarget(t).allowed ? 'FAIL' : 'PASS',
  }));
  writeReceipt('negative-path-validation.json', negResults);
  if (negResults.some((r) => r.result === 'FAIL')) throw new Error('Negative path validation failed');
  summary.steps.negative_paths = 'PASS';

  // Unknown file fail-closed (isolated fixture)
  const isoTmp = fs.mkdtempSync(path.join(os.tmpdir(), 'fw07c2c-unknown-'));
  fs.writeFileSync(path.join(isoTmp, 'unexpected.txt'), 'x');
  const isoManifest = captureDirectoryManifest(isoTmp);
  const unknownPlan = planDelivery({
    entries: [{ source_path: path.join(isoTmp, 'new.txt'), destination_path: path.join(isoTmp, 'new.txt') }],
    target_manifest: { root: isoTmp, files: isoManifest.files },
    simulate_mirror: true,
  });
  writeReceipt('unknown-file-fail-closed.json', { fixture: isoTmp, planner: unknownPlan, writes: 0, deletes: 0 });
  fs.rmSync(isoTmp, { recursive: true });
  if (unknownPlan.safe_to_apply) throw new Error('Unknown file conflict should fail closed');
  summary.steps.unknown_file = 'PASS';

  // Proof fixture
  const proof = createProofFixturePackage();

  // Dry-run
  const entries = [
    { source_path: proof.themeSrc, destination_path: proof.themeDest, expected_sha256: proof.themeHash },
    { source_path: proof.pluginSrc, destination_path: proof.pluginDest, expected_sha256: proof.pluginHash },
    { source_path: proof.acfSrc, destination_path: proof.acfDest, expected_sha256: proof.acfHash },
  ];
  const dryPlan = planDelivery({ entries, mode: DELIVERY_MODE.ADDITIVE_ONLY });
  writeReceipt('dry-run-plan.json', { uuid: PROOF_UUID, plan: dryPlan });
  if (!dryPlan.safe_to_apply || dryPlan.summary.modifies > 0 || dryPlan.summary.deletes > 0) {
    throw new Error(`Dry-run not safe: ${JSON.stringify(dryPlan.summary)}`);
  }
  summary.steps.dry_run = 'PASS';

  // Apply
  const applyResult = applyAdditiveDelivery({
    entries,
    mode: DELIVERY_MODE.ADDITIVE_ONLY,
    volume_label: volumeLabel,
    dry_run: false,
  });
  writeReceipt('apply-result.json', applyResult);
  if (!applyResult.applied) throw new Error('Apply failed');
  summary.steps.apply = 'PASS';

  // Post-delivery validation
  const postTheme = validatePostDelivery({
    initial_manifest: themeBaseline,
    current_root: THEME_RT,
    expected_new_files: [{ path: proof.themeDest, expected_hash: proof.themeHash }],
    exclude_from_compare: [],
  });
  const postPlugin = validatePostDelivery({
    initial_manifest: pluginBaseline,
    current_root: PLUGIN_RT,
    expected_new_files: [{ path: proof.pluginDest, expected_hash: proof.pluginHash }],
  });
  const postAcf = validatePostDelivery({
    initial_manifest: acfBaseline,
    current_root: ACF_RT,
    expected_new_files: [{ path: proof.acfDest, expected_hash: proof.acfHash }],
  });
  const wpStateAfter = captureWpState();
  writeReceipt('post-delivery-validation.json', {
    theme: postTheme,
    plugin: postPlugin,
    acf_json: postAcf,
    wordpress: wpStateAfter,
    wordpress_unchanged:
      wpStateBefore.active_theme === wpStateAfter.active_theme &&
      wpStateBefore.pages_count === wpStateAfter.pages_count &&
      wpStateBefore.posts_count === wpStateAfter.posts_count &&
      wpStateBefore.acf_group_count === wpStateAfter.acf_group_count,
  });
  if (!postTheme.passed || !postPlugin.passed || !postAcf.passed) throw new Error('Post-delivery validation failed');
  summary.steps.post_validation = 'PASS';

  // Rollback
  const rollbackResult = rollbackProofFiles({
    proof_files: [
      { path: proof.themeDest, expected_hash: proof.themeHash, expected_uuid: PROOF_UUID },
      { path: proof.pluginDest, expected_hash: proof.pluginHash, expected_uuid: PROOF_UUID },
      { path: proof.acfDest, expected_hash: proof.acfHash, expected_uuid: PROOF_UUID },
    ],
    expected_uuid: PROOF_UUID,
    remove_empty_proof_dirs: true,
  });
  writeReceipt('rollback-result.json', rollbackResult);
  if (!rollbackResult.success) throw new Error('Rollback failed');
  summary.steps.rollback = 'PASS';

  // Final equivalence
  const themeFinal = captureDirectoryManifest(THEME_RT);
  const pluginFinal = captureDirectoryManifest(PLUGIN_RT);
  const acfFinal = captureDirectoryManifest(ACF_RT);
  const equivTheme = checkEquivalence(themeBaseline, themeFinal, [proof.themeDest]);
  const equivPlugin = checkEquivalence(pluginBaseline, pluginFinal, [proof.pluginDest]);
  const equivAcf = checkEquivalence(acfBaseline, acfFinal, [proof.acfDest]);
  writeReceipt('final-equivalence.json', { theme: equivTheme, plugin: equivPlugin, acf_json: equivAcf });
  if (equivTheme.verdict !== 'FINAL_FILESYSTEM_STATE_EQUALS_INITIAL_STATE') throw new Error('Theme equivalence failed');
  if (equivPlugin.verdict !== 'FINAL_FILESYSTEM_STATE_EQUALS_INITIAL_STATE') throw new Error('Plugin equivalence failed');
  if (equivAcf.verdict !== 'FINAL_FILESYSTEM_STATE_EQUALS_INITIAL_STATE') throw new Error('ACF equivalence failed');
  summary.steps.final_equivalence = 'PASS';

  summary.completed_at = new Date().toISOString();
  summary.verdict = 'PASS';
  fs.mkdirSync(REPORT_ROOT, { recursive: true });
  fs.writeFileSync(path.join(REPORT_ROOT, 'fw07c2c-proof-summary.json'), JSON.stringify(summary, null, 2), 'utf8');

  console.log('\n=== PROOF COMPLETE: PASS ===');
  console.log(JSON.stringify(summary, null, 2));
}

try {
  main();
} catch (err) {
  summary.verdict = 'FAIL';
  summary.error = err.message;
  fs.mkdirSync(REPORT_ROOT, { recursive: true });
  fs.writeFileSync(path.join(REPORT_ROOT, 'fw07c2c-proof-summary.json'), JSON.stringify(summary, null, 2), 'utf8');
  console.error('PROOF FAILED:', err.message);
  process.exit(1);
}
