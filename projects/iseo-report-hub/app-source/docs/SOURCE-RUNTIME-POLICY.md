# Source / Runtime Policy (runtime copy)

**Status:** documentation only  
**Authority:** Active Brain `I-SEO-REPORT-HUB-SOURCE-RUNTIME-POLICY-v0.1.md`  
**Location note:** This file lives under Localhost runtime and is **outside** the MARS Git monorepo. It is **not** committed by Active Brain Git.

---

## Split

| Layer | Path | Role |
|-------|------|------|
| Active Brain | `X:\AI MARS\projects\iseo-report-hub\` | Committed docs / specs / decisions |
| Runtime | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` | Local runnable app workspace |

- This runtime workspace is **not** a separate Git repository.
- Do **not** run `git init` here.
- Runtime files are **not** versioned by normal Active Brain commits.
- Source preservation (recommended: Model A — `app-source/` mirror + sync to runtime) needs a **separate charter** before Phase 1.

## Never put in versioned source

- `.env`, `.env.local`
- uploads, logs, cache
- real credentials / DB dumps with real data
- unsanitized private client metrics

## Phase 0

Scaffold only. No DB. No vhost/hosts by Phase 0. No secrets.
