import { readFileSync, readdirSync } from "fs";
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
  return `#${[r, g, b].map((x) => x.toString(16).padStart(2, "0")).join("")}`;
}

function walk(id, depth = 0, acc = []) {
  const n = byGuid.get(id);
  if (!n || depth > 8) return acc;
  const fills = (n.fillPaints || []).map((p) => ({ type: p.type, hex: paintToHex(p) }));
  const text = n.textData?.characters || n.characters || null;
  acc.push({
    id,
    name: n.name,
    type: n.type,
    depth,
    fills,
    fontSize: n.fontSize,
    fontName: n.fontName,
    text: text ? String(text).trim().slice(0, 60) : null,
    cornerRadius: n.cornerRadius,
  });
  const kids = nodes
    .filter((x) => guidKey(x.parentIndex?.guid) === id)
    .sort((a, b) => (a.parentIndex?.position ?? 0) - (b.parentIndex?.position ?? 0));
  for (const k of kids) walk(guidKey(k.guid), depth + 1, acc);
  return acc;
}

const inst = byGuid.get("1:900");
const symId = guidKey(inst?.symbolData?.symbolID);
console.log(JSON.stringify({ buttonTree: walk("1:900"), symbolTree: walk(symId) }, null, 2));
