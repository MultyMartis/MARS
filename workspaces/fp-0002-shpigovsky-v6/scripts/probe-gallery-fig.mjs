import { readFileSync, writeFileSync } from "fs";
import { parseFig } from "openfig-core";

const figFull =
  "C:\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN\\Шпиговский.fig";

const doc = parseFig(new Uint8Array(readFileSync(figFull)));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const byGuid = new Map(nodes.map((n) => [guidKey(n.guid), n]));

function hashHex(buf) {
  return buf ? Buffer.from(buf).toString("hex") : null;
}

function getImageHash(n) {
  const imageFill = (n.fillPaints || []).find(
    (p) => p.type === "IMAGE" || p.imageHash || p.image?.hash,
  );
  return hashHex(imageFill?.imageHash || imageFill?.image?.hash);
}

function ancestors(id) {
  const chain = [];
  let current = byGuid.get(id);
  while (current) {
    chain.push({ id: guidKey(current.guid), name: current.name, type: current.type });
    const pi = current.parentIndex;
    if (pi == null || typeof pi !== "number" || pi < 0) break;
    current = nodes[pi];
  }
  return chain;
}

// Inspect parent frames
for (const pid of ["1:1038", "1:983", "1:984", "1:985", "1:986", "1:987", "1:988"]) {
  const n = byGuid.get(pid);
  console.log(pid, n ? { name: n.name, type: n.type, size: n.size, childCount: (n.children || []).length } : "MISSING");
}

// All image rects 376x376 under section 03 ancestor chain
const gallery = [];
for (const n of nodes) {
  const id = guidKey(n.guid);
  const ih = getImageHash(n);
  if (!ih || ih === "d3ac7d00af36722468bb8f23790ac8586fb9ae3d") continue;
  if (!n.size) continue;
  const w = Math.round(n.size.x);
  const h = Math.round(n.size.y);
  if (w < 300 || w > 420 || h < 300 || h > 420) continue;
  const chain = ancestors(id);
  if (!chain.some((c) => c.id === "1:958")) continue;
  gallery.push({
    id,
    name: n.name,
    size: { w, h },
    imageHash: ih,
    chain: chain.map((c) => c.id).slice(0, 8),
  });
}

gallery.sort((a, b) => a.id.localeCompare(b.id));
console.log("gallery in 1:958", JSON.stringify(gallery, null, 2));

// dedupe by hash keep first
const unique = [];
const seen = new Set();
for (const g of gallery) {
  if (seen.has(g.imageHash)) continue;
  seen.add(g.imageHash);
  unique.push(g);
}
console.log("unique hashes", unique.length, JSON.stringify(unique, null, 2));

writeFileSync(
  "reviews/main-content/gallery-audit/FP-0002-V6-GALLERY-FIGMA-NODES-PROBE.json",
  JSON.stringify({ gallery, unique }, null, 2),
);
