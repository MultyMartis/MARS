"use strict";

const { heading, body, metaTable, divider, shadedBlock, pageBreak } = require("./lib/docx-helpers");

function gateStatus(value) {
  if (value === true) return "YES — approved";
  if (value === false) return "NO — not approved";
  return "UNKNOWN";
}

function renderApprovals(pack, exportMeta) {
  const gates = pack.approvalGates || {};
  const elements = [
    pageBreak(),
    heading("Approval section — human-operated only"),
    body(
      "This section records approval gate snapshot at export time. Export tooling does not grant approvals.",
      { italic: true }
    ),
    metaTable([
      {
        label: "approved_for_factory",
        value: gateStatus(gates.approved_for_factory),
      },
      {
        label: "approved_for_ads",
        value: gateStatus(gates.approved_for_ads),
      },
      {
        label: "approved_for_launch",
        value: gateStatus(gates.approved_for_launch),
      },
      {
        label: "approved_for_client_export",
        value: gateStatus(gates.approved_for_client_export),
      },
    ]),
    divider(),
    shadedBlock(
      "Operator sign-off (blank)",
      [
        "Reviewed by: _________________________________",
        "Date: _________________________________",
        "Notes: _________________________________",
        "",
        `Export ID: ${exportMeta.exportId}`,
        `Generated: ${exportMeta.generatedAt}`,
      ],
      "F5F5F5",
      "CCCCCC"
    ),
    divider(),
    body("End of ORCA DOCX export pilot v1 — Triumph manipulyator 5 tonn pack."),
  ];

  if (pack.operatorApprovals.length) {
    elements.splice(
      3,
      0,
      ...require("./lib/docx-helpers").preformattedBlock(
        "Pack-level operator table:\n" +
          pack.operatorApprovals.map((r) => `${r.label}: ${r.value}`).join("\n")
      )
    );
  }

  return elements;
}

module.exports = { renderApprovals };
