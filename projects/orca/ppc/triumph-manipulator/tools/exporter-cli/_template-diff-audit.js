#!/usr/bin/env node
"use strict";

/**
 * Template vs export diff audit — Phase 1 reverse engineering helper.
 * Human-operated — NOT import automation.
 */

const fs = require("fs");
const path = require("path");
const ExcelJS = require("exceljs");
const { readZipEntryUtf8 } = require("./xlsx-zip-patch");

const TEMPLATE = path.resolve(
  __dirname,
  "../../assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx"
);
const DEFAULT_EXPORT = path.join(
  __dirname,
  "output",
  "triumph-sheet1-patch-launch-ready-v1.3.xlsx"
);

const DATA_START = 16;
const META_ROWS = [6, 7, 8, 9, 10, 11, 12, 13];
const GROUP_COLS = [1, 2, 3, 5, 6, 52, 53, 54, 55, 68, 69];

function colLetter(col) {
  let n = col;
  let s = "";
  while (n > 0) {
    const rem = (n - 1) % 26;
    s = String.fromCharCode(65 + rem) + s;
    n = Math.floor((n - 1) / 26);
  }
  return s;
}

async function readSheetCells(filePath) {
  const wb = new ExcelJS.Workbook();
  await wb.xlsx.readFile(filePath);
  const ws = wb.getWorksheet("Тексты");
  const cells = new Map();
  const get = (r, c) => {
    const key = `${r}:${c}`;
    if (!cells.has(key)) {
      cells.set(key, String(ws.getRow(r).getCell(c).value ?? "").trim());
    }
    return cells.get(key);
  };
  return { get, ws };
}

function hasInvalidNegativeSyntax(text) {
  if (!text) return false;
  return /[*?[\]{}|\\^$]/.test(text);
}

async function main() {
  const exportPath = path.resolve(process.argv[2] || DEFAULT_EXPORT);
  if (!fs.existsSync(TEMPLATE)) {
    console.error("Template not found:", TEMPLATE);
    process.exit(1);
  }
  if (!fs.existsSync(exportPath)) {
    console.error("Export not found:", exportPath);
    process.exit(1);
  }

  const tpl = await readSheetCells(TEMPLATE);
  const exp = await readSheetCells(exportPath);

  console.log("\n=== METADATA DIFF (rows 6-13) ===");
  const metaDiffs = [];
  for (const r of META_ROWS) {
    for (let c = 1; c <= 12; c++) {
      const tv = tpl.get(r, c);
      const ev = exp.get(r, c);
      if (tv !== ev) {
        metaDiffs.push({ row: r, col: c, ref: colLetter(c) + r, template: tv, export: ev });
        console.log(`${colLetter(c)}${r}: T=${JSON.stringify(tv)} | E=${JSON.stringify(ev)}`);
      }
    }
  }
  if (!metaDiffs.length) console.log("(no metadata diffs in cols 1-12)");

  console.log("\n=== GROUP SETTINGS — first ad row per group ===");
  for (let gnum = 1; gnum <= 12; gnum++) {
    for (let r = DATA_START; r <= 120; r++) {
      const num = exp.get(r, 6);
      const h1 = exp.get(r, 10);
      if (num !== String(gnum) || !h1) continue;
      const diffs = [];
      for (const c of GROUP_COLS) {
        const tv = tpl.get(r, c);
        const ev = exp.get(r, c);
        if (tv !== ev) {
          diffs.push({ col: c, template: tv.slice(0, 80), export: ev.slice(0, 80) });
        }
      }
      console.log(
        `G${gnum} R${r} ${exp.get(r, 5).slice(0, 40)}: ${diffs.length} col diffs`
      );
      diffs.forEach((d) =>
        console.log(`  C${d.col}: T=${JSON.stringify(d.template)} E=${JSON.stringify(d.export)}`)
      );
      break;
    }
  }

  console.log("\n=== INVALID NEGATIVE SYNTAX (export col 68) ===");
  let invalidGroups = 0;
  const seen = new Set();
  for (let r = DATA_START; r <= 120; r++) {
    const gn = exp.get(r, 5);
    const h1 = exp.get(r, 10);
    const neg = exp.get(r, 68);
    if (!gn || !h1 || seen.has(gn)) continue;
    seen.add(gn);
    if (hasInvalidNegativeSyntax(neg)) {
      invalidGroups++;
      const stars = (neg.match(/\*/g) || []).length;
      console.log(`${gn}: * count=${stars}, len=${neg.length}`);
    }
  }
  console.log(`Groups with invalid syntax: ${invalidGroups}/${seen.size}`);

  console.log("\n=== ROW MODEL ===");
  let tplAds = 0,
    tplKw = 0,
    expAds = 0,
    expKw = 0;
  for (let r = DATA_START; r <= 120; r++) {
    if (tpl.get(r, 10)) tplAds++;
    if (tpl.get(r, 8)) tplKw++;
    if (exp.get(r, 10)) expAds++;
    if (exp.get(r, 8)) expKw++;
  }
  console.log(`Template: ad_rows=${tplAds} kw_rows=${tplKw}`);
  console.log(`Export:   ad_rows=${expAds} kw_rows=${expKw}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
