# ZPM SERP Workflow Recovery Audit — Corvonero session

**Session:** `mig-20260622-corv01`  
**Date:** 2026-06-22  
**Purpose:** Locate operator-referenced ZPM SERP workflow; select verified execution route for Corvonero R1.

## Search scope

| Locus | Result |
|-------|--------|
| `projects/website-factory/execution-cases/bzpm-market-intelligence/` | W3S SERP wave — **WebSearch synthesis only**; no Playwright scripts |
| `.recovery-temp/w3s-extract.txt` | States: «прямой автоматический парсинг Yandex заблокирован SmartCaptcha» |
| `projects/website-factory/execution-cases/bzpm-catalog-redesign/` | No SERP capture artefacts |
| `incoming/mig/pilots/` (ZPM/BZPM pilots) | **None** |
| `C:\AI MARS STORAGE\mig\` | Wordstat only (Corvonero); **no SERP capture tree** |
| `projects/ocpilot/sites/site-002/` | No SERP capture scripts |

## ZPM / BZPM SERP evidence (factual)

**SAFE UNKNOWN:** No executable Playwright SERP script, capture manifest, or Grade B PNG/HTML bundle tied to project ЗПМ (SITE-002 / BZPM MI) was found in-repo or MARS Storage.

**Documented BZPM W3S route (2026-06-14):** 20-query matrix; organic visibility via **systematic WebSearch synthesis** + operator dedup — **not** browser-rendered Yandex capture.

## Recoverable verified browser SERP workflow

The only in-repo **successful** Yandex mobile Playwright SERP with artefact proof:

| Field | Value |
|-------|-------|
| Script | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-multi-20260604/capture-serp-multi.mjs` |
| Single-query variant | `.../serp-20260604/capture-serp.mjs` |
| Proof | `captures/q01/capture-raw.json` — `has_captcha: false`, 35 items; `capture-notes.md` — 8/11 queries captured |
| Delay | `CAPTURE_DELAY_MS` default **55000**; notes recommend **60–90s** between batch queries |
| Browser | **Fresh Chromium launch per query attempt** (close after each) |
| Headless | Triumph used `headless: true` |
| Device | iPhone 13 emulation, `ru-RU`, touch |
| URL | `https://yandex.ru/search/touch/?text=...&lr=...` |
| Wait | `domcontentloaded` + **4500ms** post-load |
| CAPTCHA | Detect only — no bypass |

## Corvonero failed routes (preserved)

| Route | Failure ID | Root difference from Triumph |
|-------|------------|------------------------------|
| Direct HTTP fetch | af-004 | No browser; Yandex anti-bot |
| `tools/capture-serp-r1.mjs` | af-008 | **Reused single browser context** across 10 queries; headless; 45s delay |

## Selected route for this run

**Label:** `zpm-workflow-corv01` (ZPM-derived naming; **implementation source = Triumph multi-capture mechanics**)

Adapter: `tools/capture-serp-zpm-workflow.mjs`

Corvonero-specific changes only:

- Output: `evidence/serp/zpm-workflow-corv01/capture-run/captures/`
- Region: `lr=65` (Новосибирск)
- **Headful** default for operator-supervised run (`CAPTURE_HEADLESS=false`)
- **Fresh browser per query** (Triumph pattern restored)
- Delay: **55000ms** base + optional jitter (fallback 30–60s documented if env unset)
- Validation batch first; stop on CAPTCHA when `STOP_ON_CAPTCHA=1`

## Operator decision note

Operator asserted ZPM completed successful SERP without CAPTCHA. **Not provable from repository artefacts.** Triumph workflow is the evidence-backed browser route used for prior MIG pilots and referenced in Corvonero session docs as `triumph_pattern_ref`.
