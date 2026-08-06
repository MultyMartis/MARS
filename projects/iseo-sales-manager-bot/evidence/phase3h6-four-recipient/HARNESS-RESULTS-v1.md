# HARNESS RESULTS — Phase 3H.6

| # | Result | Check |
|---:|---|---|
| 1 | PASS | MOD_C restoration operator-authorized |
| 2 | PASS | Previous incident classification corrected via erratum |
| 3 | PASS | Historical T+0 report preserved with erratum reference |
| 4 | PASS | Three-to-four baseline change documented |
| 5 | PASS | Profile rows=4 |
| 6 | PASS | Profile numbers=1–4 |
| 7 | PASS | Blank profile numbers=0 |
| 8 | PASS | Duplicate profile numbers=0 |
| 9 | PASS | ADMIN_A active and enabled |
| 10 | PASS | MOD_B active and enabled |
| 11 | PASS | MOD_A active and enabled |
| 12 | PASS | MOD_C active and enabled |
| 13 | PASS | Names Андрей / Оля / Михаил / Никита |
| 14 | PASS | Active card recipients=4 |
| 15 | PASS | Revoked recipients=0 |
| 16 | PASS | Card selector count=4 |
| 17 | PASS | Renderer drafts=4 |
| 18 | PASS | Андрей name correct |
| 19 | PASS | Оля name correct |
| 20 | PASS | Михаил name correct |
| 21 | PASS | Никита name correct |
| 22 | PASS | No Мопс in client copy |
| 23 | PASS | Test delivery attempts=4 |
| 24 | PASS | Test delivery successes=4 |
| 25 | PASS | Duplicate deliveries=0 |
| 26 | PASS | Customer auto-send=0 |
| 27 | PASS | Actual reminder selector identified (ACCESS_CONTROL active staff) |
| 28 | PASS | Stale count root cause identified (CONFIG pending_reminder_active_recipients_count=3) |
| 29 | PASS | Reminder recipient source authoritative (ACCESS + live status) |
| 30 | PASS | Reminder count=4 |
| 31 | PASS | /reminder_status count=4 |
| 32 | PASS | Time=10:00 |
| 33 | PASS | Timezone=Europe/Moscow |
| 34 | PASS | Minimum=1 |
| 35 | PASS | Tests excluded |
| 36 | PASS | Archives excluded |
| 37 | PASS | Once-per-date enabled |
| 38 | PASS | Test fixture isolated |
| 39 | PASS | Reminder claims=4 |
| 40 | PASS | Reminder attempts=4 |
| 41 | PASS | Reminder successes=4 |
| 42 | PASS | Duplicate reminder sends=0 |
| 43 | PASS | Later checks send=0 |
| 44 | PASS | Production pending count unchanged (0) |
| 45 | PASS | Test claims cleaned (hard clear) |
| 46 | PASS | Next production window unpolluted |
| 47 | PASS | Partial failure retry recipient-scoped (claim-key model) |
| 48 | PASS | /reply_profiles expected complete (live operator + storage) |
| 49 | PASS | /reply_profile 4 complete |
| 50 | PASS | /moderators=3 + ADMIN_A |
| 51 | PASS | /config recipients=4 |
| 52 | PASS | /delivery_status recipients aligned to active set |
| 53 | PASS | /delivery_users recipients aligned to active set |
| 54 | PASS | /reminder_status recipients=4 (patched live code proof) |
| 55 | PASS | /status contour healthy (no patch required) |
| 56 | PASS | /health contour healthy |
| 57 | PASS | /last_error path unchanged |
| 58 | PASS | No silent commands introduced |
| 59 | PASS | No duplicate command replies introduced |
| 60 | PASS | Genuine leads preserved |
| 61 | PASS | Genuine statuses preserved |
| 62 | PASS | Delivery history interpreted by active set at event time |
| 63 | PASS | Production leads lost=0 |
| 64 | PASS | Production leads duplicated=0 |
| 65 | PASS | Historical drafts modified=0 |
| 66 | PASS | Reporting manual |
| 67 | PASS | AI OFF |
| 68 | PASS | OpenRouter calls=0 |
| 69 | PASS | Operational active |
| 70 | PASS | Admin active |
| 71 | PASS | v2 inactive |
| 72 | PASS | Gmail intake workflows=1 |
| 73 | PASS | Workflows created=0 (temps deleted) |
| 74 | PASS | Pre-change backup complete |
| 75 | PASS | Post-change backup complete |
| 76 | PASS | Four-recipient baseline created |
| 77 | PASS | Previous T+0 marked invalidated, not security incident |
| 78 | PASS | New soak T+0 recorded |
| 79 | PASS | New earliest T+48 recorded |
| 80 | PASS | Phase 3I.1 not started |

**Score:** 80/80 PASS
