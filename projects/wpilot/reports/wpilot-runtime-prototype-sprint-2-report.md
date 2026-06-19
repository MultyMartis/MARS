# REPORT — WPilot Runtime Prototype Sprint 2

**Date:** 2026-06-19  
**Environment:** DEV only — `https://dev.gktriumph.ru`  
**Plugin:** MetaCODE WPilot `0.3.0` / schema `0.2.0`  
**Sprint result:** **PASS** (3/3 scoped-replace + rollback runs)  
**Evidence archive:**  
- Run #1 + deploy: `C:\AI MARS STORAGE\wpilot\backups\dev.gktriumph.ru\runtime-sprint2-20260619-153953\`  
- Runs #2–#3 (final): `C:\AI MARS STORAGE\wpilot\backups\dev.gktriumph.ru\runtime-sprint2-resume-20260619-154211\`

---

## 1. Endpoint Implementation

| Item | Fact |
|------|------|
| Route | `POST /wp-json/wpilot/v1/pages/{id}/scoped-replace` |
| Operation type | `apply_content_change` (`scoped_replace`) |
| Scope | `page.post_content` only |
| Match mode | exact once (`str_replace` count must be `1`) |
| Auth | `require_scoped_replace_access` (= rollback/write gate + token + schema) |
| Request fields | `search`, `replace`, `approval_ref`, `changeset_ref` |
| Response fields | `operation_id`, `backup_id`, `checksum_before`, `checksum_after`, `replacements_count`, `validation_result` |
| Internal flow | validate → backup → verify backup → `wp_update_post` → re-read → verify → audit |
| Failure policy | no auto-rollback on validation failure; `rollback_available: true` when backup exists |
| New files | `includes/class-wpilot-scoped-replace-service.php` |
| Modified | REST controller, auth, audit metadata, dry-run zone rules, constants `0.3.0`, plugin bootstrap, README |

Post-deploy route list confirmed `scoped-replace` live (`plugin_version: 0.3.0`).

---

## 2. Run #1 — WPilot Test Page

**Target:** page ID `954` (`/wpilot-test-page/`)

| Field | Value |
|-------|-------|
| `apply_operation_id` | `op_f3ab7fac-eeef-4a1f-9f86-aac6bbe8e3cd` |
| `rollback_operation_id` | `op_127ab97b-f943-44c1-96ba-4a482e6153e0` |
| `backup_id` | `4` |
| `search` | `МАРС успешно изменил этот WPBakery-блок через WPilot scoped edit test.!` |
| `replace` | `МАРС Sprint2-Run1: scoped-replace apply_content_change подтверждён.!` |
| `checksum_before` | `sha256:6e4852dd7948960cfd97b2e7a49da829204064090b681d3bf74d66a98f2888e2` |
| `checksum_after_apply` | `sha256:347b144def406dff85136009beb8272ef97dd58c9657f4179bde36628175548d` |
| `checksum_after_rollback` | `sha256:6e4852dd7948960cfd97b2e7a49da829204064090b681d3bf74d66a98f2888e2` |
| `replacements_count` | `1` |
| `validation_result` | `passed` / **PASS** |

---

## 3. Run #2 — Контакты

**Target:** page ID `69` (`/contacts/`)

| Field | Value |
|-------|-------|
| `apply_operation_id` | `op_e23762fe-d55f-4f4e-8e25-575f6b4a2177` |
| `rollback_operation_id` | `op_1c967d7f-0da5-453f-8a15-f08ac5cd363a` |
| `backup_id` | `6` |
| `search` | `География присутствия` |
| `replace` | `География присутствия · WPilot S2` |
| `checksum_before` | `sha256:f5440c198c3480092d91c3cc12cf74c3ac50efed8ecfc0f596e9635d4d4ec312` |
| `checksum_after_apply` | `sha256:88df5b22d6e699789e106167e3e302d9a05a5e1fe40fef0b67ed1d5a782a8bdd` |
| `checksum_after_rollback` | `sha256:f5440c198c3480092d91c3cc12cf74c3ac50efed8ecfc0f596e9635d4d4ec312` |
| `replacements_count` | `1` |
| `validation_result` | `passed` / **PASS** |

**Note:** first attempt failed post-write validation (`replacement_confirmed: false` when `search` is substring of `replace`); validation rule fixed; page `69` manually rolled back (`backup_id: 5`) before resume run.

---

## 4. Run #3 — Грузовое такси

**Target:** page ID `38` (`/services/gruzovoe-taksi/`)

| Field | Value |
|-------|-------|
| `apply_operation_id` | `op_89f33ca7-4c82-48ae-998e-079e0d46907b` |
| `rollback_operation_id` | `op_440652b0-67f4-4d41-97ef-b3595997d7e2` |
| `backup_id` | `7` |
| `search` | `«ВАМ НЕ ПРИДЁТСЯ ПЕРЕПЛАЧИВАТЬ ЗА ЛИШНИЕ ЧАСЫ»` |
| `replace` | `«ВАМ НЕ ПРИДЁТСЯ ПЕРЕПЛАЧИВАТЬ ЗА ЛИШНИЕ ЧАСЫ» · WPilot S2` |
| Zone | plain text gap between WPBakery shortcode blocks (not inside `vc_raw_html`) |
| `checksum_before` | `sha256:8f450f24c575fe7e41c253bb16dc82e8436eaa850350b3e5fd965e3b99fa5ec1` |
| `checksum_after_apply` | `sha256:11ba0ee2db2a07d4ee531de4dc4572b4864b74ea475cd715ee5f913a581fa587` |
| `checksum_after_rollback` | `sha256:8f450f24c575fe7e41c253bb16dc82e8436eaa850350b3e5fd965e3b99fa5ec1` |
| `replacements_count` | `1` |
| `validation_result` | `passed` / **PASS** |

---

## 5. Apply Validation

| Check | Run #1 | Run #2 | Run #3 |
|-------|--------|--------|--------|
| `replacements_count == 1` | yes | yes | yes |
| `checksum_before != checksum_after` | yes | yes | yes |
| target page exists | yes | yes | yes |
| backup created (`backup_id`) | yes (`4`) | yes (`6`) | yes (`7`) |
| replacement confirmed in `post_content` | yes | yes | yes |
| API `validation_result: passed` | yes | yes | yes |
| inspect checksum matches API after apply | yes | yes | yes |

---

## 6. Rollback Validation

| Check | Run #1 | Run #2 | Run #3 |
|-------|--------|--------|--------|
| rollback API `ok: true` | yes | yes | yes |
| `mutation_performed: true` | yes | yes | yes |
| `restored_checksum == backup checksum` | yes | yes | yes |
| final inspect checksum == baseline | yes | yes | yes |
| `content_length` restored | yes | yes | yes |
| sprint marker absent after rollback | yes | yes | yes |

---

## 7. Audit Validation

Apply lifecycle per `operation_id` (example Run #1):

| Order | `event_type` | `outcome` |
|-------|--------------|-----------|
| 1 | `scoped_replace_requested` | `accepted` |
| 2 | `backup_created` | `succeeded` |
| 3 | `scoped_replace_verified` | `succeeded` |

Rollback lifecycle: `rollback_requested` → `rollback_verified` (`outcome: rolled_back`) — confirmed for all three runs.

Failed apply attempt on Run #2 (pre-fix) logged `scoped_replace_failed` with `backup_id: 5`, `reason_code: POST_WRITE_VALIDATION_FAILED`.

No token or content dumps in audited rows (spot-checked).

---

## 8. Findings

1. **`apply_content_change` execute path proven** on DEV via `scoped-replace` endpoint (`0.3.0`).
2. **All three targets** completed apply → validate → rollback → validate with checksum integrity.
3. **Run #2 first attempt** exposed false-negative when `search` is a substring of `replace`; fixed in `class-wpilot-scoped-replace-service.php` before resume.
4. **Dry-run zone rules narrowed** (shortcode delimiter tags + raw block boundaries only) so heading attribute text and inter-shortcode plain text are eligible; full raw block interior still protected by HTML-tag overlap checks.
5. **Manual recovery** required once between attempts on page `69` (rollback `backup_id: 5`).

---

## 9. Risks

| Risk | Level | Note |
|------|-------|------|
| CDN/page cache after apply/rollback | SAFE UNKNOWN | inspect checksums passed; live HTML not formally diffed in this sprint |
| Replace text containing search substring | Low | mitigated by `substr_count` confirmation rule |
| Attribute-level replaces (Contacts heading) | Medium | permitted by narrowed tag-range policy; still exact-once |
| Base64 `vc_raw_html` interiors | Medium | still largely blocked; Contacts used heading attribute, not raw HTML body |
| FTP patch deploy | Low | same method as Sprint 1 proof |
| Orphan backup rows from failed attempt | Low | `backup_id: 5` used; marked after manual rollback |

---

## 10. Recommendation

**Sprint 2 success criteria met:** first WPilot write operation (`apply_content_change` / `scoped-replace`) implemented and proven on DEV with backup, validation, rollback, and audit lifecycle on three pages.

**Do not start:** production enablement, multi-page/mass replace, regex replace, menu/widget/CSS writes, or new Core Layer documents.

**Next runtime step (operator choice):** keep `0.3.0` on DEV; extend proof to additional pages only with HITL and pre-run dry-run.

---

## Git / repo note

**Changed files (repo):**

- `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-scoped-replace-service.php` (new)
- `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-rest-controller.php`
- `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-dry-run.php`
- `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-auth.php`
- `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-audit-service.php`
- `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-constants.php`
- `projects/wpilot/plugin/metacode-wpilot/metacode-wpilot.php`
- `projects/wpilot/plugin/metacode-wpilot/README.md`
- `projects/wpilot/reports/wpilot-runtime-prototype-sprint-2-report.md` (this file)

**Evidence:** `C:\AI MARS STORAGE\` only (gitignored)  
**No commit performed** (default policy)
