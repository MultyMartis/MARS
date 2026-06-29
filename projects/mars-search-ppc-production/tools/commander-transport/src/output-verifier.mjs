import fs from 'node:fs';
import { assertReadablePath } from './filesystem-guard.mjs';
import { validateTemplate } from './template-validator.mjs';

/**
 * Verify generated Commander output against template constraints.
 * @param {string} outputPath
 * @param {object} [options]
 */
export async function verifyOutput(outputPath, options = {}) {
  const resolved = assertReadablePath(outputPath, options);
  const templateResult = await validateTemplate(
    options.templatePath,
    options
  );

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

  return {
    status: 'PASS',
    output_path: resolved,
    size_bytes: stat.size,
    template_sha256: templateResult.sha256,
    note: 'Structural verification only — no import or Direct API',
  };
}
