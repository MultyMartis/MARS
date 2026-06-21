import { readFileSync, writeFileSync } from "fs";
import { join } from "path";
import { parseFig } from "openfig-core";
import { readdirSync } from "fs";

const figPath = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN`;
const figFile = readdirSync(figPath).find(f => f.endsWith('.fig'));
const doc = parseFig(new Uint8Array(readFileSync(join(figPath, figFile))));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => g ? `${g.sessionID}:${g.localID}` : null;
const children = new Map();
for (const n of nodes) {
  const pk = guidKey(n.parentIndex?.guid);
  if (!pk) continue;
  if (!children.has(pk)) children.set(pk, []);
  children.get(pk).push(n);
}

function nodeSize(n) {
  if (n.size?.x) return { w: Math.round(n.size.x), h: Math.round(n.size.y) };
  return null;
}

// inspect TEXT node fields
const texts = nodes.filter(n => n.type === 'TEXT');
const sample = texts[0];
const textKeys = sample ? Object.keys(sample) : [];
const withChars = texts.filter(t => t.characters);
const withDerived = texts.filter(t => t.derivedTextData || t.textData);

// home page: find texts under frame
const home = nodes.find(n => n.name==='Главная страница' && n.type==='FRAME');
const homeGuid = guidKey(home.guid);
const homeTexts = [];
function walk(g) {
  const kids = children.get(g)||[];
  for (const k of kids) {
    if (k.type==='TEXT') homeTexts.push({name:k.name, chars:(k.characters||'').slice(0,100), keys:Object.keys(k).filter(x=>x.includes('text')||x.includes('char')||x.includes('Text')||x.includes('Char'))});
    walk(guidKey(k.guid));
  }
}
walk(homeGuid);

// build page table for report
const page1 = nodes.find(n => n.type==='CANVAS' && n.name==='Page 1');
const topFrames = (children.get(guidKey(page1.guid))||[]).filter(n=>n.type==='FRAME');

function classify(w,h,name) {
  const nm=(name||'').toLowerCase();
  if (nm.includes('моб')||nm.includes('mobile')) return 'mobile';
  if (w<=480) return 'mobile';
  if (w<=900) return 'tablet';
  if (w>=1200) return 'desktop';
  return 'unknown';
}

const pageTable = topFrames.map((f,i) => {
  const s = nodeSize(f);
  return { idx: i+1, name: f.name, w: s?.w, h: s?.h, viewport: classify(s?.w,s?.h,f.name) };
});

// count nested frames per top page frame
const nestedCounts = topFrames.map(f => {
  let count=0;
  function w(g){ count++; for (const c of (children.get(g)||[])) if (c.type==='FRAME') w(guidKey(c.guid)); }
  w(guidKey(f.guid));
  return { name:f.name, nestedFrames: count };
});

const out = { textKeys, textTotal: texts.length, withChars: withChars.length, withDerived: withDerived.length, textFieldSample: texts.slice(0,3).map(t=>({name:t.name, characters:t.characters, textData:!!t.textData, derived:!!t.derivedTextData})), homeTextsCount: homeTexts.length, homeTextSamples: homeTexts.slice(0,10), pageTable, nestedCounts };
writeFileSync(String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\_fig_forensic_text_pages.json`, JSON.stringify(out,null,2));
console.log('texts', texts.length, 'withChars', withChars.length, 'homeTexts', homeTexts.length);
console.log(JSON.stringify(pageTable,null,2));
