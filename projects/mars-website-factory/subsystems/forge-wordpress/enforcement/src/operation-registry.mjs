/**
 * FW-07C-0 — Forge operation registry loader (canonical operations-v1.json adapter).
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { REASON_CODES as RC } from './reason-codes.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FW_ROOT = path.resolve(__dirname, '../..');
const REGISTRY_PATH = path.join(FW_ROOT, 'operations', 'ag-wp-001', 'operations-v1.json');
const OPS_DIR = path.join(FW_ROOT, 'operations', 'ag-wp-001');

let cachedRegistry = null;

function inferScopes(op) {
  const sideEffects = op.side_effects || 'NONE';
  const envScope = op.environment_scope || [];
  const filesystem_scope = sideEffects.includes('MUTATION') || sideEffects === 'SOURCE_MUTATION' || sideEffects === 'RUNTIME_MUTATION'
    ? 'MUTATION'
    : envScope.some((e) => e.includes('RUNTIME'))
      ? 'RUNTIME_READ'
      : 'BRAIN_READ';
  const database_scope = sideEffects === 'DATABASE_MUTATION' ? 'MUTATION' : op.risk_class === 'R5' ? 'READ' : 'NONE';
  const remote_scope = (op.environment_scope || []).some((e) => e.startsWith('REMOTE') || e.includes('STAGING') || e.includes('PRODUCTION'))
    ? 'REMOTE'
    : 'NONE';
  return { filesystem_scope, database_scope, remote_scope };
}

function normalizeOperation(op) {
  const scopes = inferScopes(op);
  return Object.freeze({
    operation_id: op.operation_id,
    legacy_op_id: op.legacy_op_id ?? null,
    risk_class: op.risk_class,
    filesystem_scope: scopes.filesystem_scope,
    database_scope: scopes.database_scope,
    remote_scope: scopes.remote_scope,
    snapshot_required: op.rollback?.required === true || ['R2', 'R3', 'R4', 'R5'].includes(op.risk_class),
    approval_required: op.approval?.required === true,
    rollback_method: op.rollback?.method ?? 'not_applicable',
    fw07c_phase: op.risk_class === 'R0' ? 'FW-07C-0' : op.risk_class === 'R1' ? 'FW-07C-2' : op.risk_class === 'R5' ? 'FW-07C-5' : 'FW-07C-3',
    runtime_binding_status: op.implementation_status === 'VALIDATED_LOCAL' ? 'PROVEN' : 'UNBOUND',
    implementation_status: op.implementation_status,
    environment_scope: Object.freeze([...(op.environment_scope || [])]),
    side_effects: op.side_effects,
    category: op.category,
  });
}

export function loadCanonicalRegistry(sourcePath = REGISTRY_PATH) {
  const raw = JSON.parse(fs.readFileSync(sourcePath, 'utf8'));
  const seenIds = new Set();
  const duplicates = [];
  const operations = [];
  const errors = [];

  for (const op of raw.operations || []) {
    if (seenIds.has(op.operation_id)) {
      duplicates.push(op.operation_id);
      errors.push(`duplicate operation_id: ${op.operation_id}`);
    }
    seenIds.add(op.operation_id);
    operations.push(normalizeOperation(op));
  }

  const registry = Object.freeze({
    registry_id: raw.registry_id,
    version: raw.version,
    operation_count: operations.length,
    operations: Object.freeze(operations),
    operation_ids: Object.freeze(operations.map((o) => o.operation_id)),
    duplicates,
    errors,
    loaded_from: sourcePath,
  });

  return registry;
}

export function getOperationRegistry(forceReload = false) {
  if (!cachedRegistry || forceReload) {
    cachedRegistry = loadCanonicalRegistry();
  }
  return cachedRegistry;
}

export function resetOperationRegistryCache() {
  cachedRegistry = null;
}

export function lookupOperation(operationId, registry = getOperationRegistry()) {
  return registry.operations.find((o) => o.operation_id === operationId) ?? null;
}

export function validateOperationId(operationId, registry = getOperationRegistry()) {
  if (!operationId) {
    return { known: false, reason_codes: [RC.FW_OPERATION_UNKNOWN] };
  }
  const op = lookupOperation(operationId, registry);
  if (!op) {
    return { known: false, reason_codes: [RC.FW_OPERATION_UNKNOWN] };
  }
  return { known: true, operation: op, reason_codes: [] };
}

export function loadIndividualContracts() {
  const files = fs.readdirSync(OPS_DIR).filter(
    (f) => f.endsWith('.json') && f !== 'operations-v1.json' && f !== 'manifest-v1.json'
  );
  return files.map((f) => {
    const full = path.join(OPS_DIR, f);
    const data = JSON.parse(fs.readFileSync(full, 'utf8'));
    return { file: f, operation_id: data.operation_id };
  });
}

export function assertAllContractsLoaded() {
  const registry = getOperationRegistry();
  const contracts = loadIndividualContracts();
  const contractIds = new Set(contracts.map((c) => c.operation_id));
  const missing = registry.operation_ids.filter((id) => !contractIds.has(id));
  const extra = contracts.filter((c) => !registry.operation_ids.includes(c.operation_id));
  return {
    registry_count: registry.operation_count,
    contract_count: contracts.length,
    missing_in_contracts: missing,
    extra_in_contracts: extra.map((c) => c.operation_id),
    all_loaded: missing.length === 0 && extra.length === 0 && registry.duplicates.length === 0,
  };
}

export default getOperationRegistry;
