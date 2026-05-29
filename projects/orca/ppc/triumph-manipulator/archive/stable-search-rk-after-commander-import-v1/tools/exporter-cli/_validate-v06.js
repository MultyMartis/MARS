#!/usr/bin/env node
"use strict";

/**
 * Post-export validation for region fix v0.6.
 * Reads sheet1.xml from ZIP — NOT full workbook rewrite.
 */

const path = require("path");
const { readZipEntryUtf8, verifyPreservedEntries } = require("./xlsx-zip-patch");

const OUTPUT = path.join(__dirname, "output", "triumph-sheet1-patch-region-v0.6.xlsx");
const TEMPLATE = path.resolve(
  __dirname,
  "../../assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx"
);

const DATA_START_ROW = 16;
const EXPORT_ROW_COUNT = 15;
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

  if (!require("fs").existsSync(OUTPUT)) {
    console.error(`FAIL: output missing: ${OUTPUT}`);
    process.exit(1);
  }

  const preserve = verifyPreservedEntries(TEMPLATE, OUTPUT);
  if (preserve.sharedStringsIntroduced) {
    failures.push("sharedStrings.xml introduced");
  } else {
    passes.push("no sharedStrings");
  }

  for (const e of preserve.preservedEntries) {
    if (e.match) passes.push(`${e.entry} byte-identical`);
    else failures.push(`${e.entry} mismatch (${e.templateBytes} vs ${e.patchedBytes})`);
  }

  const sheet1 = readZipEntryUtf8(OUTPUT, "xl/worksheets/sheet1.xml");

  if (/<t>Все<\/t>/i.test(sheet1)) {
    failures.push('sheet1 contains <t>Все</t>');
  } else {
    passes.push('no <t>Все</t> in sheet1');
  }

  const geoRef = `${colToLetter(GEO_COL)}`;
  for (let r = DATA_START_ROW; r <= LAST_EXPORT_ROW; r++) {
    const rowXml = extractRowXml(sheet1, r);
    if (!rowXml) {
      failures.push(`row ${r} missing`);
      continue;
    }
    const ref = `${geoRef}${r}`;
    const val = cellValue(rowXml, ref);
    if (val === null || val === "") {
      failures.push(`row ${r} col ${GEO_COL} empty`);
    } else if (val.includes("\n")) {
      failures.push(`row ${r} col ${GEO_COL} multi-line: ${JSON.stringify(val)}`);
    } else if (val === "Все") {
      failures.push(`row ${r} col ${GEO_COL} = Все`);
    } else if (val !== EXPECTED_REGION) {
      failures.push(`row ${r} col ${GEO_COL} = ${JSON.stringify(val)}`);
    }
    const adType = cellValue(rowXml, `${colToLetter(AD_TYPE_COL)}${r}`);
    if (adType !== EXPECTED_AD_TYPE) {
      failures.push(`row ${r} ad type = ${JSON.stringify(adType)}`);
    }
    const display = cellValue(rowXml, `${colToLetter(DISPLAY_URL_COL)}${r}`);
    if (display && /manipulator-triumph\.ru/i.test(display)) {
      failures.push(`row ${r} display URL has domain composite`);
    }
    if (/<v>https?:\/\/direct\.yandex\.ru\/images/i.test(rowXml)) {
      failures.push(`row ${r} has image URL in sheet1`);
    }
  }
  if (!failures.some((f) => f.startsWith("row ") && f.includes("col 52"))) {
    passes.push(`rows ${DATA_START_ROW}–${LAST_EXPORT_ROW} col ${GEO_COL} = ${EXPECTED_REGION}`);
  }

  const rows = listRowNumbers(sheet1);
  const maxRow = Math.max(...rows);
  const tail = rows.filter((n) => n > LAST_EXPORT_ROW);
  if (tail.length) {
    failures.push(`stale rows remain after ${LAST_EXPORT_ROW}: ${tail.join(", ")}`);
  } else {
    passes.push(`no rows after ${LAST_EXPORT_ROW} (max row ${maxRow})`);
  }

  console.log("\n--- Region fix v0.6 validation ---");
  for (const p of passes) console.log(`PASS: ${p}`);
  for (const f of failures) console.log(`FAIL: ${f}`);

  if (failures.length) {
    console.log(`\n${failures.length} failure(s)`);
    process.exit(1);
  }
  console.log("\nAll checks passed.");
}

main();
