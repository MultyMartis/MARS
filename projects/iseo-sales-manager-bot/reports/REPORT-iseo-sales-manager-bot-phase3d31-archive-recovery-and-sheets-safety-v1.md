# REPORT — ISEO SALES MANAGER BOT PHASE 3D.3.1 ARCHIVE RECOVERY AND SHEETS VALUE SAFETY

**Verdict:** PHASE 3D.3.1 COMPLETE — ARCHIVE RECOVERY ACCEPTED  
**Secondary:** COMPLETE — ARCHIVE FIXED, HISTORICAL CONTACT DAMAGE PRESERVED  

**Date:** 2026-08-01  
**Locus:** `projects/iseo-sales-manager-bot/`  
**Evidence:** `evidence/phase3d31/`

---

## 1. Archive root cause

`Recent Leads` correctly emitted N archive cards (+ notice), but **`Capture Admin Reply` collapsed to `$input.first()`**, so `Safe Telegram Reply` sent only «📁 Архивная карточка 1 из N». The same newest lead therefore appeared for every `/leads` command.

## 2. Argument parsing

Exact tokens only: `/leads`→5; `/leads 3|5|10`; reject `7`, `03`, trailing garbage; `10` never truncated to `1`. Route uses Switch **equals** on `/leads`. Invalid text:

```
⚠️ Укажите количество: 3, 5 или 10.
Например: /leads 5
```

## 3. Unique lead selection

Bounded CLEAN read (`A1:ZZ250` + code scan cap 250). Exclude synthetic + technical-retry-only. Identity: `lead_id` → Gmail message id → deterministic fallback (not phone/site alone). Prefer newest valid CLEAN state per key. Return `min(requested, available_unique)` newest first.

## 4. Multi-card send

Capture passthrough `$input.all()`. Live: `/leads 3` → 3 cards / 4 Telegram items; `/leads 5` → 5/6; `/leads 10` → 5 available / 6 items; ordinals 1..N unique.

## 5. Formula error origin

CLEAN `phone` cells stored under default Sheets **USER_ENTERED**; leading `+` evaluated as formula → `#ERROR! (Formula parse error.)`. Not a wrong column mapping. Historical cells preserved.

## 6. Phone write safety

Operational.dev Append CLEAN + Append RAW: `options.cellFormat=RAW`. New plus-prefixed phones store as text. Formatters suppress invalid contacts.

## 7. Live command results

| Command | Result |
|---------|--------|
| `/leads 3` | PASS — 3 distinct cards |
| `/leads 5` | PASS — 5 distinct cards |
| `/leads 10` | PASS — 5 available (honest), ordinals 1..5 |
| `/leads 7` | PASS — invalid warning |
| Formula as phone | PASS — suppressed / corrupt warning |
| Lifecycle buttons on archive | none |
| AI calls | **0** |
| Client messages | **0** |
| New workflows | **0** |

## 8. Workflow final states

| Workflow | active | nodes |
|----------|--------|-------|
| Sales-Manager-v2 (`h8I2Tl2yl4uzhUnB`) | false | — |
| Operational.dev (`xSnXPy8cEHoZw6xG`) | true | 36 |
| Admin.dev (`wLrLp4WQHm1VJmxz`) | true | 42 |

Sole Gmail intake: **1**. AI OFF. parser `sm-parser-v3.1`. messages `sm-msg-v2`. Callback lifecycle unchanged.

## 9. Harness

Local Phase 3D.3.1 harness: **29/29 PASS** (Storage incoming; not committed).

## 10. Git

Commit: `03a52547e206c38907781fc05c161d98c318031f` — `fix(iseo-sales-manager-bot): repair archive lead recovery`  
Push: `origin/mars/canonical-post-recovery` @ `03a52547` (no force).

---

**STOP.** AI remains OFF. Sales-Manager-v2 remains inactive. No Olya Admin enrollment. No automatic client messaging.
