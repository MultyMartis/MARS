import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const figPath =
  "C:\\MARS Phenix\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN\\Spig_v1.2.fig";

const { parseFig } = await import("openfig-core");
const doc = parseFig(new Uint8Array(readFileSync(figPath)));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const byGuid = new Map(nodes.map((n) => [guidKey(n.guid), n]));
const children = new Map();

for (const n of nodes) {
  const p = guidKey(n.parentIndex?.guid);
  if (!p) continue;
  if (!children.has(p)) children.set(p, []);
  children.get(p).push(n);
}

function getText(n) {
  if (!n) return "";
  if (n.characters) return n.characters;
  const so = n.symbolData?.symbolOverrides || [];
  for (const o of so) if (o.characters) return o.characters;
  return "";
}

function walk(id, depth = 0) {
  const n = byGuid.get(id);
  if (!n) return { error: "not found", id };
  const out = { id, name: n.name, type: n.type };
  const text = getText(n);
  if (text) out.text = text;
  if (n.fillPaints?.length) {
    out.fills = n.fillPaints.map((f) => ({
      type: f.type,
      opacity: f.opacity,
      color: f.color,
      imageHash: f.image?.hash,
    }));
  }
  if (n.strokePaints?.length) {
    out.strokes = n.strokePaints.map((s) => ({
      type: s.type,
      opacity: s.opacity,
      color: s.color,
    }));
  }
  const kids = (children.get(id) || []).sort(
    (a, b) => (a.parentIndex?.position || 0) - (b.parentIndex?.position || 0),
  );
  if (kids.length && depth < 10) {
    out.children = kids.map((k) => walk(guidKey(k.guid), depth + 1));
  }
  return out;
}

function collectText(id, acc = []) {
  const n = byGuid.get(id);
  if (!n) return acc;
  const t = getText(n);
  if (t && t.trim()) acc.push({ id, name: n.name, text: t.trim() });
  for (const k of children.get(id) || []) collectText(guidKey(k.guid), acc);
  return acc;
}

function collectImages(id, acc = []) {
  const n = byGuid.get(id);
  if (!n) return acc;
  for (const f of n.fillPaints || []) {
    if (f.type === "IMAGE" || f.image) {
      acc.push({ id, name: n.name, imageHash: f.image?.hash, transform: f.imageTransform });
    }
  }
  for (const k of children.get(id) || []) collectImages(guidKey(k.guid), acc);
  return acc;
}

const targets = [
  "1:1368",
  "1:1405",
  "1:1474",
  "1:1569",
  "32:4586",
  "1:4624",
  "1:4685",
  "1:4744",
  "1:4832",
];

const result = {
  targets: {},
  texts: {},
  images: {},
};

for (const id of targets) {
  result.targets[id] = walk(id);
  result.texts[id] = collectText(id);
  result.images[id] = collectImages(id);
}

mkdirSync(__dirname, { recursive: true });
writeFileSync(join(__dirname, "_fig-services-extract.json"), JSON.stringify(result, null, 2));
console.log("written", join(__dirname, "_fig-services-extract.json"));
