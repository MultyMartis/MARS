# ORCA LRL Foundation v1 — Archive

**Label:** `orca-lrl-foundation-v1`  
**Freeze date:** 2026-05-30  
**Checkpoint commit:** `d6b67ea6776e304775cd9be371cd4d480770f4f8`  
**Commit message:** `ORCA Landing Readiness Layer v1 foundation`  
**Branch at freeze:** `mars/post-cycle8-live-tests`

---

## Milestone purpose

Point-in-time survivability backup of the **ORCA Landing Readiness Layer (LRL) v1 foundation** — documentation-only architecture that formalizes deployed landing truth before PPC work.

This freeze captures the approved foundation package after Triumph Search Battle v1 lessons, Commander import PASS, and Makita pilot preparation. It does **not** include pilot execution artifacts, PPC export work, or unrelated ORCA domains.

---

## Why this milestone matters

Triumph Search Battle v1 proved that **semantic packs alone are insufficient** for PPC alignment: deployed copy, URLs, and CTAs can diverge from semantic intent. LRL v1 closes that gap with:

- **Landing Readiness Layer** — domain model and boundaries
- **Landing Ready Contract (LRC)** — human-readable gate record per route
- **Final Website Copy Pack (FWCP)** — approved deployed copy artifact
- **Makita pilot preparation** — execution plan, success criteria, preflight review, observation log

Without this freeze, operators risk losing the canonical v1 foundation if live `projects/orca/` paths evolve during pilot or Triumph migration work.

---

## Files included

| Archive path | Live source (at commit) |
|--------------|-------------------------|
| `intelligence/landing-readiness-layer-v1.md` | `projects/orca/intelligence/landing-readiness-layer-v1.md` |
| `intelligence/landing-ready-contract-v1.md` | `projects/orca/intelligence/landing-ready-contract-v1.md` |
| `intelligence/final-website-copy-pack-v1.md` | `projects/orca/intelligence/final-website-copy-pack-v1.md` |
| `pilots/makita-lrl-pilot-v1.md` | `projects/orca/pilots/makita-lrl-pilot-v1.md` |
| `pilots/makita-lrl-success-criteria-v1.md` | `projects/orca/pilots/makita-lrl-success-criteria-v1.md` |
| `pilots/makita-lrl-observation-log-v1.md` | `projects/orca/pilots/makita-lrl-observation-log-v1.md` |
| `pilots/makita-lrl-preflight-review-v1.md` | `projects/orca/pilots/makita-lrl-preflight-review-v1.md` |

**Also in this folder (freeze metadata, not copied from live tree):**

- `ARCHIVE-README.md` — this file
- `LRL-FOUNDATION-SUMMARY-v1.md` — freeze summary

---

## Excluded (by design)

- Triumph PPC exporter, validation-cli, freeze layers, content-packs
- Website Factory implementation, workspaces, dist/build outputs
- Makita project runtime artifacts (`projects/orca/projects/makita*/` — created at pilot execution)
- Governance, MARS-survivability, HomeGateway, unrelated ORCA archives

---

## Restoration notes

1. **Verify commit:** `git show d6b67ea` or checkout files from that commit under `projects/orca/`.
2. **Compare to live:** If live intelligence/pilot docs drift, treat **this archive + commit** as the v1 foundation SoT unless a newer human charter supersedes.
3. **Restore procedure:** Copy archived files back to their live paths (preserve relative structure under `projects/orca/`).
4. **Internal links:** Archived copies retain relative links as in live tree (e.g. `../freeze/...`). From archive folder those links may not resolve — use live repo paths or commit checkout for full context.
5. **Pilot state:** Observation log in archive is the **prep-time** template; live log may gain entries during Makita execution — do not overwrite live execution notes with archive copy without operator review.

---

## Boundaries

Human-operated documentation backup. **Not** runtime. **Not** orchestration. **Not** launch approval. **Not** automated validation.

Makita Pilot status at freeze: **READY** (preparation complete; execution not started in this checkpoint).
