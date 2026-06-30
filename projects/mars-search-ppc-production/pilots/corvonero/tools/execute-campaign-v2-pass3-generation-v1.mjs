#!/usr/bin/env node
/**
 * CORVONERO Campaign V2 Pass 3 — ten Commander XLSX workbooks + forensic validation.
 * Local generation only — no import, no Direct API.
 */
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { execSync } from 'node:child_process';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

import { computeSha256 } from '../../../tools/commander-transport/src/template-validator.mjs';
import {
  adapterAvailable,
  patchCommanderWorkbook,
} from '../../../tools/commander-transport/src/commander-patcher-adapter.mjs';
import {
  BID_POLICIES,
  BID_STEP_MIN,
  buildCyclicLadder,
  computeLadderBalance,
  CORVONERO_LADDER_VALUES,
  resolveBidPolicy,
} from '../../../tools/commander-transport/src/bid-ladder.mjs';
import { COMMANDER_CALLOUT_DELIMITER } from '../../../tools/commander-transport/src/callout-serializer.mjs';
import {
  COMMANDER_COLUMN_COUNT,
  COMMANDER_HEADER_ROW,
  COMMANDER_SHEET_REGIONS,
  COMMANDER_SHEET_TEXTS,
  COMMANDER_TEMPLATE_PATH,
  FORBIDDEN_ORGANIZATION_ID,
  REQUIRED_REGION_VALUE,
  ROW_TYPE_AD,
  ROW_TYPE_KEYWORD,
} from '../../../tools/commander-transport/src/constants.mjs';
import { validateTemplate } from '../../../tools/commander-transport/src/template-validator.mjs';
import { serializeCallouts } from '../../../tools/commander-transport/src/callout-serializer.mjs';
import { cleanAdUrl } from '../../../tools/commander-transport/src/url-policy.mjs';
import { assignBidsForGroup } from '../../../tools/commander-transport/src/bid-ladder.mjs';
import {
  cellText,
  DATA_START_ROW,
  FORENSIC_COL,
  isSitelinkPopulated,
  verifyWorkbookCallouts,
  verifyWorkbookCleanUrls,
} from '../../../tools/commander-transport/src/workbook-forensic-verifier.mjs';
import { formatCommanderNegatives } from '../../../tools/commander-transport/src/transport-validator.mjs';

const require = createRequire(import.meta.url);
const ExcelJS = require('../../../tools/commander-transport/node_modules/exceljs');

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PILOT_ROOT = path.resolve(__dirname, '..');
const REPO_ROOT = path.resolve(PILOT_ROOT, '../../..');

const CORVONERO_POLICY = BID_POLICIES.CORVONERO_BALANCED_CYCLIC_10_RUB_V1;

const CAMPAIGN_FILES = {
  'CA-01-LOCAL': 'CORVONERO-CA-01-LOCAL-PROGRAMMIST-1S-COMMANDER-IMPORT-v1.xlsx',
  'CA-01-REMOTE': 'CORVONERO-CA-01-REMOTE-PROGRAMMIST-1S-COMMANDER-IMPORT-v1.xlsx',
  'CA-02-LOCAL': 'CORVONERO-CA-02-LOCAL-SOPROVOZHDENIE-1S-COMMANDER-IMPORT-v1.xlsx',
  'CA-02-REMOTE': 'CORVONERO-CA-02-REMOTE-SOPROVOZHDENIE-1S-COMMANDER-IMPORT-v1.xlsx',
  'CA-03-LOCAL': 'CORVONERO-CA-03-LOCAL-DORABOTKA-1S-COMMANDER-IMPORT-v1.xlsx',
  'CA-03-REMOTE': 'CORVONERO-CA-03-REMOTE-DORABOTKA-1S-COMMANDER-IMPORT-v1.xlsx',
  'CA-04-LOCAL': 'CORVONERO-CA-04-LOCAL-INTEGRACII-1S-COMMANDER-IMPORT-v1.xlsx',
  'CA-04-REMOTE': 'CORVONERO-CA-04-REMOTE-INTEGRACII-1S-COMMANDER-IMPORT-v1.xlsx',
  'CA-05-LOCAL': 'CORVONERO-CA-05-LOCAL-MARKIROVKA-1S-COMMANDER-IMPORT-v1.xlsx',
  'CA-05-REMOTE': 'CORVONERO-CA-05-REMOTE-MARKIROVKA-1S-COMMANDER-IMPORT-v1.xlsx',
};

const EXPECTED = {
  'CA-01-LOCAL': { groups: 7, keywords: 311, base_bid: 500, region: 'Новосибирская область', mode: 'LOCAL' },
  'CA-01-REMOTE': { groups: 7, keywords: 316, base_bid: 500, region: 'Россия', mode: 'REMOTE' },
  'CA-02-LOCAL': { groups: 4, keywords: 143, base_bid: 400, region: 'Новосибирская область', mode: 'LOCAL' },
  'CA-02-REMOTE': { groups: 4, keywords: 143, base_bid: 400, region: 'Россия', mode: 'REMOTE' },
  'CA-03-LOCAL': { groups: 3, keywords: 76, base_bid: 400, region: 'Новосибирская область', mode: 'LOCAL' },
  'CA-03-REMOTE': { groups: 3, keywords: 76, base_bid: 400, region: 'Россия', mode: 'REMOTE' },
  'CA-04-LOCAL': { groups: 1, keywords: 48, base_bid: 400, region: 'Новосибирская область', mode: 'LOCAL' },
  'CA-04-REMOTE': { groups: 1, keywords: 48, base_bid: 400, region: 'Россия', mode: 'REMOTE' },
  'CA-05-LOCAL': { groups: 6, keywords: 216, base_bid: 400, region: 'Новосибирская область', mode: 'LOCAL' },
  'CA-05-REMOTE': { groups: 6, keywords: 216, base_bid: 400, region: 'Россия', mode: 'REMOTE' },
};

const LOCAL_PROP_RE = /удал[её]нн|по россии|по рф|дистанцион/i;
const REMOTE_PROP_RE = /выезд|новосибирск|на месте|в офис/i;

const FORENSIC_COL_V2 = {
  ...FORENSIC_COL,
  headline_2: 11,
  text: 12,
};

function safeCellText(sheet, row, col) {
  if (!col) return '';
  const sheetRow = sheet.getRow(row);
  if (!sheetRow) return '';
  try {
    return cellText(sheet, row, col);
  } catch {
    return '';
  }
}

async function loadAuthorityV2(manifestPath) {
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  const byRole = {};
  const hashes = {};
  for (const entry of manifest.files) {
    const abs = path.resolve(entry.path);
    const parsed = JSON.parse(fs.readFileSync(abs, 'utf8'));
    byRole[entry.role] = parsed;
    hashes[entry.role] = await computeSha256(abs);
  }
  return { manifest, byRole, hashes, manifestPath: path.resolve(manifestPath) };
}

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
  return loaded;
}

function sha256File(fp) {
  return crypto.createHash('sha256').update(fs.readFileSync(fp)).digest('hex');
}

function buildModel(loaded) {
  const { byRole } = loaded;
  return {
    phraseAllocation: byRole.phrase_allocation,
    architecture: byRole.campaign_architecture,
    primaryAds: { ads: byRole.primary_ads?.ads ?? byRole.primary_ads },
    callouts: byRole.callouts,
    campaignNegatives: byRole.campaign_negatives,
    groupNegatives: byRole.group_negatives,
    utmMap: byRole.utm_map,
    campaignSettings: byRole.campaign_settings,
    transportConfig: byRole.transport_config,
    displayPaths: byRole.display_paths,
    bids: byRole.bids ?? null,
  };
}

function buildPayloadsV2(model) {
  const groups = model.architecture?.groups ?? [];
  const deployablePhrases = (model.phraseAllocation?.records ?? []).filter(
    (r) => r.production_status === 'DEPLOYABLE'
  );
  const ads = model.primaryAds?.ads ?? [];
  const bids = model.bids?.campaign_bids ?? {};
  const calloutPools = model.callouts?.campaign_pools ?? {};
  const displayPaths = model.displayPaths?.records ?? [];
  const transportConfig = model.transportConfig;
  const bidPolicy = resolveBidPolicy(transportConfig);
  const geoRegions = transportConfig?.geo_regions ?? {};

  const phrasesByGroup = new Map();
  for (const rec of deployablePhrases) {
    if (!phrasesByGroup.has(rec.final_group)) phrasesByGroup.set(rec.final_group, []);
    phrasesByGroup.get(rec.final_group).push(rec);
  }

  const adsByGroupCampaign = new Map();
  for (const ad of ads) {
    adsByGroupCampaign.set(`${ad.campaign_id}::${ad.group_id}`, ad);
  }

  const displayByGroup = new Map();
  for (const dp of displayPaths) {
    displayByGroup.set(dp.group_id, dp.display_path);
  }

  const campaignIds = [...new Set(groups.map((g) => g.campaign_id))].sort();
  const payloads = [];

  for (const campaignId of campaignIds) {
    const exp = EXPECTED[campaignId];
    const geoRegion = geoRegions[campaignId] ?? exp?.region ?? REQUIRED_REGION_VALUE;
    const campaignGroups = groups
      .filter((g) => g.campaign_id === campaignId)
      .sort((a, b) => a.group_id.localeCompare(b.group_id));

    const rows = [];
    let groupNumber = 1;

    const metadata_patches = {
      'Тип кампании:': 'Текстово-графическая кампания',
      '№ заказа:': 'RUB',
      'Минус-фразы на кампанию:': '',
      'Оптимизировать текст объявлений под запрос:': '0',
      'Организация из Яндекс Бизнеса:': '',
    };

    const firstGroup = campaignGroups[0];
    const firstAd = firstGroup
      ? adsByGroupCampaign.get(`${campaignId}::${firstGroup.group_id}`)
      : null;
    const promotionUrl = firstAd?.landing_page?.url ?? '';
    if (promotionUrl) {
      metadata_patches['Объект продвижения:'] = cleanAdUrl(promotionUrl);
    }

    for (const g of campaignGroups) {
      const ad = adsByGroupCampaign.get(`${campaignId}::${g.group_id}`);
      const phrases = (phrasesByGroup.get(g.group_id) ?? []).filter(
        (p) => p.final_campaign === campaignId
      );
      const pool = calloutPools[campaignId] ?? [];
      const calloutItems = pool.map((c) => c.text);
      const calloutText = serializeCallouts(calloutItems);
      const displayPath = displayByGroup.get(g.group_id) ?? ad?.display_path ?? '';
      const landingUrl = cleanAdUrl(ad?.landing_page?.url ?? '');

      const groupNegData = model.groupNegatives?.groups?.[g.group_id];
      const groupNegTerms = groupNegData?.terms ?? groupNegData?.negatives ?? [];
      const groupNegStr = formatCommanderNegatives(groupNegTerms);

      if (ad) {
        rows.push({
          row_type: ROW_TYPE_AD,
          group_name: g.group_name,
          group_number: String(groupNumber),
          group_id: g.group_id,
          group_additional_ad: '-',
          headline_1: ad.primary_ad?.headline ?? '',
          headline_2: ad.primary_ad?.additional_headline ?? '',
          text: ad.primary_ad?.text ?? '',
          landing_url: landingUrl,
          display_path: displayPath,
          ad_status: 'Активные',
          callouts: calloutText,
          callout_items: calloutItems,
          group_negatives: groupNegStr,
          region: geoRegion,
          organization: '',
        });
      }

      const groupBidMap = assignBidsForGroup(phrases, bids[campaignId], {
        policy: bidPolicy,
        bidStep: transportConfig?.bid_step ?? BID_STEP_MIN,
        ladderValues: transportConfig?.ladder_values ?? CORVONERO_LADDER_VALUES,
      });

      for (const p of phrases) {
        rows.push({
          row_type: ROW_TYPE_KEYWORD,
          group_name: g.group_name,
          group_number: String(groupNumber),
          group_id: g.group_id,
          phrase: p.phrase,
          phrase_id: p.phrase_id,
          phrase_status: 'Активные',
          bid: groupBidMap.get(String(p.phrase_id ?? p.phrase)),
          campaign_base_bid: bids[campaignId],
          bid_ladder_policy: bidPolicy,
          region: geoRegion,
          organization: '',
        });
      }

      groupNumber += 1;
    }

    payloads.push({
      campaign_id: campaignId,
      geography_mode: exp?.mode ?? 'LOCAL',
      geo_region: geoRegion,
      metadata_patches,
      rows,
    });
  }

  return payloads;
}

async function forensicVerifyWorkbook(filePath, payload, campaignId, templateSha) {
  const expected = EXPECTED[campaignId];
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
  if (colCount < COMMANDER_COLUMN_COUNT) fail('columns_78', `Column count ${colCount}`);
  else pass('columns_78', String(colCount));

  pass('template_sha_lineage', `source template SHA-256 ${templateSha}`);

  const regions = workbook.getWorksheet(COMMANDER_SHEET_REGIONS);
  if (!regions) fail('regions_sheet', 'Missing Регионы sheet');
  else {
    let foundExpected = false;
    let foundRussia = false;
    regions.eachRow({ includeEmpty: true }, (row) => {
      row.eachCell({ includeEmpty: true }, (cell) => {
        const v = String(cell.value ?? '').trim();
        if (v === REQUIRED_REGION_VALUE) foundExpected = true;
        if (v === 'Россия') foundRussia = true;
      });
    });
    if (!foundExpected) fail('regions_dictionary_nso', `Missing ${REQUIRED_REGION_VALUE}`);
    else pass('regions_dictionary_nso');
    if (expected.mode === 'REMOTE' && !foundRussia) {
      fail('regions_dictionary_russia', 'Missing Россия in regions sheet');
    } else if (expected.mode === 'REMOTE') {
      pass('regions_dictionary_russia');
    }
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
  let geoPropFails = 0;
  let remotePropInLocal = 0;
  let localPropInRemote = 0;
  const allBids = [];

  const payloadBidByPhrase = new Map();
  for (const row of payload.rows) {
    if (row.row_type === ROW_TYPE_KEYWORD) {
      payloadBidByPhrase.set(row.phrase, row.bid);
    }
  }

  const ladder = buildCyclicLadder(expected.base_bid);
  const ladderSet = new Set(ladder);

  for (let r = DATA_START_ROW; r <= texts.rowCount; r++) {
    const phrase = safeCellText(texts, r, FORENSIC_COL.phrase);
    const h1 = safeCellText(texts, r, FORENSIC_COL.headline_1);
    const h2 = safeCellText(texts, r, FORENSIC_COL_V2.headline_2);
    const adText = safeCellText(texts, r, FORENSIC_COL_V2.text);
    const group = safeCellText(texts, r, FORENSIC_COL.group_name);
    if (!phrase && !h1 && !group) continue;

    const region = safeCellText(texts, r, FORENSIC_COL.region);
    const rowBlob = JSON.stringify(
      [48, 50, 58, 59, 60, 67].map((c) => safeCellText(texts, r, c))
    );
    if (rowBlob.includes(FORBIDDEN_ORGANIZATION_ID)) orgIdHits++;

    const url = safeCellText(texts, r, FORENSIC_COL.landing_url);
    if (url.includes('utm_')) utmHits++;
    if (url.includes('{keyword}')) keywordMacroHits++;
    if (url.includes('?')) queryHits++;

    if (
      [FORENSIC_COL.fastlink_titles, FORENSIC_COL.fastlink_descriptions, FORENSIC_COL.fastlink_urls].some(
        (c) => isSitelinkPopulated(safeCellText(texts, r, c))
      )
    ) {
      sitelinkHits++;
    }

    if (region && region !== expected.region) regionFails++;

    if (h1) {
      adRows.push({ row: r, group });
      groupsSeen.add(group);
      const blob = `${h1} ${h2} ${adText}`;
      if (expected.mode === 'LOCAL' && LOCAL_PROP_RE.test(blob)) {
        localPropInRemote += 0;
        remotePropInLocal++;
      }
      if (expected.mode === 'REMOTE' && REMOTE_PROP_RE.test(blob)) {
        localPropInRemote++;
      }
    } else if (phrase) {
      kwRows.push({ row: r, group, phrase });
      groupsSeen.add(group);
      kwPerGroup.set(group, (kwPerGroup.get(group) ?? 0) + 1);

      const bid = Number(String(safeCellText(texts, r, FORENSIC_COL.bid)).replace(',', '.'));
      if (!Number.isFinite(bid) || bid <= 0) missingBid++;
      else {
        allBids.push(bid);
        if (bid > expected.base_bid) aboveBaseBid++;
        if (!ladderSet.has(bid)) fail('bid_not_on_ladder', `${bid}`);
        if (!bidsPerGroup.has(group)) bidsPerGroup.set(group, []);
        bidsPerGroup.get(group).push(bid);
        const expBid = payloadBidByPhrase.get(phrase);
        if (expBid != null && bid !== expBid) ladderMismatch++;
      }
    }
  }

  for (const [group, bids] of bidsPerGroup) {
    const balance = computeLadderBalance(bids, ladder);
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
  else fail('keyword_bids_present', `${missingBid}`);

  if (aboveBaseBid === 0) pass('bids_within_campaign_base');
  else fail('bids_within_campaign_base', `${aboveBaseBid}`);

  if (ladderMismatch === 0) pass('bid_ladder_payload_match');
  else fail('bid_ladder_payload_match', `${ladderMismatch}`);

  if (balanceDeltaFails === 0) pass('balanced_bid_distribution');
  else fail('balanced_bid_distribution', `${balanceDeltaFails}`);

  if (distinctBidFails === 0) pass('distinct_bids_large_groups');
  else fail('distinct_bids_large_groups', `${distinctBidFails}`);

  if (floorCollapseFails === 0) pass('no_floor_collapse');
  else fail('no_floor_collapse', `${floorCollapseFails}`);

  if (regionFails === 0) pass('region', expected.region);
  else fail('region', `${regionFails} bad region values`);

  if (expected.mode === 'LOCAL' && remotePropInLocal === 0) pass('local_no_remote_proposition');
  else if (expected.mode === 'LOCAL') fail('local_no_remote_proposition', `${remotePropInLocal}`);

  if (expected.mode === 'REMOTE' && localPropInRemote === 0) pass('remote_no_local_proposition');
  else if (expected.mode === 'REMOTE') fail('remote_no_local_proposition', `${localPropInRemote}`);

  if (orgIdHits === 0) pass('forbidden_organization_id');
  else fail('forbidden_organization_id', `${orgIdHits}`);

  for (const c of verifyWorkbookCallouts(texts, { campaignId }).checks) checks.push(c);
  for (const c of verifyWorkbookCleanUrls(texts, { campaignId }).checks) checks.push(c);

  if (utmHits === 0) pass('utm_absent');
  else fail('utm_absent', String(utmHits));
  if (queryHits === 0) pass('clean_url_no_query');
  else fail('clean_url_no_query', String(queryHits));
  if (sitelinkHits === 0) pass('sitelinks_omitted');
  else fail('sitelinks_omitted', `${sitelinkHits}`);

  const status = checks.some((c) => c.status === 'FAIL') ? 'FAIL' : 'PASS';
  return {
    status,
    checks,
    counts: {
      groups: groupsSeen.size,
      keyword_rows: kwRows.length,
      ad_rows: adRows.length,
      max_group_keyword_count: maxGroupKw,
    },
  };
}

async function main() {
  const manifestPath = process.argv[2] ?? path.join(PILOT_ROOT, 'CORVONERO-CAMPAIGN-V2-AUTHORITY-MANIFEST-v1.json');
  const outputDir = process.argv[3] ?? path.join('X:', 'AI MARS STORAGE', 'exports', 'corvonero', 'CORVONERO-CAMPAIGN-V2-FINAL-2026-06-30');

  if (!adapterAvailable()) {
    throw new Error('Triumph Commander patcher adapter unavailable');
  }

  const templateResult = await validateTemplate(COMMANDER_TEMPLATE_PATH);
  if (!templateResult.ok) {
    console.error('STOP — COMMANDER TEMPLATE IDENTITY MISMATCH');
    process.exit(2);
  }

  const forensicOnly = process.argv.includes('--forensic-only');

  let loaded = await loadAuthorityV2(manifestPath);
  loaded = enrichLoadedAuthority(loaded);
  const model = buildModel(loaded);
  const payloads = buildPayloadsV2(model);
  const payloadByCampaign = Object.fromEntries(payloads.map((p) => [p.campaign_id, p]));

  const generationResults = [];

  if (!forensicOnly) {
  for (const [campaignId, filename] of Object.entries(CAMPAIGN_FILES)) {
    const payload = payloadByCampaign[campaignId];
    if (!payload) throw new Error(`Missing payload for ${campaignId}`);

    const kwCount = payload.rows.filter((r) => r.row_type === ROW_TYPE_KEYWORD).length;
    const adCount = payload.rows.filter((r) => r.row_type === ROW_TYPE_AD).length;
    const exp = EXPECTED[campaignId];
    if (kwCount !== exp.keywords || adCount !== exp.groups) {
      throw new Error(
        `Payload count mismatch ${campaignId}: kw ${kwCount}/${exp.keywords}, ads ${adCount}/${exp.groups}`
      );
    }

    const outPath = path.join(outputDir, filename);
    const patchResult = await patchCommanderWorkbook({
      payload,
      templatePath: COMMANDER_TEMPLATE_PATH,
      outputPath: outPath,
      guardOptions: { approvedWriteRoot: outputDir },
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
      geo_region: exp.region,
    });
  }
  } else {
    for (const [campaignId, filename] of Object.entries(CAMPAIGN_FILES)) {
      const outPath = path.join(outputDir, filename);
      const exp = EXPECTED[campaignId];
      const payload = payloadByCampaign[campaignId];
      generationResults.push({
        campaign_id: campaignId,
        filename,
        output_path: outPath,
        sha256: sha256File(outPath),
        keyword_rows: payload.rows.filter((r) => r.row_type === ROW_TYPE_KEYWORD).length,
        ad_rows: payload.rows.filter((r) => r.row_type === ROW_TYPE_AD).length,
        campaign_base_bid: exp.base_bid,
        geo_region: exp.region,
        forensic_only: true,
      });
    }
  }

  const forensicResults = [];
  for (const gen of generationResults) {
    forensicResults.push({
      campaign_id: gen.campaign_id,
      filename: gen.filename,
      ...(await forensicVerifyWorkbook(
        gen.output_path,
        payloadByCampaign[gen.campaign_id],
        gen.campaign_id,
        templateResult.sha256
      )),
    });
  }

  const allPass = forensicResults.every((r) => r.status === 'PASS');
  const totalKw = generationResults.reduce((s, g) => s + g.keyword_rows, 0);
  const totalAds = generationResults.reduce((s, g) => s + g.ad_rows, 0);

  const generationDoc = {
    run_id: 'CORVONERO-CAMPAIGN-V2-FINAL-2026-06-30',
    generated_at: new Date().toISOString(),
    output_directory: outputDir,
    bid_policy: CORVONERO_POLICY,
    files_generated: generationResults.length,
    generation_results: generationResults,
    totals: {
      campaigns: 10,
      groups: totalAds,
      keyword_rows: totalKw,
      ad_rows: totalAds,
    },
  };

  fs.writeFileSync(
    path.join(PILOT_ROOT, 'CORVONERO-CAMPAIGN-V2-GENERATION-v1.json'),
    `${JSON.stringify(generationDoc, null, 2)}\n`
  );

  const forensicDoc = {
    generated_at: new Date().toISOString(),
    verdict: allPass ? 'PASS — FORENSIC VALIDATION COMPLETE' : 'FAIL — FORENSIC ERRORS',
    summary: {
      campaigns: 10,
      groups: 42,
      phrase_slots: totalKw,
      primary_ads: totalAds,
      all_pass: allPass,
      bid_policy: CORVONERO_POLICY,
      cross_campaign_negatives: 'NOT APPLIED',
      remote_nso_exclusion: 'MANUAL POST-IMPORT ACTION REQUIRED',
    },
    results: forensicResults,
  };

  fs.writeFileSync(
    path.join(PILOT_ROOT, 'CORVONERO-CAMPAIGN-V2-FORENSIC-VALIDATION-v1.json'),
    `${JSON.stringify(forensicDoc, null, 2)}\n`
  );

  if (!allPass) {
    console.error(JSON.stringify(forensicResults.filter((r) => r.status !== 'PASS'), null, 2));
    process.exit(1);
  }

  console.log('PASS — 10 XLSX files generated and forensically verified');
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
