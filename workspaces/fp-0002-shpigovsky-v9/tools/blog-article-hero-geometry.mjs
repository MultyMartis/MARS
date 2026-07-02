import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { createRequire } from "module";
import { pathToFileURL } from "url";

const require = createRequire(
  pathToFileURL(
    "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/_fig_parse_temp/package.json",
  ),
);

const fig =
  "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig";
const outPath =
  "X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8/blog-article-recovery-corrective-pass-01-2/temp/hero-geometry.json";

const { parseFig } = await import(pathToFileURL(require.resolve("openfig-core")).href);
const doc = parseFig(new Uint8Array(readFileSync(fig)));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const byGuid = new Map(nodes.map((n) => [guidKey(n.guid), n]));
const childMap = new Map();
for (const n of nodes) {
  const pk = guidKey(n.parentIndex?.guid);
  if (!pk) continue;
  if (!childMap.has(pk)) childMap.set(pk, []);
  childMap.get(pk).push(n);
}

function sortedKids(id) {
  return [...(childMap.get(id) || [])].sort(
    (a, b) => (a.parentIndex?.position ?? 0) - (b.parentIndex?.position ?? 0),
  );
}

function walk(id) {
  const n = byGuid.get(id);
  if (!n) return null;
  const bb = n.size ? { w: Math.round(n.size.x), h: Math.round(n.size.y) } : null;
  const tr = n.transform ? { x: Math.round(n.transform.m02), y: Math.round(n.transform.m12) } : null;
  const kids = sortedKids(id)
    .map((k) => walk(guidKey(k.guid)))
    .filter(Boolean);
  return { id, name: n.name, type: n.type, bb, tr, children: kids };
}

const root = walk("1:3316");
mkdirSync(outPath.replace(/[^/\\]+$/, ""), { recursive: true });
writeFileSync(outPath, JSON.stringify(root, null, 2));
console.log(JSON.stringify(root, null, 2));
