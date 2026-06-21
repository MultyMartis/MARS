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

function nodeSize(n) {
  if (n.size?.x != null) return { w: Math.round(n.size.x), h: Math.round(n.size.y) };
  if (n.absoluteBoundingBox)
    return {
      w: Math.round(n.absoluteBoundingBox.width),
      h: Math.round(n.absoluteBoundingBox.height),
    };
  return null;
}

function nodePosition(n) {
  if (n.transform?.m02 != null && n.transform?.m12 != null) {
    return { x: Math.round(n.transform.m02), y: Math.round(n.transform.m12) };
  }
  if (n.absoluteBoundingBox) {
    return {
      x: Math.round(n.absoluteBoundingBox.x),
      y: Math.round(n.absoluteBoundingBox.y),
    };
  }
  return { x: null, y: null };
}

function getText(n) {
  if (n.type !== "TEXT") return null;
  const c = n.textData?.characters ?? n.characters;
  return c && String(c).trim() ? String(c).trim() : null;
}

function hasImageFill(n) {
  for (const p of n.fillPaints || []) {
    if (p.image || p.imageHash || p.imageRef || p.type === "IMAGE") return true;
  }
  return false;
}

function isAutoLayout(n) {
  return !!(n.stackMode || (n.layoutMode && n.layoutMode !== "NONE"));
}

function sortedKids(id) {
  return [...(children.get(id) || [])].sort(
    (a, b) => (a.parentIndex?.position ?? 0) - (b.parentIndex?.position ?? 0),
  );
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
  return texts.length ? texts.join(" | ") : null;
}

function walk(id, depth = 0) {
  const n = byGuid.get(id);
  if (!n) return null;
  const pos = nodePosition(n);
  const sz = nodeSize(n);
  const kids = sortedKids(id).map((c) => walk(guidKey(c.guid), depth + 1)).filter(Boolean);
  return {
    id: guidKey(n.guid),
    name: n.name,
    type: n.type,
    x: pos.x,
    y: pos.y,
    w: sz?.w ?? null,
    h: sz?.h ?? null,
    text: getText(n),
    instanceText: n.type === "INSTANCE" ? getInstanceText(n) : null,
    isInstance: n.type === "INSTANCE",
    instanceName: n.type === "INSTANCE" ? byGuid.get(guidKey(n.symbolData?.symbolID))?.name : null,
    hasImage: hasImageFill(n),
    autoLayout: isAutoLayout(n),
    stackMode: n.stackMode || n.layoutMode || null,
    childCount: sortedKids(id).length,
    depth,
    children: kids,
  };
}

const section01 = walk("1:876");
const flat = [];
function flatten(node) {
  if (!node) return;
  const { children: ch, ...rest } = node;
  flat.push(rest);
  for (const c of ch || []) flatten(c);
}

flatten(section01);

const out = {
  figFile,
  section01,
  flatCount: flat.length,
  flat,
};

writeFileSync(
  join(String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS`, "_section01_full_decomp_v1.json"),
  JSON.stringify(out, null, 2),
);
console.log("flatCount", flat.length);
console.log("topChildren", section01.children.map((c) => `${c.name} (${c.id})`));
