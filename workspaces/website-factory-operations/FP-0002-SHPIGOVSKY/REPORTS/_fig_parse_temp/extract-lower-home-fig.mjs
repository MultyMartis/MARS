import { readFileSync, copyFileSync, mkdirSync, writeFileSync } from "fs";
import { join } from "path";
import { execSync } from "child_process";
import { createHash } from "crypto";
import { parseFig } from "openfig-core";

const figFull =
  "C:\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN\\Шпиговский.fig";
const workspaceRoot = "C:\\AI MARS\\workspaces\\fp-0002-shpigovsky-v6";
const tempDir = join(workspaceRoot, "reviews", "main-content", "lower-home-audit", "_fig_extract_temp");

const assets = [
  {
    key: "corridor",
    nodeId: "1:1080",
    hash: "ec9d4d7fc4836c95be5826b45a872d22786407f9",
    out: "src/img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp",
  },
  {
    key: "video-preview",
    nodeId: "1:1230",
    hash: "cd50b3a4eaacdbabd71fe6be78b63f99d364810c",
    out: "src/img/content/home-videos/shpigovsky-center-video-preview.webp",
  },
  {
    key: "specialist-01",
    nodeId: "1:1243",
    hash: "61ac41e3c7a1be44e3d3af59dd86ccd30673ad67",
    out: "src/img/content/home-specialists/sergey-shpigovsky.webp",
  },
  {
    key: "specialist-02",
    nodeId: "1:1244",
    hash: "d1b7af910d4977f3772b0a776f3084f0885ab59f",
    out: "src/img/content/home-specialists/maxim-kazakov.webp",
  },
  {
    key: "specialist-03",
    nodeId: "1:1245",
    hash: "371503e29b6df5d2801abbfca7338672cc8e4dd5",
    out: "src/img/content/home-specialists/darya-kostyuk.webp",
  },
  {
    key: "specialist-04",
    nodeId: "1:1246",
    hash: "371503e29b6df5d2801abbfca7338672cc8e4dd5",
    out: "src/img/content/home-specialists/tatyana-shapiguzova.webp",
  },
  {
    key: "article-01",
    nodeId: "1:1279",
    hash: "c99de51de7ef596f94192ef37f866353c573659f",
    out: "src/img/content/home-articles/article-alcohol-dependence.webp",
  },
  {
    key: "article-02",
    nodeId: "1:1280",
    hash: "2a1c33e99775c186541c8d81d3d8bec41973239c",
    out: "src/img/content/home-articles/article-yoga-therapy.webp",
  },
  {
    key: "article-03",
    nodeId: "1:1281",
    hash: "4e1d0887e79c3d8aec97e6a90a7cfa54a7dbd725",
    out: "src/img/content/home-articles/article-bos-therapy.webp",
  },
  {
    key: "comfort-01",
    nodeId: "1:1195",
    hash: "e4f40bb169a20b7239113b6f0154ecdf4769b142",
    out: "src/img/content/home-comfort/comfort-room-01.webp",
  },
  {
    key: "comfort-02",
    nodeId: "1:1198",
    hash: "696568a7986120af10e2b35b537cc171a5152ce2",
    out: "src/img/content/home-comfort/comfort-room-02.webp",
  },
  {
    key: "comfort-03",
    nodeId: "1:1199",
    hash: "56d93c21bb8affe8a77e7b4e59f9720c79686990",
    out: "src/img/content/home-comfort/comfort-room-03.webp",
  },
  {
    key: "comfort-04",
    nodeId: "1:1200",
    hash: "be546a9d18ee86201de5ea4cb7ce07b214505d3a",
    out: "src/img/content/home-comfort/comfort-room-04.webp",
  },
  {
    key: "comfort-05",
    nodeId: "1:1202",
    hash: "a278c7c06175e004645580d162956fc7a79d5260",
    out: "src/img/content/home-comfort/comfort-room-05.webp",
  },
  {
    key: "comfort-06",
    nodeId: "1:1207",
    hash: "44e80c1d81101538aec2e23532d0b592720046f3",
    out: "src/img/content/home-comfort/comfort-room-06.webp",
  },
  {
    key: "comfort-07",
    nodeId: "1:1204",
    hash: "8fd30cd90d8efd6ba5a36c8d07b30ffeb0049200",
    out: "src/img/content/home-comfort/comfort-room-07.webp",
  },
  {
    key: "comfort-08",
    nodeId: "1:1205",
    hash: "12d46737cb690c3c8094e6483a6dd53cc9e1eda0",
    out: "src/img/content/home-comfort/comfort-room-08.webp",
  },
  {
    key: "comfort-09",
    nodeId: "1:1206",
    hash: "6a46faf0e239a93a14d4fe4252af39337232fa19",
    out: "src/img/content/home-comfort/comfort-room-09.webp",
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
  join(workspaceRoot, "reviews", "main-content", "lower-home-audit", "FP-0002-V6-LOWER-HOME-FIG-EXPORT.json"),
  JSON.stringify(records, null, 2),
);
console.log(JSON.stringify({ count: records.length }, null, 2));
