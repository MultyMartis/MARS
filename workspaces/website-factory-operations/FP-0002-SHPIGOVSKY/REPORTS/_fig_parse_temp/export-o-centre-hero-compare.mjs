import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { createHash } from "crypto";
import { join } from "path";
import { execSync } from "child_process";

const figPath =
  "C:/MARS Phenix/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig";
const servicesHero =
  "C:/MARS Phenix/AI MARS/workspaces/fp-0002-shpigovsky-v8/src/img/content/services/services-hero.webp";
const tempDir =
  "C:/MARS Phenix/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8/o-centre-asset-content-resolution/temp";
const evidenceDir =
  "C:/MARS Phenix/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8/o-centre-asset-content-resolution/evidence";

mkdirSync(tempDir, { recursive: true });
mkdirSync(evidenceDir, { recursive: true });

const { parseFig } = await import("openfig-core");
const doc = parseFig(new Uint8Array(readFileSync(figPath)));
const byGuid = new Map(
  (doc.message?.nodeChanges || []).map((n) => [`${n.guid.sessionID}:${n.guid.localID}`, n]),
);

function hashHex(h) {
  const bytes = Object.keys(h)
    .sort((a, b) => Number(a) - Number(b))
    .map((k) => h[k]);
  return Buffer.from(bytes).toString("hex");
}

const heroNode = byGuid.get("1:2226");
const heroHash = hashHex(heroNode.fillPaints.find((f) => f.image?.hash).image.hash);
const zipEntry = `images/${heroHash}`;
const rawPath = join(tempDir, `${heroHash}.bin`);
execSync(
  `powershell -NoProfile -Command "Add-Type -AssemblyName System.IO.Compression.FileSystem; $z=[IO.Compression.ZipFile]::OpenRead('${figPath.replace(/'/g, "''")}'); $e=$z.GetEntry('${zipEntry}'); $fs=[IO.File]::Create('${rawPath.replace(/'/g, "''")}'); $s=$e.Open(); $s.CopyTo($fs); $fs.Close(); $s.Close(); $z.Dispose()"`,
  { stdio: "inherit" },
);
const heroBuf = readFileSync(rawPath);
const heroSha = createHash("sha256").update(heroBuf).digest("hex");
const svcBuf = readFileSync(servicesHero);
const svcSha = createHash("sha256").update(svcBuf).digest("hex");

const outJpg = join(evidenceDir, "o-centre-hero-fig-c96ae505.jpg");
writeFileSync(outJpg, heroBuf);

const report = {
  figNode: "1:2226",
  figNodeName: "image 13030403",
  figImageHash: heroHash,
  exportedBytes: heroBuf.length,
  exportedSha256: heroSha,
  servicesHeroPath: servicesHero,
  servicesHeroSha256: svcSha,
  exactBinaryMatch: heroSha === svcSha,
  historicalHomeHash52431f99: "52431f9977e354192c7f56fe9d5503bdc6374fbb",
  figDimensions: { w: 1400, h: 628 },
};
writeFileSync(join(tempDir, "FP-0002-V8-OCENTRE-HERO-COMPARE.json"), JSON.stringify(report, null, 2));
console.log(JSON.stringify(report, null, 2));
