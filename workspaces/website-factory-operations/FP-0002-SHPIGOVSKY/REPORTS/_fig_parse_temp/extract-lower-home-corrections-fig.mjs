import { readFileSync, copyFileSync, mkdirSync, writeFileSync } from "fs";
import { join } from "path";
import { execSync } from "child_process";
import { createHash } from "crypto";
import { readdirSync } from "fs";
import { parseFig } from "openfig-core";

const figPath =
  "C:\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN";
const figFile = readdirSync(figPath).find((f) => f.endsWith(".fig"));
const figFull = join(figPath, figFile);
const workspaceRoot = "C:\\AI MARS\\workspaces\\fp-0002-shpigovsky-v6";
const tempDir = join(workspaceRoot, "reviews", "main-content", "lower-home-corrections", "_fig_extract_temp");

const assets = [
  {
    key: "program-genotyping",
    nodeId: "1:1123",
    hash: "4fa6e0b012fe85889e2b149febe080d7357605f1",
    out: "src/img/content/rehabilitation-program/program-genotyping.webp",
    direction: "01 — Генотипирование",
  },
  {
    key: "program-neuropsychology",
    nodeId: "1:1124",
    hash: "8571376fd0b8c6d1cb6094e46948fcf477a82817",
    out: "src/img/content/rehabilitation-program/program-neuropsychology.webp",
    direction: "02 — Нейропсихологическая коррекция",
  },
  {
    key: "program-psychocorrection",
    nodeId: "1:1125",
    hash: "6f28af819caac9ded0313cd5dd1835359943a6b3",
    out: "src/img/content/rehabilitation-program/program-psychocorrection.webp",
    direction: "03 — Психокоррекция",
  },
  {
    key: "program-kinesiotherapy",
    nodeId: "1:1126",
    hash: "64992cc03ac61aaeaa6bfe95a740409e4a7967bd",
    out: "src/img/content/rehabilitation-program/program-kinesiotherapy.webp",
    direction: "04 — Кинезиотерапия",
  },
  {
    key: "video-preview-01",
    nodeId: "1:4420",
    hash: "2cbaae6126ecf41276665e0f246fdd59284ebdeb",
    out: "src/img/content/home-videos/video-preview-01.webp",
  },
  {
    key: "video-preview-02",
    nodeId: "1:4421",
    hash: "0d9d00cc81bf1318cbed247544120161d3e094f1",
    out: "src/img/content/home-videos/video-preview-02.webp",
  },
  {
    key: "comfort-decor",
    nodeId: "1:1179",
    hash: "de219c6e462c8bf42469bb33751a81252eedc07f",
    out: "src/img/content/home-comfort/comfort-gallery-logo-decor.webp",
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

function renderComfortDecor(destPath) {
  const script = `
from PIL import Image, ImageDraw
from pathlib import Path

w, h = 383, 360
bg = (255, 255, 255, 255)
border = (71, 83, 113, 255)
img = Image.new('RGBA', (w, h), bg)
draw = ImageDraw.Draw(img)
draw.rectangle([0, 0, w - 1, h - 1], outline=border, width=1)
logo_path = Path(r'${join(workspaceRoot, "src", "img", "branding", "logo.svg").replace(/\\/g, "\\\\")}')
out = Path(r'${destPath.replace(/\\/g, "\\\\")}')
out.parent.mkdir(parents=True, exist_ok=True)
try:
    import cairosvg
    logo_png = out.parent / '_logo-temp.png'
    cairosvg.svg2png(url=str(logo_path), write_to=str(logo_png), output_width=180)
    logo = Image.open(logo_png).convert('RGBA')
    img.alpha_composite(logo, ((w - logo.width) // 2, (h - logo.height) // 2))
    logo_png.unlink(missing_ok=True)
except Exception:
    draw.text((w // 2 - 40, h // 2 - 10), 'Шпиговский', fill=border)
rgb = Image.new('RGB', img.size, (255, 255, 255))
rgb.paste(img, mask=img.split()[3] if img.mode == 'RGBA' else None)
rgb.save(out.with_suffix('.webp'), 'WEBP', quality=86)
print(rgb.size[0], rgb.size[1])
`;
  mkdirSync(join(destPath, ".."), { recursive: true });
  const dimOut = execSync(`py -3 -c "${script.replace(/"/g, '\\"').replace(/\r?\n/g, "; ")}"`, {
    encoding: "utf8",
  }).trim();
  const [width, height] = dimOut.split(" ").map(Number);
  const bytes = readFileSync(destPath);
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
  let meta;
  if (asset.key === "comfort-decor") {
    meta = renderComfortDecor(outPath);
  } else {
    meta = extractFromZip(asset.hash, outPath);
  }
  records.push({ ...asset, exportedTo: asset.out, ...meta });
}

writeFileSync(
  join(workspaceRoot, "reviews", "main-content", "lower-home-corrections", "FP-0002-V6-LOWER-HOME-FIG-EXPORT.json"),
  JSON.stringify(records, null, 2),
);
console.log(JSON.stringify({ count: records.length }, null, 2));
