import { readFileSync } from "fs";
import { join } from "path";
import { parseFig } from "openfig-core";
import { readdirSync } from "fs";

const figPath = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN`;
const figFile = readdirSync(figPath).find((f) => f.endsWith(".fig"));
const doc = parseFig(new Uint8Array(readFileSync(join(figPath, figFile))));
const nodes = doc.message?.nodeChanges || [];
const texts = nodes.filter((n) => n.type === "TEXT");
const withTextData = texts.filter(
  (t) => t.textData?.characters && String(t.textData.characters).trim(),
);
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const children = new Map();
for (const n of nodes) {
  const pk = guidKey(n.parentIndex?.guid);
  if (!pk) continue;
  if (!children.has(pk)) children.set(pk, []);
  children.get(pk).push(n);
}
const home = nodes.find((n) => n.name === "Главная страница" && n.type === "FRAME");
const homeTexts = [];
function walk(g) {
  for (const k of children.get(g) || []) {
    if (k.type === "TEXT" && k.textData?.characters)
      homeTexts.push(String(k.textData.characters));
    walk(guidKey(k.guid));
  }
}
walk(guidKey(home.guid));

let imageRefs = 0;
for (const n of nodes) {
  for (const p of n.fillPaints || [])
    if (p.image || p.imageHash || p.imageRef) imageRefs++;
}

console.log("text with content", withTextData.length, "/", texts.length);
console.log("home text strings", homeTexts.length);
console.log("unique home texts", [...new Set(homeTexts)].length);
console.log("image fill refs", imageRefs);
