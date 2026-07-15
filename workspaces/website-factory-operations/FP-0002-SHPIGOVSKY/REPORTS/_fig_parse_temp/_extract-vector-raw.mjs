import { readFileSync, writeFileSync } from "fs";

const figPath =
  "C:\\MARS Phenix\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN\\Spig_v1.2.fig";

const { parseFig } = await import("openfig-core");

const doc = parseFig(new Uint8Array(readFileSync(figPath)));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const byGuid = new Map(nodes.map((n) => [guidKey(n.guid), n]));

const ids = ["1:3610", "1:3611", "1:966"];
const out = {};
for (const id of ids) {
  const n = byGuid.get(id);
  if (!n) continue;
  out[id] = {
    name: n.name,
    type: n.type,
    size: n.size,
    transform: n.transform,
    absoluteBoundingBox: n.absoluteBoundingBox,
    relativeTransform: n.relativeTransform,
    fillPaints: n.fillPaints,
    strokePaints: n.strokePaints,
    strokeWeight: n.strokeWeight,
    vectorData: n.vectorData,
    vectorNetwork: n.vectorNetwork,
    pointCount: n.pointCount,
    innerRadius: n.innerRadius,
    cornerRadius: n.cornerRadius,
  };
}

writeFileSync(
  "C:\\MARS Phenix\\AI MARS\\workspaces\\fp-0002-shpigovsky-v7\\reviews\\package-002\\_fig-vector-raw.json",
  JSON.stringify(out, null, 2),
);

console.log("ok");
