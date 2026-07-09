#!/usr/bin/env node
/**
 * MetaBOT Developer — read-only n8n workflow exporter (GET-only).
 *
 * Modes:
 *   --dry-run      (default) list allowlisted workflows by exact name
 *   --report-only  fetch and print summary, no writes
 *   --export       fetch, write raw (gitignored) + sanitized evidence pack
 */

import { mkdirSync, writeFileSync, readFileSync, existsSync } from 'node:fs';
import { resolve, dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

import { resolveAllowlist, workflowNameToSlug } from './lib/allowlist.mjs';
import {
  loadCredentials,
  listWorkflows,
  getWorkflow,
} from './lib/n8n-api-client.mjs';
import { sanitizeWorkflow, scanForObviousSecrets } from './sanitize-workflow.mjs';
import { generateManifestDocs } from './lib/manifest.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = resolve(__dirname, '../..');
const REPO_ROOT = resolve(__dirname, '../../../..');

/**
 * @typedef {'dry-run' | 'report-only' | 'export'} RunMode
 */

/**
 * @returns {RunMode}
 */
function parseMode(argv) {
  if (argv.includes('--export')) return 'export';
  if (argv.includes('--report-only')) return 'report-only';
  return 'dry-run';
}

/**
 * @param {string[]} argv
 * @returns {string}
 */
function parseDate(argv) {
  const idx = argv.indexOf('--date');
  if (idx !== -1 && argv[idx + 1]) {
    const d = argv[idx + 1];
    if (!/^\d{4}-\d{2}-\d{2}$/.test(d)) {
      throw new Error(`Invalid --date format: ${d} (expected YYYY-MM-DD)`);
    }
    return d;
  }
  const now = new Date();
  const yyyy = now.getFullYear();
  const mm = String(now.getMonth() + 1).padStart(2, '0');
  const dd = String(now.getDate()).padStart(2, '0');
  return `${yyyy}-${mm}-${dd}`;
}

/**
 * @param {string[]} argv
 * @returns {string | undefined}
 */
function parseNames(argv) {
  const idx = argv.indexOf('--names');
  if (idx !== -1) return argv[idx + 1];
  return undefined;
}

/**
 * @param {string} rawDir
 */
function assertRawFolderGitignored(rawDir) {
  const gitignorePath = resolve(REPO_ROOT, '.gitignore');
  if (!existsSync(gitignorePath)) {
    throw new Error('.gitignore not found — cannot verify raw export path is ignored.');
  }
  const gitignore = readFileSync(gitignorePath, 'utf8');
  const normalizedRaw = rawDir.replace(/\\/g, '/');
  const repoRelative = normalizedRaw.includes('projects/metabot-seo-content-agent/raw')
    ? 'projects/metabot-seo-content-agent/raw/'
    : null;

  if (!repoRelative) {
    throw new Error(`Raw export path is outside expected raw folder: ${rawDir}`);
  }

  const ignored =
    gitignore.includes(repoRelative) ||
    gitignore.includes('projects/metabot-seo-content-agent/raw/');

  if (!ignored) {
    throw new Error(
      `STOP — raw folder is not gitignored: ${repoRelative}\n` +
        'Add projects/metabot-seo-content-agent/raw/ to .gitignore before writing raw exports.',
    );
  }
}

/**
 * @param {Array<{ id: string, name: string, active?: boolean }>} allWorkflows
 * @param {string[]} allowlist
 */
function matchAllowlisted(allWorkflows, allowlist) {
  const byName = new Map(allWorkflows.map((w) => [w.name, w]));
  /** @type {Array<{ name: string, id: string, active: boolean, found: boolean }>} */
  const results = [];

  for (const name of allowlist) {
    const hit = byName.get(name);
    results.push({
      name,
      id: hit?.id ?? '',
      active: Boolean(hit?.active),
      found: Boolean(hit),
    });
  }

  return results;
}

/**
 * @param {RunMode} mode
 * @param {Array<{ name: string, id: string, active: boolean, found: boolean }>} matches
 */
function printDryRunSummary(mode, matches) {
  console.log(`Mode: ${mode}`);
  console.log('Target workflows (exact name match):');
  console.log('');

  for (const m of matches) {
    const status = m.found ? `FOUND id=${m.id} active=${m.active}` : 'NOT FOUND';
    console.log(`  [${m.found ? 'OK' : 'MISS'}] ${m.name} — ${status}`);
  }

  const foundCount = matches.filter((m) => m.found).length;
  console.log('');
  console.log(`Summary: ${foundCount}/${matches.length} workflows matched.`);
}

async function main() {
  const argv = process.argv.slice(2);
  const mode = parseMode(argv);
  const date = parseDate(argv);
  const allowlist = resolveAllowlist(parseNames(argv));

  const rawDir = resolve(PROJECT_ROOT, `raw/live-export-${date}`);
  const evidenceDir = resolve(PROJECT_ROOT, `exports/live-v14-evidence/${date}`);

  console.log('MetaBOT n8n read-only exporter v1');
  console.log(`Project root: ${PROJECT_ROOT}`);
  console.log(`Allowlist (${allowlist.length}):`);
  for (const name of allowlist) console.log(`  - ${name}`);
  console.log('');

  let creds;
  try {
    creds = loadCredentials();
    console.log(`Credentials: loaded from ${creds.envPath}`);
    console.log(`API URL: ${creds.apiUrl}`);
    console.log('API key: <redacted>');
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    console.error(`Credential error: ${message}`);
    process.exitCode = 2;
    return;
  }

  let allWorkflows;
  try {
    allWorkflows = await listWorkflows(creds);
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    console.error(message);
    process.exitCode = 1;
    return;
  }

  const matches = matchAllowlisted(allWorkflows, allowlist);

  if (mode === 'dry-run') {
    printDryRunSummary(mode, matches);
    const missing = matches.filter((m) => !m.found);
    if (missing.length) process.exitCode = 1;
    return;
  }

  const foundMatches = matches.filter((m) => m.found);
  if (!foundMatches.length) {
    console.error('No allowlisted workflows found — aborting.');
    process.exitCode = 1;
    return;
  }

  /** @type {import('./lib/manifest.mjs').WorkflowExportRecord[]} */
  const exportRecords = [];

  for (const match of foundMatches) {
    let workflow;
    try {
      workflow = await getWorkflow(match.id, creds);
    } catch (err) {
      const message = err instanceof Error ? err.message : String(err);
      console.error(`Failed to fetch ${match.name}: ${message}`);
      process.exitCode = 1;
      return;
    }

    const { sanitized, stats } = sanitizeWorkflow(workflow);
    const slug = workflowNameToSlug(match.name);
    const sanitizedFile = `${slug}.sanitized.json`;

    if (mode === 'report-only') {
      const nodeCount = Array.isArray(sanitized?.nodes) ? sanitized.nodes.length : 0;
      console.log(`--- ${match.name} ---`);
      console.log(`  id: ${match.id}`);
      console.log(`  active: ${match.active}`);
      console.log(`  nodes: ${nodeCount}`);
      console.log(`  sanitization: credentials=${stats.credentialsRedacted} tokens=${stats.tokensRedacted} webhookIds=${stats.webhookIdsRedacted}`);
      console.log(`  risky patterns remaining: ${stats.riskyPatternsRemaining.length}`);
      console.log('');
      continue;
    }

    exportRecords.push({
      name: match.name,
      id: match.id,
      active: match.active,
      sanitized,
      stats,
      sanitizedFile,
    });
  }

  if (mode === 'report-only') {
    return;
  }

  // --export mode
  assertRawFolderGitignored(rawDir);
  mkdirSync(rawDir, { recursive: true });
  mkdirSync(evidenceDir, { recursive: true });

  for (const record of exportRecords) {
    const rawPath = join(rawDir, `${record.sanitizedFile.replace('.sanitized.json', '.raw.json')}`);
    const sanitizedPath = join(evidenceDir, record.sanitizedFile);

    // Re-fetch raw for write (already have sanitized from record.sanitized — write raw from unsanitized)
    const rawWorkflow = await getWorkflow(record.id, creds);
    writeFileSync(rawPath, JSON.stringify(rawWorkflow, null, 2), 'utf8');
    writeFileSync(sanitizedPath, JSON.stringify(record.sanitized, null, 2), 'utf8');

    console.log(`Wrote raw: ${rawPath}`);
    console.log(`Wrote sanitized: ${sanitizedPath}`);
  }

  /** @type {Array<{ file: string, pattern: string }>} */
  const securityFindings = [];
  let safeToCommit = true;

  for (const record of exportRecords) {
    const sanitizedPath = join(evidenceDir, record.sanitizedFile);
    const content = readFileSync(sanitizedPath, 'utf8');
    const scan = scanForObviousSecrets(content);
    if (!scan.safe) {
      safeToCommit = false;
      for (const finding of scan.findings) {
        securityFindings.push({ file: record.sanitizedFile, pattern: finding.pattern });
      }
    }
    if (record.stats.riskyPatternsRemaining.length) {
      safeToCommit = false;
    }
  }

  const manifestDocs = generateManifestDocs(exportRecords, {
    date,
    classification: 'LIVE_API_EXPORT',
    safeToCommit,
    securityFindings,
  });

  for (const [filename, content] of Object.entries(manifestDocs)) {
    const outPath = join(evidenceDir, filename);
    writeFileSync(outPath, content, 'utf8');
    console.log(`Wrote manifest: ${outPath}`);
  }

  console.log('');
  console.log(`Export complete. Evidence pack: ${evidenceDir}`);
  console.log(`Safe to commit: ${safeToCommit ? 'SAFE_TO_COMMIT' : 'NOT_SAFE_TO_COMMIT'}`);
  if (securityFindings.length) {
    console.log('Security scan flagged patterns — see SANITIZATION-REPORT.md');
    process.exitCode = 1;
  }
}

main().catch((err) => {
  console.error(err instanceof Error ? err.message : String(err));
  process.exitCode = 1;
});
