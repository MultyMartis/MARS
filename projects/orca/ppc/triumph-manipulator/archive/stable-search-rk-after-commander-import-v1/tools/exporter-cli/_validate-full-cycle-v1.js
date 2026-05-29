#!/usr/bin/env node
"use strict";

const path = require("path");
const { readZipEntryUtf8, verifyPreservedEntries } = require("./xlsx-zip-patch");

const OUTPUT = path.join(__dirname, "output", "triumph-sheet1-patch-full-cycle-v1.xlsx");
const TEMPLATE = path.resolve(
  __dirname,
  "../../assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx"
);

const DATA_START_ROW = 16;
const EXPORT_ROW_COUNT = 82;
const LAST_EXPORT_ROW = DATA_START_ROW + EXPORT_ROW_COUNT - 1;
const GEO_COL = 52;
const AD_TYPE_COL = 2;
const DISPLAY_URL_COL = 49;
const EXPECTED_REGION = "Краснодарский край";
const EXPECTED_AD_TYPE = "Текстово-графическое";

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
  if (!m) return null;
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

function main() {
  const failures = [];
  const passes = [];

  const preserve = verifyPreservedEntries(TEMPLATE, OUTPUT);
  if (preserve.sharedStringsIntroduced) failures.push("sharedStrings introduced");
  else passes.push("no sharedStrings");

  for (const e of preserve.preservedEntries) {
    if (e.match) passes.push(`${e.entry} byte-identical`);
    else failures.push(`${e.entry} mismatch`);
  }

  const sheet1 = readZipEntryUtf8(OUTPUT, "xl/worksheets/sheet1.xml");
  const geoRef = colToLetter(GEO_COL);

  for (let r = DATA_START_ROW; r <= LAST_EXPORT_ROW; r++) {
    const rowXml = extractRowXml(sheet1, r);
    if (!rowXml) {
      failures.push(`row ${r} missing`);
      continue;
    }
    const geo = cellValue(rowXml, `${geoRef}${r}`);
    if (geo !== EXPECTED_REGION) failures.push(`row ${r} geo=${JSON.stringify(geo)}`);
    const adType = cellValue(rowXml, `${colToLetter(AD_TYPE_COL)}${r}`);
    if (adType !== EXPECTED_AD_TYPE) failures.push(`row ${r} adType=${JSON.stringify(adType)}`);
    const display = cellValue(rowXml, `${colToLetter(DISPLAY_URL_COL)}${r}`);
    if (display && /manipulator-triumph\.ru/i.test(display)) {
      failures.push(`row ${r} display has domain`);
    }
    if (/<v>https?:\/\/direct\.yandex\.ru\/images/i.test(rowXml)) {
      failures.push(`row ${r} image URL`);
    }
  }

  if (!failures.some((f) => f.startsWith("row") && f.includes("geo"))) {
    passes.push(`rows ${DATA_START_ROW}-${LAST_EXPORT_ROW} geo=${EXPECTED_REGION}`);
  }

  const tail = listRowNumbers(sheet1).filter((n) => n > LAST_EXPORT_ROW);
  if (tail.length) failures.push(`stale rows after ${LAST_EXPORT_ROW}: ${tail.join(", ")}`);
  else passes.push(`no rows after ${LAST_EXPORT_ROW}`);

  console.log("\n--- Full cycle v1 export validation ---");
  passes.forEach((p) => console.log(`PASS: ${p}`));
  failures.forEach((f) => console.log(`FAIL: ${f}`));
  process.exit(failures.length ? 1 : 0);
}

main();
