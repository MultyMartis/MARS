import { readFileSync, readdirSync } from "fs";
import { join } from "path";
import { parseFig } from "openfig-core";

const figPath = "C:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN";
const figFile = readdirSync(figPath).find((f) => f.endsWith(".fig"));
const doc = parseFig(new Uint8Array(readFileSync(join(figPath, figFile))));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const byGuid = new Map(nodes.map((n) => [guidKey(n.guid), n]));

function hashHex(h) {
  if (!h) return null;
  if (typeof h === "string") return h;
  const bytes = Object.values(h);
  return bytes.map((b) => Number(b).toString(16).padStart(2, "0")).join("");
}

function parentChain(id) {
  const chain = [];
  let cur = byGuid.get(id);
  while (cur?.parentIndex !== undefined) {
    const parent = nodes[cur.parentIndex];
    if (!parent) break;
    chain.push(`${parent.name} (${guidKey(parent.guid)})`);
    cur = parent;
  }
  return chain;
}

function imageNodes(filter) {
  const out = [];
  for (const n of nodes) {
    const id = guidKey(n.guid);
    for (const p of n.fillPaints || []) {
      if (p.type === "IMAGE" || p.imageHash) {
        const item = {
          id,
          name: n.name,
          type: n.type,
          w: n.size ? Math.round(n.size.x) : null,
          h: n.size ? Math.round(n.size.y) : null,
          hash: hashHex(p.imageHash || p.image?.hash),
          parents: parentChain(id).slice(0, 5),
        };
        if (!filter || filter(item, n)) out.push(item);
      }
    }
  }
  return out;
}

const headerIds = new Set();
function collect(id) {
  headerIds.add(id);
  const n = byGuid.get(id);
  if (!n?.children) return;
  for (const c of n.children) collect(guidKey(c));
}
collect("1:877");

const headerImages = imageNodes((item) => headerIds.has(item.id));
const nameHits = imageNodes((item) =>
  /logo|логотип|brand|бренд|шпигов|skinerica|дом/i.test(item.name || "")
);
const sizeHits = imageNodes(
  (item) => item.w >= 120 && item.w <= 400 && item.h >= 24 && item.h <= 100
);

const hashGroups = new Map();
for (const item of sizeHits) {
  const list = hashGroups.get(item.hash) || [];
  list.push(item);
  hashGroups.set(item.hash, list);
}

const uniqueHashes = [...hashGroups.entries()].map(([hash, items]) => ({
  hash,
  count: items.length,
  sample: items.slice(0, 3),
}));

const targets = [
  "96ca32e4d2ef068e987d8bae141b0bcf51a095a4",
  "262f79db29ec4dc2b9ae2e793d5c8cc6382c307b",
  "de219c6e462c8bf42469bb33751a81252eedc07f",
];

const hashHits = [];
for (const n of nodes) {
  const id = guidKey(n.guid);
  for (const p of n.fillPaints || []) {
    const hash = hashHex(p.imageHash || p.image?.hash);
    if (targets.includes(hash)) {
      hashHits.push({
        id,
        name: n.name,
        type: n.type,
        w: n.size ? Math.round(n.size.x) : null,
        h: n.size ? Math.round(n.size.y) : null,
        hash,
        parent: parentChain(id).slice(0, 4),
      });
    }
  }
}

console.log(
  JSON.stringify(
    {
      headerImages,
      hashHits,
      uniqueLogoSizedHashes: uniqueHashes,
    },
    null,
    2
  )
);
