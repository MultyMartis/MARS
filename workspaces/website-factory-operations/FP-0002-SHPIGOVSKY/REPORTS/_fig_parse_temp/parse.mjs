import { readFileSync, writeFileSync } from "fs";
import { parseFig } from "openfig-core";

const figPath = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN`;
import { readdirSync } from "fs";
import { join } from "path";
const figFile = readdirSync(figPath).find(f => f.endsWith('.fig'));
const full = join(figPath, figFile);
const data = readFileSync(full);
const doc = parseFig(new Uint8Array(data));
const msg = doc.message;

function getName(n) {
  return n?.name || n?.characters || n?.type || 'UNNAMED';
}

function getType(n) {
  return n?.type || 'UNKNOWN';
}

function getSize(n) {
  const t = n?.size || n?.absoluteBoundingBox || n?.absoluteRenderBounds;
  if (!t) return null;
  const w = t.x ?? t.width;
  const h = t.y ?? t.height;
  if (typeof w === 'number' && typeof h === 'number') {
    // size object uses x/y as width/height in some nodes
    if (n.size) return { w: n.size.x, h: n.size.y };
    return { w: t.width ?? t.x, h: t.height ?? t.y };
  }
  return null;
}

// Build parent map from nodeChanges
const nodes = msg?.nodeChanges || msg?.nodes || [];
console.log('ROOT_KEYS', Object.keys(msg || {}));
console.log('NODE_CHANGES_COUNT', nodes.length);

// Index by guid
const byGuid = new Map();
for (const n of nodes) {
  const g = n.guid || n.nodeId || n.id;
  if (g != null) byGuid.set(String(g), n);
}

// children map via parentIndex
const children = new Map();
for (const n of nodes) {
  const p = n.parentIndex?.guid ?? n.parentIndex?.id ?? n.parentGuid;
  if (p != null) {
    const key = String(p);
    if (!children.has(key)) children.set(key, []);
    children.get(key).push(n);
  }
}

// find pages (CANVAS children or type PAGE)
const pages = nodes.filter(n => n.type === 'CANVAS' || n.type === 'PAGE');
console.log('PAGES_RAW', pages.length, pages.slice(0,5).map(p => ({type:p.type,name:p.name,guid:p.guid})));

// frames
const frames = nodes.filter(n => n.type === 'FRAME');
console.log('FRAMES_TOTAL', frames.length);

// components
const components = nodes.filter(n => n.type === 'COMPONENT' || n.type === 'COMPONENT_SET');
console.log('COMPONENTS', components.length);

// text
const texts = nodes.filter(n => n.type === 'TEXT');
console.log('TEXT_NODES', texts.length);

// auto layout
const autoLayout = nodes.filter(n => n.layoutMode && n.layoutMode !== 'NONE');
console.log('AUTO_LAYOUT', autoLayout.length);

// sample frame sizes
const frameSizes = frames.slice(0,20).map(f => ({
  name: f.name,
  w: f.size?.x,
  h: f.size?.y,
  layoutMode: f.layoutMode,
}));

const out = {
  nodeChangesCount: nodes.length,
  pages: pages.map(p => ({ type: p.type, name: p.name, guid: p.guid })),
  framesTotal: frames.length,
  componentsTotal: components.length,
  textTotal: texts.length,
  autoLayoutTotal: autoLayout.length,
  frameSamples: frameSizes,
};

writeFileSync('parse_out.json', JSON.stringify(out, null, 2));
