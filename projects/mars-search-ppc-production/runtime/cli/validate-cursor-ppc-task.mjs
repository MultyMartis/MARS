#!/usr/bin/env node
/**
 * MARS Search PPC — Cursor Task Contract Linter (Wave 1.1)
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../');
const SCHEMA_PATH = path.resolve(__dirname, '../schemas/cursor-search-ppc-task-contract-v1.schema.json');
const BLOCKER = 'BLOCKED — CURSOR SEARCH PPC TASK CONTRACT INVALID';

const REQUIRED_FIELDS = [
  'project_id',
  'manifest_path',
  'lifecycle_stage',
  'requested_action',
  'authoritative_inputs',
  'expected_outputs',
  'forbidden_outputs',
  'pre_validation_command',
  'post_validation_command',
  'git_scope',
];

function parseArgs(argv) {
  const args = { task: null, help: false };
  const rest = argv.slice(2);
  if (rest[0] && !rest[0].startsWith('-')) args.task = rest[0];
  for (const a of rest) {
    if (a === '--help' || a === '-h') args.help = true;
  }
  return args;
}

function validateTask(task) {
  const errors = [];
  for (const field of REQUIRED_FIELDS) {
    if (task[field] === undefined || task[field] === null || task[field] === '') {
      errors.push(`missing required field: ${field}`);
    }
  }
  if (task.manifest_path && !fs.existsSync(path.resolve(REPO_ROOT, task.manifest_path))) {
    errors.push(`manifest not found: ${task.manifest_path}`);
  }
  if (task.lifecycle_stage && !/^SPPC-\d{2}$/.test(task.lifecycle_stage)) {
    errors.push(`invalid lifecycle_stage: ${task.lifecycle_stage}`);
  }
  if (!Array.isArray(task.authoritative_inputs)) {
    errors.push('authoritative_inputs must be an array');
  }
  if (!Array.isArray(task.expected_outputs)) {
    errors.push('expected_outputs must be an array');
  }
  if (!Array.isArray(task.forbidden_outputs)) {
    errors.push('forbidden_outputs must be an array');
  }
  if (task.pre_validation_command && !task.pre_validation_command.includes('validate-search-ppc-lifecycle')) {
    errors.push('pre_validation_command must invoke lifecycle validator');
  }
  return errors;
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help || !args.task) {
    console.log(`Usage: node validate-cursor-ppc-task.mjs <task-contract.json>`);
    process.exit(args.help ? 0 : 1);
  }

  const taskPath = path.resolve(args.task);
  if (!fs.existsSync(taskPath)) {
    console.error(BLOCKER);
    console.error(`Task file not found: ${taskPath}`);
    process.exit(2);
  }

  let task;
  try {
    task = JSON.parse(fs.readFileSync(taskPath, 'utf8'));
  } catch (e) {
    console.error(BLOCKER);
    console.error(`Invalid JSON: ${e.message}`);
    process.exit(2);
  }

  const errors = validateTask(task);
  if (errors.length) {
    console.error(BLOCKER);
    for (const e of errors) console.error(`- ${e}`);
    process.exit(2);
  }

  console.log(JSON.stringify({ status: 'VALID', schema: path.basename(SCHEMA_PATH), task: taskPath }, null, 2));
  process.exit(0);
}

main();
