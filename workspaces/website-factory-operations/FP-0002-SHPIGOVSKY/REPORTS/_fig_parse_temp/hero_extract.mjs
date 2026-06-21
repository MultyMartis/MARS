import { readFileSync, readdirSync, copyFileSync, mkdirSync } from "fs";
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

function hashHex(buf) {
  if (!buf) return null;
  if (typeof buf === "string") return buf;
  return Buffer.from(buf).toString("hex");
}

function paintToCss(p) {
  if (!p) return null;
  if (p.type === "IMAGE") return { type: "IMAGE", hash: hashHex(p.imageHash || p.image?.hash) };
  const c = p.color || p.solidColor;
  if (!c) return null;
  const r = Math.round((c.r ?? 0) * 255);
  const g = Math.round((c.g ?? 0) * 255);
  const b = Math.round((c.b ?? 0) * 255);
  const a = p.opacity ?? c.a ?? 1;
  return { type: p.type, rgba: `rgba(${r},${g},${b},${a})` };
}

function info(id) {
  const n = byGuid.get(id);
  if (!n) return null;
  return {
    id,
    name: n.name,
    type: n.type,
    size: n.size ? { w: Math.round(n.size.x), h: Math.round(n.size.y) } : null,
    cornerRadius: n.cornerRadius,
    fontSize: n.fontSize,
    fontName: n.fontName,
    lineHeight: n.lineHeight,
    fontWeight: n.fontWeight,
    textAlign: n.textAlignHorizontal,
    text: n.textData?.characters || n.characters || null,
    fills: (n.fillPaints || []).map(paintToCss),
  };
}

const ids = [
  "1:912",
  "1:913",
  "1:916",
  "1:917",
  "1:918",
  "1:919",
  "1:920",
  "1:921",
  "1:922",
  "1:923",
];

const heroImage = byGuid.get("1:916");
const heroFill = heroImage?.fillPaints?.find((p) => p.type === "IMAGE" || p.imageHash);
const imageHash = hashHex(heroFill?.imageHash || heroFill?.image?.hash);

const outDir = join(String.raw`C:\AI MARS\workspaces\fp-0002-shpigovsky-frontend\src\img\hero`);
const tempDir = join(String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\_fig_parse_temp\_hero_img_temp`);
let copied = false;

if (imageHash) {
  mkdirSync(outDir, { recursive: true });
  mkdirSync(tempDir, { recursive: true });
  const zipEntry = `images/${imageHash}`;
  const ps = `
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $zip = [System.IO.Compression.ZipFile]::OpenRead('${figFull.replace(/'/g, "''")}')
    $entry = $zip.Entries | Where-Object { $_.FullName -eq '${zipEntry}' }
    if (-not $entry) { throw "Missing zip entry ${zipEntry}" }
    $dest = '${join(tempDir, imageHash).replace(/'/g, "''")}'
    [System.IO.Compression.ZipFileExtensions]::ExtractToFile($entry, $dest, $true)
    $zip.Dispose()
  `;
  execSync(`powershell -NoProfile -Command "${ps.replace(/"/g, '\\"').replace(/\r?\n/g, '; ')}"`, {
    stdio: "pipe",
  });
  copyFileSync(join(tempDir, imageHash), join(outDir, "hero-background.jpg"));
  copied = true;
}

console.log(
  JSON.stringify(
    {
      nodes: ids.map(info),
      heroImageHash: imageHash,
      heroImageCopied: copied,
    },
    null,
    2,
  ),
);
