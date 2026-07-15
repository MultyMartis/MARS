import { readFileSync, writeFileSync } from "fs";
import { join } from "path";
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
for (const [, arr] of children) arr.sort((a,b)=>(a.parentIndex?.position??0)-(b.parentIndex?.position??0));
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
function collectText(id, acc=[], depth=0) {
  const n = byGuid.get(id);
  if (!n) return acc;
  const t = getText(n);
  if (t?.trim()) acc.push({id, depth, name:n.name, type:n.type, visible:isVisibleChain(id), text:t.trim()});
  for (const k of children.get(id)||[]) collectText(guidKey(k.guid), acc, depth+1);
  return acc;
}
function collectImages(id, acc=[]) {
  const n = byGuid.get(id);
  if (!n) return acc;
  for (const f of n.fillPaints||[]) {
    if (f.type==="IMAGE"||f.image) acc.push({id,name:n.name,hash:f.image?.hash});
  }
  for (const k of children.get(id)||[]) collectImages(guidKey(k.guid), acc);
  return acc;
}
function sectionKids(frameId) {
  const kids = (children.get(frameId)||[]).filter(k=>k.type==="FRAME"||k.type==="INSTANCE");
  return kids.map(k=>({id:guidKey(k.guid), name:k.name, w:Math.round(k.size?.x||0), h:Math.round(k.size?.y||0)}));
}
const frames = {
  desktop_page: "1:3491",
  mobile_page: "1:7096",
  hero: "1:da4",
  intro: "1:de6",
  services: "1:e46",
  mobile_hero: "1:1bb9",
  mobile_intro: "1:1bef",
  mobile_services: "1:1c0d",
};
const out = { sections: {}, texts: {}, images: {} };
for (const [k,id] of Object.entries(frames)) {
  out.sections[k] = sectionKids(id);
  out.texts[k] = collectText(id).filter(x=>x.visible);
  out.images[k] = collectImages(id);
}
const outPath = process.argv[2];
writeFileSync(outPath, JSON.stringify(out, null, 2));
for (const [k,arr] of Object.entries(out.texts)) {
  console.log(`\n=== ${k} (${arr.length}) ===`);
  arr.forEach(t=>console.log(`${" ".repeat(t.depth)}${t.name}: ${t.text.slice(0,150)}`));
}
