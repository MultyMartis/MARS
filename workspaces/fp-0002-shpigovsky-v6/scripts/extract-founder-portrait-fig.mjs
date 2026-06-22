import { readFileSync, copyFileSync, mkdirSync, writeFileSync } from "fs";
import { join } from "path";
import { execSync } from "child_process";
import { createHash } from "crypto";
import { parseFig } from "openfig-core";

const figFull = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN\Шпиговский.fig`;
const portraitNodeId = "1:1212";
const imageHash = "93c2fbf520f20835924b1087ba607519a103a3e7";
const outPath = String.raw`C:\AI MARS\workspaces\fp-0002-shpigovsky-v6\src\img\content\founder-sergey-shpigovsky.png`;
const tempDir = String.raw`C:\AI MARS\workspaces\fp-0002-shpigovsky-v6\reviews\main-content\section-02-portrait-fix\_fig_extract_temp`;

const doc = parseFig(new Uint8Array(readFileSync(figFull)));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const byGuid = new Map(nodes.map((n) => [guidKey(n.guid), n]));

function hashHex(buf) {
  if (!buf) return null;
  return Buffer.from(buf).toString("hex");
}

function nodeInfo(id) {
  const n = byGuid.get(id);
  if (!n) return null;
  const imageFill = (n.fillPaints || []).find((p) => p.type === "IMAGE" || p.imageHash || p.image?.hash);
  return {
    id,
    name: n.name,
    type: n.type,
    size: n.size ? { w: Math.round(n.size.x), h: Math.round(n.size.y) } : null,
    imageHash: hashHex(imageFill?.imageHash || imageFill?.image?.hash),
    fills: (n.fillPaints || []).map((p) => ({
      type: p.type,
      hash: hashHex(p.imageHash || p.image?.hash),
    })),
  };
}

mkdirSync(tempDir, { recursive: true });
const zipEntry = `images/${imageHash}`;
const tempExtract = join(tempDir, imageHash);
const ps = `
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead('${figFull.replace(/'/g, "''")}')
$entry = $zip.Entries | Where-Object { $_.FullName -eq '${zipEntry}' }
if (-not $entry) { throw "Missing zip entry ${zipEntry}" }
$dest = '${tempExtract.replace(/'/g, "''")}'
[System.IO.Compression.ZipFileExtensions]::ExtractToFile($entry, $dest, $true)
$zip.Dispose()
`;
execSync(`powershell -NoProfile -Command "${ps.replace(/"/g, '\\"').replace(/\r?\n/g, "; ")}"`, {
  stdio: "pipe",
});

copyFileSync(tempExtract, outPath);
const bytes = readFileSync(outPath);
const sha256 = createHash("sha256").update(bytes).digest("hex");

const meta = {
  figFile: "Шпиговский.fig",
  figPath: figFull,
  page: "Page 1",
  frame: "Слово спецу (1:1208)",
  nodeName: nodeInfo(portraitNodeId)?.name || "СЮШ",
  nodeId: portraitNodeId,
  assetType: "PNG",
  imageHash,
  fileBytes: bytes.length,
  sha256,
  exportedTo: outPath,
  node: nodeInfo(portraitNodeId),
  parentFrame: nodeInfo("1:1210"),
};

writeFileSync(
  String.raw`C:\AI MARS\workspaces\fp-0002-shpigovsky-v6\reviews\main-content\section-02-portrait-fix\FP-0002-V6-SECTION-02-FIGMA-PORTRAIT-META.json`,
  JSON.stringify(meta, null, 2),
);
console.log(JSON.stringify(meta, null, 2));
