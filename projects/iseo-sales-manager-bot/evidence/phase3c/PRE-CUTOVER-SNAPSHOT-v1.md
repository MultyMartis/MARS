# PRE-CUTOVER SNAPSHOT v1

## Captured

`2026-07-30T21:55:01.239Z` on host `n8n.ai-metacode.com`

## Workflows

| Key | ID | Name | active | nodes | connectionHash |
|-----|----|------|--------|-------|----------------|
| PROD | h8I2Tl2yl4uzhUnB | Sales-Manager-v2 | true | 19 | `93E3D2F3AD42A02B5B775E8780AD5F6ABAFE096F44BB4D9786109D2208D47345` |
| OPS | xSnXPy8cEHoZw6xG | i-SEO Sales Manager - Operational.dev | false | 30 | `BFA3776A7A8E9DDEAA30EA02FEE8325E7BDA5B911A37A908BF840C0F3E28DA5C` |
| ADMIN | wLrLp4WQHm1VJmxz | i-SEO Sales Manager - Admin.dev | true | 26 | `7D57282DD0D7FF074BE263AC59497ECEDBF941813777602F9A894D6EA096162C` |

## Project workflow count

**4** (includes historical Sales-Manager-v1 inactive)

## Destination decision

- Policy: preserve Sales-Manager-v2 manager destination
- PROD chat hash: `3FBE21323E22BFC1`
- OPS chat resolution: CONFIG expression
- Match with prior sandbox binding hash `3FBE21323E22BFC1`: **yes**

## Local backups

Raw backups stored local-only under Storage `incoming/iseo-sales-manager-bot/phase3c-local/backups/` (not committed).
