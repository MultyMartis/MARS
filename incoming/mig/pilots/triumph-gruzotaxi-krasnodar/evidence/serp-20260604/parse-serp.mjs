import { readFileSync, writeFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const dir = dirname(fileURLToPath(import.meta.url));
const html = readFileSync(join(dir, "serp-page.html"), "utf8");

const AGG_DOMAINS = [
  "avito.ru",
  "uslugi.yandex.ru",
  "profi.ru",
  "2gis.ru",
  "youdo.com",
  "yandex.ru/maps",
];

function classify(url, inAdv) {
  if (inAdv || url.includes("yabs.yandex.ru")) return "ad";
  if (url.includes("yandex.ru/maps")) return "local_pack";
  for (const d of AGG_DOMAINS) {
    if (url.includes(d)) return "aggregator";
  }
  return "organic";
}

function domainFromUrl(url) {
  try {
    const u = new URL(url);
    return u.hostname.replace(/^www\./, "");
  } catch {
    return url;
  }
}

const items = [];
const seen = new Set();

const liRe =
  /<li[^>]*class="[^"]*(?:serp-item|VanillaReact|AdvItem)[^"]*"[^>]*>([\s\S]*?)<\/li>/gi;
let m;
while ((m = liRe.exec(html)) !== null) {
  const block = m[1];
  const isAdv = /AdvItem|serp-adv|Промо|data-bem[^>]*adv/i.test(block);
  const titleMatch =
    block.match(/OrganicTitle-LinkText[^>]*>([^<]+)/) ||
    block.match(/OrganicTitle[^>]*>([^<]+)/) ||
    block.match(/<h2[^>]*>([^<]+)/);
  const hrefMatch = block.match(/href="(https?:\/\/[^"]+)"/);
  const pathMatch = block.match(/Path-Item[^>]*>([^<]+)/);
  if (!titleMatch && !pathMatch) continue;
  const title = (titleMatch?.[1] || pathMatch?.[1] || "").trim();
  let url = hrefMatch?.[1] || "";
  if (!title || title.length < 4) continue;
  const surface = classify(url, isAdv);
  const key = `${surface}|${domainFromUrl(url)}|${title.slice(0, 60)}`;
  if (seen.has(key)) continue;
  seen.add(key);
  items.push({ title, url, surface_type: surface });
}

const organicOnly = items.filter(
  (i) =>
    !i.url.includes("yabs.yandex.ru") &&
    !i.url.startsWith("tel:") &&
    i.title.length > 10 &&
    ["organic", "aggregator", "local_pack"].includes(i.surface_type)
);

writeFileSync(
  join(dir, "parsed-items.json"),
  JSON.stringify({ all: items.length, organicOnly, items: items.slice(0, 40) }, null, 2)
);
console.log("parsed", items.length, "organic-like", organicOnly.length);
