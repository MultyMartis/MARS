# I-SEO Report Hub — Summary Assembly Finalized Report Policy v0.1

**Status:** CHARTER / POLICY — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Apply Charter 01

This wave does **not** implement reopen, apply, export, or PDF regeneration.

---

## 1. Default rule

**Apply to a finalized monthly report is blocked.**

This reuses the existing block CRUD lock (`ReportBlockService::canMutateAgainstParent`): parent status `finalized` or `archived` → no create/edit, including `admin_owner`, until reopen.

Assembly apply must **not** bypass that lock.

---

## 2. Why report id 1 cannot be applied

Local monthly report id **1** is:

- `status = finalized`
- `report_blocks` **6**, all `reviewed`
- active snapshot exists (`report_snapshots` id 1)
- `report_exports` **4**
- `report_export_shares` **7** (active **1**, likely id 7 / `test-first-link`)
- client PDF checksum prefix unchanged in recent waves: `a8c4d61c6216e8d70b19`

If apply wrote live `report_blocks` while the report stayed finalized (or after a silent bypass):

1. Live `/preview` would show new text.
2. Frozen snapshot / HTML / PDF / public share would still show the **issued** artifact.
3. Operators would believe the client report changed when the share did not.
4. Block statuses would stay `reviewed` unless reset — readiness/re-finalize would lie about review of the new prose.

That is why Implementation 01 **disables** apply on report 1 and **does not** reopen it.

---

## 3. UX copy (finalized)

On `GET /monthly-reports/{id}/assembly-preview` when parent is `finalized`:

```
Отчет финализирован. Чтобы применить черновик, сначала нужен отдельный безопасный reopen/update/finalize/export процесс.
```

Keep the existing preview warning that assembly does not change PDF/snapshots/shares.

Do **not** put a reopen button on the assembly page.

Do **not** offer “apply anyway”.

---

## 4. Reopen is a separate process

Existing reopen (`ReportFinalizationService::reopen`):

- `admin_owner` only
- `finalized` → `reviewed`
- `finalized_at` **preserved**
- does **not** delete or regenerate snapshots, exports, shares, or PDFs
- after reopen, block CRUD is allowed again

Assembly Apply Implementation 01 **must not** call reopen.

A future **Reopen Charter / Revised Export Charter** owns:

1. Who may reopen a report that already has an active share.
2. Whether the active share must be revoked first.
3. How a revised snapshot/export/PDF is created.
4. How the client is told that a new version exists.

Those questions are **out of scope** here. Default until that charter: **do not reopen report 1 for apply smoke**.

---

## 5. Publication chain (unchanged)

| Surface | Reads | Updates when blocks change? |
|---------|-------|------------------------------|
| `/monthly-reports/{id}/preview` | Live `assemble()` | Yes, after a successful apply on a **non-finalized** report |
| Active `report_snapshots` | Payload frozen at create | **No** |
| `report_exports` HTML/PDF | Snapshot / artifact | **No** |
| Public share token | Existing export file | **No** |

Apply never regenerates PDF and never mutates export/share rows.

---

## 6. Future operator sequence

1. **Draft preview** — GET assembly-preview (already implemented).
2. **If not finalized** — select blocks, confirm, POST apply.
3. **Review** live report preview (`/monthly-reports/{id}/preview`).
4. **Edit** remaining manual shells (`executive_summary`, `results_summary`, `key_findings`) in existing block CRUD if needed.
5. **Review block statuses** — apply will set written blocks to `in_progress`; finalize still requires the five required keys in `reviewed` / `approved`.
6. **Finalize / snapshot / export / PDF / share** — existing separate processes.
7. **If a finalized issued report needs changes** — separate Reopen + Revised Export charter. Not this apply wave.

---

## 7. Archived reports

Same as finalized for apply: **blocked**. No apply, no silent un-archive.

---

## 8. Work entries vs finalized

Work-entry editor may still run on a finalized report (existing warning that PDF does not auto-rebuild). That split stays:

- specialist log can move;
- client shells stay frozen until reopen **and** explicit block edit or a **future** apply after reopen.

---

## 9. SAFE UNKNOWN

- Whether operators will later want apply-after-reopen on report 1 in a controlled lab with share revoke. Default **no** until a dedicated charter.  
- Exact operator wording for the revised-export client message (not this wave).
