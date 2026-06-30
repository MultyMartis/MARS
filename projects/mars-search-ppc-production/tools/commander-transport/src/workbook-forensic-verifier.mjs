import {
  COMMANDER_CALLOUT_DELIMITER,
  splitCallouts,
  validateSerializedCallouts,
} from './callout-serializer.mjs';
import { validateCleanAdUrl } from './url-policy.mjs';

export const FORENSIC_COL = {
  group_name: 5,
  phrase: 8,
  headline_1: 10,
  landing_url: 48,
  organization: 50,
  region: 52,
  bid: 54,
  fastlink_titles: 58,
  fastlink_descriptions: 59,
  fastlink_urls: 60,
  callouts: 67,
  group_negatives: 68,
};

export const DATA_START_ROW = 16;

function cellText(sheet, row, col) {
  const v = sheet.getRow(row).getCell(col).value;
  if (v == null) return '';
  if (typeof v === 'object' && v.text) return String(v.text).trim();
  if (typeof v === 'object' && v.richText) {
    return v.richText.map((p) => p.text).join('').trim();
  }
  return String(v).trim();
}

function isSitelinkPopulated(value) {
  const text = String(value ?? '').trim();
  return text.length > 0 && text !== '-';
}

/**
 * Forensic callout verification on an open ExcelJS worksheet.
 * @param {object} textsSheet
 * @param {object} [options]
 */
export function verifyWorkbookCallouts(textsSheet, options = {}) {
  const checks = [];
  const fail = (name, message) => checks.push({ check: name, status: 'FAIL', message });
  const pass = (name, detail = '') => checks.push({ check: name, status: 'PASS', message: detail });

  let adRows = 0;
  let combinedDefects = 0;
  let lengthDefects = 0;
  let delimiterDefects = 0;

  for (let r = DATA_START_ROW; r <= textsSheet.rowCount; r++) {
    const h1 = cellText(textsSheet, r, FORENSIC_COL.headline_1);
    if (!h1) continue;
    adRows++;
    const raw = cellText(textsSheet, r, FORENSIC_COL.callouts);
    if (!raw) continue;

    const violations = validateSerializedCallouts(raw, { campaignId: options.campaignId });
    if (violations.some((v) => v.code === 'COMBINED_CALLOUT_VALUE')) combinedDefects++;
    if (violations.some((v) => v.code === 'CALLOUT_LENGTH')) lengthDefects++;
    if (
      violations.some(
        (v) =>
          v.code === 'DOUBLE_DELIMITER_CALLOUT' ||
          v.code === 'LEADING_CALLOUT_DELIMITER' ||
          v.code === 'TRAILING_CALLOUT_DELIMITER'
      )
    ) {
      delimiterDefects++;
    }

    if (raw.includes(';;') || raw.includes(',,')) {
      fail(`callout_row_${r}`, `Wrong delimiter in row ${r}: ${raw}`);
    }

    const parts = splitCallouts(raw);
    if (parts.length > 1) {
      pass(`callout_separate_row_${r}`, `${parts.length} callouts`);
    }
  }

  if (combinedDefects === 0) pass('no_combined_callout_string');
  else fail('no_combined_callout_string', `${combinedDefects} ad rows with combined callouts`);

  if (lengthDefects === 0) pass('callout_length_limits');
  else fail('callout_length_limits', `${lengthDefects} callouts outside 1–25`);

  if (delimiterDefects === 0) pass('callout_delimiter_integrity');
  else fail('callout_delimiter_integrity', `${delimiterDefects} delimiter defects`);

  if (adRows > 0) pass('callout_ad_rows_checked', String(adRows));

  return {
    status: checks.some((c) => c.status === 'FAIL') ? 'FAIL' : 'PASS',
    delimiter: COMMANDER_CALLOUT_DELIMITER,
    checks,
  };
}

/**
 * Forensic clean-URL verification on an open ExcelJS worksheet.
 * @param {object} textsSheet
 * @param {object} [options]
 */
export function verifyWorkbookCleanUrls(textsSheet, options = {}) {
  const checks = [];
  const fail = (name, message) => checks.push({ check: name, status: 'FAIL', message });
  const pass = (name, detail = '') => checks.push({ check: name, status: 'PASS', message: detail });

  let adRows = 0;
  let queryHits = 0;
  let utmHits = 0;
  let macroHits = 0;
  let fragmentHits = 0;

  for (let r = DATA_START_ROW; r <= textsSheet.rowCount; r++) {
    const h1 = cellText(textsSheet, r, FORENSIC_COL.headline_1);
    if (!h1) continue;
    adRows++;
    const url = cellText(textsSheet, r, FORENSIC_COL.landing_url);
    if (!url) continue;

    const violations = validateCleanAdUrl(url, { groupId: `row-${r}` });
    if (violations.some((v) => v.code === 'URL_QUERY_FORBIDDEN')) queryHits++;
    if (violations.some((v) => v.code === 'UTM_IN_AD_URL')) utmHits++;
    if (violations.some((v) => v.code === 'KEYWORD_MACRO_IN_URL')) macroHits++;
    if (violations.some((v) => v.code === 'URL_FRAGMENT_FORBIDDEN')) fragmentHits++;
  }

  if (queryHits === 0) pass('no_query_string');
  else fail('no_query_string', `${queryHits} URLs with query string`);

  if (utmHits === 0) pass('no_utm_in_url');
  else fail('no_utm_in_url', `${utmHits} URLs with utm_`);

  if (macroHits === 0) pass('no_keyword_macro');
  else fail('no_keyword_macro', `${macroHits} URLs with {keyword}`);

  if (fragmentHits === 0) pass('no_fragment');
  else fail('no_fragment', `${fragmentHits} URLs with fragment`);

  return {
    status: checks.some((c) => c.status === 'FAIL') ? 'FAIL' : 'PASS',
    ad_rows_checked: adRows,
    checks,
  };
}

export { cellText, isSitelinkPopulated };
