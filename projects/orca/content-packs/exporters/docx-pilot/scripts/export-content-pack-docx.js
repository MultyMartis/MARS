#!/usr/bin/env node
"use strict";

/**
 * ORCA DOCX Export Pilot v1
 * Human-triggered, local-only. NOT a service, daemon, queue, or orchestration.
 */

const fs = require("fs");
const path = require("path");
const { Document, Packer, HeadingLevel } = require("docx");

const { parsePackFile } = require("./pack-parser");
const { renderCover } = require("./render-cover");
const { renderSection, renderPpcContinuity, renderSeoContinuity } = require("./render-section");
const { renderSafeUnknown } = require("./render-safe-unknown");
const { renderFactoryNotes } = require("./render-factory-notes");
const { renderApprovals } = require("./render-approvals");

const PILOT_ROOT = path.resolve(__dirname, "..");
const DEFAULT_INPUT = path.join(
  PILOT_ROOT,
  "..",
  "..",
  "examples",
  "triumph-manipulyator-5-tonn-pack-v0.md"
);
const DEFAULT_OUTPUT = path.join(
  PILOT_ROOT,
  "output",
  "triumph-manipulyator-5-tonn-pack-v1.docx"
);

const EXPORTER_LABEL = "ORCA DOCX Export Pilot v1";

function usage() {
  console.error(
    `${EXPORTER_LABEL}\n\n` +
      `Usage: node export-content-pack-docx.js [input.md] [output.docx]\n\n` +
      `Defaults:\n` +
      `  input:  ../../examples/triumph-manipulyator-5-tonn-pack-v0.md\n` +
      `  output: ../output/triumph-manipulyator-5-tonn-pack-v1.docx\n\n` +
      `Human-triggered only. No automatic approvals. Exit 0 on success, 1 on error.`
  );
  process.exit(1);
}

function buildExportMeta(pack) {
  const now = new Date();
  return {
    exportVersion: "v1",
    exportId: `orca-docx-${pack.meta.pack_id || "pack"}-${now.toISOString().slice(0, 10)}`,
    generatedAt: now.toISOString(),
    exportedBy: process.env.ORCA_EXPORTED_BY || "human-operator (local)",
  };
}

async function main() {
  const args = process.argv.slice(2);
  if (args.includes("-h") || args.includes("--help")) usage();

  const inputPath = path.resolve(args[0] || DEFAULT_INPUT);
  const outputPath = path.resolve(args[1] || DEFAULT_OUTPUT);

  if (!fs.existsSync(inputPath)) {
    console.error(`[ERROR] Input pack not found: ${inputPath}`);
    process.exit(1);
  }

  console.log(`\n--- ${EXPORTER_LABEL} ---`);
  console.log(`Input:  ${inputPath}`);
  console.log(`Output: ${outputPath}`);

  const pack = parsePackFile(inputPath);
  const exportMeta = buildExportMeta(pack);

  if (pack.sections.length < 10) {
    console.warn(
      `[WARN] Expected 10 sections, parsed ${pack.sections.length}. Export continues — verify output.`
    );
  }

  const children = [];

  children.push(...renderCover(pack, exportMeta));
  children.push(...renderPpcContinuity(pack));
  children.push(...renderSeoContinuity(pack));

  for (const section of pack.sections) {
    children.push(...renderSection(section, pack));
  }

  children.push(...renderSafeUnknown(pack));
  children.push(...renderFactoryNotes(pack));
  children.push(...renderApprovals(pack, exportMeta));

  const doc = new Document({
    creator: "ORCA DOCX Pilot",
    title: `ORCA Export — ${pack.meta.pack_id || "content-pack"}`,
    description: "Operational content pack export for Website Factory handoff",
    styles: {
      default: {
        document: {
          run: { font: "Calibri", size: 22 },
        },
        heading1: {
          run: { size: 32, bold: true, color: "1A1A2E" },
          paragraph: { spacing: { before: 240, after: 120 } },
        },
        heading2: {
          run: { size: 28, bold: true, color: "1A1A2E" },
          paragraph: { spacing: { before: 200, after: 100 } },
        },
        heading3: {
          run: { size: 24, bold: true },
          paragraph: { spacing: { before: 160, after: 80 } },
        },
      },
    },
    sections: [
      {
        properties: {
          page: {
            margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
          },
        },
        children,
      },
    ],
  });

  const buffer = await Packer.toBuffer(doc);
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, buffer);

  console.log(`\n[OK] DOCX written (${buffer.length} bytes)`);
  console.log(`Sections exported: ${pack.sections.length}`);
  console.log(`SAFE UNKNOWN items: ${pack.safeUnknown.length}+`);
  console.log(`Semantic lock: ${pack.meta.semantic_lock || "active"}`);
  console.log("\nOperator: open DOCX → run validation/export-checklist-v1.md → sign off manually.\n");
}

main().catch((err) => {
  console.error(`[ERROR] ${err.message}`);
  if (process.env.DEBUG) console.error(err.stack);
  process.exit(1);
});
