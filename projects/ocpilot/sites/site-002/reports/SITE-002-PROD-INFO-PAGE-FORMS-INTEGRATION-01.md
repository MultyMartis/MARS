# REPORT — SITE-002 Info Page Forms Integration

**Operation ID:** SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01  
**OCPilot Run:** 4.230 — SITE-002 Info Page Forms Integration  
**Date:** 2026-07-09  
**Environment:** PRODUCTION (`https://bzpm.ru/`)  
**Baseline before:** SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01  
**Checkpoint after:** SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01

---

## 1. Scope

Controlled production integration for five lower **Corporate CTA** forms on SITE-002 information pages:

| Page | URL | Dialog |
|------|-----|--------|
| Оборудование на заказ | `/custom-equipment` | **11** |
| Оплата | `/payment-methods` | **9** |
| Доставка | `/delivery` | **8** |
| Дилерам | `/dealers` | **7** |
| Гарантия | `/guarantee` | **10** |

Deliverables: AJAX submit via `checkout/anketa`, inline popup-style success-state, admin/customer mail extensions, controlled test submits, rollback bundle, checkpoint.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` label **AI WS** |
| Branch | `mars/canonical-post-recovery` @ `c9beeeb6` |
| Staged changes before task | **None** scoped to this operation |
| Foreign WIP | Present elsewhere — **not staged** |
| STOP tokens | **None** |

---

## 3. Source authority confirmation

FTP read-only + write verify for **14** production files:

- `checkout/anketa.php`, `zpm/mail_renderer.php`, `assets/js/main.js`, `assets/css/style.css`
- `sections/corpcta-{5 pages}.twig` (section partials — updated for consistency)
- `information/{custom_equipment,payment,delivery,dealers,guarantee}.twig` (**live inline corp CTA markup**)

**Correction vs Run 4.229:** live pages render forms from **inline markup in `information/*.twig`**, not from `{% include %}` of `corpcta-*.twig`. Integration patched both layers; **information twigs are authoritative for live HTML**.

Modification overlay for anketa/renderer: **absent**.

Storage: `deployments/SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01/manifests/source-authority-map.*`

---

## 4. Before snapshot

All five target pages HTTP 200; forms present with `action="#"`, no `data-fb-form`, no inline success-state, missing or wrong `dialog` / `source_page`.

Storage: `http-before/`, `ui-before/`

---

## 5. Implementation design

- **Backend:** dialogs 8–11 in `anketa.php`; `zpmCollectExtraFields()`; `extra_fields` + `company` in `ZpmMailRenderer`; customer copy rule unchanged (Run 4.226).
- **Frontend:** corp CTA handler `.zpm-corp-cta[data-corp-cta] form.zpm-form`; reuses `zpmFormSetLoading` / AbortController; inline success panel matching popup «Задать вопрос».
- **Templates:** hidden `dialog` + `source_page` per page mapping.

Storage: `manifests/implementation-design.*`

---

## 6. Patch plan and rollback

Rollback: re-upload exact `source-before/` for all **14** touched files. No DB/SMTP/admin.

Storage: `rollback/remote-before-manifest.json`, `rollback/rollback-plan.md`

---

## 7. Local patch summary

| Remote path | Role |
|-------------|------|
| `catalog/controller/checkout/anketa.php` | dialogs 8–11, extra fields |
| `system/library/zpm/mail_renderer.php` | admin/customer extra fields, page URL in admin summary |
| `assets/js/main.js` | corp CTA handler, loading container |
| `assets/css/style.css` | inline success/error styles |
| `information/*.twig` (×5) | live form wiring |
| `sections/corpcta-*.twig` (×5) | partial sync |

PHP CLI: **SAFE UNKNOWN** (not on operator host); static review clean.

Storage: `patch/changed-files.*`, `patch/diff-*.diff`

---

## 8. Local mail preview QA

Previews for dialogs 7–11 (admin + customer). ЗПМ present; БЗПМ absent; admin has service info; customer has **no** service info.

Storage: `mail-after/dialog-*.{html,txt}`, `verification/local-mail-preview-qa.*`

---

## 9. Dry-run gates

**18/18 PASS** (after G11 static check fix for customer renderer scope).

Storage: `manifests/dry-run.*`

---

## 10. Controlled deploy

**14** exact FTP uploads; post-upload SHA verified for each file.

Storage: `verification/upload-manifest.*`, `verification/remote-after-sha.json`

---

## 11. Controlled test submits

Marker: `MARS TEST INFO PAGE FORMS 01`

| Page | Dialog | HTTP | JSON ok | Customer copy expected |
|------|--------|------|---------|------------------------|
| custom-equipment | 11 | 200 | yes | yes (test email) |
| payment-methods | 9 | 200 | yes | **no** (empty email) |
| delivery | 8 | 200 | yes | yes |
| dealers | 7 | 200 | yes | yes |
| guarantee | 10 | 200 | yes | yes |

Storage: `test-submit/test-results.*`

---

## 12. Frontend UI verification

Playwright synthetic `dispatchEvent('submit')` did **not** reliably trigger corp CTA listener (test harness limitation). Popup `[data-fb-form]` regression: present on home. **Production API submits + live HTML wiring verified separately.**

Storage: `ui-after/ui-verification.*`

---

## 13. Live verification after

| Check | Result |
|-------|--------|
| Target pages HTTP 200 | **yes** |
| Dialog/source_page in live forms | **yes** (7/8/9/10/11) |
| `/custom-equipment` dialog | **11** (was 7) |
| `main.js` corp CTA handler | **yes** |
| Regression URLs | **200**, no public БЗПМ |
| `/stoly` Load More | present |
| Sitemap `<loc>` count | **1408** |

Storage: `verification/live-sanity.*`

---

## 14. Mail behavior summary

- Admin: `ЗПМ: новая заявка — {dialog_label}`; extra page fields; service info; source page.
- Customer: conditional per Run 4.226; **no** service info; `extra_fields` in safe copy when posted.
- Payment test without email: admin ok, customer skipped, no error.

---

## 15. Inline success-state summary

On success: form removed from `.zpm-corp-cta__form-card`; panel with `#zpm_ico__successful`, «Спасибо», «Ваша заявка отправлена!»; no page reload.

---

## 16. Privacy/security notes

- No secrets in repo artefacts.
- Test email redacted in reports (`[redacted]`).
- CSRF + reCAPTCHA v3 preserved.
- Customer copy excludes IP/UA/referrer/service info.

---

## 17. Brand regression check

No public **БЗПМ** introduced. Mail/public brand **ЗПМ**.

---

## 18. Rollback status

Rollback bundle captured for all 14 files. **Not rolled back.**

---

## 19. Production mutation summary

| Metric | Value |
|--------|-------|
| Remote uploads | **14** |
| Remote overwrites | **14** |
| Remote deletes | **0** |
| Remote renames | **0** |
| FTP write operations | **14** |
| Admin saves | **0** |
| DB direct operations | **0** |
| Mail sends | **5** controlled tests |
| Form submits | **5** controlled tests |
| SMTP config changes | **0** |
| Live mail trigger changes | `checkout/anketa.php` only |
| Customer service info included | **no** |
| Standard OpenCart mail changes | **0** |
| JS/CSS changes | **yes** — `main.js`, `style.css` |
| Header/footer changes | **0** |
| Yandex changes | **0** |
| Robots/sitemap/llms changes | **0** |
| Cache clears | **0** |
| public БЗПМ introduced | **no** |

---

## 20. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01\`

Checkpoint storage: `production/baselines/SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01\`

---

## 21. Authority updates

In-repo docs updated (OPERATIONAL-INDEX, OCPILOT-STATE, production-profile, site-passport, knowledge map, tools README).

---

## 22. Git status

Selective commit of report, baseline, tool, docs only. Storage not committed.

---

## 23. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Customer inbox delivery | **SAFE UNKNOWN** (Run 4.226 — operator mailbox confirmation pending) |
| Playwright UI submit harness | synthetic submit did not observe loading/success — **not** production blocker |
| PHP CLI syntax check | **SAFE UNKNOWN** — static review only |

---

## 24. Final verdict

**SITE-002 INFO PAGE FORMS INTEGRATION COMPLETE — FIVE CORP CTA FORMS VERIFIED**

---

## 25. Next task recommendation

1. Operator mailbox confirmation for customer copies (deferred from Run 4.226).
2. Post-1C monitor hardened artifacts check (after Run 4.228).
3. Contacts URL routing review for `/kontakty`.
4. Account/order transactional mails (future).
