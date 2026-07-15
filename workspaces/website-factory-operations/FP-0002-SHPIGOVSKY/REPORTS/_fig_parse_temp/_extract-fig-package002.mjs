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

function isVisible(n) {
  if (!n) return false;
  if (n.visible === false) return false;
  let cur = n;
  while (cur) {
    if (cur.visible === false) return false;
    const pk = guidKey(cur.parentIndex?.guid);
    cur = pk ? byGuid.get(pk) : null;
  }
  return true;
}

function getText(n) {
  if (n.type !== "TEXT") return null;
  const c = n.textData?.characters ?? n.characters;
  return c && String(c).trim() ? String(c).trim() : null;
}

function findByName(namePart) {
  return nodes.filter((n) => n.name && n.name.includes(namePart));
}

const out = {};

const intro = findByName("2 - Дом - вступление").find(
  (n) => n.type === "FRAME" || n.type === "GROUP",
);

if (intro) {
  const texts = [];
  function walk(id, depth = 0) {
    const n = byGuid.get(id);
    if (!n || !isVisible(n)) return;
    const t = getText(n);
    if (t) texts.push({ id: guidKey(n.guid), name: n.name, text: t, depth });
    for (const k of sortedKids(id)) walk(guidKey(k.guid), depth + 1);
  }
  walk(guidKey(intro.guid));
  out.introTexts = texts;
}

const svc = findByName("3- Услуги").find((n) => n.type === "FRAME");
if (svc) {
  const vecs = [];
  function walkV(id, path = []) {
    const n = byGuid.get(id);
    if (!n || !isVisible(n)) return;
    const nextPath = [...path, n.name || n.type];
    if (
      n.type === "VECTOR" ||
      n.type === "BOOLEAN_OPERATION" ||
      n.type === "STAR" ||
      n.type === "REGULAR_POLYGON"
    ) {
      const sz = n.size || n.absoluteBoundingBox;
      const w = sz?.x ?? sz?.width ?? 0;
      const h = sz?.y ?? sz?.height ?? 0;
      if (w <= 48 && h <= 48) {
        vecs.push({
          id: guidKey(n.guid),
          name: n.name,
          type: n.type,
          w,
          h,
          path: nextPath.join(" > "),
          hasVectorData: !!n.vectorData,
          fillPaints: n.fillPaints?.length || 0,
        });
      }
    }
    for (const k of sortedKids(id)) walkV(guidKey(k.guid), nextPath);
  }
  walkV(guidKey(svc.guid));
  out.serviceSmallVectors = vecs;
}

// Also search icon components by name
out.linkNamedNodes = nodes
  .filter(
    (n) =>
      isVisible(n) &&
      n.name &&
      /external|link|ссылк|arrow.*up|up-right|square/i.test(n.name),
  )
  .slice(0, 40)
  .map((n) => ({
    id: guidKey(n.guid),
    name: n.name,
    type: n.type,
    parent: byGuid.get(guidKey(n.parentIndex?.guid))?.name,
  }));

writeFileSync(
  "C:\\MARS Phenix\\AI MARS\\workspaces\\fp-0002-shpigovsky-v7\\reviews\\package-002\\_fig-extract-output.json",
  JSON.stringify(out, null, 2),
);

console.log("written", Object.keys(out));
