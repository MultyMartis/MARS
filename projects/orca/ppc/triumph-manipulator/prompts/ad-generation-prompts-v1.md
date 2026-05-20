# Ad Generation Prompts v1

**Role:** Prompt patterns for **Ad** entities under existing **Group** nodes — JSON only.

**Prerequisite:** Campaign/group graph from [campaign-generation-prompts-v1.md](campaign-generation-prompts-v1.md).

---

## Generation target

Per group, emit `ads[]` items conforming to `orca-ppc-document-v1.schema.json` ad definitions:

- `headline_1`, `headline_2` (optional)
- `description`
- `display_url_path` / path fields as schema requires
- `fastlinks[]`, `callouts[]`
- `alignment` metadata (primary phrase, intent continuation)
- `status`: `draft` | `active` (default **draft** until human review)
- Mobile-first flags where schema provides

**Not in scope:** Changing group intent, keywords, or landing strategy — escalate to campaign prompts.

---

## Doctrine embedding (required in every ad prompt)

From [generation-logic-v0.md](../doctrine/generation-logic-v0.md):

1. **Phrase in headline** — primary keyword phrase appears in `headline_1` for bold-highlight continuation.  
2. **Anti-generic** — forbid лучшие цены, высокое качество, лидер рынка, etc.  
3. **Commercial PPC ≠ SEO** — solution/fit/speed, not storytelling.  
4. **Mobile-first** — readable in 5–10 seconds; short lines.  
5. **Landing continuation** — ad promise matches `group.landing_route`.  
6. **Capability truthfulness** — only intake-confirmed facts.

---

## Prompt A — Single ad per group (default)

```
TASK: Generate ONE draft ad JSON for group <group_id>.

INPUT:
- group.semantic_intent
- keyword_cluster (primary phrase flagged)
- landing_route
- intake capabilities.confirmed

OUTPUT: single object suitable for ads[] append:
{
  "ad_id": "ad_{group_slug}_v1",
  "status": "draft",
  "headline_1": "...",
  "headline_2": "...",
  "description": "...",
  "fastlinks": [...],
  "callouts": [...],
  "alignment": {
    "primary_phrase": "...",
    "phrase_in_headline": true,
    "continuation_with_landing": true
  }
}

RULES:
- headline_1 contains primary phrase verbatim or inflected form allowed by Russian grammar.
- description continues headline; includes geo + capability where confirmed.
- Respect Yandex symbol limits (do not truncate — stay under limits).
- No SEO fluff, no generic trust words.
- JSON only.

If primary phrase cannot fit headline within limit, output SAFE UNKNOWN note in alignment.risk_note — do not silently drop phrase.
```

---

## Prompt B — Headline variants (controlled A/B)

```
Generate at most 2 additional draft ads (max 3 total per group).
Variants must differ in wording but SAME semantic intent and SAME primary phrase alignment.
Do not create near-duplicate spam variants.
Output: JSON array of ad objects.
```

---

## Prompt C — Fastlinks

```
Generate 2–4 fastlinks that qualify intent (capability, use-case, geo, B2B).

GOOD: "Манипулятор 5 т", "Перевозка бытовок", "Безналичный расчёт"
BAD: "Главная", "О компании", "Наши услуги"

Output: fastlinks[] only as JSON.
Each link text must respect symbol limits.
```

---

## Prompt D — Callouts

```
Generate 3–5 callouts reinforcing capability and operational clarity.

GOOD: "Борт 5 т", "Стрела 14 м", "Без посредников", "Работа по краю"
BAD: "Лучшее качество", "Низкие цены"

Only confirmed capabilities from intake.
Output: callouts[] JSON only.
```

---

## Prompt E — CTA semantics (mobile-first)

```
description must imply clear next step without generic "оставьте заявку" spam:
- заказ / вызов / расчёт / звонок — match group commercial stage
- short sentences; line breaks mentally for mobile scan
Output: description field JSON only + cta_semantics: "call" | "order" | "quote" in alignment meta if schema allows
```

---

## Prompt F — Yandex bold-highlight continuation

```
Optimize for search phrase continuation:
- primary phrase in headline_1
- same stem or phrase fragment in description
- optional fastlink echo

Output: alignment object documenting:
phrase_in_headline, phrase_in_description, fastlink_echo (bool)

Do not keyword-stuff unnaturally — SE rules apply.
```

---

## Field limits (prompt must cite — no silent trim)

Operator or future validator enforces SY-* rules. Generation prompts instruct model to **stay under** limits:

| Field | Operational target |
|-------|---------------------|
| headline_1 | ≤ 56 characters (incl. spaces) — verify against [symbol-validation-rules-v1.md](../validation/symbol-validation-rules-v1.md) |
| headline_2 | ≤ 30 characters |
| description | ≤ 81 characters per line semantics |
| fastlink | per Direct limits in symbol doc |

If over limit, shorten copy — **do not** truncate with ellipsis in generation pass.

---

## Alignment checklist (model self-check before JSON emit)

- [ ] Primary cluster phrase reflected in `headline_1`  
- [ ] No generic forbidden phrases  
- [ ] Capability claims ⊆ intake.confirmed  
- [ ] Geo matches document `geo.primary_region`  
- [ ] Landing continuation consistent with `landing_route.blueprint_id`  
- [ ] `status: draft` unless operator requested active  

---

## Forbidden ad behaviors

| Forbidden | Reason |
|-----------|--------|
| Bulk “write 50 headlines” | Anti-chaos; SV rules |
| SEO articles in description | CM / SE generic failures |
| Claims not in intake | CM capability truth |
| Changing URL to undeclared landing | LM mismatch |
| Emoji, excessive punctuation, ALL CAPS spam | SY / brand risk |
| Excel output | JSON-first discipline |

---

## Handoff to validation

After ad pass:

1. Merge into full `OrcaPpcDocument`  
2. Run validation checklist / future CLI  
3. Use [validation-fix-prompts-v1.md](validation-fix-prompts-v1.md) for FAIL/WARN  

Human review required before export: [human-review-gates-v1.md](human-review-gates-v1.md).
