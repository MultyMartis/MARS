import {
  ROW_TYPE_AD,
  ROW_TYPE_KEYWORD,
  REQUIRED_REGION_VALUE,
} from './constants.mjs';
import {
  formatCommanderNegatives,
  parseCampaignNegatives,
  validateTransport,
} from './transport-validator.mjs';

/**
 * @param {import('./authority-loader.mjs').LoadedAuthority} loaded
 * @param {object} validationResult
 */
export function buildPayloads(loaded, validationResult) {
  if (validationResult.status !== 'PASS') {
    const err = new Error('Cannot build payload from failed validation');
    err.validation = validationResult;
    throw err;
  }

  const model = validationResult.model;
  const groups = model.architecture?.groups ?? [];
  const deployablePhrases = (model.phraseAllocation?.records ?? []).filter(
    (r) => r.production_status === 'DEPLOYABLE'
  );
  const ads = model.primaryAds?.ads ?? [];
  const bids = model.bids?.campaign_bids ?? {};
  const utmSlugs = model.utmMap?.campaign_slugs ?? {};
  const groupSlugs = model.utmMap?.group_slugs ?? {};
  const calloutPools = model.callouts?.campaign_pools ?? {};
  const displayPaths = model.displayPaths?.records ?? [];
  const geoRegion = model.transportConfig?.geo_region ?? REQUIRED_REGION_VALUE;

  const phrasesByGroup = new Map();
  for (const rec of deployablePhrases) {
    if (!phrasesByGroup.has(rec.final_group)) phrasesByGroup.set(rec.final_group, []);
    phrasesByGroup.get(rec.final_group).push(rec);
  }

  const adsByGroup = new Map();
  for (const ad of ads) {
    adsByGroup.set(ad.group_id, ad);
  }

  const displayByGroup = new Map();
  for (const dp of displayPaths) {
    displayByGroup.set(dp.group_id, dp.display_path);
  }

  const campaignIds = [...new Set(groups.map((g) => g.campaign_id))].sort();
  const payloads = [];

  for (const campaignId of campaignIds) {
    const campaignGroups = groups
      .filter((g) => g.campaign_id === campaignId)
      .sort((a, b) => a.group_id.localeCompare(b.group_id));

    const rows = [];
    let groupNumber = 1;

    const campaignNegTerms = parseCampaignNegatives(model.campaignNegatives, campaignId);
    const metadata_patches = {
      'Тип кампании:': 'Текстово-графическая кампания',
      '№ заказа:': 'RUB',
      'Минус-фразы на кампанию:': formatCommanderNegatives(campaignNegTerms),
      'Оптимизировать текст объявлений под запрос:': '0',
      'Организация из Яндекс Бизнеса:': '',
    };

    const promotionUrl = campaignGroups[0]
      ? (adsByGroup.get(campaignGroups[0].group_id)?.landing_page?.url ?? '')
      : '';
    if (promotionUrl) {
      metadata_patches['Объект продвижения:'] = promotionUrl.split('?')[0].split('#')[0];
    }

    for (const g of campaignGroups) {
      const ad = adsByGroup.get(g.group_id);
      const phrases = phrasesByGroup.get(g.group_id) ?? [];
      const pool = calloutPools[campaignId] ?? [];
      const calloutText = pool.map((c) => c.text).join(';;');
      const displayPath = displayByGroup.get(g.group_id) ?? '';
      const slug = utmSlugs[campaignId];
      const content = groupSlugs[g.group_id];
      const baseUrl = ad?.landing_page?.url ?? '';
      let landingUrl = baseUrl;
      if (baseUrl && slug && content) {
        const sep = baseUrl.includes('?') ? '&' : '?';
        landingUrl = `${baseUrl.split('#')[0]}${sep}utm_source=yandex&utm_medium=cpc&utm_campaign=${slug}&utm_content=${content}`;
      }

      const groupNegData = model.groupNegatives?.groups?.[g.group_id];
      const groupNegTerms = groupNegData?.terms ?? groupNegData?.negatives ?? [];
      const groupNegStr = formatCommanderNegatives(groupNegTerms);

      if (ad) {
        rows.push({
          row_type: ROW_TYPE_AD,
          group_name: g.group_name,
          group_number: String(groupNumber),
          group_id: g.group_id,
          group_additional_ad: '-',
          headline_1: ad.primary_ad?.headline ?? '',
          headline_2: ad.primary_ad?.additional_headline ?? '',
          text: ad.primary_ad?.text ?? '',
          landing_url: landingUrl,
          display_path: displayPath,
          ad_status: 'Активные',
          callouts: calloutText,
          group_negatives: groupNegStr,
          region: geoRegion,
          organization: '',
        });
      }

      for (const p of phrases) {
        rows.push({
          row_type: ROW_TYPE_KEYWORD,
          group_name: g.group_name,
          group_number: String(groupNumber),
          group_id: g.group_id,
          phrase: p.phrase,
          phrase_id: p.phrase_id,
          phrase_status: 'Активные',
          bid: bids[campaignId],
          region: geoRegion,
          organization: '',
        });
      }

      groupNumber += 1;
    }

    payloads.push({
      campaign_id: campaignId,
      geo_region: geoRegion,
      metadata_patches,
      rows,
      validation_receipt: {
        validated_at: validationResult.validated_at,
        status: validationResult.status,
        manifest_checkpoint: loaded.manifest.authority_checkpoint,
      },
      authority_hashes: { ...loaded.hashes },
    });
  }

  return payloads;
}

export function assertPayloadDeterminism(payloads) {
  const serialized = JSON.stringify(payloads);
  const copy = JSON.parse(serialized);
  return JSON.stringify(copy) === serialized;
}

export { validateTransport };
