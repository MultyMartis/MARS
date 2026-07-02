/**
 * V9-05C — Project admission registry loader.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ADMISSIONS_DIR = path.resolve(__dirname, '../project-admissions');

const SITE_ADMISSION_FILES = Object.freeze({
  'fp-0002-shpigovsky': 'fp-0002-project-admission-v1.json',
});

export function loadProjectAdmission(siteId) {
  const file = SITE_ADMISSION_FILES[siteId];
  if (!file) return null;
  const filePath = path.join(ADMISSIONS_DIR, file);
  return Object.freeze(JSON.parse(fs.readFileSync(filePath, 'utf8')));
}

export function loadFailureMappings(siteId) {
  const admission = loadProjectAdmission(siteId);
  if (!admission?.failure_mappings) return null;
  const filePath = path.join(ADMISSIONS_DIR, admission.failure_mappings);
  return Object.freeze(JSON.parse(fs.readFileSync(filePath, 'utf8')));
}

export function isProjectSite(siteId) {
  return Object.prototype.hasOwnProperty.call(SITE_ADMISSION_FILES, siteId);
}

export default { loadProjectAdmission, loadFailureMappings, isProjectSite };
