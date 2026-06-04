"use strict";

const PRICE_RE = /(?:₽|руб|рублей|\bот\s+\d+)/i;
const SPEED_RE = /(?:подач|минут|срочн|быстр|через\s+\d+\s*мин)/i;
const FLEET_RE = /(?:машин|автопарк|газел|тонн|кузов|единиц)/i;
const SCOPE_RE = /(?:переезд|межгород|вывоз|грузчик|доставк)/i;
const QUALITY_RE = /(?:опыт|профессион|аккурат|квалифиц)/i;
const CONVENIENCE_RE = /(?:приложен|онлайн|без рации|удобн)/i;
const B2B_RE = /(?:юридическ|ип\s|договор|для\s+юр)/i;
const APP_RE = /(?:скачать|app\s*store|google\s*play|мобильн(?:ое|ого)\s+прилож)/i;

/**
 * Rules-only offer category (no LLM). Returns enum from mig-landing-offer-model-v2.
 */
function classifyOfferCategory(text) {
  if (!text) {
    return "unknown";
  }
  const lower = text.toLowerCase();
  if (PRICE_RE.test(lower)) {
    return "price";
  }
  if (SPEED_RE.test(lower)) {
    return "speed";
  }
  if (FLEET_RE.test(lower)) {
    return "fleet";
  }
  if (SCOPE_RE.test(lower)) {
    return "scope";
  }
  if (APP_RE.test(lower)) {
    return "app_channel";
  }
  if (B2B_RE.test(lower)) {
    return "b2b";
  }
  if (QUALITY_RE.test(lower)) {
    return "quality";
  }
  if (CONVENIENCE_RE.test(lower)) {
    return "convenience";
  }
  return "unknown";
}

function hasDeliveryTimeTokens(text) {
  if (!text) {
    return false;
  }
  const lower = text.toLowerCase();
  return /(?:минут|24\s*\/\s*7|24\/7|круглосуточ|срочн|подач)/i.test(lower);
}

function hasPriceTokens(text) {
  return PRICE_RE.test(text || "");
}

function hasServiceCoverageTokens(text) {
  if (!text) {
    return false;
  }
  const lower = text.toLowerCase();
  return /(?:краснодар|край|межгород|город|регион|тонн|грузов|перевоз)/i.test(lower);
}

module.exports = {
  classifyOfferCategory,
  hasDeliveryTimeTokens,
  hasPriceTokens,
  hasServiceCoverageTokens,
};
