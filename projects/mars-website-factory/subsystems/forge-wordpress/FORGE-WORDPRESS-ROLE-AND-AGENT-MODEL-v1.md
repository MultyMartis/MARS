# Forge WordPress — Role and Agent Model v1

**Document type:** Role registry (no agent registration)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-01

**Principle:** Minimal system — one primary implementation specialist + reusable skills + independent validators + human approval. **No agent army.**

---

## 1. Role registry

| Role | Phase 1 need | Merge candidate | Skill candidate | Validator | Human-only | Notes |
|------|--------------|-----------------|-----------------|-----------|------------|-------|
| **Forge WordPress Architect** | **Yes** | — | Partial (spec compile) | No | Gate authority | Owns WAD, spec, packaging |
| **Content Modeler** | **Yes** | With Architect on small projects | ACF/CPT assist | No | Approval on model | High-risk role |
| **Theme Implementation Specialist** | **Yes** (design); impl deferred | Primary future agent | Theme scaffold | No | Merge review | Future **primary agent** |
| **Admin UX Specialist** | **Yes** | With Content Modeler | Editor map assist | No | Client-facing approval | |
| **WordPress Validator** | **Yes** | — | WV runners | **Yes** | WV blockers | Must not implement same build |
| **Visual Parity Validator** | **Yes** | — | Screenshot diff | **Yes** | PIXEL_PERFECT sign-off | Independent from implementer |
| **Security Reviewer** | **Yes** | With WordPress Validator | PHPCS/security scan | **Yes** | WV4 failures | |
| **WPilot Handoff Reviewer** | **Yes** | — | Manifest check | **Yes** | **Final handoff** | **HUMAN ONLY** at G10 |

---

## 2. Merge guidance (small projects)

| Combined hat | When acceptable |
|--------------|-----------------|
| Architect + Content Modeler | Single brochure site; WAD documents merge |
| Architect + Theme Specialist (design only) | Trivial template count |
| WordPress Validator + Security Reviewer | **Not** merged at implementation review — same person may run tools but **independent review** required for WV4 on non-trivial projects |

**Never merge:** Implementer + Visual Parity Validator on same delivery.

---

## 3. AG-WP-001 disposition

| Field | FW-01 decision |
|-------|----------------|
| **Registration** | **NOT REGISTERED** |
| **Role** | Internal seed — methodology source |
| **Promotion path** | FW-05 pilot charter may promote **Theme Implementation Specialist** agent; seed informs prompts, not registry row |
| **vs MARS Forge** | Unrelated — no shared agent |

---

## 4. Future agent model (documentation only)

```text
Phase 1 (FW-01–FW-04):  Human roles + methodology + skills design
Phase FW-05 pilot:       Optional single "Forge WordPress Implementation" agent charter
Post-pilot:              Validators remain separate or skill-based — not absorbed into implementer
```

| Future agent | Status | Charter required |
|--------------|--------|------------------|
| Primary implementation specialist | **CANDIDATE** | Yes — FW-05+ |
| Validator agents | **REJECT** as autonomous — validators stay human-gated skills |
| WPilot operations agent | **OUT OF SCOPE** — WPilot separate |

---

## 5. Skills vs agents boundary

| Fits **skill** | Fits **agent** (future) |
|----------------|---------------------------|
| Checklist execution | Multi-step implementation under spec |
| Manifest diff | Branch-wide theme/plugin edits |
| Report generation | Iterative fix loops with human merge |
| PHPCS/Playwright runner | — |

FW-02 defines skill **names and contracts** — FW-01 does not create skills.

---

## 6. Research alignment

| Research finding | MARS adaptation |
|------------------|-----------------|
| Human-supervised engineering systems | **ADOPT** — all roles human-gated |
| Subagents for specialized tasks | **ADAPT** — skills first, not agent swarm |
| PR-gated merge | **ADOPT** — implementer ≠ merger |

---

## Related documents

- [FORGE-WORDPRESS-CAPABILITY-MODEL-v1.md](FORGE-WORDPRESS-CAPABILITY-MODEL-v1.md)
- [FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md](FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md)

---

*Role model v1 — no agents registered.*
