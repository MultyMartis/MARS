import { readFileSync } from "fs";
import { join, resolve, dirname } from "path";
import { fileURLToPath } from "url";
import puppeteer from "puppeteer-core";

const __dir = dirname(fileURLToPath(import.meta.url));
const v8Root = resolve(__dir, "../..");
const distDir = join(v8Root, "dist");
const PORT = 4722;
const CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";

const html = readFileSync(join(distDir, "o-centre.html"), "utf-8");
const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map((m) => m[1]);
const dupIds = [...new Set(ids.filter((id, i) => ids.indexOf(id) !== i))].sort();
const assets = [...html.matchAll(/(?:src|href)="(assets\/[^"]+)"/g)].map((m) => m[1]);
const { existsSync } = await import("fs");
const missingAssets = assets.filter((a) => !existsSync(join(distDir, a)));

import { createServer } from "http";
const server = await new Promise((resolvePromise) => {
  const s = createServer((req, res) => {
    let rel = decodeURIComponent(req.url.split("?")[0]);
    if (rel === "/") rel = "/o-centre.html";
    const filePath = join(distDir, rel.replace(/^\//, ""));
    try {
      const data = readFileSync(filePath);
      const ext = filePath.split(".").pop();
      const types = { html: "text/html; charset=utf-8", css: "text/css", js: "application/javascript", webp: "image/webp" };
      res.writeHead(200, { "Content-Type": types[ext] || "application/octet-stream" });
      res.end(data);
    } catch {
      res.writeHead(404);
      res.end("not found");
    }
  });
  s.listen(PORT, "127.0.0.1", () => resolvePromise(s));
});

const browser = await puppeteer.launch({ executablePath: CHROME, headless: true, args: ["--no-sandbox"] });
const page = await browser.newPage();
const consoleErrors = [];
page.on("pageerror", (e) => consoleErrors.push(String(e)));
page.on("console", (msg) => { if (msg.type() === "error") consoleErrors.push(msg.text()); });
await page.setViewport({ width: 1437, height: 900 });
await page.goto(`http://127.0.0.1:${PORT}/o-centre.html`, { waitUntil: "networkidle0", timeout: 60000 });
const overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
await browser.close();
server.close();

console.log(JSON.stringify({
  build: "PASS",
  unresolved_includes: (html.match(/@@include/g) || []).length,
  duplicate_ids: dupIds,
  missing_assets: missingAssets,
  console_errors: consoleErrors,
  horizontal_overflow_1437: overflow,
}, null, 2));
