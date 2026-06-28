#!/usr/bin/env python3
"""Read-only offline parse helper for FP-0002 services hub anatomy (Spig_v1.2.fig)."""
import json
import sys
from pathlib import Path

# Use openfig-core from project temp node_modules via a tiny inline loader
ROOT = Path(r"C:\MARS Phenix\AI MARS")
FIG = ROOT / r"workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN\Spig_v1.2.fig"
OPENFIG = ROOT / r"workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\_fig_parse_temp\node_modules\openfig-core\dist\index.cjs"

# Load openfig via node subprocess if direct import fails
import subprocess
node_script = f"""
const {{ readFileSync, writeFileSync }} = require('fs');
const {{ parseFig }} = require({json.dumps(str(OPENFIG))});
const doc = parseFig(new Uint8Array(readFileSync({json.dumps(str(FIG))})));
const nodes = doc.message?.nodeChanges || [];
const gk = (g) => (g ? `${{g.sessionID}}:${{g.localID}}` : null);
const by = new Map(nodes.map(n => [gk(n.guid), n]));
const kids = new Map();
for (const n of nodes) {{
  const pk = gk(n.parentIndex?.guid);
  if (!pk) continue;
  if (!kids.has(pk)) kids.set(pk, []);
  kids.get(pk).push(n);
}}
function sortedKids(id) {{
  return [...(kids.get(id) || [])].sort((a,b)=>(a.parentIndex?.position??0)-(b.parentIndex?.position??0));
}}
function isVisible(n) {{
  if (!n || n.visible === false) return false;
  let cur = n;
  while (cur) {{
    if (cur.visible === false) return false;
    const pk = gk(cur.parentIndex?.guid);
    cur = pk ? by.get(pk) : null;
  }}
  return true;
}}
function size(n) {{
  const sz = n.size || n.absoluteBoundingBox || {{}};
  return {{ w: Math.round(sz.x ?? sz.width ?? 0), h: Math.round(sz.y ?? sz.height ?? 0) }};
}}
function walk(id, depth=0, acc=[]) {{
  const n = by.get(id);
  if (!n || !isVisible(n)) return acc;
  acc.push({{ id, name: n.name, type: n.type, depth, ...size(n), layoutMode: n.layoutMode || null }});
  for (const c of sortedKids(id)) walk(gk(c.guid), depth+1, acc);
  return acc;
}}
function findFrame(name) {{
  return nodes.find(n => n.name === name && n.type === 'FRAME');
}}
const out = {{}};
for (const nm of ['Услуги хаб', 'Услуги хаб - мob', 'Услуги хаб - моб']) {{
  const f = findFrame(nm);
  if (f) out[nm] = {{ id: gk(f.guid), ...size(f), children: sortedKids(gk(f.guid)).map(c => ({{ id: gk(c.guid), name: c.name, type: c.type, ...size(c) }})) }};
}}
const hero = findFrame('1 - Главный экран');
if (hero) {{
  const hid = gk(hero.guid);
  out.hero = {{ id: hid, ...size(hero), tree: walk(hid).slice(0, 80) }};
}}
// hero under services hub specifically
const hub = findFrame('Услуги хаб');
if (hub) {{
  const hubId = gk(hub.guid);
  out.hubRoot = {{ id: hubId, ...size(hub) }};
  const heroChild = sortedKids(hubId).find(c => c.name === '1 - Главный экран');
  if (heroChild) {{
    const hid = gk(heroChild.guid);
    out.servicesHero = {{ id: hid, ...size(heroChild), directChildren: sortedKids(hid).map(c => ({{ id: gk(c.guid), name: c.name, type: c.type, ...size(c) }})) }};
    out.servicesHeroTree = walk(hid);
  }}
}}
// search named layers
const named = [];
for (const n of nodes) {{
  if (!isVisible(n)) continue;
  const nm = (n.name || '').toLowerCase();
  if (['хлеб','крош','breadcrumb','frame 10','frame 20','с чего начать'].some(k => nm.includes(k))) {{
    named.push({{ id: gk(n.guid), name: n.name, type: n.type, parent: gk(n.parentIndex?.guid), ...size(n) }});
  }}
}}
out.namedHits = named.slice(0, 50);
process.stdout.write(JSON.stringify(out, null, 2));
"""

# find node
node_candidates = [
    r"C:\Program Files\nodejs\node.exe",
    r"C:\Program Files (x86)\nodejs\node.exe",
    r"C:\Users\MetaCODE ONE\AppData\Local\Programs\cursor\resources\app\resources\helpers\node.exe",
    r"C:\Program Files\Microsoft Visual Studio\18\Community\MSBuild\Microsoft\VisualStudio\NodeJs\node.exe",
]
node = None
for c in node_candidates:
    if Path(c).exists():
        node = c
        break
if not node:
    # try where via cmd
    import shutil
    node = shutil.which("node")
if not node:
    print(json.dumps({"error": "node not found"}))
    sys.exit(1)

proc = subprocess.run([node, "-e", node_script], capture_output=True, text=True)
if proc.returncode != 0:
    print(json.dumps({"error": proc.stderr, "stdout": proc.stdout}))
    sys.exit(proc.returncode)
print(proc.stdout)
