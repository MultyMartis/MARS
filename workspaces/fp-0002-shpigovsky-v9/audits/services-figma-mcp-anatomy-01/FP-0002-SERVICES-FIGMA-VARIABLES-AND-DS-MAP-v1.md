# FP-0002 — Services Figma Variables and DS Map v1

**Date:** 2026-06-26  
**MCP variable pass:** **NOT RUN** (cloud fileKey blocked)

## Figma variables (live)

```text
SAFE UNKNOWN — get_variable_defs not executed
tryKey
```

## Operator-canonical frontend baseline (V7)

| Token / rule | Value | Figma correlation |
| ------------ | ----- | ----------------- |
| Container max | 1230px | ~1170–1172px content columns in frames |
| Desktop gutter | 30px | Matches hub horizontal inset |
| Mobile gutter | 15px | Mobile frames 380px width |
| Breakpoint | 1024 / 1025 | Standard V7 split |
| `--radius-main` | project SCSS | Banner radius ~rounded rect on `1:1351` |
| `.btn` system | shared | CTA instances `Кнопка` symbol `1:8` family |

## Components (offline)

| Figma component | Node examples | Frontend |
| --------------- | ------------- | -------- |
| `Кнопка` | `1:1359`, hub CTAs | `.btn.btn_dark` |
| `Тэг` | `1:1368`–`1:1373` | **Not implemented** |
| `Пункт услуги` | category lists | `services-category-hub__service` |
| `Услуга` | gallery cards | gallery figures |
| `Подвал` | `1:1747` | `site-footer` |
| External link icon | `1:3609` | `external-link.svg` |

## Libraries

```text
SAFE UNKNOWN — get_libraries not run
No Code Connect mappings in repo for Services page
```

## Production code generated

**None.** No Figma MCP React/Tailwind output used.

## Verdict

Design-to-project mapping documented from **offline parse + operator SCSS baseline** only. Live DS token pass deferred until MCP file access restored.
