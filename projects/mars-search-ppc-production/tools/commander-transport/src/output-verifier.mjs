import fs from 'node:fs';
import { assertReadablePath } from './filesystem-guard.mjs';
import { validateTemplate } from './template-validator.mjs';
import {
  verifyWorkbookCallouts,
  verifyWorkbookCleanUrls,
  DATA_START_ROW,
} from './workbook-forensic-verifier.mjs';

export { verifyWorkbookCallouts, verifyWorkbookCleanUrls, DATA_START_ROW };

/**
 * Verify generated Commander output against template constraints.
 * @param {string} outputPath
 * @param {object} [options]
 */
export async function verifyOutput(outputPath, options = {}) {
  const resolved = assertReadablePath(outputPath, options);
  const templateResult = await validateTemplate(options.templatePath, options);

  if (!templateResult.ok) {
    return {
      status: 'FAIL',
      message: 'Template reference invalid',
      template: templateResult,
    };
  }

  const stat = fs.statSync(resolved);
  if (!stat.isFile() || !resolved.toLowerCase().endsWith('.xlsx')) {
    return { status: 'FAIL', message: 'Output is not an XLSX file' };
  }

  let callouts = { status: 'SKIP', note: 'ExcelJS read not requested' };
  let urls = { status: 'SKIP', note: 'ExcelJS read not requested' };

  if (options.deep !== false) {
    const { createRequire } = await import('node:module');
    const require = createRequire(import.meta.url);
    const ExcelJS = require('./../node_modules/exceljs');
    const workbook = new ExcelJS.Workbook();
    await workbook.xlsx.readFile(resolved);
    const texts = workbook.getWorksheet('Тексты');
    if (texts) {
      callouts = verifyWorkbookCallouts(texts, options);
      urls = verifyWorkbookCleanUrls(texts, options);
    } else {
      callouts = { status: 'FAIL', message: 'Missing Тексты sheet' };
      urls = { status: 'FAIL', message: 'Missing Тексты sheet' };
    }
  }

  const structuralFail = callouts.status === 'FAIL' || urls.status === 'FAIL';

  return {
    status: structuralFail ? 'FAIL' : 'PASS',
    output_path: resolved,
    size_bytes: stat.size,
    template_sha256: templateResult.sha256,
    callouts,
    urls,
    note: 'Structural verification — no import or Direct API',
  };
}
