# SEO Content Agent — Model routing

**Status:** **plan** — strategy for OpenRouter. **No** live router exists in this repo. Actual model IDs change; verify in OpenRouter catalog before implementation.

**Gateway (fact):** OpenRouter is the intended **single** API surface for LLM calls (**plan** — org may add direct providers later; **SAFE UNKNOWN**).

---

## Role-based model families

| Role | Model family (intent) | Typical steps |
|------|------------------------|---------------|
| **Analytics / extraction** | **Gemini-like** (fast multimodal reasoning, long context) — *if available and allowed* | Parse Telegram Task, Analyze Brief, Analyze Sources (summaries) |
| **Creative drafting** | **GPT-like** (fluent commercial copy) | Write SEO Text (first draft), outline bullet expansion |
| **Accuracy / consolidation** | **Claude-like** (careful, lower hallucination pressure in many workloads) | Fact Check, SEO QA, Rewrite With Fixes, final outline tightening |

**SAFE UNKNOWN:** Exact model slugs, regional availability, and enterprise terms at implementation time.

---

## OpenRouter usage (plan)

- One **HTTP** (or n8n OpenRouter node) call per step unless batched by design.
- Pass **model** parameter per step from a **routing table** maintained outside repo (n8n env or credentials — **no secrets here**).
- Log **model id**, **latency**, and **token counts** for cost review (**align** with MARS `models/cost-token-budget-v0.md` concepts where useful).

---

## Fallback

**Plan:**

1. Primary model for the step fails (timeout, 5xx, context length) → retry once with **reduced max_tokens** if applicable.
2. Retry on **fallback model** of the **same family** if configured; else step down: Claude-like → GPT-like for QA-only steps (**policy TBD**).
3. If all fail → return user-visible error; persist failure reason in run log (**SAFE UNKNOWN:** storage).

**Fact:** Fallback chains must be tested per environment; this doc does not certify behavior.

---

## Temperature recommendations (plan)

| Step type | Temperature (starting point) | Note |
|-----------|------------------------------|------|
| Parse / normalize | `0.0` – `0.2` | Deterministic JSON |
| Brief / source analysis | `0.1` – `0.3` | Favor fidelity over creativity |
| Build outline | `0.3` – `0.5` | Some variation acceptable |
| Write SEO text | `0.5` – `0.7` | Commercial fluency; cap if brand voice drifts |
| Fact check | `0.0` – `0.2` | Conservative |
| SEO QA | `0.1` – `0.3` | Consistent rubric |
| Rewrite with fixes | `0.2` – `0.4` | Apply edits without rewriting whole piece creatively |

**SAFE UNKNOWN:** Per-model optimal settings; run small golden-set evals before production.

---

## Context and cost

- Long articles + many sources may require **truncation** or **map-reduce** sub-workflows (**planned** — not specified here).
- **SAFE UNKNOWN:** Hard token ceilings per org budget.

---

## Honesty

This routing document is **guidance only**. It does **not** mean models are integrated, tested, or approved for your tenant.
