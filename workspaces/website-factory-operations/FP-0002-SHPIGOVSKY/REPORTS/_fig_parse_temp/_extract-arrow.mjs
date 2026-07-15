import { readFileSync, writeFileSync } from "fs";

const figPath =
  "C:\\MARS Phenix\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN\\Spig_v1.2.fig";

const { parseFig } = await import("openfig-core");

const doc = parseFig(new Uint8Array(readFileSync(figPath)));
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

function dumpNode(id, depth = 0) {
  const n = byGuid.get(id);
  if (!n) return [];
  const row = {
    id,
    name: n.name,
    type: n.type,
    visible: n.visible,
    size: n.size || n.absoluteBoundingBox,
    vectorNetwork: n.vectorData?.vectorNetwork ? "yes" : n.vectorNetwork ? "legacy" : "no",
    fillPaints: n.fillPaints?.map((p) => p.type),
    strokePaints: n.strokePaints?.map((p) => p.type),
  };
  const out = [row];
  for (const k of sortedKids(id)) out.push(...dumpNode(guidKey(k.guid), depth + 1));
  return out;
}

// Service item icon: Пункт услуги > arrow-up-right
const targets = ["1:3609", "1:963", "1:966"];
const result = {};
for (const t of targets) {
  result[t] = dumpNode(t);
}

writeFileSync(
  "C:\\MARS Phenix\\AI MARS\\workspaces\\fp-0002-shpigovsky-v7\\reviews\\package-002\\_fig-arrow-extract.json",
  JSON.stringify(result, null, 2),
);

console.log("done");
