# FP-0002 — WPilot Install Readiness (Beget) — PROD-P01 / updated P03 / FU02 / P05-FU01

**Status:** **INSTALLED AND CURRENT** — WPilot **0.3.2-RC1** active; authenticated READ **PROVEN**; write **disabled**  
**Host:** `http://shpigovsky.beget.tech/`  
**Date:** 2026-08-14 (P05-FU01 closeout; FU02 remains content/FS product authority)

**P05-FU01:** Canonical package **0.3.2-RC1** SHA `d55c19d6…` **MATCH** and **installed** via native Upload Plugin replace. Production WPilot **0.3.2 / 0.3.2-RC1**, schema **0.2.0**, `write_enabled=false`. Local token file present. Authenticated MARS READ **PROVEN**.

---

## 0. Critical production finding (changes the next gate)

Public read-only discovery shows WPilot is **already present** on Beget after the full local migration:

`GET /wp-json/wpilot/v1/ping` → **200**

Public snapshot (no secrets):

| Field | Public value |
|-------|----------------|
| plugin | `metacode-wpilot` |
| status | `installed` |
| bridge_enabled | **true** |
| write_enabled | **false** |
| state | **token-generated** |
| dev_confirmed | **true** (bridge_state_snapshot) |
| emergency_disabled | **false** |
| Plugin Version / RELEASE_LABEL | **SAFE UNKNOWN** in P01 ping; **PROD-P03 Admin: Version `0.3.0`** (not `0.3.2-RC1`) |

**Implication:** Do **not** treat the next wave as a naive clean ZIP install on an empty site.  
**PROD-P03:** WP Admin proves installed **Version `0.3.0`**, schema **`0.2.0`**, active. Classification vs current baseline: **OLDER**. Likely migrated `v0.3.0-rc5` lineage. **STOP before upgrade** until an exact-package charter.

Historical local FP-0002 note (WPilot OPERATIONAL-INDEX): `shpigovsky.test` previously ran **v0.3.0-rc5** — production Admin now matches **0.3.0** header (RC label not printed as 0.3.2-RC1).

---

## 1. CURRENT GLOBAL NEW-PRODUCTION BASELINE (repo truth)

Resolved from live MARS repository + STORAGE packages (not chat memory):

| Field | Value |
|-------|-------|
| Plugin slug | `metacode-wpilot` |
| Plugin Version (source header/constants) | **`0.3.2`** |
| Release label | **`0.3.2-RC1`** |
| Schema version | **`0.2.0`** |
| REST namespace | **`wpilot/v1`** |
| Auth header | `X-WPilot-Token` (fallback `x_wpilot_token`) |
| Canonical ZIP | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.2-rc1.zip` |
| SHA-256 (documented + recomputed match) | **`d55c19d6ea1a55cd145e9b67c42ca201c30e4356f08d8cf3932ef6a5ebc80934`** |

### Does RC6 remain the default new-production baseline?

**No — not as current source/package authority.**

| Package | Role |
|---------|------|
| **0.3.2-RC1** | **CURRENT source + current deploy package** in repo/STORAGE; Polygon production final |
| **0.3.0-RC6** | Historical **proven install baseline** for i-seo / metallka; still preserved ZIP `…-v0.3.0-rc6.zip` SHA `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| **0.3.1-RC1** | Intermediate CLASS-1 package; superseded by 0.3.2-RC1 |

### POLYGON HISTORICAL FINAL VERSION

**`0.3.2 / 0.3.2-RC1`** — production deployed (P07), CLASS-1 lifecycle proven (P09–P12-R01), connection closeout P13.

Polygon 0.3.2 was **not** merely a disposable experiment: it is the current upstream package that matches MARS source. Older sites remaining on RC6 are **site-historical**, not a reason to ignore 0.3.2-RC1 for a newly onboarded production that will follow current source.

### Recommendation for FP-0002

1. **First:** operator reports live WP Admin Version/Release for installed WPilot.  
2. **If upgrade required:** use **0.3.2-RC1** exact ZIP above (Polygon-style overwrite upgrade charter — separate wave).  
3. **If already 0.3.2-RC1:** skip install; proceed to **safe-defaults / token hygiene** charter (separate).  
4. **Do not** install RC6 onto FP-0002 as “default” while source is 0.3.2.

---

## 2. Expected safe defaults (current source — `WPilot_Settings::defaults` / `activate`)

Immediately after a **clean** activation, current source forces:

| Option | Expected safe value |
|--------|---------------------|
| `bridge_enabled` | **false** |
| `write_enabled` | **false** |
| `emergency_disabled` | **false** |
| `dev_confirmed` | **false** |
| `token_hash` | empty (no token) |

**Beget current public state differs:** bridge **true**, DEV confirmed **true**, token **generated**, write **false**.  
That is **not** the clean-install safe default posture. Resetting it requires a **separate operator charter** (not executed here).

---

## 3. Auth / secret model (documentation only — no secrets created)

| Topic | Current truth |
|-------|----------------|
| Auth header | `X-WPilot-Token` |
| Token creation | WP Admin → MetaCODE WPilot → generate (RC6+ `can_manage_token` model in current lineage); plaintext shown once |
| Site-side storage | Password hash in `wpilot_options` only — **never** plaintext in DB |
| Client-side storage | Local-only file under `X:\AI MARS\local\tokens\` — **never Git** |
| Reserved future path (FP-0002 production) | `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token` |
| Existing local DEV token filename (historical) | `wpilot-local-shpigovsky.token` — **do not reuse as production authority without explicit rotation charter** |
| Rotation | Revoke in Admin + generate new + replace local file |
| Protected test | Authenticated `site-info` (expects token); public `ping` is unauthenticated |
| Never enter Git | Token plaintext, `.token` files, screenshots with tokens, bridge credentials |

**PROD-P01 actions:** token **not** created; secret file **not** written; no authenticated calls.

**PROD-P02:** local Site Ops contour created (`local\sites\shpigovsky-production\`). Production token file still **not** created at that time.

**PROD-P05-FU01:** production token **reissued once** to `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token`. Authenticated GET **PROVEN**. See [FP-0002-WPILOT-CONNECTION-STATE-v1.md](FP-0002-WPILOT-CONNECTION-STATE-v1.md).

---

## 4. Operator manual actions — NEXT WAVE ONLY

### Gate shape (reconcile-first)

1. Confirm Layer A Beget full backup is still recent enough for a WPilot mutate/upgrade wave.  
2. WP Admin → **Plugins** → locate **MetaCODE WPilot**.  
3. Record and report to MARS: **Version**, visible release/UI label if any, Active/Inactive.  
4. **STOP** — do not generate token, do not toggle bridge/write, do not upload ZIP until MARS returns the exact next charter.  
5. If MARS authorizes **upgrade to 0.3.2-RC1**:  
   - Use ZIP: `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.2-rc1.zip`  
   - Verify SHA-256: `d55c19d6ea1a55cd145e9b67c42ca201c30e4356f08d8cf3932ef6a5ebc80934`  
   - Plugins → Add New → Upload Plugin → install/overwrite per WordPress UI  
   - Activate if required  
   - **STOP** again and report result  
6. Token generation / bridge enable / write enable = **later gates only**.

### If a clean install were ever needed on an empty site (reference only)

Same ZIP/SHA; Upload → Install → Activate → STOP at safe defaults.  
**Not** the assumed path for current Beget copy.

---

## 5. Explicit non-actions (remaining)

P05-FU01 **did** the authorized package replace and one token reissue. Still not done:

- No write enable  
- No business/content WPilot writes  
- No FTP-based plugin copy (native WP Admin replace used)  
- No commit/push  
- No DNS cutover / migration-tail cleanup  

---

## 6. Evidence

- `REPORTS/evidence/prod-p01-beget-read-only-onboarding/wpilot-ping-full.json`  
- `REPORTS/evidence/prod-p01-beget-read-only-onboarding/wpilot-version-reconciliation.json`  
- Package hash recomputed against STORAGE ZIP in PROD-P01  
