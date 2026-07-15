import { readFileSync, writeFileSync } from "fs";
const figPath = "C:/MARS Phenix/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig";
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
for (const [, arr] of children) arr.sort((a, b) => (a.parentIndex?.position ?? 0) - (b.parentIndex?.position ?? 0));
function getText(n) {
  if (!n) return "";
  if (n.characters) return n.characters;
  for (const o of n.symbolData?.symbolOverrides || []) {
    if (o.characters) return o.characters;
    if (o.textData?.characters) return o.textData.characters;
  }
  return "";
}
function isVisible(id) {
  let c = byGuid.get(id);
  while (c) {
    if (c.visible === false) return false;
    c = byGuid.get(guidKey(c.parentIndex?.guid));
  }
  return true;
}
function collectText(id, acc = [], d = 0) {
  const n = byGuid.get(id);
  if (!n) return acc;
  const t = getText(n);
  if (t?.trim() && isVisible(id)) acc.push({ id, d, name: n.name, text: t.trim() });
  for (const k of children.get(id) || []) collectText(guidKey(k.guid), acc, d + 1);
  return acc;
}
function collectImages(id, acc = []) {
  const n = byGuid.get(id);
  if (!n) return acc;
  for (const f of n.fillPaints || []) if (f.image?.hash) acc.push({ id, name: n.name });
  for (const k of children.get(id) || []) collectImages(guidKey(k.guid), acc);
  return acc;
}
function sectionKids(fid) {
  return (children.get(fid) || [])
    .filter((k) => k.type === "FRAME" || k.type === "INSTANCE")
    .map((k) => {
      const id = guidKey(k.guid);
      const n = byGuid.get(id);
      return {
        id,
        name: k.name,
        y: Math.round(n?.transform?.m42 ?? n?.relativeTransform?.[1]?.[2] ?? 0),
        w: Math.round(k.size?.x || 0),
        h: Math.round(k.size?.y || 0),
      };
    });
}
const desktop = "1:3491";
const mobile = "1:7096";
const sections = { desktop: sectionKids(desktop), mobile: sectionKids(mobile) };
const blocks = {};
for (const view of ["desktop", "mobile"]) {
  for (const s of sections[view]) {
    const key = `${view}:${s.id}`;
    const texts = collectText(s.id);
    blocks[key] = {
      frame: s,
      texts,
      images: collectImages(s.id),
      textCount: texts.length,
      imgCount: collectImages(s.id).length,
      ctaCount: texts.filter((t) => /запис|консультац|звонок|узнать/i.test(t.text)).length,
      heading: texts.find((t) => t.d <= 2 && t.text.length > 8 && t.text.length < 120)?.text || s.name,
    };
  }
}
writeFileSync(process.argv[2], JSON.stringify({ sections, blocks }, null, 2));
for (const s of sections.desktop) {
  const b = blocks[`desktop:${s.id}`];
  console.log(`${s.id}\t${s.name}\t${s.h}\ttexts=${b.textCount}\timgs=${b.imgCount}\tcta=${b.ctaCount}`);
}
