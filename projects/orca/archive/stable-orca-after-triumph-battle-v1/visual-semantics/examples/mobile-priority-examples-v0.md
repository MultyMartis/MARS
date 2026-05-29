# Mobile Priority Examples v0

## Example A — Triumph zakaz as-built (gap)

```yaml
mobile_critical: [form_submit, capability_scan]
cta_priority: form
# PPC instance: call-first  ← tension
```

**Risk:** call not in first screen on 390px stack.

---

## Example B — Recommended call-first alignment (vNext)

```yaml
mobile_critical: [call, form_submit, capability_scan]
mobile_hero_cta_order: [call, form]
cta_priority: form  # desktop may remain form-aside
```

**Factory hints:** sticky bar `Позвонить | Рассчитать`; verify header `tel:` on device.

---

## Example C — Qualification-critical

```yaml
mobile_critical: [qualification_line, form_submit]
qualification_mode: hero_lower_band
```

**Copy:** anti-evacuation notice above cargo — addresses D1 on mobile.

---

## Operator checklist (all examples)

- 390px primary CTA reachable
- no horizontal overflow through FAQ
- consent error state visible

**SAFE UNKNOWN:** measured scroll px thresholds.
