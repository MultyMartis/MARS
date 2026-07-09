# i-SEO Report Hub — Product Charter v0.1

**Status:** APPROVED (operator persist 2026-07-10)  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Implementation:** **NOT STARTED**

---

## 1. Project background

i-SEO ведёт SEO-проекты для клиентов и регулярно готовит отчёты о проделанной работе и результатах. Сейчас отчётность фрагментирована: разные специалисты (Denis, Ilya и др.) используют разные форматы и уровни детализации. На i-seo.su уже работает WordPress и есть web commercial proposal generator для лидов — это создаёт естественную платформенную базу для internal reporting tool.

**i-SEO Report Hub** формализует единую операционную систему отчётности: от weekly checkpoints до monthly final report и controlled client web delivery.

---

## 2. Owner roles

| Role | Person / entity | Responsibility |
|------|-----------------|----------------|
| **Product architect / owner** | Андрей | Product direction, architecture, MARS documentation |
| **Business owner / vision** | Никита / i-SEO | Business requirements, reporting standards, client expectations |
| **Developer** | Антон | Future WordPress implementation |
| **SEO specialists** | i-SEO team | Data entry, commentary, evidence, draft reports |
| **Reviewer / lead** | TBD | Review and approval workflow (role model in architecture doc) |

---

## 3. Approved purpose

Internal i-SEO reporting workspace для:

- подготовки отчётов;
- управления reporting cycles;
- weekly checkpoints и monthly final reports;
- work log и evidence;
- metric snapshots и specialist commentary;
- review/approval workflow;
- publish/export и controlled client delivery.

**Strategic decision:** это **не** PDF generator. Финальный отчёт — structured rendered output всего reporting cycle.

---

## 4. Approved platform direction

**WordPress-based internal tool на существующем сайте i-seo.su.**

**Reason:** i-seo.su уже на WordPress; уже есть похожий web generator для commercial proposals. Report Hub добавляется как WordPress-based internal reporting admin/workspace + client web report renderer.

---

## 5. Approved reporting cycle

**Base period:** 1 month.

**Monthly cycle contains:**
- Week 1 — preliminary weekly report/checkpoint
- Week 2 — preliminary weekly report/checkpoint
- Week 3 — preliminary weekly report/checkpoint
- Week 4 / Month Close — final monthly report

Weekly checkpoints **≠** full monthly copies. Monthly final **≠** simple rollup of three weeklies without interpretation layer.

---

## 6. Corpus evidence

**Location:** `X:\AI MARS STORAGE\incoming\iseo-report-hub\`

**Known folders:**
- materials from Nikita
- reports from Denis
- reports from Ilya

**Known corpus (attested):**
- 33 files total
- 30 PDF reports (15 Denis, 15 Ilya)
- 3 Nikita materials

**Corpus conclusions (persisted, not re-audited):**

| Source | Pattern |
|--------|---------|
| **Denis reports** | More branded, client-document oriented |
| **Ilya reports** | More compact, Topvisor-link oriented |
| **Both** | Useful patterns; common core should standardize structure while preserving flexibility |
| **Nikita materials** | Work dictionary foundation |
| **Nikita XLSX Лист2** | Access/credential-related — **EXCLUDED** from product corpus, exports, AI prompts |

---

## 7. Deep research evidence summary

Prior operator review of source corpus (attested in charter persist task) established:

- Existing reports show **two viable stylistic lanes** (branded document vs compact metrics link).
- **Work dictionary** from Nikita materials is foundational for standardized "completed works" blocks.
- **Topvisor** appears as external online report link in Ilya-style reports — acceptable MVP pattern.
- **No single existing format** is sufficient alone; product must unify cycle, blocks, and approval without forcing one specialist's style exclusively.

Full corpus re-analysis is **deferred** to work dictionary extraction stage.

---

## 8. Product goals

1. Единый internal workspace для SEO-специалистов i-SEO.
2. Стандартизированный monthly reporting cycle с weekly checkpoints.
3. Block-based report composition с work dictionary.
4. Manual metric entry + evidence attachments + external links (Topvisor MVP).
5. Review/approval before client-facing publication.
6. Client web report as primary delivery format.
7. Event model для future n8n (reminders, AI draft assist, delivery notifications).
8. Project-type profiles для flexible block sets (service, e-commerce, local, etc.).

---

## 9. Non-goals

- Autonomous AI publication to clients
- Full client self-service portal with login (MVP)
- Complete BI/data warehouse
- Secrets/credentials storage inside report tables
- n8n as source of truth
- PDF-only reporting paradigm
- Public unrestricted report URLs as canonical delivery
- MARS runtime orchestration of report production
- Replacement of OPS, ATLAS, or CRM functions

---

## 10. Constraints

- **Documentation-first persist only** in MARS at this stage — no code.
- WordPress on i-seo.su is **external production runtime** — not MARS Localhost.
- n8n on operator server is **external** — helper only.
- Credential/access materials **must not** enter report content or product docs.
- MVP may start **without API integrations**.
- Human approval required for all client-facing publication.
- AI assistance (when added) — **draft only**.

---

## 11. Risks

| Risk | Mitigation direction |
|------|---------------------|
| Format fragmentation persists | Block library + work dictionary + project profiles |
| Credential leakage into reports | Explicit exclusion policy; separate integration concern |
| Over-scoping MVP | Strict MVP in/out doc; defer API/portal/iframe |
| WordPress custom module complexity | Phased implementation charter after data model review |
| Topvisor dependency | MVP: external link + screenshot; iframe only if safe later |
| Specialist adoption friction | Preserve flexibility within standardized blocks |
| n8n scope creep | Events/triggers boundary; WP remains SoT |

---

## 12. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Exact WordPress plugin/module architecture on i-seo.su | **UNKNOWN** — planning stage |
| i-seo.su hosting constraints for custom admin modules | **UNKNOWN** — requires hosting review |
| Topvisor API availability/licensing for future import | **UNKNOWN** |
| Exact reviewer role assignment (SEO Lead vs Account Manager) | **UNKNOWN** — operator decision |
| Client web report URL security mechanism (token, auth, IP) | **UNKNOWN** — design in implementation planning |
| ATLAS integration for client/project identity | **UNKNOWN** — optional consumer later |
| OPS WF-01 binding to Report Hub workflow | **UNKNOWN** — cross-program alignment deferred |
| Work dictionary final sanitized content | **UNKNOWN** — extraction stage pending |
| PDF export engine choice | **UNKNOWN** — post-MVP |
| n8n workflow inventory for Report Hub | **UNKNOWN** — no workflows exist |

---

## 13. Next decision gates

1. **Architecture review** — operator approves WordPress product architecture v0.1
2. **Data model gate** — entities, relations, WP admin UX wireframes
3. **Work dictionary gate** — sanitized extraction from Nikita materials (exclude credential sheet)
4. **MVP implementation charter** — explicit HITL scope for Anton / WordPress work on i-seo.su
5. **Security gate** — private report link strategy before client-facing MVP
6. **n8n event contract gate** — before any automation wiring

---

## Document control

- **Created:** 2026-07-10 (persist task 01)
- **Authority:** operator-approved decisions in MARS persist charter
- **Does not claim:** any runtime, plugin, API, or n8n workflow exists
