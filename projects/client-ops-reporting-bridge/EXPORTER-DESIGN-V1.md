# Exporter Design v1 — Read-Only Client Ops Exporter

**Status:** DESIGN ONLY / PHASE 0B  
**Implementation:** NOT STARTED  
**Executable CLI / scripts:** none authorized by this document  
**All interfaces below are DESIGN ONLY.**

---

## 1. Purpose

Design a future **separate** read-only exporter that:

1. Reads immutable SITE monitor artifacts.
2. Validates completeness and freshness.
3. Applies shared precedence and normalization.
4. Emits a sanitized atomic `mars.client_ops.report` v1 envelope.
5. Publishes (PROFILE A) and/or pushes (PROFILE B) without mutating source truth.

---

## 2. Inputs

| Input | Role |
|-------|------|
| Scheduled monitor run root (SITE-002) | Source of completed run folders |
| Required artifacts per run | Classification, metrics, execution metadata |
| Exporter configuration | Site identity, paths, profile mode, thresholds |
| Policy constants | Freshness 93600s; clock skew 300s |
| Wall clock (UTC) | Freshness / skew calculation |

**SITE-002 source root (operational reference, not envelope field):**  
`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\scheduled-monitors\post-1c\`

---

## 3. Outputs

| Output | Role |
|--------|------|
| Normalized envelope JSON | `mars.client_ops.report` v1 |
| Immutable by-run published file | Promoted protocol |
| Latest file/manifest | After successful by-run publish |
| Structured internal logs | Local/ops evidence; not in envelope |
| Optional failed diagnostics | Outside distributable envelope |
| PROFILE B HTTP POST body | Same envelope bytes |

---

## 4. Required artifact files (SITE-002 MVP)

| File | Authority role |
|------|----------------|
| `monitor-classification.json` | Primary classification |
| `changed-summary.json` | Metric authority |
| `run-summary.json` | Execution metadata |

Missing any required file → fail closed (`SOURCE_ARTIFACT_MISSING` / BLOCKED). Do not invent metrics.

---

## 5. Optional / companion artifact files

| File / pattern | Role |
|----------------|------|
| `run.log`, `run.stderr.log` | Evidence/debug only — never override JSON authorities |
| `added-urls.*`, `removed-urls.*` | Completeness companions |
| `hygiene-flags.*` | Completeness companions |
| `sitemap-baseline.xml`, `sitemap-current.xml` | Completeness companions |
| `monitor-classification.md`, human twins | Non-authoritative |

Companions may inform completeness checks; they must not silently supply missing required JSON fields.

---

## 6. Directory discovery

**DESIGN ONLY algorithm:**

1. List immediate child directories under the configured scheduled-monitor root.
2. Keep candidates matching the SITE-002 run id pattern: `YYYY-MM-DD_HH-MM-SS`.
3. Sort by run id descending (lexicographic equals chronological for this pattern).
4. Evaluate newest candidates until one passes completed-run detection.
5. Do **not** rely solely on newest directory name without completeness/stability checks.

---

## 7. Completed-run detection

A candidate run is **completed** only if **all** hold:

| Check | Rule |
|-------|------|
| Naming | Valid `YYYY-MM-DD_HH-MM-SS` |
| Required artifacts | All three required JSON files exist |
| Readable | Files open successfully read-only |
| Finished evidence | `run-summary.json` contains finished/completion timestamp field (e.g. `finished_at` or documented equivalent) **or** equivalent completion evidence accepted by site adapter |
| No in-progress marker | No active lock / `.in-progress` / writer lock owned by monitor |
| Stability | Two reads of required file sizes (and optional mtimes) separated by **stability interval** match |
| Age plausible | Not clock-invalid beyond skew policy when timestamps present |
| Reprocess | Not already successfully processed unless retry of publication/delivery is required |

### Stability observation interval (Phase 1 design recommendation)

- **Recommended interval:** **8 seconds** between stability samples (within the allowed **5–10 second** band).
- **Rationale:** Long enough to avoid reading mid-write of multi-file monitor completion; short enough for near-daily reporting latency.
- Phase 0B does **not** execute delays.

### In-progress rejection

If required files are missing, sizes change across the stability window, or an in-progress marker exists → **reject candidate**; do not normalize as OK/ATTENTION.

---

## 8. Read-only guarantees

| Guarantee | Requirement |
|-----------|-------------|
| No source artifact writes | Never open source files for write |
| No baseline writes | Never refresh or rewrite baseline artifacts |
| No production calls | No FTP/SFTP/SSH/REST write/DB |
| No scheduler changes | No Task Scheduler mutation |
| No monitor code changes | Separate process; does not patch monitor |
| Source folder immutable | Publish only to promoted / local outbox paths |

---

## 9. Parsing model

1. Read each required JSON as independent UTF-8 document.
2. Parse independently; one malformed file fails closed without “best effort” merge.
3. Validate required source fields per `NORMALIZATION-ALGORITHM-V1.md`.
4. Map SITE-002 field names to envelope metrics (see Phase 0A precedence doc):
   - `baseline_url_count` → `baseline_count`
   - `current_url_count` → `current_count`
   - `added_count` → `added_urls`
   - `removed_count` → `removed_urls`
   - prefer `monitor-classification.json.onboarding_needs_count` → `onboarding_needed_count`

**Rule:** Missing metric must **not** silently become zero.

---

## 10. Normalization call boundary

Exporter invokes the shared normalization algorithm (design: `NORMALIZATION-ALGORITHM-V1.md`) as a pure function over parsed artifacts + clock + config.

n8n must **not** re-run raw artifact normalization; n8n validates the resulting envelope.

---

## 11. Sanitization

Before publication:

- Strip absolute Windows paths and UNC paths from action text and public fields.
- Reject token-like markers, embedded credentials in URIs, raw stack traces, raw log bodies.
- Set `security.classification = "internal"`, `contains_secrets = false`, `redacted = true` only when checks pass.
- If security validation fails → **no publication**, **no Telegram**, distribution BLOCKED with `ENVELOPE_SECURITY_REJECTED`.

---

## 12. Envelope validation

Exporter validates against Phase 0A field table before publish:

- Required fields present; types correct; enums allowed.
- `freshness.stale` consistent with age vs 93600.
- `run.normalized_status` consistent with summary/action rules.
- Unsupported schema major → BLOCKED / `SOURCE_SCHEMA_UNSUPPORTED` (or reject before claim).

---

## 13. Output naming

| Kind | Recommended name |
|------|------------------|
| Temp write | `.tmp-<run_id>-<random>.json` in target directory |
| By-run final | `by-run\<run_id>\<event_id>.json` |
| Latest | `latest\site.post_1c_monitor.json` (atomic replace) |
| Failed diagnostic | `failed\<run_id>-<timestamp>.json` (ops only; may include non-distributable diagnostics carefully redacted) |

---

## 14. Atomic write

Preferred protocol (frozen recommendation):

1. Build envelope fully in memory.
2. Validate envelope.
3. Write UTF-8 JSON to temporary file in the **same** target directory.
4. Flush and close.
5. Optionally calculate checksum sidecar.
6. Atomically rename temp → immutable by-run final.
7. Atomically replace `latest` only after by-run success.
8. Never expose partially written final filename.
9. Never modify a published by-run file.
10. On failure, retain diagnostics outside distributable envelope; do not replace latest.

**Windows/NTFS note:** Same-volume `MoveFile`/`rename` replacement is the design assumption for atomicity. Cross-volume copy+rename is **not** atomic; exporter must write temp on the same volume as the final path. Phase 0B does not claim stronger guarantees than OS rename behavior.

---

## 15. Locking and overlap

| Concern | Design |
|---------|--------|
| Exporter lock | Single instance lock file under promoted `state/exporter.lock` (or local state) |
| Overlap | Second instance exits with non-zero “busy” status; does not write |
| Stale lock | If lock holder PID dead / lock older than configured TTL → operator-safe recovery documented; default fail closed until TTL |
| Source locks | Respect monitor in-progress markers; never clear them |

---

## 16. Restart behavior

- Restart must rediscover latest eligible completed run.
- If by-run file for same `event_id` already published → treat as publish success; proceed to transfer retry if needed without regenerating a different `event_id`.
- Must not create a second site event for the same normalized observation.

---

## 17. Exit / status codes (DESIGN ONLY)

| Code | Meaning |
|------|---------|
| 0 | Success (envelope published and/or validated per mode) |
| 2 | No eligible completed run |
| 3 | Source validation / normalization BLOCKED outcome published or recorded per mode |
| 4 | Security rejection (no distributable publish) |
| 5 | Publication failure |
| 6 | Transfer failure (PROFILE B) |
| 7 | Lock busy / overlap |
| 8 | Configuration / preflight failure |
| 10 | Unexpected internal error |

Exact numeric mapping may be adjusted at implementation charter time; semantics above are binding.

---

## 18. Structured internal logging

Log (ops only, not in envelope):

- run_id selected
- mode
- validation outcome
- summary_code / normalized_status
- event_id
- publish path basename (not required to log full raw secrets)
- transfer result
- duration

Forbidden in logs destined for Git: tokens, chat IDs, raw secret values.

---

## 19. Secret handling

- Config may reference credential **names**, never values.
- PROFILE B auth material from environment / secret store only.
- Envelope security gates as above.

---

## 20. Configuration inputs (DESIGN ONLY)

| Key | Purpose |
|-----|---------|
| `source_root` | Scheduled monitor root |
| `promoted_root` | Promoted Storage root |
| `site_id` / `site_name` / `domain` | Envelope site block |
| `producer_name` / `producer_version` | Producer identity |
| `profile` | `file` \| `push` \| `both` |
| `webhook_url_ref` | Credential/reference name only |
| `stale_after_seconds` | Default `93600` |
| `max_future_skew_seconds` | Default `300` |
| `stability_seconds` | Default `8` |
| `dry_run` | Boolean |

---

## 21. PROFILE A behavior

- Mode `publish-file`: normalize → atomic by-run + latest.
- n8n reads promoted files; exporter does not call Telegram.

## 22. PROFILE B behavior

- Mode `push-webhook`: normalize → (optional local by-run for audit) → authenticated POST of envelope.
- Retry uses same `event_id` and same payload identity.
- No webhook is created by Phase 0B.

---

## 23. Proposed future modes (DESIGN ONLY)

| Mode | Behavior | Phase 1 minimum |
|------|----------|-----------------|
| `validate-only` | Discover + normalize + validate; no publish/push | **Recommended first** |
| `build-envelope` | Write envelope to local path / stdout for fixtures | Useful for L1–L2 |
| `publish-file` | Atomic promoted publish | Required for PROFILE A |
| `push-webhook` | Authenticated POST | Required for PROFILE B |

Phase 1 implementation should initially support only the minimum approved modes for the selected profile. Phase 0B documents all boundaries.

**Do not treat the mode names as an existing CLI.**

---

## 24. Dry-run requirement

Every Phase 1 implementation charter must include a dry-run path that:

- performs discovery and normalization;
- prints/writes a sanitized envelope to a test location;
- performs **zero** production mutations;
- performs **zero** Telegram sends.

---

## 25. Testability

- Pure normalization function testable against fixtures under future `fixtures/`.
- No network required for `validate-only` / `build-envelope`.
- Atomic publish testable against isolated test Storage folder (not production promoted root until approved).

---

## 26. Future multi-site adapter boundary

| Shared | Site-specific adapter |
|--------|------------------------|
| Envelope schema, severity, freshness policy, event_id, publish protocol | Run id pattern, field name mapping, companion completeness set, source root |

SITE-002 is the first adapter. Additional sites require explicit adapters; do not assume identical artifact shapes.
