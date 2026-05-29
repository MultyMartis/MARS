"use strict";

/**
 * Campaign metadata transport constants — triumph-manipulator-commander-template-v1.xlsx SoT.
 * Values verified from template rows 7–12 (2026-05-29 reverse engineering).
 * NOT semantic campaign editing — template fidelity transport only.
 */

/** Template row 11 col 5 — root promotion object, not per-route landing. */
const TRIUMPH_PROMOTION_URL_TRANSPORT = "https://manipulator-triumph.ru/";

/** Template row 7 col 8 — search-only placement marker. */
const TRIUMPH_PLACEMENT_TRANSPORT = "search";

/** Template row 8 col 8. */
const TRIUMPH_CURRENCY_TRANSPORT = "RUB";

/** Template row 10 col 5 — optimize ad text for query (disabled). */
const TRIUMPH_OPTIMIZE_TEXT_TRANSPORT = "0";

/** Template row 7 col 5 — unified performance campaign type. */
const TRIUMPH_CAMPAIGN_TYPE_TRANSPORT = "Единая перфоманс-кампания";

/**
 * Verified metadata block cell positions (sheet Тексты, value column).
 * Extends sheet1-xml-builder METADATA_CELL_MAP for v1.4 fidelity.
 */
const TEMPLATE_METADATA_CELL_MAP = Object.freeze({
  "campaigns.campaign_type": { row: 7, col: 5 },
  "campaigns.placement": { row: 7, col: 8 },
  "campaigns.currency": { row: 8, col: 8 },
  "campaigns.campaign_negatives": { row: 9, col: 5 },
  "campaigns.optimize_text": { row: 10, col: 5 },
  "campaigns.promotion_url": { row: 11, col: 5 },
});

/**
 * Build campaign metadata patches aligned with template v1 SoT.
 * @param {object} document — OrcaPpcDocument
 * @param {object} [options]
 * @param {function} [options.formatCampaignNegativesForTransport]
 */
function buildTemplateFidelityMetadataPatches(document, options = {}) {
  const formatNegatives =
    options.formatCampaignNegativesForTransport ||
    ((keywords) => {
      if (!Array.isArray(keywords) || !keywords.length) return "";
      return keywords
        .map((k) => {
          const word = String(typeof k === "string" ? k : k.phrase || k.keyword || "").trim();
          if (!word) return "";
          return word.startsWith("-") ? word : `-${word}`;
        })
        .filter(Boolean)
        .join(" ");
    });

  const campaign = (document.campaigns || [])[0];
  if (!campaign) return {};

  const patches = {};

  patches["campaigns.campaign_type"] = TRIUMPH_CAMPAIGN_TYPE_TRANSPORT;
  patches["campaigns.placement"] = TRIUMPH_PLACEMENT_TRANSPORT;
  patches["campaigns.currency"] = TRIUMPH_CURRENCY_TRANSPORT;
  patches["campaigns.optimize_text"] = TRIUMPH_OPTIMIZE_TEXT_TRANSPORT;
  patches["campaigns.promotion_url"] = TRIUMPH_PROMOTION_URL_TRANSPORT;

  const negatives = campaign.campaign_negatives?.keywords;
  if (negatives?.length) {
    patches["campaigns.campaign_negatives"] = formatNegatives(negatives);
  }

  return patches;
}

module.exports = {
  TRIUMPH_PROMOTION_URL_TRANSPORT,
  TRIUMPH_PLACEMENT_TRANSPORT,
  TRIUMPH_CURRENCY_TRANSPORT,
  TRIUMPH_OPTIMIZE_TEXT_TRANSPORT,
  TRIUMPH_CAMPAIGN_TYPE_TRANSPORT,
  TEMPLATE_METADATA_CELL_MAP,
  buildTemplateFidelityMetadataPatches,
};
