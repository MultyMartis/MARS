#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadContracts } from '../src/contract-loader.mjs';
import { buildConsumptionReport, consumptionReportMarkdown } from '../src/consumption-report.mjs';
import { runAdmissionIntegration } from '../src/admission-orchestrator.mjs';
import { validateRecordShape } from '../src/record-generator.mjs';
import { validateInvariants } from '../src/invariant-validator.mjs';
import { ensureDir, readJson, RUNTIME_ROOT, writeJson } from '../src/lib.mjs';
import {
  enforceLegacyBoundary,
  emitLegacyBlock,
  isDiagnosticContext,
  LIFECYCLE_AUTH_ENV,
} from '../../../../../mars-search-ppc-production/runtime/src/legacy-entry-boundary.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const DEFAULT_LOCK = path.join(RUNTIME_ROOT, 'config/orca-semantic-contract-runtime-lock-v1.json');
const DEFAULT_CONFIG = path.join(RUNTIME_ROOT, 'config/integration-config-v1.json');
const OUTPUT_DIR = path.join(RUNTIME_ROOT, 'output');
const REPORTS_DIR = path.join(RUNTIME_ROOT, 'reports');

function usage() {
  console.log(`ORCA Admission Integration CLI v1

Usage:
  node cli/orca-admission.mjs contracts:validate [--lock <path>]
  node cli/orca-admission.mjs contracts:report [--lock <path>] [--out <dir>]
  node cli/orca-admission.mjs record:validate <fixture-path>
  node cli/orca-admission.mjs integration:run <fixture-path> [--lock <path>] [--out <dir>] [--diagnostic]

Production Search PPC integration:run requires lifecycle gate via orca-ppc-gate.mjs.
Ungated integration:run is blocked unless --diagnostic is set (diagnostic output only).
`);
}

function parseArgs(argv) {
  const args = {
    command: null,
    positional: [],
    lock: DEFAULT_LOCK,
    out: OUTPUT_DIR,
    config: DEFAULT_CONFIG,
    diagnostic: false,
  };
  const rest = argv.slice(2);
  if (!rest.length) return args;
  args.command = rest[0];
  for (let i = 1; i < rest.length; i++) {
    if (rest[i] === '--lock') args.lock = path.resolve(rest[++i]);
    else if (rest[i] === '--out') args.out = path.resolve(rest[++i]);
    else if (rest[i] === '--config') args.config = path.resolve(rest[++i]);
    else if (rest[i] === '--diagnostic') args.diagnostic = true;
    else if (!rest[i].startsWith('--')) args.positional.push(path.resolve(rest[i]));
  }
  return args;
}

const DIAGNOSTIC_COMMANDS = new Set(['contracts:validate', 'contracts:report', 'record:validate']);

function guardProductionCommand(args) {
  if (DIAGNOSTIC_COMMANDS.has(args.command)) {
    return { allowed: true, mode: 'diagnostic_contract' };
  }
  if (args.command !== 'integration:run') {
    return { allowed: true, mode: 'non_production' };
  }

  const boundary = enforceLegacyBoundary({
    entryPointId: 'orca-admission',
    replacementKey: 'orca-admission',
    tool: 'orca-admission.mjs',
    requestedAction: 'integration:run',
    requestedStage: 'SPPC-05',
    searchPpcMode: true,
    isDiagnostic: args.diagnostic || isDiagnosticContext(),
    command: `node cli/orca-admission.mjs ${args.command}`,
  });

  if (!boundary.allowed) {
    emitLegacyBlock(boundary);
    process.exit(boundary.exit_code || 2);
  }

  if (boundary.mode === 'diagnostic') {
    process.env.MARS_SEARCH_PPC_DIAGNOSTIC = '1';
    if (!args.out.includes('diagnostic')) {
      args.out = path.join(RUNTIME_ROOT, 'output', 'diagnostic');
    }
  }

  return boundary;
}

async function main() {
  const args = parseArgs(process.argv);
  if (!args.command || args.command === '--help' || args.command === '-h') {
    usage();
    process.exit(args.command ? 0 : 1);
  }

  guardProductionCommand(args);

  ensureDir(args.out);
  ensureDir(REPORTS_DIR);

  const cmdMeta = `node cli/orca-admission.mjs ${args.command}${args.diagnostic ? ' --diagnostic' : ''}`;

  if (args.command === 'contracts:validate') {
    const result = loadContracts({ lockPath: args.lock });
    const report = buildConsumptionReport(result, { command: cmdMeta });
    const outJson = path.join(args.out, 'contract-validation-result.json');
    writeJson(outJson, report);
    console.log(JSON.stringify({ ok: result.ok, blocked: result.blocked, message: result.message, out: outJson }, null, 2));
    process.exit(result.ok ? 0 : 2);
  }

  if (args.command === 'contracts:report') {
    const result = loadContracts({ lockPath: args.lock });
    const report = buildConsumptionReport(result, { command: cmdMeta });
    const jsonPath = path.join(REPORTS_DIR, 'contract-consumption-report-v1.json');
    const mdPath = path.join(REPORTS_DIR, 'contract-consumption-report-v1.md');
    writeJson(jsonPath, report);
    fs.writeFileSync(mdPath, `${consumptionReportMarkdown(report)}\n`, 'utf8');
    console.log(JSON.stringify({ ok: result.ok, json: jsonPath, md: mdPath }, null, 2));
    process.exit(result.ok ? 0 : 2);
  }

  if (args.command === 'record:validate') {
    const fixturePath = args.positional[0];
    if (!fixturePath || !fs.existsSync(fixturePath)) {
      console.error('fixture path required');
      process.exit(1);
    }
    const record = readJson(fixturePath);
    const shapeErrors = validateRecordShape(record);
    const validation = validateInvariants(record, { contracts_consumed: true, abstain_supported: true });
    const ok = !shapeErrors.length && validation.ok;
    const out = { ok, shapeErrors, findings: validation.findings };
    const outPath = path.join(args.out, `record-validate-${path.basename(fixturePath)}`);
    writeJson(outPath, out);
    console.log(JSON.stringify(out, null, 2));
    process.exit(ok ? 0 : 2);
  }

  if (args.command === 'integration:run') {
    const fixturePath = args.positional[0];
    if (!fixturePath || !fs.existsSync(fixturePath)) {
      console.error('fixture path required');
      process.exit(1);
    }
    const fixture = readJson(fixturePath);
    const config = fs.existsSync(args.config) ? readJson(args.config) : undefined;
    const result = runAdmissionIntegration(fixture, { lockPath: args.lock, config, configPath: args.config });
    const outPath = path.join(args.out, `integration-${fixture.fixture_id || path.basename(fixturePath, '.json')}.json`);
    const outputClass =
      args.diagnostic || process.env.MARS_SEARCH_PPC_DIAGNOSTIC === '1' || process.env[LIFECYCLE_AUTH_ENV] !== '1'
        ? 'diagnostic'
        : 'production_authority';
    const envelope = {
      output_class: outputClass,
      diagnostic_only: outputClass === 'diagnostic',
      may_authorize_downstream: outputClass === 'production_authority',
      integration_result: result,
    };
    writeJson(outPath, envelope);
    console.log(JSON.stringify({
      fixture_id: fixture.fixture_id,
      ok: result.ok,
      blocked: result.blocked,
      admission_decision: result.admission_decision,
      review_routed: result.routing?.routed,
      output_class: outputClass,
      out: outPath,
    }, null, 2));
    process.exit(result.ok ? 0 : 2);
  }

  console.error(`unknown command: ${args.command}`);
  usage();
  process.exit(1);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
