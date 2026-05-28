"use strict";

const {
  heading,
  h2,
  body,
  labelValue,
  metaTable,
  divider,
  pageBreak,
  COLORS,
  Paragraph,
  TextRun,
  AlignmentType,
} = require("./lib/docx-helpers");

function gateLabel(value) {
  if (value === true) return "APPROVED";
  if (value === false) return "NOT APPROVED";
  return String(value || "UNKNOWN");
}

function renderCover(pack, exportMeta) {
  const { meta, approvalGates } = pack;
  const gates = approvalGates || {};

  const elements = [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 400 },
      children: [
        new TextRun({
          text: "ORCA Content Pack Export",
          bold: true,
          size: 40,
          color: COLORS.heading,
          font: "Calibri",
        }),
      ],
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 600 },
      children: [
        new TextRun({
          text: "Operational specification — Website Factory handoff",
          size: 24,
          color: COLORS.muted,
          font: "Calibri",
        }),
      ],
    }),
    heading("Cover / export metadata"),
    metaTable([
      { label: "project_id", value: meta.project_ref || "—", mono: true },
      { label: "route_id", value: meta.route_slug || "—", mono: true },
      { label: "pack_id", value: meta.pack_id || "—", mono: true },
      { label: "pack_version", value: meta.pack_version || "—" },
      { label: "export_version", value: exportMeta.exportVersion },
      { label: "generated_at", value: exportMeta.generatedAt },
      { label: "exported_by", value: exportMeta.exportedBy },
      { label: "canonical_url", value: meta.canonical_url || "—", mono: true },
      { label: "locale", value: meta.locale || "—" },
      { label: "artifact_state", value: meta.artifact_state || "—" },
      { label: "content_mode", value: meta.content_mode || "MODE_1" },
      {
        label: "semantic_lock",
        value: meta.semantic_lock === "active" ? "ACTIVE (MODE 1)" : String(meta.semantic_lock || "—"),
      },
    ]),
    divider(),
    h2("Approval states (snapshot)"),
    metaTable([
      {
        label: "approved_for_factory",
        value: gateLabel(gates.approved_for_factory),
      },
      {
        label: "approved_for_client_export",
        value: gateLabel(gates.approved_for_client_export),
      },
      { label: "approved_for_ads", value: gateLabel(gates.approved_for_ads) },
      { label: "approved_for_launch", value: gateLabel(gates.approved_for_launch) },
    ]),
    body(
      "Human-operated gates only. This export does not grant or modify approvals.",
      { italic: true, color: COLORS.muted }
    ),
    divider(),
    labelValue("Page name", "Манипулятор 5 тонн в Краснодаре"),
    labelValue("Document type", "PPC capability landing — semantic lock export"),
    pageBreak(),
  ];

  return elements;
}

module.exports = { renderCover };
