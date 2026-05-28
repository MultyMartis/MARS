"use strict";

const {
  heading,
  h2,
  h3,
  body,
  labelValue,
  bullet,
  divider,
  ctaBlock,
  lockBlock,
  metaTable,
  preformattedBlock,
  warningBlock,
} = require("./lib/docx-helpers");

function parseCtaLines(ctaText) {
  if (!ctaText) return [];
  const lines = [];
  const rows = ctaText.match(/\|[^|\n]+\|/g);
  if (rows) {
    for (const row of rows) {
      if (row.includes("---") || row.includes("Role")) continue;
      const cells = row.split("|").filter((c) => c.trim());
      if (cells.length >= 2) lines.push(`${cells[0].trim()}: ${cells[1].trim()}${cells[2] ? " → " + cells[2].trim() : ""}`);
    }
  }
  if (!lines.length && ctaText.trim()) {
    for (const line of ctaText.split("\n")) {
      const t = line.replace(/^[-*]\s+/, "").trim();
      if (t) lines.push(t);
    }
  }
  return lines;
}

function renderSection(section, pack) {
  const elements = [];
  const { contract, copyBlocks, cta, proof, semanticLocks, safeUnknown, factoryNotes } =
    section;

  elements.push(heading(section.displayTitle));
  elements.push(
    body(`Section ID: ${contract.section_id || section.titleKey.toLowerCase()}`, {
      italic: true,
    })
  );

  if (contract.section_purpose) {
    elements.push(labelValue("Purpose", contract.section_purpose));
  }
  if (section.ppcContinuity) {
    elements.push(labelValue("PPC continuity", section.ppcContinuity));
  }
  if (contract.seo_continuity || section.seoContinuity) {
    elements.push(labelValue("SEO continuity", contract.seo_continuity || section.seoContinuity));
  }

  elements.push(divider());
  elements.push(h2("Content"));

  if (copyBlocks) {
    elements.push(...preformattedBlock(copyBlocks.replace(/🔒/g, "[LOCK]")));
  } else {
    elements.push(body("(No copy blocks subsection — see pack source)"));
  }

  const ctaLines = parseCtaLines(cta);
  if (ctaLines.length) {
    elements.push(h3("CTA"));
    elements.push(ctaBlock(ctaLines));
  }

  if (proof) {
    elements.push(h3("Proof elements"));
    elements.push(...preformattedBlock(proof));
  }

  if (semanticLocks.length) {
    elements.push(h3("Semantic lock state"));
    elements.push(lockBlock(semanticLocks.map((l) => `🔒 ${l}`)));
  } else {
    elements.push(h3("Semantic lock state"));
    elements.push(lockBlock(["Active — inherit global MODE 1 locks from pack"]));
  }

  if (safeUnknown.length) {
    elements.push(h3("Section SAFE UNKNOWN"));
    elements.push(warningBlock("⚠ Unverified in this section", safeUnknown));
  }

  if (factoryNotes) {
    elements.push(h3("Frontend / Factory notes"));
    elements.push(...preformattedBlock(factoryNotes));
  }

  elements.push(
    metaTable([
      { label: "semantic_lock", value: "ACTIVE (MODE 1)", mono: false },
      { label: "section_export", value: "validated", mono: false },
    ])
  );

  elements.push(divider());
  return elements;
}

function renderPpcContinuity(pack) {
  const elements = [heading("PPC continuity", require("docx").HeadingLevel.HEADING_1)];
  elements.push(body("Validated export state — ad ↔ landing continuity for operator review."));

  if (pack.ppc.rows.length) {
    elements.push(metaTable(pack.ppc.rows.map((r) => ({ label: r.label, value: r.value }))));
  }

  elements.push(h2("Intent continuity"));
  elements.push(
    bullet(
      "Primary intents: манипулятор 5 тонн Краснодар · заказать · борт 5 т · стрела 3 т · цена"
    )
  );
  elements.push(
    body(
      "Hero and specs must match ad callouts: 5 т board, 3 т boom, 14 m reach. Mismatch = launch blocker for group 01.",
      { italic: true }
    )
  );
  elements.push(divider());
  return elements;
}

function renderSeoContinuity(pack) {
  const elements = [heading("SEO continuity")];
  if (pack.seo.rows.length) {
    elements.push(metaTable(pack.seo.rows.map((r) => ({ label: r.label, value: r.value }))));
  }
  elements.push(
    body("Default robots: noindex,nofollow until operator opens indexing.", { italic: true })
  );
  elements.push(divider());
  return elements;
}

module.exports = { renderSection, renderPpcContinuity, renderSeoContinuity };
