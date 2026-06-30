/**
 * Campaign release gate — mandatory shared gate before operator import.
 */

import fs from 'node:fs';
import path from 'node:path';
import { loadTemplateContract } from './template-sanitizer.mjs';
import { validateArtifactXlsx } from './artifact-xlsx-validator.mjs';
import { reconcileAuthorityToArtifact } from './authority-artifact-reconciler.mjs';
import {
  reconcilePackagePhraseSlots,
  resolveAuthorityPathsFromReceipt,
} from './phrase-slot-reconciler.mjs';
import { validateApprovalReceipt, loadApprovalReceipt } from './operator-approval-receipt.mjs';
import { verifyChecksumManifest } from './checksum-manifest.mjs';
import { scanTemplateContamination } from './template-sanitizer.mjs';
import { GATE_STATUS, SCRIPT_STATUS, deriveCurrentPhase } from './release-state.mjs';
import ExcelJS from 'exceljs';
import { validateTemplate } from './template-validator.mjs';

/**
 * @param {object} input
 */
export async function runReleaseGate(input) {
  const violations = [];
  const checks = [];
  let loadedReceipt = null;
  const fail = (code, message, detail = {}) => {
    violations.push({ code, message, ...detail });
    checks.push({ check: code, status: 'FAIL', message });
  };
  const pass = (code, message = '') => {
    checks.push({ check: code, status: 'PASS', message });
  };

  if (!input.project_id) fail('MISSING_PROJECT_ID', 'project_id required');
  if (!input.package_path && !input.package_root) {
    fail('MISSING_PACKAGE', 'package_path or package_root required');
  }
  if (!input.authority_path && !input.authority_summary) {
    fail('MISSING_AUTHORITY', 'authority_path or authority_summary required');
  }

  const packageRoot = input.package_root ?? input.package_path;

  const manifestXlsxFiles = loadPackageManifestXlsxFiles(packageRoot, input.package_manifest_path);

  if (input.receipt_path) {
    try {
      const receipt = loadApprovalReceipt(input.receipt_path);
      loadedReceipt = receipt;
      const receiptValidation = validateApprovalReceipt(receipt);
      if (!receiptValidation.valid) {
        for (const v of receiptValidation.violations) fail(v.code, v.message);
      } else {
        pass('operator_semantic_approval');
      }
    } catch (err) {
      fail('RECEIPT_LOAD_FAIL', err.message);
    }
  } else if (input.require_operator_approval !== false) {
    fail('MISSING_OPERATOR_RECEIPT', 'Operator semantic approval receipt required');
  }

  let authoritySummary = input.authority_summary;
  if (input.authority_path && fs.existsSync(input.authority_path)) {
    const auth = JSON.parse(fs.readFileSync(input.authority_path, 'utf8'));
    authoritySummary = {
      campaign_count: auth.campaign_count ?? auth.campaign_scope?.length,
      group_count: auth.group_count ?? auth.expected_counts?.groups,
      phrase_slot_count: auth.phrase_slot_count ?? auth.expected_counts?.phrase_slots,
      ad_count: auth.ad_count ?? auth.expected_counts?.ads,
      embedded_negative_policy: auth.embedded_negative_policy ?? 'blank',
      authority_frozen: auth.authority_frozen ?? auth.states?.AUTHORITY_FROZEN,
      ...authoritySummary,
    };
    if (!authoritySummary.authority_frozen && input.require_frozen_authority !== false) {
      fail('AUTHORITY_NOT_FROZEN', 'Authority must be frozen');
    } else if (authoritySummary.authority_frozen) {
      pass('authority_frozen');
    }
  }

  const contract = loadTemplateContract();
  pass('template_contract_loaded');

  if (input.template_path) {
    const templateResult = await validateTemplate(input.template_path, input.guardOptions ?? {});
    if (!templateResult.ok) {
      fail('TEMPLATE_INVALID', 'Template contract validation failed');
    } else {
      pass('template_contract_valid');
      const wb = new ExcelJS.Workbook();
      await wb.xlsx.readFile(input.template_path);
      const texts = wb.getWorksheet('Тексты');
      if (texts) {
        const contamination = scanTemplateContamination(texts, contract);
        if (contamination.contaminated) {
          pass('template_contamination_detected', `${contamination.findings.length} findings — sanitization required`);
        }
      }
    }
  }

  const xlsxFiles = input.xlsx_files ?? manifestXlsxFiles ?? findXlsxInPackage(packageRoot);
  if (xlsxFiles.length === 0) {
    fail('NO_XLSX_IN_PACKAGE', 'No XLSX files found in package');
  }

  const artifactResults = [];
  for (const xlsxRel of xlsxFiles) {
    const fullPath = path.isAbsolute(xlsxRel) ? xlsxRel : path.join(packageRoot, xlsxRel);
    if (!fs.existsSync(fullPath)) {
      fail('XLSX_MISSING', `XLSX not found: ${xlsxRel}`);
      continue;
    }

    const expectations = {
      embedded_campaign_negatives_policy: authoritySummary?.embedded_negative_policy ?? 'blank',
      forbidden_strings: input.forbidden_strings ?? contract.contamination_signatures?.stale_campaign_negatives,
      ...(input.per_xlsx_expectations?.[path.basename(fullPath)] ?? {}),
      ...(authoritySummary ?? {}),
    };

    const artifactResult = await validateArtifactXlsx(fullPath, expectations);
    artifactResults.push({ file: xlsxRel, result: artifactResult });

    if (artifactResult.status !== 'ARTIFACT_VALIDATED') {
      for (const v of artifactResult.violations) {
        fail(`ARTIFACT_${v.code}`, `${xlsxRel}: ${v.message}`, { file: xlsxRel });
      }
    } else {
      pass(`artifact_validated_${path.basename(fullPath)}`);
    }

    if (authoritySummary && input.enforce_per_file_package_totals === true) {
      const recon = await reconcileAuthorityToArtifact(authoritySummary, fullPath, {
        filename: path.basename(fullPath),
      });
      if (recon.status !== 'RECONCILED') {
        for (const d of recon.differences) {
          fail('RECONCILIATION_' + d.type, `${xlsxRel}: ${d.message ?? d.field}`, { file: xlsxRel });
        }
      }
    }
  }

  let phraseSlotReconciliation = null;
  const groupPlanPath =
    input.group_plan_path ??
    resolveAuthorityPathsFromReceipt(loadedReceipt ?? {}).group_plan_path;
  let architecturePath =
    input.architecture_path ??
    resolveAuthorityPathsFromReceipt(loadedReceipt ?? {}).architecture_path;

  if (groupPlanPath && fs.existsSync(groupPlanPath)) {
    const groupPlan = JSON.parse(fs.readFileSync(groupPlanPath, 'utf8'));
    const architecture = architecturePath && fs.existsSync(architecturePath)
      ? JSON.parse(fs.readFileSync(architecturePath, 'utf8'))
      : { groups: [] };

    phraseSlotReconciliation = await reconcilePackagePhraseSlots({
      group_plan: groupPlan,
      architecture,
      package_root: packageRoot,
      xlsx_files: xlsxFiles.map((f) => (path.isAbsolute(f) ? path.basename(f) : f)),
      authority_source_file: path.basename(groupPlanPath),
    });

    if (!phraseSlotReconciliation.phrase_slot_reconciliation_pass) {
      fail(
        'PHRASE_SLOT_RECONCILIATION_FAIL',
        `Authority phrase slots ${phraseSlotReconciliation.authority_phrase_slots} != artifact ${phraseSlotReconciliation.artifact_phrase_slots} (delta ${phraseSlotReconciliation.phrase_slot_delta})`,
        {
          authority_phrase_slots: phraseSlotReconciliation.authority_phrase_slots,
          artifact_phrase_slots: phraseSlotReconciliation.artifact_phrase_slots,
          phrase_slot_delta: phraseSlotReconciliation.phrase_slot_delta,
          missing_slots: phraseSlotReconciliation.missing_slots,
          unexpected_slots: phraseSlotReconciliation.unexpected_slots,
          duplicate_slots: phraseSlotReconciliation.duplicate_slots,
        },
      );
      for (const m of phraseSlotReconciliation.expected_but_missing ?? []) {
        fail(
          'MISSING_PHRASE_SLOT',
          `${m.campaign_id}/${m.group_id}: missing "${m.phrase}"`,
          { slot: m },
        );
      }
      for (const u of phraseSlotReconciliation.unexpected_in_artifact ?? []) {
        fail(
          'UNEXPECTED_PHRASE_SLOT',
          `${u.filename} row ${u.xlsx_row}: unexpected "${u.phrase}"`,
          { slot: u },
        );
      }
      for (const d of phraseSlotReconciliation.duplicate_in_artifact ?? []) {
        fail(
          'DUPLICATE_PHRASE_SLOT',
          `${d.filename} row ${d.xlsx_row}: duplicate "${d.phrase}"`,
          { slot: d },
        );
      }
      for (const c of phraseSlotReconciliation.campaign_reconciliation ?? []) {
        if (!c.pass) {
          fail(
            'CAMPAIGN_PHRASE_SLOT_MISMATCH',
            `${c.campaign_id}: authority ${c.authority_phrase_slots} vs artifact ${c.artifact_phrase_slots}`,
            { campaign: c },
          );
        }
      }
    } else {
      pass('phrase_slot_reconciliation');
    }
  } else if (input.require_phrase_slot_reconciliation !== false) {
    fail('MISSING_GROUP_PLAN', 'Group plan required for phrase-slot reconciliation');
  }

  if (input.checksum_manifest_path) {
    const manifest = JSON.parse(fs.readFileSync(input.checksum_manifest_path, 'utf8'));
    const checksumResult = verifyChecksumManifest(packageRoot, manifest);
    if (checksumResult.status !== SCRIPT_STATUS.PASS) {
      for (const v of checksumResult.violations) fail(v.code, v.message, { file: v.file });
    } else {
      pass('checksum_verified');
    }
  }

  if (input.package_manifest_path && fs.existsSync(input.package_manifest_path)) {
    pass('package_manifest_present');
  }

  const releaseState = input.release_state ?? {};
  const currentPhase = deriveCurrentPhase({ states: releaseState });

  const status = violations.length === 0 ? GATE_STATUS.PASS : GATE_STATUS.FAIL;

  return {
    status,
    script_status: violations.length === 0 ? SCRIPT_STATUS.PASS : SCRIPT_STATUS.FAIL,
    project_id: input.project_id,
    package_root: packageRoot,
    current_release_phase: currentPhase,
    violation_count: violations.length,
    violations,
    checks,
    artifact_results: artifactResults,
    phrase_slot_reconciliation: phraseSlotReconciliation
      ? {
          authority_phrase_slots: phraseSlotReconciliation.authority_phrase_slots,
          artifact_phrase_slots: phraseSlotReconciliation.artifact_phrase_slots,
          phrase_slot_delta: phraseSlotReconciliation.phrase_slot_delta,
          campaign_reconciliation: phraseSlotReconciliation.campaign_reconciliation,
          group_reconciliation: phraseSlotReconciliation.group_reconciliation,
          missing_slots: phraseSlotReconciliation.missing_slots,
          unexpected_slots: phraseSlotReconciliation.unexpected_slots,
          duplicate_slots: phraseSlotReconciliation.duplicate_slots,
          normalization_collisions: phraseSlotReconciliation.normalization_collisions,
          phrase_slot_reconciliation_pass: phraseSlotReconciliation.phrase_slot_reconciliation_pass,
          missing_slots_list: phraseSlotReconciliation.missing_slots_list,
          unexpected_slots_list: phraseSlotReconciliation.unexpected_slots_list,
          duplicate_slots_list: phraseSlotReconciliation.duplicate_slots_list,
        }
      : null,
    evaluated_at: new Date().toISOString(),
    note: 'RELEASE_GATE_PASS means artifact technically consistent with frozen authority — NOT semantic/launch approval',
  };
}

function findXlsxInPackage(packageRoot) {
  if (!fs.existsSync(packageRoot)) return [];
  const results = [];
  const walk = (dir, prefix = '') => {
    for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
      const rel = prefix ? `${prefix}/${ent.name}` : ent.name;
      if (ent.isDirectory()) walk(path.join(dir, ent.name), rel);
      else if (ent.name.toLowerCase().endsWith('.xlsx')) results.push(rel);
    }
  };
  walk(packageRoot);
  return results;
}

function loadPackageManifestXlsxFiles(packageRoot, explicitManifestPath) {
  const candidates = [];
  if (explicitManifestPath && fs.existsSync(explicitManifestPath)) {
    candidates.push(explicitManifestPath);
  }
  if (fs.existsSync(packageRoot)) {
    for (const ent of fs.readdirSync(packageRoot)) {
      if (/OUTPUT-MANIFEST/i.test(ent) && ent.endsWith('.json')) {
        candidates.push(path.join(packageRoot, ent));
      }
    }
  }
  for (const manifestPath of candidates) {
    try {
      const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
      const files = manifest.xlsx_files ?? manifest.files?.filter((f) => String(f).toLowerCase().endsWith('.xlsx'));
      if (Array.isArray(files) && files.length > 0) {
        return files.filter((f) => fs.existsSync(path.join(packageRoot, f)));
      }
    } catch {
      /* try next */
    }
  }
  return null;
}
