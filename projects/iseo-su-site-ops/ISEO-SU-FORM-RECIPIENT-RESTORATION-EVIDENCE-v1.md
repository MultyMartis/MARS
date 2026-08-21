# ISEO-SU FORM RECIPIENT RESTORATION EVIDENCE v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-FORM-RECIPIENT-RESTORE-01  
**Date:** 2026-08-21  
**Authority:** current recipient-restoration verification for public form mail routing on `https://i-seo.su/`  
**Supersedes (recipient-restore claims only):** blind trust in Acceptance 02 / Form Antispam REPORT statements that “normal recipients restored” without independent reconstruction of the pre-antispam active set.

---

## 1. Reason for Correction

Operator suspected that legitimate production recipients were not actually restored after isolated mail testing / anti-spam centralization. Previous REPORT lines claiming restoration were not to be trusted without re-deriving the original active set from production backups and verifying live production.

## 2. Previous Claimed State

| Claim source | Claim |
|--------------|-------|
| Acceptance 02 evidence / REPORT | Normal recipients restored; operator `im.work@mail.ru` retained; typo `im.work@nail.ru` absent; production recipient count **2** |
| Form security baseline | Prior legitimate recipients preserved |
| Antispam validation evidence | Production recipient set count = 2 (prior primary + operator) |

## 3. Actual Production State Found

Independent SFTP read of production authority file `iseo-form-config.php` (stamp `20260821T053743Z`, SHA-256 `dea5b3482feb914f…`):

| Field | Value |
|-------|-------|
| Authority | `iseo-form-config.php` via `iseo_form_recipients()` in `iseo-form-security.php` |
| `test_mode` | **false** (OFF) |
| Production recipient count | **2** |
| `im.work@mail.ru` | **PRESENT ONCE** |
| `im.work@nail.ru` | **ABSENT** |
| CC/BCC in send helper | **NONE** |
| Root handlers using shared send | **12/12** |
| Service-tree forms | thin `require` delegates to root handlers |
| Hardcoded recipient overrides in handlers | **NONE** |
| Production ↔ MARS source config SHA | **MATCH** |

## 4. Original Recipient Recovery

Pre-antispam production handler backups (scoped stamp `20260820T164529Z` under local `_form-antispam-01-tmp/backups/`) were the primary authority.

### ORIGINAL_RECIPIENT_SET (active)

| Address | Role |
|---------|------|
| `nikel007i33@yandex.ru` | Sole active `$sendto` on all 12 root handlers before centralization |

### Not part of active original set

| Address | Classification |
|---------|----------------|
| `chrra@yandex.ru` | Present only as **commented** alternate (`//$sendto = "chrra@yandex.ru";`) on 10/12 root handlers; **never active** in the pre-antispam production authority. Correctly **not** added to `production_recipients`. |
| `noreply@i-seo.su` | From-address only — not a To recipient |
| `im.work@mail.ru` | Operator mailbox added during antispam/acceptance work — not pre-antispam original |
| `im.work@nail.ru` | Typo — must remain absent |

### Handler subset note

`tariff_3__FORM.php` and `tariff_4__FORM.php` historically lacked even the commented `chrra` line; active recipient was still only `nikel007i33@yandex.ru`. Shared config therefore correctly represents the proven active original set for all 12 roots without per-handler divergence.

## 5. Provenance

| Address | Source / provenance | Confidence |
|---------|---------------------|------------|
| `nikel007i33@yandex.ru` | Pre-antispam root handler backups `20260820T164529Z` — active `$sendto` (e.g. `callback__FORM.php` SHA-256 `50cfa2b4…`); mirrored across all 12 roots | **PROVEN** |
| `chrra@yandex.ru` (commented only) | Same backups — commented lines only; not used by `@mail()` | **PROVEN non-active** |
| `im.work@mail.ru` | Operator mailbox retained from Acceptance 02; present in live production + canonical source | **PROVEN** (operator retention requirement) |

Resolution rule applied: timestamped production backups immediately before the first form-antispam recipient centralization. No guessing. No unresolved conflict requiring operator input.

## 6. Set Comparison

| Set | Members |
|-----|---------|
| ORIGINAL BEFORE ANTISPAM (active) | `nikel007i33@yandex.ru` |
| CURRENT PRODUCTION (before this task) | `nikel007i33@yandex.ru`, `im.work@mail.ru` |
| DESIRED FINAL | original active + `im.work@mail.ru` |

| Class | Result |
|-------|--------|
| MISSING_LEGITIMATE | **0** |
| PRESENT_LEGITIMATE | `nikel007i33@yandex.ru` |
| OPERATOR_NEW | `im.work@mail.ru` (required retention) |
| UNEXPECTED | **0** |
| TYPO_WRONG | `im.work@nail.ru` **ABSENT** |

## 7. Production Correction

**No production recipient mutation was required.**

Live production already matched DESIRED FINAL. Scoped verify backup of production config/handlers was taken (`local/sites/iseo-su-production/_form-recipient-restore-01/backups/verify-20260821T053743Z/`). Anti-spam, validation, HMAC, rate limits, honeypot, duplicate protection, markup, JS, and CSS were **not** touched.

## 8. Final Recipient Set

Effective `production_recipients` (order as in config):

1. `nikel007i33@yandex.ru`
2. `im.work@mail.ru`

`test_recipients`: `im.work@mail.ru` only (unused while `test_mode=false`).

## 9. Handler Coverage

| Check | Result |
|-------|--------|
| Root handlers verified | **12/12** |
| Shared `iseo_form_send_mail()` | YES |
| Hardcoded divergent To | NO |
| Lingering test override | NO |
| Typo address | NO |
| Hidden CC/BCC | NO |
| Service delegates | require → root (same authority) |

## 10. Test Mode State

**OFF** (`"test_mode" => false`).

## 11. Production / Source Alignment

`iseo-form-config.php` production SHA-256 ≡ `projects/iseo-su-site-ops/production-source/forms/iseo-form-config.php` (`dea5b3482feb914f…`). Handlers and `iseo-form-security.php` also SHA-matched. Normalized recipient sets identical. No runtime→source tail.

## 12. Mail Sends During Task

**0** — config/source/handler inspection and runtime recipient resolution via config only. No form POSTs. No fake leads.

## 13. Rollback

Not applicable for recipient mutation (none performed). Verify backups retained locally under `_form-recipient-restore-01/` (Git-ignored). Pre-antispam handler backups remain under `_form-antispam-01-tmp/backups/`.

## 14. Final Decision

**COMPLETE — ORIGINAL ISEO-SU FORM RECIPIENTS RESTORED / OPERATOR MAILBOX RETAINED / ROUTING NORMALIZED**

Independent reconstruction **confirms** the previous Acceptance 02 restoration claim for the **active** original recipient set. The correction is that recipient truth is now evidenced by this file (backup provenance + live SFTP verify), not by REPORT narrative alone. Commented historical alternate `chrra@yandex.ru` remains correctly excluded from active routing.
