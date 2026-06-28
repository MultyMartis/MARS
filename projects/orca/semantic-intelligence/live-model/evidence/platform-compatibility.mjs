/**
 * Platform/service compatibility — Wave 3.1F repair v2.
 * Project-independent: compares detected platform to business-scope-approved platforms.
 */
export const PLATFORM_COMPATIBILITY_VERSION = 'v1.1';

export const PLATFORM_CLASSIFICATION = {
  EXPLICIT_COMPATIBLE: 'EXPLICIT_COMPATIBLE',
  EXPLICIT_INCOMPATIBLE: 'EXPLICIT_INCOMPATIBLE',
  GENERIC_PLATFORM_FAMILY: 'GENERIC_PLATFORM_FAMILY',
  PLATFORM_UNKNOWN: 'PLATFORM_UNKNOWN',
};

const PLATFORM_PATTERNS = [
  { id: '1c', pattern: /(?:1[\s-]?с|1c|один[\s-]?эс)/i },
  { id: 'sap', pattern: /\bsap(?:\s+business\s+one)?\b/i },
  { id: 'dynamics', pattern: /(?:microsoft\s+)?dynamics(?:\s+365|\s+ax|\s+nav)?/i },
  { id: 'oracle', pattern: /oracle\s+(?:erp|ebs|cloud)/i },
  { id: 'bitrix', pattern: /bitrix(?:24)?/i },
  { id: 'autocad', pattern: /autocad/i },
  { id: 'photoshop', pattern: /(?:adobe\s+)?photoshop/i },
  { id: 'office', pattern: /microsoft\s+office/i },
];

const GENERIC_FAMILY_PATTERNS = [
  { id: 'erp', pattern: /\berp(?:\s+систем[аыуе])?\b/i },
  { id: 'corporate_accounting', pattern: /корпоративн(?:ая|ой|ую)\s+учетн(?:ая|ой|ую)\s+систем/i },
];

const SCOPE_PLATFORM_MAP = {
  '1c_services': ['1c'],
  '1c': ['1c'],
};

export function detectPlatforms(text) {
  const normalized = (text || '').toLowerCase();
  return PLATFORM_PATTERNS.filter(({ pattern }) => pattern.test(normalized)).map(({ id }) => id);
}

export function detectGenericPlatformFamily(text) {
  const normalized = (text || '').toLowerCase();
  return GENERIC_FAMILY_PATTERNS.filter(({ pattern }) => pattern.test(normalized)).map(({ id }) => id);
}

export function resolveApprovedPlatforms(businessScope, serviceRegistry) {
  const fromScope = SCOPE_PLATFORM_MAP[businessScope?.scope] || [];
  if (fromScope.length) return fromScope;

  const registryText = (serviceRegistry?.services || [])
    .map((s) => `${s.name || ''} ${s.description || ''}`)
    .join(' ')
    .toLowerCase();
  if (/(?:1[\s-]?с|1c|один[\s-]?эс)/i.test(registryText)) return ['1c'];
  return [];
}

export function classifyPlatformCompatibility(detected, approved, genericFamilies) {
  if (detected.length) {
    const compatible = detected.filter((p) => approved.includes(p));
    const incompatible = detected.filter((p) => !approved.includes(p));
    if (incompatible.length) {
      return PLATFORM_CLASSIFICATION.EXPLICIT_INCOMPATIBLE;
    }
    if (compatible.length) {
      return PLATFORM_CLASSIFICATION.EXPLICIT_COMPATIBLE;
    }
  }

  if (genericFamilies.length && !detected.length) {
    return PLATFORM_CLASSIFICATION.GENERIC_PLATFORM_FAMILY;
  }

  return PLATFORM_CLASSIFICATION.PLATFORM_UNKNOWN;
}

export function evaluatePlatformCompatibility(phrase, businessScope, serviceRegistry) {
  const text = phrase?.normalized_query || phrase?.raw_query || '';
  const detected = detectPlatforms(text);
  const genericFamilies = detectGenericPlatformFamily(text);
  const approved = resolveApprovedPlatforms(businessScope, serviceRegistry);
  const classification = classifyPlatformCompatibility(detected, approved, genericFamilies);

  if (!detected.length && !genericFamilies.length) {
    return {
      version: PLATFORM_COMPATIBILITY_VERSION,
      detected_platforms: [],
      generic_platform_families: [],
      approved_platforms: approved,
      classification: PLATFORM_CLASSIFICATION.PLATFORM_UNKNOWN,
      foreign_platform: false,
      platform_unspecified: true,
      generic_platform_family: false,
      incompatible_product_maintenance: false,
    };
  }

  const foreign = approved.length > 0 && detected.some((p) => !approved.includes(p));
  const genericOnly = genericFamilies.length > 0 && !detected.length;

  return {
    version: PLATFORM_COMPATIBILITY_VERSION,
    detected_platforms: detected,
    generic_platform_families: genericFamilies,
    approved_platforms: approved,
    classification,
    foreign_platform: foreign,
    platform_unspecified: !detected.length && !genericFamilies.length,
    generic_platform_family: genericOnly,
    incompatible_product_maintenance: foreign,
  };
}
