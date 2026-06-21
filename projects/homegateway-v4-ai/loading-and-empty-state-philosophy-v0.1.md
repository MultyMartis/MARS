# HomeGateway v4.ai — loading and empty state philosophy v0.1

**Статус:** **DRAFT** · **PLANNING** · **POST-PROTOTYPE**  
**Назначение:** skeleton, reserved layout, calm emptiness — premium cockpit при отсутствии данных.

**Не является:** loading spinner library, API error handling spec.

**Связанные:** [viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md) · [visual-language-direction-v0.1.md](visual-language-direction-v0.1.md) · [information-priority-model-v0.1.md](information-priority-model-v0.1.md)

---

## Why empty states matter

Cheap emptiness («No data» centered on white) **breaks cockpit illusion**.  
Premium HG treats absence as **operational calm** — reserved instruments, not broken SaaS page.

---

## Skeleton philosophy

| Principle | Application |
|-----------|-------------|
| **Shape fidelity** | Skeleton matches final block-screen geometry |
| **Reserved height** | Row/block height fixed before data arrives |
| **No layout jumps** | Shell zones stable on load |
| **Muted motion** | Optional slow pulse — OFF default v0.1 |
| **Token-based** | Uses `--hg-surface` / muted text tokens |

Skeleton lives **inside** block boundaries — not fullscreen spinner replacing cockpit.

---

## Reserved layout spaces

| Zone | Reserved behavior |
|------|-------------------|
| `top_bar` | Always rendered — logo, stubs |
| `main_menu` | Nav items present; disabled until auth mock done |
| `main_area` | Grid slots with skeleton blocks |
| `info_area` | Rail width fixed; 3–5 skeleton rows |
| `system_status` | Placeholder glyphs |

**Viewport-first:** no collapse of shell when content loading ([viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md)).

---

## No layout jumps (CLS discipline)

| Rule | Detail |
|------|--------|
| Block min-height | Per size S/M/L taxonomy |
| Images / icons | Fixed boxes |
| Signal list | Row height constant |
| Theme switch | No reflow of shell grid |

---

## Empty cockpit behavior

| Scenario | Treatment |
|----------|-----------|
| First login / no clients yet | Calm empty `main_area` with **one** guided block — not 12 empty cards |
| No deadlines | `info_area` shows calm «All clear» INFO tone — not error red |
| No leads | Lead block empty state inline |
| Systems unreachable (future) | **stale** state — [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md) |

**Empty cockpit ≠ broken cockpit** — atmosphere and shell remain.

---

## Calm emptiness

| Do | Don't |
|----|-------|
| Short operator-facing copy | Apologetic paragraphs |
| Suggest next action (add client — future admin) | Giant sad icons |
| Maintain glass surfaces | Remove panels leaving holes |
| P3 ambient tone | Alarm styling for empty |

---

## Ambient empty states

Optional subtle background continues — **environment without data**.

Empty `info_area`: muted copy + optional single INFO line — rail **still visible** (width preserved).

---

## Stale / offline placeholders

| State | Display |
|-------|---------|
| **loading** | Skeleton in block |
| **empty** | Calm copy, reserved space |
| **stale** | Last known value + «stale» badge (future integration) |
| **offline** | Display-only degradation; no fake OK |

MARS/bots blocks: prefer **unknown honest** over fabricated green ([AGENTS.md](../../AGENTS.md) status honesty).

---

## Per-zone empty examples (draft copy tone)

| Zone | Empty message direction |
|------|-------------------------|
| `info_area` | «No active signals — clear horizon» |
| Client list | «No clients yet — add when admin ready» |
| MARS block | «MARS summary unavailable — display-only stub» |
| Favorites | «Pin frequent links here» |

RU/EN mix — **SAFE UNKNOWN** final locale.

---

## Relationship to focus states

Loading does not trigger **overlay-open**.  
Empty project overlay: show structured empty sections, not collapse panel.

---

## Anti-patterns

| Anti-pattern | Why |
|--------------|-----|
| Full-screen spinner | Breaks station metaphor |
| Remove rail when empty | Layout jump |
| Flash empty→full | jarring |
| Fake sample data without label | Honesty violation in production; static MVP labels sample |

---

## SAFE UNKNOWN

- Error retry UI — Phase 7 integrations.
- Skeleton animation preference in Settings — future.

---

*Last updated: 2026-05-24 — Loading and empty state philosophy.*
