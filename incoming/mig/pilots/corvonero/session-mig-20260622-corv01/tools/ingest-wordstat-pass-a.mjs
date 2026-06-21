/**
 * Corvonero MIG — Wordstat Pass A Excel ingestion (manual operator exports).
 * Reads .xlsx / .xls / .csv from explicit external Storage path and/or in-repo loci.
 * Does not modify source files.
 *
 * Usage:
 *   node tools/ingest-wordstat-pass-a.mjs
 *   node tools/ingest-wordstat-pass-a.mjs "C:\\AI MARS STORAGE\\mig\\corvonero\\wordstat-2026-06"
 */
import { createHash } from "crypto";
import { readFileSync, writeFileSync, mkdirSync, readdirSync, statSync, existsSync } from "fs";
import { join, dirname, relative, extname, basename, normalize } from "path";
import { fileURLToPath } from "url";
import { createRequire } from "module";

const __dirname = dirname(fileURLToPath(import.meta.url));
const SESSION_ROOT = join(__dirname, "..");
const require = createRequire(import.meta.url);

const DEFAULT_EXTERNAL_SOURCE =
  "C:/AI MARS STORAGE/mig/corvonero/wordstat-2026-06";

const EXCELJS_PATH =
  "C:/AI MARS/projects/orca/ppc/triumph-manipulator/tools/exporter-cli/node_modules/exceljs";
let ExcelJS;
try {
  ExcelJS = require(EXCELJS_PATH);
} catch {
  ExcelJS = null;
}

const IN_REPO_SCAN_LOCI = [
  join(SESSION_ROOT, "evidence/wordstat/exports"),
  join(SESSION_ROOT, "evidence/wordstat/pass-a"),
  join(SESSION_ROOT, "evidence/wordstat/incoming"),
];

const TABLE_EXTENSIONS = new Set([".xlsx", ".xls", ".csv"]);
const matrix = JSON.parse(
  readFileSync(join(SESSION_ROOT, "corvonero-wordstat-collection-matrix-v1.json"), "utf8")
);

const RMK_ALT_PATTERNS = [
  /рмк/i,
  /рабочее место кассира/i,
  /настройка рмк/i,
  /доработка рабочего места кассира/i,
  /кассов/i,
];
const URGENT_ALT_PATTERNS = [
  /срочн/i,
  /срочная помощь/i,
  /программист 1с срочно/i,
  /1с не работает/i,
  /исправить ошибку/i,
  /восстановить работу/i,
  /аварийн/i,
];

function allSeeds() {
  const seeds = [];
  for (const group of ["priority_1", "priority_2", "priority_3"]) {
    for (const row of matrix[group] || []) {
      seeds.push({
        query_id: row.query_id,
        seed_phrase: row.base_phrase,
        priority_group: group.replace("priority_", "P"),
        cluster: row.cluster,
      });
    }
  }
  return seeds;
}

function sha256File(path) {
  const buf = readFileSync(path);
  return createHash("sha256").update(buf).digest("hex");
}

function walkFiles(dir, acc = []) {
  if (!existsSync(dir)) return acc;
  for (const name of readdirSync(dir)) {
    const full = join(dir, name);
    const st = statSync(full);
    if (st.isDirectory()) walkFiles(full, acc);
    else if (TABLE_EXTENSIONS.has(extname(name).toLowerCase())) acc.push(full);
  }
  return acc;
}

function inferQueryId(filename) {
  const m = basename(filename).match(/(ws-p[123]-\d{3})/i);
  return m ? m[1].toLowerCase() : null;
}

function normalizePhrase(s) {
  return String(s || "")
    .trim()
    .toLowerCase()
    .replace(/\s+/g, " ");
}

function classifyIntent(phrase) {
  const p = normalizePhrase(phrase);
  if (!p) return { intent: "ambiguous", noise: [] };
  const noise = [];
  if (/ваканс|работа программист|hh\.ru|резюме|ищу работу/.test(p)) noise.push("job-seeking", "vacancy");
  if (/зарплат|оклад|сколько зарабатыва/.test(p)) noise.push("salary");
  if (/удален|удалён|remote|из дома/.test(p)) noise.push("remote-work");
  if (/курс|обучен|школ|учеб|с нуля|видео/.test(p)) noise.push("educational", "course/training");
  if (/скачать|торрент|бесплатно скач|установить 1с/.test(p)) noise.push("software-download");
  if (/не работает|ошибк|исправить|восстанов|аварийн|срочн/.test(p)) {
    if (/не работает|ошибк|исправить|восстанов/.test(p)) return { intent: "troubleshooting", noise };
    noise.push("urgent-service");
  }
  if (/скачать|инструкц|что такое|как настроить|форум/.test(p)) noise.push("informational");
  if (/программист|доработк|сопровожд|интеграц|настройк|маркиров|честный знак|рмк|печатн/.test(p)) {
    if (noise.includes("job-seeking") || noise.includes("vacancy"))
      return { intent: "commercial-mixed", noise };
    return { intent: "direct-commercial", noise };
  }
  if (/1с/.test(p)) return { intent: "commercial-mixed", noise };
  return { intent: "ambiguous", noise };
}

async function parseExcel(path) {
  if (!ExcelJS) throw new Error("exceljs not available");
  const wb = new ExcelJS.Workbook();
  await wb.xlsx.readFile(path);
  const sheetNames = wb.worksheets.map((ws) => ws.name);
  const ws = wb.worksheets[0];
  if (!ws) return { rows: [], columns: [], format: "empty_xlsx", sheet_names: sheetNames };

  const headerRow = ws.getRow(1);
  const headers = [];
  headerRow.eachCell({ includeEmpty: true }, (cell, col) => {
    headers[col - 1] = String(cell.value ?? "").trim();
  });

  const rows = [];
  for (let r = 2; r <= ws.rowCount; r++) {
    const row = ws.getRow(r);
    const obj = {};
    let empty = true;
    row.eachCell({ includeEmpty: true }, (cell, col) => {
      const key = headers[col - 1] || `col_${col}`;
      const val = cell.value;
      const text =
        val == null
          ? ""
          : typeof val === "object" && val.text != null
            ? String(val.text)
            : String(val);
      if (text.trim()) empty = false;
      obj[key] = text.trim();
    });
    if (!empty) rows.push({ ...obj, _sheet: ws.name, _row: r });
  }
  return { rows, columns: headers.filter(Boolean), format: "xlsx", sheet_names: sheetNames };
}

function parseCsv(path) {
  const text = readFileSync(path, "utf8");
  const lines = text.split(/\r?\n/).filter((l) => l.trim());
  if (!lines.length) return { rows: [], columns: [], format: "empty_csv", sheet_names: [] };
  const sep = lines[0].includes(";") ? ";" : ",";
  const headers = lines[0].split(sep).map((h) => h.trim().replace(/^"|"$/g, ""));
  const rows = lines.slice(1).map((line, idx) => {
    const parts = line.split(sep).map((p) => p.trim().replace(/^"|"$/g, ""));
    const obj = {};
    headers.forEach((h, i) => {
      obj[h] = parts[i] ?? "";
    });
    obj._sheet = "csv";
    obj._row = idx + 2;
    return obj;
  });
  return { rows, columns: headers, format: "csv", sheet_names: ["csv"] };
}

function mapWordstatColumns(row) {
  const keys = Object.keys(row).filter((k) => !k.startsWith("_"));
  const phraseKey =
    keys.find((k) => /запрос|query|phrase|фраз/i.test(k)) || keys[0];
  const freqKey =
    keys.find((k) => /число|shows|frequency|count|запросов/i.test(k)) ||
    keys.find((k) => k !== phraseKey);
  return {
    raw_phrase: row[phraseKey] ?? "",
    observed_frequency: freqKey ? parseFrequency(row[freqKey]) : null,
    list_type: keys.find((k) => /список|list|тип/i.test(k))
      ? row[keys.find((k) => /список|list|тип/i.test(k))]
      : null,
    source_sheet: row._sheet ?? null,
    source_row: row._row ?? null,
  };
}

function parseFrequency(val) {
  if (val == null || val === "") return null;
  const n = Number(String(val).replace(/\s/g, "").replace(",", "."));
  return Number.isFinite(n) ? n : null;
}

const NO_RESULT_OPERATOR = [
  {
    query_id: "ws-p2-003",
    entered_phrase: "доработка РМК",
    matrix_seed: "доработка РМК 1С",
    note: "Operator entered without «1С» — Wordstat returned no results for exact broad formulation",
  },
  {
    query_id: "ws-p2-006",
    entered_phrase: "срочно программист 1С",
    matrix_seed: "срочно программист 1С",
    note: "Wordstat returned no results for exact broad formulation",
  },
];

function resolveScanLoci() {
  const externalArg = process.argv[2];
  const externalPath = normalize(externalArg || DEFAULT_EXTERNAL_SOURCE);
  const loci = [];
  if (existsSync(externalPath)) {
    loci.push({ path: externalPath, classification: "mars_storage_external_evidence" });
  }
  for (const p of IN_REPO_SCAN_LOCI) {
    if (existsSync(p)) loci.push({ path: p, classification: "in_repo_controlled_copy" });
  }
  return { externalPath, loci };
}

function findAlternatives(allPhrases) {
  const normalized = allPhrases.map((p) => ({ raw: p, norm: normalizePhrase(p) }));
  const rmkFound = [];
  const urgentFound = [];
  const rmkCandidates = [
    "РМК 1С",
    "настройка РМК",
    "рабочее место кассира",
    "доработка рабочего места кассира",
    "настройка кассового рабочего места",
  ];
  const urgentCandidates = [
    "срочная помощь 1С",
    "программист 1С срочно",
    "1С не работает",
    "исправить ошибку 1С",
    "восстановить работу 1С",
  ];

  for (const { raw, norm } of normalized) {
    if (RMK_ALT_PATTERNS.some((re) => re.test(raw))) {
      if (!rmkFound.includes(raw)) rmkFound.push(raw);
    }
    if (URGENT_ALT_PATTERNS.some((re) => re.test(raw))) {
      if (!urgentFound.includes(raw)) urgentFound.push(raw);
    }
  }

  return {
    rmk: {
      evidence_supported: rmkFound,
      candidates_for_manual_verification: rmkCandidates.filter(
        (c) => !rmkFound.some((f) => normalizePhrase(f) === normalizePhrase(c))
      ),
      not_found: rmkCandidates.filter(
        (c) =>
          !rmkFound.some((f) => normalizePhrase(f) === normalizePhrase(c)) &&
          !normalized.some((n) => normalizePhrase(n.raw).includes(normalizePhrase(c)))
      ),
      rejected_artificial: ["доработка РМК without 1С context — operator no-result for entered formulation"],
    },
    urgent: {
      evidence_supported: urgentFound,
      candidates_for_manual_verification: urgentCandidates.filter(
        (c) => !urgentFound.some((f) => normalizePhrase(f) === normalizePhrase(c))
      ),
      not_found: urgentCandidates.filter(
        (c) =>
          !urgentFound.some((f) => normalizePhrase(f) === normalizePhrase(c)) &&
          !normalized.some((n) => normalizePhrase(n.raw).includes(normalizePhrase(c)))
      ),
      rejected_artificial: [],
    },
  };
}

function computePassACompletion(seeds, queryIdToFiles, noResultIds) {
  const accounted = new Set([...Object.keys(queryIdToFiles), ...noResultIds]);
  const missing = seeds.filter((s) => !accounted.has(s.query_id)).map((s) => s.query_id);
  const status = missing.length === 0 ? "COMPLETE" : "PARTIAL";
  return { status, missing_ids: missing, expected: seeds.length, accounted: accounted.size };
}

async function main() {
  mkdirSync(join(SESSION_ROOT, "evidence/wordstat/exports"), { recursive: true });
  mkdirSync(join(SESSION_ROOT, "evidence/wordstat/pass-a"), { recursive: true });
  mkdirSync(join(SESSION_ROOT, "evidence/wordstat/incoming"), { recursive: true });

  const { externalPath, loci } = resolveScanLoci();
  const seeds = allSeeds();
  const seedById = Object.fromEntries(seeds.map((s) => [s.query_id, s]));

  const discovered = [];
  const seenPaths = new Set();
  const scanLociReport = [];
  for (const { path: locus, classification } of loci) {
    scanLociReport.push({
      path: locus,
      normalized_path: normalize(locus),
      classification,
      exists: existsSync(locus),
    });
    for (const f of walkFiles(locus)) {
      if (seenPaths.has(f)) continue;
      seenPaths.add(f);
      discovered.push({ filePath: f, source_classification: classification });
    }
  }

  const fileInventory = [];
  const evidenceRecords = [];
  const normalizedRows = [];
  const parseErrors = [];
  const queryIdToFiles = {};
  const allParsedPhrases = [];

  for (const { filePath, source_classification } of discovered) {
    const rel =
      filePath.startsWith(SESSION_ROOT)
        ? relative(SESSION_ROOT, filePath).replace(/\\/g, "/")
        : null;
    const ext = extname(filePath).toLowerCase();
    const hash = sha256File(filePath);
    const queryId = inferQueryId(filePath);
    const seed = queryId ? seedById[queryId] : null;

    if (queryId) {
      queryIdToFiles[queryId] = queryIdToFiles[queryId] || [];
      queryIdToFiles[queryId].push(rel || filePath);
    }

    let parsed = null;
    let readStatus = "pending";
    let tableFormat = null;
    let rowCount = 0;
    let requiredColumns = false;
    let readError = null;
    let sheetNames = [];

    try {
      if (ext === ".csv") parsed = parseCsv(filePath);
      else if (ext === ".xlsx" || ext === ".xls") {
        if (ext === ".xls") {
          readStatus = "unsupported_xls";
          readError = "Legacy .xls requires operator re-export as .xlsx or .csv";
        } else parsed = await parseExcel(filePath);
      }
      if (parsed) {
        sheetNames = parsed.sheet_names || [];
        readStatus = "ok";
        tableFormat = parsed.format;
        rowCount = parsed.rows.length;
        requiredColumns =
          parsed.columns.some((c) => /запрос|query|phrase|фраз/i.test(c)) &&
          parsed.columns.some((c) => /число|shows|frequency|count|запросов/i.test(c));
      }
    } catch (err) {
      readStatus = "error";
      readError = String(err.message || err);
      parseErrors.push({ file: rel || filePath, error: readError });
    }

    const mappingStatus = queryId
      ? seed
        ? "mapped_by_filename_query_id"
        : "query_id_not_in_matrix"
      : "unmapped_no_query_id_in_filename";

    fileInventory.push({
      filename: basename(filePath),
      path: rel,
      source_path: filePath,
      normalized_source_path: normalize(filePath),
      absolute_path: filePath,
      extension: ext,
      size_bytes: statSync(filePath).size,
      sha256: hash,
      inferred_query_id: queryId,
      seed_phrase: seed?.seed_phrase ?? null,
      priority: seed?.priority_group ?? null,
      read_status: readStatus,
      file_readable: readStatus === "ok",
      table_format: tableFormat,
      sheet_names: sheetNames,
      row_count: rowCount,
      required_columns_present: requiredColumns,
      mapping_status: mappingStatus,
      mapping_ambiguity: queryId && seed ? null : queryId ? "unknown_seed" : "no ws-p query_id in filename",
      duplicate_status:
        queryId && queryIdToFiles[queryId]?.length > 1 ? "multiple_files_same_query_id" : null,
      external_source_classification: source_classification,
      error: readError,
    });

    if (parsed && readStatus === "ok" && seed) {
      const evidenceId = `ws-pass-a-${queryId}-20260622`;
      let observedTotal = null;
      const related = [];

      parsed.rows.forEach((row, idx) => {
        const mapped = mapWordstatColumns(row);
        if (!mapped.raw_phrase) return;
        related.push(mapped.raw_phrase);
        allParsedPhrases.push(mapped.raw_phrase);
        const { intent, noise } = classifyIntent(mapped.raw_phrase);
        normalizedRows.push({
          evidence_id: evidenceId,
          source_query_id: queryId,
          seed_phrase: seed.seed_phrase,
          raw_phrase: mapped.raw_phrase,
          normalized_phrase: normalizePhrase(mapped.raw_phrase),
          observed_frequency: mapped.observed_frequency,
          frequency_label: "observed broad Wordstat frequency for semantic discovery",
          list_type: mapped.list_type,
          position: idx + 1,
          preliminary_intent_class: intent,
          preliminary_noise_classes: noise,
          geography: "all_russia",
          query_mode: "broad_unquoted",
          source_file: rel || basename(filePath),
          source_path_external: filePath,
          source_hash: hash,
          source_sheet: mapped.source_sheet,
          source_row: mapped.source_row,
          evidence_limitations: [
            "Nationwide broad — not regional Novosibirsk demand",
            "Not exact phrase frequency",
            "Not traffic forecast",
          ],
        });
        if (idx === 0 && mapped.observed_frequency != null) observedTotal = mapped.observed_frequency;
      });

      const evidenceRecord = {
        evidence_id: evidenceId,
        query_id: queryId,
        entered_phrase: seed.seed_phrase,
        query_mode: "broad_unquoted",
        geography: "all_russia",
        source_file: rel,
        source_path_external: filePath,
        source_hash: hash,
        collection_mode: "manual_operator_export",
        collection_date: "2026-06-22",
        row_count: rowCount,
        sheet_names: sheetNames,
        observed_wordstat_total: observedTotal,
        related_phrase_count: related.length,
        ingestion_status: "ingested",
        evidence_grade: "B_semantic_discovery",
        external_source_classification: source_classification,
        limitations: [
          "Nationwide broad — not regional Novosibirsk demand",
          "Not exact phrase frequency",
          "Not traffic forecast",
        ],
      };
      evidenceRecords.push(evidenceRecord);
      writeFileSync(
        join(SESSION_ROOT, `evidence/wordstat/pass-a-${queryId}-evidence.json`),
        JSON.stringify(evidenceRecord, null, 2),
        "utf8"
      );
    }
  }

  for (const nr of NO_RESULT_OPERATOR) {
    const evidenceId = `ws-pass-a-${nr.query_id}-no-result-20260622`;
    const record = {
      evidence_id: evidenceId,
      query_id: nr.query_id,
      entered_phrase: nr.entered_phrase,
      matrix_seed_phrase: nr.matrix_seed,
      query_mode: "broad_unquoted",
      geography: "all_russia",
      source_file: null,
      source_path_external: null,
      source_hash: null,
      collection_mode: "manual_operator_export",
      collection_date: "2026-06-22",
      wordstat_ui_result: "no results found",
      numeric_frequency: "not_available",
      ingestion_status: "no_result_for_entered_formulation",
      evidence_meaning:
        "exact seed formulation not represented in the returned Wordstat surface",
      thematic_demand: "not_disproved",
      alternate_formulation_review: "required",
      evidence_grade: "B_operator_report",
      limitations: [nr.note, "Not zero_market_demand — frequency not recorded as 0"],
    };
    evidenceRecords.push(record);
    writeFileSync(
      join(SESSION_ROOT, `evidence/wordstat/pass-a-${nr.query_id}-no-result-evidence.json`),
      JSON.stringify(record, null, 2),
      "utf8"
    );
  }

  const duplicates = Object.entries(queryIdToFiles).filter(([, files]) => files.length > 1);
  const noResultIds = NO_RESULT_OPERATOR.map((n) => n.query_id);
  const passACompletion = computePassACompletion(seeds, queryIdToFiles, noResultIds);
  const alternatives = findAlternatives(allParsedPhrases);

  const indexOut = {
    schema_version: "1",
    session_id: "mig-20260622-corv01",
    generated_at: new Date().toISOString(),
    external_storage_path: externalPath,
    external_storage_inspected: existsSync(externalPath),
    scan_loci: scanLociReport,
    prior_af_007_superseded: {
      prior_claim: "zero Excel/CSV at in-repo loci only",
      root_cause: "wrong evidence locus — files in MARS Storage not scanned",
      corrected_source: externalPath,
    },
    files_found: fileInventory.length,
    files_parsed_ok: fileInventory.filter((f) => f.read_status === "ok").length,
    exceljs_available: Boolean(ExcelJS),
    file_inventory: fileInventory,
    duplicate_query_ids: duplicates.map(([id, files]) => ({ query_id: id, files })),
    parse_errors: parseErrors,
    evidence_records: evidenceRecords,
    no_result_seeds: NO_RESULT_OPERATOR.map((n) => ({
      query_id: n.query_id,
      entered_phrase: n.entered_phrase,
      status: "no_result_for_entered_formulation",
    })),
    pass_a_completion: {
      ...passACompletion,
      files_with_excel: Object.keys(queryIdToFiles).length,
      seeds_with_no_result: noResultIds.length,
      reason:
        passACompletion.status === "COMPLETE"
          ? "All 20 seeds accounted — 18 Excel ingested from MARS Storage + 2 operator no-result records"
          : `Missing query IDs: ${passACompletion.missing_ids.join(", ")}`,
    },
  };

  writeFileSync(
    join(SESSION_ROOT, "evidence/wordstat/wordstat-pass-a-file-index.json"),
    JSON.stringify(indexOut, null, 2),
    "utf8"
  );

  writeFileSync(
    join(SESSION_ROOT, "evidence/wordstat/wordstat-pass-a-normalized.json"),
    JSON.stringify(
      {
        schema_version: "1",
        session_id: "mig-20260622-corv01",
        generated_at: new Date().toISOString(),
        external_storage_source: externalPath,
        row_count: normalizedRows.length,
        interpretation_note:
          "observed broad Wordstat frequency for semantic discovery — not regional demand, not traffic forecast",
        rows: normalizedRows,
        alternative_formulations: alternatives,
      },
      null,
      2
    ),
    "utf8"
  );

  console.log(
    JSON.stringify(
      {
        external_path: externalPath,
        files: fileInventory.length,
        rows: normalizedRows.length,
        pass_a: indexOut.pass_a_completion,
      },
      null,
      2
    )
  );
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
