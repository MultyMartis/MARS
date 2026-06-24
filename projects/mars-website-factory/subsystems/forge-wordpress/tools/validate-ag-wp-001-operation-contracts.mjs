#!/usr/bin/env node
/**
 * AG-WP-001 Operation Contract Validator v1 (FW-07B)
 * Read-only. Does not execute WordPress operations.
 *
 * Usage:
 *   node validate-ag-wp-001-operation-contracts.mjs
 *   node validate-ag-wp-001-operation-contracts.mjs --fixtures
 *   node validate-ag-wp-001-operation-contracts.mjs --schema-only
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FW_ROOT = path.resolve(__dirname, '..');
const SCHEMAS = path.join(FW_ROOT, 'schemas');
const OPS_DIR = path.join(FW_ROOT, 'operations', 'ag-wp-001');
const BIND_DIR = path.join(FW_ROOT, 'bindings', 'ag-wp-001');
const FIXTURES = path.join(FW_ROOT, 'fixtures', 'ag-wp-001');

export const EXIT = { OK: 0, VALIDATION_FAIL: 1, FIXTURE_FAIL: 2, IO_ERROR: 3 };

const LIFECYCLE = new Set(['DRAFT', 'DEFINED', 'APPROVED', 'DEPRECATED']);
const IMPL_STATUS = new Set([
  'UNBOUND', 'BOUND_NOT_IMPLEMENTED', 'IMPLEMENTED_NOT_VALIDATED',
  'VALIDATED_LOCAL', 'AUTHORIZED_LOCAL', 'AUTHORIZED_STAGING', 'PRODUCTION_PROHIBITED',
]);
const ENV_SCOPE = new Set([
  'BRAIN_ONLY', 'LOCAL_SOURCE', 'LOCAL_RUNTIME_READ_ONLY', 'LOCAL_RUNTIME_MUTATION',
  'STAGING_READ_ONLY', 'STAGING_MUTATION', 'PRODUCTION_READ_ONLY', 'PRODUCTION_MUTATION',
]);
const IDEMPOTENCY = new Set(['IDEMPOTENT', 'CONDITIONALLY_IDEMPOTENT', 'NON_IDEMPOTENT']);
const SIDE_EFFECTS = new Set(['NONE', 'READ_ONLY_ARTIFACTS', 'SOURCE_MUTATION', 'RUNTIME_MUTATION', 'DATABASE_MUTATION']);
const SAFE_UNKNOWN = new Set(['BLOCK', 'REPORT_AND_CONTINUE', 'ESCALATE', 'STOP']);
const SECRET_POLICY = new Set(['NO_ACCESS', 'INDIRECT_CONSUMPTION', 'OPERATOR_PROVIDED_SESSION', 'PROHIBITED']);
const OP_ID_RE = /^wp\.[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)+$/;

const REQUIRED_FIELDS = [
  'operation_id', 'version', 'title', 'description', 'category', 'lifecycle_status',
  'implementation_status', 'risk_class', 'environment_scope', 'production_allowed',
  'input_schema', 'output_schema', 'preconditions', 'postconditions', 'invariants',
  'approval', 'approval_evidence', 'tool_binding', 'tool_status', 'idempotency',
  'side_effects', 'rollback', 'audit_evidence', 'success_criteria', 'failure_codes',
  'safe_unknown_behavior', 'timeout_policy', 'retry_policy', 'secret_policy',
  'logging_policy', 'dependencies', 'conflicts', 'allowed_next_operations',
];

function loadJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function validateSchemaSelf(schema) {
  const errors = [];
  if (!schema.$schema) errors.push('schema missing $schema');
  if (!schema.required?.length) errors.push('schema missing required fields');
  if (!schema.properties?.operation_id) errors.push('schema missing operation_id property');
  return errors;
}

export function validateOperation(op, ctx) {
  const errors = [];
  const { failureCodes, toolIds, seenIds } = ctx;

  if (!op || typeof op !== 'object') return ['operation is not an object'];
  for (const f of REQUIRED_FIELDS) {
    if (!(f in op)) errors.push(`missing required field: ${f}`);
  }
  if (op.operation_id) {
    if (!OP_ID_RE.test(op.operation_id)) errors.push(`invalid operation_id format: ${op.operation_id}`);
    if (seenIds.has(op.operation_id)) errors.push(`duplicate operation_id: ${op.operation_id}`);
    seenIds.add(op.operation_id);
  }
  if (op.lifecycle_status && !LIFECYCLE.has(op.lifecycle_status)) {
    errors.push(`invalid lifecycle_status: ${op.lifecycle_status}`);
  }
  if (op.implementation_status && !IMPL_STATUS.has(op.implementation_status)) {
    errors.push(`invalid implementation_status: ${op.implementation_status}`);
  }
  if (op.production_allowed !== false) {
    errors.push('production_allowed must be false at foundation');
  }
  if (op.environment_scope?.some((e) => !ENV_SCOPE.has(e))) {
    errors.push(`invalid environment_scope entry in ${op.operation_id}`);
  }
  if (op.environment_scope?.some((e) => e.startsWith('PRODUCTION'))) {
    errors.push(`production scope forbidden: ${op.operation_id}`);
  }
  if (op.risk_class === 'R5' && op.implementation_status !== 'PRODUCTION_PROHIBITED') {
    errors.push(`R5 must be PRODUCTION_PROHIBITED: ${op.operation_id}`);
  }
  if (op.implementation_status === 'AUTHORIZED_LOCAL' && op.risk_class === 'R5') {
    errors.push(`R5 cannot be AUTHORIZED: ${op.operation_id}`);
  }
  if (op.idempotency && !IDEMPOTENCY.has(op.idempotency)) errors.push(`invalid idempotency: ${op.operation_id}`);
  if (op.side_effects && !SIDE_EFFECTS.has(op.side_effects)) errors.push(`invalid side_effects: ${op.operation_id}`);
  if (op.safe_unknown_behavior && !SAFE_UNKNOWN.has(op.safe_unknown_behavior)) {
    errors.push(`invalid safe_unknown_behavior: ${op.operation_id}`);
  }
  if (op.secret_policy && !SECRET_POLICY.has(op.secret_policy)) errors.push(`invalid secret_policy: ${op.operation_id}`);

  const mutation = ['SOURCE_MUTATION', 'RUNTIME_MUTATION', 'DATABASE_MUTATION'].includes(op.side_effects);
  if (mutation && op.rollback?.required !== true) {
    errors.push(`mutation requires rollback.required=true: ${op.operation_id}`);
  }
  if (mutation && ['R2', 'R3', 'R4'].includes(op.risk_class) && op.approval?.required !== true) {
    errors.push(`mutation requires approval: ${op.operation_id}`);
  }

  for (const fc of op.failure_codes || []) {
    if (!failureCodes.has(fc)) errors.push(`unknown failure_code ${fc} in ${op.operation_id}`);
  }
  for (const tid of op.tool_binding?.tool_ids || []) {
    if (tid !== 'UNBOUND' && toolIds.size && !toolIds.has(tid)) {
      errors.push(`unregistered tool_id ${tid} in ${op.operation_id}`);
    }
  }
  if (op.tool_status === 'PROVEN' && op.implementation_status === 'UNBOUND') {
    errors.push(`PROVEN tool_status with UNBOUND implementation: ${op.operation_id}`);
  }

  return errors;
}

export function validateRegistry(registry, failureRegistry, bindings) {
  const seenIds = new Set();
  const failureCodes = new Set((failureRegistry.codes || []).map((c) => c.code));
  const toolIds = new Set();
  for (const b of bindings.bindings || []) {
    for (const t of b.tool_ids || [b.tool_id].filter(Boolean)) toolIds.add(t);
  }
  toolIds.add('FW-TOL-001');
  toolIds.add('FW-TOL-010');
  toolIds.add('MLI-TOOL-007');

  const ctx = { failureCodes, toolIds, seenIds };
  const allErrors = [];
  const ops = registry.operations || [];

  for (const op of ops) {
    allErrors.push(...validateOperation(op, ctx));
  }

  return {
    operation_count: ops.length,
    valid_count: ops.length - new Set(allErrors.map((e) => e.split(':')[1]?.trim())).size,
    errors: allErrors,
    duplicate_ids: ops.length - seenIds.size,
    bindings_defined: (bindings.bindings || []).length,
  };
}

function validateFixture(name, op, expectValid, failureRegistry) {
  const failureCodes = new Set((failureRegistry.codes || []).map((c) => c.code));
  const errors = validateOperation(op, { failureCodes, toolIds: new Set(), seenIds: new Set() });
  const valid = errors.length === 0;
  if (valid !== expectValid) {
    return { name, pass: false, message: expectValid ? `expected valid, got: ${errors.join('; ')}` : `expected invalid, but passed` };
  }
  return { name, pass: true };
}

function parseArgs(argv) {
  return {
    fixtures: argv.includes('--fixtures'),
    schemaOnly: argv.includes('--schema-only'),
    help: argv.includes('--help') || argv.includes('-h'),
  };
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help) {
    console.log('Usage: node validate-ag-wp-001-operation-contracts.mjs [--fixtures] [--schema-only]');
    process.exit(0);
  }

  const schemaPath = path.join(SCHEMAS, 'AG-WP-001-OPERATION-CONTRACT-SCHEMA-v1.json');
  const schema = loadJson(schemaPath);
  const schemaErrors = validateSchemaSelf(schema);
  if (schemaErrors.length) {
    console.error('Schema self-validation failed:', schemaErrors);
    process.exit(EXIT.IO_ERROR);
  }
  console.log('Schema self-validation: PASS');

  if (args.schemaOnly) process.exit(EXIT.OK);

  const registry = loadJson(path.join(OPS_DIR, 'operations-v1.json'));
  const failureRegistry = loadJson(path.join(SCHEMAS, 'AG-WP-001-FAILURE-CODE-REGISTRY-v1.json'));
  const bindings = loadJson(path.join(BIND_DIR, 'bindings-v1.json'));

  const result = validateRegistry(registry, failureRegistry, bindings);
  if (result.errors.length) {
    console.error('Operation validation FAILED:');
    for (const e of result.errors) console.error(`  - ${e}`);
    process.exit(EXIT.VALIDATION_FAIL);
  }
  console.log(`Operations: ${result.operation_count} discovered, ${result.operation_count} valid`);
  console.log(`Bindings: ${result.bindings_defined} defined`);
  console.log(`Failure codes: ${failureRegistry.codes?.length || 0}`);

  if (args.fixtures) {
    const fixtureResults = [];
    const validReadOnly = loadJson(path.join(FIXTURES, 'valid-read-only-operation.json'));
    fixtureResults.push(validateFixture('valid-read-only-operation', validReadOnly, true, failureRegistry));

    const validSource = loadJson(path.join(FIXTURES, 'valid-local-source-operation.json'));
    fixtureResults.push(validateFixture('valid-local-source-operation', validSource, true, failureRegistry));

    const validMutation = loadJson(path.join(FIXTURES, 'valid-local-runtime-mutation-operation.json'));
    fixtureResults.push(validateFixture('valid-local-runtime-mutation-operation', validMutation, true, failureRegistry));

    const invalidProd = loadJson(path.join(FIXTURES, 'invalid-production-operation.json'));
    fixtureResults.push(validateFixture('invalid-production-operation', invalidProd, false, failureRegistry));

    const invalidRollback = loadJson(path.join(FIXTURES, 'invalid-missing-rollback.json'));
    fixtureResults.push(validateFixture('invalid-missing-rollback', invalidRollback, false, failureRegistry));

    const invalidApproval = loadJson(path.join(FIXTURES, 'invalid-missing-approval.json'));
    fixtureResults.push(validateFixture('invalid-missing-approval', invalidApproval, false, failureRegistry));

    const invalidDup = loadJson(path.join(FIXTURES, 'invalid-duplicate-operation-id.json'));
    fixtureResults.push(validateFixture('invalid-duplicate-operation-id', invalidDup, false, failureRegistry));

    const failed = fixtureResults.filter((r) => !r.pass);
    if (failed.length) {
      console.error('Fixture tests FAILED:');
      for (const f of failed) console.error(`  - ${f.name}: ${f.message}`);
      process.exit(EXIT.FIXTURE_FAIL);
    }
    console.log(`Fixtures: ${fixtureResults.length} passed, 0 failed`);
  }

  console.log('VALIDATION: PASS');
  process.exit(EXIT.OK);
}

if (process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1])) {
  main();
}
