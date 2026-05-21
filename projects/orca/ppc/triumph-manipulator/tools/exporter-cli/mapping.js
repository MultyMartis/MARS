"use strict";

const MATCH_POLICY_MAP = Object.freeze({
  exact: "Exact",
  phrase: "Phrase",
  broad: "Broad",
});

/** v0.1: empty status — Commander applies defaults on import (literal enums SAFE UNKNOWN). */
const AD_STATUS_MAP = Object.freeze({
  draft: "",
  active: "",
});

const KEYWORD_STATUS_MAP = Object.freeze({
  active: "",
  paused: "",
  draft: "",
});

/** Readable group prefix separator (em dash + spaces). */
const GROUP_NAME_SEP = " — ";

/** Commander autotarget transport markers observed in template row 16. */
const AUTOTARGET_PHRASE_PATTERNS = [
  /^---\s*autotargeting\s*$/i,
  /^---\s*autotarget\s*$/i,
  /^---\s*autotargeting/i,
];

/** Commander template dictionary — probable search campaign literal. */
const CAMPAIGN_TYPE_COMMANDER_MAP = Object.freeze({
  search: "Единая перфоманс-кампания",
});

const TEMPLATE_FILL_JOIN = "||";

/** ORCA Triumph doctrine v0.2: transport up to 8 fastlinks per ad (combined Commander cells). */
const MAX_FASTLINKS_TRANSPORT = 8;

const PRODUCTION_DISPLAY_DOMAIN = "manipulator-triumph.ru";

/** Commander display URL field (col 49) — short path only, not landing URL. */
const DISPLAY_URL_MAX_CHARS = 20;
const DISPLAY_URL_WARN_CHARS = 18;
const DISPLAY_URL_ALLOWED_RE = /^[a-z0-9-]+$/;

/** Production landing slugs for fastlink routing discipline (v0.3). */
const PRODUCTION_LANDING_SLUGS = Object.freeze([
  "manipulyator-5-tonn",
  "perevozka-bytovok",
  "dostavka-stroymaterialov",
  "manipulyator-dlya-yurlic",
  "manipulyator-vezdehod",
]);

const CYRILLIC_TRANSLIT_MAP = Object.freeze({
  а: "a",
  б: "b",
  в: "v",
  г: "g",
  д: "d",
  е: "e",
  ё: "e",
  ж: "zh",
  з: "z",
  и: "i",
  й: "y",
  к: "k",
  л: "l",
  м: "m",
  н: "n",
  о: "o",
  п: "p",
  р: "r",
  с: "s",
  т: "t",
  у: "u",
  ф: "f",
  х: "h",
  ц: "ts",
  ч: "ch",
  ш: "sh",
  щ: "sch",
  ъ: "",
  ы: "y",
  ь: "",
  э: "e",
  ю: "yu",
  я: "ya",
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

function collapseWhitespace(text) {
  return String(text ?? "")
    .replace(/[\t\r\n]+/g, " ")
    .replace(/\s{2,}/g, " ")
    .trim();
}

/**
 * Deterministic Commander-safe text normalization (v0.4).
 * Replaces transport-problematic Unicode symbols; preserves Cyrillic.
 */
function normalizeTransportText(text) {
  let s = String(text ?? "");
  s = s.replace(/\u00D7/g, "x");
  s = s.replace(/[\u2013\u2014]/g, "-");
  s = s.replace(/\u00A0/g, " ");
  return collapseWhitespace(s);
}

/**
 * Commander col 52 «Регион» — single parent label for Triumph search-only fixture (v0.6).
 * Operator-confirmed via direct.xlsx: «Краснодарский край» only — not city, not multi-line.
 */
const TRIUMPH_GEO_REGION_TRANSPORT = "Краснодарский край";

/**
 * Commander col 52 «Регион» — stable krai label for all Triumph export rows.
 */
function buildGeoRegionForTransport(_geo) {
  return TRIUMPH_GEO_REGION_TRANSPORT;
}

/** Search-only export: Commander dictionary literal for col 2 «Тип объявления». */
const SEARCH_ONLY_AD_TYPE_TRANSPORT = "Текстово-графическое";

function mapMatchPolicy(policy) {
  return MATCH_POLICY_MAP[policy] || policy || "";
}

function mapAdStatus(status) {
  const key = String(status || "").toLowerCase();
  if (Object.prototype.hasOwnProperty.call(AD_STATUS_MAP, key)) {
    return AD_STATUS_MAP[key];
  }
  return "";
}

function mapKeywordStatus(status) {
  const key = String(status || "").toLowerCase();
  if (Object.prototype.hasOwnProperty.call(KEYWORD_STATUS_MAP, key)) {
    return KEYWORD_STATUS_MAP[key];
  }
  return "";
}

function isAutotargetPhrase(phrase) {
  const p = collapseWhitespace(phrase);
  if (!p) return false;
  return AUTOTARGET_PHRASE_PATTERNS.some((re) => re.test(p));
}

/**
 * Suppress Commander autotarget garbage phrases — never export transport markers.
 */
function normalizePhraseForTransport(phrase) {
  const p = collapseWhitespace(phrase);
  if (!p || isAutotargetPhrase(p)) return "";
  return p;
}

/**
 * Deterministic readable group naming for Commander import.
 * - UTF-8 safe string ops only
 * - Normalizes separators to «NN — Title»
 * - Strips machine suffixes (_grp, duplicate prefixes)
 * - Does NOT truncate for length
 */
function normalizeGroupName(rawName, groupOrdinal) {
  let name = collapseWhitespace(rawName);
  if (!name) {
    if (groupOrdinal) {
      return `${String(groupOrdinal).padStart(2, "0")}${GROUP_NAME_SEP}Группа`;
    }
    return "";
  }

  name = name.replace(/_+grp$/i, "").replace(/__+/g, " ").replace(/_+/g, " ");

  const prefixed = name.match(/^(\d{1,2})\s*[_\-–—]+\s*(.+)$/);
  if (prefixed) {
    const num = prefixed[1].padStart(2, "0");
    const title = collapseWhitespace(prefixed[2]);
    name = `${num}${GROUP_NAME_SEP}${title}`;
  } else if (groupOrdinal && !/^\d{2}\s*—\s*.+/.test(name)) {
    const num = String(groupOrdinal).padStart(2, "0");
    name = `${num}${GROUP_NAME_SEP}${name}`;
  }

  name = name.replace(/\s*—\s*/g, GROUP_NAME_SEP);
  name = name.replace(/^(\d{2}\s*—\s*)(\d{2}\s*—\s*)+/, "$1");

  return name;
}

function transliterateToAscii(text) {
  let out = "";
  const lower = String(text ?? "").toLowerCase();
  for (const ch of lower) {
    if (CYRILLIC_TRANSLIT_MAP[ch] !== undefined) {
      out += CYRILLIC_TRANSLIT_MAP[ch];
      continue;
    }
    const code = ch.charCodeAt(0);
    if ((code >= 97 && code <= 122) || (code >= 48 && code <= 57) || ch === "-") {
      out += ch;
    } else if (/\s|_/.test(ch)) {
      out += "-";
    }
  }
  return out;
}

function stripDisplayPathInput(raw) {
  let s = collapseWhitespace(raw).toLowerCase();
  s = s.replace(/^https?:\/\//i, "");
  s = s.replace(/^www\./i, "");
  s = s.replace(/^[a-z0-9][a-z0-9.-]*\.[a-z]{2,}\/?/i, "");
  s = s.replace(/[/\\]+/g, "-");
  s = s.replace(/\.html?$/i, "");
  return s;
}

/**
 * Deterministic Commander display path: no domain, no slash, [a-z0-9-], max 20.
 * UTF-8 source → ASCII kebab-case. Does not mutate document — transport only.
 */
function normalizeDisplayPathForTransport(display) {
  if (!display || typeof display !== "object") return "";

  const explicit = collapseWhitespace(
    display.display_url_path || display.path_1 || ""
  );
  const p2 = collapseWhitespace(display.path_2 || "");
  let raw = explicit;
  if (!raw && p2) raw = p2;
  if (!raw) {
    const legacy = [collapseWhitespace(display.path_1 || ""), p2]
      .filter(Boolean)
      .join("-");
    raw = legacy;
  }
  if (!raw) return "";

  let path = transliterateToAscii(stripDisplayPathInput(raw));
  path = path.replace(/[^a-z0-9-]+/g, "-").replace(/-+/g, "-").replace(/^-|-$/g, "");
  if (!path) return "";
  if (path.length > DISPLAY_URL_MAX_CHARS) {
    path = path.slice(0, DISPLAY_URL_MAX_CHARS).replace(/-$/, "");
  }
  return path;
}

/**
 * Commander «Отображаемая ссылка» — short display path only (v0.3).
 * NOT landing URL; NOT domain/path composite.
 */
function buildDisplayUrl(display) {
  return normalizeDisplayPathForTransport(display);
}

function extractSlugFromLandingUrl(url) {
  const trimmed = collapseWhitespace(url || "");
  if (!trimmed) return "";
  try {
    const u = new URL(trimmed);
    const parts = u.pathname.split("/").filter(Boolean);
    return parts[parts.length - 1] || "";
  } catch {
    return "";
  }
}

function isProductionFastlinkUrl(url) {
  const slug = extractSlugFromLandingUrl(url);
  if (!slug) return false;
  return PRODUCTION_LANDING_SLUGS.includes(slug);
}

function joinExtensionField(items, field) {
  return items
    .map((item) => collapseWhitespace(item[field] || ""))
    .filter(Boolean)
    .join(TEMPLATE_FILL_JOIN);
}

/**
 * Stable sort, dedupe title+url and duplicate URLs, cap at MAX_FASTLINKS_TRANSPORT.
 * v0.3: prefer landing slugs from production route table; drop duplicate URL slots.
 */
function normalizeFastlinksForTransport(fastlinks) {
  const sorted = stableSort(fastlinks || [], (f) => {
    const url = collapseWhitespace(f.url || "");
    const slugKnown = isProductionFastlinkUrl(url) ? "0" : "1";
    return `${slugKnown}\0${collapseWhitespace(f.title || "")}\0${url}`;
  });
  const seenPairs = new Set();
  const seenUrls = new Set();
  const out = [];
  for (const fl of sorted) {
    const title = collapseWhitespace(fl.title || "");
    const url = collapseWhitespace(fl.url || "");
    if (!title) continue;
    const pairKey = `${title.toLocaleLowerCase("ru-RU")}\0${url.toLocaleLowerCase("ru-RU")}`;
    if (seenPairs.has(pairKey)) continue;
    if (url) {
      const urlKey = url.toLocaleLowerCase("ru-RU");
      if (seenUrls.has(urlKey)) continue;
      seenUrls.add(urlKey);
    }
    seenPairs.add(pairKey);
    out.push({
      ...fl,
      title,
      url,
      description_1: collapseWhitespace(fl.description_1 || fl.description || ""),
    });
    if (out.length >= MAX_FASTLINKS_TRANSPORT) break;
  }
  return out;
}

function formatCampaignNegativesForTransport(keywords) {
  if (!Array.isArray(keywords) || !keywords.length) return "";
  return keywords
    .map((k) => {
      const word = collapseWhitespace(typeof k === "string" ? k : k.phrase || k.keyword || "");
      if (!word) return "";
      return word.startsWith("-") ? word : `-${word}`;
    })
    .filter(Boolean)
    .join(" ");
}

/**
 * Campaign metadata block values for sheet1 rows 7–12 (verified cell positions).
 * NOT semantic campaign editing — transport normalization only.
 */
function buildCampaignMetadataPatches(document) {
  const campaign = (document.campaigns || [])[0];
  if (!campaign) return {};

  const patches = {};
  const campaignType = campaign.campaign_type || "search";
  if (CAMPAIGN_TYPE_COMMANDER_MAP[campaignType]) {
    patches["campaigns.campaign_type"] = CAMPAIGN_TYPE_COMMANDER_MAP[campaignType];
  }

  const negatives = campaign.campaign_negatives?.keywords;
  if (negatives?.length) {
    patches["campaigns.campaign_negatives"] = formatCampaignNegativesForTransport(negatives);
  }

  let promotionUrl = "";
  for (const group of campaign.groups || []) {
    const url = group.landing_route?.final_url;
    if (url) {
      promotionUrl = collapseWhitespace(url);
      break;
    }
    for (const ad of group.ads || []) {
      if (ad.landing_url) {
        promotionUrl = collapseWhitespace(ad.landing_url);
        break;
      }
    }
    if (promotionUrl) break;
  }
  if (promotionUrl) {
    patches["campaigns.promotion_url"] = promotionUrl;
  }

  return patches;
}

/**
 * Flat Commander "Тексты" rows: stable keyword×ad combinations per group.
 * v0.1: import-feedback normalization (group names, autotarget, status, group numbers).
 */
function mapTemplateFillRows(document) {
  const fillRows = [];
  const groupOrdinalByKey = new Map();
  let nextGroupOrdinal = 0;

  const documentGeo = document.geo || {};
  const defaultGeoRegion = buildGeoRegionForTransport(documentGeo);

  const campaigns = stableSort(document.campaigns || [], (c) =>
    String(c.campaign_id || c.campaign_name || "")
  );

  for (const campaign of campaigns) {
    const campaignId = campaign.campaign_id || "";
    const campaignName = campaign.campaign_name || "";
    const campaignGeoRegion =
      buildGeoRegionForTransport(campaign.geo || documentGeo) || defaultGeoRegion;

    const groups = stableSort(campaign.groups || [], (g) =>
      String(g.group_id || g.group_name || "")
    );

    for (const group of groups) {
      const groupKey = String(group.group_id || group.group_name || "");
      if (!groupOrdinalByKey.has(groupKey)) {
        nextGroupOrdinal += 1;
        groupOrdinalByKey.set(groupKey, nextGroupOrdinal);
      }
      const groupOrdinal = groupOrdinalByKey.get(groupKey);
      const groupName = normalizeTransportText(
        normalizeGroupName(group.group_name || "", groupOrdinal)
      );
      const groupId = group.group_id || "";
      const groupNumber = String(groupOrdinal);

      const keywords = stableSort(
        (group.keyword_cluster && group.keyword_cluster.keywords) || [],
        (k) => `${k.phrase || ""}\0${k.match_policy || ""}`
      );

      const ads = stableSort(group.ads || [], (a) => String(a.ad_id || ""));

      const kwList = keywords.length ? keywords : [null];
      const adList = ads.length ? ads : [null];

      for (const ad of adList) {
        const display = (ad && ad.display_url) || {};
        const fastlinks = ad ? normalizeFastlinksForTransport(ad.fastlinks) : [];
        const callouts = ad ? stableSort(ad.callouts || [], (c) => c.text || "") : [];

        const fastlinkTitles = fastlinks
          .map((f) => normalizeTransportText(f.title || ""))
          .filter(Boolean)
          .join(TEMPLATE_FILL_JOIN);
        const fastlinkDescriptions = fastlinks
          .map((f) => normalizeTransportText(f.description_1 || ""))
          .filter(Boolean)
          .join(TEMPLATE_FILL_JOIN);
        const fastlinkUrls = joinExtensionField(fastlinks, "url");
        const calloutText = callouts
          .map((c) => normalizeTransportText(c.text || ""))
          .filter(Boolean)
          .join(TEMPLATE_FILL_JOIN);

        for (const kw of kwList) {
          const phrase = kw
            ? normalizeTransportText(normalizePhraseForTransport(kw.phrase || ""))
            : "";
          const rowKey = `fill:${campaignId}:${groupId}:${ad ? ad.ad_id : ""}:${phrase}`;

          fillRows.push({
            row_key: rowKey,
            campaign_id: campaignId,
            campaign_name: campaignName,
            group_id: groupId,
            group_name: groupName,
            group_number: groupNumber,
            phrase,
            keyword_status: kw ? mapKeywordStatus(kw.status) : "",
            headline_1: ad ? normalizeTransportText(ad.headline_1 || "") : "",
            headline_2: ad ? normalizeTransportText(ad.headline_2 || "") : "",
            description: ad ? normalizeTransportText(ad.description || "") : "",
            geo_region: campaignGeoRegion,
            ad_type_transport: SEARCH_ONLY_AD_TYPE_TRANSPORT,
            landing_url: ad ? collapseWhitespace(ad.landing_url || "") : "",
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
 * Transport-only: stable ordering, dedupe keys — light normalization on group names for logical sheets.
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
  const groupOrdinalByKey = new Map();
  let nextGroupOrdinal = 0;

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
      const groupKey = String(group.group_id || group.group_name || "");
      if (!groupOrdinalByKey.has(groupKey)) {
        nextGroupOrdinal += 1;
        groupOrdinalByKey.set(groupKey, nextGroupOrdinal);
      }
      const groupOrdinal = groupOrdinalByKey.get(groupKey);
      const groupName = normalizeTransportText(
        normalizeGroupName(group.group_name || "", groupOrdinal)
      );
      const groupId = group.group_id || "";
      const finalUrl =
        (group.landing_route && group.landing_route.final_url) || "";

      groupRows.push({
        row_key: `group:${campaignId}:${groupId}`,
        campaign_id: campaignId,
        campaign_name: campaignName,
        group_id: groupId,
        group_name: groupName,
        group_number: String(groupOrdinal),
        final_url: finalUrl,
      });

      const keywords = stableSort(
        (group.keyword_cluster && group.keyword_cluster.keywords) || [],
        (k) => `${k.phrase || ""}\0${k.match_policy || ""}`
      );

      for (const kw of keywords) {
        const phrase = normalizePhraseForTransport(kw.phrase || "");
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
          status: mapKeywordStatus(kw.status),
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
          headline_1: collapseWhitespace(ad.headline_1 || ""),
          headline_2: collapseWhitespace(ad.headline_2 || ""),
          description: collapseWhitespace(ad.description || ""),
          display_url_domain: display.domain || "",
          display_url_path_1: display.path_1 || "",
          display_url_path_2: display.path_2 || "",
          landing_url: collapseWhitespace(ad.landing_url || ""),
          ad_status: mapAdStatus(ad.status),
        });

        const fastlinks = normalizeFastlinksForTransport(ad.fastlinks);
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
            title: collapseWhitespace(fl.title || ""),
            url: collapseWhitespace(fl.url || ""),
            description_1: collapseWhitespace(fl.description_1 || ""),
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
            text: collapseWhitespace(co.text || ""),
          });
        }
      }
    }
  }

  const templateFillRows = mapTemplateFillRows(document);
  const metadataPatches = buildCampaignMetadataPatches(document);

  return {
    meta: {
      document_id: document.project_id || "",
      schema_version: document.schema_version || "",
      exporter_version: "orca-exporter-cli-region-fix-v0.6",
      generated_at: new Date().toISOString(),
    },
    campaigns: campaignRows,
    groups: groupRows,
    keywords: keywordRows,
    ads: adRows,
    extensions: extensionRows,
    templateFillRows,
    metadataPatches,
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
  normalizeDisplayPathForTransport,
  buildCampaignMetadataPatches,
  buildGeoRegionForTransport,
  normalizeTransportText,
  normalizeGroupName,
  normalizePhraseForTransport,
  normalizeFastlinksForTransport,
  isProductionFastlinkUrl,
  extractSlugFromLandingUrl,
  isAutotargetPhrase,
  collapseWhitespace,
  formatCampaignNegativesForTransport,
  MATCH_POLICY_MAP,
  mapMatchPolicy,
  mapAdStatus,
  mapKeywordStatus,
  TEMPLATE_FILL_JOIN,
  MAX_FASTLINKS_TRANSPORT,
  DISPLAY_URL_MAX_CHARS,
  DISPLAY_URL_WARN_CHARS,
  DISPLAY_URL_ALLOWED_RE,
  PRODUCTION_DISPLAY_DOMAIN,
  PRODUCTION_LANDING_SLUGS,
  GROUP_NAME_SEP,
  AUTOTARGET_PHRASE_PATTERNS,
  CAMPAIGN_TYPE_COMMANDER_MAP,
  TRIUMPH_GEO_REGION_TRANSPORT,
  SEARCH_ONLY_AD_TYPE_TRANSPORT,
};
