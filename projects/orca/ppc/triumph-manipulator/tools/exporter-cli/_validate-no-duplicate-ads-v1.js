#!/usr/bin/env node
"use strict";

/**
 * Post-export QA — Commander transport split v1.2 (no duplicate ads by keyword).
 * Human-operated gate — NOT Commander import automation.
 */

const fs = require("fs");
const path = require("path");
const { readZipEntryUtf8, verifyPreservedEntries } = require("./xlsx-zip-patch");
const { runIntegrityCheck } = require("./xlsx-integrity-check");
const { loadHeaderMap } = require("./workbook-writer");
const {
  PRODUCTION_LANDING_SLUGS,
  PRODUCTION_DISPLAY_DOMAIN,
  SEARCH_ONLY_AD_TYPE_TRANSPORT,
  TRIUMPH_GEO_REGION_TRANSPORT,
} = require("./mapping");

const DEFAULT_OUTPUT = path.join(
  __dirname,
  "output",
  "triumph-sheet1-patch-full-cycle-v1.2.xlsx"
);
const TEMPLATE = path.resolve(
  __dirname,
  "../../assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx"
);
const DATA_START_ROW = 16;

const COL = {
  groupAdditional: 1,
  adType: 2,
  groupName: 5,
  phrase: 8,
  headline1: 10,
  headline2: 11,
  description: 12,
  landingUrl: 48,
  displayUrl: 49,
  geo: 52,
  fastlinkUrls: 60,
};

const LEGACY_DOMAIN_RE = /gruzotaxi-triumph\.ru/i;
const IMAGE_URL_RE = /https?:\/\/direct\.yandex\.ru\/images/i;

function colToLetter(col) {
  let n = col;
  let s = "";
  while (n > 0) {
    const rem = (n - 1) % 26;
    s = String.fromCharCode(65 + rem) + s;
    n = Math.floor((n - 1) / 26);
  }
  return s;
}

function cellValue(rowXml, ref) {
  const re = new RegExp(
    `<c\\s+r="${ref}"[^>]*>[\\s\\S]*?<v>([\\s\\S]*?)</v>`,
    "i"
  );
  const m = rowXml.match(re);
  if (!m) return "";
  return m[1]
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&apos;/g, "'");
}

function extractRowXml(sheetXml, rowNum) {
  const re = new RegExp(`<row r="${rowNum}"[^>]*>[\\s\\S]*?</row>`);
  const m = sheetXml.match(re);
  return m ? m[0] : null;
}

function listRowNumbers(sheetXml) {
  const rows = [];
  const re = /<row r="(\d+)"/g;
  let m;
  while ((m = re.exec(sheetXml)) !== null) {
    rows.push(parseInt(m[1], 10));
  }
  return rows.sort((a, b) => a - b);
}

function isCanonicalLandingUrl(url) {
  const u = String(url || "").trim();
  if (!u) return true;
  if (LEGACY_DOMAIN_RE.test(u)) return false;
  if (!/^https:\/\/manipulator-triumph\.ru(\/|$)/i.test(u)) return false;
  if (/^https:\/\/manipulator-triumph\.ru\/?$/i.test(u)) return true;
  if (!/\.html$/i.test(u)) return false;
  try {
    const slug = u.split("/").filter(Boolean).pop() || "";
    return PRODUCTION_LANDING_SLUGS.includes(slug);
  } catch {
    return false;
  }
}

function parseFastlinkUrls(cell) {
  if (!cell) return [];
  return String(cell)
    .split("||")
    .map((s) => s.trim())
    .filter(Boolean);
}

function readExportedRows(sheetXml, lastRow) {
  const rows = [];
  for (let r = DATA_START_ROW; r <= lastRow; r++) {
    const rowXml = extractRowXml(sheetXml, r);
    if (!rowXml) continue;
    const ref = (col) => cellValue(rowXml, `${colToLetter(col)}${r}`);
    rows.push({
      rowNum: r,
      groupName: ref(COL.groupName),
      phrase: ref(COL.phrase),
      headline1: ref(COL.headline1),
      headline2: ref(COL.headline2),
      description: ref(COL.description),
      landingUrl: ref(COL.landingUrl),
      displayUrl: ref(COL.displayUrl),
      geo: ref(COL.geo),
      adType: ref(COL.adType),
      fastlinkUrls: ref(COL.fastlinkUrls),
      rowXml,
    });
  }
  return rows;
}

async function main() {
  const outputPath = path.resolve(process.argv[2] || DEFAULT_OUTPUT);
  const failures = [];
  const passes = [];

  if (!fs.existsSync(outputPath)) {
    console.error(`FAIL: output not found: ${outputPath}`);
    process.exit(1);
  }

  const preserve = verifyPreservedEntries(TEMPLATE, outputPath);
  if (preserve.sharedStringsIntroduced) failures.push("sharedStrings introduced");
  else passes.push("no sharedStrings");

  for (const e of preserve.preservedEntries) {
    if (e.match) passes.push(`${e.entry} byte-identical`);
    else failures.push(`${e.entry} mismatch`);
  }

  const sheet1 = readZipEntryUtf8(outputPath, "xl/worksheets/sheet1.xml");
  const allRows = listRowNumbers(sheet1);
  const dataRows = allRows.filter((n) => n >= DATA_START_ROW);
  const lastExportRow = Math.max(...dataRows);
  const exported = readExportedRows(sheet1, lastExportRow);
  const exportRowCount = exported.length;

  const groups = new Set(exported.map((r) => r.groupName).filter(Boolean));
  const adRows = exported.filter((r) => r.headline1 && r.headline1.trim());
  const keywordRows = exported.filter((r) => r.phrase && r.phrase.trim());

  if (groups.size === 12) passes.push(`groups=${groups.size}`);
  else failures.push(`groups=${groups.size} (expected 12)`);

  if (adRows.length === 20) passes.push(`ad_rows=${adRows.length}`);
  else failures.push(`ad_rows=${adRows.length} (expected 20)`);

  if (keywordRows.length === 64) passes.push(`keyword_rows=${keywordRows.length}`);
  else failures.push(`keyword_rows=${keywordRows.length} (expected 64)`);

  if (exportRowCount === 84) passes.push(`total_export_rows=${exportRowCount}`);
  else failures.push(`total_export_rows=${exportRowCount} (expected 84)`);

  const adSignatures = new Map();
  let duplicateAdCount = 0;
  for (const row of adRows) {
    const sig = `${row.groupName}\0${row.headline1}\0${row.headline2}\0${row.description}\0${row.landingUrl}`;
    if (adSignatures.has(sig)) duplicateAdCount++;
    else adSignatures.set(sig, row.rowNum);
  }
  if (duplicateAdCount === 0) passes.push("duplicate_ad_signatures=0");
  else failures.push(`duplicate_ad_signatures=${duplicateAdCount}`);

  for (const row of keywordRows) {
    if (row.headline1 || row.headline2 || row.description || row.landingUrl) {
      failures.push(`keyword row ${row.rowNum} has ad-level text`);
    }
  }
  if (!failures.some((f) => f.startsWith("keyword row"))) {
    passes.push("keyword rows have no ad text");
  }

  for (const row of adRows) {
    if (row.phrase) failures.push(`ad row ${row.rowNum} has phrase column set`);
  }
  if (!failures.some((f) => f.startsWith("ad row") && f.includes("phrase"))) {
    passes.push("ad rows have empty phrase column");
  }

  let legacyUrlCount = 0;
  let nonCanonicalLanding = 0;
  let nonCanonicalFastlink = 0;
  let imageUrlRows = 0;
  let badGeo = 0;
  let badAdType = 0;
  let displayDomain = 0;

  for (const row of exported) {
    if (LEGACY_DOMAIN_RE.test(row.rowXml)) legacyUrlCount++;
    if (IMAGE_URL_RE.test(row.rowXml)) imageUrlRows++;

    if (row.geo !== TRIUMPH_GEO_REGION_TRANSPORT) badGeo++;

    if (row.headline1) {
      if (row.adType !== SEARCH_ONLY_AD_TYPE_TRANSPORT) badAdType++;
      if (row.landingUrl && !isCanonicalLandingUrl(row.landingUrl)) nonCanonicalLanding++;
      if (row.displayUrl && /manipulator-triumph\.ru/i.test(row.displayUrl)) {
        displayDomain++;
      }
      for (const flUrl of parseFastlinkUrls(row.fastlinkUrls)) {
        if (LEGACY_DOMAIN_RE.test(flUrl)) legacyUrlCount++;
        if (!isCanonicalLandingUrl(flUrl)) nonCanonicalFastlink++;
      }
    }
  }

  if (legacyUrlCount === 0) passes.push("legacy_url=0");
  else failures.push(`legacy_url_hits=${legacyUrlCount}`);

  if (nonCanonicalLanding === 0) passes.push("landing_urls_canonical");
  else failures.push(`non_canonical_landing=${nonCanonicalLanding}`);

  if (nonCanonicalFastlink === 0) passes.push("fastlink_urls_canonical");
  else failures.push(`non_canonical_fastlinks=${nonCanonicalFastlink}`);

  if (imageUrlRows === 0) passes.push("no_image_urls");
  else failures.push(`image_url_rows=${imageUrlRows}`);

  if (badGeo === 0) passes.push(`region=${TRIUMPH_GEO_REGION_TRANSPORT}`);
  else failures.push(`bad_geo_rows=${badGeo}`);

  if (badAdType === 0) passes.push(`ad_type=${SEARCH_ONLY_AD_TYPE_TRANSPORT} on ad rows`);
  else failures.push(`bad_ad_type_rows=${badAdType}`);

  if (displayDomain === 0) passes.push("display_path_no_domain");
  else failures.push(`display_domain_in_path=${displayDomain}`);

  const tail = allRows.filter((n) => n > lastExportRow);
  if (tail.length) failures.push(`stale rows after ${lastExportRow}: ${tail.slice(0, 5).join(", ")}…`);
  else passes.push(`no rows after ${lastExportRow}`);

  const headerMap = loadHeaderMap();
  const columns = {};
  for (const [key, spec] of Object.entries(headerMap || {})) {
    if (spec.status === "verified" && spec.column) columns[key] = spec.column;
  }
  const allowed = new Set(Object.values(columns));

  const integrity = await runIntegrityCheck(outputPath, {
    sheetName: "Тексты",
    dataStartRow: DATA_START_ROW,
    rowsWritten: exportRowCount,
    mappedColumns: allowed,
    columnsByKey: columns,
    probeLogicalKeys: ["groups.group_name", "keywords.phrase", "ads.headline_1"],
    probeLogicalKeysMode: "any-row",
  });

  if (integrity.ok) passes.push(`integrity: ${integrity.code}`);
  else failures.push(`integrity: ${integrity.message}`);

  console.log("\n--- No-duplicate-ads transport QA v1.2 ---");
  console.log(`File: ${outputPath}`);
  passes.forEach((p) => console.log(`PASS: ${p}`));
  failures.forEach((f) => console.log(`FAIL: ${f}`));

  const ready =
    failures.length === 0 &&
    groups.size === 12 &&
    adRows.length === 20 &&
    keywordRows.length === 64 &&
    duplicateAdCount === 0;

  console.log(`\nCommander readiness (transport QA only): ${ready ? "READY" : "NOT READY"}`);
  console.log(
    "NOT Commander import proof · Human import test still required · SAFE UNKNOWN until operator confirms."
  );

  process.exit(failures.length ? 1 : 0);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
