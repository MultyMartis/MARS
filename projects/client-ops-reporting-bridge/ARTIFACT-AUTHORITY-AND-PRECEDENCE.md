# Artifact Authority and Precedence

**Status:** FROZEN DOCUMENTATION SEMANTICS / PHASE 0A  
**Applies to:** MVP SITE post-1C monitor → future exporter normalization  
**SITE-002 evidence:** see [SITE-002-MVP-INTAKE.md](SITE-002-MVP-INTAKE.md)

---

## 1. Authority roles

| Role | Meaning |
|------|---------|
| **Primary source authority** | Machine-readable artifact that determines classification for MVP |
| **Supporting source (metrics)** | Machine-readable counts / deltas |
| **Execution metadata** | Run timing, exit code, runner notes |
| **Debug evidence** | Human/debug logs; cannot override machine-readable authorities |
| **Generated normalized output** | Future sanitized report envelope (`mars.client_ops.report`) |

---

## 2. Required artifact set (MVP)

For a trustworthy SITE-002 post-1C monitor observation, the scheduled run folder must include at least:

| Artifact | Role |
|----------|------|
| `monitor-classification.json` | **Primary classification authority** |
| `changed-summary.json` | **Metric authority** |
| `run-summary.json` | **Execution metadata** |
| Completeness companions (hardened contract) | `added-urls.*`, `removed-urls.*`, `hygiene-flags.*`, sitemap snapshots, UTF-8 logs as evidence |

Reference hardening contract: `projects/ocpilot/sites/site-002/reports/SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01.md` and tools README classification notes.

`run.log` / `run.stderr.log` are **evidence/debug only**.

---

## 3. Exact MVP precedence

1. **Artifact completeness and freshness validation**
2. **`monitor-classification.json`**
3. **`changed-summary.json` metrics**
4. **`run-summary.json` execution metadata**
5. **`run.log` as evidence/debug only**

### Mapping notes (SITE-002 observed field names)

| Envelope metric | Typical source field in `changed-summary.json` |
|-----------------|-----------------------------------------------|
| `baseline_count` | `baseline_url_count` |
| `current_count` | `current_url_count` |
| `added_urls` | `added_count` |
| `removed_urls` | `removed_count` |
| `onboarding_needed_count` | Prefer `monitor-classification.json.onboarding_needs_count` when present |

Future exporter owns the mapping; envelope must not embed absolute Storage paths.

---

## 4. Authority matrix

| Concern | Primary | Supporting | Forbidden override |
|---------|---------|------------|--------------------|
| Classification / onboarding need | `monitor-classification.json` | human MD twin | `run-summary.json.classification` alone; `run.log` |
| Counts / delta | `changed-summary.json` | added/removed URL lists | silent zero defaults; log prose |
| Exit/duration/run identity | `run-summary.json` | runner timestamps | classification authority |
| Debug narrative | `run.log` | stderr | cannot win over JSON authorities |
| Normalized site_status | Future exporter + severity rules | — | Telegram/AI outcomes |

---

## 5. Completeness checks

Before normalization:

- Required JSON artifacts exist.
- JSON parses.
- Required fields for each authority role are present.
- Counts are integers when present; missing counts are **not** coerced to 0.
- Run identity (`run_id`) is known without placing absolute paths into the envelope.

Incomplete required set → **BLOCKED** / `SOURCE_ARTIFACT_CONFLICT` or more specific missing-artifact code if Phase 1 defines one; unresolved trust failure must not become OK/ATTENTION.

---

## 6. Freshness checks

- Observation age computed deterministically from `observed_at` / capture timestamps vs exporter/consumer policy clock.
- `freshness.stale=true` → **BLOCKED**.
- Stale reports must not be sent as authoritative OK/ATTENTION/FAILED site claims.

Exact stale threshold is a Phase 1 operator/design parameter; Phase 0A freezes the **behavior** of stale=true.

---

## 7. Conflict rules

### 7.1 Core rule

`run-summary.json.classification` **must not** be the sole authority.

If machine-readable artifacts (precedence steps 2–4) are missing, malformed, stale, or **logically contradictory** such that trustworthy normalization is impossible:

| Field | Required value |
|-------|----------------|
| `site_status` / `run.normalized_status` | `BLOCKED` |
| `summary_code` | `SOURCE_ARTIFACT_CONFLICT` |
| `action.required` | `true` |
| `action.code` | `REVIEW_SOURCE_ARTIFACTS` |

**No OK or ATTENTION claim may be sent as authoritative** in that condition.

### 7.2 Forbidden silent reconciliation

- Contradictory source artifacts **must not** be silently reconciled into ATTENTION.
- Conflicts **must not** be hidden.
- `run.log` **cannot** override machine-readable artifacts.

### 7.3 Example contradiction class (SITE-002 latest)

Classification mismatch between:

- `monitor-classification.json` → `ONBOARDING_REQUIRED`
- `run-summary.json` → `NO_ACTION_REQUIRED`

with metrics showing non-zero onboarding needs / added category PLPs is an **unresolved logical contradiction**.

**Phase 0A freeze:**

- Do **not** silently reconcile this into ATTENTION.
- Do **not** hide the conflict.
- Normalize to **BLOCKED** / `SOURCE_ARTIFACT_CONFLICT` / `REVIEW_SOURCE_ARTIFACTS`.
- Prefer fail-closed over fail-open.

`monitor-classification.json` remains the **primary classification artifact** for MVP once conflicts are resolved (for example by monitor tooling fix under a separate charter). Until contradiction is gone, exporters must not emit authoritative OK or ATTENTION.

**D5R confirmation (2026-07-26, analysis-only):** the ONBOARDING vs NO_ACTION pair is a confirmed SITE-002 runner `Finish-Summary` overwrite bug (`MONITOR_ARTIFACT_GENERATION_BUG`), not an intended dual-layer health/action split. Client Ops must keep fail-closed until the emitter is repaired.

---

## 8. Malformed / missing handling

| Condition | Result |
|-----------|--------|
| Missing required JSON | BLOCKED |
| Malformed JSON | BLOCKED |
| Missing required fields | BLOCKED |
| Unsupported schema major (envelope) | BLOCKED |
| Impossible source verification | BLOCKED |
| Stale observation | BLOCKED |
| Metric missing (would require silent zero) | BLOCKED |

---

## 9. Latest known SITE-002 conflict (sanitized evidence)

**Run folder (Storage, read-only inspected 2026-07-23):**  
`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\scheduled-monitors\post-1c\2026-07-23_12-30-03`

| Artifact | Observed classification / key facts |
|----------|--------------------------------------|
| `monitor-classification.json` | `ONBOARDING_REQUIRED`; `onboarding_needs_count: 4`; `added_count: 80` |
| `run.log` | Contains `ONBOARDING_REQUIRED` (debug evidence) |
| `run-summary.json` | `classification: NO_ACTION_REQUIRED`; same run also `added_count: 80`, `onboarding_needs_count: 4` |
| `changed-summary.json` | `baseline_url_count: 1737`; `current_url_count: 1817`; `added_count: 80`; `removed_count: 0`; added page types include `CATEGORY_PLP: 4` |

**Required conclusion for this pack:**

- `run-summary.json.classification` is **not** sole authority.
- `monitor-classification.json` is primary classification artifact for MVP.
- `changed-summary.json` provides metric authority.
- `run-summary.json` provides execution metadata.
- `run.log` is evidence/debug only.
- Unresolved contradiction must normalize to **BLOCKED** / `SOURCE_ARTIFACT_CONFLICT` when trustworthy reconciliation is impossible.

Do not copy raw production logs into Git. Do not put absolute artifact paths into the report envelope.

---

## 10. Generated normalized output

Only the future exporter may emit `mars.client_ops.report`. Until then, no generated normalized runtime output is claimed.
