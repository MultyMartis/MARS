# Information architecture — Triumph Manipulator Landing (v0)

**Scope:** **Single primary landing URL** for this reference execution. Legal / privacy / thank-you pages — **SAFE UNKNOWN** (assumed required before publish; not detailed here).

---

## 1. Page hierarchy

```text
/  (manipulator landing — primary)
├── /privacy-policy/     (assumed — content TBD)
├── /legal/              (optional — SAFE UNKNOWN)
└── /thank-you/          (post-form — optional)
```

**Decision:** Blueprint focuses on **`/`** only for v0 doc run.

---

## 2. Section ordering (on-page)

Aligned with [page-blueprint-v0.md](page-blueprint-v0.md) `section_order`:

1. **Hero** — orientation + primary CTA  
2. **Trust block** — badges / certs (verifiable only)  
3. **Geo trust** — service area honesty  
4. **Process steps** — how engagement works  
5. **Services grid** — scoped “capabilities / lift categories” (not unrelated SKUs)  
6. **Cases** — proof (permissioned)  
7. **FAQ** — objections  
8. **Lead form** — conversion  
9. **Final CTA** — repeat primary intent  
10. **Sticky CTA** — mobile behavior layer (not duplicate content)

---

## 3. CTA placement

| Zone | CTA |
|------|-----|
| Hero | Primary + secondary contact |
| Post-process | Primary repeat (anchor to form) |
| End | **final_cta** + form proximity |
| Mobile scroll | **sticky_cta** |

---

## 4. Trust flow

**Problem awareness** (hero) → **credibility** (trust + geo) → **how it works** (process) → **scope clarity** (grid) → **proof** (cases) → **objections** (faq) → **convert**.

---

## 5. Mobile reading flow

- First screen: **headline + one proof line + primary CTA** visible without hero media blocking taps.
- **Process** and **FAQ** use short steps / accordion — **implementation** in frontend handoff.
- Tap targets for `tel:` and form fields per WCAG intent (frontend QA verifies).

---

## 6. Scanability

- Section titles are **outcome-oriented** where possible (“How we plan a safe lift” vs internal jargon).
- Avoid walls of dense specs; use **`services_grid`** for scannable capability rows.

---

*IA v0 — reference execution only*
