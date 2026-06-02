# EAR Future Consumers v1

**Purpose:** Document **expected consumers** of EAR snapshots and their **acquisition track preferences** — documentation only, **no** runtime or consumer implementation claims.  
**Status:** architecture guidance — **no** delivery promises.  
**Phase:** 2E  
**Parent:** [EAR-ARCHITECTURE-v1.md](EAR-ARCHITECTURE-v1.md), [EAR-ACQUISITION-TRACKS-v1.md](EAR-ACQUISITION-TRACKS-v1.md)

---

## Consumer stack (unchanged)

All listed consumers sit **above** the Snapshot Package boundary:

```
Operator → EAR → Snapshot → Consumer → Reports / artifacts
```

**DD-2E-04:** Consumers **never bypass EAR** for acquisition.

---

## Expected consumers

| Consumer | Platform / domain | EAR relationship (documented) | Implementation in repo |
|----------|-------------------|-------------------------------|-------------------------|
| **OCPilot** | OpenCart / ocStore | Primary v1 consumer; SITE-001, Run 5 | OCPilot project docs exist; **no** EAR runtime |
| **WPilot** | WordPress | Future read-only acquisition | **SAFE UNKNOWN** depth |
| **Website Factory** | Multi-site production | Future unified intake | **SAFE UNKNOWN** |
| **Landing Pilot** | Landing / static sites | File tree / asset manifest | **SAFE UNKNOWN** |
| **Future CMS Pilots** | Magento, Bitrix, custom, … | Per-platform snapshot spec TBD | **Not claimed** |

This table is **expectation management**, not a product roadmap with dates.

---

## Acquisition preferences (guidance)

Preferences inform **charter defaults** — operator may override per engagement.

| Consumer | Default track bias | Typical modes | Notes |
|----------|-------------------|---------------|-------|
| **OCPilot** | **Hybrid** for active sites; **Offline** for legacy | 0/1 now; 2 when pilot | See [EAR-OCPILOT-INTEGRATION-v1.md](EAR-OCPILOT-INTEGRATION-v1.md) |
| **WPilot** | **Connected** for managed WP; **Offline** for exports | 2 target; 0/1 fallback | Reuse generic snapshot sections where possible — Phase 4 harmonization |
| **Website Factory** | **Connected** at scale; **Offline** for imports | **SAFE UNKNOWN** batch policy | May need multi-site acquisition charter — not designed Phase 2E |
| **Landing Pilot** | **Offline** (archive / repo export) | 0/1 | Live connector need **LOW** unless hosted dynamic assets |
| **Future CMS Pilots** | **Case-by-case** | Per platform spec | New connector classes under Connected track |

---

## OCPilot

| Aspect | Guidance |
|--------|----------|
| **Primary use** | Read-only audit (Run 5, baselines) |
| **Preferred track** | Connected for SITE-001-class; Offline for backup-first |
| **Snapshot spec** | [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md) |
| **Min level** | Run 5: Level 1+ documented for structural work |

---

## WPilot

| Aspect | Guidance |
|--------|----------|
| **Preferred track** | Connected for plugin/theme inventory on live managed sites |
| **Offline fit** | All-in-One WP Export, hosting backup ZIP |
| **Dependency** | Phase 2 EAR OpenCart lessons; WordPress connector catalog **not** written Phase 2E |
| **SAFE UNKNOWN** | Shared vs forked snapshot contract with OpenCart |

---

## Website Factory

| Aspect | Guidance |
|--------|----------|
| **Preferred track** | Connected when maintaining fleet; Offline for client handoff packages |
| **Concern** | Multi-site batch acquisition — outside single-site Phase 2E scope |
| **SAFE UNKNOWN** | Unified factory snapshot ID scheme, Factory↔EAR orchestration |

---

## Landing Pilot

| Aspect | Guidance |
|--------|----------|
| **Preferred track** | **Offline** — static tree, assets, build output archives |
| **Connected** | Only if hosted app with chartered read-only channel |
| **Depth** | Manifest + asset hashes — **SAFE UNKNOWN** vs OpenCart depth |

---

## Future CMS Pilots

| Aspect | Guidance |
|--------|----------|
| **Pattern** | New platform spec + connector classes under Connected; Offline always available |
| **Anti-pattern** | Consumer-specific SFTP logic outside EAR |
| **Governance** | Each pilot gets explicit consumer guide (OCPilot guide as template) |

---

## Cross-consumer rules (normative)

1. **Published snapshot only** — no Evidence Package consumption.
2. **Quality level gating** — consumer-specific phase maps (OCPilot documented; others TBD).
3. **`safe-unknown` discipline** — shared from [EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md).
4. **No credentials in consumer repos** — [EAR-SECURITY-MODEL-v1.md](EAR-SECURITY-MODEL-v1.md).
5. **Track metadata** — optional transparency; not a substitute for quality level.

---

## Phase alignment (documentation)

| Phase | Consumer impact |
|-------|-----------------|
| **2E** (this) | Two-track model for all consumers |
| **3** | Connected pilot — OCPilot first beneficiary |
| **4** (roadmap) | Unified snapshot contract — Factory + WPilot |
| **5** (roadmap) | Write-mode evaluation — **not** acquisition default |

See [EAR-ROADMAP-v1.md](EAR-ROADMAP-v1.md) — phases are **not** promises.

---

## SAFE UNKNOWN

- Consumer priority order for first runtime connector — likely OCPilot; confirm in Phase 3 charter.
- Whether Factory shares OCPilot external storage roots — storage policy.
- Licensing of third-party CMS connector development — organizational.

---

## Cross-references

| Document | Use |
|----------|-----|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Consumer table |
| [EAR-ACQUISITION-SELECTION-GUIDE-v1.md](EAR-ACQUISITION-SELECTION-GUIDE-v1.md) | Track selection |
