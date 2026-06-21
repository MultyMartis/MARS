import { readFileSync, readdirSync, copyFileSync, mkdirSync, writeFileSync } from "fs";
import { join } from "path";
import { execSync } from "child_process";
import { parseFig } from "openfig-core";

const figPath = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN`;
const figFile = readdirSync(figPath).find((f) => f.endsWith(".fig"));
const figFull = join(figPath, figFile);
const doc = parseFig(new Uint8Array(readFileSync(figFull)));
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
  return [...(children.get(id) || [])].sort((a,b)=>(a.parentIndex?.position??0)-(b.parentIndex?.position??0));
}
function hashHex(h) {
  if (!h) return null;
  if (typeof h === "string") return h;
  if (Buffer.isBuffer(h)) return h.toString("hex");
  return Buffer.from(Object.values(h)).toString("hex");
}
function getText(n) {
  const c = n.textData?.characters ?? n.characters;
  return c && String(c).trim() ? String(c).trim() : null;
}
function getInstanceText(inst) {
  const symId = inst.symbolData?.symbolID ? guidKey(inst.symbolData.symbolID) : null;
  if (!symId) return null;
  const texts = [];
  function collect(id) {
    const n = byGuid.get(id);
    if (!n) return;
    const t = getText(n);
    if (t) texts.push(t);
    for (const k of sortedKids(id)) collect(guidKey(k.guid));
  }
  collect(symId);
  return texts;
}
function nodeInfo(id) {
  const n = byGuid.get(id);
  if (!n) return null;
  const imageFill = (n.fillPaints||[]).find(p=>p.type==="IMAGE"||p.imageHash);
  return {
    id, name: n.name, type: n.type,
    size: n.size ? { w: Math.round(n.size.x), h: Math.round(n.size.y) } : null,
    text: getText(n),
    fontSize: n.fontSize,
    fontName: n.fontName,
    imageHash: imageFill ? hashHex(imageFill.imageHash||imageFill.image?.hash) : null,
    cornerRadius: n.cornerRadius,
    instanceText: n.type==="INSTANCE" ? getInstanceText(n) : null,
  };
}
function walk(id, depth=0, acc=[]) {
  const n = byGuid.get(id);
  if (!n||depth>12) return acc;
  acc.push({...nodeInfo(id), depth});
  for (const k of sortedKids(id)) walk(guidKey(k.guid), depth+1, acc);
  return acc;
}
const headerWalk = walk("1:877");
const LOGO_HASH = "262f79db29ec4dc2b9ae2e793d5c8cc6382c307b";
const outDir = String.raw`C:\AI MARS\workspaces\fp-0002-shpigovsky-v2\src\img\brand`;
const tempDir = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\_fig_parse_temp\_logo_temp`;
mkdirSync(outDir, { recursive: true });
mkdirSync(tempDir, { recursive: true });
const zipEntry = `images/${LOGO_HASH}`;
const ps = `Add-Type -AssemblyName System.IO.Compression.FileSystem; $zip = [System.IO.Compression.ZipFile]::OpenRead('${figFull.replace(/'/g,"''")}'); $entry = $zip.Entries | Where-Object { $_.FullName -eq '${zipEntry}' }; if (-not $entry) { throw 'Missing ${zipEntry}' }; $dest = '${join(tempDir, LOGO_HASH).replace(/'/g,"''")}'; [System.IO.Compression.ZipFileExtensions]::ExtractToFile($entry, $dest, $true); $zip.Dispose()`;
execSync(`powershell -NoProfile -Command "${ps}"`, { stdio: "pipe" });
copyFileSync(join(tempDir, LOGO_HASH), join(outDir, "logo-shpigovsky-dom.png"));
const result = {
  headerFrame: nodeInfo("1:877"),
  rowCount: 2,
  textNodes: headerWalk.filter(n=>n.text).map(({id,name,text,fontSize,fontName,depth})=>({id,name,text,fontSize,fontName,depth})),
  instances: headerWalk.filter(n=>n.instanceText?.length).map(({id,name,instanceText,depth})=>({id,name,instanceText,depth})),
  imageNodes: headerWalk.filter(n=>n.imageHash).map(({id,name,imageHash,size,depth})=>({id,name,imageHash,size,depth})),
  logoExport: { selectedNodeId: "1:6720", hash: LOGO_HASH, file: "src/img/brand/logo-shpigovsky-dom.png" },
};
writeFileSync(String.raw`C:\AI MARS\workspaces\fp-0002-shpigovsky-v2\reports\_header_fig_walk_v1.json`, JSON.stringify(result,null,2));
console.log(JSON.stringify(result,null,2));
