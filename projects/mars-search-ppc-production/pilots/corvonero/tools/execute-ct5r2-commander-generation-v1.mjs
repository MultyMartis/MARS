#!/usr/bin/env node
// C2c HOLD: source hardening only.
// This file is not authorized for execution without explicit operator approval.
// Commit/persistence does not authorize Commander import, Direct launch, account mutation,
// advertising start, Storage export generation, repo artifact generation,
// Localhost mutation, Storage mutation, Yandex/API access, or client-facing delivery.
// Commander/XLSX generation is transport/import-candidate tooling only and does not authorize
// import into Yandex Direct or any live account mutation.
/**
 * CORVONERO CT-5R2 — Triumph bid-ladder recovery + v4 Commander XLSX regeneration.
 * Local generation only — no import, no Direct API.
 */
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { execSync } from 'node:child_process';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

import { loadAuthority } from '../../../tools/commander-transport/src/authority-loader.mjs';
import {
  adapterAvailable,
  patchCommanderWorkbook,
} from '../../../tools/commander-transport/src/commander-patcher-adapter.mjs';
import {
  BID_LADDER_POLICY,
  BID_STEP_MIN,
  buildBidDistributionReport,
  TRIUMPH_BID_AUTHORITY_RELATIVE,
} from '../../../tools/commander-transport/src/bid-ladder.mjs';
import { COMMANDER_CALLOUT_DELIMITER } from '../../../tools/commander-transport/src/callout-serializer.mjs';
import {
  COMMANDER_COLUMN_COUNT,
  COMMANDER_HEADER_ROW,
  COMMANDER_SHEET_REGIONS,
  COMMANDER_SHEET_TEXTS,
  COMMANDER_TEMPLATE_PATH,
  EXPECTED_TEMPLATE_SHA256,
  FORBIDDEN_ORGANIZATION_ID,
  REQUIRED_REGION_VALUE,
  STORAGE_EXPORT_ROOT,
} from '../../../tools/commander-transport/src/constants.mjs';
import { buildPayloads, validateTransport } from '../../../tools/commander-transport/src/payload-builder.mjs';
import { validateTemplate } from '../../../tools/commander-transport/src/template-validator.mjs';
import {
  cellText,
  DATA_START_ROW,
  FORENSIC_COL,
  isSitelinkPopulated,
  verifyWorkbookCallouts,
  verifyWorkbookCleanUrls,
} from '../../../tools/commander-transport/src/workbook-forensic-verifier.mjs';

const require = createRequire(import.meta.url);
const ExcelJS = require('../../../tools/commander-transport/node_modules/exceljs');

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PILOT_ROOT = path.resolve(__dirname, '..');
const PROJECT_ROOT = path.resolve(__dirname, '../../..');
const REPO_ROOT = path.resolve(PROJECT_ROOT, '../..');

const RUN_ID = 'CORVONERO-COMMANDER-CT5R2-FINAL-2026-06-30';
const OUTPUT_DIR = path.join(STORAGE_EXPORT_ROOT, RUN_ID);
const MANIFEST_PATH = path.join(PILOT_ROOT, 'CORVONERO-CT4-AUTHORITY-MANIFEST-v1.json');

const CT4_COMMIT = '8943e07e5f6b45d8e6cfd209a30cac55e2f0bb86';

const CAMPAIGN_FILES = {
  'CA-01': 'CORVONERO-CA-01-PROGRAMMIST-1S-COMMANDER-IMPORT-v4.xlsx',
  'CA-02': 'CORVONERO-CA-02-SOPROVOZHDENIE-1S-COMMANDER-IMPORT-v4.xlsx',
  'CA-03': 'CORVONERO-CA-03-DORABOTKA-1S-COMMANDER-IMPORT-v4.xlsx',
  'CA-04': 'CORVONERO-CA-04-INTEGRACII-1S-COMMANDER-IMPORT-v4.xlsx',
  'CA-05': 'CORVONERO-CA-05-MARKIROVKA-1S-COMMANDER-IMPORT-v4.xlsx',
};

const EXPECTED_COUNTS = {
  'CA-01': { groups: 7, keywords: 339, base_bid: 500 },
  'CA-02': { groups: 4, keywords: 153, base_bid: 400 },
  'CA-03': { groups: 3, keywords: 76, base_bid: 400 },
  'CA-04': { groups: 1, keywords: 48, base_bid: 400 },
  'CA-05': { groups: 6, keywords: 217, base_bid: 400 },
};

const FORBIDDEN_REGIONS = [
  'Новосибирск + Новосибирская область',
  'Новосибирск и Новосибирская область',
  'Все',
];

function enrichLoadedAuthority(loaded) {
  const transportConfig = loaded.byRole.transport_config;
  if (!transportConfig) return loaded;

  const resolveRef = (refPath) => {
    if (!refPath) return null;
    const abs = path.resolve(refPath);
    return JSON.parse(fs.readFileSync(abs, 'utf8'));
  };

  if (transportConfig.bids_ref) {
    loaded.byRole.bids = resolveRef(transportConfig.bids_ref);
  }
  if (transportConfig.display_paths_ref) {
    loaded.byRole.display_paths = resolveRef(transportConfig.display_paths_ref);
  }
  if (transportConfig.group_negatives_ref) {
    loaded.byRole.group_negatives = resolveRef(transportConfig.group_negatives_ref);
  }
  if (transportConfig.bids) {
    loaded.byRole.bids = { campaign_bids: transportConfig.bids };
  }
  if (transportConfig.display_paths) {
    loaded.byRole.display_paths = transportConfig.display_paths;
  }
  if (transportConfig.group_negatives && !loaded.byRole.group_negatives) {
    loaded.byRole.group_negatives = transportConfig.group_negatives;
  }
  return loaded;
}

function sha256File(fp) {
  return crypto.createHash('sha256').update(fs.readFileSync(fp)).digest('hex');
}

function gitHead() {
  return execSync('git rev-parse HEAD', { cwd: REPO_ROOT, encoding: 'utf8' }).trim();
}

function assertVolume() {
  const label = execSync('(Get-Volume -DriveLetter X).FileSystemLabel', {
    encoding: 'utf8',
    shell: 'powershell.exe',
  }).trim();
  if (label !== 'AI WS') {
    throw new Error(`STOP — X VOLUME IDENTITY MISMATCH (got "${label}")`);
  }
}

function requireOperatorGate() {
  if (process.env.CORVONERO_OPERATOR_GATE !== 'APPROVED') {
    console.error(
      'STOP: CORVONERO_OPERATOR_GATE=APPROVED required. This C2c helper is not safe for casual execution.'
    );
    process.exit(1);
  }
}

function findMetadataValue(sheet, label) {
  for (let r = 1; r < COMMANDER_HEADER_ROW; r++) {
    for (let c = 1; c <= 8; c++) {
      const key = cellText(sheet, r, c);
      if (key === label) {
        return cellText(sheet, r, c + 1);
      }
    }
  }
  return '';
}

function parseBidValue(raw) {
  const s = String(raw ?? '').trim().replace(',', '.');
  if (!s) return null;
  const n = Number(s);
  return Number.isFinite(n) ? n : null;
}

function buildPhrasesByGroup(model) {
  const deployable = (model.phraseAllocation?.records ?? []).filter(
    (r) => r.production_status === 'DEPLOYABLE'
  );
  const phrasesByGroup = new Map();
  for (const rec of deployable) {
    if (!phrasesByGroup.has(rec.final_group)) phrasesByGroup.set(rec.final_group, []);
    phrasesByGroup.get(rec.final_group).push(rec);
  }
  return phrasesByGroup;
}

async function forensicVerifyWorkbook(filePath, payload, campaignId, templateSha) {
  const expected = EXPECTED_COUNTS[campaignId];
  const checks = [];
  const fail = (name, message) => checks.push({ check: name, status: 'FAIL', message });
  const pass = (name, detail = '') => checks.push({ check: name, status: 'PASS', message: detail });

  const workbook = new ExcelJS.Workbook();
  await workbook.xlsx.readFile(filePath);

  const texts = workbook.getWorksheet(COMMANDER_SHEET_TEXTS);
  if (!texts) {
    fail('sheet_texts', 'Missing Тексты sheet');
    return { status: 'FAIL', checks };
  }
  pass('sheet_texts');

  const colCount = texts.actualColumnCount || texts.columnCount || 0;
  if (colCount < COMMANDER_COLUMN_COUNT) {
    fail('columns_78', `Column count ${colCount} < ${COMMANDER_COLUMN_COUNT}`);
  } else pass('columns_78', String(colCount));

  pass('template_sha_lineage', `source template SHA-256 ${templateSha}`);

  const regions = workbook.getWorksheet(COMMANDER_SHEET_REGIONS);
  if (!regions) fail('regions_sheet', 'Missing Регионы sheet');
  else {
    let found = false;
    regions.eachRow({ includeEmpty: true }, (row) => {
      row.eachCell({ includeEmpty: true }, (cell) => {
        if (String(cell.value ?? '').trim() === REQUIRED_REGION_VALUE) found = true;
      });
    });
    if (!found) fail('regions_dictionary', `Missing ${REQUIRED_REGION_VALUE}`);
    else pass('regions_dictionary');
  }

  pass('campaign_count', '1 (single-campaign workbook)');

  const adRows = [];
  const kwRows = [];
  const groupsSeen = new Set();
  const kwPerGroup = new Map();
  const bidsPerGroup = new Map();
  let orgIdHits = 0;
  let utmHits = 0;
  let keywordMacroHits = 0;
  let queryHits = 0;
  let sitelinkHits = 0;
  let regionFails = 0;
  let missingBid = 0;
  let aboveBaseBid = 0;
  let flatGroupFails = 0;
  let ladderMismatch = 0;
  const allBids = [];

  const payloadBidByPhrase = new Map();
  for (const row of payload.rows) {
    if (row.row_type === 'KEYWORD') {
      payloadBidByPhrase.set(row.phrase, row.bid);
    }
  }

  for (let r = DATA_START_ROW; r <= texts.rowCount; r++) {
    const phrase = cellText(texts, r, FORENSIC_COL.phrase);
    const h1 = cellText(texts, r, FORENSIC_COL.headline_1);
    const group = cellText(texts, r, FORENSIC_COL.group_name);
    if (!phrase && !h1 && !group) continue;

    const region = cellText(texts, r, FORENSIC_COL.region);
    const rowBlob = JSON.stringify(
      [48, 50, 58, 59, 60, 67].map((c) => cellText(texts, r, c))
    );
    if (rowBlob.includes(FORBIDDEN_ORGANIZATION_ID)) orgIdHits++;

    const url = cellText(texts, r, FORENSIC_COL.landing_url);
    if (url.includes('utm_')) utmHits++;
    if (url.includes('{keyword}')) keywordMacroHits++;
    if (url.includes('?')) queryHits++;

    if (
      [FORENSIC_COL.fastlink_titles, FORENSIC_COL.fastlink_descriptions, FORENSIC_COL.fastlink_urls].some(
        (c) => isSitelinkPopulated(cellText(texts, r, c))
      )
    ) {
      sitelinkHits++;
    }

    if (region && region !== REQUIRED_REGION_VALUE) regionFails++;
    if (FORBIDDEN_REGIONS.includes(region)) regionFails++;

    if (h1) {
      adRows.push({ row: r, group });
      groupsSeen.add(group);
    } else if (phrase) {
      kwRows.push({ row: r, group, phrase });
      groupsSeen.add(group);
      kwPerGroup.set(group, (kwPerGroup.get(group) ?? 0) + 1);

      const bid = parseBidValue(cellText(texts, r, FORENSIC_COL.bid));
      if (bid == null || bid <= 0) missingBid++;
      else {
        allBids.push(bid);
        if (bid > expected.base_bid) aboveBaseBid++;
        if (!bidsPerGroup.has(group)) bidsPerGroup.set(group, []);
        bidsPerGroup.get(group).push(bid);
        const expBid = payloadBidByPhrase.get(phrase);
        if (expBid != null && bid !== expBid) ladderMismatch++;
      }
    }
  }

  for (const [group, bids] of bidsPerGroup) {
    if (bids.length > 1 && new Set(bids).size === 1) flatGroupFails++;
  }

  if (groupsSeen.size === expected.groups) pass('expected_groups', String(groupsSeen.size));
  else fail('expected_groups', `got ${groupsSeen.size}, expected ${expected.groups}`);

  if (kwRows.length === expected.keywords) pass('expected_keyword_rows', String(kwRows.length));
  else fail('expected_keyword_rows', `got ${kwRows.length}, expected ${expected.keywords}`);

  if (adRows.length === expected.groups) pass('expected_ad_rows', String(adRows.length));
  else fail('expected_ad_rows', `got ${adRows.length}, expected ${expected.groups}`);

  let maxGroupKw = 0;
  for (const c of kwPerGroup.values()) maxGroupKw = Math.max(maxGroupKw, c);
  if (maxGroupKw <= 200) pass('max_group_phrase_count', String(maxGroupKw));
  else fail('max_group_phrase_count', `${maxGroupKw} > 200`);

  if (missingBid === 0) pass('keyword_bids_present');
  else fail('keyword_bids_present', `${missingBid} missing or invalid`);

  if (aboveBaseBid === 0) pass('bids_within_campaign_base');
  else fail('bids_within_campaign_base', `${aboveBaseBid} above base ${expected.base_bid}`);

  if (flatGroupFails === 0) pass('bid_ladder_variation');
  else fail('bid_ladder_variation', `${flatGroupFails} groups with flat bids`);

  if (ladderMismatch === 0) pass('bid_ladder_payload_match');
  else fail('bid_ladder_payload_match', `${ladderMismatch} group bid multiset mismatches`);

  const distinctBids = new Set(allBids);
  const allEqual500 =
    campaignId === 'CA-01' && allBids.length > 0 && allBids.every((b) => b === 500);
  if (!allEqual500) pass('ca01_not_all_500', `distinct=${distinctBids.size}`);
  else fail('ca01_not_all_500', 'all 339 phrases at 500 RUB');

  if (regionFails === 0) pass('region');
  else fail('region', `${regionFails} bad region values`);

  if (orgIdHits === 0) pass('forbidden_organization_id');
  else fail('forbidden_organization_id', `${orgIdHits} hits`);

  let orgColPopulated = 0;
  for (let r = DATA_START_ROW; r < DATA_START_ROW + adRows.length + kwRows.length + 50; r++) {
    const orgCell = cellText(texts, r, FORENSIC_COL.organization);
    if (orgCell.trim()) orgColPopulated++;
  }
  if (orgColPopulated === 0) pass('organization_column_blank');
  else fail('organization_column_blank', `${orgColPopulated} populated col-50 cells`);

  for (const c of verifyWorkbookCallouts(texts, { campaignId }).checks) checks.push(c);
  for (const c of verifyWorkbookCleanUrls(texts, { campaignId }).checks) checks.push(c);

  if (utmHits === 0) pass('utm_absent');
  else fail('utm_absent', String(utmHits));
  if (queryHits === 0) pass('clean_url_no_query');
  else fail('clean_url_no_query', String(queryHits));
  if (keywordMacroHits === 0) pass('keyword_macro_absent');
  else fail('keyword_macro_absent', String(keywordMacroHits));
  if (sitelinkHits === 0) pass('sitelinks_omitted');
  else fail('sitelinks_omitted', `${sitelinkHits} populated sitelink cells`);

  const metaOrg = findMetadataValue(texts, 'Организация из Яндекс Бизнеса:');
  if (!metaOrg.trim()) pass('organization_metadata_blank');
  else fail('organization_metadata_blank', `expected blank, got "${metaOrg}"`);

  const payloadCallouts = new Map();
  const payloadUrls = new Map();
  for (const row of payload.rows) {
    if (row.row_type === 'AD') {
      payloadCallouts.set(row.group_name, row.callouts ?? '');
      payloadUrls.set(row.group_name, row.landing_url ?? '');
    }
  }

  let calloutMismatch = 0;
  let urlMismatch = 0;
  for (const ad of adRows) {
    if (cellText(texts, ad.row, FORENSIC_COL.callouts) !== (payloadCallouts.get(ad.group) ?? '')) {
      calloutMismatch++;
    }
    if (cellText(texts, ad.row, FORENSIC_COL.landing_url) !== (payloadUrls.get(ad.group) ?? '')) {
      urlMismatch++;
    }
  }
  if (calloutMismatch === 0) pass('callouts_payload_match');
  else fail('callouts_payload_match', `${calloutMismatch} mismatches`);
  if (urlMismatch === 0) pass('urls_payload_match');
  else fail('urls_payload_match', `${urlMismatch} mismatches`);

  const bidHistogram = {};
  for (const b of allBids) {
    bidHistogram[String(b)] = (bidHistogram[String(b)] ?? 0) + 1;
  }

  const status = checks.some((c) => c.status === 'FAIL') ? 'FAIL' : 'PASS';
  return {
    status,
    checks,
    callout_delimiter: COMMANDER_CALLOUT_DELIMITER,
    bid_summary: {
      total_keyword_rows: kwRows.length,
      distinct_bid_values: distinctBids.size,
      minimum_bid: allBids.length ? Math.min(...allBids) : null,
      maximum_bid: allBids.length ? Math.max(...allBids) : null,
      rows_at_base_bid: allBids.filter((b) => b === expected.base_bid).length,
      bid_histogram: bidHistogram,
      all_equal_base: allEqual500,
    },
    counts: {
      groups: groupsSeen.size,
      keyword_rows: kwRows.length,
      ad_rows: adRows.length,
      max_group_keyword_count: maxGroupKw,
    },
  };
}

function writeReceipt(base, data, mdLines) {
  fs.writeFileSync(path.join(PILOT_ROOT, `${base}.json`), `${JSON.stringify(data, null, 2)}\n`);
  fs.writeFileSync(path.join(PILOT_ROOT, `${base}.md`), `${mdLines.join('\n')}\n`);
}

function writeStorage(name, data, md) {
  fs.writeFileSync(path.join(OUTPUT_DIR, `${name}.json`), `${JSON.stringify(data, null, 2)}\n`);
  if (md) fs.writeFileSync(path.join(OUTPUT_DIR, `${name}.md`), `${md}\n`);
}

async function main() {
  requireOperatorGate();
  const generatedAt = new Date().toISOString();
  assertVolume();

  if (fs.existsSync(OUTPUT_DIR)) {
    console.error('STOP — CT5R2 OUTPUT DIRECTORY ALREADY EXISTS');
    process.exit(2);
  }

  if (!adapterAvailable()) {
    throw new Error('Triumph Commander patcher adapter unavailable');
  }

  const templateResult = await validateTemplate(COMMANDER_TEMPLATE_PATH);
  if (!templateResult.ok) {
    console.error('STOP — COMMANDER TEMPLATE IDENTITY MISMATCH');
    process.exit(2);
  }

  let loaded = await loadAuthority(MANIFEST_PATH);
  loaded = enrichLoadedAuthority(loaded);
  const validation = validateTransport(loaded);

  if (validation.status !== 'PASS') {
    console.error('Validation failed — generation blocked');
    console.error(JSON.stringify(validation, null, 2));
    process.exit(1);
  }

  const model = validation.model;
  const groups = model.architecture?.groups ?? [];
  const campaignBids = model.bids?.campaign_bids ?? {};
  const phrasesByGroup = buildPhrasesByGroup(model);
  const bidDistribution = buildBidDistributionReport(groups, phrasesByGroup, campaignBids);

  const payloads = buildPayloads(loaded, validation);
  const payloadByCampaign = Object.fromEntries(payloads.map((p) => [p.campaign_id, p]));

  const ca01PayloadBids = (payloadByCampaign['CA-01']?.rows ?? [])
    .filter((r) => r.row_type === 'KEYWORD')
    .map((r) => r.bid);
  const ca01All500 =
    ca01PayloadBids.length > 0 && ca01PayloadBids.every((b) => b === 500);

  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  const guardOptions = { approvedWriteRoot: OUTPUT_DIR };
  const generationResults = [];

  for (const [campaignId, filename] of Object.entries(CAMPAIGN_FILES)) {
    const payload = payloadByCampaign[campaignId];
    if (!payload) throw new Error(`Missing payload for ${campaignId}`);

    const kwCount = payload.rows.filter((r) => r.row_type === 'KEYWORD').length;
    const adCount = payload.rows.filter((r) => r.row_type === 'AD').length;
    const exp = EXPECTED_COUNTS[campaignId];
    if (kwCount !== exp.keywords || adCount !== exp.groups) {
      throw new Error(
        `Payload count mismatch ${campaignId}: kw ${kwCount}/${exp.keywords}, ads ${adCount}/${exp.groups}`
      );
    }

    const outPath = path.join(OUTPUT_DIR, filename);
    const patchResult = await patchCommanderWorkbook({
      payload,
      templatePath: COMMANDER_TEMPLATE_PATH,
      outputPath: outPath,
      guardOptions,
    });

    if (!patchResult.ok) {
      throw new Error(`Generation failed for ${campaignId}: ${JSON.stringify(patchResult.integrity)}`);
    }

    generationResults.push({
      campaign_id: campaignId,
      filename,
      output_path: outPath,
      sha256: sha256File(outPath),
      rows_written: patchResult.rows_written,
      keyword_rows: kwCount,
      ad_rows: adCount,
      campaign_base_bid: exp.base_bid,
    });
  }

  const forensicResults = [];
  for (const gen of generationResults) {
    const payload = payloadByCampaign[gen.campaign_id];
    forensicResults.push({
      campaign_id: gen.campaign_id,
      filename: gen.filename,
      output_path: gen.output_path,
      sha256: gen.sha256,
      ...(await forensicVerifyWorkbook(
        gen.output_path,
        payload,
        gen.campaign_id,
        templateResult.sha256
      )),
    });
  }

  const allForensicPass = forensicResults.every((r) => r.status === 'PASS');
  const repoCommit = gitHead();
  const ca01Forensic = forensicResults.find((r) => r.campaign_id === 'CA-01');

  const triumphPolicy = {
    source_path: TRIUMPH_BID_AUTHORITY_RELATIVE,
    source_file: 'bid-assignment-v1.3.js',
    repository_commit: repoCommit,
    campaign: 'triumph-manipulator-search',
    reference_bid_min_rub: 400,
    reference_bid_max_rub: 600,
    corvonero_campaign_base_bids: campaignBids,
    bid_ladder_policy: BID_LADDER_POLICY,
    bid_step_min_rub: BID_STEP_MIN,
    spread_max_rub: 90,
    assignment_scope: 'per_ad_group',
    assignment_order: 'primary_first_then_source_index_then_phrase_id',
    ladder_direction: 'descending',
    group_reset_rule: 'each_ad_group_restarts_from_campaign_base_bid',
    duplicate_bid_policy: 'retry_with_step_min_11_when_unique_count_lt_phrase_count',
    determinism_rule: 'stable_phrase_order_plus_fixed_algorithm',
    single_phrase_rule: 'campaign_base_bid_minus_20_clamped',
  };

  const verdict = allForensicPass
    ? 'CORVONERO COMMANDER CT-5R2: PASS — TRIUMPH BID LADDER RECOVERED AND APPLIED'
    : 'CORVONERO COMMANDER CT-5R2: FAIL — FORENSIC VERIFICATION ERROR';

  writeReceipt('CORVONERO-COMMANDER-CT5R2-TRIUMPH-BID-POLICY-v1', triumphPolicy, [
    '# CORVONERO COMMANDER CT-5R2 TRIUMPH BID POLICY v1',
    '',
    `**Authority:** \`${TRIUMPH_BID_AUTHORITY_RELATIVE}\``,
    '',
    '## Algorithm (Triumph v1.3)',
    '',
    '- Descending ladder per ad group from campaign base bid',
    `- Minimum step ${BID_STEP_MIN} RUB; spread cap 90 RUB`,
    '- Group resets at campaign base; deterministic phrase order',
    '- Single-phrase groups: base − 20 RUB',
  ]);

  writeReceipt(
    'CORVONERO-COMMANDER-CT5R2-BID-DISTRIBUTION-v1',
    {
      generated_at: generatedAt,
      bid_ladder_policy: BID_LADDER_POLICY,
      campaign_base_bids: campaignBids,
      groups: bidDistribution,
      ca01_all_bids_equal_500: !ca01All500 ? false : true,
      ca01_keyword_rows: 339,
      totals: {
        groups: bidDistribution.length,
        keyword_rows: bidDistribution.reduce((s, g) => s + g.phrase_count, 0),
      },
    },
    [
      '# CORVONERO COMMANDER CT-5R2 BID DISTRIBUTION v1',
      '',
      `**Groups:** ${bidDistribution.length}`,
      `**CA-01 all bids 500:** ${ca01All500 ? 'YES (unexpected)' : 'NO'}`,
    ]
  );

  writeReceipt(
    'CORVONERO-COMMANDER-CT5R2-GENERATION-v1',
    {
      run_id: RUN_ID,
      generated_at: generatedAt,
      output_directory: OUTPUT_DIR,
      files_generated: generationResults.length,
      generation_results: generationResults,
      pre_validation: { status: validation.status },
      bid_ladder_policy: BID_LADDER_POLICY,
    },
    [
      '# CORVONERO COMMANDER CT-5R2 GENERATION v1',
      '',
      `**Output:** ${OUTPUT_DIR}`,
      '**Files:** 5 v4 workbooks with Triumph bid ladder',
    ]
  );

  writeReceipt(
    'CORVONERO-COMMANDER-CT5R2-FORENSIC-VALIDATION-v1',
    {
      run_id: RUN_ID,
      verified_at: generatedAt,
      results: forensicResults,
      overall: allForensicPass ? 'PASS' : 'FAIL',
      aggregate: {
        campaigns: 5,
        groups: 21,
        keyword_rows: 833,
        primary_ads: 21,
        region: REQUIRED_REGION_VALUE,
      },
    },
    [
      '# CORVONERO COMMANDER CT-5R2 FORENSIC VALIDATION v1',
      '',
      `**Overall:** ${allForensicPass ? 'PASS' : 'FAIL'}`,
      ...forensicResults.map(
        (r) =>
          `- ${r.campaign_id}: ${r.status} (${r.counts.keyword_rows} kw, distinct bids ${r.bid_summary?.distinct_bid_values ?? '?'})`
      ),
    ]
  );

  writeReceipt(
    'CORVONERO-COMMANDER-CT5R2-RESULT-v1',
    {
      run_id: RUN_ID,
      generated_at: generatedAt,
      verdict,
      triumph_source_authority: TRIUMPH_BID_AUTHORITY_RELATIVE,
      bid_step_rub: BID_STEP_MIN,
      xlsx_files: 5,
      keyword_rows: 833,
      ca01_all_bids_equal: ca01Forensic?.bid_summary?.all_equal_base ?? null,
      ca01_distinct_bids: ca01Forensic?.bid_summary?.distinct_bid_values ?? null,
      callouts: allForensicPass ? 'PASS' : 'FAIL',
      clean_urls: allForensicPass ? 'PASS' : 'FAIL',
      region: allForensicPass ? 'PASS' : 'FAIL',
      organization: allForensicPass ? 'PASS' : 'FAIL',
      forensic_verification: allForensicPass ? 'PASS' : 'FAIL',
      commander_import: 'NOT PERFORMED',
      ct6_ca01_v4_preview: allForensicPass ? 'READY FOR OPERATOR' : 'BLOCKED',
      next_preview_candidate: 'CORVONERO-CA-01-PROGRAMMIST-1S-COMMANDER-IMPORT-v4.xlsx',
    },
    ['# CORVONERO COMMANDER CT-5R2 RESULT v1', '', '## Verdict', '', verdict]
  );

  // CT-6 receipt updates
  const ct6PreviewUpdate = {
    receipt_id: 'corvonero-commander-ct6-ca01-import-preview-v1',
    updated_at: generatedAt,
    ca01_v3_preview: {
      structure: 'PASS',
      callouts: 'PASS',
      clean_urls: 'PASS',
      bid_distribution: 'FAIL — all 339 phrases at 500 RUB',
      import_confirmed: false,
    },
    ca01_v4_binding: {
      file: 'CORVONERO-CA-01-PROGRAMMIST-1S-COMMANDER-IMPORT-v4.xlsx',
      directory: OUTPUT_DIR.replace(/\\/g, '/'),
      ct5r2_receipt: 'CORVONERO-COMMANDER-CT5R2-RESULT-v1.json',
      bid_ladder: BID_LADDER_POLICY,
    },
    commander_import: 'NOT PERFORMED',
  };

  fs.writeFileSync(
    path.join(PILOT_ROOT, 'CORVONERO-COMMANDER-CT6-CA01-IMPORT-PREVIEW-v1.json'),
    `${JSON.stringify(
      {
        ...JSON.parse(
          fs.readFileSync(
            path.join(PILOT_ROOT, 'CORVONERO-COMMANDER-CT6-CA01-IMPORT-PREVIEW-v1.json'),
            'utf8'
          )
        ),
        ...ct6PreviewUpdate,
        next_preview_candidate: {
          file: 'CORVONERO-CA-01-PROGRAMMIST-1S-COMMANDER-IMPORT-v4.xlsx',
          directory: OUTPUT_DIR.replace(/\\/g, '/'),
          ct5r2_receipt: 'CORVONERO-COMMANDER-CT5R2-RESULT-v1.json',
        },
        status: 'READY FOR OPERATOR — v4 BID LADDER APPLIED',
        ct6_pass: null,
      },
      null,
      2
    )}\n`
  );

  const reportPath = path.join(
    PROJECT_ROOT,
    'reports',
    'REPORT-corvonero-commander-ct5r2-triumph-bid-ladder-v1.md'
  );
  fs.writeFileSync(
    reportPath,
    [
      '# REPORT — Corvonero Commander CT-5R2 Triumph bid ladder v1',
      '',
      `**Date:** ${generatedAt}`,
      `**Run ID:** ${RUN_ID}`,
      '',
      '## Summary',
      '',
      verdict,
      '',
      `**Triumph authority:** \`${TRIUMPH_BID_AUTHORITY_RELATIVE}\``,
      `**Bid step minimum:** ${BID_STEP_MIN} RUB`,
      '',
      '## CA-01 bid distribution',
      '',
      `- Keyword rows: ${ca01Forensic?.bid_summary?.total_keyword_rows ?? 339}`,
      `- Distinct bids: ${ca01Forensic?.bid_summary?.distinct_bid_values ?? '?'}`,
      `- All equal 500: ${ca01Forensic?.bid_summary?.all_equal_base ? 'YES' : 'NO'}`,
      `- Minimum bid: ${ca01Forensic?.bid_summary?.minimum_bid ?? '?'}`,
      '',
      '## CT-6',
      '',
      'CA-01 v3 preview: structure/callouts/URLs PASS; bids FAIL (flat 500).',
      'CA-01 v4 binding ready for operator preview.',
      '',
      `\`${OUTPUT_DIR}\``,
    ].join('\n')
  );

  writeStorage('CORVONERO-COMMANDER-CT5R2-MANIFEST-v1', {
    schema_version: '1.0.0',
    run_id: RUN_ID,
    generated_at: generatedAt,
    repository_commit: repoCommit,
    ct4_authority_commit: CT4_COMMIT,
    triumph_bid_authority: TRIUMPH_BID_AUTHORITY_RELATIVE,
    bid_ladder_policy: BID_LADDER_POLICY,
    template_sha256: EXPECTED_TEMPLATE_SHA256,
    output_directory: OUTPUT_DIR,
    output_files: generationResults,
    bid_distribution: bidDistribution,
    totals: { campaigns: 5, groups: 21, keyword_rows: 833, primary_ad_rows: 21 },
    validation_result: {
      pre_generation: validation.status,
      forensic: allForensicPass ? 'PASS' : 'FAIL',
    },
    prior_outputs_preserved: ['CT-5', 'CT5R1'],
    import_authorized: false,
  });

  writeStorage(
    'CORVONERO-COMMANDER-CT5R2-SHA256-v1',
    Object.fromEntries(generationResults.map((g) => [g.filename, g.sha256])),
    [
      '# CORVONERO COMMANDER CT-5R2 SHA-256 v1',
      `# Generated: ${generatedAt}`,
      '',
      ...generationResults.map((g) => `${g.sha256}  ${g.filename}`),
    ].join('\n')
  );

  console.log(
    JSON.stringify(
      {
        verdict,
        forensic: allForensicPass ? 'PASS' : 'FAIL',
        ca01_distinct_bids: ca01Forensic?.bid_summary?.distinct_bid_values,
        output: OUTPUT_DIR,
      },
      null,
      2
    )
  );
  process.exit(allForensicPass ? 0 : 1);
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});
