/**
 * Three-state metadata operation model for Commander transport.
 * Distinguishes MISSING, PRESERVE, EXPLICIT_CLEAR, SET_VALUE without truthiness ambiguity.
 */

export const METADATA_OPERATIONS = Object.freeze({
  SET: 'set',
  CLEAR: 'clear',
  PRESERVE: 'preserve',
});

export const METADATA_OPERATION_STATES = Object.freeze({
  MISSING: 'missing',
  PRESERVE: 'preserve',
  EXPLICIT_CLEAR: 'explicit_clear',
  SET_VALUE: 'set_value',
});

const RUSSIAN_KEY_MAP = Object.freeze({
  'Тип кампании:': 'campaign_type',
  'Минус-фразы на кампанию:': 'campaign_negatives',
  'Оптимизировать текст объявлений под запрос:': 'optimize_text',
  'Объект продвижения:': 'promotion_url',
  '№ заказа:': 'currency',
  'Организация из Яндекс Бизнеса:': 'organization',
});

const LOGICAL_KEY_MAP = Object.freeze({
  campaign_type: 'campaigns.campaign_type',
  campaign_negatives: 'campaigns.campaign_negatives',
  optimize_text: 'campaigns.optimize_text',
  promotion_url: 'campaigns.promotion_url',
  currency: 'campaigns.currency',
  organization: 'campaigns.organization',
});

/**
 * Normalize a single metadata field declaration to typed operation.
 * @param {unknown} declaration — string | { operation, value? } | undefined
 * @param {object} [options]
 * @returns {{ state: string, operation: string|null, value: string|null, field: string }}
 */
export function resolveMetadataOperation(fieldKey, declaration, options = {}) {
  const missingBehavior = options.missingBehavior ?? METADATA_OPERATIONS.PRESERVE;

  if (declaration === undefined || declaration === null) {
    return {
      field: fieldKey,
      state:
        missingBehavior === METADATA_OPERATIONS.CLEAR
          ? METADATA_OPERATION_STATES.EXPLICIT_CLEAR
          : METADATA_OPERATION_STATES.MISSING,
      operation: missingBehavior === METADATA_OPERATIONS.CLEAR ? METADATA_OPERATIONS.CLEAR : null,
      value: null,
    };
  }

  if (typeof declaration === 'object' && declaration !== null && 'operation' in declaration) {
    const op = declaration.operation;
    if (op === METADATA_OPERATIONS.CLEAR) {
      return {
        field: fieldKey,
        state: METADATA_OPERATION_STATES.EXPLICIT_CLEAR,
        operation: METADATA_OPERATIONS.CLEAR,
        value: null,
      };
    }
    if (op === METADATA_OPERATIONS.PRESERVE) {
      return {
        field: fieldKey,
        state: METADATA_OPERATION_STATES.PRESERVE,
        operation: METADATA_OPERATIONS.PRESERVE,
        value: null,
      };
    }
    if (op === METADATA_OPERATIONS.SET) {
      return {
        field: fieldKey,
        state: METADATA_OPERATION_STATES.SET_VALUE,
        operation: METADATA_OPERATIONS.SET,
        value: declaration.value == null ? '' : String(declaration.value),
      };
    }
    throw new Error(`Unknown metadata operation for ${fieldKey}: ${op}`);
  }

  if (typeof declaration === 'string') {
    if (Object.prototype.hasOwnProperty.call({ '': 1 }, declaration)) {
      return {
        field: fieldKey,
        state: METADATA_OPERATION_STATES.EXPLICIT_CLEAR,
        operation: METADATA_OPERATIONS.CLEAR,
        value: null,
      };
    }
    return {
      field: fieldKey,
      state: METADATA_OPERATION_STATES.SET_VALUE,
      operation: METADATA_OPERATIONS.SET,
      value: declaration,
    };
  }

  throw new Error(`Invalid metadata declaration for ${fieldKey}`);
}

/**
 * Parse legacy Russian-key patches or typed operation map into resolved operations.
 * @param {Record<string, unknown>} rawPatches
 * @param {Record<string, { operation?: string, value?: string }>} [typedOverrides]
 */
export function parseMetadataPatchMap(rawPatches = {}, typedOverrides = {}) {
  const resolved = {};

  for (const [ruKey, fieldKey] of Object.entries(RUSSIAN_KEY_MAP)) {
    const fieldId = `campaigns.${fieldKey}`;
    if (typedOverrides[fieldId] !== undefined) {
      resolved[fieldId] = resolveMetadataOperation(fieldId, typedOverrides[fieldId]);
      continue;
    }
    if (Object.prototype.hasOwnProperty.call(rawPatches, ruKey)) {
      resolved[fieldId] = resolveMetadataOperation(fieldId, rawPatches[ruKey]);
    } else {
      resolved[fieldId] = resolveMetadataOperation(fieldId, undefined);
    }
  }

  return resolved;
}

/**
 * Convert resolved operations to Triumph patcher logical-key map.
 * Only SET operations produce patch values; CLEAR omits key (then explicit cell clear applies).
 * PRESERVE omits key so template value remains.
 * @param {Record<string, ReturnType<resolveMetadataOperation>>} resolved
 */
export function toLogicalMetadataPatches(resolved) {
  const out = {};
  for (const [fieldId, op] of Object.entries(resolved)) {
    const logicalKey = fieldId.startsWith('campaigns.') ? fieldId : `campaigns.${fieldId}`;
    if (op.state === METADATA_OPERATION_STATES.SET_VALUE) {
      out[logicalKey] = op.value ?? '';
    }
  }
  return out;
}

/**
 * Legacy adapter: Russian patches with explicit empty string = CLEAR not skip.
 * @deprecated Prefer typed operation map via parseMetadataPatchMap
 */
export function translateMetadataPatchesTyped(russianPatches) {
  const resolved = parseMetadataPatchMap(russianPatches);
  return toLogicalMetadataPatches(resolved);
}

export function shouldClearEmbeddedCampaignNegativesFromResolved(resolved) {
  const op = resolved['campaigns.campaign_negatives'];
  return op?.state === METADATA_OPERATION_STATES.EXPLICIT_CLEAR;
}

export function shouldClearOrganizationFromResolved(resolved) {
  const op = resolved['campaigns.organization'];
  return (
    op?.state === METADATA_OPERATION_STATES.EXPLICIT_CLEAR ||
    (op?.state === METADATA_OPERATION_STATES.SET_VALUE && op.value === '')
  );
}

export function buildMetadataOperationsFromPolicy(metadataPolicy = {}) {
  const typed = {};
  for (const [field, spec] of Object.entries(metadataPolicy)) {
    if (spec?.operation) {
      typed[field] = spec;
    } else if (spec?.classification === 'MUST_CLEAR') {
      typed[field] = { operation: METADATA_OPERATIONS.CLEAR };
    } else if (spec?.classification === 'MUST_SET' && spec.value !== undefined) {
      typed[field] = { operation: METADATA_OPERATIONS.SET, value: spec.value };
    } else if (spec?.classification === 'MAY_PRESERVE') {
      typed[field] = { operation: METADATA_OPERATIONS.PRESERVE };
    }
  }
  return typed;
}

export { RUSSIAN_KEY_MAP, LOGICAL_KEY_MAP };
