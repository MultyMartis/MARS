import { readFileSync, writeFileSync, createHash } from "fs";
import { execFileSync } from "child_process";
import { parseFig } from "openfig-core";

const figPath =
  "C:\\MARS Phenix\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN\\Spig_v1.2.fig";
const outPath =
  "C:\\MARS Phenix\\AI MARS STORAGE\\website-factory\\fp-0002-shpigovsky-v8\\o-centre-asset-content-resolution\\temp\\FP-0002-V8-OCENTRE-HERO-IMAGE-HASH.json";

const doc = parseFig(new Uint8Array(readFileSync(figPath)));
const nodes = doc.message?.nodeChanges || [];

function listZipImages() {
  const ps = `
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [IO.Compression.ZipFile]::OpenRead('${figPath.replace(/'/g, "''")}')
$zip.Entries | Where-Object { $_.FullName -like 'images/*' } | ForEach-Object { $_.FullName + '|' + $_.Length }
$zip.Dispose()
`;
  return execFileSync("powershell", ["-NoProfile", "-Command", ps], { encoding: "utf8" })
    .trim()
    .split(/\r?\n/)
    .filter(Boolean);
}

const imageNodes = nodes.filter(
  (n) =>
    (n.name || "").includes("13030403") ||
    (n.name || "").includes("image 219") ||
    (n.fillPaints || []).some((f) => f.type === "IMAGE"),
);

const entries = listZipImages();
const sampleHashes = [];
for (const line of entries.slice(0, 20)) {
  const [full, len] = line.split("|");
  const name = full.replace("images/", "");
  const ps = `
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [IO.Compression.ZipFile]::OpenRead('${figPath.replace(/'/g, "''")}')
$e = $zip.GetEntry('${full.replace(/'/g, "''")}')
$ms = New-Object IO.MemoryStream
$s = $e.Open(); $s.CopyTo($ms); $s.Close(); $zip.Dispose()
[Convert]::ToBase64String($ms.ToArray())
`;
  const b64 = execFileSync("powershell", ["-NoProfile", "-Command", ps], {
    encoding: "utf8",
    maxBuffer: 20 * 1024 * 1024,
  }).trim();
  const buf = Buffer.from(b64, "base64");
  sampleHashes.push({ name, bytes: buf.length, sha256: createHash("sha256").update(buf).digest("hex") });
}

writeFileSync(
  outPath,
  JSON.stringify(
    {
      imageNodeCount: imageNodes.length,
      imageNodeSample: imageNodes.slice(0, 10).map((n) => ({
        id: `${n.guid.sessionID}:${n.guid.localID}`,
        name: n.name,
        fills: n.fillPaints,
      })),
      zipImageCount: entries.length,
      sampleHashes,
      servicesHeroWebpSha256: "f4fcac4135e2d7155327eb6c6b785ad8e651f4497f9fbdc608b443d0bed586e08",
      historicalExtractHash52431f99: "52431f9977e354192c7f56fe9d5503bdc6374fbb",
    },
    null,
    2,
  ),
);
console.log("zip images", entries.length, "sample hashed", sampleHashes.length);
