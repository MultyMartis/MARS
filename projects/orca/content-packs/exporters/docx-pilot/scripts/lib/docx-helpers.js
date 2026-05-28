"use strict";

const {
  Paragraph,
  TextRun,
  HeadingLevel,
  AlignmentType,
  Table,
  TableRow,
  TableCell,
  WidthType,
  BorderStyle,
  ShadingType,
  PageBreak,
} = require("docx");

const COLORS = {
  metaBg: "F5F5F5",
  ctaBg: "E8F4FD",
  ctaBorder: "B8D4E8",
  warnBg: "FFF3CD",
  warnBorder: "FFC107",
  warnText: "664D03",
  lockBg: "EEEEEE",
  divider: "CCCCCC",
  heading: "1A1A2E",
  muted: "666666",
  approved: "D4EDDA",
  denied: "F8D7DA",
};

function heading(text, level = HeadingLevel.HEADING_1) {
  return new Paragraph({
    heading: level,
    spacing: { before: 320, after: 160 },
    children: [
      new TextRun({ text, bold: true, color: COLORS.heading, font: "Calibri" }),
    ],
  });
}

function h2(text) {
  return heading(text, HeadingLevel.HEADING_2);
}

function h3(text) {
  return heading(text, HeadingLevel.HEADING_3);
}

function body(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 120, line: 276 },
    children: [
      new TextRun({
        text,
        size: 22,
        font: "Calibri",
        italics: opts.italic || false,
        bold: opts.bold || false,
        color: opts.color || "000000",
      }),
    ],
  });
}

function labelValue(label, value, mono = false) {
  return new Paragraph({
    spacing: { after: 60 },
    children: [
      new TextRun({ text: `${label}: `, bold: true, size: 20, font: "Calibri" }),
      new TextRun({
        text: value,
        size: 20,
        font: mono ? "Consolas" : "Calibri",
        color: COLORS.muted,
      }),
    ],
  });
}

function bullet(text) {
  return new Paragraph({
    bullet: { level: 0 },
    spacing: { after: 60 },
    children: [new TextRun({ text, size: 22, font: "Calibri" })],
  });
}

function divider() {
  return new Paragraph({
    spacing: { before: 200, after: 200 },
    border: {
      bottom: { style: BorderStyle.SINGLE, size: 6, color: COLORS.divider },
    },
    children: [],
  });
}

function shadedBlock(title, lines, bg, borderColor) {
  const children = [];
  if (title) {
    children.push(
      new Paragraph({
        spacing: { after: 80 },
        children: [new TextRun({ text: title, bold: true, size: 22, font: "Calibri" })],
      })
    );
  }
  for (const line of lines) {
    children.push(
      new Paragraph({
        spacing: { after: 60 },
        children: [new TextRun({ text: line, size: 20, font: "Calibri" })],
      })
    );
  }

  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({
        children: [
          new TableCell({
            shading: { fill: bg, type: ShadingType.CLEAR },
            borders: {
              top: { style: BorderStyle.SINGLE, size: 4, color: borderColor },
              bottom: { style: BorderStyle.SINGLE, size: 4, color: borderColor },
              left: { style: BorderStyle.SINGLE, size: 4, color: borderColor },
              right: { style: BorderStyle.SINGLE, size: 4, color: borderColor },
            },
            children,
          }),
        ],
      }),
    ],
  });
}

function ctaBlock(lines) {
  return shadedBlock("CTA", lines, COLORS.ctaBg, COLORS.ctaBorder);
}

function warningBlock(title, lines) {
  return shadedBlock(title, lines, COLORS.warnBg, COLORS.warnBorder);
}

function lockBlock(lines) {
  return shadedBlock("Semantic lock", lines, COLORS.lockBg, COLORS.divider);
}

function metaTable(rows) {
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: rows.map(
      (r) =>
        new TableRow({
          children: [
            new TableCell({
              width: { size: 35, type: WidthType.PERCENTAGE },
              shading: { fill: COLORS.metaBg, type: ShadingType.CLEAR },
              children: [
                new Paragraph({
                  children: [new TextRun({ text: r.label, bold: true, size: 20 })],
                }),
              ],
            }),
            new TableCell({
              width: { size: 65, type: WidthType.PERCENTAGE },
              children: [
                new Paragraph({
                  children: [
                    new TextRun({
                      text: r.value,
                      size: 20,
                      font: r.mono ? "Consolas" : "Calibri",
                    }),
                  ],
                }),
              ],
            }),
          ],
        })
    ),
  });
}

function pageBreak() {
  return new Paragraph({ children: [new PageBreak()] });
}

function preformattedBlock(text) {
  const lines = text.split("\n").filter((l) => l.trim());
  return lines.map((l) =>
    new Paragraph({
      spacing: { after: 40 },
      children: [new TextRun({ text: l, size: 20, font: "Calibri" })],
    })
  );
}

module.exports = {
  COLORS,
  heading,
  h2,
  h3,
  body,
  labelValue,
  bullet,
  divider,
  shadedBlock,
  ctaBlock,
  warningBlock,
  lockBlock,
  metaTable,
  pageBreak,
  preformattedBlock,
  Paragraph,
  TextRun,
  AlignmentType,
};
