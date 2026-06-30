import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import {
  COMMANDER_CALLOUT_DELIMITER,
  isCombinedCalloutDefect,
  serializeCallouts,
  splitCallouts,
  validateCalloutPool,
  validateSerializedCallouts,
} from '../src/callout-serializer.mjs';

const BAD_COMBINED =
  'Удалённо по России,,Выезд в Новосибирске,,Работа по договору,,Минимальный заказ 2 часа';

const VALID_FOUR = [
  'Удалённо по России',
  'Выезд в Новосибирске',
  'Работа по договору',
  'Минимальный заказ 2 часа',
];

describe('callout-serializer', () => {
  it('serializes separate callouts with Commander || delimiter', () => {
    const serialized = serializeCallouts(VALID_FOUR);
    assert.equal(
      serialized,
      'Удалённо по России||Выезд в Новосибирске||Работа по договору||Минимальный заказ 2 часа'
    );
    assert.equal(splitCallouts(serialized).length, 4);
    assert.equal(COMMANDER_CALLOUT_DELIMITER, '||');
  });

  it('rejects bad double-comma combined callout value', () => {
    assert.equal(isCombinedCalloutDefect(BAD_COMBINED), true);
    const violations = validateCalloutPool([{ text: BAD_COMBINED }]);
    assert.ok(violations.some((v) => v.code === 'COMBINED_CALLOUT_VALUE'));
    const serializedViolations = validateSerializedCallouts(BAD_COMBINED);
    assert.ok(serializedViolations.some((v) => v.code === 'COMBINED_CALLOUT_VALUE'));
  });

  it('accepts valid four-callout fixture as separate entries', () => {
    const violations = validateCalloutPool(VALID_FOUR.map((text) => ({ text })));
    assert.equal(violations.length, 0);
    const serialized = serializeCallouts(VALID_FOUR);
    assert.equal(validateSerializedCallouts(serialized).length, 0);
  });

  it('rejects callout length >25', () => {
    const violations = validateCalloutPool([{ text: 'x'.repeat(26) }]);
    assert.ok(violations.some((v) => v.code === 'CALLOUT_LENGTH'));
  });

  it('rejects empty callout', () => {
    const violations = validateCalloutPool([{ text: '   ' }]);
    assert.ok(violations.some((v) => v.code === 'EMPTY_CALLOUT'));
  });

  it('rejects duplicate callout after normalization', () => {
    const violations = validateCalloutPool([
      { text: 'Test Callout' },
      { text: 'test callout' },
    ]);
    assert.ok(violations.some((v) => v.code === 'DUPLICATE_CALLOUT'));
  });

  it('rejects wrong ;; delimiter serialization', () => {
    const wrong = VALID_FOUR.join(';;');
    assert.equal(isCombinedCalloutDefect(wrong), true);
    const violations = validateSerializedCallouts(wrong);
    assert.ok(violations.some((v) => v.code === 'COMBINED_CALLOUT_VALUE'));
  });
});
