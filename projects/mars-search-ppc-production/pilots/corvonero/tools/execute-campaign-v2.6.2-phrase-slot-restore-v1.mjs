#!/usr/bin/env node
// C2c HOLD: source hardening only.
// This file is not authorized for execution without explicit operator approval.
// Commit/persistence does not authorize Commander import, Direct launch, account mutation,
// advertising start, Storage export generation, repo artifact generation,
// Localhost mutation, Storage mutation, Yandex/API access, or client-facing delivery.
// Commander/XLSX generation is transport/import-candidate tooling only and does not authorize
// import into Yandex Direct or any live account mutation.
/**
 * CORVONERO V2.6.2 — restore 2 missing phrase slots from V2.6.1 package.
 * Root cause: build_phrase_allocation omitted merged group ca-02-troubleshooting-not-working → ca-02-support-tech.
 * Semantic authority V2.6 unchanged. Only deployable keyword rows restored.
 */
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import { DATA_START_ROW, FORENSIC_COL } from '../../../tools/commander-transport/src/workbook-forensic-verifier.mjs';
import { sanitizationCellValue as cellText } from '../../../tools/commander-transport/src/template-sanitizer.mjs';
import { assignBidsForGroup, resolveBidPolicy } from '../../../tools/commander-transport/src/bid-ladder.mjs';

const require = createRequire(import.meta.url);
const ExcelJS = require('../../../tools/commander-transport/node_modules/exceljs');

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PILOT = path.resolve(__dirname, '..');
const V261 = path.resolve('X:/AI MARS STORAGE/exports/corvonero/CORVONERO-CAMPAIGN-V2.6.1-FINAL-2026-06-30');
const V262 = path.resolve('X:/AI MARS STORAGE/exports/corvonero/CORVONERO-CAMPAIGN-V2.6.2-FINAL-2026-06-30');
const GENERATED_AT = new Date().toISOString();

const RESTORE_SLOTS = [
  {
    campaign_id: 'CA-02-LOCAL',
    source_v261: 'CORVONERO-CA-02-LOCAL-SOPROVOZHDENIE-1S-COMMANDER-IMPORT-v2.6.1.xlsx',
    target: 'CORVONERO-CA-02-LOCAL-SOPROVOZHDENIE-1S-COMMANDER-IMPORT-v2.6.2.xlsx',
    group_name: 'Сопровождение 1С — техподдержка и администрирование',
    group_id: 'ca-02-support-tech',
    phrase: 'программа 1с не работает',
    phrase_id: 'PHR-0447',
  },
  {
    campaign_id: 'CA-02-REMOTE',
    source_v261: 'CORVONERO-CA-02-REMOTE-SOPROVOZHDENIE-1S-COMMANDER-IMPORT-v2.6.1.xlsx',
    target: 'CORVONERO-CA-02-REMOTE-SOPROVOZHDENIE-1S-COMMANDER-IMPORT-v2.6.2.xlsx',
    group_name: 'Сопровождение 1С — техподдержка и администрирование',
    group_id: 'ca-02-support-tech',
    phrase: 'программа 1с не работает',
    phrase_id: 'PHR-0447',
  },
];

function requireOperatorGate() {
  if (process.env.CORVONERO_OPERATOR_GATE !== 'APPROVED') {
    console.error(
      'STOP: CORVONERO_OPERATOR_GATE=APPROVED required. This C2c helper is not safe for casual execution.'
    );
    process.exit(1);
  }
}

function sha256File(fp) {
  return crypto.createHash('sha256').update(fs.readFileSync(fp)).digest('hex');
}

function copyPackageTree() {
  if (fs.existsSync(V262)) {
    console.log('V2.6.2 output directory already exists — reusing for idempotent patch');
    return;
  }
  fs.mkdirSync(V262, { recursive: true });
  for (const ent of fs.readdirSync(V261)) {
    const src = path.join(V261, ent);
    const dstName = ent.replace(/v2\.6\.1/gi, 'v2.6.2').replace(/V2\.6\.1/g, 'V2.6.2');
    fs.copyFileSync(src, path.join(V262, dstName));
  }
}

function renameXlsxFromV261() {
  for (const ent of fs.readdirSync(V261)) {
    if (!ent.toLowerCase().endsWith('.xlsx')) continue;
    const target = ent.replace(/v2\.6\.1/i, 'v2.6.2');
    const src = path.join(V261, ent);
    const dst = path.join(V262, target);
    if (!fs.existsSync(dst)) fs.copyFileSync(src, dst);
  }
}

async function insertMissingKeywordRow(filePath, slot, bids, transportConfig) {
  const wb = new ExcelJS.Workbook();
  await wb.xlsx.readFile(filePath);
  const texts = wb.getWorksheet('Тексты');
  let templateRowNum = null;

  for (let r = DATA_START_ROW; r <= texts.rowCount; r++) {
    const groupName = cellText(texts, r, FORENSIC_COL.group_name);
    const phrase = cellText(texts, r, FORENSIC_COL.phrase);
    if (groupName === slot.group_name && phrase) {
      if (normalize(phrase) === normalize(slot.phrase)) return;
      templateRowNum = r;
    }
  }
  if (templateRowNum == null) {
    throw new Error(`No template keyword row in group ${slot.group_name} for ${filePath}`);
  }

  const templateRow = texts.getRow(templateRowNum);
  const insertAt = templateRowNum + 1;
  const newRow = texts.insertRow(insertAt, []);
  templateRow.eachCell({ includeEmpty: true }, (cell, colNumber) => {
    newRow.getCell(colNumber).value = cell.value;
    if (cell.style) newRow.getCell(colNumber).style = { ...cell.style };
  });

  const bidPolicy = resolveBidPolicy(transportConfig);
  const bidMap = assignBidsForGroup(
    [{ phrase: slot.phrase, phrase_id: slot.phrase_id }],
    bids[slot.campaign_id],
    { policy: bidPolicy, bidStep: transportConfig?.bid_step ?? 10, ladderValues: transportConfig?.ladder_values ?? 10 },
  );
  newRow.getCell(FORENSIC_COL.phrase).value = slot.phrase;
  newRow.getCell(FORENSIC_COL.bid).value = bidMap.get(slot.phrase_id) ?? bids[slot.campaign_id];

  await wb.xlsx.writeFile(filePath);
}

function normalize(s) {
  return String(s ?? '').toLowerCase().trim().replace(/\s+/g, ' ');
}

async function main() {
  requireOperatorGate();
  if (!fs.existsSync(V261)) throw new Error(`V2.6.1 package missing: ${V261}`);

  if (fs.existsSync(V262)) {
    for (const slot of RESTORE_SLOTS) {
      const dst = path.join(V262, slot.target);
      fs.copyFileSync(path.join(V261, slot.source_v261), dst);
    }
    for (const ent of fs.readdirSync(V261)) {
      if (!ent.toLowerCase().endsWith('.xlsx')) continue;
      const target = ent.replace(/v2\.6\.1/i, 'v2.6.2');
      const dst = path.join(V262, target);
      if (!fs.existsSync(dst)) {
        fs.copyFileSync(path.join(V261, ent), dst);
      }
    }
  } else {
    copyPackageTree();
    renameXlsxFromV261();
  }

  const transportConfig = JSON.parse(
    fs.readFileSync(path.join(PILOT, 'CORVONERO-CAMPAIGN-V2.6-TRANSPORT-CONFIG-v1.json'), 'utf8'),
  );
  const bids = JSON.parse(
    fs.readFileSync(path.join(PILOT, 'CORVONERO-CAMPAIGN-V2.1-BIDS-v1.json'), 'utf8'),
  ).campaign_bids;

  const patched = [];
  for (const slot of RESTORE_SLOTS) {
    const fp = path.join(V262, slot.target);
    if (!fs.existsSync(fp)) {
      fs.copyFileSync(path.join(V261, slot.source_v261), fp);
    }
    await insertMissingKeywordRow(fp, slot, bids, transportConfig);
    patched.push({ file: slot.target, phrase: slot.phrase, campaign_id: slot.campaign_id });
  }

  const xlsxFiles = fs
    .readdirSync(V262)
    .filter((f) => f.toLowerCase().endsWith('.xlsx') && f.toLowerCase().includes('v2.6.2'))
    .sort();
  if (xlsxFiles.length !== 10) {
    throw new Error(`Expected 10 v2.6.2 XLSX files, found ${xlsxFiles.length}`);
  }

  const manifest = {
    generated_at: GENERATED_AT,
    output_directory: V262.replace(/\\/g, '/'),
    hotfix: 'phrase-slot-restore-v2.6.2',
    supersedes_deployable_generation: 'CORVONERO-CAMPAIGN-V2.6.1-FINAL-2026-06-30',
    semantic_authority_unchanged: 'CORVONERO-CAMPAIGN-V2.6-FINAL-v1',
    campaigns: 10,
    groups: 71,
    phrase_slots: 926,
    ads: 71,
    restored_slots: patched,
    xlsx_files: xlsxFiles,
  };
  fs.writeFileSync(
    path.join(V262, 'CORVONERO-CAMPAIGN-V2.6.2-OUTPUT-MANIFEST-v1.json'),
    JSON.stringify(manifest, null, 2) + '\n',
  );

  const checksumTargets = fs
    .readdirSync(V262)
    .filter((f) => !f.includes('SHA256SUMS'))
    .map((f) => path.join(V262, f));
  const shaLines = checksumTargets
    .filter((f) => fs.statSync(f).isFile())
    .sort((a, b) => path.basename(a).localeCompare(path.basename(b)))
    .map((f) => `${sha256File(f)}  ${path.basename(f)}`);
  fs.writeFileSync(path.join(V262, 'CORVONERO-CAMPAIGN-V2.6.2-SHA256SUMS-v1.txt'), shaLines.join('\n') + '\n');

  const genDoc = {
    generated_at: GENERATED_AT,
    version: 'V2.6.2',
    root_cause: 'GENERATION_DEFECT — phrase allocation omitted merged ca-02-troubleshooting-not-working slots',
    fix: 'Restored 2 keyword rows in CA-02 LOCAL/REMOTE XLSX; build_phrase_allocation now applies V26_SINGLE_PHRASE_MERGE',
    semantic_decisions_changed: false,
    restored_phrases: ['программа 1с не работает'],
    phrase_slots: 926,
    output_directory: V262.replace(/\\/g, '/'),
  };
  fs.writeFileSync(
    path.join(PILOT, 'CORVONERO-CAMPAIGN-V2.6.2-GENERATION-v1.json'),
    JSON.stringify(genDoc, null, 2) + '\n',
  );

  console.log(JSON.stringify({ status: 'OK', patched, phrase_slots: 926, output: V262 }, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
