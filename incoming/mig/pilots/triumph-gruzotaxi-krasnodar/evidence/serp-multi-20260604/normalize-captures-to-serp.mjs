/**
 * Normalize Playwright capture-raw.json → serp_result per query (MIG schema v0.1).
 */
import { readFileSync, writeFileSync, mkdirSync, readdirSync, existsSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const SESSION_ID = "mig-20260604-mqgt01";
const CAPTURES_DIR = join(__dirname, "captures");
const OUT_SERP_DIR = join(__dirname, "serp_results");
const QUERY_SET_PATH = join(
  __dirname,
  "..",
  "..",
  "multi-query-market-query-set-v1.json"
);

const AGGREGATOR_HINTS = [
  "avito",
  "uslugi.yandex",
  "profi.ru",
  "2gis",
  "yandex.ru/maps",
  "dostavka.yandex",
  "youdo",
  "zoon.ru",
];

function domainFromUrl(url) {
  if (!url || typeof url !== "string") return null;
  if (url.startsWith("tel:")) return null;
  try {
    const u = url.startsWith("http") ? url : `https://${url}`;
    const host = new URL(u).hostname.toLowerCase().replace(/^www\./, "");
    if (host.includes("yabs.yandex")) return null;
    return host || null;
  } catch {
    return null;
  }
}

function domainFromPathText(pathText, title) {
  const blob = `${pathText || ""} ${title || ""}`;
  const m = blob.match(
    /([a-z0-9][-a-z0-9]*\.(?:ru|com|рф|net|org|by|kz))(?:\s|\/|$|›|·)/i
  );
  return m ? m[1].toLowerCase() : null;
}

function resolveUrl(item) {
  let host = domainFromUrl(item.url);
  if (host) {
    return { url: item.url.startsWith("http") ? item.url : `https://${item.url}`, host };
  }
  host = domainFromPathText(item.path_text, item.title);
  if (host) {
    return { url: `https://${host}/`, host };
  }
  return { url: null, host: null };
}

function classifySurface(host, surfaceType) {
  if (surfaceType === "ad") return "ad";
  if (surfaceType === "local_pack") return "local_pack";
  if (!host) return "organic";
  const h = host.toLowerCase();
  if (AGGREGATOR_HINTS.some((a) => h.includes(a.replace("www.", "")))) return "aggregator";
  if (h.includes("avito")) return "aggregator";
  return "organic";
}

function buildSerpFromRaw(raw, queryMeta) {
  const items = Array.isArray(raw.items) ? raw.items : [];
  const ads = items.filter((i) => i.surface_type === "ad");
  const organicRows = [];
  const aggregators = new Set();
  const marketplaces = new Set();
  const safeUnknown = [];

  if (raw.has_captcha) {
    safeUnknown.push("Yandex captcha suspected — organic list may be incomplete");
  }
  safeUnknown.push(
    "Promo/yabs hrefs resolved via visible Path line where possible; unresolved yabs-only rows omitted from organic_results"
  );
  safeUnknown.push("Automated normalization — human screenshot review recommended");

  let position = 0;
  for (const item of items) {
    if (item.surface_type === "local_pack") continue;
    const resolved = resolveUrl(item);
    if (!resolved.host && item.surface_type !== "ad") continue;

    position += 1;
    const surface = classifySurface(resolved.host, item.surface_type);
    if (surface === "aggregator" && resolved.host) {
      if (resolved.host.includes("avito")) marketplaces.add("Авито");
      aggregators.add(resolved.host);
    }

    organicRows.push({
      position,
      title: item.title,
      url: resolved.url || item.url,
      surface_type: item.surface_type === "ad" ? "ad" : surface,
      snippet: item.path_text || null,
    });
    if (position >= 15) break;
  }

  const mapsLocal =
    items.some((i) => i.surface_type === "local_pack") ? "present" : "absent";

  return {
    schema_version: "0.1",
    session_id: SESSION_ID,
    query_id: queryMeta.query_id,
    captured_at: raw.captured_at,
    source_mode: "manual",
    search_engine: "yandex",
    region: "Краснодар",
    city: "Краснодар",
    device: "mobile",
    localization: "ru, city-level (Yandex lr=35)",
    query: raw.query_text || queryMeta.query_text,
    serp_type: ads.length >= 2 ? "local commercial" : "mixed",
    ads_blocks: {
      top_count: Math.min(ads.length, 5),
      bottom_count: null,
      visible_patterns: ads.slice(0, 6).map((a) => a.title.slice(0, 60)),
    },
    maps_local_pack: mapsLocal,
    aggregators: [...aggregators].map((d) => {
      if (d.includes("avito")) return "Авито";
      if (d.includes("uslugi.yandex")) return "Яндекс Услуги";
      if (d.includes("profi")) return "Profi.ru";
      if (d.includes("2gis")) return "2GIS";
      return d;
    }),
    marketplaces: [...marketplaces],
    review_signals: [],
    offer_patterns: [],
    cta_patterns: [],
    landing_observations: [],
    organic_results: organicRows,
    safe_unknown: safeUnknown,
    capture_evidence_ref: `evidence/serp-multi-20260604/captures/${queryMeta.query_id}/`,
  };
}

function main() {
  const querySet = JSON.parse(readFileSync(QUERY_SET_PATH, "utf8"));
  mkdirSync(OUT_SERP_DIR, { recursive: true });

  const serpById = {};
  for (const q of querySet.approved_query_set) {
    const rawPath = join(CAPTURES_DIR, q.query_id, "capture-raw.json");
    if (!existsSync(rawPath)) {
      console.warn(`Skip ${q.query_id}: no capture-raw.json`);
      continue;
    }
    const raw = JSON.parse(readFileSync(rawPath, "utf8"));
    if (raw.has_captcha || !raw.extracted_count) {
      console.warn(`Skip ${q.query_id}: captcha or empty extraction`);
      continue;
    }
    const serp = buildSerpFromRaw(raw, q);
    const outPath = join(OUT_SERP_DIR, `${q.query_id}.json`);
    writeFileSync(outPath, JSON.stringify(serp, null, 2), "utf8");
    serpById[q.query_id] = serp;
    console.log(`Wrote ${outPath} organic=${serp.organic_results.length}`);
  }

  writeFileSync(
    join(__dirname, "serp-results-bundle.json"),
    JSON.stringify(serpById, null, 2),
    "utf8"
  );
}

main();
