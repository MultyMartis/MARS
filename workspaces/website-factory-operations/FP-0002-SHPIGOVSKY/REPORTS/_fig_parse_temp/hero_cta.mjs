import { readFileSync } from "fs";
import { join } from "path";
import { parseFig } from "openfig-core";
import { readdirSync } from "fs";

const figPath =
  "C:\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN";
const figFile = readdirSync(figPath).find((f) => f.endsWith(".fig"));
const nodes = parseFig(new Uint8Array(readFileSync(join(figPath, figFile)))).message
  ?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const children = new Map();
for (const n of nodes) {
  const pk = guidKey(n.parentIndex?.guid);
  if (!pk) continue;
  if (!children.has(pk)) children.set(pk, []);
  children.get(pk).push(n);
}
function getText(n) {
  if (n.type !== "TEXT") return null;
  return n.textData?.characters ?? n.characters;
}
function collectTexts(node, out = []) {
  const t = getText(node);
  if (t) out.push({ name: node.name, text: String(t).trim() });
  for (const k of children.get(guidKey(node.guid)) || []) collectTexts(k, out);
  return out;
}
const hero = nodes.find((n) => n.name === "1 - Главный экран");
const btnSymbol = nodes.find((n) => n.type === "SYMBOL" && n.name === "Кнопка");
const heroButtons = [];
function findButtons(node) {
  if (node.type === "INSTANCE" && node.name === "Кнопка")
    heroButtons.push({
      id: guidKey(node.guid),
      parent: nodes.find((x) => guidKey(x.guid) === guidKey(node.parentIndex?.guid))?.name,
    });
  for (const k of children.get(guidKey(node.guid)) || []) findButtons(k);
}
findButtons(hero);
const group6 = (children.get(guidKey(hero.guid)) || []).find((n) => n.name === "Group 6");
console.log(
  JSON.stringify(
    {
      symbolDefaultTexts: collectTexts(btnSymbol),
      heroButtons,
      group6Structure: (children.get(guidKey(group6?.guid)) || []).map((n) => ({
        type: n.type,
        name: n.name,
        id: guidKey(n.guid),
      })),
      heroContentTexts: collectTexts(group6).filter(
        (t) => !/^(Лечение|Генотип|Специал|О центр|Отзыв|Стать|Контакт|Москва|пн-пт|режим|8 \()/i.test(t.text),
      ),
    },
    null,
    2,
  ),
);
