import { readFileSync, readdirSync } from "fs";
import { join } from "path";
import { parseFig } from "openfig-core";

const figPath =
  "C:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN";
const figFile = readdirSync(figPath).find((f) => f.endsWith(".fig"));
const doc = parseFig(new Uint8Array(readFileSync(join(figPath, figFile))));
const nodes = doc.message?.nodeChanges || [];

const fonts = new Map();
const fontSizes = new Map();
for (const n of nodes) {
  if (n.type !== "TEXT") continue;
  const fam = n.fontName?.family || n.fontFamily || null;
  const style = n.fontName?.style || n.fontStyle || null;
  const size = n.fontSize ? Math.round(n.fontSize) : null;
  if (fam) {
    const key = `${fam}|${style || ""}`;
    fonts.set(key, (fonts.get(key) || 0) + 1);
  }
  if (size) fontSizes.set(size, (fontSizes.get(size) || 0) + 1);
}

const variables = nodes.filter((n) => n.type === "VARIABLE" || n.type === "VARIABLE_SET");
const varSets = variables.filter((n) => n.type === "VARIABLE_SET").map((n) => n.name);
const varItems = variables
  .filter((n) => n.type === "VARIABLE")
  .slice(0, 40)
  .map((n) => ({ name: n.name, resolvedType: n.resolvedType }));

console.log(
  JSON.stringify(
    {
      fontFamilies: [...fonts.entries()]
        .sort((a, b) => b[1] - a[1])
        .slice(0, 20)
        .map(([k, c]) => ({ familyStyle: k, count: c })),
      topFontSizes: [...fontSizes.entries()]
        .sort((a, b) => b[1] - a[1])
        .slice(0, 25)
        .map(([size, count]) => ({ size, count })),
      variableSetCount: varSets.length,
      variableSetNames: varSets,
      variableSampleCount: variables.filter((n) => n.type === "VARIABLE").length,
      variableSamples: varItems,
    },
    null,
    2
  )
);
