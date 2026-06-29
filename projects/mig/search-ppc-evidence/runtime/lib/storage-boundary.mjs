export const STORAGE_POLICY = {
  git_contains: [
    'contracts',
    'schemas',
    'manifests',
    'small fixtures',
    'indexes',
    'reports',
    'checksums',
    'sanitized examples',
  ],
  external_storage: [
    'large screenshots',
    'bulk HTML',
    'raw SERP captures',
    'browser profiles',
    'full corpus exports',
  ],
  forbidden_in_git: [
    'secrets',
    'cookies',
    'browser profiles',
    'uncontrolled third-party bulk data',
  ],
  default_external_roots: [
    'X:\\AI MARS STORAGE',
    'incoming/mig',
  ],
};

export function classifyArtifactPath(filePath, sizeBytes) {
  const lower = filePath.toLowerCase();
  if (/\.(png|jpg|webp)$/.test(lower) && sizeBytes > 500_000) return 'external_storage';
  if (/\.html$/.test(lower) && sizeBytes > 200_000) return 'external_storage';
  if (/cookie|secret|profile/i.test(lower)) return 'forbidden_in_git';
  if (/fixtures|schemas|contracts|reports/.test(lower)) return 'git_safe';
  return 'review_required';
}
