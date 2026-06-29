import {
  APPROVED_AD_STATES,
  FORBIDDEN_ORGANIZATION_ID,
  FORBIDDEN_REGION_VALUES,
  GROUP_LIMIT_STOP_CODE,
  MAX_PHRASES_PER_GROUP,
  REQUIRED_ORGANIZATION_VALUE,
  REQUIRED_REGION_VALUE,
} from './constants.mjs';

/**
 * @param {import('./authority-loader.mjs').LoadedAuthority} loaded
 */
export function buildTransportModel(loaded) {
  const { byRole } = loaded;
  const phraseAllocation = byRole.phrase_allocation;
  const architecture = byRole.campaign_architecture;
  const primaryAds = byRole.primary_ads;
  const callouts = byRole.callouts;
  const campaignNegatives = byRole.campaign_negatives;
  const groupNegatives = byRole.group_negatives;
  const crossRules = byRole.cross_campaign_rules;
  const utmMap = byRole.utm_map;
  const campaignSettings = byRole.campaign_settings;
  const transportConfig = byRole.transport_config;

  return {
    phraseAllocation,
    architecture,
    primaryAds,
    callouts,
    campaignNegatives,
    groupNegatives,
    crossRules,
    utmMap,
    campaignSettings,
    transportConfig,
    displayPaths: loaded.byRole.display_paths,
    bids: loaded.byRole.bids ?? null,
    manifest: loaded.manifest,
    hashes: loaded.hashes,
  };
}

function normalizePhrase(s) {
  return String(s ?? '')
    .trim()
    .toLowerCase()
    .replace(/\s+/g, ' ');
}

function parseCampaignNegatives(negData, campaignId) {
  if (!negData?.layers) return [];
  const shared = (negData.layers.account_shared_deployable ?? []).map((t) => t.term);
  const campaign = (negData.layers.campaign_deployable ?? [])
    .filter((t) => t.campaign_id === campaignId)
    .map((t) => t.term);
  return [...shared, ...campaign];
}

function formatCommanderNegatives(terms) {
  return terms
    .filter((t) => t && String(t).trim())
    .map((t) => {
      const s = String(t).trim();
      return s.startsWith('-') ? s : `-${s.includes(' ') ? `"${s}"` : s}`;
    })
    .join(' ');
}

/**
 * @param {import('./authority-loader.mjs').LoadedAuthority} loaded
 */
export function validateTransport(loaded) {
  const violations = [];
  const warnings = [];
  const model = buildTransportModel(loaded);
  const campaignScope = new Set(loaded.manifest.campaign_scope);
  const groupPhraseCounts = {};

  const groups = model.architecture?.groups ?? [];
  const knownCampaignIds = new Set(groups.map((g) => g.campaign_id));
  const knownGroupIds = new Set(groups.map((g) => g.group_id));

  for (const cid of campaignScope) {
    if (!knownCampaignIds.has(cid)) {
      violations.push({
        code: 'UNKNOWN_CAMPAIGN_SCOPE',
        message: `Campaign scope references unknown campaign: ${cid}`,
        campaign_id: cid,
      });
    }
  }

  for (const g of groups) {
    if (!campaignScope.has(g.campaign_id)) {
      violations.push({
        code: 'GROUP_OUTSIDE_SCOPE',
        message: `Group ${g.group_id} campaign ${g.campaign_id} outside manifest scope`,
        campaign_id: g.campaign_id,
        group_id: g.group_id,
      });
    }
  }

  const deployablePhrases = (model.phraseAllocation?.records ?? []).filter(
    (r) => r.production_status === 'DEPLOYABLE'
  );

  const phrasesByGroup = new Map();
  const phrasesByCampaign = new Map();

  for (const rec of deployablePhrases) {
    const gid = rec.final_group;
    const cid = rec.final_campaign;
    if (!knownGroupIds.has(gid)) {
      violations.push({
        code: 'UNKNOWN_GROUP',
        message: `Phrase ${rec.phrase_id} assigned to unknown group ${gid}`,
        group_id: gid,
      });
      continue;
    }
    if (!knownCampaignIds.has(cid)) {
      violations.push({
        code: 'UNKNOWN_CAMPAIGN',
        message: `Phrase ${rec.phrase_id} assigned to unknown campaign ${cid}`,
        campaign_id: cid,
      });
      continue;
    }
    const groupMeta = groups.find((g) => g.group_id === gid);
    if (groupMeta && groupMeta.campaign_id !== cid) {
      violations.push({
        code: 'GROUP_CAMPAIGN_MISMATCH',
        message: `Phrase ${rec.phrase_id} campaign ${cid} does not match group ${gid} campaign ${groupMeta.campaign_id}`,
        campaign_id: cid,
        group_id: gid,
      });
    }

    if (!phrasesByGroup.has(gid)) phrasesByGroup.set(gid, []);
    phrasesByGroup.get(gid).push(rec);

    const campKey = cid;
    if (!phrasesByCampaign.has(campKey)) phrasesByCampaign.set(campKey, []);
    phrasesByCampaign.get(campKey).push(rec);
  }

  for (const g of groups) {
    if (!g.deployable && g.deployable !== undefined) continue;
    const phrases = phrasesByGroup.get(g.group_id) ?? [];
    const count = phrases.length || g.phrase_count || 0;
    groupPhraseCounts[g.group_id] = count;

    if (count === 0) {
      violations.push({
        code: 'EMPTY_GROUP',
        message: `Group ${g.group_id} has no deployable phrases`,
        campaign_id: g.campaign_id,
        group_id: g.group_id,
      });
    }

    if (count > MAX_PHRASES_PER_GROUP) {
      violations.push({
        code: 'GROUP_PHRASE_LIMIT',
        message: GROUP_LIMIT_STOP_CODE,
        campaign_id: g.campaign_id,
        group_id: g.group_id,
        actual_phrase_count: count,
        maximum_phrase_count: MAX_PHRASES_PER_GROUP,
      });
    }

    const seenInGroup = new Set();
    for (const p of phrases) {
      const norm = normalizePhrase(p.phrase);
      if (seenInGroup.has(norm)) {
        violations.push({
          code: 'DUPLICATE_PHRASE_IN_GROUP',
          message: `Duplicate phrase in group ${g.group_id}: ${p.phrase}`,
          group_id: g.group_id,
        });
      }
      seenInGroup.add(norm);
    }
  }

  for (const [cid, phrases] of phrasesByCampaign) {
    const seen = new Set();
    for (const p of phrases) {
      const norm = normalizePhrase(p.phrase);
      if (seen.has(norm)) {
        violations.push({
          code: 'DUPLICATE_PHRASE_IN_CAMPAIGN',
          message: `Duplicate phrase in campaign ${cid}: ${p.phrase}`,
          campaign_id: cid,
        });
      }
      seen.add(norm);
    }
  }

  const crossCampaignDuplicates = [];
  const globalPhraseMap = new Map();
  for (const rec of deployablePhrases) {
    const norm = normalizePhrase(rec.phrase);
    if (!globalPhraseMap.has(norm)) globalPhraseMap.set(norm, []);
    globalPhraseMap.get(norm).push({
      phrase: rec.phrase,
      campaign_id: rec.final_campaign,
      group_id: rec.final_group,
    });
  }
  for (const [norm, entries] of globalPhraseMap) {
    const campaigns = new Set(entries.map((e) => e.campaign_id));
    if (campaigns.size > 1) {
      crossCampaignDuplicates.push({ phrase: entries[0].phrase, entries });
      warnings.push({
        code: 'CROSS_CAMPAIGN_DUPLICATE',
        message: `Phrase "${entries[0].phrase}" appears in multiple campaigns (report only, not removed)`,
      });
    }
  }

  const ads = model.primaryAds?.ads ?? [];
  const adsByGroup = new Map();
  for (const ad of ads) {
    if (!adsByGroup.has(ad.group_id)) adsByGroup.set(ad.group_id, []);
    adsByGroup.get(ad.group_id).push(ad);
  }

  for (const g of groups) {
    const groupAds = adsByGroup.get(g.group_id) ?? [];
    if (groupAds.length === 0) {
      violations.push({
        code: 'MISSING_AD',
        message: `No primary ad for group ${g.group_id}`,
        group_id: g.group_id,
        campaign_id: g.campaign_id,
      });
    } else if (groupAds.length > 1) {
      violations.push({
        code: 'MULTIPLE_ADS',
        message: `Multiple primary ads for group ${g.group_id}: ${groupAds.length}`,
        group_id: g.group_id,
      });
    } else {
      const ad = groupAds[0];
      const status = ad.status ?? ad.operator_status ?? ad.primary_ad?.status;
      if (!APPROVED_AD_STATES.includes(status)) {
        violations.push({
          code: 'UNAPPROVED_AD',
          message: `Unapproved ad status for group ${g.group_id}: ${status}`,
          group_id: g.group_id,
        });
      }
    }
  }

  const geoRegion =
    model.transportConfig?.geo_region ?? REQUIRED_REGION_VALUE;
  const orgPolicy =
    model.transportConfig?.organization_policy?.required_value ??
    REQUIRED_ORGANIZATION_VALUE;

  if (FORBIDDEN_REGION_VALUES.includes(geoRegion) || geoRegion !== REQUIRED_REGION_VALUE) {
    violations.push({
      code: 'INVALID_REGION_AUTHORITY',
      message: `Invalid transport region authority: "${geoRegion}" (required "${REQUIRED_REGION_VALUE}")`,
    });
  }

  const campaignSettingsGeo =
    model.campaignSettings?.confirmed_boundary?.geography ??
    model.campaignSettings?.campaigns?.[0]?.geography;
  if (
    campaignSettingsGeo &&
    (campaignSettingsGeo.includes('Новосибирск и') ||
      campaignSettingsGeo === 'Все' ||
      campaignSettingsGeo !== REQUIRED_REGION_VALUE)
  ) {
    if (campaignSettingsGeo !== REQUIRED_REGION_VALUE) {
      violations.push({
        code: 'INVALID_REGION_CAMPAIGN_SETTINGS',
        message: `Campaign settings geography not transport-safe: "${campaignSettingsGeo}"`,
      });
    }
  }

  if (orgPolicy !== REQUIRED_ORGANIZATION_VALUE) {
    violations.push({
      code: 'NONBLANK_ORGANIZATION_POLICY',
      message: `Organization policy must be blank, got "${orgPolicy}"`,
    });
  }

  if (orgPolicy === FORBIDDEN_ORGANIZATION_ID) {
    violations.push({
      code: 'FORBIDDEN_ORGANIZATION_ID',
      message: `Forbidden organization ID in policy: ${FORBIDDEN_ORGANIZATION_ID}`,
    });
  }

  if (
    model.transportConfig?.forbidden_organization_ids?.includes(FORBIDDEN_ORGANIZATION_ID) ===
      false &&
    model.transportConfig
  ) {
    violations.push({
      code: 'MISSING_ORGANIZATION_POLICY',
      message: `Organization policy missing forbidden ID ${FORBIDDEN_ORGANIZATION_ID}`,
    });
  }

  if (!model.transportConfig?.organization_policy) {
    violations.push({
      code: 'MISSING_ORGANIZATION_POLICY',
      message: 'Transport config missing organization_policy block',
    });
  }

  const bidsData = model.bids?.campaign_bids ?? null;

  const utmSlugs = model.utmMap?.campaign_slugs ?? {};
  const groupSlugs = model.utmMap?.group_slugs ?? {};
  const calloutPools = model.callouts?.campaign_pools ?? {};

  for (const g of groups) {
    const phrases = phrasesByGroup.get(g.group_id) ?? [];
    const groupAds = adsByGroup.get(g.group_id) ?? [];
    const bid = bidsData?.[g.campaign_id];

    for (const p of phrases) {
      if (bid == null || bid === '') {
        violations.push({
          code: 'MISSING_BID',
          message: `Missing bid for phrase ${p.phrase_id} in campaign ${g.campaign_id}`,
          campaign_id: g.campaign_id,
          group_id: g.group_id,
        });
        break;
      }
    }

    if (groupAds.length === 1) {
      const ad = groupAds[0];
      const baseUrl = ad.landing_page?.url ?? ad.primary_ad?.landing_url ?? '';
      validateUrlUtm(
        violations,
        baseUrl,
        g.campaign_id,
        g.group_id,
        utmSlugs,
        groupSlugs,
        model.utmMap
      );
    }
  }

  for (const [cid, pool] of Object.entries(calloutPools)) {
    if (!campaignScope.has(cid)) continue;
    const texts = pool.map((c) => c.text);
    for (const ad of ads.filter((a) => a.campaign_id === cid)) {
      const calloutField = ad.callouts ?? ad.primary_ad?.callouts;
      if (calloutField) {
        for (const c of String(calloutField).split(';;')) {
          const t = c.trim();
          if (t && !texts.includes(t)) {
            violations.push({
              code: 'INVENTED_CALLOUT',
              message: `Callout not in approved pool for ${cid}: ${t}`,
              campaign_id: cid,
            });
          }
        }
      }
    }
  }

  validateNegatives(violations, warnings, model, groups, knownGroupIds, campaignScope);

  if (!model.groupNegatives) {
    violations.push({
      code: 'MISSING_GROUP_NEGATIVES',
      message: 'Group negatives authority file missing or not loaded',
    });
  }

  const crossDeployed =
    model.crossRules?.cross_campaign_negatives_deployed ??
    model.crossRules?.deployment_policy;
  if (
    model.crossRules &&
    model.crossRules.cross_campaign_negatives_deployed === 0 &&
    model.crossRules.operator_decision === 'NOT_DEPLOYED'
  ) {
    warnings.push({
      code: 'CROSS_CAMPAIGN_NOT_APPLIED',
      message: 'Cross-campaign negatives: NOT APPLIED',
    });
  } else if (!model.crossRules) {
    violations.push({
      code: 'MISSING_CROSS_CAMPAIGN_AUTHORITY',
      message: 'Cross-campaign rules authority missing',
    });
  }

  const sitelinksPolicy = model.transportConfig?.sitelinks_policy;
  if (sitelinksPolicy !== 'OMITTED' && model.transportConfig) {
    warnings.push({
      code: 'SITELINKS_NOT_OMITTED',
      message: `Sitelinks policy: ${sitelinksPolicy ?? 'UNSPECIFIED'}`,
    });
  }

  const stopLimit = violations.find((v) => v.code === 'GROUP_PHRASE_LIMIT');

  return {
    status: violations.length > 0 ? 'FAIL' : 'PASS',
    validated_at: new Date().toISOString(),
    stop_code: stopLimit ? GROUP_LIMIT_STOP_CODE : violations.length ? 'VALIDATION_FAILED' : null,
    violations,
    warnings,
    cross_campaign_duplicate_report: crossCampaignDuplicates,
    group_phrase_counts: groupPhraseCounts,
    model,
  };
}

function validateUrlUtm(violations, baseUrl, campaignId, groupId, utmSlugs, groupSlugs, utmMap) {
  if (!baseUrl) {
    violations.push({
      code: 'MISSING_URL',
      message: `Missing landing URL for group ${groupId}`,
      group_id: groupId,
    });
    return;
  }
  if (!baseUrl.startsWith('https://')) {
    violations.push({
      code: 'INVALID_URL',
      message: `URL must be https for group ${groupId}: ${baseUrl}`,
      group_id: groupId,
    });
  }
  if (baseUrl.includes('#') && !utmMap?.fragment_anchor_approved) {
    violations.push({
      code: 'UNAPPROVED_FRAGMENT',
      message: `Fragment anchor not approved for group ${groupId}`,
      group_id: groupId,
    });
  }

  const slug = utmSlugs[campaignId];
  const content = groupSlugs[groupId];
  if (!slug || !content) return;

  const suffix = `utm_source=yandex&utm_medium=cpc&utm_campaign=${slug}&utm_content=${content}`;
  if (baseUrl.includes('utm_term')) {
    violations.push({
      code: 'INVALID_UTM',
      message: `utm_term forbidden for group ${groupId}`,
      group_id: groupId,
    });
  }
  if (baseUrl.includes('{keyword}')) {
    violations.push({
      code: 'INVALID_UTM',
      message: `{keyword} macro forbidden for group ${groupId}`,
      group_id: groupId,
    });
  }
}

function validateNegatives(violations, warnings, model, groups, knownGroupIds, campaignScope) {
  const neg = model.campaignNegatives;
  if (!neg?.layers) return;

  const ca05Only = (neg.layers.campaign_deployable ?? [])
    .filter((t) => t.campaign_id === 'CA-05' && t.term === 'заказать коды маркировки')
    .map((t) => t.term);

  const collect = (arr, label) => {
    const seen = [];
    for (const item of arr ?? []) {
      const term = item.term ?? item;
      if (!term || !String(term).trim()) {
        violations.push({ code: 'EMPTY_NEGATIVE', message: `Empty negative in ${label}` });
        continue;
      }
      const norm = normalizePhrase(term);
      if (seen.includes(norm)) {
        violations.push({
          code: 'DUPLICATE_NEGATIVE',
          message: `Duplicate negative after normalization: ${term}`,
        });
      }
      seen.push(norm);
    }
  };

  collect(neg.layers.account_shared_deployable, 'account_shared');

  const byCampaign = new Map();
  for (const item of neg.layers.campaign_deployable ?? []) {
    const cid = item.campaign_id ?? 'UNKNOWN';
    if (!byCampaign.has(cid)) byCampaign.set(cid, []);
    byCampaign.get(cid).push(item);
  }
  for (const [cid, items] of byCampaign) {
    collect(items, `campaign:${cid}`);
  }

  for (const cid of campaignScope) {
    if (cid === 'CA-05') continue;
    const campaignNegs = parseCampaignNegatives(neg, cid);
    for (const t of ca05Only) {
      const formatted = formatCommanderNegatives([t]);
      if (campaignNegs.some((n) => normalizePhrase(n) === normalizePhrase(t))) {
        violations.push({
          code: 'CA05_NEGATIVE_LEAK',
          message: `CA-05-only negative "${t}" leaked into campaign ${cid}`,
          campaign_id: cid,
        });
      }
    }
  }

  const groupNeg = model.groupNegatives;
  if (groupNeg?.groups) {
    for (const [gid, data] of Object.entries(groupNeg.groups)) {
      if (!knownGroupIds.has(gid)) {
        violations.push({
          code: 'UNKNOWN_GROUP_NEGATIVE_REF',
          message: `Group negative references unknown group ${gid}`,
          group_id: gid,
        });
      }
      const terms = data.terms ?? data.negatives ?? [];
      collect(terms, `group:${gid}`);
    }
  }
}

export { normalizePhrase, formatCommanderNegatives, parseCampaignNegatives };
