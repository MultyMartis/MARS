import path from 'node:path';
import { authorizeAction } from '../../../../mars-search-ppc-production/runtime/src/lifecycle-gate.mjs';
import { loadJson } from '../../../../mars-search-ppc-production/runtime/src/validate-lifecycle.mjs';
import { BLOCKERS, REPO_ROOT } from './lib.mjs';

export function authorizeProductionRun({ manifestPath, action = 'production_admission', actor = 'orca-semantic-production' }) {
  const gate = authorizeAction({
    manifestPath,
    requestedAction: action,
    requestedStage: 'SPPC-05',
    actor,
    tool: 'orca-semantic-production-v1',
    repoRoot: REPO_ROOT,
    writeReceipt: false,
  });

  if (!gate.allowed) {
    return { ok: false, blocked: true, message: gate.blockers?.[0]?.message || gate.message || 'BLOCKED', gate };
  }

  const manifest = loadJson(path.resolve(manifestPath));
  if (manifest.lifecycle_status === 'FROZEN' || manifest.risk_mode === 'DIAGNOSTIC_FREEZE') {
    return { ok: false, blocked: true, message: BLOCKERS.FROZEN_PROJECT, gate };
  }

  const s03 = manifest.stage_registry?.['SPPC-03']?.status;
  const s04 = manifest.stage_registry?.['SPPC-04']?.status;
  if (s03 !== 'COMPLETED' || s04 !== 'COMPLETED') {
    return {
      ok: false,
      blocked: true,
      message: `BLOCKED — SPPC-03/04 not complete (SPPC-03=${s03}, SPPC-04=${s04})`,
      gate,
    };
  }

  return { ok: true, manifest, gate };
}

export function validateCorpusMode(corpusMeta, expectedCount) {
  if (corpusMeta.corpus_mode && /DIAGNOSTIC|PILOT|SAMPLE/i.test(corpusMeta.corpus_mode)) {
    return { ok: false, message: BLOCKERS.DIAGNOSTIC_SUBSTITUTION };
  }
  if (expectedCount && corpusMeta.phrase_count && corpusMeta.phrase_count !== expectedCount) {
    return { ok: false, message: BLOCKERS.COUNT_MISMATCH };
  }
  return { ok: true };
}
