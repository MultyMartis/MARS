# ADMIN-PRODUCTION-CLOSEOUT v1

**Phase:** 3D.2

## `/status` (harness)

- Рабочий контур
- Operational active / Admin active
- AI OFF
- Contour healthy after clean lead

## `/stats` (policy unchanged from 3D.1)

- Unique business leads not inflated by retries
- Technical retries separate
- Accepted clean lead counted once
- Synthetic/test rows excluded

## `/last_error`

- No new active production error introduced by this phase
- Historical resolved errors retained by design

## `/health`

- Gmail bounded query path available
- Sheets available
- Telegram available
- AI probe skipped (OFF)

## `/config`

- `Версия парсера: sm-parser-v3.1`
- AI OFF
- Working contour
- Allowlist size shown as count only

## `/start`

- Live harness PASS
- Operator-typed Trigger matrix PENDING (notice sent)
