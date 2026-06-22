import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const wpRoot = path.resolve(__dirname, '../../WORDPRESS');
const reportPath = path.resolve(__dirname, '../reports/FWS-0001-STATIC-STRUCTURE-REVIEW-v1.md');

const requiredTheme = [
  'theme-source/fws-synthetic/style.css',
  'theme-source/fws-synthetic/functions.php',
  'theme-source/fws-synthetic/front-page.php',
  'theme-source/fws-synthetic/archive-service.php',
  'theme-source/fws-synthetic/single-service.php',
  'theme-source/fws-synthetic/page-contacts.php',
];

const requiredPlugin = [
  'functionality-plugin/fws-synthetic-core/fws-synthetic-core.php',
  'functionality-plugin/fws-synthetic-core/includes/class-cpt-service.php',
];

const checks = [...requiredTheme, ...requiredPlugin].map((rel) => ({
  rel,
  ok: fs.existsSync(path.join(wpRoot, rel)),
}));

const missing = checks.filter((c) => !c.ok);
const result = missing.length === 0 ? 'PASS' : 'FAIL';

const body = `# FWS-0001 Static Structure Review v1

**Date:** 2026-06-22  
**Result:** ${result}

## Theme / plugin file checks

${checks.map((c) => `- [${c.ok ? 'x' : ' '}] \`${c.rel}\``).join('\n')}

## Notes

Static review substitutes WV3 where WordPress runtime rendering is limited on Profile B without live URL capture.

${missing.length ? `\n## Missing\n${missing.map((m) => `- ${m.rel}`).join('\n')}` : ''}
`;

fs.mkdirSync(path.dirname(reportPath), { recursive: true });
fs.writeFileSync(reportPath, body);
console.log('Wrote', reportPath, result);
