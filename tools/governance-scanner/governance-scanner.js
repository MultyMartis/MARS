#!/usr/bin/env node
/**
 * PILOT 01 — Governance phrase scan (read-only, explicit invocation).
 * Does not write files, persist state, watch the tree, or enforce policy.
 */

const fs = require("fs");
const path = require("path");

const DEFAULT_EXCLUDE_DIR_NAMES = new Set([
  ".git",
  "node_modules",
  "dist",
  "build",
  "out",
  ".next",
  "coverage",
]);

function parseArgs(argv) {
  const args = { root: process.cwd(), help: false };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--help" || a === "-h") args.help = true;
    else if (a === "--root" && argv[i + 1]) {
      args.root = path.resolve(argv[++i]);
    } else if (a.startsWith("--root=")) {
      args.root = path.resolve(a.slice("--root=".length));
    }
  }
  return args;
}

function printHelp() {
  const script = path.basename(__filename);
  process.stdout.write(
    [
      "Governance phrase scan (pilot) — read-only markdown triage helper.",
      "",
      "Usage:",
      `  node ${script} [--root <path>]`,
      "",
      "  --root <path>   Directory to scan (default: current working directory)",
      "  -h, --help      Show this help",
      "",
      "Behavior: walks the tree for *.md files, prints line hits, summary only.",
      "No file mutation, no background mode, no telemetry.",
      "",
    ].join("\n")
  );
}

function loadRules(scriptDir) {
  const rulesPath = path.join(scriptDir, "forbidden-phrases.json");
  const raw = fs.readFileSync(rulesPath, "utf8");
  const data = JSON.parse(raw);
  if (!Array.isArray(data)) {
    throw new Error("forbidden-phrases.json must be a JSON array");
  }
  return data.map((entry) => {
    if (!entry || typeof entry.phrase !== "string" || !entry.phrase.trim()) {
      throw new Error("Each rule needs a non-empty string phrase");
    }
    return {
      phrase: entry.phrase,
      severity: typeof entry.severity === "string" ? entry.severity : "medium",
      category: typeof entry.category === "string" ? entry.category : "uncategorized",
    };
  });
}

function collectMarkdownFiles(dir, acc, excludeDirNames) {
  let entries;
  try {
    entries = fs.readdirSync(dir, { withFileTypes: true });
  } catch (e) {
    return acc;
  }
  for (const ent of entries) {
    const full = path.join(dir, ent.name);
    if (ent.isDirectory()) {
      if (excludeDirNames.has(ent.name)) continue;
      collectMarkdownFiles(full, acc, excludeDirNames);
    } else if (ent.isFile() && ent.name.toLowerCase().endsWith(".md")) {
      acc.push(full);
    }
  }
  return acc;
}

function findLineMatches(line, rules) {
  const lower = line.toLowerCase();
  const hits = [];
  for (const rule of rules) {
    const needle = rule.phrase.toLowerCase();
    let start = 0;
    let idx = lower.indexOf(needle, start);
    while (idx !== -1) {
      hits.push({ rule, index: idx });
      start = idx + needle.length;
      idx = lower.indexOf(needle, start);
    }
  }
  hits.sort((a, b) => a.index - b.index);
  return hits;
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help) {
    printHelp();
    process.exit(0);
  }

  const scriptDir = path.dirname(fs.realpathSync(__filename));
  const rules = loadRules(scriptDir);

  if (!fs.existsSync(args.root) || !fs.statSync(args.root).isDirectory()) {
    process.stderr.write(`Error: root is not a directory: ${args.root}\n`);
    process.exit(2);
  }

  const files = collectMarkdownFiles(args.root, [], DEFAULT_EXCLUDE_DIR_NAMES);
  files.sort((a, b) => a.localeCompare(b));

  let totalMatches = 0;
  const bySeverity = {};

  for (const file of files) {
    let content;
    try {
      content = fs.readFileSync(file, "utf8");
    } catch {
      continue;
    }
    const lines = content.split(/\r?\n/);
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      const matches = findLineMatches(line, rules);
      if (!matches.length) continue;
      for (const m of matches) {
        totalMatches++;
        const sev = m.rule.severity;
        bySeverity[sev] = (bySeverity[sev] || 0) + 1;
        const rel = path.relative(args.root, file) || path.basename(file);
        process.stdout.write(
          [
            rel,
            `line ${i + 1}`,
            `phrase: ${m.rule.phrase}`,
            `severity: ${sev}`,
            `category: ${m.rule.category}`,
            "",
          ].join(" | ") + "\n"
        );
      }
    }
  }

  process.stdout.write("\n--- summary ---\n");
  process.stdout.write(`root: ${args.root}\n`);
  process.stdout.write(`markdown files scanned: ${files.length}\n`);
  process.stdout.write(`match lines reported: ${totalMatches}\n`);
  const sevKeys = Object.keys(bySeverity).sort();
  if (sevKeys.length) {
    for (const k of sevKeys) {
      process.stdout.write(`  ${k}: ${bySeverity[k]}\n`);
    }
  } else {
    process.stdout.write("  (no phrase hits)\n");
  }
  process.stdout.write(
    "\nNote: output is triage-only; context may be quotes, negation, or governance definitions.\n"
  );
}

main();
