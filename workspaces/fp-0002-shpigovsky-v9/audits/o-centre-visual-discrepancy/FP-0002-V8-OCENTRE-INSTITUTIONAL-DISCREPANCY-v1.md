# FP-0002 V8 O-Centre Institutional Discrepancy v1

| Issue | Classification | Evidence |
|---|---|---|
| Founder quote separated from institutional band | WRONG_COMPONENT_BOUNDARY | Figma `1:2279` contains `1:2301-1:2309`; impl uses standalone `founder-quote.html` after CTA |
| Institutional body text groups match | NO_ISSUE | Four paragraphs present; matches Figma text nodes |
| Red accent lead present | NO_ISSUE | `block-whith-red-line` on lead |
| Decorative background layers missing | DECORATION | No page-scoped institutional decoration in impl |
| Typo `Шпиговсикй` | COPY_ERROR | Matches Figma `1:2282` — correction requires explicit operator authorization |
| Desktop/mobile restructuring | RESPONSIVE | Institutional is single column; acceptable base, missing founder subregion on mobile order |

**Required correction:** Merge founder quote into institutional composition context; keep CF-004 base partial; add page wrapper/decoration only.
