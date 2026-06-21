import { readFileSync } from "fs";
import { join } from "path";
import { parseFig } from "openfig-core";
import { readdirSync } from "fs";

const figPath = String.raw`C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN`;
const figFile = readdirSync(figPath).find(f => f.endsWith('.fig'));
const doc = parseFig(new Uint8Array(readFileSync(join(figPath, figFile))));
const nodes = doc.message?.nodeChanges || [];
const blobs = doc.message?.blobs || [];
console.log('blobs', blobs.length);

const t = nodes.find(n => n.name === 'Записаться на консультацию');
console.log('textData', t?.textData);
console.log('textData chars type', typeof t?.textData?.characters, t?.textData?.characters?.constructor?.name);
if (t?.textData?.characters instanceof Uint8Array) {
  const dec = new TextDecoder('utf-8').decode(t.textData.characters);
  console.log('decoded', dec);
}
// try name as fallback
const namesAsText = nodes.filter(n=>n.type==='TEXT' && n.name && !n.name.startsWith('Текст')).map(n=>n.name);
console.log('named text nodes', namesAsText.length);
console.log(namesAsText.slice(0,30));
