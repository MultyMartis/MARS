#!/usr/bin/env node
/**
 * ORCA Campaign Production Contract Validator v1
 * Read-only. Does not modify production data.
 *
 * Usage:
 *   node validate-campaign-production-contract.mjs --config <audit-config.json>
 *   node validate-campaign-production-contract.mjs --help
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const INFORMATIONAL_BLOCKLIST = [
  /\bваканс/i,
  /\bрезюме\b/i,
  /\bобучен/i,
  /\bкурс(ы|а)?\b/i,
  /\bурок/i,
  /\bучебник/i,
  /\bстажиров/i,
  /\bчто такое\b/i,
  /\bкак стать\b/i,
  /\bскачать\b/i,
  /\bторрент\b/i,
  /\bкряк\b/i,
  /\bcrack\b/i,
  /\bсвоими руками\b/i,
  /\bинструкци/i,
  /\bфорум\b/i,
  /\bдиплом\b/i,
  /\bреферат\b/i,
];

const INLINE_MINUS_MAX_TOKENS = 3;

function loadJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

function kwPhrase(kw) {
  return kw.source_phrase || kw.ad_phrase || kw.normalized_phrase || kw.phrase || kw.keyword || '';
}

function kwStatus(kw) {
  return kw.semantic_decision || kw.final_status || kw.status || '';
}

function normPhrase(p) {
  return String(p || '')
    .toLowerCase()
    .replace(/\s+/g, ' ')
    .trim();
}

function isActiveKeyword(kw) {
  const st = String(kwStatus(kw)).toUpperCase();
  return st.includes('ACTIVE') || st.includes('CONTROLLED TEST');
}

function landingBase(url) {
  try {
    const u = new URL(String(url || '').trim());
    return `${u.origin}${u.pathname}`.replace(/\/$/, '');
  } catch {
    return normPhrase(String(url || '').split('?')[0].replace(/\/$/, ''));
  }
}

function parseArgs(argv) {
  const args = { config: null, help: false };
  for (let i = 2; i < argv.length; i++) {
    if (argv[i] === '--config') args.config = argv[++i];
    else if (argv[i] === '--help' || argv[i] === '-h') args.help = true;
  }
  return args;
}

function violation({ invariant_id, law_id, severity, entity_type, entity_id, message, required_action }) {
  return { invariant_id, law_id, severity, entity_type, entity_id, message, required_action };
}

function stripInlineNegatives(phrase) {
  return String(phrase || '')
    .replace(/\s+-[\wа-яё]+/gi, '')
    .replace(/\s+/g, ' ')
    .trim();
}

function splitInlineNegatives(phrase) {
  const negatives = [];
  const positive = String(phrase || '')
    .replace(/\s+(-[\wа-яё]+)/gi, (_, neg) => {
      negatives.push(neg.replace(/^-/, '').toLowerCase());
      return '';
    })
    .replace(/\s+/g, ' ')
    .trim();
  return { positive, negatives };
}

function isExcludedPositivePhrase(phrase, exclusionRegistry) {
  const { positive } = splitInlineNegatives(phrase);
  const np = normPhrase(positive);
  for (const e of exclusionRegistry?.exclusions || []) {
    if (normPhrase(e.normalized_phrase) === np) return e;
  }
  return null;
}

const EDUCATION_CAREER_RE = [
  /\bбез образован/i,
  /\bвысшее образован/i,
  /\bвысшего образован/i,
  /^образование программист/i,
];

const INLINE_MINUS_RESCUE_CATEGORIES = [
  'вакансия',
  'обучение',
  'курсы',
  'резюме',
  'как стать',
  'зарплат',
  'образован',
];

function countInlineMinusTokens(phrase) {
  const matches = phrase.match(/(?:^|\s)-\S+/g);
  return matches ? matches.length : 0;
}

function isHoldStatus(s) {
  return String(s || '').includes('HOLD');
}

function isActiveRepresentation(s) {
  const st = String(s || '').toUpperCase();
  return (st.includes('ACTIVE') || st.includes('CONTROLLED TEST')) && !isHoldStatus(s);
}

function isMandatoryService(svc) {
  return !svc.absence_from_production_permitted;
}

function isServiceRepresentedInProduction(grp, keywords, gid) {
  if (!grp) return false;
  const prodHold = isHoldStatus(grp.viability_status);
  const exportable = grp.export_to_xlsx !== false && !prodHold;
  const groupKws = keywords.filter((k) => k.group_id === gid && isActiveKeyword(k));
  return exportable && groupKws.length > 0;
}

export function validateCampaignProductionContract(inputs) {
  const {
    operator_service_scope: scope,
    protected_seed_registry: seeds = [],
    production_dataset: dataset,
    controlled_test_registry: controlled = { tests: [] },
    ad_registry: adReg = { ads: [] },
    group_registry: groupReg = { groups: [] },
    negative_validation: negVal = {},
    collision_validation: collision = {},
    exclusion_registry: exclusionRegistry = { exclusions: [] },
    project_meta: meta = {},
  } = inputs;

  const violations = [];
  const warnings = [];
  const authorityDrift = [];
  const groupById = new Map((dataset.groups || []).map((g) => [g.group_id, g]));
  const keywords = dataset.keywords || [];
  const kwById = new Map(keywords.map((k) => [k.keyword_id || k.id, k]));
  const activeKeywords = keywords.filter(isActiveKeyword);

  // INV-SCOPE-01
  for (const svc of scope?.services || []) {
    if (svc.absence_from_production_permitted) continue;
    const gid = svc.current_group;
    const grp = groupById.get(gid);
    if (!grp) {
      violations.push(
        violation({
          invariant_id: 'INV-SCOPE-01',
          law_id: 'ORCA-LAW-12',
          severity: 'critical',
          entity_type: 'service',
          entity_id: svc.service_id,
          message: `Mandatory service «${svc.service_name}» owner group ${gid} missing from production dataset`,
          required_action: 'Restore group or document operator absence',
        })
      );
      continue;
    }
    const exportable = grp.export_to_xlsx !== false && !String(grp.viability_status || '').includes('HOLD');
    const groupKws = keywords.filter((k) => k.group_id === gid && isActiveKeyword(k));
    if (!exportable || groupKws.length === 0) {
      violations.push(
        violation({
          invariant_id: 'INV-SCOPE-01',
          law_id: 'ORCA-LAW-12',
          severity: 'critical',
          entity_type: 'service',
          entity_id: svc.service_id,
          message: `Service «${svc.service_name}» not commercially represented (group ${gid}, status ${grp.viability_status}, phrases ${groupKws.length})`,
          required_action: 'Restore commercial phrase and group viability',
        })
      );
    }
  }

  // INV-SCOPE-02 — authority registry vs production drift (read-only; does not mutate files)
  const scopeGroupIds = new Set((scope?.services || []).map((s) => s.current_group));
  for (const svc of scope?.services || []) {
    const gid = svc.current_group;
    const grp = groupById.get(gid);
    const scopeHold = isHoldStatus(svc.current_group_status);
    const scopeActive = isActiveRepresentation(svc.current_group_status);
    const inProduction = isServiceRepresentedInProduction(grp, keywords, gid);
    const mandatory = isMandatoryService(svc);

    if (scopeHold && inProduction) {
      const v = violation({
        invariant_id: 'INV-SCOPE-02',
        law_id: 'ORCA-LAW-01',
        severity: 'high',
        entity_type: 'service',
        entity_id: svc.service_id,
        message: `Scope registry HOLD contradicts production ACTIVE for «${svc.service_name}» (${gid})`,
        required_action: 'Sync operator-service-scope registry to production truth',
      });
      violations.push(v);
      authorityDrift.push(v);
    }

    if (mandatory && scopeActive && !inProduction) {
      const v = violation({
        invariant_id: 'INV-SCOPE-02',
        law_id: 'ORCA-LAW-12',
        severity: 'high',
        entity_type: 'service',
        entity_id: svc.service_id,
        message: `Authority ACTIVE but production missing or HOLD for «${svc.service_name}» (${gid})`,
        required_action: 'Restore production representation or correct authority registry',
      });
      violations.push(v);
      authorityDrift.push(v);
    }

    if (grp && mandatory && scopeActive && isHoldStatus(grp.viability_status)) {
      const v = violation({
        invariant_id: 'INV-SCOPE-02',
        law_id: 'ORCA-LAW-01',
        severity: 'high',
        entity_type: 'service',
        entity_id: svc.service_id,
        message: `Authority/production group status contradiction for «${svc.service_name}»: scope ${svc.current_group_status}, group ${grp.viability_status}`,
        required_action: 'Align authority registry and production group status',
      });
      if (!authorityDrift.some((d) => d.entity_id === svc.service_id)) {
        violations.push(v);
        authorityDrift.push(v);
      }
    }
  }

  // INV-SCOPE-03 — exportable production group not covered by operator-approved architecture
  const authorizedGroupIds = new Set([
    ...(scope?.services || []).map((s) => s.current_group),
    ...(groupReg.groups || []).map((g) => g.group_id),
  ]);
  for (const g of dataset.groups || []) {
    if (g.export_to_xlsx === false) continue;
    if (!isActiveRepresentation(g.viability_status)) continue;
    const gk = keywords.filter((k) => k.group_id === g.group_id && isActiveKeyword(k));
    if (gk.length === 0) continue;
    if (!authorizedGroupIds.has(g.group_id)) {
      const v = violation({
        invariant_id: 'INV-SCOPE-03',
        law_id: 'ORCA-LAW-01',
        severity: 'high',
        entity_type: 'group',
        entity_id: g.group_id,
        message: `Production group ${g.group_id} is active in export but absent from operator scope or approved group registry`,
        required_action: 'Add operator scope/architecture entry or remove unauthorized production group',
      });
      violations.push(v);
      authorityDrift.push(v);
    }
  }

  // INV-SCOPE-04 — mandatory service family disappeared from export dataset
  for (const svc of scope?.services || []) {
    if (!isMandatoryService(svc)) continue;
    if (svc.advertising_status !== 'MUST REPRESENT IN CAMPAIGN') continue;
    const grp = groupById.get(svc.current_group);
    if (!grp) continue;
    if (grp.export_to_xlsx === false && isActiveRepresentation(svc.current_group_status)) {
      const v = violation({
        invariant_id: 'INV-SCOPE-04',
        law_id: 'ORCA-LAW-12',
        severity: 'high',
        entity_type: 'service',
        entity_id: svc.service_id,
        message: `Required service «${svc.service_name}» marked for export in authority but group ${svc.current_group} excluded from export`,
        required_action: 'Enable export or update authority registry',
      });
      violations.push(v);
      authorityDrift.push(v);
    }
  }

  // INV-SEED-01
  for (const seed of seeds) {
    const kid = seed.keyword_id;
    const phrase = seed.phrase || seed.anchor;
    const excl = isExcludedPositivePhrase(phrase, exclusionRegistry);
    if (excl && kid && excl.normalized_phrase === normPhrase(phrase)) {
      continue;
    }
    const kw = kwById.get(kid);
    if (!kw) {
      violations.push(
        violation({
          invariant_id: 'INV-SEED-01',
          law_id: 'ORCA-LAW-02',
          severity: 'critical',
          entity_type: 'protected_seed',
          entity_id: kid || phrase,
          message: `Protected seed missing from production dataset: «${phrase}»`,
          required_action: 'Restore protected seed',
        })
      );
      continue;
    }
    const st = kwStatus(kw);
    if (!st.includes('ACTIVE') && !st.includes('CONTROLLED TEST')) {
      violations.push(
        violation({
          invariant_id: 'INV-SEED-01',
          law_id: 'ORCA-LAW-02',
          severity: 'critical',
          entity_type: 'protected_seed',
          entity_id: kid,
          message: `Protected seed «${phrase}» not active (status: ${st})`,
          required_action: 'Restore or operator-remove with explicit decision',
        })
      );
    }
    if (seed.group_id && kw.group_id !== seed.group_id) {
      violations.push(
        violation({
          invariant_id: 'INV-SEED-01',
          law_id: 'ORCA-LAW-02',
          severity: 'critical',
          entity_type: 'protected_seed',
          entity_id: kid,
          message: `Protected seed «${phrase}» wrong group: expected ${seed.group_id}, got ${kw.group_id}`,
          required_action: 'Fix group ownership',
        })
      );
    }
  }

  // INV-HOLD-01
  const held = (dataset.held_groups || []).length;
  const holdGroups = (dataset.groups || []).filter((g) => String(g.viability_status || '').includes('HOLD'));
  if (holdGroups.length > 0 || held > 0) {
    for (const g of holdGroups) {
      violations.push(
        violation({
          invariant_id: 'INV-HOLD-01',
          law_id: 'ORCA-LAW-04',
          severity: 'critical',
          entity_type: 'group',
          entity_id: g.group_id,
          message: `Unexpected HOLD group ${g.group_id} in export candidate`,
          required_action: 'Reactivate or operator-approve HOLD',
        })
      );
    }
  }

  // INV-GRP-01
  for (const g of dataset.groups || []) {
    if (g.export_to_xlsx === false) continue;
    const gk = keywords.filter((k) => k.group_id === g.group_id && isActiveKeyword(k));
    const ad = (adReg.ads || []).find((a) => a.group_id === g.group_id || a.ad_id === `ad-${g.group_id}-a1`);
    if (gk.length === 0) {
      violations.push(
        violation({
          invariant_id: 'INV-GRP-01',
          law_id: 'ORCA-LAW-04',
          severity: 'critical',
          entity_type: 'group',
          entity_id: g.group_id,
          message: `Export group ${g.group_id} has no active phrases`,
          required_action: 'Add commercial phrase or remove from export',
        })
      );
    }
    if (!ad && !(dataset.ads || []).find((a) => a.group_id === g.group_id)) {
      violations.push(
        violation({
          invariant_id: 'INV-AD-01',
          law_id: 'ORCA-LAW-10',
          severity: 'critical',
          entity_type: 'group',
          entity_id: g.group_id,
          message: `Export group ${g.group_id} missing ad`,
          required_action: 'Assign ad before export',
        })
      );
    }
  }

  // INV-SEM-01 informational leakage
  for (const kw of activeKeywords) {
    const phrase = kwPhrase(kw);
    for (const re of INFORMATIONAL_BLOCKLIST) {
      if (re.test(phrase)) {
        violations.push(
          violation({
            invariant_id: 'INV-SEM-01',
            law_id: 'ORCA-LAW-06',
            severity: 'critical',
            entity_type: 'keyword',
            entity_id: kw.keyword_id || phrase,
            message: `Informational leakage in active phrase: «${phrase}»`,
            required_action: 'EXCLUDE keyword',
          })
        );
        break;
      }
    }
    const st = kwStatus(kw);
    const reason = kw.final_decision_reason || kw.reason || '';
    if (st.includes('ACTIVE') && /informational|обучен|карьер|ваканс/i.test(reason)) {
      violations.push(
        violation({
          invariant_id: 'INV-SEM-01',
          law_id: 'ORCA-LAW-11',
          severity: 'critical',
          entity_type: 'keyword',
          entity_id: kw.keyword_id,
          message: `Status/reason contradiction: ACTIVE with informational reason for «${phrase}»`,
          required_action: 'Align status and reason',
        })
      );
    }
  }

  // INV-SEM-02 duplicate ownership
  const phraseOwners = new Map();
  for (const kw of activeKeywords) {
    const p = normPhrase(kwPhrase(kw));
    if (!p) continue;
    if (!phraseOwners.has(p)) phraseOwners.set(p, []);
    phraseOwners.get(p).push(kw.group_id);
  }
  for (const [p, groups] of phraseOwners) {
    const unique = [...new Set(groups)];
    if (unique.length > 1) {
      violations.push(
        violation({
          invariant_id: 'INV-SEM-02',
          law_id: 'ORCA-LAW-08',
          severity: 'critical',
          entity_type: 'keyword',
          entity_id: p,
          message: `Duplicate phrase ownership: «${p}» in groups ${unique.join(', ')}`,
          required_action: 'Finalize phrase ownership',
        })
      );
    }
  }

  // INV-INLINE-01
  for (const kw of activeKeywords) {
    const phrase = kwPhrase(kw);
    const tokens = countInlineMinusTokens(phrase);
    if (tokens > INLINE_MINUS_MAX_TOKENS || (tokens >= 2 && phrase.length > 80)) {
      violations.push(
        violation({
          invariant_id: 'INV-INLINE-01',
          law_id: 'ORCA-LAW-07',
          severity: 'high',
          entity_type: 'keyword',
          entity_id: kw.keyword_id,
          message: `Long inline-minus repair pattern (${tokens} tokens): «${phrase}»`,
          required_action: 'Rewrite or exclude phrase',
        })
      );
    }

    const { positive, negatives } = splitInlineNegatives(phrase);
    const excl = isExcludedPositivePhrase(phrase, exclusionRegistry);
    if (excl) {
      violations.push(
        violation({
          invariant_id: 'INV-EXCL-01',
          law_id: 'ORCA-LAW-07',
          severity: 'critical',
          entity_type: 'keyword',
          entity_id: kw.keyword_id || excl.exclusion_id,
          message: `Excluded positive phrase active in registry: «${positive}» (${excl.exclusion_id})`,
          required_action: 'Remove keyword; inline negatives cannot bypass exclusion authority',
        })
      );
    }

    if (tokens >= 3) {
      const diverse = negatives.filter((n) =>
        INLINE_MINUS_RESCUE_CATEGORIES.some((c) => n.includes(c))
      );
      if (diverse.length >= 3 && positive.split(/\s+/).length <= 4) {
        violations.push(
          violation({
            invariant_id: 'INV-INLINE-02',
            law_id: 'ORCA-LAW-07',
            severity: 'high',
            entity_type: 'keyword',
            entity_id: kw.keyword_id,
            message: `Destructive inline-minus rescue on weak base «${positive}»`,
            required_action: 'Exclude base phrase or narrow with single precise negative',
          })
        );
      }
    }

    for (const re of EDUCATION_CAREER_RE) {
      if (re.test(normPhrase(positive))) {
        violations.push(
          violation({
            invariant_id: 'INV-SEM-EDU-01',
            law_id: 'ORCA-LAW-04',
            severity: 'high',
            entity_type: 'keyword',
            entity_id: kw.keyword_id,
            message: `Educational/career regression phrase active: «${positive}»`,
            required_action: 'Exclude per operator semantic exclusion authority',
          })
        );
        break;
      }
    }
  }

  // INV-CT-01
  for (const t of controlled.tests || []) {
    const phrase = t.phrase || '';
    const hyp = t.commercial_hypothesis || '';
    if (!phrase || !hyp.includes(phrase)) {
      violations.push(
        violation({
          invariant_id: 'INV-CT-01',
          law_id: 'ORCA-LAW-06',
          severity: 'high',
          entity_type: 'controlled_test',
          entity_id: t.keyword_id,
          message: `Controlled test hypothesis missing phrase reference: «${phrase}»`,
          required_action: 'Phrase-specific hypothesis required',
        })
      );
    }
    if (!t.matching_ad || !t.matching_landing) {
      violations.push(
        violation({
          invariant_id: 'INV-CT-01',
          law_id: 'ORCA-LAW-10',
          severity: 'high',
          entity_type: 'controlled_test',
          entity_id: t.keyword_id,
          message: `Controlled test missing ad or landing: «${phrase}»`,
          required_action: 'Complete controlled test record',
        })
      );
    }
  }

  // INV-AD-01 alignment
  for (const ad of adReg.ads || dataset.ads || []) {
    const gid = ad.group_id;
    const grp = groupById.get(gid);
    const landing = ad.landing_url || ad.planned_url || grp?.planned_url;
    const grpUrl = grp?.planned_url;
    if (grpUrl && landing && landingBase(landing) !== landingBase(grpUrl)) {
      warnings.push(
        violation({
          invariant_id: 'INV-AD-01',
          law_id: 'ORCA-LAW-10',
          severity: 'high',
          entity_type: 'ad',
          entity_id: ad.ad_id,
          message: `Ad landing mismatch for ${gid}: ad=${landing}, group=${grpUrl}`,
          required_action: 'Align ad and group landing',
        })
      );
    }
  }

  // INV-NEG-01
  if (collision.final_status && collision.final_status !== 'PASS') {
    violations.push(
      violation({
        invariant_id: 'INV-NEG-01',
        law_id: 'ORCA-LAW-09',
        severity: 'critical',
        entity_type: 'negative_architecture',
        entity_id: 'collision',
        message: `Collision validation not PASS: ${collision.final_status}`,
        required_action: 'Resolve blocking collisions',
      })
    );
  }
  if (negVal.unresolved_unique_risks > 0 || negVal.blocking_collisions > 0) {
    violations.push(
      violation({
        invariant_id: 'INV-NEG-01',
        law_id: 'ORCA-LAW-09',
        severity: 'critical',
        entity_type: 'negative_architecture',
        entity_id: 'negative_validation',
        message: `Unresolved negative risks: blocking=${negVal.blocking_collisions || 0}, unique=${negVal.unresolved_unique_risks || 0}`,
        required_action: 'Rebuild negatives after ownership freeze',
      })
    );
  }

  const critical = violations.filter((v) => v.severity === 'critical');
  const high = violations.filter((v) => v.severity === 'high');

  let gate_decision;
  if (critical.length === 0 && high.length === 0) {
    gate_decision =
      meta.authority_synchronized === true
        ? meta.repair_version === 'v7.1'
          ? 'PASS — V7.1 REGRESSION REPAIR; OPERATOR ACTUAL XLSX REVIEW AND COMMANDER DRY-RUN AUTHORIZED'
          : 'PASS — V7 AUTHORITY SYNCHRONIZED; ACTUAL XLSX REVIEW AND COMMANDER DRY-RUN AUTHORIZED'
        : meta.repair_version === 'v7.1'
          ? 'PASS — V7.1 MAY PROCEED TO OPERATOR ACTUAL XLSX REVIEW'
          : 'PASS — V7 MAY PROCEED TO ACTUAL XLSX REVIEW AND COMMANDER DRY-RUN';
  } else if (critical.length > 0) {
    gate_decision = 'BLOCKED — V7 REQUIRES CONTRACT-GUIDED CORRECTION';
  } else if (authorityDrift.length > 0) {
    gate_decision = 'BLOCKED — OPERATOR SCOPE AUTHORITY STILL INCONSISTENT';
  } else {
    gate_decision = 'PASS — V7 MAY PROCEED TO ACTUAL XLSX REVIEW AND COMMANDER DRY-RUN';
  }

  return {
    validator_id: 'validate-campaign-production-contract-v1',
    validated_at: new Date().toISOString(),
    contract_id: 'ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1',
    project_id: meta.project_id || dataset.project_id,
    dataset_id: meta.dataset_id || dataset.dataset_id,
    candidate_status: meta.candidate_status || 'PRODUCTION CANDIDATE — NOT OPERATOR APPROVED',
    summary: {
      groups: (dataset.groups || []).length,
      active_keywords: activeKeywords.length,
      ads: (adReg.ads || dataset.ads || []).length,
      protected_seeds_checked: seeds.length,
      operator_services_checked: (scope?.services || []).length,
      controlled_tests: (controlled.tests || []).length,
      critical_violations: critical.length,
      high_violations: high.length,
      authority_drift_violations: authorityDrift.length,
      authority_production_mismatches: authorityDrift.length,
      warnings: warnings.length,
    },
    gate_decision,
    authority_drift_blocked: authorityDrift.length > 0,
    critical_violations: critical,
    high_violations: high,
    authority_drift_violations: authorityDrift,
    warnings,
    group_audit: buildGroupAudit(dataset, keywords, adReg, controlled, violations, warnings),
    laws_evaluated: [
      'ORCA-LAW-01',
      'ORCA-LAW-02',
      'ORCA-LAW-04',
      'ORCA-LAW-06',
      'ORCA-LAW-07',
      'ORCA-LAW-08',
      'ORCA-LAW-09',
      'ORCA-LAW-10',
      'ORCA-LAW-11',
      'ORCA-LAW-12',
    ],
  };
}

function buildGroupAudit(dataset, keywords, adReg, controlled, violations, warnings) {
  const allIssues = [...violations, ...warnings];
  return (dataset.groups || []).map((g) => {
    const gid = g.group_id;
    const gk = keywords.filter((k) => k.group_id === gid);
    const active = gk.filter(isActiveKeyword);
    const ct = (controlled.tests || []).filter((t) => t.group === gid);
    const ad = (adReg.ads || []).find((a) => a.group_id === gid);
    const issues = allIssues.filter((v) => v.entity_id === gid || v.entity_type === 'group' && v.message?.includes(gid));
    const contractResult = issues.some((i) => i.severity === 'critical')
      ? 'FAIL'
      : issues.length
        ? 'WARN'
        : 'PASS';
    return {
      group_id: gid,
      name: g.export_name || g.group_name,
      direction: g.direction_marker,
      service: g.service_family || g.semantic_intent,
      keyword_count: active.length,
      controlled_test_count: ct.length,
      ad_id: ad?.ad_id,
      landing: g.planned_url || ad?.landing_url,
      contract_result: contractResult,
      required_action: issues.length ? issues.map((i) => i.required_action).join('; ') : 'None',
    };
  });
}

function loadConfig(configPath) {
  const cfg = loadJson(configPath);
  const root = path.dirname(configPath);
  const resolve = (p) => (path.isAbsolute(p) ? p : path.resolve(root, p));
  return {
    operator_service_scope: loadJson(resolve(cfg.operator_service_scope)),
    protected_seed_registry: cfg.protected_seed_registry
      ? (() => {
          const raw = loadJson(resolve(cfg.protected_seed_registry));
          return raw.seeds || raw;
        })()
      : (loadJson(resolve(cfg.recovery_package)).phrases_to_restore || []),
    production_dataset: loadJson(resolve(cfg.production_dataset)),
    controlled_test_registry: loadJson(resolve(cfg.controlled_test_registry)),
    ad_registry: loadJson(resolve(cfg.ad_registry)),
    group_registry: cfg.group_registry ? loadJson(resolve(cfg.group_registry)) : { groups: [] },
    negative_validation: cfg.negative_validation ? loadJson(resolve(cfg.negative_validation)) : {},
    collision_validation: cfg.collision_validation ? loadJson(resolve(cfg.collision_validation)) : {},
    exclusion_registry: cfg.exclusion_registry ? loadJson(resolve(cfg.exclusion_registry)) : { exclusions: [] },
    project_meta: cfg.project_meta || {},
  };
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help || !args.config) {
    console.log(`Usage: node validate-campaign-production-contract.mjs --config <audit-config.json>`);
    process.exit(args.help ? 0 : 1);
  }
  const inputs = loadConfig(path.resolve(args.config));
  const result = validateCampaignProductionContract(inputs);
  console.log(JSON.stringify(result, null, 2));
  process.exit(result.gate_decision.startsWith('BLOCKED') ? 2 : 0);
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main();
}
