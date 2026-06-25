#!/usr/bin/env node
'use strict';

/**
 * Strict structural validation for Corvonero Commander XLSX v4.
 */
const fs = require('fs');
const path = require('path');
const { readZipEntryUtf8 } = require(path.resolve(
  __dirname,
  '../../../ppc/triumph-manipulator/tools/exporter-cli/xlsx-zip-patch'
));

const ROOT = path.resolve(__dirname, '..');
const XLSX = path.join(ROOT, 'exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v7.1.xlsx');
const DATASET = path.join(ROOT, 'production/direct-commander-production-dataset-v7.1.json');
const EXCLUSION_REG = path.join(ROOT, 'production/operator-semantic-exclusion-registry-v1.json');
const OUT_JSON = path.join(ROOT, 'production/validation/direct-commander-validation-v7.1.json');
const OUT_MD = path.join(ROOT, 'production/validation/direct-commander-validation-v7.1.md');

const DATA_START = 16;
const COL = { groupName: 5, phrase: 8, h1: 10, h2: 11, text: 12, url: 48, bid: 54, groupNeg: 68, adType: 2 };

const BAD_AD_CLAIMS = [
  /под ключ/i,
  /срочно/i,
  /быстро и точно/i,
  /гарант/i,
  /24\/7/,
  /официальн.*партн/i,
  /сертифиц/i,
  /лучш/i,
  /любой сложности/i,
  /без ошибок/i,
  /результат гарант/i,
  /найд[её]м причину и верн/i,
  /сохраним ваши доработки/i,
  /без потери данных/i,
  /обновим 1с и сохраним/i,
];
const BAD_KW_PATTERNS = [
  { re: /^как (сделать|настроить|изменить|подключить|установить)/, label: 'DIY/informational' },
  { re: /инструкц/, label: 'informational' },
  { re: /личный кабинет/, label: 'informational' },
  { re: /какие автозапчасти подлежат/, label: 'regulatory' },
  { re: /когда начн.*маркиров/, label: 'regulatory' },
  { re: /с какого года/, label: 'regulatory' },
  { re: /попадают под маркиров/, label: 'regulatory' },
  { re: /лекарство без маркиров/, label: 'regulatory' },
  { re: /час[аы]? работы программист/, label: 'employment' },
  { re: /как стать программист/, label: 'training' },
  { re: /лекарства подлежащие маркиров/, label: 'regulatory' },
  { re: /скачать|торрент|кряк/, label: 'download' },
  { re: /ваканс|резюме|зарплат/, label: 'employment' },
];

const MARKER_RE = /\[C0[1-8]\]/;

const V7_HARD_EXCLUDE_PHRASES = [
  'маркировка лекарств проверить',
  'маркировка автозапчастей 2026',
  'маркировка автозапчастей честный знак 2026',
  '1с программист 2026',
];

const RESCUE_TAIL_RE = /\s+-(?:вакансия|обучение|курсы|резюме|как стать)/i;

function loadExclusionPhrases() {
  const phrases = [...V7_HARD_EXCLUDE_PHRASES];
  if (fs.existsSync(EXCLUSION_REG)) {
    const reg = JSON.parse(fs.readFileSync(EXCLUSION_REG, 'utf8'));
    for (const e of reg.exclusions || []) phrases.push(e.normalized_phrase);
  }
  return [...new Set(phrases.map(normPhrase))];
}

function colToLetter(col) {
  let n = col;
  let s = '';
  while (n > 0) {
    s = String.fromCharCode(65 + ((n - 1) % 26)) + s;
    n = Math.floor((n - 1) / 26);
  }
  return s;
}

function cellValue(rowXml, ref) {
  const re = new RegExp(`<c\\s+r="${ref}"[^>]*>[\\s\\S]*?<v>([\\s\\S]*?)</v>`, 'i');
  const m = rowXml.match(re);
  if (!m) return '';
  return m[1]
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&apos;/g, "'");
}

function rowXml(sheet, rowNum) {
  const re = new RegExp(`<row r="${rowNum}"[^>]*>[\\s\\S]*?</row>`);
  const m = sheet.match(re);
  return m ? m[0] : null;
}

function getCell(sheet, row, col) {
  const rx = rowXml(sheet, row);
  if (!rx) return '';
  return cellValue(rx, `${colToLetter(col)}${row}`);
}

function listRows(sheet) {
  const rows = [];
  const re = /<row r="(\d+)"/g;
  let m;
  while ((m = re.exec(sheet)) !== null) rows.push(parseInt(m[1], 10));
  return rows.sort((a, b) => a - b);
}

function stripInlineNeg(p) {
  return p.replace(/\s+-[\wа-яё]+/gi, '').trim();
}

function normPhrase(s) {
  return String(s || '').toLowerCase().replace(/ё/g, 'е').replace(/\s+/g, ' ').trim();
}

function collisionTest(phrase, neg) {
  const p = normPhrase(stripInlineNeg(phrase));
  const n = normPhrase(neg);
  if (!n) return false;
  if (n.includes(' ')) return p.includes(n);
  const words = p.split(/\s+/);
  return words.includes(n) || p.includes(` ${n} `) || p.startsWith(`${n} `) || p.endsWith(` ${n}`);
}

function main() {
  const errors = [];
  const warnings = [];
  const checks = [];

  if (!fs.existsSync(XLSX)) {
    errors.push('XLSX file missing');
    writeReport(errors, warnings, checks, {});
    process.exit(1);
  }

  const dataset = JSON.parse(fs.readFileSync(DATASET, 'utf8'));
  const exclusionPhrases = loadExclusionPhrases();
  const REVIEW_WB = path.join(ROOT, 'production/validation/review-workbook-v7.1-result.json');
  let sheet;
  try {
    sheet = readZipEntryUtf8(XLSX, 'xl/worksheets/sheet1.xml');
    checks.push('workbook_opens: pass');
  } catch (e) {
    errors.push(`Cannot read sheet1: ${e.message}`);
    writeReport(errors, warnings, checks, {});
    process.exit(1);
  }

  const dataRows = listRows(sheet).filter((r) => r >= DATA_START);
  const groupsSeen = new Map();
  const phrases = [];
  const phraseOwners = new Map();
  const h1ByGroup = new Map();
  let adRows = 0;
  let kwRows = 0;
  let triumphRefs = 0;
  let markerMissing = 0;

  for (const r of dataRows) {
    const gn = getCell(sheet, r, COL.groupName);
    const ph = getCell(sheet, r, COL.phrase);
    const h1 = getCell(sheet, r, COL.h1);
    const url = getCell(sheet, r, COL.url);
    const bid = getCell(sheet, r, COL.bid);
    const blob = `${gn}${ph}${h1}${url}${bid}`;

    if (/triumph|manipulator-triumph|gruzotaxi/i.test(blob)) triumphRefs++;

    if (gn) {
      if (!groupsSeen.has(gn)) groupsSeen.set(gn, { ads: 0, kws: 0, hasUrl: false, hasNeg: false });
      if (ph) groupsSeen.get(gn).kws++;
      if (h1) groupsSeen.get(gn).ads++;
      if (!MARKER_RE.test(gn)) markerMissing++;
    }

    if (h1) {
      adRows++;
      if (h1.length > 56) errors.push(`row ${r}: h1 length ${h1.length}`);
      const h2 = getCell(sheet, r, COL.h2);
      const tx = getCell(sheet, r, COL.text);
      if (h2.length > 30) errors.push(`row ${r}: h2 length ${h2.length}`);
      if (tx.length > 81) errors.push(`row ${r}: text length ${tx.length}`);
      if (url && !/^https:\/\/lk\.corvonero\.ru\//.test(url)) errors.push(`row ${r}: bad url ${url.slice(0, 80)}`);
      if (url && url.includes('??')) errors.push(`row ${r}: double question mark in url`);
      if (url && !/utm_campaign=corvonero_1c_search_nsk/.test(url)) warnings.push(`row ${r}: non-unified utm_campaign in url`);
      if (url && /triumph|gruzotaxi/i.test(url)) errors.push(`row ${r}: triumph url reference`);

      const adBlob = `${h1}${h2}${tx}`;
      for (const re of BAD_AD_CLAIMS) {
        if (re.test(adBlob)) errors.push(`row ${r}: unsupported claim in ad (${re})`);
      }

      if (gn) {
        if (!h1ByGroup.has(gn)) h1ByGroup.set(gn, new Set());
        h1ByGroup.get(gn).add(h1);
      }
    }

    if (ph) {
      kwRows++;
      const np = normPhrase(stripInlineNeg(ph));
      phrases.push(ph);
      if (parseFloat(bid) <= 0) errors.push(`row ${r}: zero bid`);
      if (!ph.trim()) errors.push(`row ${r}: empty phrase`);

      if (phraseOwners.has(np)) {
        errors.push(`row ${r}: duplicate phrase ownership ${np}`);
      } else {
        phraseOwners.set(np, gn);
      }

      for (const { re, label } of BAD_KW_PATTERNS) {
        if (re.test(np)) errors.push(`row ${r}: bad keyword pattern (${label}): ${ph.slice(0, 60)}`);
      }

      for (const banned of exclusionPhrases) {
        if (np === banned) errors.push(`row ${r}: excluded phrase leaked to export: ${ph}`);
      }

      if (RESCUE_TAIL_RE.test(ph) && ph.split(/\s+-/).length >= 5) {
        errors.push(`row ${r}: destructive inline-minus rescue tail: ${ph.slice(0, 80)}`);
      }

      const globalNegs = dataset.global_negatives || [];
      const hits = globalNegs.filter((n) => collisionTest(ph, n));
      if (hits.length) errors.push(`row ${r}: global negative collision on active keyword: ${hits.join(', ')}`);
    }

    const groupNeg = getCell(sheet, r, COL.groupNeg);
    if (gn && groupNeg && groupsSeen.has(gn)) groupsSeen.get(gn).hasNeg = true;
    if (gn && url && groupsSeen.has(gn)) groupsSeen.get(gn).hasUrl = true;
  }

  if (triumphRefs > 0) errors.push(`Triumph legacy references: ${triumphRefs}`);
  if (markerMissing > 0) errors.push(`Group names missing [C0x] marker: ${markerMissing} rows`);

  const expectedGroups = dataset.groups.length;
  if (groupsSeen.size !== expectedGroups) {
    errors.push(`Expected ${expectedGroups} active groups in sheet, found ${groupsSeen.size}`);
  }

  if (kwRows !== dataset.keywords.length) {
    errors.push(`Keyword rows ${kwRows} vs dataset ${dataset.keywords.length}`);
  }

  for (const [gn, info] of groupsSeen) {
    if (info.kws < 1) errors.push(`Group "${gn.slice(0, 40)}" has no keywords`);
    if (info.ads < 1) errors.push(`Group "${gn.slice(0, 40)}" has no ads`);
    if (!info.hasUrl && info.ads > 0) warnings.push(`Group "${gn.slice(0, 40)}" url not verified on ad row`);
  }

  const heldInSheet = [...groupsSeen.keys()].filter((g) =>
    (dataset.held_groups || []).some((h) => g.includes(h.group_name))
  );
  if (heldInSheet.length) errors.push(`Held groups found in sheet: ${heldInSheet.length}`);

  const dupPhrases = phrases.filter((p, i) => phrases.indexOf(p) !== i);
  if (dupPhrases.length) errors.push(`Duplicate phrases in sheet: ${dupPhrases.slice(0, 5).join('; ')}`);

  const metaType = getCell(sheet, 7, 5);
  if (!metaType.includes('перфоманс') && !metaType.includes('Текстово')) {
    warnings.push(`Campaign type cell: ${metaType}`);
  }
  const promo = getCell(sheet, 11, 5);
  if (!promo.includes('lk.corvonero.ru')) errors.push(`Promotion URL wrong: ${promo}`);

  const dsCollisions = dataset.collision_validation?.literal_collisions_after || 0;
  if (dsCollisions) errors.push(`Dataset collision blocking after correction: ${dsCollisions}`);

  if (fs.existsSync(REVIEW_WB)) {
    const rw = JSON.parse(fs.readFileSync(REVIEW_WB, 'utf8'));
    if (!rw.evidence_populated) errors.push('Review workbook v7.1 evidence not populated');
    checks.push(`review_workbook_evidence: ${rw.evidence_populated ? 'pass' : 'fail'}`);
  } else {
    warnings.push('review-workbook-v7.1-result.json missing');
  }

  checks.push(`exclusion_registry_phrases_checked: ${exclusionPhrases.length}`);

  const kwBands = dataset.group_viability
    ? {}
    : {};
  const bandCounts = { '1': 0, '2': 0, '3-4': 0, '5-9': 0, '10+': 0 };
  for (const g of dataset.groups) {
    const n = g.keywords.length;
    if (n === 1) bandCounts['1']++;
    else if (n === 2) bandCounts['2']++;
    else if (n <= 4) bandCounts['3-4']++;
    else if (n <= 9) bandCounts['5-9']++;
    else bandCounts['10+']++;
  }

  const counts = {
    data_rows: dataRows.length,
    active_groups_in_sheet: groupsSeen.size,
    held_groups: (dataset.held_groups || []).length,
    ad_rows: adRows,
    keyword_rows: kwRows,
    excluded_keywords_v2: (dataset.keywords?.length || 0) - kwRows,
    global_negatives: (dataset.global_negatives || []).length,
    direction_negative_tokens: Object.values(dataset.direction_negatives || {}).flat().length,
    group_cross_negatives: Object.values(dataset.cross_negatives || {}).flat().length,
    collision_errors: errors.filter((e) => e.includes('collision')).length + dsCollisions,
    keyword_bands: bandCounts,
  };

  const ok = errors.length === 0;
  writeReport(errors, warnings, checks, counts, ok);
  console.log(ok ? 'VALIDATION PASS' : 'VALIDATION FAIL', counts);
  if (!ok) process.exit(1);
}

function writeReport(errors, warnings, checks, counts, ok = false) {
  fs.mkdirSync(path.dirname(OUT_JSON), { recursive: true });
  const report = {
    validated_at: new Date().toISOString(),
    file: XLSX,
    dataset: DATASET,
    status: ok ? 'STRUCTURALLY_VALIDATED' : 'FAILED',
    version: 'v7.1',
    export_model: 'UNIFIED_SINGLE_CAMPAIGN',
    errors,
    warnings,
    checks_performed: checks,
    counts,
    manual_import_check_required: true,
    v7_status: 'REJECTED — SUPERSEDED BY V7.1',
    v7_1_status: ok ? 'GENERATED_AND_EXTERNALLY_VALIDATED' : 'FAILED',
  };
  fs.writeFileSync(OUT_JSON, JSON.stringify(report, null, 2));
  fs.writeFileSync(
    OUT_MD,
    `# Direct Commander XLSX Validation — v7.1\n\n**Status:** ${report.status}\n**Model:** unified single campaign\n**v7:** SUPERSEDED BY V7.1\n\n## Counts\n\n${Object.entries(counts).map(([k, v]) => `- ${k}: ${typeof v === 'object' ? JSON.stringify(v) : v}`).join('\n')}\n\n## Errors (${errors.length})\n\n${errors.length ? errors.map((e) => `- ${e}`).join('\n') : '- none'}\n\n## Warnings (${warnings.length})\n\n${warnings.length ? warnings.map((w) => `- ${w}`).join('\n') : '- none'}\n\n**Manual Commander import check required after operator review.**\n`
  );
}

main();
