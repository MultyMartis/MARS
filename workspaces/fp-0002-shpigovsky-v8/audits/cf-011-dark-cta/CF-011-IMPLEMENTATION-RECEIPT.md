# CF-011 IMPLEMENTATION RECEIPT

**Wave:** FP-0002 V8 CF-011  
**Canonical partial:** `src/partials/components/program-cta-band.html`  
**Canonical class:** `.program-cta-band`

## Removed

- `services-program-cta-band-v2.html`
- `service-subdivision-first-cta-v1.html`
- `service-leaf-cta-01-v1.html`
- `service-subdivision-second-cta-v1.html` (orphan)

## Migrated consumers

- `uslugi-v2.html` — secondary band via `wrapContainer`
- `usluga-podrazdel-v1.html` — section band + ARIA repair
- `usluga-konechnaya-v1.html` — section band + hidden heading
- `services-program-v2.html` — embedded band include path
- `service-subdivision-stages-v1.html` — inline copy → include
- `service-leaf-stages-v1.html` — inline copy → include

## Validation

- Build: PASS
- DOM/ARIA: PASS
- Selector/partial: PASS
- Page-wide DOM gate: PASS
- Functional CTA QA: PASS
- Protected hash guard: PASS
