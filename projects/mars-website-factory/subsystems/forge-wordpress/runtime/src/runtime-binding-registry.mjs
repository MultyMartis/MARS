/**
 * FW-07C-1 / V9-05C — Runtime binding registry loader (site-aware).
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { RUNTIME_REASON_CODES as RC } from './runtime-reason-codes.mjs';
import { REGISTERED_SITES } from './runtime-authority.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const BINDINGS_DIR = path.resolve(__dirname, '../bindings');

const SITE_BINDING_FILES = Object.freeze({
  'fws-0001': 'fws-0001-readonly-bindings-v1.json',
  'fp-0002-shpigovsky': 'fp-0002-readonly-bindings-v1.json',
});

const registryCache = new Map();

export const BINDING_DECISIONS = Object.freeze([
  'BOUND_READ_ONLY_PROVEN',
  'BOUND_READ_ONLY_WITH_LIMITS',
  'DEFER_SIDE_EFFECT_RISK',
  'DEFER_EXTERNAL_TOOL',
  'DEFER_DATABASE',
  'REJECT',
  'UNBOUND',
]);

export function getBindingFileForSite(siteId) {
  return SITE_BINDING_FILES[siteId] ?? null;
}

export function loadBindingRegistry(bindingFile = 'fws-0001-readonly-bindings-v1.json') {
  const filePath = path.join(BINDINGS_DIR, bindingFile);
  const raw = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  const byOperationId = new Map();
  for (const binding of raw.bindings || []) {
    byOperationId.set(binding.operation_id, Object.freeze(binding));
  }
  return Object.freeze({
    ...raw,
    bindings: Object.freeze(raw.bindings || []),
    byOperationId,
    loaded_from: filePath,
  });
}

export function getBindingRegistry(siteId = 'fws-0001') {
  const bindingFile = getBindingFileForSite(siteId);
  if (!bindingFile) {
    return loadBindingRegistry();
  }
  if (!registryCache.has(siteId)) {
    registryCache.set(siteId, loadBindingRegistry(bindingFile));
  }
  return registryCache.get(siteId);
}

export function resetBindingRegistryCache() {
  registryCache.clear();
}

/**
 * Lookup binding for operation — fail-closed for unproven bindings.
 */
export function lookupBinding(operationId, siteId = 'fws-0001', options = {}) {
  const registry = options.registry ?? getBindingRegistry(siteId);
  const binding = registry.byOperationId.get(operationId);

  if (!binding) {
    return {
      found: false,
      binding: null,
      allowed: false,
      reason_codes: [RC.RT_BINDING_NOT_FOUND],
    };
  }

  if (registry.site_id !== siteId) {
    const siteAuth = REGISTERED_SITES[siteId];
    if (!siteAuth?.test_fixture) {
      return {
        found: true,
        binding,
        allowed: false,
        reason_codes: [RC.RT_BINDING_NOT_FOUND],
      };
    }
  }

  if (binding.binding_decision === 'UNBOUND') {
    return {
      found: true,
      binding,
      allowed: false,
      reason_codes: [RC.RT_BINDING_UNBOUND],
    };
  }

  if (binding.binding_decision === 'REJECT') {
    return {
      found: true,
      binding,
      allowed: false,
      reason_codes: [RC.RT_BINDING_REJECTED],
    };
  }

  const allowed = binding.binding_decision === 'BOUND_READ_ONLY_PROVEN';

  return {
    found: true,
    binding,
    allowed,
    reason_codes: allowed ? [] : [RC.RT_BINDING_REJECTED],
  };
}

export default { getBindingRegistry, lookupBinding, loadBindingRegistry, getBindingFileForSite };
