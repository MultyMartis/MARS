import { readFileSync, writeFileSync } from "fs";

const figPath =
  "C:\\MARS Phenix\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN\\Spig_v1.2.fig";

const { parseFig } = await import("openfig-core");

const doc = parseFig(new Uint8Array(readFileSync(figPath)));
const blobs = doc.message?.blobs || [];
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const byGuid = new Map(nodes.map((n) => [guidKey(n.guid), n]));

function dumpBlob(idx) {
  const b = blobs[idx];
  if (!b) return null;
  if (typeof b === "string") return { type: "string", len: b.length, preview: b.slice(0, 200) };
  if (b instanceof Uint8Array) return { type: "uint8", len: b.length, hex: Buffer.from(b.slice(0, 120)).toString("hex") };
  if (Array.isArray(b)) return { type: "array", len: b.length, preview: b.slice(0, 20) };
  return { type: typeof b, keys: Object.keys(b || {}), value: b };
}

const out = {
  blob153: dumpBlob(153),
  blob155: dumpBlob(155),
};

for (const id of ["1:3610", "1:3611"]) {
  const n = byGuid.get(id);
  out[id] = n?.vectorData;
}

writeFileSync(
  "C:\\MARS Phenix\\AI MARS\\workspaces\\fp-0002-shpigovsky-v7\\reviews\\package-002\\_fig-blobs.json",
  JSON.stringify(out, null, 2),
);

console.log("blob153 type", out.blob153?.type, "len", out.blob153?.len);
