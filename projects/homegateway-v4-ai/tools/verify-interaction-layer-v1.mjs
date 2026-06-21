import fs from 'fs';

const root = process.argv[2] || 'workspaces/homegateway-v4-ai/v1';
const html = fs.readFileSync(`${root}/dist/index.html`, 'utf8');
const css = fs.readFileSync(`${root}/dist/assets/css/main.css`, 'utf8');

const checks = [
  ['backup README', fs.existsSync('workspaces/homegateway-v4-ai/archive/v1.3-operational-interaction-prepass/ARCHIVE-README.md')],
  ['no utility 01', !html.includes('data-utility="01"')],
  ['no literal >01<', !/>01</.test(html)],
  ['profile utility', html.includes('data-utility="profile"') && html.includes('fa-user-circle')],
  ['theme icon', html.includes('fa-adjust') && html.includes('data-hook="theme-toggle"')],
  ['telemetry block', html.includes('class="hg-telemetry"')],
  ['telemetry icons', html.includes('fa-exclamation-triangle') && html.includes('fa-check-circle')],
  ['value 999', html.includes('>999<')],
  ['fav zones', html.includes('hg-fav-btn__icon-zone') && html.includes('hg-fav-btn__external')],
  ['signal icons', html.includes('fa-exclamation-circle') && html.includes('fa-bell')],
  ['A4 heartbeat', html.includes('fa-heartbeat')],
  ['main_area', html.includes('id="main_area"')],
  ['Russian Общий', html.includes('Общий')],
  ['FA stylesheet', html.includes('vendor/fontawesome/css/all.min.css')],
  ['FA in dist', fs.existsSync(`${root}/dist/assets/vendor/fontawesome/css/all.min.css`)],
];

let fail = 0;
for (const [name, ok] of checks) {
  console.log(`${ok ? 'OK' : 'FAIL'}: ${name}`);
  if (!ok) fail++;
}
process.exit(fail ? 1 : 0);
