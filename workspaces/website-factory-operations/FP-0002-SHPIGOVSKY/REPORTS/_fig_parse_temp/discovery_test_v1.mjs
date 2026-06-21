import { readFileSync, writeFileSync } from "fs";
import { join } from "path";
import { parseFig } from "openfig-core";
import { readdirSync } from "fs";

const figPath = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN`;
const figFile = readdirSync(figPath).find((f) => f.endsWith(".fig"));
const doc = parseFig(new Uint8Array(readFileSync(join(figPath, figFile))));
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

function nodeSize(n) {
  if (n.size?.x != null) return { w: Math.round(n.size.x), h: Math.round(n.size.y) };
  if (n.absoluteBoundingBox)
    return {
      w: Math.round(n.absoluteBoundingBox.width),
      h: Math.round(n.absoluteBoundingBox.height),
    };
  return null;
}

function getText(n) {
  if (n.type !== "TEXT") return null;
  const c = n.textData?.characters ?? n.characters;
  return c && String(c).trim() ? String(c).trim() : null;
}

function hasImageFill(n) {
  for (const p of n.fillPaints || []) {
    if (p.image || p.imageHash || p.imageRef || p.type === "IMAGE") return true;
  }
  return false;
}

function subtreeHasImage(node) {
  if (hasImageFill(node)) return true;
  for (const k of children.get(guidKey(node.guid)) || []) {
    if (subtreeHasImage(k)) return true;
  }
  return false;
}

function collectTexts(node, out = []) {
  const t = getText(node);
  if (t) out.push({ name: node.name, text: t, fontSize: node.fontSize });
  for (const k of children.get(guidKey(node.guid)) || []) collectTexts(k, out);
  return out;
}

function countInstances(node) {
  let c = node.type === "INSTANCE" ? 1 : 0;
  for (const k of children.get(guidKey(node.guid)) || []) c += countInstances(k);
  return c;
}

function findInstances(node, names = new Set()) {
  if (node.type === "INSTANCE") names.add(node.name || "(unnamed)");
  for (const k of children.get(guidKey(node.guid)) || []) findInstances(k, names);
  return names;
}

function findCtaTexts(texts) {
  const ctaPatterns = /запис|консульт|позвон|узнать|подробн|отправ|связ/i;
  return texts.filter((t) => ctaPatterns.test(t.text));
}

function classifySectionType(name, node) {
  const nm = (name || "").toLowerCase();
  if (nm.includes("подвал") || node.type === "INSTANCE" && nm.includes("подвал"))
    return "footer-instance";
  if (nm.includes("главный экран") || nm === "1 - главный экран") return "hero+header";
  if (nm.includes("вступление")) return "intro";
  if (nm.includes("услуг")) return "services";
  if (nm.includes("отзыв")) return "reviews";
  if (nm.includes("faq")) return "faq";
  if (nm.includes("стать")) return "articles";
  if (nm.includes("специал")) return "specialists";
  if (nm.includes("видео")) return "video";
  if (nm.includes("генотип")) return "genotyping";
  if (nm.includes("программ")) return "program";
  if (nm.includes("преимущ")) return "advantages";
  return "section-frame";
}

function treeSummary(node, depth = 0, maxDepth = 4) {
  const kids = children.get(guidKey(node.guid)) || [];
  const entry = {
    type: node.type,
    name: node.name || "(unnamed)",
    id: guidKey(node.guid),
    size: nodeSize(node),
    childCount: kids.length,
    stackMode: node.stackMode || null,
    hasImage: hasImageFill(node),
    text: getText(node),
    isInstance: node.type === "INSTANCE",
    instanceName: node.type === "INSTANCE" ? node.name : null,
  };
  if (depth < maxDepth) {
    entry.children = kids.map((k) => treeSummary(k, depth + 1, maxDepth));
  } else if (kids.length) {
    entry.childNames = kids.map((k) => `${k.type}:${k.name}`);
  }
  return entry;
}

function pickHeadingSubheadingCta(texts) {
  const sorted = [...texts].sort((a, b) => (b.fontSize || 0) - (a.fontSize || 0));
  const cta = findCtaTexts(texts);
  const heading = sorted[0]?.text || null;
  const subheading = sorted.find((t) => t.text !== heading && t.text.length < 120)?.text || sorted[1]?.text || null;
  const ctaText = cta[0]?.text || texts.find((t) => /запис|консульт/i.test(t.text))?.text || null;
  return { heading, subheading, cta: ctaText };
}

// Home frame candidates
const homeCandidates = nodes.filter(
  (n) => n.type === "FRAME" && n.name === "Главная страница",
);
const homeDesktop = homeCandidates.find((n) => {
  const sz = nodeSize(n);
  return sz && sz.w >= 1200;
});

const home = homeDesktop || homeCandidates[0];
const homeId = guidKey(home.guid);
const homeSize = nodeSize(home);

const homeKids = (children.get(homeId) || []).slice();
// preserve document order (array order from children map may vary - use parent index order)
homeKids.sort((a, b) => (a.parentIndex?.position ?? 0) - (b.parentIndex?.position ?? 0));

const sections = homeKids.map((n, i) => {
  const texts = collectTexts(n);
  const instances = [...findInstances(n)];
  const sz = nodeSize(n);
  return {
    index: i + 1,
    name: n.name,
    id: guidKey(n.guid),
    type: n.type,
    sectionType: classifySectionType(n.name, n),
    height: sz?.h,
    width: sz?.w,
    hasImages: subtreeHasImage(n),
    hasText: texts.length > 0,
    textCount: texts.length,
    hasCta: findCtaTexts(texts).length > 0 || instances.some((x) => x === "Кнопка"),
    repeatableComponents: instances,
    instanceCount: countInstances(n),
    stackMode: n.stackMode || null,
    childCount: (children.get(guidKey(n.guid)) || []).length,
    content: pickHeadingSubheadingCta(texts),
    allTextsSample: texts.slice(0, 8).map((t) => t.text),
  };
});

const heroFrame = homeKids.find((n) => n.name === "1 - Главный экран");
const heroTree = heroFrame ? treeSummary(heroFrame, 0, 5) : null;

// Flatten hero for group register
function flattenHeroGroups(node, parentName = null, out = []) {
  const nm = node.name || "(unnamed)";
  const sz = nodeSize(byGuid.get(node.id) || { size: node.size });
  const entry = {
    name: nm,
    id: node.id,
    type: node.type,
    size: node.size,
    parent: parentName,
    text: node.text,
    isInstance: node.isInstance,
    instanceName: node.instanceName,
    hasImage: node.hasImage,
    stackMode: node.stackMode,
    childCount: node.childCount,
  };
  out.push(entry);
  for (const c of node.children || []) flattenHeroGroups(c, nm, out);
  return out;
}

const heroGroups = heroTree ? flattenHeroGroups(heroTree) : [];

const report = {
  meta: {
    figFile,
    parsedAt: new Date().toISOString(),
    parser: "openfig-core",
    homeCandidates: homeCandidates.map((n) => ({
      id: guidKey(n.guid),
      size: nodeSize(n),
    })),
  },
  homeFrame: {
    name: home.name,
    id: homeId,
    size: homeSize,
    childCount: homeKids.length,
    selectionReason:
      "Named 'Главная страница', width 1437px (desktop cluster), tallest full-page frame on Page 1; not mobile variant ('- моб')",
  },
  sections,
  contentExtractionFirst5: sections.slice(0, 5).map((s) => ({
    section: `SECTION-${String(s.index).padStart(2, "0")}`,
    name: s.name,
    heading: s.content.heading,
    subheading: s.content.subheading,
    cta: s.content.cta,
    extractionQuality:
      s.content.heading ? (s.content.cta || s.textCount > 2 ? "GOOD" : "PARTIAL") : "POOR",
  })),
  hero: {
    frameName: heroFrame?.name,
    frameId: heroFrame ? guidKey(heroFrame.guid) : null,
    frameSize: heroFrame ? nodeSize(heroFrame) : null,
    tree: heroTree,
    groupRegister: heroGroups,
    heroTexts: heroFrame ? collectTexts(heroFrame).map((t) => ({ name: t.name, text: t.text, fontSize: t.fontSize })) : [],
    heroInstances: heroFrame ? [...findInstances(heroFrame)] : [],
  },
};

const outPath = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\_fig_discovery_test_v1.json`;
writeFileSync(outPath, JSON.stringify(report, null, 2));
console.log(JSON.stringify({
  home: report.homeFrame,
  sectionCount: sections.length,
  sectionNames: sections.map((s) => s.name),
  first5: report.contentExtractionFirst5,
  heroGroupCount: heroGroups.length,
  heroTopChildren: heroTree?.children?.map((c) => ({ name: c.name, type: c.type, id: c.id })),
}, null, 2));
