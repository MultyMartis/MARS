import { readFileSync, copyFileSync, mkdirSync, writeFileSync } from "fs";
import { join } from "path";
import { execSync } from "child_process";
import { createHash } from "crypto";
import { parseFig } from "openfig-core";

const figFull =
  "C:\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN\\Шпиговский.fig";
const outDir =
  "C:\\AI MARS\\workspaces\\fp-0002-shpigovsky-v6\\src\\img\\content\\gallery";
const tempDir =
  "C:\\AI MARS\\workspaces\\fp-0002-shpigovsky-v6\\reviews\\main-content\\gallery-audit\\_fig_extract_temp";

const galleryInstanceIds = ["1:986", "1:987", "1:988", "1:989"];

const doc = parseFig(new Uint8Array(readFileSync(figFull)));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const byGuid = new Map(nodes.map((n) => [guidKey(n.guid), n]));

function hashHex(buf) {
  return buf ? Buffer.from(buf).toString("hex") : null;
}

function extractInstanceImageHash(nodeId) {
  const n = byGuid.get(nodeId);
  if (!n?.symbolData?.symbolOverrides) return null;
  for (const override of n.symbolData.symbolOverrides) {
    for (const paint of override.fillPaints || []) {
      if (paint.type === "IMAGE") {
        const h = hashHex(paint.imageHash || paint.image?.hash);
        if (h) return h;
      }
    }
  }
  return null;
}

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
  copyFileSync(tempExtract, destPath);
}

mkdirSync(outDir, { recursive: true });
mkdirSync(tempDir, { recursive: true });

const records = [];

for (let i = 0; i < galleryInstanceIds.length; i += 1) {
  const nodeId = galleryInstanceIds[i];
  const n = byGuid.get(nodeId);
  const imageHash = extractInstanceImageHash(nodeId);
  if (!imageHash) {
    throw new Error(`Missing image hash for ${nodeId}`);
  }
  const pngTemp = join(tempDir, `gallery-${i + 1}.png`);
  const webpOut = join(outDir, `shpigovsky-gallery-0${i + 1}.webp`);
  extractFromZip(imageHash, pngTemp);
  execSync(
    `py -3 -c "from PIL import Image; im=Image.open(r'${pngTemp.replace(/'/g, "''")}'); im.save(r'${webpOut.replace(/'/g, "''")}', 'WEBP', quality=86)"`,
    { stdio: "inherit" },
  );
  const bytes = readFileSync(webpOut);
  const dimOut = execSync(
    `py -3 -c "from PIL import Image; im=Image.open(r'${webpOut.replace(/'/g, "''")}'); print(im.size[0], im.size[1])"`,
    { encoding: "utf8" },
  ).trim();
  const [width, height] = dimOut.split(" ").map(Number);
  records.push({
    index: i + 1,
    page: "Page 1",
    frame: "3- Услуги (1:958) / Frame 81513740 (1:983)",
    nodeName: n?.name || "Услуга",
    nodeId,
    nativeDimensions: { width, height },
    displayDimensions: n?.size
      ? { width: Math.round(n.size.x), height: Math.round(n.size.y) }
      : null,
    imageHash,
    cropMode: "Figma instance override fill (symbol child 535:11169)",
    exportedTo: webpOut.replace(/\\/g, "/"),
    sha256: createHash("sha256").update(bytes).digest("hex"),
    fileBytes: bytes.length,
  });
}

const provenance = `# Gallery asset provenance

| # | Node ID | Node name | Image hash | Export | Dimensions |
| - | ------- | --------- | ---------- | ------ | ---------- |
${records
  .map(
    (r) =>
      `| ${r.index} | ${r.nodeId} | ${r.nodeName} | ${r.imageHash} | shpigovsky-gallery-0${r.index}.webp | ${r.nativeDimensions.width}×${r.nativeDimensions.height} |`,
  )
  .join("\n")}

Export settings: extracted PNG from Figma \`.fig\` zip \`images/<hash>\`, converted to WebP quality 86 via Pillow.
`;

writeFileSync(join(outDir, "GALLERY-ASSET-PROVENANCE.md"), provenance, "utf8");
writeFileSync(
  "reviews/main-content/gallery-audit/FP-0002-V6-GALLERY-FIGMA-NODES.json",
  JSON.stringify(records, null, 2),
);
console.log(JSON.stringify(records, null, 2));
