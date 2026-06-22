import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createHash } from 'crypto';
import { execSync } from 'child_process';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '../..');
const releaseDir = path.join(root, 'RELEASE', 'FWS-0001-RC2');

function sha256(file) {
  const data = fs.readFileSync(file);
  return createHash('sha256').update(data).digest('hex');
}

function zipDir(source, destZip) {
  if (process.platform === 'win32') {
    execSync(
      `powershell -NoProfile -Command "Compress-Archive -Path '${source}\\*' -DestinationPath '${destZip}' -Force"`,
      { stdio: 'inherit' }
    );
  } else {
    execSync(`cd "${source}" && zip -r "${destZip}" .`, { stdio: 'inherit' });
  }
}

function copyDir(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const from = path.join(src, entry.name);
    const to = path.join(dest, entry.name);
    if (entry.isDirectory()) copyDir(from, to);
    else fs.copyFileSync(from, to);
  }
}

function main() {
  const themeSrc = path.join(root, 'WORDPRESS', 'theme-source', 'fws-synthetic');
  const pluginSrc = path.join(root, 'WORDPRESS', 'functionality-plugin', 'fws-synthetic-core');
  const acfSrc = path.join(root, 'WORDPRESS', 'acf-json');
  const reportsSrc = path.join(root, 'VALIDATION', 'reports');

  fs.mkdirSync(releaseDir, { recursive: true });
  const themeZip = path.join(releaseDir, 'fws-synthetic-theme.zip');
  const pluginZip = path.join(releaseDir, 'fws-synthetic-core.zip');
  zipDir(themeSrc, themeZip);
  zipDir(pluginSrc, pluginZip);
  copyDir(acfSrc, path.join(releaseDir, 'acf-json'));

  const reportNames = [
    'FWS-0001-PHPCS-WPCS-LIVE-v1.md',
    'FWS-0001-SECURITY-LIVE-VALIDATION-v1.md',
    'FWS-0001-FUNCTIONAL-LIVE-VALIDATION-v1.md',
    'FWS-0001-ADMIN-UX-LIVE-VALIDATION-v1.md',
    'FWS-0001-WORDPRESS-VISUAL-PARITY-v1.md',
    'FWS-0001-WORDPRESS-CORRECTNESS-LIVE-v1.md',
    'FWS-0001-ACF-COMPATIBILITY-LIVE-v1.md',
  ];
  const evidenceDir = path.join(releaseDir, 'validation-evidence');
  fs.mkdirSync(evidenceDir, { recursive: true });
  for (const name of reportNames) {
    const src = path.join(reportsSrc, name);
    if (fs.existsSync(src)) fs.copyFileSync(src, path.join(evidenceDir, name));
  }

  fs.writeFileSync(
    path.join(releaseDir, 'ACF-COMPATIBILITY-NOTE.md'),
    '# ACF Compatibility (FW-05R live)\n\nACF Pro: NOT PROVEN.\nACF Free 6.8.4 + Settings API global options: PROVEN in MLI-WP-SYN-001.\n'
  );

  const checksums = {
    'fws-synthetic-theme.zip': sha256(themeZip),
    'fws-synthetic-core.zip': sha256(pluginZip),
  };

  const manifest = {
    release: 'FWS-0001-RC2',
    date: '2026-06-23',
    synthetic: true,
    production: false,
    tested_runtime: 'MLI-WP-SYN-001',
    wordpress: '7.0',
    php: '8.3.30',
    mysql: '8.4.3',
    packages: Object.keys(checksums),
    checksums_sha256: checksums,
    known_limitations: [
      'ACF Pro workflow not proven',
      'fws-0001.test hosts elevation pending for operator browser gate',
      'Operator WV6 visual gate pending',
    ],
  };

  fs.writeFileSync(path.join(releaseDir, 'release-manifest.json'), JSON.stringify(manifest, null, 2));
  fs.writeFileSync(
    path.join(releaseDir, 'SOURCE-MANIFEST.md'),
    `# FWS-0001-RC2 Source Manifest\n\n- Theme: WORDPRESS/theme-source/fws-synthetic\n- Plugin: WORDPRESS/functionality-plugin/fws-synthetic-core\n- Runtime: MLI-WP-SYN-001\n- Stage: FW-05R live synthetic validation\n`
  );
  console.log('RC2 packaged at', releaseDir);
}

main();
