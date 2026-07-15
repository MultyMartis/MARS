import { readFileSync, writeFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dir = dirname(fileURLToPath(import.meta.url));
const figPath =
  "C:\\MARS Phenix\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN\\Spig_v1.2.fig";
const outPath =
  "C:\\MARS Phenix\\AI MARS STORAGE\\website-factory\\fp-0002-shpigovsky-v8\\o-centre-asset-content-resolution\\temp\\FP-0002-V8-OCENTRE-SPIG-V1-RAW-EXTRACT.json";

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
  return c != null && String(c).trim() ? String(c) : null;
}

function findFrame(nameExact) {
  return nodes.find((n) => n.name === nameExact && n.type === "FRAME") || null;
}

function walk(id, visitor, depth = 0, path = []) {
  const n = byGuid.get(id);
  if (!n) return;
  const nextPath = [...path, n.name || n.type];
  visitor(n, depth, nextPath);
  for (const k of sortedKids(id)) walk(guidKey(k.guid), visitor, depth + 1, nextPath);
}

function collectTexts(rootId) {
  const texts = [];
  walk(rootId, (n, depth, path) => {
    if (!isVisible(n)) return;
    const t = getText(n);
    if (t) {
      texts.push({
        id: guidKey(n.guid),
        name: n.name,
        text: t,
        depth,
        path: path.join(" > "),
        fontSize: n.fontSize ?? null,
      });
    }
  });
  return texts;
}

function collectImages(rootId) {
  const images = [];
  walk(rootId, (n, depth, path) => {
    if (!isVisible(n)) return;
    const fills = n.fillPaints || [];
    for (const f of fills) {
      if (f.type === "IMAGE" && f.imageRef) {
        images.push({
          nodeId: guidKey(n.guid),
          nodeName: n.name,
          nodeType: n.type,
          imageRef: f.imageRef,
          path: path.join(" > "),
          w: n.size?.x ?? null,
          h: n.size?.y ?? null,
        });
      }
    }
  });
  return images;
}

function sectionSummary(frame) {
  const id = guidKey(frame.guid);
  const kids = sortedKids(id).map((k) => ({
    id: guidKey(k.guid),
    name: k.name,
    type: k.type,
    w: k.size?.x ?? null,
    h: k.size?.y ?? null,
  }));
  return {
    frameId: id,
    frameName: frame.name,
    w: frame.size?.x,
    h: frame.size?.y,
    directChildren: kids,
    texts: collectTexts(id),
    images: collectImages(id),
  };
}

const desktop = findFrame("О центре");
const mobile = findFrame("О центре - моб");

if (!desktop || !mobile) {
  console.error("Missing O-centre frames", { desktop: !!desktop, mobile: !!mobile });
  process.exit(1);
}

const desktopSections = sortedKids(guidKey(desktop.guid))
  .filter((n) => isVisible(n))
  .map((n) => sectionSummary(n));

const mobileSections = sortedKids(guidKey(mobile.guid))
  .filter((n) => isVisible(n))
  .map((n) => sectionSummary(n));

const out = {
  source: figPath,
  parsedAt: new Date().toISOString(),
  desktopFrame: {
    id: guidKey(desktop.guid),
    name: desktop.name,
    w: desktop.size?.x,
    h: desktop.size?.y,
  },
  mobileFrame: {
    id: guidKey(mobile.guid),
    name: mobile.name,
    w: mobile.size?.x,
    h: mobile.size?.y,
  },
  desktopSections,
  mobileSections,
};

writeFileSync(outPath, JSON.stringify(out, null, 2), "utf8");
console.log("Wrote", outPath);
console.log("Desktop sections:", desktopSections.length);
for (const s of desktopSections) {
  console.log(`  D ${s.frameName} (${s.frameId}) texts=${s.texts.length} images=${s.images.length}`);
}
