# ORCA Domain + Max Fastlinks v0.2 — transport notes

**Phase:** Lane B · PPC transport + routing refinement  
**NOT:** Direct API · runtime · auto-import

---

## Production domain

- **Host:** `https://manipulator-triumph.ru`
- **Replaces:** `triumph-krd.ru` placeholder in drafts and fixtures

---

## Fastlinks doctrine (v0.2)

| Policy | Value |
|--------|-------|
| Target per ad | **8** fastlinks |
| Minimum (warn) | **6** |
| Hard max | **8** (SY-11) |
| Transport cap | `MAX_FASTLINKS_TRANSPORT = 8` in [mapping.js](mapping.js) |

---

## Commander combined-cell encoding

- Delimiter: `||` (`TEMPLATE_FILL_JOIN`)
- Columns: titles, descriptions, URLs joined separately
- **SAFE UNKNOWN:** Commander UI max combined cell length; whether `||` splits correctly on import for 8 slots; Russian UTF-8 normalization on re-export

---

## mapping.js v0.2 changes

- `normalizeFastlinksForTransport()` — stable sort, dedupe title+url, cap 8
- `exporter_version`: `orca-exporter-cli-domain-fastlinks-v0.2`
- No silent title truncation

---

## Run export

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm run export:sheet1-patch:v0.2
```

Output: `output/triumph-sheet1-patch-domain-fastlinks-v0.2.xlsx`

---

## Human verification checklist

1. Open XLSX in Excel — no recovery dialog  
2. Promotion URL row 11 → `https://manipulator-triumph.ru/manipulyator-5-tonn/` (first group)  
3. Fastlink columns show up to 8 `||`-separated segments  
4. Sheet2/sheet3 SHA unchanged vs template (ZIP patch)  
5. Commander import — **human session only**
