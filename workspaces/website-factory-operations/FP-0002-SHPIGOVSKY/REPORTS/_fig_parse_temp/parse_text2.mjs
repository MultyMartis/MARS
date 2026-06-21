import { readFileSync, writeFileSync } from "fs";
import { join } from "path";
import { parseFig } from "openfig-core";
import { readdirSync } from "fs";

const figPath = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN`;
const figFile = readdirSync(figPath).find(f => f.endsWith('.fig'));
const doc = parseFig(new Uint8Array(readFileSync(join(figPath, figFile))));
const nodes = doc.message?.nodeChanges || [];
const texts = nodes.filter(n => n.type==='TEXT');

function extractText(t) {
  if (t.characters) return t.characters;
  const d = t.derivedTextData;
  if (d?.characters) return d.characters;
  if (d?.glyphs) return d.glyphs.map(g=>g.codePoint ? String.fromCodePoint(g.codePoint):'').join('');
  const td = t.textData;
  if (td?.characters) return td.characters;
  return null;
}

const samples = texts.slice(0,20).map(t => ({
  name: t.name,
  extracted: extractText(t),
  derivedKeys: t.derivedTextData ? Object.keys(t.derivedTextData) : [],
  textDataKeys: t.textData ? Object.keys(t.textData) : [],
}));

const extracted = texts.map(extractText).filter(Boolean);
console.log('extracted count', extracted.length, 'of', texts.length);
console.log(JSON.stringify(samples.slice(0,5), null, 2));
console.log('sample texts', extracted.slice(0,15));
