import { readFileSync } from "fs";
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
function allStrings(n, acc=[]) {
  if (!n) return acc;
  if (n.characters) acc.push({src:'characters', text:n.characters});
  if (n.name && /[А-Яа-яЁё]/.test(n.name) && n.name.length>6) acc.push({src:'name', text:n.name});
  for (const o of n.symbolData?.symbolOverrides||[]) {
    if (o.characters) acc.push({src:'override.characters', text:o.characters});
    if (o.textData?.characters) acc.push({src:'override.textData', text:o.textData.characters});
    if (o.name && /[А-Яа-яЁё]/.test(o.name) && o.name.length>6) acc.push({src:'override.name', text:o.name});
  }
  return acc;
}
function walk(id, depth=0, acc=[]) {
  const n = byGuid.get(id);
  if (!n) return acc;
  const strs = allStrings(n);
  if (strs.length) acc.push({id, depth, type:n.type, name:n.name, strs});
  for (const k of children.get(id)||[]) walk(guidKey(k.guid), depth+1, acc);
  return acc;
}
const targets = ["1:3492","1:3558","1:3654","1:7097","1:7151","1:7181"];
for (const t of targets) {
  console.log(`\n===== ${t} ${byGuid.get(t)?.name} =====`);
  const rows = walk(t).filter(r=>!/^Пункт|^Кнопка$|^Тэг$|^Frame|^Vector|^Group|^Rectangle|^Ellipse|^Line|^Mask|^Component|^Instance$/.test(r.name));
  rows.slice(0,80).forEach(r=>{
    for (const s of r.strs) console.log(' '.repeat(r.depth)+`[${r.type}] ${r.name} (${s.src}): ${s.text.slice(0,160)}`);
  });
  console.log('total rows', rows.length);
}
