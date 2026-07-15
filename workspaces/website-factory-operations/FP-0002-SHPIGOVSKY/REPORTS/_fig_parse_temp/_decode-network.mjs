import { readFileSync } from "fs";
import { parseFig } from "openfig-core";

const figPath =
  "C:\\MARS Phenix\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN\\Spig_v1.2.fig";

const doc = parseFig(new Uint8Array(readFileSync(figPath)));
const blobs = doc.message.blobs;

function blobBytes(idx) {
  const b = blobs[idx];
  if (!b?.bytes) return null;
  if (b.bytes instanceof Uint8Array) return b.bytes;
  return Uint8Array.from(Object.values(b.bytes));
}

function readF32(bytes, off) {
  const view = new DataView(bytes.buffer, bytes.byteOffset + off, 4);
  return view.getFloat32(0, true);
}

function readU32(bytes, off) {
  const view = new DataView(bytes.buffer, bytes.byteOffset + off, 4);
  return view.getUint32(0, true);
}

function decodeNetwork(idx) {
  const bytes = blobBytes(idx);
  if (!bytes) return null;
  const vertexCount = readU32(bytes, 0);
  const segmentCount = readU32(bytes, 4);
  const regionCount = readU32(bytes, 8);
  const vertices = [];
  let off = 12;
  for (let i = 0; i < vertexCount; i++) {
    vertices.push({ x: readF32(bytes, off), y: readF32(bytes, off + 4) });
    off += 8;
  }
  const segments = [];
  for (let i = 0; i < segmentCount; i++) {
    segments.push({
      start: readU32(bytes, off),
      end: readU32(bytes, off + 4),
    });
    off += 8;
  }
  return { vertexCount, segmentCount, regionCount, vertices, segments };
}

for (const idx of [153, 155]) {
  console.log("blob", idx, JSON.stringify(decodeNetwork(idx), null, 2));
}
