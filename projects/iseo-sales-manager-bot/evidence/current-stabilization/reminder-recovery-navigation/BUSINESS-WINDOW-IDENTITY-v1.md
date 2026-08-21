# BUSINESS WINDOW IDENTITY

## Canonical key (reused)

`pending-reminder:<YYYY-MM-DD>:<HH:MM>:<timezone>`

Example for this day:

`pending-reminder:2026-08-21:10:00:Europe/Moscow`

## Rules

- Built from **configured** reminder time (`10:00`), not execution clock minute.
- Primary (~10:00) and recovery (~10:15) share the **same** key when within the due window.
- Do **not** use raw execution timestamp as business identity.
- No second competing identity model introduced.

## Gate completion marker

`CONFIG.pending_reminder_last_window` must equal the business window key after successful full delivery.
