/**
 * Selectable bid-assignment policies for Commander transport.
 *
 * Triumph canonical authority (preserved, not modified):
 * projects/orca/ppc/triumph-manipulator/tools/exporter-cli/bid-assignment-v1.3.js
 *
 * Corvonero large-group adaptation:
 * CORVONERO_BALANCED_CYCLIC_10_RUB_V1 — separate policy for 132–144 phrase groups.
 *
 * Human-operated export aid — NOT autobid.
 */

/** @typedef {'TRIUMPH_DYNAMIC_SPREAD_V1_3' | 'CORVONERO_BALANCED_CYCLIC_10_RUB_V1'} BidPolicyId */

export const BID_POLICIES = Object.freeze({
  TRIUMPH_DYNAMIC_SPREAD_V1_3: 'TRIUMPH_DYNAMIC_SPREAD_V1_3',
  CORVONERO_BALANCED_CYCLIC_10_RUB_V1: 'CORVONERO_BALANCED_CYCLIC_10_RUB_V1',
});

/** Primary Triumph policy constant (replaces legacy triumph-v1.3-descending-per-group). */
export const BID_LADDER_POLICY = BID_POLICIES.TRIUMPH_DYNAMIC_SPREAD_V1_3;

/** @deprecated Legacy alias — maps to TRIUMPH_DYNAMIC_SPREAD_V1_3 */
export const LEGACY_TRIUMPH_POLICY_ALIAS = 'triumph-v1.3-descending-per-group';

export const SUPPORTED_BID_POLICIES = Object.values(BID_POLICIES);

export const TRIUMPH_BID_AUTHORITY_RELATIVE =
  'projects/orca/ppc/triumph-manipulator/tools/exporter-cli/bid-assignment-v1.3.js';

/** Triumph SPREAD_MIN — minimum step between adjacent phrase bids (₽). */
export const BID_STEP_MIN = 10;

/** Triumph SPREAD_MAX — maximum within-group bid spread (₽). */
export const SPREAD_MAX = 90;

/** Corvonero cyclic ladder depth (values). */
export const CORVONERO_LADDER_VALUES = 10;

/** Triumph BID_MAX offset for single-phrase groups (600 → 580). */
export const SINGLE_PHRASE_OFFSET = 20;

/** Floor for any assigned bid (₽). */
export const ABSOLUTE_BID_MIN = 10;

/** Triumph reference range (documentation only — Corvonero uses campaign base). */
export const TRIUMPH_REFERENCE_BID_MIN = 400;
export const TRIUMPH_REFERENCE_BID_MAX = 600;

export const ASSIGNMENT_SCOPE = 'per_ad_group';
export const ASSIGNMENT_ORDER = 'primary_first_then_source_index_then_phrase_id';
export const CORVONERO_ASSIGNMENT_ORDER = 'CT4_AUTHORITY_ORDER';

/**
 * Resolve explicit bid policy from transport config. No implicit fallback.
 * @param {object} [transportConfig]
 * @returns {BidPolicyId}
 */
export function resolveBidPolicy(transportConfig) {
  const raw = transportConfig?.bid_policy ?? transportConfig?.bid_ladder_policy;
  if (!raw || String(raw).trim() === '') {
    const err = new Error('STOP — BID POLICY NOT EXPLICITLY SELECTED');
    err.code = 'BID_POLICY_NOT_EXPLICITLY_SELECTED';
    throw err;
  }
  if (raw === LEGACY_TRIUMPH_POLICY_ALIAS) {
    return BID_POLICIES.TRIUMPH_DYNAMIC_SPREAD_V1_3;
  }
  if (!SUPPORTED_BID_POLICIES.includes(raw)) {
    const err = new Error(`Unsupported bid policy: ${raw}`);
    err.code = 'UNSUPPORTED_BID_POLICY';
    throw err;
  }
  return raw;
}

/**
 * Stable phrase ordering — mirrors Triumph stableKeywordOrder / CT-4 authority order.
 * @param {object[]} phrases
 * @returns {object[]}
 */
export function stablePhraseOrder(phrases) {
  const indexed = (phrases || []).map((p, index) => ({ p, index }));
  indexed.sort((a, b) => {
    const ap = a.p.is_primary === true ? 0 : 1;
    const bp = b.p.is_primary === true ? 0 : 1;
    if (ap !== bp) return ap - bp;
    const aid = String(a.p.phrase_id ?? '');
    const bid = String(b.p.phrase_id ?? '');
    if (aid !== bid) return aid.localeCompare(bid);
    return a.index - b.index;
  });
  return indexed.map((x) => x.p);
}

/**
 * Build cyclic 10-RUB ladder from campaign base.
 * @param {number} campaignBaseBid
 * @param {number} [step]
 * @param {number} [depth]
 * @returns {number[]}
 */
export function buildCyclicLadder(campaignBaseBid, step = BID_STEP_MIN, depth = CORVONERO_LADDER_VALUES) {
  const base = Number(campaignBaseBid);
  const ladder = [];
  for (let i = 0; i < depth; i++) {
    ladder.push(base - i * step);
  }
  return ladder;
}

/**
 * Triumph v1.3 descending dynamic-spread assignment per group.
 * @param {object[]} phrases
 * @param {number} campaignBaseBid
 * @param {object} [options]
 * @returns {Map<string, number>}
 */
export function assignTriumphBidsForGroup(phrases, campaignBaseBid, options = {}) {
  const stepMin = options.bidStep ?? BID_STEP_MIN;
  const spreadMax = options.spreadMax ?? SPREAD_MAX;
  const absoluteMin = options.minimumBid ?? ABSOLUTE_BID_MIN;

  const ordered = stablePhraseOrder(phrases);
  const n = ordered.length;
  /** @type {Map<string, number>} */
  const bids = new Map();
  if (!n) return bids;

  const base = Number(campaignBaseBid);
  if (!Number.isFinite(base) || base <= 0) {
    throw new Error(`Invalid campaign base bid: ${campaignBaseBid}`);
  }

  if (n === 1) {
    const bid = Math.max(absoluteMin, Math.min(base, base - SINGLE_PHRASE_OFFSET));
    bids.set(phraseKey(ordered[0]), bid);
    return bids;
  }

  let step = Math.max(stepMin, Math.min(30, Math.floor(spreadMax / (n - 1))));
  let spread = step * (n - 1);
  if (spread > spreadMax) {
    step = Math.max(1, Math.floor(spreadMax / (n - 1)));
    spread = step * (n - 1);
  }
  if (spread < stepMin) {
    step = stepMin;
    spread = step * (n - 1);
  }

  const bidFloor = Math.max(absoluteMin, base - spreadMax);

  let groupMax = base;
  let groupMin = groupMax - spread;
  if (groupMin < bidFloor) {
    groupMin = bidFloor;
    groupMax = Math.min(base, groupMin + spread);
  }

  for (let i = 0; i < n; i++) {
    const bid = Math.round(groupMax - i * step);
    const clamped = Math.min(base, Math.max(bidFloor, bid));
    bids.set(phraseKey(ordered[i]), clamped);
  }

  const values = [...bids.values()];
  const unique = new Set(values);
  if (unique.size < n) {
    const retryStep = Math.max(step, stepMin + 1);
    for (let i = 0; i < n; i++) {
      const adjusted = Math.min(base, Math.max(bidFloor, groupMax - i * retryStep));
      bids.set(phraseKey(ordered[i]), adjusted);
    }
  }

  return bids;
}

/**
 * Corvonero balanced cyclic 10-RUB ladder — bid = ladder[index modulo depth].
 * @param {object[]} phrases
 * @param {number} campaignBaseBid
 * @param {object} [options]
 * @returns {Map<string, number>}
 */
export function assignCorvoneroCyclicBidsForGroup(phrases, campaignBaseBid, options = {}) {
  const step = options.bidStep ?? BID_STEP_MIN;
  const depth = options.ladderValues ?? CORVONERO_LADDER_VALUES;

  const base = Number(campaignBaseBid);
  if (!Number.isFinite(base) || base <= 0) {
    throw new Error(`Invalid campaign base bid: ${campaignBaseBid}`);
  }

  const ladder = buildCyclicLadder(base, step, depth);
  const ordered = stablePhraseOrder(phrases);
  /** @type {Map<string, number>} */
  const bids = new Map();

  for (let i = 0; i < ordered.length; i++) {
    bids.set(phraseKey(ordered[i]), ladder[i % depth]);
  }

  return bids;
}

/**
 * Policy-dispatching bid assignment per group.
 * @param {object[]} phrases
 * @param {number} campaignBaseBid
 * @param {object} [options]
 * @param {BidPolicyId} options.policy — required
 * @returns {Map<string, number>}
 */
export function assignBidsForGroup(phrases, campaignBaseBid, options = {}) {
  const policy = options.policy ?? BID_POLICIES.TRIUMPH_DYNAMIC_SPREAD_V1_3;
  switch (policy) {
    case BID_POLICIES.TRIUMPH_DYNAMIC_SPREAD_V1_3:
      return assignTriumphBidsForGroup(phrases, campaignBaseBid, options);
    case BID_POLICIES.CORVONERO_BALANCED_CYCLIC_10_RUB_V1:
      return assignCorvoneroCyclicBidsForGroup(phrases, campaignBaseBid, options);
    default:
      throw new Error(`Unsupported bid policy: ${policy}`);
  }
}

/**
 * @param {object[]} groups
 * @param {Map<string, object[]>} phrasesByGroup
 * @param {Record<string, number>} campaignBids
 * @param {object} [options]
 */
export function assignBidsForCampaign(groups, phrasesByGroup, campaignBids, options = {}) {
  const allBids = new Map();
  for (const g of groups) {
    const phrases = phrasesByGroup.get(g.group_id) ?? [];
    const baseBid = campaignBids[g.campaign_id];
    const groupBids = assignBidsForGroup(phrases, baseBid, options);
    for (const [id, bid] of groupBids) {
      allBids.set(id, bid);
    }
  }
  return allBids;
}

/**
 * Compute per-ladder-value usage counts and balance delta.
 * @param {number[]} values — bids in assignment order
 * @param {number[]} ladder
 */
export function computeLadderBalance(values, ladder) {
  const counts = new Map();
  for (const lv of ladder) counts.set(lv, 0);
  for (const v of values) {
    counts.set(v, (counts.get(v) ?? 0) + 1);
  }
  const countList = [...counts.values()];
  const maxCount = countList.length ? Math.max(...countList) : 0;
  const minCount = countList.length ? Math.min(...countList) : 0;
  const countPerBid = Object.fromEntries(
    ladder.map((lv) => [String(lv), counts.get(lv) ?? 0])
  );
  return {
    count_per_bid: countPerBid,
    maximum_repeated_count: maxCount,
    minimum_repeated_count: minCount,
    balance_delta: maxCount - minCount,
  };
}

/**
 * @param {object[]} groups
 * @param {Map<string, object[]>} phrasesByGroup
 * @param {Record<string, number>} campaignBids
 * @param {object} [options]
 */
export function buildBidDistributionReport(groups, phrasesByGroup, campaignBids, options = {}) {
  const policy = options.policy ?? BID_POLICIES.TRIUMPH_DYNAMIC_SPREAD_V1_3;
  const step = options.bidStep ?? BID_STEP_MIN;
  const depth = options.ladderValues ?? CORVONERO_LADDER_VALUES;
  const report = [];

  for (const g of groups) {
    const phrases = phrasesByGroup.get(g.group_id) ?? [];
    const baseBid = campaignBids[g.campaign_id];
    const ordered = stablePhraseOrder(phrases);
    const groupBids = assignBidsForGroup(phrases, baseBid, { ...options, policy });
    const values = ordered.map((p) => groupBids.get(phraseKey(p)));
    const distinct = new Set(values);
    const ladder =
      policy === BID_POLICIES.CORVONERO_BALANCED_CYCLIC_10_RUB_V1
        ? buildCyclicLadder(baseBid, step, depth)
        : null;
    const balance = ladder ? computeLadderBalance(values, ladder) : null;

    let duplicateBidCount = 0;
    const bidCounts = new Map();
    for (const v of values) {
      bidCounts.set(v, (bidCounts.get(v) ?? 0) + 1);
    }
    for (const c of bidCounts.values()) {
      if (c > 1) duplicateBidCount += c - 1;
    }

    report.push({
      campaign_id: g.campaign_id,
      group_id: g.group_id,
      phrase_count: phrases.length,
      base_bid: baseBid,
      bid_policy: policy,
      ladder_values: ladder,
      count_per_bid: balance?.count_per_bid ?? Object.fromEntries(bidCounts),
      distinct_bids: distinct.size,
      maximum_repeated_count: balance?.maximum_repeated_count ?? null,
      minimum_repeated_count: balance?.minimum_repeated_count ?? null,
      balance_delta: balance?.balance_delta ?? null,
      minimum_assigned_bid: values.length ? Math.min(...values) : null,
      maximum_assigned_bid: values.length ? Math.max(...values) : null,
      distinct_bid_count: distinct.size,
      duplicate_bid_count: duplicateBidCount,
      assignment_sequence_sample: ordered.slice(0, 5).map((p, i) => ({
        phrase_id: p.phrase_id,
        phrase: p.phrase,
        bid: groupBids.get(phraseKey(p)),
        position: i,
      })),
    });
  }
  return report;
}

/**
 * Triumph-specific group bid validation.
 */
export function validateTriumphGroupBids(bids, campaignBaseBid, phraseCount) {
  const errors = [];
  const values = [...bids.values()];
  const bidFloor = Math.max(ABSOLUTE_BID_MIN, campaignBaseBid - SPREAD_MAX);

  if (values.length !== phraseCount) {
    errors.push(`bid_count_mismatch:${values.length}/${phraseCount}`);
  }

  for (const v of values) {
    if (!Number.isFinite(v) || v <= 0) errors.push(`zero_or_invalid:${v}`);
    if (v > campaignBaseBid) errors.push(`above_base:${v}>${campaignBaseBid}`);
    if (v < bidFloor) errors.push(`below_floor:${v}<${bidFloor}`);
  }

  if (values.length > 1) {
    const unique = new Set(values);
    if (unique.size === 1) errors.push('flat_bids');
    const spread = Math.max(...values) - Math.min(...values);
    if (spread < BID_STEP_MIN) errors.push(`spread_too_low:${spread}`);
    if (spread > SPREAD_MAX) errors.push(`spread_too_high:${spread}`);
  }

  return errors;
}

/**
 * Corvonero cyclic ladder validation.
 * @param {Map<string, number>} bids
 * @param {object[]} phrases — original phrase records
 * @param {number} campaignBaseBid
 * @param {object} [options]
 */
export function validateCorvoneroGroupBids(bids, phrases, campaignBaseBid, options = {}) {
  const errors = [];
  const step = options.bidStep ?? BID_STEP_MIN;
  const depth = options.ladderValues ?? CORVONERO_LADDER_VALUES;
  const ladder = buildCyclicLadder(campaignBaseBid, step, depth);
  const ladderSet = new Set(ladder);
  const bidFloor = campaignBaseBid - step * (depth - 1);
  const ordered = stablePhraseOrder(phrases);
  const values = ordered.map((p) => bids.get(phraseKey(p)));

  if (values.length !== phrases.length) {
    errors.push(`bid_count_mismatch:${values.length}/${phrases.length}`);
  }

  for (const v of values) {
    if (!Number.isFinite(v) || v <= 0) errors.push(`zero_or_invalid:${v}`);
    if (!ladderSet.has(v)) errors.push(`not_on_ladder:${v}`);
    if (v > campaignBaseBid) errors.push(`above_base:${v}>${campaignBaseBid}`);
    if (v < bidFloor) errors.push(`below_floor:${v}<${bidFloor}`);
    if (v % 10 !== 0) errors.push(`not_multiple_of_10:${v}`);
  }

  if (ordered.length > 0) {
    const firstBid = bids.get(phraseKey(ordered[0]));
    if (firstBid !== campaignBaseBid) {
      errors.push(`first_phrase_not_base:${firstBid}!=${campaignBaseBid}`);
    }
  }

  for (let i = 0; i < ordered.length; i++) {
    const expected = ladder[i % depth];
    const actual = bids.get(phraseKey(ordered[i]));
    if (actual !== expected) {
      errors.push(`modulo_sequence_mismatch:idx${i}:${actual}!=${expected}`);
      break;
    }
  }

  const balance = computeLadderBalance(values, ladder);
  if (balance.balance_delta > 1) {
    errors.push(`unbalanced_distribution:delta=${balance.balance_delta}`);
  }

  if (phrases.length > 10) {
    const floorValue = ladder[ladder.length - 1];
    const floorCount = balance.count_per_bid[String(floorValue)] ?? 0;
    const maxAllowed = Math.ceil(phrases.length / depth);
    if (floorCount > maxAllowed) {
      errors.push(`floor_collapse:${floorValue}:${floorCount}>${maxAllowed}`);
    }
    const dominant = Object.entries(balance.count_per_bid).find(
      ([, count]) => count > maxAllowed
    );
    if (dominant) {
      errors.push(`floor_collapse_pattern:${dominant[0]}:${dominant[1]} rows`);
    }
  }

  return errors;
}

/**
 * Policy-dispatching validation.
 */
export function validateGroupBids(bids, campaignBaseBid, phraseCount, options = {}) {
  const policy = options.policy ?? BID_POLICIES.TRIUMPH_DYNAMIC_SPREAD_V1_3;
  if (policy === BID_POLICIES.CORVONERO_BALANCED_CYCLIC_10_RUB_V1) {
    return validateCorvoneroGroupBids(bids, options.phrases ?? [], campaignBaseBid, options);
  }
  return validateTriumphGroupBids(bids, campaignBaseBid, phraseCount);
}

/**
 * Verify assigned bids match recomputed ladder (determinism check).
 */
export function verifyBidLadderDeterminism(phrases, campaignBaseBid, assignedBids, options = {}) {
  const policy = options.policy ?? BID_POLICIES.TRIUMPH_DYNAMIC_SPREAD_V1_3;
  const expected = assignBidsForGroup(phrases, campaignBaseBid, { ...options, policy });
  const errors = [];
  for (const p of phrases) {
    const key = phraseKey(p);
    const exp = expected.get(key);
    const act = assignedBids.get(key);
    if (exp !== act) {
      errors.push(`determinism_mismatch:${key}:${act}!=${exp}`);
    }
  }
  return errors;
}

/** @param {object} phrase */
function phraseKey(phrase) {
  return String(phrase.phrase_id ?? phrase.phrase ?? '');
}
