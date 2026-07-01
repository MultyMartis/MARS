/**
 * Ad-copy validation against group intent, mode, and authority alignment.
 */

import { CHECK_SEVERITY } from './campaign-architecture-validator.mjs';

const HEADLINE_MAX = 56;
const TEXT_MAX = 81;

/**
 * @param {object} ad — { group_id, mode, headline_1, headline_2, text, landing_url, display_path_1, display_path_2, group_intent }
 * @param {object} [group]
 */
export function validateAdCopy(ad, group = {}) {
  const violations = [];
  const mode = (ad.mode ?? group.mode ?? '').toUpperCase();
  const h1 = String(ad.headline_1 ?? '');
  const text = String(ad.text ?? ad.ad_text ?? '');

  if (!h1.trim()) {
    violations.push({ code: 'MISSING_HEADLINE', severity: CHECK_SEVERITY.HARD_FAIL, message: 'Headline required' });
  }
  if (h1.length > HEADLINE_MAX) {
    violations.push({ code: 'HEADLINE_TOO_LONG', severity: CHECK_SEVERITY.HARD_FAIL, message: `Headline ${h1.length} > ${HEADLINE_MAX}` });
  }
  if (text.length > TEXT_MAX) {
    violations.push({ code: 'TEXT_TOO_LONG', severity: CHECK_SEVERITY.HARD_FAIL, message: `Text ${text.length} > ${TEXT_MAX}` });
  }

  const intent = String(group.group_intent ?? ad.group_intent ?? '').toLowerCase();
  if (intent && h1 && !sharesToken(h1, intent) && !sharesToken(text, intent)) {
    violations.push({
      code: 'HEADLINE_INTENT_MISMATCH',
      severity: CHECK_SEVERITY.WARNING,
      message: `Headline may not reflect group intent for ${ad.group_id}`,
    });
  }

  if (mode === 'LOCAL' && !/новосибирск|выезд|нск/i.test(`${h1} ${ad.headline_2 ?? ''} ${text}`)) {
    violations.push({
      code: 'LOCAL_PROPOSITION_MISSING',
      severity: CHECK_SEVERITY.OPERATOR_REVIEW,
      message: `LOCAL ad ${ad.group_id} lacks local proposition`,
    });
  }
  if (mode === 'REMOTE' && /выезд|новосибирск/i.test(text) && !/удалён|росси/i.test(text)) {
    violations.push({
      code: 'REMOTE_PROMISES_LOCAL_VISIT',
      severity: CHECK_SEVERITY.HARD_FAIL,
      message: `REMOTE ad ${ad.group_id} promises local visit without remote framing`,
    });
  }

  const unsupported = ['гарантируем', 'лучшие цены', '№1', 'бесплатно навсегда'];
  for (const claim of unsupported) {
    if (text.toLowerCase().includes(claim)) {
      violations.push({
        code: 'UNSUPPORTED_COMMERCIAL_CLAIM',
        severity: CHECK_SEVERITY.OPERATOR_REVIEW,
        message: `Possible unsupported claim "${claim}" in ${ad.group_id}`,
      });
    }
  }

  if (group.landing_url && ad.landing_url && group.landing_url !== ad.landing_url) {
    violations.push({
      code: 'LANDING_URL_MISMATCH',
      severity: CHECK_SEVERITY.HARD_FAIL,
      message: `Ad landing URL != group landing URL for ${ad.group_id}`,
    });
  }

  const hardFails = violations.filter((v) => v.severity === CHECK_SEVERITY.HARD_FAIL);
  return { status: hardFails.length === 0 ? 'PASS' : 'FAIL', violations };
}

function sharesToken(a, b) {
  const ta = new Set(a.toLowerCase().split(/\s+/).filter((w) => w.length > 3));
  const tb = new Set(b.toLowerCase().split(/\s+/).filter((w) => w.length > 3));
  for (const t of ta) if (tb.has(t)) return true;
  return false;
}

/**
 * @param {object} authorityAd
 * @param {object} artifactAd
 */
export function validateAuthorityArtifactEquality(authorityAd, artifactAd) {
  const violations = [];
  const fields = ['headline_1', 'headline_2', 'text', 'landing_url', 'display_path_1', 'display_path_2'];
  for (const f of fields) {
    const a = String(authorityAd[f] ?? '').trim();
    const b = String(artifactAd[f] ?? '').trim();
    if (a && b && a !== b) {
      violations.push({
        code: 'AUTHORITY_ARTIFACT_MISMATCH',
        field: f,
        severity: CHECK_SEVERITY.HARD_FAIL,
        message: `${f} mismatch for ${authorityAd.group_id ?? artifactAd.group_id}`,
      });
    }
  }
  return violations;
}
