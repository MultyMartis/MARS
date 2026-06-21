import { readFileSync, writeFileSync } from "fs";
import { join } from "path";
import { parseFig } from "openfig-core";

const figPath = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN`;
import { readdirSync } from "fs";
const figFile = readdirSync(figPath).find(f => f.endsWith('.fig'));
const data = readFileSync(join(figPath, figFile));
const doc = parseFig(new Uint8Array(data));
const nodes = doc.message?.nodeChanges || [];

const guidKey = (g) => g ? `${g.sessionID}:${g.localID}` : null;

const byGuid = new Map();
for (const n of nodes) {
  const k = guidKey(n.guid);
  if (k) byGuid.set(k, n);
}

// parent map
const children = new Map();
for (const n of nodes) {
  const pk = guidKey(n.parentIndex?.guid);
  if (!pk) continue;
  if (!children.has(pk)) children.set(pk, []);
  children.get(pk).push(n);
}

function nodeSize(n) {
  if (n.size && typeof n.size.x === 'number') return { w: Math.round(n.size.x), h: Math.round(n.size.y) };
  if (n.absoluteBoundingBox) return { w: Math.round(n.absoluteBoundingBox.width), h: Math.round(n.absoluteBoundingBox.height) };
  return null;
}

function classifyViewport(w, h, name='') {
  const nm = (name||'').toLowerCase();
  if (nm.includes('моб') || nm.includes('mobile')) return 'mobile';
  if (nm.includes('tablet') || nm.includes('планш')) return 'tablet';
  if (nm.includes('desktop') || nm.includes('деск')) return 'desktop';
  if (!w || !h) return 'unknown';
  if (w <= 480) return 'mobile';
  if (w <= 900) return 'tablet';
  if (w >= 1200) return 'desktop';
  return 'unknown';
}

// Pages = CANVAS
const canvases = nodes.filter(n => n.type === 'CANVAS');
const pageReports = [];

for (const canvas of canvases) {
  const ck = guidKey(canvas.guid);
  const topChildren = children.get(ck) || [];
  const frames = topChildren.filter(n => n.type === 'FRAME' || n.type === 'SECTION');
  const allDescFrames = [];

  function walk(node, depth=0) {
    const k = guidKey(node.guid);
    const kids = children.get(k) || [];
    if (node.type === 'FRAME') {
      const sz = nodeSize(node);
      allDescFrames.push({
        name: node.name || '(unnamed)',
        depth,
        ...sz,
        viewport: classifyViewport(sz?.w, sz?.h, node.name),
        layoutMode: node.layoutMode || 'NONE',
        childCount: kids.length,
      });
    }
    for (const c of kids) walk(c, depth+1);
  }
  for (const c of topChildren) walk(c, 0);

  pageReports.push({
    pageName: canvas.name,
    guid: ck,
    topLevelCount: topChildren.length,
    topLevelTypes: [...new Set(topChildren.map(n => n.type))],
    topLevelNames: topChildren.slice(0,50).map(n => ({ type:n.type, name:n.name, size: nodeSize(n) })),
    directFrames: frames.map(f => ({ name:f.name, size: nodeSize(f), viewport: classifyViewport(nodeSize(f)?.w, nodeSize(f)?.h, f.name) })),
    allFramesCount: allDescFrames.length,
    frames: allDescFrames,
  });
}

// Global stats
const typeCounts = {};
for (const n of nodes) typeCounts[n.type] = (typeCounts[n.type]||0)+1;

const namedFrames = nodes.filter(n => n.type==='FRAME' && n.name).map(n => ({name:n.name, size:nodeSize(n)}));
const uniqueFrameNames = [...new Set(namedFrames.map(f=>f.name))];

// top-level frames across file (likely page mockups)
const page1 = canvases.find(c => c.name === 'Page 1');
const page1Frames = pageReports.find(p => p.pageName === 'Page 1');

// Groups
const groups = nodes.filter(n => n.type === 'GROUP' || n.type === 'BOOLEAN_OPERATION');

// Components / instances
const components = nodes.filter(n => ['COMPONENT','COMPONENT_SET'].includes(n.type));
const instances = nodes.filter(n => n.type === 'INSTANCE');

// Auto layout - check multiple fields
const autoLayout = nodes.filter(n => (n.layoutMode && n.layoutMode !== 'NONE') || n.stackMode);

// Text with characters
const texts = nodes.filter(n => n.type === 'TEXT');
const textWithChars = texts.filter(n => n.characters && n.characters.trim());

// Styles / variables hints
const styleFields = nodes.filter(n => n.styleType || n.styles || n.fillStyleId || n.textStyleId);

// SECTION nodes
const sections = nodes.filter(n => n.type === 'SECTION');

// Find likely page-level frames by width ~1440 or ~375
const likelyPageFrames = nodes.filter(n => n.type==='FRAME').map(n => {
  const sz = nodeSize(n);
  return { name:n.name, ...sz, viewport: classifyViewport(sz?.w, sz?.h, n.name) };
}).filter(f => f.w && f.h && f.h > 800);

// cluster by width bands
const widthBands = { mobile: [], tablet: [], desktop: [], unknown: [] };
for (const f of likelyPageFrames) widthBands[f.viewport].push(f);

const report = {
  meta: {
    fileName: figFile,
    nodeChangesCount: nodes.length,
    typeCounts,
    imagesInZip: 166,
  },
  pages: pageReports.map(p => ({
    pageName: p.pageName,
    topLevelCount: p.topLevelCount,
    topLevelTypes: p.topLevelTypes,
    allFramesCount: p.allFramesCount,
    directFramesCount: p.directFrames.length,
    topLevelNames: p.topLevelNames,
    directFrames: p.directFrames,
  })),
  pageFrameTables: pageReports.map(p => ({
    pageName: p.pageName,
    frames: p.frames,
  })),
  structureAudit: {
    separatePages: canvases.length,
    canvasNames: canvases.map(c => c.name),
    groupsCount: groups.length,
    componentsCount: components.length,
    instancesCount: instances.length,
    autoLayoutCount: autoLayout.length,
    textNodes: texts.length,
    textWithContent: textWithChars.length,
    styleLinkedNodes: styleFields.length,
    sectionsCount: sections.length,
    uniqueFrameNameCount: uniqueFrameNames.length,
    sampleFrameNames: uniqueFrameNames.slice(0, 100),
  },
  viewportSummary: {
    likelyPageFramesTotal: likelyPageFrames.length,
    byViewport: {
      mobile: widthBands.mobile.length,
      tablet: widthBands.tablet.length,
      desktop: widthBands.desktop.length,
      unknown: widthBands.unknown.length,
    },
    desktopSamples: widthBands.desktop.slice(0,30).map(f => ({name:f.name,w:f.w,h:f.h})),
    mobileSamples: widthBands.mobile.slice(0,30).map(f => ({name:f.name,w:f.w,h:f.h})),
  }
};

writeFileSync(String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\_fig_forensic_full.json`, JSON.stringify(report, null, 2));
console.log('DONE');
console.log('CANVASES', canvases.map(c=>c.name));
console.log('PAGE1_TOP', page1Frames?.topLevelNames?.slice(0,20));
console.log('TYPE_COUNTS', JSON.stringify(typeCounts));
console.log('VIEWPORT', report.viewportSummary.byViewport);
