# REPORT — SITE-001 WF-V3 Homepage Decision v1

**Type:** Homepage program decision — documentation only  
**Date:** 2026-06-11  
**Site:** SITE-001 — Автосалон СИБКАР  
**Program:** Website Factory · WF-V3  

**Inputs:**

- [SITE-001-WFV3-HOMEPAGE-DISCOVERY-v1.md](SITE-001-WFV3-HOMEPAGE-DISCOVERY-v1.md)
- [SITE-001-WFV3-HOMEPAGE-BLUEPRINT-v1.md](SITE-001-WFV3-HOMEPAGE-BLUEPRINT-v1.md)
- [SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md](../governance/SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md)
- [SITE-001-WFV3-HOMEPAGE-PROTOTYPE-CHARTER-v1.md](../governance/SITE-001-WFV3-HOMEPAGE-PROTOTYPE-CHARTER-v1.md)

**Explicit exclusions (honored):** No prototype · No implementation · No commit implied

---

# FINAL DECISION

## **A — Ready for Homepage Prototype**

Homepage discovery and blueprint are **complete**. PDP design authority is **sufficient** to inherit. No new design language required or authorized.

---

## Justification

| Question | Answer |
|----------|--------|
| Is discovery complete? | **YES** — purpose, class, 3-second test, IA, strategies documented in discovery + blueprint v1 |
| Is PDP authority sufficient? | **YES** — freeze v1 defines header, footer, tokens, trust, CTA, Class B; homepage charter defines scope |
| Can prototype start without new concept PNG? | **YES** — charter explicitly allows derivation from PDP + discovery + blueprint |
| Is Class B still valid for Homepage? | **YES** — validated and frozen in discovery §2 |
| Does homepage invent new visual class? | **NO** — alignment table maps H0–H10 to PDP Z0–Z10 grammar |

### Why not B (Discovery incomplete)

All 12 prompt sections are addressed across discovery and blueprint artifacts. Business persona, task ranking, anti-patterns, and TEST baseline gaps are documented with evidence citations.

### Why not C (PDP authority insufficient)

PDP freeze status: Architecture **COMPLETE**, Visual System **COMPLETE**, Asset Layer **PARTIAL** (acceptable for prototype placeholders). Header/footer/trust/CTA models are frozen and directly mappable to homepage zones. Homepage does not require PDP anatomy changes.

---

# Preconditions Before Implementation (not blockers to decision A)

Decision **A** authorizes **next planning stage** (Homepage Prototype Write Charter + workspace). Implementation still requires:

| # | Precondition | Status |
|---|--------------|--------|
| 1 | Operator ratification of homepage charter | **OPEN** |
| 2 | Operator ratification of discovery + blueprint v1 | **OPEN** |
| 3 | Homepage Prototype Write Charter document | **NOT CREATED** |
| 4 | Workspace scaffold (`workspaces/site-001-wf-v3-homepage-prototype/` or shared PDP workspace) | **NOT STARTED** |
| 5 | Above-fold single-red resolution (header callback vs search submit) | **OPEN** — operator HITL at v0.1 |
| 6 | `qa/README.md` screenshot policy | **OPEN** |

---

# Blockers (implementation — not discovery)

| Blocker | Severity | Notes |
|---------|----------|-------|
| Operator HITL `VISUAL_ACCEPT` on prior waves | Medium | P0-02 — prototype isolated until ACCEPT; does not block charter |
| No homepage concept PNG | Low | Mitigated — PDP PNG + blueprint ASCII |
| Featured inventory static content | Low | Prototype uses placeholder vehicles |
| Mobile layout authority | Low | Desktop-first per freeze; responsive deferred |

**No blockers prevent authoring Homepage Prototype Write Charter.**

---

# Recommended Sequence

```text
1. Operator reviews discovery + blueprint + this decision     ← HITL
2. Ratify homepage charter (if not done)
3. Create SITE-001-WFV3-HOMEPAGE-PROTOTYPE-WRITE-CHARTER-v1
4. Create homepage workspace — extend PDP partials (header/footer/tokens)
5. Build homepage v0.1 desktop static HTML
6. Side-by-side HITL: Homepage + frozen PDP
7. If ACCEPT → catalog card prototype
8. Integration charter — explicitly deferred
```

---

# Risk Summary

| Risk | Mitigation |
|------|------------|
| Header/hero red CTA conflict (P-09) | Documented in blueprint §9; operator choice at v0.1 |
| Carousel regression | Charter + discovery anti-patterns; HITL checklist |
| Search decorative only | P-05 gate in success criteria |
| Homepage drift from PDP | Shared partials mandate in charter |

---

# Artifacts Produced (this program step)

| File | Role |
|------|------|
| [SITE-001-WFV3-HOMEPAGE-DISCOVERY-v1.md](SITE-001-WFV3-HOMEPAGE-DISCOVERY-v1.md) | Purpose, class, 3-second test, evidence |
| [SITE-001-WFV3-HOMEPAGE-BLUEPRINT-v1.md](SITE-001-WFV3-HOMEPAGE-BLUEPRINT-v1.md) | IA, strategies, alignment, ASCII, success criteria |
| [SITE-001-WFV3-HOMEPAGE-DECISION-v1.md](SITE-001-WFV3-HOMEPAGE-DECISION-v1.md) | This decision record |

---

## UNKNOWN / SECURITY

| Item | Status |
|------|--------|
| Operator acceptance of decision A | **SAFE UNKNOWN** — pending HITL |
| Shared vs separate homepage workspace | **OPEN** — write charter |
| Exact Phase 1 copy for benefit row items | **PARTIAL** — verify against TEST twig at implementation |

**SECURITY RISK:** None (documentation only).

---

*SITE-001 WF-V3 Homepage Decision v1 — documentation only; no implementation; no commit implied.*
