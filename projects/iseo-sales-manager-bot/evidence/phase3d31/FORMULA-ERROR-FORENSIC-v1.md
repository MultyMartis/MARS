# FORMULA-ERROR-FORENSIC-v1

## Observed display

Archive cards showed:

`📞 Телефон:` / `#ERROR! (Formula parse error.)`

## Origin (sanitized)

| Check | Result |
|-------|--------|
| Literal corrupted CLEAN cell | YES — 2/36 rows in forensic read had `phoneKind=formula_error` |
| Phone beginning with `+` under USER_ENTERED | YES — Google Sheets interprets leading `+` as formula |
| Dedicated formula column | NO — `phone` is a plain string column |
| Stale mapping / wrong field | NO — value came from CLEAN `phone` |
| Wrong row selection | NO — same lead hash repeated as newest unique lead |

RAW `parsed_phone` and CLEAN `phone` were written with default `cellFormat=USER_ENTERED` (n8n Google Sheets v4.7), which maps to Sheets `valueInputOption=USER_ENTERED`.

Historical cells retain `#ERROR!`. No broad historical rewrite in this phase.
