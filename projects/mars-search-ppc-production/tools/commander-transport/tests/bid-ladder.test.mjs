import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import {
  ABSOLUTE_BID_MIN,
  assignBidsForGroup,
  assignCorvoneroCyclicBidsForGroup,
  assignTriumphBidsForGroup,
  BID_LADDER_POLICY,
  BID_POLICIES,
  BID_STEP_MIN,
  buildBidDistributionReport,
  buildCyclicLadder,
  computeLadderBalance,
  CORVONERO_LADDER_VALUES,
  resolveBidPolicy,
  SPREAD_MAX,
  stablePhraseOrder,
  TRIUMPH_REFERENCE_BID_MAX,
  TRIUMPH_REFERENCE_BID_MIN,
  validateCorvoneroGroupBids,
  validateGroupBids,
  validateTriumphGroupBids,
  verifyBidLadderDeterminism,
} from '../src/bid-ladder.mjs';

function mkPhrase(id, extra = {}) {
  return { phrase_id: id, phrase: `phrase-${id}`, ...extra };
}

const TRIUMPH = BID_POLICIES.TRIUMPH_DYNAMIC_SPREAD_V1_3;
const CORVONERO = BID_POLICIES.CORVONERO_BALANCED_CYCLIC_10_RUB_V1;

describe('bid-ladder — explicit policy selection', () => {
  it('resolveBidPolicy throws when policy missing', () => {
    assert.throws(() => resolveBidPolicy({}), /BID POLICY NOT EXPLICITLY SELECTED/);
    assert.throws(() => resolveBidPolicy(null), /BID POLICY NOT EXPLICITLY SELECTED/);
  });

  it('resolveBidPolicy accepts supported policies', () => {
    assert.equal(resolveBidPolicy({ bid_policy: TRIUMPH }), TRIUMPH);
    assert.equal(resolveBidPolicy({ bid_policy: CORVONERO }), CORVONERO);
    assert.equal(
      resolveBidPolicy({ bid_ladder_policy: 'triumph-v1.3-descending-per-group' }),
      TRIUMPH
    );
  });
});

describe('bid-ladder — Triumph v1.3 preserved', () => {
  it('exposes triumph policy constants', () => {
    assert.equal(BID_LADDER_POLICY, TRIUMPH);
    assert.equal(BID_STEP_MIN, 10);
    assert.equal(SPREAD_MAX, 90);
    assert.equal(TRIUMPH_REFERENCE_BID_MIN, 400);
    assert.equal(TRIUMPH_REFERENCE_BID_MAX, 600);
  });

  it('matches Triumph reference algorithm for 5 phrases at base 600', () => {
    const phrases = [1, 2, 3, 4, 5].map((i) => mkPhrase(`P${i}`));
    const bids = assignTriumphBidsForGroup(phrases, TRIUMPH_REFERENCE_BID_MAX);
    const ordered = stablePhraseOrder(phrases);
    const values = ordered.map((p) => bids.get(p.phrase_id));
    assert.deepEqual(values, [600, 578, 556, 534, 512]);
    assert.equal(new Set(values).size, 5);
  });

  it('Triumph policy via assignBidsForGroup unchanged for small groups', () => {
    const phrases = [1, 2, 3, 4, 5].map((i) => mkPhrase(`P${i}`));
    const direct = assignTriumphBidsForGroup(phrases, TRIUMPH_REFERENCE_BID_MAX);
    const dispatched = assignBidsForGroup(phrases, TRIUMPH_REFERENCE_BID_MAX, { policy: TRIUMPH });
    assert.deepEqual([...direct.entries()], [...dispatched.entries()]);
  });

  it('single phrase gets base minus 20 offset under Triumph', () => {
    const bids = assignTriumphBidsForGroup([mkPhrase('P1')], 500);
    assert.equal(bids.get('P1'), 480);
    const bids400 = assignTriumphBidsForGroup([mkPhrase('P1')], 400);
    assert.equal(bids400.get('P1'), 380);
  });

  it('descending ladder with minimum step 10 for CA-01 base 500', () => {
    const phrases = [1, 2, 3, 4].map((i) => mkPhrase(`P${i}`));
    const bids = assignTriumphBidsForGroup(phrases, 500);
    const ordered = stablePhraseOrder(phrases);
    const seq = ordered.map((p) => bids.get(p.phrase_id));
    assert.deepEqual(seq, [500, 470, 440, 410]);
    for (const v of seq) {
      assert.ok(v <= 500);
      assert.ok(v >= ABSOLUTE_BID_MIN);
    }
  });

  it('validateTriumphGroupBids rejects flat multi-phrase groups', () => {
    const bids = new Map([
      ['P1', 500],
      ['P2', 500],
    ]);
    const errors = validateTriumphGroupBids(bids, 500, 2);
    assert.ok(errors.includes('flat_bids'));
  });
});

describe('bid-ladder — Corvonero cyclic 10-RUB', () => {
  it('builds CA-01 ladder from base 500', () => {
    assert.deepEqual(
      buildCyclicLadder(500, 10, 10),
      [500, 490, 480, 470, 460, 450, 440, 430, 420, 410]
    );
  });

  it('builds CA-02 ladder from base 400', () => {
    assert.deepEqual(
      buildCyclicLadder(400, 10, 10),
      [400, 390, 380, 370, 360, 350, 340, 330, 320, 310]
    );
  });

  it('assigns cyclic sequence modulo 10', () => {
    const phrases = Array.from({ length: 12 }, (_, i) => mkPhrase(`P${i}`));
    const bids = assignCorvoneroCyclicBidsForGroup(phrases, 500);
    const ordered = stablePhraseOrder(phrases);
    const seq = ordered.map((p) => bids.get(p.phrase_id));
    assert.deepEqual(seq, [500, 490, 480, 470, 460, 450, 440, 430, 420, 410, 500, 490]);
  });

  it('single phrase gets campaign base under Corvonero', () => {
    const bids = assignCorvoneroCyclicBidsForGroup([mkPhrase('P1')], 500);
    assert.equal(bids.get('P1'), 500);
    const bids400 = assignCorvoneroCyclicBidsForGroup([mkPhrase('P1')], 400);
    assert.equal(bids400.get('P1'), 400);
  });

  it('all values are multiples of 10', () => {
    for (const size of [1, 4, 7, 10, 11, 23, 132, 144, 201]) {
      const phrases = Array.from({ length: size }, (_, i) => mkPhrase(`P${String(i).padStart(3, '0')}`));
      const bids = assignCorvoneroCyclicBidsForGroup(phrases, 500);
      for (const v of bids.values()) {
        assert.equal(v % 10, 0, `size ${size} bid ${v}`);
      }
    }
  });

  it('restarts ladder per group independently', () => {
    const g1 = [mkPhrase('A1'), mkPhrase('A2')];
    const g2 = [mkPhrase('B1'), mkPhrase('B2')];
    const b1 = assignCorvoneroCyclicBidsForGroup(g1, 400);
    const b2 = assignCorvoneroCyclicBidsForGroup(g2, 400);
    assert.equal(b1.get('A1'), 400);
    assert.equal(b2.get('B1'), 400);
    assert.equal(b1.get('A2'), 390);
    assert.equal(b2.get('B2'), 390);
  });

  it('balanced distribution — balance delta <= 1', () => {
    for (const size of [1, 4, 7, 10, 11, 23, 132, 144, 201]) {
      const phrases = Array.from({ length: size }, (_, i) => mkPhrase(`P${String(i).padStart(3, '0')}`));
      const bids = assignCorvoneroCyclicBidsForGroup(phrases, 500);
      const ordered = stablePhraseOrder(phrases);
      const values = ordered.map((p) => bids.get(p.phrase_id));
      const ladder = buildCyclicLadder(500);
      const balance = computeLadderBalance(values, ladder);
      assert.ok(balance.balance_delta <= 1, `size ${size} delta ${balance.balance_delta}`);
    }
  });

  it('regression — group size 144 base 500 no floor collapse', () => {
    const phrases = Array.from({ length: 144 }, (_, i) => mkPhrase(`P${String(i).padStart(3, '0')}`));
    const bids = assignCorvoneroCyclicBidsForGroup(phrases, 500);
    const ordered = stablePhraseOrder(phrases);
    const values = ordered.map((p) => bids.get(p.phrase_id));
    const ladder = buildCyclicLadder(500);
    const balance = computeLadderBalance(values, ladder);

    assert.equal(balance.count_per_bid['500'], 15);
    assert.equal(balance.count_per_bid['490'], 15);
    assert.equal(balance.count_per_bid['480'], 15);
    assert.equal(balance.count_per_bid['470'], 15);
    for (const lv of ['460', '450', '440', '430', '420', '410']) {
      assert.equal(balance.count_per_bid[lv], 14);
    }
    assert.ok(balance.count_per_bid['410'] === 14 || balance.count_per_bid['410'] === 15);
    assert.ok(balance.count_per_bid['410'] < 20, '410 must not dominate (floor collapse)');

    const errors = validateCorvoneroGroupBids(bids, phrases, 500);
    assert.deepEqual(errors, []);
  });

  it('large group does not collapse to floor under Triumph (contrast)', () => {
    const phrases = Array.from({ length: 144 }, (_, i) => mkPhrase(`P${String(i).padStart(3, '0')}`));
    const triumphBids = assignTriumphBidsForGroup(phrases, 500);
    const values = [...triumphBids.values()];
    const floorCount = values.filter((v) => v === 410).length;
    assert.ok(floorCount > 100, 'Triumph collapses to floor for large groups');
  });

  it('is deterministic for same input', () => {
    const phrases = Array.from({ length: 8 }, (_, i) => mkPhrase(`P${i}`));
    const a = assignCorvoneroCyclicBidsForGroup(phrases, 500);
    const b = assignCorvoneroCyclicBidsForGroup(phrases, 500);
    assert.deepEqual([...a.entries()], [...b.entries()]);
  });

  it('verifyBidLadderDeterminism passes for Corvonero', () => {
    const phrases = [mkPhrase('P1'), mkPhrase('P2'), mkPhrase('P3')];
    const assigned = assignCorvoneroCyclicBidsForGroup(phrases, 400);
    const errors = verifyBidLadderDeterminism(phrases, 400, assigned, { policy: CORVONERO });
    assert.deepEqual(errors, []);
  });

  it('campaign base 400 cyclic ladder', () => {
    const phrases = [1, 2, 3, 4].map((i) => mkPhrase(`P${i}`));
    const bids = assignCorvoneroCyclicBidsForGroup(phrases, 400);
    const ordered = stablePhraseOrder(phrases);
    assert.deepEqual(
      ordered.map((p) => bids.get(p.phrase_id)),
      [400, 390, 380, 370]
    );
  });

  it('buildBidDistributionReport includes balance metrics for Corvonero', () => {
    const groups = [{ campaign_id: 'CA-01', group_id: 'g1' }];
    const phrases = Array.from({ length: 23 }, (_, i) => mkPhrase(`P${i}`));
    const phrasesByGroup = new Map([['g1', phrases]]);
    const report = buildBidDistributionReport(groups, phrasesByGroup, { 'CA-01': 500 }, {
      policy: CORVONERO,
      bidStep: 10,
      ladderValues: CORVONERO_LADDER_VALUES,
    });
    assert.equal(report.length, 1);
    assert.equal(report[0].balance_delta, 1);
    assert.equal(report[0].distinct_bids, 10);
    assert.ok(report[0].ladder_values.length === 10);
  });

  it('primary phrases sort before non-primary', () => {
    const phrases = [
      mkPhrase('P2', { is_primary: false }),
      mkPhrase('P1', { is_primary: true }),
      mkPhrase('P3'),
    ];
    const ordered = stablePhraseOrder(phrases);
    assert.equal(ordered[0].phrase_id, 'P1');
  });
});
