# Search PPC Strategist Contract v1

**Stage:** SPPC-13  
**Interface:** `buildSearchPpcStrategy({ analyticalPack, businessAuthority, operatorConstraints, campaignPlatform, strategyPolicy })`

## Blind authority boundary

Must NOT receive: Commander export, answer keys, unapproved operator conclusions, diagnostic labels as facts.

## Output

Strategy record with tier policy, campaign architecture recommendation, keyword/negative policy, ad-message principles, landing/offer alignment, bidding/budget framework, measurement requirements, blockers, assumptions, operator decisions required, supporting evidence IDs.

## Provisional mode

When Paid SERP or other mandatory evidence missing: `PROVISIONAL STRATEGY DRAFT` only — no production authority, no Commander, no final budgets/bids.

## Model

Preferred: OpenRouter `openai/gpt-5-mini` via dedicated strategist prompt (`strategist/prompts/strategist-prompt-v1.mjs`) — separate from ORCA semantic assessment.
