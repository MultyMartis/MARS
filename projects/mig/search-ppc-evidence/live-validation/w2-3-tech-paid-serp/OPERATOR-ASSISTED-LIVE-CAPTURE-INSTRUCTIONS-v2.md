# Operator-Assisted Live Capture Instructions v2

**Project:** `MIG-W2-3-TECH-PAID-SERP`  
**Wave:** 2.3 — Genuine Live Paid SERP Closure  
**Authority:** `TECHNICAL TEST — NOT CLIENT PRODUCTION EVIDENCE`

## When to capture

- **Timezone:** Europe/Moscow  
- **Window:** Monday–Friday, 09:00–21:00 local  
- **Device:** Desktop browser (Chrome or Edge recommended)  
- **Region:** Москва (lr=213) — verify in Yandex UI before capture

Do **not** capture outside the approved window.

## What you do (5 steps only)

### Step 1 — Open browser

Use your normal browser (not automated tooling). Confirm region **Москва**.

### Step 2 — Open prepared search URL

Primary recommended query (highest priority for closure):

```text
https://yandex.ru/search/?text=ремонт%20квартир%20под%20ключ&lr=213
```

Alternate queries (optional second capture):

| Query ID | URL |
|----------|-----|
| w2-3-q03 | `https://yandex.ru/search/?text=доставка%20суши&lr=213` |
| w2-3-q01 | `https://yandex.ru/search/?text=установка%20кондиционера%20цена&lr=213` |

### Step 3 — Confirm paid ads visible

Ensure the page shows Yandex advertising blocks (marked as реклама / sponsored).  
If CAPTCHA appears — **stop**. Do not solve via third-party services. Save screenshot only and note CAPTCHA in folder.

### Step 4 — Run DevTools snippet

1. Open DevTools (F12) → Console  
2. Paste contents of:  
   `projects/mig/search-ppc-evidence/runtime/tools/assisted-capture-snippet.js`  
3. Press Enter — snippet downloads `capture-bundle.json` metadata

### Step 5 — Save bundle files

Copy into prepared folder:

```text
C:\AI MARS STORAGE\incoming\mig\live-validation\w2-3-tech-paid-serp\assisted-capture-pending\w2-3-q02\
```

Required files:

| File | How |
|------|-----|
| `screenshot.png` | Full-page screenshot (Win+Shift+S or browser extension) |
| `page.html` | DevTools → Elements → right-click `<html>` → Copy → Copy outerHTML → save as `page.html` |
| `capture-manifest.json` | Edit template in folder — set `captured_at` (ISO UTC), `page_url`, `device_browser`, `project_id`: `MIG-W2-3-TECH-PAID-SERP`, `operator_attestation.attested`: `true` |

Finalize checksums:

```powershell
cd "C:\AI MARS"
node projects/mig/search-ppc-evidence/runtime/cli/prepare-assisted-capture-bundle.mjs --finalize --bundle "C:/AI MARS STORAGE/incoming/mig/live-validation/w2-3-tech-paid-serp/assisted-capture-pending/w2-3-q02"
```

## Import (operator or Cursor after bundle exists)

```powershell
node projects/mig/search-ppc-evidence/runtime/cli/mig-evidence.mjs paid-serp:import-assisted `
  --manifest projects/mig/search-ppc-evidence/live-validation/w2-3-tech-paid-serp/project-ppc-state-manifest-v1.json `
  --bundle "C:/AI MARS STORAGE/incoming/mig/live-validation/w2-3-tech-paid-serp/assisted-capture-pending/w2-3-q02" `
  --session projects/mig/search-ppc-evidence/live-validation/w2-3-tech-paid-serp/session-config-v1.json `
  --queries projects/mig/search-ppc-evidence/live-validation/w2-3-tech-paid-serp/query-set-v1.json
```

## What you must NOT do

- Do not retype ad headlines, domains, or advertiser names into spreadsheets  
- Do not classify organic vs paid manually — parser handles this from HTML  
- Do not use CAPTCHA-solving services, proxies, or stealth extensions  
- Do not use Corvonero queries or client project manifests

## Minimum closure target

```text
1 genuine live SERP page
2 genuine paid ad observations
1 validated advertiser entity
1 bounded landing resolution
```

## Automated attempt note (2026-06-23)

Mode A session `w2-3-live-session-001` stopped on CAPTCHA for query `w2-3-q01`.  
Evidence preserved at:  
`C:\AI MARS STORAGE\incoming\mig\live-validation\w2-3-tech-paid-serp\session-001\`
