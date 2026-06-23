# ORCA Live Semantic Model — Wave 3.1

**Status:** `IMPLEMENTED — OPERATOR REVIEW REQUIRED` (uncommitted)  
**Locus:** `projects/orca/semantic-intelligence/live-model/`

Wave 3.1 integrates a provider-neutral live semantic model adapter with blind primary assessment, independent reassessment, model-aware adjudication, D3 quality evaluation, and bounded calibration.

Wave 3 core (`../production/`) remains the deterministic enforcement pipeline. Live model execution is validated here — not in Wave 3 core.

## Entry points

```bash
node tests/run-wave31-bypass-audit.mjs
node tests/run-blind-evaluation.mjs
node tests/run-full-corpus-readiness.mjs
node evaluation/build-evaluation-corpus.mjs
```

## Environment (operator-supplied, not in Git)

| Variable | Purpose |
|----------|---------|
| `OPENAI_API_KEY` | OpenAI-compatible primary provider |
| `OPENROUTER_API_KEY` | OpenRouter gateway (OpenAI-compatible) |
| `ORCA_SEMANTIC_MODEL` | Model identifier override |
| `ORCA_SEMANTIC_PROVIDER` | `openai` \| `openrouter` |

Without credentials: pipeline reports `BLOCKED — PRODUCTION SEMANTIC MODEL UNAVAILABLE`.

## Maturity

Live model validation requires operator-supplied credentials and D3 gate review. Do not claim Wave 3 operational until operator quality approval.
