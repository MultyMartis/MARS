# No-Import Watchdog

After expected import completion window (deadline 13:00 Barnaul), if no terminal for the local date and import not running → one ATTENTION «Свежий импорт 1С не обнаружен» with event_id `site002-no-fresh-import-YYYY-MM-DD`.

Skips if terminal exists, import running, or already sent today.
