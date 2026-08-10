# MISSED LEAD DEDUP FORENSIC — Phase 3H.7

Dedup false-positive for `MISSED_PROD_LEAD_1` **not proven** and **not excluded**.

Reason: Gmail message identity unavailable while OAuth is broken; CLEAN gmail_message_id fields frequently empty in sanitized extracts.

After Gmail reauth, compare message id / fingerprint against EXISTING_SPAM_LEAD_A/B before recovery replay.
