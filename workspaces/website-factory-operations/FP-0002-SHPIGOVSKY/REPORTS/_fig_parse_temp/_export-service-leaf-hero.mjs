import { readFileSync, mkdirSync } from "fs";
import { join, dirname } from "path";
import { execSync } from "child_process";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const figPath =
  "C:/MARS Phenix/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig";
const heroOut =
  "C:/MARS Phenix/AI MARS/workspaces/fp-0002-shpigovsky-v7/src/img/content/services/service-leaf-alcohol-hero.webp";
const tempDir = join(__dirname, "_hero-temp");
mkdirSync(tempDir, { recursive: true });
mkdirSync(dirname(heroOut), { recursive: true });

const { parseFig } = await import("openfig-core");
const doc = parseFig(new Uint8Array(readFileSync(figPath)));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const byGuid = new Map(nodes.map((n) => [guidKey(n.guid), n]));
const children = new Map();
for (const n of nodes) {
  const p = guidKey(n.parentIndex?.guid);
  if (!p) continue;
  if (!children.has(p)) children.set(p, []);
  children.get(p).push(n);
}

function hashHex(h) {
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

const heroHash = findImageHash("1:1789");
const zipEntry = `images/${heroHash}`;
const rawPath = join(tempDir, heroHash);
const ps = `
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead('${figPath.replace(/'/g, "''")}')
$entry = $zip.Entries | Where-Object { $_.FullName -eq '${zipEntry}' }
if (-not $entry) { throw "Missing zip entry ${zipEntry}" }
$dest = '${rawPath.replace(/'/g, "''")}'
[System.IO.Compression.ZipFileExtensions]::ExtractToFile($entry, $dest, $true)
$zip.Dispose()
`;
execSync(`powershell -NoProfile -Command "${ps.replace(/"/g, '\\"').replace(/\r?\n/g, "; ")}"`, { stdio: "inherit" });
const pngTemp = join(tempDir, `${heroHash}.png`);
execSync(`copy /Y "${rawPath}" "${pngTemp}"`, { shell: true, stdio: "inherit" });
const dim = execSync(
  `py -3 -c "from PIL import Image; im=Image.open(r'${pngTemp.replace(/'/g, "''")}'); im.save(r'${heroOut.replace(/'/g, "''")}', 'WEBP', quality=86); print(im.size[0], im.size[1])"`,
  { encoding: "utf8" },
).trim();
console.log("heroHash", heroHash);
console.log("heroOut", heroOut);
console.log("dimensions", dim);
