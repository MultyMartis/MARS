import { BLOCKER_CODES } from './constants.mjs';
import { getArtifact } from './manifest-normalize.mjs';

export function validateFullCorpus(manifest, stageId) {
  const blockers = [];
  const corpus = getArtifact(manifest, 'full_semantic_corpus_intake');
  const sourceReg = getArtifact(manifest, 'source_registry');

  if (stageId !== 'SPPC-03' && getStageStatus(manifest, 'SPPC-03') === 'COMPLETED') {
    return { valid: true, blockers: [] };
  }

  if (!['SPPC-03', 'SPPC-04', 'SPPC-05', 'SPPC-06', 'SPPC-07', 'SPPC-08', 'SPPC-09'].includes(stageId)) {
    if (!corpus) return { valid: true, blockers: [] };
  }

  const checkComplete = manifest.stage_registry?.['SPPC-03']?.status === 'COMPLETED'
    || manifest.stage_statuses?.['SPPC-03']?.status === 'COMPLETED';

  if (checkComplete || stageId === 'SPPC-03') {
    if (!corpus) {
      blockers.push({
        code: 'FULL_CORPUS_NOT_REGISTERED',
        message: BLOCKER_CODES.FULL_CORPUS_NOT_REGISTERED,
        owner: 'MIG',
      });
      return { valid: false, blockers };
    }

    const mode = corpus.corpus_mode || manifest.corpus_mode;
    const nonProductionModes = [
      'TECHNICAL PILOT', 'BENCHMARK', 'DIAGNOSTIC SAMPLE', 'RANDOM QA SAMPLE', 'HUMAN REVIEW SUBSET',
    ];

    if (nonProductionModes.includes(mode)) {
      blockers.push({
        code: 'FULL_CORPUS_NOT_REGISTERED',
        message: `${BLOCKER_CODES.FULL_CORPUS_NOT_REGISTERED} — corpus_mode is ${mode}`,
        owner: 'MIG',
      });
    }

    if (corpus.pilot_substitution === true || corpus.diagnostic_only === true) {
      blockers.push({
        code: 'FULL_CORPUS_NOT_REGISTERED',
        message: `${BLOCKER_CODES.FULL_CORPUS_NOT_REGISTERED} — pilot/diagnostic substituted for full corpus`,
        owner: 'MIG',
      });
    }

    if (sourceReg?.expected_row_count != null && corpus.registered_row_count != null) {
      if (Number(corpus.registered_row_count) !== Number(sourceReg.expected_row_count)) {
        blockers.push({
          code: 'FULL_CORPUS_NOT_REGISTERED',
          message: `${BLOCKER_CODES.FULL_CORPUS_NOT_REGISTERED} — extraction count ${corpus.registered_row_count} != source registry ${sourceReg.expected_row_count}`,
          owner: 'MIG',
        });
      }
    }

    if (corpus.exclusions_documented === false) {
      blockers.push({
        code: 'FULL_CORPUS_NOT_REGISTERED',
        message: `${BLOCKER_CODES.FULL_CORPUS_NOT_REGISTERED} — exclusions not documented`,
        owner: 'MIG',
      });
    }
  }

  return { valid: blockers.length === 0, blockers };
}

function getStageStatus(manifest, stageId) {
  return manifest.stage_registry?.[stageId]?.status || manifest.stage_statuses?.[stageId]?.status || 'NOT STARTED';
}
