import { readFileSync, readdirSync, writeFileSync } from "fs";
import { join } from "path";
import { parseFig } from "openfig-core";

const figPath = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN`;
const figFile = readdirSync(figPath).find((f) => f.endsWith(".fig"));
const doc = parseFig(new Uint8Array(readFileSync(join(figPath, figFile))));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const byGuid = new Map(nodes.map((n) => [guidKey(n.guid), n]));
const children = new Map();
for (const n of nodes) {
  const pk = guidKey(n.parentIndex?.guid);
  if (!pk) continue;
  if (!children.has(pk)) children.set(pk, []);
  children.get(pk).push(n);
}
function sortedKids(id) {
  return [...(children.get(id) || [])].sort(
    (a, b) => (a.parentIndex?.position ?? 0) - (b.parentIndex?.position ?? 0),
  );
}
function hashHex(h) {
  if (!h) return null;
  if (typeof h === "string") return h;
  if (Buffer.isBuffer(h)) return h.toString("hex");
  return Buffer.from(Object.values(h)).toString("hex");
}
function getText(n) {
  const c = n.textData?.characters ?? n.characters;
  return c && String(c).trim() ? String(c).trim() : null;
}
function getInstanceText(inst) {
  const symId = inst.symbolData?.symbolID ? guidKey(inst.symbolData.symbolID) : null;
  if (!symId) return null;
  const texts = [];
  function collect(id) {
    const n = byGuid.get(id);
    if (!n) return;
    const t = getText(n);
    if (t) texts.push(t);
    for (const k of sortedKids(id)) collect(guidKey(k.guid));
  }
  collect(symId);
  return texts;
}
function nodeInfo(id) {
  const n = byGuid.get(id);
  if (!n) return null;
  const imageFill = (n.fillPaints || []).find((p) => p.type === "IMAGE" || p.imageHash);
  return {
    id,
    name: n.name,
    type: n.type,
    size: n.size ? { w: Math.round(n.size.x), h: Math.round(n.size.y) } : null,
    text: getText(n),
    fontSize: n.fontSize,
    fontName: n.fontName,
    imageHash: imageFill ? hashHex(imageFill.imageHash || imageFill.image?.hash) : null,
    instanceText: n.type === "INSTANCE" ? getInstanceText(n) : null,
  };
}
function walk(id, depth = 0, acc = []) {
  const n = byGuid.get(id);
  if (!n || depth > 14) return acc;
  acc.push({ ...nodeInfo(id), depth });
  for (const k of sortedKids(id)) walk(guidKey(k.guid), depth + 1, acc);
  return acc;
}

const footerSymbolWalk = walk("1:584");
const footerInstanceWalk = walk("1:1309");
const textNodes = footerSymbolWalk.filter((n) => n.text);
const instanceNodes = footerSymbolWalk.filter((n) => n.instanceText?.length);

const result = {
  footerInstance: nodeInfo("1:1309"),
  footerSymbol: nodeInfo("1:584"),
  rowCount: 3,
  textNodes,
  instanceNodes,
  allTexts: textNodes.map((n) => ({ id: n.id, name: n.name, text: n.text })),
  buttonInstances: instanceNodes.map((n) => ({
    id: n.id,
    name: n.name,
    size: n.size,
    texts: n.instanceText,
  })),
};

writeFileSync(
  String.raw`C:\AI MARS\workspaces\fp-0002-shpigovsky-v2\reports\_footer_fig_walk_v1.json`,
  JSON.stringify(result, null, 2),
);
console.log(JSON.stringify(result, null, 2));
