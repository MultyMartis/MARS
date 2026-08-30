# i-SEO Report Hub — Local Roadmap After Host Demo v0.1

**Дата:** 2026-08-24  
**Контекст:** host demo выложен вручную; возврат к локальной разработке  
**Status source:** [I-SEO-REPORT-HUB-FULL-LOCAL-SYSTEM-STATUS-v0.1.md](I-SEO-REPORT-HUB-FULL-LOCAL-SYSTEM-STATUS-v0.1.md)

Не implementation plan с кодом — практический порядок следующих волн.

---

## Phase A — Stabilize local/host baseline

1. Full Local System Status Audit 01 — **this wave (done)**.
2. Add source `public/.htaccess` + minimal deployment package hygiene (Pre-hosting Readiness Fix / equivalent).
3. **Production Config Normalization 01** — charter then implementation: `.env.local` contract, production defaults, session/HTTPS notes, no local-only web guards.

**Exit:** source deployable without manual rewrite guesswork; config story clear for host vs local.

---

## Phase B — Product MVP polish

1. **Browser Filled Demo Report Pass 01** — real browser fill of August / in-progress path.
2. **SEO Team Feedback Fix 01** — only after actionable notes exist.
3. Work entry / report block editing UX polish from real use.
4. Honest empty states / disabled CTAs for PDF/share while parked.

**Exit:** demo usable for internal SEO training without broken file/export expectations.

---

## Phase C — Real usage readiness

1. Replace/disable weak demo passwords for any reachable host.
2. Real users/roles (or admin seed flow).
3. Real client/project creation flow (or controlled seed).
4. Backup/export instructions for operator.

**Exit:** not “demo-only” for daily specialist work.

---

## Phase D — PDF / share (optional for MVP)

1. Decide if MVP needs PDF/share now.
2. If yes: **Export Share PDF Readiness Charter 01** — architecture fit for shared hosting (no Windows Edge assumption).
3. HTML export alignment / PDF generation only after charter.

**Exit:** either consciously deferred, or hosting-safe delivery path.

---

## Phase E — Production operations

1. Deploy package/script (exact include/exclude).
2. DB migration/import procedure.
3. Backup/rollback.
4. Host smoke checklist (public + authenticated).

---

## Recommended next 3 prompts

1. **`I-SEO Report Hub — Pre-hosting Readiness Fix 01`**  
   Add `public/.htaccess` to source; document host rewrite; optional HTTPS/session notes; no PDF; no DB mutation; no host upload unless operator asks.

2. **`I-SEO Report Hub — Production Config Normalization 01`** (charter first if preferred)  
   Normalize production vs local env contract; keep CLI local DB guards; clean `.env.example`; no secrets in Git.

3. **`I-SEO Report Hub — Browser Filled Demo Report Pass 01`**  
   Browser-driven August / work-entry content pass on local; improve demo realism; still no PDF/share enablement.

If SEO team sends concrete notes before (1)–(3), insert **SEO Team Feedback Fix 01** immediately after triage.

---

## What not to do yet

- Do not enable PDF/export/share on host.
- Do not run local seed/migrate tools against host DB.
- Do not broad-sync entire runtime (including `tools/`, `.env.local`) to host.
- Do not push monorepo blindly (foreign WIP + unpushed history).
- Do not invent SEO feedback fixes without notes.
- Do not treat host as fully verified from this audit’s public GET alone.
- Do not start real-client production onboarding before Phase C password/users hygiene.
