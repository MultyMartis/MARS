import { readFileSync, writeFileSync } from "fs";
import { parseFig } from "openfig-core";

const figPath =
  "C:\\MARS Phenix\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN\\Spig_v1.2.fig";
const outPath =
  "C:\\MARS Phenix\\AI MARS STORAGE\\website-factory\\fp-0002-shpigovsky-v8\\o-centre-asset-content-resolution\\temp\\FP-0002-V8-OCENTRE-HERO-PROBE.json";

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

function walk(id, visitor, path = []) {
  const n = byGuid.get(id);
  if (!n) return;
  const p = [...path, `${n.type}:${n.name}`];
  visitor(n, p);
  for (const k of children.get(id) || []) walk(guidKey(k.guid), visitor, p);
}

const desktop = nodes.find((n) => n.name === "О центре" && n.type === "FRAME");
const heroId = guidKey(
  (children.get(guidKey(desktop.guid)) || []).find((n) => n.name === "1 - Главный экран")?.guid,
);

const heroNodes = [];
const imageNodes = [];
walk(heroId, (n, path) => {
  heroNodes.push({
    id: guidKey(n.guid),
    type: n.type,
    name: n.name,
    w: n.size?.x,
    h: n.size?.y,
    fillTypes: (n.fillPaints || []).map((f) => ({ type: f.type, imageRef: f.imageRef || null })),
    path: path.join(" > "),
  });
  for (const f of n.fillPaints || []) {
    if (f.imageRef) imageNodes.push({ id: guidKey(n.guid), name: n.name, imageRef: f.imageRef, path: path.join(" > ") });
  }
});

const tabs = (children.get(heroId) || []).find((n) => n.name === "Табы");
const tabNodes = [];
if (tabs) {
  walk(guidKey(tabs.guid), (n, path) => {
    const t = n.textData?.characters ?? n.characters;
    tabNodes.push({
      id: guidKey(n.guid),
      type: n.type,
      name: n.name,
      text: t ? String(t) : null,
      path: path.join(" > "),
    });
  });
}

writeFileSync(outPath, JSON.stringify({ heroNodes: heroNodes.slice(0, 80), imageNodes, tabNodes }, null, 2));
console.log("imageNodes", imageNodes.length, "tabNodes", tabNodes.length);
