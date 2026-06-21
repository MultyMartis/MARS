# HomeGateway v4.ai — visual anti-patterns v0.1

**Статус:** **DRAFT** · **PLANNING** · Lane B  
**Назначение:** канон **визуальных опасностей** — detection, why dangerous, mitigation philosophy.

**Не является:** automated linter, design review tool.

**Связанные:** [visual-direction-exploration-pack-v0.1.md](visual-direction-exploration-pack-v0.1.md) · [layout-variants-analysis-v0.1.md](layout-variants-analysis-v0.1.md) · [cognitive-load-and-density-notes-v0.1.md](cognitive-load-and-density-notes-v0.1.md)

---

## How to use this document

Before static MVP and any mood board:

1. Scan UI against **detection cues**.
2. If matched — apply **mitigation philosophy** (not one-off pixel hacks).
3. Escalate repeated drift to operator review.

---

## Anti-pattern catalog

### 1. SaaS dashboard drift

| Aspect | Detail |
|--------|--------|
| **Why dangerous** | Collapses spatial cockpit into widget wall; destroys tri-focus |
| **How it appears** | Equal card grid; KPI vanity blocks; «overview» hero |
| **Detection** | Screenshot works as generic analytics product; no left/center/right roles |
| **Mitigation** | Restore zone roles; block-screens as instruments; [cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md) |

---

### 2. Enterprise admin drift

| Aspect | Detail |
|--------|--------|
| **Why dangerous** | Gray table dominance; operator becomes data clerk |
| **How it appears** | Full-width dense tables as home; breadcrumb hell |
| **Detection** | Main view is CRUD table without operational canvas |
| **Mitigation** | Admin as future layer; `main_area` = work; admin entry in `top_bar` only |

---

### 3. Cyberpunk overload

| Aspect | Detail |
|--------|--------|
| **Why dangerous** | Neon illegibility; adrenaline; signal semantics lost |
| **How it appears** | Cyan+magenta everywhere; hex grids; glitch effects |
| **Detection** | Cannot read body text on glass; eyes tired in 5 min |
| **Mitigation** | Signal-only color; neutral chrome; [color-behavior-and-accent-philosophy-v0.1.md](color-behavior-and-accent-philosophy-v0.1.md) |

---

### 4. RGB gamer UI

| Aspect | Detail |
|--------|--------|
| **Why dangerous** | Wrong emotional target; undermines professional trust |
| **How it appears** | Rainbow borders; cycling accents; pulsing RGB logos |
| **Detection** | Looks like gaming peripheral software |
| **Mitigation** | Single accent family; no cycles; [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md) glow rules |

---

### 5. Fantasy hologram clichés

| Aspect | Detail |
|--------|--------|
| **Why dangerous** | Movie prop over scan speed; «fake future» |
| **How it appears** | Scanlines, hologram blue UI, floating wireframes, AI brain bg |
| **Detection** | UI could be sci-fi movie still without data |
| **Mitigation** | Architectural glass; no scanlines; [background-and-environment-philosophy-v0.1.md](background-and-environment-philosophy-v0.1.md) |

---

### 6. Giant card-grid syndrome

| Aspect | Detail |
|--------|--------|
| **Why dangerous** | Equal emphasis → overload; dashboard psychology |
| **How it appears** | 12 same-size cards; Masonry vanity |
| **Detection** | No P1 center; all blocks same visual weight |
| **Mitigation** | Tri-focus; P-tier sizing; mode-dependent density |

---

### 7. Over-glassification

| Aspect | Detail |
|--------|--------|
| **Why dangerous** | Illegibility; Apple-clone without contrast budget |
| **How it appears** | Invisible panels; text on pure blur |
| **Detection** | WCAG fail; squint to read |
| **Mitigation** | Alpha floor; denser overlay panels; [surface-material-language-v0.1.md](surface-material-language-v0.1.md) |

---

### 8. Glow spam

| Aspect | Detail |
|--------|--------|
| **Why dangerous** | Fatigue; CRITICAL loses meaning |
| **How it appears** | Every hover glows; red panels; bloom |
| **Detection** | More than one glow focal per region |
| **Mitigation** | One elevation focal; badge-only signal light |

---

### 9. Animation overload

| Aspect | Detail |
|--------|--------|
| **Why dangerous** | Breaks calm-control; alert anxiety |
| **How it appears** | Staggered cascades; blink; parallax chrome |
| **Detection** | Motion noticed constantly during idle work |
| **Mitigation** | [motion-atmosphere-v0.1.md](motion-atmosphere-v0.1.md); charter timing |

---

### 10. Sci-fi movie prop aesthetics

| Aspect | Detail |
|--------|--------|
| **Why dangerous** | Style over operator task; illegible fantasy type |
| **How it appears** | Orbitron body text; fake 3D globes as hero |
| **Detection** | Demo impresses non-operators only |
| **Mitigation** | Exo 2; real data density; restraint |

---

### 11. Sterile Apple-clone minimalism

| Aspect | Detail |
|--------|--------|
| **Why dangerous** | Loses cockpit depth and identity; feels like generic app |
| **How it appears** | Pure white, no atmosphere, tiny gray text |
| **Detection** | Could be iOS settings; no tactical periphery |
| **Mitigation** | Environmental depth without noise; tri-focus visible |

---

### 12. CRM / pipeline drift

| Aspect | Detail |
|--------|--------|
| **Why dangerous** | Wrong product metaphor for solo operator cockpit |
| **How it appears** | Kanban columns, deal stages as home |
| **Detection** | Sales pipeline is hero UI |
| **Mitigation** | Project/deadline operational model; [product-positioning-v0.1.md](product-positioning-v0.1.md) |

---

### 13. Notification / inbox drift

| Aspect | Detail |
|--------|--------|
| **Why dangerous** | Interrupt culture; dismiss-to-zero psychology |
| **How it appears** | Unread badges; feed chronology; modal stack |
| **Detection** | `info_area` behaves like Slack |
| **Mitigation** | [tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md) |

---

### 14. Fake AI visual clichés

| Aspect | Detail |
|--------|--------|
| **Why dangerous** | Marketing «AI product» over operational trust |
| **How it appears** | Sparkle icons, brain networks, purple gradients «AI» |
| **Detection** | Branding screams AI without function |
| **Mitigation** | Ambient intelligence via calm system UI — no mascots |

---

### 15. AI startup aesthetic

| Aspect | Detail |
|--------|--------|
| **Why dangerous** | Landing-page gradient + glass cards ≠ cockpit |
| **How it appears** | Purple-blue mesh gradient, huge hero CTA |
| **Detection** | Marketing site with login button |
| **Mitigation** | Viewport station; operator density |

---

## Mitigation philosophy (global)

| Principle | Action |
|-----------|--------|
| **Spatial first** | Fix layout role before polish |
| **Signal honesty** | Color = meaning |
| **Restraint budget** | One strong emphasis per region |
| **Operator time scale** | Review at 30 min, not 30 sec demo |
| **Reference filter** | [reference-analysis-and-visual-boundaries-v0.1.md](reference-analysis-and-visual-boundaries-v0.1.md) |

---

## Review checklist (quick)

- [ ] Tri-focus readable in grayscale screenshot?
- [ ] Signal colors only on semantics?
- [ ] Background calm at P3?
- [ ] No blink/pulse on CRITICAL?
- [ ] Exo 2 body readable on glass?
- [ ] Could this be mistaken for Dribbble SaaS?

---

## SAFE UNKNOWN

- Automated screenshot regression — not implemented.
- Operator formal design review cadence — TBD.

---

*Last updated: 2026-05-24 — Visual anti-patterns.*
