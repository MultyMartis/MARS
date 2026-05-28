"use strict";

const { heading, body, warningBlock, bullet, divider, metaTable } = require("./lib/docx-helpers");

const CANONICAL_UNKNOWNS = [
  "Live canonical URL — verify DNS/SSL and route before indexing",
  "Final NAP (name, address, phone) and business hours — operator sign-off",
  "Form action endpoint — unknown until Factory wiring confirmed",
  "Exact hourly rate in RUB — not published until operator supplies approved figure",
  "Review widget URLs — pending integration",
  "VAT / closing documents wording — confirm before B2B claims",
  "Production messenger deep links — verify per channel",
];

function renderSafeUnknown(pack) {
  const combined = [...pack.safeUnknown];
  for (const item of CANONICAL_UNKNOWNS) {
    if (!combined.some((u) => u.toLowerCase().includes(item.slice(0, 25).toLowerCase()))) {
      combined.push(item);
    }
  }

  const elements = [
    heading("SAFE UNKNOWN — operator review required"),
    body(
      "The following items are intentionally unresolved. Website Factory and ads must NOT invent values.",
      { italic: true }
    ),
    warningBlock(
      "⚠ DO NOT AUTO-RESOLVE",
      combined.map((u, i) => `${i + 1}. ${u}`)
    ),
    divider(),
    heading("SAFE UNKNOWN classification"),
    metaTable([
      { label: "live_urls", value: "unverified" },
      { label: "final_nap", value: "pending operator" },
      { label: "form_endpoint", value: "unknown" },
      { label: "exact_pricing", value: "unpublished" },
      { label: "review_integrations", value: "pending" },
      { label: "export_policy", value: "preserve all UNKNOWN in DOCX and Factory handoff" },
    ]),
    divider(),
  ];

  return elements;
}

module.exports = { renderSafeUnknown };
