import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import {
  BLOCK_MESSAGES,
  readJson,
  resolveFromRepo,
  RUNTIME_ROOT,
} from './lib.mjs';

function sha256File(absPath) {
  const buf = fs.readFileSync(absPath);
  return crypto.createHash('sha256').update(buf).digest('hex').toUpperCase();
}

function validateManifestStructure(manifest) {
  const errors = [];
  if (!manifest.bundle_version) errors.push('missing bundle_version');
  if (!Array.isArray(manifest.contracts) || manifest.contracts.length === 0) {
    errors.push('contracts must be non-empty array');
  }
  const ids = new Set();
  for (const c of manifest.contracts || []) {
    if (!c.contract_id) errors.push('contract missing contract_id');
    if (ids.has(c.contract_id)) errors.push(`duplicated contract ID: ${c.contract_id}`);
    ids.add(c.contract_id);
    if (!c.canonical_path) errors.push(`unresolved canonical path for ${c.contract_id}`);
    if (!c.consumer) errors.push(`missing consumer for ${c.contract_id}`);
  }
  return errors;
}

export function loadContracts(options = {}) {
  const lockPath = options.lockPath || path.join(RUNTIME_ROOT, 'config/orca-semantic-contract-runtime-lock-v1.json');
  const manifest = readJson(lockPath);
  const bundleVersion = options.bundleVersion || manifest.bundle_version;
  const structuralErrors = validateManifestStructure(manifest);
  if (structuralErrors.length) {
    return {
      ok: false,
      blocked: true,
      message: BLOCK_MESSAGES.INVALID_MANIFEST,
      errors: structuralErrors,
      evidence: [],
    };
  }

  const requiredConsumers = new Set(manifest.required_consumers || []);
  const loadedConsumers = new Set();
  const evidence = [];
  const bundle = {};
  const sorted = [...manifest.contracts].sort((a, b) => a.load_order - b.load_order);

  for (const entry of sorted) {
    const absPath = resolveFromRepo(entry.canonical_path);
    const record = {
      contract_id: entry.contract_id,
      canonical_path: entry.canonical_path,
      expected_checksum: entry.checksum_sha256,
      declared_version: entry.version,
      consumer: entry.consumer,
      required: !!entry.required,
      load_order: entry.load_order,
    };

    if (!fs.existsSync(absPath)) {
      if (entry.required) {
        return failLoad(record, BLOCK_MESSAGES.MISSING, `file not found: ${absPath}`, evidence);
      }
      evidence.push({ ...record, load_status: 'OPTIONAL — NOT LOADED', blocking: false });
      continue;
    }

    if (entry.required && Array.isArray(entry.compatibility) && !entry.compatibility.includes(bundleVersion)) {
      return failLoad(record, BLOCK_MESSAGES.VERSION, `bundle ${bundleVersion} not in compatibility`, evidence);
    }

    let actualChecksum = null;
    let parsed = null;
    const isJson = absPath.endsWith('.json') || absPath.endsWith('.schema.json');

    try {
      if (isJson) {
        const raw = fs.readFileSync(absPath, 'utf8');
        actualChecksum = crypto.createHash('sha256').update(raw).digest('hex').toUpperCase();
        parsed = JSON.parse(raw);
      } else {
        actualChecksum = sha256File(absPath);
      }
    } catch (err) {
      if (entry.required) {
        return failLoad(record, BLOCK_MESSAGES.INVALID_MANIFEST, `invalid content: ${err.message}`, evidence);
      }
    }

    if (entry.required && entry.checksum_sha256 && actualChecksum !== entry.checksum_sha256) {
      record.actual_checksum = actualChecksum;
      return failLoad(record, BLOCK_MESSAGES.CHECKSUM, 'checksum mismatch', evidence);
    }

    let actualVersion = entry.version;
    if (parsed && typeof parsed === 'object') {
      actualVersion = parsed.version || parsed.schema_version || parsed.manifest_version || entry.version;
      if (entry.required && actualVersion && entry.version && actualVersion !== entry.version && !String(actualVersion).startsWith(entry.version)) {
        return failLoad(record, BLOCK_MESSAGES.VERSION, `declared ${entry.version} actual ${actualVersion}`, evidence);
      }
    }

    bundle[entry.contract_id] = {
      path: absPath,
      content: parsed ?? { _type: 'non_json', path: absPath },
      meta: entry,
    };
    loadedConsumers.add(entry.consumer);
    evidence.push({
      ...record,
      actual_checksum: actualChecksum,
      actual_version: actualVersion,
      load_status: 'LOADED AND CONSUMED',
      usage_evidence: `consumer:${entry.consumer};load_order:${entry.load_order}`,
      blocking: false,
    });
  }

  for (const consumer of requiredConsumers) {
    if (!loadedConsumers.has(consumer)) {
      return {
        ok: false,
        blocked: true,
        message: BLOCK_MESSAGES.MISSING,
        errors: [`required consumer missing: ${consumer}`],
        evidence,
      };
    }
  }

  return {
    ok: true,
    blocked: false,
    bundle,
    manifest,
    bundleVersion,
    evidence,
    load_order: evidence.map((e) => e.contract_id),
  };
}

function failLoad(record, message, detail, evidence) {
  evidence.push({
    ...record,
    load_status: message.includes('CHECKSUM') ? 'BLOCKED — CHECKSUM' : message.includes('VERSION') ? 'BLOCKED — VERSION' : 'BLOCKED — MISSING',
    blocking: true,
    detail,
  });
  return {
    ok: false,
    blocked: true,
    message,
    errors: [detail],
    evidence,
  };
}
