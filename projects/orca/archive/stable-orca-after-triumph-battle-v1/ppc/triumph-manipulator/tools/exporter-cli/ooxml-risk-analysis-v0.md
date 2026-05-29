# OOXML Risk Analysis v0

**Phase:** ORCA OOXML Workbook Forensics v0  
**Symptom:** Generated `triumph-commander-template-fill-draft.xlsx` opens in ExcelJS; **Microsoft Excel** triggers workbook recovery citing corruption in `sheet1.xml`, `sheet2.xml`, `sheet3.xml`.

**Scope:** Forensic debugging only — **NOT** a production fix charter.

---

## Confidence legend

| Level | Meaning |
|-------|---------|
| **Proven** | Directly observed in ZIP/XML comparison (this run) |
| **Likely** | Strong structural evidence; not binary-proven against Excel internals |
| **Speculative** | Plausible; needs Excel-internal or Microsoft docs confirmation |

---

## Most likely corruption causes

### 1. ExcelJS full-workbook roundtrip (sheet2/sheet3 destruction) — **Likely (high)**

| Evidence | Detail |
|----------|--------|
| **Proven** | sheet2 `<c>` count 102 170 → 17 344; rows unchanged 17 344 |
| **Proven** | sheet2 uncompressed XML −2.76 MB |
| **Proven** | Exporter only maps writes to sheet1 (Тексты); sheet2/sheet3 not intentionally edited |
| **Likely** | Excel flags sparse `sheetData` inconsistent with `dimension ref="B3:G17461"` spanning 17k rows |

**Mechanism:** `workbook.xlsx.readFile` + `writeFile` re-serializes **entire** workbook. ExcelJS does not preserve Commander reference-sheet XML fidelity.

**Survivability implication:** Integrity hardening (exact-cell writes, no range clear) **cannot** fix this while save path rewrites all sheets.

---

### 2. Inline string → sharedStrings migration — **Likely (medium)**

| Evidence | Detail |
|----------|--------|
| **Proven** | Template has no `xl/sharedStrings.xml`; generated adds ~850 KB part |
| **Proven** | sheet1 inline cells 7 868 → shared indices 2 872 |
| **Likely** | Commander template expects inline string worksheet model; Excel repair may stem from combined effects |

**SAFE UNKNOWN:** Whether Commander **requires** inline strings vs accepts shared — not tested in Commander UI.

---

### 3. `ignoredErrors` removal — **Likely (low–medium)**

| Evidence | Detail |
|----------|--------|
| **Proven** | Each template worksheet had `ignoredErrors` count 2; generated 0 |
| **Speculative** | Excel may depend on these blocks for region-tree / validation tolerance |

---

### 4. Dimension ref column-A drop (sheet2/sheet3) — **Likely (medium)**

| Evidence | Detail |
|----------|--------|
| **Proven** | `A3:G17461` → `B3:G17461`; `A2:E32` → `B2:E32` |
| **Likely** | Mismatch between declared used range and sparse cell addresses |

---

### 5. Prior mass null clears (integrity v0 removed) — **Speculative (low for current file)**

| Evidence | Detail |
|----------|--------|
| **Proven** | Current pipeline removed `clearDataRows` |
| **Likely** | Recovery symptom **persists** after that fix → primary failure is rewrite, not clears |

---

## ExcelJS fidelity assessment

| Option | Assessment |
|--------|------------|
| **A. Safe with restrictions** | **Unlikely** for this Commander template as-is |
| **B. Requires template-preservation strategy** | **Likely** — only patch sheet1 XML inside ZIP, or copy template bytes for sheets 2–3 |
| **C. Requires binary patch strategy** | **Likely** for minimal cell updates without model roundtrip |
| **D. ExcelJS incompatible with workbook complexity** | **Likely** for **full** roundtrip; partial use (read-only introspection) still OK |

**Recommended engineering direction (documentation only, not implemented):**

1. **Do not** `writeFile` entire workbook after loading Commander template.  
2. Investigate **ZIP-level** surgical edit of `sheet1.xml` only.  
3. Keep `template-reader.js` / ExcelJS for **analysis**; separate transport path for **mutation**.

**SAFE UNKNOWN:** Whether any ExcelJS configuration preserves inline strings and full grid on save.

---

## Remaining unknowns

- Exact Excel repair log message → OOXML schema violation code  
- Whether Excel accepts generated file **after** repair (data fidelity loss)  
- Commander import behavior post-repair  
- Full merge / `dataValidation` inventory in template (not exhaustively diffed in v0)  
- calcChain / defined names — absent in template index; not compared  

---

## Risks if operator proceeds

| Risk | Severity |
|------|----------|
| Import corrupted region tree (sheet2) | **High** |
| Silent loss of template example rows on sheet1 | **Medium** |
| False confidence from ExcelJS `INTEGRITY_OK` | **High** — parser ≠ Excel |
| Production export via current ExcelJS save | **Blocked** until preservation strategy exists |

---

## Distinction (required)

| Category | This phase |
|----------|------------|
| **Proven** | ZIP/worksheet metrics in structure indexes; XML well-formed; ExcelJS vs Excel divergence |
| **Likely** | ExcelJS full rewrite causes recovery; sheet2 sparse collapse primary suspect |
| **Speculative** | `ignoredErrors` criticality; Commander shared-string tolerance |

**NOT:** runtime · orchestration · Direct API · production fix delivered.
