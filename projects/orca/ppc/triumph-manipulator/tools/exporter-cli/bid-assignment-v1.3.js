"use strict";

/**
 * Deterministic manual search bid assignment v1.3 (400–600 ₽, spread 10–90 per group).
 * Human-operated export aid — NOT autobid.
 */

const BID_MIN = 400;
const BID_MAX = 600;
const SPREAD_MIN = 10;
const SPREAD_MAX = 90;

function stableKeywordOrder(keywords) {
  const indexed = (keywords || []).map((kw, index) => ({ kw, index }));
  indexed.sort((a, b) => {
    const ap = a.kw.is_primary === true ? 0 : 1;
    const bp = b.kw.is_primary === true ? 0 : 1;
    if (ap !== bp) return ap - bp;
    return a.index - b.index;
  });
  return indexed.map((x) => x.kw);
}

/**
 * @param {object[]} keywords
 * @returns {Map<string, number>} phrase → bid (₽)
 */
function assignBidsForGroup(keywords) {
  const ordered = stableKeywordOrder(keywords);
  const n = ordered.length;
  const bids = new Map();
  if (!n) return bids;

  if (n === 1) {
    bids.set(ordered[0].phrase, 580);
    return bids;
  }

  let step = Math.max(SPREAD_MIN, Math.min(30, Math.floor(SPREAD_MAX / (n - 1))));
  let spread = step * (n - 1);
  if (spread > SPREAD_MAX) {
    step = Math.floor(SPREAD_MAX / (n - 1));
    spread = step * (n - 1);
  }
  if (spread < SPREAD_MIN) {
    step = SPREAD_MIN;
    spread = step * (n - 1);
  }

  let groupMax = BID_MAX;
  let groupMin = groupMax - spread;
  if (groupMin < BID_MIN) {
    groupMin = BID_MIN;
    groupMax = Math.min(BID_MAX, groupMin + spread);
  }

  for (let i = 0; i < n; i++) {
    const bid = Math.round(groupMax - i * step);
    const clamped = Math.min(BID_MAX, Math.max(BID_MIN, bid));
    bids.set(ordered[i].phrase, clamped);
  }

  const values = [...bids.values()];
  const unique = new Set(values);
  if (unique.size < n) {
    for (let i = 0; i < n; i++) {
      const adjusted = Math.min(BID_MAX, Math.max(BID_MIN, groupMax - i * Math.max(step, 11)));
      bids.set(ordered[i].phrase, adjusted);
    }
  }

  return bids;
}

function validateGroupBids(bids) {
  const values = [...bids.values()];
  const errors = [];
  if (!values.length) return errors;

  for (const v of values) {
    if (!Number.isFinite(v) || v <= 0) errors.push(`zero_or_invalid:${v}`);
    if (v < BID_MIN || v > BID_MAX) errors.push(`out_of_range:${v}`);
  }

  const unique = new Set(values);
  if (values.length > 1 && unique.size === 1) {
    errors.push("flat_bids");
  }

  if (values.length > 1) {
    const spread = Math.max(...values) - Math.min(...values);
    if (spread < SPREAD_MIN) errors.push(`spread_too_low:${spread}`);
    if (spread > SPREAD_MAX) errors.push(`spread_too_high:${spread}`);
  }

  return errors;
}

module.exports = {
  BID_MIN,
  BID_MAX,
  SPREAD_MIN,
  SPREAD_MAX,
  stableKeywordOrder,
  assignBidsForGroup,
  validateGroupBids,
};
