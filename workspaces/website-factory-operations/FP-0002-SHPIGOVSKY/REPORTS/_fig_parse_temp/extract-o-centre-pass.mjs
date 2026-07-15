import { readFileSync, writeFileSync } from "fs";
import { createHash } from "crypto";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const figPath =
  "C:/MARS Phenix/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig";
const outRepo =
  "C:/MARS Phenix/AI MARS/workspaces/fp-0002-shpigovsky-v8/audits/o-centre-asset-content-resolution/data/FP-0002-V8-OCENTRE-SPIG-V1-FIG-EXTRACT.json";
const outStorage =
  "C:/MARS Phenix/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8/o-centre-asset-content-resolution/temp/FP-0002-V8-OCENTRE-SPIG-V1-FIG-EXTRACT.json";

const { parseFig } = await import("openfig-core");
const figBytes = readFileSync(figPath);
const doc = parseFig(new Uint8Array(figBytes));
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
  if (n.textData?.characters) return n.textData.characters;
  for (const o of n.symbolData?.symbolOverrides || []) {
    if (o.characters) return o.characters;
    if (o.textData?.characters) return o.textData.characters;
  }
  return "";
}

function collectText(id, acc = [], depth = 0, section = null) {
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
      text: t.trim(),
      section,
    });
  for (const k of children.get(id) || [])
    collectText(guidKey(k.guid), acc, depth + 1, section);
  return acc;
}

function collectImages(id, acc = [], section = null) {
  const n = byGuid.get(id);
  if (!n) return acc;
  for (const f of n.fillPaints || []) {
    if (f.type === "IMAGE" || f.image)
      acc.push({
        id,
        name: n.name,
        hash: f.image?.hash || null,
        imageRef: f.imageRef || null,
        section,
        w: Math.round(n.size?.x || 0),
        h: Math.round(n.size?.y || 0),
      });
  }
  for (const k of children.get(id) || [])
    collectImages(guidKey(k.guid), acc, section);
  return acc;
}

function sectionKids(frameId) {
  return (children.get(frameId) || [])
    .filter((k) => k.type === "FRAME" || k.type === "INSTANCE")
    .map((k) => ({
      id: guidKey(k.guid),
      name: k.name,
      type: k.type,
      w: Math.round(k.size?.x || 0),
      h: Math.round(k.size?.y || 0),
    }));
}

function findFrameByName(name) {
  const frame = nodes.find((n) => n.type === "FRAME" && n.name === name);
  if (!frame) return null;
  return {
    id: guidKey(frame.guid),
    name: frame.name,
    w: Math.round(frame.size?.x || 0),
    h: Math.round(frame.size?.y || 0),
  };
}

const desktop = findFrameByName("О центре");
const mobile = findFrameByName("О центре - моб");

const desktopSectionTexts = {};
const desktopSectionImages = {};
for (const sec of desktop ? sectionKids(desktop.id) : []) {
  desktopSectionTexts[sec.name] = collectText(sec.id, [], 0, sec.name).filter((x) => x.visible);
  desktopSectionImages[sec.name] = collectImages(sec.id, [], sec.name);
}

const out = {
  figPath,
  figSha256: createHash("sha256").update(figBytes).digest("hex"),
  parsedAt: new Date().toISOString(),
  desktop,
  mobile,
  desktopSections: desktop ? sectionKids(desktop.id) : [],
  mobileSections: mobile ? sectionKids(mobile.id) : [],
  desktopTexts: desktop ? collectText(desktop.id).filter((x) => x.visible) : [],
  mobileTexts: mobile ? collectText(mobile.id).filter((x) => x.visible) : [],
  desktopImages: desktop ? collectImages(desktop.id) : [],
  mobileImages: mobile ? collectImages(mobile.id) : [],
  desktopSectionTexts,
  desktopSectionImages,
};

writeFileSync(outRepo, JSON.stringify(out, null, 2), "utf8");
writeFileSync(outStorage, JSON.stringify(out, null, 2), "utf8");
console.log("sections", out.desktopSections.length, "texts", out.desktopTexts.length, "images", out.desktopImages.length);
const tabs = out.desktopTexts.filter((t) => t.type === "INSTANCE" && t.name === "Тэг");
console.log("tags", tabs.map((t) => t.text));
