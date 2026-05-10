# Integration boundary — MetaBOT vs MARS

**Normative** for how this repository may reference MetaBOT — SEO Content Agent.

---

## 1. MARS is not the runtime owner

- **MARS** (this repo’s documented architecture) **does not** own execution of MetaBOT workflows.
- **No** claim is made that MARS control plane, execution bridge, or in-repo runtime **dispatches** MetaBOT tasks unless future work explicitly implements that and evidence exists in-repo.

**SAFE UNKNOWN:** Future bridging patterns (webhooks from n8n to MARS, or the reverse) are **not** specified in workflow JSON or runtime code **in this repository** as of this documentation pack.

---

## 2. n8n is the execution runtime

- **n8n** hosts the **Intake**, **Worker**, and **Admin** workflows (names used operationally).
- Graph structure, scheduling, error branches, retries, and credential scopes are **n8n’s responsibility**.
- **Worker v13 stable** is the referenced production line for worker behavior; exact version pinning and deployment topology are **SAFE UNKNOWN** from this repo.

---

## 3. MARS is the orchestration *knowledge* layer (here)

Inside **`D:\AI MARS`**, MARS’s role is to hold:

- **Architecture narrative** — multi-workflow mental model, lifecycle, locks, QA.
- **Contracts at documentation level** — command vocabulary, state names, integration *posture* (not live endpoints).
- **Maps and registries** — `project-registry` row, capability cross-references, pointers to this pack.

This supports **humans and future MARS tooling** without pretending the repo **runs** the bot.

---

## 4. Credentials stay inside n8n (and chat providers)

- **OpenRouter** keys, **Telegram** bot tokens, **Google** service accounts or OAuth for Sheets — **must not** be committed here.
- MARS documentation may list **integration types** (e.g. “Sheets API”) but **not** secrets, URLs with embedded tokens, or private spreadsheet IDs unless the project explicitly chooses to publish non-secret identifiers elsewhere.

---

## 5. Sanitized exports only

What may live in MARS over time:

- **Redacted** workflow maps (this pack).
- **Field-level** data schemas described in prose (not necessarily machine JSON Schema).
- **Bridge** or **contract** snippets that contain **no** secrets (e.g. shape of a webhook payload — **SAFE UNKNOWN** until published as a formal contract).

What must **not** be treated as authoritative execution truth without verification:

- Paraphrases of n8n graphs **without** export from the live editor.
- Assumed node order or error handling **not** confirmed in operations.

---

## 6. Classification reminder

MetaBOT — SEO Content Agent is an **external multi-workflow AI system**, **not** a “simple tool” entry in the MARS tool registry. Any future `tools/registry.md` row must preserve that distinction (or link here) to avoid **architecture drift** toward “single webhook” misconceptions.

---

## 7. MARS posture (canonical integration knowledge)

- **MARS must treat** MetaBOT — SEO Content Agent as an **external multi-workflow AI system** (Intake, Worker, Admin, and future File Export — as documented in this pack), **not** as a single interchangeable “tool” node in MARS diagrams or registries.
- **MARS must not reduce** it to a simple tool shorthand: internal **n8n** orchestration, branching, locks, and Sheets-backed state remain **owned by the MetaBOT system** and live **outside** MARS core runtime ownership.
- **Runtime adapters** in this repository (when present) may call **one stable entrypoint** (e.g. a webhook) for experiments or tests; that **does not** make MARS the owner of MetaBOT’s **internal** workflow graphs, credentials, or multi-workflow semantics.
- **Authoritative execution truth** is always the **live n8n** configuration; this repository holds **sanitized** maps, contracts, and bridge notes only — **not** a claim of complete live integration or parity.

---

*See also [README.md](README.md) and [workflow-map.md](workflow-map.md).*
