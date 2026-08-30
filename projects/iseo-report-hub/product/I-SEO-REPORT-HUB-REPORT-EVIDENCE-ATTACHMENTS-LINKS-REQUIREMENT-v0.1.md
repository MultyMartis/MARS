# I-SEO Report Hub — Report Evidence / Attachments / External Proof Links Requirement v0.1

**Date:** 2026-08-27  
**Status:** product requirement — **not implemented**  
**Layer name:** Report Evidence / Attachments / External Proof Links  
**Scope:** next major product layer after local specialist MVP acceptance

---

## 1. Problem

The current specialist workflow can describe work and results in text, but it lacks **structured evidence**:

- screenshots of rankings, analytics, or tool reports;
- attached files (exports, PDFs, spreadsheets);
- links to **external services** with client-visible or guest reports;
- dated **position-scan reports** from rank trackers;
- proof from Yandex Webmaster, Google Search Console, Metrica, Analytics.

Without evidence slots, specialists fall back to informal notes, email attachments, and chat — which does not scale for client-facing monthly reports.

**This wave documents requirements only.** No upload, no external API, no DB migration.

---

## 2. Evidence Types

### 2.1 Screenshot / image evidence

- Uploaded screenshot (PNG/JPG/WebP)
- Title / caption
- Capture date
- Source (manual upload, pasted from clipboard — future)
- Related report section (`section_key`)
- Visibility: client-visible vs internal-only

### 2.2 File attachment

- Formats: PDF, XLSX, CSV, DOCX, image
- Title
- Source (upload)
- Date / period
- Visibility:
  - **internal only** — team reference
  - **client-visible** — may appear in preview / future client delivery

### 2.3 External proof link

- URL
- Title / label
- Service / source name (free text + optional enum later)
- Date or date range covered
- Visibility
- **Public accessibility status** (required metadata):
  - `public` — open without login
  - `guest_link` — token/guest URL (may expire)
  - `requires_login` — not safe for client preview
  - `unknown` — must be verified before client visibility

### 2.4 Rank tracking report link

Specialized external proof for position monitoring tools.

Metadata:

- Project / site
- Search engine (Yandex, Google, …)
- Region
- Device (desktop / mobile / smartphone)
- Group / tag filters
- Date range
- Link to live or exported report

### 2.5 Yandex / Google analytics evidence

- Yandex Webmaster, Metrica, Google Search Console, Analytics
- Screenshot and/or link
- **Strict privacy rules** — no accidental exposure of private dashboards in client preview
- Default visibility: **internal-only** until operator policy confirms client-safe sharing

---

## 3. Per-Section Evidence Slots

Report content workflow sections (Hybrid MVP) — evidence attach points:

| Section key (RU label) | Screenshots | External links | Files | Client-visible allowed | Notes |
|------------------------|-------------|----------------|-------|------------------------|-------|
| **Результаты** | yes | yes | yes | yes (with review) | Primary home for rank/analytics proof |
| **Что сделали** | yes | optional | optional | yes | Work proof, before/after |
| **Ключевые выводы** | yes | yes | optional | yes | Interpretation backed by data |
| **Краткое резюме** | optional | optional | no | yes | Light evidence only |
| **Риски и блокеры** | optional | optional | optional | mixed | Internal notes may dominate |
| **План на следующий месяц** | no | optional | no | yes | Links to planned checks |
| **Внутренние заметки** (future) | yes | yes | yes | **internal only** | Never in client preview |

Each slot should support **multiple evidence items** ordered by date or manual sort.

---

## 4. Rank Tracker Public Report Services

**Candidates to verify with real i-SEO accounts** — do **not** hard-commit until verified:

| Service | Likely use | Verify |
|---------|------------|--------|
| **Topvisor / Топвизор** | Rank tracking, project reports, exports; guest/public links **may** exist | Exact guest-link workflow, expiry, client-safe URL pattern |
| **Keys.so Monitoring** | Rank monitoring candidate | Public link / export workflow |
| **Toolzar** | Rank monitoring candidate | Public link / export workflow |
| **Other tools** used by i-SEO specialists | Collect from team interviews | — |

**Yandex Webmaster:** query stats, impressions, clicks, CTR — public/client sharing workflow **unknown**; verify manually.

**Do not assert** exact third-party product names in UI until operator confirms account access and sharing model.

---

## 5. Uploaded Screenshot Analysis (reference)

Reference screenshot (operator-provided) shows a **rank monitoring / SEO position tracking** interface for:

- **Project:** `goodkitchen.su / goodkitchen.su`
- **Search engine:** Yandex
- **Region / device:** Moscow / smartphone-like selector
- **Date range:** 05.05.2026 – 01.09.2026
- **Query list** with frequency column
- **SERP features** column
- **Daily position grid** with color-coded movement

**Likely category:** external rank-tracking report (Topvisor or similar — **SAFE UNKNOWN** until account verification).

**Report Hub representation (future):**

1. **External rank tracking report link** — primary record (URL + metadata above)
2. **Optional screenshot attachment** — static proof if link expires
3. **Section association** — `Результаты` and/or `Ключевые выводы`

---

## 6. Future UI Proposal

### Option A — dedicated tab

New navigation item on monthly report:

**«Доказательства»** (`/monthly-reports/{id}/evidence`)

List all evidence for the month; filter by section and visibility.

### Option B — inline per section (preferred for MVP of evidence layer)

Inside **content workflow**, each section card gets an evidence block:

- **Добавить скриншот**
- **Добавить файл**
- **Добавить внешнюю ссылку**
- **Видимость:** клиенту / только внутренне
- **Дата / период**
- **Источник** (service name)

**Phasing suggestion:**

- **Phase 1:** external links + metadata (no file storage)
- **Phase 2:** screenshot/file upload + storage policy
- **Phase 3:** preview rendering + client delivery integration

---

## 7. Data Model Sketch (not implemented)

Candidate table: `monthly_report_evidence`

| Field | Type / notes |
|-------|----------------|
| `id` | PK |
| `monthly_report_id` | FK |
| `section_key` | e.g. `results`, `key_findings`, … |
| `evidence_type` | screenshot / file / external_link / rank_report |
| `title` | string |
| `description` | optional text |
| `source_service` | e.g. topvisor, yandex_webmaster |
| `source_url` | nullable |
| `file_path` | nullable — storage TBD |
| `file_name` | nullable |
| `date_from` | nullable date |
| `date_to` | nullable date |
| `visibility` | client / internal |
| `public_access_status` | public / guest_link / requires_login / unknown |
| `created_by` | user id |
| `created_at` | timestamp |
| `updated_at` | timestamp |

**Storage:** file path design, backup, retention, and antivirus scanning — **future charter**.

**Security:** client-visible files/links must pass review; never expose login-gated analytics URLs in preview.

---

## 8. Acceptance Criteria (future implementation wave)

Future implementation must prove:

1. Specialist can add an **external proof link** to section **Результаты**.
2. Specialist can mark link **client-visible** or **internal-only**.
3. **Client preview** renders client-visible evidence links (labeled, safe).
4. **Internal-only** evidence does **not** appear in client preview.
5. Links marked `requires_login` are **blocked** from client visibility by default.
6. Screenshot/file upload (if in scope) stays on **local/dev** until storage security review.
7. **No PDF / share / export** required for evidence MVP.

---

## 9. Risks

| Risk | Mitigation |
|------|------------|
| Accidental exposure of private analytics links | Default internal-only; explicit confirm for client-visible; block `requires_login` in preview |
| Guest links expiring | Show “link may expire”; encourage screenshot backup |
| Screenshots contain PII or unrelated clients | Upload review; naming conventions |
| File storage security | Separate storage charter; no public web root for internal files |
| Client vs internal confusion | Strong UI labels; preview dry-run |
| Production backup / cleanup | Ops charter with retention policy |

---

## 10. Recommended Future Waves

**After operator manual walkthrough:**

1. **I-SEO Report Hub — Report Evidence Links Charter 01** — scope, UX, security, phasing  
2. **I-SEO Report Hub — Report Evidence Links MVP Implementation 01** — external links + preview (Phase 1)

Optional parallel:

- Collect **real service list** from SEO team (Topvisor, Keys.so, Toolzar, Webmaster, …)
- Verify **guest/public link** behavior on live accounts before promising client-visible links

---

## Related

- [I-SEO-REPORT-HUB-LOCAL-SPECIALIST-MVP-ACCEPTANCE-CLOSEOUT-v0.1.md](I-SEO-REPORT-HUB-LOCAL-SPECIALIST-MVP-ACCEPTANCE-CLOSEOUT-v0.1.md)
- [I-SEO-REPORT-HUB-SEO-SPECIALIST-DRAFT-INSTRUCTION-v0.1.md](../operator-guides/I-SEO-REPORT-HUB-SEO-SPECIALIST-DRAFT-INSTRUCTION-v0.1.md)
