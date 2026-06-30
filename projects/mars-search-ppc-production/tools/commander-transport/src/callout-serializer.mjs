/** Commander-native callout join delimiter (triumph exporter-cli TEMPLATE_FILL_JOIN). */
export const COMMANDER_CALLOUT_DELIMITER = '||';

export const MIN_CALLOUT_LENGTH = 1;
export const MAX_CALLOUT_LENGTH = 25;

export function normalizeCalloutText(text) {
  return String(text ?? '').trim();
}

/**
 * @param {string|{text?: string}} item
 */
export function calloutItemText(item) {
  if (typeof item === 'string') return normalizeCalloutText(item);
  return normalizeCalloutText(item?.text);
}

/**
 * Split serialized Commander callout cell value into individual callouts.
 * @param {string} serialized
 */
export function splitCallouts(serialized) {
  return String(serialized ?? '')
    .split(COMMANDER_CALLOUT_DELIMITER)
    .map(normalizeCalloutText)
    .filter(Boolean);
}

/**
 * Serialize approved callout pool for Commander XLSX column «Уточнения».
 * @param {Array<string|{text?: string}>} callouts
 */
export function serializeCallouts(callouts) {
  const texts = (Array.isArray(callouts) ? callouts : [])
    .map(calloutItemText)
    .filter(Boolean);
  return texts.join(COMMANDER_CALLOUT_DELIMITER);
}

/**
 * Detect a single combined callout value (wrong delimiter or over-length blob).
 * @param {string} value
 */
export function isCombinedCalloutDefect(value) {
  const s = normalizeCalloutText(value);
  if (!s) return false;

  if (s.includes(',,')) return true;
  if (s.includes(';;')) return true;

  if (s.includes(COMMANDER_CALLOUT_DELIMITER)) {
    const parts = splitCallouts(s);
    if (parts.length <= 1) return false;
    return parts.some((p) => p.length > MAX_CALLOUT_LENGTH);
  }

  return s.length > MAX_CALLOUT_LENGTH;
}

/**
 * @param {Array<string|{text?: string}>} callouts
 * @param {object} [options]
 */
export function validateCalloutPool(callouts, options = {}) {
  const violations = [];
  const campaignId = options.campaignId;
  const items = Array.isArray(callouts) ? callouts : [];
  const seen = new Set();

  for (const item of items) {
    const text = calloutItemText(item);
    if (!text) {
      violations.push({
        code: 'EMPTY_CALLOUT',
        message: 'Callout must be non-empty',
        campaign_id: campaignId,
      });
      continue;
    }
    if (text.length < MIN_CALLOUT_LENGTH || text.length > MAX_CALLOUT_LENGTH) {
      violations.push({
        code: 'CALLOUT_LENGTH',
        message: `Callout length ${text.length} outside 1–25: "${text}"`,
        campaign_id: campaignId,
      });
    }
    if (isCombinedCalloutDefect(text)) {
      violations.push({
        code: 'COMBINED_CALLOUT_VALUE',
        message: `Callout appears as combined value: "${text}"`,
        campaign_id: campaignId,
      });
    }
    const norm = text.toLowerCase();
    if (seen.has(norm)) {
      violations.push({
        code: 'DUPLICATE_CALLOUT',
        message: `Duplicate callout after normalization: "${text}"`,
        campaign_id: campaignId,
      });
    }
    seen.add(norm);
  }

  const serialized = serializeCallouts(items);
  if (serialized.startsWith(COMMANDER_CALLOUT_DELIMITER)) {
    violations.push({
      code: 'LEADING_CALLOUT_DELIMITER',
      message: 'Callout serialization has leading delimiter',
      campaign_id: campaignId,
    });
  }
  if (serialized.endsWith(COMMANDER_CALLOUT_DELIMITER)) {
    violations.push({
      code: 'TRAILING_CALLOUT_DELIMITER',
      message: 'Callout serialization has trailing delimiter',
      campaign_id: campaignId,
    });
  }
  if (serialized.includes(`${COMMANDER_CALLOUT_DELIMITER}${COMMANDER_CALLOUT_DELIMITER}`)) {
    violations.push({
      code: 'DOUBLE_DELIMITER_CALLOUT',
      message: 'Callout serialization has empty slot (double delimiter)',
      campaign_id: campaignId,
    });
  }

  return violations;
}

/**
 * Validate already-serialized callout cell content.
 * @param {string} serialized
 * @param {object} [options]
 */
export function validateSerializedCallouts(serialized, options = {}) {
  const campaignId = options.campaignId;
  const s = String(serialized ?? '').trim();
  if (!s) return [];

  if (s.includes(';;') || s.includes(',,')) {
    return [
      {
        code: 'COMBINED_CALLOUT_VALUE',
        message: `Serialized callout uses wrong delimiter: "${s}"`,
        campaign_id: campaignId,
      },
    ];
  }

  if (!s.includes(COMMANDER_CALLOUT_DELIMITER) && s.length > MAX_CALLOUT_LENGTH) {
    return [
      {
        code: 'COMBINED_CALLOUT_VALUE',
        message: `Single callout value exceeds ${MAX_CALLOUT_LENGTH} chars: "${s}"`,
        campaign_id: campaignId,
      },
    ];
  }

  return validateCalloutPool(splitCallouts(s).map((text) => ({ text })), { campaignId });
}
