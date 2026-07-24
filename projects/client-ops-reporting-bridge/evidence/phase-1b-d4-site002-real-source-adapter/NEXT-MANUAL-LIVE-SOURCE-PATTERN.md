# Next Manual Live Source Pattern

**Selected exactly one pattern (not executed in D4):**

**B — Manual explicit completed SITE-002 monitor artifact to adapter to producer to webhook**

1. Operator selects one completed hardened run directory (explicit path).
2. site002-adapter-dry-run preview (offline).
3. Operator gate / freshness confirmation.
4. Temporarily activate n8n (new real-source charter; D3 charter cannot be reused).
5. One real producer POST.
6. Correlate dedupe/Telegram.
7. Deactivate.

Not selected: A (monitor calls adapter), C (pickup daemon), D (other).
Reason: monitor unchanged; inspect-before-send; no scheduler; simpler rollback.
