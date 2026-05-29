# Field Normalization Rules v1

**Role:** Transport-safe string handling for Commander Excel — **not** semantic editing.  
**Critical rule:** **No silent truncation.** Overflow → block export (validation should have caught SY-*).

---

## Scope

Normalization applies to **cell values written to xlsx**, after validation passed. It does **not**:

- Shorten headlines to fit limits  
- Replace forbidden generic phrases  
- Change landing URLs for “better” pages  
- Merge or split keywords  

---

## Whitespace

| Rule | Action |
|------|--------|
| Leading / trailing space | **Trim** on export (manifest logs `TRIM_APPLIED` per field) |
| Internal double spaces | **Collapse** to single space for text fields |
| Tabs in copy | Replace with single space |
| Empty after trim | **Block** — should not pass validation |

Trim is **not** used to sneak under character limits — re-validate length after trim in future CLI.

---

## Newlines

| Field type | Policy |
|------------|--------|
| Headlines, description, callouts, fastlink titles | **Remove** `\n` `\r` → space; warn in manifest |
| Notes / optional columns | Allow single `\n` if template supports multiline (**SAFE UNKNOWN**) |

Commander search ads are single-line transport.

---

## Quote normalization

| Rule | Action |
|------|--------|
| Straight vs curly quotes | Normalize to `"` or strip decorative quotes per operator policy |
| Excel formula injection | Escape cells starting with `=`, `+`, `-`, `@` by prefixing `'` |
| Embedded `"` | Standard xlsx string escaping by library |

---

## UTF-8 safety

| Rule | Action |
|------|--------|
| Encoding | UTF-8 workbook only |
| Cyrillic | Preserve verbatim — no transliteration |
| Mojibake detection | Block if replacement chars `` appear |
| BOM | No BOM in JSON input; xlsx writer handles internally |

---

## ё / е policy

| Context | Policy |
|---------|--------|
| **Exported text** | **Verbatim** from document — no ё→е conversion on export |
| **Dedup keys only** | ё→е for duplicate keyword detection ([row-generation-rules-v1.md](row-generation-rules-v1.md)) |
| **Validation** | Validator handles equivalence; exporter does not re-check semantics |

---

## URL normalization

| Rule | Action |
|------|--------|
| Scheme | Require `https://` — if missing, **block** (do not auto-add) |
| Trailing slash | **Verbatim** unless validation policy standardizes |
| Encoding | Percent-encode illegal characters only if already invalid — prefer block |
| `display_url.domain` | Lowercase domain only; paths verbatim |
| UTM injection | **Forbidden** — exporter does not add tracking params |

---

## Phone formatting

| Rule | Action |
|------|--------|
| Phone in copy fields | Verbatim — no auto-format |
| Dedicated phone column (if template has) | Copy from entity if present; empty otherwise |
| Click-to-call | Not exporter concern |

**SAFE UNKNOWN:** Whether template includes phone columns — verify xlsx.

---

## Symbol-safe export

| Check | On overflow |
|-------|-------------|
| `len(headline_1)` > 56 after normalization | **Block** `POST_NORM_LENGTH_VIOLATION` — do not truncate |
| Same for SY limits | Block, reference validation rule id in error |

Exporter assumes validation caught limits; post-normalize length check is safety net only.

---

## Numeric and enum fields

| Type | Policy |
|------|--------|
| Device modifiers | Copy number or empty cell |
| Match type | Enum map only — no inference |
| Campaign type | Map `search` only |

---

## Manifest logging (future)

```yaml
normalization:
  trim_applied: [{ entity_id, field_path }]
  newline_stripped: [...]
  post_norm_length_blocks: [...]
```

---

## Related

- [validation/symbol-validation-rules-v1.md](../validation/symbol-validation-rules-v1.md)  
- [export-blocking-rules-v1.md](export-blocking-rules-v1.md)
