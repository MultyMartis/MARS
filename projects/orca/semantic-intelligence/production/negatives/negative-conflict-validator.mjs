import { BLOCKERS } from '../runtime/lib.mjs';

export function validateNegativeConflicts(negativeLibrary, acceptedRecords, clusters) {
  const conflicts = [];
  const acceptedQueries = new Set(acceptedRecords
    .filter((r) => r.adjudication_result?.outcome === 'FINAL ACCEPT')
    .map((r) => (r.normalized_query || r.raw_query || '').toLowerCase()));

  const acceptedPhraseIds = new Set(acceptedRecords
    .filter((r) => r.adjudication_result?.outcome === 'FINAL ACCEPT')
    .map((r) => r.phrase_id));

  const allNegatives = [
    ...(negativeLibrary.global_negatives || []),
    ...(negativeLibrary.campaign_level_candidates || []),
    ...(negativeLibrary.group_level_candidates || []),
    ...(negativeLibrary.cross_negatives || []),
  ];

  for (const neg of allNegatives) {
    if (!neg.term || neg.exclusion_type === 'observation_only' || neg.exclusion_type === 'cross_separation') continue;

    const term = String(neg.term).toLowerCase();
    for (const q of acceptedQueries) {
      if (q.includes(term) || term.includes(q)) {
        conflicts.push({
          negative_id: neg.negative_id,
          term: neg.term,
          blocked_query: q,
          type: 'blocks_accepted_phrase',
        });
      }
    }

    if (neg.affected_phrase_ids?.some((id) => acceptedPhraseIds.has(id)) && neg.exclusion_type === 'definite_exclusion') {
      conflicts.push({
        negative_id: neg.negative_id,
        type: 'blocks_accepted_phrase_id',
        phrase_ids: neg.affected_phrase_ids,
      });
    }
  }

  const blocked = conflicts.some((c) => c.type === 'blocks_accepted_phrase');
  return {
    conflicts,
    blocked,
    blocker: blocked ? BLOCKERS.NEGATIVE_CONFLICT : null,
    production_authority: !blocked,
  };
}
