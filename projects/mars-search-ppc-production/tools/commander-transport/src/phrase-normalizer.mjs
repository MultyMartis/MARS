/**
 * Deterministic phrase normalization for authority ↔ artifact slot keys.
 */
export function normalizePhrase(phrase) {
  return String(phrase ?? '')
    .toLowerCase()
    .trim()
    .replace(/\s+/g, ' ');
}

/**
 * Composite deployable slot key: campaign_id + mode + group_id + normalized_phrase.
 */
export function phraseSlotKey(campaignId, mode, groupId, phrase) {
  return `${campaignId}|${mode}|${groupId}|${normalizePhrase(phrase)}`;
}

export function parseCampaignMode(campaignId) {
  if (String(campaignId).endsWith('-LOCAL')) return 'LOCAL';
  if (String(campaignId).endsWith('-REMOTE')) return 'REMOTE';
  return '';
}
