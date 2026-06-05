"use strict";

/**
 * Rules-only delivery promise detection (no inference).
 * Excludes pricing/tariff minute mentions that are not dispatch promises.
 */

const DELIVERY_POSITIVE_RE =
  /(?:\d+\s*минут|быстр\w*\s+подач|подач\w*\s+за\s+\d+\s*мин|через\s+\d+\s*мин|круглосуточ|24\s*\/\s*7|24\/7|срочн\w*\s+(?:вызов|подач|доставк)|оперативн\w*\s+доставк)/i;

const DELIVERY_EXCLUDE_RE =
  /(?:стоимост\w*\s+за\s+\d+\s*мин|расч(?:ита|ет)\w*[^.]{0,40}\d+\s*мин|в\s+часе\s+\d+\s*мин|фиксирован\w+\s+количеств\w+\s+минут|продолжительност\w+[^.]{0,60}\d+\s*мин|доплат\w+[^.]{0,60}\d+\s*мин)/i;

const CLAUSE_SPLIT_RE = /(?<=[.!?])\s+|(?=\s*[А-ЯA-Z][а-яa-z«])/;

function isDeliveryPromiseText(text) {
  if (!text || typeof text !== "string") {
    return false;
  }
  const trimmed = text.trim();
  if (!trimmed || DELIVERY_EXCLUDE_RE.test(trimmed)) {
    return false;
  }
  if (/\d+\s*минут/i.test(trimmed) && /(?:стоимост|расчит|рассчит)/i.test(trimmed)) {
    return false;
  }
  return DELIVERY_POSITIVE_RE.test(trimmed);
}

function hasDeliveryTimeTokens(text) {
  return isDeliveryPromiseText(text);
}

/**
 * Extract delivery-promise clauses from a longer blob (e.g. trust + rating composite).
 */
function extractDeliveryPromiseSegments(text) {
  if (!text) {
    return [];
  }
  const segments = [];
  const seen = new Set();

  function addSegment(segment) {
    const s = (segment || "").trim();
    if (!s || !isDeliveryPromiseText(s) || seen.has(s.toLowerCase())) {
      return;
    }
    seen.add(s.toLowerCase());
    segments.push(s);
  }

  const parts = text.split(CLAUSE_SPLIT_RE).map((p) => p.trim()).filter(Boolean);
  for (const part of parts) {
    if (isDeliveryPromiseText(part)) {
      addSegment(part);
    }
  }

  if (!segments.length && isDeliveryPromiseText(text)) {
    addSegment(text);
  }

  if (!segments.length) {
    const inline = text.match(
      /[^.!?]*(?:\d+\s*минут|быстр\w*\s+подач|подач\w*\s+за\s+\d+\s*минут?|через\s+\d+\s*мин|оперативн\w*\s+доставк[^.!?]*)/gi
    );
    for (const m of inline || []) {
      addSegment(m);
    }
  }

  return segments;
}

/**
 * Remaining text after removing delivery clauses (for trust/social routing).
 */
function stripDeliveryPromiseSegments(text) {
  if (!text) {
    return "";
  }
  const segments = extractDeliveryPromiseSegments(text);
  let remainder = text;
  for (const seg of segments) {
    remainder = remainder.replace(seg, " ").trim();
  }
  remainder = remainder.replace(/\s{2,}/g, " ").trim();
  if (remainder.length < 12) {
    return "";
  }
  return remainder;
}

module.exports = {
  isDeliveryPromiseText,
  hasDeliveryTimeTokens,
  extractDeliveryPromiseSegments,
  stripDeliveryPromiseSegments,
};
