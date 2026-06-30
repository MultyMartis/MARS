/**
 * Authority-to-artifact reconciliation — compares frozen authority counts/values to actual XLSX.
 */

import { validateArtifactXlsx } from './artifact-xlsx-validator.mjs';

/**
 * @param {object} authority — frozen authority summary
 * @param {string} xlsxPath
 * @param {object} [options]
 */
export async function reconcileAuthorityToArtifact(authority, xlsxPath, options = {}) {
  const differences = [];
  const expectations = {
    expected_campaign_count: authority.campaign_count,
    expected_group_count: authority.group_count,
    expected_phrase_count: authority.phrase_slot_count ?? authority.phrase_count,
    expected_ad_count: authority.ad_count,
    embedded_campaign_negatives_policy: authority.embedded_negative_policy ?? 'blank',
    metadata_policy: authority.metadata_policy,
    expected_metadata: authority.expected_metadata,
    forbidden_strings: authority.forbidden_strings,
    ...options,
  };

  const artifactResult = await validateArtifactXlsx(xlsxPath, {
    ...expectations,
    xlsxPath,
    filename: options.filename,
  });

  if (authority.campaign_count != null) {
    const actualGroups = artifactResult.evidence.find((e) => e.summary === 'tabular_counts');
    if (actualGroups) {
      if (authority.group_count != null && actualGroups.group_count !== authority.group_count) {
        differences.push({
          type: 'STRUCTURAL_CHANGE',
          field: 'group_count',
          authority: authority.group_count,
          artifact: actualGroups.group_count,
        });
      }
      if (authority.ad_count != null && actualGroups.ad_count !== authority.ad_count) {
        differences.push({
          type: 'STRUCTURAL_CHANGE',
          field: 'ad_count',
          authority: authority.ad_count,
          artifact: actualGroups.ad_count,
        });
      }
      if (
        authority.phrase_slot_count != null &&
        actualGroups.phrase_count !== authority.phrase_slot_count
      ) {
        differences.push({
          type: 'STRUCTURAL_CHANGE',
          field: 'phrase_slot_count',
          authority: authority.phrase_slot_count,
          artifact: actualGroups.phrase_count,
        });
      }
    }
  }

  for (const v of artifactResult.violations) {
    differences.push({
      type: 'UNEXPECTED_CHANGE',
      code: v.code,
      message: v.message,
      detail: v,
    });
  }

  return {
    status: differences.length === 0 ? 'RECONCILED' : 'RECONCILIATION_FAIL',
    script_status: differences.length === 0 ? 'SCRIPT_PASS' : 'SCRIPT_FAIL',
    differences,
    artifact_validation: artifactResult,
    reconciled_at: new Date().toISOString(),
  };
}

/**
 * Reconcile package-level authority manifest to all XLSX files.
 */
export async function reconcilePackage(authorityManifest, packageManifest, options = {}) {
  const results = [];
  const allDiffs = [];

  const xlsxFiles = (packageManifest.files ?? []).filter((f) =>
    String(f).toLowerCase().endsWith('.xlsx')
  );

  for (const file of xlsxFiles) {
    const fullPath = options.packageRoot
      ? `${options.packageRoot}/${file}`.replace(/\\/g, '/')
      : file;
    const perCampaign = authorityManifest.per_campaign?.[pathBasename(file)] ?? authorityManifest;
    const result = await reconcileAuthorityToArtifact(perCampaign, fullPath, {
      filename: pathBasename(file),
    });
    results.push({ file, result });
    allDiffs.push(...result.differences.map((d) => ({ file, ...d })));
  }

  return {
    status: allDiffs.length === 0 ? 'RECONCILED' : 'RECONCILIATION_FAIL',
    script_status: allDiffs.length === 0 ? 'SCRIPT_PASS' : 'SCRIPT_FAIL',
    results,
    differences: allDiffs,
  };
}

function pathBasename(p) {
  return String(p).split(/[/\\]/).pop();
}
