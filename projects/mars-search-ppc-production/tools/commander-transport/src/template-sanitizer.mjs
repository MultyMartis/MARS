import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  clearCampaignNegativesMetadataCell,
  clearOrganizationMetadataCell,
  clearOrganizationColumnOnDataRows,
  DATA_START_ROW,
} from './commander-patcher-adapter.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const CONTRACTS_DIR = path.join(__dirname, '../contracts');

export function loadTemplateContract() {
  const p = path.join(CONTRACTS_DIR, 'commander-template-contract-v1.json');
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

export function loadSanitizationManifest() {
  const p = path.join(CONTRACTS_DIR, 'template-sanitization-manifest-v1.json');
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

import { createRequire } from 'node:module';

const requireTriumph = createRequire(import.meta.url);
const TRIUMPH_SHEET1 = path.resolve(
  __dirname,
  '../../../../orca/ppc/triumph-manipulator/tools/exporter-cli/sheet1-xml-builder.js'
);

function getSheet1Builder() {
  return requireTriumph(TRIUMPH_SHEET1);
}

/**
 * Apply sanitization to sheet1 XML before project data is written.
 * @param {string} sheetXml
 * @param {object} [options]
 */
export function sanitizeTemplateSheetXml(sheetXml, options = {}) {
  const manifest = options.manifest ?? loadSanitizationManifest();
  const contract = options.contract ?? loadTemplateContract();
  const dataStartRow = options.dataStartRow ?? DATA_START_ROW;
  const rowCount = options.estimatedRowCount ?? 100;

  let next = sheetXml;
  const applied = [];

  for (const entry of manifest.entries) {
    if (entry.range === 'data_rows') {
      if (entry.field === 'organization_data' && entry.col === 50) {
        next = clearOrganizationColumnOnDataRows(next, dataStartRow, rowCount);
        applied.push({ field: entry.field, operation: 'clear', scope: 'data_rows' });
      }
      continue;
    }

    if (entry.field === 'campaign_negatives') {
      next = clearCampaignNegativesMetadataCell(next);
      applied.push({ field: entry.field, cell: entry.cell, operation: 'clear' });
    } else if (entry.field === 'organization') {
      next = clearOrganizationMetadataCell(next);
      applied.push({ field: entry.field, cell: entry.cell, operation: 'clear' });
    } else if (entry.field === 'promotion_url' || entry.field === 'campaign_type') {
      const meta = contract.metadata_fields[entry.field];
      if (meta) {
        next = clearMetadataCell(next, meta.row, meta.col);
        applied.push({ field: entry.field, cell: `${colToLetter(meta.col)}${meta.row}`, operation: 'clear' });
      }
    }
  }

  return { sheetXml: next, applied, sanitized: true };
}

function colToLetter(col) {
  let s = '';
  let c = col;
  while (c > 0) {
    const rem = (c - 1) % 26;
    s = String.fromCharCode(65 + rem) + s;
    c = Math.floor((c - 1) / 26);
  }
  return s;
}

function clearMetadataCell(sheetXml, rowNum, col) {
  const { extractRowXml, patchCellInRow, cellRef } = getSheet1Builder();
  const rowXml = extractRowXml(sheetXml, rowNum);
  if (!rowXml) return sheetXml;
  const ref = cellRef(rowNum, col);
  const { rowXml: patchedRow } = patchCellInRow(rowXml, ref, '');
  const re = new RegExp(`<row r="${rowNum}"[^>]*>[\\s\\S]*?</row>`);
  return sheetXml.replace(re, patchedRow);
}

/**
 * Scan template workbook for known contamination signatures.
 * @param {import('exceljs').Worksheet} textsSheet
 * @param {object} contract
 */
export function scanTemplateContamination(textsSheet, contract) {
  const findings = [];
  const sig = contract.contamination_signatures ?? {};

  for (const [fieldId, meta] of Object.entries(contract.metadata_fields ?? {})) {
    const val = cellValue(textsSheet, meta.row, meta.col);
    if (!val) continue;
    findings.push({
      field: fieldId,
      sheet: meta.sheet,
      cell: `${colToLetter(meta.col)}${meta.row}`,
      raw_value: val,
      type: 'populated_metadata',
    });
  }

  for (const term of sig.stale_campaign_negatives ?? []) {
    const e9 = cellValue(textsSheet, 9, 5);
    if (e9 && e9.toLowerCase().includes(term.toLowerCase())) {
      findings.push({
        field: 'campaign_negatives',
        cell: 'E9',
        raw_value: e9,
        matched_signature: term,
        type: 'stale_campaign_negative',
      });
    }
  }

  for (const domain of sig.stale_domains ?? []) {
    for (const [fieldId, meta] of Object.entries(contract.metadata_fields ?? {})) {
      const val = cellValue(textsSheet, meta.row, meta.col);
      if (val && val.includes(domain)) {
        findings.push({
          field: fieldId,
          cell: `${colToLetter(meta.col)}${meta.row}`,
          raw_value: val,
          matched_signature: domain,
          type: 'stale_domain',
        });
      }
    }
  }

  return {
    contaminated: findings.length > 0,
    findings,
    clean_template_contract_requires_sanitization: contract.sanitization_required_before_use,
  };
}

function cellValue(sheet, row, col) {
  const v = sheet.getRow(row).getCell(col).value;
  if (v == null) return '';
  if (typeof v === 'object' && v.text) return String(v.text).trim();
  if (typeof v === 'object' && v.richText) {
    return v.richText.map((p) => p.text).join('').trim();
  }
  return String(v).trim();
}

export { colToLetter, cellValue as sanitizationCellValue };
