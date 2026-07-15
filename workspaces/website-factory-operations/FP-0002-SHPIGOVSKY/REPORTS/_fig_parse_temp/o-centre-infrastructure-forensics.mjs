/**
 * FP-0002 V8 O-Centre infrastructure forensics — desktop 1:2440 + mobile 1:5697
 */
import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { createHash } from "crypto";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dir = dirname(fileURLToPath(import.meta.url));
const figPath =
  "C:\\MARS Phenix\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN\\Spig_v1.2.fig";
const outDir =
  "C:\\MARS Phenix\\AI MARS\\workspaces\\fp-0002-shpigovsky-v8\\audits\\o-centre-targeted-asset-export\\data";
const outJson = join(outDir, "FP-0002-V8-OCENTRE-INFRASTRUCTURE-FIGMA-FORENSICS.json");

const { parseFig } = await import("openfig-core");
const figBytes = readFileSync(figPath);
const doc = parseFig(new Uint8Array(figBytes));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const byGuid = new Map(nodes.map((n) => [guidKey(n.guid), n]));
const children = new Map();
for (const n of nodes) {
  const p = guidKey(n.parentIndex?.guid);
  if (!p) continue;
  if (!children.has(p)) children.set(p, []);
  children.get(p).push(n);
}
for (const [, arr] of children)
  arr.sort((a, b) => (a.parentIndex?.position ?? 0) - (b.parentIndex?.position ?? 0));

function isVisibleChain(id) {
  let cur = byGuid.get(id);
  while (cur) {
    if (cur.visible === false) return false;
    cur = byGuid.get(guidKey(cur.parentIndex?.guid));
  }
  return true;
}

function hashHex(h) {
  if (!h) return null;
  if (typeof h === "string") return h;
  if (Buffer.isBuffer(h)) return h.toString("hex");
  if (h instanceof Uint8Array) return Buffer.from(h).toString("hex");
  if (typeof h === "object") {
    const keys = Object.keys(h).sort((a, b) => Number(a) - Number(b));
    return keys.map((k) => Number(h[k]).toString(16).padStart(2, "0")).join("");
  }
  return null;
}

function getImageFills(n) {
  const out = [];
  for (const f of n.fillPaints || []) {
    if (f.type === "IMAGE" || f.image) {
      out.push({
        type: f.type,
        imageRef: f.imageRef || hashHex(f.image?.hash) || null,
        hash: hashHex(f.image?.hash),
        scaleMode: f.image?.scaleMode ?? f.scaleMode ?? null,
        rotation: f.image?.rotation ?? f.rotation ?? 0,
        opacity: f.opacity ?? 1,
      });
    }
  }
  return out;
}

function walkForensics(rootId, platform, acc = []) {
  const n = byGuid.get(rootId);
  if (!n) return acc;
  const parentId = guidKey(n.parentIndex?.guid);
  const parent = parentId ? byGuid.get(parentId) : null;
  const fills = getImageFills(n);
  const visible = isVisibleChain(rootId);
  for (const fill of fills) {
    acc.push({
      node: rootId,
      layer: n.name,
      parent: parentId,
      parentLayer: parent?.name ?? null,
      nodeType: n.type,
      visible,
      fillType: fill.type,
      imageRef: fill.imageRef,
      imageHash: fill.hash,
      scaleMode: fill.scaleMode,
      opacity: fill.opacity,
      rotation: fill.rotation,
      frameBounds: {
        w: Math.round(n.size?.x || 0),
        h: Math.round(n.size?.y || 0),
      },
      platform,
    });
  }
  for (const k of children.get(rootId) || [])
    walkForensics(guidKey(k.guid), platform, acc);
  return acc;
}

const DESKTOP_ROOT = "1:2440";
const MOBILE_ROOT = "1:5697";
const SECTION_BG_HASH = "d3ac7d00af36722468bb8f23790ac8586fb9ae3d";

const desktopRows = walkForensics(DESKTOP_ROOT, "desktop");
const mobileRows = walkForensics(MOBILE_ROOT, "mobile");
const allRows = [...desktopRows, ...mobileRows];

function classify(row) {
  const { imageHash, frameBounds, layer, node, visible } = row;
  if (!visible) return "HIDDEN_NOT_EXPORT";
  if (imageHash === SECTION_BG_HASH) {
    if (node === DESKTOP_ROOT) return "DECORATIVE_RASTER";
    if (frameBounds.w <= 50 && frameBounds.h <= 50) return "DECORATIVE_RASTER";
    return "DECORATIVE_RASTER";
  }
  if (frameBounds.w <= 50 || frameBounds.h <= 50) return "DECORATIVE_RASTER";
  if (layer === "этап" || layer.startsWith("image ") || /screenshot|Снимок/i.test(layer))
    return "PHOTO_REQUIRED";
  return "PHOTO_REQUIRED";
}

for (const row of allRows) {
  row.classification = classify(row);
  row.desktop = row.platform === "desktop" ? 1 : 0;
  row.mobile = row.platform === "mobile" ? 1 : 0;
}

// duplicate ref tracking
const refUses = new Map();
for (const row of allRows) {
  if (!row.imageHash) continue;
  if (!refUses.has(row.imageHash)) refUses.set(row.imageHash, []);
  refUses.get(row.imageHash).push(row.node);
}
for (const row of allRows) {
  const uses = refUses.get(row.imageHash) || [];
  if (
    row.classification === "PHOTO_REQUIRED" &&
    uses.length > 1 &&
    !uses.every((id) => id === row.node)
  ) {
    const crossPlatform = new Set(
      allRows.filter((r) => r.imageHash === row.imageHash).map((r) => r.platform),
    );
    if (crossPlatform.size === 1 && uses.length > 1)
      row.classification = "PHOTO_DUPLICATE_REF";
  }
}

const requiredPhotos = allRows.filter((r) =>
  ["PHOTO_REQUIRED", "PHOTO_DUPLICATE_REF"].includes(r.classification),
);
const uniqueRequiredHashes = new Set(
  requiredPhotos.map((r) => r.imageHash).filter(Boolean),
);

const summary = {
  figPath,
  figSha256: createHash("sha256").update(figBytes).digest("hex"),
  parsedAt: new Date().toISOString(),
  desktopFrame: DESKTOP_ROOT,
  mobileFrame: MOBILE_ROOT,
  metrics: {
    desktop: {
      imageLikeNodes: desktopRows.length,
      visibleBitmapNodes: desktopRows.filter((r) => r.visible).length,
      uniqueBitmapRefs: new Set(desktopRows.map((r) => r.imageHash).filter(Boolean)).size,
      requiredPhotoRefs: new Set(
        desktopRows
          .filter((r) => ["PHOTO_REQUIRED", "PHOTO_DUPLICATE_REF"].includes(r.classification))
          .map((r) => r.imageHash),
      ).size,
      hiddenRefs: desktopRows.filter((r) => r.classification === "HIDDEN_NOT_EXPORT").length,
      decorativeRefs: desktopRows.filter((r) => r.classification === "DECORATIVE_RASTER").length,
      unresolvedRefs: desktopRows.filter((r) => r.classification === "UNRESOLVED").length,
    },
    mobile: {
      imageLikeNodes: mobileRows.length,
      visibleBitmapNodes: mobileRows.filter((r) => r.visible).length,
      uniqueBitmapRefs: new Set(mobileRows.map((r) => r.imageHash).filter(Boolean)).size,
      requiredPhotoRefs: new Set(
        mobileRows
          .filter((r) => ["PHOTO_REQUIRED", "PHOTO_DUPLICATE_REF"].includes(r.classification))
          .map((r) => r.imageHash),
      ).size,
      hiddenRefs: mobileRows.filter((r) => r.classification === "HIDDEN_NOT_EXPORT").length,
      decorativeRefs: mobileRows.filter((r) => r.classification === "DECORATIVE_RASTER").length,
      unresolvedRefs: mobileRows.filter((r) => r.classification === "UNRESOLVED").length,
    },
    combined: {
      imageLikeNodes: allRows.length,
      visibleBitmapNodes: allRows.filter((r) => r.visible).length,
      uniqueBitmapRefs: refUses.size,
      requiredPhotoRefs: uniqueRequiredHashes.size,
      hiddenRefs: allRows.filter((r) => r.classification === "HIDDEN_NOT_EXPORT").length,
      decorativeRefs: allRows.filter((r) => r.classification === "DECORATIVE_RASTER").length,
      unresolvedRefs: allRows.filter((r) => r.classification === "UNRESOLVED").length,
    },
  },
  rows: allRows,
  refUses: Object.fromEntries(
    [...refUses.entries()].map(([h, nodes]) => [h, { nodes, count: nodes.length }]),
  ),
};

mkdirSync(outDir, { recursive: true });
writeFileSync(outJson, JSON.stringify(summary, null, 2), "utf8");
console.log(JSON.stringify(summary.metrics, null, 2));
console.log("unique required:", uniqueRequiredHashes.size);
console.log("wrote", outJson);
