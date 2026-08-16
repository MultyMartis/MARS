# TYPOGRAPHY RULE SET — PROD-P16

Canonical processor: `Shpigovsky\Core\Typography\RussianTypography`

## Representation

- Canonical NBSP: Unicode `U+00A0` (`\xC2\xA0`)
- Entity forms (`&nbsp;`, `&#160;`, …) normalized **to** Unicode on input
- Idempotent: second pass yields identical output
- No `&amp;nbsp;` generation

## Rules (conservative)

1. Short prepositions/conjunctions → NBSP before following word: в, во, к, ко, с, со, у, о, об, от, до, по, на, за, из, без, для, и, а, не, ни, но, же, ли, бы  
2. Initials: `А. Б.` / `А. Фамилия`  
3. Numbers + units: год/лет/минут/час/день/%/₽/руб.  
4. Sentence hyphen-as-dash ` - ` → `—` with NBSP before  
5. NBSP before existing em/en dashes  
6. Straight `"…"` → `«…»` only when inner text contains Cyrillic and is not URL/technical  
7. Collapse accidental duplicate regular spaces  

## HTML

- Split on tags; process text segments only
- Skip depth inside: script, style, code, pre, textarea, kbd, samp, tt, svg
- Skip shortcode-like / URL / email-only segments
- Never rewrite attributes

## Exclusions

URLs, emails, tel, slugs, JSON, shortcodes, technical identifiers, SEO URL/robots fields, media keys.

## Search safety

`shpigovsky_smart_search_lower()` collapses NBSP → space before match.
