#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  CLI_MODES,
  COMMANDER_TEMPLATE_PATH,
  EXPLICIT_MODE_REQUIRED,
  PROJECT_ROOT,
  TASK_ALLOWED_MODES,
} from './constants.mjs';
import { loadAuthority } from './authority-loader.mjs';
import { createGuardContext } from './filesystem-guard.mjs';
import {
  buildAuthorityManifest,
  CORVONERO_FROZEN_AUTHORITY_SPEC,
  CORVONERO_MANIFEST_PATH,
  writeValidationReceipt,
} from './manifest-builder.mjs';
import { buildPayloads, validateTransport } from './payload-builder.mjs';
import { patchCommanderWorkbook } from './commander-patcher-adapter.mjs';
import { verifyOutput } from './output-verifier.mjs';
import { validateTemplate } from './template-validator.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

function parseArgs(argv) {
  const args = {
    mode: null,
    manifest: null,
    template: COMMANDER_TEMPLATE_PATH,
    outJson: null,
    outMd: null,
    payloadOut: null,
    output: null,
    help: false,
    skipVolumeCheck: false,
    useCorvoneroFrozen: false,
  };

  const rest = argv.slice(2);
  for (let i = 0; i < rest.length; i++) {
    const a = rest[i];
    if (a === '--help' || a === '-h') args.help = true;
    else if (a === '--manifest') args.manifest = rest[++i];
    else if (a === '--template') args.template = rest[++i];
    else if (a === '--out-json') args.outJson = rest[++i];
    else if (a === '--out-md') args.outMd = rest[++i];
    else if (a === '--payload-out') args.payloadOut = rest[++i];
    else if (a === '--output') args.output = rest[++i];
    else if (a === '--skip-volume-check') args.skipVolumeCheck = true;
    else if (a === '--corvonero-frozen') args.useCorvoneroFrozen = true;
    else if (CLI_MODES.includes(a)) args.mode = a;
    else if (!args.mode && !a.startsWith('-')) args.mode = a;
  }
  return args;
}

function formatMd(result) {
  const lines = [
    `# Commander Transport Validation`,
    ``,
    `**Status:** ${result.status}`,
    `**Validated at:** ${result.validated_at}`,
  ];
  if (result.stop_code) lines.push(`**Stop code:** ${result.stop_code}`);
  lines.push('', '## Violations', '');
  if (!result.violations?.length) lines.push('- (none)');
  else {
    for (const v of result.violations) {
      let line = `- **${v.code}**: ${v.message}`;
      if (v.group_id) line += ` (group: ${v.group_id})`;
      if (v.actual_phrase_count != null) {
        line += ` — ${v.actual_phrase_count} > ${v.maximum_phrase_count}`;
      }
      lines.push(line);
    }
  }
  if (result.warnings?.length) {
    lines.push('', '## Warnings', '');
    for (const w of result.warnings) {
      lines.push(`- **${w.code}**: ${w.message}`);
    }
  }
  return `${lines.join('\n')}\n`;
}

async function resolveManifest(args) {
  if (args.manifest) return path.resolve(args.manifest);
  if (args.useCorvoneroFrozen) {
    if (!fs.existsSync(CORVONERO_MANIFEST_PATH)) {
      const manifest = await buildAuthorityManifest(CORVONERO_FROZEN_AUTHORITY_SPEC);
      fs.mkdirSync(path.dirname(CORVONERO_MANIFEST_PATH), { recursive: true });
      fs.writeFileSync(CORVONERO_MANIFEST_PATH, `${JSON.stringify(manifest, null, 2)}\n`);
    }
    return CORVONERO_MANIFEST_PATH;
  }
  throw new Error('Manifest path required (--manifest or --corvonero-frozen)');
}

async function enrichLoadedAuthority(loaded) {
  const transportConfig = loaded.byRole.transport_config;
  if (!transportConfig) return loaded;

  const resolveRef = (refPath) => {
    if (!refPath) return null;
    const abs = path.resolve(refPath);
    return JSON.parse(fs.readFileSync(abs, 'utf8'));
  };

  if (transportConfig.bids_ref) {
    loaded.byRole.bids = resolveRef(transportConfig.bids_ref);
  }
  if (transportConfig.display_paths_ref) {
    loaded.byRole.display_paths = resolveRef(transportConfig.display_paths_ref);
  }
  if (transportConfig.group_negatives_ref) {
    loaded.byRole.group_negatives = resolveRef(transportConfig.group_negatives_ref);
  }
  if (transportConfig.bids) {
    loaded.byRole.bids = { campaign_bids: transportConfig.bids };
  }
  if (transportConfig.display_paths) {
    loaded.byRole.display_paths = transportConfig.display_paths;
  }
  if (transportConfig.group_negatives && !loaded.byRole.group_negatives) {
    loaded.byRole.group_negatives = transportConfig.group_negatives;
  }
  return loaded;
}

async function main() {
  const args = parseArgs(process.argv);

  if (args.help) {
    console.log(`Usage: node cli.mjs <mode> [options]

Modes: ${CLI_MODES.join(', ')}
Task-allowed: ${TASK_ALLOWED_MODES.join(', ')}

Options:
  --manifest <path>       Authority manifest JSON
  --corvonero-frozen      Use frozen Corvonero authority manifest
  --template <path>       Commander template XLSX
  --out-json <path>       Write validation JSON
  --out-md <path>         Write validation Markdown
  --payload-out <dir>     Write per-campaign payloads (build-payload only)
  --output <path>         Output XLSX (generate only — blocked in this task)
  --skip-volume-check     Test-only: skip AI WS volume check`);
    process.exit(0);
  }

  if (!args.mode) {
    console.error(EXPLICIT_MODE_REQUIRED);
    process.exit(2);
  }

  if (!CLI_MODES.includes(args.mode)) {
    console.error(`Unknown mode: ${args.mode}`);
    process.exit(2);
  }

  const guardOpts = { skipVolumeCheck: args.skipVolumeCheck };

  if (args.mode === 'generate' || args.mode === 'verify-output') {
    console.error(`Mode "${args.mode}" is not authorized in CT-1/CT-2 task scope`);
    process.exit(2);
  }

  createGuardContext(guardOpts);

  if (args.mode === 'validate' || args.mode === 'build-payload') {
    const manifestPath = await resolveManifest(args);
    let loaded = await loadAuthority(manifestPath, guardOpts);
    loaded = await enrichLoadedAuthority(loaded);

    const templateResult = await validateTemplate(args.template, guardOpts);
    const validation = validateTransport(loaded);

    const combined = {
      ...validation,
      template: templateResult.ok ? { ok: true, sha256: templateResult.sha256 } : templateResult,
      manifest_path: manifestPath,
    };

    const jsonOut = JSON.stringify(combined, null, 2);
    const mdOut = formatMd(combined);

    if (args.outJson) {
      const out = path.resolve(args.outJson);
      createGuardContext(guardOpts);
      writeValidationReceipt(combined, out);
    }
    if (args.outMd) {
      const out = path.resolve(args.outMd);
      fs.mkdirSync(path.dirname(out), { recursive: true });
      fs.writeFileSync(out, mdOut);
    }

    console.log(mdOut);

    if (args.mode === 'build-payload') {
      if (validation.status !== 'PASS') {
        console.error('build-payload blocked: validation failed');
        process.exit(1);
      }
      const payloads = buildPayloads(loaded, validation);
      if (args.payloadOut) {
        const dir = path.resolve(args.payloadOut);
        fs.mkdirSync(dir, { recursive: true });
        for (const p of payloads) {
          const file = path.join(dir, `payload-${p.campaign_id}.json`);
          fs.writeFileSync(file, `${JSON.stringify(p, null, 2)}\n`);
        }
        console.log(`Wrote ${payloads.length} payloads to ${dir}`);
      } else {
        console.log(JSON.stringify(payloads, null, 2));
      }
      process.exit(0);
    }

    process.exit(validation.status === 'PASS' ? 0 : 1);
  }
}

main().catch((err) => {
  if (err.errors) {
    console.error(JSON.stringify({ error: err.message, details: err.errors }, null, 2));
  } else {
    console.error(err.message || err);
  }
  process.exit(1);
});

export { parseArgs, formatMd, enrichLoadedAuthority };
