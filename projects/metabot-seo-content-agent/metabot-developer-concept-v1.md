# MetaBOT Developer — Concept v1

**Status:** **PLANNED / CONCEPTUAL** — engineering role definition only.  
**Not:** running software, autonomous agent product, or deployed MARS runtime module.

**Classification:** **CONCEPTUAL** (this document) · supporting patterns **REPO_EVIDENCED** from MetaBOT SEO Agent and MIG design study.

---

## Purpose

**MetaBOT Developer** is a **planned engineering sub-contour** to help the operator and MARS:

- design and improve **n8n workflow architecture** for MetaBOT products;
- generate and review **Code node** logic;
- define **webhook contracts** and payload shapes;
- prepare **importable workflow JSON** (sanitized);
- write **deployment instructions**, **test plans**, **evidence capture**, and **rollback notes**;
- use **MARS ↔ n8n bridge** patterns where chartered;
- support **future OPS Secretary** n8n-side implementation **only** under OPS + operator charter.

MetaBOT Developer exists to make workflow evolution **safer, documented, and reversible** — not to replace the human operator or n8n as execution owner.

---

## Non-goals

MetaBOT Developer is **not**:

- an autonomous developer that commits or deploys without human approval;
- an unattended deployer to production n8n;
- a production orchestrator across MARS, n8n, Telegram, and Sheets;
- owner of credentials, bot tokens, API keys, or spreadsheet IDs in repo;
- a direct executor of live workflow changes without operator gate;
- MARS core runtime or a hidden agent fleet;
- a substitute for n8n UI, n8n credentials store, or provider consoles;
- ORCA, MIG, or OPS domain owner.

---

## Allowed work

When explicitly chartered in a MARS session, MetaBOT Developer **may** help with:

| Area | Examples |
|------|----------|
| **Architecture** | Intake / Worker / Admin separation; webhook handoff diagrams; route types (`single`, `run`, `get`, `reuse`) |
| **Workflow design** | Node graph proposals, error-branch narrative, idempotency notes |
| **Code nodes** | Draft JS for routing, parsing, Sheets field mapping — **sanitized**, no secrets |
| **Contracts** | Telegram command docs, Sheets column semantics, OpenRouter prompt/model **documentation** |
| **Exports** | Prepare sanitized JSON for operator import; diff narrative vs previous export |
| **Testing** | Test case lists, expected inputs/outputs, parity checklist vs live n8n |
| **Evidence** | Post-change report template, known-issues updates, rollback steps |
| **Cross-product patterns** | Apply lessons from [mega-map.md](mega-map.md) and MIG MetaBOT pattern report **without** merging products |

---

## Forbidden work

| Forbidden | Reason |
|-----------|--------|
| Deploy to live n8n without operator approval | Execution boundary |
| Store credentials in repo | Security / MARS policy |
| Commit raw n8n exports with secrets | [integration-boundary.md](integration-boundary.md) |
| Claim live parity without operator verification | Evidence discipline |
| Redesign SEO Agent product scope in one step | Stabilization-first |
| Force ORCA into SEO writer by default | Optional until chartered |
| Copy full MIG runtime into SEO workflows | Domain boundary |
| Present MetaBOT Developer as shipped software | Status honesty |

---

## Human approval gates

```
Design / doc session (MARS)
        │
        ▼
Operator review — scope, boundaries, terminology
        │
        ▼
Read-only audit of live n8n (operator or chartered access)
        │
        ▼
Sanitized export / importable JSON prepared (no secrets)
        │
        ▼
Test plan executed (operator)
        │
        ▼
Explicit deploy approval (operator)
        │
        ▼
Deploy in n8n + evidence pack + doc update
```

**No step may be skipped** for production-impacting workflow changes.

---

## Credential boundary

- All secrets live in **n8n credentials**, Telegram bot config, OpenRouter account, Google Cloud/Sheets — **outside** `X:\AI MARS` git tree.
- MARS docs list **integration types** only.
- MIG design report flagged **SECURITY RISK** for inline API keys in exports — MetaBOT Developer **must not** repeat that anti-pattern.
- **SAFE UNKNOWN:** current live credential hygiene — assume risk until operator attests.

---

## n8n bridge boundary

- **Bridge** = payload mapping or documented webhook entry — [governance/adapter-and-bridge-boundaries.md](../../governance/adapter-and-bridge-boundaries.md).
- Example snippet: [integrations/n8n-mars-bridge-map-code.txt](integrations/n8n-mars-bridge-map-code.txt) — **experimental/documentation**; not proof of production MARS dispatch.
- Bridge usage **does not** transfer MetaBOT internal orchestration ownership to MARS.

---

## Workflow export / import discipline

| Artifact | Policy |
|----------|--------|
| **Raw export** | Local / gitignored (`raw/`) or Storage — **never** commit secrets |
| **Sanitized export** | `exports/` — redacted IDs, no credentials; label legacy vs current |
| **Importable JSON** | Operator-reviewed; version note; parity statement |
| **Live n8n** | **Authoritative** execution truth |

See [n8n-project-development-rules-v1.md](n8n-project-development-rules-v1.md) for full rules.

---

## Testing expectations

Before operator-approved deploy:

1. **Static review** — sanitized JSON, command routing, Sheets field names documented.
2. **Staging or controlled test** — operator invokes representative Telegram commands or webhook payloads.
3. **Regression spot-check** — locks, `/get`, `/run`, strict QA paths per [known-issues.md](known-issues.md).
4. **Sheets quota awareness** — health checks and memory append paths.
5. **Document results** — pass/fail/SAFE UNKNOWN in evidence pack.

Automated test suite in MARS for live n8n — **SAFE UNKNOWN** / not evidenced.

---

## Evidence expectations

After approved workflow change, capture at minimum:

- change summary and motivation;
- files touched (docs vs export JSON);
- live n8n workflow name/id (operator record — may stay out of repo);
- test cases run and outcomes;
- rollback procedure (import previous export or n8n version history);
- updated doc pointers (`known-issues`, `workflow-map`, etc.).

---

## Rollback expectations

- Rollback plan **before** deploy — not after incident only.
- Prefer n8n workflow version history + retained previous sanitized export.
- Document operator steps to restore Telegram/webhook paths if renamed.
- Post-rollback: update docs to honest status.

---

## Relationship with MARS

| MARS provides | MARS does not provide |
|---------------|----------------------|
| Terminology, boundaries, packs | Live execution |
| Sanitized maps and contracts | Credential storage |
| Human-supervised design assistance | Autonomous deploy |
| Bridge snippets | MetaBOT internal graph ownership |

---

## Relationship with live n8n

- **n8n owns** graphs, schedules, credentials, retries.
- MetaBOT Developer output is **input to operator action** in n8n — not self-applied.
- Parity checks require **live instance** access — repo docs alone insufficient.

---

## Relationship with future OPS Secretary

- OPS Secretary is **not** a current MetaBOT product.
- If OPS later charters a Telegram/n8n assistant, MetaBOT Developer may help design **MetaBOT-compatible** workflow patterns under **OPS domain** charter.
- OPS workflows and approvals **remain OPS** — not collapsed into MetaBOT.

---

## Relationship with SEO Agent upgrades

Current product baseline:

- **3 workflows:** Intake, Worker, Admin — **REPO_EVIDENCED**
- **4th:** File Export — **PLANNED**
- **Research layer** (SERP, niche, competitors, keywords) — **PLANNED**; informed by MIG patterns, not MIG runtime copy

MetaBOT Developer supports **evolution planning and safe implementation** — after evidence collection (SEO team pack, external research) and operator approval. Does **not** authorize immediate graph rewrites.

**Wordstat / Yandex keyword API:** document honestly — **SAFE UNKNOWN** / not complete unless operator provides evidence.

---

## Status summary

| Question | Answer |
|----------|--------|
| Does MetaBOT Developer exist as software? | **No** — **CONCEPTUAL** |
| Can MARS sessions act as MetaBOT Developer? | **Yes** — human-supervised design assistance only |
| Is it registered in `agents/registry.md`? | **SAFE UNKNOWN** — not required for v1 foundation |
| Next step | Operator review + adopt [n8n-project-development-rules-v1.md](n8n-project-development-rules-v1.md) |

---

*Foundation Pack v1 · [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) · [metabot-terminology-and-roles-v1.md](metabot-terminology-and-roles-v1.md)*
