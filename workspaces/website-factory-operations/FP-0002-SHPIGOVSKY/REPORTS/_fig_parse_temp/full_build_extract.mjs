import { readFileSync, readdirSync, copyFileSync, mkdirSync, writeFileSync, existsSync } from "fs";
import { join } from "path";
import { execSync } from "child_process";
import { parseFig } from "openfig-core";

const figPath = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN`;
const figFile = readdirSync(figPath).find((f) => f.endsWith(".fig"));
const figFull = join(figPath, figFile);
const doc = parseFig(new Uint8Array(readFileSync(figFull)));
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

const SECTIONS = [
  { id: "SECTION-01", frameId: "1:876", slug: "hero" },
  { id: "SECTION-02", frameId: "1:927", slug: "intro" },
  { id: "SECTION-03", frameId: "1:958", slug: "services" },
  { id: "SECTION-04", frameId: "1:991", slug: "why-us" },
  { id: "SECTION-05", frameId: "1:1050", slug: "reviews" },
  { id: "SECTION-06", frameId: "1:1079", slug: "how-to-start" },
  { id: "SECTION-07", frameId: "1:1115", slug: "program" },
  { id: "SECTION-08", frameId: "1:1136", slug: "genotyping" },
  { id: "SECTION-09", frameId: "1:1164", slug: "advantages" },
  { id: "SECTION-10", frameId: "1:1208", slug: "specialist-word" },
  { id: "SECTION-11", frameId: "1:1224", slug: "video" },
  { id: "SECTION-12", frameId: "1:1231", slug: "specialists" },
  { id: "SECTION-13", frameId: "1:1268", slug: "articles" },
  { id: "SECTION-14", frameId: "1:1282", slug: "faq" },
  { id: "SECTION-15", frameId: "1:1309", slug: "footer" },
];

function hashHex(buf) {
  if (!buf) return null;
  if (typeof buf === "string") return buf;
  return Buffer.from(buf).toString("hex");
}

function sortedKids(parentId) {
  return (children.get(parentId) || []).sort(
    (a, b) => (a.parentIndex?.position ?? 0) - (b.parentIndex?.position ?? 0),
  );
}

function collectSubtree(rootId, out = []) {
  const root = byGuid.get(rootId);
  if (!root) return out;
  const walk = (node) => {
    out.push(node);
    for (const k of sortedKids(guidKey(node.guid))) walk(k);
  };
  walk(root);
  return out;
}

function getText(n) {
  if (n.type !== "TEXT") return null;
  const t = n.textData?.characters ?? n.characters;
  return t && String(t).trim() ? String(t).trim() : null;
}

function getImages(node) {
  const imgs = [];
  for (const p of node.fillPaints || []) {
    if (p.type === "IMAGE" || p.imageHash) {
      imgs.push({
        nodeId: guidKey(node.guid),
        nodeName: node.name,
        hash: hashHex(p.imageHash || p.image?.hash),
      });
    }
  }
  return imgs;
}

function extractFromZip(hash, destPath) {
  if (!hash || existsSync(destPath)) return existsSync(destPath);
  mkdirSync(join(destPath, ".."), { recursive: true });
  const zipEntry = `images/${hash}`;
  const tempDir = join(figPath, "..", "..", "REPORTS", "_fig_parse_temp", "_img_temp");
  mkdirSync(tempDir, { recursive: true });
  const tempFile = join(tempDir, hash);
  const ps = `
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $zip = [System.IO.Compression.ZipFile]::OpenRead('${figFull.replace(/'/g, "''")}')
    $entry = $zip.Entries | Where-Object { $_.FullName -eq '${zipEntry}' }
    if (-not $entry) { throw "Missing zip entry ${zipEntry}" }
    $dest = '${tempFile.replace(/'/g, "''")}'
    [System.IO.Compression.ZipFileExtensions]::ExtractToFile($entry, $dest, $true)
    $zip.Dispose()
  `;
  try {
    execSync(`powershell -NoProfile -Command "${ps.replace(/"/g, '\\"').replace(/\r?\n/g, "; ")}"`, {
      stdio: "pipe",
    });
    copyFileSync(tempFile, destPath);
    return true;
  } catch {
    return false;
  }
}

const imgOutBase = String.raw`C:\AI MARS\workspaces\fp-0002-shpigovsky-frontend\src\img\home`;
mkdirSync(imgOutBase, { recursive: true });

const result = { sections: [], exportedImages: [] };

for (const sec of SECTIONS) {
  const subtree = collectSubtree(sec.frameId);
  const texts = [];
  const images = [];
  for (const n of subtree) {
    const t = getText(n);
    if (t) {
      texts.push({
        id: guidKey(n.guid),
        name: n.name,
        text: t,
        fontSize: n.fontSize,
        fontWeight: n.fontWeight,
        fontName: n.fontName,
      });
    }
    images.push(...getImages(n));
  }
  texts.sort((a, b) => (b.fontSize || 0) - (a.fontSize || 0));

  const uniqueImages = [];
  const seen = new Set();
  for (const img of images) {
    if (!img.hash || seen.has(img.hash)) continue;
    seen.add(img.hash);
    const ext = "jpg";
    const fileName = `${sec.slug}-${img.nodeName.replace(/[^a-zA-Z0-9а-яА-Я_-]+/g, "-").slice(0, 40)}-${img.hash.slice(0, 8)}.${ext}`;
    const dest = join(imgOutBase, fileName);
    const ok = extractFromZip(img.hash, dest);
    uniqueImages.push({ ...img, fileName, exported: ok });
    if (ok) result.exportedImages.push({ section: sec.id, fileName, hash: img.hash });
  }

  result.sections.push({
    ...sec,
    frameName: byGuid.get(sec.frameId)?.name,
    textCount: texts.length,
    texts,
    images: uniqueImages,
  });
}

const outJson = join(figPath, "..", "..", "REPORTS", "_fig_full_build_extract.json");
writeFileSync(outJson, JSON.stringify(result, null, 2), "utf8");
console.log(JSON.stringify({ outJson, sectionCount: result.sections.length, imageCount: result.exportedImages.length }, null, 2));
