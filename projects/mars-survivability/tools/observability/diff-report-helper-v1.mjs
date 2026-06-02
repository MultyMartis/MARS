#!/usr/bin/env node
/**
 * MARS Survivability — Diff Report Helper v1
 *
 * READ-ONLY. Parses git diff --stat or path lists. Does NOT run git or modify files.
 *
 * Usage:
 *   git diff --stat | node diff-report-helper-v1.mjs
 *   node diff-report-helper-v1.mjs --file examples/diff-stat-example.txt
 *   node diff-report-helper-v1.mjs --paths "a,b,c" [--json]
 */

import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const REGISTRY_PATH = join(__dirname, "..", "validator", "rules", "validator-rules-registry-v1.json");

const DANGEROUS_CLASSES = [
  { id: "DC-01", pattern: /^governance\//, label: "P0 governance" },
  { id: "DC-02", pattern: /^registry\//, label: "P0 registry" },
  { id: "DC-03", pattern: /^AGENTS\.md$/, label: "Root agent contract" },
  { id: "DC-04", pattern: /^\.cursorrules$/, label: "Cursor rules" },
  { id: "DC-05", pattern: /^web-gpt-sources\//, label: "Legacy pack" },
  { id: "DC-06", pattern: /^workspaces\/_snapshots\//, label: "Snapshot store" },
  { id: "DC-07", pattern: /^projects\/orca\/ppc\/triumph-manipulator\/schema\//, label: "Campaign schema SoT" },
  { id: "DC-08", pattern: /^shared\/assets\//, label: "Shared assets" },
];

function printUsage() {
  console.error(`Usage:
  git diff --stat | node diff-report-helper-v1.mjs [--json]
  node diff-report-helper-v1.mjs --file "<path>" [--json]
  node diff-report-helper-v1.mjs --paths "path1,path2" [--json]
`);
}

function loadProtectedPrefixes() {
  const registry = JSON.parse(readFileSync(REGISTRY_PATH, "utf8"));
  return (registry.protected_paths || []).map((z) => ({
    id: z.id,
    prefix: z.prefix.replace(/\\/g, "/"),
    tier: z.tier,
    zone: z.zone,
  }));
}

function normalizePath(p) {
  return p.trim().replace(/\\/g, "/").replace(/^\.\//, "");
}

function parseDiffStat(text) {
  const files = [];
  for (const line of text.split("\n")) {
    const m = line.match(/^\s*(.+?)\s+\|\s+(\d+)/);
    if (m) {
      files.push({ path: normalizePath(m[1]), changes: parseInt(m[2], 10) });
    }
  }
  const summary = text.match(/(\d+)\s+files?\s+changed/);
  return {
    files,
    totalFiles: summary ? parseInt(summary[1], 10) : files.length,
  };
}

function extractWorkspaceRoot(p) {
  const m = p.match(/^workspaces\/([^/]+)/);
  return m ? `workspaces/${m[1]}` : null;
}

function analyze(paths, protectedPrefixes) {
  const findings = [];
  const touchedZones = new Set();
  const protectedHits = [];
  const dangerousClasses = [];
  const workspaceRoots = new Set();

  for (const raw of paths) {
    const p = normalizePath(raw);
    if (!p) continue;

    const ws = extractWorkspaceRoot(p);
    if (ws) workspaceRoots.add(ws);

    for (const zone of protectedPrefixes) {
      if (p.startsWith(zone.prefix) || p === zone.prefix.replace(/\/$/, "")) {
        touchedZones.add(zone.prefix);
        protectedHits.push({ path: p, zone: zone.prefix, tier: zone.tier, id: zone.id });
      }
    }

    for (const dc of DANGEROUS_CLASSES) {
      if (dc.pattern.test(p)) {
        dangerousClasses.push({ path: p, class: dc.label, id: dc.id });
      }
    }
  }

  const fileCount = paths.length;
  let riskSummary = "low";
  const signals = [];

  if (workspaceRoots.size > 1) {
    signals.push("CROSS-WORKSPACE");
    findings.push({
      id: "DR-010",
      severity: "HIGH",
      message: `Multiple workspace roots touched: ${[...workspaceRoots].join(", ")}`,
    });
    riskSummary = "high";
  }

  if (fileCount > 15) {
    signals.push("WORKSPACE-EXPLOSION");
    findings.push({
      id: "DR-020",
      severity: "HIGH",
      message: `${fileCount} files changed — possible scope escape (threshold 15)`,
    });
    riskSummary = "high";
  } else if (fileCount > 8) {
    signals.push("SUSPICIOUS-SPREAD");
    findings.push({
      id: "DR-021",
      severity: "WARNING",
      message: `${fileCount} files changed — review against scope lock`,
    });
    if (riskSummary === "low") riskSummary = "medium";
  }

  if (protectedHits.length > 0) {
    signals.push("PROTECTED-ZONE-HIT");
    riskSummary = "high";
  }

  if (dangerousClasses.length > 0) {
    signals.push("DANGEROUS-CLASS");
    riskSummary = "high";
  }

  const projectsAndWorkspaces =
    paths.some((p) => p.startsWith("projects/")) &&
    paths.some((p) => p.startsWith("workspaces/"));
  if (projectsAndWorkspaces) {
    signals.push("DRIFT-SUSPICION");
    findings.push({
      id: "DR-030",
      severity: "WARNING",
      message: "Both projects/ and workspaces/ touched — lane contamination risk",
    });
    if (riskSummary === "low") riskSummary = "medium";
  }

  if (paths.some((p) => /^governance\/|^registry\//.test(p))) {
    signals.push("GOVERNANCE-DRIFT");
    findings.push({
      id: "DR-040",
      severity: "CRITICAL",
      message: "Governance/registry paths in diff — charter required",
    });
    riskSummary = "critical";
  }

  return {
    fileCount,
    touchedZones: [...touchedZones],
    protectedHits,
    dangerousClasses,
    workspaceRoots: [...workspaceRoots],
    signals,
    findings,
    riskSummary,
    driftSuspicion: signals.includes("DRIFT-SUSPICION") || signals.includes("GOVERNANCE-DRIFT"),
  };
}

async function readStdin() {
  const chunks = [];
  for await (const chunk of process.stdin) chunks.push(chunk);
  return Buffer.concat(chunks).toString("utf8");
}

async function main() {
  if (process.argv.includes("--help") || process.argv.includes("-h")) {
    printUsage();
    process.exit(0);
  }

  const json = process.argv.includes("--json");
  let paths = [];
  let source = "stdin";

  const fileIdx = process.argv.indexOf("--file");
  if (fileIdx !== -1) {
    const fp = process.argv[fileIdx + 1];
    const text = readFileSync(fp, "utf8");
    const parsed = parseDiffStat(text);
    paths = parsed.files.map((f) => f.path);
    source = `file:${fp}`;
  } else {
    const pathsIdx = process.argv.indexOf("--paths");
    if (pathsIdx !== -1) {
      paths = (process.argv[pathsIdx + 1] || "")
        .split(",")
        .map((s) => s.trim())
        .filter(Boolean);
      source = "paths";
    } else if (!process.stdin.isTTY) {
      const text = await readStdin();
      const parsed = parseDiffStat(text);
      paths = parsed.files.map((f) => f.path);
      source = "stdin";
    } else {
      printUsage();
      process.exit(3);
    }
  }

  let protectedPrefixes;
  try {
    protectedPrefixes = loadProtectedPrefixes();
  } catch (e) {
    console.error(e.message);
    process.exit(3);
  }

  const report = analyze(paths, protectedPrefixes);
  const payload = {
    timestamp: new Date().toISOString(),
    source,
    paths,
    ...report,
    tool: "diff-report-helper-v1.mjs",
    advisoryNote: "Read-only report — does not run git or rollback.",
  };

  if (json) {
    console.log(JSON.stringify(payload, null, 2));
  } else {
    console.log("=== Diff Report Helper v1 (read-only) ===\n");
    console.log(`Source: ${source}`);
    console.log(`Files: ${report.fileCount}`);
    console.log(`Risk summary: ${report.riskSummary}`);
    console.log(`Signals: ${report.signals.join(", ") || "(none)"}`);
    if (report.touchedZones.length) {
      console.log("\nTouched zones:");
      for (const z of report.touchedZones) console.log(`  - ${z}`);
    }
    if (report.protectedHits.length) {
      console.log("\nProtected zone hits:");
      for (const h of report.protectedHits) {
        console.log(`  - ${h.path} → ${h.zone} (${h.tier})`);
      }
    }
    if (report.findings.length) {
      console.log("\nFindings:");
      for (const f of report.findings) {
        console.log(`  [${f.id}] ${f.severity}: ${f.message}`);
      }
    }
    console.log("\n" + payload.advisoryNote);
  }

  process.exit(report.riskSummary === "critical" ? 2 : report.riskSummary === "high" ? 1 : 0);
}

main();
