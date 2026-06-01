"use strict";

const { stripTags } = require("../website-acquisition/extract-page-facts");
const { trustIdFor, makeEvidence, uniqueByKey } = require("./utils");

function classifyTrustText(text, registry) {
  const lower = text.toLowerCase();
  const rules = registry.trust_classification || {};

  for (const [trustType, patterns] of Object.entries(rules)) {
    for (const pattern of patterns) {
      const isRegex = pattern.startsWith("\\");
      if (isRegex) {
        try {
          if (new RegExp(pattern, "i").test(text)) {
            return trustType;
          }
        } catch {
          /* skip invalid */
        }
      } else if (lower.includes(pattern.toLowerCase())) {
        return trustType;
      }
    }
  }
  return "review_snippet";
}

function parseNumericValue(text) {
  const match = text.match(/(\d+[\d\s.,]*)\+?/);
  if (!match) {
    return null;
  }
  const num = Number(match[1].replace(/[\s,]/g, ""));
  return Number.isFinite(num) ? num : null;
}

function findBlockForType(blocks, blockType) {
  return blocks.find((b) => b.block_type === blockType) || null;
}

/**
 * Extract trust pattern observations (no scoring).
 */
function extractTrustPatterns(snapshot, options = {}) {
  const landingId = options.landing_id;
  const blocks = options.visible_blocks || [];
  const registry = options.registry || {};
  const patterns = [];
  let seq = 1;

  for (let i = 0; i < (snapshot.trust_signals_visible || []).length; i += 1) {
    const signal = snapshot.trust_signals_visible[i];
    const trustType = classifyTrustText(signal.text, registry);
    patterns.push({
      trust_id: trustIdFor(landingId, seq),
      trust_type: trustType,
      text: signal.text,
      numeric_value: parseNumericValue(signal.text),
      block_id: findBlockForType(blocks, ["reviews", "hero"])?.block_id || null,
      evidence: makeEvidence(snapshot, {
        snapshot_field: `/trust_signals_visible/${i}`,
        verbatim_text: signal.text,
        ambiguity: trustType === "rating_display" ? "high" : "none",
      }),
    });
    seq += 1;
  }

  if (options.html) {
    const text = stripTags(options.html);
    const sentences = text.split(/(?<=[.!?])\s+/).map((s) => s.trim()).filter(Boolean);
    for (const sentence of sentences) {
      if (sentence.length > 200) {
        continue;
      }
      const trustType = classifyTrustText(sentence, registry);
      const already = patterns.some((p) => p.text.toLowerCase() === sentence.toLowerCase());
      if (already) {
        continue;
      }
      if (
        trustType !== "review_snippet" ||
        /отзыв|review|рейтинг|гарант|лет на рынке|лиценз|сертификат|инн|огрн/i.test(sentence)
      ) {
        patterns.push({
          trust_id: trustIdFor(landingId, seq),
          trust_type: trustType,
          text: sentence,
          numeric_value: parseNumericValue(sentence),
          block_id: findBlockForType(blocks, ["reviews", "hero"])?.block_id || null,
          evidence: makeEvidence(snapshot, {
            source: "page_html",
            verbatim_text: sentence,
          }),
        });
        seq += 1;
      }
    }
  }

  const reviewBlock = findBlockForType(blocks, "reviews");
  if (reviewBlock && !patterns.some((p) => p.trust_type === "review_snippet")) {
    patterns.push({
      trust_id: trustIdFor(landingId, seq),
      trust_type: "review_snippet",
      text: reviewBlock.heading_text || "Reviews section visible",
      numeric_value: null,
      block_id: reviewBlock.block_id,
      evidence: reviewBlock.evidence,
    });
    seq += 1;
  }

  return uniqueByKey(patterns, (p) => `${p.trust_type}:${p.text.toLowerCase()}`);
}

module.exports = { extractTrustPatterns, classifyTrustText };
