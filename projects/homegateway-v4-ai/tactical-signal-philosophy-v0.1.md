# HomeGateway v4.ai — tactical signal philosophy v0.1

**Статус:** **DRAFT** · **PLANNING** · **POST-PROTOTYPE**  
**Назначение:** каноническая роль **`info_area`** и операторской психологии тактических сигналов.

**Не является:** alerting product, push service, automation engine, inbox UI.

**Связанные:** [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md) (levels + sample data) · [cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md) · [information-priority-model-v0.1.md](information-priority-model-v0.1.md)

---

## Canonical definition: `info_area`

### `info_area` IS

- **Peripheral tactical awareness system** — оператор держит «радар» в периферии.
- **Ambient operational intelligence layer** — сжатые, приоритизированные сигналы о времени, риске, recurring.
- **Companion to `main_area`** — не заменяет работу, дополняет осведомлённость.

### `info_area` IS NOT

| Anti-pattern | Why rejected |
|--------------|--------------|
| Notification center | Implies dismiss-to-zero, badge wars, interrupt culture |
| Inbox | Implies read/unread workflow, reply semantics |
| Feed / news column | Implies chronological noise, engagement scrolling |
| Social timeline | Irrelevant to solo operator cockpit |
| Alert modal stack | Breaks calm-control; use sticky critical, not popups |

---

## Operator psychology (intended)

| Goal | Design stance |
|------|---------------|
| **Situational awareness without anxiety** | Levels are calm by default; escalation is **earned** by proximity/overdue |
| **Peripheral cognition** | Right rail scanned in < 3 s on morning entry ([cognitive-load-and-density-notes-v0.1.md](cognitive-load-and-density-notes-v0.1.md)) |
| **Trust through persistence** | OVERDUE does not vanish until human resolve |
| **No alert fatigue** | Anti-blink, anti-neon, anti-every-row-red |
| **Mission board, not calendar widget** | Rows = operational commitments with client/project context |

Оператор должен чувствовать: *«Я вижу риски, но кокпит не кричит»*.

---

## Canonical signal levels

Согласовано с [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md):

| Level | Operator feeling | Typical use in `info_area` |
|-------|------------------|----------------------------|
| **INFO** | В плане, фон | Distant deadlines, ambient system OK |
| **WATCH** | Периодически проверить | Approaching work, recurring prep |
| **WARNING** | Риск срыва | 3–7 days, content freeze, approval pending |
| **CRITICAL** | Сегодня / завтра — внимание | `due-today` band; strong token, no fullscreen |
| **OVERDUE** | Не исчезает | Persistent row until admin resolve (future) |

### Orthogonal states

| State | Notes |
|-------|-------|
| **due-today** | May coincide with CRITICAL; badge «Today» |
| **upcoming** | «in Nd» muted copy |
| **overdue** | Negative days; sort weight highest |

---

## Severity ordering (display)

**Default sort in `info_area` preview:**

1. OVERDUE (pinned section top)
2. CRITICAL (+ due-today)
3. WARNING
4. WATCH
5. INFO

Within band: by date proximity, then client/project name (stable tie-break).

**Filter rule:** filters on Tactical full view **never hide** OVERDUE section.

---

## Persistence philosophy

| Rule | Rationale |
|------|-----------|
| OVERDUE survives mode switch | Danger context in Focus ([operational-focus-state-model-v0.1.md](operational-focus-state-model-v0.1.md)) |
| No auto-dismiss of CRITICAL | Human snooze only (future admin) |
| Sticky critical logic | Max 1–2 rows with elevated chrome; not all rows CRITICAL-colored |
| Sample v0.1 | Manual `data-hg-signal-level`; automation Phase 6+ |

---

## Tactical grouping

| Group | Content |
|-------|---------|
| **Immediate risk** | OVERDUE + CRITICAL |
| **Horizon** | WARNING + WATCH |
| **Ambient** | INFO + system hints (sparse) |
| **Recurring wave** | Monthly reports — separate subsection in full Tactical view |

Rail preview: top **5–8** rows across groups, not full database.

---

## Signal lifetime concepts (draft)

| Phase | Behavior |
|-------|----------|
| **Born** | Item enters at computed/manual level |
| **Escalate** | INFO → WATCH → WARNING → CRITICAL by proximity (future automation) |
| **Peak** | due-today / CRITICAL day |
| **Overdue** | Level locks OVERDUE; row styling persistent |
| **Resolve** | Human marks done in admin (future) — row leaves active set |
| **Archive** | History timeline Phase 7 — **not** v0.1 |

**No** «fade away because old» for unresolved OVERDUE.

---

## Hybrid delivery model (canonical)

| Surface | Role |
|---------|------|
| **`info_area` rail** | Preview 5–8 rows on Main / shared shell |
| **Full Tactical view** | Filters, recurring, full lists ([wireframes/tactical-signals-wireframe-v0.1.md](wireframes/tactical-signals-wireframe-v0.1.md)) |
| **Top global chip** | OVERDUE count — single persistent strip ([cognitive-load-and-density-notes-v0.1.md](cognitive-load-and-density-notes-v0.1.md)) |
| **Overlay (optional L3)** | Single signal detail — rare |

---

## Future: compact / collapsed rail

| Mode | Behavior (planned) |
|------|-------------------|
| **Expanded rail** | Default wide desktop |
| **Compact rail** | Icons + counts + worst level dot |
| **Collapsed chip** | Focus mode — overdue chip only on `top_bar` |
| **Tactical-only** | Full `view-tactical-signals` when rail insufficient (monthly wave) |

**SAFE UNKNOWN:** breakpoint triggers; animation on collapse ([motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md)).

---

## Anti-alert-fatigue rules

| Do | Don't |
|----|-------|
| Token color + icon + label | Color-only rows |
| One global overdue chip | Multiple screaming banners |
| Calm INFO typography | Exclamation on every row |
| Restrained motion | Blink, pulse loops |
| Pin OVERDUE section | Auto-clear on login |
| Escalate by rules | Manual «mark all critical» |

---

## Relationship to systems signals

MARS / n8n / bot status **primarily** live in `main_area` (Systems blocks). `info_area` may show **cross-cutting** deadline-like or operator-task signals — not duplicate full NOC grid.

Display-only integration future — [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md) § system signals.

---

## SAFE UNKNOWN

- Push notifications — not decided.
- Snooze semantics — Phase 6 admin.
- Sound/haptic — out of scope v0.1.
- Empirical operator testing — not conducted.

---

*Last updated: 2026-05-24 — Tactical signal philosophy canon.*
