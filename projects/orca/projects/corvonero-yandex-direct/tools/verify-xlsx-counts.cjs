#!/usr/bin/env node
'use strict';
const { readZipEntryUtf8 } = require(require('path').resolve(
  __dirname,
  '../../../ppc/triumph-manipulator/tools/exporter-cli/xlsx-zip-patch'
));
const XLSX = require('path').resolve(__dirname, '../exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v2.xlsx');
const sheet = readZipEntryUtf8(XLSX, 'xl/worksheets/sheet1.xml');
const DATA_START = 16;
function colToLetter(col) {
  let n = col;
  let s = '';
  while (n > 0) {
    s = String.fromCharCode(65 + ((n - 1) % 26)) + s;
    n = Math.floor((n - 1) / 26);
  }
  return s;
}
function rowXml(sheet, rowNum) {
  const re = new RegExp(`<row r="${rowNum}"[^>]*>[\\s\\S]*?</row>`);
  const m = sheet.match(re);
  return m ? m[0] : null;
}
function getCell(sheet, row, col) {
  const rx = rowXml(sheet, row);
  if (!rx) return '';
  const ref = `${colToLetter(col)}${row}`;
  const re = new RegExp(`<c\\s+r="${ref}"[^>]*>[\\s\\S]*?<v>([\\s\\S]*?)</v>`, 'i');
  const m = rx.match(re);
  return m ? m[1].replace(/&amp;/g, '&') : '';
}
const rows = [...sheet.matchAll(/<row r="(\d+)"/g)].map((m) => parseInt(m[1], 10)).filter((r) => r >= DATA_START);
const groups = new Set();
let ads = 0;
let kw = 0;
let missingMarker = 0;
for (const r of rows) {
  const gn = getCell(sheet, r, 5);
  const ph = getCell(sheet, r, 8);
  const h1 = getCell(sheet, r, 10);
  if (gn) {
    groups.add(gn);
    if (!/^\[C0[1-8]\]/.test(gn)) missingMarker++;
  }
  if (h1) ads++;
  if (ph) kw++;
}
console.log(JSON.stringify({ data_rows: rows.length, groups: groups.size, missing_marker: missingMarker, ads, kw, samples: [...groups].slice(0, 4) }, null, 2));
