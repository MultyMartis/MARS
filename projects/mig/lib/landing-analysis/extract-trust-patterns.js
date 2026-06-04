"use strict";

const { stripTags } = require("../website-acquisition/extract-page-facts");
const { trustIdFor, makeEvidence, uniqueByKey } = require("./utils");
const {
  classifyTrustSubtypeV2,
  splitTrustLines,
  isTrustBoilerplate,
  MAX_TRUST_LINE_CHARS,
} = require("./trust-subtype-v2");

function classifyTrustText(text, registry) {
  const v2 = classifyTrustSubtypeV2(text, registry);
  if (v2) {
    return v2;
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
    const lines =
      signal.text && signal.text.length > MAX_TRUST_LINE_CHARS
        ? splitTrustLines(signal.text)
        : [signal.text];

    for (const line of lines) {
      if (!line) {
        continue;
      }
      const trustType = classifyTrustText(line, registry);
      if (!trustType || trustType === "statistics") {
        continue;
      }
      patterns.push({
        trust_id: trustIdFor(landingId, seq),
        trust_type: trustType,
        text: line,
        numeric_value: parseNumericValue(line),
        block_id: findBlockForType(blocks, ["reviews", "hero"])?.block_id || null,
        evidence: makeEvidence(snapshot, {
          snapshot_field: `/trust_signals_visible/${i}`,
          verbatim_text: line,
          ambiguity: trustType === "rating_display" ? "high" : "none",
        }),
      });
      seq += 1;
    }
  }

  if (options.html) {
    const text = stripTags(options.html);
    const sentences = text.split(/(?<=[.!?])\s+/).map((s) => s.trim()).filter(Boolean);
    for (const sentence of sentences) {
      if (sentence.length > MAX_TRUST_LINE_CHARS || isTrustBoilerplate(sentence)) {
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
