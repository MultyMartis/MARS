<!-- Phase 3H.7.3 operator resurface production-parity repair 2026-08-10 -->
## Phase 3H.7.3 (current)

| Field | Value |
|-------|-------|
| **Phase** | 3H.7.3 — Operator resurface production-parity, contact error fix, multi-card sync hardening |
| **Verdict** | `COMPLETE — RESURFACE PARITY REPAIRED; OPERATOR ACCEPTANCE PENDING` |
| **Repairs** | Canonical renderer for resurface · formula-error contact filter · authoritative card registry · semantic ack ≠ sync warning |
| **Acceptance leads** | REAL_REOPEN_A/B/C pending · 12 parity cards · no new LEADS rows |
| **Runtime** | Ops **45** active · Admin **87** active · v2 inactive · AI **OFF** · reminders recipients=4 |
| **Soak** | 3H.7.2 interrupted · Fresh T+0 **2026-08-10 12:44 Europe/Moscow** · earliest T+48 **2026-08-12 12:44 Europe/Moscow** |
| **Evidence** | [evidence/phase3h73/](evidence/phase3h73/) |
| **Report** | [REPORT-iseo-sales-manager-bot-phase3h73-resurface-production-parity-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3h73-resurface-production-parity-v1.md) |
| **Gate** | Phase 3I.1 blocked until soak PASS + operator acceptance |

# OPERATOR-APPROVED LEAD RESURFACE — Phase 3H.7.2

Semantic action: `operator_resurface`

Exception to default «reopen does not redistribute». Global default unchanged.

For REAL_REOPEN_A/B/C only:
- same lead_id
- no new LEADS/CLEAN identity
- fresh pending cards to 4 active recipients
- delivery_key encodes operator_resurface
