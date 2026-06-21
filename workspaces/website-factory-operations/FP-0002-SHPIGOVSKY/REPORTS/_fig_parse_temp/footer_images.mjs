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
function hashHex(h) {
  if (!h) return null;
  if (typeof h === "string") return h;
  return Buffer.from(Object.values(h)).toString("hex");
}
function walk(id, out = []) {
  const n = byGuid.get(id);
  if (!n) return out;
  const imageFill = (n.fillPaints || []).find((p) => p.type === "IMAGE" || p.imageHash);
  out.push({
    id,
    name: n.name,
    type: n.type,
    size: n.size ? { w: Math.round(n.size.x), h: Math.round(n.size.y) } : null,
    hash: imageFill ? hashHex(imageFill.imageHash || imageFill.image?.hash) : null,
  });
  for (const k of children.get(id) || []) walk(guidKey(k.guid), out);
  return out;
}
const all = walk("1:584");
console.log(
  JSON.stringify(
    {
      logo: all.find((x) => x.id === "1:586"),
      paymentImages: all.filter((x) => x.hash && ["1:629", "1:630", "1:631", "1:632", "1:633", "1:634", "1:635", "1:636", "1:637", "1:638", "1:639", "1:640", "1:641", "1:642", "1:643", "1:644", "1:645", "1:646", "1:647", "1:648", "1:649", "1:650", "1:651", "1:652", "1:653", "1:654", "1:655", "1:656", "1:657", "1:658", "1:659", "1:660", "1:661", "1:662", "1:663", "1:664", "1:665", "1:666", "1:667", "1:668", "1:669"].some((p) => x.id.startsWith(p.slice(0, 4)))),
      allImages: all.filter((x) => x.hash),
    },
    null,
    2,
  ),
);
