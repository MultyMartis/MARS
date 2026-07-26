# METALLKA — WPilot Compatibility Assessment v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** UPDATED — Phase 4C-R1: production auth + read-only REST **PROVEN**; final posture `dev_confirmed=true` / `bridge_enabled=true` / `write_enabled=false`  
**Date:** 2026-07-26  
**Package:** `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc6.zip`  
**SHA-256 verified (Phase 4A + 4B + FIX01 vs i-seo):** `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` (**MATCH**)  
**Source:** `X:\AI MARS\projects\wpilot\plugin\metacode-wpilot\` (v0.3.0 / `0.3.0-RC6` / schema 0.2.0)  
**Source↔package byte identity:** **27 / 27** exact match (Phase 4A)  
**i-seo.su runtime CODE (FIX01):** **identical** to package + metallka install (aggregate `f2be244567da7c0c69e210f3b7a4dce1680889ce79f5d6c1dfd9654db3ee37ed`)

---

## Decision

# INSTALL PROVEN (bounded Phase 4B) + READ CONNECTION PROVEN (Phase 4C-R1)

Prior Phase 4A label **CONDITIONALLY READY** remains historically correct for pre-install readiness. Phase 4B executed install/activate/token on metallka.ru with safe defaults preserved and REST not run. Phase 4C-R1 proved authenticated read REST under charter-authorized confirmation + bridge with writes off.

---

## Presence

### Pre-install (Phase 4B immediate recheck)

| Check | Result |
|-------|--------|
| Installed | **NO** (pre-install) |
| Ghost directories | **NO** |
| `wpilot_options` | **ABSENT** |
| WPilot tables | **NONE** |
| REST ns collision | **NONE** (`wpilot/v1` absent from public index) |

### Post-install (Phase 4B)

| Check | Result |
|-------|--------|
| Installed / active | **YES / YES** |
| Version / schema | **0.3.0 / 0.2.0** |
| Token | **YES** (local-only; not REST-tested) |
| `bridge_enabled` / `write_enabled` / `dev_confirmed` | **false / false / false** |
| REST smoke | **NOT RUN** |

### Post-FIX01 reconciliation (2026-07-26)

| Check | Result |
|-------|--------|
| i-seo production identity | **0.3.0-RC6** (not a newer unpublished build) |
| METALLKA CODE == ISEO CODE | **YES** |
| Metallka CODE update executed | **NO** (already identical) |
| Safe defaults / token | **preserved** |
| Gate E | **later authorized (Phase 4C)** |

### Post–Gate E (Phase 4C, 2026-07-26)

| Check | Result |
|-------|--------|
| Gate E approval | **RECEIVED** — `APPROVE METALLKA WPILOT GATE E — BRIDGE AND READ-ONLY REST SMOKE` |
| Source read gate | Authenticated reads require **`bridge_enabled` AND `dev_confirmed`** |
| Bridge-only sufficient? | **NO** |
| `dev_confirmed` authorized by Gate E? | **NO** — charter forbids inferred toggle |
| Bridge enable executed | **NO** (STOP before mutation) |
| Authenticated REST | **0** |
| Auth / read smoke | **NOT PROVEN** |
| `bridge` / `write` / `dev_confirmed` | **false / false / false** (unchanged) |
| Public `/ping` snapshot | installed; state `disabled`; flags OFF |
| Outcome | **BLOCKED — CURRENT RC6 READ GATE REQUIRES DEV_CONFIRMATION NOT AUTHORIZED BY GATE E** |

### Post–4C-R0 semantics (2026-07-26)

| Check | Result |
|-------|--------|
| `dev_confirmed` functional meaning | Operator confirmation gate for `operational_readiness` — **not** auto env detector |
| Admin label | “I confirm this is a DEV/test WordPress site, not production.” — **historically misleading** for production Site Ops |
| Production use verdict | **SAFE WITH CONDITIONS** |
| Public `/ping` 200 | Presence only — **not** auth proof |
| Read-only target | `dev_confirmed=true` + `bridge_enabled=true` + `write_enabled=false` |
| Backup vs write gate | Backup **not** gated by `write_enabled` — must remain forbidden in read smoke |
| Gate E retry charter | **PREPARED** — [METALLKA-WPILOT-GATE-E-RETRY-CHARTER-v1.md](METALLKA-WPILOT-GATE-E-RETRY-CHARTER-v1.md) |
| Retry execution (as of 4C-R0) | **NOT AUTHORIZED** (historical) |
| Production flags after 4C-R0 | **unchanged** (false/false/false) |

### Post–4C-R1 Gate E retry (2026-07-26)

| Check | Result |
|-------|--------|
| Approval | `APPROVE METALLKA WPILOT GATE E RETRY — SET PRODUCTION CONFIRMED + BRIDGE / READ-ONLY REST ONLY` |
| Settings saves | **1** (`save_bridge` → T/T/F) |
| Token auth | **PROVEN** |
| Authenticated GET smoke | ping / site-info / themes / plugins / pages — **PASS** (5) |
| Page 52 represented | **YES** |
| Connection tracking | **PROVEN** (last endpoint `pages`; last token use observed) |
| Final flags | **dev_confirmed=true · bridge_enabled=true · write_enabled=false** |
| Writes | **BLOCKED** / **NOT TESTED** |
| Rollback | **not required** |
| Outcome | **COMPLETE — WPILOT PRODUCTION AUTH + READ-ONLY REST PROVEN** |

---

## Compatibility factors

| Factor | Assessment |
|--------|------------|
| WordPress 7.0.2 | **Compatible** — install/activation + auth reads succeeded |
| PHP HTTP runtime 8.3.20 | **Compatible** in practice on metallka; hard `Requires PHP` header remains **SAFE UNKNOWN** as formal claim |
| Hard `Requires at least` (WP) | **SAFE UNKNOWN** — do not invent formal minimums |
| The7 11.6.0.1 + WPBakery 6.10.0 | **OK for install + read** — page 52 inventory visible via `/pages`; complex `vc_raw_html` remains high-risk for **writes** |
| Activation hook | Forced safe defaults false; options/schema created as designed |
| REST registration | Present when active; authenticated reads **proven** under T/T/F |
| Token management (RC6) | Proven: token generated without bridge/dev/write (4B); reused successfully (4C-R1) |
| REST API availability | Public `/wp-json/` **200**; public `/wpilot/v1/ping` **200**; authenticated reads **200** |
| Security plugin hard block | Clearfy active — no auth-read blocker observed in 4C-R1 |
| Proxy / CDN | No Cloudflare evidenced |
| `Authorization` forwarding | `.htaccess` maps `HTTP_AUTHORIZATION` — metallka used `X-WPilot-Token` successfully |
| `X-WPilot-Token` feasibility | **PROVEN** on metallka (4C-R1) |
| `dev_confirmed` vs production | **SAFE WITH CONDITIONS** — operator confirmation prerequisite; production use authorized and executed under 4C-R1 |
| Uninstall cleanup | **No `uninstall.php`** — residual options/tables likely after delete |

---

## Conditions satisfied for Phase 4B

1. Exact approval: `APPROVE METALLKA WPILOT INSTALL — RC6 INSTALL ACTIVATE TOKEN ONLY` — **received**  
2. Fresh Beget backup operator confirmation — **received**  
3. Package SHA re-match at execution — **MATCH**  
4. WPilot absent immediately before install — **confirmed**  
5. Bridge / REST / writes remained **NOT AUTHORIZED** — **honored (REST=0)**  
6. Residual schema/options cleanup limitation — accepted  
7. Beget panel credentials still incomplete — backup proof remained operator-attested  

---

## Blockers?

**No hard compatibility blocker** for bounded RC6 install/activate/token-only onboarding — **proven by Phase 4B**.

**Historical Gate E procedural blocker (Phase 4C):** authenticated reads require `dev_confirmed=true`, which Gate E did not authorize — **resolved by 4C-R0 semantics + 4C-R1 authorized retry**.

Remaining holds: WPilot **writes** / write enable / backup / dry-run / scoped-replace / rollback — **BLOCKED** pending Phase 4D+ charter.

---

## Explicit non-actions remaining

No write enable · no WPilot content mutation · no backup/dry-run/scoped-replace/rollback endpoint calls · no Phase 4D auto-start.

---

*WPilot Compatibility Assessment v1 · Phase 4B INSTALL PROVEN · FIX01 CODE match · Phase 4C Gate E BLOCKED (historical) · Phase 4C-R0 semantics SAFE WITH CONDITIONS · Phase 4C-R1 AUTH + READ REST PROVEN · writes BLOCKED.*
