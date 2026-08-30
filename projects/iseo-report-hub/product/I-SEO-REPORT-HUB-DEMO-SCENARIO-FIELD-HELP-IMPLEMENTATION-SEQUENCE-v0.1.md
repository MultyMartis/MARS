# I-SEO Report Hub — Demo Scenario + Field Help Implementation Sequence v0.1

**Status:** sequencing decision  
**Date:** 2026-08-21  
**Wave:** Pre-hosting Demo Scenario and Field Help Charter 01  
**Safety preference:** do **not** combine Field Help + DB seed into one wave unless operator explicitly confirms DB mutation in the same pass

---

## Recommended sequence (safest)

### 1. Field Help Question Icon Implementation 01 — **NEXT**

| | |
|--|--|
| **Type** | Render / UI only |
| **DB** | No |
| **Runtime sync** | Source → runtime for CSS/views/support only |
| **Delivers** | `?` icon, help panels, copy from Field Help Copy Pack on work entry / block / monthly forms |
| **Why first** | Improves specialist UX before demo fill; no backup risk; team sees how fields are meant to be used |

### 2. Demo User and Scenario Seed Charter 01

| | |
|--|--|
| **Type** | DB mutation charter |
| **Delivers** | Exact SQL/CLI steps, backup/rollback, entity IDs plan, hybrid seed vs UI boundary, acceptance |
| **Includes** | User `seo_specialist`, client/project/site `ПРОВЕРКА.рa`, periods July/August 2026 shells |

### 3. Demo User and Scenario Seed Implementation 01

| | |
|--|--|
| **Type** | Local DB mutation |
| **Requires** | Backup of `iseo_report_hub_dev` first |
| **Delivers** | Base entities only (or empty monthlies); preserve Demo Client report 1 / report 5 |
| **Forbids** | Host upload; PDF/export/share; printing hashes |

### 4. Browser Filled Demo Report Pass 01

| | |
|--|--|
| **Type** | UI content fill + evidence |
| **Browser** | Firefox Developer + `mars-research` profile |
| **Delivers** | Realistic July complete + August in-progress content; screenshots; issue log |
| **On UI bugs** | Capture + fix charter — do not silent-bypass |

### 5. Pre-hosting Deployment Readiness Charter 01

| | |
|--|--|
| **When** | After demo accepted by operator |
| **Delivers** | Host checklist for `reports.i-seo.su`, PHP 8.3, rewrite, writable dirs, env, rollback |
| **Still forbids** | Upload until **explicit** operator approval |

---

## Explicitly deferred

- Production file/DB upload to `reports.i-seo.su`
- PDF / export / share mutation
- Combining Wave A+B without operator confirmation
- Push to remote
- Password `test` on production

---

## Decision on combining A+B

**Default: split.**  
Field Help first, then seed charter, then seed impl, then browser fill.

Combine only if operator replies that DB mutation in the same implementation as Field Help is explicitly approved **and** backup is prepared in that same wave.

---

## Parallel track (unchanged)

Production Operator Decision / deployment readiness can be prepared in docs, but must not override the demo sequence or authorize upload early.
