# Manual SERP Capture Checklist — Pilot #1

**Market:** Грузотакси · **Region:** Краснодар · **Project:** Триумф  
**Primary query (MVP):** `грузотакси Краснодар`

---

## 1. Environment setup

| Step | Action |
|------|--------|
| Search engine | **Yandex** — https://yandex.ru/search/ |
| Region | Set Yandex region to **Краснодар** (city-level, not only krai) |
| Device mode | **Mobile** — real phone preferred; otherwise DevTools mobile emulation (document which) |
| Language | Russian (`ru`) |
| Logged-in state | Record whether Yandex account is signed in (affects personalization) |
| Incognito / clean | Prefer clean session or note personalization risk in `safe_unknown` |

---

## 2. Execute search

1. Enter primary query: **грузотакси Краснодар**
2. Wait for full SERP render (maps block, ads, organic).
3. Do **not** click through to competitors during capture (separate website pass handles URLs).
4. Record **UTC timestamp** at moment of observation.

---

## 3. What to record

### Required observations

| Category | Record |
|----------|--------|
| Query string | Exact query typed |
| Engine / region / city / device | Match Research Request `scope` |
| SERP type | e.g. `local commercial`, `mixed`, `informational` |
| Ads | `ads_blocks.top_count`, `bottom_count`, `visible_patterns[]` (text patterns only) |
| Maps / local pack | `maps_local_pack`: `dominant` \| `present` \| `absent` \| `unknown` |
| Aggregators | Names visible on SERP (2GIS, Яндекс Услуги, Profi, etc.) |
| Marketplaces | Avito, Youla, etc. if visible |
| Organic results | Top **10** (or all visible): `position`, `title`, `url`, optional `snippet` |
| Review signals | Map ratings, review counts visible on SERP (text note) |
| Offer / CTA patterns | Visible price cues, phone CTAs, "заказать", "от N ₽" — pattern strings only |

### Required evidence files

Store under pilot evidence folder (operator choice, suggested path):

```text
incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-<YYYYMMDD>/
```

| Artifact | Required | Format |
|----------|----------|--------|
| Full SERP screenshot | **Yes** | PNG — include URL bar showing query + region if possible |
| Mobile viewport screenshot | **Yes** | Same SERP, full scroll stitched or key viewport |
| Organic block screenshot | **Yes** | If not clear in full-page shot |
| Maps / local pack screenshot | **Yes** if present | Mark `absent` in JSON if not shown |
| Top ads screenshot | **Yes** if ads present | Count in JSON must match screenshot |
| `capture-notes.md` | **Yes** | Device, browser, region setting steps, anomalies |

### Required URLs (in `organic_results`)

- Copy **exact** URLs from SERP (no guessing, no shortened redirects unless that is what SERP shows).
- Include aggregator and marketplace URLs if they rank organically.
- Position numbering starts at **1** for first organic below ads/maps as operator sees it — document ambiguity in `safe_unknown`.

---

## 4. What NOT to record

| Do not | Reason |
|--------|--------|
| Invent competitor names or URLs | MIG discovers from real SERP only |
| Paste LLM-generated SERP JSON | Violates groundtruth discipline |
| Record full page HTML of landings | Website pass handles fetch |
| Record Wordstat / keyword volumes | `keyword_pass` is off for this pilot |
| Record semantic clusters or campaign structure | ORCA domain |
| Include credentials or personal data | Security |

---

## 5. Build `manual_serp` JSON

1. Use structure from [test-payload-manual-serp-v0.1.json](../../../../projects/mig/test/test-payload-manual-serp-v0.1.json).
2. Set `query` to primary query.
3. Populate `organic_results` from recorded URLs only.
4. Add every gap to `safe_unknown[]` (e.g. `"exact ad positions not verified"`, `"personalization unknown"`).
5. Validate JSON parses cleanly before inserting into Research Request.

---

## 6. Insert into Research Request

1. Open [request-triumph-gruzotaxi-krasnodar-v1.json](request-triumph-gruzotaxi-krasnodar-v1.json).
2. Confirm `request_type` is `groundtruth_run` (unchanged).
3. Add top-level `"manual_serp": { ... }` object.
4. Save copy as inbox file: `incoming/mig/requests/request-triumph-gruzotaxi-krasnodar-v1.json`.
5. Keep evidence screenshots **outside** the JSON file (paths in `capture-notes.md`).

---

## 7. Pre-flight verification

- [ ] Region confirmed Краснодар on Yandex
- [ ] Mobile mode confirmed
- [ ] Screenshot set saved
- [ ] `manual_serp.organic_results` matches screenshots
- [ ] `safe_unknown` lists all unverified items
- [ ] No fabricated entries
