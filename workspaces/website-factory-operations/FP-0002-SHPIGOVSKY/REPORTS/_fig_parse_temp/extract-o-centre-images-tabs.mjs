import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
import { createHash } from "crypto";
import { execFileSync } from "child_process";

const __dir = dirname(fileURLToPath(import.meta.url));
const figPath =
  "C:\\MARS Phenix\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN\\Spig_v1.2.fig";
const tempDir =
  "C:\\MARS Phenix\\AI MARS STORAGE\\website-factory\\fp-0002-shpigovsky-v8\\o-centre-asset-content-resolution\\temp";
const evidenceDir =
  "C:\\MARS Phenix\\AI MARS STORAGE\\website-factory\\fp-0002-shpigovsky-v8\\o-centre-asset-content-resolution\\evidence";

const { parseFig } = await import("openfig-core");

const doc = parseFig(new Uint8Array(readFileSync(figPath)));
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
function sortedKids(id) {
  return [...(children.get(id) || [])].sort(
    (a, b) => (a.parentIndex?.position ?? 0) - (b.parentIndex?.position ?? 0),
  );
}
function isVisible(n) {
  if (!n || n.visible === false) return false;
  let cur = n;
  while (cur) {
    if (cur.visible === false) return false;
    const pk = guidKey(cur.parentIndex?.guid);
    cur = pk ? byGuid.get(pk) : null;
  }
  return true;
}
function getText(n) {
  if (n.type !== "TEXT") return null;
  const c = n.textData?.characters ?? n.characters;
  return c != null && String(c).trim() ? String(c) : null;
}
function findFrame(name) {
  return nodes.find((n) => n.name === name && n.type === "FRAME") || null;
}
function walk(id, visitor, depth = 0, path = []) {
  const n = byGuid.get(id);
  if (!n) return;
  const nextPath = [...path, n.name || n.type];
  visitor(n, depth, nextPath);
  for (const k of sortedKids(id)) walk(guidKey(k.guid), visitor, depth + 1, nextPath);
}
function collectImagesDeep(rootId) {
  const images = [];
  walk(rootId, (n, depth, path) => {
    if (!isVisible(n)) return;
    for (const f of n.fillPaints || []) {
      if (f.type === "IMAGE" && f.imageRef) {
        images.push({
          nodeId: guidKey(n.guid),
          nodeName: n.name,
          nodeType: n.type,
          imageRef: f.imageRef,
          path: path.join(" > "),
          w: Math.round(n.size?.x ?? 0),
          h: Math.round(n.size?.y ?? 0),
        });
      }
    }
  });
  return images;
}

const desktop = findFrame("О центре");
const hero = sortedKids(guidKey(desktop.guid)).find((n) => n.name === "1 - Главный экран");
const tabsFrame = sortedKids(guidKey(hero.guid)).find((n) => n.name === "Табы");
const tabTexts = [];
if (tabsFrame) {
  walk(guidKey(tabsFrame.guid), (n) => {
    const t = getText(n);
    if (t) tabTexts.push({ id: guidKey(n.guid), name: n.name, text: t });
  });
}

const heroImages = collectImagesDeep(guidKey(hero.guid));
const advantages = sortedKids(guidKey(desktop.guid)).find((n) => n.name === "преимущества");
const advImages = advantages ? collectImagesDeep(guidKey(advantages.guid)) : [];

function readZipImage(figPath, imageRef) {
  const ps = `
$zip = [System.IO.Compression.ZipFile]::OpenRead('${figPath.replace(/'/g, "''")}')
$entry = $zip.GetEntry('images/${imageRef}')
if ($null -eq $entry) { $zip.Dispose(); exit 2 }
$ms = New-Object System.IO.MemoryStream
$stream = $entry.Open()
$stream.CopyTo($ms)
$stream.Close()
$zip.Dispose()
[Convert]::ToBase64String($ms.ToArray())
`;
  try {
    const b64 = execFileSync("powershell", [
      "-NoProfile",
      "-Command",
      "Add-Type -AssemblyName System.IO.Compression.FileSystem;" + ps,
    ], { encoding: "utf8", maxBuffer: 50 * 1024 * 1024 }).trim();
    return Buffer.from(b64, "base64");
  } catch {
    return null;
  }
}

mkdirSync(evidenceDir, { recursive: true });
const imageReport = [];
for (const img of [...heroImages, ...advImages]) {
  const buf = readZipImage(figPath, img.imageRef);
  const sha256 = buf ? createHash("sha256").update(buf).digest("hex") : null;
  imageReport.push({ ...img, sha256, bytes: buf?.length ?? 0, inZip: !!buf });
  if (buf && img.path.includes("Group 6")) {
    const out = join(evidenceDir, `hero-${img.imageRef.slice(0, 12)}.jpg`);
    writeFileSync(out, buf);
  }
}

const out = {
  tabs: tabTexts,
  heroImages,
  advantagesImages: advImages,
  imageReport,
};
writeFileSync(join(tempDir, "FP-0002-V8-OCENTRE-IMAGES-TABS-EXTRACT.json"), JSON.stringify(out, null, 2));
console.log(JSON.stringify({ tabs: tabTexts, heroImages, advCount: advImages.length }, null, 2));
