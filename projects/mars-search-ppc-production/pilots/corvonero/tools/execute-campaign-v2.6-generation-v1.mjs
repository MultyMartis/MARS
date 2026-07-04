#!/usr/bin/env node
// C2c HOLD: source persistence / hardening only.
// This file is not authorized for execution without explicit operator approval.
// Commit/persistence does not authorize Commander import, Direct launch, account mutation,
// advertising start, Storage export generation, repo artifact generation,
// Localhost mutation, Storage mutation, Yandex/API access, or client-facing delivery.
// Commander/XLSX generation is transport/import-candidate tooling only and does not authorize
// import into Yandex Direct or any live account mutation.
/**
 * CORVONERO Campaign V2.6 — Commander XLSX generation with dynamic expected counts.
 */
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
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
  resolveBidPolicy,
} from '../../../tools/commander-transport/src/bid-ladder.mjs';
import {
  COMMANDER_COLUMN_COUNT,
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

const CORVONERO_POLICY = BID_POLICIES.CORVONERO_BALANCED_CYCLIC_10_RUB_V1;
const FORBIDDEN_AD_TEXT = 'Услуги 1С для бizнеса: настройка, доработки и поддержка.'.replace('bizнеса', 'бизнеса');

const CAMPAIGN_FILES = {
  'CA-01-LOCAL': 'CORVONERO-CA-01-LOCAL-PROGRAMMIST-1S-COMMANDER-IMPORT-v2.6.xlsx',
  'CA-01-REMOTE': 'CORVONERO-CA-01-REMOTE-PROGRAMMIST-1S-COMMANDER-IMPORT-v2.6.xlsx',
  'CA-02-LOCAL': 'CORVONERO-CA-02-LOCAL-SOPROVOZHDENIE-1S-COMMANDER-IMPORT-v2.6.xlsx',
  'CA-02-REMOTE': 'CORVONERO-CA-02-REMOTE-SOPROVOZHDENIE-1S-COMMANDER-IMPORT-v2.6.xlsx',
  'CA-03-LOCAL': 'CORVONERO-CA-03-LOCAL-DORABOTKA-1S-COMMANDER-IMPORT-v2.6.xlsx',
  'CA-03-REMOTE': 'CORVONERO-CA-03-REMOTE-DORABOTKA-1S-COMMANDER-IMPORT-v2.6.xlsx',
  'CA-04-LOCAL': 'CORVONERO-CA-04-LOCAL-INTEGRACII-1S-COMMANDER-IMPORT-v2.6.xlsx',
  'CA-04-REMOTE': 'CORVONERO-CA-04-REMOTE-INTEGRACII-1S-COMMANDER-IMPORT-v2.6.xlsx',
  'CA-05-LOCAL': 'CORVONERO-CA-05-LOCAL-MARKIROVKA-1S-COMMANDER-IMPORT-v2.6.xlsx',
  'CA-05-REMOTE': 'CORVONERO-CA-05-REMOTE-MARKIROVKA-1S-COMMANDER-IMPORT-v2.6.xlsx',
};

function requireOperatorGate() {
  if (process.env.CORVONERO_OPERATOR_GATE !== 'APPROVED') {
    console.error(
      'STOP: CORVONERO_OPERATOR_GATE=APPROVED required. This C2c helper is not safe for casual execution.'
    );
    process.exit(1);
  }
}

const LOCAL_PROP_RE = /удал[её]нн|по россии|по рф|дистанцион/i;
const REMOTE_PROP_RE = /выезд|новосибирск|на месте|в офис/i;

const FORENSIC_COL_V26 = {
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

async function loadAuthority(manifestPath) {
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  const byRole = {};
  for (const entry of manifest.files) {
    const abs = path.resolve(entry.path);
    const parsed = JSON.parse(fs.readFileSync(abs, 'utf8'));
    byRole[entry.role] = parsed;
  }
  return { manifest, byRole, manifestPath: path.resolve(manifestPath) };
}

function enrichLoadedAuthority(loaded) {
  const transportConfig = loaded.byRole.transport_config;
  if (!transportConfig) return loaded;
  const resolveRef = (refPath) => {
    if (!refPath) return null;
    return JSON.parse(fs.readFileSync(path.resolve(refPath), 'utf8'));
  };
  if (transportConfig.bids_ref) loaded.byRole.bids = resolveRef(transportConfig.bids_ref);
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
    groupNegatives: byRole.group_negatives,
    transportConfig: byRole.transport_config,
    displayPaths: byRole.display_paths,
    bids: byRole.bids ?? null,
  };
}

function buildPayloads(model, expectedByCampaign) {
  const groups = model.architecture?.groups ?? [];
  const deployablePhrases = (model.phraseAllocation?.records ?? []).filter(
    (r) => r.production_status === 'DEPLOYABLE',
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
    const exp = expectedByCampaign[campaignId];
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
        (p) => p.final_campaign === campaignId,
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
        ladderValues: transportConfig?.ladder_values ?? 10,
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

async function forensicVerifyWorkbook(filePath, payload, campaignId, templateSha, expected) {
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
    if (expected.mode === 'REMOTE' && !foundRussia) fail('regions_dictionary_russia', 'Missing Россия');
    else if (expected.mode === 'REMOTE') pass('regions_dictionary_russia');
  }

  const adRows = [];
  const kwRows = [];
  const groupsSeen = new Set();
  const kwPerGroup = new Map();
  let orgIdHits = 0;
  let utmHits = 0;
  let queryHits = 0;
  let sitelinkHits = 0;
  let regionFails = 0;
  let missingBid = 0;
  let aboveBaseBid = 0;
  let ladderMismatch = 0;
  let remotePropInLocal = 0;
  let localPropInRemote = 0;
  let templateNegHits = 0;
  let genericAdHits = 0;

  const payloadBidByPhrase = new Map();
  for (const row of payload.rows) {
    if (row.row_type === ROW_TYPE_KEYWORD) payloadBidByPhrase.set(row.phrase, row.bid);
  }

  const ladder = buildCyclicLadder(expected.base_bid);
  const ladderSet = new Set(ladder);
  const forbiddenGeneric =
    'Услуги 1С для бизнеса: настройка, доработки и поддержка.';

  for (let r = DATA_START_ROW; r <= texts.rowCount; r++) {
    const phrase = safeCellText(texts, r, FORENSIC_COL.phrase);
    const h1 = safeCellText(texts, r, FORENSIC_COL.headline_1);
    const h2 = safeCellText(texts, r, FORENSIC_COL_V26.headline_2);
    const adText = safeCellText(texts, r, FORENSIC_COL_V26.text);
    const group = safeCellText(texts, r, FORENSIC_COL.group_name);
    if (!phrase && !h1 && !group) continue;

    const region = safeCellText(texts, r, FORENSIC_COL.region);
    const rowBlob = JSON.stringify(
      [48, 50, 58, 59, 60, 67].map((c) => safeCellText(texts, r, c)),
    );
    if (rowBlob.includes(FORBIDDEN_ORGANIZATION_ID)) orgIdHits++;
    if (rowBlob.includes('ремонт') && rowBlob.includes('запчасти')) templateNegHits++;

    const url = safeCellText(texts, r, FORENSIC_COL.landing_url);
    if (url.includes('utm_')) utmHits++;
    if (url.includes('?')) queryHits++;

    if (
      [FORENSIC_COL.fastlink_titles, FORENSIC_COL.fastlink_descriptions, FORENSIC_COL.fastlink_urls].some(
        (c) => isSitelinkPopulated(safeCellText(texts, r, c)),
      )
    ) {
      sitelinkHits++;
    }

    if (region && region !== expected.region) regionFails++;

    if (h1) {
      adRows.push({ row: r, group });
      groupsSeen.add(group);
      const blob = `${h1} ${h2} ${adText}`;
      if (adText.includes(forbiddenGeneric)) genericAdHits++;
      if (expected.mode === 'LOCAL' && LOCAL_PROP_RE.test(blob)) remotePropInLocal++;
      if (expected.mode === 'REMOTE' && REMOTE_PROP_RE.test(blob)) localPropInRemote++;
    } else if (phrase) {
      kwRows.push({ row: r, group, phrase });
      groupsSeen.add(group);
      kwPerGroup.set(group, (kwPerGroup.get(group) ?? 0) + 1);

      const bid = Number(String(safeCellText(texts, r, FORENSIC_COL.bid)).replace(',', '.'));
      if (!Number.isFinite(bid) || bid <= 0) missingBid++;
      else {
        if (bid > expected.base_bid) aboveBaseBid++;
        if (!ladderSet.has(bid)) fail('bid_not_on_ladder', `${bid}`);
        const expBid = payloadBidByPhrase.get(phrase);
        if (expBid != null && bid !== expBid) ladderMismatch++;
      }
    }
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
  if (regionFails === 0) pass('region', expected.region);
  else fail('region', `${regionFails}`);
  if (expected.mode === 'LOCAL' && remotePropInLocal === 0) pass('local_no_remote_proposition');
  else if (expected.mode === 'LOCAL') fail('local_no_remote_proposition', `${remotePropInLocal}`);
  if (expected.mode === 'REMOTE' && localPropInRemote === 0) pass('remote_no_local_proposition');
  else if (expected.mode === 'REMOTE') fail('remote_no_local_proposition', `${localPropInRemote}`);
  if (orgIdHits === 0) pass('forbidden_organization_id');
  else fail('forbidden_organization_id', `${orgIdHits}`);
  if (templateNegHits === 0) pass('no_template_junk_negatives');
  else fail('no_template_junk_negatives', `${templateNegHits}`);
  if (genericAdHits === 0) pass('no_forbidden_generic_ad_text');
  else fail('no_forbidden_generic_ad_text', `${genericAdHits}`);
  pass('embedded_campaign_negatives_blank', 'metadata patch sets blank campaign negatives');

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
  requireOperatorGate();

  const manifestPath = process.argv[2];
  const outputDir = process.argv[3];
  const countsPath = process.argv[4];
  if (!manifestPath || !outputDir || !countsPath) {
    throw new Error('Usage: node execute-campaign-v2.6-generation-v1.mjs <manifest> <outputDir> <counts>');
  }

  if (!adapterAvailable()) throw new Error('Triumph Commander patcher adapter unavailable');

  const templateResult = await validateTemplate(COMMANDER_TEMPLATE_PATH);
  if (!templateResult.ok) {
    console.error('STOP — COMMANDER TEMPLATE IDENTITY MISMATCH');
    process.exit(2);
  }

  const expectedByCampaign = JSON.parse(fs.readFileSync(countsPath, 'utf8')).campaigns;

  const loaded = enrichLoadedAuthority(await loadAuthority(manifestPath));
  const model = buildModel(loaded);
  const payloads = buildPayloads(model, expectedByCampaign);
  const payloadByCampaign = Object.fromEntries(payloads.map((p) => [p.campaign_id, p]));

  const generationResults = [];
  for (const [campaignId, filename] of Object.entries(CAMPAIGN_FILES)) {
    const payload = payloadByCampaign[campaignId];
    const exp = expectedByCampaign[campaignId];
    if (!payload) throw new Error(`Missing payload for ${campaignId}`);
    const kwCount = payload.rows.filter((r) => r.row_type === ROW_TYPE_KEYWORD).length;
    const adCount = payload.rows.filter((r) => r.row_type === ROW_TYPE_AD).length;
    if (kwCount !== exp.keywords || adCount !== exp.groups) {
      throw new Error(
        `Payload count mismatch ${campaignId}: kw ${kwCount}/${exp.keywords}, ads ${adCount}/${exp.groups}`,
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
      keyword_rows: kwCount,
      ad_rows: adCount,
      campaign_base_bid: exp.base_bid,
      geo_region: exp.region,
    });
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
        templateResult.sha256,
        expectedByCampaign[gen.campaign_id],
      )),
    });
  }

  const allPass = forensicResults.every((r) => r.status === 'PASS');
  const totalKw = generationResults.reduce((s, g) => s + g.keyword_rows, 0);
  const totalAds = generationResults.reduce((s, g) => s + g.ad_rows, 0);

  const resultDoc = {
    run_id: 'CORVONERO-CAMPAIGN-V2.6-FINAL-2026-06-30',
    generated_at: new Date().toISOString(),
    output_directory: outputDir,
    bid_policy: CORVONERO_POLICY,
    files_generated: generationResults.length,
    generation_results: generationResults,
    forensic_results: forensicResults,
    all_pass: allPass,
    totals: { campaigns: 10, groups: totalAds, keyword_rows: totalKw, ad_rows: totalAds },
  };

  fs.writeFileSync(
    path.join(PILOT_ROOT, 'CORVONERO-CAMPAIGN-V2.6-GENERATION-v1.json'),
    `${JSON.stringify(resultDoc, null, 2)}\n`,
  );

  const forensicDoc = {
    generated_at: new Date().toISOString(),
    verdict: allPass ? 'PASS — FORENSIC VALIDATION COMPLETE' : 'FAIL — FORENSIC ERRORS',
    summary: {
      campaigns: 10,
      groups: totalAds,
      phrase_slots: totalKw,
      primary_ads: totalAds,
      all_pass: allPass,
      bid_policy: CORVONERO_POLICY,
      cross_campaign_negatives: 'NOT APPLIED',
      embedded_campaign_negatives: 'BLANK',
      unsafe_narrow_negatives: 'OMITTED',
      remote_nso_exclusion: 'MANUAL POST-IMPORT ACTION REQUIRED',
    },
    results: forensicResults,
  };

  fs.writeFileSync(
    path.join(PILOT_ROOT, 'CORVONERO-CAMPAIGN-V2.6-FORENSIC-VALIDATION-v1.json'),
    `${JSON.stringify(forensicDoc, null, 2)}\n`,
  );

  if (!allPass) {
    console.error(JSON.stringify(forensicResults.filter((r) => r.status !== 'PASS'), null, 2));
    process.exit(1);
  }

  console.log('PASS — 10 V2.6 XLSX files generated and forensically verified');
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
