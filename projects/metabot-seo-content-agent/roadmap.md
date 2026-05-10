# Roadmap — MetaBOT SEO Content Agent

Documentation-only planning buckets. **No** implementation commitment in MARS repo.

---

## Near-term stabilization

- Fix or mitigate **`/get`** non-responses (timeouts, error visibility).
- Align **`seo_active_jobs`** terminal state with **lock** lifecycle after `/run`.
- Reduce **`/health`** Sheets chatter or add backoff / caching to avoid quota errors.

---

## Production hardening

- Stronger **strict QA** prompts and checks without adding **niche-only validators**.
- Expand **cleanup rewrite** coverage where it helps universal editorial quality.
- Operational runbooks for **stuck pending** rows and **lock** cleanup — [admin-operations.md](admin-operations.md).

---

## Future multi-workflow orchestration

- Clarify **Intake → Worker → Admin** contracts in **sanitized** maps (still **no** secrets in MARS).
- Optional: formal **event** or **task id** correlation across workflows — **SAFE UNKNOWN** design.

---

## Future file export workflow

- **File Export Workflow** (artifacts to drive, CMS, or handoff packages) — **planned**; not evidenced in-repo.
- Attachment point likely **post-Worker** — [workflow-map.md](workflow-map.md).

---

## Future MARS integration

- If MARS later **orchestrates** or **observes** MetaBOT, respect [integration-boundary.md](integration-boundary.md): credentials in n8n; MARS holds **knowledge** and possibly **sanitized** telemetry contracts only.
- **SAFE UNKNOWN:** webhook shapes, auth, and whether MetaBOT remains primary SoT for task state.

---

*See [known-issues.md](known-issues.md), [lessons-learned.md](lessons-learned.md).*
