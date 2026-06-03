# MARS v2 Stable Baseline — Web-GPT Source Pack (2026-06)

**Status:** **CORE** — canonical upload pack for external Web-GPT after official **MARS v2 Stable Baseline 2026-06** publication.  
**Publication:** commit `45518bb` · checkpoint `mars-v2-stable-baseline-2026-06` · evidence `c2876cf`  
**Post-cleanup refresh:** 2026-06-03 — same pack folder (no new version); aligns GitGuard, IdeaBox, Incoming, Lifecycle, ISBD with Wave 1–2B. See `web-gpt-sources/REPORT-WEB-GPT-PACK-REFRESH-2026-06.md`.  
**Path:** `web-gpt-sources/mars-v2-stable-baseline-2026-06/` — **10 topic files + this README**

---

## One-line default

**Tier 0 honesty → lane OPERATIONAL-INDEX → ship work + REPORT.** Governance is authoritative but **not** the default work product. **Documentation-first baseline** — not MARS v3, not shipped runtime.

---

## What changed from prior packs

| Prior pack | Disposition |
|------------|-------------|
| `mars-v2-final/` | **Superseded for upload** — absorbed into this pack; keep in-repo as Cycle 8 alignment artefact at `45518bb` |
| `mars-v2/` | **Duplicate / historical** — do not upload alongside this pack |
| `chat-migration/` | **Paste-only continuity** — not upload SoT |
| Numbered `01_system.md` … `14_roadmap.md` | **Legacy import** — reconcile via governance, not parallel upload |

---

## Load order (minimum → full)

| Order | File | Topic |
|-------|------|-------|
| 1 | `01_MARS_IDENTITY.md` | What MARS is / is not |
| 2 | `02_OPERATIONAL_POSTURE.md` | Post–Cycle 8 + maintenance mode |
| 3 | `10_RUNTIME_BOUNDARY_RULES.md` | Hard runtime honesty line |
| 4 | `07_STABLE_BASELINE_PUBLICATION.md` | Official baseline scope |
| 5 | `03_PROGRAM_REGISTRY_SUMMARY.md` | Registered programs |
| 6 | `09_OPERATIONAL_PRIORITIES.md` | Ranked delivery focus |
| 7 | `04_INFRASTRUCTURE_REALITY.md` | `C:\AI MARS` vs `C:\AI MARS STORAGE` |
| 8 | `05_ACTIVE_VISUAL_COLD_BRAIN.md` | Brain layers |
| 9 | `06_KNOWLEDGE_CENTER.md` | Operator navigation (out-of-git) |
| 10 | `08_SYSTEM_MATURITY_MAP.md` | Maturity buckets |
| — | `WEB-GPT-SOURCE-PACK-INDEX.md` (parent folder) | Human upload sequence |
| — | `WEB-GPT-CHAT-SYNC-PACK.md` (parent folder) | Per-program chat sync targets |

**Minimum truth bundle:** `01` + `02` + `10` → declare lane → open **one** in-repo `OPERATIONAL-INDEX.md` Core Run row.

**Do not** read all files before starting work.

---

## Migration notes (from audit)

### Upload to Web-GPT

1. **Replace** prior project sources built from `mars-v2-final/` or `mars-v2/` with **this folder only** (plus index files at `web-gpt-sources/` root).
2. **Do not** upload numbered legacy topics (`01_system.md` …) unless doing historical archaeology.
3. **Do not** paste `chat-migration/` as SoT — use for one-time continuity only.
4. **Exclude** vendor trees, `dist/`, `mars-runtime/**/*.js`, OCPilot `baselines/**/files/**` bulk.

### In-repo only (not Web-GPT pack)

- Full `governance/**` — cite paths; do not mirror entire tree into Web-GPT.
- Knowledge Center bulk at `C:\AI MARS STORAGE\MARS KNOWLEDGE CENTER` — operator Obsidian vault; not git.
- Workspaces WIP excluded from baseline checkpoint — re-verify per task.

---

## Repo anchor

| Surface | Path |
|---------|------|
| Working copy | `C:\AI MARS` |
| Baseline evidence | `logs/releases/mars-v2-stable-baseline-2026-06.md` |
| IDE rules | `AGENTS.md`, `.cursorrules` |
| Ecosystem posture | `governance/mars-operational-evolution-state-after-cycles-1-8-v0.md` |

*Stable Baseline Web-GPT pack v1 — 2026-06-03 — Lane B.*
