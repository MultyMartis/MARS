"use strict";

/**
 * ORCA XLSX ZIP Patch v0
 * Byte-preserving transport: clone template ZIP, replace ONLY xl/worksheets/sheet1.xml.
 * Uses .NET ZipFile (same family as ooxml-forensics.js) — local Windows operator path.
 * NOT a production OOXML engine.
 */

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const { execFileSync } = require("child_process");

const SHEET1_ENTRY = "xl/worksheets/sheet1.xml";
const PRESERVE_VERIFY_ENTRIES = [
  "xl/worksheets/sheet2.xml",
  "xl/worksheets/sheet3.xml",
  "xl/_rels/workbook.xml.rels",
  "xl/workbook.xml",
  "xl/styles.xml",
  "[Content_Types].xml",
];

class ZipPatchError extends Error {
  constructor(code, message, details = []) {
    super(message);
    this.name = "ZipPatchError";
    this.code = code;
    this.details = details;
  }
}

function psQuote(p) {
  return String(p).replace(/'/g, "''");
}

function sha256Buffer(buf) {
  return crypto.createHash("sha256").update(buf).digest("hex");
}

function readZipEntryBytes(xlsxPath, entryPath) {
  const script = [
    "Add-Type -AssemblyName System.IO.Compression.FileSystem",
    `$z = [IO.Compression.ZipFile]::OpenRead('${psQuote(path.resolve(xlsxPath))}')`,
    `$e = $z.GetEntry('${psQuote(entryPath)}')`,
    "if ($null -eq $e) { $z.Dispose(); throw 'ENTRY_NOT_FOUND' }",
    "$ms = New-Object IO.MemoryStream",
    "$s = $e.Open()",
    "$s.CopyTo($ms)",
    "$s.Close()",
    "$z.Dispose()",
    "[Convert]::ToBase64String($ms.ToArray())",
  ].join("\n");

  const b64 = execFileSync(
    "powershell",
    ["-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script],
    { encoding: "utf8", maxBuffer: 256 * 1024 * 1024 }
  ).trim();

  return Buffer.from(b64, "base64");
}

function readZipEntryUtf8(xlsxPath, entryPath) {
  const buf = readZipEntryBytes(xlsxPath, entryPath);
  return buf.toString("utf8");
}

/**
 * Clone template to output (binary), then replace one ZIP entry.
 * Other entries remain as stored in the cloned archive until ZipFile rewrite.
 */
function replaceZipEntry(xlsxPath, entryPath, contentUtf8) {
  const resolved = path.resolve(xlsxPath);
  const tmp = `${resolved}.sheet1-patch.tmp`;
  const xmlSidecar = path.join(path.dirname(resolved), `.patch-xml-${process.pid}.xml`);
  fs.writeFileSync(xmlSidecar, contentUtf8, "utf8");

  const script = [
    "Add-Type -AssemblyName System.IO.Compression",
    "Add-Type -AssemblyName System.IO.Compression.FileSystem",
    `$src = '${psQuote(resolved)}'`,
    `$tmp = '${psQuote(tmp)}'`,
    `$entry = '${psQuote(entryPath)}'`,
    `$xmlFile = '${psQuote(path.resolve(xmlSidecar))}'`,
    "if (Test-Path $tmp) { Remove-Item -Force $tmp }",
    "[IO.File]::Copy($src, $tmp, $true)",
    `$z = [IO.Compression.ZipFile]::Open($tmp, [IO.Compression.ZipArchiveMode]::Update)`,
    "$old = $z.GetEntry($entry)",
    "if ($null -ne $old) { $old.Delete() }",
    "$ne = $z.CreateEntry($entry, [IO.Compression.CompressionLevel]::Optimal)",
    "$sw = New-Object IO.StreamWriter($ne.Open(), (New-Object Text.UTF8Encoding $false))",
    "$xml = [IO.File]::ReadAllText($xmlFile, (New-Object Text.UTF8Encoding $false))",
    "$sw.Write($xml)",
    "$sw.Close()",
    "$z.Dispose()",
    "[IO.File]::Copy($tmp, $src, $true)",
    "Remove-Item -Force $tmp",
  ].join("\n");

  try {
    execFileSync(
      "powershell",
      ["-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script],
      { encoding: "utf8", maxBuffer: 64 * 1024 * 1024 }
    );
  } finally {
    try {
      fs.unlinkSync(xmlSidecar);
    } catch {
      /* ignore */
    }
  }
}

function cloneTemplateBinary(templatePath, outputPath) {
  const tpl = path.resolve(templatePath);
  const out = path.resolve(outputPath);
  if (!fs.existsSync(tpl)) {
    throw new ZipPatchError("TEMPLATE_NOT_FOUND", `Template not found: ${tpl}`);
  }
  fs.mkdirSync(path.dirname(out), { recursive: true });
  fs.copyFileSync(tpl, out);
  return out;
}

/**
 * @param {string} templatePath
 * @param {string} outputPath
 * @param {string} sheet1XmlUtf8
 */
function patchSheet1InWorkbook(templatePath, outputPath, sheet1XmlUtf8) {
  const tplStatBefore = fs.statSync(path.resolve(templatePath));
  const out = cloneTemplateBinary(templatePath, outputPath);
  const tplStatAfter = fs.statSync(path.resolve(templatePath));

  if (
    tplStatBefore.mtimeMs !== tplStatAfter.mtimeMs ||
    tplStatBefore.size !== tplStatAfter.size
  ) {
    throw new ZipPatchError(
      "TEMPLATE_SOURCE_MUTATED",
      "Original template file changed during export — aborting"
    );
  }

  replaceZipEntry(out, SHEET1_ENTRY, sheet1XmlUtf8);

  return {
    outputPath: out,
    sheet1Entry: SHEET1_ENTRY,
    templateSource: path.resolve(templatePath),
    templateUnmodified: true,
  };
}

/**
 * Compare SHA-256 of selected ZIP entries between template clone baseline and patched output.
 * Expects byte-identical parts except sheet1.xml.
 */
function verifyPreservedEntries(templatePath, patchedPath, entries = PRESERVE_VERIFY_ENTRIES) {
  const results = [];
  let allMatch = true;

  for (const entry of entries) {
    let tplBuf;
    let outBuf;
    try {
      tplBuf = readZipEntryBytes(templatePath, entry);
      outBuf = readZipEntryBytes(patchedPath, entry);
    } catch (err) {
      results.push({
        entry,
        match: false,
        error: err.message,
      });
      allMatch = false;
      continue;
    }

    const tplHash = sha256Buffer(tplBuf);
    const outHash = sha256Buffer(outBuf);
    const match = tplHash === outHash;
    if (!match) allMatch = false;

    results.push({
      entry,
      match,
      templateBytes: tplBuf.length,
      patchedBytes: outBuf.length,
      templateSha256: tplHash,
      patchedSha256: outHash,
    });
  }

  let sheet1Changed = false;
  try {
    const t1 = sha256Buffer(readZipEntryBytes(templatePath, SHEET1_ENTRY));
    const t2 = sha256Buffer(readZipEntryBytes(patchedPath, SHEET1_ENTRY));
    sheet1Changed = t1 !== t2;
  } catch {
    sheet1Changed = true;
  }

  const sharedStringsInPatched = entryExists(patchedPath, "xl/sharedStrings.xml");

  return {
    ok: allMatch && sheet1Changed && !sharedStringsInPatched,
    preservedEntries: results,
    sheet1Changed,
    sharedStringsIntroduced: sharedStringsInPatched,
  };
}

function entryExists(xlsxPath, entryPath) {
  const script = [
    "Add-Type -AssemblyName System.IO.Compression.FileSystem",
    `$z = [IO.Compression.ZipFile]::OpenRead('${psQuote(path.resolve(xlsxPath))}')`,
    `$e = $z.GetEntry('${psQuote(entryPath)}')`,
    "$z.Dispose()",
    "if ($null -eq $e) { 'false' } else { 'true' }",
  ].join("\n");
  const out = execFileSync(
    "powershell",
    ["-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script],
    { encoding: "utf8" }
  ).trim();
  return out === "true";
}

module.exports = {
  ZipPatchError,
  SHEET1_ENTRY,
  PRESERVE_VERIFY_ENTRIES,
  readZipEntryBytes,
  readZipEntryUtf8,
  cloneTemplateBinary,
  patchSheet1InWorkbook,
  verifyPreservedEntries,
  replaceZipEntry,
};
