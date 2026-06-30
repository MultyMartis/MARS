import fs from 'node:fs';
import path from 'node:path';
import ExcelJS from 'exceljs';
import { loadTemplateContract } from './template-sanitizer.mjs';
import { colToLetter, sanitizationCellValue as cellText } from './template-sanitizer.mjs';
import {
  verifyWorkbookCallouts,
  verifyWorkbookCleanUrls,
  DATA_START_ROW,
  FORENSIC_COL,
} from './workbook-forensic-verifier.mjs';
import { scanTemplateContamination } from './template-sanitizer.mjs';

export { DATA_START_ROW };

/**
 * Artifact-first XLSX validator — reopens actual written file.
 * @param {string} xlsxPath
 * @param {object} expectations
 */
export async function validateArtifactXlsx(xlsxPath, expectations = {}) {
  const contract = expectations.contract ?? loadTemplateContract();
  const evidence = [];
  const violations = [];
  const checks = [];

  const fail = (code, message, detail = {}) => {
    violations.push({ code, message, ...detail });
    checks.push({ check: code, status: 'FAIL', message });
  };
  const pass = (code, message = '') => {
    checks.push({ check: code, status: 'PASS', message });
  };

  if (!fs.existsSync(xlsxPath)) {
    fail('FILE_MISSING', `XLSX not found: ${xlsxPath}`);
    return buildResult(violations, checks, evidence);
  }

  const workbook = new ExcelJS.Workbook();
  try {
    await workbook.xlsx.readFile(xlsxPath);
    pass('file_opens');
  } catch (err) {
    fail('FILE_CORRUPT', `Cannot open XLSX: ${err.message}`);
    return buildResult(violations, checks, evidence);
  }

  const texts = workbook.getWorksheet(contract.sheets.texts.name);
  if (!texts) {
    fail('MISSING_SHEET_TEXTS', `Sheet "${contract.sheets.texts.name}" missing`);
    return buildResult(violations, checks, evidence);
  }
  pass('sheet_texts_exists');

  const regions = workbook.getWorksheet(contract.sheets.regions.name);
  if (!regions) {
    fail('MISSING_SHEET_REGIONS', `Sheet "${contract.sheets.regions.name}" missing`);
  } else {
    pass('sheet_regions_exists');
  }

  validateMetadataCells(texts, contract, expectations, evidence, pass, fail);
  validateDataRows(texts, expectations, evidence, pass, fail);
  validateContamination(texts, contract, expectations, pass, fail);

  const calloutResult = verifyWorkbookCallouts(texts, expectations);
  if (calloutResult.status === 'FAIL') {
    for (const c of calloutResult.checks.filter((x) => x.status === 'FAIL')) {
      fail('CALLOUT_' + c.check, c.message);
    }
  } else {
    pass('callout_serialization');
  }

  const urlResult = verifyWorkbookCleanUrls(texts, expectations);
  if (urlResult.status === 'FAIL') {
    for (const c of urlResult.checks.filter((x) => x.status === 'FAIL')) {
      fail('URL_' + c.check, c.message);
    }
  } else {
    pass('url_policy');
  }

  return buildResult(violations, checks, evidence, xlsxPath);
}

function validateMetadataCells(texts, contract, expectations, evidence, pass, fail) {
  const policy = expectations.metadata_policy ?? {};

  for (const [fieldId, meta] of Object.entries(contract.metadata_fields)) {
    const raw = cellText(texts, meta.row, meta.col);
    const normalized = raw.trim();
    const cellRef = `${colToLetter(meta.col)}${meta.row}`;
    const fieldPolicy = policy[fieldId] ?? meta.classification;

    evidence.push({
      filename: expectations.filename ?? path.basename(expectations.xlsxPath ?? ''),
      sheet: meta.sheet,
      cell: cellRef,
      field: fieldId,
      raw_value: raw,
      normalized_value: normalized,
      expected: fieldPolicy,
    });

    if (fieldPolicy === 'MUST_CLEAR' || expectations.embedded_campaign_negatives_policy === 'blank') {
      if (fieldId === 'campaign_negatives' && expectations.embedded_campaign_negatives_policy === 'blank') {
        if (normalized) {
          fail('E9_NOT_BLANK', `Campaign negatives E9 must be blank, got: "${normalized}"`, {
            cell: cellRef,
            raw_value: raw,
          });
        } else {
          pass('e9_blank');
        }
      }
      if (fieldId === 'organization' && (policy.organization === 'blank' || meta.classification === 'MUST_CLEAR')) {
        if (normalized) {
          fail('ORGANIZATION_NOT_BLANK', `Organization metadata must be blank, got: "${normalized}"`, {
            cell: cellRef,
          });
        } else {
          pass('organization_blank');
        }
      }
    }

    if (expectations.expected_metadata?.[fieldId] !== undefined) {
      const expected = expectations.expected_metadata[fieldId];
      if (String(expected ?? '') !== normalized) {
        fail('METADATA_MISMATCH', `${fieldId} expected "${expected}", got "${normalized}"`, {
          cell: cellRef,
          expected,
          actual: normalized,
        });
      } else {
        pass(`metadata_${fieldId}_match`);
      }
    }
  }
}

function validateDataRows(texts, expectations, evidence, pass, fail) {
  const dataStart = expectations.data_start_row ?? DATA_START_ROW;
  const groups = new Set();
  const phrases = [];
  let adCount = 0;
  let kwCount = 0;

  for (let r = dataStart; r <= texts.rowCount; r++) {
    const h1 = cellText(texts, r, FORENSIC_COL.headline_1);
    const phrase = cellText(texts, r, FORENSIC_COL.phrase);
    const group = cellText(texts, r, FORENSIC_COL.group_name);

    if (h1) {
      adCount++;
      if (group) groups.add(group);
      const url = cellText(texts, r, FORENSIC_COL.landing_url);
      if (!url && expectations.require_urls !== false) {
        fail('MISSING_AD_URL', `Ad row ${r} missing landing URL`);
      }
    }
    if (phrase) {
      kwCount++;
      phrases.push({ row: r, phrase, group });
      if (group) groups.add(group);
    }
  }

  if (expectations.expected_ad_count != null && adCount !== expectations.expected_ad_count) {
    fail('AD_COUNT_MISMATCH', `Expected ${expectations.expected_ad_count} ads, got ${adCount}`);
  } else if (expectations.expected_ad_count != null) {
    pass('ad_count_match');
  }

  if (expectations.expected_phrase_count != null && kwCount !== expectations.expected_phrase_count) {
    fail('PHRASE_COUNT_MISMATCH', `Expected ${expectations.expected_phrase_count} phrases, got ${kwCount}`);
  } else if (expectations.expected_phrase_count != null) {
    pass('phrase_count_match');
  }

  if (expectations.expected_group_count != null && groups.size !== expectations.expected_group_count) {
    fail('GROUP_COUNT_MISMATCH', `Expected ${expectations.expected_group_count} groups, got ${groups.size}`);
  } else if (expectations.expected_group_count != null) {
    pass('group_count_match');
  }

  const seenPhrases = new Set();
  for (const p of phrases) {
    const norm = p.phrase.toLowerCase().trim();
    if (seenPhrases.has(norm)) {
      fail('DUPLICATE_PHRASE', `Duplicate phrase in campaign: ${p.phrase}`, { row: p.row });
    }
    seenPhrases.add(norm);
  }

  evidence.push({
    summary: 'tabular_counts',
    ad_count: adCount,
    phrase_count: kwCount,
    group_count: groups.size,
  });
}

function validateContamination(texts, contract, expectations, pass, fail) {
  const scan = scanTemplateContamination(texts, contract);
  const foreign = expectations.forbidden_strings ?? [];
  const sig = contract.contamination_signatures ?? {};

  for (const term of sig.stale_campaign_negatives ?? []) {
    const e9 = cellText(texts, 9, 5);
    if (e9 && e9.toLowerCase().includes(term.toLowerCase())) {
      fail('STALE_TEMPLATE_NEGATIVE', `Stale Triumph negative "${term}" found in E9`, { raw: e9 });
    }
  }

  for (const f of foreign) {
    for (let r = DATA_START_ROW; r <= texts.rowCount; r++) {
      for (const col of Object.values(FORENSIC_COL)) {
        const v = cellText(texts, r, col);
        if (v && v.includes(f)) {
          fail('FOREIGN_CLIENT_CONTAMINATION', `Forbidden string "${f}" in row ${r}`, { value: v });
        }
      }
    }
  }
}

function buildResult(violations, checks, evidence, xlsxPath = null) {
  return {
    status: violations.length === 0 ? 'ARTIFACT_VALIDATED' : 'ARTIFACT_VALIDATION_FAIL',
    script_status: violations.length === 0 ? 'SCRIPT_PASS' : 'SCRIPT_FAIL',
    xlsx_path: xlsxPath,
    violation_count: violations.length,
    violations,
    checks,
    evidence,
    validated_at: new Date().toISOString(),
    note: 'Artifact-first validation — actual XLSX is source of truth',
  };
}
