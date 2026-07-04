#!/usr/bin/env node
// C2b source persistence only. This file is not authorized for execution without explicit operator approval. Commit/persistence does not authorize Storage export generation, repo artifact generation, Commander import, Direct launch, account mutation, advertising start, Localhost mutation, Storage mutation, or Yandex/API access.
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import { DATA_START_ROW, FORENSIC_COL } from '../src/workbook-forensic-verifier.mjs';
import { sanitizationCellValue as cellText } from '../src/template-sanitizer.mjs';

function requireOperatorGate() {
  if (process.env.CORVONERO_OPERATOR_GATE !== 'APPROVED') {
    console.error(
      'STOP: CORVONERO_OPERATOR_GATE=APPROVED required. This C2b helper is not safe for casual execution.'
    );
    process.exit(1);
  }
}

requireOperatorGate();

const require = createRequire(import.meta.url);
const ExcelJS = require('exceljs');

const PILOT = path.resolve('X:/AI MARS/projects/mars-search-ppc-production/pilots/corvonero');
const PKG = path.resolve('X:/AI MARS STORAGE/exports/corvonero/CORVONERO-CAMPAIGN-V2.6.1-FINAL-2026-06-30');

function norm(s) {
  return String(s ?? '').toLowerCase().trim().replace(/\s+/g, ' ');
}

function slotKey(campaignId, mode, groupId, phrase) {
  return `${campaignId}|${mode}|${groupId}|${norm(phrase)}`;
}

const groupPlan = JSON.parse(fs.readFileSync(path.join(PILOT, 'CORVONERO-CAMPAIGN-V2.6-FINAL-GROUP-PLAN-v1.json'), 'utf8'));
const phraseAlloc = JSON.parse(fs.readFileSync(path.join(PILOT, 'CORVONERO-CAMPAIGN-V2.6-PHRASE-ALLOCATION-v1.json'), 'utf8'));
const arch = JSON.parse(fs.readFileSync(path.join(PILOT, 'CORVONERO-CAMPAIGN-V2.6-CAMPAIGN-ARCHITECTURE-v1.json'), 'utf8'));

const groupNameById = new Map();
for (const g of arch.groups) {
  groupNameById.set(`${g.campaign_id}::${g.group_id}`, g.group_name);
}

const fromGroupPlan = new Map();
for (const g of groupPlan.groups) {
  const phrases = g.phrase_list.split('; ').map((p) => p.trim()).filter(Boolean);
  for (const phrase of phrases) {
    const key = slotKey(g.campaign, g.mode, g.group_id, phrase);
    fromGroupPlan.set(key, {
      campaign_id: g.campaign,
      mode: g.mode,
      group_id: g.group_id,
      group_name: g.group_name,
      phrase,
      source: 'group_plan',
    });
  }
}

const fromAlloc = new Map();
for (const r of phraseAlloc.records.filter((x) => x.production_status === 'DEPLOYABLE')) {
  const mode = r.final_campaign.endsWith('LOCAL') ? 'LOCAL' : 'REMOTE';
  const key = slotKey(r.final_campaign, mode, r.final_group, r.phrase);
  fromAlloc.set(key, {
    campaign_id: r.final_campaign,
    mode,
    group_id: r.final_group,
    group_name: groupNameById.get(`${r.final_campaign}::${r.final_group}`) ?? '',
    phrase: r.phrase,
    phrase_id: r.phrase_id,
    source: 'phrase_allocation',
  });
}

const manifest = JSON.parse(fs.readFileSync(path.join(PKG, 'CORVONERO-CAMPAIGN-V2.6.1-OUTPUT-MANIFEST-v1.json'), 'utf8'));
const fromXlsx = new Map();

for (const file of manifest.xlsx_files ?? manifest.files?.filter((f) => f.endsWith('.xlsx')) ?? []) {
  const full = path.join(PKG, file);
  const wb = new ExcelJS.Workbook();
  await wb.xlsx.readFile(full);
  const texts = wb.getWorksheet('Тексты');
  const m = file.match(/CA-\d+-(LOCAL|REMOTE)/);
  const campaignId = m ? m[0] : '';
  const mode = m ? m[1] : '';
  for (let r = DATA_START_ROW; r <= texts.rowCount; r++) {
    const phrase = cellText(texts, r, FORENSIC_COL.phrase);
    if (!phrase) continue;
    const groupName = cellText(texts, r, FORENSIC_COL.group_name);
    const archG = arch.groups.find((g) => g.campaign_id === campaignId && g.group_name === groupName);
    const gid = archG?.group_id ?? '';
    const key = slotKey(campaignId, mode, gid, phrase);
    fromXlsx.set(key, { campaign_id: campaignId, mode, group_id: gid, group_name: groupName, phrase, file, row: r });
  }
}

const gpNotAlloc = [...fromGroupPlan.keys()].filter((k) => !fromAlloc.has(k));
const allocNotGp = [...fromAlloc.keys()].filter((k) => !fromGroupPlan.has(k));
const gpNotXlsx = [...fromGroupPlan.keys()].filter((k) => !fromXlsx.has(k));
const allocNotXlsx = [...fromAlloc.keys()].filter((k) => !fromXlsx.has(k));

console.log(JSON.stringify({
  group_plan_slots: fromGroupPlan.size,
  phrase_alloc_slots: fromAlloc.size,
  xlsx_slots: fromXlsx.size,
  group_plan_not_in_alloc: gpNotAlloc.length,
  alloc_not_in_group_plan: allocNotGp.length,
  group_plan_not_in_xlsx: gpNotXlsx.length,
  alloc_not_in_xlsx: allocNotXlsx.length,
  missing_from_xlsx_sample: gpNotXlsx.slice(0, 10).map((k) => fromGroupPlan.get(k)),
  alloc_missing_from_xlsx: allocNotXlsx.map((k) => fromAlloc.get(k)),
  group_plan_not_alloc_details: gpNotAlloc.map((k) => fromGroupPlan.get(k)),
}, null, 2));
