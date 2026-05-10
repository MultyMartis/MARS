# Lessons learned — MetaBOT SEO Content Agent

Operational and design lessons from running a **multi-workflow** external AI system. **Not** a post-mortem for a single incident.

---

## Multi-workflow systems are not simple tools

- A **Telegram bot** surface hides **Intake**, **Worker**, and **Admin** graphs. Documentation and onboarding must say **multi-workflow** explicitly or newcomers assume “one webhook = one tool”.
- MARS should **classify** MetaBOT as an **external multi-workflow AI system** in registries/maps to prevent **architecture drift** toward undersized mental models.

---

## AI quality problems

- **Strict** layers and **cleanup rewrite** reduce but do not eliminate generic phrases (*order now*, *professional*, *improvement*, *helps*, *affects*, *visibility*).
- **Universal senior SEO editor** framing scales better than many **niche validators**.

---

## Lock system problems

- **Locks** can agree with user-visible state while **`seo_active_jobs` still says pending** — operators must reconcile multiple sources of truth.
- **Lock cleanup** is essential; without it, UX collapses into “bot stuck”.

---

## Telegram UX lessons

- Silent failures (**`/get`**) read as “broken bot”; need timeouts, error messages, or fallback prompts — **SAFE UNKNOWN** when fixed.
- Users need explicit guidance: **strict QA is not inherited** unless they run canonical `/seoqa --strict` / `/factcheck --strict`.

---

## Google Sheets limitations

- **Rate limits** bite **health checks** and any chatty polling — design for **backoff** and **minimal reads**.
- Sheets are **not** a transactional database; job rows and locks can **diverge**.

---

## Cleanup rewrite importance

- A dedicated **rewrite** pass after `/text` catches boilerplate that **QA** might not flag if QA is run rarely or without `--strict`.

---

## Architecture drift risks

- Treating MetaBOT as a **MARS adapter** or **single tool** mis-allocates ownership: **n8n** runs it; MARS may only **document** or **integrate** later under explicit contracts — [integration-boundary.md](integration-boundary.md).

---

## SAFE UNKNOWN importance

- When workflow JSON and credentials are **out of repo**, honest **SAFE UNKNOWN** markers prevent **hallucinated** node graphs and fake integration paths.
- Prefer **explicit assumptions** (“mechanism unknown until export”) over fabricated certainty.

---

*See [roadmap.md](roadmap.md), [known-issues.md](known-issues.md).*
