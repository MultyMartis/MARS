"use strict";

const { heading, h2, body, bullet, divider, shadedBlock, metaTable } = require("./lib/docx-helpers");

function renderFactoryNotes(pack) {
  const { meta } = pack;
  const elements = [
    heading("Factory implementation notes"),
    body(
      "Website Factory receives presentation-layer implementation guidance only. Approved copy is locked under MODE 1."
    ),
    shadedBlock(
      "Semantic lock — MODE 1 ACTIVE",
      [
        `content_mode: ${meta.content_mode || "MODE_1"}`,
        `semantic_lock: ${meta.semantic_lock || "active"}`,
        "Website Factory may NOT rewrite approved copy, headlines, specs, or CTAs.",
        "Allowed: layout, spacing, imagery slots, form wiring, anchor IDs, theme tokens.",
        "Forbidden: paraphrase locked copy, invent fleet/pricing/stats, remove SAFE UNKNOWN markers.",
      ],
      "EEEEEE",
      "999999"
    ),
    divider(),
    h2("Implementation scope"),
    bullet("Map sections 01–10 to v4 partials per section factory_notes"),
    bullet("Preserve CTA targets: #contacts, tel:+79004658331"),
    bullet("Messenger order in final CTA: MAX → Telegram → WhatsApp"),
    bullet("Remove legacy fleet framing («автопарк», «5–10 т») from hero/trust"),
    bullet("No hero hourly rate until operator publishes approved figure"),
    divider(),
    h2("Source artifacts"),
    metaTable([
      {
        label: "factory_workspace",
        value: "workspaces/triumph-manipulator-landing-v4/",
        mono: true,
      },
      {
        label: "handoff",
        value: "projects/orca/ppc/triumph-manipulator/handoff/…5-tonn-handoff.md",
        mono: true,
      },
      {
        label: "blueprint",
        value: "landing-pages/05-capability-5-ton.md",
        mono: true,
      },
    ]),
    divider(),
  ];

  return elements;
}

module.exports = { renderFactoryNotes };
