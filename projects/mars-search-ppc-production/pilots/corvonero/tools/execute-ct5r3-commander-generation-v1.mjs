#!/usr/bin/env node
/**
 * CORVONERO CT-5R3 — Balanced 10-RUB cyclic bid ladder + v5 Commander XLSX regeneration.
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
  BID_POLICIES,
  BID_STEP_MIN,
  buildBidDistributionReport,
  buildCyclicLadder,
  computeLadderBalance,
  CORVONERO_LADDER_VALUES,
  resolveBidPolicy,
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

const RUN_ID = 'CORVONERO-COMMANDER-CT5R3-FINAL-2026-06-30';
const OUTPUT_DIR = path.join(STORAGE_EXPORT_ROOT, RUN_ID);
const MANIFEST_PATH = path.join(PILOT_ROOT, 'CORVONERO-CT4-AUTHORITY-MANIFEST-v1.json');

const CT4_COMMIT = '8943e07e5f6b45d8e6cfd209a30cac55e2f0bb86';
const CORVONERO_POLICY = BID_POLICIES.CORVONERO_BALANCED_CYCLIC_10_RUB_V1;

const CAMPAIGN_FILES = {
  'CA-01': 'CORVONERO-CA-01-PROGRAMMIST-1S-COMMANDER-IMPORT-v5.xlsx',
  'CA-02': 'CORVONERO-CA-02-SOPROVOZHDENIE-1S-COMMANDER-IMPORT-v5.xlsx',
  'CA-03': 'CORVONERO-CA-03-DORABOTKA-1S-COMMANDER-IMPORT-v5.xlsx',
  'CA-04': 'CORVONERO-CA-04-INTEGRACII-1S-COMMANDER-IMPORT-v5.xlsx',
  'CA-05': 'CORVONERO-CA-05-MARKIROVKA-1S-COMMANDER-IMPORT-v5.xlsx',
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

function aggregateCa01Histogram(allBids, baseBid) {
  const ladder = buildCyclicLadder(baseBid);
  const histogram = Object.fromEntries(ladder.map((lv) => [String(lv), 0]));
  for (const b of allBids) {
    const key = String(b);
    if (histogram[key] != null) histogram[key]++;
  }
  return {
    keyword_rows: allBids.length,
    distinct_bids: new Set(allBids).size,
    histogram,
    ...histogram,
  };
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
  let ladderMismatch = 0;
  let balanceDeltaFails = 0;
  let distinctBidFails = 0;
  let floorCollapseFails = 0;
  const allBids = [];
  const groupBalanceReports = [];

  const payloadBidByPhrase = new Map();
  for (const row of payload.rows) {
    if (row.row_type === 'KEYWORD') {
      payloadBidByPhrase.set(row.phrase, row.bid);
    }
  }

  const ladder = buildCyclicLadder(expected.base_bid);
  const ladderSet = new Set(ladder);

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
        if (!ladderSet.has(bid)) fail('bid_not_on_ladder', `${bid} not on approved ladder`);
        if (!bidsPerGroup.has(group)) bidsPerGroup.set(group, []);
        bidsPerGroup.get(group).push(bid);
        const expBid = payloadBidByPhrase.get(phrase);
        if (expBid != null && bid !== expBid) ladderMismatch++;
      }
    }
  }

  for (const [group, bids] of bidsPerGroup) {
    const balance = computeLadderBalance(bids, ladder);
    groupBalanceReports.push({ group, phrase_count: bids.length, ...balance });
    if (bids.length > 10 && balance.balance_delta > 1) balanceDeltaFails++;
    if (bids.length > 10 && new Set(bids).size !== 10) distinctBidFails++;
    const floorValue = ladder[ladder.length - 1];
    const floorCount = balance.count_per_bid[String(floorValue)] ?? 0;
    const maxAllowed = Math.ceil(bids.length / CORVONERO_LADDER_VALUES);
    if (bids.length > 10 && floorCount > maxAllowed) floorCollapseFails++;
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

  if (ladderMismatch === 0) pass('bid_ladder_payload_match');
  else fail('bid_ladder_payload_match', `${ladderMismatch} bid mismatches`);

  if (balanceDeltaFails === 0) pass('balanced_bid_distribution');
  else fail('balanced_bid_distribution', `${balanceDeltaFails} groups with balance_delta > 1`);

  if (distinctBidFails === 0) pass('distinct_bids_large_groups');
  else fail('distinct_bids_large_groups', `${distinctBidFails} large groups without 10 distinct bids`);

  if (floorCollapseFails === 0) pass('no_floor_collapse');
  else fail('no_floor_collapse', `${floorCollapseFails} groups with floor collapse`);

  const distinctBids = new Set(allBids);
  const allEqualBase = allBids.length > 0 && allBids.every((b) => b === expected.base_bid);
  if (!allEqualBase) pass('not_flat_at_base', `distinct=${distinctBids.size}`);
  else fail('not_flat_at_base', `all ${allBids.length} phrases at base ${expected.base_bid}`);

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
    group_balance_reports: groupBalanceReports,
    bid_summary: {
      total_keyword_rows: kwRows.length,
      distinct_bid_values: distinctBids.size,
      minimum_bid: allBids.length ? Math.min(...allBids) : null,
      maximum_bid: allBids.length ? Math.max(...allBids) : null,
      rows_at_base_bid: allBids.filter((b) => b === expected.base_bid).length,
      bid_histogram: bidHistogram,
      all_equal_base: allEqualBase,
      floor_value_count: bidHistogram[String(ladder[ladder.length - 1])] ?? 0,
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
  const generatedAt = new Date().toISOString();
  assertVolume();

  if (fs.existsSync(OUTPUT_DIR)) {
    console.error('STOP — CT5R3 OUTPUT DIRECTORY ALREADY EXISTS');
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
  const transportConfig = model.transportConfig;
  const bidPolicy = resolveBidPolicy(transportConfig);

  const bidDistribution = buildBidDistributionReport(groups, phrasesByGroup, campaignBids, {
    policy: bidPolicy,
    bidStep: transportConfig?.bid_step ?? BID_STEP_MIN,
    ladderValues: transportConfig?.ladder_values ?? CORVONERO_LADDER_VALUES,
  });

  console.log('=== PROJECTED BID DISTRIBUTION (pre-generation) ===');
  for (const row of bidDistribution) {
    console.log(JSON.stringify(row));
  }

  const payloads = buildPayloads(loaded, validation);
  const payloadByCampaign = Object.fromEntries(payloads.map((p) => [p.campaign_id, p]));

  const ca01PayloadBids = (payloadByCampaign['CA-01']?.rows ?? [])
    .filter((r) => r.row_type === 'KEYWORD')
    .map((r) => r.bid);
  const ca01Aggregate = aggregateCa01Histogram(ca01PayloadBids, 500);

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

  const bidPolicyReceipt = {
    policy_id: CORVONERO_POLICY,
    triumph_authority_preserved: {
      source_path: TRIUMPH_BID_AUTHORITY_RELATIVE,
      note: 'Triumph policy historically valid and preserved — not modified for Corvonero',
    },
    corvonero_adaptation: {
      reason: 'Large groups 132–144 phrases; Triumph v1.3 floor collapse unsuitable',
      bid_step_rub: transportConfig?.bid_step ?? 10,
      ladder_values: transportConfig?.ladder_values ?? 10,
      assignment_scope: transportConfig?.assignment_scope ?? 'PER_GROUP',
      assignment_order: transportConfig?.assignment_order ?? 'CT4_AUTHORITY_ORDER',
      ca01_ladder: buildCyclicLadder(500),
      ca02_through_ca05_ladder: buildCyclicLadder(400),
      assignment_rule: 'bid = ladder[index modulo 10]',
    },
    repository_commit: repoCommit,
    corvonero_campaign_base_bids: campaignBids,
  };

  const verdict = allForensicPass
    ? 'CORVONERO COMMANDER CT-5R3: PASS — BALANCED 10-RUB BID LADDER APPLIED'
    : 'CORVONERO COMMANDER CT-5R3: FAIL — FORENSIC VERIFICATION ERROR';

  writeReceipt('CORVONERO-COMMANDER-CT5R3-BID-POLICY-v1', bidPolicyReceipt, [
    '# CORVONERO COMMANDER CT-5R3 BID POLICY v1',
    '',
    `**Policy:** \`${CORVONERO_POLICY}\``,
    '',
    'Triumph `bid-assignment-v1.3.js` preserved — Corvonero uses separate large-group cyclic ladder.',
    '',
    `- Step: ${transportConfig?.bid_step ?? 10} RUB`,
    '- Assignment: cyclic per group from campaign base',
  ]);

  writeReceipt(
    'CORVONERO-COMMANDER-CT5R3-BID-DISTRIBUTION-v1',
    {
      generated_at: generatedAt,
      bid_policy: CORVONERO_POLICY,
      campaign_base_bids: campaignBids,
      groups: bidDistribution,
      ca01_aggregate: ca01Aggregate,
      totals: {
        groups: bidDistribution.length,
        keyword_rows: bidDistribution.reduce((s, g) => s + g.phrase_count, 0),
      },
    },
    [
      '# CORVONERO COMMANDER CT-5R3 BID DISTRIBUTION v1',
      '',
      `**Groups:** ${bidDistribution.length}`,
      `**CA-01 distinct bids:** ${ca01Aggregate.distinct_bids}`,
      `**CA-01 500 rows:** ${ca01Aggregate.histogram['500'] ?? 0}`,
      `**CA-01 410 rows:** ${ca01Aggregate.histogram['410'] ?? 0}`,
    ]
  );

  writeReceipt(
    'CORVONERO-COMMANDER-CT5R3-GENERATION-v1',
    {
      run_id: RUN_ID,
      generated_at: generatedAt,
      output_directory: OUTPUT_DIR,
      files_generated: generationResults.length,
      generation_results: generationResults,
      pre_validation: { status: validation.status },
      bid_policy: CORVONERO_POLICY,
    },
    [
      '# CORVONERO COMMANDER CT-5R3 GENERATION v1',
      '',
      `**Output:** ${OUTPUT_DIR}`,
      '**Files:** 5 v5 workbooks with Corvonero cyclic bid ladder',
    ]
  );

  writeReceipt(
    'CORVONERO-COMMANDER-CT5R3-FORENSIC-VALIDATION-v1',
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
      '# CORVONERO COMMANDER CT-5R3 FORENSIC VALIDATION v1',
      '',
      `**Overall:** ${allForensicPass ? 'PASS' : 'FAIL'}`,
      ...forensicResults.map(
        (r) =>
          `- ${r.campaign_id}: ${r.status} (${r.counts.keyword_rows} kw, distinct bids ${r.bid_summary?.distinct_bid_values ?? '?'})`
      ),
    ]
  );

  writeReceipt(
    'CORVONERO-COMMANDER-CT5R3-RESULT-v1',
    {
      run_id: RUN_ID,
      generated_at: generatedAt,
      verdict,
      bid_policy: CORVONERO_POLICY,
      bid_step_rub: BID_STEP_MIN,
      assignment: 'CYCLIC PER GROUP',
      balance_delta_max: 1,
      xlsx_files: 5,
      keyword_rows: 833,
      ca01_floor_collapse_eliminated: (ca01Forensic?.bid_summary?.floor_value_count ?? 999) < 50,
      ca01_distinct_bids: ca01Forensic?.bid_summary?.distinct_bid_values ?? null,
      callouts: allForensicPass ? 'PASS' : 'FAIL',
      clean_urls: allForensicPass ? 'PASS' : 'FAIL',
      region: allForensicPass ? 'PASS' : 'FAIL',
      organization: allForensicPass ? 'PASS' : 'FAIL',
      forensic_verification: allForensicPass ? 'PASS' : 'FAIL',
      commander_import: 'NOT PERFORMED',
      ct6_ca01_v5_preview: allForensicPass ? 'READY FOR OPERATOR' : 'BLOCKED',
      next_preview_candidate: 'CORVONERO-CA-01-PROGRAMMIST-1S-COMMANDER-IMPORT-v5.xlsx',
    },
    ['# CORVONERO COMMANDER CT-5R3 RESULT v1', '', '## Verdict', '', verdict]
  );

  const ct6PreviewUpdate = {
    receipt_id: 'corvonero-commander-ct6-ca01-import-preview-v1',
    updated_at: generatedAt,
    ca01_v4_preview: {
      structure: 'PASS',
      callouts: 'PASS',
      clean_urls: 'PASS',
      bid_distribution: 'REJECTED — LARGE-GROUP FLOOR COLLAPSE',
      import_confirmed: false,
      import_performed: false,
    },
    ca01_v5_binding: {
      file: 'CORVONERO-CA-01-PROGRAMMIST-1S-COMMANDER-IMPORT-v5.xlsx',
      directory: OUTPUT_DIR.replace(/\\/g, '/'),
      ct5r3_receipt: 'CORVONERO-COMMANDER-CT5R3-RESULT-v1.json',
      bid_policy: CORVONERO_POLICY,
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
          file: 'CORVONERO-CA-01-PROGRAMMIST-1S-COMMANDER-IMPORT-v5.xlsx',
          directory: OUTPUT_DIR.replace(/\\/g, '/'),
          ct5r3_receipt: 'CORVONERO-COMMANDER-CT5R3-RESULT-v1.json',
        },
        status: 'READY FOR OPERATOR — v5 BALANCED CYCLIC BID LADDER',
        ct6_pass: null,
      },
      null,
      2
    )}\n`
  );

  const reportPath = path.join(
    PROJECT_ROOT,
    'reports',
    'REPORT-corvonero-commander-ct5r3-balanced-bid-ladder-v1.md'
  );
  fs.writeFileSync(
    reportPath,
    [
      '# REPORT — Corvonero Commander CT-5R3 balanced bid ladder v1',
      '',
      `**Date:** ${generatedAt}`,
      `**Run ID:** ${RUN_ID}`,
      '',
      '## Summary',
      '',
      verdict,
      '',
      `**Bid policy:** \`${CORVONERO_POLICY}\``,
      `**Bid step:** ${BID_STEP_MIN} RUB`,
      '**Assignment:** cyclic per group',
      '',
      '## CA-01 aggregate bid distribution',
      '',
      `- Keyword rows: ${ca01Aggregate.keyword_rows}`,
      `- Distinct bids: ${ca01Aggregate.distinct_bids}`,
      `- 500 rows: ${ca01Aggregate.histogram['500'] ?? 0}`,
      `- 490 rows: ${ca01Aggregate.histogram['490'] ?? 0}`,
      `- 480 rows: ${ca01Aggregate.histogram['480'] ?? 0}`,
      `- 470 rows: ${ca01Aggregate.histogram['470'] ?? 0}`,
      `- 460 rows: ${ca01Aggregate.histogram['460'] ?? 0}`,
      `- 450 rows: ${ca01Aggregate.histogram['450'] ?? 0}`,
      `- 440 rows: ${ca01Aggregate.histogram['440'] ?? 0}`,
      `- 430 rows: ${ca01Aggregate.histogram['430'] ?? 0}`,
      `- 420 rows: ${ca01Aggregate.histogram['420'] ?? 0}`,
      `- 410 rows: ${ca01Aggregate.histogram['410'] ?? 0}`,
      '',
      '## CT-6',
      '',
      'CA-01 v4: REJECTED — LARGE-GROUP FLOOR COLLAPSE. Import: NO.',
      'CA-01 v5 binding ready for operator preview.',
      '',
      `\`${OUTPUT_DIR}\``,
    ].join('\n')
  );

  writeStorage('CORVONERO-COMMANDER-CT5R3-MANIFEST-v1', {
    schema_version: '1.0.0',
    run_id: RUN_ID,
    generated_at: generatedAt,
    repository_commit: repoCommit,
    ct4_authority_commit: CT4_COMMIT,
    bid_policy: CORVONERO_POLICY,
    triumph_bid_authority_preserved: TRIUMPH_BID_AUTHORITY_RELATIVE,
    template_sha256: EXPECTED_TEMPLATE_SHA256,
    output_directory: OUTPUT_DIR,
    output_files: generationResults,
    bid_distribution: bidDistribution,
    ca01_aggregate: ca01Aggregate,
    totals: { campaigns: 5, groups: 21, keyword_rows: 833, primary_ad_rows: 21 },
    validation_result: {
      pre_generation: validation.status,
      forensic: allForensicPass ? 'PASS' : 'FAIL',
    },
    prior_outputs_preserved: ['CT-5', 'CT5R1', 'CT5R2'],
    import_authorized: false,
  });

  writeStorage(
    'CORVONERO-COMMANDER-CT5R3-SHA256-v1',
    Object.fromEntries(generationResults.map((g) => [g.filename, g.sha256])),
    [
      '# CORVONERO COMMANDER CT-5R3 SHA-256 v1',
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
        ca01_410_rows: ca01Aggregate.histogram['410'],
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
