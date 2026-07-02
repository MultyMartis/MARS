import { readFileSync, writeFileSync, mkdirSync, existsSync } from "fs";
import { join } from "path";
import { createRequire } from "module";
import { pathToFileURL } from "url";
import { execSync } from "child_process";

const require = createRequire(
  pathToFileURL(
    "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/_fig_parse_temp/package.json",
  ),
);

const { parseFig } = await import(pathToFileURL(require.resolve("openfig-core")).href);

const fig =
  "X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig";
const outDir = "X:/AI MARS/workspaces/fp-0002-shpigovsky-v8/src/img/content/blog-article";
const evidenceDir =
  "X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8/blog-article-desktop-pass-02/temp";

mkdirSync(outDir, { recursive: true });
mkdirSync(evidenceDir, { recursive: true });

const doc = parseFig(new Uint8Array(readFileSync(fig)));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const byGuid = new Map(nodes.map((n) => [guidKey(n.guid), n]));

function hashToHex(hashObj) {
  const bytes = Object.keys(hashObj)
    .sort((a, b) => Number(a) - Number(b))
    .map((k) => hashObj[k]);
  return Buffer.from(bytes).toString("hex");
}

function exportInline(num, nodeId, frameId) {
  const n = byGuid.get(nodeId);
  const hash = hashToHex(n.fillPaints[0].image.hash);
  const unzipDir = join(evidenceDir, "fig-unzip");
  mkdirSync(unzipDir, { recursive: true });
  const imagePath = join(unzipDir, "images", hash);
  if (!existsSync(imagePath)) {
    execSync(
      `powershell -NoProfile -Command "Expand-Archive -LiteralPath '${fig}' -DestinationPath '${unzipDir}' -Force"`,
      { stdio: "inherit" },
    );
  }
  const pngOut = join(outDir, `blog-article-inline-${String(num).padStart(2, "0")}-source.png`);
  writeFileSync(pngOut, readFileSync(imagePath));
  const webpOut = join(outDir, `blog-article-inline-${String(num).padStart(2, "0")}.webp`);
  execSync(
    `python -c "from PIL import Image; im=Image.open(r'${pngOut.replace(/\\/g, "/")}'); im.save(r'${webpOut.replace(/\\/g, "/")}', 'WEBP', quality=86); print(im.size)"`,
    { stdio: "inherit" },
  );
  return {
    num,
    figmaFillNodeId: nodeId,
    figmaFrameNodeId: frameId,
    imageHash: hash,
    sourcePath: pngOut,
    outputPath: webpOut,
    desktopRenderBox: "1170x603",
  };
}

const results = [
  exportInline(2, "1:3376", "1:3372"),
  exportInline(3, "1:3395", "1:3391"),
];

writeFileSync(join(evidenceDir, "inline-image-export.json"), JSON.stringify(results, null, 2));
console.log(JSON.stringify(results, null, 2));
