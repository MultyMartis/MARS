# OCPilot — Baseline Acquisition Strategy

**Purpose:** define how clean OpenCart / ocStore baseline packages may enter OCPilot, how to evaluate their origin, and when to reject them.

**Status:** documented strategy only; **no** baseline files imported in this run; **no** automation; **no** runtime claims.

**Core safety principle:**

```
Incoming Material  ≠  Trusted Baseline
```

Everything enters through [incoming/](incoming/README.md) and [intake-workflow.md](intake-workflow.md) before any baseline folder is populated.

---

## What baseline acquisition is

**Baseline acquisition** is the human-supervised process of obtaining a **clean vendor distribution** (OpenCart or ocStore) and, after intake review, placing sanitized reference material into a versioned folder under `baselines/`.

Acquisition is **not**:

- cloning a live client site
- copying production `public_html/` as-is
- accepting operator archives without quarantine review
- automatic download, unpack, or commit

See [baseline-storage-model.md](baseline-storage-model.md) for what belongs in a baseline after acquisition succeeds.

---

## Possible baseline sources

| Source type | Description | Typical trust |
|-------------|-------------|---------------|
| **Official OpenCart releases** | Download from opencart.com official release pages | High (when verified) |
| **Official ocStore releases** | Download from ocstore.com or documented official ocStore distribution | High (when verified) |
| **GitHub releases** | Tagged release assets from official or well-known upstream repos | Medium–High (verify repo identity) |
| **Official archives** | Vendor-provided ZIP/TAR from documented mirror or release channel | Medium (verify mirror authenticity) |
| **Manually provided packages** | Operator-supplied ZIP on disk, USB, client handoff, hosting export labeled «clean install» | Low–Medium (must not trust label alone) |

**Rule:** Source label on filename or operator brief is **evidence**, not proof. OCPilot evaluates origin during intake; see [intake-workflow.md](intake-workflow.md).

---

## Trust levels

| Level | Meaning | OCPilot stance |
|-------|---------|----------------|
| **High** | Origin verified against known official release channel; checksum or manifest cross-check possible; no signs of live-site contamination | May proceed to readiness review after quarantine pass |
| **Medium** | Plausible official source but incomplete verification (mirror, older download, GitHub asset without checksum match) | Proceed only with explicit operator confirmation; record gaps in intake report |
| **Low** | Unknown origin, repackaged archive, «clean install» claim without evidence, mixed folder, or customer/hosting handoff | **Quarantine** — do not promote to `baselines/` without operator review and rejection of unsuitable content |

Trust level is assigned per package in [templates/intake-report-template.md](templates/intake-report-template.md); it is **not** permanent until passport and readiness checklist pass.

---

## How OCPilot should evaluate baseline origin

Human-operated review (agent assists; operator approves):

1. **Declared source** — operator states URL, vendor, or handoff context.
2. **Archive identity** — filename, size, internal root folder name vs expected vendor layout.
3. **Version signals** — `index.php`, `admin/index.php`, `system/startup.php`, README, changelog, version constants (when present in archive listing — **do not execute** unknown code).
4. **Distribution integrity** — expected top-level directories (`admin/`, `catalog/`, `system/`, `image/` structure); absence of live-site artifacts (see rejection criteria).
5. **Cross-check** — when High trust required: compare against known official release page or GitHub release tag; note **SAFE UNKNOWN** if checksum unavailable.
6. **Secret scan (metadata)** — filenames suggesting `config.php` with values, `.env`, credential dumps → escalate per [quarantine-policy.md](quarantine-policy.md).

OCPilot **must not** assume archives match their labels. A file named `opencart-3037-clean.zip` may contain a modified or live site.

---

## Preferred acquisition order

When operator has choice of source, prefer in this order:

| Priority | Source | Rationale |
|----------|--------|-----------|
| 1 | Official OpenCart / ocStore release download (operator-supervised) | Strongest vendor lineage |
| 2 | Official GitHub release asset from verified upstream repository | Tag + release notes aid version pin |
| 3 | Documented official mirror or vendor archive with operator verification | Acceptable when primary site unavailable |
| 4 | Previously acquired baseline already in OCPilot `baselines/` (same version) | Reuse only if passport + readiness still valid |
| 5 | Manually provided package | Last resort — full quarantine and intake report required |

**Never** use as acquisition source:

- Installed client production or staging site tree
- Hosting «one-click install» snapshot taken after modules/themes were added
- Backup labeled «fresh OpenCart» that includes `config.php`, uploads, or custom extensions

---

## Why installed client sites should NOT become clean baselines

| Reason | Explanation |
|--------|-------------|
| **Not vendor-clean** | Live sites accumulate extensions, theme overrides, ocMod/vQmod, custom controllers, and hotfixes |
| **Secrets risk** | `config.php`, admin path, DB credentials, API keys often present |
| **Customer data** | Orders, accounts, sessions, cache, logs — forbidden in baseline per [baseline-storage-model.md](baseline-storage-model.md) |
| **False comparison** | Diffing another project against a «baseline» cloned from a different customized site produces misleading core/custom classification |
| **Version drift** | Partial updates, manual core file edits, and mixed ocStore patches break version truth |
| **Label lie** | Operators and hosts often call exports «clean» when they are full-site backups |

A client site belongs under `sites/<slug>/` after **project site intake** — never promoted directly to `baselines/`.

---

## When a baseline may be rejected

Reject (or halt promotion to `baselines/`) when intake finds:

| Rejection trigger | Action |
|-------------------|--------|
| **Missing files** | Expected vendor directories absent; incomplete archive; truncated upload |
| **Modified distribution** | Core files differ from known release without documented ocStore delta; unexpected patches in `system/` |
| **Unknown source** | Cannot verify origin; repackaged bundle; trust level Low with no operator override |
| **Credentials found** | `config.php` with values, `.env`, SQL with users/passwords, API tokens in tree or sidecar files |
| **Custom modules present** | Third-party extensions, vQmod/ocMod caches, upload catalog not part of vanilla vendor tree |
| **Live-site artifacts** | `storage/cache/`, session data, `error.log`, customer uploads, `.htaccess` with site-specific rules only |
| **Wrong platform/version** | Archive is OpenCart 2.x but target folder is `opencart-3037/`; ocStore vs OpenCart mismatch; wrong rs build for `ocstore-3038-rs2` / `ocstore-3039-rs1` |
| **Mixed package** | Baseline archive bundled with DB dump, theme pack, or unrelated project files |
| **Readiness fail** | After placement, [baseline-readiness-checklist.md](baseline-readiness-checklist.md) required items not satisfiable without unacceptable sanitization |

Rejection means: package **stays in quarantine** or is removed by operator; **no** move to `baselines/`; intake report documents reason; **SAFE UNKNOWN** until resolved.

---

## Acquisition → storage flow (summary)

```
Operator obtains package (external)
        ↓
Place in incoming/baselines/          ← quarantine; not trusted
        ↓
Intake workflow + intake report       ← see intake-workflow.md
        ↓
Operator approves destination
        ↓
Sanitize + populate baselines/<ver>/  ← Run 3+; human-operated
        ↓
Passport + readiness checklist
        ↓
Baseline usable for comparison
```

No automatic moves. No automatic imports.

---

## Relation to runs

| Run | Role |
|-----|------|
| Run 2 | Storage model, passport, readiness — destination defined |
| **Run 2.5** | Acquisition strategy, incoming zone, intake workflow |
| **Run 2.6** | Target version baseline alignment — priority folders for operator real sites |
| Run 3 | First Baseline Acquisition — first real package for **ocstore-3038-rs2** or **ocstore-3039-rs1** |

### Priority first baselines (Run 2.6)

| Priority | Baseline path | Version |
|----------|---------------|---------|
| 1 | `baselines/ocstore-3038-rs2/` | ocStore 3.0.3.8 (rs.2) |
| 2 | `baselines/ocstore-3039-rs1/` | ocStore 3.0.3.9 (rs.1) |

**ocstore-3037** remains useful as older reference; not first priority for acquisition or comparison against current operator targets.

See [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md).

---

## Related documents

| Doc | Role |
|-----|------|
| [incoming/README.md](incoming/README.md) | Quarantine / intake zone |
| [intake-workflow.md](intake-workflow.md) | Step-by-step intake |
| [quarantine-policy.md](quarantine-policy.md) | Stop conditions and review triggers |
| [templates/intake-report-template.md](templates/intake-report-template.md) | Per-package report |
| [baseline-storage-model.md](baseline-storage-model.md) | Allowed content in `baselines/` |
| [baseline-readiness-checklist.md](baseline-readiness-checklist.md) | Post-placement gate |
| [access-and-safety.md](access-and-safety.md) | Secrets and external access |

---

## SAFE UNKNOWN

- Automated checksum verification against official releases — **not** claimed; operator-assisted comparison only.
- Exact list of official ocStore vs OpenCart directory deltas per version — filled during Run 3 acquisition.
- Whether OCPilot will maintain duplicate baselines per minor patch — operator decision per acquisition.
