#!/usr/bin/env node
/**
 * PILOT 02 — Registry consistency hints (read-only, explicit invocation).
 *
 * Non-goals: registry sync, auto-fix, enforcement engine, background monitoring,
 * orchestration, hidden state, mutation of scanned files.
 */

const fs = require("fs");
const path = require("path");

const SCRIPT_VERSION = "0.1.0";

function parseArgs(argv) {
  const args = {
    root: process.cwd(),
    help: false,
    dryRun: false,
    scanJsJson: false,
  };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--help" || a === "-h") args.help = true;
    else if (a === "--dry-run") args.dryRun = true;
    else if (a === "--scan-js-json") args.scanJsJson = true;
    else if (a === "--root" && argv[i + 1]) args.root = path.resolve(argv[++i]);
    else if (a.startsWith("--root=")) args.root = path.resolve(a.slice("--root=".length));
  }
  return args;
}

function printHelp() {
  const script = path.basename(__filename);
  process.stdout.write(
    [
      "Registry consistency hints (PILOT 02) — read-only, stdout-only triage helper.",
      "",
      "Usage:",
      `  node ${script} [--root <path>] [--scan-js-json] [--dry-run]`,
      "",
      "  --root <path>      Directory to scan (default: current working directory)",
      "  --scan-js-json     Include .js and .json files in addition to .md",
      "  --dry-run          List scan roots and file counts only (no rule evaluation)",
      "  -h, --help         Show this help",
      "",
      "Behavior: walks the tree, applies heuristic rules from registry-rules.json, prints hints.",
      "No file writes, no caches, no watchers, no daemons, no auto-fix.",
      "",
    ].join("\n")
  );
}

function loadRules(scriptDir) {
  const rulesPath = path.join(scriptDir, "registry-rules.json");
  const raw = fs.readFileSync(rulesPath, "utf8");
  const data = JSON.parse(raw);
  if (!data || typeof data !== "object") throw new Error("registry-rules.json must be an object");
  const exclude = new Set(
    Array.isArray(data.excludeDirNames) ? data.excludeDirNames : []
  );
  return {
    version: data.version,
    description: data.description,
    excludeDirNames: exclude,
    lineHints: Array.isArray(data.lineHints) ? data.lineHints : [],
    fileHints: Array.isArray(data.fileHints) ? data.fileHints : [],
    collectors: Array.isArray(data.collectors) ? data.collectors : [],
  };
}

function normalizeRel(rel) {
  return rel.split(path.sep).join("/");
}

function pathMatchesSubstrings(relNorm, substrings) {
  if (!substrings || !substrings.length) return true;
  return substrings.every((s) => relNorm.includes(s));
}

function collectFiles(root, extensions, excludeDirNames, acc) {
  let entries;
  try {
    entries = fs.readdirSync(root, { withFileTypes: true });
  } catch {
    return acc;
  }
  for (const ent of entries) {
    const full = path.join(root, ent.name);
    if (ent.isDirectory()) {
      if (excludeDirNames.has(ent.name)) continue;
      collectFiles(full, extensions, excludeDirNames, acc);
    } else if (ent.isFile()) {
      const ext = path.extname(ent.name).toLowerCase();
      if (extensions.has(ext)) acc.push(full);
    }
  }
  return acc;
}

function buildExtensionSet(scanJsJson) {
  const s = new Set([".md"]);
  if (scanJsJson) {
    s.add(".js");
    s.add(".json");
  }
  return s;
}

function compileRegex(entry, requireGlobal) {
  const flags = (entry.flags || "") + (requireGlobal ? "g" : "");
  try {
    return new RegExp(entry.pattern, flags);
  } catch (e) {
    throw new Error(`Invalid regex for rule ${entry.id || "?"}: ${e.message}`);
  }
}

function formatHit(rel, lineNo, issueType, ruleId, severity, matched, hint) {
  const parts = [
    rel,
    lineNo != null ? `line ${lineNo}` : "line —",
    `type: ${issueType}`,
    `rule: ${ruleId}`,
    `severity: ${severity}`,
    `matched: ${matched}`,
  ];
  if (hint) parts.push(`hint: ${hint}`);
  return parts.join(" | ") + "\n";
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help) {
    printHelp();
    process.exit(0);
  }

  const scriptDir = path.dirname(fs.realpathSync(__filename));
  const rules = loadRules(scriptDir);
  const excludeDirNames = rules.excludeDirNames;
  for (const d of [
    ".git",
    "node_modules",
    "dist",
    "build",
    "out",
    ".next",
    "coverage",
  ]) {
    excludeDirNames.add(d);
  }

  if (!fs.existsSync(args.root) || !fs.statSync(args.root).isDirectory()) {
    process.stderr.write(`Error: root is not a directory: ${args.root}\n`);
    process.exit(2);
  }

  const extensions = buildExtensionSet(args.scanJsJson);
  const files = collectFiles(args.root, extensions, excludeDirNames, []);
  files.sort((a, b) => a.localeCompare(b));

  process.stdout.write(
    `registry-checker ${SCRIPT_VERSION} | rules ${rules.version || "?"} | root: ${args.root}\n`
  );
  process.stdout.write(
    `extensions: ${[...extensions].sort().join(", ")} | files: ${files.length}\n\n`
  );

  if (args.dryRun) {
    process.stdout.write("--- dry-run (no rules evaluated) ---\n");
    process.stdout.write(`SAFE UNKNOWN: rule outcomes not computed in dry-run mode.\n`);
    process.exit(0);
  }

  /** @type {Map<string, { files: Set<string>, hits: Array<{rel: string, line: number, value: string}> }>} */
  const collectorBuckets = new Map();

  for (const c of rules.collectors) {
    collectorBuckets.set(c.id, new Map());
  }

  let lineHintCount = 0;
  let fileHintCount = 0;
  const bySeverity = {};

  function bumpSeverity(sev) {
    bySeverity[sev] = (bySeverity[sev] || 0) + 1;
  }

  for (const abs of files) {
    const rel = normalizeRel(path.relative(args.root, abs) || path.basename(abs));
    let content;
    try {
      content = fs.readFileSync(abs, "utf8");
    } catch {
      continue;
    }
    const ext = path.extname(abs).toLowerCase();

    for (const fh of rules.fileHints) {
      const exts = fh.extensions || [".md"];
      if (!exts.includes(ext)) continue;
      if (!fh.absPathMustContain && (!fh.pathSubstrings || !fh.pathSubstrings.length)) continue;
      const relNorm = normalizeRel(rel);
      const absNorm = abs.split(path.sep).join("/");
      if (fh.absPathMustContain) {
        if (!absNorm.includes(fh.absPathMustContain.replace(/\\/g, "/"))) continue;
      } else if (!pathMatchesSubstrings(relNorm, fh.pathSubstrings)) {
        continue;
      }
      const skipRe = fh.bodyMustNotMatch
        ? new RegExp(fh.bodyMustNotMatch, fh.flags || "i")
        : null;
      if (skipRe && skipRe.test(content)) continue;
      process.stdout.write(
        formatHit(rel, null, fh.issueType || "file_hint", fh.id, fh.severity || "info", "(file)", fh.hint)
      );
      fileHintCount++;
      bumpSeverity(fh.severity || "info");
    }

    const lines = content.split(/\r?\n/);

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      const lineNo = i + 1;

      for (const lh of rules.lineHints) {
        const exts = lh.extensions || [".md"];
        if (!exts.includes(ext)) continue;
        const re = compileRegex(lh, false);
        const m = line.match(re);
        if (!m) continue;
        if (lh.lineMustNotMatch) {
          const neg = new RegExp(lh.lineMustNotMatch, lh.flags || "i");
          if (neg.test(line)) continue;
        }
        const matched = m[0] || line.trim().slice(0, 120);
        process.stdout.write(
          formatHit(rel, lineNo, lh.issueType || "line_hint", lh.id, lh.severity || "low", matched, lh.hint)
        );
        lineHintCount++;
        bumpSeverity(lh.severity || "low");
      }

      for (const c of rules.collectors) {
        const exts = c.extensions || [".md"];
        if (!exts.includes(ext)) continue;
        const gFlags = (c.flags || "") + "g";
        let cre;
        try {
          cre = new RegExp(c.pattern, gFlags);
        } catch (e) {
          throw new Error(`Collector ${c.id}: ${e.message}`);
        }
        let match;
        while ((match = cre.exec(line)) !== null) {
          const capIdx = typeof c.captureGroup === "number" ? c.captureGroup : 1;
          const value = match[capIdx];
          if (!value) continue;
          const idMap = collectorBuckets.get(c.id);
          if (!idMap) continue;
          if (!idMap.has(value)) {
            idMap.set(value, { files: new Set(), hits: [] });
          }
          const bucket = idMap.get(value);
          bucket.files.add(rel);
          bucket.hits.push({ rel, line: lineNo, value });
        }
      }
    }
  }

  let collectorReportCount = 0;
  for (const c of rules.collectors) {
    const idMap = collectorBuckets.get(c.id);
    if (!idMap) continue;
    const minFiles = c.minDistinctFiles || 2;
    for (const [value, data] of idMap.entries()) {
      if (data.files.size < minFiles) continue;
      const fileList = [...data.files].sort().join("; ");
      process.stdout.write(
        formatHit(
          "(aggregate)",
          null,
          c.issueType || "collector",
          c.id,
          c.severity || "low",
          value,
          `${c.hint || ""} | files: ${fileList} | hits: ${data.hits.length}`
        )
      );
      collectorReportCount++;
      bumpSeverity(c.severity || "low");
      const maxDetail = 12;
      for (let i = 0; i < Math.min(data.hits.length, maxDetail); i++) {
        const h = data.hits[i];
        process.stdout.write(
          formatHit(h.rel, h.line, c.issueType || "collector", c.id, c.severity || "low", h.value, "")
        );
        bumpSeverity(c.severity || "low");
      }
      if (data.hits.length > maxDetail) {
        process.stdout.write(
          `(aggregate) | line — | type: ${c.issueType} | rule: ${c.id} | severity: ${c.severity} | matched: (${data.hits.length - maxDetail} more hits omitted)\n`
        );
      }
    }
  }

  process.stdout.write("\n--- summary ---\n");
  process.stdout.write(`root: ${args.root}\n`);
  process.stdout.write(`files scanned: ${files.length}\n`);
  process.stdout.write(`line hints: ${lineHintCount}\n`);
  process.stdout.write(`file hints: ${fileHintCount}\n`);
  process.stdout.write(`collector keys reported: ${collectorReportCount}\n`);
  const sevKeys = Object.keys(bySeverity).sort();
  if (sevKeys.length) {
    process.stdout.write("by severity:\n");
    for (const k of sevKeys) {
      process.stdout.write(`  ${k}: ${bySeverity[k]}\n`);
    }
  }
  process.stdout.write(
    "\nNote: hints are heuristic; human interpretation required. False positives expected.\n"
  );
  process.stdout.write("SAFE UNKNOWN: this script does not prove drift, uniqueness, or canonical truth.\n");
}

main();
