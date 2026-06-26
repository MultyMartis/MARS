import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
import { execSync } from "child_process";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ws = join(__dirname, "../..");
const figPath =
  "C:/MARS Phenix/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig";
const desktopPng =
  "C:/MARS Phenix/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/26.06.2026/Услуга - десктоп.png";
const mobilePng =
  "C:/MARS Phenix/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/26.06.2026/Услуга - мобильная.png";

const { parseFig } = await import("openfig-core");
const doc = parseFig(new Uint8Array(readFileSync(figPath)));
const nodes = doc.message?.nodeChanges || [];
const blobs = doc.message?.blobs || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const byGuid = new Map(nodes.map((n) => [guidKey(n.guid), n]));
const children = new Map();
for (const n of nodes) {
  const p = guidKey(n.parentIndex?.guid);
  if (!p) continue;
  if (!children.has(p)) children.set(p, []);
  children.get(p).push(n);
}
for (const [, arr] of children)
  arr.sort((a, b) => (a.parentIndex?.position ?? 0) - (b.parentIndex?.position ?? 0));

function getText(n) {
  if (!n) return "";
  if (n.characters) return n.characters;
  for (const o of n.symbolData?.symbolOverrides || []) {
    if (o.characters) return o.characters;
    if (o.textData?.characters) return o.textData.characters;
  }
  return "";
}

function collectText(id, acc = [], depth = 0) {
  const n = byGuid.get(id);
  if (!n) return acc;
  const t = getText(n);
  if (t?.trim())
    acc.push({ id, depth, name: n.name, type: n.type, text: t.trim() });
  for (const k of children.get(id) || []) collectText(guidKey(k.guid), acc, depth + 1);
  return acc;
}

function hashHex(h) {
  if (!h) return null;
  if (typeof h === "string") return h;
  const bytes = Object.keys(h)
    .sort((a, b) => Number(a) - Number(b))
    .map((k) => h[k]);
  return Buffer.from(bytes).toString("hex");
}

function findImageHash(nodeId) {
  const n = byGuid.get(nodeId);
  if (!n) return null;
  for (const f of n.fillPaints || []) {
    if (f.image?.hash) return hashHex(f.image.hash);
  }
  for (const k of children.get(nodeId) || []) {
    const h = findImageHash(guidKey(k.guid));
    if (h) return h;
  }
  return null;
}

const sectionIds = ["1:1749", "1:1816", "1:1847", "1:1867"];
const texts = {};
for (const id of sectionIds) texts[id] = collectText(id);

const heroHash = findImageHash("1:1753");
const outDir = join(__dirname, "_extract");
mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "group1-section-texts.json"), JSON.stringify({ texts, heroHash, heroNode: "1:1753" }, null, 2));

// Export hero webp
const heroOut = join(ws, "src/img/content/services/service-leaf-alcohol-hero.webp");
mkdirSync(dirname(heroOut), { recursive: true });
const tempDir = join(outDir, "hero-temp");
mkdirSync(tempDir, { recursive: true });
const zipEntry = `images/${heroHash}`;
const ps = `
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead('${figPath.replace(/'/g, "''")}')
$entry = $zip.Entries | Where-Object { $_.FullName -eq '${zipEntry}' }
if (-not $entry) { throw "Missing zip entry ${zipEntry}" }
$dest = '${join(tempDir, heroHash).replace(/'/g, "''")}'
[System.IO.Compression.ZipFileExtensions]::ExtractToFile($entry, $dest, $true)
$zip.Dispose()
`;
execSync(`powershell -NoProfile -Command "${ps.replace(/"/g, '\\"').replace(/\r?\n/g, "; ")}"`, { stdio: "inherit" });
const pngTemp = join(tempDir, `${heroHash}.png`);
execSync(`copy /Y "${join(tempDir, heroHash)}" "${pngTemp}"`, { shell: true, stdio: "inherit" });
execSync(
  `py -3 -c "from PIL import Image; im=Image.open(r'${pngTemp.replace(/'/g, "''")}'); im.save(r'${heroOut.replace(/'/g, "''")}', 'WEBP', quality=86); print(im.size)"`,
  { stdio: "inherit" },
);

console.log("section texts written");
for (const id of sectionIds) {
  console.log(`\n=== ${id} ===`);
  for (const t of texts[id]) console.log(`  [${t.depth}] ${t.name}: ${t.text.slice(0, 120)}`);
}
console.log("\nhero hash", heroHash);
console.log("hero out", heroOut);
