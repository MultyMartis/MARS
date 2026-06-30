export const TRACKING_POLICY_GLOBAL =
  'GLOBAL_CAMPAIGN_PARAMETERS_SET_MANUALLY_BY_OPERATOR';

export const AD_URL_QUERY_FORBIDDEN = 'FORBIDDEN';

/**
 * @param {object} [transportConfig]
 */
export function isGlobalTrackingPolicy(transportConfig) {
  if (!transportConfig) return false;
  return (
    transportConfig.tracking_policy === TRACKING_POLICY_GLOBAL ||
    transportConfig.ad_url_query_parameters === AD_URL_QUERY_FORBIDDEN
  );
}

/**
 * Strip query string and fragment — preserve path including trailing slash.
 * @param {string} url
 */
export function cleanAdUrl(url) {
  const raw = String(url ?? '').trim();
  if (!raw) return '';
  return raw.split('#')[0].split('?')[0];
}

/**
 * @param {string} url
 * @param {object} [options]
 */
export function validateCleanAdUrl(url, options = {}) {
  const violations = [];
  const groupId = options.groupId;
  const campaignId = options.campaignId;
  const u = String(url ?? '').trim();

  if (!u) {
    violations.push({
      code: 'MISSING_URL',
      message: `Missing landing URL for group ${groupId}`,
      group_id: groupId,
      campaign_id: campaignId,
    });
    return violations;
  }

  if (!u.startsWith('https://')) {
    violations.push({
      code: 'INVALID_URL',
      message: `URL must be https for group ${groupId}: ${u}`,
      group_id: groupId,
      campaign_id: campaignId,
    });
  }

  if (u.includes('?')) {
    violations.push({
      code: 'URL_QUERY_FORBIDDEN',
      message: `Query string forbidden in ad URL for group ${groupId}: ${u}`,
      group_id: groupId,
      campaign_id: campaignId,
    });
  }

  if (u.includes('#')) {
    violations.push({
      code: 'URL_FRAGMENT_FORBIDDEN',
      message: `Fragment forbidden in ad URL for group ${groupId}: ${u}`,
      group_id: groupId,
      campaign_id: campaignId,
    });
  }

  if (u.includes('utm_')) {
    violations.push({
      code: 'UTM_IN_AD_URL',
      message: `utm_ parameters forbidden in ad URL for group ${groupId}`,
      group_id: groupId,
      campaign_id: campaignId,
    });
  }

  if (u.includes('{keyword}')) {
    violations.push({
      code: 'KEYWORD_MACRO_IN_URL',
      message: `{keyword} macro forbidden in ad URL for group ${groupId}`,
      group_id: groupId,
      campaign_id: campaignId,
    });
  }

  return violations;
}

/**
 * Policy-aware URL validation for transport pre-generation.
 * @param {string} baseUrl authority landing URL
 * @param {object} transportConfig
 * @param {object} [context]
 */
export function validateAdUrlForTransport(baseUrl, transportConfig, context = {}) {
  const { groupId, campaignId, utmMap } = context;

  if (isGlobalTrackingPolicy(transportConfig)) {
    const cleaned = cleanAdUrl(baseUrl);
    return validateCleanAdUrl(cleaned, { groupId, campaignId });
  }

  const violations = [];
  const u = String(baseUrl ?? '').trim();
  if (!u) {
    violations.push({
      code: 'MISSING_URL',
      message: `Missing landing URL for group ${groupId}`,
      group_id: groupId,
    });
    return violations;
  }

  if (!u.startsWith('https://')) {
    violations.push({
      code: 'INVALID_URL',
      message: `URL must be https for group ${groupId}: ${u}`,
      group_id: groupId,
    });
  }

  if (u.includes('#') && !utmMap?.fragment_anchor_approved) {
    violations.push({
      code: 'UNAPPROVED_FRAGMENT',
      message: `Fragment anchor not approved for group ${groupId}`,
      group_id: groupId,
    });
  }

  if (u.includes('utm_term')) {
    violations.push({
      code: 'INVALID_UTM',
      message: `utm_term forbidden for group ${groupId}`,
      group_id: groupId,
    });
  }

  if (u.includes('{keyword}')) {
    violations.push({
      code: 'INVALID_UTM',
      message: `{keyword} macro forbidden for group ${groupId}`,
      group_id: groupId,
    });
  }

  return violations;
}

/**
 * Resolve ad landing URL for Commander payload row.
 * @param {string} authorityUrl
 * @param {object} [transportConfig]
 * @param {object} [utmContext] — slug/content for legacy per-ad UTM injection
 */
export function resolveAdLandingUrl(authorityUrl, transportConfig, utmContext = {}) {
  const baseUrl = String(authorityUrl ?? '').trim();
  if (!baseUrl) return '';

  if (isGlobalTrackingPolicy(transportConfig)) {
    return cleanAdUrl(baseUrl);
  }

  const { campaignSlug, groupSlug } = utmContext;
  if (campaignSlug && groupSlug) {
    const sep = baseUrl.includes('?') ? '&' : '?';
    return `${baseUrl.split('#')[0]}${sep}utm_source=yandex&utm_medium=cpc&utm_campaign=${campaignSlug}&utm_content=${groupSlug}`;
  }

  return cleanAdUrl(baseUrl);
}
