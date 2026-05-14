#!/usr/bin/env node
/**
 * PILOT 03 — Markdown link hints (read-only, explicit invocation).
 *
 * Non-goals: link integrity enforcement, auto-fix, sync, caches, watchers,
 * daemons, orchestration, hidden state, mutation of scanned files.
 */

const fs = require("fs");
const path = require("path");

const SCRIPT_VERSION = "0.1.0";

/** @typedef {{ root: string, help: boolean, dryRun: boolean, checkAnchors: boolean }} CliArgs */

function parseArgs(argv) {
  /** @type {CliArgs} */
  const args = {
    root: process.cwd(),
    help: false,
    dryRun: false,
    checkAnchors: false,
  };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--help" || a === "-h") args.help = true;
    else if (a === "--dry-run") args.dryRun = true;
    else if (a === "--check-anchors") args.checkAnchors = true;
    else if (a === "--root" && argv[i + 1]) args.root = path.resolve(argv[++i]);
    else if (a.startsWith("--root=")) args.root = path.resolve(a.slice("--root=".length));
  }
  return args;
}

function printHelp() {
  const script = path.basename(__filename);
  process.stdout.write(
    [
      "Markdown link hints (PILOT 03) — read-only, stdout-only local helper.",
      "",
      "Usage:",
      `  node ${script} [--root <path>] [--dry-run] [--check-anchors]`,
      "",
      "  --root <path>       Directory tree to scan (default: cwd)",
      "  --dry-run           List root, config, and file counts only (no link checks)",
      "  --check-anchors     Heuristic #fragment checks vs heading-derived slugs",
      "  -h, --help          Show this help",
      "",
      "Behavior: walks markdown files, reports relative local link targets that appear missing,",
      "optional anchor hints. No writes, no caches, no watchers, no auto-fix.",
      "",
    ].join("\n")
  );
}

function loadConfig(scriptDir) {
  const p = path.join(scriptDir, "validator-config.json");
  const raw = fs.readFileSync(p, "utf8");
  const data = JSON.parse(raw);
  if (!data || typeof data !== "object") throw new Error("validator-config.json must be an object");
  const exclude = new Set(
    Array.isArray(data.excludeDirNames) ? data.excludeDirNames : []
  );
  const mdExts = new Set(
    (Array.isArray(data.markdownExtensions) ? data.markdownExtensions : [".md"]).map((x) =>
      String(x).toLowerCase()
    )
  );
  const sev = data.severityByIssueType && typeof data.severityByIssueType === "object"
    ? data.severityByIssueType
    : {};
  return {
    version: data.version,
    experimental: data.experimental,
    markdownExtensions: mdExts,
    inferMarkdownExtension: Boolean(data.inferMarkdownExtension),
    excludeDirNames: exclude,
    severityByIssueType: sev,
  };
}

function normalizeRel(rel) {
  return rel.split(path.sep).join("/");
}

function collectMarkdownFiles(root, mdExtensions, excludeDirNames, acc) {
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
      collectMarkdownFiles(full, mdExtensions, excludeDirNames, acc);
    } else if (ent.isFile()) {
      const ext = path.extname(ent.name).toLowerCase();
      if (mdExtensions.has(ext)) acc.push(full);
    }
  }
  return acc;
}

function stripMarkdownLinkTitle(raw) {
  let t = raw.trim();
  if (t.startsWith("<") && t.endsWith(">")) t = t.slice(1, -1).trim();
  t = t.replace(/\s+["'][^"']*["']\s*$/, "").trim();
  return t;
}

function isNonRelativeLocalTarget(t) {
  const lower = t.toLowerCase();
  if (lower.startsWith("http://") || lower.startsWith("https://")) return true;
  if (lower.startsWith("mailto:") || lower.startsWith("tel:") || lower.startsWith("ftp:")) return true;
  if (lower.startsWith("javascript:") || lower.startsWith("data:") || lower.startsWith("vscode:"))
    return true;
  if (t.startsWith("//")) return true;
  if (/^[a-zA-Z]:[\\/]/.test(t)) return true;
  return false;
}

function splitPathAndFragment(t) {
  const hash = t.indexOf("#");
  if (hash === -1) return { pathname: t, fragment: "" };
  return {
    pathname: t.slice(0, hash),
    fragment: t.slice(hash + 1),
  };
}

function decodePathname(p) {
  try {
    return decodeURIComponent(p);
  } catch {
    return p;
  }
}

function slugifyHeading(text) {
  return text
    .trim()
    .toLowerCase()
    .replace(/[`"'’]/g, "")
    .replace(/[^\p{L}\p{N}\s-]/gu, "")
    .trim()
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-");
}

function extractHeadingSlugs(content) {
  const slugs = new Set();
  const re = /^(#{1,6})\s+(.+?)\s*$/gm;
  let m;
  while ((m = re.exec(content)) !== null) {
    const title = m[2].replace(/\s+#+\s*$/, "").trim();
    if (!title) continue;
    slugs.add(slugifyHeading(title));
    const noPunct = title.replace(/[^\p{L}\p{N}\s-]/gu, "").trim();
    if (noPunct && noPunct !== title) slugs.add(slugifyHeading(noPunct));
  }
  return slugs;
}

function resolveLocalTarget(fromFileAbs, pathnameRaw, inferMd) {
  const decoded = decodePathname(pathnameRaw);
  if (!decoded) return { resolved: null };
  const fromDir = path.dirname(fromFileAbs);
  const candidate = path.normalize(path.join(fromDir, decoded));

  if (fs.existsSync(candidate)) {
    const st = fs.statSync(candidate);
    if (st.isFile()) return { resolved: candidate };
    if (st.isDirectory()) return { resolved: null, directory: true };
  }

  if (inferMd && path.extname(candidate) === "") {
    const withMd = candidate + ".md";
    if (fs.existsSync(withMd) && fs.statSync(withMd).isFile()) return { resolved: withMd };
    const withMarkdown = candidate + ".markdown";
    if (fs.existsSync(withMarkdown) && fs.statSync(withMarkdown).isFile())
      return { resolved: withMarkdown };
  }

  return { resolved: null };
}

function severityFor(cfg, issueType) {
  return cfg.severityByIssueType[issueType] || "low";
}

function formatIssue(relFile, lineNo, broken, issueType, severity) {
  return `${relFile} | line ${lineNo} | link: ${broken} | type: ${issueType} | severity: ${severity}\n`;
}

function extractParenLinkTargets(line) {
  const out = [];
  const re = /!?\[[^\]]*\]\(([^)]+)\)/g;
  let m;
  while ((m = re.exec(line)) !== null) {
    out.push(stripMarkdownLinkTitle(m[1]));
  }
  return out;
}

function extractRefDefTarget(line) {
  const trimmed = line.trimStart();
  const m = trimmed.match(/^\[[^\]]+\]:\s+(?:<([^>\s]+)>|(\S+))/);
  if (!m) return null;
  const raw = m[1] || m[2];
  return stripMarkdownLinkTitle(raw);
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help) {
    printHelp();
    process.exit(0);
  }

  const scriptDir = path.dirname(fs.realpathSync(__filename));
  const cfg = loadConfig(scriptDir);

  for (const d of [".git", "node_modules", "dist", "build", "out", ".next", "coverage"]) {
    cfg.excludeDirNames.add(d);
  }

  if (!fs.existsSync(args.root) || !fs.statSync(args.root).isDirectory()) {
    process.stderr.write(`Error: root is not a directory: ${args.root}\n`);
    process.exit(2);
  }

  const files = collectMarkdownFiles(args.root, cfg.markdownExtensions, cfg.excludeDirNames, []);
  files.sort((a, b) => a.localeCompare(b));

  process.stdout.write(
    `markdown-link-validator ${SCRIPT_VERSION} | config ${cfg.version || "?"} | root: ${args.root}\n`
  );
  process.stdout.write(
    `anchors: ${args.checkAnchors ? "on (heuristic)" : "off"} | markdown files: ${files.length}\n`
  );
  if (cfg.experimental) process.stdout.write(`status: ${cfg.experimental}\n`);
  process.stdout.write("\n");

  if (args.dryRun) {
    process.stdout.write("--- dry-run (no link checks) ---\n");
    process.stdout.write(`excluded dir names: ${[...cfg.excludeDirNames].sort().join(", ")}\n`);
    process.stdout.write(`infer .md when link has no extension: ${cfg.inferMarkdownExtension}\n`);
    process.stdout.write("\nSAFE UNKNOWN: link outcomes not computed in dry-run mode.\n");
    process.exit(0);
  }

  /** @type {{ issueType: string, severity: string }[]} */
  const issues = [];
  const byType = {};

  function record(rel, lineNo, broken, issueType) {
    const sev = severityFor(cfg, issueType);
    issues.push({ issueType, severity: sev });
    byType[issueType] = (byType[issueType] || 0) + 1;
    process.stdout.write(formatIssue(rel, lineNo, broken, issueType, sev));
  }

  const headingCache = new Map();

  function slugsForFile(abs) {
    if (headingCache.has(abs)) return headingCache.get(abs);
    let content;
    try {
      content = fs.readFileSync(abs, "utf8");
    } catch {
      headingCache.set(abs, null);
      return null;
    }
    const slugs = extractHeadingSlugs(content);
    headingCache.set(abs, slugs);
    return slugs;
  }

  for (const abs of files) {
    const rel = normalizeRel(path.relative(args.root, abs) || path.basename(abs));
    let content;
    try {
      content = fs.readFileSync(abs, "utf8");
    } catch {
      continue;
    }
    const lines = content.split(/\r?\n/);

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      const lineNo = i + 1;

      const refT = extractRefDefTarget(line);
      const targets = [...extractParenLinkTargets(line)];
      if (refT) targets.push(refT);

      for (const rawTarget of targets) {
        if (!rawTarget || !rawTarget.trim()) continue;
        const t = rawTarget.trim();
        if (isNonRelativeLocalTarget(t)) continue;

        const { pathname, fragment } = splitPathAndFragment(t);

        if (!pathname && !fragment) {
          continue;
        }

        if (!pathname && fragment) {
          if (args.checkAnchors) {
            const slugs = slugsForFile(abs);
            if (slugs && !slugs.has(slugifyHeading(decodeURIComponent(fragment)))) {
              record(rel, lineNo, t, "missing_same_file_anchor");
            }
          }
          if (fragment.includes("  ")) {
            record(rel, lineNo, t, "suspicious_fragment");
          }
          continue;
        }

        if (pathname.startsWith("/")) {
          continue;
        }

        const decodedPath = decodePathname(pathname);
        const { resolved, directory } = resolveLocalTarget(abs, pathname, cfg.inferMarkdownExtension);

        if (directory) {
          continue;
        }

        if (!resolved) {
          const issueType =
            cfg.inferMarkdownExtension && path.extname(decodedPath) === ""
              ? "missing_target_file_inferred_md"
              : "missing_target_file";
          record(rel, lineNo, t, issueType);
          continue;
        }

        if (args.checkAnchors && fragment) {
          const slugs = slugsForFile(resolved);
          const frag = decodeURIComponent(fragment);
          if (slugs && !slugs.has(slugifyHeading(frag))) {
            record(rel, lineNo, t, "missing_cross_file_anchor");
          }
        }

        if (fragment && /[^a-zA-Z0-9_-]/.test(fragment) && args.checkAnchors) {
          record(rel, lineNo, t, "suspicious_fragment");
        }
      }
    }
  }

  process.stdout.write("\n--- summary ---\n");
  process.stdout.write(`root: ${args.root}\n`);
  process.stdout.write(`files scanned: ${files.length}\n`);
  process.stdout.write(`issues reported: ${issues.length}\n`);
  const types = Object.keys(byType).sort();
  if (types.length) {
    process.stdout.write("by issue type:\n");
    for (const k of types) {
      process.stdout.write(`  ${k}: ${byType[k]}\n`);
    }
  }
  const bySev = {};
  for (const x of issues) {
    bySev[x.severity] = (bySev[x.severity] || 0) + 1;
  }
  const sevKeys = Object.keys(bySev).sort();
  if (sevKeys.length) {
    process.stdout.write("by severity:\n");
    for (const k of sevKeys) {
      process.stdout.write(`  ${k}: ${bySev[k]}\n`);
    }
  }
  process.stdout.write(
    "\nNote: hints are heuristic; human interpretation required. False positives and misses are expected.\n"
  );
  process.stdout.write(
    "SAFE UNKNOWN: this script does not prove repository-wide link integrity, canonical paths, or anchor truth.\n"
  );
}

main();
