import { readFileSync, copyFileSync, mkdirSync, writeFileSync } from "fs";
import { join } from "path";
import { execSync } from "child_process";
import { createHash } from "crypto";

const figFull =
  "C:\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN\\Шпиговский.fig";
const workspaceRoot = "C:\\AI MARS\\workspaces\\fp-0002-shpigovsky-v6";
const tempDir = join(
  workspaceRoot,
  "reviews",
  "main-content",
  "final-corrections",
  "_fig_extract_temp",
);

const assets = [
  {
    key: "article-yoga",
    nodeId: "1:1280",
    frame: "Статьи / Статья (yoga)",
    hash: "2a1c33e99775c186541c8d81d3d8bec41973239c",
    out: "src/img/content/home-articles/article-yoga-therapy.webp",
  },
  {
    key: "article-bos",
    nodeId: "1:1281",
    frame: "Статьи / Статья (BOS)",
    hash: "4e1d0887e79c3d8aec97e6a90a7cfa54a7dbd725",
    out: "src/img/content/home-articles/article-bos-therapy.webp",
  },
  {
    key: "final-form-background",
    nodeId: "1:1295",
    frame: "Консультация",
    hash: "e4f40bb169a20b7239113b6f0154ecdf4769b142",
    out: "src/img/content/home-final-form/home-final-form-background.webp",
  },
];

function extractFromZip(imageHash, destPath) {
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
  mkdirSync(join(destPath, ".."), { recursive: true });
  const pngTemp = join(tempDir, `${imageHash}.png`);
  copyFileSync(tempExtract, pngTemp);
  execSync(
    `py -3 -c "from PIL import Image; im=Image.open(r'${pngTemp.replace(/'/g, "''")}'); im.save(r'${destPath.replace(/'/g, "''")}', 'WEBP', quality=86)"`,
    { stdio: "inherit" },
  );
  const bytes = readFileSync(destPath);
  const dimOut = execSync(
    `py -3 -c "from PIL import Image; im=Image.open(r'${destPath.replace(/'/g, "''")}'); print(im.size[0], im.size[1])"`,
    { encoding: "utf8" },
  ).trim();
  const [width, height] = dimOut.split(" ").map(Number);
  return {
    sha256: createHash("sha256").update(bytes).digest("hex"),
    width,
    height,
    bytes: bytes.length,
  };
}

mkdirSync(tempDir, { recursive: true });
const records = [];

for (const asset of assets) {
  const outPath = join(workspaceRoot, asset.out);
  const meta = extractFromZip(asset.hash, outPath);
  records.push({ ...asset, exportedTo: asset.out, ...meta });
}

writeFileSync(
  join(workspaceRoot, "reviews", "main-content", "final-corrections", "FP-0002-V6-FINAL-CORRECTIONS-FIG-EXPORT.json"),
  JSON.stringify(records, null, 2),
);
console.log(JSON.stringify({ count: records.length }, null, 2));
