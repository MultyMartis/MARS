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
function getText(n){if(!n)return"";if(n.characters)return n.characters;for(const o of n.symbolData?.symbolOverrides||[]){if(o.characters)return o.characters;if(o.textData?.characters)return o.textData.characters;}return"";}
function collectText(id,acc=[],depth=0){const n=byGuid.get(id);if(!n)return acc;const t=getText(n);if(t?.trim())acc.push({id,depth,name:n.name,type:n.type,text:t.trim()});for(const k of children.get(id)||[])collectText(guidKey(k.guid),acc,depth+1);return acc;}
function findByName(rootId, name, acc=[]){const n=byGuid.get(rootId);if(n?.name===name)acc.push({id:rootId,name,w:Math.round(n.size?.x||0),h:Math.round(n.size?.y||0)});for(const k of children.get(rootId)||[])findByName(guidKey(k.guid),name,acc);return acc;}
const desktop = "1:3491";
const mobile = "1:7096";
const names = ["1 - Главный экран","2 - Дом - вступление","3- Услуги","Этапы процедуры","Моби","Психические расстройствв","Зависимости и пристрастия"];
for (const nm of names) {
  console.log(`\n## find ${nm}`);
  for (const hit of findByName(desktop,nm).concat(findByName(mobile,nm))) {
    const texts = collectText(hit.id).slice(0,15);
    console.log(hit.id, hit.w+'x'+hit.h, texts.length, 'texts');
    texts.forEach(t=>console.log(' ', t.name+':', t.text.slice(0,120)));
  }
}
