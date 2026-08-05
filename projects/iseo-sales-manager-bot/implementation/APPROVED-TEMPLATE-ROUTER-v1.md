# APPROVED TEMPLATE ROUTER v1

**Lib:** `implementation/runtime-libs/approved-template-router-v1.mjs`  
**Versions:** `iseo-first-contact-v1.0` / `iseo-template-set-v1.0` / `iseo-sales-policy-v1.0`

## API

- `routeApprovedTemplate(ctx)` → selected template, CTA, theme, deterministic task summary, geo clause flag, confidence, warnings
- `detectControlledTheme(ctx)`, `buildDeterministicTaskSummary(theme)`
- `isNonWebsiteValue(raw)`, `shouldEnableGeoAiClause(ctx, templateId)`

## Precedence

1. **T5** special/legal/materials  
2. **T4** new site / development (over T2)  
3. **T3** meaningful task with controlled summary (over T1)  
4. **T1** valid website growth/SEO  
5. **T2** missing/non-website/ambiguous fallback  

Prompt-injection markers in comment are **ignored** for override (warning only).

## Template IDs

`T1_EXISTING_SITE_GROWTH` · `T2_SITE_MISSING` · `T3_MEANINGFUL_TASK` · `T4_NEW_SITE_DEVELOPMENT` · `T5_SPECIAL_PROJECT`

## CTA types

- `audit_agreement`
- `obtain_site_or_confirm_none`
- `clarify_development_stage`
- `obtain_materials`

## Phase 3G.2 note

Router selection unchanged (T5>T4>T3>T1>T2). Personalization of intro name is **downstream** of routing and uses `reply_sender_name` only (numbered profiles). Wording authority for operator/manager surfaces: [TELEGRAM-TEXT-CONTRACT-v2.md](../architecture/TELEGRAM-TEXT-CONTRACT-v2.md). Related: [APPROVED-TEMPLATE-RENDERER-v1.md](APPROVED-TEMPLATE-RENDERER-v1.md), [RECIPIENT-PERSONALIZED-REPLIES-v1.md](../architecture/RECIPIENT-PERSONALIZED-REPLIES-v1.md).
