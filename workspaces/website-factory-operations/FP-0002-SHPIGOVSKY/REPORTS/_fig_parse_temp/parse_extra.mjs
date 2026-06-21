import { readFileSync, writeFileSync } from "fs";
import { join } from "path";
import { parseFig } from "openfig-core";
import { readdirSync } from "fs";

const figPath = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN`;
const figFile = readdirSync(figPath).find(f => f.endsWith('.fig'));
const doc = parseFig(new Uint8Array(readFileSync(join(figPath, figFile))));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => g ? `${g.sessionID}:${g.localID}` : null;
const byGuid = new Map(nodes.map(n => [guidKey(n.guid), n]));
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

function findByName(name) {
  return nodes.find(n => n.name === name && n.type === 'FRAME');
}

const home = findByName('Главная страница');
const homeKids = children.get(guidKey(home.guid)) || [];
const homeBlocks = homeKids.map(n => ({
  type: n.type,
  name: n.name,
  size: nodeSize(n),
  childCount: (children.get(guidKey(n.guid))||[]).length,
  layoutMode: n.layoutMode || null,
  stackMode: n.stackMode || null,
}));

// auto layout deeper check
const layoutModes = {};
for (const n of nodes) {
  if (n.layoutMode) layoutModes[n.layoutMode] = (layoutModes[n.layoutMode]||0)+1;
  if (n.stackMode) layoutModes['stack:'+n.stackMode] = (layoutModes['stack:'+n.stackMode]||0)+1;
}

// symbols/components
const symbols = nodes.filter(n => n.type === 'SYMBOL');
const instances = nodes.filter(n => n.type === 'INSTANCE');
const symbolNames = [...new Set(symbols.map(s => s.name))];

// variables
const vars = nodes.filter(n => n.type === 'VARIABLE');
const varSets = nodes.filter(n => n.type === 'VARIABLE_SET');

// text sample from home
const homeText = [];
function collectText(node) {
  const kids = children.get(guidKey(node.guid))||[];
  for (const k of kids) {
    if (k.type === 'TEXT' && k.characters) homeText.push(k.characters.slice(0,80));
    collectText(k);
  }
}
collectText(home);

// internal canvas
const internal = nodes.find(n => n.type==='CANVAS' && n.name==='Internal Only Canvas');
const internalKids = children.get(guidKey(internal.guid))||[];

const out = {
  homeTopLevelBlocks: homeBlocks,
  homeTextSampleCount: homeText.length,
  homeTextSamples: homeText.slice(0,20),
  layoutModes,
  symbolCount: symbols.length,
  uniqueSymbolNames: symbolNames.slice(0,40),
  instanceCount: instances.length,
  instanceSample: instances.slice(0,15).map(i => ({name:i.name, symbolId:i.symbolData?.symbolID})),
  variables: vars.map(v => ({name:v.name, resolvedType:v.resolvedType})),
  variableSets: varSets.map(v => v.name),
  internalCanvasChildren: internalKids.map(n => ({type:n.type,name:n.name,size:nodeSize(n)})),
  groupsCount: nodes.filter(n => n.type==='GROUP').length,
  sectionsCount: nodes.filter(n => n.type==='SECTION').length,
};

writeFileSync(String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\_fig_forensic_extra.json`, JSON.stringify(out,null,2));
console.log('home blocks', homeBlocks.length);
console.log('layoutModes', layoutModes);
console.log('symbols', symbols.length, 'instances', instances.length);
console.log('home text', homeText.length);
console.log('internal', internalKids.length);
