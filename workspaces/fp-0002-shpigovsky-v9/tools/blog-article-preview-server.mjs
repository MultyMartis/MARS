import { createServer } from "http";
import { readFileSync } from "fs";
import { join } from "path";

const distDir = "X:/AI MARS/workspaces/fp-0002-shpigovsky-v8/dist";
const PORT = Number(process.env.BLOG_PREVIEW_PORT || 4322);

createServer((req, res) => {
  let rel = decodeURIComponent(req.url.split("?")[0]);
  if (rel === "/") rel = "/blog/nazvanie-stati.html";
  const filePath = join(distDir, rel.replace(/^\//, "").replace(/\.\./g, ""));
  try {
    const data = readFileSync(filePath);
    const ext = filePath.split(".").pop();
    const types = {
      html: "text/html; charset=utf-8",
      css: "text/css; charset=utf-8",
      js: "application/javascript",
      webp: "image/webp",
      png: "image/png",
      svg: "image/svg+xml",
      woff2: "font/woff2",
      woff: "font/woff",
    };
    res.writeHead(200, { "Content-Type": types[ext] || "application/octet-stream" });
    res.end(data);
  } catch {
    res.writeHead(404);
    res.end("not found");
  }
}).listen(PORT, "127.0.0.1", () => {
  console.log(`FP-0002 blog article preview: http://127.0.0.1:${PORT}/blog/nazvanie-stati.html`);
});
