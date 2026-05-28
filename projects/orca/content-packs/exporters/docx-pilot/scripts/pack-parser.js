"use strict";

const fs = require("fs");

const SECTION_HEADER = /^#\s+(\d{2})\s+(.+?)\s*$/gm;
const SAFE_UNKNOWN_MARK = /SAFE\s+UNKNOWN/i;

function parseFrontmatter(text) {
  const match = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) return { meta: {}, approvalGates: {} };

  const meta = {};
  const approvalGates = {};
  let inGates = false;

  for (const line of match[1].split("\n")) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("#")) continue;

    if (trimmed === "approval_gates:") {
      inGates = true;
      continue;
    }

    if (inGates) {
      const gateMatch = trimmed.match(/^(\w+):\s*(.+)$/);
      if (gateMatch) {
        const val = gateMatch[2].trim();
        approvalGates[gateMatch[1]] =
          val === "true" ? true : val === "false" ? false : val;
        continue;
      }
      if (!line.startsWith("  ") && !line.startsWith("\t")) inGates = false;
    }

    const kv = trimmed.match(/^([\w_]+):\s*(.*)$/);
    if (kv && !inGates) {
      meta[kv[1]] = kv[2].replace(/^["']|["']$/g, "");
    }
  }

  return { meta, approvalGates };
}

function extractTableRows(block) {
  const rows = [];
  const lines = block.split("\n");
  for (const line of lines) {
    if (!line.trim().startsWith("|")) continue;
    if (/^\|[\s\-:|]+\|$/.test(line.trim())) continue;
    const cells = line
      .split("|")
      .slice(1, -1)
      .map((c) => c.trim().replace(/\*\*/g, ""));
    if (cells.length >= 2) rows.push({ label: cells[0], value: cells.slice(1).join(" | ") });
  }
  return rows;
}

function extractContract(block) {
  const contractIdx = block.indexOf("| Contract |");
  if (contractIdx === -1) return {};
  const slice = block.slice(contractIdx, contractIdx + 800);
  const rows = extractTableRows(slice);
  const contract = {};
  for (const r of rows) {
    const key = r.label.toLowerCase().replace(/\s+/g, "_");
    contract[key] = r.value;
  }
  return contract;
}

function extractSubsection(block, heading) {
  const re = new RegExp(`###\\s+${heading}[^\\n]*\\n([\\s\\S]*?)(?=###\\s+|##\\s+|#\\s+0\\d\\s+|$)`, "i");
  const m = block.match(re);
  return m ? m[1].trim() : "";
}

function extractListItems(text) {
  const items = [];
  for (const line of text.split("\n")) {
    const m = line.match(/^[-*]\s+\*\*([^:*]+):\*\*\s*(.*)$/);
    if (m) {
      items.push({ label: m[1].trim(), text: m[2].trim() });
      continue;
    }
    const bullet = line.match(/^[-*]\s+(.+)$/);
    if (bullet) items.push({ text: bullet[1].replace(/\*\*/g, "").trim() });
  }
  return items;
}

function extractSafeUnknownLines(block) {
  const items = [];
  const suBlock = extractSubsection(block, "SAFE UNKNOWN");
  if (suBlock) {
    for (const line of suBlock.split("\n")) {
      const t = line.replace(/^[-*⚠\s]+/, "").trim();
      if (t) items.push(t);
    }
  }
  for (const line of block.split("\n")) {
    if (SAFE_UNKNOWN_MARK.test(line) && !line.startsWith("###")) {
      const cleaned = line.replace(/###\s*/, "").replace(/⚠/g, "").trim();
      if (cleaned && !items.includes(cleaned)) items.push(cleaned);
    }
  }
  return items;
}

function extractSemanticLocks(block) {
  const lockBlock = extractSubsection(block, "Semantic locks");
  if (!lockBlock) return [];
  return extractListItems(lockBlock).map((i) => i.text || `${i.label}: ${i.text}`);
}

function parseSections(body) {
  const parts = body.split(SECTION_HEADER);
  const sections = [];

  // split with capturing groups yields: [preamble, num, key, body, num, key, body, ...]
  for (let i = 1; i < parts.length; i += 3) {
    if (i + 2 > parts.length) break;
    const number = parts[i].trim();
    const titleKey = parts[i + 1].trim();
    const rest = parts[i + 2] || "";
    const block = `# ${number} ${titleKey}\n${rest}`;

    const contract = extractContract(block);
    const copyBlocks = extractSubsection(block, "Copy blocks");
    const cta = extractSubsection(block, "CTA");
    const proof = extractSubsection(block, "Proof elements");
    const factoryNotes = extractSubsection(block, "Factory notes");

    sections.push({
      number,
      titleKey,
      title: contract.section_id || titleKey.toLowerCase(),
      displayTitle: formatSectionTitle(number, titleKey),
      contract,
      copyBlocks,
      cta,
      proof,
      semanticLocks: extractSemanticLocks(block),
      safeUnknown: extractSafeUnknownLines(block),
      factoryNotes,
      ppcContinuity: contract.ppc_continuity || "",
      seoContinuity: contract.seo_continuity || "",
      raw: block.trim(),
    });
  }

  return sections;
}

function formatSectionTitle(number, key) {
  const names = {
    HERO: "Hero",
    SPECS: "Параметры техники",
    "ALLOWED TASKS": "Для каких задач подходит",
    ALLOWED_TASKS: "Для каких задач подходит",
    "DENIED TASKS": "Что не перевозим",
    DENIED_TASKS: "Что не перевозим",
    "ORDER FLOW": "Как заказать",
    ORDER_FLOW: "Как заказать",
    PRICING: "Стоимость",
    TRUST: "Доверие",
    B2B: "Для организаций",
    FAQ: "FAQ",
    "FINAL CTA": "Финальный CTA",
    FINAL_CTA: "Финальный CTA",
  };
  return `${number} — ${names[key] || names[key.replace(/\s+/g, "_")] || key}`;
}

function extractBlockBetween(body, startHeading, endPattern) {
  const re = new RegExp(
    `##\\s+${startHeading}[\\s\\S]*?(?=##\\s+(?:${endPattern})|$)`,
    "i"
  );
  const m = body.match(re);
  return m ? m[0] : "";
}

function parsePackFile(filePath) {
  const raw = fs.readFileSync(filePath, "utf8");
  const { meta, approvalGates } = parseFrontmatter(raw);
  const body = raw.replace(/^---[\s\S]*?---\r?\n/, "");

  const ppcBlock = extractBlockBetween(body, "PPC continuity", "SEO continuity|# 01");
  const seoBlock = extractBlockBetween(body, "SEO continuity", "Positioning|# 01|## Page");
  const signoffMatch = body.match(/## Operator sign-off[\s\S]*?(?=\n---|\n\*End)/i);

  const sections = parseSections(body);
  const allSafeUnknown = [];

  const globalUnknowns = [
    "Live canonical URL — verify before launch indexing",
    "Final NAP / business hours — operator sign-off required",
    "Form action endpoint — not confirmed in pack",
    "Exact hourly rate in RUB — not published until operator approval",
  ];

  for (const s of sections) {
    for (const u of s.safeUnknown) {
      if (!allSafeUnknown.includes(u)) allSafeUnknown.push(u);
    }
  }

  for (const g of globalUnknowns) {
    if (!allSafeUnknown.some((u) => u.toLowerCase().includes(g.split("—")[0].trim().toLowerCase().slice(0, 20)))) {
      allSafeUnknown.push(g);
    }
  }

  const operatorApprovals = signoffMatch
    ? extractTableRows(signoffMatch[0]).filter((r) => r.label.includes("approved"))
    : [];

  return {
    meta,
    approvalGates,
    ppc: { raw: ppcBlock.trim(), rows: extractTableRows(ppcBlock) },
    seo: { raw: seoBlock.trim(), rows: extractTableRows(seoBlock) },
    sections,
    safeUnknown: allSafeUnknown,
    operatorApprovals,
    sourcePath: filePath,
  };
}

module.exports = { parsePackFile, extractTableRows };
