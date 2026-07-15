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
for (const [, arr] of children) arr.sort((a,b)=>(a.parentIndex?.position??0)-(b.parentIndex?.position??0));
function textOf(n){if(!n)return"";if(n.characters)return n.characters.trim();for(const o of n.symbolData?.symbolOverrides||[]){if(o.characters)return o.characters.trim();if(o.textData?.characters)return o.textData.characters.trim();}return (n.name||"").trim();}
function walkTree(id, depth=0){const n=byGuid.get(id);if(!n)return null;const t=textOf(n);const node={id,name:n.name,type:n.type,depth,text:t||undefined,children:[]};for(const k of children.get(id)||[])node.children.push(walkTree(guidKey(k.guid),depth+1));return node;}
function collectImages(id,acc=[]){const n=byGuid.get(id);if(!n)return acc;for(const f of n.fillPaints||[])if(f.image?.hash)acc.push({id,name:n.name,hash:f.image.hash});for(const k of children.get(id)||[])collectImages(guidKey(k.guid),acc);return acc;}
const pass1 = {
  desktop_hero: walkTree("1:3492"),
  desktop_intro: walkTree("1:3558"),
  desktop_services: walkTree("1:3654"),
  mobile_hero: walkTree("1:7097"),
  mobile_intro_stack: walkTree("1:7151"),
  mobile_services: walkTree("1:7181"),
};
const outPath = process.argv[2];
writeFileSync(outPath, JSON.stringify(pass1, null, 2));
function printTexts(node, indent=0){if(!node)return; if(node.text && node.text.length>3 && node.type==='TEXT') console.log(' '.repeat(indent)+node.text); for(const c of node.children||[]) printTexts(c, indent+1);}
['desktop_hero','desktop_intro','desktop_services'].forEach(k=>{console.log('\n## '+k); printTexts(pass1[k]);});
