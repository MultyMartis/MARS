# MARS Website Factory — Validation runtime boundary v0

**Status:** **documentation only** — **honesty boundary** for the Validation Runtime Model v0 pack. Read together with [validation-runtime-overview-v0.md](validation-runtime-overview-v0.md) and [`../../AGENTS.md`](../../AGENTS.md).

**Version:** v0.

---

## 1. What this layer is

**Operational discipline in prose:** shared vocabulary for evidence, verdicts, waivers, escalations, lifecycle tokens, and consistency — so humans and future contracts **do not** talk past each other.

**Phase 1** for this layer means: **documentation and prompt alignment only**.

---

## 2. This layer DOES NOT provide

| Not provided | Clarification |
|--------------|----------------|
| **Runtime validator engine** | No in-repo service that validates factory artifacts automatically |
| **CI integration** | No GitHub Actions / pipeline spec claimed by this model |
| **Background validation** | No daemon, no worker pool, no scheduled scans |
| **Deployment checks** | No release automation or environment verification |
| **Lighthouse automation** | Explicitly out of v0 evidence unless org adds tools — **SAFE UNKNOWN** per [qa-validation-model.md](qa-validation-model.md) |
| **Crawling engine** | No site crawl bot |
| **Autonomous enforcement** | No auto-block, auto-merge, or auto-ship |
| **Graph database** | Semantic “graph” is **conceptual documentation** only |
| **Artifact persistence** | No storage of envelopes, QA payloads, or validation results implied |

---

## 3. Relationship to other “runtime” words in MARS

- MARS **Stage 13/14** documents may use “runtime” for **future** execution posture — **orthogonal** unless evidence shows code.
- **Execution Semantics Layer v0** prepares **lifecycle vocabulary** — still **not** an engine.
- **Artifact Bus Layer v0** is **not** a message bus — same honesty pattern applies here: **Validation Runtime Model** uses “runtime” only as **conceptual process model**, not software runtime.

---

## 4. SAFE UNKNOWN (boundary-specific)

- Whether any organization implements ticketing fields for waivers, evidence, or lifecycle tokens — **unknown** at MARS repo level.
- Whether Validator and specialist QA are separate prompts, one prompt, or human-only — **implementation TBD** per [qa-validation-model.md](qa-validation-model.md).

---

*Last updated: 2026-05-12.*
