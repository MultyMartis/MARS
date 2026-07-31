# EXTERNAL-ROUTING-CHECK-v1

**Phase:** 3C.2

## Checks

| Signal | Result |
|--------|--------|
| Gmail auto-forwarding enabled | **false** |
| Forwarding addresses configured | **0** |
| IMAP enabled | **false** |
| POP access window | disabled / leaveInInbox disposition |
| Other active n8n workflows with Gmail nodes (non Sales Manager family) | **0** |
| Sales-Manager-v2 active | **false** |
| Operational.dev active | **true** (sole intake) |
| Website transport / non-Gmail mailbox rule | SAFE UNKNOWN (outside authorized contour) |
| Connected email client rule | SAFE UNKNOWN |
| Legacy automation / script | not evidenced in n8n contour |

## Trash actor

**Not explained by Gmail filters, auto-forward, IMAP, POP, or other active n8n Gmail workflows.**

Residual: human Trash action or an external client/rule outside this contour — **SAFE UNKNOWN**.

## Operator action (Trash residual)

1. Confirm no desktop/mobile client rule auto-deletes website-form mail.
2. Avoid manual Trash of unlabeled form mail before Operational poll.
3. Optional: submit a fresh website test and confirm it stays out of Trash with OPS incoming until processed.
