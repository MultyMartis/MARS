# Semantic Assessment Prompt Contract v1

**Version:** `orca-semantic-assessment-prompt-v1`  
**Status:** `IMPLEMENTED — Wave 3.1`

## Principles

1. **Topical relevance is not commercial intent** — keyword overlap with business scope must not drive ACCEPT.
2. **Next-action judgement** — assess what the user is likely trying to do next.
3. **Provider vs career** — hiring a provider ≠ seeking employment as provider.
4. **Order vs learn** — paid service request ≠ education or DIY intent.
5. **Service vs product** — software/product search without hire signal is not commercial service demand.
6. **Problem vs information** — general informational queries without hire signal → REJECT or ABSTAIN.
7. **ABSTAIN for real ambiguity** — do not force decisions on insufficient evidence.
8. **No hallucinated services** — only approved service registry entries may be referenced.
9. **Business scope obedience** — queries outside scope → REJECT or ABSTAIN.
10. **Blind assessment** — no expected labels, deterministic outcomes, P0-I, legacy ORCA, or adjudicator results in primary input.

## Excluded from model context

- Unrelated project data
- Secrets and credentials
- Prior expected labels
- Legacy decisions during blind primary assessment
- Full corpus metadata beyond phrase + scope + registry

## Machine reference

`contracts/prompt-contract.mjs` — `PROMPT_VERSION`, `buildSystemPrompt`, `buildUserPrompt`
