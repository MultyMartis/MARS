"use strict";

const PACK_CAPS = {
  OFFERS: 8,
  PRICING: 6,
  DELIVERY_PROMISE: 5,
  SERVICE_COVERAGE: 5,
  TRUST: 6,
  SOCIAL_PROOF: 6,
  CTA: 6,
  LEAD_CAPTURE: 6,
  CONTACT_MODEL: 6,
  MARKETING_PATTERNS: 4,
};

function capList(items, cap) {
  if (!Array.isArray(items)) {
    return [];
  }
  return items.slice(0, cap);
}

function obsByFamilies(observations, families) {
  const set = new Set(families);
  return (observations || []).filter(
    (o) => set.has(o.family) && o.status !== "safe_unknown" && o.text && !o.text.startsWith("SAFE UNKNOWN")
  );
}

function formatEvidenceRef(evidence) {
  if (!evidence) {
    return "—";
  }
  if (evidence.snapshot_field) {
    return evidence.snapshot_field;
  }
  if (evidence.source === "page_html") {
    return "page_html";
  }
  return evidence.source || "—";
}

function formatObsLine(o) {
  const cat = o.category ? ` · \`${o.category}\`` : o.sub_type ? ` · \`${o.sub_type}\`` : "";
  const conf = o.confidence || "—";
  const ev = formatEvidenceRef(o.evidence);
  return `- ${o.text}${cat} · conf **${conf}** · ev \`${ev}\``;
}

function formatLandingIntelligenceCard(obs) {
  const observations = obs.observations || [];
  const lines = [
    `## Landing intelligence — ${obs.domain}`,
    "",
    `**Refs:** \`${obs.landing_id}\` · \`${obs.snapshot_id}\` · grade **${obs.evidence_grade || "—"}**`,
    "",
    "### Value & offers",
    "",
  ];

  const offers = capList(obsByFamilies(observations, ["OFFERS"]), PACK_CAPS.OFFERS);
  if (offers.length) {
    lines.push(...offers.map(formatObsLine));
  } else {
    lines.push("- SAFE UNKNOWN — no classified offers", "");
  }

  lines.push("", "### Pricing (visible)", "");
  const pricing = capList(obsByFamilies(observations, ["PRICING"]), PACK_CAPS.PRICING);
  lines.push(...(pricing.length ? pricing.map(formatObsLine) : ["- SAFE UNKNOWN — no visible pricing lines"]));

  lines.push("", "### Delivery & coverage", "");
  const delivery = capList(
    obsByFamilies(observations, ["DELIVERY_PROMISE", "SERVICE_COVERAGE"]),
    PACK_CAPS.DELIVERY_PROMISE + PACK_CAPS.SERVICE_COVERAGE
  );
  lines.push(
    ...(delivery.length ? delivery.map(formatObsLine) : ["- SAFE UNKNOWN — no delivery or coverage lines"])
  );

  lines.push("", "### Trust & social proof", "");
  const trust = capList(
    obsByFamilies(observations, ["TRUST", "SOCIAL_PROOF"]),
    PACK_CAPS.TRUST + PACK_CAPS.SOCIAL_PROOF
  );
  lines.push(...(trust.length ? trust.map(formatObsLine) : ["- SAFE UNKNOWN — trust not extracted"]));

  lines.push("", "### Contact & CTA", "");
  const contactCta = capList(
    obsByFamilies(observations, ["CONTACT_MODEL", "CTA", "LEAD_CAPTURE"]),
    PACK_CAPS.CTA + PACK_CAPS.LEAD_CAPTURE + PACK_CAPS.CONTACT_MODEL
  );
  lines.push(...(contactCta.length ? contactCta.map(formatObsLine) : ["- SAFE UNKNOWN — contact/CTA not resolved"]));

  lines.push("", "### Page structure", "");
  const blocks = (obs.visible_blocks || obs._legacy?.visible_blocks || [])
    .map((b) => b.block_type)
    .filter(Boolean);
  if (blocks.length) {
    lines.push(`- blocks: ${blocks.join(" → ")}`);
  } else {
    lines.push("- SAFE UNKNOWN — block order not detected");
  }
  const patterns = capList(obsByFamilies(observations, ["MARKETING_PATTERNS"]), PACK_CAPS.MARKETING_PATTERNS);
  for (const p of patterns) {
    lines.push(`- pattern: ${p.sub_type || p.text}`);
  }

  lines.push("", "### SAFE UNKNOWN", "");
  const unknownRows = observations.filter((o) => o.status === "safe_unknown");
  const missingFamilies = (obs.observation_summary?.families_unknown || []).filter(
    (f) => !observations.some((o) => o.family === f && o.status !== "safe_unknown")
  );
  if (unknownRows.length) {
    for (const u of unknownRows) {
      lines.push(`- ${u.family}: ${u.reason || u.text}`);
    }
  }
  for (const f of missingFamilies) {
    lines.push(`- ${f}: no observations classified`);
  }
  if (!unknownRows.length && !missingFamilies.length) {
    lines.push("- none flagged for this landing");
  }
  lines.push("");

  return lines.join("\n");
}

function formatLandingAnalysisSummaryV2(landingIndex) {
  const landings = landingIndex?.landings || [];
  const detail = landingIndex?._detail || [];
  let familiesWithData = 0;
  let familiesUnknown = 0;

  for (const row of landings) {
    const summary = row.observation_summary;
    if (summary) {
      familiesWithData += (summary.families_present || []).length;
      familiesUnknown += (summary.families_unknown || []).length;
    }
  }

  const skipped = landings.filter((l) => l.evidence_grade === "X").length;

  return [
    "## Landing analysis summary",
    "",
    `Landings analyzed: **${landings.length}** · skipped/low capture: **${skipped}**`,
    `Observation families with data (session total): **${familiesWithData}** · family slots without data: **${familiesUnknown}**`,
    "",
    "Count-only index fields removed from operator view — see per-landing intelligence cards.",
    "",
  ].join("\n");
}

function formatLandingObservationBlocksV2(landingIndex) {
  const detail = landingIndex?._detail || [];
  const cards = detail.map((obs) => formatLandingIntelligenceCard(obs));
  return [formatLandingAnalysisSummaryV2(landingIndex), ...cards].join("\n");
}

module.exports = {
  PACK_CAPS,
  formatLandingIntelligenceCard,
  formatLandingAnalysisSummaryV2,
  formatLandingObservationBlocksV2,
};
