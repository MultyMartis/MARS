# PIPELINE BEFORE / AFTER — Native Anti-Spam v1

## Before (partial)

```text
REQUEST
→ nonce
→ honeypot (non-empty → fake ok:true, spam:true) ⚠ analytics risk
→ raw client form_started_at / timestamp
→ rate limit (raw IP md5, 8/hour)
→ request_token claim
→ validate → persist → mail → JSON
```

## After (canonical)

```text
REQUEST
→ request shape / required POST
→ CSRF nonce (`fp02_lead_nonce` / `fp02_lead_submit`)
→ anti-spam (server)
    1. honeypot `company_url` (non-empty → REJECT, ok:false)
    2. signed `fp02_fs` (HMAC, min 2s, max 2h)
    3. rate limit (transient salted fingerprint; 6/60s + 20/20m)
→ request_token claim (idempotent accept)
→ sanitize / validate
→ payload heuristics (strong signals only)
→ ACCEPTED
→ persist real lead
→ bump rate attempt
→ attempt mail
→ frontend success (`accepted=true`)
→ optional consent-gated Metrika goal
```

**SPAM FILTERING OCCURS BEFORE REAL LEAD PERSISTENCE**
