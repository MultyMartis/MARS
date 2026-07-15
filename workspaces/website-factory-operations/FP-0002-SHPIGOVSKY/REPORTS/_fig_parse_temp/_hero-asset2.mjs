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
function collectImages(id,acc=[]){const n=byGuid.get(id);if(!n)return acc;for(const f of n.fillPaints||[])if(f.image?.hash)acc.push({id,name:n.name,hash:f.image.hash});for(const k of children.get(id)||[])collectImages(guidKey(k.guid),acc);return acc;}
function buttonText(id){const n=byGuid.get(id);if(!n)return"";for(const o of n.symbolData?.symbolOverrides||[]){if(o.characters)return o.characters.trim();if(o.textData?.characters)return o.textData.characters.trim();}return "";}
console.log('subdiv hero btn:', buttonText('1:3540'));
console.log('subdiv hero images:', JSON.stringify(collectImages('1:3528'),null,2));
// hub hero frame 1:1311
const hub = nodes.find(n=>n.name==='Услуги хаб');
console.log('hub id', guidKey(hub?.guid));
