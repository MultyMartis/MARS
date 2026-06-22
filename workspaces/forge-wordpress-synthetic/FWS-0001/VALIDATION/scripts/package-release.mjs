import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createHash } from 'crypto';
import { execSync } from 'child_process';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '../..');
const releaseDir = path.join(root, 'RELEASE', 'FWS-0001-RC1');

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

function copyAcfJson(dest) {
  const src = path.join(root, 'WORDPRESS', 'acf-json');
  const target = path.join(dest, 'acf-json');
  fs.mkdirSync(target, { recursive: true });
  if (fs.existsSync(src)) {
    for (const f of fs.readdirSync(src)) {
      fs.copyFileSync(path.join(src, f), path.join(target, f));
    }
  }
  fs.writeFileSync(
    path.join(dest, 'ACF-COMPATIBILITY-NOTE.md'),
    '# ACF Compatibility\n\nACF Pro not available in FW-05. Global options use Settings API. ACF Free JSON provided for home/service fields.\n'
  );
}

function main() {
  const themeSrc = path.join(root, 'WORDPRESS', 'theme-source', 'fws-synthetic');
  const pluginSrc = path.join(root, 'WORDPRESS', 'functionality-plugin', 'fws-synthetic-core');
  fs.mkdirSync(releaseDir, { recursive: true });

  const themeZip = path.join(releaseDir, 'fws-synthetic-theme.zip');
  const pluginZip = path.join(releaseDir, 'fws-synthetic-core.zip');
  zipDir(themeSrc, themeZip);
  zipDir(pluginSrc, pluginZip);
  copyAcfJson(releaseDir);

  let gitRev = 'unknown';
  try {
    gitRev = execSync('git rev-parse HEAD', { cwd: path.resolve(root, '../../..'), encoding: 'utf8' }).trim();
  } catch (_) {}

  const checksums = {
    'fws-synthetic-theme.zip': sha256(themeZip),
    'fws-synthetic-core.zip': sha256(pluginZip),
  };

  const manifest = {
    release: 'FWS-0001-RC1',
    date: '2026-06-22',
    git_revision: gitRev,
    synthetic: true,
    production: false,
    packages: Object.keys(checksums),
    checksums_sha256: checksums,
  };

  fs.writeFileSync(path.join(releaseDir, 'release-manifest.json'), JSON.stringify(manifest, null, 2));
  fs.writeFileSync(
    path.join(releaseDir, 'SOURCE-MANIFEST.md'),
    `# FWS-0001-RC1 Source Manifest\n\n- Theme: theme-source/fws-synthetic\n- Plugin: functionality-plugin/fws-synthetic-core\n- Git: ${gitRev}\n`
  );
  console.log('Release packaged at', releaseDir);
}

main();
