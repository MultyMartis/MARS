/**
 * Exact workflow name allowlist for MetaBOT SEO Content Agent Beta v14.
 * No broad matching by default — names must match exactly.
 */

export const DEFAULT_ALLOWLIST = Object.freeze([
  'SEO Content Agent Beta.v14 - Intake',
  'SEO Content Agent Beta.v14 - Worker',
  'SEO Content Agent Beta.v14 - Admin',
]);

/**
 * @param {string | undefined} namesArg - Pipe-separated override from CLI (--names "A|B|C")
 * @returns {string[]}
 */
export function resolveAllowlist(namesArg) {
  if (!namesArg || !String(namesArg).trim()) {
    return [...DEFAULT_ALLOWLIST];
  }
  return String(namesArg)
    .split('|')
    .map((n) => n.trim())
    .filter(Boolean);
}

/**
 * Slug for sanitized JSON filenames.
 * @param {string} workflowName
 * @returns {string}
 */
export function workflowNameToSlug(workflowName) {
  const slugMap = {
    'SEO Content Agent Beta.v14 - Intake': 'SEO-Content-Agent-Beta-v14-Intake',
    'SEO Content Agent Beta.v14 - Worker': 'SEO-Content-Agent-Beta-v14-Worker',
    'SEO Content Agent Beta.v14 - Admin': 'SEO-Content-Agent-Beta-v14-Admin',
  };
  if (slugMap[workflowName]) {
    return slugMap[workflowName];
  }
  return workflowName
    .replace(/[^a-zA-Z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}
