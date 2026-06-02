#!/usr/bin/env node
/**
 * MARS Survivability — Scope Analyzer v1
 *
 * ADVISORY ONLY. Does NOT modify files or block operations.
 *
 * Usage:
 *   node scope-analyzer-v1.mjs --paths "path1,path2" [--json]
 *   node scope-analyzer-v1.mjs --path "path1" --path "path2"
 */

import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const REGISTRY_PATH = join(__dirname, "..", "validator", "rules", "validator-rules-registry-v1.json");

const LABELS = ["SAFE", "RISKY", "CROSS-WORKSPACE", "PROTECTED-ZONE-HIT"];

function printUsage() {
  console.error(`Usage:
  node scope-analyzer-v1.mjs --paths "a,b,c"
  node scope-analyzer-v1.mjs --path "a" --path "b" [--json]

Outputs advisory labels (one or more per analysis):
  SAFE | RISKY | CROSS-WORKSPACE | PROTECTED-ZONE-HIT

Does NOT forbid operations — operator decides.
`);
}

function parseArgs(argv) {
  const paths = [];
  let json = false;
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--help" || a === "-h") {
      return { help: true };
    }
    if (a === "--json") {
      json = true;
      continue;
    }
    if (a === "--paths" || a === "-p") {
      const raw = argv[++i] ?? "";
      paths.push(...raw.split(",").map((s) => s.trim()).filter(Boolean));
      continue;
    }
    if (a === "--path") {
      paths.push((argv[++i] ?? "").trim());
      continue;
    }
    console.error(`Unknown argument: ${a}`);
    return { error: true };
  }
  return { paths, json };
}

function loadProtectedPaths() {
  const registry = JSON.parse(readFileSync(REGISTRY_PATH, "utf8"));
  return (registry.protected_paths || []).sort(
    (a, b) => b.prefix.length - a.prefix.length
  );
}

function normalizePath(input) {
  let p = input.trim().replace(/\\/g, "/");
  const markers = ["C:/AI MARS/", "c:/ai mars/"];
  for (const m of markers) {
    if (p.toLowerCase().startsWith(m)) p = p.slice(m.length);
  }
  if (p.startsWith("./")) p = p.slice(2);
  return p.replace(/\/$/, "");
}

function extractWorkspaceRoot(normPath) {
  const m = normPath.match(/^workspaces\/([^/]+)/);
  return m ? `workspaces/${m[1]}` : null;
}

function matchProtectedZone(normPath, protectedPaths) {
  const hits = [];
  for (const zone of protectedPaths) {
    const prefix = zone.prefix.replace(/\/$/, "");
    if (normPath === prefix || normPath.startsWith(zone.prefix)) {
      hits.push({
        id: zone.id,
        prefix: zone.prefix,
        zone: zone.zone,
        tier: zone.tier,
      });
    }
  }
  return hits;
}

function analyzePaths(paths, protectedPaths) {
  const normalized = paths.map(normalizePath).filter(Boolean);
  if (normalized.length === 0) {
    return { error: "At least one path required" };
  }

  const labels = new Set();
  const details = [];
  const protectedHits = [];
  const workspaceRoots = new Set();

  for (const p of normalized) {
    const zones = matchProtectedZone(p, protectedPaths);
    if (zones.length) {
      labels.add("PROTECTED-ZONE-HIT");
      protectedHits.push({ path: p, zones });
      details.push(`${p}: protected zone ${zones.map((z) => z.prefix).join(", ")}`);
    }

    const ws = extractWorkspaceRoot(p);
    if (ws) workspaceRoots.add(ws);

    if (p.startsWith("workspaces/") && !p.includes("_sandbox") && p.includes("/src")) {
      labels.add("RISKY");
      details.push(`${p}: production workspace src/ path`);
    } else if (p.startsWith("projects/") && !p.startsWith("projects/mars-survivability/")) {
      labels.add("RISKY");
      details.push(`${p}: cross-project pack (P1)`);
    } else if (/governance|registry|web-gpt-sources|AGENTS\.md|\.cursorrules/.test(p)) {
      if (!labels.has("PROTECTED-ZONE-HIT")) labels.add("PROTECTED-ZONE-HIT");
    } else if (!zones.length && !p.startsWith("workspaces/")) {
      labels.add("SAFE");
      details.push(`${p}: no protected zone prefix match`);
    }
  }

  if (workspaceRoots.size > 1) {
    labels.add("CROSS-WORKSPACE");
    details.push(
      `Multiple workspace roots: ${[...workspaceRoots].join(", ")} — contamination risk`
    );
  }

  if (normalized.some((p) => p === "workspaces" || p === "projects")) {
    labels.add("RISKY");
    details.push("Broad tree root in scope — narrow to subdirectory");
  }

  if (labels.size === 0 || (labels.size === 1 && labels.has("SAFE"))) {
    if (!labels.has("PROTECTED-ZONE-HIT") && !labels.has("RISKY") && !labels.has("CROSS-WORKSPACE")) {
      labels.add("SAFE");
    }
  }

  if (labels.has("PROTECTED-ZONE-HIT") || labels.has("CROSS-WORKSPACE")) {
    labels.delete("SAFE");
  } else if (labels.has("RISKY") && !labels.has("SAFE")) {
    labels.add("RISKY");
  }

  const primary =
    labels.has("PROTECTED-ZONE-HIT")
      ? "PROTECTED-ZONE-HIT"
      : labels.has("CROSS-WORKSPACE")
        ? "CROSS-WORKSPACE"
        : labels.has("RISKY")
          ? "RISKY"
          : "SAFE";

  return {
    primary,
    labels: [...labels],
    paths: normalized,
    protectedHits,
    workspaceRoots: [...workspaceRoots],
    details,
    recommendations: buildRecommendations(labels, protectedHits, workspaceRoots),
    safeUnknown: [],
  };
}

function buildRecommendations(labels, protectedHits, workspaceRoots) {
  const rec = [];
  if (labels.has("PROTECTED-ZONE-HIT")) {
    rec.push("Narrow scope or move task to Lane B with explicit path allowlist.");
    rec.push("Run scoped-operation-validator-v1.mjs on planned shell commands.");
  }
  if (labels.has("CROSS-WORKSPACE")) {
    rec.push("Split into separate tasks — one workspace per AGENT session.");
  }
  if (labels.has("RISKY")) {
    rec.push("Run snapshot-helper-v1.mjs before first mutation (MEDIUM+ risk).");
  }
  if (labels.has("SAFE") && workspaceRoots.size === 1) {
    rec.push("Scope appears bounded — still require scope lock in task header.");
  }
  if (protectedHits.some((h) => h.zones.some((z) => z.prefix.includes("_snapshots")))) {
    rec.push("Snapshot store paths: AGENT delete forbidden — human only.");
  }
  return rec;
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help) {
    printUsage();
    process.exit(0);
  }
  if (args.error || !args.paths?.length) {
    printUsage();
    process.exit(3);
  }

  let protectedPaths;
  try {
    protectedPaths = loadProtectedPaths();
  } catch (err) {
    console.error(`Failed to load registry: ${err.message}`);
    process.exit(3);
  }

  const result = analyzePaths(args.paths, protectedPaths);
  if (result.error) {
    console.error(result.error);
    process.exit(3);
  }

  const payload = {
    timestamp: new Date().toISOString(),
    input: { paths: args.paths },
    primary: result.primary,
    labels: result.labels,
    paths: result.paths,
    protectedHits: result.protectedHits,
    workspaceRoots: result.workspaceRoots,
    details: result.details,
    recommendations: result.recommendations,
    safeUnknown: result.safeUnknown,
    helper: "scope-analyzer-v1.mjs",
    advisoryNote: "Labels are advisory — operator authority is absolute.",
  };

  if (args.json) {
    console.log(JSON.stringify(payload, null, 2));
    process.exit(0);
  }

  console.log("=== MARS Scope Analyzer v1 (advisory) ===\n");
  console.log(`Primary: ${result.primary}`);
  console.log(`Labels: ${result.labels.join(", ")}`);
  console.log("\nPaths analyzed:");
  for (const p of result.paths) console.log(`  - ${p}`);
  if (result.workspaceRoots.length) {
    console.log("\nWorkspace roots:");
    for (const w of result.workspaceRoots) console.log(`  - ${w}`);
  }
  console.log("\nDetails:");
  for (const d of result.details) console.log(`  - ${d}`);
  console.log("\nRecommendations:");
  for (const r of result.recommendations) console.log(`  - ${r}`);
  console.log("\n" + payload.advisoryNote);
  process.exit(0);
}

main();
