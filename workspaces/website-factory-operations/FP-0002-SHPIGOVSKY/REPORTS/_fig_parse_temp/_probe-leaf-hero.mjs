import { readFileSync } from "fs";
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
function hashHex(h) {
  const bytes = Object.keys(h).sort((a,b)=>Number(a)-Number(b)).map(k=>h[k]);
  return Buffer.from(bytes).toString("hex");
}
function walk(id, depth=0) {
  const n = byGuid.get(id);
  if (!n) return;
  const imgs = (n.fillPaints||[]).filter(f=>f.image?.hash).map(f=>hashHex(f.image.hash));
  if (imgs.length || n.type==="RECTANGLE" || n.name?.toLowerCase().includes("image"))
    console.log("  ".repeat(depth)+`${id} ${n.type} ${n.name} ${Math.round(n.size?.x||0)}x${Math.round(n.size?.y||0)} imgs=${imgs.join(",")}`);
  for (const k of children.get(id)||[]) walk(guidKey(k.guid), depth+1);
}
console.log("=== 1:1749 hero frame ===");
walk("1:1749");
