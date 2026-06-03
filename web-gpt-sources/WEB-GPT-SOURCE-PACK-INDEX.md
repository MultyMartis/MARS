# WEB-GPT Source Pack Index — Upload Order

**Purpose:** Human upload sequence for external Web-GPT project sources after **MARS v2 Stable Baseline 2026-06**.  
**Pack folder:** `web-gpt-sources/mars-v2-stable-baseline-2026-06/`  
**Companion:** `WEB-GPT-CHAT-SYNC-PACK.md` (per-program chat synchronization)

**Do not upload:** legacy numbered topics, `mars-v2/`, `mars-v2-final/`, `chat-migration/`, vendor trees, `mars-runtime/**/*.js`.

---

## Recommended source upload sequence

Upload **one file at a time** in this order. After steps 1–3, declare lane and open the relevant in-repo `OPERATIONAL-INDEX.md` before uploading the rest (optional depth).

| Step | File | Why this order |
|------|------|----------------|
| **1** | `mars-v2-stable-baseline-2026-06/01_MARS_IDENTITY.md` | Truth baseline — what MARS is and is not |
| **2** | `mars-v2-stable-baseline-2026-06/02_OPERATIONAL_POSTURE.md` | Post–Cycle 8 defaults and maintenance mode |
| **3** | `mars-v2-stable-baseline-2026-06/10_RUNTIME_BOUNDARY_RULES.md` | Hard anti-mythology line before planning |
| **4** | `mars-v2-stable-baseline-2026-06/07_STABLE_BASELINE_PUBLICATION.md` | Official checkpoint scope and exclusions |
| **5** | `mars-v2-stable-baseline-2026-06/03_PROGRAM_REGISTRY_SUMMARY.md` | Registered programs and relationships |
| **6** | `mars-v2-stable-baseline-2026-06/09_OPERATIONAL_PRIORITIES.md` | Ranked delivery focus |
| **7** | `mars-v2-stable-baseline-2026-06/04_INFRASTRUCTURE_REALITY.md` | `C:\AI MARS` vs `C:\AI MARS STORAGE` |
| **8** | `mars-v2-stable-baseline-2026-06/05_ACTIVE_VISUAL_COLD_BRAIN.md` | Active / Visual / Cold Brain layers |
| **9** | `mars-v2-stable-baseline-2026-06/06_KNOWLEDGE_CENTER.md` | Operator KC (out-of-git) |
| **10** | `mars-v2-stable-baseline-2026-06/08_SYSTEM_MATURITY_MAP.md` | Maturity buckets and routers |
| **11** | `mars-v2-stable-baseline-2026-06/README.md` | Pack meta, migration notes, load-order reference |

**Optional step 12:** `WEB-GPT-CHAT-SYNC-PACK.md` — when opening or refreshing program-specific chats.

---

## Minimum viable upload (fast bootstrap)

If time-constrained, upload only:

1. `01_MARS_IDENTITY.md`  
2. `02_OPERATIONAL_POSTURE.md`  
3. `10_RUNTIME_BOUNDARY_RULES.md`  
4. `README.md`  

Then paste lane declaration + path to one `OPERATIONAL-INDEX.md` Core Run row in the chat instructions.

---

## Lane-specific add-ons (repo — not this pack)

After minimum bundle, pull **from repository** into chat context when needed (paste excerpts or instruct Cursor — do not duplicate whole trees into Web-GPT):

| Lane / work | Repo surface |
|-------------|--------------|
| ORCA | `projects/orca/OPERATIONAL-INDEX.md` |
| Website Factory | `projects/mars-website-factory/OPERATIONAL-INDEX.md` |
| OCPilot | `projects/ocpilot/OPERATIONAL-INDEX.md` |
| WPilot | `projects/wpilot/README.md` |
| MIG | `projects/mig/OPERATIONAL-INDEX.md` |
| MetaBOT | `projects/metabot-seo-content-agent/README.md` |
| HomeGateway | `projects/homegateway-v4-ai/OPERATIONAL-INDEX.md` |
| Governance maintenance | Targeted `governance/*.md` only with charter |

---

## Replacing prior Web-GPT project sources

| Remove from Web-GPT project | Replace with |
|---------------------------|--------------|
| `mars-v2-final/*` (all) | Steps 1–11 above |
| `mars-v2/*` | *(duplicate — remove)* |
| `01_system.md` … `14_roadmap.md` | *(legacy — remove unless archival)* |
| `chat-migration/*` as SoT | One-time paste only — not standing sources |

---

*Index v1 — MARS Web-GPT Source Pack Update — Stable Baseline 2026-06.*
