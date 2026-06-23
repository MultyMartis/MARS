/**
 * Evaluation case builder — builds analytical packs from registry mutations
 * Strategist receives ONLY pack output; never evaluation constraints.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { buildDatedAnalyticalPack } from '../../../runtime/lib/analytical-pack-builder.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

function loadJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function deepClone(obj) {
  return JSON.parse(JSON.stringify(obj));
}

export function buildEvaluationCase(caseDef, repoRoot) {
  const fixPath = path.join(repoRoot, 'projects/mars-search-ppc-production/strategy/fixtures/synthetic-wave4-e2e');
  const manifest = loadJson(path.join(fixPath, 'manifest.json'));
  const mutations = caseDef.mutations || {};

  if (mutations.manifest?.remove_artifacts) {
    for (const key of mutations.manifest.remove_artifacts) {
      delete manifest.artifact_registry[key];
    }
  }
  if (mutations.manifest?.region) manifest.region = mutations.manifest.region;
  if (mutations.manifest?.stale_artifact) {
    manifest.artifact_registry[mutations.manifest.stale_artifact] = {
      path: 'projects/mars-search-ppc-production/strategy/fixtures/scenarios/stale-admission.json',
      status: 'REGISTERED',
    };
  }
  if (mutations.manifest?.swap_artifact) {
    for (const [key, rel] of Object.entries(mutations.manifest.swap_artifact)) {
      manifest.artifact_registry[key] = {
        path: `projects/mars-search-ppc-production/strategy/fixtures/${rel}`,
        status: 'REGISTERED',
      };
    }
  }

  const businessAuthority = loadJson(path.join(fixPath, 'business-authority.json'));
  if (mutations.businessAuthority) Object.assign(businessAuthority, mutations.businessAuthority);

  let landingInventory = loadJson(path.join(fixPath, 'landing-inventory.json'));
  let offerInventory = loadJson(path.join(fixPath, 'offer-inventory.json'));
  if (mutations.options?.landingInventory) {
    landingInventory = mutations.options.landingInventory;
  }
  if (mutations.options?.offerInventory) {
    offerInventory = mutations.options.offerInventory;
  }

  const options = {
    landingInventory,
    offerInventory,
    now: mutations.options?.now,
    staleDays: mutations.options?.staleDays,
  };

  const packResult = buildDatedAnalyticalPack({
    manifest,
    repoRoot,
    options,
  });

  if (mutations.serviceOwnership?.extra_services) {
    const svc = packResult.pack.service_ownership || { services: [] };
    svc.services = [...(svc.services || []), ...mutations.serviceOwnership.extra_services];
    packResult.pack.service_ownership = svc;
  }

  if (mutations.negativeIntelligence?.conflicts) {
    packResult.pack.negative_intelligence = packResult.pack.negative_intelligence || {};
    packResult.pack.negative_intelligence.conflicts = mutations.negativeIntelligence.conflicts;
  }

  if (mutations.semanticClusters?.add_rejected) {
    const clusters = packResult.pack.semantic_clusters?.clusters || [];
    clusters.push({
      cluster_id: 'cl-rejected',
      service_id: 'unassigned',
      tier: 'T4',
      phrases: [mutations.semanticClusters.add_rejected],
    });
    packResult.pack.semantic_clusters = { ...packResult.pack.semantic_clusters, clusters };
  }

  return {
    case_id: caseDef.id,
    scenario: caseDef.scenario,
    holdout: caseDef.holdout || false,
    adversarial: caseDef.adversarial || false,
    manifest: deepClone(manifest),
    businessAuthority,
    operatorConstraints: mutations.operatorConstraints || {},
    strategyPolicy: mutations.strategyPolicy || {},
    packResult,
    pack: packResult.pack,
  };
}

export function loadCaseRegistry(repoRoot) {
  const p = path.join(repoRoot, 'projects/mars-search-ppc-production/strategy/quality/evaluation/case-registry-v1.json');
  return loadJson(p);
}

export function loadEvaluationConstraints(caseId, repoRoot) {
  const p = path.join(repoRoot, 'projects/mars-search-ppc-production/strategy/quality/evaluation/constraints', `${caseId}-constraints-v1.json`);
  if (!fs.existsSync(p)) return null;
  return loadJson(p);
}
