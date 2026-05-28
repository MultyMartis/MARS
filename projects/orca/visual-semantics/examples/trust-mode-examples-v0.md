# Trust Mode Examples v0

Real Triumph-derived patterns only.

## Example 1 — Blueprint intent (not as-built zakaz hero)

```yaml
trust_mode: social_proof
proof_priority: hero_strip
trust_hero_social: "4.9 ★ — Отзывы клиентов на Яндекс и Авито"
trust_reviews_section_required: true
```

**Factory:** hero strip = stars + source line; reviews § repeats detail.

---

## Example 2 — Triumph zakaz as-built

```yaml
trust_mode: operational_proof
proof_priority: hero_strip
trust_hero_operational:
  - "От 30 минут"
  - "Мин. заказ"
  - "Опытные водители"
  - "Для юрлиц — безнал"
trust_reviews_section_required: true
```

**Why used:** hot PPC, callout alignment, B2B hint, fleet removal.  
**Risk:** social proof delayed — see calibration trust doc.

---

## Example 3 — Recommended hybrid (vNext — not built)

```yaml
trust_mode: hybrid_proof
proof_visibility: prominent
# Max 3 hero items, e.g.:
trust_hero_social: "4.9 ★ — Яндекс и Авито"
trust_hero_operational:
  - "От 30 минут"
  - "Безнал для юрлиц"
```

---

## Anti-example — v4 index (forbidden)

```yaml
trust_mode: operational_proof  # mislabeled — actually fleet signal
# «Свой автопарк» — destructive
hero_layout_mode: legacy_clutter  # FORBIDDEN
```

Do not reuse v4 `screen-01-hero.html` on any route.
