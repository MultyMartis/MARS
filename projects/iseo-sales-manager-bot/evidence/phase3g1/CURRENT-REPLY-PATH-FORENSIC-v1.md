# CURRENT REPLY PATH FORENSIC v1 — Phase 3G.1

**Labels:** ADMIN_A · MOD_A  
**Pre-patch baseline:** First Reply Engine `sm-reply-v2.1` + Human Reply Style `sm-human-v1.0` + card `sm-msg-v2.4`  
**Target path:** Approved Template Router/Renderer + recipient personalization (`iseo-first-contact-v1.0`)

## Observed baseline path (pre 3G.1 live patch)

1. Parse (`sm-parser-v3.3`) → semantic lead  
2. First-reply v2.1 deterministic draft (shared text shape)  
3. Format card → Expand recipients → claim → Telegram send to eligible staff  
4. Manager copies reply manually — **no client auto-send**

## Gap closed by 3G.1 design

- Shared draft lacked approved per-recipient client-facing names  
- Nickname risk (internal label ≠ client name) for MOD_A  
- Need explicit five-template INTLSEO corpus + precedence  
- Need manager guidance separated from copy block with natural labels  

## Contour (pre-patch)

Ops active 45 nodes · Admin active 82 nodes · Sales-Manager-v2 inactive · AI OFF · reminders OFF · stats 1/1/0/0 epoch 05.08.2026

## Live patch status

**UNKNOWN / pending or in progress** — do not claim live n8n success until FINAL-WORKFLOW-STATE is filled.
