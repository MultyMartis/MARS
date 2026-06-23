/**
 * Cost, rate-limit, and run controls for live model execution.
 */
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';

export const DEFAULT_CONTROLS = {
  maxPhrasesPerRun: 5000,
  batchSize: 25,
  concurrency: 3,
  tokenEstimatePerPhrase: 800,
  costCapUsd: 50,
  retryCap: 3,
  timeoutMs: 30000,
  backoffBaseMs: 1000,
};

export function assertModelAvailable(adapter) {
  if (!adapter) {
    return { ok: false, blocker: 'BLOCKED — PRODUCTION SEMANTIC MODEL UNAVAILABLE' };
  }
  return { ok: true };
}

export function estimateRunCost(phraseCount, controls = DEFAULT_CONTROLS) {
  const tokens = phraseCount * controls.tokenEstimatePerPhrase * 2;
  const costUsd = (tokens / 1_000_000) * 0.15;
  return { tokens, costUsd, withinCap: costUsd <= controls.costCapUsd };
}

export function assertCostCap(phraseCount, controls = DEFAULT_CONTROLS) {
  const est = estimateRunCost(phraseCount, controls);
  if (!est.withinCap) {
    return { ok: false, blocker: 'COST_CAP_EXCEEDED', estimate: est };
  }
  return { ok: true, estimate: est };
}

export async function runWithRetry(fn, retryCap = DEFAULT_CONTROLS.retryCap, backoffBaseMs = DEFAULT_CONTROLS.backoffBaseMs) {
  let lastError;
  for (let attempt = 0; attempt <= retryCap; attempt++) {
    try {
      return await fn(attempt);
    } catch (e) {
      lastError = e;
      if (attempt < retryCap) {
        await sleep(backoffBaseMs * Math.pow(2, attempt));
      }
    }
  }
  throw lastError;
}

export function assessmentCacheKey(phrase, context, modelId) {
  const payload = {
    phrase_id: phrase.phrase_id,
    normalized_query: phrase.normalized_query,
    model_id: modelId,
    scope_version: context.businessScope?.version,
    registry_version: context.serviceRegistry?.version,
  };
  return crypto.createHash('sha256').update(JSON.stringify(payload)).digest('hex');
}

export function loadAssessmentCache(cacheDir) {
  const cachePath = path.join(cacheDir, 'assessment-cache-v1.json');
  if (!fs.existsSync(cachePath)) return new Map();
  const data = JSON.parse(fs.readFileSync(cachePath, 'utf8'));
  return new Map(Object.entries(data));
}

export function saveAssessmentCache(cacheDir, cache) {
  fs.mkdirSync(cacheDir, { recursive: true });
  const obj = Object.fromEntries(cache);
  fs.writeFileSync(path.join(cacheDir, 'assessment-cache-v1.json'), JSON.stringify(obj, null, 2));
}

export function loadRunCheckpoint(outDir) {
  const cp = path.join(outDir, 'live-run-checkpoint-v1.json');
  if (!fs.existsSync(cp)) return { processed_ids: [], cancelled: false, complete: false };
  return JSON.parse(fs.readFileSync(cp, 'utf8'));
}

export function saveRunCheckpoint(outDir, checkpoint) {
  fs.mkdirSync(outDir, { recursive: true });
  fs.writeFileSync(path.join(outDir, 'live-run-checkpoint-v1.json'), JSON.stringify(checkpoint, null, 2));
}

export function assertNotPartialComplete(checkpoint, expectedCount, processedCount) {
  if (checkpoint.cancelled) return { ok: false, blocker: 'RUN_CANCELLED' };
  if (checkpoint.complete && processedCount < expectedCount) {
    return { ok: false, blocker: 'PARTIAL_RUN_MARKED_COMPLETE' };
  }
  return { ok: true };
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}
