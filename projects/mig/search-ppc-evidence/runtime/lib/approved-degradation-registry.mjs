import fs from 'node:fs';
import path from 'node:path';
import { loadJson, writeJson, sha256Text } from './utils.mjs';

export const DEGRADED_VERDICT = 'APPROVED WITH DEGRADATION — TECHNICAL CAPABILITY ONLY';
export const GENERIC_BYPASS_FIELDS = [
  'ignore_business_hours',
  'skip_business_hours',
  'bypass_business_hours',
  'force_business_hours',
];

export function hashDegradationBody(record) {
  const copy = JSON.parse(JSON.stringify(record));
  delete copy.checksum;
  return sha256Text(JSON.stringify(copy));
}

export function loadApprovedDegradations(degradationsDir) {
  if (!degradationsDir || !fs.existsSync(degradationsDir)) return [];
  const files = fs
    .readdirSync(degradationsDir)
    .filter((f) => f.endsWith('.json') && !f.includes('consumption-registry'));
  const records = [];
  for (const file of files) {
    try {
      const record = loadJson(path.join(degradationsDir, file));
      if (record.checksum) {
        const actual = hashDegradationBody(record);
        if (actual !== record.checksum) {
          record._checksum_invalid = true;
        }
      }
      records.push(record);
    } catch {
      // skip invalid files
    }
  }
  return records;
}

export function loadConsumptionRegistry(registryPath) {
  if (!registryPath || !fs.existsSync(registryPath)) {
    return { schema_version: '1.0.0', consumed: [] };
  }
  return loadJson(registryPath);
}

export function isDegradationConsumed(degradationId, registryPath) {
  const registry = loadConsumptionRegistry(registryPath);
  return (registry.consumed || []).some((c) => c.degradation_id === degradationId);
}

export function rejectGenericBusinessHoursBypass(bundle) {
  for (const field of GENERIC_BYPASS_FIELDS) {
    if (bundle?.[field] === true) {
      return { rejected: true, reason: `generic bypass flag prohibited: ${field}` };
    }
  }
  return { rejected: false };
}

export function matchApprovedDegradation({
  bundle,
  degradations = [],
  consumptionRegistryPath,
}) {
  const bypass = rejectGenericBusinessHoursBypass(bundle);
  if (bypass.rejected) {
    return { matched: false, blockers: [bypass.reason] };
  }

  const blockers = [];
  for (const degradation of degradations) {
    if (degradation._checksum_invalid) {
      blockers.push(`degradation checksum invalid: ${degradation.degradation_id}`);
      continue;
    }
    if (degradation.status !== 'approved') continue;
    if (isDegradationConsumed(degradation.degradation_id, consumptionRegistryPath)) {
      blockers.push(`degradation already consumed: ${degradation.degradation_id}`);
      continue;
    }
    if (degradation.project_id !== bundle.project_id) continue;
    if (degradation.session_id !== bundle.session_id) continue;
    if (degradation.query_id !== bundle.query_id) continue;
    if (degradation.capture_timestamp !== bundle.captured_at) continue;

    if (degradation.production_authority === true || degradation.client_authority === true) {
      blockers.push(`degradation cannot grant production authority: ${degradation.degradation_id}`);
      continue;
    }

    return {
      matched: true,
      degradation,
      capture_time_status: 'OUTSIDE_PREFERRED_WINDOW',
      degradation_status: 'OPERATOR_APPROVED',
      degraded_verdict: DEGRADED_VERDICT,
      warnings: [
        `Capture outside preferred business-hours window; operator-approved degradation ${degradation.degradation_id} applied`,
        'Evidence authority limited to technical capability validation only',
      ],
    };
  }

  return { matched: false, blockers };
}

export function consumeApprovedDegradation({ degradationId, bundle, consumptionRegistryPath, importReceiptId }) {
  const registry = loadConsumptionRegistry(consumptionRegistryPath);
  if ((registry.consumed || []).some((c) => c.degradation_id === degradationId)) {
    return { ok: false, reason: 'degradation already consumed' };
  }
  registry.consumed = registry.consumed || [];
  registry.consumed.push({
    degradation_id: degradationId,
    consumed_at: new Date().toISOString(),
    project_id: bundle?.project_id,
    session_id: bundle?.session_id,
    query_id: bundle?.query_id,
    capture_timestamp: bundle?.captured_at,
    import_receipt_id: importReceiptId || null,
  });
  writeJson(consumptionRegistryPath, registry);
  return { ok: true, registry };
}

export function assertDegradedEvidenceAuthority({ validation, importReceipt }) {
  if (!validation?.degradation_applied) return { ok: true };
  const flags = [];
  if (validation.bundle?.production_authority === true) flags.push('bundle production_authority');
  if (validation.bundle?.registered_as_production_authority === true) flags.push('registered_as_production_authority');
  if (importReceipt?.production_authority === true) flags.push('import production_authority');
  if (importReceipt?.client_authority === true) flags.push('import client_authority');
  if (importReceipt?.evidence_class && !String(importReceipt.evidence_class).includes('TECHNICAL')) {
    flags.push('non-technical evidence_class');
  }
  return { ok: flags.length === 0, flags };
}
