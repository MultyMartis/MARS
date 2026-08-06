# Promoted Artifact Protocol v1

**Status:** DESIGN ONLY / PHASE 0B  
**Directories:** NOT CREATED by Phase 0B  
**Operator approval:** exact Storage paths subject to later approval before Phase 1 write use

---

## 1. Purpose

Define a controlled Storage inbox/outbox layout for future sanitized envelopes produced by the read-only exporter and consumed by n8n (PROFILE A) or retained for audit (PROFILE B).

---

## 2. Compatibility with MARS Storage conventions

| Convention | Assessment |
|------------|------------|
| Bulk artefacts under `X:\AI MARS STORAGE\<system>\` | **Compatible** — subsystem-scoped root |
| OCPilot site artefacts remain under `ocpilot\project-sites\...` | **Preserved** — source runs stay there; bridge does not relocate sources |
| Storage is supporting layer, not a second git repo | **Honored** — promoted envelopes are out-of-git operational artefacts |
| Secrets not in Storage public trees | **Required** — no secrets under promoted bridge tree |

**SAFE UNKNOWN:** whether n8n host can read this tree (primary Phase 1 profile blocker).

---

## 3. Proposed exact Storage locus (subject to operator approval)

```text
X:\AI MARS STORAGE\client-ops-reporting-bridge\
```

### Proposed structure

```text
client-ops-reporting-bridge\
  site-002\
    inbox\                 # optional staging for PROFILE B local drops / manual drops
    published\
      by-run\
        <run_id>\
          <event_id>.json
      latest\
        site.post_1c_monitor.json
    archive\
    failed\
    state\
      exporter.lock
      processed-events.json   # optional local mirror; not sole n8n truth unless chosen
```

**Phase 0B creates none of these directories.**

---

## 4. Source vs promoted

| Location | Role |
|----------|------|
| Existing SITE-002 scheduled-monitor path | **Source** — exporter reads only |
| `client-ops-reporting-bridge\site-002\...` | **Promoted** — sanitized envelopes only |

Exporter never writes into the source run folder.

---

## 5. Filenames and atomic rename

| Stage | Name |
|-------|------|
| Temporary | `published\by-run\<run_id>\.tmp-<event_id>-<nonce>.json` (same directory as final) |
| Final by-run | `published\by-run\<run_id>\<event_id>.json` |
| Latest | `published\latest\site.post_1c_monitor.json` |

### Atomic protocol

1. Write temp in same directory as final by-run file.
2. Flush/close.
3. Rename temp → final by-run (immutable thereafter).
4. Write temp for latest in `latest\` directory.
5. Rename/replace latest only after by-run success.
6. Never overwrite an existing by-run `<event_id>.json` with different bytes; conflict → fail closed / operator review.

---

## 6. Latest protocol — recommendation

| Option | Pros | Cons |
|--------|------|------|
| Copy of envelope | Simple for readers | Duplicate bytes; risk of drift if copy fails mid-way |
| Atomic replacement file | Single read path for pollers; replace as unit | Reader must tolerate brief absence only if non-atomic tools used incorrectly |
| Pointer manifest | Small indirection to by-run path | Extra hop; path leakage risk if absolute paths used |

**Recommendation:** **atomic replacement file** at `latest\site.post_1c_monitor.json` containing the **full sanitized envelope** (same bytes as by-run for that event).

Rationale: n8n pollers get one stable path; by-run remains immutable audit copy; no absolute source paths needed in a pointer.

Optional additive manifest (not required MVP): `latest\site.post_1c_monitor.manifest.json` with `{ "event_id", "run_id", "published_at", "sha256" }` only — still no absolute source paths.

---

## 7. Immutable by-run event file

- One file per `event_id` under `by-run\<run_id>\`.
- Never modified after successful rename.
- Retries of delivery must not rewrite by-run content.

---

## 8. Checksum option

- Optional sidecar: `<event_id>.json.sha256` containing hex digest of file bytes.
- Not required for MVP if n8n validates schema + `event_id` integrity.
- If used, compute after final bytes are closed, before or immediately after rename consistency check.

---

## 9. Encoding and JSON form

| Rule | Value |
|------|-------|
| Encoding | UTF-8 without BOM |
| Newline | LF preferred in published files |
| JSON | Compact or pretty allowed; **event_id canonicalization** uses separate canonical form (see `EVENT-ID-AND-DEDUPE-V1.md`) |
| Numbers | Integers preserved (no float coercion for counts) |

---

## 10. Permissions expectations (design)

| Actor | Access |
|-------|--------|
| Exporter writer identity | Create/write under `published`, `failed`, `state`, `archive`; **no** write to OCPilot source monitor tree |
| n8n reader (PROFILE A) | Read `published\` (and optionally `state\` if shared) |
| Operators | Read for audit; controlled write for manual recovery only |

Exact Windows ACLs are operator host configuration — **SAFE UNKNOWN** until set.

---

## 11. Writer / reader ownership

| Role | Owner |
|------|-------|
| Writer of promoted envelopes | Future exporter only (or explicit operator recovery charter) |
| Reader | Future n8n (PROFILE A); humans for audit |
| Source monitor writer | Existing SITE-002 monitor/runner — unchanged |

---

## 12. Archive policy

- Move or copy aged by-run files to `archive\` after retention window.
- Recommended retention: **90 days** hot under `published\by-run`, then archive; exact retention operator-tunable.
- Archiving must not delete the sole copy without confirmation.

---

## 13. Failed publication handling

- On publish failure: write redacted diagnostic under `failed\` if safe; **do not** replace `latest`.
- Do not place secrets, raw logs, or absolute source paths into failed artefacts destined for broad sharing.

---

## 14. State / dedupe persistence boundary

- Promoted `state\` may hold exporter locks and optional processed-event mirror.
- n8n delivery dedupe authority is defined in `EVENT-ID-AND-DEDUPE-V1.md` (recommended MVP: n8n Data Store; optional Storage mirror for PROFILE A audit).
- State files are **not** distributable Telegram content.

---

## 15. Lock file design

| Item | Design |
|------|--------|
| Path | `state\exporter.lock` |
| Contents | writer id, pid, started_at (UTC), hostname — no secrets |
| Acquire | Create-new exclusive if supported; else atomic create pattern |
| Release | Delete on clean exit |

### Stale lock recovery

| Condition | Action |
|-----------|--------|
| Lock age ≤ TTL (recommend **30 minutes**) | Fail busy |
| Lock age > TTL and process not alive | Operator-approved recovery: remove lock and record evidence |
| Ambiguous | Fail closed; manual review |

---

## 16. Retention recommendation

| Path | Recommendation |
|------|----------------|
| `published/by-run` | 90 days hot |
| `latest` | Current only |
| `failed` | 30–90 days |
| `archive` | Per Storage archive policy |
| `inbox` | Drain promptly; do not accumulate secrets |

---

## 17. Security constraints

- No secrets in promoted envelopes.
- No raw logs.
- No absolute source paths in distributable envelope.
- Internal ops docs may reference canonical MARS paths; envelope payloads must not.

---

## 18. Inbox usage (optional)

`inbox\` is reserved for manual operator drops or PROFILE B local staging. Automated PROFILE A happy path uses `published\` only.
