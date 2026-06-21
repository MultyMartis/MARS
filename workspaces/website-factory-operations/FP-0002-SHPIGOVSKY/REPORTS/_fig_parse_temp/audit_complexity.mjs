import { readFileSync, readdirSync } from "fs";
import { join } from "path";
import { parseFig } from "openfig-core";

const figPath =
  "C:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN";
const figFile = readdirSync(figPath).find((f) => f.endsWith(".fig"));
const doc = parseFig(new Uint8Array(readFileSync(join(figPath, figFile))));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const children = new Map();
for (const n of nodes) {
  const pk = guidKey(n.parentIndex?.guid);
  if (!pk) continue;
  if (!children.has(pk)) children.set(pk, []);
  children.get(pk).push(n);
}

function countInSubtree(node, pred) {
  let c = pred(node) ? 1 : 0;
  for (const k of children.get(guidKey(node.guid)) || []) c += countInSubtree(k, pred);
  return c;
}

const pages = [
  ["PG-001", "Главная страница"],
  ["PG-002", "Услуги хаб"],
  ["PG-003", "Услуга подраздел"],
  ["PG-004", "Услуга конечная"],
  ["PG-005", "О центре"],
  ["PG-006", "Контакты"],
  ["PG-007", "Отзывы"],
  ["PG-008", "Блог хаб"],
  ["PG-009", "Статья"],
  ["PG-010", "Правовая инфа"],
  ["PG-011", "404"],
];

const out = [];
for (const [id, name] of pages) {
  const frame = nodes.find((n) => n.type === "FRAME" && n.name === name);
  if (!frame) {
    out.push({ id, name, missing: true });
    continue;
  }
  const sections = (children.get(guidKey(frame.guid)) || []).filter(
    (k) => k.type === "FRAME" || k.type === "INSTANCE"
  );
  const instances = new Set();
  function walk(n) {
    if (n.type === "INSTANCE") instances.add(n.name || "(unnamed)");
    for (const k of children.get(guidKey(n.guid)) || []) walk(k);
  }
  walk(frame);
  out.push({
    id,
    name,
    sections: sections.length,
    uniqueBlocks: sections.length,
    forms: countInSubtree(frame, (n) => n.name === "Поле ввода" || (n.type === "INSTANCE" && /поле/i.test(n.name || ""))),
    faq: countInSubtree(frame, (n) => /вопрос|faq|Расскрытие/i.test(n.name || "")),
    buttons: countInSubtree(frame, (n) => n.type === "INSTANCE" && n.name === "Кнопка"),
    carouselHints: countInSubtree(frame, (n) => /pagination|стрел|swiper|slider|отзыв/i.test(n.name || "")),
    modalHints: 0,
    instanceNames: [...instances].sort(),
  });
}
console.log(JSON.stringify(out, null, 2));
