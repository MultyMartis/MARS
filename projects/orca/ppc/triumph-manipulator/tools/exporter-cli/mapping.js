"use strict";

const MATCH_POLICY_MAP = Object.freeze({
  exact: "Exact",
  phrase: "Phrase",
  broad: "Broad",
});

const AD_STATUS_MAP = Object.freeze({
  draft: "Draft",
  active: "Active",
});

function stableSort(arr, keyFn) {
  return [...arr].sort((a, b) => {
    const ka = keyFn(a);
    const kb = keyFn(b);
    if (ka < kb) return -1;
    if (ka > kb) return 1;
    return 0;
  });
}

function mapMatchPolicy(policy) {
  return MATCH_POLICY_MAP[policy] || policy || "";
}

function mapAdStatus(status) {
  return AD_STATUS_MAP[status] || status || "";
}

function buildDisplayUrl(display) {
  if (!display || typeof display !== "object") return "";
  const domain = (display.domain || "").trim();
  const p1 = (display.path_1 || "").trim();
  const p2 = (display.path_2 || "").trim();
  if (!domain) return "";
  const pathPart = [p1, p2].filter(Boolean).join("/");
  return pathPart ? `${domain}/${pathPart}` : domain;
}

function joinExtensionField(items, field) {
  return items
    .map((item) => (item[field] || "").trim())
    .filter(Boolean)
    .join("||");
}

const TEMPLATE_FILL_JOIN = "||";

/**
 * Flat Commander "Тексты" rows: stable keyword×ad combinations per group.
 * Transport-only — no semantic rewriting, no match-type column (unsupported in template).
 */
function mapTemplateFillRows(document) {
  const fillRows = [];
  const campaigns = stableSort(document.campaigns || [], (c) =>
    String(c.campaign_id || c.campaign_name || "")
  );

  for (const campaign of campaigns) {
    const campaignId = campaign.campaign_id || "";
    const campaignName = campaign.campaign_name || "";

    const groups = stableSort(campaign.groups || [], (g) =>
      String(g.group_id || g.group_name || "")
    );

    for (const group of groups) {
      const groupName = group.group_name || "";
      const groupId = group.group_id || "";

      const keywords = stableSort(
        (group.keyword_cluster && group.keyword_cluster.keywords) || [],
        (k) => `${k.phrase || ""}\0${k.match_policy || ""}`
      );

      const ads = stableSort(group.ads || [], (a) => String(a.ad_id || ""));

      const kwList = keywords.length ? keywords : [null];
      const adList = ads.length ? ads : [null];

      for (const ad of adList) {
        const display = (ad && ad.display_url) || {};
        const fastlinks = ad ? stableSort(ad.fastlinks || [], (f) => `${f.title}\0${f.url}`) : [];
        const callouts = ad ? stableSort(ad.callouts || [], (c) => c.text || "") : [];

        const fastlinkTitles = joinExtensionField(fastlinks, "title");
        const fastlinkDescriptions = joinExtensionField(fastlinks, "description_1");
        const fastlinkUrls = joinExtensionField(fastlinks, "url");
        const calloutText = callouts
          .map((c) => (c.text || "").trim())
          .filter(Boolean)
          .join(TEMPLATE_FILL_JOIN);

        for (const kw of kwList) {
          const phrase = kw ? kw.phrase || "" : "";
          const rowKey = `fill:${campaignId}:${groupId}:${ad ? ad.ad_id : ""}:${phrase}`;

          fillRows.push({
            row_key: rowKey,
            campaign_id: campaignId,
            campaign_name: campaignName,
            group_id: groupId,
            group_name: groupName,
            phrase,
            keyword_status: kw ? kw.status || "" : "",
            headline_1: ad ? ad.headline_1 || "" : "",
            headline_2: ad ? ad.headline_2 || "" : "",
            description: ad ? ad.description || "" : "",
            landing_url: ad ? ad.landing_url || "" : "",
            display_url: ad ? buildDisplayUrl(display) : "",
            ad_status: ad ? mapAdStatus(ad.status) : "",
            ad_id: ad ? ad.ad_id || "" : "",
            fastlink_titles: fastlinkTitles,
            fastlink_descriptions: fastlinkDescriptions,
            fastlink_urls: fastlinkUrls,
            callouts: calloutText,
          });
        }
      }
    }
  }

  return fillRows;
}

/**
 * Deterministic row generation from OrcaPpcDocument.
 * Transport-only: verbatim copy, stable ordering, dedupe keys — no semantic rewriting.
 */
function mapDocument(document) {
  const campaignRows = [];
  const groupRows = [];
  const keywordRows = [];
  const adRows = [];
  const extensionRows = [];

  const seenKeywords = new Set();
  const seenAds = new Set();
  const seenExtensions = new Set();

  const campaigns = stableSort(document.campaigns || [], (c) =>
    String(c.campaign_id || c.campaign_name || "")
  );

  for (const campaign of campaigns) {
    const campaignName = campaign.campaign_name || "";
    const campaignId = campaign.campaign_id || "";

    campaignRows.push({
      row_key: `campaign:${campaignId}`,
      campaign_id: campaignId,
      campaign_name: campaignName,
      campaign_type: campaign.campaign_type || "search",
      primary_region: (campaign.geo && campaign.geo.primary_region) || "",
      strategy_label: (campaign.strategy && campaign.strategy.strategy_label) || "",
      bid_intent: (campaign.strategy && campaign.strategy.bid_intent) || "",
    });

    const groups = stableSort(campaign.groups || [], (g) =>
      String(g.group_id || g.group_name || "")
    );

    for (const group of groups) {
      const groupName = group.group_name || "";
      const groupId = group.group_id || "";
      const finalUrl =
        (group.landing_route && group.landing_route.final_url) || "";

      groupRows.push({
        row_key: `group:${campaignId}:${groupId}`,
        campaign_id: campaignId,
        campaign_name: campaignName,
        group_id: groupId,
        group_name: groupName,
        final_url: finalUrl,
      });

      const keywords = stableSort(
        (group.keyword_cluster && group.keyword_cluster.keywords) || [],
        (k) => `${k.phrase || ""}\0${k.match_policy || ""}`
      );

      for (const kw of keywords) {
        const phrase = kw.phrase || "";
        const dedupeKey = `${campaignId}|${groupId}|${phrase}|${kw.match_policy || ""}`;
        if (seenKeywords.has(dedupeKey)) continue;
        seenKeywords.add(dedupeKey);

        keywordRows.push({
          row_key: `keyword:${dedupeKey}`,
          campaign_id: campaignId,
          campaign_name: campaignName,
          group_id: groupId,
          group_name: groupName,
          phrase,
          match_type: mapMatchPolicy(kw.match_policy),
          status: kw.status || "",
          is_primary: kw.is_primary === true,
        });
      }

      const ads = stableSort(group.ads || [], (a) => String(a.ad_id || ""));

      for (const ad of ads) {
        const adId = ad.ad_id || "";
        const adDedupe = `${campaignId}|${groupId}|${adId}`;
        if (seenAds.has(adDedupe)) continue;
        seenAds.add(adDedupe);

        const display = ad.display_url || {};

        adRows.push({
          row_key: `ad:${adDedupe}`,
          campaign_id: campaignId,
          campaign_name: campaignName,
          group_id: groupId,
          group_name: groupName,
          ad_id: adId,
          headline_1: ad.headline_1 || "",
          headline_2: ad.headline_2 || "",
          description: ad.description || "",
          display_url_domain: display.domain || "",
          display_url_path_1: display.path_1 || "",
          display_url_path_2: display.path_2 || "",
          landing_url: ad.landing_url || "",
          ad_status: mapAdStatus(ad.status),
        });

        const fastlinks = stableSort(ad.fastlinks || [], (f) =>
          `${f.title || ""}\0${f.url || ""}`
        );
        for (let i = 0; i < fastlinks.length; i++) {
          const fl = fastlinks[i];
          const extKey = `fastlink:${adDedupe}:${fl.title || ""}:${fl.url || ""}:${i}`;
          if (seenExtensions.has(extKey)) continue;
          seenExtensions.add(extKey);

          extensionRows.push({
            row_key: extKey,
            extension_type: "fastlink",
            campaign_id: campaignId,
            campaign_name: campaignName,
            group_id: groupId,
            group_name: groupName,
            ad_id: adId,
            title: fl.title || "",
            url: fl.url || "",
            description_1: fl.description_1 || "",
            text: "",
          });
        }

        const callouts = stableSort(ad.callouts || [], (c) => c.text || "");
        for (let i = 0; i < callouts.length; i++) {
          const co = callouts[i];
          const extKey = `callout:${adDedupe}:${co.text || ""}:${i}`;
          if (seenExtensions.has(extKey)) continue;
          seenExtensions.add(extKey);

          extensionRows.push({
            row_key: extKey,
            extension_type: "callout",
            campaign_id: campaignId,
            campaign_name: campaignName,
            group_id: groupId,
            group_name: groupName,
            ad_id: adId,
            title: "",
            url: "",
            description_1: "",
            text: co.text || "",
          });
        }
      }
    }
  }

  const templateFillRows = mapTemplateFillRows(document);

  return {
    meta: {
      document_id: document.project_id || "",
      schema_version: document.schema_version || "",
      exporter_version: "orca-exporter-cli-prototype-v0",
      generated_at: new Date().toISOString(),
    },
    campaigns: campaignRows,
    groups: groupRows,
    keywords: keywordRows,
    ads: adRows,
    extensions: extensionRows,
    templateFillRows,
    counts: {
      campaigns: campaignRows.length,
      groups: groupRows.length,
      keywords: keywordRows.length,
      ads: adRows.length,
      extensions: extensionRows.length,
      template_fill_rows: templateFillRows.length,
    },
  };
}

module.exports = {
  mapDocument,
  mapTemplateFillRows,
  buildDisplayUrl,
  MATCH_POLICY_MAP,
  mapMatchPolicy,
  mapAdStatus,
  TEMPLATE_FILL_JOIN,
};
