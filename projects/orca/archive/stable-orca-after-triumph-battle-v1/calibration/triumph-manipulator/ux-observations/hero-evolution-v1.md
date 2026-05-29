# Hero Evolution v1 — why original ORCA hero model failed in Factory

## «Original ORCA hero» = blueprint + legacy v4 index

Blueprint defined **correct semantics**. Legacy v4 **index** hero (`screen-01-hero.html`) was the first Factory implementation — **semantically wrong** for MODE 1.

## Why G0 (v4 index hero) was insufficient

| Problem | Evidence | UX effect |
|---------|----------|-----------|
| **Visual clutter** | 6 `hero__features` lines + rate + CTA row | No single focal point |
| **Semantic overload** | Mixed fleet, NDС, hourly rental, geo | User cannot extract 5 т / 3 т in 5 sec |
| **Image competition** | `hero__visual-note` placeholder area | Implied large visual without clear machine params |
| **Fake pricing** | `от XXXX ₽/час` | Trust destroyer; violates honesty lock |
| **Wrong capability** | «5-10 тонн» | PPC lie vs ads |
| **Fleet framing** | «Свой автопарк» | Breaks one-machine doctrine |
| **Weak CTA hierarchy** | «Оставить заявку» without inline form | Extra scroll; weaker than form-in-hero v5 |
| **CTA visibility** | Rate block above features | Price anxiety before qualification |

## Why G2 (v5 zakaz) works better

| Improvement | Mechanism |
|-------------|-----------|
| **Focus hierarchy** | H1 → lead → 5 specs → form |
| **Reduced image competition** | Text on dark gradient over photo |
| **CTA visibility** | Dedicated aside column; primary button in form |
| **Capability-first** | Specs match ad callouts immediately |
| **Task qualification** | Cargo cards segment intent |
| **Compactness** | Specs as icon list vs paragraph features |
| **Honest pricing** | No fake hero rate |

## Remaining UX weaknesses (G2)

| Issue | Severity |
|-------|----------|
| Lower band still dense (4 proof + 6 cargo) | medium |
| No hero qualification one-liner | medium |
| Mobile stack: form may push below fold | **UNKNOWN** — needs device QA |
| Six cargo CTAs compete with one primary | medium |

## Hero v2 direction (observation only)

See [../next-evolution/hero-v2-requirements.md](../next-evolution/hero-v2-requirements.md).

**Not a redesign charter** — calibration input only.
