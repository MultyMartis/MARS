# ONE-CARD MESSAGE REFERENCE TRACE — LIVE_CARD_PROOF_1

Execution: 27669 (Spam)

1. callback_query received: yes (webhook)
2. callback_data parsed: action=spam
3. lead resolved: suffix 6e4c68e4
4. status before: pending
5. transition: pending → spam
6. LEADS mutation: yes (Update CLEAN Lifecycle)
7. LEAD_EVENTS append: yes
8. authoritative card-instance lookup: Expand Card Sync Copies (v1.1 buggy)
9. chat_id selected: initiator chat prefix 499… (correct chat)
10. message_id selected: MSG_883 (STALE parity) — operator clicked MSG_898
11. rendered target text: full canonical status card len≈378
12. rendered reply_markup: reopen keyboard (Edit Lead Card Message)
13. Telegram edit node called: Edit Lead Card Message ×4
14. API operation: editMessageText
15. API result initiator: error `message to edit not found`; others ok=true on stale msgs
16. error class: message_to_edit_not_found
17. post-edit sync state: Aggregate edit_ok=false, card_sync_ok=3, failed=1, semantic ack still spam
