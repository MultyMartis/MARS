# EAR OpenCart Snapshot Specification v1

**Purpose:** Define the canonical **OpenCart / ocStore Snapshot Package** structure — the interface between acquisition systems and consumer systems (primarily OCPilot).  
**Status:** architecture specification only — **no** serializer, validator, connector, or schema file in-repo.  
**Phase:** 2A — OpenCart Snapshot Specification  
**Relation:** Specializes [EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md) for OpenCart / ocStore / ocStore forks. General contract remains valid for cross-platform fields; this document is **source of truth** for OpenCart-shaped packages.

---

## Design principles

| Principle | Meaning |
|-----------|---------|
| **Snapshot as interface** | Consumers receive packages; they do **not** depend on raw FTP, SSH, DB credentials, or live hosting access. |
| **Metadata over bulk** | v1 emphasizes inventories, manifests, and structural metadata — not full file trees or row data in the package contract. |
| **No PII in contract** | Database section is schema-level only; no customer, order, or session row content. |
| **SAFE UNKNOWN** | Missing or unverified data must be explicit; consumers must not infer completeness from empty sections. |
| **Baseline comparison** | File manifest and version fields exist to support diff against approved baselines (e.g. `ocstore-3038-rs2`). |

---

## Reference pilot (documentation only)

| Field | Example (SITE-001) |
|-------|---------------------|
| Site ID | `SITE-001` |
| Platform claim | ocStore 3.0.3.8 (rs.2) |
| Approved baseline | `ocstore-3038-rs2` |
| Consumer | OCPilot |

This table illustrates alignment only — **not** an actual snapshot.

---

## Package identity (required at package root)

Conceptual fields every OpenCart Snapshot Package must carry (in `metadata/` or equivalent root descriptor):

| Field | Required | Notes |
|-------|----------|-------|
| `snapshot_id` | Yes | Unique id, e.g. `snap-20260601-site-001-p1` |
| `snapshot_contract` | Yes | `ear-opencart-snapshot-v1` (this spec) |
| `parent_contract` | Yes | `ear-snapshot-v1` — link to generic contract |
| `site_id` | Yes | Consumer registry id (e.g. `SITE-001`) |
| `created_at` | Yes | ISO 8601; operator timezone noted in metadata |
| `ear_mode` | Yes | `0`, `1`, or `2` at acquisition time |
| `operator_approval` | Yes | Non-secret identifier of publish approver |

Physical encoding (folder tree, single archive, sidecar index) — **SAFE UNKNOWN** until Phase 2B charter; logical structure below is normative.

---

## Logical package structure

```
Snapshot/
├── metadata/
├── file-manifest/
├── theme-info/
├── extension-inventory/
├── ocmod-inventory/
├── database-metadata/
├── seo-structure/
├── environment/
├── safe-unknown/
└── acquisition-log/
```

Optional bulk payloads (full file trees, SQL exports) may live **outside** this logical tree, referenced from metadata — not required for contract compliance at quality Level 1–2.

---

## Section reference matrix

| Section | Purpose | Required | Optional | Typical source | Consumer usage |
|---------|---------|----------|----------|----------------|----------------|
| **metadata** | Identity, platform, acquisition context | Always (min set per quality level) | Extended claims, URLs, bulk refs | Operator + acquisition | Route audit, version proof, baseline selection |
| **file-manifest** | Structural file inventory for baseline diff | L1+ | Hash algorithm detail, archive ref | File scan / operator drop | Diff vs `ocstore-*` baseline; modified-core detection |
| **theme-info** | Active and installed theme structure | L1+ (if themes relevant) | Child theme chain detail | Admin theme settings, `catalog/view/theme/` scan | UI/UX audit, override mapping |
| **extension-inventory** | Extensions, modules, integrations | L2+ | Deep config excerpts | Admin extension list, `extension/` tree | Risk analysis, unknown surface |
| **ocmod-inventory** | Modification system state | L2+ | XML content refs (names only in v1) | `system/modification.xml`, ocMod storage | Customization mapping |
| **database-metadata** | Schema-level DB facts | L1+ | Engine/collation detail | Read-only schema export or table list | Schema drift, prefix, extra tables |
| **seo-structure** | SEO URL and routing indicators | L1+ | Extension-specific SEO modules | `config.php` flags, `.htaccess` patterns, SEO tables metadata | SEO audit without live crawl |
| **environment** | Deployment class for safety | Always | Host panel labels | Operator declaration + weak signals | Halt rules on PRODUCTION vs TEST |
| **safe-unknown** | Explicit gaps | Always (may be empty list only if truly complete) | Per-topic unblock hints | Acquisition honesty | Block dependent audit phases |
| **acquisition-log** | How evidence was obtained | Always | HITL checklist refs | Operator + EAR procedure | Audit trail, reproducibility |

---

## Section: metadata

**Purpose:** Give consumers enough context to start analysis without opening bulk storage or connecting to the live site.

**Required categories (conceptual fields — not a formal schema):**

### Platform and version

| Field category | Description | Verification |
|----------------|-------------|--------------|
| **Platform** | Product family: OpenCart, ocStore, or fork name | Cross-check file-manifest and version files |
| **Version** | Operator- or acquisition-recorded version string | Must not be sole proof |
| **Detected version** | Version derived from `index.php`, `admin/index.php`, `system/version.php` or equivalent | Consumer may override `Version` if mismatch |
| **Build / release suffix** | e.g. `(rs.2)` for ocStore | Documented in platform claim |

### Environment and site

| Field category | Description |
|----------------|-------------|
| **Environment** | See dedicated `environment/` section; summary may duplicate here |
| **Site ID** | Consumer registry id |
| **Site display name** | Human label (non-secret) |
| **Store URLs** | Storefront and admin URL patterns — **no** credentials |

### Acquisition

| Field category | Description |
|----------------|-------------|
| **Acquisition date** | When evidence was collected |
| **Acquisition mode** | EAR Mode 0 / 1 / 2 |
| **Acquisition scope** | What was attempted (files only, DB metadata only, etc.) |
| **Operator** | Non-secret handle of acquiring operator |
| **Snapshot sequence** | Optional: `p1`, `p2` for partial reruns |

### Baseline alignment (OCPilot)

| Field category | Description |
|----------------|-------------|
| **Baseline candidate** | Suggested baseline id for comparison (e.g. `ocstore-3038-rs2`) |
| **Baseline approved** | Whether operator/charter approved this baseline for the site |
| **Baseline version note** | Why this baseline was chosen |

### References

| Field category | Description |
|----------------|-------------|
| **Consumer target** | e.g. `ocpilot` |
| **Bulk root reference** | External path to optional full tree — outside git |
| **Prior snapshot reference** | Optional link to previous `snapshot_id` |

### Contract and honesty

| Field category | Description |
|----------------|-------------|
| **SAFE UNKNOWN summary** | Optional high-level count; detail lives in `safe-unknown/` |
| **Package quality level** | 0–3 per section below |

**Rules:**

- Platform claims in metadata are **claims** until corroborated by file-manifest or version files.
- Credentials, API keys, and connection strings **must not** appear in metadata committed to git.

---

## Section: file-manifest

**Purpose:** Enable comparison against an approved baseline (e.g. `ocstore-3038-rs2`) and prior snapshots **without** requiring full file contents inside the package at v1.

### What EAR should collect (conceptual)

| Manifest element | Description |
|------------------|-------------|
| **Root folders** | Presence and names of standard OpenCart roots: `admin/`, `catalog/`, `system/`, `image/`, `storage/` or legacy layout |
| **File counts** | Per top-level folder and optionally per subtree policy |
| **Path list** | Relative paths with size and optional hash (SHA-256 recommended) |
| **Custom folders** | Paths not present in baseline — flagged |
| **Modified core indicators** | Paths that exist in baseline but differ by hash or size beyond policy threshold |
| **Missing baseline paths** | Expected baseline paths absent on site |
| **Theme paths** | `catalog/view/theme/<name>/` roots detected |
| **Storage paths** | `storage/` or `system/storage/` layout variant |
| **Upload / cache exclusions** | Documented paths excluded from manifest (cache, logs, sessions) |
| **Version proof files** | Explicit listing of `index.php`, `admin/index.php`, `system/version.php` if present |

### Manifest form (v1)

One of:

- **Inline manifest** — path list with size + optional hash in package
- **External manifest reference** — pointer to archive + sidecar manifest in bulk storage

**Rules:**

- v1 contract: **no file contents required** in the manifest section itself.
- Manifest purpose is **comparison**, not backup.
- Absolute server paths in operator copies should be avoided in git-bound artifacts; use relative site-root paths.

### Consumer usage

- Diff manifest vs baseline manifest (OCPilot Run 5 model).
- Halt or partial-run phases that require manifest if section missing — record in consumer report.
- Treat `Modified core indicators` as **signals**, not automatic verdicts.

---

## Section: theme-info

**Purpose:** Describe theme installation and override surface without shipping full theme assets in metadata-only packages.

| Element | Required | Source | Consumer usage |
|---------|----------|--------|----------------|
| **Active storefront theme** | L1+ | Admin settings, config | Audit scope |
| **Installed themes** | Optional | `catalog/view/theme/` scan | Inventory |
| **Theme version markers** | Optional | `style.css` or theme metadata files if present | Drift detection |
| **Admin theme** | Optional | Admin view paths | Separate from storefront |
| **Override indicators** | Optional | Twig/PHP override paths under theme | Customization map |
| **Editor / live theme tools** | Optional | Extension signals | Risk flags |

**SAFE UNKNOWN:** Child theme chains and multi-store theme mapping — document in `safe-unknown` if not resolved.

---

## Section: extension-inventory

**Purpose:** Support **risk analysis** — what code modules and integrations are present.

### Categories to capture

| Category | Description |
|----------|-------------|
| **Installed extensions** | Extensions visible in admin or under `extension/` (type + code + title if available) |
| **Detected modules** | Payment, shipping, feed, fraud, analytics modules |
| **Detected integrations** | Marketplaces, CRM, telephony, pixel trackers — indicator level only |
| **Third-party indicators** | Vendor folders, copyright headers in index scans — heuristic |
| **Unknown extensions** | Present on disk but not mappable to admin list |
| **Disabled but present** | Installed but inactive — if detectable |
| **Vqmod / other modifier systems** | If present — note alongside ocmod-inventory |

### Source (conceptual)

- OpenCart admin Extension list (screenshot or export metadata — not live automation in v1 spec)
- Filesystem scan of `extension/`, `admin/controller/extension/`, upload packages
- Operator-provided inventory spreadsheet (Mode 0)

### Consumer usage

- Risk scoring and unknown-surface reports
- Cross-link to `ocmod-inventory` for modification overlap
- **Must not assume** extension list is complete if acquisition was partial

---

## Section: ocmod-inventory

**Purpose:** **Customization mapping** via OpenCart Modification system (and related artifacts).

| Element | Description |
|---------|-------------|
| **Installed modifications** | Mod names / ids from modification table or XML storage |
| **Enabled state** | Enabled vs disabled per mod |
| **Custom modifications** | Site-specific XML not matching known vendor packs |
| **Unknown modifications** | XML present but source unclear |
| **Refresh / cache state** | Whether modification cache was refreshed recently — if observable metadata only |
| **Conflict indicators** | Multiple mods touching same target — heuristic only in v1 |

### Source (conceptual)

- `system/modification.xml` or storage-backed modification directory
- Admin Modifications list metadata
- File scan of `system/storage/modification/` or equivalent

### Rules

- v1: **names and paths preferred** over full XML bodies in package; full XML may live in bulk storage with reference only.
- Consumer maps mods to baseline diff findings; does not apply mods.

---

## Section: database-metadata

**Purpose:** Schema-level audit **without** row data, customer data, or PII.

| Element | Required | Description |
|---------|----------|-------------|
| **Database engine** | L1+ | MySQL / MariaDB / Percona — version if available |
| **Table prefix** | L1+ | e.g. `oc_` |
| **Table count** | L1+ | Total tables in scope |
| **Table list** | L1+ | Names only |
| **Extra tables** | Optional | Tables not expected for baseline platform version |
| **Missing tables** | Optional | Baseline-expected tables absent |
| **Schema indicators** | Optional | Key settings from `oc_setting` — **keys and structure only**, not customer values |
| **Collation / charset summary** | Optional | Database-default level |
| **Storage engine mix** | Optional | InnoDB vs MyISAM counts |

### Explicitly forbidden in package (v1)

- Full SQL dumps with row data
- Contents of customer, address, order, session, cart tables
- Admin user passwords or salts
- API keys stored in DB

### Source (conceptual)

- `SHOW TABLES`, `information_schema` read-only queries
- Operator-provided sanitized schema export (Mode 0)
- phpMyAdmin structure-only export metadata

### Consumer usage

- Schema drift vs baseline `database-metadata` artifacts
- Prefix and engine confirmation for migration planning — analysis only in OCPilot

---

## Section: seo-structure

**Purpose:** Capture **SEO and URL routing indicators** at metadata level — not a live SEO score or crawl.

| Element | Description |
|---------|-------------|
| **SEO URLs enabled** | Use SEO URL setting from config metadata |
| **Rewrite indicators** | `.htaccess` or nginx rules present — pattern summary, not secrets |
| **URL patterns** | Category/product/information route patterns if documented |
| **Custom routing indicators** | Non-standard routers, SEO Pro, multilingual URL extensions |
| **SEO extensions** | Named SEO-related extensions from extension-inventory cross-ref |
| **Multilingual SEO** | Language prefix patterns — if multi-store / multi-lang detected |
| **Canonical / robots indicators** | robots.txt present; meta robot patterns — file presence only |

### Rules

- No requirement to store full `oc_seo_url` table contents in v1.
- If URL sample needed, use **synthetic or operator-redacted** examples outside PII policy.

---

## Section: environment

**Purpose:** **Operational safety** — consumers apply stricter halt rules when environment is production or unknown.

### Allowed values (normative enum)

| Value | Meaning |
|-------|---------|
| `TEST` | Non-production test store |
| `DEV` | Development / local |
| `STAGING` | Pre-production mirror |
| `PRODUCTION` | Live customer-facing |
| `UNKNOWN` | Not verified — treat as highest caution |

### Fields (conceptual)

| Field | Description |
|-------|-------------|
| **environment_class** | One of enum above |
| **operator_assertion** | Operator-declared environment |
| **weak_signals** | Hostname patterns, robots, IP hints — documented as non-proof |
| **multi_store_note** | If multiple stores under one install |

### Rules

- `PRODUCTION` requires explicit operator assertion in acquisition-log.
- Consumers **must not** assume `TEST` from URL alone.
- Unknown environment → consumer runs read-only analysis only; no change recommendations that imply live mutation.

---

## Section: safe-unknown

**Purpose:** Explicit honesty — same rule as generic contract, OpenCart-specific topics encouraged.

**Required behavior:**

- If any required section for the declared quality level is missing or unverified, an entry **must** exist here.
- Empty section elsewhere **without** a `safe-unknown` entry is a contract violation.

### Example topic categories (illustrative)

| Topic | Example reason |
|-------|----------------|
| `live_version_proof` | No `index.php` in acquisition |
| `file-manifest` | SFTP scope excluded `image/` |
| `database-metadata` | No DB access granted |
| `seo-structure` | Could not read config — files only |
| `ocmod-inventory` | Modification cache not exported |
| `environment` | Operator could not confirm PRODUCTION vs STAGING |

Each entry should support: **topic**, **reason**, **impact on consumer**, **optional unblock hint** (procedure id, not implementation).

---

## Section: acquisition-log

**Purpose:** Audit trail of **how** this snapshot was acquired — distinct from site access logs or web server logs.

| Entry type | Description |
|------------|-------------|
| **approved_by** | Operator who approved acquisition |
| **approved_at** | Timestamp |
| **published_by** | Operator who approved consumer handoff |
| **ear_mode** | 0 / 1 / 2 |
| **channel** | e.g. `manual-drop`, `sftp-readonly`, `panel-export` — conceptual only in v1 |
| **scope** | Paths or subsystems included/excluded |
| **hitl_reference** | Charter, run id, or checklist id |
| **partial_run** | If snapshot is Phase 1 of multi-part acquisition |
| **tooling_note** | Human-readable tools used — **no** credentials |

**Relation to generic contract:** Maps to `access-log` in [EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md); OpenCart packages use the name `acquisition-log` for clarity. Cross-walk in Phase 4 unification — **SAFE UNKNOWN** until then.

---

## Snapshot quality levels

Packages declare a **quality level** in metadata. Higher levels subsume lower requirements.

### Level 0 — Identity only

**Minimum contents:**

| Section | Requirement |
|---------|-------------|
| metadata | `snapshot_id`, `site_id`, platform claim, `created_at`, quality level `0` |
| environment | `environment_class` (may be `UNKNOWN`) |
| safe-unknown | Lists all sections not acquired |
| acquisition-log | Minimum approval + mode |

**Consumer:** May register snapshot existence only; **must not** run baseline diff or extension risk phases.

---

### Level 1 — Identity + structure

**Minimum contents:** Level 0 plus:

| Section | Requirement |
|---------|-------------|
| metadata | `Detected version` or explicit safe-unknown for version proof |
| file-manifest | Root folders, file counts OR path list subset covering version proof files |
| database-metadata | Prefix + table list **or** safe-unknown with unblock |
| seo-structure | SEO URLs enabled flag **or** safe-unknown |
| theme-info | Active theme name **or** safe-unknown |

**Consumer:** Structural audit and baseline diff **if** manifest sufficient; extension risk phases remain blocked or partial.

---

### Level 2 — Identity + structure + extensions

**Minimum contents:** Level 1 plus:

| Section | Requirement |
|---------|-------------|
| extension-inventory | Installed extensions list (may include unknowns bucket) |
| ocmod-inventory | Installed mods list with enabled state **or** safe-unknown |

**Consumer:** Risk analysis and customization mapping allowed; full audit snapshot phases may still wait on Level 3.

---

### Level 3 — Full read-only audit snapshot

**Minimum contents:** Level 2 plus:

| Section | Requirement |
|---------|-------------|
| file-manifest | Comprehensive path list per acquisition scope policy (exclusions documented) |
| extension-inventory | Modules and integration indicators populated |
| ocmod-inventory | Custom and unknown mods classified |
| database-metadata | Extra/missing tables vs baseline indicators |
| seo-structure | Rewrite indicators + SEO extensions cross-ref |
| safe-unknown | Only genuinely residual unknowns |

**Consumer:** OCPilot Run 5 full read-only audit may proceed subject to charter; individual phases may still halt on residual `safe-unknown` entries.

**Note:** Level 3 does **not** require full file **contents** or row data in v1 — it requires **comprehensive metadata coverage** per scope policy. Bulk archives are optional and referenced externally.

---

## Versioning and compatibility

| Identifier | Role |
|------------|------|
| `ear-opencart-snapshot-v1` | This document |
| `ear-snapshot-v1` | Parent generic contract |

Breaking changes require a new spec version and explicit consumer bump. Additive optional fields may be documented without bump if consumers treat unknown fields as opaque.

---

## Relation to flow

```
SITE (external)
    ↓
EAR (acquire + assemble — future)
    ↓
OpenCart Snapshot Package (this spec)
    ↓
OCPilot (consume — read-only analysis)
```

---

## SAFE UNKNOWN (spec-level)

- Official JSON Schema / YAML schema file — not in Phase 2A.
- Exact hash algorithm mandate — SHA-256 recommended, not enforced by tooling in-repo.
- Zip bundle layout and encryption at rest — Phase 2B+.
- Unified `acquisition-log` vs `access-log` naming across WordPress — Phase 4.
- Automated quality level validator — not claimed.

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md) | Parent contract |
| [EAR-SNAPSHOT-LIFECYCLE-v1.md](EAR-SNAPSHOT-LIFECYCLE-v1.md) | Acquire → Archive |
| [EAR-OPENCART-CONSUMER-GUIDE-v1.md](EAR-OPENCART-CONSUMER-GUIDE-v1.md) | OCPilot consumption rules |
| [EAR-ARCHITECTURE-v1.md](EAR-ARCHITECTURE-v1.md) | Layer model |
| [projects/ocpilot/freeze/site-001-pre-runtime-bridge/](../../projects/ocpilot/freeze/site-001-pre-runtime-bridge/) | SITE-001 blockers |
