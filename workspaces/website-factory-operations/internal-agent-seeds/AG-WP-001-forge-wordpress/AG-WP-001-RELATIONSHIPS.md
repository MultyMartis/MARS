# AG-WP-001 — Forge WordPress Relationship Map

**Agent ID:** AG-WP-001  
**Status:** SEED  
**Date:** 2026-06-11  

**Rule:** Только **подтверждённые** связи из in-repo evidence. Planned/future — помечены явно.

---

## Confirmed relationships

### Website Factory → Forge WordPress

| Aspect | Evidence |
|--------|----------|
| **Parent → internal seed** | Website Factory — производственная система; Forge WordPress — Internal Agent Seed в LOC-ZONE `workspaces/website-factory-operations/` |
| **Not standalone** | Seed не зарегистрирован в `agents/registry.md`; не отдельный `projects/` charter |
| **Documentation zone** | Factory Authorized Records: [README.md](../../README.md) |

```text
  Website Factory (methodology + operations)
           │
           │  internal direction (SEED)
           ▼
  Forge WordPress (AG-WP-001)
```

---

### Forge WordPress → WPilot

| Aspect | Evidence |
|--------|----------|
| **Technical Companion** | Зафиксировано в seed passport; детали — [AG-WP-001-WPILOT-CONNECTION.md](AG-WP-001-WPILOT-CONNECTION.md) |
| **Complementary, not same** | WPilot: `projects/wpilot/README.md` — human-supervised WordPress admin tool; Forge: expertise direction |
| **WPilot → Factory (planned)** | WPilot README: «planned upstream source for Factory-native WordPress payloads» — **planned**, not runtime |

```text
  Forge WordPress (expertise / production direction)
           │
           │  uses / aligns with (not replaces)
           ▼
  WPilot (instrumental bridge)
```

---

### FP-0002 → Forge WordPress Learning Source

| Aspect | Evidence |
|--------|----------|
| **First Learning Project** | [FP-0002-PROJECT-PASSPORT.md](../../FP-0002-SHPIGOVSKY/FP-0002-PROJECT-PASSPORT.md) |
| **Learning charter** | [WORDPRESS-PRODUCTION-LEARNING-CHARTER.md](../../FP-0002-SHPIGOVSKY/WORDPRESS-PRODUCTION-LEARNING-CHARTER.md) |
| **Knowledge routing** | [KNOWLEDGE-EXTRACTION/](../../FP-0002-SHPIGOVSKY/KNOWLEDGE-EXTRACTION/) — post-hoc containers |
| **Agent-specific container** | [KNOWLEDGE-EXTRACTION/wordpress-agent/](../../FP-0002-SHPIGOVSKY/KNOWLEDGE-EXTRACTION/wordpress-agent/) |

```text
  FP-0002 (Shpigovsky.ru delivery)
           │
           │  post-hoc pattern extraction (when delivery allows)
           ▼
  Forge WordPress knowledge accumulation
```

---

### WordPress Knowledge Extraction → Forge WordPress

| Aspect | Evidence |
|--------|----------|
| **Extraction discipline** | FP-0002 KNOWLEDGE-EXTRACTION folders — empty by design until production evidence |
| **wordpress-agent container** | Dedicated sink for Forge WordPress-oriented learnings from FP-0002 |
| **Sibling containers** | `wp-patterns/`, `acf-patterns/`, `theme-patterns/`, `deployment-patterns/`, `wpilot-improvements/` — project-level, may feed Forge indirectly |

```text
  KNOWLEDGE-EXTRACTION/ (FP-0002)
    ├── wp-patterns/          ─┐
    ├── acf-patterns/         ─┼─▶ may inform Forge (evidence-based)
    ├── theme-patterns/       ─┤
    ├── deployment-patterns/  ─┤
    ├── wpilot-improvements/  ─┘ (WPilot evolution, not Forge rules)
    └── wordpress-agent/      ──▶ Forge WordPress seed sink
```

---

## Related systems (not parent-child)

| System | Relationship to Forge WordPress | Status |
|--------|--------------------------------|--------|
| **ATLAS** | Registry refs for FP-0002 (PRJ-0012, WEB-SHPIG-01) — project context only | **confirmed** refs; Forge **does not** own ATLAS |
| **Gulp Frontend Agent / MARS Forge** | Upstream Frontend lanes | **confirmed** Factory agents; WordPress is downstream **intent** |
| **OCPilot** | Sibling CMS pilot family (OpenCart) | **no** direct Forge coupling evidenced |
| **EAR Runtime** | Future acquisition snapshots | **SAFE UNKNOWN** for WordPress path |

---

## Not established (do not claim)

| Claim | Status |
|-------|--------|
| Forge WordPress registered in `agents/registry.md` | **Not established** |
| Automated handoff Frontend → WordPress | **Not established** |
| WPilot plugin live on FP-0002 | **SAFE UNKNOWN** |
| Forge WordPress operational doc pack | **Not established** |

---

*Relationship map for SEED only. No runtime graph.*
