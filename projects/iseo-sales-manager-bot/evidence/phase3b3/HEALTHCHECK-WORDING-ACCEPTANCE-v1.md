# HEALTHCHECK WORDING ACCEPTANCE v1

Wording vocabulary:

- **доступна** — actual safe read / accepted readable probe;
- **привязка найдена, письма не читались** — structural credential/reference only (Gmail);
- **Ошибка** — validation failed;
- **выключен / отключено** — intentionally disabled.

Forbidden tokens removed: `readable_ref_ok`, `structural_ok_no_fetch`, `inactive_expected`.

Accepted live `/health` includes Russian lines for CONFIG/RAW/CLEAN/EVENTS/ERRORS/DEDUP, Gmail structural, Telegram sandbox, workflow inactive expected, AI off, AI probe not run.
