import { readFileSync, writeFileSync } from "fs";
import { parseFig } from "openfig-core";

const figPath =
  "C:\\MARS Phenix\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\INCOMING\\01_DESIGN\\Spig_v1.2.fig";
const outPath =
  "C:\\MARS Phenix\\AI MARS STORAGE\\website-factory\\fp-0002-shpigovsky-v8\\o-centre-asset-content-resolution\\temp\\FP-0002-V8-OCENTRE-TAG-INSTANCE-RESOLVE.json";

const doc = parseFig(new Uint8Array(readFileSync(figPath)));
const nodes = doc.message?.nodeChanges || [];
const guidKey = (g) => (g ? `${g.sessionID}:${g.localID}` : null);
const byGuid = new Map(nodes.map((n) => [guidKey(n.guid), n]));

function getText(n) {
  const c = n.textData?.characters ?? n.characters;
  return c != null ? String(c).trim() : null;
}

const tagSymbol = nodes.find((n) => n.type === "SYMBOL" && n.name === "Тэг");
const tagInstances = nodes.filter((n) => n.type === "INSTANCE" && n.name === "Тэг" && n.parentIndex?.guid?.sessionID === 1 && [2241,2242,2243,2244,2245,2246,2247].includes(n.parentIndex?.guid?.localID === undefined ? -1 : n.guid?.localID >= 2241 && n.guid?.localID <= 2247 ? n.guid.localID : n.parentIndex?.guid?.localID));

// O-centre tab instances by id
const tabIds = ["1:2241","1:2242","1:2243","1:2244","1:2245","1:2246","1:2247"];
const tabs = tabIds.map((id) => {
  const inst = byGuid.get(id);
  const overrides = (inst?.componentProperties || []).map((p) => ({ name: p.name, value: p.value, type: p.type }));
  const symbolId = inst?.symbolData?.symbolID ? guidKey(inst.symbolData.symbolID) : null;
  const symbol = symbolId ? byGuid.get(symbolId) : tagSymbol;
  // collect override texts from inst and descendants via overrideKey
  const texts = [];
  for (const n of nodes) {
    if (!n.overrideKey) continue;
    if (n.overrideKey.overriddenComponentID?.guid?.sessionID === inst?.guid?.sessionID && n.overrideKey.overriddenComponentID?.guid?.localID === inst?.guid?.localID) {
      const t = getText(n);
      if (t) texts.push({ id: guidKey(n.guid), name: n.name, text: t });
    }
  }
  // fallback: walk symbol template for default text
  const symbolTexts = [];
  if (symbol) {
    const walk = (gid, depth = 0) => {
      const nn = byGuid.get(gid);
      if (!nn || depth > 8) return;
      const t = getText(nn);
      if (t) symbolTexts.push({ id: guidKey(nn.guid), name: nn.name, text: t });
      for (const ch of nodes) {
        if (ch.parentIndex?.guid?.sessionID === nn.guid?.sessionID && ch.parentIndex?.guid?.localID === nn.guid?.localID) {
          walk(guidKey(ch.guid), depth + 1);
        }
      }
    };
    walk(guidKey(symbol.guid));
  }
  return { id, overrides, texts, symbolTexts, symbolId: symbol ? guidKey(symbol.guid) : null };
});

// Also dump all TEXT under tab parent frame
const tabFrame = byGuid.get("1:2240");
const allTabTexts = nodes.filter((n) => {
  if (n.type !== "TEXT") return false;
  let cur = n;
  for (let i = 0; i < 20; i++) {
    if (!cur?.parentIndex?.guid) return false;
    const pk = guidKey(cur.parentIndex.guid);
    if (pk === "1:2240") return true;
    cur = byGuid.get(pk);
  }
  return false;
}).map((n) => ({ id: guidKey(n.guid), name: n.name, text: getText(n) }));

// Search component property strings on tab instances
const propTexts = tabIds.map((id) => {
  const inst = byGuid.get(id);
  return {
    id,
    props: inst?.componentProperties,
    exposed: inst?.exposedInstances,
    symbolOverrides: inst?.symbolOverrides,
    overrides: inst?.overrides,
  };
});

writeFileSync(outPath, JSON.stringify({ tabs, allTabTexts, propTexts, tagSymbolId: tagSymbol ? guidKey(tagSymbol.guid) : null }, null, 2));
console.log("allTabTexts", allTabTexts.length);
for (const t of tabs) console.log(t.id, t.texts, t.overrides?.slice?.(0,3));
