import { readFileSync, readdirSync, copyFileSync, mkdirSync } from "fs";
import { join } from "path";
import { parseFig } from "openfig-core";

const figPath = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN`;
const figFile = readdirSync(figPath).find((f) => f.endsWith(".fig"));
const doc = parseFig(new Uint8Array(readFileSync(join(figPath, figFile))));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const byGuid = new Map(nodes.map((n) => [guidKey(n.guid), n]));

function paintToHex(p) {
  if (!p || p.type === "IMAGE") return null;
  const c = p.color || p.solidColor;
  if (!c) return null;
  const r = Math.round((c.r ?? 0) * 255);
  const g = Math.round((c.g ?? 0) * 255);
  const b = Math.round((c.b ?? 0) * 255);
  const a = c.a ?? 1;
  if (a < 1) return `rgba(${r},${g},${b},${a.toFixed(2)})`;
  return `#${[r, g, b].map((x) => x.toString(16).padStart(2, "0")).join("")}`;
}

function nodeInfo(id) {
  const n = byGuid.get(id);
  if (!n) return null;
  const fills = (n.fillPaints || []).map((p) => ({
    type: p.type,
    hex: paintToHex(p),
    imageHash: p.imageHash || p.image?.hash || null,
  }));
  return {
    id,
    name: n.name,
    type: n.type,
    fontSize: n.fontSize,
    fontName: n.fontName,
    lineHeight: n.lineHeight,
    text: n.textData?.characters || n.characters || null,
    fills,
    cornerRadius: n.cornerRadius,
    size: n.size ? { w: Math.round(n.size.x), h: Math.round(n.size.y) } : null,
  };
}

const headerIds = [
  "1:877",
  "1:878",
  "1:879",
  "1:880",
  "1:883",
  "1:888",
  "1:889",
  "1:890",
  "1:900",
  "1:903",
  "1:911",
  "1:893",
  "1:897",
];

const out = {};
for (const id of headerIds) out[id] = nodeInfo(id);

const logo = byGuid.get("1:880");
const logoFill = logo?.fillPaints?.find((p) => p.type === "IMAGE" || p.imageHash);

const result = {
  nodes: out,
  logoImageHash: logoFill?.imageHash || logoFill?.image?.hash || null,
};

const outPath = join(figPath, "..", "..", "REPORTS", "_header_fig_extract.json");
import { writeFileSync } from "fs";
writeFileSync(outPath, JSON.stringify(result, null, 2));
console.log(JSON.stringify(result, null, 2));
