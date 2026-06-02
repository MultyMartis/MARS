#!/usr/bin/env python3
"""Generate MARS Obsidian Canvas Export Pack v1 (JSON Canvas 1.0)."""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parent


def text_node(nid: str, label: str, x: int, y: int, w: int = 280, h: int = 100, color: str | None = None) -> dict:
    n: dict = {
        "id": nid,
        "type": "text",
        "text": label,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
    }
    if color:
        n["color"] = color
    return n


def group_node(nid: str, label: str, x: int, y: int, w: int, h: int, color: str = "5") -> dict:
    return {
        "id": nid,
        "type": "group",
        "label": label,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "color": color,
    }


def edge(eid: str, fr: str, to: str, label: str | None = None, fr_side: str = "right", to_side: str = "left") -> dict:
    e: dict = {
        "id": eid,
        "fromNode": fr,
        "fromSide": fr_side,
        "toNode": to,
        "toSide": to_side,
        "toEnd": "arrow",
    }
    if label:
        e["label"] = label
    return e


def save(name: str, nodes: list, edges: list) -> None:
    path = OUT / name
    path.write_text(json.dumps({"nodes": nodes, "edges": edges}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def build_master() -> tuple[list, list]:
    nodes = [
        text_node(
            "n-mars-root",
            "# MARS Ecosystem\n\nDocumentation-first multi-program workspace.\n\nSoT: `AGENTS.md`",
            400,
            -40,
            320,
            120,
            "6",
        ),
        text_node(
            "n-layer-governance",
            "## Governance Layer\n\n`governance/`\n\nSpine, boundaries, survivability S1–S7.\n**Maintenance mode** post–Cycle 8.",
            0,
            140,
        ),
        text_node(
            "n-layer-registry",
            "## Registry Layer\n\n`registry/`, `agents/registry.md`, `tools/registry.md`\n\nProject / agent / tool identity rows.",
            340,
            140,
        ),
        text_node(
            "n-layer-core-contract",
            "## Core Contract Layer\n\n`control-plane/`, `workflows/`, `interfaces/`, `security/`, `tools/`, `models/`, `storage/`, `memory/`, `observability/`, `evaluation/`, `integrations/`, `mars-runtime/`",
            680,
            140,
            300,
            130,
        ),
        text_node(
            "n-layer-program",
            "## Program Layer\n\n`projects/*`\n\nORCA, Website Factory, WPilot, MIG, …",
            0,
            320,
        ),
        text_node(
            "n-layer-agent",
            "## Agent Layer\n\n`agents/*`\n\nCards, Gulp foundation, Forge overlay.",
            340,
            320,
        ),
        text_node(
            "n-layer-execution",
            "## Execution Layer\n\n`workspaces/*`, human + Cursor sessions.\n\n**Not** MARS orchestration SoT.",
            680,
            320,
        ),
        text_node(
            "n-layer-infrastructure",
            "## Infrastructure Layer\n\n`C:\\AI MARS` (repo root)\n`C:\\AI MARS STORAGE` (bulk)\n\nSee `infrastructure.canvas`.",
            170,
            500,
            300,
            110,
        ),
        text_node(
            "n-layer-external",
            "## External Systems Layer\n\nn8n (MetaBOT), WordPress, hosting, Telegram, Sheets.\n\nExecution truth **outside** repo.",
            520,
            500,
            300,
            110,
        ),
        text_node(
            "n-layer-archive",
            "## Archive Layer\n\n`archive/`, `web-gpt-sources/`, lifecycle candidates.\n\nSee `archive.canvas`.",
            860,
            500,
            280,
            100,
        ),
    ]
    edges = [
        edge("e-root-gov", "n-mars-root", "n-layer-governance", "spine", "bottom", "top"),
        edge("e-gov-reg", "n-layer-governance", "n-layer-registry", "precedence"),
        edge("e-reg-core", "n-layer-registry", "n-layer-core-contract", "contracts"),
        edge("e-gov-prog", "n-layer-governance", "n-layer-program", "charter", "bottom", "top"),
        edge("e-prog-agent", "n-layer-program", "n-layer-agent", "agent packs"),
        edge("e-agent-exec", "n-layer-agent", "n-layer-execution", "implements in"),
        edge("e-exec-infra", "n-layer-execution", "n-layer-infrastructure", "runs on", "bottom", "top"),
        edge("e-prog-external", "n-layer-program", "n-layer-external", "integrates", "bottom", "top"),
        edge("e-gov-archive", "n-layer-governance", "n-layer-archive", "historical", "bottom", "top"),
        edge("e-infra-ext", "n-layer-infrastructure", "n-layer-external", "hosts / paths"),
    ]
    return nodes, edges


def build_programs() -> tuple[list, list]:
    y0 = 80
    dy = 150
    programs = [
        ("n-prog-orca", "ORCA\n\nPPC operational toolkit\n`projects/orca/`", 0),
        ("n-prog-factory", "Website Factory\n\nMethodology + contracts\n`projects/mars-website-factory/`", 1),
        ("n-prog-wpilot", "WPilot\n\nWordPress admin (External)\n`projects/wpilot/`", 2),
        ("n-prog-ocpilot", "OCPilot\n\nOpenCart bridge (External)\n`projects/ocpilot/`", 3),
        ("n-prog-mig", "MIG\n\nMarket groundtruth R1\n`projects/mig/`", 4),
        ("n-prog-metabot", "MetaBOT\n\nSEO Content Agent (n8n external)\n`projects/metabot-seo-content-agent/`", 5),
        ("n-prog-ear", "EAR Runtime\n\nMode 2 acquisition helpers\n`projects/ear-runtime/`", 6),
        ("n-prog-nova", "NOVA\n\nMobile factory foundation\n`projects/nova/`", 7),
        ("n-prog-homegateway", "HomeGateway v4.ai\n\nPersonal operational cockpit\n`projects/homegateway-v4-ai/`", 8),
        ("n-prog-survivability", "MARS Survivability\n\nSafe execution pack\n`projects/mars-survivability/`", 9),
        ("n-prog-triumph", "Triumph\n\nReference / production pack\n`projects/triumph-manipulator-landing/`", 10),
    ]
    nodes = [
        text_node(
            "n-prog-hub",
            "# MARS Programs\n\nCross-program relationships (doc-first).\n\nOpen `programs.canvas` from `master.canvas`.",
            380,
            -20,
            300,
            100,
            "6",
        ),
    ]
    for pid, label, i in programs:
        col = i % 3
        row = i // 3
        nodes.append(text_node(pid, f"## {label.split(chr(10))[0]}\n\n" + "\n".join(label.split("\n")[1:]), 40 + col * 320, y0 + row * dy, 280, 120))

    edges = [
        edge("e-hub-factory", "n-prog-hub", "n-prog-factory", None, "bottom", "top"),
        edge("e-mig-orca", "n-prog-mig", "n-prog-orca", "human handoff"),
        edge("e-orca-factory", "n-prog-orca", "n-prog-factory", "optional strategy / semantic"),
        edge("e-factory-triumph", "n-prog-factory", "n-prog-triumph", "reference case"),
        edge("e-orca-triumph", "n-prog-orca", "n-prog-triumph", "PPC + landing QA"),
        edge("e-factory-wpilot", "n-prog-factory", "n-prog-wpilot", "planned WP bridge", "right", "left"),
        edge("e-ocpilot-ear", "n-prog-ocpilot", "n-prog-ear", "snapshots (future)"),
        edge("e-wpilot-ocpilot", "n-prog-wpilot", "n-prog-ocpilot", "CMS pilot family"),
        edge("e-metabot-factory", "n-prog-metabot", "n-prog-factory", "content lane (external)"),
        edge("e-surv-all", "n-prog-survivability", "n-prog-hub", "guardrails", "left", "right"),
        edge("e-nova-factory", "n-prog-nova", "n-prog-factory", "methodology parallel"),
        edge("e-homegateway-hub", "n-prog-homegateway", "n-prog-hub", "surface layer", "top", "bottom"),
    ]
    return nodes, edges


def build_website_factory() -> tuple[list, list]:
    nodes = [
        text_node(
            "n-wf-root",
            "# Website Factory\n\n`projects/mars-website-factory/`\n\nStrategic planned · methodology operational",
            360,
            0,
            320,
            110,
            "4",
        ),
        text_node("n-wf-core", "## Core\n\nOPERATIONAL-INDEX, workflow, runbook, handoff law", 0, 160),
        text_node("n-wf-extended", "## Extended\n\nLayer map, artifact bus, semantic vocabulary", 340, 160),
        text_node("n-wf-forge", "## Forge\n\n`agents/mars-forge/` overlay on Gulp foundation", 680, 160),
        text_node("n-wf-gulp", "## Frontend Gulp Agent\n\n`agents/frontend-gulp-agent/` — canonical SoT", 0, 320),
        text_node("n-wf-ref-ws", "## Reference Workspace\n\n`workspaces/website-factory-reference-v1/`", 340, 320),
        text_node("n-wf-client-tpl", "## Client Template\n\n`workspaces/_template-client-v1/`", 680, 320),
        text_node("n-wf-prod-cases", "## Production Cases\n\nTriumph, reference-cases/", 0, 480),
        text_node("n-wf-qa", "## QA Layers\n\nValidator, HITL, operational-qa-entry", 340, 480),
        text_node("n-wf-design", "## Design Layers\n\nSemantics, implementation-pack, design governance", 680, 480),
        text_node("n-wf-build", "## Build Layers\n\nGulp src → dist (workspace execution)", 340, 640),
        text_node("n-wf-triumph", "## Triumph\n\n`triumph-manipulator-landing` + workspaces v5/v6", 0, 640, 280, 100),
        text_node(
            "n-wf-isbd-note",
            "## ISBD\n\n**SAFE UNKNOWN** — no `ISBD` execution case found in repo at export time.\n\nAdd node when case is registered.",
            680,
            640,
            280,
            110,
            "1",
        ),
    ]
    edges = [
        edge("e-wf-root-core", "n-wf-root", "n-wf-core"),
        edge("e-wf-root-ext", "n-wf-root", "n-wf-extended"),
        edge("e-wf-root-forge", "n-wf-root", "n-wf-forge"),
        edge("e-wf-core-gulp", "n-wf-core", "n-wf-gulp", "foundation"),
        edge("e-wf-forge-gulp", "n-wf-forge", "n-wf-gulp", "overlays"),
        edge("e-wf-gulp-build", "n-wf-gulp", "n-wf-build", "implements"),
        edge("e-wf-ref-build", "n-wf-ref-ws", "n-wf-build"),
        edge("e-wf-tpl-build", "n-wf-client-tpl", "n-wf-build", "adoption"),
        edge("e-wf-design-build", "n-wf-design", "n-wf-build", "handoff"),
        edge("e-wf-qa-build", "n-wf-qa", "n-wf-build", "gates"),
        edge("e-wf-prod-triumph", "n-wf-prod-cases", "n-wf-triumph"),
        edge("e-wf-triumph-qa", "n-wf-triumph", "n-wf-qa", "calibration"),
        edge("e-wf-ext-qa", "n-wf-extended", "n-wf-qa"),
    ]
    return nodes, edges


def build_orca() -> tuple[list, list]:
    nodes = [
        text_node("n-orca-root", "# ORCA\n\nHuman-supervised PPC toolkit\n`projects/orca/`", 40, 200, 260, 100, "3"),
        text_node("n-orca-fast", "## Fast Path\n\n`fast-path/` — default session entry", 380, 40),
        text_node("n-orca-review", "## Review\n\nStarter Core, assembly areas, live session reports", 380, 200),
        text_node("n-orca-ppc", "## PPC\n\nCampaign QA, content packs, Triumph PPC instances", 380, 360),
        text_node("n-orca-triumph", "## Triumph\n\nKrasnodar landing QA, route registry, exports", 720, 120),
        text_node("n-orca-validate", "## Validation / Freeze\n\n`freeze/`, URL registry sync, cross-negative QA", 720, 280),
        text_node("n-orca-mig", "## MIG Handoff\n\nHuman-only groundtruth consumption\n`contracts/mig-orca-*`", 720, 440),
        text_node("n-orca-factory", "## Factory Handoff\n\nOptional semantic / landing handoff artifacts", 720, 600),
    ]
    edges = [
        edge("e-orca-fast", "n-orca-root", "n-orca-fast", "default"),
        edge("e-orca-review", "n-orca-root", "n-orca-review"),
        edge("e-orca-ppc", "n-orca-root", "n-orca-ppc"),
        edge("e-orca-triumph", "n-orca-ppc", "n-orca-triumph"),
        edge("e-orca-validate", "n-orca-review", "n-orca-validate", "before platform work"),
        edge("e-orca-mig", "n-orca-mig", "n-orca-root", "upstream", "left", "right"),
        edge("e-orca-factory", "n-orca-validate", "n-orca-factory", "optional downstream"),
        edge("e-orca-factory-triumph", "n-orca-factory", "n-orca-triumph", "landing implementation"),
    ]
    return nodes, edges


def build_infrastructure() -> tuple[list, list]:
    nodes = [
        text_node(
            "n-inf-brain",
            "# Active Brain\n\n`C:\\AI MARS`\n\nGit workspace root — governance, projects, workspaces, docs.",
            40,
            80,
            320,
            120,
            "6",
        ),
        text_node(
            "n-inf-storage-root",
            "# Storage Layer\n\n`C:\\AI MARS STORAGE`\n\nBulk out-of-git — **not** a second repo.",
            480,
            80,
            320,
            120,
            "2",
        ),
        text_node("n-inf-repo", "## repository\n\nSingle MARS git working copy", 40, 260),
        text_node("n-inf-logs", "## logs\n\n`logs/` lifecycle, survivability, infrastructure", 40, 400),
        text_node("n-inf-workspaces", "## workspaces\n\nLane A execution loci (`workspaces/*`)", 40, 540),
        text_node("n-inf-archive-cand", "## archive candidates\n\n`archive/`, heavy imports, migration residue", 40, 680),
        text_node("n-inf-storage-repo", "## repository (bulk)\n\nPromoted baselines, snapshots per system registry", 480, 260),
        text_node("n-inf-storage-logs", "## logs (bulk)\n\nDrill exports, large run evidence (when used)", 480, 400),
        text_node("n-inf-storage-ws", "## workspaces (bulk)\n\nSite archives, temp extracts", 480, 540),
        text_node("n-inf-storage-arch", "## archive candidates\n\nCold paths (operator-defined)", 480, 680),
        text_node(
            "n-inf-external",
            "## external systems\n\nn8n · WordPress/Beget · OpenCart hosting · Telegram",
            260,
            840,
            360,
            100,
        ),
        text_node(
            "n-inf-doc-storage",
            "## In-repo `storage/` docs\n\nArchitecture contracts only — **not** `C:\\AI MARS STORAGE`",
            260,
            980,
            360,
            90,
            "5",
        ),
    ]
    edges = [
        edge("e-brain-repo", "n-inf-brain", "n-inf-repo"),
        edge("e-brain-logs", "n-inf-brain", "n-inf-logs"),
        edge("e-brain-ws", "n-inf-brain", "n-inf-workspaces"),
        edge("e-brain-arch", "n-inf-brain", "n-inf-archive-cand"),
        edge("e-storage-repo", "n-inf-storage-root", "n-inf-storage-repo"),
        edge("e-storage-logs", "n-inf-storage-root", "n-inf-storage-logs"),
        edge("e-storage-ws", "n-inf-storage-root", "n-inf-storage-ws"),
        edge("e-storage-arch", "n-inf-storage-root", "n-inf-storage-arch"),
        edge("e-brain-storage", "n-inf-brain", "n-inf-storage-root", "metadata ↔ bulk", "right", "left"),
        edge("e-ws-ext", "n-inf-workspaces", "n-inf-external", "deploy target", "bottom", "top"),
        edge("e-brain-doc", "n-inf-brain", "n-inf-doc-storage", "disambiguate", "bottom", "top"),
    ]
    return nodes, edges


def build_archive() -> tuple[list, list]:
    categories = [
        ("n-cat-active", "ACTIVE", 40, 80, "1"),
        ("n-cat-operational", "OPERATIONAL", 280, 80, "4"),
        ("n-cat-experimental", "EXPERIMENTAL", 520, 80, "3"),
        ("n-cat-planned", "PLANNED", 760, 80, "5"),
        ("n-cat-frozen", "FROZEN", 200, 380, "6"),
        ("n-cat-retired", "RETIRED", 520, 380, "2"),
        ("n-cat-archive-cand", "ARCHIVE CANDIDATE", 760, 380, "1"),
    ]
    nodes: list[dict] = [
        text_node(
            "n-arch-title",
            "# MARS Lifecycle Placement\n\nVisualization buckets — not automated enforcement.",
            300,
            -60,
            400,
            80,
            "6",
        ),
    ]
    for cid, label, x, y, color in categories:
        nodes.append(group_node(cid, label, x, y, 220, 220, color))

    placements = [
        ("n-ent-orca", "ORCA", "n-cat-active", 20, 30),
        ("n-ent-mig", "MIG", "n-cat-active", 20, 90),
        ("n-ent-wpilot", "WPilot", "n-cat-active", 20, 150),
        ("n-ent-metabot", "MetaBOT (docs)", "n-cat-active", 120, 30),
        ("n-ent-factory", "Website Factory methodology", "n-cat-operational", 20, 30),
        ("n-ent-forge", "MARS Forge overlay", "n-cat-operational", 20, 90),
        ("n-ent-gulp", "frontend-gulp-agent", "n-cat-operational", 20, 150),
        ("n-ent-surv", "mars-survivability", "n-cat-operational", 120, 30),
        ("n-ent-continuity", "continuity / IdeaBox", "n-cat-operational", 120, 90),
        ("n-ent-r1", "mars-runtime R1 JS", "n-cat-experimental", 20, 30),
        ("n-ent-ear", "EAR Runtime R1 skeleton", "n-cat-experimental", 20, 90),
        ("n-ent-wp-plugin", "WPilot DEV plugin source", "n-cat-experimental", 20, 150),
        ("n-ent-nova", "NOVA foundation", "n-cat-planned", 20, 30),
        ("n-ent-homegateway", "HomeGateway v4.ai", "n-cat-planned", 20, 90),
        ("n-ent-triumph-reg", "triumph-manipulator-landing (registry planned)", "n-cat-planned", 20, 150),
        ("n-ent-gov-freeze", "Governance post–Cycle 8 freeze", "n-cat-frozen", 20, 30),
        ("n-ent-ear-arch", "EAR Architecture (`shared/external-access-runtime/`)", "n-cat-frozen", 20, 100),
        ("n-ent-orca-freeze", "ORCA freeze packs (e.g. PPC export v1.3)", "n-cat-frozen", 120, 30),
        ("n-ent-seo-legacy", "seo-content-agent (legacy)", "n-cat-retired", 20, 30),
        ("n-ent-orca-lrl-arch", "archive/orca-lrl-foundation-v1", "n-cat-retired", 20, 100),
        ("n-ent-lifecycle-log", "Lifecycle Log (`logs/lifecycle-log.md`)", "n-cat-archive-cand", 20, 30),
        ("n-ent-web-gpt", "web-gpt-sources/", "n-cat-archive-cand", 20, 90),
        ("n-ent-chat-mig", "chat-migration imports", "n-cat-archive-cand", 20, 150),
    ]

    cat_pos = {c[0]: (c[2], c[3]) for c in categories}
    for eid, title, cat, ox, oy in placements:
        cx, cy = cat_pos[cat]
        nodes.append(text_node(eid, title, cx + ox, cy + oy + 40, 180, 50))

    edges = [
        edge("e-title-active", "n-arch-title", "n-cat-active", None, "bottom", "top"),
    ]
    return nodes, edges


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    canvases = {
        "master.canvas": build_master(),
        "programs.canvas": build_programs(),
        "website-factory.canvas": build_website_factory(),
        "orca.canvas": build_orca(),
        "infrastructure.canvas": build_infrastructure(),
        "archive.canvas": build_archive(),
    }
    stats = []
    for name, (nodes, edges) in canvases.items():
        save(name, nodes, edges)
        stats.append((name, len(nodes), len(edges)))
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
