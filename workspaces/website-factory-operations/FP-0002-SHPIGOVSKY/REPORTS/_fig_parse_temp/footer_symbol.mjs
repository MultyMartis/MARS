import { readFileSync, readdirSync } from "fs";
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
  return null;
}

function nodePosition(n) {
  if (n.transform?.m02 != null)
    return { x: Math.round(n.transform.m02), y: Math.round(n.transform.m12) };
  return { x: null, y: null };
}

// Find Подвал symbol
const footerSymbols = nodes.filter(
  (n) => n.type === "SYMBOL" && (n.name === "Подвал" || n.name?.includes("Подвал")),
);
const footerInstance = nodes.find(
  (n) => n.type === "INSTANCE" && n.name === "Подвал" && guidKey(n.parentIndex?.guid) === "1:875",
);

function walk(node, depth = 0, out = []) {
  const kids = (children.get(guidKey(node.guid)) || []).sort(
    (a, b) => (a.parentIndex?.position ?? 0) - (b.parentIndex?.position ?? 0),
  );
  const sz = nodeSize(node);
  const pos = nodePosition(node);
  out.push({
    depth,
    name: node.name,
    id: guidKey(node.guid),
    type: node.type,
    x: pos.x,
    y: pos.y,
    w: sz?.w,
    h: sz?.h,
    childCount: kids.length,
    text:
      node.type === "TEXT"
        ? (node.textData?.characters ?? node.characters ?? "").slice(0, 60)
        : null,
  });
  if (depth < 4) for (const k of kids) walk(k, depth + 1, out);
  return out;
}

const symbol = footerSymbols.find((s) => s.name === "Подвал") || footerSymbols[0];
console.log(
  JSON.stringify(
    {
      footerInstance: footerInstance
        ? {
            id: guidKey(footerInstance.guid),
            size: nodeSize(footerInstance),
            pos: nodePosition(footerInstance),
          }
        : null,
      symbol: symbol
        ? { name: symbol.name, id: guidKey(symbol.guid), tree: walk(symbol) }
        : null,
      allFooterSymbols: footerSymbols.map((s) => ({
        name: s.name,
        id: guidKey(s.guid),
        childCount: (children.get(guidKey(s.guid)) || []).length,
      })),
    },
    null,
    2,
  ),
);
