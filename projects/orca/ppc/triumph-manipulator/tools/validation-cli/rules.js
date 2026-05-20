"use strict";

const GENERIC_PHRASES = [
  "лучшие цены",
  "высокое качество",
  "профессиональный подход",
  "лидер рынка",
  "надёжная компания",
  "надежная компания",
];

const GENERIC_CTA_PHRASES = [
  "оставить заявку",
  "отправить заявку",
  "получить консультацию",
];

const SPECIFIC_INTENT_MARKERS = [
  /бытовк/i,
  /юрлиц/i,
  /5\s*тонн|5\s*т\b/i,
  /стройматериал/i,
  /вездеход/i,
  /6\s*[x×]\s*6/i,
  /безнал/i,
];

const MIXED_INTENT_MARKERS = [
  { id: "bytovka", pattern: /бытовк/i },
  { id: "yurlica", pattern: /юрлиц/i },
  { id: "5ton", pattern: /5\s*тонн|5\s*т\b/i },
];

const REQUIRED_TOP_LEVEL = [
  "schema_version",
  "project_id",
  "project_name",
  "market",
  "geo",
  "source_pack",
  "search_only_scope",
  "campaigns",
  "global_negatives",
  "validation_policy",
  "export_policy",
  "human_review",
];

function normalizeText(value) {
  return String(value || "")
    .toLowerCase()
    .replace(/\s+/g, " ")
    .trim();
}

function charCount(value) {
  return String(value || "").length;
}

function containsPhrase(haystack, needle) {
  const h = normalizeText(haystack);
  const n = normalizeText(needle);
  if (!h || !n) return false;
  return h.includes(n);
}

function cleanFinding({ rule_id, message, entity_ref, suggested_fix }) {
  const item = { rule_id, message };
  if (entity_ref && (entity_ref.entity_kind || entity_ref.entity_id)) {
    item.entity_ref = entity_ref;
  }
  if (suggested_fix) item.suggested_fix = suggested_fix;
  return item;
}

function isHighlySpecificIntent(group) {
  const intentType = group.intent_type;
  if (
    intentType &&
    intentType !== "hot_general" &&
    intentType !== "mixed_container"
  ) {
    return true;
  }
  const blob = normalizeText(
    [group.semantic_intent, group.group_name, group.keyword_cluster?.intent_summary].join(
      " "
    )
  );
  return SPECIFIC_INTENT_MARKERS.some((p) => p.test(blob));
}

function isMasterLandingRoute(route) {
  const landingType = route.landing_type || "";
  const blueprint = normalizeText(route.blueprint_id || "");
  return (
    landingType === "master_hot" ||
    landingType === "fallback" ||
    blueprint.includes("master")
  );
}

function makeResult({
  ruleId,
  ruleClass,
  severity,
  status,
  message,
  entityRef = null,
  suggestedFix = null,
}) {
  const result = {
    rule_id: ruleId,
    rule_class: ruleClass,
    severity,
    status,
    message,
  };
  if (entityRef) result.entity_ref = entityRef;
  if (suggestedFix) result.suggested_fix = suggestedFix;
  return result;
}

function pass(ruleId, ruleClass, message, entityRef) {
  return makeResult({
    ruleId,
    ruleClass,
    severity: "info",
    status: "pass",
    message,
    entityRef,
  });
}

function fail(ruleId, ruleClass, severity, message, entityRef, suggestedFix) {
  return makeResult({
    ruleId,
    ruleClass,
    severity,
    status: severity === "warn" ? "warn" : "fail",
    message,
    entityRef,
    suggestedFix,
  });
}

function getSymbolLimits(doc) {
  const policy = doc.validation_policy || {};
  const limits = policy.symbol_limits || {};
  return {
    headline1Max: limits.headline_1_max ?? 56,
    descriptionMax: limits.description_max ?? 81,
  };
}

/** ST-01 — required top-level structure */
function ruleST01(doc) {
  const results = [];
  const missing = REQUIRED_TOP_LEVEL.filter(
    (key) => doc[key] === undefined || doc[key] === null
  );

  if (missing.length === 0 && doc.schema_version === "v1") {
    results.push(
      pass(
        "ST-01",
        "structural",
        "Required top-level fields present; schema_version is v1.",
        { entity_kind: "document", entity_id: doc.project_id || "document" }
      )
    );
  } else {
    const parts = [];
    if (missing.length) parts.push(`missing: ${missing.join(", ")}`);
    if (doc.schema_version !== "v1") {
      parts.push(`schema_version must be v1 (got: ${doc.schema_version})`);
    }
    results.push(
      fail(
        "ST-01",
        "structural",
        "error",
        `Required top-level structure invalid. ${parts.join("; ")}`,
        { entity_kind: "document", entity_id: doc.project_id || "document" },
        "Complete required root fields per orca-ppc-document-v1.schema.json."
      )
    );
  }
  return results;
}

/** ST-02 — search_only_scope must be true */
function ruleST02(doc) {
  const results = [];
  const docRef = { entity_kind: "document", entity_id: doc.project_id || "document" };

  if (doc.search_only_scope !== true) {
    results.push(
      fail(
        "ST-02",
        "structural",
        "error",
        "Document search_only_scope must be true.",
        docRef,
        "Set search_only_scope: true at document root."
      )
    );
  } else {
    results.push(
      pass("ST-02", "structural", "Document search_only_scope is true.", docRef)
    );
  }

  for (const campaign of doc.campaigns || []) {
    const campRef = {
      entity_kind: "campaign",
      entity_id: campaign.campaign_id || "unknown",
    };
    if (campaign.search_only_scope !== true) {
      results.push(
        fail(
          "ST-02",
          "structural",
          "error",
          `Campaign ${campaign.campaign_id}: search_only_scope must be true.`,
          campRef,
          "Set campaign.search_only_scope: true."
        )
      );
    } else {
      results.push(
        pass(
          "ST-02",
          "structural",
          `Campaign ${campaign.campaign_id}: search_only_scope is true.`,
          campRef
        )
      );
    }
  }

  return results;
}

/** SY-01 — headline_1 symbol limit */
function ruleSY01(doc) {
  const limits = getSymbolLimits(doc);
  const results = [];

  for (const campaign of doc.campaigns || []) {
    for (const group of campaign.groups || []) {
      for (const ad of group.ads || []) {
        const len = charCount(ad.headline_1);
        const ref = {
          entity_kind: "ad",
          entity_id: ad.ad_id,
          field_path: "headline_1",
        };
        if (len > limits.headline1Max) {
          results.push(
            fail(
              "SY-01",
              "symbol",
              "error",
              `headline_1 length ${len} exceeds max ${limits.headline1Max}.`,
              ref,
              "Shorten headline_1 to fit Yandex limit."
            )
          );
        } else {
          results.push(
            pass(
              "SY-01",
              "symbol",
              `headline_1 length ${len} within limit ${limits.headline1Max}.`,
              ref
            )
          );
        }
      }
    }
  }

  return results;
}

/** SY-02 — description symbol limit (v0: description field) */
function ruleSY02(doc) {
  const limits = getSymbolLimits(doc);
  const results = [];

  for (const campaign of doc.campaigns || []) {
    for (const group of campaign.groups || []) {
      for (const ad of group.ads || []) {
        const len = charCount(ad.description);
        const ref = {
          entity_kind: "ad",
          entity_id: ad.ad_id,
          field_path: "description",
        };
        if (len > limits.descriptionMax) {
          results.push(
            fail(
              "SY-02",
              "symbol",
              "error",
              `description length ${len} exceeds max ${limits.descriptionMax}.`,
              ref,
              "Shorten description to fit Yandex limit."
            )
          );
        } else {
          results.push(
            pass(
              "SY-02",
              "symbol",
              `description length ${len} within limit ${limits.descriptionMax}.`,
              ref
            )
          );
        }
      }
    }
  }

  return results;
}

/** SE-05 — primary keyword phrase present in headline_1 */
function ruleSE05(doc) {
  const results = [];

  for (const campaign of doc.campaigns || []) {
    for (const group of campaign.groups || []) {
      for (const ad of group.ads || []) {
        const ref = {
          entity_kind: "ad",
          entity_id: ad.ad_id,
          field_path: "keyword_alignment.phrase_in_headline_1",
        };
        const alignment = ad.keyword_alignment || {};
        const primary = alignment.primary_keyword || "";
        const inHeadline =
          alignment.phrase_in_headline_1 === true ||
          containsPhrase(ad.headline_1, primary);

        if (!primary) {
          results.push(
            fail(
              "SE-05",
              "semantic",
              "error",
              "primary_keyword missing on ad.",
              ref,
              "Set keyword_alignment.primary_keyword from cluster."
            )
          );
        } else if (!inHeadline) {
          results.push(
            fail(
              "SE-05",
              "semantic",
              "error",
              `Primary keyword phrase not detected in headline_1: "${primary}".`,
              ref,
              "Include primary keyword phrase in headline_1 for Yandex relevance."
            )
          );
        } else {
          results.push(
            pass(
              "SE-05",
              "semantic",
              `Primary keyword present in headline_1: "${primary}".`,
              ref
            )
          );
        }
      }
    }
  }

  return results;
}

/** SE-07 — generic wording detection */
function ruleSE07(doc) {
  const results = [];

  for (const campaign of doc.campaigns || []) {
    for (const group of campaign.groups || []) {
      for (const ad of group.ads || []) {
        const ref = {
          entity_kind: "ad",
          entity_id: ad.ad_id,
          field_path: "headline_1",
        };
        const texts = [ad.headline_1, ad.headline_2, ad.description].filter(Boolean);
        const combined = normalizeText(texts.join(" "));
        const hits = GENERIC_PHRASES.filter((phrase) => combined.includes(phrase));

        if (hits.length > 0) {
          results.push(
            fail(
              "SE-07",
              "semantic",
              "error",
              `Generic wording detected: ${hits.join(", ")}.`,
              ref,
              "Replace generic marketing phrases with intent-specific copy."
            )
          );
        } else {
          results.push(
            pass("SE-07", "semantic", "No generic blacklist phrases detected.", ref)
          );
        }
      }
    }
  }

  return results;
}

/** LM-01 — landing continuation mismatch (v0 heuristic) */
function ruleLM01(doc) {
  const results = [];

  for (const campaign of doc.campaigns || []) {
    for (const group of campaign.groups || []) {
      const ref = {
        entity_kind: "group",
        entity_id: group.group_id,
        field_path: "landing_route",
      };
      const intent = normalizeText(group.semantic_intent);
      const route = group.landing_route || {};
      const blueprint = normalizeText(route.blueprint_id || "");
      const finalUrl = normalizeText(route.final_url || "");

      if (intent.includes("бытовк")) {
        const ok =
          blueprint.includes("bytovka") || finalUrl.includes("bytovka");
        if (!ok) {
          results.push(
            fail(
              "LM-01",
              "landing_mismatch",
              "error",
              'Group intent references бытовка but landing route lacks "bytovka" continuation.',
              ref,
              'Route to blueprint 02-use-case-bytovka or URL containing "bytovka".'
            )
          );
        } else {
          results.push(
            pass(
              "LM-01",
              "landing_mismatch",
              "Bytovka intent matches bytovka landing route (v0 heuristic).",
              ref
            )
          );
        }
      } else {
        results.push(
          pass(
            "LM-01",
            "landing_mismatch",
            "Landing continuation check not required for this group (v0).",
            ref
          )
        );
      }
    }
  }

  return results;
}

/** CM-02 — CTA clarity (v0: primary_cta present and phrase when calculate/order) */
function ruleCM02(doc) {
  const results = [];

  for (const campaign of doc.campaigns || []) {
    for (const group of campaign.groups || []) {
      for (const ad of group.ads || []) {
        const ref = {
          entity_kind: "ad",
          entity_id: ad.ad_id,
          field_path: "cta_semantics",
        };
        const cta = ad.cta_semantics || {};
        const primary = cta.primary_cta;
        const phrase = (cta.cta_phrase || "").trim();
        const needsPhrase = primary === "calculate" || primary === "order";

        if (!primary) {
          results.push(
            fail(
              "CM-02",
              "commercial",
              "warn",
              "CTA primary_cta missing — unclear action for user.",
              ref,
              "Set cta_semantics.primary_cta (call, calculate, order, whatsapp)."
            )
          );
        } else if (needsPhrase && !phrase) {
          results.push(
            fail(
              "CM-02",
              "commercial",
              "warn",
              `CTA type "${primary}" should include cta_phrase for clarity.`,
              ref,
              "Add explicit cta_phrase (e.g. Получить расчёт)."
            )
          );
        } else {
          results.push(
            pass(
              "CM-02",
              "commercial",
              `CTA clarity OK: primary_cta=${primary}${phrase ? `, phrase="${phrase}"` : ""}.`,
              ref
            )
          );
        }
      }
    }
  }

  return results;
}

/** SV-03 — duplicate ad detection (v0: duplicate headline_1 within group) */
function ruleSV03(doc) {
  const results = [];

  for (const campaign of doc.campaigns || []) {
    for (const group of campaign.groups || []) {
      const ref = { entity_kind: "group", entity_id: group.group_id };
      const seen = new Map();

      let hasDupe = false;

      for (const ad of group.ads || []) {
        const key = normalizeText(ad.headline_1);
        if (!key) continue;
        if (!seen.has(key)) {
          seen.set(key, ad.ad_id);
        } else {
          hasDupe = true;
          results.push(
            fail(
              "SV-03",
              "survivability",
              "warn",
              `Duplicate headline_1 in group: "${ad.headline_1}" (ads ${seen.get(key)}, ${ad.ad_id}).`,
              { ...ref, field_path: "ads" },
              "Differentiate headlines or remove redundant ad variant."
            )
          );
        }
      }

      if (!hasDupe) {
        results.push(
          pass(
            "SV-03",
            "survivability",
            "No duplicate headline_1 within group.",
            ref
          )
        );
      }
    }
  }

  return results;
}

/** SY-03 — empty fastlink titles */
function ruleSY03(doc) {
  const results = [];

  for (const campaign of doc.campaigns || []) {
    for (const group of campaign.groups || []) {
      for (const ad of group.ads || []) {
        const fastlinks = ad.fastlinks || [];
        if (fastlinks.length === 0) continue;

        for (let i = 0; i < fastlinks.length; i++) {
          const fl = fastlinks[i];
          const ref = {
            entity_kind: "ad",
            entity_id: ad.ad_id,
            field_path: `fastlinks[${i}].title`,
          };
          const title = (fl.title || "").trim();
          if (!title) {
            results.push(
              fail(
                "SY-03",
                "symbol",
                "error",
                "Fastlink title is empty.",
                ref,
                "Set a non-empty fastlink title (max 30 chars)."
              )
            );
          } else {
            results.push(
              pass(
                "SY-03",
                "symbol",
                `Fastlink title present: "${title}".`,
                ref
              )
            );
          }
        }
      }
    }
  }

  return results;
}

/** SY-04 — empty callout text */
function ruleSY04(doc) {
  const results = [];

  for (const campaign of doc.campaigns || []) {
    for (const group of campaign.groups || []) {
      for (const ad of group.ads || []) {
        const callouts = ad.callouts || [];
        if (callouts.length === 0) continue;

        for (let i = 0; i < callouts.length; i++) {
          const co = callouts[i];
          const ref = {
            entity_kind: "ad",
            entity_id: ad.ad_id,
            field_path: `callouts[${i}].text`,
          };
          const text = (co.text || "").trim();
          if (!text) {
            results.push(
              fail(
                "SY-04",
                "symbol",
                "error",
                "Callout text is empty.",
                ref,
                "Set callout text or remove empty callout row."
              )
            );
          } else {
            results.push(
              pass("SY-04", "symbol", `Callout text present: "${text}".`, ref)
            );
          }
        }
      }
    }
  }

  return results;
}

/** SE-08 — generic CTA detection */
function ruleSE08(doc) {
  const results = [];

  for (const campaign of doc.campaigns || []) {
    for (const group of campaign.groups || []) {
      for (const ad of group.ads || []) {
        const ref = {
          entity_kind: "ad",
          entity_id: ad.ad_id,
          field_path: "cta_semantics",
        };
        const cta = ad.cta_semantics || {};
        const texts = normalizeText(
          [cta.cta_phrase, ad.headline_2, ad.description].filter(Boolean).join(" ")
        );
        const hits = GENERIC_CTA_PHRASES.filter((p) => texts.includes(p));

        if (hits.length > 0) {
          results.push(
            fail(
              "SE-08",
              "semantic",
              "warn",
              `Generic CTA phrasing detected: ${hits.join(", ")}.`,
              ref,
              "Prefer practical CTA aligned to intent (call, calculate, order)."
            )
          );
        } else {
          results.push(
            pass("SE-08", "semantic", "No generic CTA blacklist phrases detected.", ref)
          );
        }
      }
    }
  }

  return results;
}

/** LM-02 — master/fallback landing with highly specific intent */
function ruleLM02(doc) {
  const results = [];

  for (const campaign of doc.campaigns || []) {
    for (const group of campaign.groups || []) {
      const ref = {
        entity_kind: "group",
        entity_id: group.group_id,
        field_path: "landing_route",
      };
      const route = group.landing_route || {};
      const masterRoute = isMasterLandingRoute(route);
      const specific = isHighlySpecificIntent(group);

      if (masterRoute && specific) {
        results.push(
          fail(
            "LM-02",
            "landing_mismatch",
            "warn",
            "Highly specific semantic intent routed to master/fallback landing (v0.1 heuristic).",
            ref,
            "Use intent-specific blueprint from landing-pages INDEX."
          )
        );
      } else {
        results.push(
          pass(
            "LM-02",
            "landing_mismatch",
            "No master/fallback mismatch for specific intent (v0.1).",
            ref
          )
        );
      }
    }
  }

  return results;
}

/** SV-05 — duplicate keyword phrases within group */
function ruleSV05(doc) {
  const results = [];

  for (const campaign of doc.campaigns || []) {
    for (const group of campaign.groups || []) {
      const ref = {
        entity_kind: "group",
        entity_id: group.group_id,
        field_path: "keyword_cluster.keywords",
      };
      const seen = new Map();
      let hasDupe = false;

      for (const kw of group.keyword_cluster?.keywords || []) {
        const key = normalizeText(kw.phrase);
        if (!key) continue;
        if (!seen.has(key)) {
          seen.set(key, kw.phrase);
        } else {
          hasDupe = true;
          results.push(
            fail(
              "SV-05",
              "survivability",
              "warn",
              `Duplicate keyword phrase in group: "${kw.phrase}".`,
              ref,
              "Remove duplicate keyword or merge into one phrase row."
            )
          );
        }
      }

      if (!hasDupe) {
        results.push(
          pass(
            "SV-05",
            "survivability",
            "No duplicate keyword phrases within group.",
            ref
          )
        );
      }
    }
  }

  return results;
}

/** SV-04 — mixed semantic intent in group (v0 markers) */
function ruleSV04(doc) {
  const results = [];

  for (const campaign of doc.campaigns || []) {
    for (const group of campaign.groups || []) {
      const ref = { entity_kind: "group", entity_id: group.group_id };
      const blob = normalizeText(
        [
          group.semantic_intent,
          group.group_name,
          group.keyword_cluster?.intent_summary,
          ...(group.keyword_cluster?.keywords || []).map((k) => k.phrase),
        ].join(" ")
      );

      const matched = MIXED_INTENT_MARKERS.filter((m) => m.pattern.test(blob)).map(
        (m) => m.id
      );

      if (matched.length >= 2) {
        results.push(
          fail(
            "SV-04",
            "survivability",
            "warn",
            `Mixed semantic intent markers in one group: ${matched.join(", ")}.`,
            ref,
            "Split group by intent (бытовка / юрлиц / 5 тонн) per doctrine."
          )
        );
      } else {
        results.push(
          pass(
            "SV-04",
            "survivability",
            "No mixed intent marker combination detected (v0).",
            ref
          )
        );
      }
    }
  }

  return results;
}

const RULE_RUNNERS = [
  ruleST01,
  ruleST02,
  ruleSY01,
  ruleSY02,
  ruleSY03,
  ruleSY04,
  ruleSE05,
  ruleSE07,
  ruleSE08,
  ruleLM01,
  ruleLM02,
  ruleCM02,
  ruleSV03,
  ruleSV04,
  ruleSV05,
];

function executeRules(doc) {
  const ruleResults = [];
  for (const run of RULE_RUNNERS) {
    ruleResults.push(...run(doc));
  }
  return ruleResults;
}

function rollupEntityResults(ruleResults) {
  const byEntity = new Map();

  for (const r of ruleResults) {
    if (!r.entity_ref?.entity_id) continue;
    const key = `${r.entity_ref.entity_kind}:${r.entity_ref.entity_id}`;
    if (!byEntity.has(key)) {
      byEntity.set(key, {
        entity_kind: r.entity_ref.entity_kind,
        entity_id: r.entity_ref.entity_id,
        status: "pass",
        rule_ids: [],
        message: "",
      });
    }
    const entry = byEntity.get(key);
    entry.rule_ids.push(r.rule_id);

    if (r.status === "fail") entry.status = "fail";
    else if (r.status === "warn" && entry.status !== "fail") entry.status = "warn";
  }

  return Array.from(byEntity.values()).filter((e) =>
    ["campaign", "group", "ad"].includes(e.entity_kind)
  );
}

function buildReport(doc, ruleResults, schemaValid, schemaErrors, options = {}) {
  const blocking = [];
  const warnings = [];
  const safeUnknown = [];

  if (!schemaValid) {
    for (const err of schemaErrors.slice(0, 20)) {
      blocking.push(
        cleanFinding({
          rule_id: "ST-01",
          message: `JSON Schema: ${err}`,
          suggested_fix:
            "Fix document structure per orca-ppc-document-v1.schema.json.",
        })
      );
    }
  }

  let passed = 0;
  let warned = 0;
  let failed = 0;
  let notChecked = 0;

  for (const r of ruleResults) {
    if (r.status === "pass") passed++;
    else if (r.status === "warn") {
      warned++;
      warnings.push(
        cleanFinding({
          rule_id: r.rule_id,
          message: r.message,
          entity_ref: r.entity_ref,
          suggested_fix: r.suggested_fix,
        })
      );
    } else if (r.status === "fail") {
      if (r.severity === "error") {
        failed++;
        blocking.push(
          cleanFinding({
            rule_id: r.rule_id,
            message: r.message,
            entity_ref: r.entity_ref,
            suggested_fix: r.suggested_fix,
          })
        );
      } else {
        warned++;
        warnings.push(
          cleanFinding({
            rule_id: r.rule_id,
            message: r.message,
            entity_ref: r.entity_ref,
            suggested_fix: r.suggested_fix,
          })
        );
      }
    } else {
      notChecked++;
    }
  }

  const totalRules = ruleResults.length;
  let validationStatus = "passed";
  if (!schemaValid || failed > 0) validationStatus = "failed";
  else if (warned > 0) validationStatus = "passed_with_warnings";

  const humanReviewRequired =
    validationStatus !== "passed" ||
    warnings.length > 0 ||
    doc.human_review?.required === true;

  const exportAllowed =
    schemaValid &&
    blocking.length === 0 &&
    validationStatus !== "failed" &&
    validationStatus !== "incomplete";

  const timestamp =
    options.fixedTimestamp ||
    process.env.ORCA_VALIDATOR_FIXED_TIMESTAMP ||
    new Date().toISOString();

  return {
    schema_version: "v1",
    project_id: doc.project_id || "unknown",
    validated_document_id: doc.project_id || "unknown",
    validation_timestamp: timestamp,
    validation_status: validationStatus,
    summary: {
      total_rules: totalRules,
      passed,
      warned,
      failed,
      not_checked: notChecked,
      safe_unknown_count: safeUnknown.length,
      message: `ORCA Validation CLI Hardening v0.1 — ${totalRules} rule evaluations.`,
    },
    rule_results: ruleResults,
    entity_results: rollupEntityResults(ruleResults),
    blocking_errors: blocking,
    warnings,
    safe_unknown: safeUnknown,
    human_review_required: humanReviewRequired,
    export_allowed: exportAllowed,
    meta: {
      validator_version: "orca-validation-cli-hardening-v0.1",
      ruleset_ref: "triumph-manipulator-validation-v0.1-subset",
      input_schema_valid: schemaValid,
      report_schema_valid: null,
      launch_allowed: null,
    },
  };
}

/**
 * Fail-closed when ValidationReport does not match validation-report-v1.schema.json.
 * Never sets launch_allowed — field reserved null to document human-only launch.
 */
function applyReportSchemaFailure(report, reportErrors) {
  const next = { ...report };
  next.export_allowed = false;
  next.human_review_required = true;
  if (next.validation_status === "passed") {
    next.validation_status = "failed";
  }
  next.meta = {
    ...next.meta,
    report_schema_valid: false,
    launch_allowed: null,
  };
  next.blocking_errors = [
    ...next.blocking_errors,
    cleanFinding({
      rule_id: "REPORT-SCHEMA",
      message: `ValidationReport failed JSON Schema: ${reportErrors[0] || "unknown"}`,
      suggested_fix:
        "Fix validator output to match validation-report-v1.schema.json.",
    }),
  ];
  if (reportErrors.length > 1) {
    for (let i = 1; i < Math.min(reportErrors.length, 5); i++) {
      next.blocking_errors.push(
        cleanFinding({
          rule_id: "REPORT-SCHEMA",
          message: `ValidationReport schema: ${reportErrors[i]}`,
        })
      );
    }
  }
  return next;
}

function markReportSchemaValid(report) {
  return {
    ...report,
    meta: {
      ...report.meta,
      report_schema_valid: true,
      launch_allowed: null,
    },
  };
}

module.exports = {
  executeRules,
  buildReport,
  applyReportSchemaFailure,
  markReportSchemaValid,
  GENERIC_PHRASES,
  GENERIC_CTA_PHRASES,
};
