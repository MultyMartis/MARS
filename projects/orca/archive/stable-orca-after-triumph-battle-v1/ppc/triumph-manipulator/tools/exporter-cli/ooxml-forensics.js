#!/usr/bin/env node
"use strict";

/**
 * ORCA OOXML Workbook Forensics v0
 * ZIP + OOXML comparison: original Commander template vs generated export.
 * Forensic debugging only — NOT exporter fix · NOT runtime · NOT Direct API.
 */

const fs = require("fs");
const path = require("path");
const os = require("os");
const { execFileSync } = require("child_process");

const ROOT = __dirname;
const DEFAULT_TEMPLATE = path.resolve(
  ROOT,
  "../../assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx"
);
const DEFAULT_GENERATED = path.resolve(
  ROOT,
  "output/triumph-commander-template-fill-draft.xlsx"
);

const OUT_TEMPLATE_INDEX = path.join(ROOT, "xlsx-structure-index-v0.json");
const OUT_GENERATED_INDEX = path.join(ROOT, "generated-xlsx-structure-index-v0.json");

const WORKSHEET_MARKERS = [
  "mergeCell",
  "dataValidation",
  "conditionalFormatting",
  "hyperlinks",
  "ignoredErrors",
  "extLst",
  "sheetPr",
  "sheetViews",
  "cols",
  "sheetData",
];

function usage() {
  console.error(
    "Usage: node ooxml-forensics.js [template.xlsx] [generated.xlsx]\n\n" +
      "Outputs:\n" +
      "  xlsx-structure-index-v0.json\n" +
      "  generated-xlsx-structure-index-v0.json\n\n" +
      "Forensic only — NOT production fix."
  );
  process.exit(1);
}

function psQuote(p) {
  return p.replace(/'/g, "''");
}

function listZipEntries(xlsxPath) {
  const script = [
    "Add-Type -AssemblyName System.IO.Compression.FileSystem",
    `$z = [IO.Compression.ZipFile]::OpenRead('${psQuote(path.resolve(xlsxPath))}')`,
    "$entries = $z.Entries | ForEach-Object {",
    "  [PSCustomObject]@{",
    "    path = $_.FullName",
    "    uncompressedBytes = [int64]$_.Length",
    "    compressedBytes = [int64]$_.CompressedLength",
    "    lastWriteTimeUtc = $_.LastWriteTime.ToUniversalTime().ToString('o')",
    "  }",
    "}",
    "$z.Dispose()",
    "$entries | ConvertTo-Json -Compress -Depth 4",
  ].join("\n");

  const raw = execFileSync(
    "powershell",
    ["-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script],
    { encoding: "utf8", maxBuffer: 64 * 1024 * 1024 }
  ).trim();

  if (!raw) return [];
  const parsed = JSON.parse(raw);
  return Array.isArray(parsed) ? parsed : [parsed];
}

function extractZip(xlsxPath, destDir) {
  if (fs.existsSync(destDir)) {
    fs.rmSync(destDir, { recursive: true, force: true });
  }
  fs.mkdirSync(destDir, { recursive: true });
  const script = [
    "Add-Type -AssemblyName System.IO.Compression.FileSystem",
    `[IO.Compression.ZipFile]::ExtractToDirectory('${psQuote(path.resolve(xlsxPath))}', '${psQuote(path.resolve(destDir))}')`,
  ].join("\n");
  execFileSync("powershell", ["-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script]);
}

function validateXmlFile(filePath) {
  const script = [
    `$p = '${psQuote(path.resolve(filePath))}'`,
    "try {",
    "  $c = [IO.File]::ReadAllText($p)",
    "  [void][xml]$c",
    "  'OK'",
    "} catch {",
    "  'FAIL:' + $_.Exception.Message",
    "}",
  ].join("\n");
  const out = execFileSync(
    "powershell",
    ["-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script],
    { encoding: "utf8" }
  ).trim();
  return out.startsWith("OK")
    ? { ok: true }
    : { ok: false, error: out.replace(/^FAIL:/, "").trim() };
}

/** Latin1 preserves byte-aligned OOXML for Cyrillic / UTF-8 hybrid Commander exports. */
function readText(filePath) {
  return fs.readFileSync(filePath, "latin1");
}

function regexCount(text, pattern) {
  const source = pattern instanceof RegExp ? pattern.source : pattern;
  const re = new RegExp(source, "g");
  return (text.match(re) || []).length;
}

function extractDimension(text) {
  const m = text.match(/<dimension\s+ref="([^"]+)"/);
  return m ? m[1] : null;
}

function extractXmlHead(text, maxChars = 480) {
  const normalized = text.replace(/\r?\n/g, " ").trim();
  return normalized.length <= maxChars
    ? normalized
    : `${normalized.slice(0, maxChars)}…`;
}

function analyzeWorksheetXml(filePath, relPath) {
  const text = readText(filePath);
  const markers = {};
  for (const name of WORKSHEET_MARKERS) {
    markers[name] = regexCount(text, name);
  }
  return {
    path: relPath.replace(/\\/g, "/"),
    uncompressedBytes: fs.statSync(filePath).size,
    dimensionRef: extractDimension(text),
    rowElementCount: regexCount(text, /<row\s/),
    cellElementCount: regexCount(text, /<c\s/),
    inlineStringCells: regexCount(text, /t="str"/),
    sharedStringCells: regexCount(text, /t="s"/),
    markers,
    xmlHead: extractXmlHead(text, 480),
  };
}

function walkXmlFiles(rootDir, baseDir = rootDir) {
  const results = [];
  if (!fs.existsSync(rootDir)) return results;
  for (const ent of fs.readdirSync(rootDir, { withFileTypes: true })) {
    const full = path.join(rootDir, ent.name);
    if (ent.isDirectory()) {
      results.push(...walkXmlFiles(full, baseDir));
    } else if (ent.name.endsWith(".xml")) {
      const rel = path.relative(baseDir, full);
      results.push({ full, rel });
    }
  }
  return results;
}

function buildStructureIndex(xlsxPath, label, extractDir) {
  const generatedAt = new Date().toISOString();
  const entries = listZipEntries(xlsxPath).map((e) => ({
    path: (e.path || "").replace(/\\/g, "/"),
    uncompressedBytes: e.uncompressedBytes,
    compressedBytes: e.compressedBytes,
    lastWriteTimeUtc: e.lastWriteTimeUtc,
  }));

  entries.sort((a, b) => a.path.localeCompare(b.path));

  extractZip(xlsxPath, extractDir);

  const xmlValidation = [];
  for (const { full, rel } of walkXmlFiles(extractDir)) {
    const v = validateXmlFile(full);
    xmlValidation.push({
      path: rel.replace(/\\/g, "/"),
      parseOk: v.ok,
      error: v.error || null,
    });
  }

  const worksheets = [];
  const wsDir = path.join(extractDir, "xl", "worksheets");
  if (fs.existsSync(wsDir)) {
    for (const f of fs.readdirSync(wsDir).filter((n) => n.endsWith(".xml"))) {
      worksheets.push(analyzeWorksheetXml(path.join(wsDir, f), `xl/worksheets/${f}`));
    }
    worksheets.sort((a, b) => a.path.localeCompare(b.path));
  }

  const criticalParts = {};
  const criticalPaths = [
    "[Content_Types].xml",
    "xl/workbook.xml",
    "xl/_rels/workbook.xml.rels",
    "xl/styles.xml",
    "xl/sharedStrings.xml",
    "_rels/.rels",
    "docProps/core.xml",
    "docProps/app.xml",
  ];
  for (const rel of criticalPaths) {
    const full = path.join(extractDir, rel);
    criticalParts[rel] = fs.existsSync(full)
      ? { present: true, bytes: fs.statSync(full).size }
      : { present: false, bytes: 0 };
  }

  return {
    version: "xlsx-structure-index-v0",
    label,
    sourceFile: path.resolve(xlsxPath),
    generatedAt,
    zipEntryCount: entries.length,
    totalUncompressedBytes: entries.reduce((s, e) => s + e.uncompressedBytes, 0),
    entries,
    criticalParts,
    worksheets,
    xmlValidation,
    xmlValidationSummary: {
      total: xmlValidation.length,
      parseOk: xmlValidation.filter((x) => x.parseOk).length,
      parseFailed: xmlValidation.filter((x) => !x.parseOk).length,
    },
  };
}

function compareIndexes(templateIndex, generatedIndex) {
  const tplPaths = new Set(templateIndex.entries.map((e) => e.path));
  const genPaths = new Set(generatedIndex.entries.map((e) => e.path));

  const isRealEntry = (p) => p && !p.endsWith("/");
  const onlyInTemplate = [...tplPaths]
    .filter((p) => isRealEntry(p) && !genPaths.has(p))
    .sort();
  const onlyInGenerated = [...genPaths]
    .filter((p) => isRealEntry(p) && !tplPaths.has(p))
    .sort();

  const genByPath = Object.fromEntries(
    generatedIndex.entries.map((e) => [e.path, e])
  );
  const tplByPath = Object.fromEntries(
    templateIndex.entries.map((e) => [e.path, e])
  );

  const sizeDeltas = [];
  for (const p of [...tplPaths].filter((p) => genPaths.has(p))) {
    const delta = genByPath[p].uncompressedBytes - tplByPath[p].uncompressedBytes;
    if (delta !== 0) {
      sizeDeltas.push({
        path: p,
        templateBytes: tplByPath[p].uncompressedBytes,
        generatedBytes: genByPath[p].uncompressedBytes,
        deltaBytes: delta,
      });
    }
  }
  sizeDeltas.sort((a, b) => Math.abs(b.deltaBytes) - Math.abs(a.deltaBytes));

  const worksheetComparison = [];
  const tplWs = Object.fromEntries(
    templateIndex.worksheets.map((w) => [w.path, w])
  );
  for (const gw of generatedIndex.worksheets) {
    const tw = tplWs[gw.path];
    if (!tw) continue;
    worksheetComparison.push({
      path: gw.path,
      dimensionTemplate: tw.dimensionRef,
      dimensionGenerated: gw.dimensionRef,
      dimensionChanged: tw.dimensionRef !== gw.dimensionRef,
      cellCountTemplate: tw.cellElementCount,
      cellCountGenerated: gw.cellElementCount,
      cellCountDelta: gw.cellElementCount - tw.cellElementCount,
      rowCountTemplate: tw.rowElementCount,
      rowCountGenerated: gw.rowElementCount,
      inlineStringCellsTemplate: tw.inlineStringCells,
      sharedStringCellsGenerated: gw.sharedStringCells,
      ignoredErrorsTemplate: tw.markers.ignoredErrors,
      ignoredErrorsGenerated: gw.markers.ignoredErrors,
    });
  }

  return {
    onlyInTemplate,
    onlyInGenerated,
    sizeDeltasTop: sizeDeltas.slice(0, 20),
    worksheetComparison,
    sharedStringsAdded: generatedIndex.criticalParts["xl/sharedStrings.xml"]?.present === true &&
      templateIndex.criticalParts["xl/sharedStrings.xml"]?.present !== true,
  };
}

function printSummary(comparison, templateIndex, generatedIndex) {
  console.log("\n--- ORCA OOXML Forensics v0 — SUMMARY ---\n");
  console.log(`Template ZIP entries:  ${templateIndex.zipEntryCount}`);
  console.log(`Generated ZIP entries: ${generatedIndex.zipEntryCount}`);
  console.log(`Only in generated:     ${comparison.onlyInGenerated.join(", ") || "(none)"}`);
  console.log(`sharedStrings added:   ${comparison.sharedStringsAdded}`);
  console.log("\nTop size deltas (uncompressed):");
  for (const d of comparison.sizeDeltasTop.slice(0, 8)) {
    console.log(
      `  ${d.path}: ${d.templateBytes} → ${d.generatedBytes} (${d.deltaBytes >= 0 ? "+" : ""}${d.deltaBytes})`
    );
  }
  console.log("\nWorksheet forensics:");
  for (const w of comparison.worksheetComparison) {
    console.log(`  ${w.path}`);
    console.log(
      `    dimension: ${w.dimensionTemplate} → ${w.dimensionGenerated}${w.dimensionChanged ? " CHANGED" : ""}`
    );
    console.log(
      `    cells: ${w.cellCountTemplate} → ${w.cellCountGenerated} (Δ ${w.cellCountDelta})`
    );
    console.log(
      `    strings: inline ${w.inlineStringCellsTemplate} → shared-index ${w.sharedStringCellsGenerated}`
    );
    console.log(
      `    ignoredErrors: ${w.ignoredErrorsTemplate} → ${w.ignoredErrorsGenerated}`
    );
  }
  console.log(
    `\nXML parse: template ${templateIndex.xmlValidationSummary.parseOk}/${templateIndex.xmlValidationSummary.total} ok` +
      ` | generated ${generatedIndex.xmlValidationSummary.parseOk}/${generatedIndex.xmlValidationSummary.total} ok`
  );
  console.log(
    "\nSee ooxml-diff-report-v0.md and ooxml-risk-analysis-v0.md for interpretation."
  );
}

function main() {
  const templatePath = path.resolve(process.argv[2] || DEFAULT_TEMPLATE);
  const generatedPath = path.resolve(process.argv[3] || DEFAULT_GENERATED);

  if (!fs.existsSync(templatePath)) {
    console.error(`Template not found: ${templatePath}`);
    process.exit(1);
  }
  if (!fs.existsSync(generatedPath)) {
    console.error(`Generated workbook not found: ${generatedPath}`);
    console.error("Run export.js --template-fill first.");
    process.exit(1);
  }

  const tmpBase = path.join(os.tmpdir(), `orca-ooxml-forensics-${process.pid}`);
  const tplExtract = path.join(tmpBase, "template");
  const genExtract = path.join(tmpBase, "generated");

  console.log("Building template structure index...");
  const templateIndex = buildStructureIndex(
    templatePath,
    "commander-template-v0",
    tplExtract
  );
  console.log("Building generated structure index...");
  const generatedIndex = buildStructureIndex(
    generatedPath,
    "template-fill-draft",
    genExtract
  );

  const comparison = compareIndexes(templateIndex, generatedIndex);

  fs.writeFileSync(OUT_TEMPLATE_INDEX, JSON.stringify(templateIndex, null, 2), "utf8");
  fs.writeFileSync(OUT_GENERATED_INDEX, JSON.stringify(generatedIndex, null, 2), "utf8");

  const comparisonPath = path.join(ROOT, "ooxml-comparison-v0.json");
  fs.writeFileSync(
    comparisonPath,
    JSON.stringify(
      {
        version: "ooxml-comparison-v0",
        generatedAt: new Date().toISOString(),
        templateFile: templatePath,
        generatedFile: generatedPath,
        comparison,
      },
      null,
      2
    ),
    "utf8"
  );

  printSummary(comparison, templateIndex, generatedIndex);
  console.log(`\nWrote: ${OUT_TEMPLATE_INDEX}`);
  console.log(`Wrote: ${OUT_GENERATED_INDEX}`);
  console.log(`Wrote: ${comparisonPath}`);

  try {
    fs.rmSync(tmpBase, { recursive: true, force: true });
  } catch {
    /* ignore */
  }
}

if (require.main === module) {
  const args = process.argv.slice(2);
  if (args.includes("-h") || args.includes("--help")) usage();
  main();
}

module.exports = {
  buildStructureIndex,
  compareIndexes,
  listZipEntries,
  analyzeWorksheetXml,
};
