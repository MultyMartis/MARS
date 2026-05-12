# Operational template — AI visibility / entity authority (v0)

**Status:** **documentation-only** pattern for how a site **represents authority**, **structured facts**, and **attribution** in an era of LLM-mediated discovery. **Not** SEO-for-LLMs snake oil.

**Normative references:** [semantic-object-model-v0.md](semantic-object-model-v0.md), [trust-semantics-v0.md](trust-semantics-v0.md), [seo-intent-model-v0.md](seo-intent-model-v0.md), [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md), [validation-evidence-model-v0.md](validation-evidence-model-v0.md).

---

## 1. Entity authority

| Question | Documentation action |
|----------|----------------------|
| What is the **canonical entity** (brand, product line, service)? | Name it in blueprint + semantic objects. |
| Who **owns** updates to that entity’s facts? | Lane + HITL per [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md). |
| What **supersedes** a prior claim? | Lineage per [artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md). |

---

## 2. Structured trust

- Prefer **human-readable** primary content; structured data (JSON-LD, etc.) is **secondary** to clear prose unless project explicitly scopes schema work.
- Any **FAQ / HowTo** schema must match **visible** on-page answers ([semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md)).

---

## 3. Source attribution

- **Citations** — primary sources, dates, retrieval context where relevant for B2B/regulated industries.
- **Third-party** claims (“studies show…”) — link or archive reference; else **SAFE UNKNOWN** / remove.

---

## 4. Citation semantics

- Distinguish **paraphrase** vs **direct quote** vs **summary statistic**.
- **Confidence** labels for inferred connections ([validation-evidence-model-v0.md](validation-evidence-model-v0.md)).

---

## 5. AI visibility boundaries (mandatory)

**Explicit non-guarantees:**

- **No guarantee** of inclusion in any LLM answer, overview, or assistant result.
- **No guarantee** of placement, sentiment, or persistence of any third-party model behavior.
- **No claim** of proprietary “AI SEO” algorithms in MARS doc scope.

This template only ensures **honest representation** and **consistent** facts across artifacts.

---

## 6. QA focus

- Drift between blueprint facts and frontend visible text ([cross-artifact-semantics-v0.md](cross-artifact-semantics-v0.md)).
- “Invisible” claims only in schema — **blocker** unless waived with HITL ([semantic-qa-rules-v0.md](semantic-qa-rules-v0.md)).

---

## 7. SAFE UNKNOWN

- How target LLMs **train** or **retrieve** on your domain — **unknown** and outside factory static-site scope.
- Whether future **MCP/tool** integrations will expose structured feeds — **unknown**.

---

*Template v0 — authority and attribution without LLM outcome promises.*
