# Sample run — Domain + Max Fastlinks v0.2

**Date:** 2026-05-21  
**Command:** `npm run export:sheet1-patch:v0.2`

---

## Output

`output/triumph-sheet1-patch-domain-fastlinks-v0.2.xlsx`

---

## Checks

| Check | Result |
|-------|--------|
| Export exit code | 0 |
| ZIP preserve sheet2/sheet3 | PASS (byte-identical) |
| Integrity reopen | INTEGRITY_OK |
| Stale rows removed | 103 (rows 31–133) |
| Promotion URL | `https://manipulator-triumph.ru/manipulyator-5-tonn/` |
| Fastlinks per ad row (mapping) | **8** (`||`-joined) |
| Exporter version | `orca-exporter-cli-domain-fastlinks-v0.2` |

---

## Human follow-up

- Open XLSX in Excel — confirm no recovery prompt  
- Commander import — operator session only  
- Review duplicate fastlink URLs per SY-14 before launch-ready
