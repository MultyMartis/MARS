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
for (const [, arr] of children) {
  arr.sort((a, b) => (a.parentIndex?.position ?? 0) - (b.parentIndex?.position ?? 0));
}

const pages = [
  "Главная страница",
  "Главная страница - моб",
  "О центре",
  "О центре - моб",
  "Услуги хаб",
  "Услуги хаб - моб",
  "Услуга подраздел",
  "Услуга подраздел - моб",
  "Услуга конечная",
  "Услуга конечная - моб",
  "Контакты",
  "Контакты - моб",
  "Отзывы",
  "Отзывы - моб",
  "Блог хаб",
  "Блог хаб - моб",
  "Статья",
  "Статья - моб",
  "Правовая инфа",
  "Правовая инфа - моб",
  "404",
  "404 - моб",
];

const report = {};
for (const pname of pages) {
  const frame = nodes.find((n) => n.type === "FRAME" && n.name === pname);
  if (!frame) {
    report[pname] = { missing: true };
    continue;
  }
  const kids = (children.get(guidKey(frame.guid)) || []).filter(
    (k) => k.type === "FRAME" || k.type === "INSTANCE"
  );
  report[pname] = {
    w: Math.round(frame.size?.x ?? 0),
    h: Math.round(frame.size?.y ?? 0),
    sections: kids.map((k, i) => ({
      idx: i + 1,
      type: k.type,
      name: k.name,
      w: Math.round(k.size?.x ?? 0),
      h: Math.round(k.size?.y ?? 0),
    })),
  };
}

console.log(JSON.stringify(report, null, 2));
