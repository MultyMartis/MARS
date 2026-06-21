import { readFileSync, writeFileSync, readdirSync } from "fs";
import { join } from "path";
import { parseFig } from "openfig-core";

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

function nodePosition(n) {
  if (n.transform?.m02 != null && n.transform?.m12 != null) {
    return { x: Math.round(n.transform.m02), y: Math.round(n.transform.m12) };
  }
  if (n.absoluteBoundingBox) {
    return {
      x: Math.round(n.absoluteBoundingBox.x),
      y: Math.round(n.absoluteBoundingBox.y),
    };
  }
  return { x: null, y: null };
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

function isAutoLayout(n) {
  return !!(n.stackMode || (n.layoutMode && n.layoutMode !== "NONE"));
}

function sortedChildren(parentId) {
  const kids = children.get(parentId) || [];
  return [...kids].sort(
    (a, b) => (a.parentIndex?.position ?? 0) - (b.parentIndex?.position ?? 0),
  );
}

// Forbidden aggregate patterns (Group Decomposition Law)
const FORBIDDEN_AGGREGATES =
  /content block|info block|utility block|contact block|hero area|contact area|info area|utility area|nav area|top bar content/i;

function isVisualGroupCandidate(node) {
  const t = node.type;
  if (["FRAME", "GROUP", "INSTANCE", "COMPONENT"].includes(t)) return true;
  if (t === "TEXT" && getText(node)) return true;
  if (["RECTANGLE", "ROUNDED_RECTANGLE", "VECTOR", "ELLIPSE"].includes(t)) {
    const sz = nodeSize(node);
    if (sz && (sz.w > 40 || sz.h > 40)) return true;
  }
  return false;
}

function describeGroup(node) {
  const text = getText(node);
  const sz = nodeSize(node);
  const pos = nodePosition(node);
  const instances = node.type === "INSTANCE" ? [node.name] : [];
  return {
    figName: node.name || "(unnamed)",
    frameId: guidKey(node.guid),
    type: node.type,
    x: pos.x,
    y: pos.y,
    width: sz?.w ?? null,
    height: sz?.h ?? null,
    childrenCount: sortedChildren(guidKey(node.guid)).length,
    autoLayout: isAutoLayout(node),
    isInstance: node.type === "INSTANCE",
    mainComponentName: node.type === "INSTANCE" ? node.name : null,
    hasImage: hasImageFill(node),
    textPreview: text ? text.slice(0, 80) : null,
    stackMode: node.stackMode || null,
  };
}

function buildGroupRegister(sectionNode, maxDepth = 3) {
  const groups = [];
  let groupIndex = 0;

  function walk(node, depth, parentName) {
    if (depth > maxDepth) return;
    const kids = sortedChildren(guidKey(node.guid));
    const nm = (node.name || "").toLowerCase();

    if (depth === 0) {
      for (const child of kids) {
        if (!isVisualGroupCandidate(child)) continue;
        groupIndex += 1;
        const g = describeGroup(child);
        groups.push({
          groupId: `GROUP-${String(groupIndex).padStart(2, "0")}`,
          ...g,
          depth: 1,
          parentSectionChild: true,
        });
        decomposeChild(child, 2);
      }
      return;
    }
  }

  function decomposeChild(node, depth) {
    if (depth > maxDepth) return;
    const kids = sortedChildren(guidKey(node.guid));
    const meaningfulKids = kids.filter(isVisualGroupCandidate);
    if (meaningfulKids.length <= 1) return;

    for (const child of meaningfulKids) {
      const childKids = sortedChildren(guidKey(child.guid));
      const nm = (child.name || "").toLowerCase();
      if (FORBIDDEN_AGGREGATES.test(child.name || "")) {
        for (const gc of childKids.filter(isVisualGroupCandidate)) {
          groupIndex += 1;
          groups.push({
            groupId: `GROUP-${String(groupIndex).padStart(2, "0")}`,
            ...describeGroup(gc),
            depth,
            note: `Decomposed from forbidden aggregate parent: ${child.name}`,
          });
        }
        continue;
      }
      if (
        child.type === "GROUP" ||
        (child.type === "FRAME" && childKids.length > 0) ||
        child.type === "INSTANCE"
      ) {
        groupIndex += 1;
        groups.push({
          groupId: `GROUP-${String(groupIndex).padStart(2, "0")}`,
          ...describeGroup(child),
          depth,
          parentGroup: node.name,
        });
        decomposeChild(child, depth + 1);
      }
    }
  }

  walk(sectionNode, 0, sectionNode.name);
  return groups;
}

// Home frame
const homeCandidates = nodes.filter(
  (n) => n.type === "FRAME" && n.name === "Главная страница",
);
const home = homeCandidates.find((n) => (nodeSize(n)?.w ?? 0) >= 1200);
const homeId = guidKey(home.guid);
const homePos = nodePosition(home);
const homeSize = nodeSize(home);

const sectionNodes = sortedChildren(homeId);
const sectionRegister = sectionNodes.map((n, i) => {
  const pos = nodePosition(n);
  const sz = nodeSize(n);
  const kids = sortedChildren(guidKey(n.guid));
  const instances = [];
  function collectInstances(node) {
    if (node.type === "INSTANCE") instances.push(node.name);
    for (const k of sortedChildren(guidKey(node.guid))) collectInstances(k);
  }
  collectInstances(n);
  const uniqueInstances = [...new Set(instances)];
  const autoLayoutFrames = [];
  function collectAL(node) {
    if (isAutoLayout(node)) autoLayoutFrames.push(node.name);
    for (const k of sortedChildren(guidKey(node.guid))) collectAL(k);
  }
  collectAL(n);

  return {
    sectionId: `SECTION-${String(i + 1).padStart(2, "0")}`,
    name: n.name,
    frameId: guidKey(n.guid),
    type: n.type,
    x: pos.x,
    y: pos.y,
    width: sz?.w ?? null,
    height: sz?.h ?? null,
    childrenCount: kids.length,
    autoLayout: isAutoLayout(n),
    stackMode: n.stackMode || null,
    componentInstances: uniqueInstances,
    instanceCount: instances.length,
    autoLayoutNodeCount: autoLayoutFrames.length,
    groupRegister: buildGroupRegister(n),
  };
});

// Validation
const unknowns = [];
const conflicts = [];
const aggregationRisks = [];

if (sectionRegister.length !== 15) {
  conflicts.push(
    `Section count ${sectionRegister.length} — expected 15 from prior FIG discovery`,
  );
}

const jpgBlockCount = 17;
if (sectionRegister.length < jpgBlockCount) {
  conflicts.push(
    `FIG has ${sectionRegister.length} top-level sections vs JPG inferred ${jpgBlockCount} blocks — header not split from hero at section level`,
  );
}

for (const s of sectionRegister) {
  if (s.x == null || s.y == null) {
    unknowns.push(`${s.sectionId}: position x/y not available from offline parse`);
  }
  const genericNames = s.groupRegister.filter((g) =>
    /^(group \d+|frame \d+|rectangle \d+)/i.test(g.figName),
  );
  if (genericNames.length > 3) {
    aggregationRisks.push(
      `${s.sectionId} (${s.name}): ${genericNames.length} groups with generic FIG names — semantic naming requires heuristics`,
    );
  }
  if (s.name === "1 - Главный экран" && s.childrenCount <= 3) {
    aggregationRisks.push(
      `${s.sectionId}: header+hero bundled in one section — Factory Hero boundary differs from FIG section model`,
    );
  }
  if (s.type === "INSTANCE" && s.name === "Подвал") {
    unknowns.push(
      `${s.sectionId}: footer INSTANCE — nested text not fully expanded in offline instance traversal`,
    );
  }
}

const autoLayoutTotal = nodes.filter(isAutoLayout).length;
const instanceTotal = nodes.filter((n) => n.type === "INSTANCE").length;

const report = {
  meta: {
    figFile,
    parser: "openfig-core",
    parsedAt: new Date().toISOString(),
    jpgReference:
      "INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg",
    homeFrame: {
      name: home.name,
      frameId: homeId,
      x: homePos.x,
      y: homePos.y,
      width: homeSize?.w,
      height: homeSize?.h,
      childrenCount: sectionNodes.length,
    },
  },
  sectionRegister,
  validation: {
    sectionCount: sectionRegister.length,
    sectionOrder: sectionRegister.map((s) => s.name),
    unknowns,
    conflicts,
    aggregationRisks,
    componentInstancesTotal: instanceTotal,
    autoLayoutNodesTotal: autoLayoutTotal,
  },
  factoryReadiness: {
    canSectionRegisterAutoGenerate: "YES",
    canGroupRegistersAutoGenerate: "PARTIAL",
    canLayoutSpecFromFig: "PARTIAL",
    canAssemblySpecFromFig: "PARTIAL",
    canHtmlSkeletonFromFig: "PARTIAL",
  },
};

const outJson = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\_fig_full_page_discovery_v1.json`;
writeFileSync(outJson, JSON.stringify(report, null, 2));

console.log(
  JSON.stringify(
    {
      sections: sectionRegister.length,
      names: sectionRegister.map((s) => s.name),
      groupCounts: sectionRegister.map((s) => ({
        id: s.sectionId,
        groups: s.groupRegister.length,
      })),
      validation: report.validation,
      readiness: report.factoryReadiness,
    },
    null,
    2,
  ),
);
