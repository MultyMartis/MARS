import { readFileSync, writeFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const figPath =
  "C:/MARS Phenix/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig";
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
for (const [, arr] of children)
  arr.sort((a, b) => (a.parentIndex?.position ?? 0) - (b.parentIndex?.position ?? 0));

function isVisibleChain(id) {
  let cur = byGuid.get(id);
  while (cur) {
    if (cur.visible === false) return false;
    cur = byGuid.get(guidKey(cur.parentIndex?.guid));
  }
  return true;
}

function getText(n) {
  if (!n) return "";
  if (n.characters) return n.characters;
  for (const o of n.symbolData?.symbolOverrides || []) {
    if (o.characters) return o.characters;
    if (o.textData?.characters) return o.textData.characters;
  }
  return "";
}

function collectText(id, acc = [], depth = 0) {
  const n = byGuid.get(id);
  if (!n) return acc;
  const t = getText(n);
  if (t?.trim())
    acc.push({
      id,
      depth,
      name: n.name,
      type: n.type,
      visible: isVisibleChain(id),
      y: Math.round(n.transform?.m42 ?? n.absoluteTransform?.m42 ?? 0),
      text: t.trim(),
    });
  for (const k of children.get(id) || []) collectText(guidKey(k.guid), acc, depth + 1);
  return acc;
}

const TARGETS = [
  { label: "desktop-signs-section", id: "1:1847" },
  { label: "desktop-signs-frame", id: "1:1867" },
  { label: "desktop-vazhno", id: "1:1886" },
  { label: "mobile-signs-section", id: "1:5168" },
];

const out = { figPath, targets: {} };
for (const t of TARGETS) {
  const texts = collectText(t.id).filter((x) => x.visible);
  out.targets[t.label] = { nodeId: t.id, count: texts.length, texts };
}

const outPath = join(__dirname, "_g2-fig-text-extract.json");
writeFileSync(outPath, JSON.stringify(out, null, 2), "utf8");
console.log("wrote", outPath);
for (const [k, v] of Object.entries(out.targets)) {
  console.log(k, v.count, "text nodes");
}
